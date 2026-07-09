import json
import os, sys, unittest, platform, subprocess, tempfile
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


def resolve_ios_wda_client_url():
    """組出 wda.Client 使用的 URL（優先回傳上次探活成功的 URL）。"""
    cached = gl.get_value('WDA_ACTIVE_URL')
    if cached:
        return cached
    urls = resolve_ios_wda_client_urls()
    return urls[0] if urls else 'http://127.0.0.1:8100'


def resolve_ios_wda_client_urls():
    """列出可嘗試的 WDA URL（usbmux / localhost / 設定檔 port）。"""
    urls = []
    seen = set()

    def _add(url):
        if url and url not in seen:
            seen.add(url)
            urls.append(url)

    wda_port = gl.get_value('WDA_PORT')
    phone_name = gl.get_value('PHONE_NAME')
    connect_type = gl.get_value('CONNECT_TYPE')
    connection = Setting_Phone().get_phone_connect_link(
        phone_name, gl.get_value('PHONE_REMOTE_IP'), connect_type,
    )
    try:
        conf = Setting_Phone().get_device_conf().get('Phone_conf', {})
        device = conf.get(phone_name, {}) if phone_name else {}
    except Exception:
        device = {}
    port = wda_port or device.get('port', 8100)
    udid = device.get('udid')

    if udid:
        _add(f'http+usbmux://{udid}')
    _add(f'http://127.0.0.1:{port}')
    _add(connection.split('///')[-1])
    cached = gl.get_value('WDA_ACTIVE_URL')
    if cached:
        urls.insert(0, cached)
        # 去重保留順序
        deduped = []
        seen.clear()
        for u in urls:
            if u not in seen:
                seen.add(u)
                deduped.append(u)
        return deduped
    return urls


def wait_for_ios_wda_ready(timeout=90, interval=2, wda_process=None):
    """輪詢 WDA /status（多 URL），直到就緒或逾時。回傳 bool。"""
    if gl.get_value('PHONE_PLATFORM') != 'iOS':
        return True
    urls = resolve_ios_wda_client_urls()
    deadline = time.time() + timeout
    attempt = 0
    last_err = None
    while time.time() < deadline:
        attempt += 1
        if wda_process is not None and wda_process.poll() is not None:
            print(f'❌ go-ios runwda 已結束 (exit={wda_process.returncode})')
            print_go_ios_failure_logs()
            gl.set_value('WDA_START_FAILED', True)
            return False

        for url in urls:
            try:
                client = wda.Client(url)
                client.status()
                print(f'✅ WDA 已就緒 (URL: {url}, 第 {attempt} 次探活)')
                gl.set_value('WDA_ACTIVE_URL', url)
                gl.set_value('WDA_START_FAILED', False)
                return True
            except Exception as e:
                last_err = e

        if attempt == 1 or attempt % 5 == 0:
            print(f'⏳ 等待 WDA 就緒... ({attempt} 次) {last_err}')
        time.sleep(interval)

    print(f'❌ WDA 在 {timeout}s 內未就緒 (嘗試 URL: {urls}): {last_err}')
    print_go_ios_failure_logs()
    gl.set_value('WDA_START_FAILED', True)
    return False


def _read_log_tail(path, max_lines=40):
    if not path or not os.path.isfile(path):
        return ''
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        return ''.join(lines[-max_lines:]).strip()
    except Exception:
        return ''


def print_go_ios_failure_logs():
    """印出 tunnel / runwda 相關 log 尾端，方便排查 go-ios 失敗。"""
    for label, key in (
        ('runwda', 'WDA_RUN_LOG_PATH'),
        ('tunnel', 'IOS_TUNNEL_LOG_PATH'),
    ):
        path = gl.get_value(key)
        tail = _read_log_tail(path)
        if tail:
            print(f'--- {label} log ({path}) ---')
            print(tail)
            print(f'--- end {label} log ---')
        err_tail = _read_log_tail(f'{path}.err') if path else ''
        if err_tail:
            print(f'--- {label} stderr ({path}.err) ---')
            print(err_tail)
            print(f'--- end {label} stderr ---')


