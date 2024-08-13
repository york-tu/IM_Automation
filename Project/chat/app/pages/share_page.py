from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


class SharePageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = SharePageLocator.base.check_device(
            Android=SharePageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=SharePageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    copy_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制'),
        iOS=base.data_collation(type_kind='name', type_name='拷贝'),
    )

    share_text = base.check_device(
        Android=base.data_collation(type_kind='name',type_name='com.huawei.android.internal.app:id/chooser_document_description_title'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='分享股聊.*'),
    )


class SharePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def get_share_text(self):
        if self.common.poco_exists(SharePageLocator.share_text):

            if self.phone_platform.lower() == 'ios':  # iOS part
                message = self.common.poco_get_text(SharePageLocator.share_text)
                # message = self.poco(type='Other')[29].attr('name')
                share_list = message.split('\n')
                name = self.get_brand_name()

                if SharePageLocator.brand == 'chit':
                    assert share_list[1].__contains__('下载免费' + name + 'App，分享乐趣 一起畅聊!')
                else:
                    assert share_list[1].__contains__('加强好友间联系！下载免费' + name + 'App，串连好友')

                self.common.poco_click(SharePageLocator.copy_btn)
                self.wait_loading_finish()

                return share_list[1], None

            else:  # android part
                message = self.common.poco_get_text(SharePageLocator.share_text)
                share_list = message.split('\n')
                name = self.get_brand_name()

                if SharePageLocator.brand == 'chit':
                    assert share_list[0].__contains__('下载免费' + name + 'App，分享乐趣 一起畅聊!')
                else:
                    assert share_list[0].__contains__('加强好友间联系！下载免费' + name + 'App，串连好友')

                self.common.poco_click(SharePageLocator.copy_btn)
                self.wait_loading_finish()

                return message, share_list[1]

    def get_brand_name(self):
        if SharePageLocator.brand == 'gu':
            name = '股聊'
        elif SharePageLocator.brand == 'mee':
            name = '覓聊'
        elif SharePageLocator.brand == 's365':
            name = '365'
        elif SharePageLocator.brand == 'chit':
            name = '趣聊'
        return name
