import subprocess
import unittest, sys, os, datetime, random, re
import logging
from time import sleep

import time
from retrying import retry
from airtest.core.api import snapshot, stop_app, clear_app, connect_device

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

import common.utils.globalvar as gl
import stf_api.stf as stf
from driver.app_driver import AppDriver
from common.app.decorator import DecorateClass
from Project.chat.app.testcase.base_testcase import BaseTestCase
from Project.chat.app.pages.pages import AppPages
from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.apis.function_layer.functions import Functions
from Project.chat.apis.function_layer.base_functions import BaseFunction as BaseFunction_API


class AppTestCase(BaseTestCase, BaseFunction_API):
    brand = gl.get_value('BRAND')
    # ================================= TestSetting ===============================
    
    @classmethod
    def setUpClass(cls):
        cls.setting_test_data()  # 設定測試數據
        app_dr = AppDriver()
        poco, wda_service = app_dr.airtest_connect_phone()  # 連線測試手機
        # poco, wda_service = app_dr.AppDriver.airtest_connect_phone(cls)
        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))
        cls.folderpath = gl.get_value('FOLDER_PATH')

    def setUp(self):
        if gl.get_value('VERSION_MESSAGE') is not None:
            self.function_dict['ap'].commomPage().skip_test(gl.get_value('VERSION_MESSAGE'))

        self.functions = Functions()
        self.test_choose_app()

        self.start_time = time.time()

    def tearDown(self):
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

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

    @classmethod
    def tearDownClass(cls):
        if cls.phone_platform == 'Android':
            clear_app(cls.poco_package)
        else:
            stop_app(cls.poco_package)
        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))
        
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def test_choose_app(self):
        # 選APP
        try:
            self.function_dict['ap'].commomPage().find_app(self.package)

            login_status = self.function_dict['ap'].mainPage().into_home_check(self._login_status[0])
            if login_status is False:
                self._login_status[0] = False
        except Exception as e:
            if 'device offline' in str(e):
                self.device_reconnect()     # 手機斷線重連
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

