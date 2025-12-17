from time import sleep
from datetime import datetime, timedelta
# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
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
        iOS=base.data_collation(type_kind='name', type_name='setting_credit_cell'),
    )

    point_page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='xxxx'),
    )

    point_total = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_point'),
        iOS=base.data_collation(type_kind='name', type_name='credit_totalAmount_label'),
    )

    point_value = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_value'),
        iOS=base.data_collation(type_kind='name', type_name='credit_recordCell_amount_label')
    )

    point_type = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_type'),
        iOS=base.data_collation(type_kind='name', type_name='credit_recordCell_tradingType_label')
    )

    point_status = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_state'),
        iOS=base.data_collation(type_kind='name', type_name='credit_recordCell_status_label')
    )

    point_date = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_date'),
        iOS=base.data_collation(type_kind='name', type_name='credit_recordCell_time_label')
    )
    main_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_my_button')
    )
    main_functions_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_menu_button')
    )

class PointPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_point_record(self):
        if self.common.poco_exists(PointPageLocator.main_btn):
            self.common.poco_click(PointPageLocator.main_btn)
        if self.common.poco_exists(PointPageLocator.main_functions_btn):
            self.common.poco_click(PointPageLocator.main_functions_btn)
        self.common.poco_click(PointPageLocator.point_button)
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_text(PointPageLocator.point_page_title) == '积分', f'非積分頁'

    def check_point_record(self, grab_type, grab_amount, grab_time):
        assert self.common.poco_get_text(PointPageLocator.point_value) == grab_amount, f'積分領取錯誤'
        assert self.common.poco_get_text(PointPageLocator.point_type) == grab_type, f'積分類型錯誤'
        assert self.common.poco_get_text(PointPageLocator.point_status) == '成功', f'領取失敗'
        actual_grab_time = self.common.poco_get_text(PointPageLocator.point_date).replace('\n', ' ')

        expected = datetime.strptime(grab_time, "%Y-%m-%d %H:%M")
        actual = datetime.strptime(actual_grab_time, "%Y-%m-%d %H:%M")
        # 誤差 ±1 分鐘
        tolerance = timedelta(minutes=1)
        assert abs(expected - actual) <= tolerance

        # assert actual_grab_time == grab_time, f'領取時間有誤, 預期:{grab_time},實際:{actual_grab_time}'
        return self.common.poco_get_text(PointPageLocator.point_total)
