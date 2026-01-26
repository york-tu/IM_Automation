from datetime import datetime
from time import sleep
import re

from airtest.core.api import touch

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.chatroom_page import ChatRoomPage, ChatRoomPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class ChatListPageLocator(BaseLocator):
    """聊天列表頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    # 系統通知icon
    system_notification = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_system_notification'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_notification_button'),
    )
    # 系統通知最新一筆系統訊息內容
    latest_system_message_text = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=0),
        iOS=base.data_collation(type_kind='name', type_name='systemNotification_content_label', num=0),
    )
    # 系統通知最新一筆系統訊息時間
    latest_system_message_time = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_create_at', num=0),
        iOS=base.data_collation(type_kind='name', type_name='systemNotification_time_label', num=0),
    )
    message_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/navigation_bar_item_icon_view',
                                    num=1),
        iOS=base.data_collation(type_kind='name', type_name='mainTabBar_chat_button'),
    )

    search_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_search_textField'),
    )

    search_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_clear_iv'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本'),
    )

    search_empty = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='找不到任何结果'),
        iOS=base.data_collation(type_kind='name', type_name='找不到任何结果'),
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button'),
    )

    add_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_add'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_addAction_button'),
    )

    add_chat_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增聊天'),
        iOS=base.data_collation(type_kind='name', type_name='新增聊天'),
    )

    add_group_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增群组'),
        iOS=base.data_collation(type_kind='name', type_name='新增群组'),
    )

    add_friend_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增好友'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_addFriend_button'),
    )
    add_friend_page_note = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name=f'我的 IM ID：.*'),
        iOS=base.data_collation(type_kind='nameMatches', type_name=f'我的 IM ID：.*'),
    )

    input_share_code_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='输入邀请码'),
        iOS=base.data_collation(type_kind='name', type_name='输入邀请码'),
    )
    input_share_code_column = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_input_text'),
        iOS=base.data_collation(type_kind='name', type_name='输入邀请码'),
    )
    share_code_send_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_send'),
        iOS=base.data_collation(type_kind='name', type_name='送出'),
    )

    group_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=1),
        iOS=base.data_collation(type_kind='name', type_name='chatList_nameCell_roomName_label'),
    )

    friend_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=1),
        iOS=base.data_collation(type_kind='name', type_name='chatList_nameCell_roomName_label'),
    )

    list_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name'),
        iOS=base.data_collation(
            type_kind='name', type_name='chatList_chatCell_lastMessage_label',
            parent={'type_kind': 'name', 'type_name': 'Cell', 'num': 0}
        ),
    )

    chat_room_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=1),
    )

    group_member_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_checked'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    selected_empty_text = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_selected_empty_text'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    selected_list = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rv_selected_users'),
        iOS=base.data_collation(type_kind='name', type_name=''),
    )

    last_message_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_textMessageRCell_textView', num=-1),
    )
    last_other_message_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='message_textMessageLCell_textView', num=-1),
    )
    last_reply_message_room = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='message_replyMessageRCell_textView', num=-1),
    )
    last_voice_message_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_duration', num=-1),
        iOS=base.data_collation(type_kind='nameMatches', type_name='', num=-1),
    )

    last_message_list = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_last_message', num=0),
        iOS=base.data_collation(
            type_kind='name', type_name='chatList_chatCell_lastMessage_label',
            parent={'type_kind': 'name', 'type_name': 'Cell', 'num': 0}
        ),
    )


def convert_to_24hr(time_str: str) -> str:
    """
    將 '2025-10-30 上午10:52' 或 '2025/10/30 下午3:15'
    轉換為 '2025-10-30 10:52' 或 '2025-10-30 15:15' (24小時制)
    """
    if not time_str:
        return ""

    # 去除多餘空白
    time_str = time_str.strip()
    # 中文上午/下午 → 英文 AM/PM
    time_str = time_str.replace("上午", "AM").replace("下午", "PM")
    # 統一日期分隔符為 "-"
    time_str = re.sub(r"[./]", "-", time_str)
    # 嘗試多種格式解析
    possible_formats = [
        "%Y-%m-%d %p%I:%M",
        "%Y-%m-%d%p%I:%M",   # 沒有空格的情況
        "%Y-%m-%d %I:%M",    # 無上午/下午
        "%Y-%m-%d%I:%M",
    ]
    for fmt in possible_formats:
        try:
            dt = datetime.strptime(time_str, fmt)
            return dt.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            continue
    # 若無法解析就原樣返回
    return time_str


class ChatListPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_chat_room(self, name):
        self.common.poco_click(ChatListPageLocator.message_btn)
        self.common.poco_click(ChatListPageLocator.search_input)
        if self.common.poco_exists(ChatListPageLocator.search_clear):
            self.common.poco_click(ChatListPageLocator.search_clear)
        self.common.poco_send_text(ChatListPageLocator.search_input, name)
        
        # iOS 優化：使用動態等待替代固定 3 秒等待
        if self.phone_platform.lower() == 'ios':
            # 快速檢查搜索結果出現（最多等待 2 秒）
            # 修改：同時檢查 friend_frist 和 group_frist，支持個人和群組聊天室
            for i in range(4):  # 4 * 0.5 = 2 秒
                if self.common.poco_exists(ChatListPageLocator.friend_frist) or \
                   self.common.poco_exists(ChatListPageLocator.group_frist) or \
                   self.common.poco_exists(ChatListPageLocator.search_empty):
                    break
                sleep(0.5)
        else:
            sleep(3)
        
        if self.common.poco_exists(ChatListPageLocator.search_empty):
            raise EOFError('找不到任何結果')
        else:
            if self.phone_platform.lower() == 'ios':
                # 修改：同時處理個人和群組聊天室
                if self.common.poco_exists(ChatListPageLocator.friend_frist):
                    assert self.common.poco_get_attr(ChatListPageLocator.friend_frist, 'value').__contains__(
                    name), f'好友搜查結果有誤'
                    self.common.poco_click(ChatListPageLocator.friend_frist)
                elif self.common.poco_exists(ChatListPageLocator.group_frist):
                    assert self.common.poco_get_attr(ChatListPageLocator.group_frist, 'value').__contains__(
                        name), f'群組搜查結果有誤'
                    self.common.poco_click(ChatListPageLocator.group_frist)
                else:
                    raise EOFError(f'找不到聊天室: {name}')
                # iOS 優化：減少等待時間（從 1 秒降到 0.5 秒）
                sleep(0.5)
            else:
                if self.common.poco_exists(ChatListPageLocator.friend_frist):
                    aaa = self.common.poco_get_text(ChatListPageLocator.friend_frist)
                    assert self.common.poco_get_text(ChatListPageLocator.friend_frist).__contains__(
                        name), f'好友搜查結果有誤'
                    self.common.poco_click(ChatListPageLocator.friend_frist)
                    sleep(1)
                elif self.common.poco_exists(ChatListPageLocator.group_frist):
                    assert self.common.poco_get_text(ChatListPageLocator.group_frist).__contains__(
                        name), f'群組搜查結果有誤'
                    self.common.poco_click(ChatListPageLocator.group_frist)
                    sleep(1)

    def into_add_friend_page(self, self_id=None):
        self.common.poco_click(ChatListPageLocator.add_button)
        assert self.common.poco_exists(ChatListPageLocator.add_friend_button), '預期顯示, 實際新增好友鍵未顯示'
        self.common.poco_click(ChatListPageLocator.add_friend_button)
        assert self.common.poco_exists(ChatListPageLocator.add_friend_page_note)
        self_id_note = self.common.poco_get_text(ChatListPageLocator.add_friend_page_note)
        if self_id is not None:
            assert self_id_note.split("：")[1] == self_id

    def into_system_notification(self):
        self.common.poco_click(ChatListPageLocator.message_btn)
        self.common.poco_click(ChatListPageLocator.system_notification)
        if self.phone_platform.lower() == 'android':
            assert self.common.poco_get_text(ChatListPageLocator.chat_room_title) == '系统通知', '頁面錯誤'

    def add_chat_room(self, name):
        self.wait_loading_finish()
        self.common.poco_click(ChatListPageLocator.add_button)

        self.common.poco_click(ChatListPageLocator.add_chat_button)
        if self.common.poco_exists(ChatListPageLocator.search_input):
            self.common.poco_click(ChatListPageLocator.search_input)
            self.common.poco_send_text(ChatListPageLocator.search_input, name)

        self.wait_loading_finish()
        self.common.poco_click(ChatListPageLocator.list_frist)
        assert self.common.poco_get_text(ChatListPageLocator.chat_room_title).__conatins__(name), f'進入聊天室失誤'

    def add_group_room(self, name):
        self.wait_loading_finish()
        self.common.poco_click(ChatListPageLocator.add_button)
        self.common.poco_click(ChatListPageLocator.add_group_button)
        if self.common.poco_exists(ChatListPageLocator.search_input):
            self.common.poco_click(ChatListPageLocator.search_input)
            self.common.poco_send_text(ChatListPageLocator.search_input, name)

        assert self.common.poco_get_text(
            ChatListPageLocator.selected_empty_text) == "您最多可以邀请2,000位好友加入群组。请在此选择您要邀请的好友。在他们加入群组后，即可开始聊天。"

        self.wait_loading_finish()
        self.common.poco_click(ChatListPageLocator.group_member_button)
        assert self.common.poco_exists(ChatListPageLocator.selected_list) == True

    def leave_group(self, group_name):
        if self.common.poco_exists(ChatListPageLocator.search_clear):
            self.common.poco_click(ChatListPageLocator.search_clear)
        self.wait_loading_finish()
        self.common.poco_send_text(ChatListPageLocator.search_input, group_name)  # 搜尋群組
        sleep(1)
        self.common.poco_click(ChatListPageLocator.group_frist)  # 進入該群組
        self.common.poco_click(ChatRoomPageLocator.options_btn)  # 點群組右上角設定鍵
        self.common.poco_click(ChatRoomPageLocator.options_delete_and_leave)  # 點"刪除並退出"鍵
        self.common.poco_click(ChatRoomPageLocator.options_leave_group_confirm_btn)  # 點二次確認鍵
        self.wait_loading_finish()
        self.common.poco_send_text(ChatListPageLocator.search_input, group_name)
        sleep(3)
        assert self.common.poco_exists(ChatListPageLocator.search_empty), f'未確實離開群組'  # 搜尋該群組, 確認已搜尋不到

    def join_group_by_input_share_code(self, share_code, group_name):
        if self.common.poco_wait_exists(ChatListPageLocator.message_btn):
            self.common.poco_click(ChatListPageLocator.message_btn)
        self.wait_loading_finish()

        self.common.poco_wait_exists(ChatListPageLocator.add_button)
        self.common.poco_click(ChatListPageLocator.add_button)

        self.common.poco_wait_exists(ChatListPageLocator.input_share_code_button)
        self.common.poco_click(ChatListPageLocator.input_share_code_button)  # 點右上角"+" > "輸入邀請碼"鍵

        self.common.poco_send_text(ChatListPageLocator.input_share_code_column, share_code)  # "輸入邀請碼"

        self.common.poco_click(ChatListPageLocator.share_code_send_btn)
        self.wait_loading_finish()
        self.common.poco_send_text(ChatListPageLocator.search_input, group_name)
        sleep(3)
        assert self.common.poco_get_text(ChatListPageLocator.group_frist).__contains__(
            group_name), f'綁定群組名與預期不符'  # 搜尋群組名, 確認已透過邀請碼加入該群組

    def check_last_message(self, message_type='text', is_reply=False, other_msg=False):
        # if self.common.poco_exists(ChatListPageLocator.search_clear):
        #     self.common.poco_click(ChatListPageLocator.search_clear)
        if self.phone_platform.lower() == 'ios':
            # ==================== 獲取聊天室內最後一則訊息 ====================
            if message_type == 'voice':
                room_message = '语音讯息'
            elif message_type == 'file':
                room_message = '档案讯息'
            else:
                if is_reply:
                    room_message = self.common.poco_get_text(ChatListPageLocator.last_reply_message_room)
                elif other_msg:
                    room_message = self.common.poco_get_text(ChatListPageLocator.last_other_message_room)
                else:
                    room_message = self.common.poco_get_text(ChatListPageLocator.last_message_room)

            # ==================== 回到聊天列表 > 獲取聊天室最後一則訊息 ====================
            self.common.poco_click(ChatListPageLocator.back_btn)  # 回到聊天列表
            
            # iOS 優化：快速檢查是否已回到聊天列表（最多等待 1 秒）
            for i in range(2):  # 2 * 0.5 = 1 秒
                if self.common.poco_exists(ChatListPageLocator.search_input):
                    break
                sleep(0.5)

            self.common.poco_click(ChatListPageLocator.search_input)
            if self.common.poco_exists(ChatListPageLocator.search_clear):
                self.common.poco_click(ChatListPageLocator.search_clear)

            # iOS 優化：快速檢查列表訊息出現（最多等待 1 秒）
            for i in range(2):  # 2 * 0.5 = 1 秒
                try:
                    list_message = self.common.poco_get_text(ChatListPageLocator.last_message_list)
                    if list_message and room_message in list_message:
                        break  # 已經找到匹配的訊息
                except:
                    pass
                sleep(0.5)
            
            list_message = self.common.poco_get_text(ChatListPageLocator.last_message_list)
            assert list_message.__contains__(
                room_message), f'最後一筆訊息顯示錯誤, 目前:{list_message},預期:{room_message}'

            self.common.poco_click(ChatListPageLocator.list_frist)  # 重新進入聊天室
            
            # iOS 優化：快速檢查是否已進入聊天室（最多等待 1 秒）
            for i in range(2):  # 2 * 0.5 = 1 秒
                if self.common.poco_exists(ChatRoomPageLocator.message_input):
                    break
                sleep(0.5)

        else:
            self.wait_loading_finish()
            if message_type == 'voice':
                room_message = '语音讯息'
            elif message_type == 'file':
                room_message = '档案讯息'
            else:
                room_message = self.common.poco_get_text(ChatListPageLocator.last_message_room)

            self.common.poco_click(ChatListPageLocator.back_btn)

            if self.common.poco_exists(ChatListPageLocator.search_clear):
                self.common.poco_click(ChatListPageLocator.search_clear)

            self.wait_loading_finish()
            list_message = self.common.poco_get_text(ChatListPageLocator.last_message_list)

            assert list_message.__contains__(room_message), f'最後一筆訊息顯示錯誤'

            self.common.poco_click(ChatListPageLocator.list_frist)

    def back_to_checklist(self):
        self.common.poco_click(ChatListPageLocator.back_btn)

    def check_latest_system_message(self, message, time):
        sleep(1)
        if self.phone_platform.lower() == 'android':
            system_message = self.common.poco_get_text(ChatListPageLocator.latest_system_message_text)
            system_time = self.common.poco_get_text(ChatListPageLocator.latest_system_message_time)
        else:
            system_message = self.poco(type='Cell')[0].offspring(name='systemNotification_content_label')[0].attr('value')
            system_time = self.poco(type='Cell')[0].offspring(name='systemNotification_time_label')[0].attr('value')
        system_time = convert_to_24hr(system_time)  # 時間轉24hr制
        assert system_message == message, f'最新一筆系統訊息錯誤, 目前:{system_message},預期:{message}'
        assert system_time == time, f'最新一筆系統訊息時間錯誤, 目前:{system_time},預期:{time}'
