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

    # security_check_change_pw = base.check_device(
    #     Android=base.data_collation(type_kind='nameMatches', type_name='.*密码'),
    #     iOS=base.data_collation(type_kind='name', type_name='更改密码'),
    # )
    logout = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='登出'),
        iOS=base.data_collation(type_kind='name', type_name='登出')
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
        iOS=base.data_collation(type_kind='name', type_name='setting_share_cell'),
    )

    share_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制'),
        iOS=base.data_collation(type_kind='name', type_name='titleLabel', num=0),
    )

    about_button = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='关于.*'),
        iOS=base.data_collation(type_kind='name', type_name='setting_aboutApp_cell'),
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
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text'),
        iOS=base.data_collation(type_kind='name', type_name='TextField'),
    )
    main_nickname_display = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='name', type_name='TextField'),
    )
    self_introduction_input = base.check_device(
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
        iOS=base.data_collation(type_kind='name', type_name='myProfile_editMyInfoPage_button'),
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='返回'),
    )
    main_description_display = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_introduction_label'),
    )
    toast_wordings = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='请勿包含.*'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='请勿包含.*'),
    )
    toast_confirm_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确定'),
        iOS=base.data_collation(type_kind='name', type_name='确定'),
    )


class MemberPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    phone_name = gl.get_value('PHONE_NAME')

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
        assert self.common.poco_wait_exists(MemberPageLocator.logout), f'進入帳號安全頁面錯誤'

    def into_blacklist(self):
        if self.common.poco_wait_exists(MemberPageLocator.blacklist_button):
            self.common.poco_click(MemberPageLocator.blacklist_button)
        assert self.common.poco_wait_exists(MemberPageLocator.blacklist_check), f'進入黑名單頁面錯誤'

    def into_share(self):
        if self.common.poco_wait_exists(MemberPageLocator.share_button):
            self.common.poco_click(MemberPageLocator.share_button)
        self.wait_loading_finish()
        if self.phone_name == 'IPHONE_13':
            assert self.common.poco_get_attr(MemberPageLocator.share_check, 'value') == '拷贝'
        else:
            assert self.common.poco_wait_exists(MemberPageLocator.share_check), f'進入分享頁面錯誤'

    def into_about(self):
        if self.common.poco_wait_exists(MemberPageLocator.about_button):
            self.common.poco_click(MemberPageLocator.about_button)

        assert self.common.poco_wait_exists(MemberPageLocator.about_check), f'進入關於聊天頁面錯誤'

    def get_nickname(self):
        data = self.common.poco_get_text(MemberPageLocator.main_description_display)
        return data

    def get_self_introduction(self):
        data = self.common.poco_get_text(MemberPageLocator.main_nickname_display)
        return data

    def change_nickname(self, new_nickname):
        self.common.poco_click(MemberPageLocator.clear_button)  # 在暱稱頁面 > 點[x]清除欄位

        self.common.poco_send_text(MemberPageLocator.nick_name_input, new_nickname)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(MemberPageLocator.user_id_title)
        self.common.poco_click(MemberPageLocator.save_btn)
        main_nickname = self.common.poco_get_text(MainPageLocator.main_nickname)

        # if self.phone_platform.lower() == 'android':
        #     self.common.poco_send_text(MemberPageLocator.nick_name_input, new_nickname)
        #     self.common.poco_click(MemberPageLocator.save_btn)
        #     main_nickname = self.common.poco_get_text(MainPageLocator.main_nickname)
        # else:
        #     self.common.poco_send_text(MemberPageLocator.nick_name_input, new_nickname)
        #     self.common.poco_click(MemberPageLocator.user_id_title)
        #     self.common.poco_click(MemberPageLocator.save_btn)
        #     main_nickname = self.poco(type="StaticText").attr('value')

        assert main_nickname == new_nickname, f'個人主頁_個人暱稱顯示錯誤, 預期{new_nickname},實際{main_nickname}'
        self.common.poco_click(MemberPageLocator.edit_profile_btn)

    def change_introduction(self, text):
        if self.phone_platform.lower() == 'android':
            self.common.poco_send_text(MemberPageLocator.self_introduction_input, text)
            self.common.poco_click(MemberPageLocator.save_btn)
        else:
            while not self.poco(name='全选').exists():
                self.common.poco_long_click(MemberPageLocator.self_introduction_input)  # 個人簡介欄位長按
            self.poco(name='全选').click()
            self.common.poco_send_text(MemberPageLocator.self_introduction_input, text)
            self.common.poco_click(MemberPageLocator.user_id_title)
            self.common.poco_click(MemberPageLocator.save_btn)
        self.wait_loading_finish()
        main_description = self.common.poco_get_text(MainPageLocator.main_description)
        assert main_description == text, f'個人主頁_個人簡介顯示錯誤, 預期{text},實際{main_description}'
        self.common.poco_click(MemberPageLocator.edit_profile_btn)

    def input_block_words_then_check_toast(self, block_words):
        if self.phone_platform.lower() == 'android':
            self.common.poco_send_text(MemberPageLocator.self_introduction_input, block_words)
            self.common.poco_click(MemberPageLocator.save_btn)
            actual_wordings = self.common.poco_get_text(MemberPageLocator.toast_wordings)
            assert actual_wordings == f'请勿包含{block_words}', '錯誤訊息有誤'
            self.common.poco_click(MemberPageLocator.toast_confirm_btn)
            self.wait_loading_finish()
            self.common.poco_click(MemberPageLocator.back_btn)
        else:
            self.common.poco_long_click(MemberPageLocator.self_introduction_input)  # 個人簡介欄位長按
            self.poco(name='全选').click()
            self.common.poco_send_text(MemberPageLocator.self_introduction_input, block_words)
            self.common.poco_click(MemberPageLocator.user_id_title)
            self.common.poco_click(MemberPageLocator.save_btn)
            actual_wordings = self.common.poco_get_text(MemberPageLocator.toast_wordings)
            assert actual_wordings == f'请勿包含{block_words}', '錯誤訊息有誤'
            self.common.poco_click(MemberPageLocator.toast_confirm_btn)
            self.wait_loading_finish()
            self.common.poco_click(MemberPageLocator.back_btn)

        # self.common.poco_click(MemberPageLocator.self_introduction_input)  # 點 個人簡介欄位
        # for _ in range(3):
        #     self.common.poco_long_click(MemberPageLocator.self_introduction_input)  # 欄位上長按 >>> 出現選單
        #     sleep(1)
        #
        # if self.phone_platform == 'Android':
        #     self.poco(text='全选').click()
        #     self.common.poco_send_text(MemberPageLocator.self_introduction_input, block_words)
        #     self.common.poco_click(MemberPageLocator.save_btn)
        #     actual_wordings = self.common.poco_get_text(MemberPageLocator.toast_wordings)
        #     assert actual_wordings == f'请勿包含{block_words}', '錯誤訊息有誤'
        #     self.common.poco_click(MemberPageLocator.toast_confirm_btn)
        #     self.wait_loading_finish()
        #     self.common.poco_click(MemberPageLocator.back_btn)


