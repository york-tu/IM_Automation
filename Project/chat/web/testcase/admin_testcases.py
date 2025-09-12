import random
import sys
import datetime
import re
import time

from Project.chat.web.pages.pages import WebPages, AdminPages
from Project.chat.web.testcase.base_testcase import BaseTestCase

from Project.lottery.web.Utils_folder.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass


class AdminTestCase(BaseTestCase):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    chrome_crash = 0
    folder_path = ''
    function_dict = {}
    driver_list = []
    build_time = []
    revise_time = []
    brand = gl.get_value('BRAND')
    # member_ID = datetime.datetime.now().strftime("%yy%m%d%H%M")
    manual_account_id = f'm{datetime.datetime.now().strftime("%m%d%H%M%S")}'

    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folder_path = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        admin_version = cls.function_dict['ad'].mainPage().return_admin_version()  # 獲取web版本號
        gl.set_value('APP_VERSION', admin_version)

    def setUp(self):
        for key, function in self.function_dict.items():
            try:
                function.basePage().accept_alert()
                function.basePage().dismiss_alert()
            except:
                pass

            function.basePage().switch_home_page()

        self.test_all_windows_mini()
        self.function_dict['wp'].basePage().windows_to_top()  # 切換視窗
        self.start_time = time.time()

    def tearDown(self):
        self.test_all_windows_max()
        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folder_path}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

    @classmethod
    def tearDownClass(cls):
        num = 0
        for function in cls.function_dict.values():
            function.basePage().quit_browser()
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
        cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
        cls.function_dict['wp'].basePage().hide_windows()

        if not sys.argv[0].__contains__('prod'):
            cls.driver_list.append(wd.setting_driver(1900, 1000, cls.implicitly_wait_time, is_wap=False))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPages(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].basePage().hide_windows()

    @staticmethod
    def open_url(function, url):
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

    # 測試-ADMIN登入
    @DecorateClass('CHATAPP-T1886')
    def test_admin_login(self):
        self.function_dict['ad'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password) # 登入admin

    # 測試-WEB登入
    @DecorateClass('CHATAPP-T1790')
    def test_web_login(self):
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].loginPage().login(self.web_phone, self.web_password, self.web_nation)

    # 測試-進入會員列表並檢查頁面基本資訊
    @DecorateClass('CHATAPP-T1887')
    def test_into_and_check_member_list(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_member_list()
        self.function_dict['ad'].memberPage().check_member_list_page()

    # 測試-進入會員層級並檢查頁面基本資訊
    @DecorateClass('CHATAPP-T2740')
    def test_into_and_check_member_level(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_member_level()
        self.function_dict['ad'].memberPage().check_member_level_page()

    # 測試-進入群組列表
    @DecorateClass('CHATAPP-T1888')
    def test_into_and_check_groups_list(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_groups_list()
        self.function_dict['ad'].groupsPage().check_group_list_page()

    # 測試-進入群組設定
    @DecorateClass('CHATAPP-T1889')
    def test_into_groups_set(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_groups_set()

    # 測試-進入群組建立成員
    @DecorateClass('CHATAPP-T1890')
    def test_into_groups_own(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_groups_own()

    # 測試-進入群發消息
    @DecorateClass('CHATAPP-T3251')
    def test_into_groups_message(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_group_msg()

    # 測試-進入APP/Web维护
    @DecorateClass('CHATAPP-T1891')
    def test_into_system_maintenance(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_system_maintenance()

    # 測試-進入APP/Web设定, 並檢查会员添加好友tip, 檢查手機號搜索添加好友tip
    @DecorateClass('CHATAPP-T1892')
    def test_into_system_app_setting(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_system_app_setting()
        self.function_dict['ad'].mainPage().check_member_add_friend_tip()  # 檢查會員添加好友選項tip
        self.function_dict['ad'].mainPage().check_add_friend_by_search_phone_tip()  # 檢查手機號搜索添加好友tip

    # 測試-APP/Web设定-關閉極驗
    @DecorateClass('CHATAPP-')
    def test_system_app_setting_geetest_off(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_system_app_setting()
        self.function_dict['ad'].mainPage().enable_geetest(False)

    # 測試-APP/Web设定-開啟極驗
    @DecorateClass('CHATAPP-')
    def test_system_app_setting_geetest_on(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_system_app_setting()
        self.function_dict['ad'].mainPage().enable_geetest(True)

    # 測試 - 後台登入不同權限帳號, 確認對應'好友添加白名单设定'頁顯示與不顯示
    @DecorateClass('CHATAPP-T2539')
    def test_into_system_contact_whitelist_setting(self):
        self.test_admin_login()
        self.function_dict['ad'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].loginPage().logout()
        self.function_dict['ad'].loginPage().login(self.low_rights_adm_id, self.low_rights_adm_pwd)  # 登入無新增好友權限admin帳號
        assert not self.function_dict['ad'].mainPage().system_contact_whitelist_setting_show()  # 確認不顯示好友添加白名单设定頁
        self.function_dict['ad'].loginPage().logout()
        self.test_admin_login()  # 登入full權限admin帳號
        self.function_dict['ad'].mainPage().into_system_contact_whitelist_setting() # 確認顯示好友添加白名单设定頁

    # 測試 - 後台登入不同權限帳號, 確認對應'邀請碼管理'頁顯示與不顯示
    @DecorateClass('CHATAPP-T2567')
    def test_into_share_code_setting(self):
        self.function_dict['ad'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].loginPage().logout()
        self.function_dict['ad'].loginPage().login(self.low_rights_adm_id,
                                                   self.low_rights_adm_pwd)  # 登入低權限帳號
        assert not self.function_dict['ad'].mainPage().share_code_management_show()  # 確認不顯示邀請碼管理頁
        self.function_dict['ad'].loginPage().logout()
        self.test_admin_login()  # 登入full權限admin帳號
        self.function_dict['ad'].mainPage().into_share_code()  # 確認進入邀請碼管理頁

    # 測試 - 後台新增邀請碼 > 刪除邀請碼
    @DecorateClass('CHATAPP-T2566')
    def test_add_share_code(self):
        share_code_sample = '123abc'
        self.test_admin_login()
        self.function_dict['ad'].mainPage().add_share_code(share_code_sample, 'AutoTestShareCode')
        self.function_dict['ad'].mainPage().delete_share_code(share_code_sample)

    # 測試-進入發現頁並確認可正常編輯網址, 開關切換
    @DecorateClass('CHATAPP-T2926')
    def test_into_discover_and_edit(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_discover_setting()
        self.function_dict['ad'].mainPage().disable_discover_function(3)
        self.function_dict['ad'].mainPage().restore_discover_function()
        self.function_dict['ad'].mainPage().edit_restore_discover_index0_url()

    # 測試-進入聊天纪录頁並確認紀錄
    @DecorateClass('CHATAPP-T1893')
    def test_into_record_check_chat_record(self):
        random_number = random.randint(1000000000, 9999999999)
        self.test_web_login()
        self.function_dict['wp'].chatlistPage().into_chat_room(self.operate_account)
        self.function_dict['wp'].chatroomPage().send_message(random_number)

        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_menu_recode()
        self.function_dict['ad'].recordPage().check_chat_record(self.web_account, random_number)

    # 測試-進入帳號管理
    @DecorateClass('CHATAPP-T1894')
    def test_into_setting_account(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_setting_account()

    # 測試-進入角色權限
    @DecorateClass('CHATAPP-T1895')
    def test_into_setting_role(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_setting_role()

    # 測試-進入OTP管理
    @DecorateClass('CHATAPP-T1896')
    def test_into_setting_otp(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_setting_otp()

    # 測試-進入運營OTP
    @DecorateClass('CHATAPP-T1897')
    def test_into_setting_otp_operation(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_setting_otp_operation()

    # 測試-進入操作日誌
    @DecorateClass('CHATAPP-T1898')
    def test_into_logging(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_logging()

    # 測試-進入紅包列表
    @DecorateClass('CHATAPP-T1899')
    def test_into_red_list(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_red_list()

    # 測試-進入積分使用紀錄
    @DecorateClass('CHATAPP-T1900')
    def test_into_red_integral(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_integral_record()

    # 測試-進入媒体审核
    @DecorateClass('CHATAPP-T2711')
    def test_into_media_audit(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_media_audit_page(first_enter=True)

    # 測試-進入自动审核
    @DecorateClass('CHATAPP-T2712')
    def test_into_auto_audit(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_auto_audit_page(first_enter=True)

    # 測試-進入屏蔽字詞
    @DecorateClass('CHATAPP-T2850')
    def test_into_block_words(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_block_words_page(first_enter=True)

    # 測試-進入检举内容
    @DecorateClass('CHATAPP-T2851')
    def test_into_impeach(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_impeach_page(first_enter=True)

    # 測試-進入贴文数据
    @DecorateClass('CHATAPP-T2852')
    def test_into_post_data(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_post_data_page(first_enter=True)

    # 測試-進入创作者数据
    @DecorateClass('CHATAPP-T2853')
    def test_into_creator_data(self):
        self.test_admin_login()
        self.function_dict['ad'].socialManagementPage().into_creator_data_page(first_enter=True)

    # 測試-進入水量控制
    @DecorateClass('CHATAPP-T1901')
    def test_into_red_water(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_red_water()

    # 測試-群組建立權限設定
    @DecorateClass('CHATAPP-T2507')
    def test_build_group_permission(self):
        bool_list = [False, True]
        for _bool in bool_list:
            self.test_admin_login()
            self.function_dict['ad'].mainPage().into_groups_set()
            self.function_dict['ad'].groupsPage().groups_build_switch(_bool)

            self.test_web_login()
            self.function_dict['wp'].mainPage().open_user_info()
            self.function_dict['wp'].mainPage().check_groups_build(_bool)

    # 測試-新增會員帳號
    # @DecorateClass('CHATAPP-T2508')
    # def test_member_build(self):
    #     self.test_into_and_check_member_list()
    #     self.function_dict['ad'].memberPage().build_account(self.member_ID)
    #     build_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    #     self.function_dict['ad'].memberPage().check_data(self.member_ID, build_time, self.revise_time, condition = 'confirm_build')

    # 測試-新增人工創建帳號
    @DecorateClass('CHATAPP-T2908')
    def test_manual_create_account(self):
        phone = '13141000999'
        password = '000111abc'
        self.test_into_and_check_member_list()
        self.function_dict['ad'].memberPage().manual_create_app_account(self.manual_account_id, phone, password)
        build_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        self.function_dict['ad'].memberPage().check_data(self.manual_account_id, build_time, self.revise_time, condition = 'confirm_manual_create')

        self.function_dict['wp'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].loginPage().login(phone, password, 'CN')

    # 測試-設定備註 
    @DecorateClass('CHATAPP-T2509')
    def test_member_revise_remark(self):
        time.sleep(1)
        self.test_into_and_check_member_list()
        time.sleep(1)

        self.function_dict['ad'].memberPage().revise_remark(self.manual_account_id)
        self.function_dict['ad'].memberPage().check_data(self.manual_account_id, self.build_time, self.revise_time, condition = 'confirm_base')

    # 測試-修改資料 
    @DecorateClass('CHATAPP-T2510')
    def test_member_change_data(self):
        time.sleep(1)
        self.test_into_and_check_member_list()
        time.sleep(1)

        self.function_dict['ad'].memberPage().member_change_data(self.manual_account_id)
        self.function_dict['ad'].memberPage().check_data(self.manual_account_id, self.build_time, self.revise_time, condition = 'confirm_base')

    # 測試-重製安全密碼
    @DecorateClass('CHATAPP-T2511')
    def test_member_reset_security_password(self):
        time.sleep(1)
        self.test_into_and_check_member_list()
        time.sleep(1)

        self.function_dict['ad'].memberPage().reset_security_password(self.manual_account_id)
        revise_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.function_dict['ad'].memberPage().check_data(self.manual_account_id, self.build_time, revise_time, condition = 'confirm_base')

    # 測試-變更密碼
    @DecorateClass('CHATAPP-T2512')
    def test_member_change_password(self):
        time.sleep(1)
        self.test_into_and_check_member_list()
        time.sleep(1)

        self.function_dict['ad'].memberPage().member_change_password(self.manual_account_id)
        revise_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        self.function_dict['ad'].memberPage().check_data(self.manual_account_id, self.build_time, revise_time, condition = 'confirm_revise')

    # 測試-搜尋功能
    @DecorateClass('CHATAPP-T2515')
    def test_member_search_function(self):
        self.test_into_and_check_member_list()
        self.function_dict['ad'].memberPage().search(self.manual_account_id)

    # 測試-刪除後台新增帳號
    @DecorateClass('CHATAPP-T2516')
    def test_member_delete(self):
        self.test_into_and_check_member_list()
        self.function_dict['ad'].memberPage().delete_member(self.manual_account_id)

    # @DecorateClass('')
    # def test_change_social_permission(self):
    #     self.test_into_and_check_member_list()
    #     self.function_dict['ad'].memberPage().change_social_permission(self.member_ID, enable=False)

    # 測試-刪除人工創建帳號
    @DecorateClass('CHATAPP-T2907')
    def test_manual_create_account_delete(self):
        self.test_into_and_check_member_list()
        self.function_dict['ad'].memberPage().delete_member(self.manual_account_id)

    # 測試-刪除群組
    @DecorateClass('CHATAPP-T2783')
    def test_group_delete(self):
        self.test_admin_login()
        self.function_dict['ad'].mainPage().into_groups_list()
        self.function_dict['ad'].groupsPage().groups_delete(self.get_group_name())

    def get_group_name(self):
        if self.env == 'prod':
            return 'QA_bot_only'
        elif self.env == 'uat':
            return str(datetime.datetime.now().strftime("%m%d") + "group")

    # 測試-順付成功積分紀錄
    @DecorateClass('CHATAPP-T2522')
    def test_exchange_success_recode(self):
        self.test_into_red_integral()
        self.function_dict['ad'].waterRecodePage().search_point_recode(condition='success')
        self.function_dict['ad'].waterRecodePage().check_exchange_recode(condition='success')

    # 測試-順付返還積分紀錄
    @DecorateClass('CHATAPP-T2523')
    def test_exchange_fail_recode(self):
        self.test_into_red_integral()
        self.function_dict['ad'].waterRecodePage().search_point_recode(condition='fail')
        self.function_dict['ad'].waterRecodePage().check_exchange_recode(condition='fail')

    # 測試-新增紅包
    @DecorateClass('CHATAPP-T2517')
    def test_add_redenvelope(self):
        # self.test_into_red_list()
        original_water = '99999999.99'
        operator = 'test1234'
        self.test_into_red_water()
        self.function_dict['ad'].waterControlPage().edit_point(operator, original_water)

        self.function_dict['ad'].mainPage().into_red_list()
        self.function_dict['ad'].redenvelopePage().add_redenvelope()

    # 測試-新增手氣紅包
    @DecorateClass('CHATAPP-T2518')
    def test_add_luck_redenvelope(self):
        self.test_into_red_list()
        self.function_dict['ad'].redenvelopePage().add_luck_redenvelope()


# 測試-檢查紅包詳情
    @DecorateClass('CHATAPP-T2519')
    def test_check_red_envelope(self):
        self.test_into_red_list()
        self.function_dict['ad'].redenvelopePage().redenvelope_detail(60)

    # 測試-檢查拚手氣紅包詳情
    @DecorateClass('CHATAPP-T2520')
    def test_check_luck_red_envelope(self):
        self.test_into_red_list()
        self.function_dict['ad'].redenvelopePage().luck_red_envelope_detail(60)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method

    # 新增一般紅包for自動領取測試
    @DecorateClass('')
    def add_auto_grad_red_envelope(self):
        original_water = '99999999.99'
        operator = 'test1234'
        self.test_into_red_water()
        self.function_dict['ad'].waterControlPage().edit_point(operator, original_water)
        self.function_dict['ad'].mainPage().into_red_list()
        self.function_dict['ad'].redenvelopePage().add_red_envelope_for_auto_grad()

    # 新增拚手氣紅包for自動領取測試 並 測試水量編輯&使用詳情
    @DecorateClass('CHATAPP-T2521')
    def add_auto_grad_luck_red_envelope_then_check_water_control(self):
        original_water = '99999999.99'
        operator = 'test1234'
        self.test_into_red_water()
        self.function_dict['ad'].waterControlPage().edit_point(operator, original_water)
        self.function_dict['ad'].mainPage().into_red_list()
        total_cost = self.function_dict['ad'].redenvelopePage().add_luck_red_envelope_for_auto_grad()
        operate_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        after_water = str(round((float(original_water) - float(total_cost)), 2))
        # 測試-水量編輯&使用詳情
        self.test_water_control(operator, operate_time, original_water, total_cost, after_water)

    # 測試-水量編輯&使用詳情
    def test_water_control(self, member_name, operate_time, original_water, total_cost, after_water):
        self.test_into_red_water()
        self.function_dict['ad'].waterControlPage().test_point_control_search(member_name)
        self.function_dict['ad'].waterControlPage().test_water_control_detail(operate_time, member_name, original_water, total_cost, after_water)


    # =================================================================================================================
    # 測試-sample
    @DecorateClass('')
    def test_testtest(self):
        self.function_dict['ad'].basePage().windows_to_top()  # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['ad'].loginPage().login('yorkbackend01', '000111abc')  # 登入admin
        self.function_dict['ad'].groupsPage().group_add_members()
        self.function_dict['ad'].groupsPage().group_add_members()


