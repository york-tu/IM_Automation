import os
import random
import sys
import re
from datetime import datetime
from time import sleep
import time

from Project.chat.web.pages.pages import Web2Pages, AdminPages
from Project.chat.web.testcase.base_testcase import BaseTestCase

from common.utils.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass


class Web2TestCase(BaseTestCase):
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
        current_web2_version = cls.function_dict['web2.0'].web2_main_page().return_web2_version()  # 獲取web2.0版本號
        gl.set_value('APP_VERSION', current_web2_version)

        brand = gl.get_value('BRAND') or ''
        cls.brand = brand.strip().lower()
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
        self.function_dict['web2.0'].base_page().windows_to_top(full=True)  # 切換視窗
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
        for function in cls.function_dict.values():
            function.base_page().quit_browser()
            num += 1

            if num == len(cls.driver_list):
                cls.driver_list = []
                break

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        wd = web_dr.WebDriver()
        cls.setting_test_data()  # 設定測試數據
        cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
        cls.function_dict['web2.0'] = Web2Pages(cls.driver_list[-1], cls.wait_time, cls.web2_url, cls.skipTest)  # 導入Web2.0全部頁面
        cls.function_dict['web2.0'].base_page().hide_windows()

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
    @DecorateClass('CHATAPP-T3471')
    def test_web2_login(self):
        self.test_all_windows_mini()
        self.function_dict['web2.0'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['web2.0'].base_page().open_base_url()  # 開啟wap網頁
        if 'mail' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.web2_phone, self.web2_password, self.web2_nation)

    # ADMIN登入
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].base_page().windows_to_top()  # 切換視窗
        self.function_dict['ad'].base_page().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].login_page().login(self.admin_account, self.admin_password)  # 登入admin

    # 登出
    @DecorateClass('CHATAPP-T3473')
    def test_web2_logout(self):
        self.function_dict['web2.0'].base_page().open_base_url()
        if not self.function_dict['web2.0'].web2_login_page().check_login_status():
            self.test_web2_login()
        self.function_dict['web2.0'].web2_first_page().switch_post_display_mode(1)
        self.function_dict['web2.0'].web2_login_page().logout()

    # 更改自己暱稱 & 個人簡介
    @DecorateClass('CHATAPP-T3474')
    def test_change_nickname_and_instructions(self):
        self.test_web2_login()
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        original_nickname = self.function_dict['web2.0'].web2_main_page().get_nickname()
        original_descriptions = self.function_dict['web2.0'].web2_main_page().get_descriptions().rstrip()
        self.function_dict['web2.0'].web2_main_page().change_nickname('gutest1234')
        self.function_dict['web2.0'].web2_main_page().change_nickname(original_nickname)
        self.function_dict['web2.0'].web2_main_page().change_descriptions('Web2.0ChangeDescriptionsTest')
        self.function_dict['web2.0'].web2_main_page().change_descriptions(original_descriptions)

    @DecorateClass('CHATAPP-T3475')
    def test_social_post_photo(self):
        self.test_web2_login()
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.web2_account

        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'web2.0自動化{self.brand}Test_發布photo_{current_time}'

        self.function_dict['web2.0'].web2_main_page().select_media(media_type='photo')
        self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description)
        self.function_dict['web2.0'].web2_main_page().check_post(account, description)

    @DecorateClass('CHATAPP-T3476')
    def test_social_post_video(self):
        self.test_web2_login()
        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.web2_account

        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'web2.0自動化{self.brand}Test_發布video_{current_time}'

        self.function_dict['web2.0'].web2_main_page().select_media(media_type='video')
        self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description)
        self.function_dict['web2.0'].web2_main_page().check_post(account, description)

    # 搜索視頻 & 用戶
    @DecorateClass('CHATAPP-T3477')
    def test_social_search(self):
        self.test_web2_logout()

        if self.env == 'uat':
            poster_phone_list = ['13542600001', '13542600002']
            poster_nickname_list = ['gubot01', 'gubot02']
        else:
            poster_phone_list = ['9016000202', '9016000203']
            poster_nickname_list = ['gutest002', 'gutest03']

        description_list = []

        for poster_phone, poster_nickname in zip(poster_phone_list, poster_nickname_list):
            self.function_dict['web2.0'].base_page().open_base_url()  # 開啟wap網頁
            self.function_dict['web2.0'].web2_login_page().login(poster_phone, self.wap_password, self.web_nation)
            # ========================== gubot01 & gubot02 依序發布貼文 ==================================================
            current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            description = f'Web2.0_{self.brand}_SearchTest_{current_time}'
            description_list.append(description)

            self.function_dict['web2.0'].web2_main_page().select_media(media_type='video')
            self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description)
            self.function_dict['web2.0'].web2_main_page().check_post(poster_nickname, description)
            self.test_web2_logout()
        # ========================== gubot04 or gubotmail01 登入 ========================================================
        if 'mail' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.wap_phone, self.wap_password, self.wap_nation)
        # ========================== 1. 搜索頁: 輸入01貼文說明01 > 點搜索鍵 >>> 搜索結果-視頻頁 ===============================
        self.function_dict['web2.0'].web2_search_page().search_post(description_list[0])
        self.function_dict['web2.0'].web2_search_page().check_search_post_result(poster_nickname_list[0], description_list[0])
        # ========================== 2. 搜索視頻結果頁: 輸入02貼文說明02 > 點搜索鍵 >>> 搜索結果-視頻頁 =========================
        self.function_dict['web2.0'].web2_search_page().search_post(description_list[1])
        self.function_dict['web2.0'].web2_search_page().check_search_post_result(poster_nickname_list[1], description_list[1])
        # ========================== 3. 搜索視頻結果頁: 輸入01 > 點"用戶"頁籤 > 點搜索鍵 >>> 切換到用戶頁並立即搜索 ========================
        self.function_dict['web2.0'].web2_search_page().search_poster(poster_nickname_list[0])
        self.function_dict['web2.0'].web2_search_page().check_search_poster_result(poster_nickname_list[0])
        # ========================== 4. 搜索用戶結果頁: 輸入02 > 點搜索鍵 >>> 搜索結果-用戶頁 =================================
        self.function_dict['web2.0'].web2_search_page().search_poster(poster_nickname_list[1])
        self.function_dict['web2.0'].web2_search_page().check_search_poster_result(poster_nickname_list[1])
        # ========================== 5. 搜索用戶結果頁: 輸入02貼文說明02 > 點"視頻"頁籤 > 點搜索鍵 >>> 立即搜索 ===========================
        self.function_dict['web2.0'].web2_search_page().search_post(description_list[1])
        self.function_dict['web2.0'].web2_search_page().check_search_post_result(poster_nickname_list[1], description_list[1])
        # ========================== 確認搜索紀錄頁 =======================================================================
        self.function_dict['web2.0'].web2_search_page().check_recent_search_record(
            [description_list[1], poster_nickname_list[1],
             poster_nickname_list[0], description_list[0]])

    # 關注 & 取消關注
    @DecorateClass('CHATAPP-T3478')
    def test_social_follow_unfollow(self):
        member = self.operate_account
        self.test_web2_login()
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self_counts = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得自己主頁關注數

        # ============================ 關注對方 ====================================
        # ==== 對方[主頁]粉絲數+1 ===============
        others_count_fans = self.function_dict['web2.0'].web2_main_page().follow_member_from_main_page(member, self.web2_account)  # 關注對方 >>> 確認對方粉絲數+1,"已關注"鍵, 回傳對方目前粉絲數
        # ==== 對方[粉絲列表]粉絲數+1 & 出現我 ====
        self.function_dict['web2.0'].web2_main_page().check_fans_list(self.web2_account, others_count_fans)
        # ==== 自己[主頁]關注數+1 ===============
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self_counts_1 = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得自己主頁關注數
        assert int(self_counts_1[0]) == int(self_counts[0]) + 1  # 確認自己主頁關注數+1
        # ==== 自己[關注列表]關注數+1 ============
        self.function_dict['web2.0'].web2_main_page().check_followed_list(member, self_counts_1[0])  # 確認關注列表: 關注數+1, 對方出現在列表上

        # ============================ 取消關注對方 ==================================
        # ==== 自己[關注列表]關注數-1 =============
        self.function_dict['web2.0'].web2_main_page().unfollow_first_member_from_followed_list(member)  # 取消關注對方 >>> 確認自己關注頁籤數-1, "關注"鍵
        # ==== 自己[主頁]關注數-1  ================
        self_counts_2 = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得自己主頁關注數
        assert int(self_counts_2[0]) == int(self_counts_1[0]) - 1  # 確認自己主頁關注數-1
        # ==== 自己[關注列表]不出現對方 =============
        assert not self.function_dict['web2.0'].web2_main_page().check_list_first_member(member, self_counts_2[0], '0')  # 關注列表上不出現對方
        # ==== 對方[主頁]粉絲數-1 ==================
        self.function_dict['web2.0'].web2_main_page().search_user(member)
        others_counts = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁粉絲數
        assert int(others_counts[1]) == int(others_count_fans) - 1  # 確認他人主頁粉絲數-1
        # ==== 對方[粉絲列表]粉絲數-1 & 不出現我 ======
        assert not self.function_dict['web2.0'].web2_main_page().check_list_first_member(member, others_counts[1], '1')

    # 他人貼文上評論: 我留言+回覆 > 創作者端確認留言+回覆
    @DecorateClass('CHATAPP-T3479')
    def test_social_other_post_add_comments_reply(self):
        self.test_web2_logout()
        self.test_web2_login()
        current_time = datetime.now().strftime("%H:%M")
        comment = f'Web2.0_{self.web2_account}留言Test_{current_time}'
        reply_comment = f'Web2.0_{self.web2_account}回覆{self.web2_account}留言test_{current_time}'

        # ============================ 我(gubot05/gubotmail01) 在 他人(gubot02) 的貼文上"留言"+"回覆"========================
        self.function_dict['web2.0'].web2_main_page().search_user(self.web_account)  # 進到gubot02主頁
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().post_add_comment(self.web2_account, comment, post_url=False, self_post=False)  # 留言+確認留言相關
        self.function_dict['web2.0'].web2_social_page().post_recent_comment_add_reply(self.web2_account, self.web2_account, reply_comment,self_post=False)  # 回覆留言+確認回覆相關

        # ============================ 他人(gubot02) 在 他的"第一則公開貼文"上確認"最新一則留言" & "回覆訊息" ===================
        self.test_web2_logout()
        self.function_dict['web2.0'].web2_login_page().login(self.web_phone, self.web_password, self.web_nation)
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().check_post_recent_comment(comment, self.web2_account)  # 確認出現稍早我(gubot05/gubotmail01)的留言
        self.function_dict['web2.0'].web2_social_page().check_post_recent_reply(reply_comment, self.web2_account)  # 確認出現稍早我(gubot05/gubotmail01)的回覆留言

    # 自己貼文上評論: 我(創作者)留言+回覆 > 他人留言+回覆 > 他人點贊 > 我點贊
    @DecorateClass('CHATAPP-T3480')
    def test_social_self_post_add_comments_reply_like(self):
        current_time = datetime.now().strftime("%H:%M")
        comment = f'Web2.0_[我]留言test_{current_time}'
        reply_comment = f'Web2.0_[我]回覆[我]母留言test_{current_time}'
        reply_reply_comment = f'Web2.0_[他人]回覆[我]子留言test_{current_time}'
        self.test_web2_logout()
        self.test_web2_login()
        # ============================ 我(gubot05/gubotmail01) 在 我的第一則公開貼文上"留言" =================================
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().post_add_comment(self.web2_account, comment, post_url=False, self_post=True)  # 留言+確認留言相關
        # ============================ 我(gubot05/gubotmail01) 在 我的貼文最新自己留言上"回覆留言" ===========================
        self.function_dict['web2.0'].web2_social_page().post_recent_comment_add_reply(self.web2_account, self.web2_account, reply_comment, self_post=False)  # 回覆留言+確認回覆相關
        # ============================ 他人(gubot02) 在 我(gubot05/gubotmail01) 的第一則公開貼文上確認最新一則留言&回覆訊息 ======
        self.test_web2_logout()
        self.function_dict['web2.0'].web2_login_page().login(self.web_phone, self.web_password, self.web_nation)
        self.function_dict['web2.0'].web2_main_page().search_user(self.web2_account)  # 進到我(gubot05)主頁
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().check_post_recent_comment(comment, self.web2_account)  # 確認出現稍早我(gubot05/gubotmail01)的留言
        self.function_dict['web2.0'].web2_social_page().check_post_recent_reply(reply_comment, self.web2_account)  # 確認出現稍早我(gubot05/gubotmail01)的回覆留言

        # ============================ 他人(gubot02) 在 我(gubot05/gubotmail01) 該貼文最新留言(母留言)的最新回覆訊息(子留言)上"回覆" ====================
        self.function_dict['web2.0'].web2_social_page().post_recent_comment_recent_reply_add_reply(self.web2_account, self.web_account, reply_reply_comment, self_post=False)
        # ============================ 他人(gubot02) 在 我(gubot05/gubotmail01) 該則貼文最新留言(母留言)與最新回覆訊息(子留言)上"點贊" ====================
        recent_comment_after_add_liked_counts = self.function_dict['web2.0'].web2_social_page().post_recent_comment_add_like()
        recent_reply_after_add_liked_counts = self.function_dict['web2.0'].web2_social_page().post_recent_reply_add_like()
        # ============================ 我(gubot05/gubotmail01) 在 我 該則貼文上確認最新留言(母留言)與最新回覆訊息(子留言)的"贊數" ================
        self.test_web2_logout()
        self.test_web2_login()
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)

        assert self.function_dict['web2.0'].web2_social_page().check_recent_comment_liked_counts() == recent_comment_after_add_liked_counts
        assert self.function_dict['web2.0'].web2_social_page().check_recent_reply_liked_counts() == recent_reply_after_add_liked_counts
        # ============================ 我(gubot05/gubotmail01) 在 我 該則貼文上最新留言(母留言)與最新回覆訊息(子留言)上"點贊" ====================
        self.function_dict['web2.0'].web2_social_page().post_recent_comment_add_like()
        self.function_dict['web2.0'].web2_social_page().post_recent_reply_add_like()

    # 貼文點贊+收藏
    @DecorateClass('CHATAPP-T3481')
    def test_social_post_add_remove_likes_collections(self):
        # ============================ 他人(gubot02) 發布貼文 ===============================
        self.test_web2_logout()
        self.function_dict['web2.0'].web2_login_page().login(self.web_phone, self.web_password, self.web_nation)

        account = ''
        if 'mail' in self.account_type.lower():
            account = self.mail_account
        elif 'phone' in self.account_type.lower():
            account = self.web_account

        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'Web2.0_自動化{self.brand}Test_貼文點贊收藏_{current_time}'

        self.function_dict['web2.0'].web2_main_page().select_media(media_type='photo')
        self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description)
        self.function_dict['web2.0'].web2_main_page().check_post(account, description)

        # ============================ 他人(gubot02) 對 他人(gubot02) 貼文點贊 ======================
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        others_counts = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁關注數/粉絲數/點贊數
        self.function_dict['web2.0'].web2_social_page().first_post_add_remove_like()  # 點贊第一則貼文

        others_counts_after = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁關注數/粉絲數/點贊數
        assert int(others_counts_after[2]) == int(others_counts[2]) + 1, '贊數未正確更新'  # 確認主頁贊數+1
        # ----------- 確認該貼文出現在已贊媒體櫃 -----------
        self.function_dict['web2.0'].web2_main_page().into_likes_library()
        assert self.function_dict['web2.0'].web2_main_page().check_post(account, description, is_post=False)

        # ============================ 我(gubot05/gubotmail01) 對 他人(gubot02) 貼文點贊 ======================
        # ----------- 登入"我的"帳號 -----------
        self.test_web2_logout()
        if 'mail' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.mail_address, self.mail_password, login_method='mail')
        elif 'phone' in self.account_type.lower():
            self.function_dict['web2.0'].web2_login_page().login(self.wap_phone, self.wap_password, self.wap_nation)
        # ------------------------------------
        self.function_dict['web2.0'].web2_main_page().search_user(self.web_account)  # 進到他人(gubot02)主頁
        others_counts = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁關注數/粉絲數/點贊數
        self.function_dict['web2.0'].web2_social_page().first_post_add_remove_like()  # 在他人第一則貼文上點贊
        # ----------- 確認他人主頁贊數+1 -----------
        self.function_dict['web2.0'].web2_main_page().search_user(self.web_account)
        others_counts_after = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁關注數/粉絲數/點贊數
        assert int(others_counts_after[2]) == int(others_counts[2]) + 1, '贊數未正確更新'  # 確認主頁贊數+1
        # ----------- 確認"他人"貼文出現在"我"已贊媒體櫃 -----------
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self.function_dict['web2.0'].web2_main_page().into_likes_library()
        assert self.function_dict['web2.0'].web2_main_page().check_post(account, description, is_post=False)

        # ============================ 我(gubot05/gubotmail01) 對 他人(gubot02) 貼文取消贊 ======================
        self.function_dict['web2.0'].web2_main_page().into_likes_library()
        self.function_dict['web2.0'].web2_social_page().first_post_add_remove_like(is_add=False)  # 第一則貼文上取消點贊
        # ----------- 確認"他人"貼文從"我"已贊媒體櫃移除 -----------
        self.function_dict['web2.0'].web2_main_page().into_public_library()
        self.function_dict['web2.0'].web2_main_page().into_likes_library()
        assert not self.function_dict['web2.0'].web2_main_page().check_post(account, description, is_post=False)
        # ----------- 確認他人主頁贊數-1 -----------
        self.function_dict['web2.0'].web2_main_page().search_user(self.web_account)  # 進到他人(gubot02)主頁
        others_counts_after_dislike = self.function_dict['web2.0'].web2_main_page().get_social_data()  # 取得他人主頁關注數/粉絲數/點贊數
        assert int(others_counts_after_dislike[2]) == int(others_counts_after[2]) - 1, f'取消對方贊後, 對方主頁贊數沒有-1'

        # ============================ 我(gubot05/gubotmail01) 對 他人(gubot02) 貼文進行收藏 ====================
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().post_add_remove_collect()  # 在他人剛發的貼文上點收藏
        self.function_dict['web2.0'].web2_main_page().into_main_page()
        self.function_dict['web2.0'].web2_main_page().into_collect_library()
        # ----------- 確認"他人"貼文出現在"我"收藏媒體櫃 -----------
        assert self.function_dict['web2.0'].web2_main_page().check_post(account, description, is_post=False)

        # ============================ 我(gubot05/gubotmail01) 對 他人(gubot02) 貼文取消收藏 ====================
        self.function_dict['web2.0'].web2_social_page().into_post_comment_page(1)
        self.function_dict['web2.0'].web2_social_page().post_add_remove_collect(is_add=False)  # 在我收藏櫃取消收藏該貼文
        self.function_dict['web2.0'].web2_main_page().into_public_library()
        self.function_dict['web2.0'].web2_main_page().into_collect_library()
        # ----------- 確認"他人"貼文從"我"收藏媒體櫃移除 -----------
        assert not self.function_dict['web2.0'].web2_main_page().check_post(account, description, is_post=False)

    # 發布不同隱私權限貼文 > 確認不同關注狀態用戶觀看
    @DecorateClass('CHATAPP-T3482')
    def test_social_post_with_different_privacy(self):
        self.function_dict['web2.0'].web2_login_page().login(self.app_phone, self.app_password, self.app_nation)

        # ================= gubot03 依序發布 所有人 > 互關 > 粉絲 > 僅自己 4則貼文 ===========================================
        privacy_list = [0, 1, 2, 3]  # 隱私設置: 0所有人, 1互關, 2粉絲, 3僅自己
        privacy_description_list = ['所有人', '互關', '粉絲', '僅自己']
        media_list = ['video', 'photo']
        description_list = []
        for privacy_index in privacy_list:
            current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            media_type = random.choice(media_list)
            description = f'Web2.0自動化{self.brand}Test_{media_type}_{privacy_description_list[privacy_index]}_{current_time}'
            description_list.append(description)

            self.function_dict['web2.0'].web2_main_page().select_media(media_type)
            self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description, privacy_index)
            # self.function_dict['web2.0'].web2_main_page().check_post(self.app_account, description)

        # ================= 互關成員 gubot04/05/06 觀看貼文確認 ============================================================
        # 定義每個帳號的 media_type 和 privacy_index
        if self.env == 'uat':
            account_list = ['13542600004', '13542600005', '13542600006']
        else:
            account_list = ['9016000203', '9016000204', '9016000205']  # 正式環境

        account_checks = {
            account_list[0]: {'media_index': [0, 1, 2], 'privacy_index': [2, 1, 0]},  # 04看到貼文順序: 粉絲貼文 > 互關貼文 > 所有人貼文
            account_list[1]: {'media_index': [0, 1], 'privacy_index': [2, 0]},  # 05看到貼文順序: 粉絲貼文 > 所有人貼文
            account_list[2]: {'media_index': [0], 'privacy_index': [0]},  # 06看到貼文順序: 所有人貼文
        }

        # 定義執行檢查的函數
        def check_media_for_user(_account, descriptions, _media_index, _privacy_index):
            self.test_web2_logout()
            self.function_dict['web2.0'].web2_login_page().login(account, self.app_password, self.app_nation)
            self.function_dict['web2.0'].web2_main_page().search_user(self.app_account)

            # 使用 zip 遍歷 media_type 和 privacy_index 的配對
            for zip_media_index, zip_privacy_index in zip(_media_index, _privacy_index):
                _description = descriptions[zip_privacy_index]  # 根據 privacy_index 取 description
                self.function_dict['web2.0'].web2_main_page().check_post(self.app_account, _description, False, zip_media_index)

        # 迴圈遍歷每個 account 並執行對應的檢查
        for account, checks in account_checks.items():
            media_index = checks['media_index']
            privacy_index = checks['privacy_index']
            check_media_for_user(account, description_list, media_index, privacy_index)

    # 測試 - (後台)變更發布者gubot06自動審核權限 > (前台)發布媒體 > (後台)確認媒體審核狀態
    @DecorateClass('CHATAPP-T3483')
    def test_social_change_poster_auto_audit_type(self):
        self.test_web2_logout()

        audit_type_list = [2, 0, 1]  # 2:黑名單, 0:一般會員, 1:白名單
        # ============ 將發布者自動審核權限設為不同權限後確認貼文狀態 ====================================
        for audit_type in audit_type_list:
            # ---------- 後台"自動審核"設定發布帳號審核權限 ----------
            self.test_admin_login()
            self.function_dict['ad'].social_management_page().into_auto_audit_page()
            self.function_dict['ad'].social_management_page().set_audit_privacy(self.web2_account, audit_type)
            # ---------- 前台發布貼文 ----------
            self.test_web2_login()
            instructions = self.photo_post(audit_type)
            # ---------- 後台"媒體審核"確認貼文審核狀態 ----------
            self.test_admin_login()
            self.function_dict['ad'].social_management_page().into_media_audit_page()
            self.function_dict['ad'].social_management_page().search_audit_result(self.web2_account, instructions, audit_type)

    def photo_post(self, audit_type):
        if audit_type == 1:
            _type = '白名单'
        elif audit_type == 2:
            _type = '黑名单'
        else:
            _type = '一般会员'
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        description = f'Web2.0_自動審核_{self.brand}_{_type}_{current_time}'

        self.function_dict['web2.0'].web2_main_page().select_media(media_type='photo')
        self.function_dict['web2.0'].web2_main_page().into_post_settings_and_confirm(description, privacy=0)

        sleep(5)
        return description

    # email註冊帳號 > 登出 > 登入 > 登出
    @DecorateClass('CHATAPP-T3472')
    def test_web2_email_registration(self):
        email = 'qa5@tengyuntech.com'
        pw = "000111abc"
        # ============== 後台"關閉"極驗 =======================================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(False)
        # ============== email註冊帳號 =======================================================
        self.test_web2_logout()
        self.function_dict['web2.0'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['web2.0'].base_page().open_base_url()  # 開啟web2.0網頁
        self.function_dict['web2.0'].web2_login_page().register_by_email(self.mail_account_id, email, pw)
        # =============== 登出後再登入 ================
        self.test_web2_logout()
        self.function_dict['web2.0'].base_page().windows_to_top(full=True)  # 切換視窗
        self.function_dict['web2.0'].base_page().open_base_url()  # 開啟web2.0網頁
        self.function_dict['web2.0'].web2_login_page().login(email, pw, login_method='mail')
        # ============== 後台"開啟"極驗 =======================================================
        self.test_admin_login()
        self.function_dict['ad'].main_page().into_system_app_setting()
        self.function_dict['ad'].main_page().enable_geetest(True)
        # ============== 後台刪除該帳號 ========================================================
        self.function_dict['ad'].main_page().into_member_list()
        self.function_dict['ad'].member_page().delete_member(self.mail_account_id)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method
