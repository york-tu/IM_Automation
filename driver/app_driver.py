import os, sys, unittest
import logging, wda
import time
import common.utils.globalvar as gl
import stf_api.stf as stf
import stf_api.stf_utils as stf_utils

from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from common.utils.path_utils import PathUtils
from configs.app.setting import Setting as Setting_Phone
from jira.module.base_module import UnittestModule

# 使用 PathUtils 獲取專案根目錄
path_utils = PathUtils()
root_path = str(path_utils.get_project_root())
sys.path.append(root_path)


def is_ios_wda_connection_lost(exc):
    """
    判斷是否為 iOS WDA / usbmux / HTTP 連線中斷。
    含：8100 未就緒、MuxConnectError、WDA 回應 RemoteDisconnected 等。
    """
    if exc is None:
        return False
    msg = str(exc).lower()
    name = type(exc).__name__.lower()
    if any(
        x in msg
        for x in (
            'port:8100',
            'muxconnecterror',
            'usbmux',
            'remotedisconnected',
            'remote end closed',
            'connection aborted',
            'connection reset',
            'connection refused',
            'broken pipe',
            'protocolerror',
        )
    ):
        return True
    if any(
        x in name
        for x in (
            'remotedisconnected',
            'connectionerror',
            'protocolerror',
        )
    ):
        return True
    return False


def is_android_pocoservice_dead(exc):
    """
    判斷是否為 Android pocoservice 斷線/死掉的徵兆。
    常見:
      - `still waiting for uiautomation ready` 印好幾秒/分鐘
      - urllib3.exceptions.ProtocolError / IncompleteRead
      - requests.exceptions.ChunkedEncodingError / ConnectionError
      - poco internal: PocoTargetTimeout / PocoFatalException
      - adb forward 端口連不上 (Connection refused, port:10080)
    """
    if exc is None:
        return False
    msg = str(exc).lower()
    name = type(exc).__name__.lower()
    if any(
        x in msg
        for x in (
            'still waiting for uiautomation ready',
            'incompleteread',
            'chunkedencodingerror',
            'protocolerror',
            'connection broken',
            'connection refused',
            'connection aborted',
            'connection reset',
            'remote end closed',
            'pocoservice',
            'poco target timeout',
            'port:10080',
            'port:10081',
        )
    ):
        return True
    if any(
        x in name
        for x in (
            'chunkedencodingerror',
            'protocolerror',
            'incompleteread',
            'connectionerror',
            'pocofatalexception',
            'pocotargettimeout',
        )
    ):
        return True
    return False


def _get_android_udid_for_current_phone():
    """從 phone_config 取出當前 PHONE_NAME 對應的 udid (給 adb -s 用)"""
    try:
        conf = Setting_Phone().get_device_conf().get('Phone_conf') or {}
        phone_name = gl.get_value('PHONE_NAME')
        if phone_name and phone_name in conf:
            return conf[phone_name].get('udid')
    except Exception:
        pass
    return None


def restart_android_pocoservice(udid=None, uninstall_on_fail=False):
    """
    強制重啟 Android 手機上的 pocoservice (兩支 apk 都 force-stop)。
    下次 AndroidUiautomationPoco() 初始化時會自動把 instrument 重新拉起來。
    參數:
        udid: 指定設備 udid (給 adb -s 用); None 則用單一連接設備
        uninstall_on_fail: True 時, force-stop 失敗就改成 uninstall, 讓 Poco 下次自動重裝
    """
    import subprocess

    base = ['adb']
    if udid:
        base.extend(['-s', udid])

    pkgs = [
        'com.netease.open.pocoservice',
        'com.netease.open.pocoservice.test',
    ]

    print(f"⚠️  偵測到 Android pocoservice 異常, 嘗試 force-stop 重啟 (udid={udid})...")
    all_ok = True
    for pkg in pkgs:
        cmd = base + ['shell', 'am', 'force-stop', pkg]
        try:
            r = subprocess.run(cmd, timeout=10, capture_output=True, text=True)
            if r.returncode != 0:
                all_ok = False
                print(f"   force-stop {pkg} returncode={r.returncode} stderr={r.stderr.strip()}")
        except Exception as e:
            all_ok = False
            print(f"   force-stop {pkg} 失敗: {e}")

    if not all_ok and uninstall_on_fail:
        print("⚠️  force-stop 失敗, 改用 uninstall 讓 Poco 下次自動重裝...")
        for pkg in pkgs:
            cmd = base + ['uninstall', pkg]
            try:
                subprocess.run(cmd, timeout=15, capture_output=True, text=True)
            except Exception as e:
                print(f"   uninstall {pkg} 失敗: {e}")

    # 給手機一點時間清理進程
    time.sleep(2)
    return all_ok


