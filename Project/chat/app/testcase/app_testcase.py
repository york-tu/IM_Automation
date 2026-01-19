import subprocess
import unittest, sys, os, datetime, random, re
import logging
import signal
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


class AppTestCase(BaseTestCase):
    # ================================= TestSetting ===============================
    
    @classmethod
    def setUpClass(cls):
        cls.setting_test_data()  # 設定測試數據
        app_dr = AppDriver()
        # if cls.phone_platform == 'Android':
        #     phone_name = 'HUAWEI_MATE_30_PRO_5G'
        cls.phone_name = gl.get_value('PHONE_NAME')

        poco, wda_service = app_dr.airtest_connect_phone()  # 連線測試手機

        # 儲存 WDA service，讓 tearDownClass 可存取
        cls.wda_service = wda_service

        # poco, wda_service = app_dr.AppDriver.airtest_connect_phone(cls)
        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))

        # 獲取設定資訊
        cls.folderpath = gl.get_value('FOLDER_PATH')

        env = gl.get_value('ENV')
        account_type = gl.get_value('ACCOUNT_TYPE')
        phone_platform = gl.get_value('PHONE_PLATFORM')

        brand = gl.get_value('BRAND') or ''
        cls.brand = brand.strip().lower()
        if cls.brand == 'mingpin':
            cls.test_group = 'QA bot only'
        else:
            cls.test_group = 'QA_bot_only'

    def setUp(self):
        # 在 setUp 最開始記錄開始時間，與 unittest 框架的時間計算一致
        # unittest 框架的時間包括：setUp + 測試方法 + tearDown
        self.start_time = time.time()
        
        if gl.get_value('VERSION_MESSAGE') is not None:
            self.ap.common_page().skip_test(gl.get_value('VERSION_MESSAGE'))

        self.test_choose_app()

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
        
        # 在 tearDown 最後記錄結束時間，與 unittest 框架的時間計算一致
        # unittest 框架的時間包括：setUp + 測試方法 + tearDown
        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

    @classmethod
    def tearDownClass(cls):
        if cls.phone_platform == 'Android':
            clear_app(cls.poco_package)
        else:
            stop_app(cls.poco_package)
            # 關閉 WDA
            if hasattr(cls, 'wda_service') and cls.wda_service:
                try:
                    cls.wda_service.send_signal(signal.CTRL_C_EVENT)
                    cls.wda_service.terminate()  # 嘗試正常結束
                    # 或強制結束
                    cls.wda_service.kill()
                    cls.wda_service.wait(timeout=5)
                    print(f"[INFO] WDA stopped for {cls.phone_name}")
                except Exception as e:
                    print(f"[WARN] Failed to stop WDA: {e}")

        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))
        
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
    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def test_login(self):
        if self._login_status[0] is False:
            try:
                self.login_app()
                self._login_status[0] = True

            except Exception as e:
                # iOS 特定錯誤處理
                if self.phone_platform.lower() == 'ios':
                    error_msg = str(e).lower()
                    if 'device offline' in error_msg or 'wda' in error_msg:
                        # WDA 連接問題，嘗試重新連接
                        print(f"⚠️  iOS WDA 連接問題，嘗試重新連接: {e}")
                        self.device_reconnect()
                        # 重新嘗試登入
                        self.login_app()
                        self._login_status[0] = True
                    else:
                        raise e
                else:
                    raise e

    @DecorateClass('CHATAPP-T1681')
    # 登出
    def test_logout(self):
        if self.ap.main_page().welcome_page_show():
            self.login_app()
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_security()
        self.ap.main_page().logout()

    @DecorateClass('CHATAPP-T1680')
    # 檢查版本
    def test_version_check(self):
        self.test_login()

        app_version = self.app_version
        self.ap.main_page().into_main_page()
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_about()
        self.ap.about_page().check_version(app_version)


    @DecorateClass('CHATAPP-T1752')
    # 進入主頁_我的設定頁面
    def test_into_member(self):
        self.test_login()

        self.ap.main_page().into_main_page()
        self.ap.main_page().into_main_setting_page()

    @DecorateClass('CHATAPP-T1753')
    # 進入好友頁面
    def test_into_friend(self):
        self.test_login()

        self.ap.main_page().into_friend_page()
    
    @DecorateClass('CHATAPP-T1754')
    # 變更自己暱稱 & 個人簡介
    def test_change_nickname_and_instructions(self):
        self.test_login()

        change_nickname = 'gutest1234'
        change_instruction = '👿🍀(*^ω^*)autoEDIT簡介Test(*^ω^*)🍀👿'

        self.ap.main_page().into_main_page()

        old_nickname = self.ap.main_page().get_nickname()
        old_description = self.ap.main_page().get_self_introduction()
        
        # 第一次進入編輯頁面，修改暱稱+簡介，保存後回到主頁檢查
        self.ap.member_page().into_edit()
        # 修改暱稱（保持在編輯頁面）
        self.ap.member_page().change_nickname(change_nickname)
        # 修改簡介（保存後返回主頁）
        self.ap.member_page().change_introduction(change_instruction)
        # 檢查主頁顯示的暱稱和簡介
        assert self.ap.main_page().get_nickname() == change_nickname, '第一次修改暱稱後，主頁顯示錯誤'
        assert self.ap.main_page().get_self_introduction() == change_instruction, '第一次修改簡介後，主頁顯示錯誤'
        
        # 再次進入編輯頁面，恢復原暱稱+簡介，保存後回到主頁檢查
        self.ap.member_page().into_edit()
        # 恢復原暱稱（保持在編輯頁面）
        self.ap.member_page().change_nickname(old_nickname)
        # 恢復原簡介（保存後返回主頁）
        self.ap.member_page().change_introduction(old_description)
        # 檢查主頁顯示的暱稱和簡介
        assert self.ap.main_page().get_nickname() == old_nickname, '恢復原暱稱後，主頁顯示錯誤'
        assert self.ap.main_page().get_self_introduction() == old_description, '恢復原簡介後，主頁顯示錯誤'

    @DecorateClass('CHATAPP-T1755')
    # 訊息通知設定
    def test_notify_switch(self):
        self.test_login()
        
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_notification()
        self.ap.notification_page().turn_notify_switch()

    @DecorateClass('CHATAPP-T1756')
    # 通知詳情設定
    def test_detail_switch(self):
        self.test_login()
        
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_notification()
        self.ap.notification_page().turn_detail_switch()

    @DecorateClass('CHATAPP-T1757')
    # 通知聲音設定
    def test_voice_switch(self):
        self.test_login()
        
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_notification()
        self.ap.notification_page().turn_voice_switch()

    @DecorateClass('CHATAPP-T1758')
    # 通知震動設定
    def test_vibration_switch(self):
        self.test_login()
        
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_notification()
        self.ap.notification_page().turn_vibration_switch()
    
    @DecorateClass('CHATAPP-T1759')
    # 關於聊天
    def test_about_terms(self):
        self.test_login()

        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_about()
        self.ap.about_page().check_service()
        self.ap.about_page().check_privacy()

    @DecorateClass('CHATAPP-T1767')
    # 修改登入密碼
    def test_change_password(self):
        self.test_login()

        new_pwd = 'Ps43941122'
        
        # 優化：只進入一次安全頁面，完成第一次密碼修改
        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_security()

        if 'email' in self.account_type.lower():
            self.ap.security_page().change_password(self.mail_password, new_pwd)
            self.ap.main_page().logout()
            # iOS 優化：使用優化後的登入流程
            self.ap.main_page().login(self.mail_address, new_pwd, login_method='email')

            # 優化：如果還在安全頁面，直接執行第二次修改，否則重新進入
            # 由於登出後需要重新登入，所以需要重新進入安全頁面
            self.ap.main_page().into_main_setting_page()
            self.ap.member_page().into_security()

            self.ap.security_page().change_password(new_pwd, self.mail_password)
            self.ap.main_page().logout()
            self.ap.main_page().login(self.mail_address, self.mail_password, login_method='email')

        elif 'phone' in self.account_type.lower():
            self.ap.security_page().change_password(self.app_password, new_pwd)
            self.ap.main_page().logout()
            # iOS 優化：使用優化後的登入流程
            self.ap.main_page().login(self.app_phone, new_pwd, self.app_nation)

            # 優化：如果還在安全頁面，直接執行第二次修改，否則重新進入
            # 由於登出後需要重新登入，所以需要重新進入安全頁面
            self.ap.main_page().into_main_setting_page()
            self.ap.member_page().into_security()

            self.ap.security_page().change_password(new_pwd, self.app_password)
            self.ap.main_page().logout()
            self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)

    @DecorateClass('CHATAPP-T1768')
    # 確認帳號與安全資料
    def test_account_info(self):
        self.test_login()

        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_security()
        if 'email' in self.account_type.lower():
            self.ap.security_page().check_value(self.mail_address, self.mail_account, account_type='email')
        elif 'phone' in self.account_type.lower():
            self.ap.security_page().check_value(self.app_phone, self.app_account, self.app_nation)

    @DecorateClass('CHATAPP-T3303')
    # 確認釋出空間
    def test_free_up_space(self):
        self.test_login()
        brand_config = {
            'gu': {
                'uat': {
                    'android': ('GuChat_UAT', 'gubot04'),
                    'ios': ('GuChat_UAT', 'gubot04')
                },
                'prod': {
                    'android': ('GuChat', 'gutest002'),
                    'ios': ('GuChat', 'gutest002')
                }
            },
            'mingpin': {
                'uat': {
                    'android': ('名品会_UAT', 'gubot04'),
                    'ios': ('名品会_UAT', 'gubot04')
                },
                'prod': {
                    'android': ('名品会', 'gutest002'),
                    'ios': ('名品会', 'gutest002')
                }
            },
            'chit': {
                'uat': {
                    'android': ('ChitChat_UAT', 'gubot04'),
                    'ios': ('ChitChat_UAT', 'gubot04')
                },
                'prod': {
                    'android': ('ChitChat', 'gutest002'),
                    'ios': ('ChitChat', 'gutest002')
                }
            },
        }
        product, persoanl_chatroom = brand_config.get(self.brand, {}).get(self.env, {}).get(self.phone_platform.lower(), ('', ''))
        
        # 優化：只進入一次釋出空間頁面，完成所有操作後再離開
        self.ap.main_page().into_main_setting_page()
        self.ap.freeupspace_page().into_free_up_space(product)
        
        # ============================== "釋出所有空間" ===============================
        self.ap.freeupspace_page().clear_all_chat_data()
        
        # ============================== 聊天室上傳測試檔案 ============================
        self.send_file_to_1v1_chatroom_and_group(persoanl_chatroom, self.test_group)

        self.ap.main_page().into_main_setting_page()
        self.ap.freeupspace_page().into_free_up_space(product)
        # ============================== 清除"緩存" ===================================
        self.ap.freeupspace_page().clear_cache_data()
        # ============================== 依聊天室釋出空間 ===============================
        self.ap.freeupspace_page().clear_data_by_chatroom()
        # ============================== 清除"其他檔案" ================================
        self.ap.freeupspace_page().clear_other_files()

    def send_file_to_1v1_chatroom_and_group(self, chatroom, group):
        self.ap.chatlist_page().into_chat_room(chatroom)
        self.ap.chatroom_page().send_file_message(0)
        self.ap.chatlist_page().back_to_checklist()
        self.ap.chatlist_page().into_chat_room(group)
        self.ap.chatroom_page().send_file_message(2)
        self.ap.chatlist_page().back_to_checklist()

    @DecorateClass('CHATAPP-T1760')
    # 好友頁面新增好友
    def test_add_friend(self):
        self.test_login()

        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        new_friend = self.ap.friend_page().is_new_friend(self.operate_account)
        if not new_friend:
            # 如果好友已存在，刪除好友
            self.ap.friend_page().delete_friend_from_UserDetail(self.operate_account)
            self.ap.main_page().into_chat_page()
            self.ap.chatlist_page().into_add_friend_page(self.app_account)
            # 再次檢查是否為新好友
            assert self.ap.friend_page().is_new_friend(self.operate_account)
        # 添加好友
        self.ap.friend_page().add_friend(self.operate_account)
        # 驗證好友已添加（不再是新好友）
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        assert not self.ap.friend_page().is_new_friend(self.operate_account)
    @DecorateClass('CHATAPP-T1762')
    # 好友頁面新增自己
    def test_add_myself(self):
        self.test_login()

        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        self.ap.friend_page().search_clear(self.operate_phone)

        if 'email' in self.account_type.lower():
            self.ap.friend_page().add_myself(self.mail_account, account_type='email')
        elif 'phone' in self.account_type.lower():
            self.ap.friend_page().add_myself(self.app_account, self.app_nation)

    @DecorateClass('CHATAPP-T1761')
    # 好友頁面備註暱稱
    def test_friend_remark(self):
        self.test_login()

        self.ap.main_page().into_friend_page()
        self.ap.friend_page().search_friend_from_list(self.operate_account)
        self.ap.friend_page().set_note('IM自動化測試')
        self.ap.friend_page().set_nickname('tengyuntech_騰雲科技')


    @DecorateClass('CHATAPP-T1764')
    # 好友頁面新增好友黑名單
    def test_block_friend(self):
        self.test_login()

        self.ap.main_page().into_friend_page()
        self.ap.friend_page().search_friend_from_list(self.operate_account)
        self.ap.friend_page().block_friend()
        self.ap.friend_page().impeach_friend()
    
    @DecorateClass('CHATAPP-T1763')
    # 好友頁面刪除好友
    def test_delete_friend(self):
        self.test_login()

        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page(self.app_account)
        new_friend = self.ap.friend_page().is_new_friend(self.operate_account)
        if new_friend:
            self.ap.friend_page().add_friend(self.operate_account)
            self.ap.main_page().into_friend_page()
            assert not self.ap.friend_page().is_new_friend(self.operate_account)
        self.ap.friend_page().delete_friend_from_UserDetail(self.operate_account)
        assert self.ap.friend_page().is_new_friend(self.operate_account)
    @DecorateClass('CHATAPP-T1766')
    # 黑名單頁面備註暱稱
    def test_block_setting(self):
        self.test_login()

        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_blacklist()
        self.ap.blacklist_page().search_friend_from_blackList(self.operate_account)
        self.ap.blacklist_page().set_note('黑名單設定TESt')
        self.ap.blacklist_page().set_nickname('黑名單_Paradise_天堂')
    
    @DecorateClass('CHATAPP-T1765')
    # 解除好友黑名單
    def test_unblock_friend(self):
        self.test_login()

        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_blacklist()
        self.ap.blacklist_page().search_friend_from_blackList(self.operate_account)
        self.ap.blacklist_page().unblock_friend_from_UserDetail()

    @DecorateClass('CHATAPP-T1878')
    # 分享訊息至聊天室
    def test_share_message(self):
        self.test_login()

        self.ap.main_page().into_main_setting_page()
        self.ap.member_page().into_share()
        share_text, share_url = self.ap.share_page().get_share_text()

        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().share_message(share_text)
        if self.phone_platform.lower() == 'android':
            self.ap.chatroom_page().send_message(share_url)
            self.ap.chatroom_page().check_url_message(share_url)

    @DecorateClass('CHATAPP-T1769')
    # 個人發送文字超連結訊息
    def test_send_message(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatlist_page().check_last_message()
        self.ap.chatroom_page().send_url_message()
        self.ap.chatlist_page().check_last_message()

    @DecorateClass('CHATAPP-T1770')
    # 個人訊息複製
    def test_message_copy(self):
        copy_msg = '自动化测试#0'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().copy_message(copy_msg)
        self.ap.chatlist_page().check_last_message()

    @DecorateClass('CHATAPP-T1771')
    # 個人訊息回覆
    def test_message_reply(self):
        reply_msg = '自动化测试#5'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().reply_message(reply_msg)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T1772')
    # 個人訊息刪除
    def test_message_delete(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_message('讯息删除测试case')
        room_message = self.ap.chatroom_page().get_last_message()
        self.ap.chatroom_page().send_message('刪除用测试訊息')
        self.ap.chatroom_page().delete_message('刪除用测试訊息', room_message, -1)

    @DecorateClass('CHATAPP-T1773')
    # 個人訊息撤回
    def test_message_revoke(self):
        self.test_login()

        revoke_msg = '自动化测试#5'
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().revoke_message(revoke_msg)
        self.ap.chatlist_page().check_last_message()

    @DecorateClass('CHATAPP-T2526')
    # 一對一訊息表情符號
    def test_message_emoji(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_message('表情符號用测试訊息')
        self.ap.chatroom_page().add_emoji('表情符號用测试訊息')
        self.ap.chatroom_page().check_emoji('表情符號用测试訊息')

    @DecorateClass('CHATAPP-T1928')
    # 個人訊息回覆後刪除
    def test_message_reply_delete(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_message('刪除用测试訊息')
        self.ap.chatroom_page().reply_message('刪除用测试訊息')
        room_message = self.ap.chatroom_page().get_last_message(is_reply=True)
        self.ap.chatroom_page().delete_message('刪除用测试訊息', room_message, -2, is_reply=True)
        self.ap.chatroom_page().check_reply_title('此讯息已被删除')
        
    @DecorateClass('CHATAPP-T1927')
    # 個人訊息回覆後撤回
    def test_message_reply_revoke(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_message('撤回用测试訊息')
        self.ap.chatroom_page().reply_message('撤回用测试訊息')
        self.ap.chatroom_page().revoke_message('撤回用测试訊息', -2)
        self.ap.chatroom_page().check_reply_title('此讯息已被撤回')

    @DecorateClass('CHATAPP-T1774')
    # 個人訊息設置公告
    def test_message_pin(self):
        self.test_login()
        
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().pin_full_messages()
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1775')
    # 個人訊息設置公告後回覆
    def test_message_pin_reply(self):
        reply_msg = '自动化测试#3'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().reply_message(reply_msg)
        self.ap.chatroom_page().pin_message('回覆訊息测试Test')
        self.ap.chatroom_page().check_pin_message('回覆訊息测试Test')
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1776')
    # 個人訊息設置公告後刪除
    def test_message_pin_delete(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_message('原测试訊息')
        room_message = self.ap.chatroom_page().get_last_message()
        self.ap.chatroom_page().send_message('刪除用测试訊息')
        self.ap.chatroom_page().pin_message('刪除用测试訊息')
        self.ap.chatroom_page().delete_message('刪除用测试訊息', room_message)
        self.ap.chatroom_page().check_pin_message('刪除用测试訊息')
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1777')
    # 個人訊息設置公告後撤回
    def test_message_pin_revoke(self):
        target_msg = '自动化测试#3'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().pin_message(target_msg)
        self.ap.chatroom_page().check_pin_message(target_msg)
        self.ap.chatroom_page().revoke_message(target_msg)
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T3190')
    # 個人-發送語音訊息
    def test_send_voice_message(self):
        self.test_login()

        voice_length = random.randint(10, 15)
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_voice_message(voice_length)
        self.ap.chatlist_page().check_last_message(message_type='voice')

    @DecorateClass('CHATAPP-T3191')
    # 個人-回覆語音訊息
    def test_voice_message_reply(self):
        self.test_login()

        voice_length = random.randint(10, 15)
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_voice_message(voice_length)
        room_voice_message = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().reply_voice_message(room_voice_message)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T3192')
    # 個人-刪除語音訊息
    def test_voice_message_delete(self):
        self.test_login()

        voice_length_1 = random.randint(1, 5)
        voice_length_2 = random.randint(5, 9)
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_voice_message(voice_length_1)
        room_voice_message_1 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().send_voice_message(voice_length_2)
        room_voice_message_2 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().delete_message(room_voice_message_2, room_voice_message_1, -1, is_voice=True)
        assert room_voice_message_1 == self.ap.chatroom_page().get_last_message(is_voice=True)

    @DecorateClass('CHATAPP-T3193')
    # 個人-撤回語音訊息
    def test_voice_message_revoke(self):
        self.test_login()

        voice_length_1 = random.randint(10, 15)
        voice_length_2 = random.randint(15, 19)
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_voice_message(voice_length_1)
        room_voice_message_1 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().send_voice_message(voice_length_2)
        room_voice_message_2 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().revoke_message(room_voice_message_2)
        assert room_voice_message_1 == self.ap.chatroom_page().get_last_message(is_voice=True)

    @DecorateClass('CHATAPP-T3253')
    # 個人-發送檔案訊息
    def test_send_file_message(self):
        self.test_login()
        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_file_message(0)
        self.ap.chatlist_page().check_last_message(message_type='file')

    @DecorateClass('CHATAPP-T3254')
    # 個人-回覆檔案訊息
    def test_file_message_reply(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().reply_file_message(room_file_message)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T3255')
    # 個人-刪除檔案訊息
    def test_file_message_delete(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message_1 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().send_file_message(4)
        room_file_message_2 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().delete_message(room_file_message_2, room_file_message_1, -1, is_file=True)
        assert room_file_message_1 == self.ap.chatroom_page().get_last_message(is_file=True)

    @DecorateClass('CHATAPP-T3256')
    # 個人-撤回檔案訊息
    def test_file_message_revoke(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.operate_account)
        self.ap.chatroom_page().send_file_message(0)
        room_file_message_1 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message_2 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().revoke_message(room_file_message_2, is_file=True)
        assert room_file_message_1 == self.ap.chatroom_page().get_last_message(is_file=True)

    @DecorateClass('CHATAPP-T1778')
    # 群組發送文字超連結訊息
    def test_send_message_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatlist_page().check_last_message()
        self.ap.chatroom_page().send_url_message()
        self.ap.chatlist_page().check_last_message()
        self.ap.chatroom_page().group_delete_history()

    @DecorateClass('CHATAPP-T1779')
    # 群組訊息複製
    def test_message_copy_group(self):
        copy_msg = '自动化测试#0'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().copy_message(copy_msg)
        self.ap.chatlist_page().check_last_message()

    @DecorateClass('CHATAPP-T1780')
    # 群組訊息回覆
    def test_message_reply_group(self):
        reply_msg = '自动化测试#5'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().reply_message(reply_msg)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T1781')
    # 群組訊息刪除
    def test_message_delete_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        room_message = self.ap.chatroom_page().get_last_message()
        self.ap.chatroom_page().send_message('刪除用测试訊息')
        self.ap.chatlist_page().check_last_message()
        self.ap.chatroom_page().delete_message('刪除用测试訊息', room_message, -1)

    @DecorateClass('CHATAPP-T1782')
    # 群組訊息撤回
    def test_message_revoke_group(self):
        revoke_msg = '自动化测试#5'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().revoke_message(revoke_msg)
        self.ap.chatlist_page().check_last_message()
        self.ap.chatroom_page().group_delete_history()


    @DecorateClass('CHATAPP-T1783')
    # 群組訊息設置公告
    def test_message_pin_group(self):
        self.test_login()
        
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().delete_all_pin()
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().pin_full_messages()
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1784')
    # 群組訊息設置公告後回覆
    def test_message_pin_reply_group(self):
        reply_msg = '自动化测试#3'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().group_delete_history()
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().reply_message(reply_msg)
        self.ap.chatroom_page().pin_message('回覆訊息测试Test')
        self.ap.chatroom_page().check_pin_message('回覆訊息测试Test')
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1785')
    # 群組訊息設置公告後刪除
    def test_message_pin_delete_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        room_message = self.ap.chatroom_page().get_last_message()
        self.ap.chatroom_page().send_message('刪除用测试訊息')
        self.ap.chatroom_page().pin_message('刪除用测试訊息')
        self.ap.chatroom_page().delete_message('刪除用测试訊息', room_message)
        self.ap.chatroom_page().check_pin_message('刪除用测试訊息')
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T1786')
    # 群組訊息設置公告後撤回
    def test_message_pin_revoke_group(self):
        target_msg = '自动化测试#3'
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_text_message()
        self.ap.chatroom_page().pin_message(target_msg)
        self.ap.chatroom_page().check_pin_message(target_msg)
        self.ap.chatroom_page().revoke_message(target_msg)
        self.ap.chatroom_page().delete_all_pin()

    @DecorateClass('CHATAPP-T3194')
    # 群組內發送語音訊息
    def test_send_voice_message_group(self):
        self.test_login()

        voice_length = random.randint(10, 15)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_voice_message(voice_length)
        self.ap.chatlist_page().check_last_message(message_type='voice')
        self.ap.chatroom_page().group_delete_history()

    @DecorateClass('CHATAPP-T3195')
    # 群組內回覆語音訊息
    def test_voice_message_reply_group(self):
        self.test_login()

        voice_length = random.randint(15, 19)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_voice_message(voice_length)
        room_voice_message = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().reply_voice_message(room_voice_message)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T3196')
    # 群組內刪除語音訊息
    def test_voice_message_delete_group(self):
        self.test_login()

        voice_length_1 = random.randint(1, 5)
        voice_length_2 = random.randint(5, 9)
        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_voice_message(voice_length_1)
        room_voice_message_1 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().send_voice_message(voice_length_2)
        room_voice_message_2 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().delete_message(room_voice_message_2, room_voice_message_1, -1, is_voice=True)
        assert room_voice_message_1 == self.ap.chatroom_page().get_last_message(is_voice=True)

    @DecorateClass('CHATAPP-T3197')
    # 群組內撤回語音訊息
    def test_voice_message_revoke_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_voice_message(15)
        room_voice_message_1 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().send_voice_message(10)
        room_voice_message_2 = self.ap.chatroom_page().get_last_message(is_voice=True)
        self.ap.chatroom_page().revoke_message(room_voice_message_2)
        assert room_voice_message_1 == self.ap.chatroom_page().get_last_message(is_voice=True)

    @DecorateClass('CHATAPP-T3257')
    # 群組-發送檔案訊息
    def test_send_file_message_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_file_message(0)
        self.ap.chatlist_page().check_last_message(message_type='file')
        self.ap.chatroom_page().group_delete_history()

    @DecorateClass('CHATAPP-T3258')
    # 群組-回覆檔案訊息
    def test_file_message_reply_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().reply_file_message(room_file_message)
        self.ap.chatlist_page().check_last_message(is_reply=True)

    @DecorateClass('CHATAPP-T3259')
    # 群組-刪除檔案訊息
    def test_file_message_delete_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message_1 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().send_file_message(4)
        room_file_message_2 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().delete_message(room_file_message_2, room_file_message_1, -1,
                                                               is_file=True)
        assert room_file_message_1 == self.ap.chatroom_page().get_last_message(is_file=True)

    @DecorateClass('CHATAPP-T3260')
    # 群組-撤回檔案訊息
    def test_file_message_revoke_group(self):
        self.test_login()

        self.ap.chatlist_page().into_chat_room(self.test_group)
        self.ap.chatroom_page().send_file_message(0)
        room_file_message_1 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().send_file_message(2)
        room_file_message_2 = self.ap.chatroom_page().get_last_message(is_file=True)
        self.ap.chatroom_page().revoke_message(room_file_message_2, is_file=True)
        assert room_file_message_1 == self.ap.chatroom_page().get_last_message(is_file=True)

    @DecorateClass('CHATAPP-T2568')
    # 透過邀請碼加入群組 > 退出群組
    def test_join_group_by_share_code(self):
        if self.brand.lower() == 'gu' or 'mingpin' or 'chit':
            share_code = 'AUTOTEST'
        elif self.brand.lower() == 'mee':
            share_code ='AUTOMEE'
        group_name = 'AuToTeSt'
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.chatlist_page().join_group_by_input_share_code(share_code, group_name)
        self.ap.chatlist_page().leave_group(group_name)

    @DecorateClass('CHATAPP-T2928')
    # 發現頁 > 確認功能懸浮按鈕與選單
    def test_discover_floating_icon(self):
        self.test_login()

        if self.env.lower() == 'prod':
            random_index = random.randint(0, 1)
        else:
            random_index = random.randint(0, 2)

        self.ap.discover_pages().into_discover_page()
        self.ap.discover_pages().check_discover_menu_and_icon(random_index)


    @DecorateClass('CHATAPP-T2717')
    # 媒體發布_圖片
    def test_social_post_photo(self):
        account = self.login_self_account()

        # ➤ 先決定要取幾個（3~10）
        count = random.randint(3, 10)
        # 第一次選：-4 ~ -1
        first = random.choice(range(-4, 0))
        # 後續選：-20 ~ -1（不重複），且可以包含 first
        remaining_pool = list(range(-20, 0))  # -20 到 -1 全部
        # 後續選取 count - 1 個「不重複」，但 pool 裡有 first 所以可能抽到 first
        rest = random.sample(remaining_pool, count - 1)
        # 最終結果，第一個元素必定是首次選取的
        media_index = [first] + rest

        media_type = 'photo'
        # ================= 發布頁設置=====================
        current_time = datetime.datetime.now().strftime("%H_%M")
        description = f'👿{self.phone_platform}自動化{self.brand}Test_發布{media_type}_{current_time}👿'
        privacy_index = 0  # 隱私權設定: 所有人
        save_to_local = True  # 儲存至裝置: 開啟
        post = True  # 發布
        #================================================
        if self.phone_platform.lower() == 'ios':
            self.ap.socialmediapost_page().ios_select_media(media_index)
        else:
            self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index, media_type, save_to_local, post)
        self.ap.socialmedialibrary_page().check_recent_post_media(account, description, post)
        self.ap.socialshare_page().check_share_popup_window(save_to_local, self_post=True) # 確認分享彈窗
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post(account, description)

    # 媒體發布_視頻
    @DecorateClass('CHATAPP-T2718')
    def test_social_post_video(self):
        account = self.login_self_account()

        media_index = random.randint(-11, -1)
        media_type = 'video'
        # ================= 發布頁設置=====================
        description = f'👿😡😍自動化{self.brand}Test_發布{media_type}👿😡😍{media_index}'
        privacy_index = 0  # 隱私權設定: 所有人
        save_to_local = True  # 儲存至裝置: 開啟
        post = True  # 發布
        # ================================================
        self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index, media_type, save_to_local, post)
        self.ap.socialmedialibrary_page().check_recent_post_media(account, description, post)
        self.ap.socialshare_page().check_share_popup_window(save_to_local, self_post=True)  # 確認分享彈窗
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post(account, description)

    # 發布成草稿_圖片 (測試帳號原環境無任何草稿)
    @DecorateClass('CHATAPP-T2775')
    def test_social_draft_photo(self):
        self.login_self_account()

        # ➤ 先決定要取幾個（1~5）
        count = random.randint(1, 3)
        # 第一次選：-4 ~ -1
        first = random.choice(range(-4, 0))
        # 後續選：-20 ~ -1（不重複），且可以包含 first
        remaining_pool = list(range(-20, 0))  # -20 到 -1 全部
        # 後續選取 count - 1 個「不重複」，但 pool 裡有 first 所以可能抽到 first
        rest = random.sample(remaining_pool, count - 1)
        # 最終結果，第一個元素必定是首次選取的
        media_index = [first] + rest

        media_type = 'photo'
        # ================= 發布頁設置=====================
        current_time = datetime.datetime.now().strftime("%H_%M")
        description = f'👿😡😍自動化{self.brand}Test_草稿{media_type}_{current_time}👿😡😍'
        privacy_index = 0  # 隱私權設定: 所有人
        save_to_local = True  # 儲存至裝置: 開啟
        post = False  # 存成草稿
        # ================================================
        original_draft_counts = self.ap.socialmedialibrary_page().draft_media_counts()
        current_date = datetime.datetime.now().strftime('%Y/%m/%d')
        if self.phone_platform.lower() == 'ios':
            self.ap.socialmediapost_page().ios_select_media(media_index)
        else:
            self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index, media_type, save_to_local, post)  # 發布為草稿
        self.ap.socialmedialibrary_page().check_draft_folder_exist(True)  # 確認草稿夾存在
        self.ap.socialmedialibrary_page().delete_draft_media(original_draft_counts, current_date)  # 刪除該筆草稿
        self.ap.socialmedialibrary_page().check_draft_folder_exist(False)  # 確認草稿夾內無任何草稿時, 整個草稿夾消失不顯示

    # 搜索視頻 & 用戶
    @DecorateClass('CHATAPP-T2787')
    def test_social_search(self):
        poster_phone_list = [self.web_phone, self.wap_phone]
        poster_nickname_list = [self.web_account, self.wap_account]
        description_list = []
        for poster_phone, poster_nickname in zip(poster_phone_list, poster_nickname_list):
            self.ap.main_page().login(poster_phone, self.web_password, self.web_nation)

            privacy_index = 0  # 貼文隱私設置: 0所有人
            media_list = ['video', 'photo']
            media_index = random.randint(-10, -1)
            current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

            description = f'{self.brand}SearchTest_{current_time}'
            description_list.append(description)
            save_to_local = True  # 儲存至裝置: 開啟
            post = True  # 發布

            if self.phone_platform.lower() == 'ios':
                self.ap.socialmediapost_page().ios_select_media(media_index)
                self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index,
                                                                                          'photo', save_to_local, post)
            else:
                media_type = random.choice(media_list)
                self.ap.socialmediapost_page().select_media(media_index, media_type)
                self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index,
                                                                                      media_type, save_to_local, post)
            # self.ap.socialmedialibrary_page().check_recent_post_media(poster_nickname, description, post)
            self.ap.socialhome_page().return_to_my_social_page()
        # ========================== gubot03/gubotmail01 登入 ===========================================================
        self.login_self_account()
        # ========================== 1. 搜索頁: 輸入01貼文說明01 > 點搜索鍵 >>> 搜索結果-視頻頁 ===============================
        self.ap.socialsearch_page().search_from_search_page(description_list[0])
        self.ap.socialsearch_page().check_search_post_result(poster_nickname_list[0],
                                                                             description_list[0])
        # ========================== 2. 搜索視頻結果頁: 輸入02貼文說明02 > 點搜索鍵 >>> 搜索結果-視頻頁 =========================
        self.ap.socialsearch_page().search_post(description_list[1], search_by_switch_tab=False)
        self.ap.socialsearch_page().check_search_post_result(poster_nickname_list[1],
                                                                             description_list[1])
        # ========================== 3. 搜索視頻結果頁: 輸入01 > 點"用戶"頁籤 >>> 切換到用戶頁並立即搜索 ========================
        self.ap.socialsearch_page().search_poster(poster_nickname_list[0],
                                                                  search_by_switch_tab=True)
        self.ap.socialsearch_page().check_search_post_user_result(poster_nickname_list[0])
        # ========================== 4. 搜索用戶結果頁: 輸入02 > 點搜索鍵 >>> 搜索結果-用戶頁 =================================
        self.ap.socialsearch_page().search_poster(poster_nickname_list[1],
                                                                  search_by_switch_tab=False)
        self.ap.socialsearch_page().check_search_post_user_result(poster_nickname_list[1])
        # ========================== 5. 搜索用戶結果頁: 輸入02貼文說明02 > 點"視頻"頁籤 >>> 立即搜索 ===========================
        self.ap.socialsearch_page().search_post(description_list[1], search_by_switch_tab=True)
        self.ap.socialsearch_page().check_search_post_result(poster_nickname_list[1],
                                                                             description_list[1])
        # ========================== 確認搜索紀錄頁 =======================================================================
        self.ap.socialsearch_page().check_recent_search_record(
            [description_list[1], poster_nickname_list[1],
             poster_nickname_list[0], description_list[0]])

    # 關注他人 > 取消關注他人
    @DecorateClass('CHATAPP-T2776')
    def test_social_follow_unfollow(self):
        self.test_login()

        self.add_friend_then_into_chatroom()  # 新增operator_account (test1234) 為好友
        self.ap.socialhome_page().return_to_my_social_page()
        original_main_page_followed_counts,fans_counts, thumb_up_counts = self.ap.socialhome_page().get_page_all_counts()  # 取得自己主頁關注數
        # ============================ 關注對方 ====================================
        self.ap.main_page().into_friend_page()
        self.ap.friend_page().search_friend_from_list(self.operate_account)
        self.ap.socialhome_page().into_member_social_page_from_chat(self.operate_account)  # 從聊天室個人資訊進入對方主頁
        fans_counts_after_followed = self.ap.socialhome_page().follow_member(self.operate_account)  # 關注對方 > 確認對方粉絲數+1,關注建"已關注", 回傳對方目前粉絲數
        self.ap.socialhome_page().return_to_my_social_page()
        after_followed_counts, fans_counts, thumb_up_counts = self.ap.socialhome_page().get_page_all_counts()  # 取得自己主頁關注數
        assert int(after_followed_counts) == int(original_main_page_followed_counts) + 1  # 確認自己主頁關注數新增1
        self.ap.socialhome_page().into_followed_list()  # 進入主頁關注列表
        self.ap.socialhome_page().check_followed_list(self.operate_account, after_followed_counts, add_follow=True)  # 確認關注列表: 關注數+1, 對方出現在列表
        self.ap.socialhome_page().return_to_my_social_page()
        # ============================ 取消關注對方 ==================================
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().unfollow_member(self.operate_account, after_followed_counts)  # 取消關注對方 > 確認自己關注頁籤數-1, 關注建"關注"
        self.ap.socialhome_page().return_to_my_social_page()
        after_unfollowed_counts, fans_counts, thumb_up_counts = self.ap.socialhome_page().get_page_all_counts()  # 取得自己主頁關注數
        assert int(after_unfollowed_counts) == int(after_followed_counts) - 1  # 確認自己主頁關注數減少1
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().check_followed_list(self.operate_account, after_unfollowed_counts, add_follow=False)  # 確認關注列表: 自己關注數-1, 列表不出現對方
        # ============================ 確認對方粉絲列表 ===============================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.main_page().into_friend_page()
        self.ap.friend_page().search_friend_from_list(self.operate_account)
        followed_counts, fans_counts_after_unfollowed, thumb_up_counts = self.ap.socialhome_page().into_member_social_page_from_chat(self.operate_account)  # 進入對方主頁並取得當下對方粉絲數
        assert int(fans_counts_after_unfollowed) == int(fans_counts_after_followed) - 1  # 對方主頁粉絲數少1
        self.ap.socialhome_page().into_fans_list()  # 進入對方粉絲頁
        self.ap.socialhome_page().check_fans_list(self.operate_account, fans_counts_after_unfollowed, add_fans=False) # 確認對方粉絲列表: 對方粉絲數-1, 列表上不出現我

        self.ap.socialhome_page().return_to_my_social_page()
        self.delete_friend_via_userDetail()  #刪除好友 operator_account (test1234)

    def add_friend_then_into_chatroom(self):
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page()
        new_friend = self.ap.friend_page().is_new_friend(self.operate_account)
        if not new_friend:
            self.ap.friend_page().into_chatroom_via_userDetail()
        else:
            self.ap.friend_page().into_chatroom_via_addToAddressBook()
    def delete_friend_via_userDetail(self):
        self.ap.main_page().into_chat_page()
        self.ap.chatlist_page().into_add_friend_page()
        new_friend = self.ap.friend_page().is_new_friend(self.operate_account)
        if not new_friend:
            self.ap.friend_page().delete_friend_from_UserDetail(self.operate_account)

    # 貼文點贊+收藏
    @DecorateClass('CHATAPP-T2778')
    def test_social_post_add_like_collect(self):
        # ============================ 他人(gubot02) 發布貼文 ===============================
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)

        media_index = random.randint(-20, -1)
        current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        media_type = 'photo'
        # ------------------ 發布頁設置 ------------------
        description = f'👿自動化{self.brand}Test_貼文點贊收藏_{current_time}👿'
        privacy_index = 0  # 隱私權設定: 所有人
        save_to_local = True  # 儲存至裝置: 開啟
        post = True  # 發布
        # -----------------------------------------------
        self.ap.socialmediapost_page().select_media(media_index, media_type)
        self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index, media_type, save_to_local, post)
        self.ap.socialmedialibrary_page().check_recent_post_media(self.web_account, description, post)
        # ============================ 他人(gubot02) 對 他人(gubot02) 貼文點贊 ======================
        self.ap.socialmedialibrary_page().self_post_add_like(self.web_account)
        self.ap.socialhome_page().return_to_my_social_page()
        # ============================ 我(gubot03/gubotmail01) 對 他人(gubot02) 貼文點贊 ======================
        # ----------- 登入"我的"帳號 -----------
        if 'email' in self.account_type.lower():
            self.ap.main_page().login(self.mail_address, self.mail_password, login_method='email')
        elif 'phone' in self.account_type.lower():
            self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        # ------------------------------------
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        follow_counts, fans_count, thumb_up_counts = self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account) # 進入到他人主頁
        self.ap.socialmedialibrary_page().into_first_post(self.web_account, description)
        main_after_add_liked_counts, post_after_add_liked_counts = self.ap.socialmedialibrary_page().post_add_like(thumb_up_counts)  # 在他人剛發的貼文上點贊
        self.ap.socialhome_page().return_to_my_social_page()  # 回到我的主頁
        self.ap.socialmedialibrary_page().check_my_liked_library_after_add(self.web_account, description)  # 進入我的點贊媒體櫃確認"新增"
        # ============================ 我(gubot03/gubotmail01) 對 他人(gubot02) 貼文取消贊 ======================
        self.ap.socialmedialibrary_page().check_my_liked_library_after_uncollected(description)  # 進入我的點贊媒體櫃確認"移除"
        self.ap.socialhome_page().return_to_my_social_page()  # 回到我的主頁
        self.ap.socialhome_page().into_followed_list()
        follow_counts, fans_count, thumb_up_counts_after_cancel = self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        assert int(thumb_up_counts_after_cancel) == int(main_after_add_liked_counts) - 1, f'取消對方贊後, 對方主頁贊數沒有-1'
        self.ap.socialmedialibrary_page().into_first_post(self.web_account, description)
        self.ap.socialmedialibrary_page().check_post_liked_counts_after_cancel(post_after_add_liked_counts)
        # ============================ 我(gubot03/gubotmail01) 對 他人(gubot02) 貼文進行收藏 ====================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        self.ap.socialmedialibrary_page().into_first_post(self.web_account, description)
        post_after_collected_counts = self.ap.socialmedialibrary_page().post_add_collect() # 在他人剛發的貼文上點收藏
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().check_my_collected_library_after_add(self.web_account, description)  # 進入我的收藏媒體櫃確認"新增"
        # ============================ 我(gubot03/gubotmail01) 對 他人(gubot02) 貼文取消收藏 ====================
        self.ap.socialmedialibrary_page().check_my_collected_library_after_uncollected(description)  # 進入我的收藏媒體櫃確認"移除"
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        self.ap.socialmedialibrary_page().into_first_post(self.web_account, description)
        self.ap.socialmedialibrary_page().check_post_collects_after_cancel(post_after_collected_counts)

    # 自己貼文上評論: 自己留言+回覆 > 他人留言+回覆 > 他人點贊 > 我點贊
    @DecorateClass('CHATAPP-T2780')
    def test_social_self_post_add_comments_reply_like(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        comment = f'🍄[我]留言test_{current_time}🍄'
        reply_comment = f'🍊🍉[我]回覆[我]母留言test_{current_time}🍉🍊'
        reply_reply_comment = f'🥦🥪🌭[他人]回覆[我]子留言test_{current_time}🌭🥪🥦'
        # ============================ 我(gubot03/gubotmail01) 在 我的第一則公開貼文上"留言" =================================
        self_account = self.login_self_account()
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=True)  # 確認自己貼文的評論頁出現評論/贊/觀看次數頁籤
        self.ap.socialmedialibrary_page().post_add_comment(self_account, comment, post_url=False, self_post=True)  # 留言+確認留言相關
        # ============================ 我(gubot03/gubotmail01) 在 我的貼文最新自己留言上"回覆留言" ===========================
        self.ap.socialmedialibrary_page().post_recent_comment_add_reply(self_account, self_account, reply_comment, self_post=True) # 回覆留言+確認回覆相關
        self.ap.socialhome_page().return_to_my_social_page()
        # ============================ 他人(gubot02) 在 我(gubot03/gubotmail01) 的第一則公開貼文上確認最新一則留言&回覆訊息 ======
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self_account)
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=False)
        self.ap.socialmedialibrary_page().check_post_recent_comment(comment)  # 確認出現稍早我(gubot03/gubotmail01)的留言
        self.ap.socialmedialibrary_page().check_post_recent_reply(reply_comment)  # 確認出現稍早我(gubot03/gubotmail01)的回覆留言
        # ============================ 他人(gubot02) 在 我(gubot03/gubotmail01) 該貼文最新留言(母留言)的最新回覆訊息(子留言)上"回覆" ====================
        self.ap.socialmedialibrary_page().post_recent_comment_recent_reply_add_reply(self_account, self.web_account, reply_reply_comment, self_post=False)
        # ============================ 他人(gubot02) 在 我(gubot03/gubotmail01) 該則貼文最新留言(母留言)與最新回覆訊息(子留言)上"點贊" ====================
        recent_comment_after_add_liked_counts = self.ap.socialmedialibrary_page().post_recent_comment_add_like()
        recent_reply_after_add_liked_counts = self.ap.socialmedialibrary_page().post_recent_reply_add_like()
        # ============================ 我(gubot03/gubotmail01) 在 我 該則貼文上確認最新留言(母留言)與最新回覆訊息(子留言)的"贊數" ================
        self.ap.socialhome_page().return_to_my_social_page()
        self.test_logout()
        self.login_self_account()
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=True)
        assert self.ap.socialmedialibrary_page().check_recent_comment_liked_counts() == recent_comment_after_add_liked_counts
        assert self.ap.socialmedialibrary_page().check_recent_reply_liked_counts() == recent_reply_after_add_liked_counts
        # ============================ 我(gubot03/gubotmail01) 在 我 該則貼文上最新留言(母留言)與最新回覆訊息(子留言)上"點贊" ====================
        self.ap.socialmedialibrary_page().post_recent_comment_add_like()
        self.ap.socialmedialibrary_page().post_recent_reply_add_like()
    def login_self_account(self):
        """登入自己的帳號並返回帳號名稱"""
        self.login_app()
        if 'email' in self.account_type.lower():
            return self.mail_account
        elif 'phone' in self.account_type.lower():
            return self.app_account

    # 他人貼文上評論: 自己留言+回覆 > 他人留言+回覆 > 他人點贊 > 我點贊
    @DecorateClass('CHATAPP-T2781')
    def test_social_other_post_add_comments_reply(self):
        self_account = self.login_self_account()

        current_time = datetime.datetime.now().strftime("%H:%M")
        comment = f'🌹{self_account}留言Test_{current_time}🌹'
        reply_comment = f'🥪🌭{self_account}回覆{self_account}留言test_{current_time}🌭🥪'

        # ============================ 我(gubot03/gubotmail01) 在 他人(gubot02) 的貼文上"留言"+"回覆"========================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=False)
        self.ap.socialmedialibrary_page().post_add_comment(self_account, comment, post_url=False, self_post=False)  # 留言+確認留言相關
        self.ap.socialmedialibrary_page().post_recent_comment_add_reply(self_account, self_account, reply_comment,self_post=False)  # 回覆留言+確認回覆相關
        self.ap.socialhome_page().return_to_my_social_page()
        # ============================ 他人(gubot02) 在 他的"第一則公開貼文"上確認"最新一則留言" & "回覆訊息" ===================
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialmedialibrary_page().into_post_comment_page(self_post=True)
        self.ap.socialmedialibrary_page().check_post_recent_comment(comment)  # 確認出現稍早我(gubot03/gubotmail01)的留言
        self.ap.socialmedialibrary_page().check_post_recent_reply(reply_comment)  # 確認出現稍早我(gubot03/gubotmail01)的回覆留言

    # 切換帳號隱私設定 > 確認他人端觀看"已點贊"媒體區
    @DecorateClass('CHATAPP-T2786')
    def test_social_change_account_privacy(self):
        account_privacy_setting_list = [1, 0]  # 1:僅自己, 0:所有人
        for account_privacy in account_privacy_setting_list:
            # =================== 我(gubot03/gubotmail01)更改隱私設定 ===================
            # self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
            account = self.login_self_account()
            self.ap.privacy_page().into_privacy_page()
            self.ap.privacy_page().change_privacy(account_privacy)
            self.ap.socialhome_page().return_to_my_social_page()
            # =================== 他人(gubot02)端觀看"已點贊"媒體區 ===================
            self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
            self.ap.socialhome_page().return_to_my_social_page()
            self.ap.socialhome_page().into_followed_list()
            self.ap.socialhome_page().into_member_social_page_from_followed_list(account)
            self.ap.socialmedialibrary_page().into_liked_library(account_privacy)
            self.ap.socialhome_page().return_to_my_social_page()

    # 發布不同隱私權限貼文 > 確認不同關注狀態用戶觀看
    @DecorateClass('CHATAPP-T2782')
    def test_social_post_with_different_privacy(self):
        self.ap.main_page().login(self.app_phone, self.app_password, self.app_nation)
        self.ap.socialhome_page().return_to_my_social_page()

        # ================= gubot03 依序發布 所有人 > 互關 > 粉絲 > 僅自己 4則貼文 ===========================================
        privacy_list =[0,1,2,3]  # 隱私設置: 0所有人, 1互關, 2粉絲, 3僅自己
        privacy_description_list = ['所有人', '互關', '粉絲', '僅自己']
        media_list = ['video', 'photo']
        description_list=[]
        for privacy_index in privacy_list:
            media_index = random.randint(-10, -1)
            current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            media_type = random.choice(media_list)
            description = f'👿自動化{self.brand}Test_{media_type}_{privacy_description_list[privacy_index]}_{current_time}👿'
            description_list.append(description)
            save_to_local = True  # 儲存至裝置: 開啟
            post = True  # 發布

            self.ap.socialmediapost_page().select_media(media_index, media_type)
            self.ap.socialmediapost_page().post_page_setting_and_post(description, privacy_index, media_type, save_to_local, post)
            self.ap.socialmedialibrary_page().check_recent_post_media(self.app_account, description, post)
        self.ap.socialhome_page().return_to_my_social_page()

        # ================= 互關成員 gubot04/05/06 觀看貼文確認 ============================================================
        # 定義每個帳號的 media_type 和 privacy_index
        if self.brand == 'gu':
            if self.env =='uat':
                account_list = ['13542600004', '13542600005', '13542600006']
            else:
                account_list = ['9016000203', '9016000204', '9016000205']  # 正式環境
        elif self.brand == 'mingpin':
            if self.env =='uat':
                account_list = ['13542600004', '13542600005', '13542600006']
            else:
                account_list = ['', '', '']  # 正式環境
        elif self.brand == 'mee':
            if self.env=='uat':
                account_list = ['5568844444', '5568855555', '5568866666']
            else:
                account_list = ['9016001203', '9016001204', '9016001205']  # 正式環境
        elif self.brand == 'chit':
            if self.env=='uat':
                account_list = ['15629302627', '15629302626', '15629302629']
            else:
                account_list = ['']  # 正式環境
        account_checks = {
            account_list[0]: {'media_index': [0, 1, 2], 'privacy_index': [2, 1, 0]},  # 04看到貼文順序: 粉絲貼文 > 互關貼文 > 所有人貼文
            account_list[1]: {'media_index': [0, 1], 'privacy_index': [2, 0]},  # 05看到貼文順序: 粉絲貼文 > 所有人貼文
            account_list[2]: {'media_index': [0], 'privacy_index': [0]},  # 06看到貼文順序: 所有人貼文
        }

        # 定義執行檢查的函數
        def check_media_for_user(account, descriptions, media_index, privacy_index):
            self.ap.main_page().login(account, self.app_password, self.app_nation)
            self.ap.socialhome_page().return_to_my_social_page()

            if account == account_list[2]:
                self.ap.main_page().into_friend_page()
                self.ap.friend_page().search_friend_from_list(self.app_account)
                self.ap.socialhome_page().into_member_social_page_from_chat(
                    self.app_account)  # 從聊天室進入個人頁面
            else:
                self.ap.socialhome_page().into_followed_list()
                self.ap.socialhome_page().into_member_social_page_from_followed_list(
                    self.app_account)  # 從關注列表進入個人頁面

            # 使用 zip 遍歷 media_type 和 privacy_index 的配對
            for media_index, privacy_index in zip(media_index, privacy_index):
                description = descriptions[privacy_index]  # 根據 privacy_index 取 description
                self.ap.socialmedialibrary_page().check_post_media_info(
                    self.app_account, description, media_index=media_index, privacy_index=privacy_index)

            self.ap.socialhome_page().return_to_my_social_page()

        # 迴圈遍歷每個 account 並執行對應的檢查
        for account, checks in account_checks.items():
            media_index = checks['media_index']
            privacy_index = checks['privacy_index']
            check_media_for_user(account, description_list, media_index, privacy_index)

    # 分享自己主頁
    @DecorateClass('CHATAPP-T2827')
    def test_social_share_self_main_page(self):
        self_account = self.login_self_account()

        current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        share_message = f'{self.brand}_分享自己({self_account})主頁_{current_time}'
        share_group = self.test_group
        # ============================= 自己端(gubot03/gubotmail01)分享"自己主頁"到聊天室 ==============================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialshare_page().into_share_pop_window(0)
        self.ap.socialshare_page().share_to_group(share_group, share_message, share_main_page=True)
        self.ap.chatlist_page().into_chat_room(share_group)
        # ============================= 自己端(gubot03/gubotmail01)確認聊天室內分享文 ==================================
        self.ap.socialshare_page().check_chatroom_share_result(self_account, share_message, share_main_page=True)
        self.ap.chatroom_page().group_delete_history()
        # ============================= 他人(gubot02)端確認聊天室內分享文 ====================================
        self.ap.chatlist_page().back_to_checklist()
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        self.ap.socialshare_page().check_chatroom_share_result(self_account, share_message,
                                                                               share_main_page=True, my_share=False)
        self.ap.chatroom_page().group_delete_history()

    # 分享他人主頁
    @DecorateClass('CHATAPP-T2828')
    def test_social_share_other_main_page(self):
        self_account = self.login_self_account()
        current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        share_message = f'{self.brand}_分享他人({self.web_account})主頁_{current_time}'
        share_group = self.test_group
        # ============================= 自己端(gubot03/gubotmail01)分享"他人(gubot02)主頁"到聊天室 ==========================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        self.ap.socialshare_page().into_share_pop_window(1)
        self.ap.socialshare_page().share_to_group(share_group, share_message, share_main_page=True)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        # ============================= 自己端(gubot03/gubotmail01)確認聊天室內分享文 ====================================
        self.ap.socialshare_page().check_chatroom_share_result(self.web_account, share_message,
                                                                               share_main_page=True)
        self.ap.chatroom_page().group_delete_history()
        # ============================= 他人端(gubot02)確認聊天室內分享文 ====================================
        self.ap.chatlist_page().back_to_checklist()
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        self.ap.socialshare_page().check_chatroom_share_result(self.web_account, share_message,
                                                                               share_main_page=True, my_share=False)
        self.ap.chatroom_page().group_delete_history()
    # 分享自己貼文
    @DecorateClass('CHATAPP-T2830')
    def test_social_share_self_post(self):
        self_account = self.login_self_account()

        current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        share_message = f'{self.brand}_分享自己({self_account})貼文_{current_time}'
        share_group = self.test_group
        # ============================= 自己端(gubot03/gubotmail01)分享"自己貼文"到聊天室 ==========================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialshare_page().into_share_pop_window(2)
        self.ap.socialshare_page().share_to_group(share_group, share_message, share_main_page=False)
        self.ap.chatlist_page().into_chat_room(share_group)
        # ============================= 自己端(gubot03/gubotmail01)確認聊天室內分享文 ==============================
        self.ap.socialshare_page().check_chatroom_share_result(self_account, share_message,
                                                                               share_main_page=False)
        self.ap.chatroom_page().group_delete_history()
        # ============================= 他人端(gubot02)確認聊天室內分享文 ===========================================
        self.ap.chatlist_page().back_to_checklist()
        self.ap.socialhome_page().return_to_my_social_page()

        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        self.ap.socialshare_page().check_chatroom_share_result(self_account, share_message,
                                                                               share_main_page=False, my_share=False)
        self.ap.chatroom_page().group_delete_history()

    # 分享他人貼文
    @DecorateClass('CHATAPP-T2829')
    def test_social_share_others_post(self):
        self_account = self.login_self_account()

        current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        share_message = f'{self.brand}_分享他人({self.web_account})貼文_{current_time}'
        share_group = self.test_group
        # ============================= 自己端(gubot03/gubotmail01)分享"他人(gubot02)貼文"到聊天室 =======================
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.socialhome_page().into_followed_list()
        self.ap.socialhome_page().into_member_social_page_from_followed_list(self.web_account)
        self.ap.socialmedialibrary_page().into_first_post()
        self.ap.socialshare_page().into_share_pop_window(3)
        self.ap.socialshare_page().share_to_group(share_group, share_message, share_main_page=False)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        # ============================= 自己端(gubot03/gubotmail01)確認聊天室內分享文 ====================================
        self.ap.socialshare_page().check_chatroom_share_result(self.web_account, share_message,
                                                                               share_main_page=False)
        self.ap.chatroom_page().group_delete_history()
        # ============================= 他人端(gubot02)確認聊天室內分享文 ====================================
        self.ap.chatlist_page().back_to_checklist()
        self.ap.main_page().login(self.web_phone, self.web_password, self.web_nation)
        self.ap.socialhome_page().return_to_my_social_page()
        self.ap.chatlist_page().into_chat_room(share_group)
        self.ap.socialshare_page().check_chatroom_share_result(self.web_account, share_message,
                                                                          share_main_page=False, my_share=False)
        self.ap.chatroom_page().group_delete_history()

    # 測試-email欄位檢核
    @DecorateClass('CHATAPP-T')
    def test_email_input_field_check(self):
        # ======== 登入頁 =========
        self.ap.main_page().input_email_check_in_login()
        # ======== 註冊頁 =========
        self.ap.main_page().input_email_check_in_registration()

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
