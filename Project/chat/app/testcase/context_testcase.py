import unittest, sys, os, datetime, random, re
import logging
from datetime import datetime
from retrying import retry
from airtest.core.api import *
import common.utils.globalvar as gl
import stf_api.stf as stf
import driver.app_driver as app_dr
import driver.web_driver as web_dr
from common.utils.screenshot import ScreenShot
from common.app.decorator import DecorateClass
from Project.chat.app.testcase.base_testcase import BaseTestCase
from Project.chat.app.pages.pages import AppPages
from driver.app_driver import AppDriver, is_ios_wda_connection_lost
from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.web.pages.webs.web_basepage import BasePage as BasePage_Web
from Project.chat.web.pages.admin.admin_basepage import BasePage as BasePage_Admin
from Project.chat.app.testcase.app_testcase import AppTestCase
from airtest.core.api import snapshot, stop_app, clear_app, connect_device, install
root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)


class ContextTestCase(BaseTestCase, BasePage_Web, BasePage_Admin):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    chrome_crash = 0
    folderpath = ''
    group_name = datetime.now().strftime("%y%m%d") + "_bot_group"
    mail_account_id = f'mail{datetime.now().strftime("%m%d%H%M")}'
    function_dict = {}

    driver_list = []

    # ================================= TestSetting ===============================

    @classmethod
    def setUpClass(cls):
        # web
        cls.setting_test_data()  # 設定測試數據
        app_dr = AppDriver()
        poco, wda_service = app_dr.airtest_connect_phone()  # 連線測試手機

        # 儲存 WDA service，讓 tearDownClass 可存取
        cls.wda_service = wda_service

        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))
        # app
        cls.folderpath = gl.get_value('FOLDER_PATH')
        cls.setting_browser()

        # 獲取設定資訊
        brand = gl.get_value('BRAND')
        account_type = gl.get_value('ACCOUNT_TYPE')
        phone_platform = gl.get_value('PHONE_PLATFORM')

        brand = gl.get_value('BRAND') or ''
        cls.brand = brand.strip().lower()
        if cls.brand == 'mingpin':
            cls.test_group = 'QA bot only'
        else:
            cls.test_group = 'QA_bot_only'

    def setUp(self):
        # web
        for key, function in self.function_dict.items():
            if key != 'ap':
                try:
                    function.base_page().accept_alert()
                    function.base_page().dismiss_alert()
                except:
                    pass
                    
                function.base_page().switch_home_page()

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗

        # app
        if gl.get_value('VERSION_MESSAGE') != None:
            self.ap.common_page().skip_test(gl.get_value('VERSION_MESSAGE'))

        self.test_choose_app()
        self.start_time = time.time()

    def tearDown(self):
        # web
        self.test_all_windows_max()
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')
        self.check_result(str(self.id()).split('.')[-1])

        # app
        try:
            image_path = f"{self.folderpath}\\{self._testMethodName}.png"
            image_path_list = [image_path]
            snapshot(filename=image_path, msg=f"{self.id()}")
            stop_app(self.package)
            gl.set_value('IMG_PATH', image_path_list)
            self.check_result(str(self.id()).split('.')[-1])
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
                    function.base_page().quit_browser()
            if num == len(cls.driver_list):
                cls.driver_list = []
                break
            num += 1

        # app
        else:
            if cls.phone_platform == 'Android':
                clear_app(cls.poco_package)
            else:
                stop_app(cls.poco_package)
                # 關閉 WDA
                if hasattr(cls, 'wda_service') and cls.wda_service:
                    try:
                        cls.wda_service.stop()
                        print(f"[INFO] WDA stopped for {cls.phone_name}")
                    except Exception as e:
                        print(f"[WARN] Failed to stop WDA: {e}")

        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))

    # ================================= AppSetting ================================

    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def test_choose_app(self):
        # 選APP
        try:
            self.ap.common_page().find_app(self.package)
            self.ap.main_page().login_expired_handling()  # 處理登錄狀態已過期視窗
            login_status = self.ap.main_page().check_login_status(self.app_account)
            if login_status is False:
                self._login_status[0] = False
        except Exception as e:
            err_msg = str(e).lower()
            if 'device offline' in err_msg:
                self.device_reconnect()  # 手機斷線重連
            elif 'not found' in err_msg and 'device' in err_msg:
                self.device_reconnect()
            elif is_ios_wda_connection_lost(e):
                self.device_reconnect()
            else:
                raise e

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        wd = web_dr.WebDriver()
        cls.setting_test_data()  # 設定測試數據
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].base_page().hide_windows()

        aaa = sys.argv[0]
        if not sys.argv[0].__contains__('prod'):
            cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
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
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key in ['wp', 'ad']:
                    function.base_page().hide_windows()

    def test_all_windows_max(self):
        for key, function in self.function_dict.items():
            if key != 'ap':
                if key in ['wp', 'ad']:
                    function.base_page().hide_windows()

    # 測試-WEB登入
    @DecorateClass('CHATAPP-T')
    def test_web_login(self):
        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].login_page().login(self.web_phone, self.web_password, self.web_nation)

    def web_login(self, phone, password, nation):
        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].login_page().login(phone, password, nation)

    # ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password)  # 登入admin

    # 測試 - 後台"會員添加好友"權限切換 > 前台確認"新增好友"搜尋功能
    @DecorateClass('CHATAPP-T2541')
    def test_user_contact_whitelist_be_fe_linkage(self):
        """
        添加方: 非白名單內成員
        1.0. (後台)會員添加好友 > 關閉:
            1.1. (前台)好友名單 >>> 可見"新增>新增好友"選項
            1.2. (前台)好友名單 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 跳'暫不支援此功能'toast & 沒有顯示該成員新增頁面
            1.3. (前台)好友名單 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
        2.0. (後台)會員添加好友 > 開啟:
            2.1. (前台)好友名單 > 可見"新增好友"選項
            2.2. (前台)好友名單 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
        """
        self.test_admin_login()
        self.function_dict['ad'].main_page().disable_member_add_friend_setting()  # 1.0

        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page()  # 1.1
        self.ap.friend_page().is_new_friend('outwhite01')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 1.2
        self.ap.friend_page().return_previous_page()
        self.ap.chatlist_page().into_add_friend_page()
        self.ap.friend_page().is_new_friend('inwhite01')
        self.ap.friend_page().check_add_to_address_book_display()  # 1.3
        self.ap.friend_page().return_previous_page()

        self.function_dict['ad'].main_page().enable_member_add_friend_setting()  # 2.0

        self.ap.friend_page().return_previous_page()
        self.ap.chatlist_page().into_add_friend_page()
        self.ap.friend_page().is_new_friend('outwhite01')
        self.ap.friend_page().check_add_to_address_book_display()  # 2.2

    # 測試 - [後台] 會員添加好友'開啟/關閉' >>> 前台確認非白名單成員透過'ID/手機號'搜尋'白名單/非白名單'成員功能
    @DecorateClass('CHATAPP-T2546')
    def test_search_friend_by_phone_and_ID(self):
        """
        添加方: 非白名單內成員
        1.0. (後台)會員添加好友 > 關閉:
                1.1. (前台)聊天列表 > 新增 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 跳"暫不支援此功能" toast & 沒有顯示該成員新增頁面
                1.2. (前台)聊天列表 > 新增 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 跳'暫不支援此功能'toast & 沒有顯示該成員新增頁面
                1.3. (前台)聊天列表 > 新增 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 跳"暫不支援此功能" toast & 沒有顯示該成員新增頁面
                1.4. (前台)聊天列表 > 新增 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
        2.0. (後台)會員添加好友 > 開啟:
                2.1. (前台)聊天列表 > 新增 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>> 跳"找不到相關帳號" toast & 沒有顯示該成員新增頁面
                2.2. (前台)聊天列表 > 新增 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項
                2.3. (前台)聊天列表 > 新增 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>> 跳'找不到相關帳號'toast & 沒有顯示該成員新增頁面
                2.4. (前台)聊天列表 > 新增 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 新增至通訊錄選項

        """
        self.test_admin_login()
        self.function_dict['ad'].main_page().disable_member_add_friend_setting()  # 1.0

        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        self.ap.friend_page().is_new_friend('8613141010102')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 1.1
        self.ap.friend_page().is_new_friend('outwhite02')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 1.2
        self.ap.friend_page().is_new_friend('8613141010103')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 1.3
        self.ap.friend_page().is_new_friend('inwhite02')
        self.ap.friend_page().check_add_to_address_book_display()  # 1.4
        self.ap.friend_page().return_previous_page()

        self.function_dict['ad'].main_page().enable_member_add_friend_setting()  # 2

        self.ap.friend_page().is_new_friend('8613141010102')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 2.1
        self.ap.friend_page().is_new_friend('outwhite02')
        self.ap.friend_page().check_add_to_address_book_display()  # 2.2
        self.ap.friend_page().return_previous_page(1)
        self.ap.friend_page().is_new_friend('8613141010103')
        self.ap.friend_page().check_add_to_address_book_non_display()  # 2.3
        self.ap.friend_page().is_new_friend('inwhite02')
        self.ap.friend_page().check_add_to_address_book_display()  # 2.4
        self.ap.friend_page().return_previous_page(2)

    def add_red_envelope(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().add_random_amount_red_envelope()

    def add_luck_red_envelope(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().add_random_amount_luck_red_envelope()

    def add_bulk_upload_luck_red_envelope(self):
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        amount = self.function_dict['ad'].red_envelope_page().random_red_envelope_data_type_bulk_upload()
        return amount

    # 測試 - [後台]發一般紅包 > [前台]搶紅包
    @DecorateClass('CHATAPP-T2550')
    def test_app_grab_red_envelope(self):
        grab_type = '发红包'
        self.add_red_envelope()
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        grab_amount, grab_time = self.ap.chatroom_page().app_grab_red_envelope(self.app_account)  # [前台]搶紅包, 回傳紅包時間+金額
        self.ap.point_page().into_point_record()
        remain_integral_amount = self.ap.point_page().check_point_record(grab_type, grab_amount, grab_time)  # [前台]積分頁確認紅包明細, 並回傳目前帳號總積分
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.app_account, grab_amount, grab_type, grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.app_account, grab_time, grab_amount, grab_type, self.test_group, remain_integral_amount)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

    # 測試 - [後台]發拚手氣紅包 > [前台]搶紅包
    @DecorateClass('CHATAPP-T2551')
    def test_app_grab_luck_red_envelope(self):
        grab_type = '拼手气红包'
        self.add_luck_red_envelope()
        self.test_app_login()
        self.ap.chatlist_page().into_chat_room(self.test_group)
        grab_amount, grab_time = self.ap.chatroom_page().app_grab_red_envelope(self.app_account)  # [前台]搶紅包, 回傳紅包時間+金額
        self.ap.point_page().into_point_record()
        remain_integral_amount = self.ap.point_page().check_point_record(grab_type, grab_amount, grab_time)  # [前台]積分頁確認紅包明細, 並回傳目前帳號總積分
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.app_account, grab_amount, grab_type, grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.app_account, grab_time,grab_amount, grab_type, self.test_group, remain_integral_amount)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

    # 測試 - [後台]新增批量上傳手氣紅包 > [前台]搶紅包
    @DecorateClass('CHATAPP-T3302')
    def test_app_grab_bulk_upload_luck_red_envelope(self):
        grab_type = '拼手气红包'
        amount = self.add_bulk_upload_luck_red_envelope()
        self.test_app_login()
        self.ap.chatlist_page().into_chat_room(self.test_group)
        grab_amount, grab_time = self.ap.chatroom_page().app_grab_red_envelope(self.app_account)  # [前台]搶紅包, 回傳紅包時間+金額
        assert grab_amount == amount
        self.ap.point_page().into_point_record()
        remain_integral_amount = self.ap.point_page().check_point_record(grab_type, grab_amount,grab_time)  # [前台]積分頁確認紅包明細, 並回傳目前帳號總積分
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.app_account, grab_amount, grab_type,grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.app_account, grab_time, grab_amount,
                                                                                 grab_type, self.test_group,
                                                                                 remain_integral_amount)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

    # 測試 - [群組擁有者] 群組成員權限設定
    @DecorateClass('CHATAPP-T2572')
    def test_group_change_group_rules(self):
        self.test_web_login()
        self.test_app_login()

        self.function_dict['wp'].chatlist_page().into_chat_room(self.test_group)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.function_dict['wp'].chatroom_page().into_setting()

        # rule = [傳送訊息, 傳送圖片, 傳送影片, 傳送超連結, 傳送檔案, 加入新成員]
        self.function_dict['wp'].chatroom_page().change_group_rule('100000')  # 可發文字
        self.ap.chatsetup_page().check_group_rule('100000')

        self.function_dict['wp'].chatroom_page().change_group_rule('000000')  # 權限全關
        self.ap.chatsetup_page().check_group_rule('000000')

        self.function_dict['wp'].chatroom_page().change_group_rule('111111')  # 權限全開
        self.ap.chatsetup_page().check_group_rule('111111')

    # 測試 - [群組擁有者] 1. 新增管理員 + 更改該管理員權限
    @DecorateClass('CHATAPP-T2573')
    def test_group_add_admin_and_change_admin_rules(self):

        self.test_web_login()
        self.test_app_login()
        default_rule = '11111'

        self.function_dict['wp'].chatlist_page().into_chat_room(self.test_group)
        self.ap.chatlist_page().into_chat_room(self.test_group)

        self.function_dict['wp'].chatroom_page().into_setting()
        self.function_dict['wp'].chatroom_page().add_admin(self.app_account, self.web_account)

        self.function_dict['wp'].chatroom_page().change_admin_rule(self.app_account, default_rule, '00000')
        self.ap.chatsetup_page().check_admin_rule('00000')

        self.function_dict['wp'].chatroom_page().change_admin_rule(self.app_account, "00000", '11111')
        self.ap.chatsetup_page().check_admin_rule('11111')

    # 測試 - [群組管理員] 2. 群組新增/刪除成員
    @DecorateClass('CHATAPP-T2574')
    def test_group_add_and_remove_member(self):
        self.function_dict['wp'].base_page().hide_windows()
        friend = ''
        if self.brand == 'gu':
            friend = "auto_test_7788"
        elif self.brand == 'mee':
            friend = "meebot03"
        elif self.brand =='mingpin':
            friend = 'mingpinbot01'
        elif self.brand == 'chit':
            friend = 'chitbot1000'

        # =============== 新增指定成員為好友 ============================
        self.test_app_login()
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        new_friend = self.ap.friend_page().is_new_friend(friend)
        if new_friend:
            self.ap.friend_page().add_friend(friend)
        else:
            self.ap.friend_page().back_from_detail_to_chatList()

        # =============== 添加該好友到群組 ==============================
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatsetup_page().into_setting()
        self.ap.chatsetup_page().group_member_add(friend)
        # =============== 群組移除該好友 ================================
        self.ap.chatsetup_page().group_member_delete(friend)
        # =============== 刪除該好友 ===================================
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        self.ap.friend_page().is_new_friend(friend)
        self.ap.friend_page().delete_friend_from_UserDetail(friend)

    # 測試 - [群組管理員] 3. 新增/刪除黑名單成員
    @DecorateClass('CHATAPP-T2576')
    def test_group_add_and_remove_block_member(self):
        self.function_dict['wp'].base_page().hide_windows()
        block_name = "gubot05"
        self.ap.main_page().login(self.web_phone, self.web_password,self.web_nation)  # 登入gubot02群組擁有者帳號
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatsetup_page().into_setting()
        detail_page_before_add_black_amount, black_setting_page_before_add_black_amount = self.function_dict[
            'ap'].chatsetup_page().into_group_black()
        # =======================將指定成員加入黑名單========================================
        self.ap.chatsetup_page().add_block_member(block_name, detail_page_before_add_black_amount,
                                                                  black_setting_page_before_add_black_amount)
        self.ap.chatsetup_page().into_group_member_list()
        self.ap.chatsetup_page().search_block_member(block_name)
        # =======================將指定成員移出黑名單========================================
        detail_page_before_delete_black_amount, black_setting_page_before_delete_black_amount = self.function_dict[
            'ap'].chatsetup_page().into_group_black()
        self.ap.chatsetup_page().remove_block_member(block_name,
                                                                     detail_page_before_delete_black_amount,
                                                                     black_setting_page_before_delete_black_amount)
        # =======================將指定成員加回群組==========================================
        self.ap.chatsetup_page().group_member_add(block_name)

    # 測試 - [群組擁有者] 4. 移除管裡員
    @DecorateClass('CHATAPP-T2575')
    def test_group_remove_admin(self):
        self.test_web_login()
        self.function_dict['wp'].chatlist_page().into_chat_room(self.test_group)
        self.function_dict['wp'].chatroom_page().into_setting()

        self.function_dict['wp'].chatroom_page().delete_admin(self.app_account, self.web_account)

    # 測試 - (前台)變更"貼文隱私" > (後台)確認媒體"觀看權限"
    @DecorateClass('CHATAPP-T2784')
    def test_social_change_post_privacy(self):
        self.test_admin_login()
        # ================ 貼文設定 =================================================================
        media_list = ['video', 'photo']
        media_index = random.randint(-10, -1)
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        media_type = random.choice(media_list)
        user = self.app_account
        description = f'😯自動化{self.brand}Test_後台"觀看權限"測試_{current_time}😯'
        default_privacy_index = 0  # 貼文發布隱私設置 (0所有人, 1互關, 2粉絲, 3僅自己)
        # ================ 發布貼文 =================================================================
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, default_privacy_index, media_type, save_to_local=True, post=True)
        self.ap.socialhome_page().return_to_my_social_page()
        # ------------------------------------------------------------------------------------------
        privacy_list = [3, 2, 1, 0]  # 隱私設置: 3僅自己, 2粉絲, 1互關, 0所有人
        for privacy_index in privacy_list:
            # ============ 前台切換貼文隱私設定 =======
            self.ap.socialhome_page().return_to_my_social_page()
            self.ap.socialmedialibrary_page().change_first_post_privacy_type(user, description, privacy_index)
            self.ap.socialhome_page().return_to_my_social_page()
            self.ap.socialmedialibrary_page().check_first_post_privacy_type(user, description, privacy_index)
            # ============ 後台確認貼文觀看權限 =======
            self.function_dict['ad'].social_management_page().into_media_audit_page()
            self.function_dict['ad'].social_management_page().check_post_viewing_permission(user,  privacy_index, audit_page='媒体审核')

    # (前台)提出貼文檢舉 > (後台)approve > (前台)確認貼文下架
    @DecorateClass('CHATAPP-T2847')
    def test_post_removed_after_impeach_approve(self):
        # ================ 貼文設定 =================================================================
        media_list = ['video', 'photo']
        media_index = random.randint(-10, -1)
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        media_type = random.choice(media_list)
        description = f'😯自動化{self.brand}Test_檢舉貼文"測試_{current_time}😯'
        default_privacy_index = 0  # 貼文發布隱私設置 (0所有人, 1互關, 2粉絲, 3僅自己)
        # ================ A發布貼文 =================================================================
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description,
                                                                                  default_privacy_index, media_type,
                                                                                  save_to_local=True, post=True)
        self.ap.socialhome_page().return_to_my_social_page()
        # ================ B檢舉A貼文 =================================================================
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_fans_list()
        self.ap.socialhome_page().into_member_social_page_from_fans_list(self.app_account)
        self.ap.socialmedialibrary_page().into_first_post(self.app_account, description)
        request_reason = self.ap.socialshare_page().submit_impeach_request(
            random.choice([0, 1, 2, 3]))
        self.ap.socialhome_page().return_to_my_social_page()
        # ================ 後台approve檢舉request =====================================================
        self.test_admin_login()
        self.function_dict['ad'].social_management_page().into_impeach_page()
        self.function_dict['ad'].social_management_page().search_impeach_content(self.web_account, self.app_account,
                                                                               request_reason)
        self.function_dict['ad'].social_management_page().impeach_request_approve()
        # ================ B端重進A主頁, 確認貼文下架 =================================================================
        self.ap.socialhome_page().into_fans_list()
        self.ap.socialhome_page().into_member_social_page_from_fans_list(self.app_account)
        self.ap.socialmedialibrary_page().into_first_post()
        current_user_nickname, current_content = self.function_dict[
            'ap'].socialmedialibrary_page().get_post_author_and_content()
        assert current_content != description
        self.ap.socialhome_page().return_to_my_social_page()
        self.test_logout(self.web_account)
        # ================ A進到自己主頁, 確認自己的貼文還在 =================================================================
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        post_user_nickname, post_content = self.function_dict[
            'ap'].socialmedialibrary_page().get_post_author_and_content()
        assert post_content == description

    # (前台)觀看貼文 > (後台)確認[貼文數據]&[創作者數據]觀看次數 & 觀看人數
    @DecorateClass('CHATAPP-T2854')
    def test_post_view_then_check_views_and_viewers(self):
        view_counts = 7  # 觀看次數
        # ================ 貼文設定 =================================================================
        media_list = ['video', 'photo']
        media_index = random.randint(-10, -1)
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        media_type = random.choice(media_list)
        description = f'😯自動化{self.brand}Test_觀看次數&觀看人數_{current_time}😯'
        default_privacy_index = 0  # 貼文發布隱私設置 (0所有人, 1互關, 2粉絲, 3僅自己)
        # ================ A發布貼文 =================================================================
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description,
                                                                                  default_privacy_index,
                                                                                  media_type, save_to_local=True,
                                                                                  post=True)
        self.ap.socialhome_page().return_to_my_social_page()
        # ================ 後台確認創作者A原觀看人數&觀看次數 =============================================
        self.test_admin_login()
        _original_creator_view_counts, _original_creator_viewer_counts = (
            self.function_dict['ad'].social_management_page().check_creator_view_and_viewers(self.app_account))
        # ================ B觀看A貼文10秒*觀看次數(view_counts) ========================================
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_fans_list()
        self.ap.socialhome_page().into_member_social_page_from_fans_list(self.app_account)
        for i in range(view_counts):
            self.ap.socialmedialibrary_page().into_first_post()
            sleep(10)
            self.ap.socialmedialibrary_page().return_to_post_list()
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_fans_list()
        self.ap.socialhome_page().into_member_social_page_from_fans_list(self.app_account)
        after_view_counts = self.ap.socialhome_page().get_post_view_counts()
        # ================ 後台[創作者數據]確認創作者總觀看人數 & 觀看次數 ===================================
        _after_creator_view_counts, _after_creator_viewer_counts = self.function_dict[
            'ad'].social_management_page().check_creator_view_and_viewers(self.app_account)
        assert int(_after_creator_view_counts) == int(_original_creator_view_counts) + int(
            view_counts), f"預期{_after_creator_view_counts},實際{_original_creator_view_counts}+{view_counts}"
        assert int(_after_creator_viewer_counts) == int(_original_creator_viewer_counts) + 1
        # ================ 後台[貼文數據]確認貼文觀看人數 & 觀看次數 ========================================
        _data_view_counts, _data_viewer_counts = self.function_dict[
            'ad'].social_management_page().check_post_view_and_viewers(self.app_account, description)
        assert _data_view_counts == after_view_counts
        assert _data_viewer_counts == '1'

    # 測試 - (後台)變更發布者gubot06自動審核權限 > (前台)發布媒體 > (後台)確認媒體審核狀態
    @DecorateClass('CHATAPP-T2719')
    def test_social_change_poster_auto_audit_type(self):
        self.test_admin_login()
        if self.brand == 'gu' or 'mingpin':
            self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        elif self.brand == 'mee':
            self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        audit_type_list = [2, 0, 1]  # 2:黑名單, 0:一般會員, 1:白名單
        # ============ 將發布者自動審核權限設為不同權限後確認貼文狀態 ====================================
        for audit_type in audit_type_list:
            self.function_dict['ad'].social_management_page().into_auto_audit_page()
            self.function_dict['ad'].social_management_page().set_audit_privacy(self.app_account, audit_type)
            instructions = self.media_photo_post(audit_type)
            self.ap.socialhome_page().return_to_my_social_page()
            self.function_dict['ad'].social_management_page().into_media_audit_page()
            self.function_dict['ad'].social_management_page().search_audit_result(self.app_account, instructions, audit_type)

    def media_photo_post(self, audit_type):
        if audit_type == 1:
            _type = '白名单'
        elif audit_type == 2:
            _type = '黑名单'
        else:
            _type = '一般会员'
        media_index = random.randint(-10, -1)
        media_type = 'photo'
        description = f'自動審核_{self.brand}_{_type}_{media_index}'
        if self.phone_platform.lower() == 'ios':
            self.ap.socialmediapost_page().ios_select_media(media_index)
        else:
            self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index=0,
                                                                                  media_type=media_type, post=True)
        sleep(5)
        return description

    # (後台)新增屏蔽字 > (前台)確認個人簡介不可輸入屏蔽字
    @DecorateClass('CHATAPP-T2846')
    def test_block_words_blocks_instructions_input(self):
        current_time = datetime.now().strftime("%H_%M_%S")
        block_words = f'asshole_{current_time}'
        self.test_admin_login()
        self.function_dict['ad'].social_management_page().into_block_words_page()
        self.function_dict['ad'].social_management_page().add_block_words(block_words)

        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.main_page().into_main_page()
        self.ap.member_page().into_edit()
        self.ap.member_page().input_block_words_then_check_toast(block_words)
        self.function_dict['ad'].social_management_page().delete_block_words(block_words)

    # (後台)發送系統通知 > (前台)確認系統訊息
    @DecorateClass('CHATAPP-T2848')
    def test_admin_send_system_notification(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        deposit_amount = '1.11'
        system_message = f'自動化{self.brand}Test_系統訊息_{current_time}'
        # ================ 後台發布系統通知訊息 =================================================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_manual_deposit()
        send_system_message_time = self.function_dict['ad'].main_page().manual_add_system_notification(self.app_account, deposit_amount, system_message, deposit_item=random.choice([0,1,2,3]))

        # ================ 前台確認系統通知訊息內容===============================================================
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_system_notification()
        self.ap.chatlist_page().check_latest_system_message(system_message, send_system_message_time)

    # (後台)發送群組訊息 > (前台)群組內確認訊息
    @DecorateClass('CHATAPP-T3252')
    def test_admin_send_group_msg(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        group_msg = f'群發訊息_自動化測試_{current_time}'
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_group_msg()
        # ============ (後台)發送群組訊息 ============
        group_msg_send_time = self.function_dict['ad'].groups_page().group_add_group_msg(group_msg)
        # ============ (後台)確認群組訊息 ============
        self.function_dict['ad'].groups_page().check_group_msg_list(group_msg_send_time, 'gubot01', self.test_group, group_msg)
        # ============ (前台)確認群組內訊息 ============
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatlist_page().check_last_message(other_msg=True)

    # (後台)切換發現功能 > (前台)確認排序
    @DecorateClass('CHATAPP-T2927')
    def test_discover_list(self):
        # ================ 後台關閉發現功能 > 前台確認發現頁排序 ========================================
        self.test_admin_login()
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.function_dict['ad'].main_page().into_discover_setting()
        for _ in range(5):
            self.function_dict['ad'].main_page().disable_discover_function(1)
            expect_list = self.function_dict['ad'].main_page().get_discover_enable_list()

            self.ap.discover_pages().into_discover_page()
            current_list = self.ap.discover_pages().check_discover_list()
            assert current_list == expect_list
            self.function_dict['ad'].main_page().restore_discover_function()
            self.ap.socialhome_page().return_to_my_social_page()
        # ================ 後台restore to default > 前台確認發現頁排序 ========================================
        expect_list = self.function_dict['ad'].main_page().get_discover_enable_list()
        self.ap.discover_pages().into_discover_page()
        current_list = self.ap.discover_pages().check_discover_list()
        assert current_list == expect_list

    # (後台)切換帳號社群權限 > (前台)確認評論留言
    @DecorateClass('CHATAPP-T2988')
    def test_post_comment_when_social_permission_change(self):
        self.test_admin_login()
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)

        # ================ (後台)關閉帳號社群權限 > (前台)確認不可評論留言 =================
        self.function_dict['ad'].main_page().into_member_list()
        self.change_social_permission(enable=False)
        # 確認無法在自己與他人貼文上留言
        self.check_post_comment_permission(expected=False, is_own_post=True)
        self.check_post_comment_permission(expected=False, is_own_post=False)

        # ================ (後台)開啟帳號社群權限 > (前台)確認可評論留言 =================
        self.change_social_permission(enable=True)

        # 確認可在自己與他人貼文上留言
        self.check_post_comment_permission(expected=True, is_own_post=True)
        self.check_post_comment_permission(expected=True, is_own_post=False)

    def change_social_permission(self, enable: bool):
        """變更社群權限"""
        self.function_dict['ad'].member_page().change_social_permission(self.app_account, enable)

    def check_post_comment_permission(self, expected: bool, is_own_post: bool):
        """檢查貼文留言權限"""
        if is_own_post:
            self.ap.socialhome_page().return_to_my_social_page()
            self.ap.socialmedialibrary_page().into_first_post()
        else:
            self.ap.socialhome_page().return_to_my_social_page()
            self.ap.socialhome_page().into_followed_list()
            self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
            self.ap.socialmedialibrary_page().into_first_post()

        self.ap.socialmedialibrary_page().is_post_comment(expected)

    # (後台)切換貼文評論超連結開關 > (前台)確認評論留言URL
    @DecorateClass('CHATAPP-T2989')
    def test_post_URL_when_post_permission_change(self):
        comment = "https://www.youtube.com/"

        self.test_admin_login()
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        # ================ 後台"開啟"貼文評論超連結開關 > 前台確認成功留言URL =================
        self.function_dict['ad'].social_management_page().enable_post_url_setting()
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=True)
        self.ap.socialmedialibrary_page().post_add_comment(self.app_account, comment, post_url=True, self_post=True)  # 留言+確認留言相關
        # ================ 後台"關閉"貼文評論超連結開關 > 前台確認阻擋留言URL =================
        self.function_dict['ad'].social_management_page().disable_post_url_setting()
        self.ap.socialmedialibrary_page().post_add_comment(self.app_account, comment, post_url=False, self_post=True)  # 留言+確認留言相關

    @DecorateClass('CHATAPP-T3312')
    def test_app_email_registration(self):
        self.test_admin_login()
        self.test_logout(self.app_account)
        mail_address = 'qa5@tengyuntech.com'

        # ============== 後台"關閉"極驗 =======================================================
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(False)
        # ============== email註冊帳號 =======================================================
        self.ap.main_page().register_by_email(self.mail_account_id, mail_address, self.mail_password)
        # ============== 登出後再登入 =======================================================
        self.test_logout(self.mail_account_id)
        self.ap.main_page().login(mail_address, self.mail_password, login_method='email')
        self.test_logout(self.mail_account_id)
        # ============== 後台"開啟"極驗 =======================================================
        self.function_dict['ad'].main_page().enable_geetest(True)
        # ============== 後台刪除該帳號 ========================================================
        self.function_dict['ad'].main_page().into_member_list()
        self.function_dict['ad'].member_page().delete_member(self.mail_account_id)

    @DecorateClass('CHATAPP-T3352')
    def test_app_email_forgetPW(self):
        self.test_admin_login()
        self.test_logout(self.app_account)
        newPW = '000111abc'
        # ============== 後台"關閉"極驗 ======================================================
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(False)
        # ============== email帳號 > 忘記密碼 ================================================
        self.ap.main_page().email_forgetPW_resetPW_loginNewPW(self.mail_address, newPW)
        # ============== 改回原密碼 ==========================================================
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_security()
        self.ap.security_page().change_password(newPW, self.mail_password)
        # ============== 後台"開啟"極驗 ======================================================
        self.function_dict['ad'].main_page().enable_geetest(True)

    # ==================================================================================================================
    def test_app_login(self):
        if self._login_status[0] is False:
            if 'email' in self.account_type.lower():
                self.ap.main_page().login(self.mail_address, self.mail_password, login_method='email')
            elif 'phone' in self.account_type.lower():
                self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
            self._login_status[0] = True

    def test_logout(self, account):
        if self.ap.main_page().check_login_status(account) is True:
            self.ap.main_page().into_main_page()
            self.ap.main_page().into_main_setting_page()
            self.ap.member_page().into_security()
            self.ap.main_page().logout()

    # 測試-發訊息檢查
    @DecorateClass('CHATAPP-T')
    def test_message_check(self):
        self.test_web_login()
        self.test_app_login()

        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')
        self.ap.chatlist_page().into_chat_room('QA_bot_only')

        self.function_dict['wp'].chatroom_page().send_text_message()
        self.function_dict['wp'].chatlist_page().check_last_message()
        self.ap.chatlist_page().check_last_message()

        self.function_dict['wp'].chatroom_page().send_url_message()
        self.function_dict['wp'].chatlist_page().check_last_message()
        self.ap.chatlist_page().check_last_message()

    # 測試-群組擁有者 新增/刪除成員
    @DecorateClass('CHATAPP-T')
    def test_owner_member_delete(self):
        self.test_web_login()

        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')
        self.function_dict['wp'].chatroom_page().into_setting()

        self.function_dict['wp'].chatroom_page().group_member_add('test1234')
        self.function_dict['wp'].chatroom_page().group_member_delete('test1234')

    # 測試-群組擁有者 新增/刪除黑名單
    @DecorateClass('CHATAPP-T')
    def test_owner_member_block(self):
        self.test_web_login()

        self.ap.chatlist_page().into_chat_room('QA_bot_only')

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
