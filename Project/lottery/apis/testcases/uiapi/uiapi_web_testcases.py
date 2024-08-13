# -*- coding: utf-8 -*-
import hashlib, sys, os, requests, time, random, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from lottery.web.testcases.base_testcase import BaseTestCase
from lottery.apis.function_layer.functions import Functions
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
import common.utils.globalvar as gl
from common.web.decorator import DecorateClass



class UiApiWebTestCases(BaseTestCase, BaseFunction_API):

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

    # 登入
    @DecorateClass('PFREQ-T1808')
    def test_reseller_login(self):
        return self.do_reseller_login(self.reseller_account, self.reseller_password, self.reseller_otp, self.reseller_url)

    # 登入
    @DecorateClass('PFREQ-T1809')
    def test_cmweb_login(self):
        if self.env == 'stage':
            self.skipTest('stage沒有cmweb')
        return self.do_cm_login(self.cmweb_account, self.cmweb_password)

    # 登入
    @DecorateClass('PFREQ-T1810')
    def test_dwh_login(self):
        if self.env == 'stage':
            self.skipTest('stage沒有dwh')
        password = self.dwhweb_password
        hash_object = hashlib.md5(password.encode())
        passwd_md5 = hash_object.hexdigest()
    
        return self.do_dwh_login(self.dwhweb_account, passwd_md5,self.dwhweb_url)

    # 登入
    @DecorateClass('PFREQ-T1843')
    def test_mynah_web(self):
        if self.env == 'stage':
            self.skipTest('stage沒有mynah')
        api_service = ['peacock', 'magpie', 'pelican']
        self.functions.mynah_web_customer_service().mynah_health(self.mynah_web_url, self.mynah_admin_url, api_service)


    # 登入
    @DecorateClass('PFREQ-T1837')
    def test_mynah_admin_login(self):
        if self.env == 'stage':
            self.skipTest('stage沒有mynah')
        return self.do_mynah_login(self.mynah_account, self.mynah_password, self.mynah_admin_url)

    # 註冊
    @DecorateClass('PFREQ-T1847')
    def test_register(self):
        # Web - 註冊
        register_account, status_code = self.functions.ui_web_register().do_register(self.web_url)

    # 線上支付
    @DecorateClass('PFREQ-T1869')
    def test_desposit_onlinepay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的商號
        merchant_id = self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, '线上支付', 'card', '365pay_wy', '12345', '12345')

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用線上支付渠道存款
        desposit_id = self.functions.ui_web_my_wallet().online_merchant_deposit(merchant_id, web_certification, self.web_url)

        # Admin
        # 驗證，在線入款是否有資料
        self.functions.ui_admin_deposit_management().get_online_deposit(desposit_id, self.web_account, admin_certification, self.admin_url)
        
        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_webdeposit_apply(self.web_account, admin_certification, self.admin_url, desposit_id, self.admin_otp)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, 100, web_certification, self.web_url)

    # 銀聯支付
    @DecorateClass('PFREQ-T1871')
    def test_desposit_unionpay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增银联支付的商號
        merchant_id = self.functions.ui_admin_account_management().readd_online_merchant('银联支付', admin_certification, self.admin_url, '线上支付', 'card', '365pay_wy', '12345', '12345')

        # Web
        # 登入
        res, web_certification = self.test_web_login()
        
        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用银联支付渠道存款
        desposit_id = self.functions.ui_web_my_wallet().online_merchant_deposit(merchant_id, web_certification, self.web_url)

        # Admin
        # 驗證，在線入款是否有資料
        self.functions.ui_admin_deposit_management().get_online_deposit(desposit_id, self.web_account, admin_certification, self.admin_url)
        
        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_webdeposit_apply(self.web_account, admin_certification, self.admin_url, desposit_id, self.admin_otp)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, 100, web_certification, self.web_url)

    # 京東支付
    @DecorateClass('PFREQ-T1873')
    def test_desposit_jdpay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增京東支付的商號
        merchant_id = self.functions.ui_admin_account_management().readd_online_merchant('京东支付', admin_certification, self.admin_url, '线上支付', 'card', '365pay_wy', '12345', '12345')

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用京東支付渠道存款
        desposit_id = self.functions.ui_web_my_wallet().online_merchant_deposit(merchant_id, web_certification, self.web_url)

        # Admin
        # 驗證，在線入款是否有資料
        self.functions.ui_admin_deposit_management().get_online_deposit(desposit_id, self.web_account, admin_certification, self.admin_url)
        
        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_webdeposit_apply(self.web_account, admin_certification, self.admin_url, desposit_id, self.admin_otp)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, 100, web_certification, self.web_url)

    # 公司入款
    @DecorateClass('PFREQ-T1877')
    def test_company_deposit(self):
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
        deposit_money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', web_certification, self.web_url)

        # Admin
        # 驗證，公司入款是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(deposit_money), web_certification, self.web_url)

    # 支付寶-面對面掃碼
    @DecorateClass('PFREQ-T1891')
    def test_alipay_qrcode(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增支付寶-面對面掃碼的銀行帳號
        bank_account = self.functions.ui_admin_account_management().readd_bank_account('支付宝面对面扫码', '支付宝', '支付宝面对面扫码', '支付寶面對面自動測試', '2', admin_certification, self.admin_url)
        
        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('支付宝', '支付宝面对面扫码', '支付寶面對面自動測試', admin_certification, self.admin_url)

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用支付寶-面對面掃碼渠道存款
        deposit_money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'qrcode', '支付宝', '11111', 'ALIPAY', web_certification, self.web_url)

        # Admin
        # 驗證，支付寶-面對面掃碼是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(deposit_money), web_certification, self.web_url)

    # 支付寶-轉帳
    @DecorateClass('PFREQ-T1894')
    def test_alipay_transfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增支付寶-轉帳的銀行帳號
        bank_account = self.functions.ui_admin_account_management().readd_bank_account('支付宝转帐', '支付宝', '支付宝转帐', '支付寶轉帳自動測試', '4', admin_certification, self.admin_url)
        
        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('支付宝', '支付宝转帐', '支付寶轉帳自動測試', admin_certification, self.admin_url)

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用支付寶-轉帳渠道存款
        deposit_money = self.functions.ui_web_my_wallet().transfer_deposit('alipay', bank_id, 'ALIPAY', '支付宝', 'ALIPAY', 'ALIPAY', web_certification, self.web_url)

        # Admin
        # 驗證，支付寶-轉帳是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, float(deposit_money), web_certification, self.web_url)

    # 微信-面對面掃碼
    @DecorateClass('PFREQ-T1895')
    def test_weixin_qrcode(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增微信-面對面掃碼的銀行帳號
        bank_account = self.functions.ui_admin_account_management().readd_bank_account('微信面对面扫码', '微信', '微信面对面扫码', '微信面對面自動測試', '1', admin_certification, self.admin_url)
        
        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('微信', '微信面对面扫码', '微信面對面自動測試', admin_certification, self.admin_url)

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用微信-面對面掃碼渠道存款
        deposit_money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'qrcode', '微信', '11111', 'WEIXIN', web_certification, self.web_url)

        # Admin
        # 驗證，微信-面對面掃碼是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, int(deposit_money), web_certification, self.web_url)

    # 微信-轉帳
    @DecorateClass('PFREQ-T1896')
    def test_weixin_transfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增微信-轉帳的銀行帳號
        bank_account = self.functions.ui_admin_account_management().readd_bank_account('微信转帐', '微信', '微信转帐', '微信轉帳自動測試', '3', admin_certification, self.admin_url)
        
        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('微信', '微信转帐', '微信轉帳自動測試', admin_certification, self.admin_url)

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 存款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 使用微信-轉帳渠道存款
        deposit_money = self.functions.ui_web_my_wallet().transfer_deposit('wechat', bank_id, 'WEIXIN', '微信', 'WEIXIN', 'WEIXIN', web_certification, self.web_url)

        # Admin
        # 驗證，微信-轉帳是否有資料
        self.functions.ui_admin_deposit_management().get_company_deposit(deposit_money, self.web_account, admin_certification, self.admin_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # Web
        # 確認主錢包金額有正確增加
        self.functions.ui_web_my_wallet().check_specific_balance('cp', before_money, float(deposit_money), web_certification, self.web_url)

    # 測試線上取款
    @DecorateClass('PFREQ-T1897')
    def test_withdraw(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 提款前，先記錄主錢包金額
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 線上取款
        withdraw_money, real_withdraw = self.functions.ui_web_my_wallet().online_withdraw(web_certification, self.web_url)

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

    # 彩票遊戲-BG澳門六合彩
    @DecorateClass('PFREQ-T6982')
    def test_bg_lottery_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bg_lottery', '3799', web_certification, self.web_url)
    
    # 棋牌遊戲-開元棋牌
    @DecorateClass('PFREQ-T1898')
    def test_ky_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('ky_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('ky_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-VG棋牌
    @DecorateClass('PFREQ-T1899')
    def test_vg_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('vg_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('vg_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-GM棋牌
    @DecorateClass('PFREQ-T1900')
    def test_gm_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('gm_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('gm_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-龍城棋牌
    @DecorateClass('PFREQ-T1905')
    def test_lc_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('lc_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('lc_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-百勝棋牌
    @DecorateClass('PFREQ-T1906')
    def test_bs_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('bs_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('bs_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-FG棋牌
    @DecorateClass('PFREQ-T1907')
    def test_fg_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('fg_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('fg_qipai', game_list, web_certification, self.web_url)

    # 棋牌遊戲-KK棋牌
    @DecorateClass('PFREQ-T1908')
    def test_kk_qipai_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('kk_qipai', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('kk_qipai', game_list, web_certification, self.web_url)

    # 電子遊戲-MG電子
    @DecorateClass('PFREQ-T1909')
    def test_mg_electron_game(self):

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('mg_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('mg_game', game_list, web_certification, self.web_url)

    # 電子遊戲-AG電子
    @DecorateClass('PFREQ-T1910')
    def test_ag_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('ag_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('ag_game', game_list, web_certification, self.web_url)

    # 電子遊戲-CQ9電子
    @DecorateClass('PFREQ-T2635')
    def test_cq_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('cq_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('cq_game', game_list, web_certification, self.web_url)

    # 電子遊戲-dt電子
    @DecorateClass('PFREQ-T1912')
    def test_dt_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('dt_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('dt_game', game_list, web_certification, self.web_url)

    # 電子遊戲-pt電子
    @DecorateClass('PFREQ-T1913')
    def test_pt_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('pt_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('pt_game', game_list, web_certification, self.web_url)

    # 電子遊戲-bbin電子
    @DecorateClass('PFREQ-T1914')
    def test_bbin_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()
        
        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('bbin_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('bbin_game', game_list, web_certification, self.web_url)

    # 電子遊戲-sb電子
    @DecorateClass('PFREQ-T1915')
    def test_sb_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('sb_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('sb_game', game_list, web_certification, self.web_url)

    # 電子遊戲-fg電子
    @DecorateClass('PFREQ-T1920')
    def test_fg_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('fg_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('fg_game', game_list, web_certification, self.web_url)

    # 電子遊戲-sw電子
    @DecorateClass('PFREQ-T1921')
    def test_sw_electron_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得特定的遊戲list
        game_list = self.functions.ui_web_third_party().get_game_list('sw_game', web_certification, self.web_url)

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_games('sw_game', game_list, web_certification, self.web_url)

    # 真人視訊-BG視訊廳
    @DecorateClass('PFREQ-T6981')
    def test_bg_video_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bg_video', '3798', web_certification, self.web_url)

    # 真人視訊-DG視訊廳
    @DecorateClass('PFREQ-T1922')
    def test_dg_video_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('dg_video', '3120', web_certification, self.web_url)    

    # 真人視訊-AG視訊廳
    @DecorateClass('PFREQ-T1925')
    def test_ag_video_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('ag_video', '508', web_certification, self.web_url)

    # 真人視訊-BBIN視訊廳
    @DecorateClass('PFREQ-T1926')
    def test_bbin_video_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_video', '1357', web_certification, self.web_url) 
        
    # 真人視訊-MG歐美廳
    @DecorateClass('PFREQ-T1927')
    def test_mg_occident_game(self):

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('mg_video', '977', web_certification, self.web_url)

    # 真人視訊-MG亞洲廳
    @DecorateClass('PFREQ-T1928')
    def test_mg_asia_game(self):

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('mg_video', '1586', web_certification, self.web_url) 

    # 真人視訊-GC甜心主播廳
    def test_gc_video_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('gc_video', '1395', web_certification, self.web_url)        

    # 全民捕魚-3D海盜來了
    @DecorateClass('PFREQ-T1929')
    def test_bs_fish_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bs_fish', '3103', web_certification, self.web_url)

    # 全民捕魚-3D美人魚
    @DecorateClass('PFREQ-T1930')
    def test_bs_fish2_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()
        
        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bs_fish', '3104', web_certification, self.web_url)

    # 全民捕魚-CQ9歡樂捕魚
    @DecorateClass('PFREQ-T1931')
    def test_cq_fish_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('cq_fish', '3149', web_certification, self.web_url)

    # 全民捕魚-AG館
    @DecorateClass('PFREQ-T1932')
    def test_ag_fish_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('ag_fish', '519', web_certification, self.web_url)

    # 全民捕魚-bb捕魚達人
    @DecorateClass('PFREQ-T1933')
    def test_bbin_fish_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_fish', '1555', web_certification, self.web_url)

    # 全民捕魚-BS千炮捕魚王
    @DecorateClass('PFREQ-T1934')
    def test_bs_fish3_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bs_fish', '2960', web_certification, self.web_url)

    # 全民捕魚-bb富貴漁場
    @DecorateClass('PFREQ-T1936')
    def test_bbin_fish2_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_fish', '3049', web_certification, self.web_url)

    # 全民捕魚-BS捕魚王中王
    @DecorateClass('PFREQ-T1937')
    def test_bs_fish4_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bs_fish', '2961', web_certification, self.web_url)

    # 全民捕魚-CQ9皇金漁場2
    def test_cq_fish2_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('cq_fish', '2298', web_certification, self.web_url)

    # 全民捕魚-CQ9皇金漁場1
    @DecorateClass('PFREQ-T1946')
    def test_cq_fish3_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('cq_fish', '2309', web_certification, self.web_url)

    # 全民捕魚-PT館
    def test_pt_fish_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('pt_fish', '2232', web_certification, self.web_url)

    # 全民捕魚-bb捕魚大師
    @DecorateClass('PFREQ-T1947')
    def test_bbin_fish3_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_fish', '1554', web_certification, self.web_url)

    # 全民捕魚-bb捕魚達人2
    @DecorateClass('PFREQ-T1948')
    def test_bbin_fish4_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_fish', '1999', web_certification, self.web_url)

    # 體育投注-沙巴體育
    @DecorateClass('PFREQ-T1949')
    def test_saba_sport_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('sb_sportbooks', '1080', web_certification, self.web_url)

    # 體育投注-BBIN體育
    @DecorateClass('PFREQ-T1950')
    def test_bbin_sport_game(self):
        if self.brand == 'sc':
            self.skipTest(f'此品牌沒有 BBIN 體育，brand: {self.brand}')

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('bbin_sport', '1358', web_certification, self.web_url)

    # 體育投注-皇冠體育
    @DecorateClass('PFREQ-T1951')
    def test_hg_sport_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('hg_sport', '3030', web_certification, self.web_url)

    # 體育投注-三昇體育
    @DecorateClass('PFREQ-T1952')
    def test_ss_sport_game(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 確認每一款遊戲是否正常
        self.functions.ui_web_third_party().open_game('ss_sport', '2816', web_certification, self.web_url)

    # 額度轉換

        # x to x 使用者輸入
    def test_x_to_x(self):
        money = 1
        # Web
        # 登入
        res, web_certification = self.test_web_login()
        
        a_wallet = gl.get_value('A')
        b_wallet = gl.get_value('B')
        num = gl.get_value('NUM')

        if a_wallet == b_wallet:
            raise EOFError(f'不可以同個錢包進行轉換 錢包1: {a_wallet} 錢包2: {b_wallet}')
        
        # 使用者選擇錢包
        for n in range(num):
            print(f'\n\n第{n+1}次 *****')
            print('----------------------------------')
            for _ in range(2):
                print(f'額度轉換 {a_wallet} to {b_wallet}\n----------------------------------')
                # 取得主錢包轉帳前的金額
                before_a = self.functions.ui_web_utils().get_specific_balance(a_wallet, web_certification, self.web_url)
                # 取得 a, b 錢包轉帳前的金額
                before_b = self.functions.ui_web_utils().get_specific_balance(b_wallet, web_certification, self.web_url)
                # 額度轉換
                self.functions.ui_web_my_wallet().quota_conversion(a_wallet, b_wallet, money, web_certification, self.web_url)
                # 確認額度轉換是否成功
                self.functions.ui_web_my_wallet().check_quota_conversion(a_wallet, b_wallet, int(before_a), int(before_b), money, web_certification, self.web_url)

                a_wallet = gl.get_value('B')
                b_wallet = gl.get_value('A')

            print('Pass')

    # 一鍵歸戶
    @DecorateClass('PFREQ-T1953')
    def test_return_cp(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得一鍵歸戶前各錢包的金額和應歸戶總金額
        before_wallet, return_money = self.functions.ui_web_utils().get_all_balance(web_certification, self.web_url)

        # 一鍵歸戶
        self.functions.ui_web_my_wallet().return_cp(web_certification, self.web_url)

        # 取得正在維護的錢包清單
        maintenance_list = self.functions.ui_web_my_wallet().wallet_in_maintenance(web_certification, self.web_url)

        # 確認一鍵歸戶後，各錢包的金額
        self.functions.ui_web_my_wallet().check_return_cp_wallet(before_wallet, return_money, maintenance_list, web_certification, self.web_url)

    # cp to ag
    @DecorateClass('PFREQ-T1954')
    def test_cp_to_ag(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 ag 錢包轉帳前的金額
        before_ag = self.functions.ui_web_utils().get_specific_balance('ag', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'ag', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'ag', int(before_cp), int(before_ag), 1, web_certification, self.web_url)

    # cp to mg
    @DecorateClass('PFREQ-T1955')
    def test_cp_to_mg(self):

        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 mg 錢包轉帳前的金額
        before_mg = self.functions.ui_web_utils().get_specific_balance('mg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'mg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'mg', int(before_cp), int(before_mg), 1, web_certification, self.web_url)

    # cp to sb
    @DecorateClass('PFREQ-T1956')
    def test_cp_to_sb(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 sb 錢包轉帳前的金額
        before_sb = self.functions.ui_web_utils().get_specific_balance('sb', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'sb', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'sb', int(before_cp), int(before_sb), 1, web_certification, self.web_url)

    # cp to bbin
    @DecorateClass('PFREQ-T1957')
    def test_cp_to_bbin(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 bbin 錢包轉帳前的金額
        before_bbin = self.functions.ui_web_utils().get_specific_balance('bbin', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'bbin', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'bbin', int(before_cp), int(before_bbin), 1, web_certification, self.web_url)

    # cp to 3s
    @DecorateClass('PFREQ-T1958')
    def test_cp_to_3s(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 3s 錢包轉帳前的金額
        before_3s = self.functions.ui_web_utils().get_specific_balance('ss', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'ss', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'ss', int(before_cp), int(before_3s), 1, web_certification, self.web_url)

    # cp to dt
    @DecorateClass('PFREQ-T1959')
    def test_cp_to_dt(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 dt 錢包轉帳前的金額
        before_dt = self.functions.ui_web_utils().get_specific_balance('dt', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'dt', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'dt', int(before_cp), int(before_dt), 1, web_certification, self.web_url)

    # cp to gc
    def test_cp_to_gc(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 gc 錢包轉帳前的金額
        before_gc = self.functions.ui_web_utils().get_specific_balance('gc', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'gc', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'gc', int(before_cp), int(before_gc), 1, web_certification, self.web_url)

    # cp to ky
    @DecorateClass('PFREQ-T1988')
    def test_cp_to_ky(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 ky 錢包轉帳前的金額
        before_ky = self.functions.ui_web_utils().get_specific_balance('ky', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'ky', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'ky', int(before_cp), int(before_ky), 1, web_certification, self.web_url)

    # cp to vg
    @DecorateClass('PFREQ-T1989')
    def test_cp_to_vg(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 vg 錢包轉帳前的金額
        before_vg = self.functions.ui_web_utils().get_specific_balance('vg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'vg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'vg', int(before_cp), int(before_vg), 1, web_certification, self.web_url)

    # cp to sw
    @DecorateClass('PFREQ-T1990')
    def test_cp_to_sw(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 sw 錢包轉帳前的金額
        before_sw = self.functions.ui_web_utils().get_specific_balance('sw', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'sw', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'sw', int(before_cp), int(before_sw), 1, web_certification, self.web_url)

    # cp to pt
    @DecorateClass('PFREQ-T1991')
    def test_cp_to_pt(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 pt 錢包轉帳前的金額
        before_pt = self.functions.ui_web_utils().get_specific_balance('pt', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'pt', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'pt', int(before_cp), int(before_pt), 1, web_certification, self.web_url)

    # cp to kx
    @DecorateClass('PFREQ-T1992')
    def test_cp_to_lc(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 lc 錢包轉帳前的金額
        before_lc = self.functions.ui_web_utils().get_specific_balance('lc', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'lc', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'lc', int(before_cp), int(before_lc), 1, web_certification, self.web_url)

    # cp to hg
    @DecorateClass('PFREQ-T1993')
    def test_cp_to_hg(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 hg 錢包轉帳前的金額
        before_hg = self.functions.ui_web_utils().get_specific_balance('hg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'hg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'hg', int(before_cp), int(before_hg), 1, web_certification, self.web_url)

    # cp to gm
    @DecorateClass('PFREQ-T1994')
    def test_cp_to_gm(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 gm 錢包轉帳前的金額
        before_gm = self.functions.ui_web_utils().get_specific_balance('gm', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'gm', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'gm', int(before_cp), int(before_gm), 1, web_certification, self.web_url)

    # cp to fg
    @DecorateClass('PFREQ-T1995')
    def test_cp_to_fg(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 fg 錢包轉帳前的金額
        before_fg = self.functions.ui_web_utils().get_specific_balance('fg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'fg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'fg', int(before_cp), int(before_fg), 1, web_certification, self.web_url)

    # cp to dg
    @DecorateClass('PFREQ-T1996')
    def test_cp_to_dg(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 dg 錢包轉帳前的金額
        before_dg = self.functions.ui_web_utils().get_specific_balance('dg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'dg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'dg', int(before_cp), int(before_dg), 1, web_certification, self.web_url)

    # cp to cq9
    @DecorateClass('PFREQ-T1997')
    def test_cp_to_cq9(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 cq9 錢包轉帳前的金額
        before_cq9 = self.functions.ui_web_utils().get_specific_balance('cq', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'cq', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'cq', int(before_cp), int(before_cq9), 1, web_certification, self.web_url)

    # cp to bsp
    @DecorateClass('PFREQ-T1998')
    def test_cp_to_bsp(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 bsp 錢包轉帳前的金額
        before_bsp = self.functions.ui_web_utils().get_specific_balance('bs', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'bs', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'bs', int(before_cp), int(before_bsp), 1, web_certification, self.web_url)

    # cp to kk
    @DecorateClass('PFREQ-T1999')
    def test_cp_to_kk(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 kk 錢包轉帳前的金額
        before_kk = self.functions.ui_web_utils().get_specific_balance('kk', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'kk', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'kk', int(before_cp), int(before_kk), 1, web_certification, self.web_url)

    # cp to bg
    @DecorateClass('PFREQ-T6983')
    def test_cp_to_bg(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得主錢包轉帳前的金額
        before_cp = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # 取得 bg 錢包轉帳前的金額
        before_bg = self.functions.ui_web_utils().get_specific_balance('bg', web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'bg', '1', web_certification, self.web_url)

        # 確認額度轉換是否成功
        self.functions.ui_web_my_wallet().check_quota_conversion('cp', 'bg', int(before_cp), int(before_bg), 1, web_certification, self.web_url)


    # 修改登入密码
    @DecorateClass('PFREQ-T2000')
    def test_change_login_password(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 修改成新密碼
        self.functions.ui_web_my_profile().change_login_password(self.web_password, '0123456', '111111', web_certification, self.web_url)

        # 修改回原本密碼
        self.functions.ui_web_my_profile().change_login_password('0123456', self.web_password, '111111', web_certification, self.web_url)

    # 修改提款密码
    @DecorateClass('PFREQ-T2001')
    def test_change_security_password(self):
        # Web
        # 登入
        res, web_certification = self.test_web_login()

        # 修改成新密碼
        self.functions.ui_web_my_profile().change_security_password(self.withdraw_password, '666666', web_certification, self.web_url)

        # 修改回原本密碼
        self.functions.ui_web_my_profile().change_security_password('666666', self.withdraw_password, web_certification, self.web_url)

    # 修改聯繫方式
    @DecorateClass('PFREQ-T2002')
    def test_change_contact(self):
        phone = '13' + str(random.randrange(100000000, 999999999, 9))
        phone_1 = '13' + str(random.randrange(100000000, 999999999, 9))
        # Web
        # 登入
        res, web_certification = self.test_web_login()
        # 修改成新的聯繫方式
        self.functions.ui_web_my_profile().change_contact('test000@gmail.com', phone, '654321', self.withdraw_password, web_certification, self.web_url)

        # 修改回原本密碼
        # 因為"13162490240"已有太多人使用過，目前機制會阻擋相同號碼輸入
        # self.functions.ui_web_my_profile().change_contact('autotest@qq.com', '13162490240', '123456', self.withdraw_password, web_certification, self.web_url)
        self.functions.ui_web_my_profile().change_contact('autotest@qq.com', phone_1, '123456', self.withdraw_password, web_certification, self.web_url)

    # 绑定出款银行
    def test_change_bank_card(self):
        # Web
        # 登入
        if self.brand == 'ttmj':
            res, web_certification = self.test_wap_login()
            url = self.mobile_url
        else:
            res, web_certification = self.test_web_login()
            url = self.web_url

        # 修改成新銀行
        self.functions.ui_web_my_profile().change_bank_card('人之初', '654', '321', self.withdraw_password, web_certification, url)

        # 修改回原本銀行
        self.functions.ui_web_my_profile().change_bank_card('性本善', '123', '456', self.withdraw_password, web_certification, url)

    # 站內消息
    @DecorateClass('PFREQ-T2003')
    def test_station_news(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 寄送站內信
        self.functions.ui_admin_station_news().send_message('Bot Message test', self.web_account, admin_certification, self.admin_url)

        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得站內信
        response = self.functions.ui_web_my_news().get_messages(web_certification, self.web_url)

        # 刪除所有站內信
        self.functions.ui_web_my_news().delete_messages(response, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特碼號碼
    @DecorateClass('PFREQ-T2004')
    def lottery_order_special_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特碼兩面
    @DecorateClass('PFREQ-T1893')
    def lottery_order_special_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特码-特肖
    @DecorateClass('PFREQ-T2024')
    def lottery_order_special_teshaw(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-特肖', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特码-合肖
    @DecorateClass('PFREQ-T2025')
    def lottery_order_special_he_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_special_he_xiao('smam6', handicap_info, '特码-合肖', '特码-特肖', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特码-头数
    @DecorateClass('PFREQ-T2026')
    def lottery_order_special_head_count(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-头数', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特码-尾数
    @DecorateClass('PFREQ-T2027')
    def lottery_order_special_mantissa(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-尾数', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 特码-五行
    @DecorateClass('PFREQ-T2028')
    def lottery_order_special_five_elements(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-五行', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码-号码
    @DecorateClass('PFREQ-T2029')
    def lottery_order_positive_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码-总和
    @DecorateClass('PFREQ-T2030')
    def lottery_order_positive_sum(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码-总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码-正肖
    @DecorateClass('PFREQ-T2031')
    def lottery_order_positive_zheng_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码-正肖', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码-总肖
    @DecorateClass('PFREQ-T2032')
    def lottery_order_positive_chief_shaw(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码-总肖', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特一-号码
    @DecorateClass('PFREQ-T2033')
    def lottery_order_positive_special_one_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特一-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特一-两面
    @DecorateClass('PFREQ-T2034')
    def lottery_order_positive_special_one_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特一-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特一-色波
    @DecorateClass('PFREQ-T2035')
    def lottery_order_positive_special_one_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特一-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特二-号码
    @DecorateClass('PFREQ-T2036')
    def lottery_order_positive_special_two_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特二-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特二-两面
    @DecorateClass('PFREQ-T2037')
    def lottery_order_positive_special_two_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特二-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特二-色波
    @DecorateClass('PFREQ-T2038')
    def lottery_order_positive_special_two_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特二-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特三-号码
    @DecorateClass('PFREQ-T2039')
    def lottery_order_positive_special_three_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特三-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特三-两面
    @DecorateClass('PFREQ-T2040')
    def lottery_order_positive_special_three_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特三-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特三-色波
    @DecorateClass('PFREQ-T2041')
    def lottery_order_positive_special_three_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特三-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特四-号码
    @DecorateClass('PFREQ-T2042')
    def lottery_order_positive_special_four_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特四-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特四-两面
    @DecorateClass('PFREQ-T2043')
    def lottery_order_positive_special_four_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特四-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特四-色波
    @DecorateClass('PFREQ-T2063')
    def lottery_order_positive_special_four_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特四-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特五-号码
    @DecorateClass('PFREQ-T2064')
    def lottery_order_positive_special_five_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特五-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特五-两面
    @DecorateClass('PFREQ-T2065')
    def lottery_order_positive_special_five_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特五-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特五-色波
    @DecorateClass('PFREQ-T2066')
    def lottery_order_positive_special_five_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特五-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特六-号码
    @DecorateClass('PFREQ-T2067')
    def lottery_order_positive_special_six_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特六-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特六-两面
    @DecorateClass('PFREQ-T2068')
    def lottery_order_positive_special_six_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特六-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 正码特-正码特六-色波
    @DecorateClass('PFREQ-T2069')
    def lottery_order_positive_special_six_color(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '正码特-正码特六-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 平特肖尾-一尾
    @DecorateClass('PFREQ-T2070')
    def lottery_order_pinshaw_tail_one_tail(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '平特肖尾-一尾', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 平特肖尾-一肖
    @DecorateClass('PFREQ-T2071')
    def lottery_order_pinshaw_tail_yi_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '平特肖尾-一肖', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-二尾碰
    @DecorateClass('PFREQ-T2072')
    def lottery_order_lian_xiao_lian_tail_two_tail(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-二尾碰', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-三尾碰
    @DecorateClass('PFREQ-T2073')
    def lottery_order_lian_xiao_lian_tail_three_tail(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-三尾碰', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-四尾碰
    @DecorateClass('PFREQ-T2074')
    def lottery_order_lian_xiao_lian_tail_four_tail(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-四尾碰', 4, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-五尾碰
    @DecorateClass('PFREQ-T2076')
    def lottery_order_lian_xiao_lian_tail_five_tail(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-五尾碰', 5, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-二肖连
    @DecorateClass('PFREQ-T2077')
    def lottery_order_lian_xiao_lian_tail_two_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-二肖连', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-三肖连
    @DecorateClass('PFREQ-T2079')
    def lottery_order_lian_xiao_lian_tail_three_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-三肖连', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-四肖连
    @DecorateClass('PFREQ-T2080')
    def lottery_order_lian_xiao_lian_tail_four_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-四肖连', 4, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连肖连尾-五肖连
    @DecorateClass('PFREQ-T2082')
    def lottery_order_lian_xiao_lian_tail_five_xiao(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '连肖连尾-五肖连', 5, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-特串
    @DecorateClass('PFREQ-T2083')
    def lottery_order_consecutive_number_special(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-特串', '特码-号码', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-二中特
    @DecorateClass('PFREQ-T2085')
    def lottery_order_consecutive_number_two_special_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-二中特', '特码-号码', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-二全中
    @DecorateClass('PFREQ-T2087')
    def lottery_order_consecutive_number_two_all_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-二全中', '特码-号码', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-三中二
    @DecorateClass('PFREQ-T2088')
    def lottery_order_consecutive_number_three_win_two(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-三中二', '特码-号码', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-三全中
    @DecorateClass('PFREQ-T2089')
    def lottery_order_consecutive_number_three_all_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-三全中', '特码-号码', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 连码-四全中
    @DecorateClass('PFREQ-T2111')
    def lottery_order_consecutive_number_four_all_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order_consecutive_number('smam6', handicap_info, '连码-四全中', '特码-号码', 4, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-五不中
    @DecorateClass('PFREQ-T2112')
    def lottery_order_not_win_five_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-五不中', 5, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-六不中
    @DecorateClass('PFREQ-T2113')
    def lottery_order_not_win_six_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-六不中', 6, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-七不中
    @DecorateClass('PFREQ-T2114')
    def lottery_order_not_win_seven_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-七不中', 7, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-八不中
    @DecorateClass('PFREQ-T2115')
    def lottery_order_not_win_eight_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-八不中', 8, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-九不中
    @DecorateClass('PFREQ-T2116')
    def lottery_order_not_win_nine_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-九不中', 9, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-十不中
    @DecorateClass('PFREQ-T2117')
    def lottery_order_not_win_ten_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-十不中', 10, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-十一不中
    @DecorateClass('PFREQ-T2118')
    def lottery_order_not_win_eleven_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-十一不中', 11, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 不中-十二不中
    @DecorateClass('PFREQ-T2119')
    def lottery_order_not_win_twelve_not_win(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '不中-十二不中', 12, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 色波-色波
    @DecorateClass('PFREQ-T2120')
    def lottery_order_sb_sb(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '色波-色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 色波-半波
    @DecorateClass('PFREQ-T2121')
    def lottery_order_sb_bb(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '色波-半波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)
        
    # 彩票投注 - 澳門賽馬會 - 色波-半半波
    @DecorateClass('PFREQ-T2122')
    def lottery_order_sb_bbb(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '色波-半半波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 色波-七色波
    @DecorateClass('PFREQ-T2123')
    def lottery_order_sb_seven_sb(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '色波-七色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-五中一
    @DecorateClass('PFREQ-T2124')
    def lottery_order_win_five_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-五中一', 5, self.env, web_certification, self.web_url)
        
        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-六中一
    @DecorateClass('PFREQ-T2125')
    def lottery_order_win_six_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-六中一', 6, self.env, web_certification, self.web_url)
        
        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-七中一
    @DecorateClass('PFREQ-T2126')
    def lottery_order_win_seven_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-七中一', 7, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-八中一
    @DecorateClass('PFREQ-T2127')
    def lottery_order_win_eight_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-八中一', 8, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-九中一
    @DecorateClass('PFREQ-T2128')
    def lottery_order_win_nine_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-九中一', 9, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 澳門賽馬會 - 中一-十中一
    @DecorateClass('PFREQ-T2129')
    def lottery_order_win_ten_win_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 澳門賽馬會 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '中一-十中一', 10, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 两面 - 万
    @DecorateClass('PFREQ-T2130')
    def ssc_order_two_sides_ten_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 万', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 两面 - 千
    @DecorateClass('PFREQ-T2131')
    def ssc_order_two_sides_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 千', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 两面 - 百
    @DecorateClass('PFREQ-T2132')
    def ssc_order_two_sides_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 两面 - 十
    @DecorateClass('PFREQ-T2144')
    def ssc_order_two_sides_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 两面 - 个
    @DecorateClass('PFREQ-T2145')
    def ssc_order_two_sides_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 总和
    @DecorateClass('PFREQ-T2146')
    def ssc_order_sum(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 总和 - 尾数
    @DecorateClass('PFREQ-T2147')
    def ssc_order_sum_mantissa(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '总和 - 尾数', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 龙虎和
    @DecorateClass('PFREQ-T2148')
    def ssc_order_long_hu_he(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '龙虎和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 五字
    @DecorateClass('PFREQ-T2149')
    def ssc_order_sum_five_characters(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 五字', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 前三
    @DecorateClass('PFREQ-T2150')
    def ssc_order_sum_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 前三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 中三
    @DecorateClass('PFREQ-T2151')
    def ssc_order_sum_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 中三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 后三
    @DecorateClass('PFREQ-T2152')
    def ssc_order_sum_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 后三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 万千
    @DecorateClass('PFREQ-T2153')
    def ssc_order_sum_ten_thousand_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 万千', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 万百
    @DecorateClass('PFREQ-T2154')
    def ssc_order_sum_ten_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 万百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 万十
    @DecorateClass('PFREQ-T2155')
    def ssc_order_sum_ten_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 万十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 万个
    @DecorateClass('PFREQ-T2156')
    def ssc_order_sum_ten_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 万个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 千百
    @DecorateClass('PFREQ-T2157')
    def ssc_order_sum_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 千百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 千十
    @DecorateClass('PFREQ-T2158')
    def ssc_order_sum_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 千十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 千个
    @DecorateClass('PFREQ-T2159')
    def ssc_order_sum_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 千个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 百十
    @DecorateClass('PFREQ-T2160')
    def ssc_order_sum_hundred_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 百十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 百个
    @DecorateClass('PFREQ-T2161')
    def ssc_order_sum_hundred_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 百个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和值 - 十个
    @DecorateClass('PFREQ-T2162')
    def ssc_order_sum_ten_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和值 - 十个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 五字
    @DecorateClass('PFREQ-T2163')
    def ssc_order_sum_mantissa_five_characters(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 五字', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 前三
    @DecorateClass('PFREQ-T2164')
    def ssc_order_sum_mantissa_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 前三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 中三
    @DecorateClass('PFREQ-T2165')
    def ssc_order_sum_mantissa_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 中三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 后三
    @DecorateClass('PFREQ-T2166')
    def ssc_order_sum_mantissa_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 后三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 万千
    @DecorateClass('PFREQ-T2167')
    def ssc_order_sum_mantissa_ten_thousand_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 万千', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 万百
    @DecorateClass('PFREQ-T2168')
    def ssc_order_sum_mantissa_ten_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 万百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 万十
    @DecorateClass('PFREQ-T2169')
    def ssc_order_sum_mantissa_ten_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 万十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 万个
    @DecorateClass('PFREQ-T2170')
    def ssc_order_sum_mantissa_ten_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 万个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 千百
    @DecorateClass('PFREQ-T2171')
    def ssc_order_sum_mantissa_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 千百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 千十
    @DecorateClass('PFREQ-T2172')
    def ssc_order_sum_mantissa_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 千十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 千个
    @DecorateClass('PFREQ-T2173')
    def ssc_order_sum_mantissa_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 千个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 百十
    @DecorateClass('PFREQ-T2174')
    def ssc_order_sum_mantissa_hundred_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 百十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 百个
    @DecorateClass('PFREQ-T2175')
    def ssc_order_sum_mantissa_hundred_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 百个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 和尾数 - 十个
    @DecorateClass('PFREQ-T2176')
    def ssc_order_sum_mantissa_ten_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '和尾数 - 十个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 任选一 - 全五
    @DecorateClass('PFREQ-T2177')
    def ssc_order_choose_one_all_five(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '任选一 - 全五', 1, self.env, web_certification, self.web_url)
    
        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)
        
    # 彩票投注 - 极速时时彩 - 任选一 - 前三
    @DecorateClass('PFREQ-T2183')
    def ssc_order_choose_one_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '任选一 - 前三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 任选一 - 中三
    @DecorateClass('PFREQ-T2184')
    def ssc_order_choose_one_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '任选一 - 中三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 任选一 - 后三
    @DecorateClass('PFREQ-T2185')
    def ssc_order_choose_one_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '任选一 - 后三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 一字定位 - 万
    @DecorateClass('PFREQ-T2186')
    def ssc_order_word_positioning_ten_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '一字定位 - 万', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 一字定位 - 千
    @DecorateClass('PFREQ-T2187')
    def ssc_order_word_positioning_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '一字定位 - 千', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 一字定位 - 百
    @DecorateClass('PFREQ-T2188')
    def ssc_order_word_positioning_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '一字定位 - 百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 一字定位 - 十
    @DecorateClass('PFREQ-T2189')
    def ssc_order_word_positioning_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '一字定位 - 十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 一字定位 - 个
    @DecorateClass('PFREQ-T2190')
    def ssc_order_word_positioning_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '一字定位 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 万千
    @DecorateClass('PFREQ-T2191')
    def ssc_order_twoword_positioning_ten_thousand_thousand(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 万千 - 万', '二字定位 - 万千 - 千', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 万百
    @DecorateClass('PFREQ-T2192')
    def ssc_order_twoword_positioning_ten_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 万百 - 万', '二字定位 - 万百 - 百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 万十
    @DecorateClass('PFREQ-T2193')
    def ssc_order_twoword_positioning_ten_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 万十 - 万', '二字定位 - 万十 - 十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 万个
    @DecorateClass('PFREQ-T2194')
    def ssc_order_twoword_positioning_ten_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 万个 - 万', '二字定位 - 万个 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 千百
    @DecorateClass('PFREQ-T2195')
    def ssc_order_twoword_positioning_thousand_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 千百 - 千', '二字定位 - 千百 - 百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)
        
    # 彩票投注 - 极速时时彩 - 二字定位 - 千十
    @DecorateClass('PFREQ-T2196')
    def ssc_order_twoword_positioning_thousand_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 千十 - 千', '二字定位 - 千十 - 十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 千个
    @DecorateClass('PFREQ-T2197')
    def ssc_order_twoword_positioning_thousand_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 千个 - 千', '二字定位 - 千个 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 百十
    @DecorateClass('PFREQ-T2198')
    def ssc_order_twoword_positioning_hundred_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 百十 - 百', '二字定位 - 百十 - 十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 百个
    @DecorateClass('PFREQ-T2199')
    def ssc_order_twoword_positioning_hundred_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 百个 - 百', '二字定位 - 百个 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 二字定位 - 十个
    @DecorateClass('PFREQ-T2200')
    def ssc_order_twoword_positioning_ten_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '二字定位 - 十个 - 十', '二字定位 - 十个 - 个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 三字定位 - 前三
    @DecorateClass('PFREQ-T2201')
    def ssc_order_threeword_positioning_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '三字定位 - 前三 - 万', '三字定位 - 前三 - 千', 1, self.env, web_certification, self.web_url, '三字定位 - 前三 - 百')

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 三字定位 - 中三
    @DecorateClass('PFREQ-T2202')
    def ssc_order_threeword_positioning_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '三字定位 - 中三 - 千', '三字定位 - 中三 - 百', 1, self.env, web_certification, self.web_url, '三字定位 - 中三 - 十')

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 三字定位 - 后三
    @DecorateClass('PFREQ-T2203')
    def ssc_order_threeword_positioning_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '三字定位 - 后三 - 百', '三字定位 - 后三 - 十', 1, self.env, web_certification, self.web_url, '三字定位 - 后三 - 个')

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 五字定位
    @DecorateClass('PFREQ-T2204')
    def ssc_order_fiveword_positioning(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().ssc_order_word_positioning('jsssc', handicap_info, '五字定位 - 万', '五字定位 - 千', 1, self.env, web_certification, self.web_url, '五字定位 - 百', '五字定位 - 十', '五字定位 - 个')

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)
        
    # 彩票投注 - 极速时时彩 - 组选三 - 前三
    @DecorateClass('PFREQ-T2205')
    def ssc_order_group_three_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选三 - 前三', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 组选三 - 中三
    @DecorateClass('PFREQ-T2206')
    def ssc_order_group_three_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选三 - 中三', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 组选三 - 后三
    @DecorateClass('PFREQ-T2207')
    def ssc_order_group_three_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选三 - 后三', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 组选六 - 前三
    @DecorateClass('PFREQ-T2208')
    def ssc_order_group_six_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选六 - 前三', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 组选六 - 中三
    @DecorateClass('PFREQ-T2209')
    def ssc_order_group_six_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选六 - 中三', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 组选六 - 后三
    @DecorateClass('PFREQ-T2210')
    def ssc_order_group_six_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '组选六 - 后三', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 跨度 - 前三
    @DecorateClass('PFREQ-T2211')
    def ssc_order_span_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '跨度 - 前三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 跨度 - 中三
    @DecorateClass('PFREQ-T2212')
    def ssc_order_span_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '跨度 - 中三', 1, self.env, web_certification, self.web_url)
        
        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 跨度 - 后三
    @DecorateClass('PFREQ-T2213')
    def ssc_order_span_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '跨度 - 后三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 特殊玩法 - 前三
    @DecorateClass('PFREQ-T2214')
    def ssc_order_special_play_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '特殊玩法 - 前三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 特殊玩法 - 中三
    @DecorateClass('PFREQ-T2215')
    def ssc_order_special_play_middle_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '特殊玩法 - 中三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速时时彩 - 特殊玩法 - 后三
    @DecorateClass('PFREQ-T2216')
    def ssc_order_special_play_last_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速时时彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '特殊玩法 - 后三', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 單號1-5 - 冠军
    @DecorateClass('PFREQ-T2221')
    def pk_ten_order_champion(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 單號1-5 - 亚军
    @DecorateClass('PFREQ-T2222')
    def pk_ten_order_runner_up(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '亚军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 單號1-5 - 季军
    @DecorateClass('PFREQ-T2223')
    def pk_ten_order_third_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '季军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 單號1-5 - 第四名
    @DecorateClass('PFREQ-T2224')
    def pk_ten_order_fourth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第四名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 單號1-5 - 第五名
    @DecorateClass('PFREQ-T2225')
    def pk_ten_order_fifth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第五名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 单号6-10 - 第六名
    @DecorateClass('PFREQ-T2226')
    def pk_ten_order_sixth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第六名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 单号6-10 - 第七名
    @DecorateClass('PFREQ-T2227')
    def pk_ten_order_seventh_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第七名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 单号6-10 - 第八名
    @DecorateClass('PFREQ-T2228')
    def pk_ten_order_eighth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第八名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 单号6-10 - 第九名
    @DecorateClass('PFREQ-T2229')
    def pk_ten_order_ninth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第九名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 单号6-10 - 第十名
    @DecorateClass('PFREQ-T2230')
    def pk_ten_order_tenth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第十名', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 冠亚和 - 冠亚军和-号码
    @DecorateClass('PFREQ-T2231')
    def pk_ten_order_champion_and_runner_up_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '冠亚军和-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 冠亚和 - 冠亚军和-两面
    @DecorateClass('PFREQ-T2232')
    def pk_ten_order_champion_and_runner_up_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '冠亚军和-两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 龙虎 - 冠军VS第十名-龙虎
    @DecorateClass('PFREQ-T2233')
    def pk_ten_order_champion_vs_tenth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '冠军VS第十名-龙虎', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 龙虎 - 亚军VS第九名-龙虎
    @DecorateClass('PFREQ-T2234')
    def pk_ten_order_runner_up_vs_ninth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '亚军VS第九名-龙虎', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 龙虎 - 季军VS第八名-龙虎
    @DecorateClass('PFREQ-T2235')
    def pk_ten_order_third_vs_eighth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '季军VS第八名-龙虎', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 龙虎 - 第四名VS第七名-龙虎
    @DecorateClass('PFREQ-T2236')
    def pk_ten_order_fourth_vs_seventh_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第四名VS第七名-龙虎', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 极速PK拾 - 龙虎 - 第五名VS第六名-龙虎
    @DecorateClass('PFREQ-T2237')
    def pk_ten_order_fifth_vs_sixth_place(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 极速PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '第五名VS第六名-龙虎', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - PC蛋蛋 - 特码-号码
    @DecorateClass('PFREQ-T2238')
    def pc_egg_order_special_number(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fcxy28', handicap_info, '特码 - 号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - PC蛋蛋 - 特码 - 包三
    @DecorateClass('PFREQ-T2239')
    def pc_egg_order_special_package_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().pc_egg_order_special_package_three('fcxy28', handicap_info, '特码 - 包三', '特码 - 号码', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - PC蛋蛋 - 两面
    @DecorateClass('PFREQ-T2240')
    def pc_egg_order_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fcxy28', handicap_info, '两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - PC蛋蛋 - 色波
    @DecorateClass('PFREQ-T2241')
    def pc_egg_order_sb(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fcxy28', handicap_info, '色波', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - PC蛋蛋 - 特殊
    @DecorateClass('PFREQ-T2242')
    def pc_egg_order_special(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fcxy28', handicap_info, '特殊', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 总和
    @DecorateClass('PFREQ-T2243')
    def eleven_choice_five_order_sum(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 两面-第一球
    @DecorateClass('PFREQ-T2244')
    def eleven_choice_five_order_two_sides_first_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '两面-第一球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 两面-第二球
    @DecorateClass('PFREQ-T2245')
    def eleven_choice_five_order_two_sides_secend_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '两面-第二球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 两面-第三球
    @DecorateClass('PFREQ-T2246')
    def eleven_choice_five_order_two_sides_third_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '两面-第三球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 两面-第四球
    @DecorateClass('PFREQ-T2247')
    def eleven_choice_five_order_two_sides_fourth_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '两面-第四球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 两面-第五球
    @DecorateClass('PFREQ-T2248')
    def eleven_choice_five_order_two_sides_fifth_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '两面-第五球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 单码-第一球
    @DecorateClass('PFREQ-T2249')
    def eleven_choice_five_order_single_code_first_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '单码-第一球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 单码-第二球
    @DecorateClass('PFREQ-T2250')
    def eleven_choice_five_order_single_code_second_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '单码-第二球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 单码-第三球
    @DecorateClass('PFREQ-T2251')
    def eleven_choice_five_order_single_code_third_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '单码-第三球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 单码-第四球
    @DecorateClass('PFREQ-T2252')
    def eleven_choice_five_order_single_code_fourth_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '单码-第四球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 单码-第五球
    @DecorateClass('PFREQ-T2253')
    def eleven_choice_five_order_single_code_fifth_ball(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '单码-第五球', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-一中一
    @DecorateClass('PFREQ-T2254')
    def eleven_choice_five_order_optional_one_in_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选一', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-二中二
    @DecorateClass('PFREQ-T2255')
    def eleven_choice_five_order_optional_two_in_two(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选二', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-三中三
    @DecorateClass('PFREQ-T2256')
    def eleven_choice_five_order_optional_three_in_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选三', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-四中四
    @DecorateClass('PFREQ-T2257')
    def eleven_choice_five_order_optional_four_in_four(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选四', 4, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-五中五
    @DecorateClass('PFREQ-T2258')
    def eleven_choice_five_order_optional_five_in_five(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选五', 5, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-六中五
    @DecorateClass('PFREQ-T2259')
    def eleven_choice_five_order_optional_six_in_five(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选六', 6, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-七中五
    @DecorateClass('PFREQ-T2260')
    def eleven_choice_five_order_optional_seven_in_five(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选七', 7, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 任选-八中五
    @DecorateClass('PFREQ-T2261')
    def eleven_choice_five_order_optional_eight_in_five(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '任选八', 8, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 组选前二
    @DecorateClass('PFREQ-T2279')
    def eleven_choice_five_order_group_selection_top_two(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '组选前二', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 组选前三
    @DecorateClass('PFREQ-T2280')
    def eleven_choice_five_order_group_selection_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '组选前三', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 直选前二
    @DecorateClass('PFREQ-T2281')
    def eleven_choice_five_order_direct_selection_top_two(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().eleven_choice_five_order_direct_selection('jisu11x5', handicap_info, '直选前二', '单码-第一球', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 11选5 - 直选前三
    @DecorateClass('PFREQ-T2282')
    def eleven_choice_five_order_direct_selection_top_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().eleven_choice_five_order_direct_selection('jisu11x5', handicap_info, '直选前三', '单码-第一球', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 两面
    @DecorateClass('PFREQ-T2283')
    def k_three_order_two_sides(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 点数
    @DecorateClass('PFREQ-T2284')
    def k_three_order_point(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '点数', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 三军
    @DecorateClass('PFREQ-T2285')
    def k_three_order_three_armies(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '三军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 围骰/全骰
    @DecorateClass('PFREQ-T2286')
    def k_three_order_round_dice(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '围骰/全骰', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 长牌
    @DecorateClass('PFREQ-T2287')
    def k_three_order_long_card(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '长牌', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 快3 - 短牌
    @DecorateClass('PFREQ-T2288')
    def k_three_order_short_card(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '短牌', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 一字定位-百 
    @DecorateClass('PFREQ-T2289')
    def normal_lottery_order_word_positioning_hundred(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '一字定位-百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)
        
    # 彩票投注 - 一般彩票 - 一字定位-十 
    @DecorateClass('PFREQ-T2290')
    def normal_lottery_order_word_positioning_ten(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '一字定位-十', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 一字定位-个
    @DecorateClass('PFREQ-T2291')
    def normal_lottery_order_word_positioning_one(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '一字定位-个', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 组选 - 二星组选
    @DecorateClass('PFREQ-T2292')
    def normal_lottery_order_two_star_group_selection(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '二星组选', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 组选 - 三星组选三
    @DecorateClass('PFREQ-T2293')
    def normal_lottery_order_three_star_group_selection_three(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星组选三', 2, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 组选 - 三星组选六
    @DecorateClass('PFREQ-T2294')
    def normal_lottery_order_three_star_group_selection_six(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星组选六', 3, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 字串关
    @DecorateClass('PFREQ-T2295')
    def normal_lottery_order_word_parley(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().normal_lottery_order_word_parley('fc3d', handicap_info, '字串关-百', '字串关-十', 1, self.env, web_certification, self.web_url, '字串关-个')

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 和值(百十个位)
    @DecorateClass('PFREQ-T2296')
    def normal_lottery_order_sum(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '和值(百十个位)', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 和尾数
    @DecorateClass('PFREQ-T2297')
    def normal_lottery_order_sum_mantissa(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '和尾数', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 跨度
    @DecorateClass('PFREQ-T2298')
    def normal_lottery_order_span(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '跨度', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 龙虎和
    @DecorateClass('PFREQ-T2299')
    def normal_lottery_order_longhuhe(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '龙虎和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 彩票投注 - 一般彩票 - 三星特别玩法
    @DecorateClass('PFREQ-T2300')
    def normal_lottery_order_three_star_special(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 福彩3D 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星特别玩法', 1, self.env, web_certification, self.web_url)
 
        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-澳門分分彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2301')
    def check_lottery_amff6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('amff6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('amff6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-澳门三分彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2302')
    def check_lottery_amsf6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('amsf6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('amsf6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-澳门五分彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2303')
    def check_lottery_amwf6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('amwf6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('amwf6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-澳門賽馬會，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2303')
    def check_lottery_smam6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('smam6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('smam6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)


    # 確認六合彩盤口-分分六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2304')
    def check_lottery_ff6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('ff6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('ff6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-三分六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2305')
    def check_lottery_sf6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sf6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('sf6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-极速六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2306')
    def check_lottery_js6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('js6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('js6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-香港六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2307')
    def check_lottery_hk_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('hk', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('hk', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-新澳門六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2308')
    def check_lottery_nam6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('nam6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('nam6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認六合彩盤口-澳門六合彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2309')
    def check_lottery_am6_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 六合彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('am6', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('am6', handicap_info, '特码-号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認時時彩盤口-极速时时彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2310')
    def check_ssc_jsssc_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 時時彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jsssc', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jsssc', handicap_info, '两面 - 万', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認時時彩盤口-五分时时彩，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2311')
    def check_ssc_wfssc_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 時時彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('wfssc', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('wfssc', handicap_info, '两面 - 万', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認時時彩盤口-澳洲幸运5，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2312')
    def check_ssc_aozxy5_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 時時彩 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('aozxy5', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('aozxy5', handicap_info, '两面 - 万', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PK拾盤口-极速PK拾，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2313')
    def check_pk_ten_jspk10_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jspk10', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jspk10', handicap_info, '冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PK拾盤口-五分PK拾，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2314')
    def check_pk_ten_wfpk10_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('wfpk10', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('wfpk10', handicap_info, '冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PK拾盤口-澳洲幸运10，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2315')
    def check_pk_ten_aozxy10_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('aozxy10', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('aozxy10', handicap_info, '冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PK拾盤口-幸运飞艇，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2316')
    def check_pk_ten_malxyft_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PK拾 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('malxyft', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('malxyft', handicap_info, '冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PC蛋蛋盤口-PC蛋蛋，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2317')
    def check_pc_egg_fcxy28_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fcxy28', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fcxy28', handicap_info, '特码 - 号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PC蛋蛋盤口-加拿大幸运28，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2318')
    def check_pc_egg_jndbsxy28_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jndbsxy28', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jndbsxy28', handicap_info, '特码 - 号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PC蛋蛋盤口-台湾幸运28，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2319')
    def check_pc_egg_twxy28_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('twxy28', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('twxy28', handicap_info, '特码 - 号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認PC蛋蛋盤口-五分幸运28，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2320')
    def check_pc_egg_wfxy28_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 PC蛋蛋 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('wfxy28', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('wfxy28', handicap_info, '特码 - 号码', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認11選5盤口-极速11选5，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2321')
    def check_eleven_choice_five_jisu11x5_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11選5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisu11x5', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisu11x5', handicap_info, '总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認11選5盤口-三分11选5，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2322')
    def check_eleven_choice_five_sf11x5_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11選5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sf11x5', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('sf11x5', handicap_info, '总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認11選5盤口-五分11选5，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2323')
    def check_eleven_choice_five_wf11x5_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 11選5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('wf11x5', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('wf11x5', handicap_info, '总和', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認快3盤口-极速快3，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2324')
    def check_k_three_jisuk3_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jisuk3', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('jisuk3', handicap_info, '两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認快3盤口-三分快3，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2325')
    def check_k_three_sfk3_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sfk3', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('sfk3', handicap_info, '两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認快3盤口-五分快3，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2326')
    def check_k_three_wfk3_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 快3 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('wfk3', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('wfk3', handicap_info, '两面', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認一般彩票盤口-福彩3D，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2327')
    def check_normal_lottery_fc3d_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 一般彩票 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '一字定位-百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # 確認一般彩票盤口-排列三，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T2022')
    def check_normal_lottery_pl3_bet_record(self):
        # web
        # 登入
        res, web_certification = self.test_web_login()

        # 取得 一般彩票 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('pl3', web_certification, self.web_url)
    
        # 投注彩票
        res = self.functions.ui_web_third_party().lottery_order('pl3', handicap_info, '一字定位-百', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_lottery_bet_record(res, web_certification, self.web_url)

    # ============================== AA_Web_TestCases ==============================

    # 股指投注 - 上證100 - 定位膽 - 冠軍
    @DecorateClass('PFREQ-T5022')
    def stock_order_positioning_champion(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證100 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sz100wf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('sz100wf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)
    
    # 股指投注 - 比特幣 - 定位膽 - 冠軍
    @DecorateClass('PFREQ-T5484')
    def btcusd_order_positioning_champion(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 比特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('btcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('btcusd', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 股指投注 - 比特幣 - 定位膽 - 亞軍
    @DecorateClass('PFREQ-T5485')
    def btcusd_order_positioning_second_place(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 比特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('btcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('btcusd', handicap_info, '定位-亚军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 股指投注 - 比特幣 - 雙面盤 - 冠軍
    @DecorateClass('PFREQ-T5486')
    def btcusd_order_double_champion(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 比特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('btcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('btcusd', handicap_info, '双面-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 股指投注 - 比特幣 - 雙面盤 - 亞軍
    @DecorateClass('PFREQ-T5487')
    def btcusd_order_double_second_place(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 比特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('btcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('btcusd', handicap_info, '双面-亚军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指1分-深證成指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5488')
    def check_one_min_stock_shezcz_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證成指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezcz', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezcz', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指1分-沪深300，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5489')
    def check_one_min_stock_hs300_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 沪深300 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('hs300', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('hs300', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指1分-深證100，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5490')
    def check_one_min_stock_shez100_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證100 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shez100', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shez100', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指1分-上證指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5491')
    def check_one_min_stock_szzs_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szzs', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szzs', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-深證1000，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5492')
    def check_three_min_stock_shez1000sf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證1000 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shez1000sf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shez1000sf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-深證創新指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5493')
    def check_three_min_stock_shezcxsf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證創新指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezcxsf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezcxsf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-上證A股指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5494')
    def check_three_min_stock_szagzssf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證A股指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szagzssf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szagzssf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-上證工業指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5495')
    def check_three_min_stock_szgyzssf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證工業指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szgyzssf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szgyzssf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-深證央企，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5496')
    def check_three_min_stock_shezyqsf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證央企 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezyqsf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezyqsf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-上證B股指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5497')
    def check_three_min_stock_szbgzssf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證B股指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szbgzssf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szbgzssf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指3分-上證市值百強，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5498')
    def check_three_min_stock_szbqsf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證市值百強 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szbqsf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szbqsf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-幣安幣，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5499')
    def check_five_min_stock_bnbusd_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 幣安幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('bnbusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('bnbusd', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-上證100，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5500')
    def check_five_min_stock_sz100wf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證100 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sz100wf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('sz100wf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-比特幣，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5501')
    def check_five_min_stock_btcusd_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 比特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('btcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('btcusd', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-以太幣，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5502')
    def check_five_min_stock_ethusd_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 以太幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('ethusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('ethusd', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-香港恆生指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5503')
    def check_five_min_stock_hkhszswf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 香港恆生指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('hkhszswf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('hkhszswf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指5分-萊特幣，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5504')
    def check_five_min_stock_ltcusd_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 萊特幣 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('ltcusd', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('ltcusd', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-深證B指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5505')
    def check_eight_min_stock_shezbzbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證B指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezbzbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezbzbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-上證商業指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5506')
    def check_eight_min_stock_szsyzsbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證商業指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szsyzsbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szsyzsbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-創業板指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5507')
    def check_eight_min_stock_cybzbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 創業板指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('cybzbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('cybzbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-深證A指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5508')
    def check_eight_min_stock_shezazbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證A指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezazbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezazbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-上證能源，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5509')
    def check_eight_min_stock_sznybf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證能源 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('sznybf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('sznybf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-上證綜指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5510')
    def check_eight_min_stock_szzhzsbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 上證綜指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('szzhzsbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('szzhzsbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指8分-中小板指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5511')
    def check_eight_min_stock_zxbzbf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 中小板指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('zxbzbf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('zxbzbf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指10分-超大盤，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5512')
    def check_ten_min_stock_cdpshf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 超大盤 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('cdpshf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('cdpshf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指10分-地產指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5513')
    def check_ten_min_stock_dczsshf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 地產指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('dczsshf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('dczsshf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指10分-科創50，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5514')
    def check_ten_min_stock_kc50shf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 科創50 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('kc50shf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('kc50shf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指10分-深證綜指，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5515')
    def check_ten_min_stock_shezzzshf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 深證綜指 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezzzshf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('shezzzshf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 確認股指10分-基金指數，下注後投注紀錄是否正確
    @DecorateClass('PFREQ-T5516')
    def check_ten_min_stock_jjzsshf_bet_record(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 基金指數 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('jjzsshf', web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_order('jjzsshf', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # 股指跟投
    @DecorateClass('PFREQ-T5023')
    def stock_chat_room_follow(self):
        # wap
        # 登入
        res, web_certification = self.test_wap_login()

        # 取得 跟投 玩法
        follow_info = self.functions.ui_web_third_party().get_stock_follow_info(web_certification, self.web_url)

        # 投注股指
        res = self.functions.ui_web_third_party().stock_follow_order(follow_info, web_certification, self.web_url)

        # 驗證投注紀錄
        self.functions.ui_web_third_party().check_stock_bet_record(res, web_certification, self.web_url)

    # ================================ Dwh_TestCases =============================

    def test_Dwh_Set_Period(self):
        password = self.dwhweb_password
        hash_object = hashlib.md5(password.encode())
        passwd_md5 = hash_object.hexdigest()

        game_sort = self.test_data[0].split('&')
        ball_number_sort = self.test_data[1].split('&')
        period_num = self.test_data[2]
        
        assert len(game_sort) == len(ball_number_sort), "格式不正確,請確認彩種與球號數量"
        
        res, certification = self.do_dwh_login(self.dwhweb_account, passwd_md5,self.dwhweb_url)

        for num in range(0, len(game_sort)):
            for Sub_game in game_sort[num].split('-'):
                Period_list = self.functions.ui_admin_period_management().get_period(certification, Sub_game, period_num, self.dwhweb_url)
                self.functions.ui_admin_period_management().change_period(certification, Sub_game, period_num, Period_list, ball_number_sort[num], self.dwhweb_url)

    
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method