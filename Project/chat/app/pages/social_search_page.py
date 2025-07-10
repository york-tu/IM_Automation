import re
from time import sleep

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base

import logging
import common.utils.globalvar as gl


class SocialSearchPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = SocialSearchPageLocator.base.check_device(
            Android=SocialSearchPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=SocialSearchPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        return env

    # 主頁 > 首頁icon
    first_page = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=0),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 主頁搜索icon
    main_search_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_search'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索欄位
    search_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索欄位 > x清除鍵
    search_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_clear_iv'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索頁 > 最近搜索紀錄
    search_record = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_recent_search'),
        iOS=base.data_collation(type_kind='name', type_name='最近搜索'),
    )
    # 搜索鍵
    search_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_search'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 視頻頁籤
    search_result_post_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='视频'),
        iOS=base.data_collation(type_kind='name', type_name='视频'),
    )
    # 搜索結果頁 > 視頻 > 第一則貼文說明文字
    search_post_result_description = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_caption'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 視頻 > 第一則貼文作者暱稱
    search_post_result_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_nickname'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 上一頁鍵
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 搜索結果頁 > 用戶頁籤
    search_result_user_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='用户'),
        iOS=base.data_collation(type_kind='name', type_name='用户'),
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
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    # 搜索頁 > 最近搜索紀錄 > 第num筆紀錄
    @staticmethod
    def search_record_index(app_package, num):
        search_record_index = SocialSearchPageLocator.base.check_device(
            Android=SocialSearchPageLocator.base.data_collation(type_kind='name',
                                                                type_name=str(app_package) + ':id/tv_title',
                                                                num=num),
            iOS=SocialSearchPageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return search_record_index


class SocialSearchPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def _into_search_page(self):
        self.common.poco_click(SocialSearchPageLocator.first_page)
        self.common.poco_click(SocialSearchPageLocator.main_search_icon)

    def search_from_search_page(self, keywords):
        self._into_search_page()
        self.common.poco_send_text(SocialSearchPageLocator.search_column, keywords)
        self.common.poco_click(SocialSearchPageLocator.search_btn)

    def search_post(self, keywords, search_by_switch_tab=True):
        if search_by_switch_tab:
            self.common.poco_send_text(SocialSearchPageLocator.search_column, keywords)
            self.common.poco_click(SocialSearchPageLocator.search_result_post_tab)
        else:
            self.common.poco_click(SocialSearchPageLocator.search_result_post_tab)
            self.common.poco_send_text(SocialSearchPageLocator.search_column, keywords)
            self.common.poco_click(SocialSearchPageLocator.search_btn)

    def search_poster(self, user_nickname, search_by_switch_tab=True):
        if search_by_switch_tab:
            self.common.poco_send_text(SocialSearchPageLocator.search_column, user_nickname)
            self.common.poco_click(SocialSearchPageLocator.search_result_user_tab)
        else:
            self.common.poco_click(SocialSearchPageLocator.search_result_user_tab)
            self.common.poco_send_text(SocialSearchPageLocator.search_column, user_nickname)
            self.common.poco_click(SocialSearchPageLocator.search_btn)

    def check_search_post_result(self, nickname, description):
        assert self.common.poco_get_attr(SocialSearchPageLocator.search_result_post_tab, 'selected') is True
        assert self.common.poco_get_text(SocialSearchPageLocator.search_post_result_description) == description
        assert self.common.poco_get_text(SocialSearchPageLocator.search_post_result_nickname) == nickname

    def check_search_post_user_result(self, user_nickname):
        assert self.common.poco_get_attr(SocialSearchPageLocator.search_result_user_tab, 'selected') is True
        assert self.common.poco_get_text(SocialSearchPageLocator.search_user_result_nickname) == user_nickname
        actual_text = self.common.poco_get_text(SocialSearchPageLocator.search_post_user_result_author_counts)
        assert "个粉丝" in actual_text
        assert "个视频" in actual_text
        assert self.common.poco_exists(SocialSearchPageLocator.search_user_result_follow_status)

    def check_recent_search_record(self, expected_history):
        self.common.poco_click(SocialSearchPageLocator.back_btn)
        assert self.common.poco_get_text(SocialSearchPageLocator.search_record) == '最近搜索'

        actual_history = []
        # 動態獲取所有的搜索紀錄
        for i in range(len(expected_history)):
            locator = SocialSearchPageLocator.search_record_index(SocialSearchPageLocator.app_package, i)
            actual_history.append(self.common.poco_get_text(locator))

        # 檢查實際的搜索紀錄是否與預期的一致
        for i, expected in enumerate(expected_history):
            assert actual_history[i] == expected, f"期望的搜索紀錄為: {expected}, 但實際為: {actual_history[i]}"