def safe_snapshot(filename, msg=None, wait_before_sec=1.0):
    """
    tearDown 用截圖: Android 先稍等畫面穩定; minicap/javacap 失敗時只 WARN 不拋錯。
    回傳 True 表示截圖成功, False 表示略過。
    """
    if gl.get_value('PHONE_PLATFORM') == 'Android' and wait_before_sec:
        time.sleep(wait_before_sec)
    try:
        snapshot(filename=filename, msg=msg)
        return True
    except Exception as e:
        err = str(e).lower()
        if any(
            x in err
            for x in (
                'no available screen capture',
                'minicap',
                'screen_proxy',
                'screen capture',
                'bad_value',
                'unable to lock next buffer',
                'unable to consume pending frame',
            )
        ):
            print(f'[WARN] 截圖失敗已略過 ({filename}): {e}')
            return False
        raise


def create_android_poco_with_recovery(max_retries=3, screenshot_each_action=False):
    """
    建立 AndroidUiautomationPoco, 若 pocoservice 未就緒則 force-stop 後重試。
    回傳: AndroidUiautomationPoco 實例
    """
    udid = _get_android_udid_for_current_phone()
    last_exc = None
    restarted = False
    for attempt in range(1, max_retries + 1):
        try:
            poco = AndroidUiautomationPoco(
                use_airtest_input=True,
                screenshot_each_action=screenshot_each_action,
            )
            print(f"✅ Android pocoservice 就緒 (第 {attempt}/{max_retries} 次)")
            return poco
        except Exception as e:
            last_exc = e
            if not restarted and is_android_pocoservice_dead(e):
                restart_android_pocoservice(udid=udid)
                restarted = True
                print(f"⏳ 等待 pocoservice 重啟後重試 ({attempt}/{max_retries})...")
                time.sleep(5)
                continue
            if attempt >= max_retries:
                raise
            print(f"⏳ Android Poco 初始化失敗, {attempt}/{max_retries} 次後重試: {e}")
            time.sleep(3)
    if last_exc:
        raise last_exc
    raise RuntimeError('create_android_poco_with_recovery: 未知失敗')


