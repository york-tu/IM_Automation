from time import sleep

# from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class MediaReleasePageLocator(BaseLocator):
    """媒體發布頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    release_media_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon'),
        iOS=base.data_collation(type_kind='name', type_name='Button', num=-1),
    )

    media_select_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/ctv_selected', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    writing_instructions = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_caption'),
        iOS=base.data_collation(type_kind='text', type_name='撰写说明'),
    )

    draft_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_draft'),
        iOS=base.data_collation(type_kind='text', type_name='草稿'),
    )
    post_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_post'),
        iOS=base.data_collation(type_kind='text', type_name='发布'),
    )
    page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='text', type_name='发布'),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='text', type_name='back'),
    )
    uploading_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='正在上传中'),
        iOS=base.data_collation(type_kind='text', type_name='正在上传中'),
    )
    avatar_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_avatar'),
        iOS=base.data_collation(type_kind='text', type_name='iv_avatar'),
    )
    liked_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_liked'),
        iOS=base.data_collation(type_kind='text', type_name='iv_liked'),
    )
    message_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_message'),
        iOS=base.data_collation(type_kind='text', type_name='iv_message'),
    )
    bookmark_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_bookmark'),
        iOS=base.data_collation(type_kind='text', type_name='iv_bookmark'),
    )
    more_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_more'),
        iOS=base.data_collation(type_kind='text', type_name='iv_more'),
    )
    author_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_name'),
        iOS=base.data_collation(type_kind='text', type_name='tv_author_name'),
    )
    content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='text', type_name='tv_caption'),
    )
    draft_media_folder = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_draft'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    first_media = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_thumbnail', num=1),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    select_media_type_folder = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_album_dropdown_icon'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    media_videos_folder = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Movies'),
        iOS=base.data_collation(type_kind='name', type_name='Movies'),
    )
    media_pictures_folder = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Pictures'),
        iOS=base.data_collation(type_kind='name', type_name='Pictures'),
    )
    video_select_cover = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_edit_cover'),
        iOS=base.data_collation(type_kind='name', type_name='选择封面'),
    )
    video_select_frame_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_hint'),
        iOS=base.data_collation(type_kind='name', type_name='左右滑动，选择最优的封面'),
    )
    save_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_save'),
        iOS=base.data_collation(type_kind='name', type_name='保存'),
    )
    privacy_settings_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='所有人都可以查看这条发布内容'),
        iOS=base.data_collation(type_kind='name', type_name='所有人都可以查看这条发布内容'),
    )
    privacy_page_hint = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='谁可以查看这条发布内容'),
        iOS=base.data_collation(type_kind='name', type_name='谁可以查看这条发布内容'),
    )
    privacy_everyone_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='所有人'),
        iOS=base.data_collation(type_kind='name', type_name='所有人'),
    )
    privacy_mutual_followers_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='互关'),
        iOS=base.data_collation(type_kind='name', type_name='互关'),
    )
    privacy_followers_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='粉丝'),
        iOS=base.data_collation(type_kind='name', type_name='粉丝'),
    )
    privacy_only_self_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='仅自己'),
        iOS=base.data_collation(type_kind='name', type_name='仅自己'),
    )
    close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_end_icon'),
        iOS=base.data_collation(type_kind='name', type_name='iv_end_icon'),
    )
    allow_save_media_to_local_text = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='允许保存至设备'),
        iOS=base.data_collation(type_kind='name', type_name='允许保存至设备'),
    )
    allow_save_media_to_local = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_setting', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='仅自己'),
    )
    @staticmethod
    def media_select(app_package, num):
        message_path = MediaReleasePageLocator.base.check_device(
            Android=MediaReleasePageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/ctv_selected', num=num),
            iOS=MediaReleasePageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return message_path


class MediaReleasePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def select_media(self, media_index, media_type='photo'):
        self.common.poco_click(MediaReleasePageLocator.release_media_btn)
        sleep(2)
        self.common.poco_wait_exists(MediaReleasePageLocator.select_media_type_folder)
        self.common.poco_click(MediaReleasePageLocator.select_media_type_folder)
        if 'photo' in media_type.lower():
            self.common.poco_wait_exists(MediaReleasePageLocator.media_pictures_folder)
            self.common.poco_click(MediaReleasePageLocator.media_pictures_folder)
            sleep(1)
        else:
            self.common.poco_wait_exists(MediaReleasePageLocator.media_videos_folder)
            self.common.poco_click(MediaReleasePageLocator.media_videos_folder)
        self.common.poco_click(MediaReleasePageLocator.media_select(MediaReleasePageLocator.app_package, media_index))
        sleep(0.5)
        assert self.common.poco_get_text(MediaReleasePageLocator.page_title) == '发布', f'未進入發布頁'

    def into_post_page(self, instructions, privacy_index=0, media_type='photo', post=True):
        # ========================== 媒體選擇封面 =======================================
        if 'video' in media_type.lower():  # 當媒體為video時, 出現'選擇封面'字樣
            assert self.common.poco_get_text(MediaReleasePageLocator.video_select_cover) == "选择封面", f'未出現"选择封面"字串'
            self.common.poco_click(MediaReleasePageLocator.video_select_cover)  # 點擊進入選擇封面頁
            self.wait_loading_finish()
            assert self.common.poco_get_text(MediaReleasePageLocator.video_select_frame_hint) == '左右滑动，选择最优的封面', f'進入封面設定頁or提示訊息有誤'
            self.common.poco_click(MediaReleasePageLocator.save_btn)
        else:
            assert not self.common.poco_exists(MediaReleasePageLocator.video_select_cover), f'當媒體為photo時預期不該出現"选择封面"字串'  # 當媒體為photo時, 不出現'選擇封面'字樣
        # ========================== 撰寫說明 =======================================
        self.common.poco_send_text(MediaReleasePageLocator.writing_instructions, instructions)

        # ========================== 隱私設定頁 =======================================
        assert self.common.poco_exists(MediaReleasePageLocator.privacy_settings_btn)
        self.common.poco_click(MediaReleasePageLocator.privacy_settings_btn)
        assert self.common.poco_exists(MediaReleasePageLocator.privacy_page_hint)
        if privacy_index == 2:
            if not self.common.poco_get_attr(MediaReleasePageLocator.privacy_mutual_followers_option, 'checked'):
                self.common.poco_click(MediaReleasePageLocator.privacy_mutual_followers_option)
        elif privacy_index == 3:
            if not self.common.poco_get_attr(MediaReleasePageLocator.privacy_followers_option, 'checked'):
                self.common.poco_click(MediaReleasePageLocator.privacy_followers_option)
        elif privacy_index == 4:
            if not self.common.poco_get_attr(MediaReleasePageLocator.privacy_only_self_option, 'checked'):
                self.common.poco_click(MediaReleasePageLocator.privacy_only_self_option)
        else:
            if not self.common.poco_get_attr(MediaReleasePageLocator.privacy_everyone_option, 'checked'):
                self.common.poco_click(MediaReleasePageLocator.privacy_everyone_option)
        if self.common.poco_exists(MediaReleasePageLocator.close_btn):
            self.common.poco_click(MediaReleasePageLocator.close_btn)

        # ========================== 允許保存至設備 =======================================
        assert self.common.poco_exists(MediaReleasePageLocator.allow_save_media_to_local_text)
        if self.common.poco_get_attr(MediaReleasePageLocator.allow_save_media_to_local, 'checked'):
            self.common.poco_click(MediaReleasePageLocator.allow_save_media_to_local)
            assert not self.common.poco_get_attr(MediaReleasePageLocator.allow_save_media_to_local, 'checked'), f'"允許保存至設備"switch未成功切換至disable'
            self.common.poco_click(MediaReleasePageLocator.allow_save_media_to_local)
        else:
            self.common.poco_click(MediaReleasePageLocator.allow_save_media_to_local)
            assert self.common.poco_get_attr(MediaReleasePageLocator.allow_save_media_to_local, 'checked'), f'"允許保存至設備"switch未成功切換至enable'

        # ========================== 存到草稿夾 or 發布 =======================================
        if not post:
            self.common.poco_click(MediaReleasePageLocator.draft_btn)
        else:
            self.common.poco_click(MediaReleasePageLocator.post_btn)

    def check_media_post(self, account, instructions, post=True):
        if post:
            self.common.poco_wait_exists(MediaReleasePageLocator.avatar_icon, 120)
            assert self.common.poco_exists(MediaReleasePageLocator.avatar_icon), f'頭像icon未顯示'  # 檢查媒體畫面右側出現"頭像"icon
            assert self.common.poco_exists(MediaReleasePageLocator.liked_icon), f'贊icon未顯示'  # 檢查媒體畫面右側出現"贊"icon
            assert self.common.poco_exists(MediaReleasePageLocator.message_icon), f'留言icon未顯示'  # 檢查媒體畫面右側出現"留言"icon
            assert self.common.poco_exists(MediaReleasePageLocator.bookmark_icon), f'收藏icon未顯示'  # 檢查媒體畫面右側出現"收藏"icon
            assert self.common.poco_exists(MediaReleasePageLocator.more_icon), f'分享icon未顯示'  # 檢查媒體畫面右側出現"分享"icon
            assert self.common.poco_get_text(MediaReleasePageLocator.author_name) == account, f'創作者暱稱錯誤'  # 檢查媒體下方作者暱稱
            assert self.common.poco_get_text(MediaReleasePageLocator.content) == instructions, f'媒體說明有誤, 實際:{self.common.poco_get_text(MediaReleasePageLocator.content)}, 預期:{instructions}'  # 檢查媒體下方媒體說明
            self.common.poco_click(MediaReleasePageLocator.back_btn)

    def check_recent_post_media(self, account, instructions):
        # self.poco.swipe([0.5, 0.1], [0.5, 0.5], duration=0.1)
        if self.common.poco_exists(MainPageLocator.share_profile_btn):
            self.common.poco_click(MediaReleasePageLocator.first_media)
            assert self.common.poco_get_text(MediaReleasePageLocator.author_name) == account, f'創作者暱稱錯誤'  # 檢查媒體下方作者暱稱
            assert self.common.poco_get_text(MediaReleasePageLocator.content) == instructions, f'媒體說明有誤'  # 檢查媒體下方媒體說明

