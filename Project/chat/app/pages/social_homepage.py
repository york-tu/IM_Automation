import re
from time import sleep

from Project.chat.app.pages.social_media_library_page import SocialMediaLibraryPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.friend_page import FriendPageLocator
import logging
import common.utils.globalvar as gl


class PersonalSocialPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = PersonalSocialPageLocator.base.check_device(
            Android=PersonalSocialPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=PersonalSocialPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        return env

    # ============================= 社群個人主頁 ====================================
    social_self_page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_nickname_label'),
    )
    social_other_page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='name', type_name='otherAuthorProfile_nickname_label'),
    )

    # 個人主頁 > 已關注
    social_page_follows = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='已关注'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_followedCount_label'),
    )
    # 個人主頁 > 已關注 > 已關注頁籤
    followed_tab = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='已关注.*'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='已关注.*'),
    )
    # (自己)個人主頁 > 已關注數
    followed_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=0),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # (他人)個人主頁 > 已關注數
    other_followed_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=0),
        iOS=base.data_collation(type_kind='name', type_name='otherAuthorProfile_followedCount_label'),
    )
    # 個人主頁 > 已關注列表 > 第一位成員
    list_first_member = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 個人主頁 > 粉絲
    social_page_fans = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='粉丝'),
        iOS=base.data_collation(type_kind='name', type_name='粉丝'),
    )
    # (自己)個人主頁 > 粉絲數
    fans_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # (他人)個人主頁 > 粉絲數
    other_fans_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=1),
        iOS=base.data_collation(type_kind='name', type_name='otherAuthorProfile_followersCount_label'),
    )
    # 個人主頁 > 粉絲 > 粉絲頁籤
    fans_tab = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='粉丝.*'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='粉丝.*'),
    )
    # 個人主頁 > 贊
    social_page_thumbs = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='赞'),
        iOS=base.data_collation(type_kind='name', type_name='赞'),
    )
    # (自己)個人主頁 > 贊數
    thumb_up_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=2),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # (他人)個人主頁 > 贊數
    other_thumb_up_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count', num=2),
        iOS=base.data_collation(type_kind='name', type_name='otherAuthorProfile_likedCount_label'),
    )
    # 個人主頁 > "關注/已關注"鍵
    follow_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_follow'),
        iOS=base.data_collation(type_kind='name', type_name='otherAuthorProfile_follow_button'),
    )
    # 個人主頁 > "聊天"鍵
    chat_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_chat'),
        iOS=base.data_collation(type_kind='name', type_name='聊天'),
    )
    social_page_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_left'),
        iOS=base.data_collation(type_kind='name', type_name='chevron Left black'),
    )
    detail_page_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    main_page = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_my_button'),
    )
    # 個人主頁 > 第一則貼文觀看次數
    post_view_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_view_count', num=0),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    # ============================= 搜索用戶 ====================================
    search_member = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='authorsFollowStatus_search_textField', num=0),
    )
    search_result_list = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rv_list'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    search_result_first_member_avatar = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_avatar'),
        iOS=base.data_collation(type_kind='name', type_name='authorsFollowStatus_authorCell_avatar_imageView', num=0),
    )


class SocialHomePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_member_social_page_from_chat(self, user_nickname):
        self.common.poco_click(FriendPageLocator.personal_social_homepage_btn)

        assert self.common.poco_get_text(PersonalSocialPageLocator.social_other_page_title) == user_nickname
        assert self.common.poco_exists(PersonalSocialPageLocator.social_page_follows)
        assert self.common.poco_exists(PersonalSocialPageLocator.social_page_fans)
        assert self.common.poco_exists(PersonalSocialPageLocator.social_page_thumbs)
        assert self.common.poco_exists(PersonalSocialPageLocator.chat_btn)

        followed_counts = self.common.poco_get_text(PersonalSocialPageLocator.followed_counts)
        fans_counts = self.common.poco_get_text(PersonalSocialPageLocator.fans_counts)
        thumb_up_counts = self.common.poco_get_text(PersonalSocialPageLocator.thumb_up_counts)

        return int(followed_counts), int(fans_counts), int(thumb_up_counts)

    def follow_member(self, user_nickname):
        if self.common.poco_get_text(PersonalSocialPageLocator.social_other_page_title) == user_nickname:
            original_fans_count = int(self.common.poco_get_text(PersonalSocialPageLocator.fans_counts))
            self.common.poco_click(PersonalSocialPageLocator.follow_btn)
            after_fans_count = int(self.common.poco_get_text(PersonalSocialPageLocator.fans_counts))
            assert after_fans_count == original_fans_count + 1, f'粉絲數錯誤, 實際:{after_fans_count}, 預期為{original_fans_count}+1'
            assert self.common.poco_get_text(PersonalSocialPageLocator.follow_btn) == '已关注'
            return after_fans_count
        else:
            return False

    def get_page_all_counts(self):
        main_page_followed_counts = self.common.poco_get_text(PersonalSocialPageLocator.followed_counts)
        main_page_fans_counts = self.common.poco_get_text(PersonalSocialPageLocator.fans_counts)
        main_page_thumb_up_counts = self.common.poco_get_text(PersonalSocialPageLocator.thumb_up_counts)
        return main_page_followed_counts, main_page_fans_counts, main_page_thumb_up_counts

    def into_followed_list(self):
        self.common.poco_click(PersonalSocialPageLocator.social_page_follows)
        assert self.common.poco_exists(PersonalSocialPageLocator.followed_tab)
        assert self.common.poco_exists(PersonalSocialPageLocator.fans_tab)

    def into_member_social_page_from_followed_list(self, user_nickname):
        self.common.poco_click(PersonalSocialPageLocator.search_member)
        self.common.poco_send_text(PersonalSocialPageLocator.search_member, user_nickname)
        sleep(2)
        self.common.poco_click(PersonalSocialPageLocator.search_result_first_member_avatar)

        assert self.common.poco_get_text(PersonalSocialPageLocator.social_other_page_title) == user_nickname
        assert self.common.poco_get_text(PersonalSocialPageLocator.follow_btn) == '已关注'

        followed_counts = self.common.poco_get_text(PersonalSocialPageLocator.other_followed_counts)
        fans_counts = self.common.poco_get_text(PersonalSocialPageLocator.other_fans_counts)
        thumb_up_counts = self.common.poco_get_text(PersonalSocialPageLocator.other_thumb_up_counts)

        return int(followed_counts), int(fans_counts), int(thumb_up_counts)

    def into_fans_list(self):
        self.common.poco_click(PersonalSocialPageLocator.social_page_fans)
        assert self.common.poco_exists(PersonalSocialPageLocator.followed_tab)
        assert self.common.poco_exists(PersonalSocialPageLocator.fans_tab)

    def into_member_social_page_from_fans_list(self, user_nickname):
        self.common.poco_send_text(PersonalSocialPageLocator.search_member, user_nickname)
        sleep(2)
        self.common.poco_click(PersonalSocialPageLocator.search_result_first_member_avatar)

    def unfollow_member(self, user_nickname, main_page_followed_counts):
        self.common.poco_send_text(PersonalSocialPageLocator.search_member, user_nickname)
        self.common.poco_click(PersonalSocialPageLocator.follow_btn)
        sleep(1)
        assert self.common.poco_get_text(PersonalSocialPageLocator.follow_btn) == '关注'
        match = re.search(r'\d+', self.common.poco_get_text(PersonalSocialPageLocator.followed_tab))
        tab_followed_counts = int(match.group())
        assert tab_followed_counts == int(main_page_followed_counts) - 1

    def check_followed_list(self, user_nickname, main_page_followed_counts, add_follow=True):
        # =============================確認頁籤數字====================================
        match = re.search(r'\d+', self.common.poco_get_text(PersonalSocialPageLocator.followed_tab))
        tab_followed_counts = int(match.group())
        assert tab_followed_counts == int(main_page_followed_counts)
        # =============================確認列表第一位關注成員============================
        if add_follow:
            assert self.common.poco_get_text(PersonalSocialPageLocator.list_first_member) == user_nickname
        else:
            self.common.poco_send_text(PersonalSocialPageLocator.search_member, user_nickname)
            sleep(2)
            assert self.common.poco_exists(PersonalSocialPageLocator.list_first_member) is False
        # =============================確認列表第一位關注狀態============================
        if add_follow:
            assert self.common.poco_get_text(PersonalSocialPageLocator.follow_btn) == '已关注'

    def check_fans_list(self, user_nickname, main_page_fans_counts, add_fans=False):
        # =============================確認頁籤數字====================================
        match = re.search(r'\d+', self.common.poco_get_text(PersonalSocialPageLocator.fans_tab))
        tab_fans_counts = int(match.group())
        assert tab_fans_counts == int(main_page_fans_counts)
        # =============================確認列表第一位關注成員============================
        if add_fans:
            assert self.common.poco_get_text(PersonalSocialPageLocator.list_first_member) == user_nickname
        else:
            assert not self.common.poco_get_text(PersonalSocialPageLocator.list_first_member) == user_nickname

    def return_to_my_social_page(self):
        if self.common.poco_exists(SocialMediaLibraryPageLocator.media_back_btn):
            self.common.poco_click(SocialMediaLibraryPageLocator.media_back_btn)  # 貼文上點返回

        while self.common.poco_exists(PersonalSocialPageLocator.social_page_back_btn) or self.common.poco_exists(
                PersonalSocialPageLocator.detail_page_back_btn):
            if self.common.poco_exists(PersonalSocialPageLocator.social_page_back_btn):
                self.common.poco_click(PersonalSocialPageLocator.social_page_back_btn)
            if self.common.poco_exists(PersonalSocialPageLocator.detail_page_back_btn):
                self.common.poco_click(PersonalSocialPageLocator.detail_page_back_btn)

        sleep(0.5)

        if self.phone_platform.lower() == 'android':
            if not self.common.poco_get_attr(PersonalSocialPageLocator.main_page, 'selected'):
                self.common.poco_click(PersonalSocialPageLocator.main_page)
        else:
            if not self.common.poco_get_attr(PersonalSocialPageLocator.main_page, 'value') == 1:
                self.common.poco_click(PersonalSocialPageLocator.main_page)

    def get_post_view_counts(self):
        return self.common.poco_get_text(PersonalSocialPageLocator.post_view_counts)
