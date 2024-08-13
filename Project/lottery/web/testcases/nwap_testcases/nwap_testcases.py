import unittest
import sys
import os
import datetime, random, re

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
            if key == 'mp':
                cls.open_url(cls, function, cls.mobile_url)
                function.mainPage().maintenance()

        cls.test_all_windows_mini(cls)
        cls.function_dict['mp'].mainPage().windows_to_top() # 切換視窗

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
        cls.function_dict['mp'] = MobilePage(cls.driver_list[-1], cls.wait_time, cls.mobile_url, cls.skipTest)  # 導入Web全部頁面
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
        self.function_dict['mp'].basePage().windows_to_top()
        self.function_dict['mp'].mainPage().skip_app_download()

    # 測試-註冊後登出
    @DecorateClass('PFREQ-T1801')
    def test_register_logout(self):
        self.test_skip_app_download()
        self.function_dict['mp'].mainPage().into_nwap_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%m%d%S')
        self.function_dict['mp'].registerPage().do_register_nwap(self.bot_id, '123456', '111111')
        self.function_dict['mp'].mainPage().nwap_close_login_board()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().do_logout()
        self.function_dict['mp'].mainPage().logout_checker()

    # 測試-註冊
    def test_register(self):
        self.function_dict['mp'].mainPage().into_register_page()
        self.bot_id = datetime.datetime.now().strftime('bot%j%H%M%S')
        self.function_dict['mp'].registerPage().do_register(self.bot_id, '123456', '111111')
        self.function_dict['mp'].mainPage().nwap_close_login_board()

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
            self.function_dict['mp'].mainPage().nwap_close_login_board()  # 關閉登入公告  
        
    # 紅包 -> 掃雷下注 & 對前後台注單
    @DecorateClass('PFREQ-T2020')
    def test_mine_sweeping_betting_nwap(self):
        self.test_wap_login()
        record = []
        if gl.get_value('ENV').__contains__('prod'):
            data = self.function_dict['mp'].redEnvelopePage().get_prod_bot_hall_data(0) # 掃雷 0/ 牛牛 1
        else:
            data = self.function_dict['mp'].redEnvelopePage().get_bot_hall_data()
        betting_data = {'amount': random.randint(5, 10), 'number': random.randint(0, 9)}

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
        betting_data['name'] = '红包扫雷'
        record.append(self.function_dict['mp'].gameRecordPage().check_record_front_end_nwap(betting_data))
        ## -------------------------------- 後台 --------------------------------
        if not gl.get_value('ENV').__contains__('prod'):
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()
            self.function_dict['ad'].CheckRecord().check_red_envelope_record(record)

    # 紅包 -> 牛牛下注 & 對前後台注單
    @DecorateClass('PFREQ-T2021')
    def test_niu_niu_betting_nwap(self):
        self.test_wap_login()
        record = []
        if gl.get_value('ENV').__contains__('prod'):
            data = self.function_dict['mp'].redEnvelopePage().get_prod_bot_hall_data(1)   # 掃雷 0/ 牛牛 1
        else:
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
        betting_data['name'] = '红包牛牛'
        record.append(self.function_dict['mp'].gameRecordPage().check_record_front_end_nwap(betting_data))
        ## -------------------------------- 後台 --------------------------------
        if not gl.get_value('ENV').__contains__('prod'):
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()
            self.function_dict['ad'].CheckRecord().check_red_envelope_record(record)

    # 站內消息
    @DecorateClass('PFREQ-T2178')
    def test_station_news(self):
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_message()
        self.function_dict['mp'].messagePage().delete_messages()
        
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
        self.function_dict['mp'].messagePage().messages_check_nwap(data)

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
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_company_deposit('公司入款', '銀行自動測試')  # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_company_deposit('銀行自動測試', self.money)
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

    # 測試支付寶面對面
    @DecorateClass('PFREQ-T1839')
    def test_desposit_alipay_f2f(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_qr_deposit('支付宝', 'bot', '支付宝面对面扫码', self.money) # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_desposit_weChat_alipayf2f()
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

    # 測試微信面對面
    @DecorateClass('PFREQ-T1842')
    def test_desposit_wechat_f2f(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_qr_deposit('微信', 'bot', '微信面对面扫码', self.money) # 確認公司入帳有生成
        self.function_dict['mp'].depositPage().do_desposit_weChat_alipayf2f()
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

    # 測試支付寶轉帳
    @DecorateClass('PFREQ-T1840')
    def test_desposit_alipay_transfer(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().nwap_checktr_deposit('支付宝', '支付寶轉帳自動測試', '支付宝转帐', self.money)
        self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer()
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

    # 測試微信轉帳
    @DecorateClass('PFREQ-T1845')
    def test_desposit_wechat_transfer(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        real_money = self.function_dict['mp'].depositPage().nwap_checktr_deposit('微信', '微信轉帳自動測試', '微信转帐', self.money)
        self.function_dict['mp'].depositPage().do_desposit_wechat_alipay_transfer()
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

     # 測試線上支付
    @DecorateClass('PFREQ-T1848')
    def test_desposit_onlinepay(self):
        # before test action
        self.test_wap_login()
        # Wap  
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_onlinepay('线上支付', '线上支付','自動市_线上支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_线上支付')
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('在线入款', self.money, '线上支付') # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        # 預期會因第三方建單失敗，故先將判斷隱藏
        # if deposit_result == True:
        #     self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對
        # else:
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_fail_record(tra_money,'在线入款') # 進入入款紀錄比對
        self.test_wap_login()
        wallet_after=self.function_dict['mp'].menuPage().get_balance_wallet()
        assert wallet_before == wallet_after, f'充值失敗時，充值前{wallet_before} 與 充值失敗後{wallet_after} 金額不同'

    # 測試銀聯支付
    @DecorateClass('PFREQ-T1849')
    def test_desposit_unionpay(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_unionpay('银联支付', '银联支付','自動市_银联支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_银联支付')
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('在线入款',self.money, '线上支付') # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        # 預期會因第三方建單失敗，故先將判斷隱藏
        # if deposit_result == True:
        #     self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對
        # else:
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_fail_record(tra_money,'在线入款') # 進入入款紀錄比對
        self.test_wap_login()
        wallet_after=self.function_dict['mp'].menuPage().get_balance_wallet()
        assert wallet_before == wallet_after, f'充值失敗時，充值前{wallet_before} 與 充值失敗後{wallet_after} 金額不同'

    # 測試京東支付
    @DecorateClass('PFREQ-T1850')
    def test_desposit_jdpay(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()  # 進入會員中心
        self.function_dict['mp'].memberCenterPage().into_deposit()  # 進入充值
        self.function_dict['mp'].depositPage().check_jdpay('京东支付', '京东支付','自動市_京东支付')  # 確認存款類型有生成
        self.function_dict['mp'].depositPage().do_all_online_deposit(self.money,'自動市_京东支付')
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_entry_record('在线入款',self.money, '线上支付') # 確認產生充值中紀錄
        self.sleep(10) #等待 若為三方建單失敗，系統自動拒絕
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        self.function_dict['ad'].OnlineDepositPage().search_today_deposit_by_member(self.web_account)  # 搜尋今日申請會員
        deposit_result = self.function_dict['ad'].OnlineDepositPage().check_deposit_auto_reject()  # 確認最新一筆申請
        tra_money,offer_money,total_money,handling_money=self.function_dict['ad'].OnlineDepositPage().get_money_info(self.money)
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        # 預期會因第三方建單失敗，故先將判斷隱藏
        # if deposit_result == True:
        #     self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_record(tra_money,offer_money,total_money,wallet_before,'在线入款',handling_money) # 進入入款紀錄比對
        # else:
        self.function_dict['mp'].Store_Record_Page().nwap_check_money_entry_fail_record(tra_money,'在线入款') # 進入入款紀錄比對
        self.test_wap_login()
        wallet_after=self.function_dict['mp'].menuPage().get_balance_wallet()
        assert wallet_before == wallet_after, f'充值失敗時，充值前{wallet_before} 與 充值失敗後{wallet_after} 金額不同'

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
        self.function_dict['mp'].memberInfoPage().do_nwap_change_bank('北京', '五環', self.withdraw_password)  #設定銀行卡號
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
        total_money,Charge=self.function_dict['mp'].withdrawPage().do_nwap_withdraw(self.withdraw, self.withdraw_password, self.brand)  # 取款
        Decimal_point = self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_output_record('在线提现',total_money,Charge,'银行') # 確認產生充值中紀錄   Decimal_point為小數點差異
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  # 搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  # 確認最新一筆申請
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        owner_money = self.function_dict['mp'].memberCenterPage().get_owner_money()
        self.function_dict['mp'].memberCenterPage().into_deposit_out_report()  # 進入線上取款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_after_check_money_output_record(self.withdraw,wallet_before,Charge,Decimal_point,owner_money,'银行') # 進入入款紀錄比對


    # 測試CGPay出款
    @DecorateClass('PFREQ-T5973')
    def test_cgpay_withdraw(self):
        # before test action
        phone = '13500' + str('%06d' %random.randint(0,999999))
        # ADMIN
        self.test_admin_login()   
        self.function_dict['ad'].membermanagementpage().into_member_list()  # 進入會員列表  
        self.function_dict['ad'].MemberList().change_member_phone(self.web_account, phone, self.admin_otp)  # 修改會員手機號碼
        self.function_dict['ad'].MemberList().delete_virtual_wallet(self.web_account)  # 刪除虛擬錢包

        # Wap
        self.test_wap_login()
        wallet_before=self.function_dict['mp'].menuPage().get_balance_wallet()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_nwap_change_virtual_card(self.withdraw_password, phone)  # 設定虛擬錢包
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_withdraw()  # 進入線上取款
        total_money,Charge=self.function_dict['mp'].withdrawPage().do_nwap_cgpay_withdraw(self.withdraw, self.withdraw_password, self.brand)  # 取款
        Decimal_point = self.function_dict['mp'].Store_Record_Page().nwap_before_check_money_output_record('在线提现',total_money,Charge,'CGPay') # 確認產生充值中紀錄   Decimal_point為小數點差異
        # ADMIN PART
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  #  進入出款申請
        self.function_dict['ad'].withdrawPage().search_today_withdraw_by_member(self.web_account)  #  搜尋今日申請會員
        self.function_dict['ad'].withdrawPage().pass_first_withdraw(self.web_account)  #  確認最新一筆申請
        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        owner_money = self.function_dict['mp'].memberCenterPage().get_owner_money()
        self.function_dict['mp'].memberCenterPage().into_deposit_out_report()  # 進入線上取款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_after_check_money_output_record(self.withdraw,wallet_before,Charge,Decimal_point,owner_money,'CGPay') # 進入入款紀錄比對


    # 測試-選單功能
    @DecorateClass('PFREQ-T2110')
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
        self.function_dict['mp'].menuPage().into_news_nwap()

    @DecorateClass('PFREQ-T2181')
    def test_into_together(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_together()

    @DecorateClass('PFREQ-T4449')
    def test_into_chatroom(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_chatroom()
        # before test action

    # 測試-額度轉換
    @DecorateClass('PFREQ-T1854')
    def test_wallet_conversion_return_local_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_wallet_conversion()  # 進入額度管理
        cp_wallet = self.function_dict['mp'].thirdPartyWalletPage().do_wallet_return()
        self.function_dict['mp'].thirdPartyWalletPage().do_walletre_fresh()
        self.function_dict['mp'].thirdPartyWalletPage().nwap_do_wallet_check(cp_wallet)

    def test_WalletConversion(self, wallet_list):
        # Wap
        for _ in range(0,2):
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_wallet_conversion()  # 進入額度管理
            self.function_dict['mp'].thirdPartyWalletPage().do_walletre_fresh()
            money_before=self.function_dict['mp'].thirdPartyWalletPage().nwap_do_wallet_conversion(wallet_list[0], wallet_list[1], 1)
            self.function_dict['mp'].menuPage().into_member_center()
            self.function_dict['mp'].memberCenterPage().into_wallet_Report()  # 進入交易流水
            self.function_dict['mp'].thirdPartyWalletPage().nwap_trading_flow(wallet_list[0], 1, money_before)
            wallet_list.reverse()

    @DecorateClass('PFREQ-T1857')
    def test_ag_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','AG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1875')
    def test_mg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','MG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1874')
    def test_sb_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','SB']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1878')
    def test_bbin_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap            
        wallet_list = ['主钱包','BBIN']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1882')
    def test_lgd_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','LGD']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1890')
    def test_gc_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','GC']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1889')
    def test_hg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','HG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1879')
    def test_ky_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','KY']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1876')
    def test_pt_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','PT']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1880')
    def test_lc_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','KX']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1883')
    def test_gm_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','GM']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1884')
    def test_fg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','FG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1885')
    def test_cq_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','CQ9']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1881')
    def test_vg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','VG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1886')
    def test_sw_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','SW']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1887')
    def test_3s_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','3S']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T3070')
    def test_dg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','DG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1888')
    def test_bs_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','BSP']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T1961')
    def test_kk_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','KK']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T6979')
    def test_bg_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','BG']
        self.test_WalletConversion(wallet_list)

    @DecorateClass('PFREQ-T8201')
    def test_sp365_wallet_conversion_nwap(self):
        # before test action
        self.test_wap_login()
        # Wap
        wallet_list = ['主钱包','SP365']
        self.test_WalletConversion(wallet_list)

    # 測試- 修改會員資料
    @DecorateClass('PFREQ-T2109')
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
        self.function_dict['mp'].memberInfoPage().do_change_phone_nwap(number, self.withdraw_password)
        # 修改銀行
        self.function_dict['mp'].memberInfoPage().do_nwap_change_bank('北京', '五環', self.withdraw_password)
        # 修改提款密碼
        temp_spwd = '666666'
        self.function_dict['mp'].memberInfoPage().do_change_security_password_nwap(self.withdraw_password, temp_spwd)
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_security_password_nwap(temp_spwd, self.withdraw_password)
        # 修改會員密碼
        temp_pwd = 'Qa0123456'
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_password_nwap(self.web_password, temp_pwd, self.withdraw_password)
        self.function_dict['mp'].memberCenterPage().into_member_info()
        self.function_dict['mp'].memberInfoPage().do_change_password_nwap(temp_pwd, self.web_password, self.withdraw_password)

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
        if self.brand == "aa":
            wallet_before = self.function_dict['mp'].menuPage().get_balance_wallet()
        else:
            self.function_dict['mp'].menuPage().into_wallet_conversion()
            wallet_before = self.function_dict['mp'].thirdPartyWalletPage().get_main_wallet_nwap()
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()
        self.function_dict['ad'].ArtificialDeposit().add_bill(self.web_account, self.money)

        # Wap
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_deposit_in_report()  # 進入線上存款紀錄
        self.function_dict['mp'].Store_Record_Page().nwap_after_check_manualdeposit_record(wallet_before, '人工入款', self.money) # 進入入款紀錄比對

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
        
        into_game_func()
        # self.function_dict['mp'].lotteryGamePage().image_check(lottery) # 數字圖片辨識
        self.function_dict['mp'].lotteryGamePage().check_periods_new(2, lottery)  # 檢查期數差異
        lottery_record = self.function_dict['mp'].lotteryGamePage().betting_game_new()

        if items_check == True:
            self.function_dict['mp'].lotteryGamePage().help_items()

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        record = self.function_dict['mp'].gameRecordPage().game_lottery_nwap(lottery_record)
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

        self.function_dict['mp'].lotteryGamePage().into_sf6_bravery_tow_nwap()
        self.function_dict['mp'].lotteryGamePage().check_periods_new(1)  # 檢查期數差異
        lottery_record = self.function_dict['mp'].lotteryGamePage().betting_bravery_tow_new()

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        record = self.function_dict['mp'].gameRecordPage().game_lottery_nwap(lottery_record)
        records.append(record)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_result(records)

    # 新版 香港六合彩 下注
    @DecorateClass('PFREQ-T1979')
    def test_betting_hk_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_hk_nwap, 'HK', True)
        
    # 新版 極速快三 下注
    @DecorateClass('PFREQ-T2217')
    def test_betting_jisuk3_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jisuk3_nwap, 'JSK3')
        
    # 新版 極速六合彩 下注
    @DecorateClass('PFREQ-T1982')
    def test_betting_js6_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_js6_nwap, 'JS6')
        
    # 新版 極速時時彩 下注
    @DecorateClass('PFREQ-T1985')
    def test_betting_jsssc_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jsssc_nwap, 'JSSSC')
        
    # 新版 極速pk拾 下注
    @DecorateClass('PFREQ-T1983')
    def test_betting_jspk10_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jspk10_nwap, 'JSPK10')
        
    # 新版 福彩3D 下注
    @DecorateClass('PFREQ-T1974')
    def test_betting_fu3d_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_fu3d_nwap, 'FU3D')

    # 新版 PC蛋蛋 下注
    @DecorateClass('PFREQ-T1975')
    def test_betting_pcegg_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_pcegg_nwap, 'PCEGG')

    # 新版 極速11選5 下注
    @DecorateClass('PFREQ-T2218')
    def test_betting_jisu11to5_nwap(self):
        self.test_betting_new(self.function_dict['mp'].lotteryGamePage().into_jisu11to5_nwap, 'Jisu11to5')

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

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method

    # -------------------------------- 指數遊戲 --------------------------------
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

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_stock_recode(records)

    # 深证100下注
    @DecorateClass('PFREQ-T4450')
    def test_shez100(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shez100_stock, 'shez100', 1)

    # 沪深300下注
    @DecorateClass('PFREQ-T4451')
    def test_hs300(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_hs300_stock, 'hs300', 2)

    # 上证指数下注
    @DecorateClass('PFREQ-T4452')
    def test_szzs(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szzs_stock, 'szzs', 1)

    # 上证市值百强下注
    @DecorateClass('PFREQ-T4453')
    def test_szbqsf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szbqsf_stock, 'szbqsf', 2)

    # 深证1000下注
    @DecorateClass('PFREQ-T4454')
    def test_shez1000sf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shez1000sf_stock, 'shez1000sf', 1)

    # 上证A股指数下注
    @DecorateClass('PFREQ-T4455')
    def test_szagzssf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szagzssf_stock, 'szagzssf', 1)

    # 香港恒生指数下注
    @DecorateClass('PFREQ-T4456')
    def test_hkhszswf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_hkhszswf_stock, 'hkhszswf', 1)

    # 比特幣下注
    @DecorateClass('PFREQ-T4457')
    def test_btcusd(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_btcusd_stock, 'btcusd', 2)

    # 上证商业指数下注
    @DecorateClass('PFREQ-T4458')
    def test_szsyzsbf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_szsyzsbf_stock, 'szsyzsbf', 1)

    # 深证A指下注
    @DecorateClass('PFREQ-T4459')
    def test_shezazbf(self):
       self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_shezazbf_stock, 'shezazbf', 2)

    # 超大盘下注
    @DecorateClass('PFREQ-T4460')
    def test_cdpshf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_cdpshf_stock, 'cdpshf', 1)

    # 科创50下注
    @DecorateClass('PFREQ-T4461')
    def test_kc50shf(self):
        self.test_stock_index(self.function_dict['mp'].lotteryGamePage().into_kc50shf_stock, 'kc50shf', 2)

    #聊天室自動刷新
    @DecorateClass('PFREQ-T4462')
    def test_chatroom_analysis(self):
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_chatroom()
        
        self.function_dict['mp'].chatRoomPage().check_analysis_amount()
        self.function_dict['mp'].chatRoomPage().check_auto_analysis()

    #聊天室跟投
    @DecorateClass('PFREQ-T4463')
    def test_chatroom_follow_up(self):
        records = []
        self.test_wap_login()
        self.function_dict['mp'].menuPage().into_member_center()
        self.function_dict['mp'].memberCenterPage().into_chatroom()

        bet_record = self.function_dict['mp'].chatRoomPage().follow_up()

        self.test_wap_login()
        self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
        self.function_dict['mp'].gameRecordPage().switch_stock_order_type(1)
        record = self.function_dict['mp'].gameRecordPage().game_lottery_nwap(bet_record)
        records.append(record)

        if not gl.get_value('ENV').__contains__('prod'):
            # ADMIN PART
            self.test_admin_login()
            self.function_dict['ad'].operationmanagementPage().into_order_center()  # 注單中心
            self.function_dict['ad'].CheckRecord().check_stock_recode(records)

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
            self.function_dict['mp'].feedback_page().feedback_message＿nwap(title, text)
            # admin
            self.test_admin_login()
            self.function_dict['ad'].ServiceAgentPage().into_feedback()
            self.function_dict['ad'].feedback_page().check_feedback(self.web_account, title, text)
            num+=1