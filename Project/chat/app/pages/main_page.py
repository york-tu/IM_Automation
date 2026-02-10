from time import sleep

# from Project.chat.testsuite.app.uat_app_regression import phone_platform
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.friend_page import FriendPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl
import pandas as pd
import re


class MainPageLocator(BaseLocator):
    """主頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    login = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登录'),
        iOS=base.data_collation(type_kind='name', type_name='登录', pos=[0.25966183574879226, 0.8995535714285714])
    )

    login_expired_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登录状态已过期，请重新登录'),
        iOS=base.data_collation(type_kind='name', type_name='登录状态已过期，请重新登录')
    )
    login_expired_msg_confirm_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', num=-1)
    )
    login_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_login'),
        iOS=base.data_collation(type_kind='name', type_name='phoneLogin_login_button')
    )
    email_login_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_login'),
        iOS=base.data_collation(type_kind='name', type_name='emailLogin_login_button')
    )
    register_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='注册', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='emailLogin_register_button')
    )
    register_page_register_button = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='register_register_button')
    )
    warning_icon = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='iconIconAttention')
    )
    checkPASS_icon = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='iconIconCheckAll')
    )
    # login_email_input = base.check_device(
    #     Android=base.data_collation(type_kind='text', type_name='请填写电子邮箱'),
    #     iOS=base.data_collation(type_kind='name', type_name='')
    # )
    login_email_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text', num=0),
        iOS=base.data_collation(type_kind='name', type_name='registerVerifyEmail_email_textField')
    )
    login_email_input_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon_left_of_selector'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本')
    )
    next_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='下一步'),
        iOS=base.data_collation(type_kind='name', type_name='下一步')
    )
    get_verify_code_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_get_verification_code'),
        iOS=base.data_collation(type_kind='name', type_name='forgotPassword_verificationCode_button')
    )
    input_code = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入验证码'),
        iOS=base.data_collation(type_kind='name', type_name='codeVerify_textField')
    )
    forgetPW_input_code = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入验证码'),
        iOS=base.data_collation(type_kind='name', type_name='forgotPassword_verificationCode_textField')
    )
    input_account_id = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='填写帐号'),
        iOS=base.data_collation(type_kind='name', type_name='register_accountID_textField')
    )
    input_pw = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='设定密码'),
        iOS=base.data_collation(type_kind='name', type_name='register_password_textField')
    )
    input_confirm_pw = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='再次设定密码'),
        iOS=base.data_collation(type_kind='name', type_name='register_passwordConfirm_textField')
    )
    input_nickname = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='填写昵称'),
        iOS=base.data_collation(type_kind='name', type_name='register_nickname_textField')
    )
    input_account_note = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='填写帐号备注.*'),
        iOS=base.data_collation(type_kind='name', type_name='register_socialAccount_textField')
    )

    logout = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登出'),
        iOS=base.data_collation(type_kind='name', type_name='accountSecurity_logout_button')
    )

    logout_popup = base.check_device(
        Android=base.data_collation(type_kind='text',
                                    type_name='登出后不会删除任何资料纪录，下次登入依然可以使用本帐号。'),
        iOS=base.data_collation(type_kind='name', type_name='登出后不会删除任何资料纪录，下次登入依然可以使用本帐号。'),
    )

    confirm_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='accountSecurity_logout_alertAction'),
    )
    new_login_page_welcome_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_welcome'),
        iOS=base.data_collation(type_kind='name', type_name='loginOption_title_label'),
    )
    new_login_page_use_cellphone_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='使用手机号继续'),
        iOS=base.data_collation(type_kind='name', type_name='loginOption_withPhone_button'),
    )
    new_login_page_use_email_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='使用电子邮箱继续'),
        iOS=base.data_collation(type_kind='name', type_name='loginOption_withEmail_button'),
    )
    new_login_page_agreement_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_agreement_hint'),
        iOS=base.data_collation(type_kind='name', type_name='loginOption_info_label'),
    )
    new_login_page_close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_close'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconCross'),
    )
    account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text', num=0),
        iOS=base.data_collation(type_kind='name', type_name='phoneLogin_phone_textField')
    )
    email_account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text', num=0),
        iOS=base.data_collation(type_kind='name', type_name='emailLogin_email_textField')
    )
    password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写密码'),
        iOS=base.data_collation(type_kind='name', type_name='phoneLogin_password_textField')
    )
    email_password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写密码'),
        iOS=base.data_collation(type_kind='name', type_name='emailLogin_password_textField')
    )
    forgetPW_email_account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text', num=0),
        iOS=base.data_collation(type_kind='name', type_name='forgotPassword_email_textField')
    )
    forgetPW_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_forget_password'),
        iOS=base.data_collation(type_kind='name', type_name='emailLogin_forgot_button')
    )
    forgetPWPage_newPW = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='设定新的密码'),
        iOS=base.data_collation(type_kind='name', type_name='setupNewPassword_password_textField')
    )
    forgetPWPage_confirmNewPW = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='再次设定新的密码'),
        iOS=base.data_collation(type_kind='name', type_name='setupNewPassword_confirmPassword_textField')
    )
    PWReset_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_reset'),
        iOS=base.data_collation(type_kind='name', type_name='setupNewPassword_submit_button')
    )
    alert_msg = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/alertTitle'),
        iOS=base.data_collation(type_kind='name', type_name='密码重设成功')
    )

    error = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='手机号/密码错误，请重新输入'),
        iOS=base.data_collation(type_kind='name', type_name='手机号/密码错误，请重新输入'),
    )

    fgpws_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='取消'),
        iOS=base.data_collation(type_kind='name', type_name='取消'),
    )

    friends_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_friend'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_friendList_button'),
    )

    message_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_chat_button'),
    )

    friends_list_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组'),
        iOS=base.data_collation(type_kind='name', type_name='群组'),
    )
    discover_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view',
                                    num=-2),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_discover_button')
    )
    main_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_my_button'),
    )
    main_self_id = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_username'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_userID_label'),
    )
    main_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_nickname_label'),
    )

    main_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_introduction_label'),
    )

    mine_menu_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_menu_button'),
    )
    mine_settings_self_id = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_id'),
        iOS=base.data_collation(type_kind='name', type_name='setting_userId_label'),
    )

    followed_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='已关注'),
        iOS=base.data_collation(type_kind='name', type_name='已关注'),
    )
    recommend_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='推荐'),
        iOS=base.data_collation(type_kind='name', type_name='推荐'),
    )

    about_button = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='关于.*'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='关于.*'),
    )

    about_button_365 = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='关于365'),
        iOS=base.data_collation(type_kind='name', type_name='关于股聊'),
    )

    chat_list = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='信息'),
        iOS=base.data_collation(type_kind='name', type_name='信息'),
    )

    security_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号与安全'),
        iOS=base.data_collation(type_kind='name', type_name='帐号与安全'),
    )

    chat_list_check = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rv_chat_list'),
        iOS=base.data_collation(type_kind='name', type_name='Chat'),
    )

    nation_focus = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_country_name'),
        iOS=base.data_collation(type_kind='name', type_name='phoneLogin_region_textField'),
    )

    nation_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right_arrow'),
        iOS=base.data_collation(type_kind='name', type_name='phoneLogin_region_textField'),
    )

    nation_search = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='name', type_name='selectRegion_search_textField'),
    )

    nation_check = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='选择国家和地区', pos=[0.5013333333333333, 0.08066502463054187]),
    )

    nation_code = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_country_code'),
        iOS=base.data_collation(type_kind='name', type_name='selectRegion_contryDigit_label'),
    )

    edit_profile_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='编辑主页'),
        iOS=base.data_collation(type_kind='name', type_name='编辑主页'),
    )
    share_profile_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='分享主页'),
        iOS=base.data_collation(type_kind='name', type_name='分享主页'),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button'),
    )


class MainPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    brand = gl.get_value("BRAND")
    env = gl.get_value("ENV")
    # PASS_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_PASS.xlsx"
    # FAIL_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_FAIL.xlsx"

    # 處理登錄狀態已過期視窗
    def login_expired_handling(self):
        sleep(1)
        if self.common.poco_exists(MainPageLocator.login_expired_msg):
            self.common.poco_click(MainPageLocator.login_expired_msg_confirm_btn)
            sleep(1)

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self, login_id):
        """確認是否已登入"""
        sleep(1.5)
        self.common.poco_click(MainPageLocator.main_btn)
        sleep(0.5)
        if self.common.poco_exists(MainPageLocator.new_login_page_welcome_description):
            # 在登入頁面 → 表示未登入
            self.common.poco_click(MainPageLocator.new_login_page_close_btn)
            return False
        elif not self.common.poco_get_text(MainPageLocator.main_self_id) == f'@{login_id}':
            # 登入帳號非預期 → 表示未登入
            return False
        else:
            # 不在登入頁面 → 表示已登入
            return True

    def welcome_page_show(self):
        if not self.common.poco_exists(MainPageLocator.new_login_page_welcome_description):
            self.common.poco_click(MainPageLocator.main_btn)
        if self.common.poco_exists(MainPageLocator.new_login_page_welcome_description):
            return True
        else:
            return False

    def into_home_check(self):
        sleep(3)
        self.common.poco_click(MainPageLocator.main_btn)

    # 登出
    def logout(self):
        self.common.poco_click(MainPageLocator.logout)
        self.common.poco_click(MainPageLocator.confirm_button)

        # iOS 優化：減少登出後的等待時間
        if self.phone_platform.lower() == 'ios':
            sleep(1.5)  # 減少等待時間（從 3 秒降到 1.5 秒）
            self.common.poco_click(MainPageLocator.main_btn)
            # 快速檢查登入頁出現（最多等待 2 秒）
            for i in range(4):  # 4 * 0.5 = 2 秒
                if self.common.poco_exists(MainPageLocator.new_login_page_welcome_description):
                    break
                sleep(0.5)
            assert self.common.poco_exists(MainPageLocator.new_login_page_welcome_description), '未出現登入頁'
        else:
            self.common.sleep(3)
            assert self.common.poco_get_attr(MainPageLocator.recommend_tab, 'selected') is True, f'未回到訪客首頁推薦頁'
            self.common.poco_click(MainPageLocator.main_btn)
            assert self.common.poco_exists(MainPageLocator.new_login_page_welcome_description), '未出現登入頁'

    # 登入
    def do_login(self, account_locator, password_locator, login_btn_locator,
                 account, password):
        """共用登入流程"""
        self.common.poco_click(account_locator)
        self.common.poco_send_text(account_locator, account)
        self.common.poco_click(password_locator)
        self.common.poco_send_text(password_locator, password)

        self.common.poco_click(login_btn_locator)

        self.common.poco_click(MainPageLocator.main_btn)
        # 預設檢查：只要不出現登入頁面就視為成功
        assert not self.common.poco_exists(MainPageLocator.new_login_page_welcome_description), '登入失敗，仍在登入頁'

    def login(self, account: str, password: str, nation='CN', login_method='phone'):  # 從歡迎頁開始確認
        # 如果已登入 -> 先登出
        if not self.common.poco_exists(MainPageLocator.new_login_page_close_btn):
            self.common.poco_click(MainPageLocator.main_btn)
        if not self.common.poco_exists(MainPageLocator.new_login_page_welcome_description):
            self.into_main_setting_page()
            self.common.poco_click(MainPageLocator.security_button)
            self.logout()
        self.check_new_login_page()

        # 各種登入方式的配置表
        login_config = {
            "phone": {
                "android": {
                    "entry_btn": MainPageLocator.new_login_page_use_cellphone_btn,
                    "account": MainPageLocator.account,
                    "password": MainPageLocator.password,
                    "login_btn": MainPageLocator.login_button,
                },
                "ios": {
                    "entry_btn": MainPageLocator.new_login_page_use_cellphone_btn,
                    "account": MainPageLocator.account,
                    "password": MainPageLocator.password,
                    "login_btn": MainPageLocator.login_button,
                }
            },
            "email": {
                "android": {
                    "entry_btn": MainPageLocator.new_login_page_use_email_btn,
                    "account": MainPageLocator.account,
                    "password": MainPageLocator.password,
                    "login_btn": MainPageLocator.login_button,
                },
                "ios": {
                    "entry_btn": MainPageLocator.new_login_page_use_email_btn,
                    "account": MainPageLocator.email_account,
                    "password": MainPageLocator.email_password,
                    "login_btn": MainPageLocator.email_login_button,
                }
            }
        }

        platform = self.phone_platform.lower()
        cfg = login_config[login_method][platform]

        # 進入對應登入方式頁面
        self.common.poco_click(cfg["entry_btn"])

        # phone 登入才需要選國碼
        if login_method == "phone":
            self.switch_nation(nation)

        # 執行共用登入流程
        check_args = cfg.get("check", {})
        self.do_login(cfg["account"], cfg["password"], cfg["login_btn"],
                      account, password)

    def check_new_login_page(self):
        sleep(1)
        welcome_description = self.common.poco_get_text(MainPageLocator.new_login_page_welcome_description)
        assert ('欢迎来到' in welcome_description) and (self.get_product_name() in welcome_description)
        agreement_hint = self.common.poco_get_text(MainPageLocator.new_login_page_agreement_hint)
        assert agreement_hint == '如果您继续操作，即表示您同意《服务条款》并确认已阅读《隐私权政策》。'

    def get_product_name(self):
        brand = self.brand.lower()
        env = self.env.lower()

        suffix = "_UAT" if env == 'uat' else ""
        product_info = {
            "gu": f"GuChat{suffix}",
            "mingpin": f"名品会{suffix}",
            "chit": f"ChitChat{suffix}",
        }

        # 預設值，可避免 key 不存在報錯
        product = product_info.get(brand, "UnknownProduct")
        return product

    def into_main_setting_page(self):
        self.common.poco_click(MainPageLocator.main_btn)
        self.common.poco_click(MainPageLocator.mine_menu_btn)
        assert self.common.poco_exists(MainPageLocator.mine_settings_self_id)

    def into_main_page(self):
        self.common.poco_click(MainPageLocator.main_btn)
        sleep(3)
        assert self.common.poco_exists(MainPageLocator.main_self_id)

    def get_nickname(self):
        # iOS 優化：確保主頁元素存在後再讀取
        if self.phone_platform.lower() == 'ios':
            # 等待主頁暱稱元素出現（最多等待 3 秒）
            for i in range(6):  # 6 * 0.5 = 3 秒
                try:
                    if self.common.poco_exists(MainPageLocator.main_nickname):
                        break
                except:
                    pass
                sleep(0.5)
        
        data = self.common.poco_get_text(MainPageLocator.main_nickname)
        return data

    def get_self_introduction(self):
        # iOS 優化：確保主頁元素存在後再讀取
        if self.phone_platform.lower() == 'ios':
            # 等待主頁簡介元素出現（最多等待 3 秒）
            for i in range(6):  # 6 * 0.5 = 3 秒
                try:
                    if self.common.poco_exists(MainPageLocator.main_description):
                        break
                except:
                    pass
                sleep(0.5)
        
        data = self.common.poco_get_text(MainPageLocator.main_description)
        return data

    def into_friend_page(self):
        self.common.poco_click(MainPageLocator.message_btn)
        self.common.poco_click(MainPageLocator.friends_btn)
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)
        # self.skip_login_rush()
        assert self.common.poco_exists(MainPageLocator.friends_list_check), f'進入好友名單錯誤'

    def into_chat_page(self):
        # iOS 優化：限制返回按鈕點擊次數，避免無限循環
        if self.phone_platform.lower() == 'ios':
            back_click_count = 0
            max_back_clicks = 5
            while self.common.poco_exists(MainPageLocator.back_btn) and back_click_count < max_back_clicks:
                self.common.poco_click(MainPageLocator.back_btn)
                back_click_count += 1
                sleep(0.3)  # 減少等待時間
        else:
            while self.common.poco_exists(MainPageLocator.back_btn):
                self.common.poco_click(MainPageLocator.back_btn)
        
        # iOS 優化：縮短等待時間（從默認 10 秒降到 5 秒）
        timeout = 5 if self.phone_platform.lower() == 'ios' else 10
        self.common.poco_wait_exists(MainPageLocator.message_btn, timeout=timeout)
        self.common.poco_click(MainPageLocator.message_btn)

        assert self.common.poco_exists(MainPageLocator.chat_list_check), f'進入聊天列表錯誤'

    def switch_nation(self, nation):
        self.common.sleep(1)
        country_name = ''
        country_code = ''
        if nation == 'CN':
            if self.phone_platform.lower() == 'ios':
                country_name = '中国大陆 China mainland'
            else:
                country_name = '中国大陆 China'
            country_code = '86'
        elif nation == 'TW':
            if self.phone_platform.lower() == 'ios':
                country_name = '台湾 Taiwan'
            else:
                country_name = '中国台湾 Taiwan, China'
            country_code = '886'
        elif nation == 'JP':
            country_name = '日本 Japan'
            country_code = '81'

        for _ in range(0, 1):
            nation_now = self.common.poco_get_text(MainPageLocator.nation_focus)

            if nation_now != country_name:
                self.common.poco_click(MainPageLocator.nation_button)
                self.common.sleep(0.5)
                self.common.poco_click(MainPageLocator.nation_search)
                self.common.poco_send_text(MainPageLocator.nation_search, country_code)
                self.common.sleep(0.5)

                code_result = self.common.poco_get_text(MainPageLocator.nation_code)
                code_number = code_result.replace("+", "")
                assert code_number == country_code, f'國家搜尋有誤 應該為{country_code} 搜尋結果為{code_result}'
                self.common.poco_click(MainPageLocator.nation_code)
            else:
                break

    def register_by_email(self, account, email, pw):
        if self.common.poco_exists(MainPageLocator.main_btn):
            self.common.poco_click(MainPageLocator.main_btn)
        self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
        self.common.poco_click(MainPageLocator.register_button)
        self.common.poco_click(MainPageLocator.login_email_input)
        self.common.poco_send_text(MainPageLocator.login_email_input, email)  # 輸入email
        self.common.poco_click(MainPageLocator.next_btn)

        # ==================== 獲得驗證碼 > 輸入驗證碼 ====================
        sleep(15)
        code = self.common.get_verification_code_from_mail(self.brand)  # 獲得驗證碼
        self.common.poco_click(MainPageLocator.input_code)
        self.common.poco_send_text(MainPageLocator.input_code, code)  # 輸入驗證碼
        self.common.poco_click(MainPageLocator.next_btn)

        # ==================== 資料填寫頁 ====================
        self.common.poco_click(MainPageLocator.input_account_id)
        self.common.poco_send_text(MainPageLocator.input_account_id, account)  # 輸入帳號ID
        self.common.poco_click(MainPageLocator.input_pw)
        self.common.poco_send_text(MainPageLocator.input_pw, pw)  # 輸入密碼設置
        self.common.poco_click(MainPageLocator.input_confirm_pw)
        self.common.poco_send_text(MainPageLocator.input_confirm_pw, pw)  # 輸入確認密碼
        self.common.poco_click(MainPageLocator.input_nickname)
        self.common.poco_send_text(MainPageLocator.input_nickname, account)  # 輸入暱稱
        if self.common.poco_exists(MainPageLocator.input_account_note):
            self.common.poco_click(MainPageLocator.input_account_note)
            self.common.poco_send_text(MainPageLocator.input_account_note, 'AutoTest')  # 輸入帳號備注

        if self.phone_platform.lower() == 'android':
            self.common.poco_click(MainPageLocator.register_button)
        else:
            self.common.poco_click(MainPageLocator.register_page_register_button)
        # ==================== 進到個人主頁 ====================
        self.common.poco_click(MainPageLocator.main_btn)
        assert self.get_nickname() == account

    # 登入頁email欄位檢核
    # def input_email_check_in_login(self):
    #     if self.phone_platform.lower() == 'android':
    #         self.common.poco_click(MainPageLocator.main_btn)
    #         self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
    #         self.common.poco_send_text(MainPageLocator.password, '000111abc')
    #
    #         df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
    #         for idx, row in df1.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             result = self.common.poco_get_attr(MainPageLocator.login_button, 'enabled')
    #             assert result is False, f'輸入:{email} => {result}'
    #
    #         df2 = pd.read_excel(self.PASS_email_file_path, header=None)
    #         for idx, row in df2.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             result = self.common.poco_get_attr(MainPageLocator.login_button, 'enabled')
    #             assert result is True, f'輸入:{email} => {result}'
    #
    #         self.common.poco_click(MainPageLocator.fgpws_button)
    #
    #     else:  # 'ios'
    #         self.common.poco_click(MainPageLocator.main_btn)
    #         self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
    #         self.common.poco_click(MainPageLocator.password)
    #         self.common.poco_send_text(MainPageLocator.password, '000111abc')
    #
    #         df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
    #         for idx, row in df1.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             self.common.poco_click(MainPageLocator.password)
    #
    #             result = self.common.poco_get_attr(MainPageLocator.login_button, 'isEnabled')
    #             assert result == '0', f'輸入:{email} => {result}, (note:enable=1)'
    #             assert self.common.poco_exists(MainPageLocator.warning_icon)
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_click(MainPageLocator.login_email_input_clear)
    #
    #         df2 = pd.read_excel(self.PASS_email_file_path, header=None)
    #         for idx, row in df2.iterrows():
    #             email = str(row[0]).strip()
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             self.common.poco_click(MainPageLocator.password)
    #             result = self.common.poco_get_attr(MainPageLocator.login_button, 'isEnabled')
    #             assert result == '1', f'輸入:{email} => {result}, (note:enable=1)'
    #             assert not self.common.poco_exists(MainPageLocator.warning_icon)
    #             assert self.common.poco_exists(MainPageLocator.checkPASS_icon)
    #
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_click(MainPageLocator.login_email_input_clear)
    #
    #         self.common.poco_click(MainPageLocator.fgpws_button)

    # 註冊頁email欄位檢核
    # def input_email_check_in_registration(self):
    #     if self.phone_platform.lower() == 'android':
    #         self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
    #         self.common.poco_click(MainPageLocator.register_button)
    #
    #         df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
    #         for idx, row in df1.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             result = self.common.poco_get_attr(MainPageLocator.next_btn, 'enabled')
    #             assert result is False, f'輸入:{email} => {result}'
    #
    #         df2 = pd.read_excel(self.PASS_email_file_path, header=None)
    #         for idx, row in df2.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             result = self.common.poco_get_attr(MainPageLocator.next_btn, 'enabled')
    #             assert result is True, f'輸入:{email} => {result}'
    #
    #     else:  # 'ios'
    #         self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
    #         self.common.poco_click(MainPageLocator.register_button)
    #
    #         df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
    #         for idx, row in df1.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             self.common.poco_click(MainPageLocator.next_btn)
    #             result = self.common.poco_get_attr(MainPageLocator.next_btn, 'isEnabled')
    #             assert result == '0', f'輸入:{email} => {result}, (note:enable=1)'
    #             assert self.common.poco_exists(MainPageLocator.warning_icon)
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_click(MainPageLocator.login_email_input_clear)
    #
    #         df2 = pd.read_excel(self.PASS_email_file_path, header=None)
    #         for idx, row in df2.iterrows():
    #             email = str(row[0]).strip()
    #
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_send_text(MainPageLocator.login_email_input, email)
    #             self.common.poco_click(MainPageLocator.register_button)
    #             result = self.common.poco_get_attr(MainPageLocator.next_btn, 'isEnabled')
    #             assert result == '1', f'輸入:{email} => {result}, (note:enable=1)'
    #             assert not self.common.poco_exists(MainPageLocator.warning_icon)
    #             assert self.common.poco_exists(MainPageLocator.checkPASS_icon)
    #             self.common.poco_click(MainPageLocator.login_email_input)
    #             self.common.poco_click(MainPageLocator.login_email_input_clear)

    # email登入頁 > 忘記密碼
    def email_forgetPW_resetPW_loginNewPW(self, email, newPW):
        if self.common.poco_click(MainPageLocator.main_btn):
            self.common.poco_click(MainPageLocator.main_btn)
        self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
        self.common.poco_click(MainPageLocator.forgetPW_btn)  # 忘記密碼鍵
        # ==================== 忘記密碼頁 ====================
        self.common.poco_click(MainPageLocator.forgetPW_email_account)
        self.common.poco_send_text(MainPageLocator.forgetPW_email_account, email)  # 輸入email
        self.common.poco_click(MainPageLocator.get_verify_code_btn)  # 獲得驗證碼btn
        # ==================== 獲得驗證碼 > 輸入驗證碼 ====================
        sleep(15)
        code = self.common.get_verification_code_from_mail(self.brand)  # 獲得驗證碼
        self.common.poco_click(MainPageLocator.forgetPW_input_code)
        self.common.poco_send_text(MainPageLocator.forgetPW_input_code, code)  # 輸入驗證碼
        self.common.poco_click(MainPageLocator.next_btn)
        # ==================== 設定新密碼頁 ====================
        self.common.poco_click(MainPageLocator.forgetPWPage_newPW)
        self.common.poco_send_text(MainPageLocator.forgetPWPage_newPW, newPW)  # 設定新密碼
        self.common.poco_click(MainPageLocator.forgetPWPage_confirmNewPW)
        self.common.poco_send_text(MainPageLocator.forgetPWPage_confirmNewPW, newPW)  # 再次設定新密碼
        self.common.poco_click(MainPageLocator.PWReset_btn)  # 重設密碼btn
        # ==================== 確認密碼設定成功彈窗 ====================
        assert self.common.poco_exists(MainPageLocator.alert_msg)
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_text(MainPageLocator.alert_msg) == '密码重设成功'
            self.common.poco_click(MainPageLocator.confirm_button)
        else:
            self.poco(type='ScrollView')[-1].click()
            self.common.poco_click(MainPageLocator.email_account)
            self.common.poco_send_text(MainPageLocator.email_account, email)  # 登陸頁輸入email
        # ==================== 輸入新密碼後登入 ====================
        self.common.poco_click(MainPageLocator.email_password)
        self.common.poco_send_text(MainPageLocator.email_password, newPW)
        self.common.poco_click(MainPageLocator.email_login_button)  # 登陸
