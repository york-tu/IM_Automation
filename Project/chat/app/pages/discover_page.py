from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


class DiscoverPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = DiscoverPageLocator.base.check_device(
            Android=DiscoverPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=DiscoverPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    discover_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-2),
        iOS=base.data_collation(type_kind='name', type_name='')
    )
    main_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='')
    )
    page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_toolbar_title'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )
    floating_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/layout_assistive_touch'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )
    floating_shrink = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='缩小'),
        iOS=base.data_collation(type_kind='text', type_name='')
    )
    floating_close = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭'),
        iOS=base.data_collation(type_kind='text', type_name='')
    )

    # 發現頁上的發現功能排序
    @staticmethod
    def discover_list_index(app_package, num):
        discover_list_index = DiscoverPageLocator.base.check_device(
            Android=DiscoverPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title', num=num),
            iOS=DiscoverPageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return discover_list_index


class DiscoverPage(Base):

    def into_discover_page(self):
        if self.common.poco_exists(DiscoverPageLocator.discover_btn):
            self.common.poco_click(DiscoverPageLocator.discover_btn)
        assert self.common.poco_get_text(DiscoverPageLocator.page_title) == '发现', f'發現頁'

    def check_discover_list(self):
        function_num = len(self.poco(f'{DiscoverPageLocator.app_package}:id/tv_title'))
        current_list =[]
        for i in range(function_num):
            function_name = self.common.poco_get_text(DiscoverPageLocator.discover_list_index(DiscoverPageLocator.app_package, i))
            current_list.append(function_name)
        return current_list

    def check_discover_menu_and_icon(self, index):
        # ======================== 點擊發現功能 ======================================
        self.common.poco_click(DiscoverPageLocator.discover_list_index(DiscoverPageLocator.app_package, index))
        assert self.common.poco_exists(DiscoverPageLocator.floating_icon), f'懸浮選單鈕未出現'
        # ======================== 點開懸浮按鈕選單 ====================================
        self.common.poco_click(DiscoverPageLocator.floating_icon)
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
