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
    app_password = ''
    web_password = ''
    app_phone = ''
    web_phone = ''
    app_nation = ''
    web_nation = ''
    operate_account = ''
    operate_phone = ''
    device_id = ''

    admin_url = ''
    admin_account = ''
    admin_password = ''
    admin_otp = ''

    @classmethod
    def setting_test_data(cls):
        cls.env = gl.get_value('ENV')
        cls.brand = gl.get_value('BRAND')
        cls.user = gl.get_value('USER')
        cls.phone_name = gl.get_value('PHONE_NAME')
        cls.phone_platform = gl.get_value('PHONE_PLATFORM')
        cls.connect_type = gl.get_value('CONNECT_TYPE')
        cls.app_version = gl.get_value('APP_VERSION')
        cls.specific_os_version = gl.get_value('SPECIFIC_OS_VERSION')
        cls.duration = gl.get_value('Duration')

        cls.package = Setting().get_package_name(cls.brand, cls.env)
        cls.poco_package = Setting().get_poco_name()
        cls.web_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_url']
        cls.app_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_url']
        cls.app_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_account']
        cls.web_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_account']
        cls.app_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.web_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.app_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_phone']
        cls.web_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_phone']
        cls.app_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']
        cls.web_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']
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
