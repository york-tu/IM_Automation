# -*- coding: utf-8 -*-
import unittest, hashlib, sys, os, requests, time, random, datetime
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.exchange_wellpay.app.testcase.base_testcase import BaseTestCase
from Project.exchange_wellpay.apis.function_layer.functions import Functions
import common.utils.globalvar as gl
import logging

class UiApiToolsTestCases(BaseTestCase):

    # ================================= TestSetting ================================
    @classmethod
    def setUpClass(cls):
        # cls.setting_test_data(cls)  # 設定測試數據
        cls.functions = Functions(cls.skipTest)
        cls.env = gl.get_value('ENV')
    
    # def tearDown(self):
    #     self.check_result(str(self.id()).split('.')[-1])
    
    @classmethod
    def tearDownClass(cls):
        pass

    # ================================= Web_TestCases ==============================
    

    # 新增搶單
    def test_casher_add_order(self):
        # Web
        for money in range(100, 102):
            self.functions.ui_paybox_casher_tool().add_order(money = money, merchant_id = 2015, method = 'BANK_ZZ')
            # methon=(微信:WX, 支付寶:ZFB, QQ:QQ, 云閃付:YSF, 銀行:BANK)_(掃碼:QR, 轉帳_ZZ) ex:銀行轉帳 BANK_ZZ、支付寶轉帳 ZFB_ZZ
            time.sleep(1)
    
    # 新增買單
    def test_casher_add_sell(self):
        # Web
        for money in range(100, 102):
            self.functions.ui_paybox_casher_tool().add_sell(money = money, merchant_id = 2015)
            time.sleep(1)