def go_ios_env():
    env = os.environ.copy()
    env.setdefault('IOS_DEVICE_TUNNEL_FORCE_IPV4', '1')
    env.setdefault('ENABLE_GO_IOS_AGENT', 'user')
    return env


def _go_ios_popen_kwargs(go_ios_dir, env):
    kwargs = {'cwd': str(go_ios_dir), 'env': env}
    if platform.system() == 'Windows':
        kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
    return kwargs


def _parse_json_array_from_output(text):
    if not text:
        return []
    start = text.find('[')
    if start == -1:
        return []
    try:
        return json.loads(text[start:])
    except Exception:
        return []


def ios_tunnel_list(ios_exe, go_ios_dir, env):
    try:
        r = subprocess.run(
            [str(ios_exe), 'tunnel', 'ls'],
            capture_output=True, text=True, timeout=25,
            cwd=str(go_ios_dir), env=env,
        )
        combined = (r.stdout or '') + '\n' + (r.stderr or '')
        return _parse_json_array_from_output(combined)
    except Exception as e:
        print(f'⚠️  ios tunnel ls 失敗: {e}')
        return []


def ios_tunnel_ready(ios_exe, udid, go_ios_dir, env):
    return any(t.get('udid') == udid for t in ios_tunnel_list(ios_exe, go_ios_dir, env))


def wait_for_ios_tunnel(ios_exe, udid, go_ios_dir, env, timeout=45, interval=2):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if ios_tunnel_ready(ios_exe, udid, go_ios_dir, env):
            return True
        time.sleep(interval)
    return False


def kill_go_ios_processes():
    print('🔹 終止現有的 ios.exe 進程...')
    try:
        if platform.system() == 'Windows':
            subprocess.run(['taskkill', '/F', '/IM', 'ios.exe'], capture_output=True, check=False)
        else:
            subprocess.run(['pkill', '-f', 'ios.exe'], capture_output=True, check=False)
    except Exception:
        pass
    gl.set_value('IOS_TUNNEL_PROCESS', None)
    gl.set_value('WDA_RUN_PROCESS', None)
    time.sleep(2)


def _is_tcp_port_open(host, port, timeout=1.0):
    import socket
    try:
        with socket.create_connection((host, int(port)), timeout=timeout):
            return True
    except OSError:
        return False


def _tunnel_log_port_conflict(tunnel_log):
    text = _read_log_tail(tunnel_log, max_lines=50)
    if not text:
        return False
    lower = text.lower()
    return '60105' in text and ('bind' in lower or 'only one usage' in lower)


def _wait_port_closed(host, port, timeout=15, interval=0.5):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not _is_tcp_port_open(host, port, timeout=0.5):
            return True
        time.sleep(interval)
    return False


def _start_ios_tunnel_process(ios_exe, udid, go_ios_dir, env):
    """在 60105 已釋放後啟動 tunnel start，並等待 tunnel ls 出現裝置。"""
    print('🔹 啟動 go-ios userspace tunnel...')
    tunnel_log_fd, tunnel_log = tempfile.mkstemp(suffix='.log', prefix='goios_tunnel_')
    os.close(tunnel_log_fd)
    gl.set_value('IOS_TUNNEL_LOG_PATH', tunnel_log)

    tunnel_cmd = [str(ios_exe), 'tunnel', 'start', '--udid', udid, '--userspace']
    tunnel_log_f = open(tunnel_log, 'a', encoding='utf-8')
    tunnel_proc = subprocess.Popen(
        tunnel_cmd,
        stdout=tunnel_log_f,
        stderr=subprocess.STDOUT,
        **_go_ios_popen_kwargs(go_ios_dir, env),
    )
    gl.set_value('IOS_TUNNEL_PROCESS', tunnel_proc)

    if wait_for_ios_tunnel(ios_exe, udid, go_ios_dir, env, timeout=90):
        print('✅ go-ios tunnel 就緒')
        return True

    # tunnel 程序已退出或 bind 60105 → 若 agent 其實已在，再查一次 ls
    if _tunnel_log_port_conflict(tunnel_log) or tunnel_proc.poll() is not None:
        if ios_tunnel_ready(ios_exe, udid, go_ios_dir, env):
            print('✅ go-ios tunnel 就緒 (tunnel ls 確認)')
            return True

    print('❌ go-ios tunnel 啟動逾時')
    print_go_ios_failure_logs()
    return False


