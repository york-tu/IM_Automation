from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class DiscoverPageLocator(BaseLocator):
    """發現頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    discover_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-2),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_discover_button')
    )
    main_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_my_button')
    )
    page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_toolbar_title'),
        iOS=base.data_collation(type_kind='name', type_name='发现')
    )
    floating_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/layout_assistive_touch'),
        iOS=base.data_collation(type_kind='name', type_name='browser_floating_button')
    )
    floating_shrink = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='缩小'),
        iOS=base.data_collation(type_kind='name', type_name='browser_floatingMenu_zoomOutBrowser_button')
    )
    floating_close = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭'),
        iOS=base.data_collation(type_kind='name', type_name='browser_floatingMenu_closeBrowser_button')
    )
    discover_trend_cell = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='discover_trend_cell')
    )
    discover_sports_cell = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='discover_sports_cell')
    )
    discover_gallery_cell = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='discover_gallery_cell')
    )
    error_window = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/parentPanel'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    error_message = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='发生未知错误.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    check_point_trend = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='开奖号码')
    )
    check_point_gallery = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='六合图库')
    )
    check_point_sports = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='Popular Games')
    )

    # 發現頁上的發現功能排序
    @staticmethod
    def discover_list_index(app_package, num):
        discover_list_index = DiscoverPageLocator.base.check_device(
            Android=DiscoverPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title', num=num),
            iOS=DiscoverPageLocator.base.data_collation(type_kind='type', type_name='Cell', num=num),
        )
        return discover_list_index


class DiscoverPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_discover_page(self):
        if self.common.poco_exists(DiscoverPageLocator.discover_btn):
            self.common.poco_click(DiscoverPageLocator.discover_btn)
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_text(DiscoverPageLocator.page_title) == '发现', f'發現頁'
        else:
            assert self.common.poco_exists(DiscoverPageLocator.page_title)

    def check_discover_list(self):
        current_list = []
        if self.phone_platform.lower() == 'android':
            function_num = len(self.poco(f'{DiscoverPageLocator.app_package}:id/tv_title'))
            for i in range(function_num):
                function_name = self.common.poco_get_text(DiscoverPageLocator.discover_list_index(DiscoverPageLocator.app_package, i))
                current_list.append(function_name)
        else:  # ios part
            # 定義對應表
            name_mapping = {
                "discover_gallery_cell": "图库",
                "discover_sports_cell": "体育",
                "discover_trend_cell": "走势"
            }
            cells = self.poco(type='Cell')
            for i in range(len(cells)):
                name = cells[i].get_name()
                mapped_value = name_mapping.get(name, name)  # 轉換成中文
                current_list.append(mapped_value)
        return current_list

    def check_discover_menu_and_icon(self, index):
        # ======================== 點擊發現功能 ======================================
        self.common.poco_click(DiscoverPageLocator.discover_list_index(DiscoverPageLocator.app_package, index))
        sleep(5)
        # ======================== 確認內籤頁面正常開啟 ======================================
        if self.phone_platform.lower() == 'android':
            if self.common.poco_exists(DiscoverPageLocator.error_window):
                assert not self.common.poco_exists(DiscoverPageLocator.error_message), f'頁面出現未知錯誤'
        else:  # ios
            discover_type = self.common.poco_get_attr(DiscoverPageLocator.discover_list_index(DiscoverPageLocator.app_package, index), 'name')
            if discover_type.__contains__("trend"):
                assert self.common.poco_exists(DiscoverPageLocator.check_point_trend)
            elif discover_type.__contains__("gallery"):
                assert self.common.poco_exists(DiscoverPageLocator.check_point_gallery)
            elif discover_type.__contains__("sports"):
                assert self.common.poco_exists(DiscoverPageLocator.check_point_sports)
            else:
                return False
        # ======================== 點開懸浮按鈕選單 ====================================
        assert self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未出現'
        self.common.poco_click(DiscoverPageLocator.floating_icon)
        if self.phone_platform.lower() == 'android':
            assert not self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未隱藏'
        assert self.common.poco_exists(DiscoverPageLocator.floating_shrink), f'懸浮選單未出現縮小鈕'
        assert self.common.poco_exists(DiscoverPageLocator.floating_close), f'懸浮選單未出現關閉鈕'
        # ======================== 點懸浮選單-縮小 ======================================
        self.common.poco_click(DiscoverPageLocator.floating_shrink)
        assert self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未出現'
        # ======================== 切頁面到主頁 ========================================
        self.common.poco_click(DiscoverPageLocator.main_btn)
        assert self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未出現'
        # ======================== 點擊發現圖示 > 點開懸浮選單 ============================
        self.common.poco_click(DiscoverPageLocator.floating_icon)
        self.common.poco_click(DiscoverPageLocator.floating_icon)
        # ======================== 點懸浮選單-關閉 ======================================
        self.common.poco_click(DiscoverPageLocator.floating_close)
        assert not self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未消失'
        assert self.common.poco_exists(DiscoverPageLocator.main_btn), f'功能頁未正確關閉'
