from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class AboutPageLocator(BaseLocator):
    """關於頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    service_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='服务条款'),
        iOS=base.data_collation(type_kind='name', type_name='服务条款'),
    )

    privacy_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='隐私权政策'),
        iOS=base.data_collation(type_kind='name', type_name='隐私权政策'),
    )

    title_check = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0),
    )

    version = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='使用版本'),
        iOS=base.data_collation(type_kind='name', type_name='使用版本'),
    )

    version_value = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_version_value'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='版本.*'),
    )

    close_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_close'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconCross'),
    )


class AboutPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def check_service(self):
        self.common.poco_click(AboutPageLocator.service_button)
        title = self.common.poco_get_text(AboutPageLocator.title_check)
        assert title == '服务条款', f'服务条款頁面顯示錯誤'
        self.common.poco_click(AboutPageLocator.close_button)

    def check_privacy(self):
        self.common.poco_click(AboutPageLocator.privacy_button)
        title = self.common.poco_get_text(AboutPageLocator.title_check)
        assert title == '隐私权政策', f'隱私權政策頁面顯示錯誤'
        self.common.poco_click(AboutPageLocator.close_button)

    def check_version(self, correct_version=''):
        for loop in range(0, 3):
            if self.common.poco_exists(AboutPageLocator.version):
                info = self.common.poco_get_text(AboutPageLocator.version_value)
                app_version = info.replace('版本', '')

                if correct_version != app_version:
                    message = f'版本錯誤, 目前版本: {app_version} 正確版本: {correct_version}'
                    gl.set_value('VERSION_MESSAGE', message)
                    raise EOFError(message)
                else:
                    break

            if loop == 2:
                message = '找不到版本號碼'
                raise EOFError(message)
