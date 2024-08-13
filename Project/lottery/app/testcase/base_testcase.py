import os, sys, unittest
import logging, wda
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
import driver.app_driver as app_dr
from configs.app.setting import Setting as Setting_Phone
from Project.lottery.configs.setting import Setting
from jira.module.base_module import UnittestModule

class BaseTestCase(UnittestModule):
    # TEST SETTING
    env = ''
    brand = ''
    user = ''
    phone_name = ''
    connect_type = ''
    connection = ''
    app_version = ''
    function_dict = {}
    _login_status = [False]
    unknow_env = [False]
    # first_testcase = [True]
    wallet = ['AG', 'BBIN', 'BG', 'BSP', 'CQ9', 'DG', 'FG', 'GC', 'GM', 'HG', 'KK', 'KY', 'KX', 'LGD', 'MG', 'PT', 'SB', 'SP365', '3S', 'SW', 'VG']

    def setting_test_data(self):
        self.env = gl.get_value('ENV')
        self.brand = gl.get_value('BRAND') 
        self.user = gl.get_value('USER')
        self.phone_platform = gl.get_value('PHONE_PLATFORM')
        self.connect_type = gl.get_value('CONNECT_TYPE')
        self.app_version = gl.get_value('APP_VERSION')
        self.specific_os_version = gl.get_value('SPECIFIC_OS_VERSION')

        self.package = Setting_Phone().get_package_name(self.brand, self.env)
        self.poco_package = Setting_Phone().get_poco_name()
        self.mobile_ui = Setting().get_test_data(self.env, self.brand, self.user)['mobile_ui_mode']
        self.app_account = Setting().get_test_data(self.env, self.brand, self.user)['web_id']
        self.app_password = Setting().get_test_data(self.env, self.brand, self.user)['web_pwd']
        self.admin_url = Setting().get_test_data(self.env, self.brand, self.user)['admin_url']
        self.admin_account = Setting().get_test_data(self.env, self.brand, self.user)['admin_id']
        self.admin_password = Setting().get_test_data(self.env, self.brand, self.user)['admin_pwd']
        self.admin_otp = Setting().get_test_data(self.env, self.brand, self.user)['admin_otp']

        self.phone_name = gl.get_value('PHONE_NAME')
        if self.phone_name != 'None' and self.phone_name != None:
            self.phone_name = Setting_Phone().correct_phone_name(self.phone_name)
            gl.set_value('PHONE_NAME', self.phone_name)

        if self.connect_type == 'remote':
            app_dr.AppDriver.stf_connect_phone(self)
