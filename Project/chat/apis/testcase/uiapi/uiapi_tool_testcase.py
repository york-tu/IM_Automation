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



class UiApiToolTestCases(BaseTestCase, BaseFunction_API):

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
    def app_login(self, nation, phone, password):
        fullnumber = self.get_full_phone_number(nation, phone)
        return self.do_app_login(nation, fullnumber, password, self.device_id, self.app_url)

    def web_login(self, nation, phone, password):
        fullnumber = self.get_full_phone_number(nation, phone)
        return self.do_web_login(nation, fullnumber, password, self.device_id, self.web_url)

    def test_send_message_to_one(self):
        nation = 'TW'
        phone = 914001801
        
        for _ in range(0,50,1):
            res, token = self.web_login(nation, phone, 'abc123')
            headers = self.headers(token)
            member_id = 'uscahgdvbugvok62eakui0'
            messages = 100
            space =0.2
            groups_id = self.functions.ui_caht_function().get_members_id(member_id, headers, self.app_url)
            self.functions.ui_caht_function().do_send_messages(groups_id, messages, space, headers, self.app_url)

            phone = phone+1

    def test_add_friend(self):
        nation = 'CN'
        app_id = '13542678900'
        phone = str(886914001802)
        res, token = self.web_login(nation, app_id, 'Bu123123')
        headers = self.headers(token)
        
        for _ in range(0,5,1):
            self.functions.ui_friends_function().add_friend(phone, headers, self.web_url)
            phone = str(int(phone)+1)

    def test_add_groups(self):
        nation = 'CN'
        app_id = '13542600000'
        group_name = "Maxtest"
        phone = str(886914004279)
        
        res, token = self.web_login(nation, app_id, 'Heaven4394')
        headers = self.headers(token)
        
        num = 0
        for num in range(413,1000,1):
            name = str(group_name) + "-" + str(num)
            user_ids = []

            for _ in range(0,6,1):
                ids = self.functions.ui_friends_function().user_ids(phone, headers, self.web_url)
                user_ids.append(ids)        
                phone = str(int(phone)+1)
            
            users = ",".join(user_ids)

            groups_id = self.functions.ui_friends_function().add_groups(name, users, headers, self.web_url)
            
            messages = 50
            space =0.2
            headers = self.headers(token)
            self.functions.ui_caht_function().do_send_messages(groups_id, messages, space, headers, self.app_url)
            num = num + 1
            
    def test_add_chatroom(self):
        nation = 'TW'
        phone = 914003101
        room = str(8613543800001)
        num = 0
        
        for num in range(0,500,1):
            res, token = self.web_login(nation, phone, 'abc123')
            headers = self.headers(token)

            user_info =  self.functions.ui_friends_function().search_friend(room, headers, self.web_url)
            self.functions.ui_friends_function().add_friend(user_info, headers, self.web_url)
            user_id = self.functions.ui_friends_function().get_friend_id(user_info, headers, self.web_url)
            group_id = self.functions.ui_friends_function().friend_direct(user_id, headers, self.web_url)


            messages = 10
            space =0.1
            self.functions.ui_caht_function().do_send_messages(group_id, messages, space, headers, self.app_url, sync=True)
            
            phone = phone + 1
            num = num + 1

    def test_get_redenvelope(self):
        nation = 'CN'
        phone = 13542678901
        red_id = 1638801964617347072

        res, token = self.web_login(nation, phone, 'Bu123123')
        headers = self.headers(token)
        
        for _ in range(0,40,1):
            
            self.functions.ui_caht_function().get_redenvelope(red_id, headers, self.web_url)
            self.sleep(0.5)
            
    def get_verification(self):
        nation = 'JP'
        phone = 819016773820

        headers = self.header()
        self.functions.ui_caht_function().send_verification(nation, phone, headers)

    def check_login(self):
        nation = 'JP'
        phone = 819016773812
        
        for i in range(0,200,1):
            self.do_web_login(nation, "819016773812", "zxc12345", self.device_id, self.web_url)
            
            print(f"{phone}註冊成功")
            phone += 1
            self.sleep(0.5)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
