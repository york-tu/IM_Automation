import unittest, sys, os, datetime, random, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.sbk.web.pages.pages import WebPages, AdminPages
from Project.sbk.web.testcase.base_testcase import BaseTestCase
from Project.sbk.web.pages.webs.web_basepage import BasePage as BasePage_Web
from Project.sbk.web.pages.admin.admin_basepage import BasePage as BasePage_Admin

import common.utils.globalvar as gl
from common.utils.screenshot import ScreenShot
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass

class AdminTestCase(BaseTestCase, BasePage_Web, BasePage_Admin):
    # Chrome Setting
    wait_time =20
    implicitly_wait_time = 35
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
                function.base_page().accept_alert()
                function.base_page().dismiss_alert()
            except:
                pass
            
            function.base_page().switch_home_page()

        cls.test_all_windows_mini(cls)
        cls.function_dict['wp'].base_page().windows_to_top() # 切換視窗

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
            function.base_page().quit_browser()
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
        cls.function_dict['wp'].base_page().hide_windows()

        if not sys.argv[0].__contains__('prod'):
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPages(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].base_page().hide_windows()

    def open_url(self, function, url):
        try:
            function.base_page().dismiss_alert()
        except:
            pass
        
        function.base_page().open_browser(url)

    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.base_page().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.base_page().windows_to_top()
    

    # 測試-ADMIN登入
    @DecorateClass('SPORTSBOOK-T1797')
    def test_admin_login(self):
        self.function_dict['ad'].base_page().windows_to_top() # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password) # 登入admin

    @DecorateClass('SPORTSBOOK-T1798')
    def test_admin_switch_languages(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().switch_languages()
        self.function_dict['ad'].main_page().change_time()  

    @DecorateClass('SPORTSBOOK-T1799')
    def test_admin_change_time(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().change_time()

    @DecorateClass('SPORTSBOOK-T1800')
    def test_admin_change_pass(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().change_password()




    @DecorateClass('SPORTSBOOK-T1801')
    def test_partner_and_player_list(self): #商戶與玩家管理列表
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_list() 

    

    @DecorateClass('SPORTSBOOK-T1802')
    def test_partner_and_player_keywords_search(self): #商戶與玩家管理關鍵字搜尋
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_keywords_search() 

    @DecorateClass('SPORTSBOOK-T1803')
    def test_partner_and_player_new(self):  #商戶與玩家管理商戶新增
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_partner_new() 

    @DecorateClass('SPORTSBOOK-T1804')
    def test_partner_and_player_partner_edit(self): #商戶與玩家管理商戶編輯
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_partner_edit() 


    @DecorateClass('SPORTSBOOK-T1805')
    def test_partner_and_player_player(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_player() 

    @DecorateClass('SPORTSBOOK-T1806')
    def test_partner_and_player_player_search(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_player_search() 

    @DecorateClass('SPORTSBOOK-T1807')
    def test_partner_and_player_player_edit(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().partner_and_player_player_edit() 

    @DecorateClass('SPORTSBOOK-T1808')
    def test_transaction_log(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().transaction_log() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_transaction_number(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_transaction_number() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_partner(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_partner() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_player(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_player() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_newly_added_increase(self): #新增一筆調帳(增加)
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_newly_added_increase() 
    
    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_newly_added_decrease(self): #新增一筆調帳(減少)
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_newly_added_decrease() 
    
    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_view_edit(self): #新增一筆調帳(減少)
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_view_edit() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_view_void(self): #調帳作廢
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_view_void() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_submit_for_view(self): #調帳作廢
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_submit_for_view() 

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_applying(self): #調帳申請與審核_搜尋_進度_申請中
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_applying()    

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_submit_review(self): #調帳申請與審核_搜尋_進度_提交審核
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_submit_review()  

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_void(self): #調帳申請與審核_搜尋_進度_作廢
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_void()  

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_audit(self): #調帳申請與審核_搜尋_進度_審核中
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_audit()  

    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_approved(self): #調帳申請與審核_搜尋_進度_審核通過
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_approved() 
    
    @DecorateClass('SPORTSBOOK-T1809')
    def test_wallet_adjust_progress_reject(self): #調帳申請與審核_搜尋_進度_審核駁回
        self.test_admin_login()
        self.function_dict['ad'].main_page().wallet_adjust_progress_reject() 


    
    # # 測試-WEB登入
    # @DecorateClass('CHATAPP-T1790')
    # def test_web_login(self):
    #     self.function_dict['wp'].base_page().windows_to_top() # 切換視窗
    #     self.function_dict['wp'].base_page().open_base_url()  # 開啟前台網站
    #     self.function_dict['wp'].login_page().login(self.web_phone, self.web_password, self.web_nation)

    # # 測試-進入會員列表
    # @DecorateClass('CHATAPP-T1887')
    # def test_into_member_list(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_member_list()
        
    # # 測試-進入群組列表
    # @DecorateClass('CHATAPP-T1888')
    # def test_into_groups_list(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_groups_list()
        
    # # 測試-進入群組設定
    # @DecorateClass('CHATAPP-T1889')
    # def test_into_groups_set(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_groups_set()
        
    # # 測試-進入群組建立成員
    # @DecorateClass('CHATAPP-T1890')
    # def test_into_groups_own(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_groups_own()
        
    # # 測試-進入APP维护
    # @DecorateClass('CHATAPP-T1891')
    # def test_into_systum_maintenance(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_systum_maintenance()
        
    # # 測試-進入APP设定
    # @DecorateClass('CHATAPP-T1892')
    # def test_into_systum_app_setting(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_systum_app_setting()
        
    # # 測試-進入聊天纪录
    # @DecorateClass('CHATAPP-T1893')
    # def test_into_recode(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_menu_recode()
        
    # # 測試-進入帳號管理
    # @DecorateClass('CHATAPP-T1894')
    # def test_into_setting_account(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_setting_account()
        
    # # 測試-進入角色權限
    # @DecorateClass('CHATAPP-T1895')
    # def test_into_setting_role(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_setting_role()
        
    # # 測試-進入OTP管理
    # @DecorateClass('CHATAPP-T1896')
    # def test_into_setting_otp(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_setting_otp()
        
    # # 測試-進入運營OTP
    # @DecorateClass('CHATAPP-T1897')
    # def test_into_setting_otp_operation(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_setting_otp_operation()
        
    # # 測試-進入操作日誌
    # @DecorateClass('CHATAPP-T1898')
    # def test_into_logging(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_logging()
        
    # # 測試-進入紅包列表
    # @DecorateClass('CHATAPP-T1899')
    # def test_into_red_list(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_red_list()
        
    # # 測試-進入積分使用紀錄
    # @DecorateClass('CHATAPP-T1900')
    # def test_into_red_integral(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_red_integral()
        
    # # 測試-進入水量控制
    # @DecorateClass('CHATAPP-T1901')
    # def test_into_red_water(self):
    #     self.test_admin_login()

    #     self.function_dict['ad'].main_page().into_red_water()
        
    # # 測試-建立群組設定
    # @DecorateClass('CHATAPP-T')
    # def test_groups_biuld(self):
    #     bool_list = [False, True]
    #     for boling in bool_list: 
    #         self.test_admin_login()
    #         self.function_dict['ad'].main_page().into_groups_set()
    #         self.function_dict['ad'].groups_page().groups_biuld_switch(boling)

    #         self.test_web_login()
    #         self.function_dict['wp'].main_page().open_user_info()
    #         self.function_dict['wp'].main_page().check_groups_biuld(boling)
    
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
