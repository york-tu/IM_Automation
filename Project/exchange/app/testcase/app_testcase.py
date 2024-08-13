import datetime, re
import sys, os
import unittest, random
import logging
from airtest.core.api import *

dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dir_name)

import common.utils.globalvar as gl
import stf_api.stf as stf
import driver.app_driver as app_dr
import driver.web_driver as web_dr
from common.app.decorator import DecorateClass
from Project.exchange.app.testcase.base_testcase import BaseTestCase
from Project.exchange.app.pages.pages import WebPages, AppPages, AdminPage, AdminEPage
from Project.lottery.app.testcase.base_testcase import BaseTestCase as BaseTestCase_Web
from Project.exchange.apis.function_layer.functions import Functions
from Project.lottery.apis.function_layer.functions import Functions as Brand_fucntion
from Project.exchange.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
from Project.lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API_Web
from Project.lottery.web.Utils_folder.screenshot import ScreenShot


class AppTestCase(BaseTestCase, BaseFunction_API_Web):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    money = '300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []

    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        gl.set_value('version', True)
        cls.setting_test_data(cls)  # 設定測試數據
        poco, wda_service = app_dr.AppDriver.airtest_connect_phone(cls)  # 連線測試手機
        cls.setting_browser()

        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))
        cls.brand_fucntion = Brand_fucntion(cls.skipTest)
        cls.folderpath = gl.get_value('FOLDER_PATH')

    def setUp(self):
        if gl.get_value('version') == False:
            raise EOFError('版本錯誤, 請檢查')

        # if gl.get_value('RESULT') == True:
        #     self.function_dict['ap'].webPage().basePage().skip_test(gl.get_value('MESSAGE'))
        self.functions = Functions()
        self.test_choose_app()

        self.start_time = time.time()

    def tearDown(self):
        try:
            image_path = f"{self.folderpath}/{self._testMethodName}.png"
            image_path_list = [image_path]
            snapshot(filename=image_path, msg=f"{self.id()}")
            stop_app(self.package)
            self.check_result(str(self.id()).split('.')[-1])

            image_name = self.id().split('.')[-1]
            for driver in self.driver_list:
                image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
                image_path_list.append(image_path)

            gl.set_value('IMG_PATH', image_path_list)
        except Exception as e:
            if 'No available screen capture method found' in str(e):
                pass
            else:
                raise e
        for driver in self.driver_list:
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

        # self.test_all_windows_max()

        # self.check_result(str(self.id()).split('.')[-1])
        # image_name = self.id().split('.')[-1]
        # image_path_list = []
        # for driver in self.driver_list:
        #     image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
        #     image_path_list.append(image_path)

        # gl.set_value('IMG_PATH', image_path_list)

    @classmethod
    def tearDownClass(cls):
        num = 0
        for key, function in cls.function_dict.items():
            if key != 'ap':
                if key == 'wp':
                    function.webPage().basePage().quit_browser()
                elif key == 'ad':
                    function.adminPage().basePage().quit_browser()
                elif key == 'ade':
                    function.commonPage().quit_browser()

            if num == len(cls.driver_list):
                cls.driver_list = []
                break
        else:
            stop_app(cls.package)

        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].webPage().basePage().hide_windows()
        cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
        cls.function_dict['ade'] = AdminEPage(cls.driver_list[-1], cls.wait_time, cls.admin_url_zqb,
                                              cls.skipTest)  # 導入exchage全部頁面
        cls.function_dict['ade'].commonPage().hide_windows()

        if not sys.argv[0].__contains__('prod'):  # Prod 不帶入admin config
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPage(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].adminPage().basePage().hide_windows()

    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key == 'wp':
                    function.webPage().basePage().hide_windows()
                elif key == 'ap':
                    function.adminPage().basePage().hide_windows()
                elif key == 'ade':
                    function.commonPage().hide_windows()

    def test_all_windows_max(self):
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key == 'wp':
                    function.webPage().basePage().hide_windows()
                elif key == 'ap':
                    function.adminPage().basePage().hide_windows()
                elif key == 'ade':
                    function.commonPage().hide_windows()

    def test_choose_app(self):
        # 選APP
        self.function_dict['ap'].commonPage().find_app(self.package)
        self.function_dict['ap'].mainPage().check_open_app(self._login_status[0])
        self.test_skip_pop()

    @DecorateClass('ZQB-T2276')
    # 登入
    def test_login(self):
        self.function_dict['ap'].mainPage().login(self.app_account, self.app_password)

    @DecorateClass('ZQB-T2277')
    # 登出
    def test_logout(self):
        self.function_dict['ap'].mainPage().logout()

    @DecorateClass('ZQB-T2263')
    # 登入頁檢查版本
    def test_check_version(self):
        self.test_logout()
        self.function_dict['ap'].mainPage().check_version(gl.get_value('APP_VERSION'))

    @DecorateClass('ZQB-T2295')
    # 註冊
    def test_register(self):
        # self.test_logout()
        phone_number = str(135) + str(random.randrange(10000000, 99999999))
        self.function_dict['ap'].mainPage().into_register()
        self.function_dict['ap'].registerPage().register(phone_number, "ps43941122", None, '123456')

    @DecorateClass('ZQB-T2282')
    # 完成"我要買"教程
    def test_buy_tutorial(self):
        self.test_login()
        self.function_dict['ap'].mainPage().buy_click(first=True)
        self.function_dict['ap'].mainPage().finish_new_change_transaction_instructions(first=True)

    @DecorateClass('ZQB-T5670')
    # 完成"我要賣"教程
    def test_sell_tutorial(self):
        self.test_login()
        self.function_dict['ap'].mainPage().sell_click(first=True)
        self.function_dict['ap'].mainPage().finish_open_and_close_market_tutorial(first=True)

    @DecorateClass('ZQB-T2283')
    # 完成"充值"教程
    def test_deposit_tutorial(self):
        self.test_login()
        self.function_dict['ap'].mainPage().deposit_click()
        self.function_dict['ap'].depositPage().finish_deposit_tutorial(True)

    @DecorateClass('ZQB-T2293')
    # 客服
    def test_customer_service(self):
        self.test_login()
        self.function_dict['ap'].mainPage().service_click()
        self.function_dict['ap'].customerservicePage().check_customer_service()

    @DecorateClass('ZQB-T2279')
    # 搶單流程  #未對品牌收銀台進行上傳截圖動作
    def test_grap_order_account(self):
        money = (random.randint(100, 500))

        self.test_login()
        # 拿取交易前的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_before = self.total_amount(web_certification, self.web_url)
        exchange_wallet_before = self.function_dict['ap'].mainPage().get_current_money()

        self.test_web_login()  # web登入

        self.function_dict['wp'].webPage().menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].webPage().memberPage().check_onlinepay('线上支付', '线上支付',
                                                                        'K币_支付宝转帐')  # 確認存款類型有生成
        self.function_dict['wp'].webPage().memberPage().do_all_exchange_deposit(money, 'K币_支付宝转帐')
        # order = self.function_dict['wp'].webPage().paybox_page().get_info(money)  # 抓取pay box資訊
        bonus_money, bonus_rate = self.function_dict['ap'].graporderPage().grap_order(money, '支付宝转帐')
        self.function_dict['wp'].webPage().paybox_page().get_info(money)
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        name = self.function_dict['ap'].myinfoPage().get_user_name()
        self.function_dict['wp'].webPage().paybox_page().check_order(name)
        self.function_dict['ap'].mainPage().back_click()
        self.function_dict['ap'].myPage().into_my_order_page()
        self.function_dict['ap'].myorderPage().choose_order_first(name, money)
        self.function_dict['ap'].myorderPage().check_grap_order(money, '支付宝转账', bonus_money, bonus_rate)
        self.function_dict['ap'].mainPage().back_click()

        # 拿取交易後的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_after = self.total_amount(web_certification, self.web_url)
        exchange_wallet_after = self.function_dict['ap'].mainPage().get_current_money()

        assert (platform_wallet_before + money) == platform_wallet_after, f'平台金額不正確 交易前:{platform_wallet_before} 交易金額:{money} 交易後:{platform_wallet_after}'
        assert float(exchange_wallet_before) - float(money) + float(bonus_money) == float(
            exchange_wallet_after), f'交易平台積分不正確 交易前:{exchange_wallet_before} 交易金額:{money} 交易紅利:{bonus_money} 交易後:{exchange_wallet_after}'

    @DecorateClass('ZQB-T2297')
    # 搶單流程  #未對品牌收銀台進行上傳截圖動作
    def test_grap_order_qrcode(self):
        self.test_login()

        # 拿取交易前的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_before = self.total_amount(web_certification, self.web_url)
        exchange_wallet_before = self.function_dict['ap'].mainPage().get_current_money()

        self.test_web_login()  # web登入

        self.function_dict['wp'].webPage().menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].webPage().memberPage().check_onlinepay('线上支付', '线上支付',
                                                                        'K币_微信扫码')  # 確認存款類型有生成
        money = self.function_dict['wp'].webPage().memberPage().do_all_exchange_deposit_qrcode(
            'K币_微信扫码')  # return int money
        # order = self.function_dict['wp'].webPage().paybox_page().get_info(money)  # 抓取pay box資訊

        bonus_money, bonus_rate = self.function_dict['ap'].graporderPage().grap_order(money, '微信扫码')
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        name = self.function_dict['ap'].myinfoPage().get_user_name()
        self.function_dict['ap'].mainPage().back_click()
        self.function_dict['ap'].myPage().into_my_order_page()
        self.function_dict['wp'].webPage().paybox_page().check_qrcode_show()
        self.function_dict['wp'].webPage().basePage().switch_home_page()
        self.function_dict['ap'].myorderPage().choose_order_first(name, money)
        self.function_dict['ap'].myorderPage().check_grap_order(money, '微信扫码', bonus_money, bonus_rate)
        self.function_dict['ap'].mainPage().back_click()

        # 拿取交易後的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_after = self.total_amount(web_certification, self.web_url)
        exchange_wallet_after = self.function_dict['ap'].mainPage().get_current_money()

        assert (
                           platform_wallet_before + money) == platform_wallet_after, f'平台金額不正確 交易前:{platform_wallet_before} 交易金額:{money} 交易後:{platform_wallet_after}'
        assert float(exchange_wallet_before) - float(money) + float(bonus_money) == float(
            exchange_wallet_after), f'交易平台積分不正確 交易前:{exchange_wallet_before} 交易金額:{money} 交易紅利:{bonus_money} 交易後:{exchange_wallet_after}'

    @DecorateClass('ZQB-T2280')
    # 品牌出款我要買流程
    def test_want_buy(self):
        money = random.randint(100, 200)  # 品牌申請出款金額
        self.test_login()

        # 拿取交易前的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_before = self.total_amount(web_certification, self.web_url)
        exchange_wallet_before = self.function_dict['ap'].mainPage().get_current_money()
        # 線上取款
        withdraw_money, real_withdraw = self.brand_fucntion.ui_web_my_wallet().online_withdraw(web_certification,
                                                                                               self.web_url, money)
        # 品牌後台
        self.test_admin_login()
        self.function_dict['ad'].adminPage().financialmanagementPage().into_withdraw()  # 進入出款申请
        self.function_dict['ad'].adminPage().withdrawPage().search_today_withdraw_by_member(
            self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].adminPage().withdrawPage().pass_first_online_withdraw(self.web_account,
                                                                                       '順付我要買出款')  # 確認最新一筆申請
        # 順付app
        self.function_dict['ap'].mainPage().buy_click()
        bonus_money = self.function_dict['ap'].wantbuyPage().get_order(real_withdraw)

        # =================================================================
        # 品牌拔掉玩家自行確認收款的按鈕，故暫時隱藏
        # # web登入
        # self.test_web_login() 
        # self.function_dict['wp'].webPage().menuPage().into_menu_member_wallet()
        # self.function_dict['wp'].webPage().withdraw_record_page().exchange_submit()
        # =================================================================

        # 至順付後台協助確認款項
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_brand_order_record()
        self.function_dict['ade'].orderrecordbrandPage().brand_order_transfer_confirm()

        # 拿取交易後的平台錢包及well pay積分
        res, web_certification = self.do_web_login(self.web_account, self.web_password, self.web_url)
        platform_wallet_after = self.total_amount(web_certification, self.web_url)
        # 順付app
        self.function_dict['ap'].mainPage().hall_click()
        for i in range(3):
            self.sleep(1)
            exchange_wallet_after = self.function_dict['ap'].mainPage().get_current_money()
            if exchange_wallet_after == exchange_wallet_before:
                self.function_dict['ap'].mainPage().my_click()
                self.function_dict['ap'].mainPage().hall_click()
            else:
                break
        assert platform_wallet_before - withdraw_money == platform_wallet_after, f'品牌平台金額不正確 交易前:{platform_wallet_before} 交易金額:{withdraw_money} 交易後:{platform_wallet_after}'
        assert f'{(exchange_wallet_before + real_withdraw + bonus_money):.2f}' == f'{exchange_wallet_after:.2f}', f'交易平台積分不正確 交易前:{exchange_wallet_before} 交易金額:{real_withdraw} 交易紅利:{bonus_money} 交易後:{exchange_wallet_after}'

    @DecorateClass('ZQB-T2281')
    # 順付我要賣掛單並購買流程
    def test_want_sell(self):
        money = random.randint(100, 200)
        # 賣方我要賣
        self.test_login()
        exchange_wallet_before_sell = self.function_dict['ap'].mainPage().get_current_money()
        self.function_dict['ap'].mainPage().sell_click()
        total_money, bonus_rate = self.function_dict['ap'].wantsellPage().sell_order(money)
        self.function_dict['ap'].mainPage().hall_click()
        exchange_wallet_after_sell = self.function_dict['ap'].mainPage().get_current_money()
        self.test_logout()

        # 買方我要買
        self.function_dict['ap'].mainPage().login('13500000005', '11111111')
        self.function_dict['ap'].mainPage().hall_click()
        exchange_wallet_before_buy = self.function_dict['ap'].mainPage().get_current_money()
        self.function_dict['ap'].mainPage().buy_click()

        self.function_dict['ap'].wantbuyPage().buyer_contact_seller('13500000005', '11111111', self.app_account,
                                                                    self.app_password, money)

        bonus_money = self.function_dict['ap'].wantbuyPage().upload_photo_complete_order(total_money)
        self.function_dict['ap'].mainPage().hall_click()
        assert exchange_wallet_before_buy == self.function_dict['ap'].mainPage().get_current_money(), "我要買未完成訂單前，積分有誤"
        self.test_logout()

        # 賣方確認訂單
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_my_sell_page()
        self.function_dict['ap'].mysellPage().confirm_order(total_money)
        self.function_dict['ap'].mainPage().back_click()
        self.test_logout()

        # 買方確認訂單
        self.function_dict['ap'].mainPage().login('13500000005', '11111111')
        self.function_dict['ap'].mainPage().hall_click()
        exchange_wallet_after_buy = self.function_dict['ap'].mainPage().get_current_money()

        assert exchange_wallet_before_sell - money == exchange_wallet_after_sell, f'我要賣角色 交易前:{exchange_wallet_before_sell} 交易金額:{money} 交易後:{exchange_wallet_after_sell}'
        assert float(exchange_wallet_before_buy) + float(total_money) + float(bonus_money) == float(
            exchange_wallet_after_buy), f'我要買角色 交易前:{exchange_wallet_before_buy} 購買總販售金額:{total_money} 交易紅利:{bonus_money} 交易後:{exchange_wallet_after_buy}'
        self.function_dict['ap'].mainPage().back_click()
        self.test_logout()

    @DecorateClass('ZQB-T2278')
    # 充值
    def test_deposit(self):
        money = random.randint(500, 1000)  # 充值金額
        self.test_login()
        # self.function_dict['wp'].commonPage().open_base_url()
        self.function_dict['ad'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        wallet_before = self.function_dict['ap'].mainPage().get_current_money()
        self.function_dict['ap'].mainPage().deposit_click()
        self.function_dict['ap'].depositPage().finish_deposit_tutorial()
        bonus = self.function_dict['ap'].depositPage().deposit(money)
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_recharge_audit_management()
        self.function_dict['ade'].rechargeauditPage().recharge_audit_confirm()
        self.function_dict['ap'].mainPage().check_money_correct(wallet_before, bonus, money)

    #### 關閉搶單到期與訂單確認彈窗
    def test_skip_pop(self):
        self.function_dict['ap'].mainPage().skip_order_expire()
        self.function_dict['ap'].wantbuyPage().skip_order_confirm()

    @DecorateClass('ZQB-T2284')
    # 綁定收付款方式 > 新增銀行轉帳 > 刪除銀行轉帳
    def test_add_and_delete_bank_transfer(self):
        bank = '中国农业银行'
        self.test_login()
        self.function_dict['ap'].mainPage().bind_payment_click()
        self.function_dict['ap'].bindpaymentPage().click_account_tab()
        bank_card = self.function_dict['ap'].bindpaymentPage().add_bank_transfer(self.withdraw_password, bank)
        self.function_dict['ap'].bindpaymentPage().delete_recent_add_bank_transfer(self.withdraw_password, bank_card)

    @DecorateClass('ZQB-T2285')
    # 綁定收付款方式_新增微信轉帳
    def test_add_wechat_transfer(self):
        self.test_login()
        wechat_number = str(random.randrange(10000000000, 99999999999))
        self.function_dict['ap'].mainPage().bind_payment_click()
        self.function_dict['ap'].bindpaymentPage().click_account_tab()
        self.function_dict['ap'].bindpaymentPage().add_wechat_transfer(self.withdraw_password, wechat_number)

    @DecorateClass('ZQB-T2286')
    # 綁定收付款方式_新增支付寶轉帳
    def test_add_alipay_transfer(self):
        self.test_login()
        alipay_number = str(random.randrange(10000000000, 99999999999))
        self.function_dict['ap'].mainPage().bind_payment_click()
        self.function_dict['ap'].bindpaymentPage().click_account_tab()
        self.function_dict['ap'].bindpaymentPage().add_alipay_transfer(self.withdraw_password, alipay_number)
        self.function_dict['ap'].bindpaymentPage().delete_recent_add_alipay_transfer(self.withdraw_password,
                                                                                     alipay_number)

    # 綁定收付款方式_新增QQ轉帳
    def test_add_qq_transfer(self):
        qq_number = str(random.randrange(10000000000, 99999999999))
        self.function_dict['ap'].mainPage().bind_payment_click()
        self.function_dict['ap'].bindpaymentPage().click_account_tab()
        self.function_dict['ap'].bindpaymentPage().add_qq_transfer(self.withdraw_password, qq_number)

    def test_add_unionpay_transfer(self):
        unionpay_number = str(random.randrange(10000000000, 99999999999))
        self.function_dict['ap'].mainPage().bind_payment_click()
        self.function_dict['ap'].bindpaymentPage().click_account_tab()
        self.function_dict['ap'].bindpaymentPage().add_unionpay_transfer(self.withdraw_password, unionpay_number)

    @DecorateClass('ZQB-T2287')
    # 錢包地址入款
    def test_wallet_address_deposit(self):
        self.test_login()
        money = random.randint(100, 5000)  # 品牌出款金額
        self.function_dict['ap'].mainPage().login(self.app_account, self.app_password)
        # self.test_skip_pop()
        before_money_for_sale = self.function_dict['ap'].mainPage().get_current_money_for_sale()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        address = self.function_dict['ap'].myinfoPage().get_wallet_address()
        self.function_dict['ap'].mainPage().back_click()

        # 開啟品牌後台
        self.test_admin_login()
        phone = '13500' + str('%06d' % random.randint(0, 999999))
        self.function_dict['ad'].adminPage().membermanagementpage().into_member_list()  # 進入會員列表  
        self.function_dict['ad'].adminPage().MemberList().delete_virtual_wallet(self.web_account)  # 刪除顺付wellpay錢包
        self.function_dict['ad'].adminPage().membermanagementpage().into_member_list()  # 進入會員列表
        self.function_dict['ad'].adminPage().MemberList().change_member_phone(self.web_account, phone,
                                                                              self.admin_otp)  # 修改會員手機號碼

        # 開啟品牌前台
        self.test_web_login()
        wallet_before = self.function_dict['wp'].webPage().menuPage().get_balance_wallet()
        self.function_dict['wp'].webPage().menuPage().into_menu_member_center()
        self.function_dict['wp'].webPage().memberPage().into_L_MenuMyProfile()
        self.function_dict['wp'].webPage().memberPage().do_change_wellpay_wallet(self.withdraw_password,
                                                                                 wallet_address=address,
                                                                                 phone=phone)  # 設定顺付wellpay錢包
        self.function_dict['wp'].webPage().menuPage().into_menu_member_withdraw()  # 進入線上取款
        total_amount, real_money = self.function_dict['wp'].webPage().memberPage().do_wellpay_withdraw(money,
                                                                                                       self.withdraw_password)  # 顺付wellpay取款

        # 品牌後台
        self.test_admin_login()
        self.function_dict['ad'].adminPage().financialmanagementPage().into_withdraw()  # 進入出款申请
        self.function_dict['ad'].adminPage().withdrawPage().search_today_withdraw_by_member(
            self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].adminPage().withdrawPage().pass_first_online_withdraw(self.web_account,
                                                                                       '順付錢包出款')  # 確認最新一筆申請

        # 品牌後台 將錢包刪除，以免有單看不到
        self.function_dict['ad'].adminPage().membermanagementpage().into_member_list()  # 進入會員列表  
        self.function_dict['ad'].adminPage().MemberList().delete_virtual_wallet(self.web_account)  # 刪除顺付wellpay錢包

        # 確認金額
        self.function_dict['ap'].mainPage().hall_click()
        self.function_dict['ap'].mainPage().check_money_for_sale_correct(before_money_for_sale,
                                                                         real_money)  # 確認交易所可用販售積分
        self.test_web_login()
        self.function_dict['wp'].webPage().menuPage().into_menu_member_wallet()  # 進入額度轉換
        self.function_dict['wp'].webPage().memberPage().after_check_money_output_record(total_amount,
                                                                                        wallet_before)  # 進入出款紀錄比對

    @DecorateClass('ZQB-T2288')
    # 收支明細
    def test_pay_info(self):
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_pay_info_page()
        self.function_dict['ap'].payinfoPage().pay_sort()

    @DecorateClass('ZQB-T2289')
    # 充值紀錄
    def test_deposit_record_info(self):
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_deposit_record_page()
        self.function_dict['ap'].depositrecordPage().deposit_sort()

    @DecorateClass('ZQB-T2290')
    # 會員資料
    def test_member_data(self):
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        member_number = self.function_dict['ap'].myPage().get_member_number()
        self.function_dict['ap'].myPage().into_member_data_page()
        app_member_info = self.function_dict['ap'].myinfoPage().get_all_info()
        # 至順付後台會員列表
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_member_list()
        member_info = self.function_dict['ade'].memberlistPage().get_member_info(member_number)
        # 比對資料
        assert app_member_info['phone'][-4:] in member_info[
            'phone'], f"手機號顯示有誤, app顯示:{app_member_info['phone']}, admin顯示:{member_info['phone']}"
        assert (app_member_info['qq'][:1] == member_info['qq'][:1] and app_member_info['qq'][-4:] == member_info['qq'][
                                                                                                     -4:]), f"QQ帳號顯示有誤, app顯示:{app_member_info['qq']}, admin顯示:{member_info['qq']}"
        assert app_member_info['name'] == member_info[
            'name'], f"姓名顯示有誤{app_member_info['name']}, admin顯示:{member_info['name']}"
        assert app_member_info['address'] == member_info[
            'address'], f"錢包地址顯示有誤{app_member_info['address']}, admin顯示:{member_info['address']}"

    @DecorateClass('ZQB-T2291')
    # 會員資料_修改登入密碼
    def test_change_password(self):
        old_ps = self.app_password
        new_ps = 'test32678'
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        self.function_dict['ap'].myinfoPage().change_login_password(old_ps, new_ps, self.withdraw_password)
        self.function_dict['ap'].mainPage().back_click()
        self.test_logout()
        self.function_dict['ap'].mainPage().login(self.app_account, new_ps)
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        self.function_dict['ap'].myinfoPage().change_login_password(new_ps, old_ps, self.withdraw_password)
        self.function_dict['ap'].mainPage().back_click()
        self.test_logout()
        self.function_dict['ap'].mainPage().login(self.app_account, old_ps)

    @DecorateClass('ZQB-T5671')
    # 會員資料_修改安全密碼 >>> 修改後可正常用於修改登入帳密
    def test_change_pay_password(self):
        old_pay_ps = self.withdraw_password
        new_pay_ps = '22222222'
        old_ps = self.app_password
        new_ps = 'test32678'
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        self.function_dict['ap'].myinfoPage().change_pay_password(old_pay_ps, new_pay_ps)  # 更改安全密碼
        self.function_dict['ap'].myinfoPage().change_login_password(old_ps, new_ps, new_pay_ps)  # 確認輸入新安全密碼可更改帳號密碼
        self.function_dict['ap'].myinfoPage().change_pay_password(new_pay_ps, old_pay_ps)  # 改回舊安全密碼
        self.function_dict['ap'].myinfoPage().change_login_password(new_ps, old_ps, old_pay_ps)  # 確認輸入安全密碼可更改帳號密碼
        self.function_dict['ap'].mainPage().back_click()

    @DecorateClass('ZQB-T2292')
    # 會員資料_版本更新 (後續需要更新case內容:2024/07/08)
    def test_version_update(self):
        self.test_login()
        self.function_dict['ap'].mainPage().my_click()
        self.function_dict['ap'].myPage().into_member_data_page()
        self.function_dict['ap'].myinfoPage().version_update()
        self.test_check_version()

    # ================================= 順付ADMIN =================================
    def test_initialize_member_password(self):
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_member_list()
        member_info = self.function_dict['ade'].memberlistPage().change_member_password(self.app_number)

    def test_initialize_system_management(self):
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_site_management()
        self.function_dict['ade'].systemmanagementPage().initialize_swipeverify_setting()
        self.function_dict['ade'].systemmanagementPage().initialize_smsverify_setting()

    @DecorateClass('ZQB-T2472')
    #### 我要賣全部訂單_下架
    def test_take_off_sale_order(self):
        money = random.randint(100, 200)
        # 賣方我要賣
        self.test_login()
        exchange_wallet_before_sell = self.function_dict['ap'].mainPage().get_current_money()
        self.function_dict['ap'].mainPage().sell_click()
        total_money, bonus_rate = self.function_dict['ap'].wantsellPage().sell_order(money)
        self.function_dict['ap'].mainPage().hall_click()
        exchange_wallet_after_sell = self.function_dict['ap'].mainPage().get_current_money()
        assert (exchange_wallet_before_sell - money) == exchange_wallet_after_sell, f'掛單後可用積分有誤，掛單前:{exchange_wallet_before_sell}，掛單金額:{money}，掛單後:{exchange_wallet_after_sell}，應為{(exchange_wallet_before_sell - money)}'

        # admin
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_sale_all_order()
        self.function_dict['ade'].allrecordzqbPage().check_order_data(member_id=self.app_number, app_brand=self.brand,
                                                                      money=total_money, bonus_rate=bonus_rate,
                                                                      sell_status='1', sell_type='0')
        self.function_dict['ade'].allrecordzqbPage().cancel_sell_order(self.app_number)
        self.function_dict['ade'].allrecordzqbPage().check_order_data(member_id=self.app_number, app_brand=self.brand,
                                                                      money=total_money, bonus_rate=bonus_rate,
                                                                      sell_status='0', sell_type='0')
        self.function_dict['ap'].mainPage().sell_click()
        self.function_dict['ap'].mainPage().hall_click()
        exchange_wallet_after_cancel = self.function_dict['ap'].mainPage().get_current_money()
        assert exchange_wallet_after_cancel == exchange_wallet_before_sell, f'後台下架後可用積分有誤，下架前:{exchange_wallet_after_sell}，掛單金額:{money}，下架後:{exchange_wallet_after_cancel}，應為{exchange_wallet_before_sell}'
        # 可再加上收支明細檢查

    @DecorateClass('ZQB-T2472')
    #### 我要賣全部訂單
    def test_sell_all_record_page(self):
        sell_data_list = []
        # 我要賣掛單
        for i in range(2):
            money = random.randint(100, 200)
            self.test_login()
            self.function_dict['ap'].mainPage().sell_click()
            total_money, bonus_rate = self.function_dict['ap'].wantsellPage().sell_order(money)
            self.function_dict['ap'].mainPage().hall_click()
            order_data = {'money': total_money, 'bonus_rate': bonus_rate}
            sell_data_list.append(order_data)

        # admin
        self.function_dict['ade'].commonPage().open_base_url()
        self.function_dict['ade'].commonPage().windows_to_top()
        self.function_dict['ade'].loginPage().login_click(self.admin_id_zqb, self.admin_pwd_zqb)
        self.function_dict['ade'].menuPage().into_sale_all_order()
        # 檢查搜尋
        # self.function_dict['ade'].allrecordzqbPage().check_order_data(member_id=self.app_number,
        #                                                                      app_brand=self.brand,
        #                                                                      money_data=sell_data_list[-1])

    # ================================= 品牌WEB =================================
    # 測試品牌Web登入
    def test_web_login(self, flag=True):
        self.test_all_windows_mini()
        self.function_dict['wp'].webPage().basePage().windows_to_top()  # 切換視窗
        self.function_dict['wp'].webPage().basePage().open_base_url()  # 開啟前台網站
        self.sleep(2)
        self.function_dict['wp'].webPage().memberPage().refresh_browser()  # 關閉一般公告
        self.function_dict['wp'].webPage().memberPage().refresh_browser()  # 關閉一般公告
        captcha_status = self.function_dict['wp'].webPage().mainPage().login(self.web_account, self.web_password,
                                                                             self.web_captcha)  # 登入
        if captcha_status == False:
            res, certification = self.function_dict['wp'].webPage().apibasefunction().do_web_login(self.web_account,
                                                                                                   self.web_password,
                                                                                                   self.web_url)  # 有滑動驗證時用api登入
            self.function_dict['wp'].webPage().mainPage().add_cookie_driver(res)  # 把cookie加進driver
            self.function_dict['wp'].webPage().memberPage().refresh_browser()

        self.function_dict['wp'].webPage().basePage().close_exchange_message()  # 關閉順付通知
        self.function_dict['wp'].webPage().basePage().close_change_pwd()  # 關閉密碼更換彈窗

        if flag == True:
            self.function_dict['wp'].webPage().mainPage().close_login_board()  # 關閉登入公告

    # ================================= 品牌ADMIN =================================
    # 測試品牌ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].adminPage().basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].adminPage().basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].adminPage().loginPage().login(self.admin_account, self.admin_password,
                                                               self.admin_otp)  # 登入admin

    # =============================================================================
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method
