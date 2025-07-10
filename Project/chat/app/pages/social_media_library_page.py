import datetime
import re
from time import sleep


from Project.chat.app.pages.social_sharepage import SocialSharePage
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPageLocator
import logging
import common.utils.globalvar as gl


class SocialMediaLibraryPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = SocialMediaLibraryPageLocator.base.check_device(
            Android=SocialMediaLibraryPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=SocialMediaLibraryPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env
    # 貼文 > 貼文信息 > 頭像icon
    avatar_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_avatar'),
        iOS=base.data_collation(type_kind='text', type_name='iv_avatar'),
    )
    # 貼文 > 貼文信息 > 贊icon
    liked_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_liked'),
        iOS=base.data_collation(type_kind='text', type_name='iv_liked'),
    )
    # 貼文 > 貼文信息 > 贊icon > 贊數
    liked_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_liked_count'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 貼文 > 貼文信息 > 評論icon
    comment_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_comment'),
        iOS=base.data_collation(type_kind='text', type_name='iv_message'),
    )
    # 貼文 > 貼文信息 > 收藏icon
    collected_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_collected'),
        iOS=base.data_collation(type_kind='text', type_name='iv_bookmark'),
    )
    # 貼文 > 貼文信息 > 收藏icon > 收藏數
    collected_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_collected_count'),
        iOS=base.data_collation(type_kind='text', type_name='iv_bookmark'),
    )
    # ========================================= more設定 ========================================================
    # 貼文 > 貼文信息 > 更多icon
    more_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_shared'),
        iOS=base.data_collation(type_kind='text', type_name='iv_more'),
    )
    # ========================================= 隱私設定 ==============================
    # 貼文 > 貼文信息 > 更多icon > 隱私設定
    more_privacy_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='隐私设置'),
        iOS=base.data_collation(type_kind='text', type_name='btn_privacy_setup'),
    )
    # 更多icon > 隱私設定 > 所有人
    more_privacy_everyone_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_everyone'),
        iOS=base.data_collation(type_kind='text', type_name='rb_everyone'),
    )
    # 更多icon > 隱私設定 > 互關
    more_privacy_mutual_followers_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_mutual_followers'),
        iOS=base.data_collation(type_kind='text', type_name='rb_mutual_followers'),
    )
    # 更多icon > 隱私設定 > 粉絲
    more_privacy_fans_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_followers'),
        iOS=base.data_collation(type_kind='text', type_name='rb_followers'),
    )
    # 更多icon > 隱私設定 > 僅自己
    more_privacy_self_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rb_only_self'),
        iOS=base.data_collation(type_kind='text', type_name='rb_only_self'),
    )
    # 更多icon > 隱私設定 > x鍵
    more_privacy_close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_end_icon'),
        iOS=base.data_collation(type_kind='text', type_name='iv_end_icon'),
    )

    # =================================================================================
    # 貼文 > 貼文作者暱稱
    author_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_name'),
        iOS=base.data_collation(type_kind='text', type_name='tv_author_name'),
    )
    # 貼文 > 貼文說明文字
    content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='text', type_name='tv_caption'),
    )
    # ========================================= 評論 ========================================================
    # "x"鍵
    post_comment_close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_close'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # ========================================= 頁籤 > 評論 ==============================
    # 他人的評論頁籤
    post_others_comment_tab = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name=f'.* 条评论'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 自己的評論頁籤
    post_comment_tab = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=-3),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 評論輸入欄位
    post_input_comment_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_preview'),
        iOS=base.data_collation(type_kind='text', type_name='添加评论'),
    )
    # 評論欄位無權限hint
    post_no_comment_permission_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_no_comment_permission_hint'),
        iOS=base.data_collation(type_kind='text', type_name='无权限评论'),
    )
    # 留言框內自動帶入的文字
    post_input_comment = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 留言 > 全選
    toolbar_menu_text_select_all = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='全选'),
        iOS=base.data_collation(type_kind='text', type_name='全选'),
    )
    # 留言 > 剪切
    toolbar_menu_text_cut = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='剪切'),
        iOS=base.data_collation(type_kind='text', type_name='剪切'),
    )
    # 評論發送鍵
    post_comment_send_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_send'),
        iOS=base.data_collation(type_kind='text', type_name='添加评论'),
    )
    # 最新一筆母留言作者暱稱
    post_recent_comment_commenter = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_commenter', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 創作者tag
    post_recent_comment_author = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言內容
    post_recent_comment_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言的送出時間
    post_recent_comment_add_time = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_time', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言的回覆鍵
    post_recent_comment_reply_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言的贊icon
    post_recent_comment_thumb_up_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_like', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言的贊數
    post_recent_comment_liked_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_like_count', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆留言作者暱稱
    post_recent_comment_recent_reply_commenter = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_commenter', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 回覆子留言時暱稱上的">"箭頭
    reply_to_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_to', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 回覆子留言時暱稱上顯示的回覆對象
    reply_to_target_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply_to_commenter', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆留言創作者tag
    post_recent_comment_recent_reply_author = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆訊息內容
    post_recent_comment_recent_reply_comment_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆訊息的送出時間
    post_recent_comment_recent_reply_add_time = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_time', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆訊息的回覆鍵
    post_recent_comment_recent_reply_reply_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆母留言 > 最新一筆回覆訊息的贊icon
    post_recent_comment_recent_reply_thumb_up_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_like', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 最新一筆回覆留言的贊數
    post_recent_comment_reply_liked_counts = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_like_count', num=1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )

    # ========================================= 頁籤 > 贊 ================================
    # 自己評論頁內的"贊頁"
    post_thumb_up_tab = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=-2),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # "贊頁"列表第一位成員
    post_thumb_up_tab_first_member_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_nickname'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )

    # ========================================= 頁籤 > 觀看次數 ===========================
    # 自己評論頁內的"观看次数"頁
    post_views_tab = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=-1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # ========================================= 媒體櫃 ========================================================
    # 第一則媒體
    first_media = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_thumbnail'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    # 貼文 > 點回到上一頁
    media_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    # 他人貼文 > 點回到上一頁
    other_post_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_left'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # ========================================= 公開媒體 ================================
    # 關注狀態icon
    audience_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_audience_icon'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # ========================================= 私密媒體 ================================
    # 公開媒體頁籤
    library_public_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=0),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    # 私密媒體頁籤
    library_private_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=-3),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    # ========================================= 收藏媒體 ================================
    # 收藏媒體頁籤
    library_collected_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=-2),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # ========================================= 按贊媒體櫃 ===============================
    # 按贊媒體頁籤
    library_liked_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=-1),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 功能表隱私設定"僅自己" >>> 他人點進按贊顯示"不公開"訊息
    privacy_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='此用户的按赞视频不公开'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )

    # ========================================= 草稿 ========================================================
    # 草稿夾
    draft_media_folder = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_draft'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    # 草稿夾 > 第一則媒體
    draft_folder_first_media = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_image', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    # 草稿夾 > 第一則媒體 > 發布時間
    draft_folder_first_media_create_time = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_create_time', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    draft_folder_select_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='选择'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    draft_folder_select_first = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cb_select', num=0),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )
    draft_folder_delete_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='删除'),
        iOS=base.data_collation(type_kind='text', type_name=''),
    )

    @staticmethod
    def audience_icon_index(app_package, num):
        audience_icon_index = SocialMediaLibraryPageLocator.base.check_device(
            Android=SocialMediaLibraryPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_audience_icon', num=num),
            iOS=SocialMediaLibraryPageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return audience_icon_index

    @staticmethod
    def public_media_index(app_package, num):
        public_media_index = SocialMediaLibraryPageLocator.base.check_device(
            Android=SocialMediaLibraryPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_thumbnail', num=num),
            iOS=SocialMediaLibraryPageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return public_media_index


def post_privacy_select(privacy_index):
    privacy_type_list = [SocialMediaLibraryPageLocator.more_privacy_everyone_btn,
                         SocialMediaLibraryPageLocator.more_privacy_mutual_followers_btn,
                         SocialMediaLibraryPageLocator.more_privacy_fans_btn,
                         SocialMediaLibraryPageLocator.more_privacy_self_btn]
    return privacy_type_list[privacy_index]


class SocialMediaLibraryPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    # ========================================= 貼文相關 ================================================================
    def check_recent_post_media(self, account, instructions, save_to_local=True, post=True):
        """檢查最新的帖子媒體，並確認媒體的相關信息"""

        if post:
            self._check_avatar_icon(account)

        # 檢查媒體畫面上的其他元素
        self._check_media_icons()
        self._check_post_author_and_content(account, instructions)

    def _check_avatar_icon(self, account):
        """檢查頭像icon，並驗證是否正確跳轉到主頁"""
        self.common.poco_wait_exists(SocialMediaLibraryPageLocator.avatar_icon, 120)
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.avatar_icon), '頭像icon未顯示'
        self.common.poco_click(SocialMediaLibraryPageLocator.avatar_icon)

        from Project.chat.app.pages.social_homepage import PersonalSocialPageLocator
        assert self.common.poco_get_text(PersonalSocialPageLocator.social_page_title) == account, '點擊頭像未進入創作者主頁或主頁錯誤'
        self.common.poco_click(PersonalSocialPageLocator.social_page_back_btn)

    def _check_media_icons(self):
        """檢查媒體畫面上的各種icon是否顯示"""
        icons = [
            (SocialMediaLibraryPageLocator.liked_icon, '贊icon未顯示'),
            (SocialMediaLibraryPageLocator.comment_icon, '留言icon未顯示'),
            (SocialMediaLibraryPageLocator.collected_icon, '收藏icon未顯示'),
            (SocialMediaLibraryPageLocator.more_icon, '分享icon未顯示')
        ]

        for icon, error_msg in icons:
            assert self.common.poco_exists(icon), error_msg

    def _check_post_author_and_content(self, user_nickname, instructions):
        """檢查創作者暱稱和媒體說明是否正確"""
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.author_name) == user_nickname, '創作者暱稱錯誤'
        current = self.common.poco_get_text(SocialMediaLibraryPageLocator.content)
        assert current == instructions, f'媒體說明有誤, 預期:{instructions},實際:{current}'

    def get_post_author_and_content(self):
        current_user_nickname = self.common.poco_get_text(SocialMediaLibraryPageLocator.author_name)
        current_content = self.common.poco_get_text(SocialMediaLibraryPageLocator.content)
        return current_user_nickname, current_content

    def into_first_post(self, user_nickname=None, instructions=None):
        """進入第一篇帖子並檢查作者名稱和媒體說明"""
        self.common.poco_click(SocialMediaLibraryPageLocator.first_media)
        if user_nickname and instructions:
            self._check_post_author_and_content(user_nickname, instructions)

    def change_first_post_privacy_type(self, user_nickname, description, privacy_index):
        self.common.poco_click(SocialMediaLibraryPageLocator.first_media)
        current_display_user_nickname = self.common.poco_get_text(SocialMediaLibraryPageLocator.author_name)
        assert current_display_user_nickname == user_nickname, f'創作者暱稱錯誤, 預期:{user_nickname}, 實際:{current_display_user_nickname}'
        current = self.common.poco_get_text(SocialMediaLibraryPageLocator.content)
        assert current == description, f'媒體說明有誤, 預期:{description},實際: {current}'

        self.common.poco_click(SocialMediaLibraryPageLocator.more_icon)
        self.common.poco_click(SocialMediaLibraryPageLocator.more_privacy_btn)
        self.common.poco_click(post_privacy_select(privacy_index))

    def check_first_post_privacy_type(self, user_nickname, description, privacy_index):
        if privacy_index == 3:  # 隱私設定為僅自己時, 貼文從私密媒體區點擊
            self.common.poco_click(SocialMediaLibraryPageLocator.library_private_icon)
        else:
            self.common.poco_click(SocialMediaLibraryPageLocator.library_public_icon)

        self.common.poco_click(SocialMediaLibraryPageLocator.first_media)
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.author_name) == user_nickname, '創作者暱稱錯誤'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.content) == description, f'媒體說明有誤,預期:{description}, 實際:{self.common.poco_get_text(SocialMediaLibraryPageLocator.content)}'

        self.common.poco_click(SocialMediaLibraryPageLocator.more_icon)
        self.common.poco_click(SocialMediaLibraryPageLocator.more_privacy_btn)

        assert self.common.poco_get_attr(post_privacy_select(privacy_index), 'checked')  # 確認選項被選取

        self.common.poco_click(SocialMediaLibraryPageLocator.more_privacy_close_btn)

    def check_post_media_info(self, user_nickname, instructions, media_index=0, privacy_index=0):
        """檢查指定媒體的隱私設置和內容"""
        # if privacy_index in [1, 2]:  # 隱私設定為: 互關 or 粉絲
        #     self._check_audience_icon(media_index)
        self.common.poco_click(SocialMediaLibraryPageLocator.public_media_index(SocialMediaLibraryPageLocator.app_package, media_index))  # 點擊指定媒體
        self._check_post_author_and_content(user_nickname, instructions)
        self.common.poco_click(SocialMediaLibraryPageLocator.other_post_back_btn)

    def _check_audience_icon(self, media_index):
        """檢查指定媒體是否顯示觀眾(互關/粉絲)icon"""
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.audience_icon_index(SocialMediaLibraryPageLocator.app_package, media_index)), '媒體未出現觀眾(互關/粉絲)icon'

    def post_add_like(self, original_main_liked_counts):
        """為貼文新增贊並確認主頁與貼文的贊數更新"""
        original_liked_counts = self.common.poco_get_text(SocialMediaLibraryPageLocator.liked_counts)
        self.common.poco_click(SocialMediaLibraryPageLocator.liked_icon)
        sleep(1)
        post_page_liked_counts = self._check_post_liked_counts(original_liked_counts, increment=1)  # 確認貼文贊數
        main_page_liked_counts = self._check_main_liked_counts(original_main_liked_counts, increment=1)  # 確認主頁贊數
        return main_page_liked_counts, post_page_liked_counts

    def _check_main_liked_counts(self, original_counts, increment):
        """檢查主頁贊數是否按預期更新"""
        from Project.chat.app.pages.social_homepage import PersonalSocialPageLocator
        self.common.poco_click(PersonalSocialPageLocator.social_page_back_btn)  # 回到主頁
        sleep(1)
        main_page_liked_counts = self.common.poco_get_text(PersonalSocialPageLocator.thumb_up_counts)
        assert int(main_page_liked_counts) == int(original_counts) + increment, f'貼文贊數沒有即時更新({increment})'
        return main_page_liked_counts

    def _check_post_liked_counts(self, original_counts, increment):
        """檢查贊數是否按預期更新"""
        after_liked_counts = self.common.poco_get_text(SocialMediaLibraryPageLocator.liked_counts)
        assert int(after_liked_counts) == int(original_counts) + increment, f'貼文贊數沒有即時更新({increment})'
        return after_liked_counts

    def self_post_add_like(self, self_nickname):
        """自我點贊並確認贊數更新"""
        original_liked_counts = self.common.poco_get_text(SocialMediaLibraryPageLocator.liked_counts)
        self.common.poco_click(SocialMediaLibraryPageLocator.comment_icon)  # 點進評論頁
        sleep(1)

        post_thumb_up_tab_counts_original = self._get_thumb_up_counts()
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)  # 回到貼文畫面

        self.common.poco_click(SocialMediaLibraryPageLocator.liked_icon)  # 貼文點贊
        self._check_post_liked_counts(original_liked_counts, increment=1)

        self.common.poco_click(SocialMediaLibraryPageLocator.comment_icon)  # 點進評論頁
        sleep(1)

        post_thumb_up_tab_counts_after_add_like = self._get_thumb_up_counts()
        assert post_thumb_up_tab_counts_after_add_like == post_thumb_up_tab_counts_original + 1, '贊數未正確更新'

        self.common.poco_click(SocialMediaLibraryPageLocator.post_thumb_up_tab)  # 點進頁籤>贊
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_thumb_up_tab_first_member_nickname) == self_nickname
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)  # 回到貼文畫面

    def _get_thumb_up_counts(self):
        """獲取贊的數量"""
        match = re.search(r'\d+', self.common.poco_get_text(SocialMediaLibraryPageLocator.post_thumb_up_tab))
        return int(match.group()) if match else 0

    def check_post_liked_counts_after_cancel(self, original_post_liked_counts):
        """確認取消贊後貼文贊數減少"""
        self._check_post_liked_counts(original_post_liked_counts, increment=-1)
        from Project.chat.app.pages.social_homepage import PersonalSocialPageLocator
        self.common.poco_click(PersonalSocialPageLocator.social_page_back_btn)

    def post_add_collect(self):
        """新增收藏並確認收藏數更新"""
        original_collected_counts = self.common.poco_get_text(SocialMediaLibraryPageLocator.collected_counts)
        self.common.poco_click(SocialMediaLibraryPageLocator.collected_icon)
        sleep(1)
        return self._check_collect_counts(original_collected_counts, increment=1)

    def _check_collect_counts(self, original_counts, increment):
        """檢查收藏數是否按預期更新"""
        after_collect_counts = self.common.poco_get_text(SocialMediaLibraryPageLocator.collected_counts)
        assert int(after_collect_counts) == int(original_counts) + increment, '收藏數未更新'
        return after_collect_counts

    def check_post_collects_after_cancel(self, original_collected_counts):
        """確認取消收藏後的收藏數更新"""
        self._check_collect_counts(original_collected_counts, increment=-1)

    def check_my_collected_library_after_add(self, creator_nickname, media_info):
        """確認收藏的媒體資訊"""
        self._check_my_library_after_action(SocialMediaLibraryPageLocator.library_collected_icon, creator_nickname, media_info)

    def check_my_liked_library_after_add(self, creator_nickname, media_info):
        """確認點贊的媒體資訊"""
        self._check_my_library_after_action(SocialMediaLibraryPageLocator.library_liked_icon, creator_nickname,media_info)

    def _check_my_library_after_action(self, library_icon, creator_nickname, media_info):
        """檢查我的媒體庫中的資料"""
        self.common.poco_click(library_icon)
        sleep(1)
        self.common.poco_click(SocialMediaLibraryPageLocator.first_media)
        sleep(1)
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.author_name) == creator_nickname, '貼文創作者與預期不符'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.content) == media_info, '貼文說明與預期不符'

    def check_my_collected_library_after_uncollected(self, media_info):
        """確認取消收藏後的媒體資訊"""
        self._check_my_library_after_uncollected(SocialMediaLibraryPageLocator.collected_icon, media_info)

    def check_my_liked_library_after_uncollected(self, media_info):
        """確認取消點贊後的媒體資訊"""
        self._check_my_library_after_uncollected(SocialMediaLibraryPageLocator.liked_icon, media_info)

    def _check_my_library_after_uncollected(self, icon, media_info):
        """檢查取消收藏或取消點贊後的媒體資訊"""
        self.common.poco_click(icon)
        if self.common.poco_exists(SocialMediaLibraryPageLocator.media_back_btn):
            self.common.poco_click(SocialMediaLibraryPageLocator.media_back_btn)
            sleep(1)
            self.common.poco_click(SocialMediaLibraryPageLocator.first_media)
        sleep(1)
        assert not self.common.poco_get_text(SocialMediaLibraryPageLocator.content) == media_info, '取消收藏失敗'

    # ========================================= 草稿夾相關 ===============================================================
    def check_draft_folder_exist(self, expect):
        """檢查草稿夾是否存在"""
        if expect:
            # self._swipe_to_draft_folder()
            assert self.common.poco_exists(SocialMediaLibraryPageLocator.draft_media_folder), '草稿夾應該存在'
        else:
            assert not self.common.poco_exists(SocialMediaLibraryPageLocator.draft_media_folder), '草稿夾不應該存在'

    # def _swipe_to_draft_folder(self):
    #     """滑動到草稿夾位置"""
    #     self.poco.swipe([0.5, 0.6], [0.5, 0.8], duration=0.1)

    def draft_media_counts(self):
        """獲取草稿夾中的媒體數量"""
        self._navigate_to_mine_page()
        if self.common.poco_exists(SocialMediaLibraryPageLocator.draft_media_folder):
            return self._extract_media_count(SocialMediaLibraryPageLocator.draft_media_folder)
        return 0

    def _navigate_to_mine_page(self):
        """確保當前在個人頁面"""
        if not self.common.poco_get_attr(MainPageLocator.main_btn, "selected"):
            self.common.poco_click(MainPageLocator.main_btn)

    def _extract_media_count(self, locator):
        """提取草稿夾或媒體的數量"""
        return int(re.search(r'\d+', self.common.poco_get_text(locator)).group())

    def delete_draft_media(self, original_draft_counts, current_date):
        """刪除草稿夾中的媒體並確認數量"""
        current_draft_counts = self.draft_media_counts()
        assert current_draft_counts == original_draft_counts + 1, '草稿夾數量應該增加1'
        self.common.poco_click(SocialMediaLibraryPageLocator.draft_media_folder)
        self._check_media_creation_time(current_date)
        self._delete_first_draft_media()

    def _check_media_creation_time(self, expected_date):
        """確認草稿媒體的創建時間"""
        assert self.common.poco_get_text(
            SocialMediaLibraryPageLocator.draft_folder_first_media_create_time) == expected_date, '草稿貼文創建日期不符'

    def _delete_first_draft_media(self):
        """刪除草稿夾中的第一個媒體"""
        self.common.poco_click(SocialMediaLibraryPageLocator.draft_folder_select_btn)
        self.common.poco_click(SocialMediaLibraryPageLocator.draft_folder_select_first)
        self.common.poco_click(SocialMediaLibraryPageLocator.draft_folder_delete_btn)

    # =============================================== 貼文評論相關 =======================================================
    def into_post_comment_page(self, self_post=True):
        """進入貼文評論頁並確認頁籤"""
        self.common.poco_click(SocialMediaLibraryPageLocator.comment_icon)
        sleep(2)
        if self_post:
            self._check_comment_tabs()
        else:
            assert self.common.poco_exists(SocialMediaLibraryPageLocator.post_others_comment_tab), '他人評論頁未正確顯示'

    def _check_comment_tabs(self):
        """確認評論頁的頁籤是否正確顯示"""
        assert '评论' in self.common.poco_get_text(SocialMediaLibraryPageLocator.post_comment_tab), '評論頁籤顯示錯誤'
        assert '赞' in self.common.poco_get_text(SocialMediaLibraryPageLocator.post_thumb_up_tab), '贊頁籤顯示錯誤'
        assert '观看次数' in self.common.poco_get_text(SocialMediaLibraryPageLocator.post_views_tab), '觀看次數頁籤顯示錯誤'

    def check_post_recent_comment(self, recent_comment):
        """確認貼文最近的評論內容"""
        actual_comment = self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_content)
        assert actual_comment == recent_comment, f'最近的評論內容不符, 預期:{recent_comment},實際:{actual_comment}'

    def check_post_recent_reply(self, recent_reply):
        """確認貼文最近的回覆內容"""
        assert self.common.poco_get_text(
            SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_comment_content) == recent_reply, '最近的回覆內容不符'

    def post_recent_comment_add_like(self):
        """給最近的評論點贊並確認贊數更新"""
        return self._add_like_to_recent_comment(SocialMediaLibraryPageLocator.post_recent_comment_thumb_up_icon,
                                                self.check_recent_comment_liked_counts)

    def _add_like_to_recent_comment(self, like_icon, check_liked_counts_method):
        """給最近的評論或回覆點贊並確認贊數更新"""
        original_liked_counts = check_liked_counts_method() or 0
        self.common.poco_click(like_icon)
        after_liked_counts = check_liked_counts_method()
        assert int(after_liked_counts) == int(original_liked_counts) + 1, '贊數未正確更新'
        return after_liked_counts

    def check_recent_comment_liked_counts(self):
        return self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_liked_counts)

    def post_recent_reply_add_like(self):
        """給最近的回覆點贊並確認贊數更新"""
        after_reply_liked_counts = self._add_like_to_recent_comment(
            SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_thumb_up_icon,
            self.check_recent_reply_liked_counts)
        self._close_comment_page()
        return after_reply_liked_counts

    def _close_comment_page(self):
        """關閉評論頁"""
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)

    def check_recent_reply_liked_counts(self):
        """獲取最近的回覆贊數"""
        return self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_reply_liked_counts)

    def post_add_comment(self, commenter, comment, post_url=False, self_post=True):
        """添加評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)

        self._input_and_send_comment(comment)
        if not post_url and "https" in comment:
            assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_input_comment_column) == comment, f'URL留言未保留'
        else:
            comment_send_time = self._get_current_time()
            self._verify_comment_details(commenter, comment, comment_send_time)

            self._verify_comment_count_updated(original_comment_count, self_post)
            if self_post:
                self._verify_creator_label(SocialMediaLibraryPageLocator.post_recent_comment_author)

    def _get_original_comment_count(self, self_post):
        """獲取原始評論數"""
        if self_post:
            match = re.search(r'\d+', self.common.poco_get_text(SocialMediaLibraryPageLocator.post_comment_tab))
            return int(match.group())
        return int(self.common.poco_get_text(SocialMediaLibraryPageLocator.post_others_comment_tab).split()[0])

    def _input_and_send_comment(self, comment):
        """輸入評論並送出"""
        self.common.poco_click(SocialMediaLibraryPageLocator.post_input_comment_column)
        self.common.poco_send_text(SocialMediaLibraryPageLocator.post_input_comment, comment)
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_send_btn)

    def _verify_comment_details(self, commenter, comment, send_time):
        """驗證評論的詳細資訊"""
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_commenter) == commenter, f'留言者暱稱顯示錯誤, 預期:{commenter},實際:{self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_commenter)}'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_content) == comment, '留言內容顯示錯誤'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_add_time) == send_time, f'留言時間顯示錯誤, 預期:{send_time}, 實際: {self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_add_time)}'
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.post_recent_comment_reply_btn), '留言未出現回覆鍵'
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.post_recent_comment_thumb_up_icon), '留言未出現點贊icon'

    def _verify_comment_count_updated(self, original_count, self_post):
        """驗證評論數量是否更新"""
        updated_count = self._get_original_comment_count(self_post)
        assert updated_count == original_count + 1, '評論數量未更新'

    def _verify_creator_label(self, author_locator):
        """驗證創作者標籤是否正確顯示"""
        assert self.common.poco_exists(author_locator), '創作者標籤未顯示'
        assert self.common.poco_get_text(author_locator) == '创作者', '創作者標籤顯示錯誤'

    def _get_current_time(self):
        """獲取當前時間"""
        return datetime.datetime.now().strftime("%H:%M")

    def post_recent_comment_add_reply(self, recent_commenter, replier, reply_content, self_post=True):
        """回覆評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)

        self.common.poco_click(SocialMediaLibraryPageLocator.post_recent_comment_reply_btn)
        self._verify_reply_target(recent_commenter)

        self._clear_and_input_reply(reply_content)
        self._send_reply_and_verify(replier, reply_content, self_post,SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_commenter)

        self._verify_comment_count_updated(original_comment_count, self_post)
        if self_post:
            self._verify_creator_label(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_author)
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)  # 關閉評論頁

    def _verify_reply_target(self, recent_commenter):
        """驗證回覆目標"""
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_input_comment).__contains__(f'回复{recent_commenter}'), '留言輸入框內的回覆對象錯誤'

    def _clear_and_input_reply(self, reply_content):

        # 清除輸入框內容
        # self.common.poco_long_click(SocialMediaLibraryPageLocator.post_input_comment)
        # sleep(1)
        # self.common.poco_click(SocialMediaLibraryPageLocator.toolbar_menu_text_select_all)
        # sleep(1)
        # self.common.poco_click(SocialMediaLibraryPageLocator.toolbar_menu_text_cut)

        # 輸入回覆內容
        self.common.poco_send_text(SocialMediaLibraryPageLocator.post_input_comment, reply_content)

    def _send_reply_and_verify(self, replier, reply_content, self_post, replier_locator):
        """送出回覆並驗證回覆訊息"""
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_send_btn)
        send_time = self._get_current_time()
        assert self.common.poco_get_text(replier_locator) == replier, '母留言的回覆者暱稱顯示錯誤'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_comment_content) == reply_content, '母留言的回覆內容顯示錯誤'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_add_time) == send_time, f'母留言的回覆時間顯示錯誤, 預期:{send_time},實際:{self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_add_time)}'
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_reply_btn), '母留言的回覆未出現回覆鍵'
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_thumb_up_icon), '母留言的回覆未出現點贊icon'

    def post_recent_comment_recent_reply_add_reply(self, recent_comment_recent_replier, sub_replier,
                                                   reply_reply_content, self_post=True):
        """回覆子評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)

        self.common.poco_click(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_reply_btn)
        self._verify_reply_target(recent_comment_recent_replier)

        self._clear_and_input_reply(reply_reply_content)
        self._send_reply_and_verify(sub_replier, reply_reply_content, self_post,SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_commenter)

        self._verify_reply_chain(sub_replier, recent_comment_recent_replier)
        self._verify_comment_count_updated(original_comment_count, self_post)

    def _verify_reply_chain(self, sub_replier, recent_comment_recent_replier):
        """確認回覆鏈中的暱稱和回覆對象"""
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_commenter) == sub_replier, '回覆者暱稱顯示錯誤'
        assert self.common.poco_exists(SocialMediaLibraryPageLocator.reply_to_icon), '未出現回覆鏈中的">"符號'
        assert self.common.poco_get_text(SocialMediaLibraryPageLocator.reply_to_target_nickname) == recent_comment_recent_replier, '回覆對象顯示錯誤'

    def into_liked_library(self, privacy_self=0):
        self.common.poco_click(SocialMediaLibraryPageLocator.library_liked_icon)
        if privacy_self != 0:  # 0:所有人
            sleep(3)
            assert self.common.poco_exists(SocialMediaLibraryPageLocator.privacy_msg)
            # assert self.common.poco_get_text(SocialMediaLibraryPageLocator.privacy_msg) == '此用户的按赞视频不公开', f'預期:此用户的按赞视频不公开,實際:{self.common.poco_get_text(SocialMediaLibraryPageLocator.privacy_msg)}'
        else:
            assert self.common.poco_exists(SocialMediaLibraryPageLocator.first_media)

    def return_to_post_list(self):
        if self.common.poco_exists(SocialMediaLibraryPageLocator.post_comment_close_btn):
            self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)
        if self.common.poco_exists(SocialMediaLibraryPageLocator.media_back_btn):
            self.common.poco_click(SocialMediaLibraryPageLocator.media_back_btn)

    def is_post_comment(self, enable=True):
        self.common.poco_click(SocialMediaLibraryPageLocator.comment_icon)
        sleep(2)
        if enable:
            assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_input_comment_column) == '添加评论'
        else:
            assert self.common.poco_get_text(SocialMediaLibraryPageLocator.post_no_comment_permission_hint) == '无权限评论'
        self.common.poco_click(SocialMediaLibraryPageLocator.post_comment_close_btn)
