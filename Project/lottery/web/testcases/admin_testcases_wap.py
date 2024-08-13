import unittest, sys, os, datetime, random, string, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.lottery.web.pages.pages import WebPages, AdminPage, MobilePage, CmWebPage, ResellerPage
from Project.lottery.web.testcases.base_testcase import BaseTestCase
from Project.lottery.web.pages.admin.admin_basepage import BasePage as BasePageAdmin
from Project.lottery.web.Utils_folder.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass

class AdminTestCasesWap(BaseTestCase, BasePageAdmin):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 20
    money = '300'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []
    brand = gl.get_value('BRAND')
    brand_env = gl.get_value('ENV')
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
        cls.function_dict['mp'].basePage().windows_to_top() # 切換視窗

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
            cls.function_dict['rp'] = ResellerPage(cls.driver_list[-1], cls.wait_time, cls.reseller_url, cls.skipTest)  # 導入Reseller全部頁面
            cls.function_dict['cmweb'] = CmWebPage(cls.driver_list[-1], cls.wait_time, cls.cmweb_url, cls.skipTest)  # 導入Cmweb全部頁面

            

    # 因應紅包設計於WAP, 所以新增該功能可以開啟多一個driver for mobilepage並且結束script時, 直接pop掉減少效能消耗.
    @classmethod
    def another_open_wap(cls, close=False):
        if close == False:
            cls.setting_test_data(cls)
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000, is_wap=True))
            cls.function_dict['mp'] = MobilePage(cls.driver_list[-1], cls.wait_time, cls.mobile_url, cls.skipTest)
        elif close == True:
            cls.function_dict['mp'].basePage().quit_browser()
            cls.function_dict.pop("mp")
            cls.driver_list.pop()   # driver不pop掉, tearDown會有問題.

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass
        function.basePage().windows_to_top()
        function.basePage().open_browser(url)


    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top() 
    
    # wap測試-登入
    @DecorateClass('PFREQ-T1803')
    def test_wap_login(self):
        self.test_all_windows_mini()
        self.function_dict['mp'].mainPage().windows_to_top() # 切換視窗
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().skip_app_download()
        self.function_dict['mp'].mainPage().into_login_page()
        captcha_status = self.function_dict['mp'].loginPage().login(self.web_account, self.web_password, self.web_captcha)
        if captcha_status == False:
            res, certification = self.function_dict['mp'].apibasefunction().do_wap_login(self.web_account, self.web_password, self.mobile_url)  # 有滑動驗證時用api登入
            self.function_dict['mp'].loginPage().add_cookie_wap(res)  # 把cookie加進driver
            self.function_dict['mp'].basePage().refresh_browser()        
        self.function_dict['mp'].basePage().close_change_pwd()  # 關閉密碼更換彈窗
        self.function_dict['mp'].basePage().close_message_dialog()  # 關閉站內消息彈窗
        self.function_dict['mp'].mainPage().close_login_board()  # 關閉登入公告

    # 測試ADMIN登入
    @DecorateClass('PFREQ-T1804')
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin

    def test_admin_logout(self):
        self.function_dict["ad"].basePage().windows_to_top()
        self.function_dict["ad"].loginPage().logout()
    
    # 測試Reseller登入
    def test_reseller_login(self):
        self.test_all_windows_mini()
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_agentinfo(self.reseller_account,'BotTest')

    # 測試Reseller登入
    def test_cmweb_login(self):    
        self.test_all_windows_mini() 
        self.function_dict['cmweb'].basePage().windows_to_top() # 切換視窗
        self.function_dict['cmweb'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['cmweb'].login_page().login(self.cmweb_account, self.cmweb_password)

    # 刪除存款銀行類型
    @DecorateClass('PFREQ-T1945')
    def test_delete_bank_sort(self):
        bank = ['公司入款', '微信', '支付宝']
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().delete_bank_sort(branch='')
        #WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit(bank)  # 確認公司入款有成功刪除

    # 新增銀行入款
    @DecorateClass('PFREQ-T1962')
    def test_add_desposit_bank(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('銀行自動測試', '自動市_公司入款', '1000000', '银行','公司入款 / 公司入款 ( 公司入款 )')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(branch='自動市_公司入款')
        self.function_dict['ad'].BankAcconut_PageLocator().bank_sort_name_check('自動市_公司入款')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit('公司入款', '銀行自動測試')  # 確認公司入帳有生成
        
    # 新增微信面對面
    @DecorateClass('PFREQ-T1963')
    def test_add_desposit_wechat_f2f(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('微信面對面自動測試', '自動市_微信面對面', '1000000', '微信面对面')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(branch='自動市_微信面對面')
        self.function_dict['ad'].BankAcconut_PageLocator().bank_sort_name_check('微信面对面')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_qr_deposit('微信', 'bot', '微信面对面扫码', self.money, True) # 確認公司入帳有生成

    # 新增支付寶面對面
    @DecorateClass('PFREQ-T1964')
    def test_add_desposit_alipay_f2f(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('支付寶面對面自動測試', '自動市_支付寶面對面', '1000000', '支付宝面对面')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(branch='自動市_支付寶面對面')
        self.function_dict['ad'].BankAcconut_PageLocator().bank_sort_name_check('支付宝面对面')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_qr_deposit('支付宝', 'bot', '支付宝面对面扫码', self.money, True)  # 確認公司入帳有生成

    # 新增微信轉帳
    @DecorateClass('PFREQ-T1965')
    def test_add_desposit_wechat_transfer(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('微信轉帳自動測試', '自動市_微信轉帳', '1000000', '微信转帐')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(branch='自動市_微信轉帳')
        self.function_dict['ad'].BankAcconut_PageLocator().bank_sort_name_check('微信转帐')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('微信', '微信轉帳自動測試', '微信转帐', self.money)  # 確認存款類型有生成

    # 新增支付寶轉帳
    @DecorateClass('PFREQ-T1966')
    def test_add_desposit_alipay_transfer(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('支付寶轉帳自動測試', '自動市_支付寶轉帳', '1000000', '支付宝转帐')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(branch='自動市_支付寶轉帳')
        self.function_dict['ad'].BankAcconut_PageLocator().bank_sort_name_check('支付宝转帐')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('支付宝', '支付寶轉帳自動測試', '支付宝转帐', self.money)  # 確認存款類型有生成
    
    # 新增UPI轉帳
    @DecorateClass('PFREQ-T8351')
    def test_add_desposit_upi(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()  # 進入銀行帳號
        self.function_dict['ad'].Pay_Branch_Page().add_sort_bank('upi轉帳自動測試', 'upi', '1000000', 'UPI', 'UPI入款 / UPI入款 ( UPI入款 )')  # 新增銀行分類
        self.function_dict['ad'].Pay_Branch_Page().search_bank(bank_number='upi轉帳自動測試')
        
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit('UPI入款', 'upi轉帳自動測試')  # 確認公司入帳有生成


    # 刪除存款虛擬幣類型
    @DecorateClass('PFREQ-T7842')
    def test_delete_crypto_wallet_sort(self):
        crypto = ['USDT']
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        self.function_dict['ad'].walletaddressPage().delete_wallet_address_sort()
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit(crypto)  # 確認USDT錢包地址有成功刪除

    # 新增币安_USDT(TRC)
    @DecorateClass('PFREQ-T7843')
    def test_add_desposit_crypto_bnb_trc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('币安_TRC自動測試', 'Binance', 'USDT / USDT(TRC) ( 虚拟币 )', 'USDT(TRC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(TRC)', 'USDT(TRC20)','币安_TRC自動測試', address, 'Binance')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(TRC)', self.money)  # 確認存款類型有生成
 
    # 新增币安_USDT(ERC)
    @DecorateClass('PFREQ-T7844')
    def test_add_desposit_crypto_bnb_erc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('币安_ERC自動測試', 'Binance', 'USDT / USDT(ERC) ( 虚拟币 )', 'USDT(ERC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(ERC)', 'USDT(ERC20)','币安_ERC自動測試', address, 'Binance')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(ERC)', self.money)  # 確認存款類型有生成
    
    # 新增火币_USDT(TRC)
    @DecorateClass('PFREQ-T7845')
    def test_add_desposit_crypto_ht_trc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('火币_TRC自動測試', 'Huobi', 'USDT / USDT(TRC) ( 虚拟币 )', 'USDT(TRC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(TRC)', 'USDT(TRC20)','火币_TRC自動測試', address, 'Huobi')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(TRC)', self.money)  # 確認存款類型有生成

    # 新增imToken_USDT(TRC)
    @DecorateClass('PFREQ-T7846')
    def test_add_desposit_crypto_imtoken_trc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('imToken_TRC自動測試', 'imToken', 'USDT / USDT(TRC) ( 虚拟币 )', 'USDT(TRC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(TRC)', 'USDT(TRC20)','imToken_TRC自動測試', address, 'imToken')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(TRC)', self.money)  # 確認存款類型有生成

    # 新增OLEX_USDT(ERC)
    @DecorateClass('PFREQ-T7847')
    def test_add_desposit_crypto_olex_erc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('OLEX_ERC自動測試', 'OLEX', 'USDT / USDT(ERC) ( 虚拟币 )', 'USDT(ERC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(ERC)', 'USDT(ERC20)','OLEX_ERC自動測試', address, 'OLEX')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(ERC)', self.money)  # 確認存款類型有生成
    
    # 新增TokenPocket_USDT(ERC)
    @DecorateClass('PFREQ-T7848')
    def test_add_desposit_crypto_tokenpocket_erc(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_wallet_address()  # 進入錢包地址
        address = self.function_dict['ad'].walletaddressPage().add_sort_wallet_address('TokenPocket_ERC自動測試', 'TokenPocket', 'USDT / USDT(ERC) ( 虚拟币 )', 'USDT(ERC20)', '1000000')  # 新增銀行分類
        self.function_dict['ad'].walletaddressPage().search_wallet_address(wallet_account = address)
        self.function_dict['ad'].walletaddressPage().wallet_sort_check('USDT/USDT(ERC)', 'USDT(ERC20)','TokenPocket_ERC自動測試', address, 'TokenPocket')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('USDT', address, 'USDT(ERC)', self.money)  # 確認存款類型有生成


    # 移除所有在線商號支付方式
    @DecorateClass('PFREQ-T1960')
    def test_delete_online_bank_sort(self):
        bank = ['线上支付', '银联支付', '京东支付']
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().delete_bank_sort('All|全部', '')

        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay(bank)  # 確認存款類型有生成

    # 新增線上支付
    @DecorateClass('PFREQ-T1967')
    def test_add_online_desposit_onlinepay(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('自動市_线上支付', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '365支付网银', '12345', '54321')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', '自動市_线上支付')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','自動市_线上支付', True)  # 確認存款類型有生成

    # 新增K幣交易所線上支付的銀行掃碼
    @DecorateClass('PFREQ-T6065')
    def test_add_online_desposit_kcurrency_bankscan(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_银行扫码', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, available_amount='100')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_银行扫码')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_银行扫码')  # 確認存款類型有生成
    
    # 新增K幣交易所線上支付的銀行轉帳
    @DecorateClass('PFREQ-T7816')
    def test_add_online_desposit_kcurrency_banktransfer(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_银行转帐', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='网银(WAP)', available_amount='100')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_银行转帐')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_银行转帐')  # 確認存款類型有生成
    
    # 新增K幣交易所線上支付的微信掃碼
    @DecorateClass('PFREQ-T6066')
    def test_add_online_desposit_kcurrency_wechatscan(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_微信扫码', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='微信扫码', available_amount='100')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_微信扫码')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_微信扫码')  # 確認存款類型有生成

    # 新增K幣交易所線上支付的微信轉帳
    @DecorateClass('PFREQ-T6067')
    def test_add_online_desposit_kcurrency_wechattransfer(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_微信转帐', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='微信(WAP)')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_微信转帐')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_微信转帐')  # 確認存款類型有生成

    # 新增K幣交易所線上支付的支付寶掃碼
    @DecorateClass('PFREQ-T6068')
    def test_add_online_desposit_kcurrency_alipayscan(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_支付宝扫码', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='支付宝扫码', available_amount='100')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_支付宝扫码')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_支付宝扫码')  # 確認存款類型有生成

    # 新增K幣交易所線上支付的支付寶轉帳
    @DecorateClass('PFREQ-T6069')
    def test_add_online_desposit_kcurrency_alipaytransfer(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_支付宝转帐', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='支付宝(WAP)')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_支付宝转帐')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_支付宝转帐')  # 確認存款類型有生成

    # 新增K幣交易所線上支付的掃碼支付
    @DecorateClass('PFREQ-T6070')
    def test_add_online_desposit_kcurrency_scanpay(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('K币_扫码支付', '1000000', '线上支付 / 线上支付 ( 线上支付 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='K币扫码', available_amount='1000')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('线上支付', 'K币_扫码支付')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('线上支付/线上支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','K币_扫码支付')  # 確認存款類型有生成

     # 新增銀聯支付
    @DecorateClass('PFREQ-T1968')
    def test_add_online_desposit_unionpay(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('自動市_银联支付', '1000000', '银联支付 / 银联支付 ( 线上支付 )', '365支付网银', '12345', '54321')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('银联支付', '自動市_银联支付')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('银联支付/银联支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_unionpay('银联支付', '银联支付','自動市_银联支付', True)  # 確認存款類型有生成

     # 新增京東支付
    @DecorateClass('PFREQ-T1969')
    def test_add_online_desposit_jdpay(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('自動市_京东支付', '1000000', '京东支付 / 京东支付 ( 线上支付 )', '365支付网银', '12345', '54321')  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('京东支付', '自動市_京东支付')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('京东支付/京东支付')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_jdpay('京东支付', '京东支付','自動市_京东支付', True)  # 確認存款類型有生成


    # 新增順付WellPay我要买-银行卡账号
    @DecorateClass('PFREQ-T6779')
    def test_add_wellpay_bankaccount(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('我要买-银行卡账号', '1000000', '顺付WellPay-我要买入款 / 顺付WellPay-账号入款 ( 顺付WellPay-我要买 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='顺付-Well Pay我要买入款（银行卡账号）',store_type='顺付WellPay-我要买',range_amount=['1','100','100','5000','5000','50000'])  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('顺付WellPay-我要买入款', '我要买-银行卡账号')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('顺付WellPay-我要买入款/顺付WellPay-账号入款')
        # WAP PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_wellpay_account('顺付WellPay-我要买入款', '顺付WellPay-账号入款','我要买-银行卡账号')  # 確認存款類型有生成

    # 新增順付WellPay我要买-支付宝账号
    @DecorateClass('PFREQ-T6780')
    def test_add_wellpay_alipayaccount(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('我要买-支付宝账号', '1000000', '顺付WellPay-我要买入款 / 顺付WellPay-账号入款 ( 顺付WellPay-我要买 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='顺付-Well Pay我要买入款（支付宝账号）',store_type='顺付WellPay-我要买',range_amount=['1','100','100','5000','5000','50000'])  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('顺付WellPay-我要买入款', '我要买-支付宝账号')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('顺付WellPay-我要买入款/顺付WellPay-账号入款')
        # WEB PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_wellpay_account('顺付WellPay-我要买入款', '顺付WellPay-账号入款','我要买-支付宝账号')  # 確認存款類型有生成

    # 新增順付WellPay我要买-微信账号
    @DecorateClass('PFREQ-T6781')
    def test_add_wellpay_wechataccount(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('我要买-微信账号', '1000000', '顺付WellPay-我要买入款 / 顺付WellPay-账号入款 ( 顺付WellPay-我要买 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='顺付-Well Pay我要买入款（微信账号）',store_type='顺付WellPay-我要买',range_amount=['1','100','100','5000','5000','50000'])  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('顺付WellPay-我要买入款', '我要买-微信账号')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('顺付WellPay-我要买入款/顺付WellPay-账号入款')
        # WEB PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_wellpay_account('顺付WellPay-我要买入款', '顺付WellPay-账号入款','我要买-微信账号')  # 確認存款類型有生成

    # 新增順付WellPay我要买-支付宝扫码
    @DecorateClass('PFREQ-T6782')
    def test_add_wellpay_alipayscan(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('我要买-支付宝扫码', '1000000', '顺付WellPay-我要买入款 / 顺付WellPay-扫码入款 ( 顺付WellPay-我要买 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='顺付-Well Pay我要买入款（支付宝扫码）',store_type='顺付WellPay-我要买',range_amount=['1','100','100','5000','5000','50000'])  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('顺付WellPay-我要买入款', '我要买-支付宝扫码')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('顺付WellPay-我要买入款/顺付WellPay-扫码入款')
        # WEB PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_wellpay_account('顺付WellPay-我要买入款', '顺付WellPay-扫码入款','我要买-支付宝扫码')  # 確認存款類型有生成

    # 新增順付WellPay我要买-微信扫码
    @DecorateClass('PFREQ-T6783')
    def test_add_wellpay_wechatscan(self):
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()  # 在線商號
        self.function_dict['ad'].OnlinePay_Branch_Page().add_sort_bank('我要买-微信扫码', '1000000', '顺付WellPay-我要买入款 / 顺付WellPay-扫码入款 ( 顺付WellPay-我要买 )', '收银台', self.zqb_private_sign, bot_id=self.zqb_merchant_id, callback_address=self.zqb_deposit_callback, transfermethod='顺付-Well Pay我要买入款（微信扫码）',store_type='顺付WellPay-我要买',range_amount=['1','100','100','5000','5000','50000'])  # 新增銀行分類
        self.function_dict['ad'].OnlinePay_Branch_Page().search_bank('顺付WellPay-我要买入款', '我要买-微信扫码')
        self.function_dict['ad'].BankAcconut_PageLocator().onlinepay_sort_name_check('顺付WellPay-我要买入款/顺付WellPay-扫码入款')
        # WEB PART
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_wellpay_account('顺付WellPay-我要买入款', '顺付WellPay-扫码入款','我要买-微信扫码')  # 確認存款類型有生成


    # 新增返水/退傭方案並套用
    @DecorateClass('PFREQ-T1970')
    def test_add_rebate_and_commision(self):
        self.test_admin_login()
        self.function_dict['ad'].rebateandcommisionPage().into_commision_refund_program()                               # 進入退傭方案
        self.function_dict['ad'].CommisionPage().add_commision_program(self.commision_program)                       # 新增退傭方案
        self.function_dict['ad'].CommisionPage().into_setting_commision_program(self.commision_program)              # 設定退傭方案存取款
        self.function_dict['ad'].CommisionPage().add_setting_stair()                                                 # 設定退傭方案遊戲退傭
        self.function_dict['ad'].systemmanagementpage().into_agent_management()                                        # 進入體系管理
        self.function_dict['ad'].AgentPage().set_commision_program(self.reseller_account, self.commision_program)    # 套用新增之退傭方案

    # 財務管理 -> 帳號管理 -> 銀行帳號
    @DecorateClass('PFREQ-T2084')
    def test_bank_account_page(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_account()                # 進入銀行帳號
        
        # 宣告參數
        name = "automated_testname"                 # 銀行卡號
        bank_sort = "公司入款 / 公司入款 ( 公司入款 )"  # 所屬分類
        money = int(1000000)                          # 收款限額
        branch = "automated_testbranch"             # 開戶支行
        style = "银行"                              # 帳號類型
        depositMoney = int(2)                       # 存款金額

        # name = 'test_name'                              # 銀行卡號
        # Bank_sort = '公司入款 / 公司入款 ( 公司入款 )'      # 所屬分類
        # money = 10000                                   # 收款限額
        # Branch = 'test_branch'                          # 開戶支行
        # Style = '银行'                                      # 帳號類型
        # Deposit_Money = 2                               # 存款金額

        # 清除之前測試的資料
        while (self.function_dict['ad'].Pay_Branch_Page().check_row(name=name)) != -1:
            self.function_dict['ad'].Pay_Branch_Page().delete_bank_sort(branch='', name=name, bank_sort='')

        id = self.function_dict['ad'].Pay_Branch_Page().add_sort_bank(name, branch, money, style, bank_sort) # 確定新增功能
        self.function_dict['ad'].Pay_Branch_Page().check_search(id, branch)                                  # 確定搜尋功能
        
        # admin 取資料
        admin_AllCount, admin_TodayCount, admin_AllNumber, admin_TodayNumber = self.function_dict['ad'].Pay_Branch_Page().get_withdraw_info(id) # Admin端數值

        # 進入 WAP端 線上存款 
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit('公司入款', name)                          # 選擇存款方式
        self.function_dict['mp'].depositPage().do_company_deposit('測試', depositMoney)                         # 進入線上取款

        # admin 確認存款
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()               # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account) # 查找線上存款紀錄
        self.function_dict['ad'].companyDepositPage().pass_first_deposit()                           # 確定線上存款

        # admin 取資料
        self.function_dict['ad'].financialmanagementPage().into_bank_account()                                                                                    # 進入銀行帳號
        new_Admin_AllCount, new_Admin_TodayCount, new_Admin_AllNumber, new_Admin_TodayNumber = self.function_dict['ad'].Pay_Branch_Page().get_withdraw_info(id) # Admin端數值

        # 確認info有改
        assert new_Admin_AllCount == (admin_AllCount + 1), "總收款次數錯誤"
        assert new_Admin_TodayCount == (admin_TodayCount + 1), "當日收款次數錯誤"
        assert new_Admin_AllNumber == (admin_AllNumber + depositMoney), "總收款總額錯誤"
        assert new_Admin_TodayNumber == (admin_TodayNumber + depositMoney), "當日收款總額錯誤"

        self.function_dict['ad'].Pay_Branch_Page().change_bank_info(id)                                   # 確定修改功能
        # 警示設定功能顯示錯誤, 已開單給PM後續會請RD修正
        self.function_dict['ad'].Pay_Branch_Page().change_bank_warning_setting(id)                        # 確定警示設定功能
        self.function_dict['ad'].Pay_Branch_Page().delete_bank_sort(bank_sort=bank_sort, bank_number=id)    # 確定刪除功能        

    # 財務管理 -> 帳號管理 -> 在線商號
    @DecorateClass('PFREQ-T2086')
    def test_online_merchant_page(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()                                # 進入

        name = 'test_merchant'
        number = '45213546845443154'
        code = 'test_code'
        key = 'test_key'
        count = 8
        page = 'in'
        deposit_money = 2                            # 存款金額

        while (self.function_dict['ad'].OnlineMerchantPage().check_row(name=name, page=page)) != -1:
            self.function_dict['ad'].OnlineMerchantPage().delete_merchant_sort(account=number, name=name, page=page)

        self.function_dict['ad'].OnlineMerchantPage().add_online_marchant(name=name, number=number, code=code, key=key, count=count, page=page, type_name='线上支付')
        old_count, old_value = self.function_dict['ad'].OnlineMerchantPage().get_withdraw_info(account=number, name=name, page=page)
        self.function_dict['ad'].OnlineMerchantPage().check_search(account=number, name=name, page=page)
        self.function_dict['ad'].OnlineMerchantPage().change_merchant_info(account=number, name=name, page=page)
        self.function_dict['ad'].OnlineMerchantPage().change_merchant_warning_setting(account=number, name=name, page=page)

        # 進入 web端 線上存款
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()                                # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()                              # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付', name)     # 選擇存款方式
        self.function_dict['mp'].depositPage().do_all_online_deposit(deposit_money, name)       # 進行線上存款

        # admin 確認存款
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()                       # 進入公司入款
        self.function_dict['ad'].OnlineDepositPage().online_deposit_confirm_once(self.admin_otp)                        # 查找線上存款紀錄

        self.function_dict['ad'].financialmanagementPage().into_bank_online_account()                        # 進入
        new_count, new_value = self.function_dict['ad'].OnlineMerchantPage().get_withdraw_info(account=number, name=name, page=page)
        self.function_dict['ad'].OnlineMerchantPage().delete_merchant_sort(account=number, name=name, page=page)
        self.function_dict['ad'].OnlineMerchantPage().check_delete(account=number, name=name, page=page)

        # 因第三方建單會失敗，故次數與總合應不會增加
        assert old_count == new_count, '收款次數錯誤'
        assert old_value == new_value, '收款總額錯誤'

    # 財務管理 -> 比例設置 -> 手續費用
    @DecorateClass('PFREQ-T2090')
    def test_handing_fee_page(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_handing_fee()                     # 進入

        list, Error_List = self.function_dict['ad'].HandingFeePage().check_save()               # 確認所有存檔按鈕功能 並 取得存檔後之值

        # 進入 WAP端 取線上取款資料
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入取款
        charge, Min, Max = self.function_dict['mp'].withdrawPage().get_withdraw_info() # 抓取 線上取款 之值(進入銀行卡出款確認)

        # 比較 admin 和 web 端之值
        assert Min == str(list[4]), "admin {} 與web資料不同".format(Error_List[4])
        assert Max == str(list[5]), "admin {} 與web資料不同".format(Error_List[5])

    # 運維管理 -> * -> 期數管理
    @DecorateClass('PFREQ-T2100')
    def test_period_management_page(self):
        # 進入 web端 下注急速快三
        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_jisuk3_nwap()                            # 進入彩票遊戲
        bet_record = self.function_dict['mp'].lotteryGamePage().betting_game_new()               # 進入急速快3
        bet_period = bet_record['period']                                                        # 下注急速快3三軍的彩種1 並 回傳下注期數

        # 進入admin端
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_jisuk3_period_management()           # 進入急速快3

        period = 999999999
        results = [i for i in range(100)]

        self.function_dict['ad'].PeriodManagementPage().delete_period(period)                         # 先確認無之前資料，若有則刪除
        self.function_dict['ad'].PeriodManagementPage().add_period(period)                            # 檢查新增功能
        self.function_dict['ad'].PeriodManagementPage().revise_period(period=period, results=results) # 檢查修改功能
        self.function_dict['ad'].PeriodManagementPage().check_seal_and_unseal(period=period)          # 檢查 封盤/開盤 功能
        self.function_dict['ad'].PeriodManagementPage().delete_period(period)                         # 刪除指定期數
        self.function_dict['ad'].PeriodManagementPage().check_delete(period)                          # 檢查刪除功能

        beads_bool = self.function_dict['ad'].PeriodManagementPage().check_beads_result(bet_period)

        # 進入 web端 取得急速快三狀態
        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()                                 # 進入投注紀錄
        old_value = self.function_dict['mp'].lotteryGamePage().get_js3_bet_result(period=bet_period)
        
        # 進入 admin端 確認派彩狀況
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_jisuk3_period_management()                        # 進入急速快3
        self.function_dict['ad'].PeriodManagementPage().check_payout_state(period=bet_period, time='before') # 檢查 派彩狀態 頁面
        self.function_dict['ad'].PeriodManagementPage().check_abolishment(period=bet_period)                 # 檢查作廢功能
        self.function_dict['ad'].PeriodManagementPage().check_payout_state(period=bet_period, time='after')  # 檢查 派彩狀態 頁面

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()                   # 進入投注紀錄
        self.function_dict['mp'].lotteryGamePage().check_abolishment_record(period=bet_period)      # 檢查投注紀錄無此期數注單


    # 運維管理 -> * -> 盤口管理
    @DecorateClass('PFREQ-T2102')
    def test_handicap_management_page(self):
        code = 'code_test'
        # name = 'name_test'
        # state = True
        _min = 1
        _max = 10
        # win = 100
        # sort = 1
        odds_num = 1

        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_js6_odds_management() # 進入極速六合彩 -> 盤口管理
        # self.function_dict['ad'].OddsManagementPage().delete_Odds(code) # 先確認無之前資料，若有則刪除
        # self.function_dict['ad'].OddsManagementPage().add_Odds(code=code, name=name, _min=_min, _max=_max, win=win, sort=sort) # 檢查新增功能
        self.function_dict['ad'].OddsManagementPage().modify_handicap(code, True)
        self.function_dict['ad'].OddsManagementPage().check_handicap_modification(code, True)
        self.function_dict['ad'].OddsManagementPage().modify_handicap(code, False)
        self.function_dict['ad'].OddsManagementPage().check_handicap_modification(code, False)

        try:
            Odds_origin = self.function_dict['ad'].OddsManagementPage().modify_odds(odds_num)

            # 進入 web端 取線上取款資料
            self.test_wap_login()
            self.function_dict['mp'].lotteryGamePage().into_js6_nwap()                                               # 進入線上取款

            info = self.function_dict['mp'].lotteryGamePage().get_odds_info()

            assert info.__contains__(str(odds_num)), "admin 新增的盤口資訊沒有套用到 wap 端"

            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_js6_odds_management() # 進入極速六合彩 -> 盤口管理
            self.function_dict['ad'].OddsManagementPage().modify_odds(Odds_origin)
        except:
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_js6_odds_management() # 進入極速六合彩 -> 盤口管理
            self.function_dict['ad'].OddsManagementPage().modify_odds(Odds_origin)
            raise EOFError('admin 新增的盤口資訊沒有套用到 wap 端')

        # self.function_dict['ad'].basePage().open_base_url()
        # self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)     # 登入admin
        # self.function_dict['ad'].operationmanagementPage().into_js6_odds_management()          # 進入
        # self.function_dict['ad'].OddsManagementPage().revise_Odds(code, state)          # 檢查修改功能
        # self.function_dict['ad'].OddsManagementPage().delete_Odds(code)                 # 刪除指定盤口
        # self.function_dict['ad'].OddsManagementPage().check_delete(code)                # 檢查刪除功能
        
    # 運維管理 -> 外接平台 -> * -> 頻道設置
    @DecorateClass('PFREQ-T2101')
    def test_channel_setting_page(self):
        # 進入 admin端 禁用DT遊戲
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_channel_setting()       # 進入頻道設置
        self.function_dict['ad'].ChannelSettingsPage().into_channel_setting_lgd()       # 進入 LGD 之頻道設定
        self.function_dict['ad'].ChannelSettingsPage().click_all_disable()              # 禁用此品牌所有遊戲

        # 進入 web端 檢查是否進入維護
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_menu_electronic()                                  # 進入 LGD 電子
        self.function_dict['mp'].electronicPage().maintenance_check(is_maintenance=True)            # 檢查 LGD 電子是否進入維護
        
        # 進入 admin端 啟用LGD遊戲
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_channel_setting()       # 進入頻道設置
        self.function_dict['ad'].ChannelSettingsPage().into_channel_setting_lgd()       # 進入 LGD 之頻道設定
        self.function_dict['ad'].ChannelSettingsPage().click_all_enable()               # 啟用此品牌所有遊戲

    # 財務管理 -> 外接平台 -> 現金流水 -> CP現金流水
    @DecorateClass('PFREQ-T4593')
    def test_cp_ledger(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_cp_ledger()                                         # 進入現金流水頁面
        self.function_dict['ad'].CPLedgerPage().search_account(self.web_account)
        self.function_dict['ad'].CPLedgerPage().check_search_member(self.web_account)                             # 檢查查找的帳號
        self.function_dict['ad'].CPLedgerPage().check_transaction_type()                                          # 檢查交易類型
        self.function_dict['ad'].CPLedgerPage().check_select_transaction_time()                                   # 檢查交易時間
        # self.function_dict['ad'].CPLedgerPage().check_export_report(self.brand)
        self.function_dict['ad'].CPLedgerPage().check_record_per_page()
        self.function_dict['ad'].CPLedgerPage().check_business_number_link()
    
    # 財務管理 -> 流水系統 -> 上下分流水 -> 第三方現金流水
    @DecorateClass('PFREQ-T2097')
    def test_third_party_ledger(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_thirdparty_ledger()                                                                # 進入第三方現金流水頁面

        self.function_dict['ad'].ThirdPartyLedgerPage().check_search_member(self.web_account)
        self.function_dict['ad'].ThirdPartyLedgerPage().check_transaction_type()
        self.function_dict['ad'].ThirdPartyLedgerPage().check_wallet_code()
        self.function_dict['ad'].ThirdPartyLedgerPage().check_select_transaction_time()
        self.function_dict['ad'].ThirdPartyLedgerPage().check_record_per_page()
        self.function_dict['ad'].ThirdPartyLedgerPage().check_business_number_link()

    # 財務管理 -> 流水系統 -> 差額報表
    @DecorateClass('PFREQ-T2094')
    def test_different_report(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_difference_report()             # 進入 差額報表 頁面

        self.function_dict['ad'].DifferentReportPage().search_for_time(1)
        diff_report_list = self.function_dict['ad'].DifferentReportPage().check_data()

        # 取得公司入款
        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()     # 進入 公司入款 頁面
        company_list = self.function_dict['ad'].companyDepositPage().get_sum_info('', time='1')
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit() # 進入 人工存入 頁面
        artificial_money = self.function_dict['ad'].ArtificialDeposit().get_all_amount_money('lvbot01', '人工公司入款') # 取得轉帳的總計金額
        company_amount = float(company_list['company_amount']) + float(artificial_money)
        company_list['company_amount'] = company_amount
        assert float(diff_report_list[0]) == float(company_list['company_amount']), f"公司入款頁面與差額報表有異: {float(company_list['company_amount'])} vs {float(diff_report_list[0])}"

        # 取得在線入款
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()      # 進入 在線入款 頁面
        online_list = self.function_dict['ad'].OnlineDepositPage().get_sum_info('', time='1')
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit() # 進入 人工存入 頁面
        artificial_money = self.function_dict['ad'].ArtificialDeposit().get_all_amount_money('lvbot01', '人工在线入款') # 取得轉帳的總計金額
        online_amount = float(online_list['online_amount']) + float(artificial_money)
        online_list['online_amount'] = online_amount
        assert float(diff_report_list[2]) == float(online_list['online_amount']), f"在線入款頁面與差額報表有異: {float(online_list['online_amount'])} vs {float(diff_report_list[2])}"

        # 取得出款申請
        # self.function_dict['ad'].financialmanagementPage().into_withdraw()             # 進入 出款申請 頁面
        # withdraw_list = self.function_dict['ad'].OnlineDepositPage().get_sum_info('', time='1')
        # assert float(diff_report_list[4]) == float(withdraw_list['online_amount']), "出款申請頁面與差額報表有異"
        

    # 財務管理 -> 外接平台 -> 額度轉換
    @DecorateClass('PFREQ-T2060')
    def test_external_plateform_wallet_transfer(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_credit_conversion()                                                                # 進入外接平台 -> 額度轉換頁面

        self.function_dict['ad'].ExternalPlateformWalletPage().check_select_transaction_time()                                                   # 檢查交易時間
        self.function_dict['ad'].ExternalPlateformWalletPage().check_search_member_account(member_account=self.web_account, shareholder=self.shareholder, \
            generalagent=self.generalagent, agent=self.reseller_account)                                                        # 檢查搜尋帳號
        self.function_dict['ad'].ExternalPlateformWalletPage().check_search_order_id(shareholder=self.shareholder)
        self.function_dict['ad'].ExternalPlateformWalletPage().check_wallet_transfer(shareholder=self.shareholder)

    # # 財務管理 -> 外接平台 -> 餘額查詢        # 未避免cmweb操作衝突，除了hy，其餘品牌skip
    # def test_external_plateform_balance_inquire(self):

    #     # -------------------------------------------- cmweb --------------------------------------------
    #     self.test_cmweb_login()
    #     self.function_dict['cmweb'].deposit_log_management().into_vender_wallet()
    #     vender_name = self.function_dict['cmweb'].vendor_wallet_page().get_vender_name()
    #     balance = self.function_dict['cmweb'].vendor_wallet_page().get_amount()

    #     # -------------------------------------------- admin --------------------------------------------
    #     self.function_dict["ad"].basePage().windows_to_top()
    #     self.test_admin_login()
    #     self.function_dict['ad'].financialmanagementPage().into_over_inquire()                                                                     # 進入餘額查詢頁面
    #     self.function_dict['ad'].ExternalPlateformBalanceInquire().check_wallet_name(vender_name)
    #     self.function_dict['ad'].ExternalPlateformBalanceInquire().check_balance(balance)
    #     self.function_dict['ad'].ExternalPlateformBalanceInquire().check_threshold()

    # # 財務管理 -> 外接平台 -> 現金流水      # 未避免cmweb操作衝突，除了hy，其餘品牌skip
    # def test_external_plateform_ledger(self):
    #     apply_type_options = [2, 2, 1, 1]
    #     apply_type = ['入款', '入款', '出款', '出款']
    #     amount = ['10', '5', '20', '15']
    #     remark = ['', 'test1', 'test2', '']
    #     confirm_reject_list = [True, None, False, True]
    #     apply_status = ['已建单', '已建单', '已建单', '已建单']

    #     self.test_admin_login()
    #     self.function_dict['ad'].financialmanagementPage().into_ledger_in_external_planform()                                                                    # 進入外接平台現金流水頁面

    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_select_transaction_time()                                                               # 檢查交易時間
    #     for i in range(len(apply_type_options)):                                                                                            # 新增資料
    #         self.function_dict['ad'].ExternalPlateformLedgerPage().append_new_data(type_option=apply_type_options[i], amount=amount[i], remark=remark[i])
    #     amount.reverse()
    #     remark.reverse()
    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_apply_type_amount_remark(apply_type=apply_type, amount=amount, remark=remark)
    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_search_apply_type()
    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_search_apply_status()
    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_audit_status()
    #     # -------------------------------------------------------- CmWebPage --------------------------------------------------------
    #     self.test_cmweb_login()
    #     self.function_dict['cmweb'].deposit_log_management().into_vender_wallet()
    #     amount_before = self.function_dict['cmweb'].vendor_wallet_page().get_amount()
    #     self.function_dict['cmweb'].deposit_log_management().into_recharge_page()
    #     difference = self.function_dict['cmweb'].recharge_management_page().click_confirm_reject_and_get_difference(actions=confirm_reject_list, apply_status=apply_status)
    #     self.function_dict['cmweb'].deposit_log_management().into_vender_wallet()
    #     amount_after = self.function_dict['cmweb'].vendor_wallet_page().get_amount()
    #     assert amount_after - amount_before == difference, f'CmWebPage 廠商錢包 ... 金額顯示錯誤 {amount_after} 應為-> {amount_before + difference}'
    #     # -------------------------------------------------------- CmWebPage --------------------------------------------------------
    #     self.test_admin_login()                                                             # 開啟admin網站
    #     self.function_dict['ad'].financialmanagementPage().into_ledger_in_external_planform()                            # 進入外接平台現金流水頁面
    #     self.function_dict['ad'].ExternalPlateformLedgerPage().check_apply_status(apply_status=apply_status)
    
    # 運維管理 -> 注單中心
    def test_ticket_center_total_check(self):
        # =========前台下注=========
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['mp'].lotteryPage().into_jisuk3()       # 進入極速快3
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().js3)  # 下注極速快3
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        self.function_dict['ad'].Record_js3 = record

        self.switch_home_page()                 # 退出極速快3遊戲頁

        self.function_dict['mp'].menuPage().into_menu_lottery()  # 進入彩票遊戲
        self.function_dict['mp'].lotteryPage().into_hk()        # 進入香港六合彩
        record = self.function_dict['mp'].lotteryGamePage().betting_game(self.function_dict['mp'].lotteryGamePage().betting_hk)  # 號碼下注
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_recording()
        record = self.function_dict['mp'].gameRecordPage().game_lottery(record)
        self.function_dict['ad'].Record_hk = record

        # ===========注單中心操作=============
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().intoOrderCenter()                                                                     # 進入運維管理 -> 注單中心
        self.function_dict['ad'].ticketcenterPage().ticketnumber_memberaccount_period_check(self.function_dict['ad'].Record_hk, self.web_account)                 # 單號、帳號、期數 搜尋檢查
        self.function_dict['ad'].ticketcenterPage().type_of_channel_check()                                                                      # 頻道類型、頻道分類、產品類型、玩法類型 搜尋檢查
        self.function_dict['ad'].ticketcenterPage().payout_status_check()                                                                        # 派彩狀態 搜尋檢查
        self.function_dict['ad'].ticketcenterPage().shareholder_generalagent_agent(self.shareholder, self.generalagent, self.reseller_account)   # 股東、總代、代理 搜尋檢查
        self.function_dict['ad'].ticketcenterPage().record_sort_check_bet_time()                                                                 # 下注時間排序檢查
        self.function_dict['ad'].ticketcenterPage().record_sort_check_order_money()                                                              # 注額排序檢查
        self.function_dict['ad'].ticketcenterPage().record_sort_check_payout_money()                                                             # 派彩排序檢查
        self.function_dict['ad'].ticketcenterPage().operation_field_check(self.function_dict['ad'].Record_js3, self.shareholder, self.generalagent)               # 紀錄操作欄位檢查 
        self.function_dict['ad'].ticketcenterPage().check_25_50_100_500()                                                                        # 檢查 分別已25、50、100、500筆 檢視是否正確
        self.function_dict['ad'].ticketcenterPage().check_total_subtotal()                                                                       # 注額、派彩、損益、打碼 小計與總量檢查
        self.function_dict['ad'].ticketcenterPage().autorefresh_check()
        self.function_dict['ad'].ticketcenterPage().check_export(self.web_account)                                                               # 匯出資料比對

    # 運維管理 -> 注單中心 -> 派彩統計
    @DecorateClass('PFREQ-T2099')
    def test_payout_statistics(self):
        # ------------------------------------------------ 前台 ------------------------------------------------ 
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center() # 進入會員專區
        self.function_dict['mp'].memberCenterPage().into_member_order() # 進入投注紀錄
        self.sleep(60)
        wap_record = self.function_dict['mp'].gameRecordPage().get_nwap_record_detail()
        # 避免時間差導致前台彩票在收集record時, 彩票還未開獎紀錄導致後續判斷失敗, 先行設定flag
        # for Line691 use
        mark = 0
        # ------------------------------------------------ 派彩統計 ------------------------------------------------
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_order_center() # 進入注單中心
        total_record = self.function_dict['ad'].ticketcenterPage().get_total_information_by_shareholder(self.shareholder)
        self.function_dict['ad'].payoutstatiscticsPage().into_payout_statistic() # 進入派彩統計頁面
        self.function_dict['ad'].payoutstatiscticsPage().check_select_transaction_time() # 檢查點擊派彩時間
        self.function_dict['ad'].payoutstatiscticsPage().check_total_record_by_shareholder(self.shareholder, total_record)
        self.function_dict['ad'].basePage().refresh_browser()
        self.function_dict['ad'].payoutstatiscticsPage().into_payout_statistic() # 進入派彩統計頁面
        total_name, payout_list, record = self.function_dict['ad'].payoutstatiscticsPage().check_total_record_by_member(self.web_account, wap_record)
        mark = self.function_dict["ad"].payoutstatiscticsPage().compare_data(total_name, payout_list, record, mark)
        while mark != None and mark > 0:
            self.function_dict['mp'].basePage().windows_to_top()
            self.function_dict["mp"].basePage().refresh_browser()
            wap_record = self.function_dict['mp'].gameRecordPage().get_nwap_record_detail()
            mark = self.function_dict["ad"].payoutstatiscticsPage().compare_data(total_name, payout_list, record, mark)
            if mark == None:
                break

    # 紅包 -> 掃雷 -> 廳別管理
    @DecorateClass('PFREQ-T1971')
    def test_mine_sweeping_hall_management(self):
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_mine_sweeping_hall_management()
        data = self.function_dict['mp'].redEnvelopePage().get_bot_hall_data()

        if self.function_dict['ad'].hall_management_page().is_bot_hall_exist(data['name']):
            data = self.function_dict['ad'].hall_management_page().generate_data()

        self.function_dict['ad'].hall_management_page().mine_sweeping_add_hall(data)
        self.function_dict['ad'].hall_management_page().mine_sweeping_check_add_hall(data)
        # ----------------------------------- wap -----------------------------------
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_mine_sweeping()
        self.function_dict['mp'].redEnvelopePage().into_mine_sweeping_hall(data, gl.get_value('ENV'))
        self.function_dict['mp'].redEnvelopePage().into_give_red_envelope()
        self.function_dict['mp'].redEnvelopePage().check_give_red_envelope_data(data)

    # 紅包 -> 牛牛 -> 廳別管理
    @DecorateClass('PFREQ-T1972')
    def test_niu_niu_hall_management(self):
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_niu_niu_hall_management()
        data = self.function_dict['mp'].redEnvelopePage().get_bot_hall_data()

        if self.function_dict['ad'].hall_management_page().is_bot_hall_exist(data['name']):
            data = self.function_dict['ad'].hall_management_page().generate_data()

        self.function_dict['ad'].hall_management_page().niu_niu_add_hall(data)
        self.function_dict['ad'].hall_management_page().niu_niu_check_add_hall(data)
        # ----------------------------------- wap -----------------------------------
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_niu_niu()
        self.function_dict['mp'].redEnvelopePage().into_niu_niu_hall(data, gl.get_value('ENV'))
        self.function_dict['mp'].redEnvelopePage().into_give_red_envelope()
        self.function_dict['mp'].redEnvelopePage().check_give_red_envelope_data(data)

    def Betting_Limit(self, into_game_func):
        # 登入admin
        self.test_admin_login()
        # 進入遊戲時會順便檢查遊戲是否在維護
        into_game_func()
        self.function_dict['ad'].BettingLimitPage().check_modify_function()

    # 極速六合彩 -> 投注限額
    def test_betting_limit_js6(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().into_js6BetLimit)

    # 五分快3 -> 投注限額
    def test_betting_limit_k3(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoK3BetLimit)

    # 五分PK拾 -> 投注限額
    def test_betting_limit_pk10(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoPK10BetLimit)

    # 五分時時彩 -> 投注限額
    def test_betting_limit_sscb(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoSSCBetLimit)

    # 五分幸運28 -> 投注限額
    def test_betting_limit_xy28(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoXY28BetLimit)

    # 三分六合彩 -> 投注限額
    def test_betting_limit_3f6(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().into3F6BetLimit)

    # 香港六合彩 -> 投注限額
    def test_betting_limit_hk6(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().into_hk6BetLimit)

    # 福彩3D -> 投注限額
    def test_betting_limit_fc3d(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoFC3DBetLimit)

    # 排列三 -> 投注限額
    def test_betting_limit_pl3(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoPL3BetLimit)

    # 分分六合彩 -> 投注限額
    def test_betting_limit_ff6(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoFF6BetLimit)

    # 極速時時彩 -> 投注限額
    def test_betting_limit_jsssc(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().into_jssscBetLimit)

    # 極速PK拾 -> 投注限額
    def test_betting_limit_jspk10(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().into_jspk10BetLimit)

    # 極速快3 -> 投注限額
    def test_betting_limit_jisuk3(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoJSK3BetLimit)

    # 幸運飛艇 -> 投注限額
    def test_betting_limit_lucky_airship(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoLuckyAirshipBetLimit)

    # PC蛋蛋 -> 投注限額
    def test_betting_limit_pc(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoPCBetLimit)

    # 台灣幸運28 -> 投注限額
    def test_betting_limit_tw(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoTWBetLimit)

    # 加拿大幸運28 -> 投注限額
    def test_betting_limit_canada(self):
        self.Betting_Limit(self.function_dict['ad'].operationmanagementPage().intoCANADABetLimit)

    def Game_Setting(self, into_admin_game_func, into_web_game_func, is_maintenance):
        self.test_admin_login()
        into_admin_game_func()

        try:
            self.function_dict['ad'].GameSetting().auto_maintain_on_off(True)
            self.function_dict['ad'].GameSetting().check_maintain_on_off(False)
            # --------------------------------------- 檢查前台是否有進行維護 ---------------------------------------
            self.test_wap_login()
            self.function_dict['mp'].menuPage().into_menu_lottery()
            # 進入遊戲時會順便檢查遊戲是否在維護
            into_web_game_func(is_maintenance)
            # ---------------------------------------
            self.test_admin_login()
            # 進入遊戲時會順便檢查遊戲是否在維護
            into_admin_game_func()
            self.function_dict['ad'].GameSetting().opening_operation_setting(True, 5, 0)
            self.function_dict['ad'].GameSetting().check_opening_operation_setting(False, 5, 0)
            self.function_dict['ad'].GameSetting().settlement_operation_setting(True, 180, 120)
            self.function_dict['ad'].GameSetting().check_settlement_operation_setting(False, 180, 120)
        except AssertionError as e:
            self.function_dict['ad'].GameSetting().auto_maintain_on_off()
            self.function_dict['ad'].GameSetting().opening_operation_setting()
            self.function_dict['ad'].GameSetting().settlement_operation_setting()
            raise e

        try:
            self.function_dict['ad'].GameSetting().auto_maintain_on_off(False)
            self.function_dict['ad'].GameSetting().check_maintain_on_off(True)
            self.function_dict['ad'].GameSetting().opening_operation_setting(False, 10, 5)
            self.function_dict['ad'].GameSetting().check_opening_operation_setting(True, 10, 5)
            self.function_dict['ad'].GameSetting().settlement_operation_setting(False, 600, 600)
            self.function_dict['ad'].GameSetting().check_settlement_operation_setting(True, 600, 600)
        except AssertionError as e:
            self.function_dict['ad'].GameSetting().auto_maintain_on_off()
            self.function_dict['ad'].GameSetting().opening_operation_setting()
            self.function_dict['ad'].GameSetting().settlement_operation_setting()
            raise e
    
    # 極速六合彩 -> 遊戲設置
    def test_game_setting_js6(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().into_js6GameSetting, self.function_dict['mp'].lotteryPage().into_js6, is_maintenance=True)
    
    # 香港六合彩 -> 遊戲設置
    def test_game_setting_hk6(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().into_hk6GameSetting, self.function_dict['mp'].lotteryPage().into_hk, is_maintenance=True)
    
    # 福彩3D -> 遊戲設置
    def test_game_setting_fc3d(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().intoFC3DGameSetting, self.function_dict['mp'].lotteryPage().into_fu3d, is_maintenance=True)
    
    # 極速時時彩 -> 遊戲設置
    def test_game_setting_jsssc(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().into_jssscGameSetting, self.function_dict['mp'].lotteryPage().into_jsssc, is_maintenance=True)
    
    # 極速PK拾 -> 遊戲設置
    def test_game_setting_jspk10(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().into_jspk10GameSetting, self.function_dict['mp'].lotteryPage().into_jspk10, is_maintenance=True)
    
    # 極速快3 -> 遊戲設置
    def test_game_setting_jisuk3(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().intoJSK3GameSetting, self.function_dict['mp'].lotteryPage().into_jisuk3, is_maintenance=True)
        
    # PC蛋蛋 -> 遊戲設置
    def test_game_setting_pc(self):
        self.Game_Setting(self.function_dict['ad'].operationmanagementPage().intoPCGameSetting, self.function_dict['mp'].lotteryPage().intoPcegg, is_maintenance=True)
    
    # 運維管理 -> 外接平台 -> 遊戲列表
    # 只有做 AG電子 的測試
    @DecorateClass('PFREQ-T2096')
    def test_game_list(self):
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_game_list()
        self.function_dict['ad'].GameList().into_game_list_ag_electronics()
        self.function_dict['ad'].GameList().check_game_name()
        self.function_dict['ad'].GameList().check_all_opening_status()
        self.function_dict['ad'].GameList().check_all_recommendation_status()

    # 運維管理 -> 注單中心 -> 注單校驗
    def test_ticket_check_operating(self):
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().intoOrderCenter()                                 # 進入運維管理 -> 注單中心
        self.function_dict['ad'].ticketcheckPage().ticket_number_check(self.function_dict['ad'].Record_hk['ticket_name'])      # 注單校驗操作

    # 系統管理 -> 系統設定 -> 網站設定
    def test_website_setting_page(self):
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        account = self.web_account
        
        # 會員註冊-禁用
        # agent = self.brand + "bot_agent"
        # 使用"takochang"代理, 總代ccp88888, 股東bcp88888
        agent = "default_agent"
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting() # 進入網站設定頁
        self.function_dict['ad'].WebsiteSetting().member_registered(agent, setting=False) # 會員註冊設定
        self.sleep(70)
        self.test_wap_login()
        self.function_dict['mp'].mainPage().into_register_page()
        # 會員註冊-啟用
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()        
        self.function_dict['ad'].WebsiteSetting().member_registered(agent)
        self.sleep(70)
        self.function_dict['mp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().into_register_page()   
        self.function_dict['mp'].registerPage().do_register(self.bot_id, '123456', '111111', captcha=0)
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_member_list()
        # self.function_dict['ad'].MemberList().check_member(self.bot_id, self.brand)
        self.function_dict['ad'].MemberList().check_member(account, self.brand)

        #會員試玩-禁用
        self.function_dict['ad'].basePage().open_base_url()  # 開啟後台網站
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().memeber_play_setting(setting=False)
        #會員試玩-啟用
        self.function_dict['ad'].basePage().open_base_url()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().memeber_play_setting()

        # 會員聯盟-禁用
        self.function_dict['ad'].basePage().open_base_url()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().member_alliancr(setting=False)
        # 會員聯盟-啟用
        self.function_dict['ad'].basePage().open_base_url()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().member_alliancr()

        # 代理註冊-禁用
        self.function_dict['ad'].basePage().open_base_url()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()        
        self.function_dict['ad'].WebsiteSetting().agent_registered(self.brand,setting=False)
        self.sleep(70)
        self.driver.get(self.web_url)
        self.function_dict['mp'].mainPage().into_register_page()
        self.function_dict['mp'].registerPage().doagent_registered(self.bot_id, '123456', captcha=0)
        # 代理註冊-啟用
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().agent_registered(self.brand)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().into_register_page()
        self.function_dict['mp'].registerPage().doagent_registered(self.bot_id, '123456', captcha=0)          
        reseller_url = self.get_url()
        # assert reseller_url == "http://{}-reseller-{}.paradise-soft.com.tw/login?back=%2F".format(self.brand, self.brand_env), "驗證碼開啟無法註冊"
        self.function_dict["wp"].basePage().switch_home_page()

        # 站點維護-禁用
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().status_setting(setting=0)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.sleep(1)
        web_url = self.function_dict["wp"].basePage().get_url()
        # assert web_url == "https://{}-web-{}.paradise-soft.com.tw/stop".format(self.brand, self.brand_env), "沒有禁用"
        self.function_dict['mp'].basePage().windows_to_top()
        self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].mainPage().front_web_banned(web_url)
        # 站點維護-啟用
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().status_setting(setting=1)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.sleep(1)
        self.function_dict['mp'].memberPage().refresh_browser() # 重新啟用前台網頁後, 會出現一般公告, 刷新去除公告彈窗
        self.function_dict['mp'].mainPage().into_register_page()
        # 站點維護-自動維護
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().status_setting(setting=2)
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().check_status()
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        web_url = self.function_dict["wp"].basePage().get_url()
        self.function_dict['mp'].basePage().windows_to_top()
        self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].mainPage().front_web_banned(web_url)
        # 開啟站點
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().status_setting()
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.sleep(1)
        self.function_dict['mp'].mainPage().into_register_page()
   
        # 先行測試已有的左側浮窗開關流程
        self.test_wap_login()
        self.function_dict["wp"].mainPage().left_float_windows_action()
        # 手機優惠大廳
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().mobile_hall()
        self.function_dict['ad'].MarketCenterPage().into_float_window_management()
        self.function_dict['ad'].FloatWindows().into_left_revising()
        # self.function_dict['ad'].FloatWindows().mobile_hall_link()
        self.function_dict['ad'].FloatWindows().left_floating_add()
        self.sleep(120)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.function_dict['mp'].mainPage().check_mobile_hall()
        web_url = self.function_dict["wp"].basePage().get_url()
        assert web_url == "https://www.google.com.tw/?hl=zh-TW", "網址錯誤" 
        self.function_dict['mp'].basePage().switch_home_page()

        # 手機優惠大廳reset_左側浮窗
        self.test_admin_login()
        self.function_dict['ad'].MarketCenterPage().into_float_window_management()
        self.function_dict['ad'].FloatWindows().left_revising_reset()
        self.function_dict["ad"].FloatWindows().left_floating_reset()
        self.sleep(70)

        # 手機/郵箱/QQ號碼/微信/推薦人設定-隱藏
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().registered_setting()
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['mp'].registerPage().check_Register(self.bot_id,'123456', '111111', display=0, captcha=0) # 設計為無法註冊, 僅測試個欄位是否可用
        # self.function_dict['mp'].basePage().close_login_board() # 此流程暫定不跑, 暫定註解
        # self.function_dict['mp'].mainPage().logout() # 此流程暫定不跑, 暫定註解
        # 手機/郵箱/QQ號碼/微信/推薦人設定-必填
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().registered_setting(setting=2)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['mp'].registerPage().check_Register(self.bot_id,'123456', '111111', display=2, captcha=0) # 設計為無法註冊, 僅測試個欄位是否可用
        # self.function_dict['mp'].basePage().close_login_board() # 此流程暫定不跑, 暫定註解
        # self.function_dict['mp'].mainPage().logout() # 此流程暫定不跑, 暫定註解
        # 手機/郵箱/QQ號碼/微信/推薦人設定-選填
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().registered_setting(setting=1)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['mp'].registerPage().check_Register(self.bot_id,'123456', '111111', display=1, captcha=0) # 設計為無法註冊, 僅測試個欄位是否可用
        # self.function_dict['mp'].basePage().close_login_board() # 此流程暫定不跑, 暫定註解
        # self.function_dict['mp'].mainPage().logout() # 此流程暫定不跑, 暫定註解

        # 額度轉換框-一律顯示
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().transfer_status(setting=0)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_menu_game()
        self.function_dict['mp'].chessPage().check_transferstatus()
        # 額度轉換框-不顯示
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().transfer_status(setting=1)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_menu_game()
        self.function_dict['mp'].chessPage().check_transferstatus()
        # 額度轉換框-显示 当金额少於 $
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().transfer_status(setting=2)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_menu_game()
        self.function_dict['mp'].chessPage().check_transferstatus()

        # 會員預警(會通知於slack)
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().member_warning(self.brand)

        # 超時登出-會員系統
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().member_timeout_setting(1)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_wap_login()
        self.sleep(70)
        self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].mainPage().logout_checker()
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().member_timeout_setting(7000)
        # 超時登出-營運系統
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().user_timeout_setting(1)
        self.sleep(70)
        self.function_dict['ad'].basePage().refresh_browser()
        self.function_dict['ad'].loginPage().logout_checker()
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().user_timeout_setting(7000)
        # 超時登出-代理系統
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().reseller_timeout(1)
        self.sleep(70)
        self.driver.get(self.reseller_url)
        self.test_reseller_login()
        self.sleep(70)
        self.refresh_browser()
        self.function_dict['rp'].loginPage().logout_checker()
        self.driver.get(self.admin_url)
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().reseller_timeout(7000)

        # 超時登出-帳號自動解鎖
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().lock_timeout(1)
        self.function_dict['ad'].WebsiteSetting().lock_timeout(30)

        # 微信二維碼/提示文案
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().wechat_setting()
        self.sleep(70)
        self.another_open_wap(close=False)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().skip_app_download()
        self.function_dict['mp'].menuPage().into_wechat()
        self.function_dict['mp'].servicePage().wechat_message()
        self.sleep(1)
        self.another_open_wap(close=True)
        self.sleep(1)

        # QQ號碼
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().qq_setting(self.brand)
        self.sleep(70)
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.function_dict['mp'].mainPage().check_qq_link(self.brand) 

        # 在線客服
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().livechat_setting()
        option = self.function_dict['ad'].WebsiteSetting().customer_service_select(choose=0)
        self.sleep(120)
        # self.driver.get(self.web_url)
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.sleep(120)
        self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].mainPage().check_livechat_link(self.brand, cs=option)
        self.function_dict['mp'].basePage().switch_home_page()
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().customerservice_setting()
        option = self.function_dict['ad'].WebsiteSetting().customer_service_select(choose=1)
        self.sleep(120)
        # self.driver.get(self.web_url)
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.sleep(120)
        self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].mainPage().check_livechat_link(self.brand, cs=option)
        self.function_dict['mp'].basePage().switch_home_page()
        # 返回原始設定 "在線客服"
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().livechat_setting()
        self.function_dict['ad'].WebsiteSetting().customer_service_select(choose=0)
                 
        # 郵箱
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().email_setting(self.brand)
        self.sleep(120)
        # self.driver.get(self.web_url)
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.function_dict['mp'].mainPage().check_email_link(self.brand)

        # 先行測試已有的右側浮窗開關流程
        self.test_wap_login()
        self.function_dict["wp"].mainPage().right_float_windows_action()
        # 站內客服
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().customerservice_setting()
        self.function_dict['ad'].MarketCenterPage().into_float_window_management()
        self.function_dict['ad'].FloatWindows().into_right_revising()
        # self.function_dict['ad'].FloatWindows().customerservice_link()
        self.function_dict["ad"].FloatWindows().right_floating_add()
        self.sleep(180)
        self.function_dict["wp"].basePage().open_base_url()
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.function_dict['mp'].mainPage().check_customerservice_link()
        web_url = self.function_dict["wp"].basePage().get_url()
        # assert web_url == "http://mynah-client-uat.paradise-soft.com.tw/chatroom?company=FM3SEAMrJdrVs&site=WS3SSBeEZf2zA", "網址錯誤"  
        self.function_dict['mp'].basePage().switch_home_page()

        # 站內客服reset_右側浮窗
        self.test_admin_login()
        self.function_dict['ad'].MarketCenterPage().into_float_window_management()
        self.function_dict['ad'].FloatWindows().right_revising_reset()
        self.function_dict["ad"].FloatWindows().right_floating_reset()
        self.sleep(70)

        # APP下載框
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_admin_setting()
        self.function_dict['ad'].WebsiteSetting().app_setting()
        self.sleep(70)
        # self.driver.get(self.web_url)
        self.function_dict['mp'].mainPage().firstOpenBaseUrl()
        self.sleep(1)
        self.function_dict['mp'].mainPage().check_app_download()

    #  財務管理 -> 上分管理 -> 公司
    @DecorateClass('PFREQ-T2062')           
    def test_company_deposit(self):
        self.test_wap_login()

        # 三筆公司存款
        for _ in range(0,3):
            self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
            self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
            self.function_dict['mp'].depositPage().nwap_checktr_deposit('支付宝', '支付寶轉帳自動測試', '支付宝转帐', self.money)
            self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer()

        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        self.function_dict['ad'].companyDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].companyDepositPage().company_deposit_status()  # 產生三種交易狀態

        self.function_dict['ad'].companyDepositPage().search_all(self.web_account, '銀行自動測試', self.admin_account
                        , self.reseller_account, self.generalagent, self.shareholder, self.money)  

        self.function_dict['ad'].companyDepositPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].companyDepositPage().subtotal_and_total(self.web_account) # 測試小計及總計
        self.function_dict['ad'].companyDepositPage().check_pages() # 判斷頁數及尾頁餘數數量正確
        # self.function_dict['ad'].companyDepositPage().check_export_report(self.brand) # 匯出測試  #V2版 待修

        '''目前有問題
        self.function_dict['ad'].companyDepositPage().other_sort(self.web_account) # 排序測試 
        '''
    # 財務管理 -> 上分管理 -> 在線
    @DecorateClass('PFREQ-T2075')
    def test_online_deposit(self):
        self.test_wap_login()

        # 三筆在線存款
        for _ in range(0,3):
            self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
            self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
            self.function_dict['mp'].depositPage().check_jdpay('京东支付', '京东支付','自動市_京东支付')  # 確認存款類型有生成
            self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_京东支付')
        
        # ADMIN PART
        self.test_admin_login()
        self.sleep(15)  # 待第三方建單失敗，自動拒絕
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].OnlineDepositPage().online_deposit_status(self.admin_otp)  # 產生三種交易狀態

        self.function_dict['ad'].OnlineDepositPage().search_all(self.web_account,'銀行自動測試',self.admin_account
                        ,self.reseller_account,self.generalagent,self.shareholder,self.money)  

        self.function_dict['ad'].OnlineDepositPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].OnlineDepositPage().subtotal_and_total(self.web_account) # 測試小計及總計
        self.function_dict['ad'].OnlineDepositPage().check_pages() # 判斷頁數及尾頁餘數數量正確
        # self.function_dict['ad'].OnlineDepositPage().check_export_report(self.brand) # 匯出測試  #V2版 待修

        '''目前有問題
         # 排序測試 
        '''

    # 財務管理 -> 上分管理 -> 上分總覽
    @DecorateClass('PFREQ-T2078')  
    def test_deposit_overview(self):
        # ADMIN PART
        self.test_admin_login()
        money = {}
        # 取得公司入款頁面的第一筆轉帳金額
        self.function_dict['ad'].financialmanagementPage().into_company_deposit()  # 進入公司入款
        company_pay_money = self.function_dict['ad'].companyDepositPage().get_pay_money(self.web_account)
        money.setdefault('公司入款', company_pay_money)

        # 取得在線入款頁面的第一筆轉帳金額
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        online_pay_money = self.function_dict['ad'].OnlineDepositPage().get_pay_money(self.web_account)
        money.setdefault('在线入款', online_pay_money)
        
        self.function_dict['ad'].financialmanagementPage().into_total_deposit()  # 進入入款總覽

        self.function_dict['ad'].DepositeOverview().search_all(self.web_account, self.admin_account, self.reseller_account
                        , self.generalagent, self.shareholder, money)  
                        
        self.function_dict['ad'].DepositeOverview().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].DepositeOverview().check_pages() # 判斷頁數及尾頁餘數數量正確

    @DecorateClass('PFREQ-T2081')
    def test_member_wallet(self):
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_wallet_conversion()
        cp_wallet = self.function_dict['mp'].thirdPartyWalletPage().do_wallet_return()
        self.function_dict['mp'].thirdPartyWalletPage().do_walletre_fresh()
        self.function_dict['mp'].thirdPartyWalletPage().nwap_do_wallet_check(cp_wallet)

        self.function_dict['mp'].thirdPartyWalletPage().nwap_do_wallet_conversion('主钱包','AG', 1)
        wallet_list_front = self.function_dict['mp'].thirdPartyWalletPage().get_name_and_money()
        
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_member_wallet()  # 進入在線入款

        self.function_dict['ad'].MemberWallet().search_all(self.web_account, wallet_list_front)  
        self.function_dict['ad'].MemberWallet().page_range()  # 判斷頁數及尾頁餘數數量正確
        
    # 三筆出款申請
    @DecorateClass('PFREQ-T2092')
    def test_withdraw_page(self):        
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_nwap_change_bank('北京', '五環', self.withdraw_password)  # 設定銀行開戶網點
        
        for _ in range(0,3):
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
            self.function_dict['mp'].withdrawPage().do_nwap_withdraw(self.withdraw, self.withdraw_password, self.brand)  # 取款
            self.sleep(10)

        #ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        self.function_dict['ad'].withdrawPage().cancel_second_withdraw(self.web_account)
        self.function_dict['ad'].withdrawPage().reject_third_withdraw(self.web_account)
        self.function_dict['ad'].withdrawPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].withdrawPage().check_pages() # 判斷頁數及尾頁餘數數量正確
        self.function_dict['ad'].withdrawPage().check_total_subtotal(self.web_account) # 總計小計

        # ===========出款申請操作=============
        self.function_dict['ad'].withdrawPage().search_minamount() # 申請金額
        self.function_dict['ad'].withdrawPage().search_member(self.web_account) # 會員帳號
        self.function_dict['ad'].withdrawPage().remark(self.web_account) # 備註操作 
        self.function_dict['ad'].withdrawPage().check_autorefresh() # 自動刷新
        self.function_dict['ad'].withdrawPage().check_locklogin(self.admin_account) # 鎖定人員
        self.function_dict['ad'].withdrawPage().check_auditlogin(self.admin_account) # 確認人員
        self.function_dict['ad'].withdrawPage().check_shareholder_generalagent_agent(self.shareholder, self.generalagent, self.reseller_account) # 股東/總代/代理
        self.function_dict['ad'].withdrawPage().search_via_level() # 會員級別
        self.function_dict['ad'].withdrawPage().check_payout_status() # 出款狀態
        self.function_dict['ad'].withdrawPage().search_cardnumber(self.web_account) # 出款卡號              
        self.function_dict['ad'].withdrawPage().check_export_report(self.web_account, self.brand) # 匯出測試
        self.function_dict['ad'].financialmanagementPage().into_withdraw_general() # 進入出款總攬
        self.function_dict['ad'].withdrawPage().ledger_withdraw(self.web_account) # 流水號查找 
    

    # 三筆出款申請_CGpay
    @DecorateClass('PFREQ-T5971')
    def test_cgpay_withdraw_page(self):        
        phone = '13500' + str('%06d' %random.randint(0,999999))     
        # ADMIN PART 
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().change_member_phone(self.web_account, phone, self.admin_otp)  # 修改會員手機號碼

        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_nwap_change_virtual_card(self.withdraw_password, phone)  # 設定虛擬錢包
                      
        for _ in range(0,3):            
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
            self.function_dict['mp'].withdrawPage().do_nwap_cgpay_withdraw(self.money, self.withdraw_password, self.brand)  # CGpay取款
            self.sleep(10)        

        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        self.function_dict['ad'].withdrawPage().cancel_second_withdraw(self.web_account)
        self.function_dict['ad'].withdrawPage().reject_third_withdraw(self.web_account)
        self.function_dict['ad'].withdrawPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].withdrawPage().check_pages() # 判斷頁數及尾頁餘數數量正確
        self.function_dict['ad'].withdrawPage().check_total_subtotal(self.web_account) # 總計小計

        # ===========出款申請操作=============
        self.function_dict['ad'].withdrawPage().search_minamount() # 申請金額
        self.function_dict['ad'].withdrawPage().search_member(self.web_account) # 會員帳號
        self.function_dict['ad'].withdrawPage().remark(self.web_account) # 備註操作 
        self.function_dict['ad'].withdrawPage().check_autorefresh() # 自動刷新
        self.function_dict['ad'].withdrawPage().check_locklogin(self.admin_account) # 鎖定人員
        self.function_dict['ad'].withdrawPage().check_auditlogin(self.admin_account) # 確認人員
        self.function_dict['ad'].withdrawPage().check_shareholder_generalagent_agent(self.shareholder, self.generalagent, self.reseller_account) # 股東/總代/代理
        self.function_dict['ad'].withdrawPage().search_via_level() # 會員級別
        self.function_dict['ad'].withdrawPage().check_payout_status() # 出款狀態
        self.function_dict['ad'].withdrawPage().search_walletaddress(self.web_account) # 錢包地址              
        self.function_dict['ad'].withdrawPage().check_export_report(self.web_account, self.brand) # 匯出測試
        self.function_dict['ad'].financialmanagementPage().into_withdraw_general() # 進入出款總攬
        self.function_dict['ad'].withdrawPage().ledger_withdraw(self.web_account) # 流水號查找

    # 會員管理 >層級管理 >入款OTP(公司入款)
    @DecorateClass('PFREQ-T6079')
    def test_deposit_otp_nwap(self):
        self.test_admin_login()
        # ===========開啟otp=============
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_on_deposit_otp()  # 開啟OTP
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().search_member(self.web_account)
        otp_code = self.function_dict['ad'].MemberList().get_member_otp()
        # ===========前台操作=============
        self.test_wap_login()
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit('公司入款', '銀行自動測試')  # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_company_deposit('銀行自動測試', self.money, otp_code)
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
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
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')
        # ===========關閉otp=============
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_off_deposit_otp()  # 關閉OTP

    # 會員管理 >層級管理 >入款OTP(支付寶面對面)
    @DecorateClass('PFREQ-T6078')
    def test_deposit_alipay_f2f_otp_nwap(self):
        self.test_admin_login()
        # ===========開啟otp=============
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_on_deposit_otp()  # 開啟OTP
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().search_member(self.web_account)
        otp_code = self.function_dict['ad'].MemberList().get_member_otp()
        # ===========前台操作=============
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_qr_deposit('支付宝', 'bot', '支付宝面对面扫码', self.money) # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_desposit_weChat_alipayf2f(otp_code)
        self.function_dict['mp'].menuPage().into_member_center() # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('公司入款', self.money) # 確認產生充值中紀錄
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
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')
        # ===========關閉otp=============
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_off_deposit_otp()  # 關閉OTP

    # 會員管理 >層級管理 >入款OTP(微信轉帳)
    @DecorateClass('PFREQ-T6077')
    def test_deposit_wechat_transfer_otp_nwap(self):
        self.test_admin_login()
        # ===========開啟otp=============
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_on_deposit_otp()  # 開啟OTP
        self.function_dict['ad'].membermanagementpage().into_member_list()   # 進入會員列表
        self.function_dict['ad'].MemberList().search_member(self.web_account)
        otp_code = self.function_dict['ad'].MemberList().get_member_otp()
        # ===========前台操作=============
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        real_money = self.function_dict['mp'].depositPage().nwap_checktr_deposit('微信', '微信轉帳自動測試', '微信转帐', self.money)
        self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer(otp_code)
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('公司入款', real_money) # 確認產生充值中紀錄
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
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'公司入款')
        # ===========關閉otp=============
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_level_management() # 進入層級管理
        self.function_dict['ad'].levelmanagementPage().turn_off_deposit_otp()  # 關閉OTP

    # 財務管理 -> 下分管理 -> 人工提出
    @DecorateClass('PFREQ-T2091')
    def test_manwithdraw_page(self):       
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_manual_withdraw() # 進入人工提出       
        self.function_dict['ad'].ManwithdrawPage().pass_manpower(self.web_account,self.money) # 人工出款
        # ===========ADMIN=============
        self.function_dict['ad'].ManwithdrawPage().search_today_manpower_by_member(self.web_account) # 搜尋今日申請會員
        self.function_dict['ad'].ManwithdrawPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].ManwithdrawPage().check_pages() # 判斷頁數及尾數餘數數量正確
        self.function_dict['ad'].ManwithdrawPage().check_total_subtotal(self.web_account) # 總計小計

        # ===========人工提出操作=============
        self.function_dict['ad'].ManwithdrawPage().search_member(self.web_account) # 會員帳號
        self.function_dict['ad'].ManwithdrawPage().search_amount() # 提出金額        
        self.function_dict['ad'].ManwithdrawPage().check_shareholder_generalagent_agent(self.shareholder, self.generalagent, self.reseller_account) # 股東/總代/代理
        self.function_dict['ad'].financialmanagementPage().into_withdraw_general() # 進入出款總覽
        self.function_dict['ad'].ManwithdrawPage().ledger_manpower(self.web_account) # 流水號查找
        self.function_dict['ad'].financialmanagementPage().into_manual_withdraw() # 進入人工提出
        wallet = ('%.2f' %self.function_dict['ad'].ManwithdrawPage().get_wallet(self.web_account)) # 取得當前金額
        # ===========前台=============
        self.function_dict['mp'].basePage().open_base_url()
        self.test_wap_login()
        if self.brand == "aa":
            wallet_before = ('%.2f' %self.function_dict['mp'].menuPage().get_balance_wallet())
        else:
            self.function_dict['mp'].menuPage().into_wallet_conversion()
            wallet_before = ('%.2f' %self.function_dict['mp'].thirdPartyWalletPage().get_main_wallet_nwap())                      
        assert str(wallet_before) == str(wallet) , f'error number equal: {wallet_before} != {wallet}'

    # 財務管理 -> 下分管理 -> 下分總覽
    @DecorateClass('PFREQ-T2093')
    def test_withdrawgeneral_page(self):
        # 正是步驟
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw_general() # 進入出款總攬
        self.function_dict['ad'].withdrawGeneralPage().search_today_withdraw_general_by_member(self.web_account) # 搜尋今日申請會員
        self.function_dict['ad'].withdrawGeneralPage().page_range(self.web_account) # 每頁最大筆數測試
        self.function_dict['ad'].withdrawGeneralPage().check_pages() # 判斷尾頁及尾數餘數數量正確
        self.function_dict['ad'].withdrawGeneralPage().check_total_subtotal(self.web_account) # 總計

        # ===========出款總攬操作=============
        self.function_dict['ad'].withdrawGeneralPage().search_member(self.web_account) # 會員帳號
        self.function_dict['ad'].withdrawGeneralPage().check_shareholder_generalagent_agent(self.shareholder, self.generalagent, self.reseller_account) # 股東/總代/代理
        self.function_dict['ad'].withdrawGeneralPage().search_via_level() # 會員級別
        self.function_dict['ad'].withdrawGeneralPage().detail_withdraw(self.web_account) # 出款申請明細
        self.function_dict['ad'].withdrawGeneralPage().detail_manpower(self.web_account) # 人工出款明細

    # 維運管理 -> 即時注單
    @DecorateClass('PFREQ-T2095')
    def test_realtime_lottery_page(self):
        # ------------------------------------------------ 前台 ------------------------------------------------
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()                                                                               
        self.function_dict['mp'].memberCenterPage().into_member_order()
        wap_record = self.function_dict['mp'].gameRecordPage().get_nwap_record_detail()

        # ------------------------------------------- 後台 即時注單頁面-------------------------------------------
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_instant_order_center()
        self.function_dict['ad'].RealTimeOrderPage().product_period_check()
        self.function_dict['ad'].RealTimeOrderPage().basic_table_check()
        self.function_dict['ad'].RealTimeOrderPage().alert_action_check()
        self.function_dict['ad'].RealTimeOrderPage().history_period_action(wap_record)
        self.function_dict['ad'].RealTimeOrderPage().sort_check_action(wap_record)
        
    # 下注頁面統一使用(先以api test_lottery_bet_order取代)
    @DecorateClass('PFREQ-T2059')
    def test_bet_lottery(self, multi=False):
        # =========前台下注=========
        self.test_wap_login()
        lottery_record_list = []
        if self.brand == "ttmj":
            self.function_dict['mp'].lotteryGamePage().into_hk_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jsssc_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jspk10_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_pcegg_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jisu11to5_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jisuk3_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_fu3d_nwap()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()

        elif self.brand == "aa":
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shez100_stock, 'shez100', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_hs300_stock, 'hs300', 2)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szzs_stock, 'szzs', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szbqsf_stock, 'szbqsf', 2)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shez1000sf_stock, 'shez1000sf', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szagzssf_stock, 'szagzssf', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_hkhszswf_stock, 'hkhszswf', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_btcusd_stock, 'btcusd', 2)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szsyzsbf_stock, 'szsyzsbf', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shezazbf_stock, 'shezazbf', 2)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_cdpshf_stock, 'cdpshf', 1)
            self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_kc50shf_stock, 'kc50shf', 2)
        
        else:
            self.function_dict['mp'].lotteryGamePage().into_hk6_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jsssc_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jspk10_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_pcegg_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jisu11to5_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_jisuk3_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()
            self.function_dict['mp'].lotteryGamePage().into_fu3d_new()
            lottery_record_list.append(self.function_dict['mp'].lotteryGamePage().betting_game_new())
            self.function_dict['mp'].lotteryGamePage().back_home_page()

    # ----------------- 指數遊戲 ------------------
    ### 1 為定位玩法   2 為雙面玩法
    def test_stock_index(self, into_game_func, stock, van):
        records = []
        self.test_wap_login()

        into_game_func()
        self.function_dict['mp'].lotteryGamePage().check_periods_aa(2, stock)
        self.function_dict['mp'].lotteryGamePage().stock_tab(van)
        stock_record = self.function_dict['mp'].lotteryGamePage().stock_game()
        
        self.function_dict['mp'].lotteryGamePage().check_manual_aa(stock)

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        record = self.function_dict['mp'].gameRecordPage().game_lottery_nwap(stock_record)
        records.append(record)
        # 此僅需要下注資料，故不至admin比對，在uat_nwap_regression時才會進行比對
        # if not gl.get_value('ENV').__contains__('prod'):
        #     # ADMIN PART
        #     self.test_admin_login()
        #     self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
        #     self.function_dict['ad'].CheckRecord().check_stock_recode(records)

    # 財務管理 -> 上分管理 -> 人工存入
    @DecorateClass('PFREQ-T2103')
    def test_artificial_deposit_page(self):
        # ------------------------------------------------ 前台動作 ------------------------------------------------
        self.test_wap_login()
        wallet_balance = self.function_dict['mp'].menuPage().get_balance_wallet()
        # ------------------------------------------------ 後台動作 ------------------------------------------------
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        account_id = self.web_account
        # # for _ in range(5):
        # #     self.function_dict['ad'].ArtificialDeposit().add_new_deposit_action(account_id)
        self.function_dict['ad'].ArtificialDeposit().add_new_deposit_action(account_id)
        self.function_dict['ad'].ArtificialDeposit().basic_search_setting_action()
        all_info_record = self.function_dict['ad'].ArtificialDeposit().after_search_get_all_data()
        self.function_dict['ad'].ArtificialDeposit().table_check_action(all_info_record)
        deposit_amount = self.function_dict['ad'].ArtificialDeposit().mandeposit_group_normal_action(all_info_record)
        # 系統時間獲取
        # # systemtime, systemsec = self.function_dict['ad'].ArtificialDeposit().system_time_return_action()
        # 回到tab[1]的地方繼續比對, 並把全部資料已入帳比對完成
        self.function_dict['ad'].ArtificialDeposit().mandeposit_check_action()
        # ------------------------------------------------ 前台動作 ------------------------------------------------
        # 重回前台拿取錢包金額
        self.function_dict['mp'].basePage().windows_to_top()
        self.function_dict['mp'].mainPage().refresh_browser()
        self.function_dict['mp'].mainPage().sleep(1)
        new_wallet = self.function_dict['mp'].menuPage().get_balance_wallet()
        # 比較前台金額是否成功添加
        self.function_dict['ad'].ArtificialDeposit().wallet_balance_diff(wallet_balance, deposit_amount, new_wallet)
        # 取消用流程start
        self.function_dict["ad"].basePage().windows_to_top()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        self.function_dict['ad'].ArtificialDeposit().add_new_deposit_action(account_id)
        self.function_dict['ad'].ArtificialDeposit().mandeposit_cancel_action()
        # -----------------------------------------------------------------------
        # excel 批次新增
        self.function_dict['mp'].basePage().windows_to_top()
        self.function_dict['mp'].mainPage().refresh_browser()
        self.function_dict['mp'].mainPage().sleep(1)
        wallet_balance = self.function_dict['mp'].menuPage().get_balance_wallet()

        self.function_dict['ad'].basePage().windows_to_top()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        # 製作excel表
        self.function_dict['ad'].ArtificialDeposit().excelMadeForBatchAdd(account_id, self.brand, current=False)
        self.function_dict['ad'].ArtificialDeposit().excelMadeForBatchAdd(account_id, self.brand, current=True)
        # 批次流程start
        temp = self.function_dict['ad'].ArtificialDeposit().batchAddDepositAction(self.web_account, self.brand)
        # 重回前台拿取錢包金額
        self.function_dict["mp"].basePage().windows_to_top()
        self.function_dict["mp"].mainPage().refresh_browser()
        self.function_dict["mp"].mainPage().sleep(1)
        new_wallet = self.function_dict['mp'].menuPage().get_balance_wallet()
        # 比較前台金額是否成功添加
        self.function_dict['ad'].ArtificialDeposit().wallet_balance_diff(wallet_balance, temp, new_wallet)


    # 財務管理 -> 流水系統 -> 上下分報表
    @DecorateClass('PFREQ-T2956')
    def test_financial_report_page(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_financial_report()          # 進入 財務報表 頁面
        self.function_dict['ad'].FinancialReportPage().search_for_time(3)
        self.function_dict['ad'].FinancialReportPage().search_for_agent(self.reseller_account)   # 查找代理
        data_list = self.function_dict['ad'].FinancialReportPage().get_data()               # 財務報表數據

        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()     # 進入 公司入款 頁面
        company_dict = self.function_dict['ad'].companyDepositPage().get_sum_info(self.reseller_account, time='3')
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()      # 進入 在線入款 頁面
        online_dict = self.function_dict['ad'].OnlineDepositPage().get_sum_info(self.reseller_account, time='3')
        self.function_dict['ad'].financialmanagementPage().into_withdraw()                   # 進入 出款申請 頁面
        withdraw_dict = self.function_dict['ad'].withdrawPage().get_sum_info(self.reseller_account, time='3')  # 取得出款申請金額

        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()            # 進入 人工存入 頁面
        list_for_company = self.function_dict['ad'].ArtificialDeposit().get_amount_data(self.reseller_account, ['人工公司入款'], time='3')          # 取得人工公司入款金額
        list_for_online = self.function_dict['ad'].ArtificialDeposit().get_amount_data(self.reseller_account, ['人工在线入款'], time='3')          # 取得人工在线入款金額
        list_for_manual_deposit = self.function_dict['ad'].ArtificialDeposit().get_amount_data(self.reseller_account, ['其他','取消出款','负数额度归零','人工存入'], time='3')       # 取得轉帳的總計金額
        list_for_give_discount = self.function_dict['ad'].ArtificialDeposit().get_amount_data(self.reseller_account, ['全选','返点优惠'], time='3')          # 取得優惠的總計金額
        list_for_give_back = self.function_dict['ad'].ArtificialDeposit().get_amount_data(self.reseller_account, ['返点优惠'], time='3')         # 取得返點優惠的總計金額

        for_company = round(float(company_dict['company_amount']) + float(list_for_company[0]), 2)
        for_online = round(float(online_dict['online_amount']) + float(list_for_online[0]), 2)
        list_for_give_discount[1] = round(float(list_for_give_discount[1]) + float(company_dict['company_discount']) + float(online_dict['online_discount']), 2)

        self.function_dict['ad'].financialmanagementPage().into_manual_withdraw()           # 進入 人工提出 頁面
        for_manual_withdrawal = self.function_dict['ad'].ManwithdrawPage().get_withdrawal_data(self.reseller_account, time='3')            # 取得提出金額

        self.function_dict['ad'].financialmanagementPage().into_cp_ledger()                 # 進入 現金流水 頁面
        for_give_back = self.function_dict['ad'].CPLedgerPage().get_back_data(self.reseller_account,['全选','返水'], time='3')              # 取得返水金額
        for_give_back = round(float(list_for_give_back[1]) + float(for_give_back), 2)

        self.function_dict['ad'].FinancialReportPage().verify_data(data_list, for_company, withdraw_dict, for_online, list_for_give_discount, list_for_manual_deposit, for_manual_withdrawal, for_give_back) # 比對資料

    # 報表管理 -> 一般報表/頻道報表/每日報表
    @DecorateClass('PFREQ-T2981')
    def test_three_reports_page(self):
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_financial_report()                  # 進入 財務報表 頁面
        self.function_dict['ad'].FinancialReportPage().search_for_time(1)                           # 查找今日
        self.function_dict['ad'].FinancialReportPage().search_for_agent(self.reseller_account)      # 查找代理
        financial_report_data = self.function_dict['ad'].FinancialReportPage().get_data()           # 財務報表數據

        self.function_dict['ad'].reportmanagementPage().into_general_report()                       # 進入 一般報表  頁面
        self.function_dict['ad'].generalReportPage().search_for_time(1)                             # 查找今日
        self.function_dict['ad'].generalReportPage().search_for_agent(self.reseller_account)        # 查找代理
        gereral_report_data = self.function_dict['ad'].generalReportPage().get_total_data()         # 一般報表數據

        self.function_dict['ad'].reportmanagementPage().into_channel_report()                       # 進入 頻道報表  頁面
        self.function_dict['ad'].channelReportPage().search_for_time(1)                             # 查找今日
        self.function_dict['ad'].channelReportPage().search_for_agent(self.reseller_account)        # 查找代理
        channel_report_data = self.function_dict['ad'].channelReportPage().get_total_data()         # 頻道報表數據

        self.function_dict['ad'].reportmanagementPage().into_daily_report()                         # 進入 每日報表  頁面
        self.function_dict['ad'].dailyReportPage().search_for_time(1)                               # 查找今日
        self.function_dict['ad'].dailyReportPage().search_for_agent(self.reseller_account)          # 查找代理
        daily_report_bet, daily_report_fee = self.function_dict['ad'].dailyReportPage().get_total_data() # 每日報表數據
        
        self.function_dict['ad'].dailyReportPage().verify_data(financial_report_data, gereral_report_data, channel_report_data, daily_report_bet, daily_report_fee) # 驗證資料


    # 運營風控 -> 運營風控(新版) -> 出入款總覽
    @DecorateClass('PFREQ-T2991')
    def test_operational_risk_new(self):
        self.test_admin_login()
        # 取得公司入款
        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()     # 進入 公司入款 頁面
        company_dict = self.function_dict['ad'].companyDepositPage().get_sum_info(self.reseller_account, time='1')
        # 取得在線入款
        self.function_dict['ad'].financialmanagementPage().into_enter_online_deposit()      # 進入 在線入款 頁面
        online_dict = self.function_dict['ad'].OnlineDepositPage().get_sum_info(self.reseller_account, time='1')
        # 取得人工存入
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()            # 進入 人工存入 頁面
        artificial_company = self.function_dict['ad'].ArtificialDeposit().get_all_amount_money(self.web_account, '人工公司入款') # 取得轉帳的總計金額
        self.function_dict['ad'].ArtificialDeposit().refresh_browser()
        artificial_online = self.function_dict['ad'].ArtificialDeposit().get_all_amount_money(self.web_account, '人工在线入款') # 取得轉帳的總計金額
        self.function_dict['ad'].ArtificialDeposit().refresh_browser()
        artificial_virtural = self.function_dict['ad'].ArtificialDeposit().get_all_amount_money(self.web_account, '人工虚拟币入款') # 取得轉帳的總計金額
        artificial_amount = float(artificial_company) + float(artificial_online) + float(artificial_virtural)
        
        # 取得出款申請
        self.function_dict['ad'].financialmanagementPage().into_withdraw()                   # 進入 出款申請 頁面
        withdraw_dict = self.function_dict['ad'].withdrawPage().get_sum_info(self.reseller_account, time='1')  # 取得出款申請金額
        # 取得人工提出
        self.function_dict['ad'].financialmanagementPage().into_manual_withdraw()            # 進入 人工提出 頁面
        artificial_withdraw = self.function_dict['ad'].ManwithdrawPage().get_option_withdraw(self.shareholder, time='1', option='手动申请出款') # 取得人工提出的總計金額
        withdraw_dict['withdraw_amount'] = "%.2f" %(float(withdraw_dict['withdraw_amount']) + float(artificial_withdraw))
        # 取得出入款總覽
        self.function_dict['ad'].operationriskcontrolpage().into_overview_deposits_withdrawals()                  # 進入 出入款總覽 頁面
        self.function_dict['ad'].operationriskcontrolpage().search_for_time(1)                           # 查找今日
        self.function_dict['ad'].operationriskcontrolpage().search_for_shareholder(self.shareholder)     # 查找股東
        total_deposit, total_withdrawal = self.function_dict['ad'].operationriskcontrolpage().get_report_data()           # 出入款總覽數據

        self.function_dict['ad'].operationriskcontrolpage().verify_data(company_dict, online_dict, artificial_amount, withdraw_dict, total_deposit, total_withdrawal) # 驗證資料

    @DecorateClass('PFREQ-T2058')
    def test_language_check(self):
        error_list = []
        message = ''
        
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()
        message = self.function_dict['ad'].loginPage().language()
        if message != '':
            error_list.append(message)

        self.test_admin_login()
        message = self.function_dict['ad'].loginPage().language()
        if message != '':
            error_list.append(message)
        
        if len(error_list) != 0:
            raise EOFError(f'內容包含繁體字 {error_list}')
    
    # 測試匯出按鈕
    @DecorateClass('PFREQ-T2105')
    def test_check_export_btn(self):
        error_list = []
        self.test_admin_login()
        self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('注單中心'))
        self.function_dict['ad'].financialmanagementPage().into_company_deposit() # 公司
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('公司'))
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit() # 在線
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('在線'))
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit() # 人工存入
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('人工存入'))
        self.function_dict['ad'].financialmanagementPage().into_withdraw() # 下分申請 
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('下分申請'))
        self.function_dict['ad'].financialmanagementPage().into_cp_ledger() # 上下分流水 
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('上下分流水'))
        self.function_dict['ad'].financialmanagementPage().into_financial_report() # 流水系統 -> 上下分報表
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('上下分報表'))
        self.function_dict['ad'].reportmanagementPage().into_general_report() # 一般報表
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('一般報表'))
        self.function_dict['ad'].reportmanagementPage().into_effective_member_report() # 有效會員
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('有效會員'))
        self.function_dict['ad'].reportmanagementPage().into_channel_report() # 頻道報表
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('頻道報表'))
        self.function_dict['ad'].membermanagementpage().into_member_list() # 會員列表
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('會員列表'))
        self.function_dict['ad'].membermanagementpage().into_member_analysis() # 會員分析
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('會員分析'))
        self.function_dict['ad'].systemmanagementpage().into_login_log() # 登入日誌
        error_list.append(self.function_dict['ad'].basePage().check_export_btn ('登入日誌'))

        result= []

        for message in error_list:
            if message != None:
                result.append(message)
        if len(result) > 0:
            raise EOFError(f'頁面有缺匯出icon, {result}')
        
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
                    