from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
from Project.chat.app.pages.base_page import BaseLocator as BasePageLocator
import logging
import common.utils.globalvar as gl


class FreeUpSpacePageLocator(BaseLocator):
    """釋出空間頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    # ==================================== 釋出空間 =================================================
    free_up_space_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='释出空间'),
        iOS=base.data_collation(type_kind='name', type_name='setting_freeUpSpace_cell'),
    )
    free_up_space_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=0),
        iOS=base.data_collation(type_kind='type', type_name='StaticText'),
    )
    free_up_space_app_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_app_name'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    free_up_space_cache_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_cache_hint'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='缓存为使用.*'),
    )
    free_up_space_cache_clear_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete', num=-5),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearCache_button'),
    )
    pops_up_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='确定.*'),
    )
    pops_up_clear_confirm = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='清除',
                                parent={
                                    'type_kind': 'type',
                                    'type_name': 'ScrollView',
                                    'index': -1
                                }),
    )
    free_up_all_chat_data_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_free_up_chat_data_space'),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearAllChatData_cell'),
    )
    free_up_all_space_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_free_up_all_space_hint'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='清除所有.*'),
    )
    free_up_space_cache_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=0),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearCacheSize_label'),
    )
    free_up_space_other_files_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearChatDataSize_file_label', num=-1),
    )
    free_up_space_other_files_clear_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearChatData_file_button'),
    )
    free_up_space_by_chat_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_free_up_space_by_group'),
        iOS=base.data_collation(type_kind='name', type_name='freeUpSpace_clearIndividualChatData_cell'),
    )
    free_up_space_by_chat_list_first = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=0),
        iOS=base.data_collation(type_kind='name', type_name='clearChatDataGroupList_name_label', num=0),
    )
    free_up_space_by_chat_list_second = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=1),
        iOS=base.data_collation(type_kind='name', type_name='clearChatDataGroupList_name_label', num=1),
    )
    free_up_space_by_chat_list_first_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=0),
        iOS=base.data_collation(type_kind='name', type_name='clearChatDataGroupList_chatDataSize_label', num=0),
    )
    free_up_space_by_chat_list_second_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=1),
        iOS=base.data_collation(type_kind='name', type_name='clearChatDataGroupList_chatDataSize_label', num=1),
    )
    free_up_space_by_chat_other_files_size = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_size', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='clearGroupChatData_clearChatDataSize_file_label'),
    )
    free_up_all_space_from_chat = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_free_up_chat_data_space'),
        iOS=base.data_collation(type_kind='name', type_name='释出以上所有空间'),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button'),
    )


class FreeUpSpacePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    phone_name = gl.get_value('PHONE_NAME')
    brand = gl.get_value('BRAND')

    if brand.lower() == 'mingpin':
        brand_name = 'MingPinChat'
    elif brand.lower() == 'gu':
        brand_name = 'GuChat'
    elif brand.lower() == 'chit':
        brand_name = 'ChitChat'

    def into_free_up_space(self, product_name):
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_btn)
        sleep(3)
        # 優化：iOS 使用更短的等待時間
        # if self.phone_platform.lower() == 'ios':
        #     # iOS 快速檢查載入完成（最多等待 3 秒）
        #     for i in range(6):  # 6 * 0.5 = 3 秒
        #         if not self.common.poco_exists(BasePageLocator.loading):
        #             break
        #         sleep(0.5)
        # else:
        #     self.wait_loading_finish()
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_title) == '释出空间'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_cache_hint) == f'缓存为使用{product_name}时产生的临时储存数据，包含接收他人所发送之各式讯息，清除缓存不会影响应用程式的使用。'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_all_space_hint) == '清除所有聊天室中发送的数据副本，包含图片、视频、语音讯息、其他档案，以及已下载之其他档案。'

    def clear_cache_data(self):  # 釋出空間 > "緩存" > 清除
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_cache_clear_btn)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定清除缓存？'
        if self.phone_platform.lower() == 'android':
            self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
            assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_cache_clear_btn, 'enabled') is False
        else:
            self.poco(name='ScrollView').offspring(name='清除').click()
            a = self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_cache_clear_btn, 'isEnabled')
            assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_cache_clear_btn, 'isEnabled') == "0", f'實際:{a}'
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_cache_size).split()[0] == '0'

    def clear_all_chat_data(self):  # 釋出空間 > "釋出所有空間"
        self.common.poco_click(FreeUpSpacePageLocator.free_up_all_chat_data_btn)
        sleep(1)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定释出所有空间？'
        if self.phone_platform.lower() == 'android':
            self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
            assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_by_chat_btn, 'enabled') is False
        else:
            self.poco(name='ScrollView').offspring(name='清除').click()
        
        # 優化：限制返回按鈕點擊次數，避免無限循環（最多點擊 5 次）
        back_click_count = 0
        max_back_clicks = 3
        while self.common.poco_exists(FreeUpSpacePageLocator.back_btn) and back_click_count < max_back_clicks:
            self.common.poco_click(FreeUpSpacePageLocator.back_btn)
            back_click_count += 1
            sleep(0.3)  # 減少等待時間（從可能的更長等待減少）

    def clear_other_files(self):  # 釋出空間 > "其他檔案" > 清除
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_other_files_clear_btn)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定清除其他档案？'

        if self.phone_platform.lower() == 'android':
            self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
            assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_other_files_clear_btn, 'enabled') is False
        else:
            self.poco(name='ScrollView').offspring(name='清除').click()
            assert self.common.poco_get_attr(FreeUpSpacePageLocator.free_up_space_other_files_clear_btn, 'isEnabled') == "0"
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_other_files_size).split()[0] == '0'

    def clear_data_by_chatroom(self):  # 釋出空間 > 依聊天室釋出空間 > 第一聊天室 > "釋出以上所有空間"
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_by_chat_btn)
        # 優化：iOS 使用更短的等待時間
        # if self.phone_platform.lower() == 'ios':
        #     # iOS 快速檢查載入完成（最多等待 3 秒）
        #     for i in range(6):  # 6 * 0.5 = 3 秒
        #         if not self.common.poco_exists(BasePageLocator.loading):
        #             break
        #         sleep(0.5)
        # else:
        #     self.wait_loading_finish()
        sleep(1.5)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_title) == '依聊天室释出空间'
        chatDataGroupListFirst = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first)
        # ====================== 列表依佔用容量降幕排序 =============================================
        firstChatSizeText = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first_size)
        secondChatSizeText = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_second_size)

        if firstChatSizeText.split()[1] == 'MB':
            firstChatSize = float(firstChatSizeText.split()[0])*1000
        else:
            firstChatSize = firstChatSizeText.split()[0]

        if secondChatSizeText.split()[1] == 'MB':
            secondChatSize = float(secondChatSizeText.split()[0])*1000
        else:
            secondChatSize = secondChatSizeText.split()[0]

        assert float(firstChatSize) > float(secondChatSize)
        # ====================== 進入列表特定聊天室 =============================================
        self.common.poco_click(FreeUpSpacePageLocator.free_up_space_by_chat_list_first)
        if self.phone_platform.lower() == 'android':
            pageTitle = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first)
        else:
            pageTitle = self.poco(name=f'{self.brand_name}.ClearGroupChatDataView').offspring(type='StaticText').attr('value')
        assert pageTitle == chatDataGroupListFirst
        # --------------------- 釋出以上所有空間 -----------------------
        self.common.poco_click(FreeUpSpacePageLocator.free_up_all_space_from_chat)
        assert self.common.poco_get_text(FreeUpSpacePageLocator.pops_up_content) == '确定释出所有空间？'

        if self.phone_platform.lower() == 'android':
            self.common.poco_click(FreeUpSpacePageLocator.pops_up_clear_confirm)
        else:
            self.poco(name='ScrollView').offspring(name='清除').click()
        assert self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_other_files_size).split()[0] == '0'
        # ==================== 返回"依聊天室釋出空間"列表 ==============================================================
        self.common.poco_click(FreeUpSpacePageLocator.back_btn)

        if self.common.poco_exists(FreeUpSpacePageLocator.free_up_space_by_chat_list_first):
            getGroupListFirst = self.common.poco_get_text(FreeUpSpacePageLocator.free_up_space_by_chat_list_first)
            assert not getGroupListFirst == chatDataGroupListFirst
        self.common.poco_click(FreeUpSpacePageLocator.back_btn)
