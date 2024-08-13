import unittest, sys, os, random, re
from datetime import datetime
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.web.testcase.base_testcase import BaseTestCase
from Project.chat.web.pages.webs.web_basepage import BasePage as BasePage_Web
from Project.chat.web.pages.admin.admin_basepage import BasePage as BasePage_Admin

from common.utils.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass

class WebTestCase(BaseTestCase, BasePage_Web, BasePage_Admin):
    # Chrome Setting
    wait_time =20
    implicitly_wait_time = 35
    chrome_crash = 0
    foloderpath = ''
    group_name =  datetime.now().strftime("%y%m%d") + "_bot_group"
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

        cls.test_all_windows_mini(cls)
        cls.function_dict['wp'].basePage().windows_to_top() # 切換視窗

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
        cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].basePage().hide_windows()

        if not sys.argv[0].__contains__('prod'):
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
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
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top()
    
    # 測試-登入
    @DecorateClass('CHATAPP-T1790')
    def test_web_login(self):
        self.test_all_windows_mini()
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].loginPage().login(self.web_phone, self.web_password, self.web_nation)

    # 測試-登出
    @DecorateClass('CHATAPP-T1791')
    def test_web_logout(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().logout()

    # 測試-進入訊息通知
    @DecorateClass('CHATAPP-T1792')
    def test_into_notification(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_notification_page()
        self.function_dict['wp'].mainPage().close_modal(1)

    # 測試-進入帳號與安全頁面
    @DecorateClass('CHATAPP-T1793')
    def test_into_security(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].mainPage().close_modal(1)
    
    # 測試-檢查帳號與手機號碼
    @DecorateClass('CHATAPP-T1794')
    def test_account_info(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().check_mysecurity(self.web_account, self.web_phone, self.web_nation)

    # 測試-變更登入密碼
    @DecorateClass('CHATAPP-T1795')
    def test_change_password(self):
        self.test_web_login()

        new_pwd = 'Ps43941122'
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().change_password(self.web_password, new_pwd)
        
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().logout()
        self.function_dict['wp'].loginPage().login(self.web_phone, new_pwd, self.web_nation)

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().change_password(new_pwd, self.web_password)
        
        self.function_dict['wp'].mainPage().into_security_page()
        self.function_dict['wp'].securityPage().logout()
        self.function_dict['wp'].loginPage().login(self.web_phone, self.web_password, self.web_nation)

    # 測試-進入黑名單頁面
    @DecorateClass('CHATAPP-T1796')
    def test_into_black(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_black_page()
        self.function_dict['wp'].mainPage().close_modal(1)

    # 測試-進入分享頁面
    @DecorateClass('CHATAPP-T1797')
    def test_into_share(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_share_page()
        self.function_dict['wp'].mainPage().close_modal(1)
    
    # 測試-分享網址功能
    @DecorateClass('CHATAPP-T1798')
    def test_share_url(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_share_page()
        share_url = self.function_dict['wp'].sharePage().get_share_link()
        self.function_dict['wp'].mainPage().close_modal(2)

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_message(share_url)
        self.function_dict['wp'].chatroomPage().check_url_message(share_url)

    # 測試-進入關於聊天頁面
    @DecorateClass('CHATAPP-T1799')
    def test_into_about(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_about_page()
        self.function_dict['wp'].mainPage().close_modal(1)
    
    # 測試-更改個人暱稱
    @DecorateClass('CHATAPP-T1800')
    def test_change_nickname(self):
        self.test_web_login()
        self.function_dict['wp'].mainPage().open_user_info()
        preset_name = self.function_dict['wp'].mainPage().get_user_info(self.web_account)
        self.function_dict['wp'].mainPage().change_nickname(preset_name, 'testaaaa')
        self.function_dict['wp'].mainPage().change_nickname('testaaaa', preset_name)

    #測試-訊息通知開關
    @DecorateClass('CHATAPP-T1801')
    def test_notify_switch(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_notification_page()
        self.function_dict['wp'].notificationPage().check_header_text()
        self.function_dict['wp'].notificationPage().check_switch_logic()

    #測試-關於聊天
    @DecorateClass('CHATAPP-T1802')
    def test_about_terms(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_about_page()
        self.function_dict['wp'].aboutPage().check_service(self.brand)
        self.function_dict['wp'].aboutPage().check_privacy()

    #測試-新增好友
    @DecorateClass('CHATAPP-T1803')
    def test_add_friend(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_friend_add()
        self.function_dict['wp'].mainPage().add_friend(8613542600999)
        self.function_dict['wp'].mainPage().close_modal(2)
        self.function_dict['wp'].friendPage().check_friend('test1234')

    #測試-好友暱稱
    @DecorateClass('CHATAPP-T1804')
    def test_friend_remark(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().switch_tab_to('好友')
        self.function_dict['wp'].friendPage().check_show_btn()
        self.function_dict['wp'].friendPage().search_friend('test1234')
        self.function_dict['wp'].friendPage().into_chatroom()
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().friend_nickname()
        self.function_dict['wp'].chatroomPage().friend_remark()

    #測試-好友黑名單
    @DecorateClass('CHATAPP-T1805')
    def test_block_friend(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().friend_block()
        self.function_dict['wp'].mainPage().switch_tab_to('好友')
        self.function_dict['wp'].friendPage().check_notexist('test1234')

    # 測試-好友黑名單設定
    @DecorateClass('CHATAPP-T1806')
    def test_block_setting(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_black_page()
        self.function_dict['wp'].blackPage().into_blocker('test1234')
        self.function_dict['wp'].blackPage().check_block_info('test1234')

    # 測試-解除好友黑名單
    @DecorateClass('CHATAPP-T1807')
    def test_unblock_friend(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().into_friend_add()
        self.function_dict['wp'].mainPage().search_member('test1234')
        self.function_dict['wp'].mainPage().unblock_member()

    # 測試-個人發送文字超連結訊息
    @DecorateClass('CHATAPP-T1808')
    def test_send_message(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['wp'].chatroomPage().send_url_message()
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-個人訊息複製
    @DecorateClass('CHATAPP-T1809')
    def test_message_copy(self):
        self.test_web_login()
        
        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_copy('測試TeSt12345!@#$%测试#0')
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-個人訊息回覆
    @DecorateClass('CHATAPP-T1810')
    def test_message_reply(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_reply('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-個人訊息回覆後撤回
    @DecorateClass('CHATAPP-T1926')
    def test_message_reply_revoke(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_message('測試撤回使用訊息')
        self.function_dict['wp'].chatroomPage().message_reply('測試撤回使用訊息')
        self.function_dict['wp'].chatroomPage().message_revoke('測試撤回使用訊息')
        self.function_dict['wp'].chatroomPage().check_reply_disappear('測試撤回使用訊息')
        
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-個人訊息撤回
    @DecorateClass('CHATAPP-T1811')
    def test_message_revoke(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#5')
        # self.function_dict['wp'].chatlistPage().check_last_message() // web 尚未有列表最後一筆屏蔽系統功能

    # 測試-個人訊息設置公告
    @DecorateClass('CHATAPP-T1812')
    def test_message_pin(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().delete_all_pin()
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_copy('測試TeSt12345!@#$%测试#5')
        self.function_dict['wp'].chatroomPage().pin_full_messages()
        self.function_dict['wp'].chatroomPage().delete_all_pin()

    # 測試-個人訊息設置公告後回覆
    @DecorateClass('CHATAPP-T1813')
    def test_message_pin_reply(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_reply('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatroomPage().message_pin('回覆訊息測試Test')
        self.function_dict['wp'].chatroomPage().delete_all_pin()
    
    # 測試-個人訊息設置公告後撤回
    @DecorateClass('CHATAPP-T1814')
    def test_message_pin_revoke(self):
        self.test_web_login()
        
        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().delete_all_pin()
        self.function_dict['wp'].chatroomPage().pin_full_messages()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#4')
        self.function_dict['wp'].chatroomPage().delete_all_pin()

    # 測試-群組發送文字超連結訊息
    @DecorateClass('CHATAPP-T1815')
    def test_send_message_group(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['wp'].chatroomPage().send_url_message()
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-群組訊息複製
    @DecorateClass('CHATAPP-T1816')
    def test_message_copy_group(self):
        self.test_web_login()
        
        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_copy('測試TeSt12345!@#$%测试#0')
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-群組發訊息回覆
    @DecorateClass('CHATAPP-T1817')
    def test_message_reply_group(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_reply('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatlistPage().check_last_message()

    # 測試-群組訊息撤回
    @DecorateClass('CHATAPP-T1818')
    def test_message_revoke_group(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatlistPage().check_last_message()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#5')
        # self.function_dict['wp'].chatlistPage().check_last_message() // web 尚未有列表最後一筆屏蔽系統功能

    # 測試-群組訊息設置公告
    @DecorateClass('CHATAPP-T1819')
    def test_message_pin_group(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().delete_all_pin()
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_copy('測試TeSt12345!@#$%测试#5')
        self.function_dict['wp'].chatroomPage().pin_full_messages()
        self.function_dict['wp'].chatroomPage().delete_all_pin()

    # 測試-群組訊息設置公告後回覆
    @DecorateClass('CHATAPP-T1820')
    def test_message_pin_reply_group(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().message_reply('測試TeSt12345!@#$%测试#3')
        self.function_dict['wp'].chatroomPage().message_pin('回覆訊息測試Test')
        self.function_dict['wp'].chatroomPage().delete_all_pin()
    
    # 測試-群組訊息設置公告後撤回
    @DecorateClass('CHATAPP-T1821')
    def test_message_pin_revoke_group(self):
        self.test_web_login()
        
        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().send_text_message()
        self.function_dict['wp'].chatroomPage().delete_all_pin()
        self.function_dict['wp'].chatroomPage().pin_full_messages()
        self.function_dict['wp'].chatroomPage().message_revoke('測試TeSt12345!@#$%测试#4')

    # 測試-刪除好友
    @DecorateClass('CHATAPP-T1822')
    def test_delete_friend(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().switch_tab_to('好友')
        self.function_dict['wp'].friendPage().check_show_btn()
        self.function_dict['wp'].friendPage().search_friend('test1234')
        self.function_dict['wp'].friendPage().into_chatroom()
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().friend_delete()
        self.function_dict['wp'].friendPage().check_notexist('test1234')

    # 測試-訊息表情符號
    @DecorateClass('CHATAPP-T1937')
    def test_message_emoji(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room('test1234')
        self.function_dict['wp'].chatroomPage().send_message('表情符號使用訊息')
        self.function_dict['wp'].chatroomPage().add_message_emoji('表情符號使用訊息')

    # 測試-建立群組
    @DecorateClass('CHATAPP-T1938')
    def test_groups_biuld(self):
        self.test_web_login()

        self.function_dict['wp'].mainPage().open_user_info()
        self.function_dict['wp'].mainPage().check_groups_biuld()
        self.function_dict['wp'].mainPage().groups_biuld(self.web_account, self.group_name)
        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatlistPage().check_group_build(self.web_account, self.group_name)

    # 測試-變更群組名稱
    @DecorateClass('CHATAPP-T1939')
    def test_group_name_change(self):
        self.test_web_login()

        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().change_group_name(self.group_name, 'name_test')
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().change_group_name('name_test', self.group_name)

    # 測試-變更群組權限設定
    @DecorateClass('CHATAPP-T1940')
    def test_group_rule_all(self):
        self.test_web_login()
        
        self.function_dict['wp'].chatlistPage().into_chat_room(self.group_name)
        self.function_dict['wp'].chatroomPage().into_setting()
        self.function_dict['wp'].chatroomPage().all_group_rule()




    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method
