import os, sys, glob, platform, shutil
from selenium import webdriver
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from Project.sbk.configs.setting import SettingSbk
import common.utils.globalvar as gl
from jira.module.base_module import UnittestModule

class BaseTestCase(UnittestModule):
    # CHROME SETTING
    wait_time = 20
    implicitly_wait_time = 35
    driver = ''
    withdraw = '500'

    # TEST SETTING
    env = ''
    brand = ''
    user = ''

    def setting_test_data(self):
        self.env = gl.get_value('ENV')
        self.brand = gl.get_value('BRAND')
        self.user = gl.get_value('USER')

    # 登入帳號
        self.web_url = SettingSbk().get_account(self.env, self.brand, self.user)['web_url']
        self.web_account = SettingSbk().get_account(self.env, self.brand, self.user)['web_account']
        self.web_password = SettingSbk().get_account(self.env, self.brand, self.user)['password']
        # self.web_phone = SettingSbk().get_account(self.env, self.brand, self.user)['web_phone']
        # self.web_nation = SettingSbk().get_account(self.env, self.brand, self.user)['nation']
        
        
        if not self.env.__contains__('prod'):
            self.admin_url = SettingSbk().get_account(self.env, self.brand, self.user)['admin_url']
            self.admin_account = SettingSbk().get_account(self.env, self.brand, self.user)['admin_id']
            self.admin_password = SettingSbk().get_account(self.env, self.brand, self.user)['admin_pwd']
            self.admin_otp = SettingSbk().get_account(self.env, self.brand, self.user)['admin_otp']
