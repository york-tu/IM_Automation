# -*- coding: utf-8 -*-
import hashlib, sys, os, requests, time, random, re
from tokenize import group
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.chat.apis.testcase.apis_base_testcase import BaseTestCase
from Project.chat.apis.function_layer.functions import Functions
from Project.chat.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
import common.utils.globalvar as gl
from common.web.decorator import DecorateClass



class UiApiAppTestCases(BaseTestCase, BaseFunction_API):

    brand = gl.get_value('BRAND')
    # ================================= TestSetting ================================
    @classmethod
    def setUpClass(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        cls.functions = Functions(cls.skipTest)
        cls.env = gl.get_value('ENV')
    
    def tearDown(self):
        self.check_result(str(self.id()).split('.')[-1])
    
    @classmethod
    def tearDownClass(cls):
        pass

    # ================================= Web_TestCases ==============================
    # 登入
    @DecorateClass('')
    def test_app_login(self):
        fullnumber = self.get_full_phone_number(self.nation, self.app_phone)
        return self.do_app_login(self.nation, fullnumber, self.password, self.device_id, self.app_url)

    @DecorateClass('')
    def test_web_login(self):
        fullnumber = self.get_full_phone_number(self.nation, self.web_phone)
        return self.do_web_login(self.nation, fullnumber, self.password, self.device_id, self.web_url)

    @DecorateClass('')
    def test_admin_login(self):
        return self.do_admin_login(self.admin_account, self.admin_password, self.admin_url)

    @DecorateClass('')
    def test_send_message(self):
        res, token = self.test_app_login()
        headers = self.headers(token)
        groups_name = 'QA_chat_bot'
        messages = 50
        space = 0.1
        
        groups_id = self.functions.ui_caht_function().get_groups_id(groups_name, headers, self.app_url)
        self.functions.ui_caht_function().do_send_messages(groups_id, messages, space, headers, self.app_url, sync=True)

    def test_send_red_envelopet(self):
        res, token = self.test_admin_login()
        headers = self.header(token)
        

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