def ensure_ios_tunnel(ios_exe, udid, go_ios_dir, env, force_restart=False):
    """確保 go-ios userspace tunnel 就緒。"""
    if force_restart:
        kill_go_ios_processes()
        _wait_port_closed('127.0.0.1', 60105)

    if ios_tunnel_ready(ios_exe, udid, go_ios_dir, env):
        print('✅ go-ios tunnel 已在運行 (tunnel ls)')
        return True

    # 60105 有 agent 但 tunnel ls 為空 = 僵死 agent，必須先殺掉，不可再 tunnel start
    if _is_tcp_port_open('127.0.0.1', 60105):
        if wait_for_ios_tunnel(ios_exe, udid, go_ios_dir, env, timeout=10):
            print('✅ go-ios tunnel 就緒 (重用 agent)')
            return True
        print('⚠️  60105 有 go-ios agent 但 tunnel ls 無裝置，重啟 ios.exe...')
        kill_go_ios_processes()
        if not _wait_port_closed('127.0.0.1', 60105):
            print('❌ 60105 仍被占用，請手動結束 ios.exe 後重試')
            return False

    return _start_ios_tunnel_process(ios_exe, udid, go_ios_dir, env)


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

        # iOS：若上次 WDA 啟動失敗，在連線前再嘗試一次（不要直接 abort）
        if gl.get_value('WDA_START_FAILED') and gl.get_value("PHONE_PLATFORM") == 'iOS':
            print('⚠️  上次 WDA 啟動未成功，連線前重新嘗試 start_wda_for_ios...')
            gl.set_value('WDA_START_FAILED', False)
            from common.utils.utils import Utils
            Utils.start_wda_for_ios()

        if gl.get_value("PHONE_PLATFORM") == 'iOS':
            if not wait_for_ios_wda_ready(timeout=30):
                from common.utils.utils import Utils
                print('⚠️  WDA 尚未就緒，嘗試啟動 go-ios WDA...')
                Utils.start_wda_for_ios()
                if not wait_for_ios_wda_ready(timeout=90):
                    raise Exception(
                        'WDA 啟動後仍無法連線 (port:8100 is not ready)，請檢查裝置、USB 與 go-ios tunnel'
                    )

        max_retries = 5 if gl.get_value("PHONE_PLATFORM") == 'iOS' else 3
        retry_count = 0
        wda_restart_count = 0
        while retry_count < max_retries:
            try:
                auto_setup(__file__, logdir=False, devices=[f'{self.connection}?cap_method={cap_method}']) # Airtest 連線手機
                break
            except Exception as e:
                # iOS 遇到 WDA/usbmux/HTTP 連線異常時，嘗試重啟 WDA 再重試連線
                if (gl.get_value("PHONE_PLATFORM") == 'iOS'
                        and is_ios_wda_connection_lost(e)
                        and wda_restart_count < 2):
                    try:
                        from common.utils.utils import Utils
                        print(f"⚠️  偵測到 iOS WDA 連線異常，嘗試重啟 WDA 後重連... ({wda_restart_count + 1}/2)")
                        Utils.start_wda_for_ios()
                        wda_restart_count += 1
                    except Exception:
                        pass
                retry_count += 1
                if retry_count >= max_retries:
                    raise
                logging.warning('連線重試 %s/%s: %s', retry_count, max_retries, e)
                time.sleep(3 if gl.get_value("PHONE_PLATFORM") == 'iOS' else 2)

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
                wda_url = resolve_ios_wda_client_url()
                
                # 添加重試邏輯，等待 WDA 準備好
                max_retries = 15  # 最多重試 15 次（30 秒）
                retry_count = 0
                wda_restart_count = 0
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
                        
                        print(f"✅ WDA 連接成功 (URL: {wda_url})")
                        break
                    except Exception as e:
                        if (not wda_restart_count
                                and is_ios_wda_connection_lost(e)
                                and retry_count >= 3):
                            try:
                                from common.utils.utils import Utils
                                print("⚠️  WDA 尚未就緒/已斷線，嘗試重啟 WDA...")
                                Utils.start_wda_for_ios()
                                wda_restart_count = 1
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
