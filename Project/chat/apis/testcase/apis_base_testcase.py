import os, sys
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from configs.app.setting import Setting
from Project.chat.configs.setting import SettingChat
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
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        user = gl.get_value('USER')

        testdata = SettingChat().get_account(env, brand, user)
    # 登入帳號
        self.web_url = testdata['web_url']
        self.app_url = testdata['app_url']
        self.web_account = testdata['web_account']
        self.app_account = testdata['app_account']
        self.password = testdata['password']
        self.web_phone = testdata['web_phone']
        self.app_phone = testdata['app_phone']
        self.nation = testdata['nation']
        self.device_id = Setting().get_phone_device_id()

        if not sys.argv[0].__contains__('prod'):
            self.admin_url = testdata['admin_url']
            self.admin_account = testdata['admin_id']
            self.admin_password = testdata['admin_pwd']
            self.admin_otp = testdata['admin_otp']














