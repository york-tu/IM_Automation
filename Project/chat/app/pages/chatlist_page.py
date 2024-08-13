from time import sleep

from airtest.core.api import touch

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.chatroom_page import ChatRoomPage, ChatRoomPageLocator
import logging
import common.utils.globalvar as gl


class ChatListPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = ChatListPageLocator.base.check_device(
            Android=ChatListPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=ChatListPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    message = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='信息'),
        iOS=base.data_collation(type_kind='name', type_name='信息',),
    )

    search_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='type', type_name='TextField', num=0),
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
        iOS=base.data_collation(type_kind='type', type_name='Button', num=0),
    )

    add_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_add'),
        iOS=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_add'),
    )

    add_chat_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增聊天'),
        iOS=base.data_collation(type_kind='name', type_name='新增聊天'),
    )

    add_group_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增群组'),
        iOS=base.data_collation(type_kind='name', type_name='新增群组'),
    )

    add_frend_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增好友'),
        iOS=base.data_collation(type_kind='name', type_name='新增好友'),
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
        Android=base.data_collation(type_kind='text', type_name='群组', action='parent().sibling()[0].child()[1]'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=2),
    )

    friend_frist = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友', action='parent().sibling()[0].child()[1]'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=2),
    )

    list_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name'),
        iOS=base.data_collation(type_kind='name', type_name='Cell', num=0),
    )

    chat_room_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=1),
    )

    group_member_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_checked'),
        iOS=base.data_collation(type_kind='name', type_name='新增好友'),
    )

    selected_empty_text = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_selected_empty_text'),
        iOS=base.data_collation(type_kind='name', type_name='新增好友'),
    )

    selected_list = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/rv_selected_users'),
        iOS=base.data_collation(type_kind='name', type_name='新增好友'),
    )

    last_message_room = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_content', num=-1),
        iOS=base.data_collation(type_kind='nameMatches', type_name='.*测试.*', num=-1),
    )

    last_message_list = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_last_message', num=0),
        iOS=base.data_collation(type_kind='', type_name=''),
    )


class ChatListPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_chat_room(self, name):
        # if not self.common.poco_exists(ChatListPageLocator.search_input):
        self.common.poco_click(ChatListPageLocator.message)
        if self.common.poco_exists(ChatListPageLocator.search_input):
            self.common.poco_click(ChatListPageLocator.search_input)
            self.common.poco_send_text(ChatListPageLocator.search_input, name)

        # self.wait_loading_finish()
        if self.common.poco_exists(ChatListPageLocator.search_empty):
            raise EOFError('找不到任何結果')
        else:
            if self.common.poco_exists(ChatListPageLocator.friend_frist):
                assert self.common.poco_get_text(ChatListPageLocator.friend_frist).__contains__(name), f'好友搜查結果有誤'
                self.common.poco_click(ChatListPageLocator.friend_frist)
            elif self.common.poco_exists(ChatListPageLocator.group_frist):
                assert self.common.poco_get_text(ChatListPageLocator.group_frist).__contains__(name), f'群組搜查結果有誤'
                self.common.poco_click(ChatListPageLocator.group_frist)

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
        self.common.poco_click(ChatListPageLocator.group_frist)  # 進入該群組
        self.common.poco_click(ChatRoomPageLocator.options_btn)  # 點群組右上角設定鍵
        self.common.poco_click(ChatRoomPageLocator.options_delete_and_leave)  # 點"刪除並退出"鍵
        self.common.poco_click(ChatRoomPageLocator.options_leave_group_confirm_btn)  # 點二次確認鍵
        self.wait_loading_finish()
        self.common.poco_send_text(ChatListPageLocator.search_input, group_name)
        assert self.common.poco_exists(ChatListPageLocator.search_empty), f'未確實離開群組'  # 搜尋該群組, 確認已搜尋不到

    def join_group_by_input_share_code(self, share_code, group_name):
        if self.common.poco_wait_exists(ChatListPageLocator.message):
            self.common.poco_click(ChatListPageLocator.message)
        self.wait_loading_finish()
        self.common.poco_click(ChatListPageLocator.add_button)
        self.common.poco_click(ChatListPageLocator.input_share_code_button)  # 點右上角"+" > "輸入邀請碼"鍵
        self.common.poco_send_text(ChatListPageLocator.input_share_code_column, share_code)  # "輸入邀請碼"
        self.common.poco_click(ChatListPageLocator.share_code_send_btn)
        self.wait_loading_finish()
        self.common.poco_send_text(ChatListPageLocator.search_input, group_name)
        assert self.common.poco_get_text(ChatListPageLocator.group_frist).__contains__(
            group_name), f'綁定群組名與預期不符'  # 搜尋群組名, 確認已透過邀請碼加入該群組

    def check_last_message(self, is_url=None):

        if self.phone_platform.lower() == 'ios':
            self.poco(name='iconIconSearch').click()
            touch((200, 500))
            if is_url:
                room_message = self.poco(type='TextView')[-2].attr('name')
            else:
                room_message = self.common.poco_get_text(ChatListPageLocator.last_message_room)
                # room_message = self.poco(type='TextView')[-3].attr('name')

            self.poco(name='Chat').click()

            if self.common.poco_exists(ChatListPageLocator.search_input):
                self.common.poco_click(ChatListPageLocator.search_input)
            if self.common.poco_exists(ChatListPageLocator.search_clear):
                self.common.poco_click(ChatListPageLocator.search_clear)

            self.wait_loading_finish()

            list_message= self.poco(type='Cell')[0].child(type='StaticText')[-1].attr('name')
            # list_message = self.poco(type='Cell')[0].child(type='StaticText')[2].attr('name')
            assert list_message.__contains__(room_message), f'最後一筆訊息顯示錯誤, 目前:{list_message},預期:{room_message}'

            self.common.poco_click(ChatListPageLocator.list_frist)

        else:
            self.wait_loading_finish()
            room_message = self.common.poco_get_text(ChatListPageLocator.last_message_room)
            self.common.poco_click(ChatListPageLocator.back_btn)

            if self.common.poco_exists(ChatListPageLocator.search_clear):
                self.common.poco_click(ChatListPageLocator.search_clear)

            self.wait_loading_finish()
            list_message = self.common.poco_get_text(ChatListPageLocator.last_message_list)

            assert list_message.__contains__(room_message), f'最後一筆訊息顯示錯誤'

            self.common.poco_click(ChatListPageLocator.list_frist)
