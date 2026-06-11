import re
from time import sleep

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator

import logging
import common.utils.globalvar as gl


class SocialSearchPageLocator(BaseLocator):
    """社群搜尋頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    # 主頁 > 首頁icon
    first_page = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=0),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_home_button'),
    )
    # 主頁搜索icon
    main_search_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_search'),
        iOS=base.data_collation(type_kind='name', type_name='snsMain_search_button'),
    )
    # 搜索歷史-搜索欄位
    search_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchHistory_search_textField'),
    )
    # 搜索結果-搜索欄位
    search_result_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchResult_search_textField'),
    )
    # 搜索欄位 > x清除鍵
    search_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_clear_iv'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本'),
    )
    # 搜索頁 > 最近搜索紀錄
    search_record = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_recent_search'),
        iOS=base.data_collation(type_kind='name', type_name='最近搜索'),
    )
    # 搜索鍵
    history_search_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_search'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchHistory_search_button'),
    )
    result_search_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_search'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchResult_search_button'),
    )
    # 搜索結果頁 > 視頻頁籤
    search_result_post_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='视频'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchResult_post_segment'),
    )
    # 搜索結果頁 > 視頻 > 第一則貼文說明文字
    search_post_result_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_caption'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 搜索結果頁 > 視頻 > 第一則貼文作者暱稱
    search_post_result_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_nickname'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    # 搜索結果頁 > 上一頁鍵
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='iconArrowsChevronLeft'),
    )
    # 搜索結果頁 > 用戶頁籤
    search_result_user_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='用户'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchResult_author_segment'),
    )
    # 搜索結果頁 > 用戶 > 列表第一筆成員: 暱稱
    search_user_result_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_name'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 用戶 > 列表第一筆成員: 粉絲+視頻數訊息
    search_post_user_result_author_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_counts'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 用戶 > 列表第一筆成員: 關注鍵
    search_user_result_follow_status = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_follow'),
        iOS=base.data_collation(type_kind='name', type_name='snsSearchAuthorResult_authorCell_follow_button'),
    )

    # 搜索頁 > 最近搜索紀錄 > 第num筆紀錄
    @staticmethod
    def search_record_index(app_package, num):
        search_record_index = SocialSearchPageLocator.base.check_device(
            Android=SocialSearchPageLocator.base.data_collation(type_kind='name',
                                                                type_name=str(app_package) + ':id/tv_title',
                                                                num=num),
            iOS=SocialSearchPageLocator.base.data_collation(type_kind='', type_name=''),
        )
        return search_record_index


class SocialSearchPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def _into_search_page(self):
        self.common.poco_click(SocialSearchPageLocator.first_page)
        self.common.poco_click(SocialSearchPageLocator.main_search_icon)

    def search_from_search_page(self, keywords):
        self._into_search_page()
        self.common.poco_click(SocialSearchPageLocator.search_column)
        self.common.poco_send_text(SocialSearchPageLocator.search_column, keywords)
        self.common.poco_click(SocialSearchPageLocator.history_search_btn)
        sleep(2)

    def search_post(self, keywords, search_by_switch_tab=True):
        if self.common.poco_exists(SocialSearchPageLocator.search_clear):
            self.common.poco_click(SocialSearchPageLocator.search_clear)

        if search_by_switch_tab:
            self.common.poco_click(SocialSearchPageLocator.search_result_column)
            self.common.poco_send_text(SocialSearchPageLocator.search_result_column, keywords)
            self.common.poco_click(SocialSearchPageLocator.search_result_post_tab)
            sleep(2)
        else:
            self.common.poco_click(SocialSearchPageLocator.search_result_post_tab)
            self.common.poco_click(SocialSearchPageLocator.search_result_column)
            self.common.poco_send_text(SocialSearchPageLocator.search_result_column, keywords)
            self.common.poco_click(SocialSearchPageLocator.result_search_btn)
            sleep(2)

    def search_poster(self, user_nickname, search_by_switch_tab=True):
        if search_by_switch_tab:
            if self.common.poco_exists(SocialSearchPageLocator.search_clear):
                self.common.poco_click(SocialSearchPageLocator.search_clear)
                sleep(1)

            self.common.poco_send_text(SocialSearchPageLocator.search_column, user_nickname)
            self.common.poco_click(SocialSearchPageLocator.search_result_user_tab)
            sleep(2)
        else:
            self.common.poco_click(SocialSearchPageLocator.search_result_user_tab)
            if self.common.poco_exists(SocialSearchPageLocator.search_clear):
                self.common.poco_click(SocialSearchPageLocator.search_clear)
                sleep(1)

            self.common.poco_send_text(SocialSearchPageLocator.search_column, user_nickname)
            self.common.poco_click(SocialSearchPageLocator.result_search_btn)
            sleep(2)

    def check_search_post_result(self, nickname, description):

        if self.phone_platform.lower() == 'android':
            sleep(5)
            result_description = self.common.poco_get_text(SocialSearchPageLocator.search_post_result_description)
            result_nickname = self.common.poco_get_text(SocialSearchPageLocator.search_post_result_nickname)
        else:
            sleep(5)
            result_description = self.poco(name='snsSearchPostResult_post_cell')[0].offspring(type='StaticText')[0].attr('value')
            result_nickname = self.poco(name='snsSearchPostResult_post_cell')[0].offspring(type='StaticText')[1].attr('value')

        assert result_description == description
        assert result_nickname == nickname

    def check_search_post_user_result(self, user_nickname):
        self.wait_loading_finish()
        if self.phone_platform.lower() == 'android':
            result_nickname = self.common.poco_get_text(SocialSearchPageLocator.search_user_result_nickname)
            actual_text = self.common.poco_get_text(SocialSearchPageLocator.search_post_user_result_author_counts)
        else:
            result_nickname = self.poco(name='snsSearchAuthorResult_author_cell')[0].offspring(type='StaticText')[0].attr('value')
            actual_text = self.poco(name='snsSearchAuthorResult_author_cell')[0].offspring(type='StaticText')[2].attr('value')

        assert result_nickname == user_nickname
        assert "个粉丝" in actual_text
        assert "个视频" in actual_text
        assert self.common.poco_exists(SocialSearchPageLocator.search_user_result_follow_status)

    def check_recent_search_record(self, expected_history):
        self.common.poco_click(SocialSearchPageLocator.back_btn)
        assert self.common.poco_get_text(SocialSearchPageLocator.search_record) == '最近搜索'

        actual_history = []
        # 動態獲取所有的搜索紀錄
        for i in range(len(expected_history)):
            if self.phone_platform.lower() == 'android':
                locator = SocialSearchPageLocator.search_record_index(SocialSearchPageLocator.app_package, i)
                actual_history.append(self.common.poco_get_text(locator))
            else:
                record_index = self.poco(name='snsSearchHistory_searchHints_cell')[i].offspring(type='StaticText')[0].attr('value')
                actual_history.append(record_index)
        # 檢查實際的搜索紀錄是否與預期的一致
        for i, expected in enumerate(expected_history):
            assert actual_history[i] == expected, f"期望的搜索紀錄為: {expected}, 但實際為: {actual_history[i]}"