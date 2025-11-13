import re
from datetime import datetime
from time import sleep
from airtest.core.api import text, touch
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.point_page import PointPageLocator

import logging
import common.utils.globalvar as gl


class ChatRoomPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    search_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    search_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=str(app_package) + ':id/btn_search'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    message_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input'),
        iOS=base.data_collation(type_kind='name', type_name='message_inputText_textView'),
    )

    message_input_block = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tvInputBlock'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    message_input_empty = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='Aa'),
        iOS=base.data_collation(type_kind='name', type_name='Aa'),
    )

    brand = (gl.get_value('BRAND') or '').strip().lower()
    android_id = f"{app_package}:id/btn_send" if brand == 'mingpin' else f"{app_package}:id/iv_send"
    send_message_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=android_id),
        iOS=base.data_collation(type_kind='name', type_name='message_inputText_send_button'),
    )

    send_message_btn1 = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_send'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    retry_send_message_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_resend'),
        iOS=base.data_collation(type_kind='name', type_name=':id/btn_resend'),
    )

    add_function_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_add_function'),
        iOS=base.data_collation(type_kind='name', type_name='message_inputText_addAttachment_button'),
    )

    last_message_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_textMessageRCell_textView', num=-1),
    )
    last_voice_message_room = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceMessageR_cell', num=-1),
    )

    replied_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_replyMessageRCell_textView', num=-1),
    )

    messages_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content'),
        iOS=base.data_collation(type_kind='name', type_name='新增好友'),
    )

    menu_copy = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制'),
        iOS=base.data_collation(type_kind='name', type_name='复制'),
    )

    menu_reply = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='回复'),
        iOS=base.data_collation(type_kind='name', type_name='回复'),
    )

    menu_pin = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='设为公告'),
        iOS=base.data_collation(type_kind='name', type_name='设为公告'),
    )

    menu_delete = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='删除'),
        iOS=base.data_collation(type_kind='name', type_name='删除'),
    )

    popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='公告已满5则.*'),
    )

    popup_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='type', type_name='ScrollView', num=1),
    )

    menu_revoke = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='撤回'),
        iOS=base.data_collation(type_kind='name', type_name='撤回'),
    )

    menu_paste = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='粘贴'),
        iOS=base.data_collation(type_kind='name', type_name='粘贴'),
    )

    paste_popup = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='com.android.systemui:id/dismiss_image'),
        iOS=base.data_collation(type_kind='name', type_name='name'),
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button'),
    )

    next_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_next'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    reply_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply_sender_name'),
        iOS=base.data_collation(type_kind='name', type_name='message_replyMessage_sender_label'),
    )

    reply_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply_sender_message'),
        iOS=base.data_collation(type_kind='name', type_name='message_replyMessage_message_label'),
    )
    reply_file_message = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='nameMatches', type_name='0_TestExample.*', num=-1),
    )
    reply_voice_original_msg = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_reply_sender_message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='00:.*', num=-1),
    )

    reply_title_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/quoted_content',
                                    action='child()[1]'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    cancel_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_cancel'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    url_check_point = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=f'com.android.chrome:id/coordinator'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    author_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_author_name'),
        iOS=base.data_collation(type_kind='name', type_name='message_replyMessageRCell_replySender_label', num=-1),
    )

    event_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_event_name', num=-1),
        iOS=base.data_collation(type_kind='nameMatches', type_name='.*一则.*', num=-1),
    )

    pin_open_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_expand'),
        iOS=base.data_collation(type_kind='name', type_name='iconArrowsChevronDown'),
    )

    pin_close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_collapse'),
        iOS=base.data_collation(type_kind='name', type_name='iconArrowsChevronUp'),
    )

    pin_not_show_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_do_not_show_again', num=0),
        iOS=base.data_collation(type_kind='name', type_name='不再显示'),
    )

    pin_messages = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_sender_message'),
        iOS=base.data_collation(type_kind='type', type_name='Image'),
    )
    pin_messages_label = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_announcement_label'),
    )

    pin_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_sender_name', num=0),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    pin_popup = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_announcement_container'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    emoji_thumbs = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_thumbs_up'),
        iOS=base.data_collation(type_kind='name', type_name='gereralTooltipsEmojiBoxEmojiLike')
    )

    emoji_grinning = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_grinning_squinting_face'),
        iOS=base.data_collation(type_kind='name', type_name='gereralTooltipsEmojiBoxEmojiFunny')
    )

    emoji_heart = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_red_heart'),
        iOS=base.data_collation(type_kind='name', type_name='gereralTooltipsEmojiBoxEmojiLove')
    )

    emoji_crying = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_crying_face'),
        iOS=base.data_collation(type_kind='name', type_name='gereralTooltipsEmojiBoxEmojiSad')
    )

    emoji_astonished = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_astonished_face'),
        iOS=base.data_collation(type_kind='name', type_name='gereralTooltipsEmojiBoxEmojiWow')
    )

    emoji_multiple = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_emoji_1', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    emoji_count = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_count', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    emoji_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_root'),
        iOS=base.data_collation(type_kind='name', type_name='message_messageRCell_emoji_button', num=-1)
    )

    image_photo = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_photo'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    image_camera = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_camera'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    options_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_options'),
        iOS=base.data_collation(type_kind='name', type_name='message_more_button')
    )

    options_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=1)
    )

    options_delete_and_leave = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_delete_and_leave'),
        iOS=base.data_collation(type_kind='text', type_name='刪除並退出')
    )
    option_delete_history = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_delete_history'),
        iOS=base.data_collation(type_kind='name', type_name='groupDetail_deleteConversation_cell')
    )

    options_leave_group_confirm_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='退出群组'),
        iOS=base.data_collation(type_kind='text', type_name='退出群组')
    )

    red_envelope_system_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_event_name', num=-1),
        iOS=base.data_collation(type_kind='nameMatches', type_name='.*领取了.*', num=-1)
    )

    red_envelope_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_root', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_hongBaoMessageL_cell', num=-1)
    )

    red_envelope_open_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_open'),
        iOS=base.data_collation(type_kind='name', type_name='message_hongBao_open_button')
    )

    red_envelope_amount = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='message_hongBao_amount_label')
    )
    close_red_envelope_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_close'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconCross', num=-1)
    )
    close_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_close'),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_close_button')
    )

    # =========== 語音 ============
    mic_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='语音'),
        iOS=base.data_collation(type_kind='name', type_name='message_attachment_voice_button')
    )
    record_voice_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_audio_state'),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_record_button')
    )
    stop_record_voice_btn = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_recording_button')
    )
    record_count = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_count'),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_title_label')
    )
    send_voice_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_send'),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_send_button')
    )
    last_voice_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_duration', num=-1),
        iOS=base.data_collation(type_kind='nameMatches', type_name='00:.*', num=-1)
    )
    popup_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_voiceRecording_title_label')
    )

    # =========== 檔案 ============
    file_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='档案'),
        iOS=base.data_collation(type_kind='name', type_name='message_attachment_file_button')
    )
    file_first_name = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/title'),
        iOS=base.data_collation(type_kind='name', type_name='xxx')
    )
    confirm_msg_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='您要传送.*')
    )
    confirm_msg_send_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='传送'),
        iOS=base.data_collation(type_kind='name', type_name='传送')
    )
    last_chatroom_filename = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_filename', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_fileMessageRCell_fileName_label', num=-1)
    )

    @staticmethod
    def message_locator(message, num=-1):
        message_path = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='text', type_name=message, num=num),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='value', type_name=message, num=num),
        )

        return message_path

    @staticmethod
    def folder_file_index(num=-1):
        folder_file_path = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name='android:id/title', num=num),
            iOS=ChatRoomPageLocator.base.data_collation(
                type_kind='nameMatches', type_name='0_TestExample.*', num=num,
                parent={'type_kind': 'type', 'type_name': 'Cell', 'num': num}
            ),
        )
        return folder_file_path

    @staticmethod
    def chatroom_file_index(app_package, num=-1):
        chatroom_file_message_path = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_filename', num=num),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name='', num=num),
        )

        return chatroom_file_message_path

    @staticmethod
    def message_emoji_locator(message):
        message_path = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='text', type_name=message,
                                                            action='parent().sibling()[0]', num=-1),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name=message, num=-1),
        )

        return message_path

    @staticmethod
    def message_emoji_multiple_locator(message):
        message_path = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='text', type_name=message,
                                                            action='parent().sibling()[1].child()'),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name='搜索')
        )

        return message_path

    @staticmethod
    def pin_messages_locator(app_package, num):
        pin_text = ChatRoomPageLocator.base.check_device(
            Android=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_sender_message', num=num),
            iOS=ChatRoomPageLocator.base.data_collation(type_kind='name', type_name='message_announcement_message_label', num=num)
        )

        return pin_text


class ChatRoomPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_setting(self):
        if self.common.poco_exists(ChatRoomPageLocator.options_btn):
            self.common.poco_click(ChatRoomPageLocator.options_btn)
            title = self.common.poco_get_text(ChatRoomPageLocator.options_title)
            assert title[2:] == '详情', f'進入設定頁面有誤'

    def send_message(self, message):
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, message)
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)

            last_room_msg = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
            assert last_room_msg == message, f'發送聊天訊息有誤, 預期: {message}, 實際:{last_room_msg}'

        else:
            self.common.poco_send_text(ChatRoomPageLocator.message_input, message)
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
            if self.common.poco_exists(ChatRoomPageLocator.retry_send_message_btn):
                self.common.poco_click(ChatRoomPageLocator.retry_send_message_btn)
            last_room_msg = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
            assert last_room_msg == message, f'發送聊天訊息有誤, 預期: {message}, 實際:{last_room_msg}'

    def send_text_message(self):
        messages = '自动化测试'
        if self.phone_platform.lower() == 'ios':
            # self.common.poco_click(ChatRoomPageLocator.message_input)

            # messages = '測試TeSt12345!@#$%测试'
            num = 0
            for _ in range(0, 6):
                self.send_message(f'{messages}#{num}')
                num = num + 1

            touch((200, 500))

        else:  # android part
            if self.common.poco_exists(ChatRoomPageLocator.send_message_btn):
                self.common.poco_click(ChatRoomPageLocator.message_input)
                self.common.poco_send_text(ChatRoomPageLocator.message_input, 'clear_text')
                self.common.poco_click(ChatRoomPageLocator.send_message_btn)
            else:
                self.common.poco_click(ChatRoomPageLocator.message_input)

            # messages = '測試TeSt12345!@#$%测试'
            num = 0
            for _ in range(0, 6):
                text = str(messages) + '#' + str(num)
                self.send_message(text)

                if self.common.poco_exists(ChatRoomPageLocator.retry_send_message_btn):
                    self.common.sleep(1)
                    self.common.poco_click(ChatRoomPageLocator.retry_send_message_btn)
                    self.common.sleep(1)
                num = num + 1

            self.go_back()

    def send_url_message(self):
        messages = ['https://google.com.tw', 'https://gu-chat.com']

        if self.common.poco_exists(ChatRoomPageLocator.send_message_btn):
            if self.phone_platform.lower() == 'ios':
                self.poco(type='Other')[-1].click()
            else:
                self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, 'clear_text')
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
        else:
            self.common.poco_click(ChatRoomPageLocator.message_input)

        for message in messages:
            self.send_message(message)
            self.check_url_message(message)

    def check_url_message(self, message):
        if self.phone_platform.lower() == 'android':
            if self.common.poco_exists(ChatRoomPageLocator.message_locator(message)):
                self.common.poco_click(ChatRoomPageLocator.message_locator(message))
                self.common.sleep(3)
                assert self.common.poco_exists(ChatRoomPageLocator.url_check_point), f'超連結沒有出現'
                self.go_back()
        # else:
        #     context_url = self.poco(type='TextView')[-2].attr('name')
        #     assert context_url.__contains__('https://'), f'超連結沒有出現'

    def draft_message(self, message):

        if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, message)

    def copy_message(self, message):
        while not self.common.poco_exists(ChatRoomPageLocator.menu_copy):
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        self.common.poco_wait_exists(ChatRoomPageLocator.menu_copy)
        self.common.poco_click(ChatRoomPageLocator.menu_copy)  # 複製

        self.common.poco_long_click(ChatRoomPageLocator.message_input)
        # self.common.poco_wait_exists(ChatRoomPageLocator.menu_paste)
        # self.common.poco_click(ChatRoomPageLocator.menu_paste)  # 貼上

        for _ in range(0, 3):
            if self.common.poco_exists(ChatRoomPageLocator.menu_paste):
                self.common.poco_click(ChatRoomPageLocator.menu_paste)
                break
            else:
                self.common.poco_long_click(ChatRoomPageLocator.message_input)

        self.common.poco_click(ChatRoomPageLocator.send_message_btn)

    def reply_message(self, message):
        self.common.poco_click(ChatRoomPageLocator.message_locator(message))
        while not self.common.poco_exists(ChatRoomPageLocator.menu_reply):
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        self.common.poco_click(ChatRoomPageLocator.menu_reply)  # 回復

        if self.phone_platform.lower() == 'ios':
            title = self.common.poco_get_text(ChatRoomPageLocator.reply_name)
            reply_message = self.common.poco_get_text(ChatRoomPageLocator.reply_message)
            assert title.__contains__(f'回复')  # 確認訊息回覆時標題為"回覆{原訊息發話成員}}"
            assert message == reply_message, f'回覆訊息預覽有誤'  # 確認原訊息

            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, '回覆訊息测试Test')
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
            touch((300, 600))

            original_msg_user = self.common.poco_get_text(ChatRoomPageLocator.author_name)
            replied_msg = self.common.poco_get_text(ChatRoomPageLocator.replied_message)

            assert title.__contains__(original_msg_user), f'訊息回覆對象有錯, result:{original_msg_user}, expect:{title[3:]}'  # 確認聊天室內訊息回覆框原文發話成員
            assert replied_msg == '回覆訊息测试Test', f'回覆訊息內容有誤, result:{replied_msg}, expect: 回覆訊息测试Test'

        else:  # android part
            title = self.common.poco_get_text(ChatRoomPageLocator.reply_name)
            reply_message = self.common.poco_get_text(ChatRoomPageLocator.reply_message)
            assert title.__contains__('回复'), f'訊息回覆標題有誤'
            assert message == reply_message, f'回覆訊息預覽有誤'

            if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
                self.common.poco_send_text(ChatRoomPageLocator.message_input, '回覆訊息测试Test')
                self.common.poco_click(ChatRoomPageLocator.send_message_btn)

                assert title.__contains__(self.common.poco_get_text(ChatRoomPageLocator.author_name)), f'訊息回覆標題有誤'
                assert self.common.poco_get_text(ChatRoomPageLocator.last_message_room) == '回覆訊息测试Test', f'回覆訊息內容有誤'

    def reply_voice_message(self, message):
        while not self.common.poco_exists(ChatRoomPageLocator.menu_reply):
            # if self.phone_platform.lower() == 'ios':
            #     self.common.poco_long_click(ChatRoomPageLocator.last_voice_message_room)
            # else:
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        self.common.poco_click(ChatRoomPageLocator.menu_reply)

        title = self.common.poco_get_text(ChatRoomPageLocator.reply_name)  # 回覆訊息輸入框原訊息發話成員
        if self.phone_platform.lower() == 'ios':
            reply_message = self.common.poco_get_text(ChatRoomPageLocator.reply_voice_original_msg)
        else:
            reply_message = self.common.poco_get_text(ChatRoomPageLocator.reply_message)
        assert title.__contains__('回复'), f'訊息回覆標題有誤'
        assert message == reply_message, f'回覆訊息預覽有誤'

        if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, '回覆語音訊息测试Test')
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)

            original_msg_author_name = self.common.poco_get_text(ChatRoomPageLocator.author_name)
            assert title.__contains__(original_msg_author_name), f'訊息回覆標題有誤'

            if self.phone_platform.lower() == 'ios':
                reply_msg = self.common.poco_get_text(ChatRoomPageLocator.replied_message)
            else:
                reply_msg = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
            assert reply_msg == '回覆語音訊息测试Test', f'回覆訊息內容有誤'

    def reply_file_message(self, message):
        while not self.common.poco_exists(ChatRoomPageLocator.menu_reply):
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        self.common.poco_click(ChatRoomPageLocator.menu_reply)

        title = self.common.poco_get_text(ChatRoomPageLocator.reply_name)
        reply_message = self.common.poco_get_text(ChatRoomPageLocator.reply_message)
        assert title.__contains__('回复'), f'訊息回覆標題有誤'
        assert message == reply_message, f'回覆訊息預覽有誤'

        if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, '回覆檔案訊息测试Test')
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)

            original_msg_author_name = self.common.poco_get_text(ChatRoomPageLocator.author_name)
            reply_msg = self.common.poco_get_text(ChatRoomPageLocator.replied_message)
            assert title.__contains__(original_msg_author_name), f'訊息回覆標題有誤'
            assert reply_msg == '回覆檔案訊息测试Test', f'回覆訊息內容有誤'

    def check_reply_title(self, message):
        assert self.common.poco_exists(ChatRoomPageLocator.message_locator(message)), f'回覆原訊息遺失 顯示有誤'

    def delete_message(self, message, last_message='', num=-1, is_voice=None, is_file=None, is_reply=False):

        # self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
        while not self.common.poco_exists(ChatRoomPageLocator.menu_delete):
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
        self.common.poco_click(ChatRoomPageLocator.menu_delete)

        # for _ in range(0, 3):
        #     if self.common.poco_exists(ChatRoomPageLocator.menu_delete):
        #         self.common.poco_click(ChatRoomPageLocator.menu_delete)
        #         break
        #     else:
        #         if self.phone_platform.lower() == 'ios':
        #             self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
        #         else:
        #             self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
        self.common.poco_click(ChatRoomPageLocator.popup_btn)

        # self.common.poco_wait_disappearance(ChatRoomPageLocator.message_locator(message))

        if last_message == '':
            pass
        else:
            if is_voice:
                assert self.common.poco_get_text(ChatRoomPageLocator.last_voice_message) == last_message
            elif is_file:
                assert self.common.poco_get_text(ChatRoomPageLocator.last_chatroom_filename) == last_message
            elif is_reply and self.phone_platform.lower() == 'ios':
                assert self.common.poco_get_text(ChatRoomPageLocator.replied_message) == last_message
            else:
                actual_last_msg = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
                assert actual_last_msg == last_message, f'實際:{actual_last_msg}, 預期:{last_message}'

    def get_last_message(self, is_voice=False, is_file=False, is_reply=False):
        self.wait_loading_finish()
        if is_voice:
            return self.common.poco_get_text(ChatRoomPageLocator.last_voice_message)
        elif is_file:
            return self.common.poco_get_text(ChatRoomPageLocator.last_chatroom_filename)
        elif is_reply and self.phone_platform.lower() == 'ios':
            return self.common.poco_get_text(ChatRoomPageLocator.replied_message)
        else:
            return self.common.poco_get_text(ChatRoomPageLocator.last_message_room)

    def revoke_message(self, message, num=-1):
        if self.phone_platform.lower() == 'ios':
            while not self.common.poco_exists(ChatRoomPageLocator.menu_revoke):
                self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
        else:
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message, num))
            self.common.poco_wait_exists(ChatRoomPageLocator.menu_revoke)
        self.common.poco_click(ChatRoomPageLocator.menu_revoke)
        self.common.poco_wait_exists(ChatRoomPageLocator.popup_btn)
        self.common.poco_click(ChatRoomPageLocator.popup_btn)

        if self.phone_platform.lower() == 'ios' and self.common.poco_exists(ChatRoomPageLocator.event_message):
            pin_event_message = self.common.poco_get_text(ChatRoomPageLocator.event_message)
        else:
            pin_event_message = self.common.poco_get_text(ChatRoomPageLocator.event_message)

        if pin_event_message.__contains__('设定了一则公告'):
            if self.common.poco_exists(ChatRoomPageLocator.pin_open_btn):
                self.common.poco_click(ChatRoomPageLocator.pin_open_btn)
                self.wait_loading_finish()
                pin_list = self.get_pin_message()
                assert message not in pin_list, f'訊息撤回後，公告沒有消失'
            else:
                pass
        else:
            assert self.common.poco_get_text(ChatRoomPageLocator.event_message) == '你已撤收一则讯息', f'系統訊息有誤'

    def pin_message(self, message):
        self.common.poco_click(ChatRoomPageLocator.message_locator(message))

        # for _ in range(0, 5):
        #     if self.common.poco_exists(ChatRoomPageLocator.menu_pin):
        #         self.common.poco_click(ChatRoomPageLocator.menu_pin)
        #         break
        #     else:
        #         self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        #         self.common.poco_wait_exists(ChatRoomPageLocator.menu_pin)
        while not self.common.poco_exists(ChatRoomPageLocator.menu_pin):
            self.common.poco_long_click(ChatRoomPageLocator.message_locator(message))
        # self.common.poco_wait_exists(ChatRoomPageLocator.menu_pin)
        self.common.poco_click(ChatRoomPageLocator.menu_pin)

        if self.common.poco_exists(ChatRoomPageLocator.popup_message):
            assert self.common.poco_get_text(ChatRoomPageLocator.popup_message) == '公告已满5则，无法新增，请取消欲替换的公告', f'彈窗訊息有誤'
            self.common.poco_click(ChatRoomPageLocator.popup_btn)
            return False
        else:
            self.wait_loading_finish()
            assert self.common.poco_get_text(ChatRoomPageLocator.event_message).__contains__('设定了一则公告'), f'系統訊息有誤'
            return True

    def pin_full_messages(self):
        message = '自动化测试#'
        pin_sort = [3, 0, 1, 2, 5, 4]

        times = 1
        expected_list = []
        for number in pin_sort:
            text = message + str(number)
            if times < 6:
                assert self.pin_message(text) is True
                expected_list.append(text)
            else:
                assert self.pin_message(text) is False
                break

            times = times + 1

        self.common.poco_click(ChatRoomPageLocator.pin_open_btn)
        reality_list = self.get_pin_message()
        reality_list.reverse()
        assert reality_list == expected_list, f'公告排序有誤'

    def delete_all_pin(self):
        while self.common.poco_exists(ChatRoomPageLocator.pin_messages):

            if self.phone_platform.lower() == 'ios':
                if self.common.poco_exists(ChatRoomPageLocator.pin_open_btn):
                    self.common.poco_click(ChatRoomPageLocator.pin_open_btn)
                if self.common.poco_exists(ChatRoomPageLocator.pin_not_show_btn):
                    self.common.poco_click(ChatRoomPageLocator.pin_not_show_btn)
                else:
                    assert not self.common.poco_exists(ChatRoomPageLocator.pin_messages_label)
                    break

            else:
                if self.common.poco_exists(ChatRoomPageLocator.pin_open_btn):
                    self.common.poco_click(ChatRoomPageLocator.pin_open_btn)

                self.wait_loading_finish()

                if self.common.poco_exists(ChatRoomPageLocator.pin_not_show_btn):
                    before_message = self.common.poco_get_text(ChatRoomPageLocator.pin_messages)
                    self.common.poco_click(ChatRoomPageLocator.pin_not_show_btn)

                    if self.common.poco_exists(ChatRoomPageLocator.pin_close_btn):
                        after_message = self.common.poco_get_text(ChatRoomPageLocator.pin_messages)
                        assert before_message != after_message, f'公告取消失敗'
                    else:
                        break
                else:
                    print('角色權限不足')
                    break

    def check_pin_message(self, message):

        if self.phone_platform.lower() == 'android':
            if self.common.poco_exists(ChatRoomPageLocator.pin_open_btn):
                self.common.poco_click(ChatRoomPageLocator.pin_open_btn)
                assert message == self.common.poco_get_text(ChatRoomPageLocator.pin_messages)
            self.common.poco_click(ChatRoomPageLocator.pin_close_btn)
        else:
            assert message == self.common.poco_get_text(ChatRoomPageLocator.pin_messages_label)


    def get_pin_message(self):
        # if self.phone_platform.lower() == 'android':
            messages = []
            for pin_num in range(0, 5, 1):
                if self.common.poco_exists(ChatRoomPageLocator.pin_messages_locator(ChatRoomPageLocator.app_package, pin_num)):
                    message = self.common.poco_get_text(ChatRoomPageLocator.pin_messages_locator(ChatRoomPageLocator.app_package, pin_num))
                    messages.append(message)
                else:
                    break
            return messages
        # else:
        #     messages = []
        #     if self.poco(type='Other').child(nameMatches='.*测试.*').exists():
        #         total_pin_nums = len(self.poco(type='Other').child(nameMatches='.*测试.*'))
        #         for pin_num in range(0, total_pin_nums, 1):
        #             message = self.poco(type='Other').child(nameMatches='.*测试.*')[pin_num].attr('name')
        #             messages.append(message)
        #         return messages

    def share_message(self, _text):
        for _ in range(0, 10):
            if self.common.poco_exists(ChatRoomPageLocator.menu_paste):
                self.common.poco_click(ChatRoomPageLocator.menu_paste)
                break
            else:
                self.common.sleep(0.5)
                self.common.poco_long_click(ChatRoomPageLocator.message_input)

        self.common.poco_click(ChatRoomPageLocator.send_message_btn)

        share_text = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
        assert share_text.__contains__(_text), f'分享文案有誤'

    def check_share_url(self, url):
        if self.common.poco_wait_exists(ChatRoomPageLocator.message_locator(url)):
            self.common.poco_click(ChatRoomPageLocator.message_locator(url))
            self.common.sleep(3)

            assert self.common.poco_exists(ChatRoomPageLocator.url_check_point)
            self.go_back()

    def add_emoji(self, message):
        if self.common.poco_exists(ChatRoomPageLocator.message_emoji_locator(message)):
            self.common.poco_click(ChatRoomPageLocator.message_emoji_locator(message))
            self.common.poco_wait_appearance(ChatRoomPageLocator.emoji_btn)
            if self.phone_platform.lower() == 'ios':
                original_pos = self.poco(type='Cell')[-1].attr('pos')
                self.common.poco_click(ChatRoomPageLocator.emoji_btn)
                self.common.poco_click(ChatRoomPageLocator.emoji_crying)
                after_pos = self.poco(type='Cell')[-1].attr('pos')
                assert original_pos is not after_pos
            else:
                self.common.poco_click(ChatRoomPageLocator.emoji_crying)

    def check_emoji(self, message):
        if self.common.poco_exists(ChatRoomPageLocator.message_emoji_multiple_locator(message)):
            assert self.common.poco_exists(ChatRoomPageLocator.emoji_multiple) is True, f'表情符號未顯示'
            assert self.common.poco_get_text(ChatRoomPageLocator.emoji_count) == 1

    def app_grab_red_envelope(self, user_name):
        self.wait_loading_finish()
        self.common.poco_click(ChatRoomPageLocator.red_envelope_message)
        self.common.poco_click(ChatRoomPageLocator.red_envelope_open_btn)
        grab_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        grab_amount = self.common.poco_get_text(ChatRoomPageLocator.red_envelope_amount)

        if grab_amount.endswith('.0'):
            grab_amount = grab_amount[:-2]
        self.common.poco_click(ChatRoomPageLocator.close_red_envelope_btn)
        a = self.common.poco_get_text(ChatRoomPageLocator.red_envelope_system_message)
        assert self.common.poco_get_text(ChatRoomPageLocator.red_envelope_system_message) == f'{user_name} 领取了红包 {grab_amount}', f'系統紅包訊息錯誤, 實際:{a}, 預期:{user_name} 领取了红包 {grab_amount}'

        self.common.poco_click(ChatRoomPageLocator.back_btn)
        return grab_amount, grab_time

    def send_voice_message(self, record_length):
        length = int(record_length)
        sleep(3)
        if self.common.poco_exists(ChatRoomPageLocator.mic_btn):
            self.common.poco_click(ChatRoomPageLocator.mic_btn)
        else:
            self.common.poco_click(ChatRoomPageLocator.add_function_btn)
            self.common.poco_click(ChatRoomPageLocator.mic_btn)
        assert self.common.poco_get_text(ChatRoomPageLocator.popup_title) == "点击以进行录音", f'錄音初始介面有誤'

        self.common.poco_click(ChatRoomPageLocator.record_voice_btn)
        sleep(length)
        if self.phone_platform.lower() == 'android':
            self.common.poco_click(ChatRoomPageLocator.record_voice_btn)
        else:
            self.common.poco_click(ChatRoomPageLocator.stop_record_voice_btn)
        if length < 9:
            expect_result = f"00:0{length+1}"
        else:
            expect_result = f"00:{length + 1}"
        actual_result = self.common.poco_get_text(ChatRoomPageLocator.record_count)

        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_text(ChatRoomPageLocator.record_count) == expect_result, f'語音長度有誤, 預期:{expect_result}, 實際:{actual_result}'
            self.common.poco_click(ChatRoomPageLocator.send_voice_btn)
            self.common.poco_click(ChatRoomPageLocator.close_btn)
            assert self.common.poco_get_text(
                ChatRoomPageLocator.last_voice_message) == expect_result, f'聊天室內語音長度有誤'
        else:
            self.common.poco_click(ChatRoomPageLocator.send_voice_btn)
            self.common.poco_click(ChatRoomPageLocator.close_btn)

    def send_file_message(self, file_index):
        if self.common.poco_exists(ChatRoomPageLocator.file_btn):
            self.common.poco_click(ChatRoomPageLocator.file_btn)
        else:
            self.common.poco_click(ChatRoomPageLocator.add_function_btn)
            self.common.poco_click(ChatRoomPageLocator.file_btn)

        if self.phone_platform.lower() == 'android':
            file_name_1 = self.common.poco_get_text(ChatRoomPageLocator.folder_file_index(file_index))
            self.common.poco_click(ChatRoomPageLocator.folder_file_index(file_index))
        else:
            file = self.common.poco_get_text(ChatRoomPageLocator.folder_file_index(file_index+1))
            parts = [p.strip() for p in file.split(",")]
            file_name_1 = f"{parts[0]}.{parts[1]}"
            self.common.poco_click(ChatRoomPageLocator.folder_file_index(file_index+1))
        file_name = re.sub(r'(\.\w+)\1$', r'\1', file_name_1)
        confirm_msg_content = self.common.poco_get_text(ChatRoomPageLocator.confirm_msg_content)
        assert confirm_msg_content == f'您要传送『{file_name}』吗？', f'預期:{confirm_msg_content}, 實際:您要传送『{file_name}』吗？'

        self.common.poco_click(ChatRoomPageLocator.confirm_msg_send_btn)
        sleep(5)
        actual_chatroom_filename = self.common.poco_get_text(ChatRoomPageLocator.last_chatroom_filename)
        assert actual_chatroom_filename == file_name, f'檔案名稱錯誤, 預期:{file_name},實際:{actual_chatroom_filename}'

    def group_delete_history(self):
        self.common.poco_wait_exists(ChatRoomPageLocator.options_btn)
        self.common.poco_click(ChatRoomPageLocator.options_btn)
        self.common.poco_wait_exists(ChatRoomPageLocator.option_delete_history)
        self.common.poco_click(ChatRoomPageLocator.option_delete_history)  # 刪除對話紀錄
        # self.common.poco_wait_exists(ChatRoomPageLocator.menu_delete)
        self.common.poco_click(ChatRoomPageLocator.menu_delete)  # 刪除確認
