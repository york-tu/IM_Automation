from time import sleep

from Project.chat.app.pages.main_page import MainPage, MainPageLocator
from Project.chat.app.pages.social_home_page import SocialHomePage
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class PrivacyPageLocator(BaseLocator):
    """隱私頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    # 功能表 > 隱私
    privacy_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='隐私'),
        iOS=base.data_collation(type_kind='name', type_name='setting_privacy_cell'),
    )
    page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_toolbar_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0),
    )
    # 功能表 > 隱私 > 按贊貼文
    liked_post_privacy_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_sns_like_post_setting'),
        iOS=base.data_collation(type_kind='name', type_name='privacySettings_likePostAudience_cell'),
    )
    # 功能表 > 隱私 > 按贊貼文: 目前設定
    current_privacy = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_sns_like_post_privacy_option_title'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 功能表 > 隱私 > 按贊貼文 > 所有人
    privacy_all_option = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_everyone'),
        iOS=base.data_collation(type_kind='name', type_name='updateSnsLikePostAudience_open_view'),
    )
    # 功能表 > 隱私 > 按贊貼文 > 僅自己
    privacy_self_option = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_only_self'),
        iOS=base.data_collation(type_kind='name', type_name='updateSnsLikePostAudience_privates_view'),
    )
    # 功能表 > 隱私 > 按贊貼文 > 儲存
    privacy_save_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_save'),
        iOS=base.data_collation(type_kind='name', type_name='updateSnsLikePostAudience_save_button'),
    )


def account_privacy_select(privacy_index):
    privacy_list = [PrivacyPageLocator.privacy_all_option,
                    PrivacyPageLocator.privacy_self_option]
    return privacy_list[privacy_index]


class PrivacyPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_privacy_page(self):
        self.common.poco_click(MainPageLocator.main_btn)
        self.common.poco_click(MainPageLocator.mine_menu_btn)
        self.common.poco_click(PrivacyPageLocator.privacy_button)
        assert self.common.poco_get_text(PrivacyPageLocator.page_title) == '隐私'

    def change_privacy(self, privacy_index):
        self.common.poco_click(PrivacyPageLocator.liked_post_privacy_btn)
        self.common.poco_click(account_privacy_select(privacy_index))
        option_select = self.common.poco_get_text(account_privacy_select(privacy_index))
        self.common.poco_click(PrivacyPageLocator.privacy_save_btn)

        if self.phone_platform.lower() == 'android':
            privacy_display = self.common.poco_get_text(PrivacyPageLocator.current_privacy)
        else:
            privacy_display = self.poco(name='privacySettings_likePostAudience_cell').offspring(type='StaticText')[-1].attr('label')
        assert option_select == privacy_display


