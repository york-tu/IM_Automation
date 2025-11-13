from time import sleep, time

from airtest.core.api import assert_exists, assert_not_exists
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.testcase.base_testcase import BaseTestCase
from Project.chat.app.pages.chatroom_page import ChatRoomPageLocator
import logging
import common.utils.globalvar as gl


class FriendPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = FriendPageLocator.base.check_device(
            Android=FriendPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=FriendPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    search_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='type', type_name='TextField'),
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

    add_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_add_user'),
        iOS=base.data_collation(type_kind='name', type_name='friendList_addFriend_barButtonItem'),
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
        iOS=base.data_collation(type_kind='name', type_name='新增至通讯录'),
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

    friend_remark_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/cl_note'),
        iOS=base.data_collation(type_kind='name', type_name='设定备注'),
    )

    friend_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0),
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
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    friend_first_chat = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='打招呼'),
        iOS=base.data_collation(type_kind='name', type_name='打招呼'),
    )

    team_list_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    team_list_frist = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组', action='parent().sibling()[0].child()[1]'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=2),
    )

    friend_list_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    friend_list_frist = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='好友', action='parent().sibling()[0].child()[1]'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=2),
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
        iOS=base.data_collation(type_kind='name', type_name='个人页面'),
    )


class FriendPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')
    phone_name = gl.get_value('PHONE_NAME')


    def check_add_friend_btn_display(self):
        assert self.common.poco_exists(FriendPageLocator.add_button), '新增好友鍵未顯示'

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
        if self.common.poco_exists(FriendPageLocator.add_button):  # 好友名單 > 右上角新增鍵
            self.common.poco_click(FriendPageLocator.add_button)
        if self.common.poco_exists(FriendPageLocator.add_friend_input):  # 新增好友頁 > 搜尋框
            if self.phone_platform.lower() == 'ios':
                self.common.poco_click(FriendPageLocator.add_friend_input)
            self.common.poco_send_text(FriendPageLocator.add_friend_input, name)
            self.common.poco_click(FriendPageLocator.add_friend_search)
        self.wait_loading_finish()

        if self.common.poco_exists(FriendPageLocator.add_to_address_book_btn):
            return True
        else:
            return False

    def search_friend_from_list(self, name):  # 搜尋好友, 進到好友詳情頁
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)
        if self.common.poco_wait_appearance(FriendPageLocator.search_input):
            if self.phone_platform.lower() == 'ios':
                self.common.poco_click(FriendPageLocator.search_input)
            self.common.poco_send_text(FriendPageLocator.search_input, name)
        self.common.sleep(1)
        if not self.common.poco_exists(FriendPageLocator.search_none_check):
            if self.common.poco_exists(FriendPageLocator.friend_list_frist):
                assert self.common.poco_get_text(FriendPageLocator.friend_list_frist) == name, f'找不到任何結果'
                self.common.poco_click(FriendPageLocator.friend_list_frist)
            elif self.common.poco_exists(FriendPageLocator.team_list_frist):
                assert self.common.poco_get_text(FriendPageLocator.team_list_frist).__contains__(name), f'找不到任何結果'
                self.common.poco_click(FriendPageLocator.team_list_frist)

    def add_myself(self, phone_mail_id, nation='CN', account_type='phone'):

        if account_type == 'phone':
            # if gl.get_value('ENV').lower() == 'uat':
            #     self_id = "gubot03"
            # else:
            #     self_id = "gutest001"

            if self.common.poco_exists(FriendPageLocator.add_button):
                self.common.poco_click(FriendPageLocator.add_button)
                self.wait_loading_finish()
            if self.common.poco_exists(FriendPageLocator.add_friend_input):
                if self.phone_platform.lower() == 'android':
                    self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                    self.common.poco_click(FriendPageLocator.add_friend_search)
                else:
                    self.common.poco_click(FriendPageLocator.add_friend_input)
                    self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                    self.common.poco_click(FriendPageLocator.add_friend_search)

        elif account_type == 'email':
            if self.common.poco_exists(FriendPageLocator.add_button):
                self.common.poco_click(FriendPageLocator.add_button)
            if self.common.poco_exists(FriendPageLocator.add_friend_input):
                self.common.poco_send_text(FriendPageLocator.add_friend_input, phone_mail_id)
                self.common.poco_click(FriendPageLocator.add_friend_search)

        assert not self.common.poco_exists(FriendPageLocator.add_to_address_book_btn)
        assert not self.common.poco_exists(FriendPageLocator.friend_chat_btn)

    def search_clear(self, id):
        self.common.poco_click(FriendPageLocator.add_button)

        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(FriendPageLocator.add_friend_input)
            self.common.poco_send_text(FriendPageLocator.add_friend_input, 'clear')
            self.common.poco_click(FriendPageLocator.search_clear)
            default_text = self.poco(type='StaticText')[1].attr('value')
            assert '我的 IM ID：' in default_text, f'新增好友頁未清空'

        else:
            self.common.poco_send_text(FriendPageLocator.add_friend_input, id)
            assert self.common.poco_exists(FriendPageLocator.add_friend_search), f'未顯示搜查按鍵'
            self.common.poco_click(FriendPageLocator.search_clear)

    def set_note(self, note):
        self.common.poco_click(FriendPageLocator.friend_remark_btn)

        if self.phone_platform.lower() == 'ios':  # ios part
            self.common.poco_click(FriendPageLocator.note_input)
            self.common.poco_send_text(FriendPageLocator.note_input, note)
            self.common.poco_click(FriendPageLocator.remark_submit)
            self.common.poco_click(FriendPageLocator.friend_note_button)
            assert self.common.poco_get_attr(FriendPageLocator.note_input, 'value') == note, f'設定描述失敗'

            while not self.poco(name='全选'):
                self.common.poco_long_click(FriendPageLocator.note_input)
                sleep(1)
            self.poco(name='全选').click()
            self.poco(name='delete').click()

            self.common.poco_click(FriendPageLocator.remark_submit)
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            assert self.poco(type='StaticText')[-1].attr('value') == '描述最长至300字', f'描述清空失敗'

            self.common.poco_click(FriendPageLocator.remark_back)

        else:  # android part
            self.common.poco_send_text(FriendPageLocator.note_input, note)
            self.common.poco_click(FriendPageLocator.remark_submit)
            self.common.poco_click(FriendPageLocator.friend_note_button)
            assert self.common.poco_get_text(FriendPageLocator.note_input) == note, f'設定描述失敗'

            self.common.poco_send_text(FriendPageLocator.note_input, '')
            self.common.poco_click(FriendPageLocator.remark_submit)
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            assert self.common.poco_get_text(FriendPageLocator.note_input) == '描述最长至300字...', f'描述清空失敗'

            self.common.poco_click(FriendPageLocator.remark_back)

    def set_nickname(self, name):
        if self.phone_platform.lower() == 'ios':  # ios part
            # ============================= 更改原暱稱 =============================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_send_text(FriendPageLocator.nickname_input, name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.poco(type='StaticText')[1].attr('value') == name, f'暱稱更換失敗'
            # ============================= 將暱稱刪除, 欄位留空, 使用預設暱稱 ==========================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
            default_nickname = self.poco(type='TextField').attr('value')
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.poco(type='StaticText')[1].attr('value') == default_nickname, f'暱稱預設失敗'

        else:  # android part
            original_nick_name = self.common.poco_get_text(FriendPageLocator.friend_nickname)
            # ============================= 更改原暱稱 =============================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == name, f'暱稱更換失敗'
            # ============================= 將暱稱刪除, 欄位留空, 使用預設暱稱 ==========================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, '')
            sleep(3)
            default_nickname = self.common.poco_get_text(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.remark_submit)
            aaa = self.common.poco_get_text(FriendPageLocator.friend_nickname)
            assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == default_nickname, f'暱稱預設失敗, 預期:{default_nickname},實際:{aaa}'
            # ============================= 將預設暱稱改為原暱稱 =======================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, original_nick_name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            if self.common.poco_exists(FriendPageLocator.friend_nickname):
                assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == original_nick_name, f'暱稱更換失敗'

    def add_friend(self, nickname):  # 添加好友並回到聊天列表
        self.common.poco_click(FriendPageLocator.add_to_address_book_btn)
        self.wait_loading_finish()
        assert self.common.poco_get_text(ChatRoomPageLocator.options_title) == nickname
        if self.common.poco_exists(ChatRoomPageLocator.back_btn):
            self.common.poco_click(ChatRoomPageLocator.back_btn)

    def delete_friend_from_UserDetail(self, name):  # 好友名單 > 用戶詳情 > 刪除
        self.common.poco_click(FriendPageLocator.friend_delete_button)
        if self.common.poco_exists(FriendPageLocator.friend_popup_message):  # 二次刪除確認框
            if self.phone_platform.lower() == 'ios':
                popup_message = self.common.poco_get_attr(FriendPageLocator.friend_popup_message, 'value')
                assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'
                if self.phone_name.lower() == 'iphone_15_pro':
                    self.poco(name='ScrollView')[-1].offspring(name='删除').click()
                else:
                    self.poco(type='Other')[-3].child(name='删除').click()

            else:
                popup_message = self.common.poco_get_text(FriendPageLocator.friend_popup_message)
                assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'
                self.common.poco_click(FriendPageLocator.friend_popup_submit)

        assert self.common.poco_exists(FriendPageLocator.add_to_address_book_btn), f"未出現[新增至通讯录]選項"

        self.common.poco_click(FriendPageLocator.back_btn)
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)

    def block_friend(self):
        self.wait_loading_finish()
        # self.common.poco_click(FriendPageLocator.friend_setting_button)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_long_click(FriendPageLocator.friend_block_button)
            string = self.poco(name='ScrollView')[0].children()[0].children()[0].children()[0].children()[0].attr(
                'name')
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
        for _ in range(3):
            self.common.poco_click(FriendPageLocator.back_btn)
            self.wait_loading_finish()

