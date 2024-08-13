from time import sleep

# from Project.chat.testsuite.app.uat_app_regression import phone_platform
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


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
        iOS=base.data_collation(type_kind='type', type_name='Button', num=6)
    )

    register_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='注册'),
        iOS=base.data_collation(type_kind='name', type_name='注册')
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

    account = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写手机号码'),
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

    friends_list = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友'),
        iOS=base.data_collation(type_kind='name', type_name='好友'),
    )

    friends_list_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组'),
        iOS=base.data_collation(type_kind='name', type_name='群组'),
    )

    mine_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='主页'),
        iOS=base.data_collation(type_kind='name', type_name='主页'),
    )

    main_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0),
    )

    main_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_description'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=20),
    )

    mine_menu_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_menu'),
        iOS=base.data_collation(type_kind='name', type_name='icon menu', num=0),
    )

    followed_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='已关注'),
        iOS=base.data_collation(type_kind='name', type_name='已关注'),
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
        iOS=base.data_collation(type_kind='name', type_name='返回'),
    )



class MainPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查畫面上是否有注册鈕

        if self.common.poco_exists(MainPageLocator.register_button):
            return False
        elif self.phone_platform.lower() == 'ios' and self.common.poco_exists(MainPageLocator.login):
            return False
        return True


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

                if self.common.poco_exists(MainPageLocator.friends_list) or self.common.poco_exists(MainPageLocator.mine_button):
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
            assert self.common.poco_exists(MainPageLocator.register_button), f'登出失敗'
        else:
            assert self.poco(name="登录").exists(), f'登出失敗'

    # 登入
    def login(self, account: str, password: str, nation: str):
        self.wait_loading_finish()
        if self.check_login_status() is True:
            self.into_main_setting_page()
            if self.common.poco_exists(MainPageLocator.login_expired_msg):  # popup 登入狀態已過期視窗
                self.common.poco_click(MainPageLocator.logout_button)  # 點擊"確定"
            else:
                self.common.poco_click(MainPageLocator.security_button)
                self.logout()

        if self.phone_platform.lower() == 'android':
            self.common.poco_click(MainPageLocator.login)
        else:
            if not self.poco(type="StaticText").attr('value') == '登录':
                if self.common.poco_exists(MainPageLocator.login):
                    self.common.poco_click(MainPageLocator.login)

        self.switch_nation(nation)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(MainPageLocator.account)
        self.common.poco_send_text(MainPageLocator.account, account)
        if self.phone_platform.lower() == 'ios':
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
        assert self.common.poco_exists(MainPageLocator.followed_tab), f'登入失敗'

    def into_main_setting_page(self):
        if self.common.poco_wait_exists(MainPageLocator.mine_button):
            self.common.poco_click(MainPageLocator.mine_button)
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
        if self.common.poco_wait_exists(MainPageLocator.mine_button):
            self.common.poco_click(MainPageLocator.mine_button)
            assert self.common.poco_exists(MainPageLocator.share_profile_btn), f'進入主頁錯誤'
            assert self.common.poco_exists(MainPageLocator.edit_profile_btn), f'進入主頁錯誤'

    def get_nickname(self):
        data = self.common.poco_get_text(MainPageLocator.main_nickname)
        return data

    def get_self_introduction(self):
        data = self.common.poco_get_text(MainPageLocator.main_description)
        return data

    def into_friend_page(self):
        if self.common.poco_wait_exists(MainPageLocator.friends_list):
            self.common.poco_click(MainPageLocator.friends_list)
        self.skip_login_rush()

        assert self.common.poco_exists(MainPageLocator.friends_list_check), f'進入好友名單錯誤'

    def into_chat_page(self):
        while self.common.poco_wait_exists(MainPageLocator.back_btn):
            self.common.poco_click(MainPageLocator.back_btn)
        if self.common.poco_wait_exists(MainPageLocator.chat_list):
            self.common.poco_click(MainPageLocator.chat_list)
        self.skip_login_rush()

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
                        MainPageLocator.nation_check) == '国家/地区', f'進入國家選擇頁面失敗'
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