class AppDriver(UnittestModule):
    # stf控制手機
    # def stf_connect_phone(self):
    #     self.phone_name = gl.get_value('PHONE_NAME')
    #
    #     if self.phone_name == 'None':
    #         phone_platform, phone_serial, phone_manufacturer, phone_marketName, \
    #             stf_notes, os_version = stf_utils.get_unuse_phone_serial(self.specific_os_version)
    #     else:
    #         phone_platform, phone_serial, phone_manufacturer, phone_marketName, \
    #             stf_notes, os_version = stf_utils.get_specific_phone_serial(self.phone_name)
    #
    #     assert phone_serial != None, '沒有未使用中的手機 or 指定手機目前不可用'
    #
    #     stf.post_use_phone(phone_serial) # 在stf上 把手機狀態改為using
    #     remote_url = stf.post_connect_phone(phone_serial) # 取得手機stf遠端網址
    #
    #     if phone_platform == 'iOS':
    #         remote_url = remote_url[0:-5]
    #
    #     gl.set_value('PHONE_PLATFORM', phone_platform) # 手機OS
    #     gl.set_value('PHONE_SERIAL', phone_serial) # 手機UDID
    #     gl.set_value('PHONE_MANUFACTURER', phone_manufacturer) # 廠牌名稱
    #     gl.set_value('PHONE_MARKETNAME', phone_marketName) # 手機型號
    #     gl.set_value('STF_NOTES', stf_notes) # 手機備註(主要是填手機公司編號)
    #     gl.set_value('OS_VERSION', os_version) # 作業系統版本
    #     gl.set_value('PHONE_REMOTE_IP', remote_url) # 手機遠端控制的URL
    #
    #     # 覆蓋原始local手機資訊
    #     self.phone_name = stf_notes
    #     gl.set_value('PHONE_NAME', stf_notes)
    #
    #     print('\n==========================================')
    #     print(f'serial name: {gl.get_value("PHONE_SERIAL")}')
    #     print(f'manufacturer_name: {gl.get_value("PHONE_MANUFACTURER")}')
    #     print(f'marketName_name: {gl.get_value("PHONE_MARKETNAME")}')
    #     print(f'os_version: {gl.get_value("OS_VERSION")}')
    #     print(f'stf_notes: {gl.get_value("STF_NOTES")}')
    #     print('==========================================\n')

    # 注意func執行順序不可倒，要先執行過setting_test_data()
    def airtest_connect_phone(self, phone_name=None):
        self.phone_name = phone_name or gl.get_value('PHONE_NAME')
        self.connect_type = gl.get_value('CONNECT_TYPE')
        self.poco = None
        self.wda_service = None

        # 取得Airtest格式的手機連線link
        self.connection = Setting_Phone().get_phone_connect_link(self.phone_name, gl.get_value('PHONE_REMOTE_IP'), self.connect_type)

        # Android 預設用 javacap，避免 minicap 在 API 31+ / 華為等機型出現 BAD_VALUE (-22)
        cap_method = ''
        if gl.get_value('PHONE_PLATFORM') == 'Android':
            cap_method = 'javacap'
        elif 'MI' in (gl.get_value('PHONE_NAME') or ''):
            cap_method = 'javacap'
        elif 'POCO' in (gl.get_value('PHONE_NAME') or ''):
            cap_method = 'javacap'

        # 檢查 WDA 是否啟動失敗
        wda_start_failed = gl.get_value('WDA_START_FAILED', False)
        if wda_start_failed and gl.get_value("PHONE_PLATFORM") == 'iOS':
            error_msg = "WDA 啟動失敗，無法連接設備。請檢查 tunnel 是否正確啟動。"
            raise Exception(error_msg)
        
        max_retries = 3
        retry_count = 0
        wda_restarted = False
        while retry_count < max_retries:
            try:
                auto_setup(__file__, logdir=False, devices=[f'{self.connection}?cap_method={cap_method}']) # Airtest 連線手機
                break
            except Exception as e:
                # iOS 遇到 WDA/usbmux/HTTP 連線異常時，嘗試先重啟 WDA 再重試連線
                if (gl.get_value("PHONE_PLATFORM") == 'iOS'
                        and not wda_restarted
                        and is_ios_wda_connection_lost(e)):
                    try:
                        from common.utils.utils import Utils
                        print("⚠️  偵測到 iOS WDA 連線異常，嘗試重啟 WDA 後重連...")
                        Utils.start_wda_for_ios()
                        wda_restarted = True
                    except Exception:
                        # 重啟失敗不阻斷重試流程，交由原有重試次數控制
                        pass
                retry_count += 1
                if retry_count >= max_retries:
                    raise
                logging.exception('exception log')
                time.sleep(2)  # 等待 2 秒後重試

        if gl.get_value("PHONE_PLATFORM") == 'Android':
            # Android 設備：自動喚醒屏幕（如果處於待機狀態）
            try:
                # 方法 1：使用 Airtest 的 wake() 函數（推薦）
                wake()
                time.sleep(0.5)  # 等待屏幕喚醒
                logging.info("✅ Android 設備已喚醒")
            except Exception as e:
                # 方法 2：如果 wake() 失敗，使用 keyevent 喚醒
                try:
                    keyevent("KEYCODE_WAKEUP")  # 或使用 keyevent(26)
                    time.sleep(0.5)
                    logging.info("✅ Android 設備已通過 keyevent 喚醒")
                except Exception as e2:
                    logging.warning(f"⚠️  無法喚醒 Android 設備: {e2}")

            # screenshot_each_action=False: 減少每步截圖; tearDown 的 safe_snapshot 負責 Jira 附圖
            poco = create_android_poco_with_recovery(max_retries=3, screenshot_each_action=False)
            parameter = (poco, '')

        if gl.get_value("PHONE_PLATFORM") == 'iOS':
            if not cli_setup():
                auto_setup(__file__, logdir=False, devices=[self.connection,])
            if not self.poco:
                self.poco = iosPoco()
            if not self.wda_service:
                # 檢查是否有動態設置的端口
                wda_port = gl.get_value('WDA_PORT')
                
                if wda_port:
                    # 如果使用 usbmux，需要構建正確的連接字符串
                    # 格式: http://127.0.0.1:端口 或 http+usbmux://udid
                    if 'usbmux' in self.connection:
                        # usbmux 連接時，端口通過 usbmux 隧道自動轉發
                        # 但我們需要確保 WDA 在正確的端口上運行
                        wda_url = f'http://127.0.0.1:{wda_port}'
                    else:
                        wda_url = self.connection.split('///')[-1]
                else:
                    wda_url = self.connection.split('///')[-1]
                
                # 添加重試邏輯，等待 WDA 準備好
                max_retries = 15  # 最多重試 15 次（30 秒）
                retry_count = 0
                wda_restarted = False
                while retry_count < max_retries:
                    try:
                        self.wda_service = wda.Client(wda_url)
                        # 嘗試連接以確認 WDA 已準備好並獲取 iOS 設備版本信息
                        try:
                            status_info = self.wda_service.status()
                            os_version = status_info.get('os', {}).get('version', '')
                            if os_version:
                                # 格式化版本號，例如 "18.2" -> "iOS18.2"
                                gl.set_value('OS_VERSION', f'iOS{os_version}')
                                print(f"📱 檢測到 iOS 版本: {os_version}")
                        except Exception as e:
                            # 如果獲取失敗，嘗試從配置或已有值獲取
                            existing_version = gl.get_value('OS_VERSION')
                            if not existing_version:
                                print(f"⚠️  無法獲取 iOS 版本: {e}")
                        
                        print(f"✅ WDA 連接成功 (端口: {wda_port or '默認'})")
                        break
                    except Exception as e:
                        # 僅在第一次遇到 WDA/usbmux/HTTP 斷線時重啟，避免無限反覆拉起
                        if not wda_restarted and is_ios_wda_connection_lost(e):
                            try:
                                from common.utils.utils import Utils
                                print("⚠️  WDA 尚未就緒/已斷線，嘗試重啟 WDA...")
                                Utils.start_wda_for_ios()
                                wda_restarted = True
                                time.sleep(3)
                            except Exception:
                                pass
                        retry_count += 1
                        if retry_count >= max_retries:
                            raise Exception(f'無法連接到 WDA (URL: {wda_url})，已重試 {max_retries} 次: {e}')
                        print(f"⏳ 等待 WDA 準備好... ({retry_count}/{max_retries})")
                        time.sleep(2)
            parameter = (self.poco, self.wda_service)
            
        return parameter
