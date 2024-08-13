import os, sys
import common.utils.globalvar as gl
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.lottery.configs.setting import Setting
from jira.module.base_module import UnittestModule

class BaseTestCase(UnittestModule):

    # CHROME SETTING
    wait_time = 20
    implicitly_wait_time = 35
    driver = ''


    def setting_test_data(self):
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        user = gl.get_value('USER')

        testdata = Setting().get_test_data(env, brand, user)
    # 登入帳號
        self.web_url = testdata['web_url']
        self.mobile_url = testdata['mobile_url']
        self.web_account = testdata['web_id']
        self.web_password = testdata['web_pwd']
        self.web_captcha = testdata['web_captcha']
        self.withdraw_password = testdata['withdraw_pwd']
        self.mobile_ui_mode = testdata['mobile_ui_mode']
        self.mynah_admin_url = testdata['mynah_admin_url']
        self.mynah_web_url = testdata['mynah_web_url']
        self.mynah_account = testdata['mynah_id']
        self.mynah_password = testdata['mynah_pwd']

        if not sys.argv[0].__contains__('prod'):
            self.reseller_account = testdata['reseller_id']
            self.reseller_password = testdata['reseller_pwd']
            self.reseller_otp = testdata['reseller_otp']
            self.admin_otp = testdata['admin_otp']
            self.shareholder = testdata['shareholder']
            self.generalagent = testdata['generalagent']
            self.commision_program = testdata['commision_program']
            self.reseller_url = testdata['reseller_url']
            self.admin_url = testdata['admin_url']
            self.admin_account = testdata['admin_id']
            self.admin_password = testdata['admin_pwd']
            self.cmweb_url = testdata['cmweb_url']
            self.cmweb_account = testdata['cmweb_id']
            self.cmweb_password = testdata['cmweb_pwd']
            self.dwhweb_url = testdata['dwhweb_url']
            self.dwhweb_account = testdata['dwhweb_id']
            self.dwhweb_password = testdata['dwhweb_pwd']
            self.port = testdata['port']
            self.host_ip = testdata['host_ip']
            self.fileserver_url = testdata['fileserver_url']