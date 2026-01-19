from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class SharePageLocator(BaseLocator):
    """分享頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    copy_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制'),
        iOS=base.data_collation(type_kind='name', type_name='titleLabel', num=0),
    )

    share_text = base.check_device(
        Android=base.data_collation(type_kind='name',type_name='com.huawei.android.internal.app:id/chooser_document_description_title'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )


class SharePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    # app_package = Setting().get_package_name(brand, env)

    def get_share_text(self):
        if self.phone_platform.lower() == 'ios':  # iOS part
            message = self.poco(type='NavigationBar')[1].attr('name')
            share_list = message.split('\n')

            if self.brand == 'chit':
                assert share_list[1].__contains__('下载免费趣聊App，分享乐趣 一起畅聊!')
            else:
                assert share_list[1].__contains__('加强好友间联系！下载免费股聊App，串连好友')

            self.poco(name='actionGroupCell')[0].offspring(label='拷贝').click()
            self.wait_loading_finish()

            return share_list[1], None

        else:  # android part
            message = self.common.poco_get_text(SharePageLocator.share_text)
            share_list = message.split('\n')

            if self.brand == 'chit':
                assert share_list[0].__contains__('下载免费趣聊App，分享乐趣 一起畅聊!')
            else:
                aaa = share_list[0]
                assert share_list[0].__contains__('加强好友间联系！下载免费股聊App，串连好友')

            self.common.poco_click(SharePageLocator.copy_btn)
            self.wait_loading_finish()

            return message, share_list[1]

    # def get_brand_name(self):
    #     if self.brand == 'gu':
    #         name = 'GuChat'
    #     elif self.brand == 'mee':
    #         name = 'MeeChat'
    #     elif self.brand == 'chit':
    #         name = 'ChitChat'
    #     elif self.brand == 'mingpin':
    #         name = '名品会'
    #     return name
