from time import sleep, time

from airtest.core.api import assert_exists, assert_not_exists
from poco.exceptions import PocoNoSuchNodeException

from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.testcase.base_testcase import BaseTestCase
from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
from Project.chat.app.pages.chatlist_page import ChatListPage, ChatListPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
from Project.chat.app.pages.base_page import BaseLocator as BasePageLocator
import logging
import common.utils.globalvar as gl


class FriendPageLocator(BaseLocator):
    """好友頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    friend_list_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_friend'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_friendList_button'),
    )
    search_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='friendList_search_textField'),
    )

    search_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_clear_iv'),
        iOS=base.data_collation(type_kind='name', type_name='清除文本'),
    )

    search_none_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='找不到任何结果'),
        iOS=base.data_collation(type_kind='name', type_name='找不到任何结果'),
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='type', type_name='Button'),
    )
    chatroom_back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_back'),
        iOS=base.data_collation(type_kind='type', type_name='Button'),
    )

    add_friend_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增好友'),
        iOS=base.data_collation(type_kind='name', type_name='chatList_addFriend_button'),
    )

    add_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    add_friend_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='addFriend_search_textField'),
    )

    add_friend_search = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_search_id'),
        iOS=base.data_collation(type_kind='name', type_name='addFriend_searchResult_label'),
    )

    add_to_address_book_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增至通讯录'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_contact_cell'),
    )

    add_friend_submit = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='新增'),
        iOS=base.data_collation(type_kind='name', type_name='新增'),
    )

    add_myself_popup = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='您不能将自己加入到通讯录'),
        iOS=base.data_collation(type_kind='name', type_name='您不能将自己加入到通讯录'),
    )

    add_myself_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确定'),
        iOS=base.data_collation(type_kind='type', type_name='ScrollView', num=-1),
    )
    chatroom_options_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_options'),
        iOS=base.data_collation(type_kind='name', type_name='message_more_button')
    )
    friend_remark_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_note'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_memo_cell'),
    )

    userDetail_friend_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_name_label'),
    )

    friend_note_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='描述'),
        iOS=base.data_collation(type_kind='name', type_name='描述'),
    )

    nickname_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_nickname'),
        iOS=base.data_collation(type_kind='type', type_name='TextField'),
    )

    note_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/et_note'),
        iOS=base.data_collation(type_kind='type', type_name='TextView', num=-1),
    )
    user_detail_note = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_note_content'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    remark_submit = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成'),
        iOS=base.data_collation(type_kind='name', type_name='完成'),
    )

    remark_back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_start_icon'),
        iOS=base.data_collation(type_kind='type', type_name='Button'),
    )

    friend_chat_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='传讯息'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_greeting_cell'),
    )

    friend_first_chat = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='打招呼'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_greeting_cell'),
    )

    team_list_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    team_list_frist = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组', action='parent().sibling()[0].child()[1]'),
        iOS=base.data_collation(type_kind='name', type_name='friendList_nameCell_roomName_label', num=0),
    )

    friend_list_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    friendList_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='friendList_nameCell_roomName_label', num=0),
    )
    chatList_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=0),
        iOS=base.data_collation(type_kind='name', type_name='chatList_chatCell_roomName_label', num=0),
    )
    friend_setting_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_setting'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconSettings'),
    )

    friend_delete_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='删除'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_unfriend_cell'),
    )

    friend_popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='将联络人.*'),
    )

    friend_popup_submit = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', num=1),
    )

    friend_impeach_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='检举'),
        iOS=base.data_collation(type_kind='name', type_name='检举'),
    )

    impeach_radio = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='骚扰行为'),
        iOS=base.data_collation(type_kind='name', type_name='传送色情讯息'),
    )

    impeach_agree = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='同意并传送'),
        iOS=base.data_collation(type_kind='name', type_name='同意并传送'),
    )

    friend_block_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_blacklist'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_blockUser_switch'),
    )

    page_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友名单'),
        iOS=base.data_collation(type_kind='name', type_name='好友名单', num=0),
    )

    # ============================== 社群化 ===================================
    personal_social_homepage_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='个人页面'),
        iOS=base.data_collation(type_kind='name', type_name='userDetail_profile_cell'),
    )


class FriendPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    phone_name = gl.get_value('PHONE_NAME')

    def check_add_to_address_book_non_display(self):
        assert not self.common.poco_exists(FriendPageLocator.add_to_address_book_btn), f"預期不該顯示卻顯示'新增至通訊錄'選項"

    def check_add_to_address_book_display(self):
        assert self.common.poco_exists(FriendPageLocator.add_to_address_book_btn), "預期該顯示但未顯示'新增至通訊錄'選項"

    def return_previous_page(self, count=1):
        for i in range(0, count):
            self.common.poco_click(FriendPageLocator.back_btn)

    def is_new_friend(self, name):  # 好友名單列表 > 搜尋
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)
        self.common.poco_click(FriendPageLocator.add_friend_input)  # 新增好友頁 > 搜尋框
        self.common.poco_send_text(FriendPageLocator.add_friend_input, name)
        self.common.poco_click(FriendPageLocator.add_friend_search)
        sleep(1.5)
        if self.common.poco_exists(FriendPageLocator.add_to_address_book_btn):
            return True
        else:
            return False

    def search_friend_from_list(self, name):  # 搜尋好友, 進到好友詳情頁
        self.common.poco_click(FriendPageLocator.search_input)
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)
        if self.common.poco_wait_appearance(FriendPageLocator.search_input):
            if self.phone_platform.lower() == 'ios':
                self.common.poco_click(FriendPageLocator.search_input)
                sleep(0.2)  # iOS 優化：減少鍵盤彈出等待時間
            self.common.poco_send_text(FriendPageLocator.search_input, name)
        
        # iOS 優化：減少固定等待時間
        if self.phone_platform.lower() == 'ios':
            sleep(0.5)  # 減少等待時間（從 1 秒降到 0.5 秒）
        else:
            self.common.sleep(1)
        
        if not self.common.poco_exists(FriendPageLocator.search_none_check):
            if self.common.poco_exists(FriendPageLocator.friendList_frist):
                assert self.common.poco_get_text(FriendPageLocator.friendList_frist) == name, f'找不到任何結果'
                self.common.poco_click(FriendPageLocator.friendList_frist)
            elif self.common.poco_exists(FriendPageLocator.team_list_frist):
                assert self.common.poco_get_text(FriendPageLocator.team_list_frist).__contains__(name), f'找不到任何結果'
                self.common.poco_click(FriendPageLocator.team_list_frist)

    def add_myself(self, phone_mail_id, nation='CN', account_type='phone'):

        if account_type == 'phone':
            self.common.poco_wait_exists(FriendPageLocator.add_friend_input)
            if self.phone_platform.lower() == 'android':
                self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                self.common.poco_click(FriendPageLocator.add_friend_search)
            else:
                self.common.poco_click(FriendPageLocator.add_friend_input)
                self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                self.common.poco_click(FriendPageLocator.add_friend_search)

        elif account_type == 'email':
            # if self.common.poco_exists(FriendPageLocator.add_button):
            #     self.common.poco_click(FriendPageLocator.add_button)
            if self.common.poco_exists(FriendPageLocator.add_friend_input):
                self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                self.common.poco_click(FriendPageLocator.add_friend_search)

        assert not self.common.poco_exists(FriendPageLocator.add_to_address_book_btn)
        assert not self.common.poco_exists(FriendPageLocator.friend_chat_btn)

    def search_clear(self, id):
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(FriendPageLocator.add_friend_input)
            self.common.poco_send_text(FriendPageLocator.add_friend_input, 'clear')
            self.common.poco_click(FriendPageLocator.search_clear)
            default_text = self.poco(type='StaticText')[1].attr('value')
            assert '我的 IM ID：' in default_text, f'新增好友頁未清空'
        else:
            self.common.poco_send_text(FriendPageLocator.add_friend_input, id)
            sleep(1)
            assert self.common.poco_exists(FriendPageLocator.add_friend_search), f'未顯示搜查按鍵'
            self.common.poco_click(FriendPageLocator.search_clear)

    def set_note(self, note):
        self.common.poco_click(FriendPageLocator.friend_remark_btn)

        if self.phone_platform.lower() == 'ios':  # ios part
            # ====================== 改備註 ======================
            self.common.poco_click(FriendPageLocator.note_input)
            self.common.poco_send_text(FriendPageLocator.note_input, note)
            self.common.poco_click(FriendPageLocator.remark_submit)
            modified_note = self.poco(name='userDetail_memo_cell').offspring(type='StaticText')[1].attr('label')
            assert modified_note == note, f'設定描述失敗'  # 用戶詳情頁確認顯示備註
            # ====================== 回復初始狀態 ======================
            self.common.poco_click(FriendPageLocator.friend_note_button)
            # iOS 優化：限制等待「全选」按鈕出現的次數，避免無限循環
            max_attempts = 5
            attempt = 0
            while not self.poco(name='全选').exists() and attempt < max_attempts:
                self.common.poco_long_click(FriendPageLocator.note_input)
                attempt += 1
                sleep(0.3)  # 減少等待時間（從 1 秒降到 0.3 秒）

            self.poco(name='全选').click()
            self.poco(name='剪切').click()
            sleep(0.5)
            actual_note = self.poco(name='TextView').offspring(type='StaticText').attr('label')
            assert actual_note == '描述最长至300字', f'描述清空失敗'

            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            try:  # 確認用戶詳情頁無備註
                assert not self.poco(name='userDetail_memo_cell').offspring(type='StaticText')[1].exists()
            except (PocoNoSuchNodeException, AttributeError, IndexError):
                # 元素不存在時，斷言通過（因為我們期望它不存在）
                pass

        else:  # android part
            # ====================== 改備註 ======================
            self.common.poco_send_text(FriendPageLocator.note_input, note)
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.common.poco_get_text(FriendPageLocator.user_detail_note) == note, f'設定描述失敗'
            # ====================== 回復初始狀態 ======================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.note_input, '')
            sleep(0.5)
            default_note = self.common.poco_get_text(FriendPageLocator.note_input)
            assert default_note == '描述最长至300字...', f'描述清空失敗'
            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            try:  # 確認用戶詳情頁無備註
                assert not self.common.poco_exists(FriendPageLocator.user_detail_note)
            except (PocoNoSuchNodeException, AttributeError, IndexError):
                # 元素不存在時，斷言通過（因為我們期望它不存在）
                pass

    def set_nickname(self, name):
        default_nickname = self.common.poco_get_text(FriendPageLocator.userDetail_friend_nickname)

        if self.phone_platform.lower() == 'ios':  # ios part
            # ============================= 改暱稱 =============================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
            self.common.poco_send_text(FriendPageLocator.nickname_input, name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            assert self.common.poco_get_text(FriendPageLocator.userDetail_friend_nickname) == name, f'暱稱更換失敗'  # 用戶詳情頁檢查
            # --------------------- 回到聊天列表 > 確認私聊室名稱有更新 ---------------------
            self.common.poco_click(FriendPageLocator.back_btn)  # 回到好友名單頁
            self.search_friend_from_list(name)  # 好友名單頁 > 確認搜尋到改暱稱後的好友 > 進到詳情頁
            for i in range(2):
                self.common.poco_click(FriendPageLocator.back_btn)  # 回到聊天列表
            ChatListPage(self.poco, self.wda).into_chat_room(name)  # 聊天列表 > 確認搜尋到改暱稱後的好友 > 進到該聊天室
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, "ios更改暱稱, 確認聊天室名")
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)  # 發送訊息, 確保聊天室在列表最上
            self.common.poco_click(FriendPageLocator.chatroom_back_btn)  # 回到聊天列表
            self.common.poco_click(ChatListPageLocator.search_input)
            self.common.poco_click(ChatListPageLocator.search_clear)
            actual_chatroom_name = self.poco(name='Cell')[0].child(name='chatList_chatCell_roomName_label').attr('value')
            assert actual_chatroom_name == name, f'聊天室名有錯, 預期:{name},實際:{actual_chatroom_name}'  # 確認聊天列表上聊天室名有正確更新
            self.common.poco_click(FriendPageLocator.chatList_frist)
            self.common.poco_click(FriendPageLocator.chatroom_options_btn)  # 聊天視窗右上角more > 用戶詳情頁
            # ============================= 將暱稱刪除, 使用預設暱稱 ==========================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
            self.common.poco_send_text(FriendPageLocator.nickname_input, default_nickname)
            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            assert self.common.poco_get_text(FriendPageLocator.userDetail_friend_nickname) == default_nickname, f'暱稱預設失敗'

        else:  # android part
            # ============================= 改暱稱 =============================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            assert self.common.poco_get_text(FriendPageLocator.userDetail_friend_nickname) == name, f'暱稱更換失敗'
            # --------------------- 回到聊天列表 > 確認私聊室名稱有更新 ---------------------
            # self.common.poco_click(FriendPageLocator.back_btn)  # 回到好友名單頁
            # self.search_friend_from_list(name)  # 好友名單頁 > 確認搜尋到改暱稱後的好友 > 進到詳情頁
            # for i in range(2):
            #     self.common.poco_click(FriendPageLocator.back_btn)  # 回到聊天列表
            # ChatListPage(self.poco, self.wda).into_chat_room(name)  # 聊天列表 > 確認搜尋到改暱稱後的好友 > 進到該聊天室
            # self.common.poco_send_text(ChatRoomPageLocator.message_input, "更改暱稱, 確認聊天室名")
            # self.common.poco_click(ChatRoomPageLocator.send_message_btn)  # 發送訊息, 確保聊天室在列表最上
            # self.common.poco_click(FriendPageLocator.chatroom_back_btn)  # 回到聊天列表
            # self.common.poco_click(ChatListPageLocator.search_clear)
            # actual_chatroom_name = self.common.poco_get_text(FriendPageLocator.chatList_frist)
            # assert actual_chatroom_name == name, f'聊天室名有錯, 預期:{name},實際:{actual_chatroom_name}'
            # self.common.poco_click(FriendPageLocator.chatList_frist)
            # self.common.poco_click(FriendPageLocator.chatroom_options_btn)  # 聊天視窗右上角more > 用戶詳情頁
            # ============================= 將暱稱刪除, 使用預設暱稱 ==========================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, default_nickname)
            self.common.poco_click(FriendPageLocator.remark_submit)
            sleep(0.5)
            actual_nickname = self.common.poco_get_text(FriendPageLocator.userDetail_friend_nickname)
            assert actual_nickname == default_nickname, f'暱稱預設失敗, 預期:{default_nickname},實際:{actual_nickname}'

    def add_friend(self, nickname):  # 添加好友並回到聊天列表
        self.common.poco_click(FriendPageLocator.add_to_address_book_btn)
        sleep(2)
        expect = self.common.poco_get_text(ChatRoomPageLocator.options_title)
        assert expect == nickname, f'預期:{nickname}, 實際:{expect}'
        if self.common.poco_exists(ChatRoomPageLocator.back_btn):
            self.common.poco_click(ChatRoomPageLocator.back_btn)

    def delete_friend_from_UserDetail(self, name):  # 好友名單 > 用戶詳情 > 刪除
        self.common.poco_click(FriendPageLocator.friend_delete_button)
        sleep(1)
        if self.phone_platform.lower() == 'ios':
            popup_message = self.common.poco_get_attr(FriendPageLocator.friend_popup_message, 'value')
            assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'
            self.poco(name='ScrollView')[-1].offspring(name='删除').click()
        else:
            popup_message = self.common.poco_get_text(FriendPageLocator.friend_popup_message)
            assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'
            self.common.poco_click(FriendPageLocator.friend_popup_submit)

        sleep(2)
        assert self.common.poco_exists(FriendPageLocator.add_to_address_book_btn), f"未出現[新增至通讯录]選項"

        self.common.poco_click(FriendPageLocator.back_btn)
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)

    def into_chatroom_via_userDetail(self):
        if self.common.poco_exists(FriendPageLocator.friend_chat_btn):
            self.common.poco_click(FriendPageLocator.friend_chat_btn)
            sleep(1)

    def into_chatroom_via_addToAddressBook(self):
        if self.common.poco_exists(FriendPageLocator.add_to_address_book_btn):
            self.common.poco_click(FriendPageLocator.add_to_address_book_btn)
            sleep(1)

    def block_friend(self):
        self.wait_loading_finish()
        # self.common.poco_click(FriendPageLocator.friend_setting_button)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_long_click(FriendPageLocator.friend_block_button)
            string = self.poco(name='ScrollView')[0].children()[0].children()[0].children()[0].attr('name')
            assert string == '加入黑名单，你将不再收到对方的讯息，对方也无法查看你。', f'黑名單彈窗訊息有誤'
            self.common.poco_click(FriendPageLocator.friend_popup_submit)
            assert self.common.poco_get_attr(FriendPageLocator.friend_block_button, 'value') == '1', f'未成功加入黑名單'

        else:  # android parts
            self.common.poco_click(FriendPageLocator.friend_block_button)
            assert self.common.poco_get_text(
                FriendPageLocator.friend_popup_message) == '加入黑名单，你将不再收到对方的讯息，对方也无法查看你。', f'黑名單彈窗訊息有誤'
            self.common.poco_click(FriendPageLocator.friend_popup_submit)

    def impeach_friend(self):
        self.common.poco_click(FriendPageLocator.friend_impeach_button)
        self.common.poco_click(FriendPageLocator.impeach_radio)
        self.common.poco_click(FriendPageLocator.impeach_agree)

    def add_friend_first_chat(self):
        self.common.poco_click(FriendPageLocator.add_to_address_book_btn)
        self.common.poco_click(FriendPageLocator.add_friend_submit)
        self.wait_loading_finish()

        if self.common.poco_exists(FriendPageLocator.friend_first_chat):
            self.common.poco_click(FriendPageLocator.friend_first_chat)

    def back_to_friends_page(self):
        self.wait_loading_finish()
        for _ in range(1):
            self.common.poco_click(FriendPageLocator.back_btn)
            self.wait_loading_finish()

    def back_from_detail_to_chatList(self):
        while self.common.poco_exists(FriendPageLocator.back_btn):
            self.common.poco_click(FriendPageLocator.back_btn)
            self.wait_loading_finish()


