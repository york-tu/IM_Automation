from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


class FreeUpSpacePageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    # ==================================== 釋出空間 =================================================
    free_up_space_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='释出空间'),
        iOS=base.data_collation(type_kind='name', type_name='释出空间'),
    )
    free_up_space_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=0),
        iOS=base.data_collation(type_kind='name', type_name='释出空间'),
    )
    free_up_space_app_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_app_name'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_cache_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_cache_hint'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_cache_clear_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete', num=-5),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    pops_up_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    pops_up_clear_confirm = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_all_space_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_free_up_all_space_hint'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_cache_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=0),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_other_files_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=-1),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_other_files_clear_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete', num=-1),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_by_chat_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_free_up_space_by_group'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_by_chat_list_first = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=0),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_all_space_from_chat = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_free_up_chat_data_space'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )

    @staticmethod
    def env(env):
        env = FreeUpSpacePageLocator.base.check_device(
            Android=FreeUpSpacePageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=FreeUpSpacePageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env


class FreeUpSpacePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_free_up_space(self, product_name):
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_btn)
        self.wait_loading_finish()
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_title) == '释出空间'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_app_name) == product_name
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_cache_hint) == f'缓存为使用{product_name}时产生的临时储存数据，包含接收他人所发送之各式讯息，清除缓存不会影响应用程式的使用。'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_all_space_hint) == '清除所有聊天室中发送的数据副本，包含图片、视频、语音讯息、其他档案，以及已下载之其他档案。'

    def clear_cache_data(self):
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_cache_clear_btn)
        self.common.poco_wait_exists(FreeUpSpacePageLocator.pops_up_content)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定清除缓存？'
        self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
        sleep(3)
        after_clear_cache_size = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_cache_size).split()[0]
        assert after_clear_cache_size == '0'
        assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_cache_clear_btn, 'enabled') is False

    def clear_all_data(self):
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_other_files_clear_btn)
        self.common.poco_wait_exists(FreeUpSpacePageLocator.pops_up_content)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定清除其他档案？'
        self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
        sleep(3)
        after_clear_other_files_size = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_other_files_size).split()[0]
        assert after_clear_other_files_size == '0'
        assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_other_files_clear_btn, 'enabled') is False

    def clear_data_by_chatroom(self, chatroom):
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_by_chat_btn)
        self.wait_loading_finish()
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_title) == '依聊天室释出空间'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first) == chatroom
        # =================================== 進入列表特定聊天室 =============================================
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_by_chat_list_first)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first) == chatroom
        # ==================== 釋出以上所有空間 ==============================================================
        self.common.poco_click(FreeUpSpacePageLocator.free_up_all_space_from_chat)
        self.common.poco_wait_exists(FreeUpSpacePageLocator.pops_up_content)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定释出所有空间？'
        self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
        sleep(3)
        after_clear_all_size = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_other_files_size).split()[0]
        assert after_clear_all_size == '0'
        # ==================== 返回列表 ==============================================================
        self.common.poco_click(FreeUpSpacePageLocator.back_btn)
        self.wait_loading_finish()
        if self.common.poco_exists(FreeUpSpacePageLocator.free_up_space_by_chat_list_first):
            assert not self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first) == chatroom
        self.common.poco_click(FreeUpSpacePageLocator.back_btn)