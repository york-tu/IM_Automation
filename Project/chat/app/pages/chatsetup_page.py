import re
from time import sleep
from airtest.core.api import text
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.chatroom_page import ChatRoomPage, ChatRoomPageLocator
import logging
import common.utils.globalvar as gl


class ChatSetupPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = ChatSetupPageLocator.base.check_device(
            Android=ChatSetupPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=ChatSetupPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    search_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    options_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_options'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    options_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    options_start = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_start_icon'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    options_back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_back'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    options_next = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_next'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    popup_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    member_count = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_member_count'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_chevron_right'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_add_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_name_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=0),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    recent_add_member = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=1),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )
    member_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_photo'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_edit_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_edit'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_add_rule = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='加入成员'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_serch_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_delete_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_delete', num=0),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_serch_clear = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_clear_iv'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_add_radio = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_checked', num=0),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_add_delete = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete', num=0),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    member_text = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_text'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    member_empty = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/layout_empty'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    black_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='黑名单'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    black_ = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    black_amount = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_role_quantity', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    admin_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='管理员'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    admin_ = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    rule_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组设定'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    rule_ = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    room_last_icon = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_btn_incoming_header_icon',
                                    num=-1),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )

    friend_add_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_button'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )


class ChatSetupPage(Base):
    def into_setting(self):
        if self.common.poco_exists(ChatSetupPageLocator.options_btn):
            self.common.poco_click(ChatSetupPageLocator.options_btn)

            title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
            assert title[2:] == '详情', f'進入設定頁面有誤'

    def into_group_member_list(self):
        if self.common.poco_exists(ChatSetupPageLocator.member_count):
            self.common.poco_click(ChatSetupPageLocator.member_btn)
        sleep(3)
        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '成员', f'進入成員列表有誤, 實際{title}'

    def search_block_member(self, target_member):
        if self.common.poco_exists(ChatSetupPageLocator.member_serch_clear):
            self.common.poco_click(ChatSetupPageLocator.member_serch_clear)
        self.common.poco_click(ChatSetupPageLocator.member_serch_input)
        self.common.poco_send_text(ChatSetupPageLocator.member_serch_input, target_member)
        assert self.common.poco_exists(ChatSetupPageLocator.member_empty)
        if self.common.poco_exists(ChatSetupPageLocator.member_serch_clear):
            self.common.poco_click(ChatSetupPageLocator.member_serch_clear)
        self.common.poco_click(ChatSetupPageLocator.options_back)

    def into_group_member_add(self):
        if self.common.poco_exists(ChatSetupPageLocator.member_add_rule):
            self.common.poco_click(ChatSetupPageLocator.member_add_rule)

        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '成员', f'進入成員列表有誤'

    def into_group_black(self):
        detail_page_original_black_amount = self.common.poco_get_text(ChatSetupPageLocator.black_amount)
        if self.common.poco_exists(ChatSetupPageLocator.black_btn):
            self.common.poco_click(ChatSetupPageLocator.black_btn)

        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '黑名单设置', f'進入 黑名單頁面有誤'
        _text = self.common.poco_get_text(ChatSetupPageLocator.member_text)
        black_setting_page_original_black_amount = _text.split(' ')[1][-4]
        return detail_page_original_black_amount, black_setting_page_original_black_amount

    def add_block_member(self, block_name, detail_page_original_black_amount, black_setting_page_original_black_amount):
        self.common.poco_click(ChatSetupPageLocator.member_add_btn)

        if self.common.poco_exists(ChatSetupPageLocator.member_serch_clear):
            self.common.poco_click(ChatSetupPageLocator.member_serch_clear)

        self.common.poco_click(ChatSetupPageLocator.member_serch_input)
        self.common.poco_send_text(ChatSetupPageLocator.member_serch_input, block_name)
        self.wait_loading_finish()
        self.common.poco_click(ChatSetupPageLocator.member_add_radio)
        self.common.poco_click(ChatSetupPageLocator.options_next)
        aaa = self.common.poco_get_text(ChatSetupPageLocator.popup_message)
        bbb = f'将{block_name}加入黑名單嗎？\n加入黑名單將被移除群组，並不可再次加入'
        assert self.common.poco_get_text(ChatSetupPageLocator.popup_message) == f'将{block_name}加入黑名单吗？\n加入黑名單將被移除群组，並不可再次加入', f'加入黑名單成員/文案錯誤'

        self.common.poco_click(ChatSetupPageLocator.popup_btn)
        _text = self.common.poco_get_text(ChatSetupPageLocator.member_text)
        black_setting_page_current_black_amount = _text.split(' ')[1][0]
        assert black_setting_page_current_black_amount == str(int(black_setting_page_original_black_amount)+1)
        if self.common.poco_exists(ChatSetupPageLocator.member_icon):
            assert self.common.poco_get_text(ChatSetupPageLocator.recent_add_member) == block_name, f'新增的黑名單成員有誤'
        self.common.poco_click(ChatSetupPageLocator.options_back)

        detail_page_current_black_amount = self.common.poco_get_text(ChatSetupPageLocator.black_amount)
        assert detail_page_current_black_amount == str(int(detail_page_original_black_amount)+1)

    def remove_block_member(self, block_name, detail_page_original_black_amount, black_setting_page_original_black_amount):
        assert self.common.poco_get_text(ChatSetupPageLocator.recent_add_member) == block_name, f'黑名單成員有誤'
        self.common.poco_click(ChatSetupPageLocator.member_edit_btn)
        self.common.poco_click(ChatSetupPageLocator.member_delete_btn)
        assert self.common.poco_get_text(
            ChatSetupPageLocator.popup_message) == f'要把{block_name} 移除黑名单吗？\n移除黑名单，可再次加入群组', f'移除黑名單成員/文案錯誤'
        self.common.poco_click(ChatSetupPageLocator.popup_btn)
        _text = self.common.poco_get_text(ChatSetupPageLocator.member_text)
        black_setting_page_current_black_amount = _text.split(' ')[1][0]
        assert black_setting_page_current_black_amount == str(int(black_setting_page_original_black_amount) - 1)

        if self.common.poco_exists(ChatSetupPageLocator.member_icon):
            assert not self.common.poco_get_text(ChatSetupPageLocator.recent_add_member) == block_name, f'黑名單成員移除有誤'

        self.common.poco_click(ChatSetupPageLocator.options_back)

        detail_page_current_black_amount = self.common.poco_get_text(ChatSetupPageLocator.black_amount)
        assert detail_page_current_black_amount == str(int(detail_page_original_black_amount) - 1)

    def into_group_admin(self):
        if self.common.poco_exists(ChatSetupPageLocator.admin_btn):
            self.common.poco_click(ChatSetupPageLocator.admin_btn)

        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '群组管理员', f'進入 管理員頁面有誤'

    def into_group_rule(self):
        if self.common.poco_exists(ChatSetupPageLocator.rule_btn):
            self.common.poco_click(ChatSetupPageLocator.rule_btn)

        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '群组设定', f'進入 群組設定有誤'

    def check_image_rule(self):
        self.common.sleep(0.5)

        if self.common.poco_wait_exists(ChatRoomPageLocator.add_function_btn):
            self.common.poco_click(ChatRoomPageLocator.add_function_btn)
            assert self.common.poco_exists(ChatRoomPageLocator.image_camera) is True, f'沒有顯示相機/拍照按鈕'
            assert self.common.poco_exists(ChatRoomPageLocator.image_photo) is True, f'沒有顯示相機/拍照按鈕'

    def check_add_user_rule(self, status):
        self.into_setting()
        self.wait_loading_finish()

        if status == '1':
            if self.common.poco_exists(ChatSetupPageLocator.member_count):
                self.common.poco_click(ChatSetupPageLocator.member_btn)

            self.common.sleep(1)
            assert self.common.poco_exists(ChatSetupPageLocator.member_add_btn), f'權限開啟 但沒有顯示 加好友按鈕'
            assert self.common.poco_get_text(ChatSetupPageLocator.member_name_frist) == '加入成员', f'權限開啟 加好友按鈕文案有誤'

            self.common.poco_click(ChatRoomPageLocator.back_btn)

        else:
            if self.common.poco_exists(ChatSetupPageLocator.member_count):
                self.common.poco_click(ChatSetupPageLocator.member_btn)

            self.common.sleep(1)
            assert not self.common.poco_exists(ChatSetupPageLocator.member_add_btn), f'權限關閉 但有顯示 加好友按鈕'

            self.common.poco_click(ChatRoomPageLocator.back_btn)

        if self.common.poco_wait_exists(ChatSetupPageLocator.options_start):
            self.common.poco_click(ChatSetupPageLocator.options_start)

    def check_group_rule(self, rule):
        self.common.sleep(1.5)
        rule_list = list(rule)

        if rule_list[0] == '1':  # 傳送訊息"開啟"
            self.send_message_for_rule_check('群組權限更改测试')
            self.check_image_rule()

            if rule_list[3] == '1':
                self.send_url_message_for_rule_check()
            else:
                self.check_url_block()

        else:
            if self.common.poco_exists(ChatRoomPageLocator.message_input_block):
                assert self.common.poco_get_text(ChatRoomPageLocator.message_input_block) == '此群组不允许传送讯息', f'權限開啟後 訊息框未開啟'

        self.check_add_user_rule(rule_list[4])

    def send_url_message_for_rule_check(self):
        messages = ['https://www.google.com.tw/', 'https://tw.yahoo.com/']
        for message in messages:
            self.send_message_for_rule_check(message)
            self.rul_message_for_rule_check(message)

    def send_message_for_rule_check(self, message):
        if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, message)

        self.wait_loading_finish()
        self.common.poco_click(ChatRoomPageLocator.send_message_btn)

        assert self.common.poco_get_text(ChatRoomPageLocator.last_message_room) == message, f'發送聊天訊息有誤'

    def rul_message_for_rule_check(self, message):
        if self.common.poco_exists(ChatRoomPageLocator.message_locator(message)):
            self.common.poco_click(ChatRoomPageLocator.message_locator(message))
            self.common.sleep(3)

            assert self.common.poco_exists(ChatRoomPageLocator.url_check_point), f'超連結沒有出現'
            self.go_back()

    def check_url_block(self):
        url_list = ['https://google.com', 'https://tw.yahoo.com/']
        last_msg_old = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
        for url in url_list:
            self.common.sleep(0.5)
            if self.common.poco_exists(ChatRoomPageLocator.message_input_empty):
                self.common.poco_click(ChatRoomPageLocator.message_input)
                self.common.poco_send_text(ChatRoomPageLocator.message_input, url)

            self.wait_loading_finish()
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
            assert self.common.poco_exists(ChatRoomPageLocator.message_input_empty) is False, f'超連結還是送出訊息'

            self.common.sleep(0.5)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, '')

        last_msg_new = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
        assert last_msg_old == last_msg_new, f'最後一筆訊息有誤'

    def check_admin_rule(self, rule):
        self.common.sleep(1)
        rule_list = list(rule)

        self.into_setting()
        # 移除群組成員 權限
        if rule_list[0] == '1':
            self.check_member_delete()

        # 黑名單 權限
        if rule_list[1] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.black_btn), f'權限開啟沒有顯示黑名單選項'
            # 變更群組資料 權限
        if rule_list[2] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.rule_btn), f'權限開啟沒有顯示變更群組資料選項'
        # 新增管理員 權限
        if rule_list[3] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.admin_btn), f'權限開啟沒有顯示新增管理員選項'

        # 加好友 權限  ##目前有bug 會沒有刷新權限後續開啟 
        # if rule_list[4] == '1':
        # self.check_friend_add()

        self.common.poco_click(ChatSetupPageLocator.options_start)

    def member_search(self, name):
        if self.common.poco_exists(ChatSetupPageLocator.member_serch_input):
            self.common.poco_click(ChatSetupPageLocator.member_serch_input)
            self.common.poco_send_text(ChatSetupPageLocator.member_serch_input, name)
            self.wait_loading_finish()
            aaa = self.common.poco_get_text(ChatSetupPageLocator.member_text)
            if self.common.poco_get_text(ChatSetupPageLocator.member_text) != '成员 0/2300':
                if self.common.poco_get_text(ChatSetupPageLocator.member_name_frist) == name:
                    return True
                else:
                    self.common.poco_click(ChatSetupPageLocator.member_serch_clear)
                    return False
            else:
                return False


    def group_member_delete(self, name):
        self.wait_loading_finish()
        self.into_group_member_list()

        self.wait_loading_finish()
        assert self.common.poco_get_text(
            ChatSetupPageLocator.member_edit_btn) == '编辑', f'權限開啟 成員列標沒有出現編輯'
        self.common.poco_click(ChatSetupPageLocator.member_edit_btn)
        assert self.member_search(name) is True, f'在群組中沒有搜查到成員{name}'

        self.common.poco_click(ChatSetupPageLocator.member_delete_btn)
        assert self.common.poco_get_text(ChatSetupPageLocator.popup_message) == f'要把{name} 从群组里删除吗？', f'群組刪除成員訊息錯誤'
        self.common.poco_click(ChatSetupPageLocator.popup_btn)
        self.wait_loading_finish()
        assert not self.member_search(name), f'群組成員{name}刪除失敗'

        if self.common.poco_exists(ChatSetupPageLocator.options_back):
            self.common.poco_click(ChatSetupPageLocator.options_back)
            self.wait_loading_finish()
        if self.common.poco_get_text(ChatSetupPageLocator.options_title) == "群聊详情":
            self.common.poco_click(ChatSetupPageLocator.options_start)
            self.wait_loading_finish()
        if self.common.poco_exists(ChatSetupPageLocator.options_back):
            self.common.poco_click(ChatSetupPageLocator.options_back)
            self.wait_loading_finish()
    def group_member_add(self, name):
        self.wait_loading_finish()
        self.into_group_member_list()

        if self.common.poco_exists(ChatSetupPageLocator.member_add_btn):
            self.common.poco_click(ChatSetupPageLocator.member_add_btn)

            assert self.member_search(name) == True, f'沒有搜尋到好友{name}'

            self.common.poco_click(ChatSetupPageLocator.member_add_radio)
            assert self.common.poco_exists(ChatSetupPageLocator.member_add_delete), f'點擊後成員沒有被加入列表'

            self.common.sleep(1)
            self.common.poco_click(ChatSetupPageLocator.options_next)
            self.common.poco_click(ChatSetupPageLocator.popup_btn)

    def check_member_delete(self):

        for i in range(2):
            self.wait_loading_finish()

            if i == 0:
                self.into_group_member_list()
            elif i == 1:
                self.into_group_member_add()

            self.wait_loading_finish()

            assert self.common.poco_get_text(ChatSetupPageLocator.member_edit_btn) == '编辑', f'權限開啟 成員列標沒有出現編輯'
            self.common.poco_click(ChatSetupPageLocator.member_edit_btn)

            assert self.common.poco_exists(ChatSetupPageLocator.member_delete_btn)
            self.common.poco_click(ChatSetupPageLocator.options_back)

    def check_friend_add(self):
        self.wait_loading_finish()

        self.common.poco_click(ChatSetupPageLocator.options_back)
        if self.common.poco_exists(ChatSetupPageLocator.room_message_icon):
            self.common.poco_click(ChatSetupPageLocator.room_message_icon)

            status = self.common.poco_get_text(ChatSetupPageLocator.friend_add_btn)
            assert status == '传讯息' or status == '新增至通讯录', f'權限開啟 點擊成員頭像沒有出現加好友選項'
            self.common.poco_click(ChatSetupPageLocator.options_back)

        self.into_setting()
