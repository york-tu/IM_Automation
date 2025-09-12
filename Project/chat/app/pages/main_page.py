from time import sleep

# from Project.chat.testsuite.app.uat_app_regression import phone_platform
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.friend_page import FriendPageLocator
import logging
import common.utils.globalvar as gl
import pandas as pd
import re


class MainPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)


    @staticmethod
    def env(env):
        env = MainPageLocator.base.check_device(
            Android=MainPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=MainPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    login = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登录'),
        iOS=base.data_collation(type_kind='name', type_name='登录', pos=[0.25966183574879226, 0.8995535714285714])
    )

    login_expired_msg = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/parentPanel'),
        iOS=base.data_collation(type_kind='name', type_name='登录状态已过期，请重新登录')
    )

    login_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_login'),
        iOS=base.data_collation(type_kind='name', type_name='登录', num=-2)
    )
    register_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='注册', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='注册', num=-1)
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
        iOS=base.data_collation(type_kind='name', type_name='register_verify_email_input')
    )
    login_email_input_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon_left_of_selector'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本')
    )
    next_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='下一步'),
        iOS=base.data_collation(type_kind='name', type_name='register_verify_email_next_button')
    )
    input_code = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入验证码'),
        iOS=base.data_collation(type_kind='name', type_name='TextField', num=-1)
    )
    input_account_id = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='填写帐号'),
        iOS=base.data_collation(type_kind='name', type_name='TextField', num=0)
    )
    input_pw = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='设定密码'),
        iOS=base.data_collation(type_kind='name', type_name='SecureTextField', num=0)
    )
    input_confirm_pw = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='再次设定密码'),
        iOS=base.data_collation(type_kind='name', type_name='SecureTextField', num=1)
    )
    input_nickname = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='填写昵称'),
        iOS=base.data_collation(type_kind='name', type_name='TextField', num=-3)
    )

    logout = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登出'),
        iOS=base.data_collation(type_kind='name', type_name='登出')
    )

    logout_popup = base.check_device(
        Android=base.data_collation(type_kind='text',
                                    type_name='登出后不会删除任何资料纪录，下次登入依然可以使用本帐号。'),
        iOS=base.data_collation(type_kind='name', type_name='登出后不会删除任何资料纪录，下次登入依然可以使用本帐号。'),
    )

    logout_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', pos=[0.5, 0.8577008928571429]),
    )
    new_login_page_welcome_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_welcome'),
        iOS=base.data_collation(type_kind='nameMatches', type_name=f'欢迎来到.*'),
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
        iOS=base.data_collation(type_kind='nameMatches', type_name=f'如果您继续.*'),
    )
    account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text', num=0),
        iOS=base.data_collation(type_kind='name', type_name='TextField', num=-1)
    )
    password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写密码'),
        iOS=base.data_collation(type_kind='name', type_name='SecureTextField')
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
        iOS=base.data_collation(type_kind='name', type_name='iconIconGroup'),
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
        Android=base.data_collation(type_kind='text', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_discover_button'),
    )
    main_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_my_button'),
    )

    main_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0),
    )

    main_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='.*auto.*'),
    )

    mine_menu_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right'),
        iOS=base.data_collation(type_kind='name', type_name='icon menu', num=0),
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
        Android=base.data_collation(type_kind='textMatches', type_name='关于.*聊'),
        iOS=base.data_collation(type_kind='name', type_name='关于股聊'),
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
        iOS=base.data_collation(type_kind='name', type_name='TextField', pos=[0.5869565217391305, 0.21428571428571427]),
    )

    nation_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right_arrow'),
        iOS=base.data_collation(type_kind='name', type_name='TextField', pos=[0.5869565217391305, 0.21428571428571427]),
    )

    nation_search = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='name', type_name='TextField', pos=[0.5, 0.13169642857142858]),
    )

    nation_check = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='选择国家和地区', pos=[0.5, 0.07700892857142858]),
    )

    nation_code = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_country_code'),
        iOS=base.data_collation(type_kind='name', type_name='Cell', pos=[0.5, 0.19419642857142858]),
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
        iOS=base.data_collation(type_kind='name', type_name='iconArrowsChevronLeft'),
    )


class MainPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    PASS_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_PASS.xlsx"
    FAIL_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_FAIL.xlsx"

    def check_navigation_bar_items_count(self):
        sleep(1)
        counts = len(self.poco(name=str(MainPageLocator.app_package) + ":id/navigation_bar_item_icon_view"))
        return counts

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        if self.phone_platform.lower() == 'android':
            # 檢查工具列是否有5個icon(包含發現icon)
            if self.check_navigation_bar_items_count() == 5:  # 登入後才會有發現icon
                return True
            return False
        else:  # ios
            # 檢查工具列是否有發現icon
            if self.common.poco_exists(MainPageLocator.discover_btn):  # 登入後才會有發現icon
                return True
            return False

    def into_home_check(self, status):
        if self.phone_platform.lower() == 'android':
            number = 0

            self.check_login_status()

            for loop in range(0, 30):
                self.common.sleep(0.5)

                if status is True and self.check_login_status() is False:
                    logging.warning('帳號被登出了')
                    return False
                elif self.check_login_status() is False:
                    return False
                sleep(3)
                if self.common.poco_exists(MainPageLocator.message_btn) or self.common.poco_exists(MainPageLocator.main_btn):
                    number += 1  # 為避免找到首頁定位後才跳出彈窗，故找到後再跑一次
                    if number == 2:
                        break

                if loop == 29:
                    raise EOFError('開啟app錯誤')
        # =========================== ios scenario =====================================
        else:
            if self.check_login_status():
                return True
            else:
                return False

    # 登出
    def logout(self):
        if self.common.poco_wait_exists(MainPageLocator.logout, timeout=10):
            self.common.poco_click(MainPageLocator.logout)
        if self.common.poco_wait_exists(MainPageLocator.logout_popup, timeout=10):
            self.common.poco_click(MainPageLocator.logout_button)

        self.common.sleep(3)
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_attr(MainPageLocator.recommend_tab, 'selected') is True, f'未回到訪客首頁推薦頁'
            assert self.check_navigation_bar_items_count() == 4, f'未成功登出'
        else:  # ios
            assert not self.common.poco_exists(MainPageLocator.discover_btn)

    # 登入
    def login(self, account: str, password: str, nation='CN', login_method='phone'):
        if self.check_login_status() is True:  # 當狀態為已登入時先登出
            self.into_main_setting_page()
            if self.common.poco_exists(MainPageLocator.login_expired_msg):  # popup 登入狀態已過期視窗
                self.common.poco_click(MainPageLocator.logout_button)  # 點擊"確定"
            else:
                self.common.poco_click(MainPageLocator.security_button)
                self.logout()

        self.common.poco_click(MainPageLocator.main_btn)
        self.check_new_login_page()

        if self.phone_platform.lower() == 'android':
            if login_method == 'phone':  # 透過手機號登入
                self.common.poco_click(MainPageLocator.new_login_page_use_cellphone_btn)
                self.switch_nation(nation)
                self.common.poco_send_text(MainPageLocator.account, account)
                self.common.poco_send_text(MainPageLocator.password, password)
                self.common.sleep(0.5)
            else:  # 透過email登入
                self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
                self.common.poco_send_text(MainPageLocator.account, account)
                self.common.poco_send_text(MainPageLocator.password, password)
                self.common.sleep(0.5)
        else:  # ios
            if login_method == 'phone':  # 透過手機號登入
                self.common.poco_click(MainPageLocator.new_login_page_use_cellphone_btn)
                self.switch_nation(nation)
                self.common.poco_click(MainPageLocator.account)
                self.common.poco_send_text(MainPageLocator.account, account)
                self.common.poco_click(MainPageLocator.password)
                self.common.poco_send_text(MainPageLocator.password, password)
                self.common.sleep(0.5)
            else:  # 透過email登入
                self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
                self.common.poco_click(MainPageLocator.account)
                self.common.poco_send_text(MainPageLocator.account, account)
                self.common.poco_click(MainPageLocator.password)
                self.common.poco_send_text(MainPageLocator.password, password)
                self.common.sleep(0.5)

        if self.common.poco_exists(MainPageLocator.login_button):
            self.common.poco_click(MainPageLocator.login_button)
            self.common.sleep(0.5)

        if self.common.poco_exists(MainPageLocator.error):
            error_message = self.common.poco_get_text(MainPageLocator.error)
            raise EOFError(f'登入失敗-{error_message}')

        self.wait_loading_finish()
        sleep(1)
        assert self.common.poco_exists(MainPageLocator.recommend_tab), f'登入失敗'

    def check_new_login_page(self):
        if self.phone_platform.lower() == 'android':
            product = '股聊'
        else:
            product = 'GuChat'
        sleep(3)
        welcome_description = self.common.poco_get_text(MainPageLocator.new_login_page_welcome_description)
        assert ('欢迎来到' in welcome_description) and (product in welcome_description)
        agreement_hint = self.common.poco_get_text(MainPageLocator.new_login_page_agreement_hint)
        assert agreement_hint == '如果您继续操作，即表示您同意《服务条款》并确认已阅读《隐私权政策》。'

    def check_focus_recommend_tab_after_login(self):
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_attr(MainPageLocator.recommend_tab, "selected") is True, f'登入後沒有focus推薦頁'

    def into_main_setting_page(self):
        if self.common.poco_wait_exists(MainPageLocator.main_btn):
            self.common.poco_click(MainPageLocator.main_btn)
        if self.common.poco_wait_exists(MainPageLocator.mine_menu_btn):
            self.common.poco_click(MainPageLocator.mine_menu_btn)
        self.skip_login_rush()
        if gl.get_value('BRAND') == 's365':
            assert self.common.poco_exists(MainPageLocator.about_button_365), f'進入主頁_我的設定頁錯誤'
        else:
            if self.common.poco_exists(MainPageLocator.login_expired_msg):
                return
            else:
                assert self.common.poco_exists(MainPageLocator.about_button), f'進入主頁_我的設定頁錯誤'

    def into_main_page(self):
        if self.common.poco_wait_exists(MainPageLocator.main_btn):
            self.common.poco_click(MainPageLocator.main_btn)
            assert self.common.poco_exists(MainPageLocator.share_profile_btn), f'進入主頁錯誤'
            assert self.common.poco_exists(MainPageLocator.edit_profile_btn), f'進入主頁錯誤'

    def get_nickname(self):
        if self.phone_platform.lower() == 'android':
            data = self.common.poco_get_text(MainPageLocator.main_nickname)
        else:
            data = self.poco(type="StaticText").attr('value')
        return data

    def get_self_introduction(self):
        data = self.common.poco_get_text(MainPageLocator.main_description)
        return data

    def into_friend_page(self):
        if self.common.poco_wait_exists(MainPageLocator.message_btn):
            self.common.poco_click(MainPageLocator.message_btn)
        if self.common.poco_wait_exists(MainPageLocator.friends_btn):
            self.common.poco_click(MainPageLocator.friends_btn)
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)
        self.skip_login_rush()
        assert self.common.poco_exists(MainPageLocator.friends_list_check), f'進入好友名單錯誤'

    def into_chat_page(self):
        while self.common.poco_exists(MainPageLocator.back_btn):
            self.common.poco_click(MainPageLocator.back_btn)
        self.common.poco_wait_exists(MainPageLocator.message_btn)
        self.common.poco_click(MainPageLocator.message_btn)
        # self.skip_login_rush()

        assert self.common.poco_exists(MainPageLocator.chat_list_check), f'進入聊天列表錯誤'

    def switch_nation(self, nation):
        self.common.sleep(1)
        country_name = ''
        country_code = ''
        if nation == 'CN':
            country_name = '中国大陆'
            country_code = '86'
        elif nation == 'TW':
            country_name = '台湾'
            country_code = '886'
        elif nation == 'JP':
            country_name = '日本'
            country_code = '81'

        for _ in range(0, 1):
            if self.phone_platform.lower() == 'android':
                nation_now = self.common.poco_get_text(MainPageLocator.nation_focus)
            else:
                nation_now = self.common.poco_get_attr(MainPageLocator.nation_focus, 'value')

            if nation_now != country_name:
                self.common.poco_click(MainPageLocator.nation_button)

                self.common.sleep(0.5)
                if self.phone_platform.lower() == 'android':
                    assert self.common.poco_get_text(
                        MainPageLocator.nation_check) == '选择国家和地区', f'進入國家選擇頁面失敗'
                else:
                    assert self.common.poco_get_text(
                        MainPageLocator.nation_check) == '选择国家和地区', f'進入國家選擇頁面失敗'
                    self.common.poco_click(MainPageLocator.nation_search)
                self.common.poco_send_text(MainPageLocator.nation_search, country_code)
                self.common.sleep(0.5)
                if self.phone_platform.lower() == 'android':
                    code_result = self.common.poco_get_text(MainPageLocator.nation_code)
                    code_number = code_result.replace("+", "")
                    assert code_number == country_code, f'國家搜尋有誤 應該為{country_code} 搜尋結果為{code_result}'
                self.common.poco_click(MainPageLocator.nation_code)
            else:
                break

    def register_by_email(self, account, email, pw):
        self.common.poco_click(MainPageLocator.main_btn)
        self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
        self.common.poco_click(MainPageLocator.register_button)
        self.common.poco_click(MainPageLocator.login_email_input)
        self.common.poco_send_text(MainPageLocator.login_email_input, email)  # 輸入email
        self.common.poco_click(MainPageLocator.next_btn)

        # ==================== 獲得驗證碼 > 輸入驗證碼 ====================
        sleep(15)
        code = self.common.get_verification_code_from_mail()  # 獲得驗證碼
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
        self.common.poco_click(MainPageLocator.register_button)
        # ==================== 進到個人主頁 ====================
        self.common.poco_click(MainPageLocator.main_btn)
        assert self.get_nickname() == account

    # 登入頁email欄位檢核
    def input_email_check_in_login(self):
        if self.phone_platform.lower() == 'android':
            self.common.poco_click(MainPageLocator.main_btn)
            self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
            self.common.poco_send_text(MainPageLocator.password, '000111abc')

            df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
            for idx, row in df1.iterrows():
                email = str(row[0]).strip()

                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                result = self.common.poco_get_attr(MainPageLocator.login_button, 'enabled')
                assert result is False, f'輸入:{email} => {result}'

            df2 = pd.read_excel(self.PASS_email_file_path, header=None)
            for idx, row in df2.iterrows():
                email = str(row[0]).strip()

                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                result = self.common.poco_get_attr(MainPageLocator.login_button, 'enabled')
                assert result is True, f'輸入:{email} => {result}'

            self.common.poco_click(MainPageLocator.fgpws_button)

        else:  # 'ios'
            self.common.poco_click(MainPageLocator.main_btn)
            self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
            self.common.poco_click(MainPageLocator.password)
            self.common.poco_send_text(MainPageLocator.password, '000111abc')

            df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
            for idx, row in df1.iterrows():
                email = str(row[0]).strip()

                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                self.common.poco_click(MainPageLocator.password)

                result = self.common.poco_get_attr(MainPageLocator.login_button, 'isEnabled')
                assert result == '0', f'輸入:{email} => {result}, (note:enable=1)'
                assert self.common.poco_exists(MainPageLocator.warning_icon)
                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_click(MainPageLocator.login_email_input_clear)

            df2 = pd.read_excel(self.PASS_email_file_path, header=None)
            for idx, row in df2.iterrows():
                email = str(row[0]).strip()
                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                self.common.poco_click(MainPageLocator.password)
                result = self.common.poco_get_attr(MainPageLocator.login_button, 'isEnabled')
                assert result == '1', f'輸入:{email} => {result}, (note:enable=1)'
                assert not self.common.poco_exists(MainPageLocator.warning_icon)
                assert self.common.poco_exists(MainPageLocator.checkPASS_icon)

                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_click(MainPageLocator.login_email_input_clear)

            self.common.poco_click(MainPageLocator.fgpws_button)

    # 註冊頁email欄位檢核
    def input_email_check_in_registration(self):
        if self.phone_platform.lower() == 'android':
            # self.common.poco_click(MainPageLocator.main_btn)
            self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
            self.common.poco_click(MainPageLocator.register_button)

            df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
            for idx, row in df1.iterrows():
                email = str(row[0]).strip()

                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                result = self.common.poco_get_attr(MainPageLocator.next_btn, 'enabled')
                assert result is False, f'輸入:{email} => {result}'

            df2 = pd.read_excel(self.PASS_email_file_path, header=None)
            for idx, row in df2.iterrows():
                email = str(row[0]).strip()

                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                result = self.common.poco_get_attr(MainPageLocator.next_btn, 'enabled')
                assert result is True, f'輸入:{email} => {result}'

        else:  # 'ios'
            # self.common.poco_click(MainPageLocator.main_btn)
            self.common.poco_click(MainPageLocator.new_login_page_use_email_btn)
            self.common.poco_click(MainPageLocator.register_button)

            df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
            for idx, row in df1.iterrows():
                email = str(row[0]).strip()

                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                self.common.poco_click(MainPageLocator.next_btn)
                result = self.common.poco_get_attr(MainPageLocator.next_btn, 'isEnabled')
                assert result == '0', f'輸入:{email} => {result}, (note:enable=1)'
                assert self.common.poco_exists(MainPageLocator.warning_icon)
                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_click(MainPageLocator.login_email_input_clear)

            df2 = pd.read_excel(self.PASS_email_file_path, header=None)
            for idx, row in df2.iterrows():
                email = str(row[0]).strip()

                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_send_text(MainPageLocator.login_email_input, email)
                self.common.poco_click(MainPageLocator.register_button)
                result = self.common.poco_get_attr(MainPageLocator.next_btn, 'isEnabled')
                assert result == '1', f'輸入:{email} => {result}, (note:enable=1)'
                assert not self.common.poco_exists(MainPageLocator.warning_icon)
                assert self.common.poco_exists(MainPageLocator.checkPASS_icon)
                self.common.poco_click(MainPageLocator.login_email_input)
                self.common.poco_click(MainPageLocator.login_email_input_clear)
