# -*- coding: UTF-8 -*-
import unittest, hashlib, sys, os, requests, random, string, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from lottery.web.testcases.base_testcase import BaseTestCase
import time
from datetime import datetime, timedelta
from lottery.apis.function_layer.functions import Functions
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
import common.utils.globalvar as gl
from common.web.decorator import DecorateClass

class UiApiAdminTestCases(BaseTestCase, BaseFunction_API):
    brand = gl.get_value('BRAND')
    env = gl.get_value('ENV')
    # ================================= TestSetting ================================
    @classmethod
    def setUpClass(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        cls.functions = Functions(cls.skipTest)
        
    def tearDown(self):
        self.check_result(str(self.id()).split('.')[-1])

    # ================================ Admin_TestCases =============================
    
    # 登入
    @DecorateClass('PFREQ-T1817')
    def test_admin_login(self):
        return self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)

    # 關閉登入滑動驗證
    def test_close_login_slide_verified(self):
        res, admin_certification= self.test_admin_login()
        self.functions.ui_admin_system_list().close_login_slide_verified(admin_certification, self.admin_url, self.brand, self.reseller_url)

    # 關閉入款otp
    def test_close_deposit_otp(self):
        res, admin_certification= self.test_admin_login()
        self.functions.ui_admin_member_list().close_deposit_otp(admin_certification, self.admin_url)

    # 測試所有第三方遊戲Gameid是否存在
    def test_connection_link_api(self):
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        self.functions.ui_admin_interface_management().quickstart_api(admin_certification, self.host_ip, self.port)
        self.functions.ui_admin_interface_management().recommend_api(admin_certification, self.host_ip, self.port)
        self.functions.ui_admin_interface_management().menubarpc_api(admin_certification, self.host_ip, self.port)
    
    # 會員列表將在bot代理中的閒雜人等踢除
    @DecorateClass('PFREQ-T1814')
    def test_clear_user(self):
        default_agent = 'default_agent'
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        self.functions.ui_admin_member_list().clear_user(self.web_account, self.reseller_account, admin_certification, self.admin_url, self.admin_otp, default_agent)
  
    # 手續費用設定
    @DecorateClass('PFREQ-T1815')
    def test_set_charge(self):
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        self.functions.ui_admin_handling_fee().set_charge_max(admin_certification, self.admin_url)
        
    # 將彩票狀態都開啟
    @DecorateClass('PFREQ-T1816')
    def test_maintain_auto(self):
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        lottery_name = self.functions.ui_admin_maintain_setting().get_all_lottery_api(self.admin_url, self.host_ip, self.port)
        # Lottery_name = ['ff6', 'sf6', 'hbk3', 'jisuk3', 'wfk3', 'wfxy28', 'wfpk10', 'wfssc', 'cqssc', 'jsssc', 'jspk10', 'js6', 'hk', 'malxyft', 'bjpk10', 'xjssc', 'bjxy28', 'fcxy28', 'xjpxy28', 'jndbsxy28', 'twxy28', 'fc3d', 'pl3', 'shssc', 'gd11x5', 'sd11x5', 'sh11x5', 'jx11x5', 'ahk3', 'gxk3', 'hebk3', 'shk3', 'jsk3']
        self.functions.ui_admin_maintain_setting().set_lottery_status(admin_certification, self.admin_url, self.host_ip, self.port, lottery_name)

    # 將股指狀態都開啟
    @DecorateClass('PFREQ-T5476')
    def test_maintain_auto_stock(self):
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        stock_name = self.functions.ui_admin_game_setting().game_code_list(admin_certification, self.admin_url, 'zs')
        # stock_name = ['bnbusd', 'btcusd', 'cdpshf', 'cybzbf', 'dczsshf', 'ethusd', 'hkhszs', 'hkhszswf', 'hs300', 'jjzsshf', 'kc50shf', 'ltcusd', 'shez100', 'shez1000', 'shez1000sf', 'shezazbf', 'shezbzbf', 'shezcx', 'shezcxsf', 'shezcz', 'shezyq', 'shezyqsf', 'shezzzshf', 'sz100', 'sz100wf', 'szagzs', 'szagzssf', 'szbgzssf', 'szbq', 'szbqsf', 'szgyzssf', 'sznybf', 'szsyzsbf', 'szzhzsbf', 'szzs', 'zxbzbf']
        self.functions.ui_admin_maintain_setting().set_lottery_status(admin_certification, self.admin_url, self.host_ip, self.port, stock_name)

    # 後台新增銀行分類
    @DecorateClass('PFREQ-T1818')   
    def test_add_bank_api(self):
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
        self.functions.ui_admin_bank_account().check_num(admin_certification, self.admin_url) # 確認父類別有九個以上,不足新增父類別
        self.functions.ui_admin_bank_account().change_close(admin_certification, self.admin_url) # 關閉所有選項
        self.functions.ui_admin_bank_account().add_sort_all(admin_certification, self.admin_url, self.fileserver_url, self.brand) # 新增子類別及修改

    # 檢查遊戲繁簡體
    @DecorateClass('PFREQ-T1807')
    def test_language_game_check(self):
         # Admin
        # 登入
        res, admin_certification = self.test_admin_login()
        game_dict = self.functions.ui_admin_game_setting().game_list(admin_certification, self.admin_url)
        self.functions.ui_admin_game_setting().compare(game_dict)
    
    # 將指定股東下不相關之體系踢出
    @DecorateClass('PFREQ-T1813')
    def test_clear_in_shareholder(self):
        default_dict = {
           'shareholder': 'alisachang',
           'generalagent': 'ccp88888',
           'agent': 'default_agent'
        }

         # Admin
        # 登入
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_system_list().clear_user(self.web_account, self.shareholder, self.generalagent,\
             self.reseller_account, admin_certification, self.admin_url, self.admin_otp, default_dict)

    # 刪除所有銀行帳號存款方式
    @DecorateClass('PFREQ-T1819')
    def test_delete_bank_account(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 刪除所有銀行帳號存款方式
        self.functions.ui_admin_account_management().delete_all_bank_account(admin_certification, self.admin_url)

    # 新增公司入款
    @DecorateClass('PFREQ-T1820')
    def test_add_desposit_bank(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('公司入款', '公司入款', '公司入款', '銀行自動測試', '0', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', '銀行自動測試', admin_certification, self.admin_url)

    # 新增UPI入款
    @DecorateClass('PFREQ-T1820')
    def test_add_desposit_upi(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('UPI入款', 'UPI入款', 'UPI入款', 'upi自動測試', '6', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('UPI入款', 'UPI入款', 'upi自動測試', admin_certification, self.admin_url)

    # 新增微信-面對面掃碼
    @DecorateClass('PFREQ-T1821')
    def test_add_desposit_wechat_f2f(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('微信面对面扫码', '微信', '微信面对面扫码', '微信面對面自動測試', '1', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('微信', '微信面对面扫码', '微信面對面自動測試', admin_certification, self.admin_url)

    # 新增支付寶-面對面掃碼
    @DecorateClass('PFREQ-T1822')
    def test_add_desposit_alipay_f2f(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('支付宝面对面扫码', '支付宝', '支付宝面对面扫码', '支付寶面對面自動測試', '2', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('支付宝', '支付宝面对面扫码', '支付寶面對面自動測試', admin_certification, self.admin_url)

    # 新增微信-轉帳
    @DecorateClass('PFREQ-T1823')
    def test_add_desposit_wechat_transfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('微信转帐', '微信', '微信转帐', '微信轉帳自動測試', '3', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('微信', '微信转帐', '微信轉帳自動測試', admin_certification, self.admin_url)

    # 新增支付寶-轉帳
    @DecorateClass('PFREQ-T1824')
    def test_add_desposit_alipay_transfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_bank_account('支付宝转帐', '支付宝', '支付宝转帐', '支付寶轉帳自動測試', '4', admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_bank_account_exist('支付宝', '支付宝转帐', '支付寶轉帳自動測試', admin_certification, self.admin_url)

    # 刪除所有錢包地址存款方式
    @DecorateClass('PFREQ-T7826')
    def test_delete_crypto_wallet(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 刪除所有銀行帳號存款方式
        self.functions.ui_admin_account_management().delete_all_crypto_wallet(admin_certification, self.admin_url)

    # 新增币安_USDT(TRC)
    @DecorateClass('PFREQ-T7827')
    def test_add_desposit_crypto_bnb_trc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(TRC)', 'USDT', '虚拟币', '币安_TRC自動測試', '5', 'BNB',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(TRC)', '币安_TRC自動測試', admin_certification, self.admin_url)

    # 新增币安_USDT(ERC)
    @DecorateClass('PFREQ-T7828')
    def test_add_desposit_crypto_bnb_erc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(ERC)', 'USDT', '虚拟币', '币安_ERC自動測試', '5', 'BNB',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(ERC)', '币安_ERC自動測試', admin_certification, self.admin_url)

    # 新增火币_USDT(TRC)
    @DecorateClass('PFREQ-T7829')
    def test_add_desposit_crypto_ht_trc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(TRC)', 'USDT', '虚拟币', '火币_TRC自動測試', '5', 'HT',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(TRC)', '火币_TRC自動測試', admin_certification, self.admin_url)

    # 新增imToken_USDT(TRC)
    @DecorateClass('PFREQ-T7830')
    def test_add_desposit_crypto_imtoken_trc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(TRC)', 'USDT', '虚拟币', 'imToken_TRC自動測試', '5', 'LON',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(TRC)', 'imToken_TRC自動測試', admin_certification, self.admin_url)

    # 新增OLEX_USDT(ERC)
    @DecorateClass('PFREQ-T7831')
    def test_add_desposit_crypto_olex_erc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(ERC)', 'USDT', '虚拟币', 'OLEX_ERC自動測試', '5', 'OKB',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(ERC)', 'OLEX_ERC自動測試', admin_certification, self.admin_url)

    # 新增TokenPocket_USDT(ERC)
    @DecorateClass('PFREQ-T7832')
    def test_add_desposit_crypto_tokenpocket_erc(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增公司入款的銀行帳號
        self.functions.ui_admin_account_management().readd_crypto_wallet('USDT(ERC)', 'USDT', '虚拟币', 'TokenPocket_ERC自動測試', '5', 'TP',admin_certification, self.admin_url)

        # 檢查公司入款的銀行帳號是否正常新增
        self.functions.ui_admin_account_management().check_crypto_wallet_exist('USDT', 'USDT(ERC)', 'TokenPocket_ERC自動測試', admin_certification, self.admin_url)


    # 移除所有在線商號存款方式
    @DecorateClass('PFREQ-T1825')
    def test_delete_online_merchant(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 刪除所有銀行帳號存款方式
        self.functions.ui_admin_account_management().delete_all_online_merchant(admin_certification, self.admin_url)

    # 新增線上支付
    @DecorateClass('PFREQ-T1826')
    def test_add_onlinedesposit_onlinepay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, '自動市_线上支付', 'card', '365pay_wy', '12345', '12345')

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的銀行掃碼
    @DecorateClass('PFREQ-T7819')
    def test_add_onlinedesposit_kcurrency_bankscan(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_银行扫码', 'card', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, availamount='100,200')

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的銀行轉帳
    @DecorateClass('PFREQ-T7820')
    def test_add_onlinedesposit_kcurrency_banktransfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_银行转帐', 'card_wap', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback)

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的微信掃碼
    @DecorateClass('PFREQ-T7821')
    def test_add_onlinedesposit_kcurrency_wechatscan(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_微信扫码', 'weixin', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, availamount='100,200')

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的微信轉帳
    @DecorateClass('PFREQ-T7822')
    def test_add_onlinedesposit_kcurrency_wechattransfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_微信转帐', 'weixin_wap', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback)

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的支付寶掃碼
    @DecorateClass('PFREQ-T7823')
    def test_add_onlinedesposit_kcurrency_alipayscan(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_支付宝扫码', 'alipay', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, availamount='100,200')

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的支付寶轉帳
    @DecorateClass('PFREQ-T7824')
    def test_add_onlinedesposit_kcurrency_alipaytransfer(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_支付宝转帐', 'alipay_wap', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback)

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增K幣線上支付的K幣掃碼支付
    @DecorateClass('PFREQ-T7825')
    def test_add_onlinedesposit_kcurrency_scanpay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增線上支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('线上支付', admin_certification, self.admin_url, 'K币_扫码支付', 'zqb_scanpay', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, availamount='100,500,1000,2000,5000')

        # 確認是否有線上支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('线上支付', '线上支付', admin_certification, self.admin_url)

    # 新增銀聯支付
    @DecorateClass('PFREQ-T1827')
    def test_add_onlinedesposit_unionpay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增銀聯支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('银联支付', admin_certification, self.admin_url, '自動市_银联支付', 'card', '365pay_wy', '12345', '12345')

        # 確認是否有銀聯支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('银联支付', '银联支付', admin_certification, self.admin_url)

    # 新增京東支付
    @DecorateClass('PFREQ-T1828')
    def test_add_onlinedesposit_jdpay(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增京東支付的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('京东支付', admin_certification, self.admin_url, '自動市_京东支付', 'card', '365pay_wy', '12345', '12345')

        # 確認是否有京東支付的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('京东支付', '京东支付', admin_certification, self.admin_url)


    # 新增順付WellPay我要买-银行卡账号
    @DecorateClass('PFREQ-T6876')
    def test_add_wellpay_mybuy_bankaccount(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增我要买-银行卡账号的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('顺付WellPay-我要买入款', admin_certification, self.admin_url, '我要买-银行卡账号', 'zqb_my_buy_card', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_amount_interval='1-100,100-5000,5000-50000', category_subname='顺付WellPay-账号入款')

        # 確認是否有我要买-银行卡账号的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('顺付WellPay-我要买入款', '顺付WellPay-账号入款', admin_certification, self.admin_url)

    # 新增順付WellPay我要买-支付宝账号
    @DecorateClass('PFREQ-T6877')
    def test_add_wellpay_mybuy_alipayaccount(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增我要买-支付宝账号的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('顺付WellPay-我要买入款', admin_certification, self.admin_url, '我要买-支付宝账号', 'zqb_my_buy_alipay_num', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_amount_interval='1-100,100-5000,5000-50000', category_subname='顺付WellPay-账号入款')
        
        # 確認是否有我要买-支付宝账号的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('顺付WellPay-我要买入款', '顺付WellPay-账号入款', admin_certification, self.admin_url)

    # 新增順付WellPay我要买-微信账号
    @DecorateClass('PFREQ-T6878')
    def test_add_wellpay_mybuy_wechataccount(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增我要买-微信账号的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('顺付WellPay-我要买入款', admin_certification, self.admin_url, '我要买-微信账号', 'zqb_my_buy_weixin_num', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_amount_interval='1-100,100-5000,5000-50000', category_subname='顺付WellPay-账号入款')

        # 確認是否有我要买-微信账号的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('顺付WellPay-我要买入款', '顺付WellPay-账号入款', admin_certification, self.admin_url)

    # 新增順付WellPay我要买-支付宝扫码
    @DecorateClass('PFREQ-T6879')
    def test_add_wellpay_mybuy_alipayscan(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增我要买-支付宝扫码的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('顺付WellPay-我要买入款', admin_certification, self.admin_url, '我要买-支付宝扫码', 'zqb_my_buy_alipay_qr', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_amount_interval='1-100,100-5000,5000-50000', category_subname='顺付WellPay-扫码入款')

        # 確認是否有我要买-支付宝扫码的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('顺付WellPay-我要买入款', '顺付WellPay-扫码入款', admin_certification, self.admin_url)

    # 新增順付WellPay我要买-微信扫码
    @DecorateClass('PFREQ-T6880')
    def test_add_wellpay_mybuy_wechatscan(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增我要买-微信扫码的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('顺付WellPay-我要买入款', admin_certification, self.admin_url, '我要买-微信扫码', 'zqb_my_buy_weixin_qr', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_amount_interval='1-100,100-5000,5000-50000', category_subname='顺付WellPay-扫码入款')

        # 確認是否有我要买-微信扫码的商號
        self.functions.ui_admin_account_management().check_online_merchant_exist('顺付WellPay-我要买入款', '顺付WellPay-扫码入款', admin_certification, self.admin_url)


    # 新增在線出款_順付WellPay錢包出款
    @DecorateClass('PFREQ-T7817')
    def test_add_wellpay_wallet_withdraw(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增順付WellPay錢包出款的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('', admin_certification, self.admin_url, '順付錢包出款', 'zqb_kpay', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_or_withdraw='1')

        # 確認是否有順付WellPay錢包出款的商號
        self.functions.ui_admin_account_management().check_online_merchant_withdraw_exist('順付錢包出款', admin_certification, self.admin_url)


    # 新增在線出款_順付WellPay我要買出款
    @DecorateClass('PFREQ-T7818')
    def test_add_wellpay_mybuy_withdraw(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 新增順付WellPay我要買出款的在線商號
        self.functions.ui_admin_account_management().readd_online_merchant('', admin_certification, self.admin_url, '順付我要買出款', 'card', 'paybox', self.zqb_private_sign, bank_id=self.zqb_merchant_id, callback=self.zqb_deposit_callback, deposit_or_withdraw='1')

        #確認是否有順付WellPay我要買出款的商號
        self.functions.ui_admin_account_management().check_online_merchant_withdraw_exist('順付我要買出款', admin_certification, self.admin_url)


    # 新增返水/退佣方案
    @DecorateClass('PFREQ-T1829')
    def test_add_rebate_and_commision(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()
        
        # 刪除舊有方案
        self.functions.ui_admin_rebate_scale_setting().del_comm(self.commision_program, admin_certification, self.admin_url)

        # 新增退佣方案
        self.functions.ui_admin_rebate_scale_setting().add_comm(self.commision_program, admin_certification, self.admin_url)

        # 取得退佣方案id
        comm_id = self.functions.ui_admin_rebate_scale_setting().get_comm(self.commision_program, admin_certification, self.admin_url)

        # 新增階梯
        step_id = self.functions.ui_admin_rebate_scale_setting().add_step(comm_id, admin_certification, self.admin_url)

        # 更新階梯
        self.functions.ui_admin_rebate_scale_setting().push_step(comm_id, step_id, admin_certification, self.admin_url)

        # 更新頻道退佣
        self.functions.ui_admin_rebate_scale_setting().push_channel(comm_id, step_id, admin_certification, self.admin_url)

        # 更新產品比例(以 AG-捕鱼 為例)
        self.functions.ui_admin_rebate_scale_setting().push_products(comm_id, step_id, admin_certification, self.admin_url)

    # 財務管理 -> 比例設置 -> 手續費用
    @DecorateClass('PFREQ-T1867')
    def test_handing_fee(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 更新會員設定
        self.functions.ui_admin_fin_scale_setting().push_member_setting(admin_certification, self.admin_url)

        # 更新代理设定
        self.functions.ui_admin_fin_scale_setting().push_agent(admin_certification, self.admin_url)

        # 更新运营设定
        # self.functions.ui_admin_fin_scale_setting().push_payment(admin_certification, self.admin_url)

    # 運維管理 -> * -> 期數管理(极速六合彩)
    @DecorateClass('PFREQ-T1831')
    def test_period_management(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得盤口的期數列表
        handicap_record = self.functions.ui_admin_handicap().get_record('js6', admin_certification, self.admin_url)

        # 取得最新封盤的期數資料
        last_block_record_info = self.functions.ui_admin_handicap().get_last_block_record_info(handicap_record)

        # 新增期數
        self.functions.ui_admin_handicap().add_period('js6', '123', last_block_record_info, admin_certification, self.admin_url)

        # 修改期數內容
        self.functions.ui_admin_handicap().push_period('js6', '123', last_block_record_info, admin_certification, self.admin_url)

        # 派彩狀態-重派
        self.functions.ui_admin_handicap().payout('js6', '123', last_block_record_info, True, admin_certification, self.admin_url)

        # 派彩狀態-派彩
        self.functions.ui_admin_handicap().payout('js6', '123', last_block_record_info, False, admin_certification, self.admin_url)

        # 開盤
        self.functions.ui_admin_handicap().change_handicap_status('js6', '123', True, admin_certification, self.admin_url)

        # 封盤
        self.functions.ui_admin_handicap().change_handicap_status('js6', '123', False, admin_certification, self.admin_url)

        # 期数管理-作廢
        self.functions.ui_admin_handicap().rescind_period('js6', '123', admin_certification, self.admin_url)

        # 期数管理-補彩
        self.functions.ui_admin_handicap().rescind_period('js6', '123', admin_certification, self.admin_url)

        # 期数管理-刪除
        self.functions.ui_admin_handicap().del_period('js6', '123', admin_certification, self.admin_url)

    # 運維管理 -> * -> 期數管理(深證成指)
    @DecorateClass('PFREQ-T5477')
    def test_period_management_stock(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得盤口的期數列表
        handicap_record = self.functions.ui_admin_handicap().get_record('shezcz', admin_certification, self.admin_url)

        # 取得最新封盤的期數資料
        last_block_record_info = self.functions.ui_admin_handicap().get_last_block_record_info(handicap_record)

        # 新增期數
        self.functions.ui_admin_handicap().add_period('shezcz', '123', last_block_record_info, admin_certification, self.admin_url)

        # 修改期數內容
        self.functions.ui_admin_handicap().push_period('shezcz', '123', last_block_record_info, admin_certification, self.admin_url)

        # 派彩狀態-重派
        self.functions.ui_admin_handicap().payout('shezcz', '123', last_block_record_info, True, admin_certification, self.admin_url)

        # 派彩狀態-派彩
        self.functions.ui_admin_handicap().payout('shezcz', '123', last_block_record_info, False, admin_certification, self.admin_url)

        # 開盤
        self.functions.ui_admin_handicap().change_handicap_status('shezcz', '123', True, admin_certification, self.admin_url)

        # 封盤
        self.functions.ui_admin_handicap().change_handicap_status('shezcz', '123', False, admin_certification, self.admin_url)

        # 期数管理-作廢
        self.functions.ui_admin_handicap().rescind_period('shezcz', '123', admin_certification, self.admin_url)

        # 期数管理-補彩
        self.functions.ui_admin_handicap().rescind_period('shezcz', '123', admin_certification, self.admin_url)

        # 期数管理-刪除
        self.functions.ui_admin_handicap().del_period('shezcz', '123', admin_certification, self.admin_url)

    # 運維管理 -> * -> 盤口管理(极速六合彩)
    @DecorateClass('PFREQ-T1832')
    def test_handicap_management(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得盤口列表資訊
        res = self.functions.ui_admin_handicap().get_handicap_info('js6', admin_certification, self.admin_url)

        # 刪除舊有盤口
        self.functions.ui_admin_handicap().del_handicap(res, 'js6', admin_certification, self.admin_url, 'default')

        # 新增盤口
        self.functions.ui_admin_handicap().add_handicap('js6', 'bot',admin_certification, self.admin_url)

        # 取得盤口列表資訊
        res = self.functions.ui_admin_handicap().get_handicap_info('js6', admin_certification, self.admin_url)

        # 修改盤口賠率
        self.functions.ui_admin_handicap().change_rate('js6', 'bot', admin_certification, self.admin_url)

        # 修改盤口內容
        self.functions.ui_admin_handicap().change_handicap_info('js6', 'bot', admin_certification, self.admin_url)
        
        # 刪除舊有盤口
        self.functions.ui_admin_handicap().del_handicap(res, 'js6', admin_certification, self.admin_url)

    # 運維管理 -> * -> 盤口管理(深證成指)
    @DecorateClass('PFREQ-T5478')
    def test_handicap_management_stock(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得盤口列表資訊
        res = self.functions.ui_admin_handicap().get_handicap_info('shezcz', admin_certification, self.admin_url)

        # 刪除舊有盤口
        self.functions.ui_admin_handicap().del_handicap(res, 'shezcz', admin_certification, self.admin_url, 'default')

        # 新增盤口
        self.functions.ui_admin_handicap().add_handicap('shezcz', 'bot',admin_certification, self.admin_url)

        # 取得盤口列表資訊
        res = self.functions.ui_admin_handicap().get_handicap_info('shezcz', admin_certification, self.admin_url)

        # 修改盤口賠率
        self.functions.ui_admin_handicap().change_rate('shezcz', 'bot', admin_certification, self.admin_url)

        # 修改盤口內容
        self.functions.ui_admin_handicap().change_handicap_info('shezcz', 'bot', admin_certification, self.admin_url)
        
        # 刪除舊有盤口
        self.functions.ui_admin_handicap().del_handicap(res, 'shezcz', admin_certification, self.admin_url)

    # 運維管理 -> 注單中心 -> 注單作廢
    @DecorateClass('PFREQ-T1833')
    def test_betting_center_bet_rescind(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        bet_info = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星特别玩法', 1, 'prod', web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得注單列表待派彩 number
        pending_payout = self.functions.ui_admin_betting_center().get_betting_item(self.web_account, 'add', admin_certification, self.admin_url)
 
        # 注單作廢
        self.functions.ui_admin_betting_center().rescind_order(bet_info['id'], pending_payout['number'], admin_certification, self.admin_url, self.admin_otp)

    # 運維管理 -> 注單中心 -> 注單作廢
    @DecorateClass('PFREQ-T1833')
    def test_betting_center_bet_rescind_stock(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 定位-冠军 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezcz', web_certification, self.web_url)

        # 投注股指
        bet_info = self.functions.ui_web_third_party().stock_order('shezcz', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得注單列表待派彩 number
        pending_payout = self.functions.ui_admin_betting_center().get_betting_item(self.web_account, 'add', admin_certification, self.admin_url)
 
        # 注單作廢
        self.functions.ui_admin_betting_center().rescind_order(bet_info['id'], pending_payout['number'], admin_certification, self.admin_url, self.admin_otp)

    # 運維管理 -> 注單中心 -> 派彩總計
    @DecorateClass('PFREQ-T1834')
    def test_betting_center_payout_check(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        bet_info = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星特别玩法', 1, 'prod', web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得注單列表的總計資料
        bet_list_total = self.functions.ui_admin_betting_center().get_betting_pager('', 'payout', admin_certification, self.admin_url)

        # 派彩總計
        self.functions.ui_admin_betting_center().get_searchpayout(bet_list_total, admin_certification, self.admin_url)

    # 運維管理 -> 注單中心 -> 派彩總計
    @DecorateClass('PFREQ-T1834')
    def test_betting_center_payout_check_stock(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezcz', web_certification, self.web_url)

        # 投注彩票
        bet_info = self.functions.ui_web_third_party().stock_order('shezcz', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得注單列表的總計資料
        bet_list_total = self.functions.ui_admin_betting_center().get_betting_pager('', 'payout', admin_certification, self.admin_url)

        # 派彩總計
        self.functions.ui_admin_betting_center().get_searchpayout(bet_list_total, admin_certification, self.admin_url)

    # 運維管理 -> 注單中心 -> 注单校验
    @DecorateClass('PFREQ-T1835')
    def test_betting_center_bet_validation(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('fc3d', web_certification, self.web_url)

        # 投注彩票
        bet_info = self.functions.ui_web_third_party().lottery_order('fc3d', handicap_info, '三星特别玩法', 1, 'prod', web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 注单校验
        self.functions.ui_admin_betting_center().bet_validation(bet_info['number'], admin_certification, self.admin_url)

    # 運維管理 -> 注單中心 -> 注单校验
    @DecorateClass('PFREQ-T1835')
    def test_betting_center_bet_validation_stock(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 取得 11选5 玩法
        handicap_info = self.functions.ui_web_third_party().get_handicap_info('shezcz', web_certification, self.web_url)

        # 投注彩票
        bet_info = self.functions.ui_web_third_party().stock_order('shezcz', handicap_info, '定位-冠军', 1, self.env, web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 注单校验
        self.functions.ui_admin_betting_center().bet_validation(bet_info['number'], admin_certification, self.admin_url)

    # 運維管理 -> 紅包 -> 掃雷 -> 廳別管理
    @DecorateClass('PFREQ-T1836')
    def test_mine_sweeping_hall_management(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 創建廳別
        channel_name = self.functions.ui_admin_redenvelope().hb_create_channel('掃雷', admin_certification, self.admin_url)

        # 確認廳別是否有建立
        self.functions.ui_admin_redenvelope().hb_channel_search('掃雷', channel_name, admin_certification, self.admin_url)

    # 運維管理 -> 紅包 -> 牛牛 -> 廳別管理
    @DecorateClass('PFREQ-T1860')
    def test_niu_niu_hall_management(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 創建廳別
        channel_name = self.functions.ui_admin_redenvelope().hb_create_channel('牛牛', admin_certification, self.admin_url)

        # 確認廳別是否有建立
        self.functions.ui_admin_redenvelope().hb_channel_search('牛牛', channel_name, admin_certification, self.admin_url)

    # 財務管理 -> 外接平台 -> 額度轉換
    @DecorateClass('PFREQ-T1861')
    def test_external_platform_wallet_transfer(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 額度轉換
        transfer_id = self.functions.ui_web_my_wallet().quota_conversion('cp', 'ag', '1', web_certification, self.web_url)
        
        # 交易流水
        transfer_data = self.functions.ui_web_my_wallet().transfer_flow('transfer', web_certification, self.web_url)
        
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 確認Admin額度轉換是否有資料
        self.functions.ui_admin_external_platform().get_wallet_transfer_list(self.web_account, transfer_data, admin_certification, self.admin_url)

    # 財務管理 -> 外接平台 -> 餘額查詢
    @DecorateClass('PFREQ-T1862')
    def test_external_platform_balance_inquire(self):
        if self.brand != 'hy':
            self.skipTest('各品牌同時執行會互相影響cmweb的操作和數據，因此除了hy，其餘品牌skip')
        # CM Web 
        # 登入
        res, jwt = self.do_cm_login(self.cmweb_account, self.cmweb_password)

        # 取得CM Web顯示的廠商餘額
        cm_balance = self.functions.ui_admin_external_platform().get_cm_vendor_wallet(jwt, 'UAT-天堂遊戲')

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # CM 與 Admin廠商餘額比較
        self.functions.ui_admin_external_platform().vendor_balance_check(cm_balance, 'UAT-天堂遊戲', admin_certification, self.admin_url)

    #層級管理 -> 會員列表 -> 入款OTP
    @DecorateClass('PFREQ-T6178')
    def test_deposit_otp(self):
        #admin
        #登入
        res, admin_certification = self.test_admin_login()
        #開啟入款otp
        self.functions.ui_admin_member_list().open_deposit_otp(admin_certification, self.admin_url)
        #取得OTP密碼
        otp = self.functions.ui_admin_member_list().get_deposit_otp(admin_certification, self.web_account, self.admin_url)
        # 取得指定銀行的银行卡号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', '銀行自動測試', admin_certification, self.admin_url)
        
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        # 使用公司入款渠道存款
        money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', web_certification, self.web_url, otp)
        # 比對公司入款的存款記錄
        self.functions.ui_admin_deposit_management().compare_company_deposit(money, admin_certification, self.admin_url)
        
        #admin
        #登入
        res, admin_certification = self.test_admin_login()
        #關閉入款otp
        self.functions.ui_admin_member_list().close_deposit_otp(admin_certification, self.admin_url)

    # 財務管理 -> 上分管理 -> 公司
    @DecorateClass('PFREQ-T1863')
    def test_company_deposit(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得指定銀行的银行序号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', '銀行自動測試', admin_certification, self.admin_url)

        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 使用公司入款渠道存款
        money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', web_certification, self.web_url)

        # 比對公司入款的存款記錄
        self.functions.ui_admin_deposit_management().compare_company_deposit(money, admin_certification, self.admin_url)

    # 財務管理 -> 上分管理 -> 在線
    @DecorateClass('PFREQ-T1864')
    def test_online_deposit(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得對應帳號的merchantid
        merchantid = self.functions.ui_admin_account_management().check_online_merchant_exist('京东支付', '京东支付', admin_certification, self.admin_url)

        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 使用京東支付渠道存款
        self.functions.ui_web_my_wallet().online_merchant_deposit(merchantid, web_certification, self.web_url)
        
        # 比對在線入款的存款記錄
        self.functions.ui_admin_deposit_management().compare_merchant_deposit(admin_certification, self.admin_url)

    # 財務管理 -> 上分管理 -> 上分总览
    @DecorateClass('PFREQ-T1865')
    def test_deposit_overview(self):
        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 取得指定銀行的银行卡号
        bank_id = self.functions.ui_admin_account_management().check_bank_account_exist('公司入款', '公司入款', '銀行自動測試', admin_certification, self.admin_url)

        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 使用公司入款渠道存款
        deposit_money = self.functions.ui_web_my_wallet().qrcode_deposit(bank_id, 'BANK', '机器人', 'BANK', 'NONE', web_certification, self.web_url)

        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.web_account, admin_certification, self.admin_url)

        # 比對入款總覽第一筆的資訊是否正確
        self.functions.ui_admin_deposit_management().compare_company_deposit_overview('公司入款', self.web_account, admin_certification, self.admin_url)

        # 取得對應帳號的merchantid
        merchantid = self.functions.ui_admin_account_management().check_online_merchant_exist('京东支付', '京东支付', admin_certification, self.admin_url)

        # 使用京東支付渠道存款
        desposit_id = self.functions.ui_web_my_wallet().online_merchant_deposit(merchantid, web_certification, self.web_url)
        
        # 通過存款申請
        self.functions.ui_admin_deposit_management().agree_webdeposit_apply(self.web_account, admin_certification, self.admin_url, desposit_id, self.admin_otp)
        
        # 比對入款總覽第一筆的資訊是否正確
        self.functions.ui_admin_deposit_management().compare_company_deposit_overview('在线入款', self.web_account, admin_certification, self.admin_url)

    # 財務管理 -> 流水系統 -> 會員錢包
    @DecorateClass('PFREQ-T1866')
    def test_member_wallet(self):
        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)

        # 一鍵歸戶
        self.functions.ui_web_my_wallet().return_cp(web_certification, self.web_url)

        # 額度轉換
        self.functions.ui_web_my_wallet().quota_conversion('cp', 'ag', '1', web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()

        # 確認會員錢包顯示的金額是否正確
        self.functions.ui_admin_cash_system().compare_member_wallet(self.web_account, 'ag', 1, admin_certification, self.admin_url)

    # 財務管理 -> 下分管理 -> 人工提出
    @DecorateClass('PFREQ-T1830')
    def test_artificial_wallet(self):
        money = 1

        # web
        # 登入
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        before_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)

        # Admin
        # 登入
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_withdraw_management().artificial_withdraw(self.web_account, admin_certification, self.admin_url, money)
        after_money = self.functions.ui_web_utils().get_specific_balance('cp', web_certification, self.web_url)
        
        assert before_money - money == after_money, f'人工提出失敗, 提款金額:{money} 提出前:{before_money} 提出後:{after_money}'
    
    # 財務管理 -> 優惠規則 -> 上分優惠
    @DecorateClass('PFREQ-T1811')
    def delete_offer(self):
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_deposit_offer().delete_offer(admin_certification, self.admin_url)
    
    # 財務管理 -> 上分管理 -> 人工存入
    @DecorateClass('PFREQ-T1868')
    def test_manual_deposit(self):
        money = '100000'
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_manual_deposit().add_manual_deposit(self.web_account, admin_certification, self.admin_url, money)
        self.functions.ui_admin_manual_deposit().check_manual_deposit(self.web_account, admin_certification, self.admin_url)
    
    # 报表管理 -> 一般报表
    @DecorateClass('PFREQ-T6734')
    def test_general_report(self):
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_general_report().check_general_report(self.shareholder, 'payout', admin_certification, self.admin_url)

    # 報表管理 -> 頻道報表
    @DecorateClass('PFREQ-T6735')
    def test_channel_report(self):
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_channel_report().check_channel_report(self.shareholder, 'payout', admin_certification, self.admin_url)

    # 報表管理 -> 每日報表
    @DecorateClass('PFREQ-T6736')
    def test_daily_report(self):
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_daily_report().check_daily_order(self.shareholder, 'payout', admin_certification, self.admin_url)
        self.functions.ui_admin_daily_report().check_daily_overview(self.shareholder, admin_certification, self.admin_url)

    # 初始化設定
    def test_initialize_settings(self):
        res, admin_certification= self.test_admin_login()
        self.functions.ui_admin_system_list().initialize_all_settings(admin_certification, self.admin_url, self.brand, self.env, self.reseller_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)
        self.functions.ui_admin_deposit_offer().delete_offer(admin_certification, self.admin_url)
        self.functions.ui_admin_deposit_limit().set_deposit_limit_api(admin_certification, self.admin_url)
        self.functions.ui_admin_member_list().initialize_agent(self.web_account, self.reseller_account ,admin_certification, self.admin_url, self.admin_otp)

    # 產彩票下注資料(預防報表無資料錯誤)
    def test_lottery_bet_order(self):
        lottery_games = {
            'smam6': {'play_type': '特码-五行', 'bet_count': 1},
            'jspk10': {'play_type': '冠军', 'bet_count': 1},
            'jsssc': {'play_type': '任选一 - 前三', 'bet_count': 1},
            'jisu11x5': {'play_type': '任选四', 'bet_count': 4},
            'jisuk3': {'play_type': '两面', 'bet_count': 1},
            'hk': {'play_type': '特码-号码', 'bet_count': 1},
            'fc3d': {'play_type': '三星组选三', 'bet_count': 2},
            'fcxy28': {'play_type': '色波', 'bet_count': 1},
        }
        # web
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        for game, game_info in lottery_games.items():
            handicap_info = self.functions.ui_web_third_party().get_handicap_info(game, web_certification, self.web_url)
            res = self.functions.ui_web_third_party().lottery_order(game, handicap_info, game_info['play_type'], game_info['bet_count'], self.env, web_certification, self.web_url)

    # 營銷中心 -> 介面管理 -> 浮窗管理(初始化設定)
    def test_initialize_floating(self):
        # 登入Admin
        res, admin_certification= self.test_admin_login()
        # get left_float_page info
        left_info_dict = self.functions.ui_admin_float_window().get_float_window_num(admin_certification, self.admin_url, pos=1)
        # put left_float_page init
        self.functions.ui_admin_float_window().float_window_init(admin_certification, self.admin_url, left_info_dict, pos=1)
        right_info_dict = self.functions.ui_admin_float_window().get_float_window_num(admin_certification, self.admin_url, pos=2)
        self.functions.ui_admin_float_window().float_window_init(admin_certification, self.admin_url, right_info_dict, pos=2)

    # 財務管理 -> 上下分设定 -> 上分连点限制(關閉連點限制)
    def deposit_limit_close(self):
        res, admin_certification = self.test_admin_login()
        self.functions.ui_admin_deposit_limit().set_deposit_limit_api(admin_certification, self.admin_url)
    
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method