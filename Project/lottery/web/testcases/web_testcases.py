import unittest, sys, os, datetime, random, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.lottery.web.pages.pages import WebPages, AdminPage, MobilePage
from Project.lottery.web.testcases.base_testcase import BaseTestCase
from Project.lottery.web.pages.webs.web.webs_basepage import BasePage as BasePage_Web
from Project.lottery.web.pages.admin.admin_basepage import BasePage as BasePageAdmin
from Project.lottery.web.pages.webs.mobile.mobile_basepage import BasePage as BasePage_Mobile
from Project.lottery.web.Utils_folder.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass

class WebTestCases(BaseTestCase, BasePage_Web, BasePageAdmin):
    # Chrome Setting
    wait_time =20
    implicitly_wait_time = 35
    money='300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []
    brand = gl.get_value('BRAND')
    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folderpath = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        
    @classmethod
    def setUp(cls):
        for key, function in cls.function_dict.items():
            try:
                function.basePage().accept_alert()
                function.basePage().dismiss_alert()
            except:
                pass
            
            function.basePage().switch_home_page()
            if key == 'wp':
                cls.open_url(cls, function, cls.web_url)
                function.mainPage().maintenance()

        cls.test_all_windows_mini(cls)
        cls.function_dict['wp'].basePage().windows_to_top() # 切換視窗

    def tearDown(self):
        self.test_all_windows_max()
        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

    @classmethod
    def tearDownClass(cls):
        num = 0
        for function in cls.function_dict.values():
            function.basePage().quit_browser()
            num+=1

            if num == len(cls.driver_list):
                cls.driver_list = []
                break
     
    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].basePage().hide_windows()

        if not sys.argv[0].__contains__('prod'): # Prod 不帶入admin config
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPage(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].basePage().hide_windows()

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass
        
        function.basePage().open_browser(url)

    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top()

    # 檢查關於我們
    @DecorateClass('PFREQ-T2052')
    def test_about_us_help(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.function_dict['wp'].registerPage().about_us()
         
    # 檢查聯繫我們
    @DecorateClass('PFREQ-T2053')
    def test_contains_us_help(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.function_dict['wp'].registerPage().contains_us()

    # 檢查代理註冊
    @DecorateClass('PFREQ-T2054')
    def test_partners_help(self):
        if self.brand == 'co':
            pass
        else:
            self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
            self.function_dict['wp'].mainPage().refresh_browser()
            self.function_dict['wp'].mainPage().into_register_page()
            self.function_dict['wp'].registerPage().partners()

    # 檢查存款幫助
    @DecorateClass('PFREQ-T2055')
    def test_deposit_help(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.function_dict['wp'].registerPage().deposit()

    # 檢查取款幫助
    @DecorateClass('PFREQ-T2056')
    def test_withdraw_help(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.function_dict['wp'].registerPage().withdraw()

    # 檢查常見問題
    @DecorateClass('PFREQ-T2057')
    def test_questions_help(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.function_dict['wp'].registerPage().questions()

    # 測試-註冊後登出
    @DecorateClass('PFREQ-T1800')
    def test_register_logout(self):
        number = '13' + str(random.randrange(100000000, 999999999, 9))

        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['wp'].registerPage().do_register(self.bot_id, 'ps123456', self.brand, '111111', number)
        self.function_dict['wp'].mainPage().close_login_board()
        self.function_dict['wp'].mainPage().do_force_logout()
        self.function_dict['wp'].mainPage().logout_checker()

    # 測試-註冊
    def test_register(self):
        self.function_dict['wp'].mainPage().refresh_browser()
        self.function_dict['wp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['wp'].registerPage().do_register(self.bot_id, '123456', self.brand, '111111')
        self.function_dict['wp'].mainPage().close_login_board()

    # 測試ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin

    # 測試-登入
    @DecorateClass('PFREQ-T1844')
    def test_web_login(self, flag=True):
        self.test_all_windows_mini()
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].memberPage().refresh_browser()  # 關閉一般公告
        captcha_status = self.function_dict['wp'].mainPage().login(self.web_account, self.web_password, self.web_captcha)  # 登入
        if captcha_status == False:
            res, certification = self.function_dict['wp'].apibasefunction().do_web_login(self.web_account, self.web_password, self.web_url)  # 有滑動驗證時用api登入
            self.function_dict['wp'].mainPage().add_cookie_driver(res)  # 把cookie加進driver
            self.function_dict['wp'].memberPage().refresh_browser()
        self.function_dict['wp'].basePage().close_change_pwd()  # 關閉密碼更換彈窗
        if flag == True:
            self.function_dict['wp'].mainPage().close_login_board()  # 關閉登入公告
        

    # 測試-登出
    @DecorateClass('PFREQ-T2050')
    def test_web_logout(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].memberPage().refresh_browser()  # 關閉一般公告
        self.function_dict['wp'].mainPage().logout()

    # 測試線上支付
    @DecorateClass('PFREQ-T1859')
    def test_desposit_onlinepay(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_onlinepay('线上支付', '线上支付','自動市_线上支付')  # 確認存款類型有生成
        self.function_dict['wp'].memberPage().do_all_online_deposit(self.money,'自動市_线上支付')
        self.function_dict['wp'].memberPage().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney, handlingMoney = self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
         # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        # 預期會因第三方建單失敗，故先將判斷隱藏
        # if deposit_result == True:
        #     self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '在线入款', handlingMoney) # 進入入款紀錄比對
        # else:
        #     self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        

    # 測試銀聯支付
    @DecorateClass('PFREQ-T1870')
    def test_desposit_unionpay(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_unionpay('银联支付', '银联支付','自動市_银联支付')  # 確認存款類型有生成
        self.function_dict['wp'].memberPage().do_all_online_deposit(self.money,'自動市_银联支付')
        self.function_dict['wp'].memberPage().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney, handlingMoney = self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
         # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        # 預期會因第三方建單失敗，故先將判斷隱藏
        self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        # if deposit_result == True:
        #     self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '在线入款', handlingMoney) # 進入入款紀錄比對
        # else:
        #     self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        

    # 測試京東支付
    @DecorateClass('PFREQ-T1872')
    def test_desposit_jdpay(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_jdpay('京东支付', '京东支付','自動市_京东支付')  # 確認存款類型有生成
        self.function_dict['wp'].memberPage().do_all_online_deposit(self.money,'自動市_京东支付')
        self.function_dict['wp'].memberPage().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney, handlingMoney = self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
         # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        # 預期會因第三方建單失敗，故先將判斷隱藏
        self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        # if deposit_result == True:
        #     self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '在线入款', handlingMoney) # 進入入款紀錄比對
        # else:
        #     self.function_dict['wp'].memberPage().check_money_entry_fail_record(traMoney, wallet_before, '在线入款') # 進入入款紀錄比對
        

    # 測試公司入款
    @DecorateClass('PFREQ-T1851')
    def test_company_deposit(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_company_deposit('公司入款', '銀行自動測試')  # 確認公司入帳有生成
        self.function_dict['wp'].memberPage().do_company_deposit('銀行自動測試', self.money)
        self.function_dict['wp'].memberPage().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money, offer_money, total_money = self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_record(tra_money, offer_money, total_money, wallet_before, '公司入款') # 進入入款紀錄比對


    # 測試支付寶面對面
    @DecorateClass('PFREQ-T1853')
    def test_desposit_alipay_f2f(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_qr_deposit('支付宝', 'bot', '支付宝面对面扫码', self.money)
        self.function_dict['wp'].memberPage().do_desposit_weChat_alipayf2f() # 支付寶/微信 面對面
        self.function_dict['wp'].memberPage().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney = self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney,wallet_before,'公司入款') # 進入入款紀錄比對

    # 測試微信面對面
    @DecorateClass('PFREQ-T1856')
    def test_desposit_wechat_f2f(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().check_qr_deposit('微信', 'bot', '微信面对面扫码', self.money)
        self.function_dict['wp'].memberPage().do_desposit_weChat_alipayf2f()
        self.function_dict['wp'].memberPage().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney = self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '公司入款') # 進入入款紀錄比對

    # 測試支付寶轉帳
    @DecorateClass('PFREQ-T1855')
    def test_desposit_alipay_transfer(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().checktr_deposit('支付宝', '支付寶轉帳自動測試', '支付宝转帐', self.money)
        self.function_dict['wp'].memberPage().do_desposit_wechat_alipay_transfer()
        self.function_dict['wp'].memberPage().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney = self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '公司入款') # 進入入款紀錄比對

    # 測試微信轉帳
    @DecorateClass('PFREQ-T1858')
    def test_desposit_wechat_transfer(self):
        # before test action
        self.test_web_login()
        # WEB
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_deposit()  # 進入線上存款
        self.function_dict['wp'].memberPage().checktr_deposit('微信', '微信轉帳自動測試', '微信转帐', self.money)
        real_money = self.function_dict['wp'].memberPage().get_real_money(self.money)
        self.function_dict['wp'].memberPage().do_desposit_wechat_alipay_transfer()
        self.function_dict['wp'].memberPage().before_check_money_entry_record('公司入款', real_money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        traMoney, offerMoney, totalMoney = self.function_dict['ad'].companyDepositPage().get_money_info(real_money)
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().check_money_entry_record(traMoney, offerMoney, totalMoney, wallet_before, '公司入款') # 進入入款紀錄比對

    # 測試線上出款
    @DecorateClass('PFREQ-T1901')
    def test_withdraw(self):
        # ADMIN
        self.test_admin_login()   
        self.function_dict['ad'].membermanagementpage().into_member_list()  # 進入會員列表  
        self.function_dict['ad'].MemberList().delete_bank_cards(self.web_account)  # 刪除所有銀行卡
        # WEB
        self.test_web_login()
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        self.function_dict['wp'].memberPage().do_change_bankCard('台灣', '台北', self.withdraw_password) #設定銀行卡號
        self.test_web_login()
        self.function_dict['wp'].menuPage().into_menu_member_withdraw()  # 進入線上取款
        total_amount, real_money = self.function_dict['wp'].memberPage().do_withdraw(self.withdraw, self.withdraw_password)  # 取款
        self.function_dict['wp'].memberPage().before_check_money_output_record('在线提现', self.money, real_money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申请
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().after_check_money_output_record(total_amount, wallet_before) # 進入入款紀錄比對


    # 測試線上出款_CGpay 
    @DecorateClass('PFREQ-T5972')
    def test_cgpay_withdraw(self):
        # ADMIN
        phone = '13500' + str('%06d' %random.randint(0,999999))     
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().change_member_phone(self.web_account, phone, self.admin_otp)  # 修改會員手機號碼
        self.function_dict['ad'].MemberList().delete_virtual_wallet(self.web_account)  # 刪除虛擬錢包
        
        # WEB
        self.test_web_login()
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        self.function_dict['wp'].memberPage().do_change_virtualcard(self.withdraw_password, phone)  # 設定虛擬錢包
        self.test_web_login()
        self.function_dict['wp'].menuPage().into_menu_member_withdraw()  # 進入線上取款
        total_amount, real_money = self.function_dict['wp'].memberPage().do_cgpay_withdraw(self.money, self.withdraw_password)  # CGpay取款
        self.function_dict['wp'].memberPage().before_check_money_output_record('在线提现', self.money, real_money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申请
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        # WEB
        self.test_web_login() # 登入前台
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().after_check_money_output_record(total_amount, wallet_before) # 進入出款紀錄比對


    # 測試額度轉換
    @DecorateClass('PFREQ-T1902')
    def test_wallet_conversion_return_local(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_wallet_return()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        self.function_dict['wp'].memberPage().do_wallet_check()

    @DecorateClass('PFREQ-T1903')
    def test_ag_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'ag']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1904')
    def test_mg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'mg']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1911')
    def test_sb_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'sb']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()
    
    @DecorateClass('PFREQ-T1916')
    def test_bbin_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'bbin']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1917')
    def test_dt_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'dt']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1943')
    def test_hg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'hg']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1918')
    def test_ky_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp', 'ky']

        for _ in range(0, 2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    def test_gc_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','gc']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1919')
    def test_fg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','fg']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1923')
    def test_gm_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','gm']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1924')
    def test_pt_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','pt']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1935')
    def test_lc_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','lc']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1938')
    def test_cq_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','cq']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1939')
    def test_vg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','vg']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1940')
    def test_sw_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','sw']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1941')
    def test_3s_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','ss']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T3069')
    def test_dg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','dg']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1942')
    def test_bs_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','bs']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()
    
    @DecorateClass('PFREQ-T1944')
    def test_kk_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','kk']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()
    
    @DecorateClass('PFREQ-T6979')
    def test_bg_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','bg']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T8202')
    def test_sp365_wallet_conversion(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()
        self.function_dict['wp'].memberPage().do_walletre_fresh()
        wallet_list = ['cp','sp365']

        for _ in range(0,2):
            money_before = self.function_dict['wp'].memberPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['wp'].memberPage().into_wallet_Report()
            self.function_dict['wp'].memberPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    # 測試選單功能正常
    @DecorateClass('PFREQ-T1987')
    def test_into_menu_index(self):
        self.function_dict['wp'].menuPage().into_menu_index()

    @DecorateClass('PFREQ-T2005')
    def test_into_menu_lottery(self):
        self.function_dict['wp'].menuPage().into_menu_lottery()

    @DecorateClass('PFREQ-T2007')
    def test_into_menu_game(self):
        self.function_dict['wp'].menuPage().into_menu_game()

    @DecorateClass('PFREQ-T2012')
    def test_into_menu_electronic(self):
        self.function_dict['wp'].menuPage().into_menu_electronic()

    @DecorateClass('PFREQ-T2013')
    def test_into_menu_casino(self):
        self.function_dict['wp'].menuPage().into_menu_casino()

    @DecorateClass('PFREQ-T2014')
    def test_into_menu_sport(self):
        self.function_dict['wp'].menuPage().into_menu_sport()

    @DecorateClass('PFREQ-T2015')
    def test_into_menu_fish(self):
        self.function_dict['wp'].menuPage().into_menu_fish()

    @DecorateClass('PFREQ-T2016')
    def test_into_menu_promo(self):
        self.function_dict['wp'].menuPage().into_menu_promo()
    
    @DecorateClass('PFREQ-T6420')
    def test_into_menu_service(self):
        self.function_dict['wp'].menuPage().into_menu_service()

    @DecorateClass('PFREQ-T2017')
    def test_into_menu_member_deposit(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_deposit()

    @DecorateClass('PFREQ-T2018')
    def test_into_menu_member_withdraw(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_withdraw()

    @DecorateClass('PFREQ-T2019')
    def test_into_menu_member_wallet(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_wallet()

    # 測試-會員資料修改
    @DecorateClass('PFREQ-T2044')
    def test_change_member_password(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        temp_pwd = 'Qa0123456'
        self.function_dict['wp'].memberPage().do_change_password(self.web_password, temp_pwd, self.withdraw_password)
        self.function_dict['wp'].memberPage().do_change_password(temp_pwd, self.web_password, self.withdraw_password)

    @DecorateClass('PFREQ-T2045')
    def test_change_member_security_password(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        temp_spwd = '666666'
        self.function_dict['wp'].memberPage().doChangeSecurityPWD(self.withdraw_password, temp_spwd)
        self.function_dict['wp'].memberPage().doChangeSecurityPWD(temp_spwd, self.withdraw_password)

    @DecorateClass('PFREQ-T2047')
    def test_change_member_contact(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        temp_contact = 'test000@gmail.com', '00987654329', '654321', 'As321321' # 帶入資料 = E-MAIL ,手機電話 ,QQ號碼 ,微信號碼
        phone = '1350045678' + str(random.randint(0,9))
        contact = 'autotest@qq.com', phone, '123456', 'As123123'
        self.function_dict['wp'].memberPage().doChangeContact(*temp_contact, self.withdraw_password)
        self.function_dict['wp'].memberPage().doChangeContact(*contact, self.withdraw_password)

    def test_change_bank_card(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_member_center()
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        self.function_dict['wp'].memberPage().do_change_bankCard('654', '321', self.withdraw_password)
        self.function_dict['wp'].memberPage().into_L_MenuMyProfile()
        self.function_dict['wp'].memberPage().do_change_bankCard('台灣', '台北', self.withdraw_password)

    def test_maintenance(self): # 暫時關閉第三方維護測試,因緩衝時間導致無法抓到正確狀態
        is_maintenance = True
        game_list = ['捕鱼王', '三昇体育', 'GC-视讯'] # KY棋牌 DT電子 AG捕魚 三昇體育 GC視訊
        # brand_list = ['ky', 'dt', 'ag', 'ss', 'gc']
        brand_list = ['ky']

            
        # 測試遊戲維護開關,先做關閉在打開
        for _ in range(0,2):
            try:
                # Admin
                if is_maintenance == True:

                    for loop in range(0,2):
                        self.test_admin_login()
                        self.function_dict['ad'].systemmanagementpage().into_admin_setting()     
                        self.function_dict['ad'].WebsiteSetting().web_maintenance(is_maintenance)
                        self.sleep(80)

                        if loop == 0:
                            # Web
                            self.function_dict['wp'].basePage().open_base_url()
                            self.function_dict['wp'].mainPage().maintenance(is_maintenance)
                        else:
                            self.function_dict['wp'].basePage().open_base_url()
                            self.test_web_login()
                            is_maintenance = True
                            break

                        is_maintenance = False
            except:
                is_maintenance = False
                self.test_admin_login()
                self.function_dict['ad'].systemmanagementpage().into_admin_setting()     
                self.function_dict['ad'].WebsiteSetting().web_maintenance(is_maintenance)
                self.sleep(80)

                raise EOFError('主頁維護測試失敗')
                
            try:
                # Admin
                self.test_admin_login()
                
                self.function_dict['ad'].operationmanagementPage().into_hk6_game_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                self.function_dict['ad'].operationmanagementPage().into_ky_channel_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_dt_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_ag_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_3s_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_gc_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # Web
                # 額度轉換維護狀態測試
                self.function_dict['wp'].basePage().open_base_url()
                self.function_dict['wp'].menuPage().into_menu_member_wallet()
                self.function_dict['wp'].memberPage().maintenance_check(brand_list, is_maintenance)

                # KY棋牌
                # self.function_dict['wp'].basePage().open_base_url()
                # self.function_dict['wp'].menuPage().into_menu_game()
                # self.function_dict['wp'].chessPage().maintenance_check(is_maintenance)
                
                # # DT電子
                # self.function_dict['wp'].basePage().open_base_url()
                # self.function_dict['wp'].menuPage().into_menu_electronic()
                # self.function_dict['wp'].electronicPage().maintenance_check(is_maintenance)

                # # AG捕魚
                # self.function_dict['wp'].basePage().open_base_url()
                # self.function_dict['wp'].menuPage().into_menu_fish()
                # self.function_dict['wp'].fishPage().maintenance_check(game_list[0], is_maintenance)
                
                # # 三昇體育
                # self.function_dict['wp'].basePage().open_base_url()
                # self.function_dict['wp'].menuPage().into_menu_sport()
                # self.function_dict['wp'].sportPage().maintenance_check(game_list[1], is_maintenance)
            
                # # GC視訊
                # self.function_dict['wp'].basePage().open_base_url()
                # self.function_dict['wp'].menuPage().into_menu_casino()
                # self.function_dict['wp'].casinoPage().maintenance_check(game_list[2], is_maintenance)

                # 香港六合彩
                self.function_dict['wp'].basePage().open_base_url()
                self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
                self.function_dict['wp'].lotteryPage().into_hk(is_maintenance)  # 進入香港六合彩

                is_maintenance = False
                
            except:
                is_maintenance = False
                 # Admin
                self.test_admin_login()
                
                self.function_dict['ad'].operationmanagementPage().into_hk6_game_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                self.function_dict['ad'].operationmanagementPage().into_ky_channel_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                raise EOFError('KY棋牌 or 香港六合彩 維護測試失敗')
    
    # 人工入款
    @DecorateClass('PFREQ-T1892')
    def test_manual_deposit(self):
        # before test action
        self.test_web_login()
        # Admin
        wallet_before = self.function_dict['wp'].menuPage().get_balance_wallet()
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        self.function_dict['ad'].ArtificialDeposit().add_bill(self.web_account, self.money)

        # WEB
        self.function_dict['wp'].basePage().open_base_url()
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].menuPage().into_menu_member_wallet() # 進入額度轉換
        self.function_dict['wp'].memberPage().after_check_manualdeposit_record(wallet_before, '人工入款', self.money) # 進入入款紀錄比對

    # 測試-香港六合彩 下注 & 期數
    @DecorateClass('PFREQ-T1977')
    def test_betting_hk(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_hk()  # 進入香港六合彩
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_hk)  # 號碼下注
        self.function_dict['wp'].lotteryGamePage().image_check('HK') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        #  Game2
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_hk_lslw)  # 二尾碰下注
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(1)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速六合彩 下注 & 期數
    @DecorateClass('PFREQ-T1978')
    def test_betting_js6(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_js6()  # 進入極速六合彩
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_hk)  # 號碼下注
        self.function_dict['wp'].lotteryGamePage().image_check('JS6') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
         # Game2
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_hk_lslw)  # 二尾碰下注
        self.function_dict['wp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速時時彩 下注 & 期數
    @DecorateClass('PFREQ-T1980')
    def test_betting_jsssc(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_jsssc()  # 進入極速時時彩
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_jsssc)  # 兩面下注
        self.function_dict['wp'].lotteryGamePage().image_check('JSSSC') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速PK10- 下注 & 期數
    @DecorateClass('PFREQ-T1981')
    def test_betting_jspk10(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_jspk10()  # 進入極速PK10
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().betting_jspk10)  
        self.function_dict['wp'].lotteryGamePage().image_check('JSPK10') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-PC蛋蛋 下注 & 期數
    @DecorateClass('PFREQ-T1976')
    def test_betting_pcegg(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_pcegg()  # 進入PC蛋蛋
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().pcegg)  
        self.function_dict['wp'].lotteryGamePage().image_check('PCEGG') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速11選5 下注 & 期數
    @DecorateClass('PFREQ-T2203')
    def test_betting_jisu11to5(self):
        # before test action
        self.test_web_login()
        # WEB
        Lottery_name= 'Jisu11to5'
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_jisu11to5()  # 進入極速11選5
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().jisu11to5)  
        self.function_dict['wp'].lotteryGamePage().image_check('JISU11TO5') # 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(1,Lottery_name)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速快三 下注 & 期數
    @DecorateClass('PFREQ-T2182')
    def test_betting_jisuk3(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_jisuk3()  # 進入快三
        #  Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().js3)
        self.function_dict['wp'].lotteryGamePage().image_check('JS3')# 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(5)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-福彩3D 下注 & 期數
    @DecorateClass('PFREQ-T1973')
    def test_betting_fu3d(self):
        # before test action
        self.test_web_login()
        # WEB
        records = []
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_fu3d()  # 進入福彩3D
        # Game1
        record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().fu3d)  
        self.function_dict['wp'].lotteryGamePage().image_check('FU3D')# 數字圖片辨識
        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['wp'].lotteryGamePage().periods_checker(1)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 三分六合彩 下注 & 期數
    @DecorateClass('PFREQ-T1986')
    def test_betting_sf6(self):
        # before test action
        self.test_web_login()
        # WEB
        self.function_dict['wp'].menuPage().into_menu_lottery()
        self.function_dict['wp'].lotteryPage().into_sf6()

        # 膽拖生肖
        records = []
        bravery_tow = random.randint(1, 49)
        zodiac_sign = random.randint(1, 12)
        record = self.function_dict['wp'].lotteryGamePage().betting_sf6_bravery_tow_zodiac_sign(bravery_tow, zodiac_sign)

        self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
        records.append(self.function_dict['wp'].gameRecordPage().game_lottery(record))
        self.function_dict['wp'].lotteryGamePage().periods_checker(1)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 站內消息
    @DecorateClass('PFREQ-T1846')
    def test_station_news(self):
        # Admin
        self.test_admin_login()
        self.function_dict['ad'].ServiceAgentPage().into_station_message()
        data = self.function_dict['ad'].StationNews().get_message_data()
        data['start_time'] = data['start_time'].strftime('%Y-%m-%d %H:%M:00')
        data['content'] = 'Bot Message test'
        self.function_dict['ad'].StationNews().add_message(data)
        # WEB
        self.test_web_login()
        self.function_dict['wp'].menuPage().into_message_center()
        self.function_dict['wp'].messagePage().check_message(data)

    # 登入公告
    @DecorateClass('PFREQ-T1841')
    def test_login_announcement(self):
        # Admin
        self.test_admin_login()
        self.function_dict['ad'].MarketCenterPage().into_login_announcement()
        data = self.function_dict['ad'].LoginAnnouncement().get_message_data()
        data['content'] = 'Bot Message test'
        self.function_dict['ad'].LoginAnnouncement().add_message(data)
        # Web
        self.test_web_login(flag=False)
        self.function_dict['wp'].mainPage().check_login_board(data)  # 測試登入公告
        
    # 確認所有彩種玩法存在
    def test_check_lottery_game(self):
        # before test action
        self.test_web_login()
        # WEB
        ## 將各彩種種類從文件撈出來
        lottery_data, hk_game = self.function_dict['wp'].lotterylist().lotterylist()
        hk = self.function_dict['wp'].lotterylist().hk(self.brand)
        marksix = self.function_dict['wp'].lotterylist().marksix()
        ss = self.function_dict['wp'].lotterylist().ss()
        pk = self.function_dict['wp'].lotterylist().pk()
        pcegg = self.function_dict['wp'].lotterylist().pcegg()
        to115 = self.function_dict['wp'].lotterylist().to115()
        k3 = self.function_dict['wp'].lotterylist().k3()
        normal = self.function_dict['wp'].lotterylist().normal()
        hk_data = [hk]

        self.function_dict['wp'].basePage().open_base_url()
        self.test_web_login()
        self.function_dict['wp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['wp'].lotteryPage().into_hk()  # 進入香港六合彩
        
        self.function_dict['wp'].lotteryGamePage().check_game_list_name(lottery_data) # 所有彩種比對

        self.function_dict['wp'].lotteryGamePage().into_and_checkhk(hk_game, hk_data)
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('六合彩', lottery_data['六合彩'], Game_data = [marksix])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('时时彩', lottery_data['时时彩'], Game_data = [ss])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('PK拾(幸运飞艇)', lottery_data['PK拾(幸运飞艇)'], Game_data = [pk])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('PC蛋蛋(幸运28)', lottery_data['PC蛋蛋(幸运28)'], Game_data = [pcegg])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('11选5', lottery_data['11选5'], Game_data = [to115])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('快3', lottery_data['快3'], Game_data = [k3])
        self.function_dict['wp'].lotteryGamePage().into_and_checkall('一般彩票', lottery_data['一般彩票'], Game_data = [normal])

    @DecorateClass('PFREQ-T2048')
    def test_language_check(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().language(self.web_url)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
        
class MobileWebCases(BaseTestCase, BasePage_Mobile):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    money='300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []
    new_version_list = ['cdd', '3h']

    # ================================= TestSetting ================================
                
    @classmethod
    def setUpClass(cls):
        cls.folderpath = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        
    @classmethod
    def setUp(cls):
        for key, function in cls.function_dict.items():
            try:
                function.basePage().accept_alert()
                function.basePage().dismiss_alert()
            except:
                pass
            
            function.basePage().switch_home_page()
            if key == 'mp':
                cls.open_url(cls, function, cls.web_url)
                function.mainPage().maintenance()

    def tearDown(self):
        self.test_all_windows_max()
        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

        

    @classmethod
    def tearDownClass(cls):
        num = 0
        for function in cls.function_dict.values():
            function.basePage().quit_browser()
            num+=1

            if num == len(cls.driver_list):
                cls.driver_list = []
                break
    
    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000, is_wap=True))  # 設定ChromeDriver
        cls.function_dict['mp'] = MobilePage(cls.driver_list[-1], cls.wait_time, cls.mobile_url, cls.skipTest)  # 導入Wap全部頁面
        cls.function_dict['mp'].basePage().hide_windows()
        
        if not sys.argv[0].__contains__('prod'): # Prod 不帶入admin config
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPage(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].basePage().hide_windows()

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass
        
        function.basePage().open_browser(url)

    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top()

    # 測試-首次進網站
    @DecorateClass('PFREQ-T1806')
    def test_skip_app_download(self):
        self.function_dict['mp'].mainPage().skip_app_download()

    # 測試-註冊後登出
    @DecorateClass('PFREQ-T1801')
    def test_register_logout(self):
        self.test_skip_app_download()
        if self.brand in self.new_version_list:
            self.function_dict['mp'].mainPage().into_nwap_register_page()
        else:
            self.function_dict['mp'].mainPage().into_register_page()        
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['mp'].registerPage().do_register(self.bot_id, '123456', '111111')
        self.function_dict['mp'].mainPage().close_login_board()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().do_logout()
        self.function_dict['mp'].mainPage().logout_checker()

    # 測試-註冊
    def test_register(self):
        self.function_dict['mp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%j%H%M%S')
        self.function_dict['mp'].registerPage().do_register(self.bot_id, '123456', '111111')
        self.function_dict['mp'].mainPage().close_login_board()

    # 測試ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin
        
    # 測試-登入
    @DecorateClass('PFREQ-T1803')
    def test_wap_login(self, flag=True):
        self.function_dict['mp'].mainPage().windows_to_top() # 切換視窗
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_skip_app_download()
        self.function_dict['mp'].mainPage().into_login_page()
        captcha_status = self.function_dict['mp'].loginPage().login(self.web_account, self.web_password, self.web_captcha)
        if captcha_status == False:
            res, certification = self.function_dict['mp'].apibasefunction().do_wap_login(self.web_account, self.web_password, self.mobile_url)  # 有滑動驗證時用api登入
            self.function_dict['mp'].loginPage().add_cookie_wap(res)  # 把cookie加進driver
            self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].basePage().close_change_pwd()  # 關閉密碼更換彈窗
        self.function_dict['mp'].basePage().close_message_dialog()  # 關閉站內消息彈窗
        if flag == True:
            self.function_dict['mp'].mainPage().close_login_board() 
        
        if self.brand in self.new_version_list:
            self.function_dict['mp'].mainPage().into_old_page() 
        
    # 紅包 -> 掃雷下注 & 對前後台注單
    @DecorateClass('PFREQ-T2020')
    def test_mine_sweeping_betting(self):
        self.test_wap_login()
        record = []
        data = self.function_dict['mp'].redEnvelopePage().get_bot_hall_data()
        betting_data = {'amount': random.randint(1, 10), 'number': random.randint(0, 9)}

        self.function_dict['mp'].menuPage().into_mine_sweeping()
        self.function_dict['mp'].redEnvelopePage().into_mine_sweeping_hall(data, gl.get_value('ENV'))
        self.function_dict['mp'].redEnvelopePage().check_link_in_hall()
        self.function_dict['mp'].redEnvelopePage().into_give_red_envelope()
        self.function_dict['mp'].redEnvelopePage().give_red_envelope(betting_data['amount'], betting_data['number'])
        # -------------------------------- 對注單 --------------------------------
        ## -------------------------------- 前台 --------------------------------
        self.sleep(0.5)
        self.test_wap_login()
        
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        betting_data['game_name'] = '红包'
        record.append(self.function_dict['mp'].gameRecordPage().check_record_front_end(betting_data))
        ## -------------------------------- 後台 --------------------------------
        if not gl.get_value('ENV').__contains__('prod'):
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()
            self.function_dict['ad'].CheckRecord().check_red_envelope_record(record)

    # 紅包 -> 牛牛下注 & 對前後台注單
    @DecorateClass('PFREQ-T2021')
    def test_niu_niu_betting(self):
        self.test_wap_login()
        record = []
        data = self.function_dict['mp'].redEnvelopePage().get_bot_hall_data()
        betting_data = {'amount': random.randint(1, 10), 'number': random.randint(2, 10)}

        self.function_dict['mp'].menuPage().into_niu_niu()
        self.function_dict['mp'].redEnvelopePage().into_niu_niu_hall(data, gl.get_value('ENV'))
        self.function_dict['mp'].redEnvelopePage().check_link_in_hall()
        self.function_dict['mp'].redEnvelopePage().into_give_red_envelope()
        self.function_dict['mp'].redEnvelopePage().give_red_envelope(betting_data['amount'], betting_data['number'])
        # -------------------------------- 對注單 --------------------------------
        ## -------------------------------- 前台 --------------------------------
        self.sleep(0.5)
        self.test_wap_login()
        
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        # 自動化測試只會有測試開包功能，且牛1到牛牛賠率都為1，因此注單金額為 單包金額 * 紅包個數
        betting_data['amount'] = betting_data['amount'] * (betting_data['number'] - 1)
        betting_data['game_name'] = '红包'
        record.append(self.function_dict['mp'].gameRecordPage().check_record_front_end(betting_data))
        ## -------------------------------- 後台 --------------------------------
        if not gl.get_value('ENV').__contains__('prod'):
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()
            self.function_dict['ad'].CheckRecord().check_red_envelope_record(record)

    # 站內消息
    @DecorateClass('PFREQ-T2178')
    def test_station_news(self):
        # Admin
        self.test_admin_login()
        self.function_dict['ad'].ServiceAgentPage().into_station_message()
        data = self.function_dict['ad'].StationNews().get_message_data()
        data['start_time'] = data['start_time'].strftime('%Y-%m-%d %H:%M:00')
        data['content'] = 'Bot Message test'
        self.function_dict['ad'].StationNews().add_message(data)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_message()
        self.function_dict['mp'].messagePage().check_message(data)

    # 測試-登出
    @DecorateClass('PFREQ-T2107')
    def test_wap_logout(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().do_logout()

    # 測試公司入款
    @DecorateClass('PFREQ-T1838')
    def test_company_deposit(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_company_deposit('公司入款', '銀行自動測試')  # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_company_deposit('銀行自動測試', self.money)
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money,offer_money,total_money=self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')

    # 測試支付寶面對面
    @DecorateClass('PFREQ-T1839')
    def test_desposit_alipay_f2f(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_qr_deposit('支付宝', 'bot', '支付宝面对面扫码', self.money) # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_desposit_weChat_alipayf2f()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money,offer_money,total_money=self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')

    # 測試微信面對面
    @DecorateClass('PFREQ-T1842')
    def test_desposit_wechat_f2f(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_qr_deposit('微信', 'bot', '微信面对面扫码', self.money) # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_desposit_weChat_alipayf2f()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money,offer_money,total_money=self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')

    # 測試支付寶轉帳
    @DecorateClass('PFREQ-T1840')
    def test_desposit_alipay_transfer(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().checktr_deposit('支付宝', '支付寶轉帳自動測試', '支付宝转帐', self.money)
        self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
         # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money,offer_money,total_money=self.function_dict['ad'].companyDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')

    # 測試微信轉帳
    @DecorateClass('PFREQ-T1845')
    def test_desposit_wechat_transfer(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().checktr_deposit('微信', '微信轉帳自動測試', '微信转帐', self.money)
        real_money = self.function_dict['mp'].depositPage().get_real_money(self.money)
        self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('公司入款', real_money) # 確認產生充值中紀錄
         # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請
        tra_money,offer_money,total_money=self.function_dict['ad'].companyDepositPage().get_money_info(real_money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')

     # 測試線上支付
    @DecorateClass('PFREQ-T1848')
    def test_desposit_onlinepay(self):
        # before test action
        self.test_wap_login()
        # Wap  
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','自動市_线上支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_线上支付')
        self.function_dict['mp'].basePage().open_base_url()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().pass_first_deposit(self.admin_otp)  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對

    # 測試銀聯支付
    @DecorateClass('PFREQ-T1849')
    def test_desposit_unionpay(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_unionpay('银联支付', '银联支付','自動市_银联支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_银联支付')
        self.function_dict['mp'].basePage().open_base_url()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10)  #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().pass_first_deposit(self.admin_otp)  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對

    # 測試京東支付
    @DecorateClass('PFREQ-T1850')
    def test_desposit_jdpay(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().check_jdpay('京东支付', '京东支付','自動市_京东支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_京东支付')
        self.function_dict['mp'].basePage().open_base_url()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().before_check_money_entry_record('在线入款',self.money) # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().pass_first_deposit(self.admin_otp)  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對

    # 測試微信入款
    def test_WechatDeposit(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().do_wechat_deposit('1')  # 公司入帳
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請

    # 測試微信QR入款
    def test_WechatQRDeposit(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().do_wechatqa_deposit('100', '1')  # 公司入帳
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請

     # 測試支付寶QR入款
    def test_AliPayQRDeposit(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_deposit()  # 進入線上存款
        self.function_dict['mp'].depositPage().do_aliPayqr_deposit('100', '1')  # 公司入帳
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()  # 確認最新一筆申請


    # 測試線上出款
    @DecorateClass('PFREQ-T1852')
    def test_withdraw(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_bank('台灣', '台北', self.withdraw_password)  #設定銀行卡號
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
        total_money,Charge=self.function_dict['mp'].withdrawPage().do_withdraw(self.withdraw, self.withdraw_password, self.brand)  # 取款
        Decimal_point = self.function_dict['mp'].Store_Record_Page().before_check_money_output_record('在线提现',total_money,Charge,'银行') # 確認產生充值中紀錄   Decimal_point為小數點差異
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_out_report()  # 進入線上取款紀錄
        self.function_dict['mp'].Store_Record_Page().after_check_money_output_record(self.withdraw,wallet_before,Charge,Decimal_point,'银行') # 進入出款紀錄比對


    # 測試線上出款_CGpay
    @DecorateClass('PFREQ-T5973')
    def test_cgpay_withdraw(self):
        # ADMIN
        phone = '13500' + str('%06d' %random.randint(0,999999))     
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().change_member_phone(self.web_account, phone, self.admin_otp)  # 修改會員手機號碼
        
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_virtualcard(self.withdraw_password, phone)  #設定虛擬錢包
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
        total_money,Charge=self.function_dict['mp'].withdrawPage().do_cgpay_withdraw(self.withdraw, self.withdraw_password, self.brand)  # 取款
        Decimal_point = self.function_dict['mp'].Store_Record_Page().before_check_money_output_record('在线提现',total_money,Charge,'CGPay') # 確認產生充值中紀錄   Decimal_point為小數點差異
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()                          # 進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)   # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)               # 確認最新一筆申請
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_out_report()  # 進入線上取款紀錄
        self.function_dict['mp'].Store_Record_Page().after_check_money_output_record(self.withdraw,wallet_before,Charge,Decimal_point,'CGPay') # 進入出款紀錄比對


    @DecorateClass('PFREQ-T2110')
    # 測試-選單功能
    def test_into_promo(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_promo(self.brand)

    @DecorateClass('PFREQ-T2104')
    def test_into_red_envelope(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_red_envelope()

    @DecorateClass('PFREQ-T2023')
    def test_into_member_center(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()

    @DecorateClass('PFREQ-T2046')
    def test_into_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].menuPage().into_wallet_conversion()

    @DecorateClass('PFREQ-T2049')
    def test_into_deposit(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_deposit()

    @DecorateClass('PFREQ-T2051')
    def test_into_withdraw(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_withdraw()

    def test_into_trend(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_rend()

    def test_into_description(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_description()

    @DecorateClass('PFREQ-T2180')
    def test_into_news(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_news()

    @DecorateClass('PFREQ-T5087')
    def test_feedback(self):
        num = 1
        text_list = ["<script>alert('Hi')</script>", "13579!@#$%^&*()_+繁體简体english"]
        # Wap
        for text in text_list:
            self.test_wap_login()
            self.function_dict['mp'].menuPage().into_member_center()
            title = f'測試用_{num}'
            self.function_dict['mp'].memberCenterPage().into_feedback()
            self.function_dict['mp'].feedback_page().feedback_message(title, text)
            # admin
            self.test_admin_login()
            self.function_dict['ad'].ServiceAgentPage().into_feedback()
            self.function_dict['ad'].feedback_page().check_feedback(self.web_account, title, text)
            num+=1
        

    @DecorateClass('PFREQ-T2181')
    def test_into_together(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_together()

    # 測試-額度轉換
    @DecorateClass('PFREQ-T1854')
    def test_wallet_conversion_return_local(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_wallet_conversion()  # 進入額度管理
        cp_wallet = self.function_dict['mp'].thirdPartyWalletPage().do_wallet_return()
        self.function_dict['mp'].thirdPartyWalletPage().do_walletre_fresh()
        self.function_dict['mp'].thirdPartyWalletPage().do_wallet_check(cp_wallet)

    def test_WalletConversion(self, wallet_list):
        # before test action
        self.test_wap_login()
        # Wap
        for _ in range(0,2):
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_wallet_conversion()  # 進入額度管理
            self.function_dict['mp'].thirdPartyWalletPage().do_walletre_fresh()
            money_before = self.function_dict['mp'].thirdPartyWalletPage().do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_wallet_Report()  # 進入交易流水
            self.function_dict['mp'].thirdPartyWalletPage().trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1857')
    def test_ag_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','ag']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1875')
    def test_mg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','mg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1874')
    def test_sb_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','sb']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1878')
    def test_bbin_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap            
        wallet_list = ['cp','bbin']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1882')
    def test_dt_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','dt']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1890')
    def test_gc_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','dt']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1889')
    def test_hg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','hg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1879')
    def test_ky_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','ky']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1876')
    def test_pt_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','pt']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1880')
    def test_lc_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','lc']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1883')
    def test_gm_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','gm']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1884')
    def test_fg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','fg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1885')
    def test_cq_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','cq']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1881')
    def test_vg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','vg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1886')
    def test_sw_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','sw']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1887')
    def test_3s_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','ss']
        self.test_WalletConversion(wallet_list)
    
    @DecorateClass('PFREQ-T3070')
    def test_dg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','dg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1888')
    def test_bs_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','bs']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1961')
    def test_kk_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','kk']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T6980')
    def test_bg_wallet_conversion(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['cp','bg']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T2109')
    # 測試- 修改會員資料
    def test_change_member_Info(self):
        number = '13' + str(random.randrange(100000000, 999999999, 9))
        # before test action
        self.test_wap_login()
        # Wap
        # 修改EMAIL、手機、QQ號碼
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_mail('test000@gmail.com', self.withdraw_password)
        self.function_dict['mp'].memberInfoPage().do_change_mail('autotest@qq.com', self.withdraw_password)
        self.function_dict['mp'].memberInfoPage().do_change_qq('654321', self.withdraw_password)
        self.function_dict['mp'].memberInfoPage().do_change_qq('123456', self.withdraw_password)
        self.function_dict['mp'].memberInfoPage().do_change_phone(number, self.withdraw_password)
        # 修改提款密碼
        temp_spwd = '666666'
        self.function_dict['mp'].memberInfoPage().do_change_security_password(self.withdraw_password, temp_spwd)
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_security_password(temp_spwd, self.withdraw_password)
        # 修改會員密碼
        temp_pwd = 'Qa0123456'
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_password(self.web_password, temp_pwd, self.withdraw_password)
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_password(temp_pwd, self.web_password, self.withdraw_password)

    def test_maintenance(self): # 暫時關閉第三方維護測試,因緩衝時間導致無法抓到正確狀態
        is_maintenance = True
        game_list = ['捕鱼王','三昇体育','GC-视讯'] # KY棋牌 DT電子 AG捕魚 三昇體育 GC視訊
        # brand_list = ['ky', 'dt', 'ag', 'ss', 'gc']
        brand_list = ['ky']

        # 測試遊戲維護開關,先做關閉在打開
        for _ in range(0,2):
            try:
                # Admin
                if is_maintenance == True:
                    for loop in range(0,2):
                        self.test_admin_login()
                        self.function_dict['ad'].systemmanagementpage().into_admin_setting()     
                        self.function_dict['ad'].WebsiteSetting().web_maintenance(is_maintenance)
                        self.sleep(80)

                        if loop == 0:
                            # Web
                            self.function_dict['mp'].basePage().open_base_url()
                            self.function_dict['mp'].mainPage().maintenance(is_maintenance)
                        else:
                            self.function_dict['mp'].basePage().open_base_url()
                            self.test_wap_login()
                            is_maintenance = True
                            break

                        is_maintenance = False
            except:
                is_maintenance = False
                self.test_admin_login()
                self.function_dict['ad'].systemmanagementpage().into_admin_setting()     
                self.function_dict['ad'].WebsiteSetting().web_maintenance(is_maintenance)
                self.sleep(80)

                raise EOFError('主頁維護測試失敗')

            try:
                # Admin
                self.test_admin_login()
                
                self.function_dict['ad'].operationmanagementPage().into_hk6_game_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                self.function_dict['ad'].operationmanagementPage().into_ky_channel_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_dt_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_ag_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_3s_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                # self.function_dict['ad'].operationmanagementPage().into_gc_channel_setting()
                # self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)
    
                # Wap
                # 額度轉換維護狀態測試
                self.function_dict['mp'].basePage().open_base_url()
                self.function_dict['mp'].menuPage().into_member_center()
                self.function_dict['mp'].memberCenterPage().into_wallet_conversion()  # 進入額度管理
                self.function_dict['mp'].thirdPartyWalletPage().maintenance_check(brand_list, is_maintenance)

                # # KY棋牌
                # self.function_dict['mp'].basePage().open_base_url() # 開啟Wap網站
                # self.function_dict['mp'].menuPage().into_menu_game()
                # self.function_dict['mp'].chessPage().maintenance_check(is_maintenance)

                # # DT電子
                # self.function_dict['mp'].basePage().open_base_url()
                # self.function_dict['mp'].menuPage().into_menu_electronic()
                # self.function_dict['mp'].electronicPage().maintenance_check(is_maintenance)

                # # AG捕魚
                # self.function_dict['mp'].basePage().open_base_url()
                # self.function_dict['mp'].menuPage().into_menu_fish()
                # self.function_dict['mp'].fishPage().maintenance_check(game_list[0], is_maintenance)
                
                # # 三昇體育
                # self.function_dict['mp'].basePage().open_base_url()
                # self.function_dict['mp'].menuPage().into_menu_sport()
                # self.function_dict['mp'].sportPage().maintenance_check(game_list[1], is_maintenance)
            
                # # GC視訊
                # self.function_dict['mp'].basePage().open_base_url()
                # self.function_dict['mp'].menuPage().into_menu_casino()
                # self.function_dict['mp'].casinoPage().maintenance_check(game_list[2], is_maintenance)

                # 香港六合彩
                self.function_dict['mp'].basePage().open_base_url()
                
                if self.mobile_ui_mode == "new":
                    self.function_dict['mp'].mainPage().into_menu_lottery()  # 進入彩票遊戲
                else:
                    self.function_dict['mp'].mainPage().into_lottery_page()

                new_lottery_brand = ['ls','3h','tz','cdd','co']

                if self.brand in new_lottery_brand:
                    self.function_dict['mp'].lotteryGamePage().into_hk_new(is_maintenance) # 新版香港六合彩
                else:
                    self.function_dict['mp'].lotteryGamePage().into_hk(is_maintenance)  # 進入香港六合彩

                is_maintenance = False

            except:
                is_maintenance = False
                # Admin
                self.test_admin_login()
                
                self.function_dict['ad'].operationmanagementPage().into_hk6_game_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                self.function_dict['ad'].operationmanagementPage().into_ky_channel_setting()
                self.function_dict['ad'].GameSetting().web_radio_on_off(is_maintenance)

                raise EOFError('KY棋牌 or 香港六合彩 維護測試失敗')
    
    @DecorateClass('PFREQ-T2179')
    def test_manual_deposit(self):
        # Admin
        self.test_wap_login()
        wallet_before = self.function_dict['mp'].menuPage().get_balance_wallet()
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        self.function_dict['ad'].ArtificialDeposit().add_bill(self.web_account, self.money)

        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().after_check_manualdeposit_record(wallet_before, '人工入款', self.money) # 進入入款紀錄比對

    @DecorateClass('PFREQ-T1812')
    def test_login_announcement(self):
        # Admin
        self.test_admin_login()
        self.function_dict['ad'].MarketCenterPage().into_login_announcement()
        data = self.function_dict['ad'].LoginAnnouncement().get_message_data()
        data['content'] = 'Bot Message test'
        self.function_dict['ad'].LoginAnnouncement().add_message(data)
        # Wap
        self.test_wap_login(flag=False)
        self.function_dict['mp'].mainPage().check_login_board(data)  # 測試登入公告

    @DecorateClass('PFREQ-T2108')
    def test_language_check(self):
        self.test_wap_login()
        self.function_dict['mp'].mainPage().language(self.mobile_url)

    # -------------------------------- 新版彩票 --------------------------------
    # 新版 彩票 下注
    def test_betting_new(self, into_game_func, lottery, items_check = True):
        records = []
        self.test_wap_login()
        if self.brand in self.new_version_list:
            pass
        else:    
            into_game_func()
            # self.function_dict['mp'].lotteryGamePage().image_check(lottery) # 數字圖片辨識
            self.function_dict['mp'].lotteryGamePage().check_periods_new(2, lottery)  # 檢查期數差異
            lottery_record = self.function_dict['mp'].lotteryGamePage().betting_game_new()

            if items_check == True:
                self.function_dict['mp'].lotteryGamePage().help_items()

            self.test_wap_login()
            self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
            record = self.function_dict['mp'].gameRecordPage().game_lottery(lottery_record)
            records.append(record)

            if not gl.get_value('ENV').__contains__('prod'):
                # ADMIN PART
                self.test_admin_login()
                self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
                self.function_dict['ad'].CheckRecord().check_result(records)

    # 新版 三分六合彩 連碼 -> 膽拖生肖
    @DecorateClass('PFREQ-T1984')
    def test_betting_sf6_bravery_tow(self):
        records = []
        self.test_wap_login()
        if self.brand in self.new_version_list:
            pass
        else:    
            self.function_dict['mp'].lotteryGamePage().into_sf6_bravery_tow_new()
            self.function_dict['mp'].lotteryGamePage().check_periods_new(1)  # 檢查期數差異
            lottery_record = self.function_dict['mp'].lotteryGamePage().betting_bravery_tow_new()

            self.test_wap_login()
            self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
            record = self.function_dict['mp'].gameRecordPage().game_lottery(lottery_record)
            records.append(record)

            if not gl.get_value('ENV').__contains__('prod'):
                # ADMIN PART
                self.test_admin_login()
                self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
                self.function_dict['ad'].CheckRecord().check_result(records)

    # 新版 香港六合彩 下注
    @DecorateClass('PFREQ-T1979')
    def test_betting_hk_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_hk6_new, 'HK', True)
        
    # 新版 極速快三 下注
    @DecorateClass('PFREQ-T2217')
    def test_betting_jisuk3_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jisuk3_new, 'JSK3')
        
    # 新版 極速六合彩 下注
    @DecorateClass('PFREQ-T1982')
    def test_betting_js6_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_js6_new, 'JS6')
        
    # 新版 極速時時彩 下注
    @DecorateClass('PFREQ-T1985')
    def test_betting_jsssc_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jsssc_new, 'JSSSC')
        
    # 新版 極速pk拾 下注
    @DecorateClass('PFREQ-T1983')
    def test_betting_jspk10_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jspk10_new, 'JSPK10')
        
    # 新版 福彩3D 下注
    @DecorateClass('PFREQ-T1974')
    def test_betting_fu3d_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_fu3d_new, 'FU3D')

    # 新版 PC蛋蛋 下注
    @DecorateClass('PFREQ-T1975')
    def test_betting_pcegg_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_pcegg_new, 'PCEGG')
    
    # 新版 極速11選5 下注
    @DecorateClass('PFREQ-T2218')
    def test_betting_jisu11to5_new(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jisu11to5_new, 'Jisu11to5') 
    
    # 確認所有彩種玩法存在
    def test_check_lottery_game(self):
        self.test_wap_login()
        ## 將各彩種種類從文件撈出來
        lottery_data, hk_game = self.function_dict['mp'].lotterylist().lotterylist()
        hk = self.function_dict['mp'].lotterylist().hk(self.brand)
        marksix = self.function_dict['mp'].lotterylist().marksix()
        ss = self.function_dict['mp'].lotterylist().ss()
        pk = self.function_dict['mp'].lotterylist().pk()
        pcegg = self.function_dict['mp'].lotterylist().pcegg()
        to115 = self.function_dict['mp'].lotterylist().to115()
        k3 = self.function_dict['mp'].lotterylist().k3()
        normal = self.function_dict['mp'].lotterylist().normal()
        hk_data = [hk]

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_hk_new()
        self.function_dict['mp'].lotteryGamePage().into_game_list()
        self.function_dict['mp'].lotteryGamePage().check_game_list_name(lottery_data) # 所有彩種比對

        self.function_dict['mp'].lotteryGamePage().into_and_checkhk(hk_game, hk_data)
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['六合彩'], Game_data = [marksix])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['时时彩'], Game_data = [ss])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['PK拾(幸运飞艇)'], Game_data = [pk])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['PC蛋蛋(幸运28)'], Game_data = [pcegg])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['11选5'], Game_data = [to115])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['快3'], Game_data = [k3])
        self.function_dict['mp'].lotteryGamePage().into_and_checkall(lottery_data['一般彩票'], Game_data = [normal])

    # -------------------------------- 舊版彩票 --------------------------------

    # 測試-香港六合彩 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2006')
    def test_betting_hk6_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_hk6() # 進入香港六合彩
        else:
            self.function_dict["mp"].lotteryGamePage().into_hk6_new()
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting)
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('HK') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        #  Game2
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_hk_lslw)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(1)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速六合彩 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2008')
    def test_betting_js6_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_js6()
        else:
            self.function_dict["mp"].lotteryGamePage().into_js6_new()
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting)  # 號碼下注
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('JS6') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        #  Game2
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_hk_lslw)  # 二尾碰下注
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速時時彩 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2009')
    def test_betting_jsssc_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_jsssc()
        else:
            self.function_dict["mp"].lotteryGamePage().into_jsssc_new()
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting)  # 兩面下注
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('JSSSC') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速PK10- 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2010')
    def test_betting_jspk10_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_jspk10()
        else:
            self.function_dict["mp"].lotteryGamePage().into_jspk10_new()

        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting)  # 冠亞和下注
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('JSPK10') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(3)  # 檢查期數差異

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-PC蛋蛋 下注 & 期數 (前往舊版彩票)
    def test_betting_pcegg_old(self):
        self.test_wap_login()
        new_lottery_brand = ['ls','3h','tz','cdd','co']
        
        if self.brand in new_lottery_brand:
            self.test_betting_pcegg_new()
            return

        records = []

        if self.mobile_ui_mode == 'new':
            self.function_dict['mp'].mainPage().into_menu_lottery()  # 彩票大廳
        else:
            self.function_dict['mp'].mainPage().into_lottery_page()  # 無彩票大廳
            
        self.function_dict['mp'].lotteryGamePage().into_pcball()  # 進入PC蛋蛋
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_2)
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('PCEGG') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(3)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速11選5 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2219')
    def test_betting_jisu11to5_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_jisu11to5()
        else:
            self.function_dict["mp"].lotteryGamePage().into_jisu11to5_new()
        lottery_name = 'Jisu11to5'
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_2)
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('JISU11TO5') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(2, lottery_name)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-極速快三 下注 & 期數 (前往舊版彩票)
    @DecorateClass('PFREQ-T2220')
    def test_betting_jisuk3_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_jisuk3()
        else:
            self.function_dict["mp"].lotteryGamePage().into_jisuk3_new()
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_2)
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('JS3') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(5)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 測試-福彩3D 下注 & 期數 ((前往舊版彩票))
    @DecorateClass('PFREQ-T2011')
    def test_betting_fu3d_old(self):
        self.test_wap_login()
        # 前往舊版彩票
        if self.brand not in self.new_version_list:
            self.function_dict["mp"].mainPage().into_old_lottery_page()
            self.function_dict["mp"].lotteryGamePage().into_fu3d()
        else:
            self.function_dict["mp"].lotteryGamePage().into_fu3d_new()
        records = []
        #  Game1
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting)
        # 舊版圖片暫時先不比對
        # self.function_dict['mp'].lotteryGamePage().image_check('FU3D') # 數字圖片辨識
        self.sleep(1)
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        records.append(record)
        self.function_dict['mp'].lotteryGamePage().periods_checker(1)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)



    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
