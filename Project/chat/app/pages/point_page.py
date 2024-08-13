from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPage, MainPageLocator
import logging
import common.utils.globalvar as gl


class PointPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = PointPageLocator.base.check_device(
            Android=PointPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=PointPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    point_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='积分'),
        iOS=base.data_collation(type_kind='name', type_name='积分'),
    )

    point_page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='xxxx'),
    )

    point_total = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_point'),
        iOS=base.data_collation(type_kind='name', type_name='xxxx'),
    )

    point_value = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_value'),
        iOS=base.data_collation(type_kind='name', type_name='xxx')
    )

    point_type = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_type'),
        iOS=base.data_collation(type_kind='name', type_name='xxx')
    )

    point_status = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_state'),
        iOS=base.data_collation(type_kind='name', type_name='tv_type ')
    )

    point_date = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_date'),
        iOS=base.data_collation(type_kind='name', type_name='tv_type ')
    )


class PointPage(Base):

    def into_point_record(self):
        if self.common.poco_exists(MainPageLocator.mine_button):
            self.common.poco_click(MainPageLocator.mine_button)
        if self.common.poco_exists(MainPageLocator.mine_menu_btn):
            self.common.poco_click(MainPageLocator.mine_menu_btn)
        self.common.poco_click(PointPageLocator.point_button)
        assert self.common.poco_get_text(PointPageLocator.point_page_title) == '积分', f'非積分頁'

    def check_point_record(self, grab_type, grab_amount, grab_time):
        assert self.common.poco_get_text(PointPageLocator.point_value) == grab_amount, f'積分領取錯誤'
        assert self.common.poco_get_text(PointPageLocator.point_type) == grab_type, f'積分類型錯誤'
        assert self.common.poco_get_text(PointPageLocator.point_status) == '成功', f'領取失敗'
        assert self.common.poco_get_text(PointPageLocator.point_date) == grab_time, f'領取時間有誤'
        return self.common.poco_get_text(PointPageLocator.point_total)
