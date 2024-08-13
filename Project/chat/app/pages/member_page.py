from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPage, MainPageLocator
import logging
import common.utils.globalvar as gl


class MemberPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = MemberPageLocator.base.check_device(
            Android=MemberPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=MemberPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        return env

    notification_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='讯息通知'),
        iOS=base.data_collation(type_kind='name', type_name='讯息通知'),
    )

    notification_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='震动'),
        iOS=base.data_collation(type_kind='name', type_name='震动'),
    )

    security_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号与安全'),
        iOS=base.data_collation(type_kind='name', type_name='帐号与安全'),
    )

    security_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='手机号'),
        iOS=base.data_collation(type_kind='name', type_name='手机号'),
    )

    blacklist_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='黑名单'),
        iOS=base.data_collation(type_kind='name', type_name='黑名单'),
    )

    blacklist_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='黑名单'),
        iOS=base.data_collation(type_kind='name', type_name='黑名单'),
    )

    share_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='分享'),
        iOS=base.data_collation(type_kind='name', type_name='分享'),
    )

    share_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制'),
        iOS=base.data_collation(type_kind='name', type_name='拷贝'),
    )

    about_button = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='关于.*聊'),
        iOS=base.data_collation(type_kind='name', type_name='关于股聊'),
    )

    about_button_365 = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='关于365'),
        iOS=base.data_collation(type_kind='name', type_name='关于股聊'),
    )

    about_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='使用版本'),
        iOS=base.data_collation(type_kind='name', type_name='使用版本'),
    )

    user_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_username'),
        iOS=base.data_collation(type_kind='name', type_name='Image', pos=[0.9323671497584541, 0.13002232142857142] ),
    )

    user_id = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_id_value'),
        iOS=base.data_collation(type_kind='name', type_name='关于股聊'),
    )

    nick_name_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='昵称'),
        iOS=base.data_collation(type_kind='name', type_name='昵称'),
    )

    clear_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon_left_of_selector'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本'),
    )

    nick_name_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='填写眤称'),
        iOS=base.data_collation(type_kind='name', type_name='TextField'),
    )
    nickname_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text'),
        iOS=base.data_collation(type_kind='name', type_name='TextField'),
    )
    self_introduction_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_introduction'),
        iOS=base.data_collation(type_kind='name', type_name='TextView', num=-1),
    )
    user_id_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='用户ID'),
        iOS=base.data_collation(type_kind='name', type_name='用户ID'),
    )
    save_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='保存'),
        iOS=base.data_collation(type_kind='name', type_name='保存'),
    )
    edit_profile_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='编辑主页'),
        iOS=base.data_collation(type_kind='name', type_name='编辑主页'),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='返回'),
    )
    main_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':tv_description'),
        iOS=base.data_collation(type_kind='name', type_name='back'),
    )

class MemberPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_edit(self):
        if self.common.poco_wait_exists(MemberPageLocator.edit_profile_btn):
            self.common.poco_click(MemberPageLocator.edit_profile_btn)
        assert self.common.poco_wait_exists(MemberPageLocator.nick_name_title), f'進入編輯主頁錯誤'

    def into_notification(self):
        if self.common.poco_wait_exists(MemberPageLocator.notification_button):
            self.common.poco_click(MemberPageLocator.notification_button)
        assert self.common.poco_wait_exists(MemberPageLocator.notification_check), f'進入訊息通知頁面錯誤'

    def into_security(self):
        if self.common.poco_wait_exists(MemberPageLocator.security_button):
            self.common.poco_click(MemberPageLocator.security_button)
        assert self.common.poco_wait_exists(MemberPageLocator.security_check), f'進入帳號安全頁面錯誤'

    def into_blacklist(self):
        if self.common.poco_wait_exists(MemberPageLocator.blacklist_button):
            self.common.poco_click(MemberPageLocator.blacklist_button)
        assert self.common.poco_wait_exists(MemberPageLocator.blacklist_check), f'進入黑名單頁面錯誤'

    def into_share(self):
        if self.common.poco_wait_exists(MemberPageLocator.share_button):
            self.common.poco_click(MemberPageLocator.share_button)
        assert self.common.poco_wait_exists(MemberPageLocator.share_check), f'進入分享頁面錯誤'

    def into_about(self):
        if gl.get_value('BRAND') == 's365':
            if self.common.poco_wait_exists(MemberPageLocator.about_button_365):
                self.common.poco_click(MemberPageLocator.about_button_365)
        else:
            if self.common.poco_wait_exists(MemberPageLocator.about_button):
                self.common.poco_click(MemberPageLocator.about_button)

        assert self.common.poco_wait_exists(MemberPageLocator.about_check), f'進入關於聊天頁面錯誤'

    def get_nickname(self):
        data = self.common.poco_get_text(MemberPageLocator.nickname_column)
        return data

    def get_self_introduction(self):
        data = self.common.poco_get_text(MemberPageLocator.self_introduction_column)
        return data

    def change_nickname(self, new_nickname):
        self.common.poco_click(MemberPageLocator.nickname_column)  # 點 暱稱欄位
        self.common.poco_click(MemberPageLocator.clear_button)  # 在暱稱頁面 > 點[x]清除欄位
        if self.phone_platform.lower() == 'android':
            self.common.poco_send_text(MemberPageLocator.nick_name_input, new_nickname)
            sleep(3)
            user_name = self.common.poco_get_text(MemberPageLocator.nickname_column)
            assert user_name == new_nickname, f'編輯主頁_暱稱修改失敗'
            if self.common.poco_wait_exists(MemberPageLocator.back_btn):
                self.common.poco_click(MemberPageLocator.back_btn)
        else:
            self.common.poco_send_text(MemberPageLocator.nick_name_input, new_nickname)
            sleep(3)
            user_name = self.common.poco_get_attr(MemberPageLocator.nickname_column, 'value')
            assert user_name == new_nickname, f'編輯主頁_暱稱修改失敗'
            self.common.poco_click(MemberPageLocator.user_id_title)
            self.common.poco_click(MemberPageLocator.save_btn)

        sleep(1)
        main_nickname = self.common.poco_get_text(MainPageLocator.main_nickname)
        assert main_nickname == new_nickname, f'個人主頁_個人暱稱顯示錯誤'
        self.common.poco_click(MemberPageLocator.edit_profile_btn)

    def change_introduction(self, text):
        self.common.poco_click(MemberPageLocator.self_introduction_column)  # 點 個人簡介欄位
        self.common.poco_long_click(MemberPageLocator.self_introduction_column)  # 在暱稱頁面 > 點[x]清除欄位

        if self.phone_platform == 'Android':
            self.poco(text='全选').click()
            self.common.poco_send_text(MemberPageLocator.self_introduction_column, text)
            sleep(3)
            self_instruction = self.common.poco_get_text(MemberPageLocator.self_introduction_column)
            assert self_instruction == text, f'編輯主頁_個人簡介編輯錯誤'
            self.poco.swipe([0.5, 0.1], [0.5, 0.5], duration=0.1)

            if self.common.poco_wait_exists(MemberPageLocator.back_btn):
                self.common.poco_click(MemberPageLocator.back_btn)
        else:
            self.poco(name='全选').click()
            self.common.poco_send_text(MemberPageLocator.self_introduction_column, text)
            sleep(3)
            self_instruction = self.common.poco_get_attr(MemberPageLocator.self_introduction_column, 'value')

            assert self_instruction == text, f'編輯主頁_個人簡介編輯錯誤'

            self.common.poco_click(MemberPageLocator.user_id_title)
            self.common.poco_click(MemberPageLocator.save_btn)

        sleep(1)
        main_description = self.common.poco_get_text(MainPageLocator.main_description)
        assert main_description == text, f'個人主頁_個人簡介顯示錯誤'
        self.common.poco_click(MemberPageLocator.edit_profile_btn)