# -------------------------------------------------------------------------------

    @DecorateClass('CHATAPP-T1679')
    # 登入
    def test_login(self):
        if self.unknown_env[0] is True:
            self.function_dict['ap'].commomPage().skip_test('測試環境不正確')
        if self._login_status[0] is False:
            self.function_dict['ap'].mainPage().login(self.app_phone, self.app_password, self.app_nation)
            self._login_status[0] = True

    @DecorateClass('CHATAPP-T1681')
    # 登出
    def test_logout(self):
        if self._login_status[0] is False:
            self.function_dict['ap'].commomPage().skip_test('帳號已經為登出狀態')
        else:
            self.function_dict['ap'].mainPage().into_main_page()
            self.function_dict['ap'].mainPage().into_main_setting_page()
            self.function_dict['ap'].memberPage().into_security()
            self.function_dict['ap'].mainPage().logout()

    @DecorateClass('CHATAPP-T1680')
    # 檢查版本
    def test_version_check(self):
        self.test_login()
        app_version = self.app_version
        self.function_dict['ap'].mainPage().into_main_page()
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_about()
        self.function_dict['ap'].aboutPage().check_version(app_version)

    @DecorateClass('CHATAPP-T2560')
    # 進入圖庫頁
    def test_into_gallery(self):
        self.test_login()
        self.function_dict['ap'].treadandgalleryPage().into_gallery_page()

    @DecorateClass('CHATAPP-T2561')
    # 進入走勢頁
    def test_into_tread(self):
        self.test_login()
        self.function_dict['ap'].treadandgalleryPage().into_tread_page()

    @DecorateClass('CHATAPP-T1752')
    # 進入主頁_我的設定頁面
    def test_into_member(self):
        self.test_login()
        self.function_dict['ap'].mainPage().into_main_page()
        self.function_dict['ap'].mainPage().into_main_setting_page()

    @DecorateClass('CHATAPP-T1753')
    # 進入好友頁面
    def test_into_friend(self):
        self.test_login()
        self.function_dict['ap'].mainPage().into_friend_page()
    
    @DecorateClass('CHATAPP-T1754')
    # 變更自己暱稱 & 個人簡介
    def test_change_nickname_and_instructions(self):
        self.test_login()
        self.function_dict['ap'].mainPage().into_main_page()
        old_nickname = self.function_dict['ap'].mainPage().get_nickname()
        old_description = self.function_dict['ap'].mainPage().get_self_introduction()
        self.function_dict['ap'].memberPage().into_edit()
        self.function_dict['ap'].memberPage().change_nickname('gutest1234')
        self.function_dict['ap'].memberPage().change_nickname(old_nickname)
        self.function_dict['ap'].memberPage().change_introduction('👿😡😍😖😍(*^ω^*)udhヾ(@^▽^@)ノ ❤💔🎃🎓🍻🍰🍱🎰🎧🎶🎱🎫😲😱😰😭🐷🐶🍀🐱🐔🐰🐮🍀🐑')
        self.function_dict['ap'].memberPage().change_introduction(old_description)


    @DecorateClass('CHATAPP-T1755')
    # 訊息通知設定
    def test_notify_switch(self):
        self.test_login()
        
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_notification()
        self.function_dict['ap'].notificationPage().turn_notify_switch()

    @DecorateClass('CHATAPP-T1756')
    # 通知詳情設定
    def test_detail_switch(self):
        self.test_login()
        
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_notification()
        self.function_dict['ap'].notificationPage().turn_detail_switch()

    @DecorateClass('CHATAPP-T1757')
    # 通知聲音設定
    def test_voice_switch(self):
        self.test_login()
        
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_notification()
        self.function_dict['ap'].notificationPage().turn_voice_switch()

    @DecorateClass('CHATAPP-T1758')
    # 通知震動設定
    def test_vibration_switch(self):
        self.test_login()
        
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_notification()
        self.function_dict['ap'].notificationPage().turn_vibration_switch()
    
    @DecorateClass('CHATAPP-T1759')
    # 關於聊天
    def test_about_terms(self):
        self.test_login()
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_about()
        self.function_dict['ap'].aboutPage().check_service()
        self.function_dict['ap'].aboutPage().check_privacy()

    @DecorateClass('CHATAPP-T1767')
    # 修改登入密碼
    def test_change_password(self):
        self.test_login()

        new_pwd = 'Ps43941122'
        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_security()

        self.function_dict['ap'].securityPage().change_password(self.app_password, new_pwd)
        self.function_dict['ap'].mainPage().logout()
        self.function_dict['ap'].mainPage().login(self.app_phone, new_pwd, self.app_nation)

        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_security()

        self.function_dict['ap'].securityPage().change_password(new_pwd, self.app_password)
        self.function_dict['ap'].mainPage().logout()
        self.function_dict['ap'].mainPage().login(self.app_phone, self.app_password, self.app_nation)

    @DecorateClass('CHATAPP-T1768')
    # 確認帳號與安全資料
    def test_account_info(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_security()
        self.function_dict['ap'].securityPage().check_value(self.app_phone, self.app_account, self.app_nation)

    @DecorateClass('CHATAPP-T1760')
    # 好友頁面新增好友
    def test_add_friend(self):
        self.test_login()
        self.function_dict['ap'].mainPage().into_friend_page()
        can_add_friend = self.function_dict['ap'].friendPage().search_new_friend(self.operate_account)

        if not can_add_friend:
            self.function_dict['ap'].friendPage().back_to_friends_page()
            self.function_dict['ap'].friendPage().delete_friend(self.operate_account)
            self.function_dict['ap'].friendPage().search_new_friend(self.operate_account)

        self.function_dict['ap'].friendPage().add_friend()

    @DecorateClass('CHATAPP-T1762')
    # 好友頁面新增自己
    def test_add_myself(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().search_clear(self.operate_phone)
        self.function_dict['ap'].friendPage().add_myself(self.app_phone, self.app_nation)

    @DecorateClass('CHATAPP-T1761')
    # 好友頁面備註暱稱
    def test_friend_remark(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().search_new_friend(self.operate_account)
        self.function_dict['ap'].friendPage().set_note('IM自動化測試')
        self.function_dict['ap'].friendPage().set_nickname()

    @DecorateClass('CHATAPP-T1764')
    # 好友頁面新增好友黑名單
    def test_block_friend(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().search_friend(self.operate_account)
        self.function_dict['ap'].friendPage().block_friend()
        self.function_dict['ap'].friendPage().impeach_friend()
    
    @DecorateClass('CHATAPP-T1763')
    # 好友頁面刪除好友
    def test_delete_friend(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_friend_page()
        self.function_dict['ap'].friendPage().delete_friend(self.operate_account)

    @DecorateClass('CHATAPP-T1766')
    # 黑名單頁面備註暱稱
    def test_block_setting(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_blacklist()
        self.function_dict['ap'].blacklistPage().search_friend(self.operate_account)
        self.function_dict['ap'].blacklistPage().into_block_setting()
        self.function_dict['ap'].blacklistPage().set_note('asdasdasdasda')
        self.function_dict['ap'].blacklistPage().set_nickname()
    
    @DecorateClass('CHATAPP-T1765')
    # 解除好友黑名單
    def test_unblock_friend(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_blacklist()
        self.function_dict['ap'].blacklistPage().search_friend(self.operate_account)
        self.function_dict['ap'].blacklistPage().into_block_setting()
        self.function_dict['ap'].blacklistPage().unblock_friend()

    @DecorateClass('CHATAPP-T1878')
    # 分享聊天至聊天室
    def test_share_message(self):
        self.test_login()

        self.function_dict['ap'].mainPage().into_main_setting_page()
        self.function_dict['ap'].memberPage().into_share()
        share_text, share_url = self.function_dict['ap'].sharePage().get_share_text()

        self.function_dict['ap'].mainPage().into_chat_page()
        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().share_message(share_text)
        if self.phone_platform.lower() == 'android':
            self.function_dict['ap'].chatroomPage().send_message(share_url)
            self.function_dict['ap'].chatroomPage().check_url_message(share_url)

    @DecorateClass('CHATAPP-T1769')
    # 個人發送文字超連結訊息
    def test_send_message(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().send_url_message()
        self.function_dict['ap'].chatlistPage().check_last_message(1)

    @DecorateClass('CHATAPP-T1770')
    # 個人訊息複製
    def test_message_copy(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().copy_message('測試TeSt12345!@#$%测试#0')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T1771')
    # 個人訊息回覆
    def test_message_reply(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().reply_message('測試TeSt12345!@#$%测试#5')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T1772')
    # 個人訊息刪除
    def test_message_delete(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_message('讯息删除测试case')
        room_message = self.function_dict['ap'].chatroomPage().get_last_message()
        self.function_dict['ap'].chatroomPage().send_message('刪除用测试訊息')
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().delete_message('刪除用测试訊息', room_message, -1)

    @DecorateClass('CHATAPP-T1773')
    # 個人訊息撤回
    def test_message_revoke(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#5')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T2526')
    # 一對一訊息表情符號
    def test_message_emoji(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_message('表情符號用测试訊息')
        self.function_dict['ap'].chatroomPage().add_emoji('表情符號用测试訊息')
        self.function_dict['ap'].chatroomPage().check_emoji('表情符號用测试訊息')

    @DecorateClass('CHATAPP-T1928')
    # 個人訊息回覆後刪除
    def test_message_reply_delete(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().send_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().reply_message('刪除用测试訊息')
        room_message = self.function_dict['ap'].chatroomPage().get_last_message()
        self.function_dict['ap'].chatroomPage().delete_message('刪除用测试訊息', room_message, -2)
        self.function_dict['ap'].chatroomPage().check_reply_title('此讯息已被删除')
        
    @DecorateClass('CHATAPP-T1927')
    # 個人訊息回覆後撤回
    def test_message_reply_revoke(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_message('撤回用测试訊息')
        self.function_dict['ap'].chatroomPage().reply_message('撤回用测试訊息')
        self.function_dict['ap'].chatroomPage().revoke_message('撤回用测试訊息', -2)
        self.function_dict['ap'].chatroomPage().check_reply_title('此讯息已被撤回')

    @DecorateClass('CHATAPP-T1774')
    # 個人訊息設置公告
    def test_message_pin(self):
        self.test_login()
        
        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().copy_message('測試TeSt12345!@#$%测试#5')
        self.function_dict['ap'].chatroomPage().pin_full_messages()
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1775')
    # 個人訊息設置公告後回覆
    def test_message_pin_reply(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().reply_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().pin_message('回覆訊息测试Test')
        self.function_dict['ap'].chatroomPage().check_pin_message('回覆訊息测试Test')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1776')
    # 個人訊息設置公告後刪除
    def test_message_pin_delete(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        room_message = self.function_dict['ap'].chatroomPage().get_last_message()
        self.function_dict['ap'].chatroomPage().send_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().pin_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().delete_message('刪除用测试訊息', room_message)
        self.function_dict['ap'].chatroomPage().check_pin_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1777')
    # 個人訊息設置公告後撤回
    def test_message_pin_revoke(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().pin_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().check_pin_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1778')
    # 群組發送文字超連結訊息
    def test_send_message_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().send_url_message()
        self.function_dict['ap'].chatlistPage().check_last_message(1)

    @DecorateClass('CHATAPP-T1779')
    # 群組訊息複製
    def test_message_copy_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().copy_message('測試TeSt12345!@#$%测试#0')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T1780')
    # 群組訊息回覆
    def test_message_reply_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().reply_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T1781')
    # 群組訊息刪除
    def test_message_delete_group(self):
        # self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        room_message = self.function_dict['ap'].chatroomPage().get_last_message()
        self.function_dict['ap'].chatroomPage().send_message('刪除用测试訊息')
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().delete_message('刪除用测试訊息', room_message)

    @DecorateClass('CHATAPP-T1782')
    # 群組訊息撤回
    def test_message_revoke_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        # self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatlistPage().check_last_message()
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#5')
        self.function_dict['ap'].chatlistPage().check_last_message()

    @DecorateClass('CHATAPP-T1783')
    # 群組訊息設置公告
    def test_message_pin_group(self):
        self.test_login()
        
        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        # self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().copy_message('測試TeSt12345!@#$%测试#5')
        self.function_dict['ap'].chatroomPage().pin_full_messages()
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1784')
    # 群組訊息設置公告後回覆
    def test_message_pin_reply_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        # self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().reply_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().pin_message('回覆訊息测试Test')
        self.function_dict['ap'].chatroomPage().check_pin_message('回覆訊息测试Test')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1785')
    # 群組訊息設置公告後刪除
    def test_message_pin_delete_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        # self.function_dict['ap'].chatroomPage().delete_all_pin()
        room_message = self.function_dict['ap'].chatroomPage().get_last_message()
        self.function_dict['ap'].chatroomPage().send_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().pin_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().delete_message('刪除用测试訊息', room_message)
        self.function_dict['ap'].chatroomPage().check_pin_message('刪除用测试訊息')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T1786')
    # 群組訊息設置公告後撤回
    def test_message_pin_revoke_group(self):
        self.test_login()

        self.function_dict['ap'].chatlistPage().into_chat_room('QA_bot_only')
        # self.function_dict['ap'].chatroomPage().delete_all_pin()
        self.function_dict['ap'].chatroomPage().send_text_message()
        self.function_dict['ap'].chatroomPage().pin_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().check_pin_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().revoke_message('測試TeSt12345!@#$%测试#3')
        self.function_dict['ap'].chatroomPage().delete_all_pin()

    @DecorateClass('CHATAPP-T2568')
    # 透過邀請碼加入群組 > 退出群組
    def test_join_group_by_share_code(self):
        share_code = 'AUTOTEST'
        group_name = 'AuToTeSt'
        self.test_login()
        self.function_dict['ap'].chatlistPage().join_group_by_input_share_code(share_code, group_name)
        self.function_dict['ap'].chatlistPage().leave_group(group_name)

    @DecorateClass('CHATAPP-T2717')
    # 媒體發布_圖片
    def test_media_photo_post(self):
        self.test_login()

        media_index = random.randint(-21, -1)
        media_type = 'photo'
        description = f'👿😡😍自動化Test_그림👿😡😍{media_index}'

        self.function_dict['ap'].mediareleasePage().select_media(media_index, media_type)
        self.function_dict['ap'].mediareleasePage().into_post_page(description, privacy_index=0, media_type=media_type,
                                                                   post=True)
        self.function_dict['ap'].mediareleasePage().check_media_post(self.app_account, description, post=True)
        self.function_dict['ap'].mediareleasePage().check_recent_post_media(self.app_account, description)

    # 媒體發布_圖片
    @DecorateClass('CHATAPP-T2718')
    def test_media_video_post(self):
        self.test_login()

        media_index = random.randint(-11, -1)
        media_type = 'video'
        description = f'👿😡😍自動化Test_βίντεο👿😡😍{media_index}'

        self.function_dict['ap'].mediareleasePage().select_media(media_index, media_type)
        self.function_dict['ap'].mediareleasePage().into_post_page(description, privacy_index=0, media_type=media_type,
                                                                   post=True)
        self.function_dict['ap'].mediareleasePage().check_media_post(self.app_account, description, post=True)
        self.function_dict['ap'].mediareleasePage().check_recent_post_media(self.app_account, description)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
