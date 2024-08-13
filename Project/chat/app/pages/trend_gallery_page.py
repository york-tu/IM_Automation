from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPageLocator
import logging
import common.utils.globalvar as gl


class TreadGalleryPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)


    @staticmethod
    def env(env):
        env = TreadGalleryPageLocator.base.check_device(
            Android=TreadGalleryPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=TreadGalleryPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    gallery_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='图库'),
        iOS=base.data_collation(type_kind='name', type_name='图库'),
    )

    tread_button = base.check_device(
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


class TreadAndGalleryPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_gallery_page(self):
        self.common.poco_click(TreadGalleryPageLocator.gallery_button)
        sleep(5)
        if self.phone_platform == "Android":
            assert self.common.poco_exists(TreadGalleryPageLocator.widget_page_pops_up)
        self.common.poco_click(TreadGalleryPageLocator.widget_close_button)
        assert self.common.poco_get_text(TreadGalleryPageLocator.followed_tab) == '已关注', f'未回到上一頁'

    def into_tread_page(self):
        self.common.poco_click(TreadGalleryPageLocator.tread_button)
        sleep(5)
        if self.phone_platform == "Android":
            assert self.common.poco_exists(TreadGalleryPageLocator.widget_page_pops_up)
        self.common.poco_click(TreadGalleryPageLocator.widget_close_button)
        assert self.common.poco_get_text(TreadGalleryPageLocator.followed_tab) == '已关注', f'未回到上一頁'