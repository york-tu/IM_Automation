import random
import re
from time import sleep

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.main_page import MainPageLocator
import logging
import common.utils.globalvar as gl


class SocialMediaPostPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)


    @staticmethod
    def env(env):
        env = SocialMediaPostPageLocator.base.check_device(
            Android=SocialMediaPostPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=SocialMediaPostPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    #  主頁 > 發布鍵
    post_media_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view', num=2),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_newPost_button'),
    )
    # 發布媒體 > 相簿
    album_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_photo'),
        iOS=base.data_collation(type_kind='name', type_name='相簿', num=-1),
    )
    #  發布頁 > 撰寫說明
    writing_instructions = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_caption'),
        iOS=base.data_collation(type_kind='name', type_name='snsPublishPost_caption_textView'),
    )
    # 華為>隱藏鍵盤鍵
    hide_keyboard = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='com.huawei.ohos.inputmethod:id/entry_right_container'),
        iOS=base.data_collation(type_kind='name', type_name='更多建议'),
    )
    #  發布頁 > 草稿鍵
    draft_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_draft'),
        iOS=base.data_collation(type_kind='name', type_name='snsPublishPost_saveDraft_button'),
    )
    #  發布頁 > 發布鍵
    post_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_post'),
        iOS=base.data_collation(type_kind='name', type_name='snsPublishPost_publish_button'),
    )
    #  發布頁 > 發布頁標題
    page_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='发布'),
    )
    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='text', type_name='back'),
    )
    uploading_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='正在上传中'),
        iOS=base.data_collation(type_kind='text', type_name='正在上传中'),
    )
    #  發布鍵 > 媒體資料夾下拉選單
    select_media_type_folder = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_album_dropdown_icon'),
        iOS=base.data_collation(type_kind='text', type_name='sv_subtitle'),
    )
    #  發布鍵 > 媒體資料夾下拉選單 > 選video (Movies)
    media_videos_folder = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Movies'),
        iOS=base.data_collation(type_kind='name', type_name='Movies'),
    )
    #  發布鍵 > 媒體資料夾下拉選單 > 選photo
    media_pictures_folder = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Pictures'),
        iOS=base.data_collation(type_kind='name', type_name='Pictures'),
    )
    #  發布頁 > 設定video封面
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
    #  發布頁 > 隱私權設定鍵
    privacy_settings_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='所有人都可以查看这条发布内容'),
        iOS=base.data_collation(type_kind='name', type_name='snsPublishPost_privacySetting_cell'),
    )
    privacy_page_hint = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='谁可以查看这条发布内容'),
        iOS=base.data_collation(type_kind='name', type_name='谁可以查看这条发布内容'),
    )
    #  發布頁 > 隱私權設定 > 所有人
    privacy_everyone_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='所有人'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostAudience_all_view'),
    )
    #  發布頁 > 隱私權設定 > 互關
    privacy_mutual_followers_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='互关'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostAudience_mutualFollowers_view'),
    )
    #  發布頁 > 隱私權設定 > 粉絲
    privacy_followers_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='粉丝'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostAudience_followers_view'),
    )
    #  發布頁 > 隱私權設定 > 僅自己
    privacy_only_self_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='仅自己'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostAudience_onlyMe_view'),
    )
    close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_end_icon'),
        iOS=base.data_collation(type_kind='name', type_name='iv_end_icon'),
    )
    #  發布頁 > "允許保存至設備"選項"標題"
    allow_save_media_to_local_text = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='允许保存至设备'),
        iOS=base.data_collation(type_kind='name', type_name='允许保存至设备'),
    )
    #  發布頁 > "允許保存至設備"選項"開關"
    allow_save_media_to_local = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_setting', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='snsPublishPost_allowSave_switch'),
    )

    @staticmethod
    def media_select(app_package, num):
        media_select_path = SocialMediaPostPageLocator.base.check_device(
            Android=SocialMediaPostPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/ctv_selected', num=num),
            iOS=SocialMediaPostPageLocator.base.data_collation(type_kind='name', type_name='Button', num=num),
        )
        return media_select_path

    @staticmethod
    # video封面選擇則(num=-1~-10)
    def video_cover_select(num):
        video_cover_select_path = SocialMediaPostPageLocator.base.check_device(
            Android=SocialMediaPostPageLocator.base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=num),
            iOS=SocialMediaPostPageLocator.base.data_collation(type_kind='name', type_name=''),
        )
        return video_cover_select_path


class SocialMediaPostPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def select_media(self, media_index, media_type='photo'):
        self.common.poco_click(SocialMediaPostPageLocator.post_media_btn)
        self.common.poco_click(SocialMediaPostPageLocator.album_btn)
        sleep(3)
        if self.common.poco_wait_exists(SocialMediaPostPageLocator.select_media_type_folder):
            self._select_media_folder(media_type)
            sleep(1)
        self.common.poco_click(SocialMediaPostPageLocator.media_select(SocialMediaPostPageLocator.app_package, media_index))
        sleep(1)
        assert self.common.poco_get_text(SocialMediaPostPageLocator.page_title) == '发布', '未進入發布頁'

    def _select_media_folder(self, media_type):
        self.common.poco_click(SocialMediaPostPageLocator.select_media_type_folder)
        folder_locator = (SocialMediaPostPageLocator.media_pictures_folder if 'photo' in media_type.lower()
                          else SocialMediaPostPageLocator.media_videos_folder)
        self.common.poco_wait_exists(folder_locator)
        sleep(1)
        self.common.poco_click(folder_locator)
        sleep(1)

    def post_page_setting_and_post(self, instructions, privacy_index=0, media_type='photo', save_to_local=True,
                                   post=True):
        if 'video' in media_type.lower():
            self._select_video_cover()
        else:
            assert not self.common.poco_exists(
                SocialMediaPostPageLocator.video_select_cover), '當媒體為photo時預期不該出現"选择封面"字串'

        self._write_instructions(instructions)
        self._set_privacy(privacy_index)
        self._allow_save_to_local(save_to_local)

        # 存到草稿夾 or 發布
        self.common.poco_click(
            SocialMediaPostPageLocator.draft_btn if not post else SocialMediaPostPageLocator.post_btn)

    def _select_video_cover(self):
        assert self.common.poco_get_text(SocialMediaPostPageLocator.video_select_cover) == "选择封面", '未出現"选择封面"字串'
        self.common.poco_click(SocialMediaPostPageLocator.video_select_cover)
        self.wait_loading_finish()
        sleep(3)
        assert self.common.poco_get_text(
            SocialMediaPostPageLocator.video_select_frame_hint) == '左右滑动，选择最优的封面', '進入封面設定頁or提示訊息有誤'
        self.common.poco_click(SocialMediaPostPageLocator.video_cover_select(random.randint(-9, -1)))
        self.common.poco_click(SocialMediaPostPageLocator.save_btn)

    def _write_instructions(self, instructions):
        self.common.poco_click(SocialMediaPostPageLocator.writing_instructions)
        self.common.poco_send_text(SocialMediaPostPageLocator.writing_instructions, instructions)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_wait_exists(SocialMediaPostPageLocator.page_title)
            self.common.poco_click(SocialMediaPostPageLocator.page_title)
        else:
            if self.common.poco_exists(SocialMediaPostPageLocator.hide_keyboard):
                self.common.poco_click(SocialMediaPostPageLocator.hide_keyboard)

    def _set_privacy(self, privacy_index):
        privacy_options = [
            SocialMediaPostPageLocator.privacy_everyone_option,
            SocialMediaPostPageLocator.privacy_mutual_followers_option,
            SocialMediaPostPageLocator.privacy_followers_option,
            SocialMediaPostPageLocator.privacy_only_self_option
        ]
        assert self.common.poco_exists(SocialMediaPostPageLocator.privacy_settings_btn)
        self.common.poco_click(SocialMediaPostPageLocator.privacy_settings_btn)
        assert self.common.poco_exists(SocialMediaPostPageLocator.privacy_page_hint)

        if privacy_index in range(4):
            option = privacy_options[privacy_index]
            if not self.common.poco_get_attr(option, 'checked'):
                self.common.poco_click(option)
        else:
            raise ValueError('未設定媒體隱私權限')

        if self.common.poco_exists(SocialMediaPostPageLocator.close_btn):
            self.common.poco_click(SocialMediaPostPageLocator.close_btn)

    def _allow_save_to_local(self, save_to_local: bool):
        """控制 '允許保存至設備' 的開關狀態"""
        locator = SocialMediaPostPageLocator.allow_save_media_to_local
        assert self.common.poco_exists(SocialMediaPostPageLocator.allow_save_media_to_local_text), '"允許保存至設備" 元件不存在'

        def get_status():
            """取得當前開關狀態（回傳 True/False）"""
            attr = 'value' if self.phone_platform.lower() == 'ios' else 'checked'
            val = self.common.poco_get_attr(locator, attr)
            return val in ('1', True)

        current_status = get_status()

        # 若狀態不同，執行切換
        if current_status != save_to_local:
            self.common.poco_long_click(locator)

        # 驗證切換後狀態
        assert get_status() == save_to_local, \
            f'"允許保存至設備" 未成功設為 {"開啟" if save_to_local else "關閉"}'

    # =================================== ios 發布貼文 # =================================== ios 發布貼文
    def ios_select_media(self, media_index):
        self.common.poco_click(SocialMediaPostPageLocator.post_media_btn)
        self.common.poco_click(SocialMediaPostPageLocator.album_btn)
        sleep(3)
        self.common.poco_click(SocialMediaPostPageLocator.media_select(SocialMediaPostPageLocator.app_package, media_index))
        sleep(1)
