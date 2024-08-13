# -*- coding: utf-8 -*-
import unittest, hashlib, sys, os, requests, time, random, datetime
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from lottery.web.testcases.base_testcase import BaseTestCase
from lottery.apis.function_layer.functions import Functions
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
from lottery.apis.lottery_list import LotteryList
import common.utils.globalvar as gl
import logging

class UiApiToolsTestCases(BaseTestCase, BaseFunction_API):
    web_account = ''
    web_certification = ''
    admin_certification = ''
    lottery_dict = {} # 彩票列表
    user_list = [] # 使用者人數
    deposit_list = [] # 人數存款金額
    withdraw_list = [] # 人數取款金額
    bet = [] # 所有下注金額
    bet_list = [0, 0, 0, 0] # 每個人下注總金額
    bet_single = [] # 切分每個人分別每一注金額
    money = 0
    withdraw = 0
    pay_money = 0
    
    # ================================= TestSetting ================================
    @classmethod
    def setUpClass(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        cls.functions = Functions(cls.skipTest)
        cls.env = gl.get_value('ENV')
        cls.lottery_dict = LotteryList.lottery(cls)
    # ================================= Web_TestCases ==============================
    
    # 登入
    def test_web_login(self):
        return self.do_web_login(self.web_account, self.web_password, self.web_url)

    # 登入
    def test_wap_login(self):
        return self.do_wap_login(self.web_account, self.web_password, self.mobile_url)

    # 登入
    def test_admin_login(self):
        return self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)

    # 登入
    def test_reseller_login(self):
        return self.do_reseller_login(self.reseller_account, self.reseller_password, self.reseller_otp, self.reseller_url)

    # 登入
    def test_cmweb_login(self):
        return self.do_cm_login(self.cmweb_account, self.cmweb_password)

    # 登入
    def test_dwh_login(self):
        password = self.dwhweb_password
        hash_object = hashlib.md5(password.encode())
        passwd_md5 = hash_object.hexdigest()
    
        return self.do_dwh_login(self.dwhweb_account, passwd_md5,self.dwhweb_url)

    # 登入
    def test_mynah_web(self):
        api_service = ['peacock', 'magpie', 'pelican']
        self.functions.mynah_web_customer_service().mynah_health(self.mynah_web_url, self.mynah_admin_url, api_service)

    # 登入
    def test_mynah_admin_login(self):
        return self.do_mynah_login(self.mynah_account, self.mynah_password, self.mynah_admin_url)


    def test_trigger(self):
        try:
            status = False
            day = str(datetime.datetime.now().strftime('%d'))
            if str(day) == '1':
                self.user_list = [
                    'a1573719',
                    '18328321',
                    'xiaowu52',
                    'llw1234',
                ]
            else:
                status = True
                self.user_list = [
                    '15816752',
                    'hufei013',
                    'guochen8',
                    '506mmm',
                ]
                

            withdraw_money = 0
            for user in range(0, len(self.user_list)):
                if status == False:
                    if user < 2:
                        min_money = 100
                        max_money = 3000
                    else:
                        min_money = 2000
                        max_money = 5000
                else:
                    min_money = 100
                    max_money = 3000

                withdraw_money = random.randint(min_money, max_money)
                self.withdraw_list.append(withdraw_money)

            self.deposit = 0
            times = 0
            
            for _ in range(0, 50):
                self.deposit = random.randint(10, 1000)
                self.bet.append(self.deposit)
                self.bet_list[times] += self.deposit
                times+=1
                if times == len(self.user_list):
                    times=0
            
            n = len(self.user_list)  # 切分成多少份
            length = len(self.bet)

            step = int(length / n) + 1  # 每份的长度
            for i in range(0, length, step):
                self.bet_single.append(self.bet[i: i + step])

            deposit_money = 0
            for user in range(0, len(self.user_list)):
                total = int((self.bet_list[user] + self.withdraw_list[user]))
                if status == False:
                    if user < 2:
                        min_money = total
                        max_money = total + 300
                    else:
                        min_money = total * 2
                        max_money = total * 2 + 3000
                else:
                    min_money = total
                    max_money = total + 300

                deposit_money = random.randint(min_money, max_money)
                self.deposit_list.append(deposit_money)

            for user in range(0, len(self.user_list)):
                self.web_account = self.user_list[user]
                self.deposit = str(self.deposit_list[user])
                self.withdraw = self.withdraw_list[user]
                self.bet_lottery = self.bet_single[user]

                print(f'\n***********  此次使用帳號為: "{self.web_account}"')
                print(f'***********  此次存款金額為: {self.deposit}')
                print(f'***********  此次提款金額為: {self.withdraw}')
                print(f'***********  此次下注金額為: {self.bet_list[user]}\n')
                
                res, self.web_certification = self.test_web_login()
                res, self.admin_certification = self.test_admin_login()
                
                self.test_manual_deposit()
                self.test_withdraw()
                self.test_lottery_random()
        except Exception:
            logging.exception('exception log')
            raise EOFError('測試錯誤')

    # 彩票投注 - 极速时时彩 - 和值 - 万百
    def test_lottery_random(self):
        for money in (self.bet_lottery):
            i = 0
            lottery = []
            handicap_info = []
            for i in range(4):
                lottery.append(random.choice(list(self.lottery_dict.values())))
                # 取得 极速时时彩 玩法
                handicap_info.append(self.functions.ui_web_third_party().get_handicap_info(lottery[i], self.web_certification, self.web_url))
            # 投注彩票
            self.functions.ui_web_third_party().lottery_random(lottery, handicap_info, money, self.env, self.web_certification, self.web_url)

    # 財務管理 -> 上分管理 -> 公司
    def test_company_deposit(self):
        # 取得指定銀行的银行卡号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', 'Kevin', self.admin_certification, self.admin_url)
        # 使用公司入款渠道存款
        self.deposit = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', self.web_certification, self.web_url, deposit_money=self.deposit)
        # 比對公司入款的存款記錄
        self.functions.ui_admin_deposit_management().compare_company_deposit(self.deposit, self.admin_certification, self.admin_url)
        
        # Admin
        # 驗證，公司入款是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(self.deposit, self.web_account, self.admin_certification, self.admin_url)
        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, self.admin_certification, self.admin_url)

        # 測試線上取款
    def test_withdraw(self):
        # 線上取款
        withdraw_money, real_withdraw = self.functions.ui_web_my_wallet().online_withdraw(self.web_certification, self.web_url, withdraw_money=self.withdraw)
        # 驗證，出款申請是否有資料
        withdraw_id = self.functions.ui_admin_withdraw_management().get_withdraw_info(withdraw_money, self.web_account, self.admin_certification, self.admin_url)
        # 鎖定特定提款申請
        self.functions.ui_admin_withdraw_management().lock_specific_withdraw(withdraw_id, self.web_account, self.admin_certification, self.admin_url)
        # 同意出款
        self.functions.ui_admin_withdraw_management().agree_withdraw(withdraw_id, self.web_account, self.admin_certification, self.admin_url)

    # 財務管理 -> 上分管理 -> 人工存入
    def test_manual_deposit(self):
        self.functions.ui_admin_manual_deposit().add_manual_deposit(self.web_account, self.admin_certification, self.admin_url, self.deposit)
        self.functions.ui_admin_manual_deposit().check_manual_deposit(self.web_account, self.admin_certification, self.admin_url)
        