# -*- coding: utf-8 -*-
import hashlib, sys, os, requests, time, random, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from lottery.web.testcases.base_testcase import BaseTestCase
from lottery.apis.function_layer.functions import Functions
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
import common.utils.globalvar as gl
from common.web.decorator import DecorateClass



class UiApiMissionTestCases(BaseTestCase, BaseFunction_API):

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
    @DecorateClass('PFREQ-T1802')
    def test_web_login(self):
        return self.do_web_login(self.web_account, self.web_password, self.web_url)

    # 登入
    @DecorateClass('PFREQ-T1805')
    def test_wap_login(self):
        return self.do_wap_login(self.web_account, self.web_password, self.mobile_url)

    # 登入
    def test_admin_login(self):
        return self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)

    # ============================== Mission_TestCases =============================

    # 公司入款
    def test_company_deposit_mission(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        bank_account = self.functions.ui_admin_account_management().readd_bank_account('公司入款', '公司入款', '公司入款', '銀行自動測試', '0', admin_certification, self.admin_url)
        
        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', '銀行自動測試', admin_certification, self.admin_url)

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用公司入款渠道存款
        deposit_money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', web_certification, self.web_url, deposit_money=str(gl.get_value('DEPOSIT_MONEY')))

        # Admin
        # 驗證，公司入款是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(deposit_money), web_certification, self.web_url)

    # 線上取款
    def test_withdraw_mission(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 提款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 線上取款
        withdraw_money, real_withdraw = self.functions.ui_web_my_wallet().online_withdraw(web_certification, self.web_url, withdraw_money=gl.get_value('WITHDRAW'))

        if self.env == 'prod':
            # Web
            # 確認主錢包金額有正確減少
            self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(f'-{real_withdraw}'), web_certification, self.web_url)
        else:
            # Admin
            # 登入
            res, admin_certification = self.test_admin_login()

            # 驗證，出款申請是否有資料
            withdraw_id = self.functions.ui_admin_withdraw_management().get_withdraw_info(withdraw_money, self.web_account, admin_certification, self.admin_url)

            # 鎖定特定提款申請
            self.functions.ui_admin_withdraw_management().lock_specific_withdraw(withdraw_id, self.web_account, admin_certification, self.admin_url)

            # 同意出款
            self.functions.ui_admin_withdraw_management().agree_withdraw(withdraw_id, self.web_account, admin_certification, self.admin_url)

            # Web
            # 確認主錢包金額有正確減少
            self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(f'-{withdraw_money}'), web_certification, self.web_url) 

    # 彩票投注 - 分分六合彩 - 特碼兩面
    def lottery_order_special_two_sides_mission(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 分分六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('ff6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_misson('ff6', handicap_info, '特码-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 驗證任務結果
    def check_mission_result(self):
        # admin 登入
        res, admin_certification = self.test_admin_login()

        # 取得指定任務
        mission_id, campaign_no = self.functions.ui_admin_event_managment().get_mission_id(admin_certification, self.admin_url, gl.get_value('MISSION_NAME'))

        # 取的任務期數
        period_id, period_no = self.functions.ui_admin_event_managment().get_mission_period(admin_certification, self.admin_url, mission_id)

        # 驗證玩家任務狀態
        self.functions.ui_admin_event_managment().check_mission_status_of_user(self.brand, period_id, self.web_account)

        # 驗證明細頁達成任務
        amount_dict = self.functions.ui_admin_event_managment().verify_detail(admin_certification, self.admin_url, self.web_account, period_id, gl.get_value('EXPECTED_AMOUNT'))

        # # 驗證人工存入派發
        self.functions.ui_admin_event_managment().verify_mandeposit(admin_certification, self.admin_url, self.web_account, gl.get_value('MISSION_NAME'), campaign_no, period_no, amount_dict)


    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method