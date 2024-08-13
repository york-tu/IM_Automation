import unittest, sys, os, datetime, random, re
import logging
from datetime import datetime
from retrying import retry
from airtest.core.api import *


root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
import stf_api.stf as stf
import driver.app_driver as app_dr
import driver.web_driver as web_dr
from common.utils.screenshot import ScreenShot
from common.app.decorator import DecorateClass
from Project.chat.app.testcase.base_testcase import BaseTestCase
from Project.chat.app.pages.pages import AppPages
from driver.app_driver import AppDriver
from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.web.pages.webs.web_basepage import BasePage as BasePage_Web
from Project.chat.web.pages.admin.admin_basepage import BasePage as BasePage_Admin
from Project.chat.apis.function_layer.functions import Functions
from Project.chat.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
from Project.chat.app.testcase.app_testcase import AppTestCase

from airtest.core.api import snapshot, stop_app, clear_app, connect_device, install

class ContextTestCase(BaseTestCase, BaseFunction_API, BasePage_Web, BasePage_Admin):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    chrome_crash = 0
    foloderpath = ''
    group_name = datetime.now().strftime("%y%m%d") + "_bot_group"
    function_dict = {}

    brand = gl.get_value('BRAND')
    driver_list = []
    # ================================= TestSetting ===============================

    @classmethod
    def setUpClass(cls):
        # web
        cls.setting_test_data()  # 設定測試數據
        app_dr = AppDriver()
        poco, wda_service = app_dr.airtest_connect_phone()  # 連線測試手機
        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))
        # app
        cls.folderpath = gl.get_value('FOLDER_PATH')
        cls.setting_browser()

    def setUp(cls):
        # web
        for key, function in cls.function_dict.items():
            if key != 'ap':
                try:
                    function.basePage().accept_alert()
                    function.basePage().dismiss_alert()
                except:
                    pass

                function.basePage().switch_home_page()

        cls.test_all_windows_mini()
        cls.function_dict['wp'].basePage().windows_to_top()  # 切換視窗

        # app
        if gl.get_value('VERSION_MESSAGE') != None:
            cls.function_dict['ap'].commomPage().skip_test(gl.get_value('VERSION_MESSAGE'))

        cls.functions = Functions()
        cls.test_choose_app()
        cls.start_time = time.time()

    def tearDown(self):
        # web
        self.test_all_windows_max()
        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

        # app
        try:
            image_path = f"{self.folderpath}\\{self._testMethodName}.png"
            image_path_list = [image_path]
            snapshot(filename=image_path, msg=f"{self.id()}")
            stop_app(self.package)
            self.check_result(str(self.id()).split('.')[-1])
            gl.set_value('IMG_PATH', image_path_list)
        except Exception as e:
            if 'No available screen capture method found' in str(e):
                pass
            else:
                raise e

    @classmethod
    def tearDownClass(cls):
        # web
        num = 0
        for key, function in cls.function_dict.items():
            if key != 'ap':
                if key in ['wp', 'ad']:
                    function.basePage().quit_browser()
            if num == len(cls.driver_list):
                cls.driver_list = []
                break
            num += 1

        # app
        else:
            clear_app(cls.poco_package)

        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))

    # ================================= AppSetting ================================

    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def test_choose_app(self):
        # 選APP
        try:
            self.function_dict['ap'].commomPage().find_app(self.package)
            login_status = self.function_dict['ap'].mainPage().into_home_check(self._login_status[0])
            if login_status == False:
                self._login_status[0] = False
        except Exception as e:
            if 'device offline' in str(e):
                self.device_reconnect()  # 手機斷線重連
            elif 'device' and 'not found' in str(e):
                self.device_reconnect()
            else:
                raise e

    def device_reconnect(self):
        gl.set_value('PHONE_NAME', 'None')
        self._login_status[0] = False
        self.unknown_env[0] = False
        self.tearDownClass()
        self.sleep(60)
        self.setUpClass()
        self.setUp()

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        wd = web_dr.WebDriver()
        cls.setting_test_data()  # 設定測試數據
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time))  # 設定ChromeDriver
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].basePage().hide_windows()

        if not sys.argv[0].__contains__('prod'):
            cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPages(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].basePage().hide_windows()

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass

        function.basePage().open_browser(url)

    # ================================= TestCases =================================
    def test_all_windows_mini(self):
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key in ['wp', 'ad']:
                    function.basePage().hide_windows()

    def test_all_windows_max(self):
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key in ['wp', 'ad']:
                    function.basePage().hide_windows()

    # 測試-WEB登入
    @DecorateClass('CHATAPP-T')
    def test_web_login(self):
        self.test_all_windows_mini()
        self.function_dict['wp'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].loginPage().login(self.web_phone, self.web_password, self.web_nation)

    # ADMIN登入
    def test_admin_login(self):
        self.function_dict['ad'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password)  # 登入admin

    # 測試 - 後台"會員添加好友"權限切換 > 前台確認"新增好友"搜尋功能
    @DecorateClass('CHATAPP-T2541')
    def test_user_contact_whitelist_be_fe_linkage(self):
        """
        添加方: 非白名單內成員
        1.0. (後台)會員添加好友 > 關閉:
            1.1. (前台)好友名單 >>> 可見"新增好友"選項
            1.2. (前台)好友名單 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 跳'暫不支援此功能'toast & 沒有顯示該成員新增頁面
            1.3. (前台)好友名單 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
        2.0. (後台)會員添加好友 > 開啟:
            2.1. (前台)好友名單 > 可見"新增好友"選項
            2.2. (前台)好友名單 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
        """
        self.test_admin_login()
        self.function_dict['ad'].mainPage().disable_member_add_friend_setting()  # 1.0

        self.test_app_login()
        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().check_add_friend_btn_display()  # 1.1
        self.function_dict['ap'].friendPage().search_new_friend('outwhite01')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 1.2
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('inwhite01')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 1.3
        self.function_dict['ap'].friendPage().return_previous_page()

        self.function_dict['ad'].mainPage().enable_member_add_friend_setting()  # 2.0

        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().check_add_friend_btn_display()  # 2.1
        self.function_dict['ap'].friendPage().search_new_friend('outwhite01')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 2.2

    # 測試 - [後台] 手機號搜索添加好友'開啟/關閉' & 會員添加好友'開啟/關閉' >>> 前台確認非白名單成員透過'ID/手機號'搜尋'白名單/非白名單'成員功能
    @DecorateClass('CHATAPP-T2546')
    def test_search_contact_by_phone_be_fe_linkage(self):
        """
        添加方: 非白名單內成員
        0. (後台)會員添加好友 > 關閉:
            1.0. (後台)手機號搜索添加好友 > 關閉:
                1.1. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 跳"暂不支援手机号搜索" toast & 沒有顯示該成員新增頁面
                1.2. (前台)好友名單 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 跳'暫不支援此功能'toast & 沒有顯示該成員新增頁面
                1.3. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 跳"暂不支援手机号搜索" toast & 沒有顯示該成員新增頁面
                1.4. (前台)好友名單 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
            2.0. (後台)手機號搜索添加好友 > 開啟:
                2.1. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 跳"暫不支援此功能" toast & 沒有顯示該成員新增頁面
                2.2. (前台)好友名單 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 跳'暫不支援此功能'toast & 沒有顯示該成員新增頁面
                2.3. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 顯示該成員個人資訊 & 成功加入通訊錄
                2.4. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 成功加入通訊錄
        3. (後台)會員添加好友 > 開啟:
            4.0. (後台)手機號搜索添加好友 > 關閉:
                4.1. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 跳"暂不支援手机号搜索" toast & 沒有顯示該成員新增頁面
                4.2. (前台)好友名單 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
                4.3. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 跳'暂不支援手机号搜索'toast & 沒有顯示該成員新增頁面
                4.4. (前台)好友名單 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
            5.0. (後台)手機號搜索添加好友 > 開啟:
                5.1. (前台)好友名單 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
                5.2. (前台)好友名單 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite01) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
                5.3. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 顯示該成員個人資訊 & 成功加入通訊錄
                5.4. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
        """
        self.test_admin_login()
        self.function_dict['ad'].mainPage().disable_member_add_friend_setting()  # 0
        self.function_dict['ad'].mainPage().disable_add_friend_by_search_phone()  # 1.0

        self.test_app_login()
        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().search_new_friend('8613141010102')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 1.1
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('outwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 1.2
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('8613141010103')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 1.3
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('inwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 1.4
        self.function_dict['ap'].friendPage().return_previous_page()

        self.function_dict['ad'].mainPage().enable_add_friend_by_search_phone()  # 2.0

        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('8613141010102')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 2.1
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('outwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 2.2
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('8613141010103')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 2.3
        self.function_dict['ap'].friendPage().return_previous_page(2)
        self.function_dict['ap'].friendPage().search_new_friend('inwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 2.4
        self.function_dict['ap'].friendPage().return_previous_page(2)

        self.function_dict['ad'].mainPage().enable_member_add_friend_setting()  # 3
        self.function_dict['ad'].mainPage().disable_add_friend_by_search_phone()  # 4.0

        self.function_dict['ap'].friendPage().search_new_friend('8613141010102')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 4.1
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('outwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 4.2
        self.function_dict['ap'].friendPage().return_previous_page(2)
        self.function_dict['ap'].friendPage().search_new_friend('8613141010103')
        self.function_dict['ap'].friendPage().check_add_to_address_book_non_display()  # 4.3
        self.function_dict['ap'].friendPage().return_previous_page()
        self.function_dict['ap'].friendPage().search_new_friend('inwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 4.4
        self.function_dict['ap'].friendPage().return_previous_page(2)

        self.function_dict['ad'].mainPage().enable_add_friend_by_search_phone()  # 5.0

        self.function_dict['ap'].friendPage().search_new_friend('8613141010102')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 5.1
        self.function_dict['ap'].friendPage().return_previous_page(2)
        self.function_dict['ap'].friendPage().search_new_friend('outwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 5.2
        self.function_dict['ap'].friendPage().return_previous_page(2)
        self.function_dict['ap'].friendPage().search_new_friend('8613141010103')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 5.3
        self.function_dict['ap'].friendPage().return_previous_page(2)
        self.function_dict['ap'].friendPage().search_new_friend('inwhite02')
        self.function_dict['ap'].friendPage().check_add_to_address_book_display()  # 5.4

    def add_red_envelope(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_red_list()
        self.function_dict['ad'].redenvelopePage().add_random_amount_red_envelope()

    def add_luck_red_envelope(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_red_list()
        self.function_dict['ad'].redenvelopePage().add_random_amount_luck_red_envelope()

    # 測試 - [後台]發一般紅包 > [前台]搶紅包
    @DecorateClass('CHATAPP-T2550')
    def test_app_grab_red_envelope(self):
        grab_type = '发红包'
        self.add_red_envelope()
        self.test_app_login()
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        grab_amount, grab_time = self.function_dict['ap'].chatroomPage().app_grab_red_envelope(self.app_account)  # [前台]搶紅包, 回傳紅包時間+金額
        self.function_dict['ap'].pointPage().into_point_record()
        remain_integral_amount = self.function_dict['ap'].pointPage().check_point_record(grab_type, grab_amount, grab_time)  # [前台]積分頁確認紅包明細, 並回傳目前帳號總積分
        self.function_dict['ad'].redenvelopePage().red_envelope_detail_check(self.app_account, grab_amount, grab_type, grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].mainPage().into_integral_record()
        self.function_dict['ad'].waterRecodePage().check_current_exchange_record(self.app_account, grab_time, grab_amount, grab_type, 'QA_bot_only', remain_integral_amount)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

    # 測試 - [後台]發拚手氣紅包 > [前台]搶紅包
    @DecorateClass('CHATAPP-T2551')
    def test_app_grab_luck_red_envelope(self):
        grab_type = '拼手气红包'
        self.add_luck_red_envelope()
        self.test_app_login()
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        grab_amount, grab_time = self.function_dict['ap'].chatroomPage().app_grab_red_envelope(self.app_account)  # [前台]搶紅包, 回傳紅包時間+金額
        self.function_dict['ap'].pointPage().into_point_record()
        remain_integral_amount = self.function_dict['ap'].pointPage().check_point_record(grab_type, grab_amount, grab_time)  # [前台]積分頁確認紅包明細, 並回傳目前帳號總積分
        self.function_dict['ad'].redenvelopePage().red_envelope_detail_check(self.app_account, grab_amount, grab_type, grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].mainPage().into_integral_record()
        self.function_dict['ad'].waterRecodePage().check_current_exchange_record(self.app_account, grab_time,grab_amount, grab_type, 'QA_bot_only', remain_integral_amount)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

    # 測試 - [群組擁有者] 群組成員權限設定
    @DecorateClass('CHATAPP-T2572')
    def test_group_change_group_rules(self):
        self.test_web_login()
        self.test_app_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')

        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().change_group_rule('10000')  # 發文字
        self.function_dict['ap'].chatsetupPage().check_group_rule('10000')

        self.function_dict['wp'].chatroomPage().change_group_rule('11010')  # 發連結
        self.function_dict['ap'].chatsetupPage().check_group_rule('11010')

        self.function_dict['wp'].chatroomPage().change_group_rule('00001')  # 加好友
        self.function_dict['ap'].chatsetupPage().check_group_rule('00001')

        self.function_dict['wp'].chatroomPage().change_group_rule('00000')  # 權限全關
        self.function_dict['ap'].chatsetupPage().check_group_rule('00000')

        self.function_dict['wp'].chatroomPage().change_group_rule('11111')  # 權限全開
        self.function_dict['ap'].chatsetupPage().check_group_rule('11111')

    # 測試 - [群組擁有者] 1. 新增管理員 + 更改該管理員權限
    @DecorateClass('CHATAPP-T2573')
    def test_group_add_admin_and_change_admin_rules(self):
        self.test_web_login()
        self.test_app_login()
        default_rule = '11111'

        self.function_dict['wp'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')

        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().add_admin(self.app_account, self.web_account)

        self.function_dict['wp'].chatroomPage().change_admin_rule(self.app_account, default_rule, '00000')
        self.function_dict['ap'].chatsetupPage().check_admin_rule('00000')

        self.function_dict['wp'].chatroomPage().change_admin_rule(self.app_account, "00000", '11111')
        self.function_dict['ap'].chatsetupPage().check_admin_rule('11111')

    # 測試 - [群組管理員] 2. 群組新增/刪除成員
    @DecorateClass('CHATAPP-T2574')
    def test_group_add_and_remove_member(self):
        self.function_dict['wp'].basePage().hide_windows()
        friend = "gubot06"
        # =============== 新增指定成員為好友 ============================
        self.test_app_login()
        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().search_new_friend(friend)
        self.function_dict['ap'].friendPage().add_friend()
        # =============== 添加該好友到群組 ==============================
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatsetupPage().into_setting()
        self.function_dict['ap'].chatsetupPage().group_member_add(friend)
        # =============== 群組移除該好友 ================================
        self.function_dict['ap'].chatsetupPage().group_member_delete(friend)
        # =============== 刪除該好友 ===================================
        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().delete_friend(friend)

    # 測試 - [群組管理員] 3. 新增/刪除黑名單成員
    @DecorateClass('CHATAPP-T2576')
    def test_group_add_and_remove_block_member(self):
        self.function_dict['wp'].basePage().hide_windows()
        block_name = "gubot05"
        self.function_dict['ap'].mainPage().login(self.web_phone, self.web_password,
                                                  self.web_nation)  # 登入gubot02群組擁有者帳號

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatsetupPage().into_setting()
        detail_page_before_add_black_amount, black_setting_page_before_add_black_amount = self.function_dict[
            'ap'].chatsetupPage().into_group_black()
        # =======================將指定成員加入黑名單========================================
        self.function_dict['ap'].chatsetupPage().add_block_member(block_name, detail_page_before_add_black_amount,
                                                                  black_setting_page_before_add_black_amount)
        self.function_dict['ap'].chatsetupPage().into_group_member_list()
        self.function_dict['ap'].chatsetupPage().search_block_member(block_name)
        # =======================將指定成員移出黑名單========================================
        detail_page_before_delete_black_amount, black_setting_page_before_delete_black_amount = self.function_dict[
            'ap'].chatsetupPage().into_group_black()
        self.function_dict['ap'].chatsetupPage().remove_block_member(block_name,
                                                                     detail_page_before_delete_black_amount,
                                                                     black_setting_page_before_delete_black_amount)
        # =======================將指定成員加回群組==========================================
        self.function_dict['ap'].chatsetupPage().group_member_add(block_name)

    # 測試 - [群組擁有者] 4. 移除管裡員
    @DecorateClass('CHATAPP-T2575')
    def test_group_remove_admin(self):
        self.test_web_login()
        self.function_dict['wp'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().delete_admin(self.app_account, self.web_account)

    # 測試 - 後台變更發布者自動審核權限 > 前台發布媒體 > 後台確認媒體審核狀態
    @DecorateClass('CHATAPP-T2719')
    def test_change_media_audit_type(self):
        self.test_admin_login()
        self.test_app_login()

        # ============ 將發布者自動審核權限設為: 一般會員 ==============
        audit_type = 0
        self.function_dict['ad'].socialManagementPage().into_auto_audit_page()
        self.function_dict['ad'].socialManagementPage().set_audit_privacy(self.app_account, audit_type)
        instructions = self.media_photo_post(audit_type)
        self.function_dict['ad'].socialManagementPage().into_media_audit_page()
        self.function_dict['ad'].socialManagementPage().search_media_audit_result(self.app_account, instructions, audit_type)
        # ============ 將發布者自動審核權限設為: 白名單 ================
        audit_type = 1
        self.function_dict['ad'].socialManagementPage().into_auto_audit_page()
        self.function_dict['ad'].socialManagementPage().set_audit_privacy(self.app_account, audit_type)
        instructions = self.media_photo_post(audit_type)
        self.function_dict['ad'].socialManagementPage().into_media_audit_page()
        self.function_dict['ad'].socialManagementPage().search_media_audit_result(self.app_account, instructions, audit_type)
        # ============ 將發布者自動審核權限設為: 黑名單 ================
        audit_type = 2
        self.function_dict['ad'].socialManagementPage().into_auto_audit_page()
        self.function_dict['ad'].socialManagementPage().set_audit_privacy(self.app_account, audit_type)
        instructions = self.media_photo_post(audit_type)
        self.function_dict['ad'].socialManagementPage().into_media_audit_page()
        self.function_dict['ad'].socialManagementPage().search_media_audit_result(self.app_account, instructions, audit_type)

    def media_photo_post(self, audit_type):
        if audit_type == 1:
            _type = '白名单'
        elif audit_type == 2:
            _type = '黑名单'
        else:
            _type = '一般会员'
        media_index = random.randint(-5, -1)
        media_type = 'photo'
        description = f'自動審核_{_type}_{media_index}'

        self.function_dict['ap'].mediareleasePage().select_media(media_index, media_type)
        self.function_dict['ap'].mediareleasePage().into_post_page(description, privacy_index=0, media_type=media_type,
                                                                   post=True)
        return description


    # -------------------------------------------------------------------------------------------------------
    def test_app_login(self):
        if self.unknown_env[0] == True:
            self.function_dict['ap'].commomPage().skip_test('測試環境不正確')
        if self._login_status[0] == False:
            self.function_dict['ap'].mainPage().login(self.app_phone, self.app_password, self.app_nation)
            self._login_status[0] = True

    # 測試-發訊息檢查
    @DecorateClass('CHATAPP-T')
    def test_message_check(self):
        self.test_web_login()
        self.test_app_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')

        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatlistPage().check_last_message()

        self.function_dict['wp'].chatroomPage().send_url_message()
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatlistPage().check_last_message()

    # 測試-群組擁有者 新增/刪除成員
    @DecorateClass('CHATAPP-T')
    def test_owner_member_delete(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['wp'].chatroomPage().into_setting()

        self.function_dict['wp'].chatroomPage().group_member_add('test1234')
        self.function_dict['wp'].chatroomPage().group_member_delete('test1234')

    # 測試-群組擁有者 新增/刪除黑名單
    @DecorateClass('CHATAPP-T')
    def test_owner_member_block(self):
        self.test_web_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method

    # ========================================================================
    @DecorateClass('')
    def test_install_apk(self):
        # APK 文件夹路径
        apk_folder = r"C:/Users/york_tu/Desktop/apk folder"
        # 获取文件夹中的所有 APK 文件
        apk_files = [f for f in os.listdir(apk_folder) if f.endswith(".apk")]
        # 遍历 APK 文件列表，逐个安装
        for apk_file in apk_files:
            # 构建 APK 文件的完整路径
            apk_path = os.path.join(apk_folder, apk_file)
            # 使用 adb install 命令安装 APK
            install(apk_path)  # , install_options =['-g', "-t", "-r"]
            # os.system(f"adb install {apk_path}")
        print("All APKs installed successfully!")
