import os, sys, unittest
import logging, wda

# 讓 unittest 把本檔案視為框架內部，避免 _callTestMethod override
# 造成失敗 traceback 被截短到只剩 base_testcase.py 一行。
__unittest = True
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
from driver.app_driver import (
    AppDriver,
    is_ios_wda_connection_lost,
    is_android_pocoservice_dead,
    restart_android_pocoservice,
)
from configs.app.setting import Setting
from Project.chat.configs.setting import SettingChat
from jira.module.base_module import UnittestModule

# 設置 Airtest 的 logging 級別，隱藏 WARNING 訊息
logging.getLogger('airtest.core.api').setLevel(logging.ERROR)
logging.getLogger('airtest').setLevel(logging.ERROR)
# 隱藏 urllib3 連線重試的 WARNING（session 斷線時 accept_alert / window_handles 會觸發）
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
logging.getLogger('urllib3').setLevel(logging.ERROR)

class BaseTestCase(UnittestModule):
    # TEST SETTING
    env = ''
    brand = ''
    user = ''
    phone_name = ''
    phone_platform = ''
    connect_type = ''
    app_version = ''
    specific_os_version = ''
    connection = ''
    function_dict = {}
    _login_status = [False]
    unknown_env = [False]
    duration = ''

    # ACCOUNT SETTING
    package = ''
    poco_package = ''
    web_url = ''
    app_url = ''
    app_account = ''
    web_account = ''
    mail_account = ''
    app_password = ''
    web_password = ''
    mail_password = ''
    app_phone = ''
    web_phone = ''
    mail_address = ''
    app_nation = ''
    web_nation = ''
    operate_account = ''
    operate_phone = ''
    device_id = ''

    admin_url = ''
    admin_account = ''
    admin_password = ''
    admin_otp = ''

    @property
    def ap(self):
        """App Pages 快捷方式"""
        return self.function_dict.get('ap')

    def login_app(self):
        """統一的 App 登入方法"""
        if 'email' in self.account_type.lower():
            self.ap.main_page().login(self.mail_address, self.mail_password, login_method='email')
        elif 'phone' in self.account_type.lower():
            self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)

    def navigate_to_security_page(self):
        """導航到安全設定頁面"""
        self.ap.main_page().into_main_page()
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_security()

    def navigate_to_notification_page(self):
        """導航到通知設定頁面"""
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_notification()

    def navigate_to_about_page(self):
        """導航到關於頁面"""
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_about()

    @classmethod
    def setting_test_data(cls):
        cls.env = gl.get_value('ENV')
        cls.brand = gl.get_value('BRAND')
        cls.user = gl.get_value('USER')
        cls.phone_name = gl.get_value('PHONE_NAME')
        cls.phone_platform = gl.get_value('PHONE_PLATFORM')
        cls.connect_type = gl.get_value('CONNECT_TYPE')
        cls.app_version = gl.get_value('APP_VERSION')
        cls.account_type = gl.get_value('ACCOUNT_TYPE')
        cls.specific_os_version = gl.get_value('SPECIFIC_OS_VERSION')
        cls.duration = gl.get_value('Duration')

        cls.package = Setting().get_package_name(cls.brand, cls.env)
        cls.poco_package = Setting().get_poco_name()
        cls.web_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_url']
        cls.app_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_url']
        cls.wap_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_url']

        cls.app_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_account']
        cls.web_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_account']
        cls.wap_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_account']
        cls.mail_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['mail_account']

        cls.app_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.web_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.wap_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.mail_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']

        cls.app_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_phone']
        cls.web_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_phone']
        cls.wap_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_phone']
        cls.mail_address = SettingChat().get_account(cls.env, cls.brand, cls.user)['mail_address']

        cls.app_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']
        cls.web_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']
        cls.wap_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']

        cls.operate_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['operate_account']
        cls.operate_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['operate_phone']
        cls.device_id = Setting().get_phone_device_id(cls.phone_name, True)

        if not cls.env.__contains__('prod'):
            cls.admin_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_url']
            cls.admin_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_id']
            cls.admin_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_pwd']
            cls.admin_otp = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_otp']

        cls.phone_name = gl.get_value('PHONE_NAME')
        if cls.phone_name != 'None' and cls.phone_name != None:
            cls.phone_name = Setting().correct_phone_name(cls.phone_name)
            gl.set_value('PHONE_NAME', cls.phone_name)

        if cls.connect_type == 'remote':
            app_dr = AppDriver()
            app_dr.stf_connect_phone()

    def device_reconnect(self):
        """手機 / WDA 斷線時重建 session（與 AppTestCase、ContextTestCase 原邏輯一致）。"""
        original_phone_name = gl.get_value('PHONE_NAME')
        # remote 模式沿用既有邏輯，允許重新挑機；local 模式保留原設備避免找不到配置
        if self.connect_type == 'remote':
            gl.set_value('PHONE_NAME', 'None')
        else:
            gl.set_value('PHONE_NAME', original_phone_name)
        self._login_status[0] = False
        self.unknown_env[0] = False

        last_exc = None
        for attempt in range(1, 4):
            try:
                try:
                    self.tearDownClass()
                except Exception:
                    pass

                # iOS 先主動拉起 WDA，降低 setUpClass 直接卡在 8100 的機率
                if str(self.phone_platform).lower() == 'ios':
                    if not gl.get_value('PHONE_NAME') and original_phone_name:
                        gl.set_value('PHONE_NAME', original_phone_name)
                    from common.utils.utils import Utils
                    Utils.start_wda_for_ios()
                elif str(self.phone_platform).lower() == 'android':
                    # Android: 重連前先 force-stop pocoservice, 讓 setUpClass 重新拉起 instrument
                    from driver.app_driver import _get_android_udid_for_current_phone
                    restart_android_pocoservice(udid=_get_android_udid_for_current_phone())

                wait_seconds = 10 if attempt == 1 else 20
                print(f"⏳ device_reconnect 第 {attempt}/3 次，等待 {wait_seconds}s 後重建連線...")
                sleep(wait_seconds)
                self.setUpClass()
                self.setUp()
                print("✅ device_reconnect 重連成功")
                return
            except Exception as e:
                last_exc = e
                print(f"⚠️  device_reconnect 第 {attempt}/3 次失敗: {e}")
                # 若屬 WDA 斷線，下一輪再重啟並重試；否則也交由下一輪嘗試一次
                continue

        if last_exc:
            raise last_exc

    def _callTestMethod(self, method):
        """iOS/Android：裝置連線異常時重連並重跑該測試方法一次。"""
        platform = str(self.phone_platform or '').lower()
        if platform not in ('ios', 'android'):
            super()._callTestMethod(method)
            return

        reconnect_flag_attr = '_device_reconnect_done_for_test'
        setattr(self, reconnect_flag_attr, False)
        try:
            super()._callTestMethod(method)
        except Exception as e:
            if getattr(self, reconnect_flag_attr, False):
                raise
            is_connection_lost = (
                is_ios_wda_connection_lost(e) if platform == 'ios'
                else is_android_pocoservice_dead(e)
            )
            if not is_connection_lost:
                raise
            setattr(self, reconnect_flag_attr, True)
            label = 'WDA' if platform == 'ios' else 'pocoservice'
            print(f'⚠️  {label} 連線異常，嘗試 device_reconnect 後重跑該測試一次...')
            self.device_reconnect()
            super()._callTestMethod(method)
