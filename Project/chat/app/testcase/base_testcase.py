import os, sys, unittest
import logging, wda
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
from driver.app_driver import AppDriver
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
