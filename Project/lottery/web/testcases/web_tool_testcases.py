import unittest
import sys
import os
import datetime, random

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from Project.lottery.web.pages.pages import WebPages, AdminPage, MobilePage, CmWebPage
from Project.lottery.web.testcases.base_testcase import BaseTestCase
from Project.lottery.web.pages.webs.web.webs_basepage import BasePage as BasePage_Web
from Project.lottery.web.pages.admin.admin_basepage import BasePage as BasePageAdmin
from Project.lottery.web.pages.webs.mobile.mobile_basepage import BasePage as BasePage_Mobile
from Project.lottery.web.Utils_folder.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr

class WebToolsTestCases(BaseTestCase, BasePage_Web, BasePageAdmin):
    # Chrome Setting
    wait_time =20
    implicitly_wait_time = 35
    money='300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []
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
        image_name = self.id().split('.')[-1]
        for driver in self.driver_list:
            ScreenShot(driver, self.folderpath).screenshot(image_name)

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

            cls.function_dict['cmweb'] = CmWebPage(cls.driver_list[-1], cls.wait_time, cls.cmweb_url, cls.skipTest)  # 導入Cmweb全部頁面

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass
        
        function.basePage().open_browser(url)

    # ================================= TestCases ==============================
    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top()

    # 測試-登入
    def test_web_login(self, flag=True):
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

    # 測試ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin

    # 測試Cmweb登入
    def test_cmweb_login(self):
        self.test_all_windows_mini()
        self.function_dict['cmweb'].basePage().windows_to_top() # 切換視窗
        self.function_dict['cmweb'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['cmweb'].login_page().login(self.cmweb_account, self.cmweb_password)

    # 測試遊戲下架
    def test_game_remove(self):
        # web
        self.test_web_login()
        third_channel, game_type, game_code, game_list = self.function_dict['wp'].basePage().game_list_preprocessing(gl.get_value('GAME'))  # 整理遊戲列表
        if game_type == '电子':
            self.function_dict['wp'].menuPage().into_menu_electronic()  # 進入電子遊戲
        elif game_type == '棋牌':
            self.function_dict['wp'].menuPage().into_menu_game()  # 進入棋牌遊戲
        self.function_dict['wp'].basePage().channel_locate(third_channel, game_type) # 頻道定位
        web_name_list = self.function_dict['wp'].basePage().game_remove_check(third_channel, game_type, game_list)  # 檢查遊戲下架
        # admin
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_game_management()  # 進入遊戲管理
        admin_name_list = self.function_dict['ad'].GameManagement().game_status_check(third_channel, game_type, game_list) # 檢查遊戲下架
        # cmweb
        self.test_cmweb_login()
        self.function_dict['cmweb'].systemmanagementpage().into_menu_game_list()  # 進入遊戲列表
        third_channel_rename = self.function_dict['cmweb'].game_list_page().third_channel_rename(third_channel) # 轉換頻道名
        web_name_list, admin_name_list, cm_name_list = self.function_dict['cmweb'].game_list_page().remove_game_check(third_channel_rename, game_type, game_code, game_list, web_name_list, admin_name_list)  #檢查遊戲下架
        self.function_dict['wp'].basePage().compare_game_status(web_name_list,admin_name_list,cm_name_list, maintain_list=[],status=0)  # 比對未下架遊戲

    # 測試遊戲上架
    def test_game_add(self):
        # web
        self.test_web_login()
        third_channel, game_type, game_code, game_list = self.function_dict['wp'].basePage().game_list_preprocessing(gl.get_value('GAME'))  # 整理遊戲列表
        if game_type == '电子':
            self.function_dict['wp'].menuPage().into_menu_electronic()  # 進入電子遊戲
            channel = 0
        elif game_type == '棋牌':
            self.function_dict['wp'].menuPage().into_menu_game()  # 進入棋牌遊戲
            channel = 1
        electronic_game, chess_game = self.function_dict['wp'].basePage().channel_locate(third_channel, game_type) # 取得頻道定位
        web_name_list = self.function_dict['wp'].basePage().game_add_check(third_channel, game_type, game_list)  # 檢查遊戲上架
        # admin
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_game_management()  # 進入遊戲管理
        admin_name_list = self.function_dict['ad'].GameManagement().game_add_status_check(third_channel, game_type, game_list) # 檢查遊戲上架
        self.function_dict['wp'].basePage().windows_to_top()
        maintain_list = self.function_dict['wp'].basePage().game_maintain_check(electronic_game, chess_game, game_list, admin_name_list, channel) # 檢查遊戲維護
        self.function_dict['ad'].basePage().windows_to_top()
        if maintain_list != []:
            self.function_dict['ad'].GameManagement().game_add_status_check(third_channel, game_type, maintain_list) # 檢查遊戲上架
            self.function_dict['wp'].basePage().windows_to_top()
            maintain_list = self.function_dict['wp'].basePage().game_maintain_check(electronic_game, chess_game, maintain_list, admin_name_list, channel) # 檢查遊戲維護
        self.function_dict['ad'].GameManagement().game_enable(game_list, admin_name_list) # 恢復啟用遊戲

        # cmweb
        self.test_cmweb_login()
        self.function_dict['cmweb'].systemmanagementpage().into_menu_game_list()  # 進入遊戲列表
        third_channel_rename = self.function_dict['cmweb'].game_list_page().third_channel_rename(third_channel) # 轉換頻道名
        web_name_list, admin_name_list, cm_name_list = self.function_dict['cmweb'].game_list_page().add_game_check(third_channel_rename, game_type, game_code, game_list, web_name_list, admin_name_list)  #檢查遊戲下架
        self.function_dict['wp'].basePage().compare_game_status(web_name_list, admin_name_list, cm_name_list, maintain_list, status=1)  # 比對未上架遊戲


class MobileToolsTestCases(BaseTestCase, BasePage_Mobile, BasePageAdmin):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    money='300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []

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
        image_name = self.id().split('.')[-1]
        for driver in self.driver_list:
            ScreenShot(driver, self.folderpath).screenshot(image_name)
        
        

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
            
            cls.function_dict['cmweb'] = CmWebPage(cls.driver_list[-1], cls.wait_time, cls.cmweb_url, cls.skipTest)  # 導入Cmweb全部頁面
            
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
    def test_skip_app_download(self):
        self.function_dict['mp'].mainPage().skip_app_download()
    
        # 測試-登入
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
        if flag == True:
            self.function_dict['mp'].mainPage().close_login_board()
    
    # 測試ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin

    # 測試Cmweb登入
    def test_cmweb_login(self):
        self.test_all_windows_mini()
        self.function_dict['cmweb'].basePage().windows_to_top() # 切換視窗
        self.function_dict['cmweb'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['cmweb'].login_page().login(self.cmweb_account, self.cmweb_password)

    # 測試遊戲下架
    def test_game_remove(self):
        # web
        self.test_wap_login()
        third_channel, game_type, game_code, game_list = self.function_dict['mp'].basePage().game_list_preprocessing(gl.get_value('GAME'))  #整理遊戲列表
        if game_type == '电子':
            self.function_dict['mp'].menuPage().into_menu_electronic()  #進入電子遊戲
        elif game_type == '棋牌':
            self.function_dict['mp'].menuPage().into_menu_game()  #進入棋牌遊戲
        self.function_dict['mp'].basePage().channel_locate(third_channel, game_type) # 頻道定位
        wap_name_list = self.function_dict['mp'].basePage().game_remove_check(third_channel, game_type, game_list)  #檢查遊戲下架
        # admin
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_game_management()  # 進入遊戲管理
        admin_name_list = self.function_dict['ad'].GameManagement().game_status_check(third_channel, game_type, game_list) #檢查遊戲下架
        # cmweb
        self.test_cmweb_login()
        self.function_dict['cmweb'].systemmanagementpage().into_menu_game_list()  # 進入遊戲列表
        third_channel_rename = self.function_dict['cmweb'].game_list_page().third_channel_rename(third_channel) # 轉換頻道名
        wap_name_list, admin_name_list, cm_name_list = self.function_dict['cmweb'].game_list_page().remove_game_check(third_channel_rename, game_type, game_code, game_list, wap_name_list, admin_name_list)  #檢查遊戲下架
        self.function_dict['mp'].basePage().compare_game_status(wap_name_list,admin_name_list,cm_name_list,maintain_list=[],status=0)  # 比對未下架遊戲

    # 測試遊戲上架
    def test_game_add(self):
        # web
        self.test_wap_login()
        third_channel, game_type, game_code, game_list = self.function_dict['mp'].basePage().game_list_preprocessing(gl.get_value('GAME'))  # 整理遊戲列表
        if game_type == '电子':
            self.function_dict['mp'].menuPage().into_menu_electronic()  # 進入電子遊戲
        elif game_type == '棋牌':
            self.function_dict['mp'].menuPage().into_menu_game()  # 進入棋牌遊戲
        self.function_dict['mp'].basePage().channel_locate(third_channel, game_type) # 取得頻道定位
        wap_name_list = self.function_dict['mp'].basePage().game_add_check(third_channel, game_type, game_list)  # 檢查遊戲上架
        # admin
        self.test_admin_login()
        self.function_dict['ad'].systemmanagementpage().into_game_management()  # 進入遊戲管理
        admin_name_list = self.function_dict['ad'].GameManagement().game_add_status_check(third_channel, game_type, game_list) # 檢查遊戲上架
        self.function_dict['mp'].basePage().windows_to_top()
        maintain_list = self.function_dict['mp'].basePage().game_maintain_check(game_list, admin_name_list) # 檢查遊戲維護
        self.function_dict['ad'].basePage().windows_to_top()
        if maintain_list != []:
            self.function_dict['ad'].GameManagement().game_add_status_check(third_channel, game_type, maintain_list) # 檢查遊戲上架
            self.function_dict['mp'].basePage().windows_to_top()
            maintain_list = self.function_dict['mp'].basePage().game_maintain_check(maintain_list, admin_name_list) # 檢查遊戲維護
        self.function_dict['ad'].GameManagement().game_enable(game_list, admin_name_list) # 恢復啟用遊戲
        # cmweb
        self.test_cmweb_login()
        self.function_dict['cmweb'].systemmanagementpage().into_menu_game_list()  # 進入遊戲列表
        third_channel_rename = self.function_dict['cmweb'].game_list_page().third_channel_rename(third_channel) # 轉換頻道名
        wap_name_list, admin_name_list, cm_name_list = self.function_dict['cmweb'].game_list_page().add_game_check(third_channel_rename, game_type, game_code, game_list, wap_name_list, admin_name_list)  #檢查遊戲下架
        self.function_dict['mp'].basePage().compare_game_status(wap_name_list,admin_name_list,cm_name_list,maintain_list,status=1)  # 比對未上架遊戲

if __name__ == "__main__":
    unittest.main()