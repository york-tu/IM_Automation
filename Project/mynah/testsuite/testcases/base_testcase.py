import os, sys, glob, platform, shutil
import common.utils.globalvar as gl
from selenium import webdriver
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
# from Project.lottery.configs.setting import Setting
from configs.web.setting_chrome import Setting_Chrome
from Project.mynah.configs.setting import Setting
from jira.module.base_module import UnittestModule

class BaseTestCase(UnittestModule):

    # CHROME SETTING
    wait_time = 20
    implicitly_wait_time = 35
    driver = ''

    def setting_test_data(self):
        env = gl.get_value('ENV')
        platform = gl.get_value('PLATFORM')
        user = gl.get_value('USER') 

        testdata = Setting().get_test_data(env, platform, user)

        self.web_url1 = testdata['web_url1']
        self.web_url2 = testdata['web_url2']
        self.site_name1 = testdata['site_name1']
        self.site_name2 = testdata['site_name2']
        self.admin_url = testdata['admin_url']
        self.cs_account1 = testdata['cs_account1']
        self.cs_password1 = testdata['cs_password1']
        self.cs_account2 = testdata['cs_account2']
        self.cs_password2 = testdata['cs_password2']
        self.bs_account = testdata['bs_account']
        self.bs_password = testdata['bs_password']
        self.channel_url = testdata['channel_url']
        self.web_account = testdata['web_account']
        self.web_password = testdata['web_password']
        