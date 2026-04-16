import os
import sys
import re
from datetime import datetime
from time import sleep
import time

from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.web.testcase.base_testcase import BaseTestCase
from Project.chat.web.pages.admin.admin_redenvelopepage import RedEnvelopePageLocator, RedEnvelopePage
from Project.chat.web.pages.admin.admin_water_recode_page import WaterRecodePage

from common.utils.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass


class WebTestCase(BaseTestCase):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    chrome_crash = 0
    folder_path = ''
    group_name = datetime.now().strftime("%y%m%d") + "_bot_group"
    function_dict = {}
    driver_list = []
    security_code = 326789
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    # ================================= Page Shortcuts =============================
    
    @property
    def wp(self):
        """Web Pages 快捷方式"""
        return self.function_dict.get('wp')
    
    @property
    def ad(self):
        """Admin Pages 快捷方式"""
        return self.function_dict.get('ad')
    
    @property
    def wap(self):
        """WAP Pages 快捷方式（如需要）"""
        return self.function_dict.get('wap')

    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folder_path = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        # 使用臨時變數簡化代碼
        wp = cls.function_dict['wp']
        web_version = wp.main_page().return_web_version()  # 獲取web版本號
        gl.set_value('APP_VERSION', web_version)

        # 獲取設定資訊
        brand = gl.get_value('BRAND') or ''
        cls.brand = brand.strip().lower()
        if cls.brand == 'mingpin':
            cls.test_group = 'QA bot only'
        else:
            cls.test_group = 'QA_bot_only'

    def setUp(self):
        for key, function in self.function_dict.items():
            try:
                function.base_page().accept_alert()
                function.base_page().dismiss_alert()
            except:
                pass

            function.base_page().switch_home_page()

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.start_time = time.time()

    def tearDown(self):
        self.test_all_windows_max()
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folder_path}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  #測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')
        self.check_result(str(self.id()).split('.')[-1])

    @classmethod
    def tearDownClass(cls):
        num = 0
        for function in list(cls.function_dict.values()):
            try:
                function.base_page().quit_browser()
            except Exception:
                pass
            num += 1

            if num == len(cls.driver_list):
                break
        cls.driver_list = []
        try:
            cls.function_dict = {}
        except Exception:
            pass

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        wd = web_dr.WebDriver()
        cls.setting_test_data()  # 設定測試數據
        
        # 設定 Web Pages
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
        wp = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        wp.base_page().hide_windows()
        cls.function_dict['wp'] = wp

        if not sys.argv[0].__contains__('prod'):
            # 設定 Admin Pages
            cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
            ad = AdminPages(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            ad.base_page().hide_windows()
            cls.function_dict['ad'] = ad

    @staticmethod
    def open_url(function, url):
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

    def get_group_name(self):
        if self.env == 'prod':
            return self.test_group
        elif self.env == 'uat':
            return str(datetime.now().strftime("%m%d") + "group")

    # 測試-登入
    @DecorateClass('CHATAPP-T1790')
    def test_web_login(self):
        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.base_page().open_base_url()  # 開啟前台網站
        self.wp.login_page().login(self.web_phone, self.web_password, self.web_nation)

    # 登入ADMIN
    def test_admin_login(self):
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.ad.base_page().open_base_url()  # 開啟前台網站
        self.ad.login_page().login(self.admin_account, self.admin_password)  # 登入admin

    # 登入ADMIN並進入會員列表頁
    def test_admin_login_to_memberlist(self):
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.ad.base_page().open_base_url()  # 開啟前台網站
        self.ad.login_page().login(self.admin_account, self.admin_password)  # 登入admin
        self.ad.main_page().into_member_list()

    # ================================= Helper Methods =============================
    
    def _navigate_to_user_page(self, page_type):
        """
        導航到用戶相關頁面的通用方法
        
        Args:
            page_type: 頁面類型 ('notification', 'security', 'black', 'share', 'about')
        """
        self.test_web_login()
        self.wp.main_page().open_user_info()
        getattr(self.wp.main_page(), f'into_{page_type}_page')()
        self.wp.main_page().close_modal(1)

    # ================================= TestCases =================================

    # 測試-進入訊息通知
    @DecorateClass('CHATAPP-T1792')
    def test_into_notification(self):
        self._navigate_to_user_page('notification')

    # 測試-進入帳號與安全頁面
    @DecorateClass('CHATAPP-T1793')
    def test_into_security(self):
        self._navigate_to_user_page('security')

    # 測試-進入黑名單頁面
    @DecorateClass('CHATAPP-T1796')
    def test_into_black(self):
        self._navigate_to_user_page('black')

    # 測試-進入分享頁面
    @DecorateClass('CHATAPP-T1797')
    def test_into_share(self):
        self._navigate_to_user_page('share')

    # 測試-進入關於聊天頁面
    @DecorateClass('CHATAPP-T1799')
    def test_into_about(self):
        self._navigate_to_user_page('about')

    # 測試-檢查帳號與手機號碼
    @DecorateClass('CHATAPP-T1794')
    def test_account_info(self):
        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_security_page()
        self.wp.security_page().check_mysecurity(self.web_account, self.web_phone, self.web_nation)

    # 測試-變更登入密碼
    @DecorateClass('CHATAPP-T1795')
    def test_change_password(self):
        self.test_web_login()

        new_pwd = 'Ps43941122'
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_security_page()
        self.wp.security_page().change_password(self.web_password, new_pwd, self.brand)

        self.wp.main_page().into_security_page()
        self.wp.security_page().logout()
        self.wp.login_page().login(self.web_phone, new_pwd, self.web_nation)

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_security_page()
        self.wp.security_page().change_password(new_pwd, self.web_password, self.brand)

        self.wp.main_page().into_security_page()
        self.wp.security_page().logout()
        self.wp.login_page().login(self.web_phone, self.web_password, self.web_nation)

    # 測試-更改個人暱稱
    @DecorateClass('CHATAPP-T1800')
    def test_change_nickname(self):
        self.test_web_login()
        self.wp.main_page().open_user_info()
        preset_name = self.wp.main_page().get_user_info(self.web_account)
        self.wp.main_page().change_nickname(preset_name, 'testaaaa')
        self.wp.main_page().change_nickname('testaaaa', preset_name)

    # 測試-訊息通知開關
    @DecorateClass('CHATAPP-T1801')
    def test_notify_switch(self):
        self.test_web_login()

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_notification_page()
        self.wp.notification_page().check_header_text()
        self.wp.notification_page().check_switch_logic()

    # 測試-關於聊天-檢查服務條款/隱私權政策
    @DecorateClass('CHATAPP-T1802')
    def test_about_terms(self):
        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_about_page()
        self.wp.about_page().check_service(self.brand)
        self.wp.about_page().check_privacy()

    # 測試 - [後台]會員添加好友'開啟/關閉' >>> [前台]確認非白名單成員搜尋白名單/非白名單成員功能
    @DecorateClass('CHATAPP-T2540')
    def test_user_contact_whitelist_be_fe_linkage(self):
        """
        添加方: 非白名單內成員
        1.0. (後台)會員添加好友 > 關閉:
            1.1. (前台)個人資訊 > 可見"新增好友"選項
            1.2. (前台)個人資訊 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 跳"暫不支援此功能" warning
            1.3. (前台)個人資訊 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
        2.0. (後台)會員添加好友 > 開啟:
            2.1. (前台)個人資訊 > 可見"新增好友"選項
            2.2. (前台)個人資訊 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
            2.3. (前台)個人資訊 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄

        """
        self.test_admin_login()
        self.ad.main_page().disable_member_add_friend_setting()  # 後台 關閉"會員添加好友"全局設定

        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().check_friend_add_enabled()  # 1.1
        self.wp.main_page().into_friend_add()
        self.wp.main_page().add_friend('outwhite01', '暂不支援此功能')  # 1.2
        self.add_target_friend('inwhite01')  # 1.3
        self.delete_target_friend('inwhite01')

        self.test_admin_login()
        self.ad.main_page().enable_member_add_friend_setting()  # 後台 開啟"會員添加好友"全局設定

        self.wp.base_page().switch_last_page()
        self.wp.main_page().open_user_info()
        self.wp.main_page().check_friend_add_enabled()  # 2.1
        self.add_target_friend('outwhite01')  # 2.2
        self.add_target_friend('inwhite01')  # 2.3
        self.delete_target_friend('outwhite01')
        self.delete_target_friend('inwhite01')

    def add_target_friend(self, member_name):
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_friend_add()
        self.wp.main_page().add_friend(member_name)

    def delete_target_friend(self, member_name):
        self.wp.main_page().switch_tab_to('好友')
        self.wp.friend_page().check_show_btn()
        self.wp.friend_page().search_friend(member_name)
        self.wp.friend_page().into_chatroom()
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().friend_delete()

    # 測試 - [後台]會員添加好友'關閉' & [後台]好友添加白名單'加入/移除'被添加方 >>> [前台]確認非白名單成員搜尋白名單/非白名單內成員功能
    @DecorateClass('CHATAPP-T2542')
    def test_contact_whitelist_setting_be_fe_linkage(self):
        """
        添加方: 非白名單內成員
        0. (後台)會員添加好友 > 關閉:
            1.0. (後台)被添加方成員 > 添加至白名單內:
                1.1. (前台)個人資訊 >>> 可見"新增好友"選項
                1.2. (前台)個人資訊 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
                1.3. (前台)個人資訊 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
            2.0. (後台)被添加方成員 > 從白名單移除:
                2.1. (前台)個人資訊 >>> 可見"新增好友"選項
                2.2. (前台)個人資訊 > 新增好友 > 搜尋"非白名單成員(outwhite01) >>> 跳"暫不支援此功能" toast
                2.3. (前台)個人資訊 > 新增好友 > 搜尋"白名單成員(inwhite01) >>> 顯示該成員個人資訊 & 成功加入通訊錄
        3. (後台)會員添加好友 > 開啟
        """
        self.test_admin_login()
        self.ad.main_page().disable_member_add_friend_setting()  # 0
        self.ad.main_page().into_system_contact_whitelist_setting()
        self.ad.main_page().add_member_to_contact_whitelist(self.web_account)  # 1.0

        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().check_friend_add_enabled()  # 1.1
        self.add_target_friend('outwhite01')  # 1.2
        self.add_target_friend('inwhite01')  # 1.3
        self.delete_target_friend('outwhite01')
        self.delete_target_friend('inwhite01')

        self.test_admin_login()
        self.ad.main_page().into_system_contact_whitelist_setting()
        self.ad.main_page().delete_member_from_contact_whitelist(self.web_account)  # 2.0

        self.wp.main_page().open_user_info()
        self.wp.main_page().check_friend_add_enabled()  # 2.1
        self.wp.main_page().into_friend_add()
        self.wp.main_page().add_friend('outwhite01', '暂不支援此功能')  # 2.2
        self.add_target_friend('inwhite01')  # 2.3
        self.delete_target_friend('inwhite01')

        self.ad.main_page().into_system_contact_whitelist_setting()
        self.ad.main_page().enable_member_add_friend_setting()  # 3

    # 測試 - [後台]會員添加好友'關閉/開啟' >>> [前台]確認非白名單成員透過'ID/手機號'搜尋'白名單/非白名單'成員功能
    @DecorateClass('CHATAPP-T2545')
    def test_search_friend_by_phone_and_ID(self):
        """"
        添加方: 非白名單內成員
        1. (後台)會員添加好友 > 關閉
            1.1. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>>
                gu: 跳"暂不支援手机号搜索" toast
                chit: 跳"暫不支援此功能" toast
            1.2. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 跳"暂不支援此功能" toast
            1.3. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>>
                gu: 跳"暂不支援手机号搜索" toast
                chit: 搜尋的到, 且可以加
            1.4. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 成功加入通訊錄
        2. (後台)會員添加好友 > 開啟
            2.1. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋非白名單成員(8613141010102) >>>
                gu: 跳"暂不支援手机号搜索" toast
                chit: 搜尋的到, 且可以加
            2.2. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋非白名單成員(outwhite02) >>> 顯示該成員個人資訊 & 成功加入通訊錄
            2.3. (前台)個人資訊 > 新增好友 > 透過'手機號'搜尋白名單成員(8613141010103) >>>
                gu: 跳"暂不支援手机号搜索" toast
                chit: 搜尋的到, 且可以加
            2.4. (前台)個人資訊 > 新增好友 > 透過'ID'搜尋白名單成員(inwhite02) >>> 顯示該成員個人資訊 & 成功加入通訊錄
         """
        self.test_admin_login()

        self.ad.main_page().disable_member_add_friend_setting()  # 1
        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_friend_add()

        if self.brand == 'chit':
            self.wp.main_page().add_friend('8613141010102', '暂不支援此功能')  # 1.1
            self.wp.main_page().add_friend('outwhite02', '暂不支援此功能')  # 1.2
            self.add_target_friend('8613141010103')  # 1.3
            self.delete_target_friend('inwhite02')
            self.add_target_friend('inwhite02')  # 1.4
            self.delete_target_friend('inwhite02')
        else:
            self.wp.main_page().add_friend('8613141010102', '暂不支援手机号搜索')  # 1.1
            self.wp.main_page().add_friend('outwhite02', '暂不支援此功能')  # 1.2
            self.wp.main_page().add_friend('8613141010103', '暂不支援手机号搜索')  # 1.3
            self.add_target_friend('inwhite02')  # 1.4
            self.delete_target_friend('inwhite02')

        self.test_admin_login()

        self.ad.main_page().enable_member_add_friend_setting()  # 2
        self.wp.base_page().switch_last_page()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_friend_add()

        if self.brand == 'chit':
            self.add_target_friend('8613141010102')  # 2.1
            self.add_target_friend('8613141010103')  # 2.3
            self.delete_target_friend('outwhite02')
            self.delete_target_friend('inwhite02')
            self.add_target_friend('outwhite02')  # 2.2
            self.add_target_friend('inwhite02')  # 2.4
            self.delete_target_friend('outwhite02')
            self.delete_target_friend('inwhite02')
        else:
            self.wp.main_page().add_friend('8613141010102', '暂不支援手机号搜索')  # 2.1
            self.wp.main_page().add_friend('8613141010103', '暂不支援手机号搜索')  # 2.3
            self.add_target_friend('outwhite02')  # 2.2
            self.add_target_friend('inwhite02')  # 2.4
            self.delete_target_friend('outwhite02')
            self.delete_target_friend('inwhite02')

    # 測試-新增好友
    @DecorateClass('CHATAPP-T1803')
    def test_add_friend(self):
        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_friend_add()
        new_friend = self.wp.main_page().add_friend(self.operate_account)
        if new_friend:
            self.wp.friend_page().check_friend(self.operate_account)

    # 測試-好友暱稱
    @DecorateClass('CHATAPP-T1804')
    def test_friend_remark(self):
        self.test_web_login()

        self.wp.main_page().switch_tab_to('好友')
        self.wp.friend_page().check_show_btn()
        self.wp.friend_page().search_friend(self.operate_account)
        self.wp.friend_page().into_chatroom()
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().friend_nickname()
        self.wp.chatroom_page().friend_remark()

    # 測試-好友黑名單
    @DecorateClass('CHATAPP-T1805')
    def test_block_friend(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().friend_block()
        self.wp.main_page().switch_tab_to('好友')
        self.wp.friend_page().check_notexist(self.operate_account)

    # 測試-好友黑名單設定
    @DecorateClass('CHATAPP-T1806')
    def test_block_setting(self):
        self.test_web_login()

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_black_page()
        self.wp.black_page().into_blocker(self.operate_account)
        self.wp.black_page().check_block_info(self.operate_account)

    # 測試-解除好友黑名單
    @DecorateClass('CHATAPP-T1807')
    def test_unblock_friend(self):
        self.test_web_login()

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_friend_add()
        self.wp.main_page().search_member(self.operate_account)
        self.wp.main_page().unblock_member()

    # 測試-分享網址功能
    @DecorateClass('CHATAPP-T1798')
    def test_share_url(self):
        self.test_web_login()

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_share_page()
        share_url = self.wp.share_page().get_share_link()
        self.wp.main_page().close_modal(2)

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_message(share_url)
        self.wp.chatroom_page().check_url_message(share_url)

    # 測試-個人發送文字超連結訊息
    @DecorateClass('CHATAPP-T1808')
    def test_send_message(self):
        self.test_web_login()
        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_text_message()
        self.wp.chatlist_page().check_last_message()
        self.wp.chatroom_page().send_url_message()
        self.wp.chatlist_page().check_last_message()

    # 測試-A在與B的聊天室內發送圖片/影片 > B端確認該圖片影片與A端相同
    @DecorateClass('CHATAPP-T2543')
    def test_send_media(self):
        # -----------A端: 帳號A登入 > 與B的1v1聊天室內傳送圖片 > 獲取聊天室內該圖片src link > 帳號A登出
        self.test_web_login()  # login web_id
        self.wp.chatlist_page().into_chat_room(self.app_account)  # into to app_id chatroom
        self.wp.chatlist_page().delete_chatroom_record()
        self.wp.chatlist_page().into_chat_room(self.app_account)
        self.wp.chatroom_page().send_media(media_type='photo')  # send picture to chatroom
        a_side_image_src_link = self.function_dict[
            'wp'].chatroom_page().get_last_media_src_link()  # 取得聊天室該image的src link
        self.test_web_logout()

        # -----------B端: 帳號B登入 > 進入與A的1v1聊天室 > 獲取聊天室內A傳送的圖片src link > 與A端獲取的src_link做比對
        self.wp.login_page().login(self.app_phone, self.app_password,
                                                   self.app_nation)  # login app_id
        self.wp.chatlist_page().into_chat_room(self.web_account)  # into to web_id chatroom
        assert self.function_dict[
                   'wp'].chatroom_page().get_last_media_src_link() == a_side_image_src_link, '發送與接收端圖片不同'
        assert self.function_dict[
                   'wp'].chatlist_page().get_chat_list_msg_text() == f'{self.web_account}：[图片]', '聊天列表該聊天室最後一筆訊息顯示錯誤'
        self.wp.chatlist_page().delete_chatroom_record()
        self.wp.chatlist_page().into_chat_room(self.web_account)
        # -----------B端: 與A的1v1聊天室內傳送影片 > 獲取聊天室內該影片src link > 帳號B登出
        self.wp.chatroom_page().send_media(media_type='video')  # send video to chatroom
        b_side_video_src_link = self.wp.chatroom_page().get_last_media_src_link(
            'video')  # 獲取聊天室該video的src link
        self.test_web_logout()

        # -----------A端: 帳號A登入 > 進入與B的1v1聊天室 > 獲取聊天室內B傳送的影片src link > 與B端獲取的src_link做比對
        self.wp.login_page().login(self.web_phone, self.web_password,
                                                   self.web_nation)  # login web_id
        self.wp.chatlist_page().into_chat_room(self.app_account)  # into to app_id chatroom
        assert self.wp.chatroom_page().get_last_media_src_link(
            'video') == b_side_video_src_link, '發送與接收端影片不同'
        assert self.function_dict[
                   'wp'].chatlist_page().get_chat_list_msg_text() == f'{self.app_account}：[视频]', '聊天列表該聊天室最後一筆訊息顯示錯誤'

    # 測試-個人訊息複製
    @DecorateClass('CHATAPP-T1809')
    def test_message_copy(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_copy('測試TeSt12345!@#$%测试#0')
        self.wp.chatlist_page().check_last_message()

    # 測試-個人訊息回覆
    @DecorateClass('CHATAPP-T1810')
    def test_message_reply(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_reply('測試TeSt12345!@#$%测试#3')
        self.wp.chatlist_page().check_last_message()

    # 測試-個人訊息撤回
    @DecorateClass('CHATAPP-T1811')
    def test_message_revoke(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#3')
        self.wp.chatlist_page().check_last_message()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#5')

    # 測試-個人訊息回覆後撤回
    @DecorateClass('CHATAPP-T1926')
    def test_message_reply_revoke(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_message('測試撤回使用訊息')
        self.wp.chatroom_page().message_reply('測試撤回使用訊息')
        self.wp.chatroom_page().message_revoke('測試撤回使用訊息')
        self.wp.chatroom_page().check_reply_disappear('測試撤回使用訊息')

        self.wp.chatlist_page().check_last_message()

    # 測試-訊息表情符號
    @DecorateClass('CHATAPP-T1937')
    def test_message_emoji(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_message('表情符號使用訊息')
        self.wp.chatroom_page().add_message_emoji('表情符號使用訊息')

    # 測試-個人訊息設置公告
    @DecorateClass('CHATAPP-T1812')
    def test_message_pin(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_copy('測試TeSt12345!@#$%测试#5')
        self.wp.chatroom_page().pin_full_messages()
        self.wp.chatroom_page().delete_all_pin()

    # 測試-個人訊息設置公告後回覆
    @DecorateClass('CHATAPP-T1813')
    def test_message_pin_reply(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_reply('測試TeSt12345!@#$%测试#3')
        self.wp.chatroom_page().message_pin('回覆訊息測試Test')
        self.wp.chatroom_page().delete_all_pin()

    # 測試-個人訊息設置公告後撤回
    @DecorateClass('CHATAPP-T1814')
    def test_message_pin_revoke(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().pin_full_messages()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#4')
        self.wp.chatroom_page().delete_all_pin()

    # 測試-個人發送檔案訊息
    @DecorateClass('CHATAPP-T3272')
    def test_send_file_message(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatlist_page().check_last_message(message_type='file')

    # 測試-個人檔案訊息回覆
    @DecorateClass('CHATAPP-T3273')
    def test_file_message_reply(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        file_name = self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatroom_page().message_reply(file_name,message_type='file')
        self.wp.chatlist_page().check_last_message()

    # 測試-個人撤回檔案訊息
    @DecorateClass('CHATAPP-T3274')
    def test_file_message_revoke(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatroom_page().send_message('私聊檔案訊息Test_文字訊息')
        file_name = self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatroom_page().message_revoke(file_name, message_type='file')
        self.wp.chatlist_page().into_chat_room(self.operate_account)
        self.wp.chatlist_page().check_last_message()

    # 測試-建立群組
    @DecorateClass('CHATAPP-T1938')
    def test_groups_build(self):
        self.test_web_login()

        self.wp.main_page().open_user_info()
        self.wp.main_page().check_groups_build()
        self.wp.main_page().groups_build(self.web_account, self.get_group_name())
        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatlist_page().check_group_build(self.web_account, self.get_group_name())

    # 測試-變更群組名稱
    @DecorateClass('CHATAPP-T1939')
    def test_group_name_change(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().change_group_name(self.get_group_name(), 'nametest')
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().change_group_name('nametest', self.get_group_name())

    # 測試-變更群組權限設定
    @DecorateClass('CHATAPP-T1940')
    def test_group_rule_all(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().all_group_rule()

    # 測試-群組發送文字超連結訊息
    @DecorateClass('CHATAPP-T1815')
    def test_send_message_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_text_message()
        self.wp.chatlist_page().check_last_message()
        self.wp.chatroom_page().send_url_message()
        self.wp.chatlist_page().check_last_message()

    # 測試-群組訊息複製
    @DecorateClass('CHATAPP-T1816')
    def test_message_copy_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_copy('測試TeSt12345!@#$%测试#0')
        self.wp.chatlist_page().check_last_message()

    # 測試-群組發訊息回覆
    @DecorateClass('CHATAPP-T1817')
    def test_message_reply_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_reply('測試TeSt12345!@#$%测试#3')
        self.wp.chatlist_page().check_last_message()

    # 測試-群組訊息撤回
    @DecorateClass('CHATAPP-T1818')
    def test_message_revoke_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#3')
        self.wp.chatlist_page().check_last_message()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#5')

    # 測試-群組訊息設置公告
    @DecorateClass('CHATAPP-T1819')
    def test_message_pin_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_copy('測試TeSt12345!@#$%测试#5')
        self.wp.chatroom_page().pin_full_messages()
        self.wp.chatroom_page().delete_all_pin()

    # 測試-群組訊息設置公告後回覆
    @DecorateClass('CHATAPP-T1820')
    def test_message_pin_reply_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().message_reply('測試TeSt12345!@#$%测试#3')
        self.wp.chatroom_page().message_pin('回覆訊息測試Test')
        self.wp.chatroom_page().delete_all_pin()

    # 測試-群組訊息設置公告後撤回
    @DecorateClass('CHATAPP-T1821')
    def test_message_pin_revoke_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_text_message()
        self.wp.chatroom_page().delete_all_pin()
        self.wp.chatroom_page().pin_full_messages()
        self.wp.chatroom_page().message_revoke('測試TeSt12345!@#$%测试#4')
        self.wp.chatroom_page().delete_all_pin()

    # 測試-個人發送檔案訊息
    @DecorateClass('CHATAPP-T3277')
    def test_send_file_message_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatlist_page().check_last_message(message_type='file')

    # 測試-個人檔案訊息回覆
    @DecorateClass('CHATAPP-T3275')
    def test_file_message_reply_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        file_name = self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatroom_page().message_reply(file_name, message_type='file')
        self.wp.chatlist_page().check_last_message()

    # 測試-群組撤回檔案訊息
    @DecorateClass('CHATAPP-T3276')
    def test_file_message_revoke_group(self):
        self.test_web_login()

        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatroom_page().send_message('群組檔案訊息Test_文字訊息')
        file_name = self.wp.chatroom_page().send_media(media_type='file')
        self.wp.chatroom_page().message_revoke(file_name, message_type='file')
        self.wp.chatlist_page().into_chat_room(self.get_group_name())
        self.wp.chatlist_page().check_last_message()

    # 測試-刪除好友
    @DecorateClass('CHATAPP-T1822')
    def test_delete_friend(self):
        self.test_web_login()

        self.wp.main_page().switch_tab_to('好友')
        self.wp.friend_page().check_show_btn()
        self.wp.friend_page().search_friend(self.operate_account)
        self.wp.friend_page().into_chatroom()
        self.wp.chatroom_page().into_setting()
        self.wp.chatroom_page().friend_delete()
        self.wp.friend_page().check_notExist(self.operate_account)

    # 測試-登出
    @DecorateClass('CHATAPP-T1791')
    def test_web_logout(self):
        self.test_web_login()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_security_page()
        self.wp.security_page().logout()

    # 測試-綁定正確的錢包並兌換積分 (順付)
    @DecorateClass('CHATAPP-T2524')
    def test_exchange_wellpay(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        if self.brand == 'gu':
            wellpay_address = '0xe1d6cfe14f9f23d49c2637695a1570f3fa3049bb'
        else:
            wellpay_address = '0x90ebd6ff86db243597294150e472a80a3fb84d40'
        exchange_amount = 1

        self.test_admin_login_to_memberlist()
        self.ad.member_page().unbind_wellpay(member_ID)

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.base_page().open_base_url()  # 開啟前台網站
        self.wp.login_page().login(web_phone, web_password, self.web_nation)

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        self.wp.integral_page().entry_exchange_page()
        self.wp.integral_page().bind_wellpay(wellpay_address, self.security_code)
        bind_time = datetime.now().strftime("%Y/%m/%d %H:%M")

        self.test_admin_login_to_memberlist()
        self.ad.member_page().check_wellpay_bind_data(member_ID, bind_time, wellpay_address)
        self.ad.member_page().refresh_browser()
        self.wp.integral_page().wellpay_exchange(self.security_code, exchange_amount)
        self.ad.member_page().unbind_wellpay(member_ID)

    # 測試-綁定錯誤的錢包並兌換積分 (順付)
    @DecorateClass('CHATAPP-T2525')
    def test_exchange_wellpay_incorrect(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        wellpay_address_incorrect = '123'
        exchange_amount = 3

        self.test_admin_login_to_memberlist()
        self.ad.member_page().unbind_wellpay(member_ID)

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()
        self.wp.base_page().open_base_url()
        self.wp.login_page().login(web_phone, web_password, self.web_nation)

        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()

        self.wp.integral_page().entry_exchange_page()
        self.wp.integral_page().bind_wellpay(wellpay_address_incorrect, self.security_code)
        self.wp.integral_page().wellpay_exchange_incorrect(self.security_code, exchange_amount)

        self.test_admin_login_to_memberlist()
        self.ad.member_page().unbind_wellpay(member_ID)

    # 測試-兌換平臺積分 (sc)
    @DecorateClass('CHATAPP-T2753')
    def test_exchange_brand(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        operate_type = '平台'
        brand = 'SC'
        env = 'uat'
        brand_account = 'cmtest006'
        brand_pw = 'ps43941122'
        # =========================== 登入SC平臺, 設定股聊積分兌換數值 =====================
        self.wp.brand_page().into_brand_page(brand, env, brand_account, brand_pw)
        before_main_wallet_money = self.wp.brand_page().get_main_wallet_money()
        exchange_address, exchange_amount = self.wp.brand_page().online_deposit()
        # =========================== 登入前臺, 獲取原股聊積分 =============================
        self.wp.base_page().open_base_url()
        self.wp.login_page().login(web_phone, web_password, self.web_nation)
        self.wp.main_page().open_user_info()
        remain_integral_amount_before = self.wp.main_page().into_integral_page()  # 獲取原積分

        # =========================== 前台綁定平臺SC, 並兌換積分 ==========================
        self.wp.integral_page().entry_exchange_page()
        self.wp.integral_page().bind_brand_and_exchange(exchange_address, self.security_code)
        self.wp.main_page().into_integral_page()
        remain_integral_amount_after = self.wp.integral_page().exchange_record_check(exchange_amount, operate_type, None, remain_integral_amount_before)

        # =========================== 後台確認積分使用紀錄 ================================
        self.test_admin_login()
        self.ad.main_page().into_integral_record()
        self.ad.water_recode_page().check_current_exchange_record(member_ID, None, f'-{str(exchange_amount)}', f'{operate_type}-{brand}', None, remain_integral_amount_after)  # [後台]積分使用紀錄頁確認積分訊息

        # =========================== 解綁平臺 ===========================================
        self.test_admin_login_to_memberlist()
        self.ad.member_page().unbind_brand(member_ID)

        # =========================== SC平臺端確認積分紀錄 =================================
        self.wp.base_page().switch_home_page()
        after_main_wallet_money = self.wp.brand_page().get_main_wallet_money()
        self.wp.brand_page().check_deposit_record(before_main_wallet_money, exchange_amount, after_main_wallet_money)

    # 測試-人工存入積分 & 人工提出積分
    @DecorateClass('CHATAPP-T2547')
    def test_manual_deposit_and_withdraw(self):
        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_id = 'exchange0'
        integral_amount = '12.34'

        self.wp.login_page().login(web_phone, web_password, self.web_nation)
        self.wp.main_page().open_user_info()
        remain_integral_amount_deposit_before = self.wp.main_page().into_integral_page()  # 獲得原積分

        # =========================== 後台人工存入積分-檢舉獎金 ======================================
        self.test_admin_login()
        self.ad.main_page().into_manual_deposit()
        self.ad.main_page().manual_add_deposit(member_id, integral_amount)  # 後台人工存入積分
        add_deposit_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # =========================== 前台確認存入積分紀錄 ======================================
        self.wp.base_page().refresh_browser()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        current_total_integral_amount = self.wp.integral_page().exchange_record_check(integral_amount, '人工存入_检举奖金', add_deposit_time, remain_integral_amount_deposit_before)  # 前台積分詳情頁確認積分變動紀錄

        # =========================== 後台人工提出積分 ======================================
        self.ad.main_page().into_manual_withdraw()
        self.ad.main_page().manual_add_withdraw(member_id, integral_amount)  # 後台人工提出積分
        add_withdraw_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # =========================== 前台確認提出積分紀錄 ======================================
        self.wp.base_page().refresh_browser()
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        self.wp.integral_page().exchange_record_check(integral_amount, '人工提出_红包误存', add_withdraw_time, current_total_integral_amount)  # 前台積分詳情頁確認積分變動兌換紀錄

    # 測試-搶一般紅包
    @DecorateClass('CHATAPP-T2548')
    def test_grab_red_envelope(self):
        red_envelope_type = '发红包'
        self.test_web_login()
        self.wp.main_page().open_user_info()
        remain_integral_amount_before = self.wp.main_page().into_integral_page()
        self.wp.chatlist_page().into_chat_room(self.test_group)
        grab_time, grab_amount = self.wp.chatroom_page().grab_red_envelope(red_envelope_type)  # [前台]搶紅包, 回傳紅包時間+金額
        self.wp.chatroom_page().check_chatroom_system_message(self.web_account, grab_amount)  # 確認聊天室內搶紅包系統訊息
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        remain_integral_amount = self.wp.integral_page().exchange_record_check(grab_amount, red_envelope_type, grab_time, remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.ad.main_page().into_red_list()
        self.ad.red_envelope_page().red_envelope_detail_check(self.web_account, grab_amount, red_envelope_type, grab_time)  # 後台紅包詳情頁確認明細
        self.ad.main_page().into_integral_record()
        self.ad.water_recode_page().check_current_exchange_record(self.web_account, grab_time, grab_amount, red_envelope_type, self.test_group, remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-搶拚手氣紅包
    @DecorateClass('CHATAPP-T2549')
    def test_grab_luck_red_envelope(self):
        red_envelope_type = '拼手气红包'
        self.test_web_login()
        self.wp.main_page().open_user_info()
        remain_integral_amount_before = self.wp.main_page().into_integral_page()
        self.wp.chatlist_page().into_chat_room(self.test_group)
        grab_time, grab_amount = self.wp.chatroom_page().grab_red_envelope(red_envelope_type)  # [前台]搶紅包, 回傳紅包時間+金額
        self.wp.chatroom_page().check_chatroom_system_message(self.web_account, grab_amount)  # 確認聊天室內搶紅包系統訊息
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        remain_integral_amount = self.wp.integral_page().exchange_record_check(grab_amount, red_envelope_type, grab_time, remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.ad.main_page().into_red_list()
        self.ad.red_envelope_page().red_envelope_detail_check(self.web_account, grab_amount, red_envelope_type, grab_time)  # 後台紅包詳情頁確認明細
        self.ad.main_page().into_integral_record()
        self.ad.water_recode_page().check_current_exchange_record(self.web_account, grab_time, grab_amount, red_envelope_type, self.test_group, remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-自動領取一般紅包
    @DecorateClass('CHATAPP-T2570')
    def test_auto_grab_red_envelope(self):
        red_envelope_type = '发红包'
        self.test_web_login()
        self.wp.main_page().open_user_info()
        remain_integral_amount_before = self.wp.main_page().into_integral_page()
        self.wp.chatlist_page().into_chat_room(self.test_group)

        sleep(180)  # 等待系統trigger發送紅包 & 搶紅包機器人執行搶紅包

        name, amount = self.wp.chatroom_page().check_chatroom_system_message(None,None)  # 確認聊天室內紅包系統訊息
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        remain_integral_amount = self.wp.integral_page().exchange_record_check(amount, red_envelope_type, None, remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.ad.main_page().into_red_list()
        self.ad.red_envelope_page().red_envelope_detail_check(self.web_account, amount, red_envelope_type, None)  # 後台紅包詳情頁確認明細
        self.ad.main_page().into_integral_record()
        self.ad.water_recode_page().check_current_exchange_record(self.web_account, None, amount, red_envelope_type, self.test_group,remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-搶拚手氣紅包
    @DecorateClass('CHATAPP-T2571')
    def test_auto_grab_luck_red_envelope(self):
        red_envelope_type = '拼手气红包'
        self.test_web_login()
        self.wp.main_page().open_user_info()
        remain_integral_amount_before = self.wp.main_page().into_integral_page()
        self.wp.chatlist_page().into_chat_room(self.test_group)

        sleep(180)  # 等待系統trigger發送紅包 & 搶紅包機器人執行搶紅包

        name, amount = self.wp.chatroom_page().check_chatroom_system_message(None, None)  # 確認聊天室內紅包系統訊息
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_integral_page()
        remain_integral_amount = self.wp.integral_page().exchange_record_check(amount, red_envelope_type, None, remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.ad.main_page().into_red_list()
        self.ad.red_envelope_page().red_envelope_detail_check(self.web_account, amount, red_envelope_type, None)  # 後台紅包詳情頁確認明細
        self.ad.main_page().into_integral_record()
        self.ad.water_recode_page().check_current_exchange_record(self.web_account, None, amount, red_envelope_type, self.test_group,remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試 - [後台]設定邀請碼權限 > [前台]登入一般成員 & 管理員帳號確認邀請碼分享欄位顯示與否
    @DecorateClass('CHATAPP-T2569')
    def test_share_code_visible_when_permission_change(self):
        share_code = "PERMISS"
        group_name = "ShareCodePermissTest"

        # ========================= 群組一般成員 =========================
        user = "gubot02"  # 一般成員
        self.test_admin_login()
        self.ad.main_page().into_share_code()
        self.ad.main_page().modify_share_code(share_code, permission=1)  # 分享權限設為"所有成員"

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.base_page().open_base_url()  # 開啟前台網站
        self.wp.login_page().login(self.web_phone, self.web_password, self.web_nation)  # 登入群組權限"一般成員"用戶
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=1)  # 確認前台可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.ad.main_page().modify_share_code(share_code, permission=2)  # 分享權限設為"僅後台"

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=2)  # 確認前台不可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.ad.main_page().modify_share_code(share_code, permission=3)  # 分享權限設為"僅管理員"

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=3)  # 確認前台不可見邀請碼分享欄位

        # ========================= 群組管理員 =========================
        user = "gubot03"  # 管理員
        self.wp.main_page().open_user_info()
        self.wp.main_page().into_security_page()
        self.wp.security_page().logout()
        self.wp.login_page().login(self.app_phone, self.app_password, self.web_nation)  # 登入群組權限"管理員"用戶
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=3)  # 確認前台可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.test_admin_login()
        self.ad.main_page().into_share_code()
        self.ad.main_page().modify_share_code(share_code, permission=2)  # 分享權限設為"僅後台"

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=2)  # 確認前台不可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.ad.base_page().windows_to_top()  # 切換視窗
        self.ad.main_page().modify_share_code(share_code, permission=1)  # 分享權限設為"所有成員"

        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name, user, permission=1)  # 確認前台可見邀請碼分享欄位

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method

    # 測試用範例 - 傳送特定資料夾下隨機n個picture/video到聊天室內===============================================================
    @DecorateClass('')
    def test_test(self):
        self.test_web_login()
        self.wp.chatlist_page().into_chat_room('Taiwan0101')
        self.wp.chatlist_page().delete_chatroom_record()
        self.wp.chatlist_page().into_chat_room('Taiwan0101')
        self.wp.chatroom_page().send_video()
        aaaaa = self.wp.chatroom_page().get_last_media_src_link()
        # for _ in range(5):
        #     self.wp.chatroom_page().random_send_medias_to_chatroom(5, r'C:\Users\york_tu\Desktop\test_media_folder')
        # sleep(1000000)

    def test_build_hundred_groups(self):
        self.test_all_windows_mini()
        self.wp.base_page().windows_to_top()  # 切換視窗
        self.wp.base_page().open_base_url()  # 開啟前台網站
        self.wp.login_page().login('958002220', '1qaz2wsx', 'TW')
        self.wp.main_page().open_user_info()
        self.wp.main_page().build_hundred_groups()




