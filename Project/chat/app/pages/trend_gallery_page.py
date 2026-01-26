from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class TrendGalleryPageLocator(BaseLocator):
    """趨勢畫廊頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    gallery_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='图库'),
        iOS=base.data_collation(type_kind='name', type_name='图库'),
    )

    trend_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='走势'),
        iOS=base.data_collation(type_kind='name', type_name='走势'),
    )

    widget_page_pops_up = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_root'),
        iOS=base.data_collation(type_kind='name', type_name='xxxx'),
    )

    widget_close_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/layout_assistive_touch'),
        iOS=base.data_collation(type_kind='name', type_name='iconClose'),
    )

    followed_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='已关注'),
        iOS=base.data_collation(type_kind='name', type_name='已关注'),
    )


class TrendAndGalleryPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_gallery_page(self):
        self.common.poco_click(TrendGalleryPageLocator.gallery_button)
        sleep(5)
        if self.phone_platform.lower() == "android":
            assert self.common.poco_exists(TrendGalleryPageLocator.widget_page_pops_up)
        self.common.poco_click(TrendGalleryPageLocator.widget_close_button)
        assert self.common.poco_get_text(TrendGalleryPageLocator.followed_tab) == '已关注', f'未回到上一頁'

    def into_trend_page(self):
        self.common.poco_click(TrendGalleryPageLocator.trend_button)
        sleep(5)
        if self.phone_platform.lower() == "android":
            assert self.common.poco_exists(TrendGalleryPageLocator.widget_page_pops_up)
        self.common.poco_click(TrendGalleryPageLocator.widget_close_button)
        assert self.common.poco_get_text(TrendGalleryPageLocator.followed_tab) == '已关注', f'未回到上一頁'