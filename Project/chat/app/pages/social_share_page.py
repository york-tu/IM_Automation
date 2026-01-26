import re
from time import sleep
from poco.exceptions import PocoNoSuchNodeException
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator

import logging
import common.utils.globalvar as gl


class SocialSharePageLocator(BaseLocator):
    """社群分享頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    # 自己主頁-分享主頁
    share_self_profile_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_share_profile'),
        iOS=base.data_collation(type_kind='name', type_name='myProfile_shareMyInfoPage_button'),
    )
    # 他人主頁-分享鍵
    share_others_profile_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_right'),
        iOS=base.data_collation(type_kind='name', type_name='icon share img'),
    )
    # 自己貼文-更多鍵
    share_self_post_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_shared'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostFeed_more_button'),
    )
    # 他人貼文-分享鍵
    share_other_post_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_shared'),
        iOS=base.data_collation(type_kind='name', type_name='snsPostFeed_share_button'),
    )
    # 他人貼文-上一頁鍵
    post_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='chevron Left shadow'),
    )
    # ============================= 分享彈窗 ====================================
    # 分享彈窗標題
    share_popup_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='发送.*'),
    )
    # 分享彈窗close鍵
    share_popup_close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_close'),
        iOS=base.data_collation(type_kind='name', type_name='snsShare_close_button'),
    )
    # ...更多鍵
    share_more_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/v_circle'),
        iOS=base.data_collation(type_kind='name', type_name='snsShare_chatroom_more_cell'),
    )
    # 複製連結鍵_1
    copy_link_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制连结'),
        iOS=base.data_collation(type_kind='name', type_name='复制连结'),
    )
    # 三方app-短信鍵_2
    message_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='短信'),
        iOS=base.data_collation(type_kind='name', type_name='短信'),
    )
    # 三方app-電子郵箱鍵_3
    mail_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='电子邮箱'),
        iOS=base.data_collation(type_kind='name', type_name='电子邮箱'),
    )
    # 三方app-WhatsApp鍵_4
    WhatsApp_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='WhatsApp'),
        iOS=base.data_collation(type_kind='text', type_name='WhatsApp'),
    )
    # 三方app-WhatsApp鍵_4
    Telegram_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Telegram'),
        iOS=base.data_collation(type_kind='text', type_name='Telegram'),
    )
    # 分享列表-搜索欄
    share_search_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='snsShareToChatroom_search_textField'),
    )
    # 分享列表-select btn
    share_select_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_selected'),
        iOS=base.data_collation(type_kind='name', type_name='snsShareToChatroom_member_cell'),
    )
    # 分享列表-留言欄位
    share_input_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input'),
        iOS=base.data_collation(type_kind='name', type_name='snsShareToChatroom_shareMessage_textView'),
    )
    # 分享列表-留言"送出"鍵
    share_send_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_send'),
        iOS=base.data_collation(type_kind='name', type_name='snsShareToChatroom_shareMessage_send_button'),
    )

    # ============= 貼文設定相關 =============
    # 分享彈窗 > "儲存至裝置"鍵
    share_popup_save_to_device_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='储存至装置'),
        iOS=base.data_collation(type_kind='name', type_name='储存至装置'),
    )
    # 分享彈窗 > "隱私設置"鍵
    share_popup_privacy_setup_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='隐私设置'),
        iOS=base.data_collation(type_kind='name', type_name='隐私设置'),
    )
    # 分享彈窗 > "刪除"鍵
    share_popup_delete_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='删除'),
        iOS=base.data_collation(type_kind='name', type_name='删除'),
    )
    # ============= 檢舉頁 =============
    # 分享彈窗 > "檢舉"鍵
    share_popup_report_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='检举'),
        iOS=base.data_collation(type_kind='name', type_name='检举'),
    )
    # "滥发广告" radio button
    share_popup_spam_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='滥发广告'),
        iOS=base.data_collation(type_kind='name', type_name='滥发广告'),
    )
    # "色情内容" radio button
    share_popup_sexual_content_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='色情内容'),
        iOS=base.data_collation(type_kind='name', type_name='色情内容'),
    )
    # "骚扰内容" radio button
    share_popup_harassment_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='骚扰内容'),
        iOS=base.data_collation(type_kind='name', type_name='骚扰内容'),
    )
    # "其他" radio button
    share_popup_other_option = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='其他'),
        iOS=base.data_collation(type_kind='name', type_name='其他'),
    )
    # ============================= 聊天室內分享文 ====================================
    # 聊天室內-分享主頁-作者
    chat_share_author_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_name', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 聊天室內-分享主頁-貼文1
    chat_share_post_1 = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_post_1', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 聊天室內-分享主頁-貼文2
    chat_share_post_2 = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_post_2', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 聊天室內-分享主頁-貼文3
    chat_share_post_3 = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_post_3', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 聊天室內-分享主頁-留言
    chat_share_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )
    # 聊天室內-分享主頁-自己
    chat_share_self_main_page = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_shareAuthorMessageR_cell', num=-1),
    )
    # 聊天室內-分享主頁-他人
    chat_share_other_main_page = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_shareAuthorMessageL_cell', num=-1),
    )
    # 聊天室內-分享貼文-縮圖
    chat_share_self_post_thumbnail = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_post_thumbnail', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_sharePostMessageR_cell', num=-1),
    )
    chat_share_other_post_thumbnail = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_post_thumbnail', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_sharePostMessageL_cell', num=-1),
    )


class SocialSharePage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def check_share_popup_window(self, save_to_local=True, self_post=True):
        from Project.chat.app.pages.social_media_library_page import SocialMediaLibraryPageLocator
        self.common.poco_click(SocialMediaLibraryPageLocator.more_icon)
        # ====================== 上方區塊-標題 ====================================================
        assert self.common.poco_get_text(SocialSharePageLocator.share_popup_title) == '发送给'
        # ====================== 中間區塊-3方APP =================================================
        assert self.common.poco_exists(SocialSharePageLocator.copy_link_btn)  # 複製連結
        assert self.common.poco_exists(SocialSharePageLocator.message_btn)  # 短信
        assert self.common.poco_exists(SocialSharePageLocator.mail_btn)  # 電子郵件
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_exists(SocialSharePageLocator.WhatsApp_btn)  # WhatsApp
            assert self.common.poco_exists(SocialSharePageLocator.Telegram_btn)  # Telegram
        # ====================== 下方區塊-設定 ====================================================
        if save_to_local:  # 當貼文發布時"儲存至裝置"選項有開啟時, 會看到選項
            assert self.common.poco_exists(SocialSharePageLocator.share_popup_save_to_device_btn)
        else:
            assert not self.common.poco_exists(SocialSharePageLocator.share_popup_save_to_device_btn)
        if self_post:  # 當貼文為自己發布時, 自己畫面會出現"隱私設置"鍵與"刪除"鍵
            assert self.common.poco_exists(SocialSharePageLocator.share_popup_privacy_setup_btn)
            assert self.common.poco_exists(SocialSharePageLocator.share_popup_delete_btn)
        else:
            assert not self.common.poco_exists(SocialSharePageLocator.share_popup_privacy_setup_btn)
            assert not self.common.poco_exists(SocialSharePageLocator.share_popup_delete_btn)

        self.common.poco_click(SocialSharePageLocator.share_popup_close_btn)

    def into_share_pop_window(self, share_type=0):  # 0=self_main_page, 1=other_main_page, 2=self_post,3=other_post
        if share_type == 0:
            self.common.poco_click(SocialSharePageLocator.share_self_profile_btn)
        elif share_type == 1:
            self.common.poco_click(SocialSharePageLocator.share_others_profile_btn)
        elif share_type == 2:
            self.common.poco_click(SocialSharePageLocator.share_self_post_btn)
        elif share_type == 3:
            self.common.poco_click(SocialSharePageLocator.share_other_post_btn)

        assert self.common.poco_get_text(SocialSharePageLocator.share_popup_title) == '发送给', '分享彈窗錯誤'

    def share_to_group(self, share_target_group, share_message='', share_main_page=True):
        sleep(5)
        self.common.poco_click(SocialSharePageLocator.share_more_btn)
        self.common.poco_click(SocialSharePageLocator.share_search_content)
        self.common.poco_send_text(SocialSharePageLocator.share_search_content, share_target_group)
        self.common.poco_click(SocialSharePageLocator.share_select_btn)
        # assert self.common.poco_get_text(SocialSharePageLocator.share_input_message) == '有什么想和朋友说的…', f'留言欄位預設文字錯誤'
        self.common.poco_click(SocialSharePageLocator.share_input_message)
        self.common.poco_send_text(SocialSharePageLocator.share_input_message, share_message)
        self.common.poco_click(SocialSharePageLocator.share_send_btn)
        if not share_main_page:
            self.common.poco_click(SocialSharePageLocator.post_back_btn)

    def check_chatroom_share_result(self, content_creator, share_message='', share_main_page=True, my_share=True):
        sleep(3)
        if self.phone_platform.lower() == 'android':
            actual_creator = self.common.poco_get_text(SocialSharePageLocator.chat_share_author_name)
            assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'
            if share_main_page:
                assert self.common.poco_exists(SocialSharePageLocator.chat_share_post_1)
                assert self.common.poco_exists(SocialSharePageLocator.chat_share_post_2)
                assert self.common.poco_exists(SocialSharePageLocator.chat_share_post_3)
            else:
                assert self.common.poco_exists(SocialSharePageLocator.chat_share_self_post_thumbnail)
            if share_message != '':
                try:
                    actual_share_message = self.common.poco_get_text(SocialSharePageLocator.chat_share_message)
                    assert actual_share_message == share_message, f'分享貼文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                except PocoNoSuchNodeException:
                    assert False, '分享文沒有含留言'
        else:  # ios part
            if my_share:  # 我的分享
                if share_main_page:  # 分享主頁
                    assert self.common.poco_exists(SocialSharePageLocator.chat_share_self_main_page)
                    actual_creator = self.poco(name='message_shareAuthorMessageR_cell')[-1].offspring(type='StaticText')[0].attr('value')
                    assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'
                    if share_message != '':
                        try:
                            actual_share_message = self.poco(name='message_shareAuthorMessageR_cell')[-1].offspring(type='TextView')[0].attr('value')
                            assert actual_share_message == share_message, f'分享貼文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                        except PocoNoSuchNodeException:
                            assert False, '分享文沒有含留言'
                else:  # 分享貼文
                    assert self.common.poco_exists(SocialSharePageLocator.chat_share_self_post_thumbnail)
                    actual_creator = self.poco(name='message_sharePostMessageR_cell')[-1].offspring(type='StaticText')[0].attr('value')
                    assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'
                    if share_message != '':
                        try:
                            actual_share_message = self.poco(name='message_sharePostMessageR_cell')[-1].offspring(type='TextView')[0].attr('value')
                            assert actual_share_message == share_message, f'分享貼文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                        except PocoNoSuchNodeException:
                            assert False, '分享文沒有含留言'
            else:  # 他人的分享
                if share_main_page:  # 分享主頁
                    assert self.common.poco_exists(SocialSharePageLocator.chat_share_other_main_page)
                    actual_creator = self.poco(name='message_shareAuthorMessageL_cell')[-1].offspring(type='StaticText')[1].attr('value')
                    assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'
                    if share_message != '':
                        try:
                            actual_share_message = self.poco(name='message_shareAuthorMessageL_cell')[-1].offspring(type='TextView')[0].attr('value')
                            assert actual_share_message == share_message, f'分享文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                        except PocoNoSuchNodeException:
                            assert False, '分享文沒有含留言'
                else:  # 分享貼文
                    assert self.common.poco_exists(SocialSharePageLocator.chat_share_other_post_thumbnail)
                    actual_creator = self.poco(name='message_sharePostMessageL_cell')[-1].offspring(type='StaticText')[1].attr('value')
                    assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'
                    if share_message != '':
                        try:
                            actual_share_message = self.poco(name='message_sharePostMessageL_cell')[-1].offspring(type='TextView')[0].attr('value')
                            assert actual_share_message == share_message, f'分享文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                        except PocoNoSuchNodeException:
                            assert False, '分享文沒有含留言'

    def submit_impeach_request(self, reason_type):
        self.into_share_pop_window(3)
        self.common.poco_click(SocialSharePageLocator.share_popup_report_btn)
        options = {
            0: SocialSharePageLocator.share_popup_spam_option,
            1: SocialSharePageLocator.share_popup_sexual_content_option,
            2: SocialSharePageLocator.share_popup_harassment_option,
            3: SocialSharePageLocator.share_popup_other_option
        }

        if reason_type in options:
            self.common.poco_click(options[reason_type])
            reason = self.common.poco_get_text(options[reason_type])
            self.common.poco_click(SocialSharePageLocator.share_send_btn)
            return reason
        return ''