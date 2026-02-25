from os import close
from time import sleep

from airtest.core.api import touch

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class NotificationPageLocator(BaseLocator):
    """通知頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    notify_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭后，手机将不再接受新讯息通知'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', pos=[0.5, 0.7807881773399015]),
    )

    notify_switch = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_new_notify'),
        iOS=base.data_collation(type_kind='type', type_name='Switch', num=0),
    )

    detail_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭后，收到新讯息时，通知提示将不显示发信人与内容摘要'),
        iOS=base.data_collation(type_kind='name', type_name='讯息通知'),
    )

    detail_switch = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_notify_detail'),
        iOS=base.data_collation(type_kind='type', type_name='Switch', num=-3),
    )

    voice_switch = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_notify_voice'),
        iOS=base.data_collation(type_kind='type', type_name='Switch', num=-2),
    )

    vibration_switch = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_notify_vibration'),
        iOS=base.data_collation(type_kind='type', type_name='Switch', num=-1),
    )

    close_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认关闭'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', pos=[0.5, 0.8429802955665024]),
    )

    cancel_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='取消'),
        iOS=base.data_collation(type_kind='name', type_name='讯息通知'),
    )


class NotificationPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def turn_notify_switch(self):

        if self.phone_platform.lower() == 'android':
            if self.common.poco_get_attr(NotificationPageLocator.notify_switch, 'checked') is True:
                num = 2
            else:
                num = 1

            for _ in range(num):
                self.common.poco_click(NotificationPageLocator.notify_switch)
                if self.common.poco_wait_exists(NotificationPageLocator.notify_check):
                    self.common.poco_click(NotificationPageLocator.close_button)

                    assert not self.common.poco_get_attr(NotificationPageLocator.detail_switch,'enabled'), f'詳情開關沒有鎖定'
                    assert not self.common.poco_get_attr(NotificationPageLocator.voice_switch,'enabled'), f'聲音開關沒有鎖定'
                    assert not self.common.poco_get_attr(NotificationPageLocator.vibration_switch,'enabled'), f'震動開關沒有鎖定'
                else:
                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch,'enabled'), f'詳情開關沒有開啟'
                    assert self.common.poco_get_attr(NotificationPageLocator.voice_switch,'enabled'), f'聲音開關沒有開啟'
                    assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch,'enabled'), f'震動開關沒有開啟'

        # ============================ iOS scenario =====================================
        else:
            if self.common.poco_get_attr(NotificationPageLocator.notify_switch, 'value') == '1':  # 新訊息通知開啟(1)關閉(0)
                num = 2
            else:
                num = 1

            for _ in range(num):
                self.common.poco_long_click(NotificationPageLocator.notify_switch)
                if self.common.poco_wait_exists(NotificationPageLocator.notify_check):
                    self.common.poco_click(NotificationPageLocator.close_button)

                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch, 'isEnabled') == '0', f'詳情開關沒有被鎖定'
                    assert self.common.poco_get_attr(NotificationPageLocator.voice_switch, 'isEnabled') == '0', f'聲音開關沒有被鎖定'
                    assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'isEnabled') == '0', f'震動開關沒有沒有被鎖定'
                else:
                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch, 'isEnabled') == '1', f'詳情開關沒有enable'
                    assert self.common.poco_get_attr(NotificationPageLocator.voice_switch, 'isEnabled') == '1', f'聲音開關沒有enable'
                    assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'isEnabled') == '1', f'震動開關沒有enable'

    def turn_detail_switch(self):
        if self.phone_platform.lower() == 'android':
            if self.common.poco_get_attr(NotificationPageLocator.notify_switch, 'checked'):
                num = 2
            else:
                num = 1

            for _ in range(num):
                if not self.common.poco_get_attr(NotificationPageLocator.detail_switch, 'checked'):
                    self.common.poco_click(NotificationPageLocator.detail_switch)
                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch,'checked'), f'詳情開關沒有開啟'
                else:
                    self.common.poco_click(NotificationPageLocator.detail_switch)
                    if self.common.poco_wait_exists(NotificationPageLocator.detail_check):
                        self.common.poco_click(NotificationPageLocator.close_button)
                    assert not self.common.poco_get_attr(NotificationPageLocator.detail_switch,'checked'), f'詳情開關沒有關閉'
        # ============================ iOS scenario =====================================
        else:
            if self.common.poco_get_attr(NotificationPageLocator.notify_switch, 'value') == '1':
                num = 2
            else:
                num = 1

            for _ in range(num):
                if self.common.poco_get_attr(NotificationPageLocator.detail_switch, 'value') == '0':
                    self.common.poco_long_click(NotificationPageLocator.detail_switch)
                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch,'value'), f'通知訊息顯示詳情開關沒有開啟'
                else:
                    self.common.poco_long_click(NotificationPageLocator.detail_switch)
                    self.common.poco_wait_exists(NotificationPageLocator.detail_check)
                    self.common.poco_click(NotificationPageLocator.close_button)
                    assert self.common.poco_get_attr(NotificationPageLocator.detail_switch,'value') == '0', f'通知訊息顯示詳情開關沒有關閉'

    def turn_voice_switch(self):
        self.wait_loading_finish()
        if self.phone_platform.lower() == 'android':

            if not self.common.poco_get_attr(NotificationPageLocator.voice_switch, 'checked'):  # 當初始狀態為"關閉"
                self.common.poco_click(NotificationPageLocator.voice_switch)
                assert self.common.poco_get_attr(NotificationPageLocator.voice_switch,'checked'), f'聲音開關沒有開啟'
            else:  # 當初始狀態為"開啟"
                self.common.poco_click(NotificationPageLocator.voice_switch)
                assert not self.common.poco_get_attr(NotificationPageLocator.voice_switch,'checked'), f'聲音開關沒有關閉'

                self.common.poco_click(NotificationPageLocator.voice_switch)
        # ============================ iOS scenario =====================================
        else:
            if self.common.poco_get_attr(NotificationPageLocator.voice_switch, 'value') == '0':
                self.common.poco_long_click(NotificationPageLocator.voice_switch)
                sleep(3)
                assert self.common.poco_get_attr(NotificationPageLocator.voice_switch,'value') == '1', f'聲音開關沒有開啟'
            else:
                self.common.poco_long_click(NotificationPageLocator.voice_switch)
                sleep(3)
                assert self.common.poco_get_attr(NotificationPageLocator.voice_switch,'value') == '0', f'聲音開關沒有關閉'

                self.common.poco_long_click(NotificationPageLocator.voice_switch)

    def turn_vibration_switch(self):
        self.wait_loading_finish()
        if self.phone_platform.lower() == 'android':
            if not self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'checked'):  # 當初始狀態為"關閉"
                self.common.poco_click(NotificationPageLocator.vibration_switch)
                assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch,'checked'), f'震動開關沒有開啟'
            else:
                self.common.poco_click(NotificationPageLocator.vibration_switch)
                assert not self.common.poco_get_attr(NotificationPageLocator.vibration_switch,'checked'), f'震動開關沒有關閉'

                self.common.poco_click(NotificationPageLocator.vibration_switch)
        # ============================ iOS scenario =====================================
        else:
            if self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'value') == '0':
                self.common.poco_long_click(NotificationPageLocator.vibration_switch)
                assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'value') == '1', f'震動開關沒有開啟'
            else:
                self.common.poco_long_click(NotificationPageLocator.vibration_switch)
                assert self.common.poco_get_attr(NotificationPageLocator.vibration_switch, 'value') == '0', f'震動開關沒有關閉'

                self.common.poco_long_click(NotificationPageLocator.vibration_switch)
