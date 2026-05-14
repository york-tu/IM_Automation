import os
import random
import sys
import re
from datetime import datetime
from time import sleep
import time

from Project.chat.web.pages.pages import WebPages, WapPages, AdminPages
from Project.chat.web.testcase.base_testcase import BaseTestCase
from Project.chat.web.pages.admin.admin_redenvelopepage import RedEnvelopePageLocator, RedEnvelopePage
from Project.chat.web.pages.admin.admin_water_recode_page import WaterRecodePage

from common.utils.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass


class WapTestCase(BaseTestCase):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    chrome_crash = 0
    folder_path = ''
    group_name = datetime.now().strftime("%y%m%d") + "_bot_group"
    mail_account_id = f'mail{datetime.now().strftime("%m%d%H%M")}'
    security_code = 111111
    function_dict = {}
    driver_list = []

    brand = gl.get_value('BRAND')
    env = gl.get_value('ENV')
    account_type = gl.get_value('ACCOUNT_TYPE')

    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folder_path = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        current_wap_version = cls.function_dict['wap'].wap_main_page().return_wap_version()  # 獲取web版本號
        gl.set_value('APP_VERSION', current_wap_version)

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

        # self.test_all_windows_mini()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
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
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
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
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=True))  # 設定ChromeDriver
        cls.function_dict['wap'] = WapPages(cls.driver_list[-1], cls.wait_time, cls.wap_url, cls.skipTest)  # 導入Wap全部頁面
        cls.function_dict['wap'].base_page().hide_windows()

        # if not sys.argv[0].__contains__('prod'):
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
        cls.function_dict['ad'] = AdminPages(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
        cls.function_dict['ad'].base_page().hide_windows()

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
            function.base_page().windows_to_top(full=True)

    def get_group_name(self):
        if self.env == 'prod':
            return 'QA_bot_only'
        elif self.env == 'uat':
            return str(datetime.now().strftime("%y%m%d") + "_group")

    # 登入
    @DecorateClass('CHATAPP-T3205')
    def test_wap_login(self):
        self.test_all_windows_mini()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        if 'mail' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.wap_phone, self.wap_password, self.web_nation)

    # ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password)  # 登入admin

    # 登出
    @DecorateClass('CHATAPP-T3206')
    def test_wap_logout(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_main_page().into_main_page()
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_security_page()
        self.function_dict['wap'].wap_main_personal_page().logout()

    # 版本確認
    @DecorateClass('CHATAPP-T3204')
    def test_version_check(self):
        self.test_wap_login()
        wap_version = self.wap_version
        self.function_dict['wap'].wap_main_page().into_main_page()
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_about_page()
        self.function_dict['wap'].wap_main_personal_page().check_version(wap_version)

    # 進入主頁_我的設定頁
    @DecorateClass('CHATAPP-T3215')
    def test_into_member(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()

    # 進入好友名單頁
    @DecorateClass('CHATAPP-T3216')
    def test_into_friend(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_friends_page().into_friend_list()

    # 進入主頁_我的設定頁_關於股聊
    @DecorateClass('CHATAPP-T3217')
    def test_about_terms(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_about_page()
        self.function_dict['wap'].wap_main_personal_page().check_service()
        self.function_dict['wap'].wap_main_personal_page().check_privacy()

    # 修改登入密碼
    @DecorateClass('CHATAPP-T3218')
    # 修改登入密碼
    def test_change_password(self):
        self.test_wap_login()
        new_pwd = 'Ps43941122'
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_security_page()
        self.function_dict['wap'].wap_main_personal_page().change_password(self.wap_password, new_pwd)
        self.test_wap_logout()

        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁

        if 'mail' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.mail_address, new_pwd, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.wap_phone, new_pwd, self.wap_nation)

        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_security_page()
        self.function_dict['wap'].wap_main_personal_page().change_password(new_pwd, self.wap_password)
        self.test_wap_logout()

        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁

        if 'mail' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.wap_phone, self.wap_password, self.wap_nation)

    # 更改自己暱稱 & 個人簡介
    @DecorateClass('CHATAPP-T3219')
    def test_change_nickname_and_instructions(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_main_page().into_main_page()
        original_nickname = self.function_dict['wap'].wap_main_page().get_nickname()
        original_descriptions = self.function_dict['wap'].wap_main_page().get_descriptions().rstrip()
        self.function_dict['wap'].wap_main_page().change_nickname('gutest1234')
        self.function_dict['wap'].wap_main_page().change_nickname(original_nickname)
        self.function_dict['wap'].wap_main_page().change_descriptions('mWebChangeDescriptionsTest')
        self.function_dict['wap'].wap_main_page().change_descriptions(original_descriptions)

    # 新增好友
    @DecorateClass('CHATAPP-T3264')
    def test_add_friend(self):
        self.test_wap_login()

        self.function_dict['wap'].wap_message_page().into_chat_page()
        self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
        new_friend = self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)

        if not new_friend:
            self.function_dict['wap'].wap_friends_page().delete_friend_from_UserDetail(self.operate_account)
            self.function_dict['wap'].wap_message_page().into_chat_page()
            self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
            assert self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)

        self.function_dict['wap'].wap_friends_page().add_friend(self.operate_account)
        self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
        assert not self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)

    # 好友頁面備註暱稱&描述
    @DecorateClass('CHATAPP-T3284')
    def test_friend_remark(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_friends_page().into_friend_list()
        self.function_dict['wap'].wap_friends_page().list_friend_search(self.operate_account)
        self.function_dict['wap'].wap_friends_page().set_remark_note('mWeb編輯好友描述Test')
        self.function_dict['wap'].wap_friends_page().set_remark_nickname('mWeb編輯好友暱稱Test')

    # 測試-好友加入黑名單 & 檢舉
    @DecorateClass('CHATAPP-T3281')
    def test_block_and_report_friend(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_friends_page().block_friend()
        self.function_dict['wap'].wap_friends_page().report()

    # 測試-解除好友黑名單
    @DecorateClass('CHATAPP-T3282')
    def test_unblock_friend(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_main_personal_page().into_main_setting_page()
        self.function_dict['wap'].wap_main_personal_page().into_blocklist_page()
        self.function_dict['wap'].wap_main_personal_page().search_blocked_friend(self.operate_account)
        self.function_dict['wap'].wap_main_personal_page().unblock_friend()

    # 刪除好友
    @DecorateClass('CHATAPP-T3263')
    def test_delete_friend(self):
        self.test_wap_login()

        self.function_dict['wap'].wap_message_page().into_chat_page()
        self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
        new_friend = self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)

        if new_friend:
            self.function_dict['wap'].wap_friends_page().add_friend(self.operate_account)
            self.function_dict['wap'].wap_friends_page().back_to_message_page()
            self.function_dict['wap'].wap_message_page().into_chat_page()
            self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
            assert not self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)
        self.function_dict['wap'].wap_friends_page().delete_friend_from_UserDetail(self.operate_account)

    # 私聊-發送訊息
    @DecorateClass('CHATAPP-T3221')
    def test_1v1_send_message(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        # ======================= 發送"訊息"測試 =================================================
        last_text = self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(last_text)
        # ======================= 發送"超連結"測試 ===============================================
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        last_url = self.function_dict['wap'].wap_message_page().send_url_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(last_url)

    # 私聊-複製文訊息 > 貼上 > 發送
    @DecorateClass('CHATAPP-T3249')
    def test_1v1_message_copy(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().message_copy('mWeb發訊息TeSt!@#$%_3')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message('mWeb發訊息TeSt!@#$%_3')

    # 私聊-回覆文字訊息
    @DecorateClass('CHATAPP-T3222')
    def test_1v1_message_reply(self):
        self.test_wap_login()
        original_message = 'mWeb發訊息TeSt!@#$%_4'
        reply_text = 'mWeb回覆訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().message_reply(original_message, reply_text)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(reply_text)

    # 私聊-撤回文字訊息
    @DecorateClass('CHATAPP-T3223')
    def test_1v1_message_revoke(self):
        self.test_wap_login()
        revoke_message = 'mWeb_私聊_訊息撤回TeSt!@#$%'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        last_text = self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().send_message(revoke_message)
        self.function_dict['wap'].wap_message_page().message_revoke(revoke_message)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(last_text)

    # 私聊-回覆文字訊息後撤回原訊息
    @DecorateClass('CHATAPP-T3225')
    def test_1v1_message_reply_revoke(self):
        self.test_wap_login()
        reply_original_message = 'mWeb測試用原訊息_私聊_回覆後撤回'
        reply_message = 'mWeb測試:私聊_回覆訊息'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_message(reply_original_message)
        self.function_dict['wap'].wap_message_page().message_reply(reply_original_message, reply_message)
        self.function_dict['wap'].wap_message_page().message_revoke(reply_original_message)
        self.function_dict['wap'].wap_message_page().check_reply_msg('原始讯息已不存在')

    # 私聊-文字訊息添加emoji
    @DecorateClass('CHATAPP-T3226')
    def test_1v1_message_add_emoji(self):
        self.test_wap_login()
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        emoji_message = f'mWeb_私聊_添加emoji測試_{current_time}'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_message(emoji_message)
        self.function_dict['wap'].wap_message_page().add_message_emoji(emoji_message)

    # 私聊-文字訊息設為公告
    @DecorateClass('CHATAPP-T3227')
    def test_1v1_message_pin(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().pin_full_messages()
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 私聊-回覆訊息設為公告
    @DecorateClass('CHATAPP-T3228')
    def test_1v1_message_pin_reply(self):
        self.test_wap_login()
        reply_original_message = 'mWeb測試原訊息_私聊_回覆後設為公告'
        reply_message = 'mWeb測試:回覆訊息(私聊_回覆後設為公告)'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_message(reply_original_message)
        self.function_dict['wap'].wap_message_page().message_reply(reply_original_message, reply_message)
        self.function_dict['wap'].wap_message_page().message_pin(reply_message)
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 私聊-訊息設為公告後撤回
    @DecorateClass('CHATAPP-T3229')
    def test_1v1_message_pin_revoke(self):
        self.test_wap_login()
        original_message = 'mWeb測試原訊息_私聊_設為公告後撤回'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().send_message(original_message)
        self.function_dict['wap'].wap_message_page().message_pin(original_message)
        self.function_dict['wap'].wap_message_page().message_revoke(original_message, pin_revoke=True)
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 私聊-發送語音訊息
    @DecorateClass('CHATAPP-T3231')
    def test_1v1_send_voice_message(self):
        self.test_wap_login()
        voice_length = random.randint(10, 15)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message('语音讯息')

    # 私聊-回覆語音訊息
    @DecorateClass('CHATAPP-T3230')
    def test_1v1_voice_message_reply(self):
        self.test_wap_login()
        voice_length = random.randint(10, 15)
        reply_text = 'mWeb_私聊_回覆語音訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length)
        room_voice_message = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='voice')
        self.function_dict['wap'].wap_message_page().message_reply(room_voice_message, reply_text, message_type='voice')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(reply_text)

    # 私聊-撤回語音訊息
    @DecorateClass('CHATAPP-T3232')
    def test_1v1_voice_message_revoke(self):
        self.test_wap_login()
        voice_length_1 = random.randint(10, 15)
        voice_length_2 = random.randint(1, 10)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length_1)
        room_voice_message_1 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length_2)
        room_voice_message_2 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')
        self.function_dict['wap'].wap_message_page().message_revoke(room_voice_message_2, message_type='voice')
        assert room_voice_message_1 == self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')

    @DecorateClass('CHATAPP-T3265')
    # 個人-發送檔案訊息
    def test_1v1_send_file_message(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_file_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message('档案讯息')

    # 私聊-回覆檔案訊息
    @DecorateClass('CHATAPP-T3266')
    def test_1v1_file_message_reply(self):
        self.test_wap_login()
        reply_text = 'mWeb_私聊_回覆檔案訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().message_reply(room_file_message, reply_text, message_type='file')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(reply_text)

    # 私聊-撤回檔案訊息
    @DecorateClass('CHATAPP-T3267')
    def test_1v1_file_message_revoke(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message_1 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message_2 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().message_revoke(room_file_message_2, message_type='file')
        assert room_file_message_1 == self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='file')

    # 群組-發送文字訊息+超連結
    @DecorateClass('CHATAPP-T3233')
    def test_group_send_message(self):
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        # ======================= 發送"訊息"測試 =================================================
        last_text = self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(f'{account}: {last_text}')
        # ======================= 發送"超連結"測試 ===============================================
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        last_url = self.function_dict['wap'].wap_message_page().send_url_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(f'{account}: {last_url}')

    #  [Done] 群組-訊息複製並發送
    @DecorateClass('CHATAPP-T3239')
    def test_group_message_copy(self):
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().message_copy('mWeb發訊息TeSt!@#$%_4')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(f'{account}: mWeb發訊息TeSt!@#$%_4')

    #  [Done] 群組-回覆訊息
    @DecorateClass('CHATAPP-T3237')
    def test_group_message_reply(self):
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        self.test_wap_login()
        original_message = 'mWeb發訊息TeSt!@#$%_2'
        reply_text = 'mWeb群組_回覆訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().message_reply(original_message, reply_text)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(f'{account}: {reply_text}')

    # [目前聊天列表上私聊最後一筆訊息會顯示對方/自己暱稱] 群組-撤回訊息
    @DecorateClass('CHATAPP-T3238')
    def test_group_message_revoke(self):
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        self.test_wap_login()
        revoke_message = 'mWeb群組_訊息撤回TeSt!@#$%'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        last_text = self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().send_message(revoke_message)
        self.function_dict['wap'].wap_message_page().message_revoke(revoke_message)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(f'{account}: {last_text}')

    # 群聊-訊息回覆後撤回
    @DecorateClass('CHATAPP-T3240')
    def test_group_message_reply_revoke(self):
        self.test_wap_login()
        reply_original_message = 'mWeb測試用原訊息_群聊_回覆後撤回'
        reply_message = 'mWeb測試:群聊_回覆訊息'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_message(reply_original_message)
        self.function_dict['wap'].wap_message_page().message_reply(reply_original_message, reply_message)
        self.function_dict['wap'].wap_message_page().message_revoke(reply_original_message)
        self.function_dict['wap'].wap_message_page().check_reply_msg('原始讯息已不存在')

    # 群聊-訊息添加emoji
    @DecorateClass('CHATAPP-T3241')
    def test_group_message_add_emoji(self):
        self.test_wap_login()
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        emoji_message = f'mWeb_群聊_添加emoji測試_{current_time}'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_message(emoji_message)
        self.function_dict['wap'].wap_message_page().add_message_emoji(emoji_message)

    def test_admin_account_login(self):
        self.test_all_windows_mini()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().login(self.app_phone, self.app_password, self.app_nation)

    #  [Done] 群組-訊息設為公告
    @DecorateClass('CHATAPP-T3242')
    def test_group_message_pin(self):
        self.test_admin_account_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_text_message()
        self.function_dict['wap'].wap_message_page().pin_full_messages()
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 群組-回覆訊息設為公告
    @DecorateClass('CHATAPP-T3243')
    def test_group_message_pin_reply(self):
        self.test_wap_login()
        reply_original_message = 'mWeb測試原訊息_群組_回覆後設為公告'
        reply_message = 'mWeb測試:回覆訊息(群組_回覆後設為公告)'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_message(reply_original_message)
        self.function_dict['wap'].wap_message_page().message_reply(reply_original_message, reply_message)
        self.function_dict['wap'].wap_message_page().message_pin(reply_message)
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 測試-群組訊息設置公告後撤回
    @DecorateClass('CHATAPP-T3245')
    def test_group_message_pin_revoke(self):
        self.test_wap_login()
        original_message = 'mWeb測試原訊息_群聊_設為公告後撤回'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().delete_all_pin()
        self.function_dict['wap'].wap_message_page().send_message(original_message)
        self.function_dict['wap'].wap_message_page().message_pin(original_message)
        self.function_dict['wap'].wap_message_page().message_revoke(original_message, pin_revoke=True)
        self.function_dict['wap'].wap_message_page().delete_all_pin()

    # 測試-群組發送語音訊息
    @DecorateClass('CHATAPP-T3248')
    def test_group_send_voice_message(self):
        self.test_wap_login()
        voice_length = random.randint(10, 15)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length)
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message('语音讯息')

    # 測試-群組回覆語音訊息
    @DecorateClass('CHATAPP-T3246')
    def test_group_voice_message_reply(self):
        self.test_wap_login()
        voice_length = random.randint(10, 15)
        reply_text = 'mWeb_群組_回覆語音訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length)
        room_voice_message = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='voice')
        self.function_dict['wap'].wap_message_page().message_reply(room_voice_message, reply_text, message_type='voice')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(reply_text)

    # 測試-群組撤回語音訊息
    @DecorateClass('CHATAPP-T3247')
    def test_group_voice_message_revoke(self):
        self.test_wap_login()
        voice_length_1 = random.randint(10, 15)
        voice_length_2 = random.randint(1, 10)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length_1)
        room_voice_message_1 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')
        self.function_dict['wap'].wap_message_page().send_voice_message(voice_length_2)
        room_voice_message_2 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')
        self.function_dict['wap'].wap_message_page().message_revoke(room_voice_message_2, message_type='voice')
        assert room_voice_message_1 == self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='voice')

    @DecorateClass('CHATAPP-T3268')
    # 群組-發送檔案訊息
    def test_group_send_file_message(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_file_message()
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message('档案讯息')

    # 群組-回覆檔案訊息
    @DecorateClass('CHATAPP-T3269')
    def test_group_file_message_reply(self):
        self.test_wap_login()
        reply_text = 'mWeb_私聊_回覆檔案訊息Test'
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().message_reply(room_file_message, reply_text, message_type='file')
        self.function_dict['wap'].wap_message_page().check_chatroom_list_last_message(reply_text)

    # 群組-撤回檔案訊息
    @DecorateClass('CHATAPP-T3270')
    def test_group_file_message_revoke(self):
        self.test_wap_login()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message_1 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().send_file_message()
        room_file_message_2 = self.function_dict['wap'].wap_message_page().get_chatroom_last_message(message_type='file')
        self.function_dict['wap'].wap_message_page().message_revoke(room_file_message_2, message_type='file')
        assert room_file_message_1 == self.function_dict['wap'].wap_message_page().get_chatroom_last_message(
            message_type='file')

    @DecorateClass('CHATAPP-T3286')
    def test_social_post_photo(self):
        self.test_wap_login()
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'mWeb自動化{self.brand}Test_發布photo_{current_time}'

        self.function_dict['wap'].wap_main_page().select_media(media_type='photo')
        self.function_dict['wap'].wap_main_page().into_post_settings(description)
        self.function_dict['wap'].wap_main_page().check_post(account, description)

    @DecorateClass('CHATAPP-T3287')
    def test_social_post_video(self):
        self.test_wap_login()
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.wap_account

        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'mWeb自動化{self.brand}Test_發布video_{current_time}'

        self.function_dict['wap'].wap_main_page().select_media(media_type='video')
        self.function_dict['wap'].wap_main_page().into_post_settings(description)
        self.function_dict['wap'].wap_main_page().check_post(account, description)

    # 搜索視頻 & 用戶
    @DecorateClass('CHATAPP-T3285')
    def test_social_search(self):
        self.test_wap_logout()

        if self.env == 'uat':
            poster_phone_list = ['13542600001', '13542600002']
            poster_nickname_list = ['gubot01', 'gubot02']
        else:
            poster_phone_list = ['9016000202', '9016000203']
            poster_nickname_list = ['gutest002', 'gutest03']

        description_list = []

        for poster_phone, poster_nickname in zip(poster_phone_list, poster_nickname_list):
            self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
            self.function_dict['wap'].wap_login_page().login(poster_phone, self.wap_password, self.web_nation)
            # ========================== gubot01 & gubot02 依序發布貼文 ==================================================
            current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            description = f'mWeb_{self.brand}_SearchTest_{current_time}'
            description_list.append(description)

            self.function_dict['wap'].wap_main_page().select_media(media_type='video')
            self.function_dict['wap'].wap_main_page().into_post_settings(description)
            self.function_dict['wap'].wap_main_page().check_post(poster_nickname, description)
            self.test_wap_logout()
        # ========================== gubot04 or gubotmail01 登入 ========================================================
        if 'mail' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['wap'].wap_login_page().login(self.wap_phone, self.wap_password, self.wap_nation)
        # ========================== 1. 搜索頁: 輸入01貼文說明01 > 點搜索鍵 >>> 搜索結果-視頻頁 ===============================
        self.function_dict['wap'].search_page().search_from_search_page(description_list[0])
        self.function_dict['wap'].search_page().check_search_post_result(poster_nickname_list[0], description_list[0])
        # ========================== 2. 搜索視頻結果頁: 輸入02貼文說明02 > 點搜索鍵 >>> 搜索結果-視頻頁 =========================
        self.function_dict['wap'].search_page().search_post(description_list[1], search_by_switch_tab=False)
        self.function_dict['wap'].search_page().check_search_post_result(poster_nickname_list[1], description_list[1])
        # ========================== 4. 搜索視頻結果頁: 輸入01 > 點"用戶"頁籤 >>> 切換到用戶頁並立即搜索 ========================
        self.function_dict['wap'].search_page().search_poster(poster_nickname_list[0], search_by_switch_tab=True)
        self.function_dict['wap'].search_page().check_search_poster_result(poster_nickname_list[0])
        # ========================== 5. 搜索用戶結果頁: 輸入02 > 點搜索鍵 >>> 搜索結果-用戶頁 =================================
        self.function_dict['wap'].search_page().search_poster(poster_nickname_list[1], search_by_switch_tab=False)
        self.function_dict['wap'].search_page().check_search_poster_result(poster_nickname_list[1])
        # ========================== 7. 搜索用戶結果頁: 輸入02貼文說明02 > 點"視頻"頁籤 >>> 立即搜索 ===========================
        self.function_dict['wap'].search_page().search_post(description_list[1], search_by_switch_tab=True)
        self.function_dict['wap'].search_page().check_search_post_result(poster_nickname_list[1], description_list[1])
        # ========================== 確認搜索紀錄頁 =======================================================================
        self.function_dict['wap'].search_page().check_recent_search_record(
            [description_list[1], poster_nickname_list[1],
             poster_nickname_list[0], description_list[0]])

    # 關注 & 取消關注
    @DecorateClass('CHATAPP-T3288')
    def test_social_follow_unfollow(self):
        self.test_wap_login()
        origin_follows, origin_fans, origin_thumb_up = self.function_dict['wap'].wap_main_page().get_self_social_data()  # 取得自己主頁關注數

        self.add_friend_first()  # 新增operator_account (test1234) 為好友
        # ============================ 關注對方 ====================================
        self.function_dict['wap'].wap_friends_page().into_personal_profile()
        fans_counts_after_followed = self.function_dict['wap'].wap_main_page().follow_user()  # 關注對方 >>> 確認對方粉絲數+1,"已關注"鍵, 回傳對方目前粉絲數
        self.function_dict['wap'].wap_friends_page().back_to_message_page()
        after_follows, after_fans, after_thumb_up = self.function_dict['wap'].wap_main_page().get_self_social_data()  # 取得自己主頁關注數
        assert int(after_follows) == int(origin_follows) + 1  # 確認自己主頁關注數+1

        self.function_dict['wap'].wap_main_page().into_followed_list()  # 進入自己主頁關注列表
        self.function_dict['wap'].wap_main_page().check_followed_list(self.operate_account,
                                                                    after_follows)  # 確認關注列表: 關注數+1, 對方出現在列表上
        self.function_dict['wap'].wap_main_page().back_to_previous_page()
        # ============================ 取消關注對方 ==================================
        self.function_dict['wap'].wap_main_page().into_followed_list()
        self.function_dict['wap'].wap_main_page().unfollow_member(self.operate_account,
                                                                after_follows)  # 取消關注對方 >>> 確認自己關注頁籤數-1, "關注"鍵
        self.function_dict['wap'].wap_main_page().back_to_previous_page()
        after_unfollows, after_fans, after_thumb_up = self.function_dict['wap'].wap_main_page().get_self_social_data()  # 取得自己主頁關注數
        assert int(after_unfollows) == int(after_follows) - 1  # 確認自己主頁關注數-1

        self.function_dict['wap'].wap_main_page().into_followed_list()
        self.function_dict['wap'].wap_main_page().check_followed_list(self.operate_account, after_unfollows, add_follow=False)  # 確認關注列表: 自己關注數-1, 列表不出現對方
        # ============================ 確認對方粉絲列表 ===============================
        self.function_dict['wap'].wap_main_page().back_to_previous_page()
        self.function_dict['wap'].wap_message_page().into_chat_room(self.operate_account)
        self.function_dict['wap'].wap_friends_page().into_personal_profile()
        follows, fans_after_unfollowed, thumb_up_counts = self.function_dict['wap'].wap_main_page().get_others_social_data()  # 進入對方主頁, 回傳對方粉絲數
        assert int(fans_after_unfollowed) == int(fans_counts_after_followed) - 1  # 對方主頁粉絲數-1

        self.function_dict['wap'].wap_main_page().into_others_fans_list()  # 進入對方粉絲頁
        self.function_dict['wap'].wap_main_page().check_fans_list(self.operate_account, fans_after_unfollowed, add_fans=False)  # 確認對方粉絲列表: 對方粉絲數-1, 列表上不出現我
        self.function_dict['wap'].wap_friends_page().back_to_message_page()

        self.test_delete_friend()  # 刪除好友 operator_account (test1234)

    def add_friend_first(self):
        self.function_dict['wap'].wap_message_page().into_chat_page()
        self.function_dict['wap'].wap_message_page().into_add_friend_page(self.wap_account)
        new_friend = self.function_dict['wap'].wap_friends_page().is_new_friend(self.operate_account)
        if not new_friend:
            self.function_dict['wap'].wap_friends_page().into_chatroom_from_userDetail()
        else:
            self.function_dict['wap'].wap_friends_page().into_chatroom_from_addToAddressBook()

    # 分享自己主頁
    @DecorateClass('CHATAPP-T3295')
    def test_social_share_self_main_page(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        poster = ''
        if 'mail' in self.account_type.lower():
            poster = self.mail_account
        elif 'phone' in self.account_type.lower():
            poster = self.wap_account

        share_message = f'mWeb_{self.brand}_分享自己({poster})主頁_{current_time}'

        self.test_wap_login()
        self.function_dict['wap'].wap_main_page().into_main_page()
        self.function_dict['wap'].wap_main_page().into_share_to_window(0)
        self.function_dict['wap'].wap_main_page().share_to_group(self.test_group, share_message, share_main_page=True)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        # ============================= 自己端確認聊天室內分享文 ====================================
        self.function_dict['wap'].wap_message_page().check_chat_share_info(poster, share_message, share_main_page=True)
        # ============================= 他人端確認聊天室內分享文 ====================================
        self.function_dict['wap'].wap_friends_page().back_to_message_page()
        self.test_wap_logout()

        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().login(self.web_phone, self.web_password, self.web_nation)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().check_chat_share_info(poster, share_message, share_main_page=True)

    # 分享自己貼文
    @DecorateClass('CHATAPP-T3296')
    def test_social_share_self_post(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        poster = ''
        if 'mail' in self.account_type.lower():
            poster = self.mail_account
        elif 'phone' in self.account_type.lower():
            poster = self.wap_account

        share_message = f'mWeb_{self.brand}_分享自己({poster})貼文_{current_time}'
        self.test_wap_login()
        self.function_dict['wap'].wap_main_page().into_main_page()
        self.function_dict['wap'].wap_main_page().into_first_post()
        self.function_dict['wap'].wap_main_page().into_share_to_window(2)
        self.function_dict['wap'].wap_main_page().share_to_group(self.test_group, share_message, share_main_page=False)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        # ============================= 自己端確認聊天室內分享文 ====================================
        self.function_dict['wap'].wap_message_page().check_chat_share_info(poster, share_message, share_main_page=False)
        # ============================= 他人端確認聊天室內分享文 ====================================
        self.function_dict['wap'].wap_friends_page().back_to_message_page()
        self.test_wap_logout()

        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().login(self.web_phone, self.web_password, self.web_nation)
        self.function_dict['wap'].wap_message_page().into_chat_room(self.test_group)
        self.function_dict['wap'].wap_message_page().check_chat_share_info(poster, share_message, share_main_page=False)

    # email註冊帳號 > 登出 > 登入 > 登出
    @DecorateClass('CHATAPP-T3317')
    def test_mWeb_email_registration(self):
        email = 'qa5@tengyuntech.com'
        pw = "000111abc"
        # ============== 後台"關閉"極驗 =======================================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(False)
        # ============== email註冊帳號 =======================================================
        self.test_wap_logout()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().register_by_email(self.mail_account_id, email, pw)
        # =============== 登出後再登入 ================
        self.test_wap_logout()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().login(email, pw, login_method='mail')
        # ============== 後台"開啟"極驗 =======================================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(True)
        # ============== 後台刪除該帳號 ========================================================
        self.function_dict['ad'].main_page().into_member_list()
        self.function_dict['ad'].member_page().delete_member(self.mail_account_id)

    # email欄位檢核確認
    @DecorateClass('CHATAPP-T')
    def test_mWeb_email_field_check(self):
        self.test_all_windows_mini()
        self.function_dict['wap'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['wap'].base_page().open_base_url()  # 開啟wap網頁
        self.function_dict['wap'].wap_login_page().email_field_check_in_login()  # 註冊頁
        self.function_dict['wap'].wap_login_page().email_field_check_in_registration()  # 登入頁
        self.function_dict['wap'].wap_login_page().email_field_check_in_forget_pw()  # 忘記密碼頁

    # ======================================================== not yet =================================================
    # 登入ADMIN
    def test_admin_login(self):
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password)  # 登入admin

    # 登入ADMIN並進入會員列表頁
    def test_admin_login_to_memberlist(self):
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password)  # 登入admin
        self.function_dict['ad'].main_page().into_member_list()

    # 測試-進入帳號與安全頁面
    @DecorateClass('CHATAPP-T1793')
    def test_into_security(self):
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_security_page()
        self.function_dict['wp'].main_page().close_modal(1)

    # 測試-進入分享頁面
    @DecorateClass('CHATAPP-T1797')
    def test_into_share(self):
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_share_page()
        self.function_dict['wp'].main_page().close_modal(1)

    # 測試-分享網址功能
    @DecorateClass('CHATAPP-T1798')
    def test_share_url(self):
        self.test_web_login()

        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_share_page()
        share_url = self.function_dict['wp'].share_page().get_share_link()
        self.function_dict['wp'].main_page().close_modal(2)

        self.function_dict['wp'].chatlist_page().into_chat_room(self.operate_account)
        self.function_dict['wp'].chatroom_page().send_message(share_url)
        self.function_dict['wp'].chatroom_page().check_url_message(share_url)

    # 測試-A在與B的聊天室內發送圖片/影片 > B端確認該圖片影片與A端相同
    @DecorateClass('CHATAPP-T2543')
    def test_send_media(self):
        # -----------A端: 帳號A登入 > 與B的1v1聊天室內傳送圖片 > 獲取聊天室內該圖片src link > 帳號A登出
        self.test_web_login()  # login web_id
        self.function_dict['wp'].chatlist_page().into_chat_room(self.app_account)  # into to app_id chatroom
        self.function_dict['wp'].chatlist_page().delete_chatroom_record()
        self.function_dict['wp'].chatlist_page().into_chat_room(self.app_account)
        self.function_dict['wp'].chatroom_page().send_image()  # send picture to chatroom
        a_side_image_src_link = self.function_dict[
            'wp'].chatroom_page().get_last_media_src_link()  # 取得聊天室該image的src link
        self.test_web_logout()

        # -----------B端: 帳號B登入 > 進入與A的1v1聊天室 > 獲取聊天室內A傳送的圖片src link > 與A端獲取的src_link做比對
        self.function_dict['wp'].login_page().login(self.app_phone, self.app_password,
                                                   self.app_nation)  # login app_id
        self.function_dict['wp'].chatlist_page().into_chat_room(self.web_account)  # into to web_id chatroom
        assert self.function_dict[
                   'wp'].chatroom_page().get_last_media_src_link() == a_side_image_src_link, '發送與接收端圖片不同'
        assert self.function_dict[
                   'wp'].chatlist_page().get_chat_list_msg_text() == f'{self.web_account}：[图片]', '聊天列表該聊天室最後一筆訊息顯示錯誤'
        self.function_dict['wp'].chatlist_page().delete_chatroom_record()
        self.function_dict['wp'].chatlist_page().into_chat_room(self.web_account)
        # -----------B端: 與A的1v1聊天室內傳送影片 > 獲取聊天室內該影片src link > 帳號B登出
        self.function_dict['wp'].chatroom_page().send_video()  # send video to chatroom
        b_side_video_src_link = self.function_dict['wp'].chatroom_page().get_last_media_src_link(
            'video')  # 獲取聊天室該video的src link
        self.test_web_logout()

        # -----------A端: 帳號A登入 > 進入與B的1v1聊天室 > 獲取聊天室內B傳送的影片src link > 與B端獲取的src_link做比對
        self.function_dict['wp'].login_page().login(self.web_phone, self.web_password,
                                                   self.web_nation)  # login web_id
        self.function_dict['wp'].chatlist_page().into_chat_room(self.app_account)  # into to app_id chatroom
        assert self.function_dict['wp'].chatroom_page().get_last_media_src_link(
            'video') == b_side_video_src_link, '發送與接收端影片不同'
        assert self.function_dict[
                   'wp'].chatlist_page().get_chat_list_msg_text() == f'{self.app_account}：[视频]', '聊天列表該聊天室最後一筆訊息顯示錯誤'

    # 測試-建立群組
    @DecorateClass('CHATAPP-T1938')
    def test_groups_build(self):
        self.test_web_login()

        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().check_groups_build()
        self.function_dict['wp'].main_page().groups_build(self.web_account, self.get_group_name())
        self.function_dict['wp'].chatlist_page().into_chat_room(self.get_group_name())
        self.function_dict['wp'].chatlist_page().check_group_build(self.web_account, self.get_group_name())

    # 測試-變更群組名稱
    @DecorateClass('CHATAPP-T1939')
    def test_group_name_change(self):
        self.test_web_login()

        self.function_dict['wp'].chatlist_page().into_chat_room(self.get_group_name())
        self.function_dict['wp'].chatroom_page().into_setting()
        self.function_dict['wp'].chatroom_page().change_group_name(self.get_group_name(), 'name_test')
        self.function_dict['wp'].chatroom_page().into_setting()
        self.function_dict['wp'].chatroom_page().change_group_name('name_test', self.get_group_name())

    # 測試-變更群組權限設定
    @DecorateClass('CHATAPP-T1940')
    def test_group_rule_all(self):
        self.test_web_login()

        self.function_dict['wp'].chatlist_page().into_chat_room(self.get_group_name())
        self.function_dict['wp'].chatroom_page().into_setting()
        self.function_dict['wp'].chatroom_page().all_group_rule()

    # 測試-綁定正確的錢包並兌換積分 (順付)
    @DecorateClass('CHATAPP-T2524')
    def test_exchange_wellpay(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        wellpay_address = '0xe1d6cfe14f9f23d49c2637695a1570f3fa3049bb'  # original: 0x90ebd6ff86db243597294150e472a80a3fb84d40
        exchange_amount = 1

        self.test_admin_login_to_memberlist()
        self.function_dict['ad'].member_page().unbind_wellpay(member_ID)

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].login_page().login(web_phone, web_password, self.web_nation)

        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].integral_page().entry_exchange_page()
        self.function_dict['wp'].integral_page().bind_wellpay(wellpay_address, self.security_code)
        bind_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        self.test_admin_login_to_memberlist()
        self.function_dict['ad'].member_page().check_wellpay_bind_data(member_ID, bind_time, wellpay_address)
        self.function_dict['ad'].member_page().refresh_browser()
        self.function_dict['wp'].integral_page().wellpay_exchange(self.security_code, exchange_amount)
        self.function_dict['ad'].member_page().unbind_wellpay(member_ID)

    # 測試-綁定錯誤的錢包並兌換積分 (順付)
    @DecorateClass('CHATAPP-T2525')
    def test_exchange_wellpay_incorrect(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        wellpay_address_incorrect = '123'
        exchange_amount = 1

        self.test_admin_login_to_memberlist()
        self.function_dict['ad'].member_page().unbind_wellpay(member_ID)

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()
        self.function_dict['wp'].base_page().open_base_url()
        self.function_dict['wp'].login_page().login(web_phone, web_password, self.web_nation)

        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()

        self.function_dict['wp'].integral_page().entry_exchange_page()
        self.function_dict['wp'].integral_page().bind_wellpay(wellpay_address_incorrect, self.security_code)
        self.function_dict['wp'].integral_page().wellpay_exchange_incorrect(self.security_code, exchange_amount)

        self.test_admin_login_to_memberlist()
        self.function_dict['ad'].member_page().unbind_wellpay(member_ID)

    # 測試-兌換平臺積分 (sc)
    @DecorateClass('CHATAPP-T2753')
    def test_exchange_brand(self):

        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_ID = 'exchange0'
        operate_type = '平台'
        brand = 'SC'
        env = 'uat'

        # =========================== 登入SC平臺, 設定股聊積分兌換數值 =====================
        self.function_dict['wp'].brand_page().into_brand_page(brand, env)
        before_main_wallet_money = self.function_dict['wp'].brand_page().get_main_wallet_money()
        exchange_address, exchange_amount = self.function_dict['wp'].brand_page().online_deposit()
        # =========================== 登入前臺, 獲取原股聊積分 =============================
        self.function_dict['wp'].base_page().open_base_url()
        self.function_dict['wp'].login_page().login(web_phone, web_password, self.web_nation)
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_before = self.function_dict['wp'].main_page().into_integral_page()  # 獲取原積分

        # =========================== 前台綁定平臺SC, 並兌換積分 ==========================
        self.function_dict['wp'].integral_page().entry_exchange_page()
        self.function_dict['wp'].integral_page().bind_brand_and_exchange(exchange_address, self.security_code)
        self.function_dict['wp'].main_page().into_integral_page()
        remain_integral_amount_after = self.function_dict['wp'].integral_page().exchange_record_check(exchange_amount,
                                                                                                     operate_type, None,
                                                                                                     remain_integral_amount_before)

        # =========================== 後台確認積分使用紀錄 ================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(member_ID, None,
                                                                                 f'-{str(exchange_amount)}',
                                                                                 f'{operate_type}-{brand}', None,
                                                                                 remain_integral_amount_after)  # [後台]積分使用紀錄頁確認積分訊息

        # =========================== 解綁平臺 ===========================================
        self.test_admin_login_to_memberlist()
        self.function_dict['ad'].member_page().unbind_brand(member_ID)

        # =========================== SC平臺端確認積分紀錄 =================================
        self.function_dict['wp'].base_page().switch_home_page()
        after_main_wallet_money = self.function_dict['wp'].brand_page().get_main_wallet_money()
        self.function_dict['wp'].brand_page().check_deposit_record(before_main_wallet_money, exchange_amount,
                                                                  after_main_wallet_money)

    # 測試-人工存入積分 & 人工提出積分
    @DecorateClass('CHATAPP-T2547')
    def test_manual_deposit_and_withdraw(self):
        web_phone = '5568899999'
        web_password = 'ps43941122'
        member_id = 'exchange0'
        integral_amount = '12.34'

        self.function_dict['wp'].login_page().login(web_phone, web_password, self.web_nation)
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_deposit_before = self.function_dict['wp'].main_page().into_integral_page()  # 獲得原積分

        # =========================== 後台人工存入積分 ======================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_manual_deposit()
        self.function_dict['ad'].main_page().manual_add_deposit(member_id, integral_amount)  # 後台人工存入積分
        add_deposit_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # =========================== 前台確認存入積分紀錄 ======================================
        self.function_dict['wp'].base_page().refresh_browser()
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        current_total_integral_amount = self.function_dict['wp'].integral_page().exchange_record_check(integral_amount,
                                                                                                      '人工存入_红包奖励积分',
                                                                                                      add_deposit_time,
                                                                                                      remain_integral_amount_deposit_before)  # 前台積分詳情頁確認積分變動紀錄

        # =========================== 後台人工提出積分 ======================================
        self.function_dict['ad'].main_page().into_manual_withdraw()
        self.function_dict['ad'].main_page().manual_add_withdraw(member_id, integral_amount)  # 後台人工提出積分
        add_withdraw_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        # =========================== 前台確認提出積分紀錄 ======================================
        self.function_dict['wp'].base_page().refresh_browser()
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].integral_page().exchange_record_check(integral_amount, '人工提出_红包误存',
                                                                      add_withdraw_time,
                                                                      current_total_integral_amount)  # 前台積分詳情頁確認積分變動兌換紀錄

    # 測試-搶一般紅包
    @DecorateClass('CHATAPP-T2548')
    def test_grab_red_envelope(self):
        red_envelope_type = '发红包'
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_before = self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')
        grab_time, grab_amount = self.function_dict['wp'].chatroom_page().grab_red_envelope(
            red_envelope_type)  # [前台]搶紅包, 回傳紅包時間+金額
        self.function_dict['wp'].chatroom_page().check_chatroom_system_message(self.web_account,
                                                                              grab_amount)  # 確認聊天室內搶紅包系統訊息
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        remain_integral_amount = self.function_dict['wp'].integral_page().exchange_record_check(grab_amount,
                                                                                               red_envelope_type,
                                                                                               grab_time,
                                                                                               remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.web_account, grab_amount,
                                                                             red_envelope_type,
                                                                             grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.web_account, grab_time,
                                                                                 grab_amount, red_envelope_type,
                                                                                 'QA_bot_only',
                                                                                 remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-搶拚手氣紅包
    @DecorateClass('CHATAPP-T2549')
    def test_grab_luck_red_envelope(self):
        red_envelope_type = '拼手气红包'
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_before = self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')
        grab_time, grab_amount = self.function_dict['wp'].chatroom_page().grab_red_envelope(
            red_envelope_type)  # [前台]搶紅包, 回傳紅包時間+金額
        self.function_dict['wp'].chatroom_page().check_chatroom_system_message(self.web_account,
                                                                              grab_amount)  # 確認聊天室內搶紅包系統訊息
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        remain_integral_amount = self.function_dict['wp'].integral_page().exchange_record_check(grab_amount,
                                                                                               red_envelope_type,
                                                                                               grab_time,
                                                                                               remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.web_account, grab_amount,
                                                                             red_envelope_type,
                                                                             grab_time)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.web_account, grab_time,
                                                                                 grab_amount, red_envelope_type,
                                                                                 'QA_bot_only',
                                                                                 remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-自動領取一般紅包
    @DecorateClass('CHATAPP-T2570')
    def test_auto_grab_red_envelope(self):
        red_envelope_type = '发红包'
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_before = self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')

        sleep(180)  # 等待系統trigger發送紅包 & 搶紅包機器人執行搶紅包

        name, amount = self.function_dict['wp'].chatroom_page().check_chatroom_system_message(None, None)  # 確認聊天室內紅包系統訊息
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        remain_integral_amount = self.function_dict['wp'].integral_page().exchange_record_check(amount,
                                                                                               red_envelope_type, None,
                                                                                               remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.web_account, amount,
                                                                             red_envelope_type, None)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.web_account, None, amount,
                                                                                 red_envelope_type, 'QA_bot_only',
                                                                                 remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試-搶拚手氣紅包
    @DecorateClass('CHATAPP-T2571')
    def test_auto_grab_luck_red_envelope(self):
        red_envelope_type = '拼手气红包'
        self.test_web_login()
        self.function_dict['wp'].main_page().open_user_info()
        remain_integral_amount_before = self.function_dict['wp'].main_page().into_integral_page()
        self.function_dict['wp'].chatlist_page().into_chat_room('QA_bot_only')

        sleep(180)  # 等待系統trigger發送紅包 & 搶紅包機器人執行搶紅包

        name, amount = self.function_dict['wp'].chatroom_page().check_chatroom_system_message(None, None)  # 確認聊天室內紅包系統訊息
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_integral_page()
        remain_integral_amount = self.function_dict['wp'].integral_page().exchange_record_check(amount,
                                                                                               red_envelope_type, None,
                                                                                               remain_integral_amount_before)  # [前台]積分詳情頁確認紅包明細, 並回傳目前帳號總積分

        self.test_admin_login()
        self.function_dict['ad'].main_page().into_red_list()
        self.function_dict['ad'].red_envelope_page().red_envelope_detail_check(self.web_account, amount,
                                                                             red_envelope_type, None)  # 後台紅包詳情頁確認明細
        self.function_dict['ad'].main_page().into_integral_record()
        self.function_dict['ad'].water_recode_page().check_current_exchange_record(self.web_account, None, amount,
                                                                                 red_envelope_type, 'QA_bot_only',
                                                                                 remain_integral_amount)  # [後台]積分使用紀錄頁確認積分訊息

    # 測試 - [後台]設定邀請碼權限 > [前台]登入一般成員 & 管理員帳號確認邀請碼分享欄位顯示與否
    @DecorateClass('CHATAPP-T2569')
    def test_share_code_visible_when_permission_change(self):
        share_code = "PERMISS"
        group_name = "ShareCodePermissTest"

        # ========================= 群組一般成員 =========================
        user = "gubot02"  # 一般成員
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_share_code()
        self.function_dict['ad'].main_page().modify_share_code(share_code, permission=1)  # 分享權限設為"所有成員"

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].login_page().login(self.web_phone, self.web_password, self.web_nation)  # 登入群組權限"一般成員"用戶
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=1)  # 確認前台可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].main_page().modify_share_code(share_code, permission=2)  # 分享權限設為"僅後台"

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=2)  # 確認前台不可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].main_page().modify_share_code(share_code, permission=3)  # 分享權限設為"僅管理員"

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=3)  # 確認前台不可見邀請碼分享欄位

        # ========================= 群組管理員 =========================
        user = "gubot03"  # 管理員
        self.function_dict['wp'].main_page().open_user_info()
        self.function_dict['wp'].main_page().into_security_page()
        self.function_dict['wp'].security_page().logout()
        self.function_dict['wp'].login_page().login(self.app_phone, self.app_password, self.web_nation)  # 登入群組權限"管理員"用戶
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=3)  # 確認前台可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_share_code()
        self.function_dict['ad'].main_page().modify_share_code(share_code, permission=2)  # 分享權限設為"僅後台"

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=2)  # 確認前台不可見邀請碼分享欄位

        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].main_page().modify_share_code(share_code, permission=1)  # 分享權限設為"所有成員"

        self.test_all_windows_mini()
        self.function_dict['wp'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['wp'].chatroom_page().check_share_code_visible_when_permission_changed(share_code, group_name,
                                                                                                 user,
                                                                                                 permission=1)  # 確認前台可見邀請碼分享欄位

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method
