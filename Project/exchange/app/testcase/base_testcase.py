import os, sys, glob, platform, shutil, unittest, logging, wda
from selenium import webdriver
from configs.app.setting import Setting
import common.utils.globalvar as gl
import driver.app_driver as app_dr
from Project.exchange.configs.setting import Setting as Exchange
from configs.web.setting_chrome import Setting_Chrome
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import stf_api.stf as stf
import stf_api.stf_utils as stf_utils
from configs.app.setting import Setting as Setting_Phone
from jira.module.base_module import UnittestModule

class BaseTestCase(UnittestModule):
    # PHONE TEST SETTING
    env = ''
    brand = ''
    user = ''
    phone_name = ''
    connect_type = ''
    connection = ''
    app_version = ''
    function_dict = {}
    _login_status = [False]
    # wallet = ['AG', 'MG', 'SB', 'BBIN', '3S', 'DT', 'GC', 'KY', 'KK', 'VG', 'SW', 'PT', 'KX', 'HG', 'GM', 'FG', 'DG', 'CQ9', 'BSP']

    def setting_test_data(self):
        self.env = gl.get_value('ENV')
        self.brand = gl.get_value('BRAND')
        self.channel_brand = gl.get_value('CHANNEL_BRAND')
        self.user = gl.get_value('USER')
        self.phone_name = gl.get_value('PHONE_NAME')
        self.phone_platform = gl.get_value('PHONE_PLATFORM')
        self.connect_type = gl.get_value('CONNECT_TYPE')
        self.app_version = gl.get_value('APP_VERSION')
        self.specific_os_version = gl.get_value('SPECIFIC_OS_VERSION')

        testdata = Exchange().get_test_data(self.env, self.channel_brand, self.user)

        # web登入帳號
        self.web_url = testdata['web_url']
        self.web_account = testdata['web_id']
        self.web_password = testdata['web_pwd']
        self.web_captcha = testdata['web_captcha']
        self.withdraw_password = testdata['withdraw_pwd']
        self.web_account = testdata['web_id']
        self.web_password = testdata['web_pwd']
        self.admin_url = testdata['admin_url']
        self.admin_account = testdata['admin_id']
        self.admin_password = testdata['admin_pwd']
        self.admin_otp = testdata['admin_otp']
        #app setting
        testdata = Exchange().get_test_data_exchange(self.env, self.brand, self.user)
        
        self.package = Setting().get_package_name(self.brand, self.env)
        self.admin_url_zqb = testdata['admin_url']
        self.paybox_url = testdata['paybox_url']
        self.paybox_id = testdata['paybox_id']
        self.paybox_pwd = testdata['paybox_pwd']
        self.admin_id_zqb = testdata['admin_id']
        self.admin_pwd_zqb = testdata['admin_pwd']
        self.app_account = testdata['app_id']
        self.app_password = testdata['app_pwd']
        self.app_number = testdata['app_number']

        if self.connect_type == 'remote':
            app_dr.AppDriver.stf_connect_phone(self)
        