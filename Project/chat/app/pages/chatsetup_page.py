import re
from time import sleep
from airtest.core.api import text

from Project.chat.app.pages.friend_page import FriendPageLocator
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.chatroom_page import ChatRoomPage, ChatRoomPageLocator
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class ChatSetupPageLocator(BaseLocator):
    """聊天設定頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

    search_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )
    options_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_options'),
        iOS=base.data_collation(type_kind='name', type_name='message_more_button')
    )
    detail_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView'),
        iOS=base.data_collation(type_kind='name', type_name='群组详情')
    )
    options_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_title'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=0)
    )
    options_start = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_start_icon'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )
    options_back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button')
    )
    menu_back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='name', type_name='base_back_button')
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
        iOS=base.data_collation(type_kind='name', type_name='9')
    )
    member_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_chevron_right'),
        iOS=base.data_collation(type_kind='name', type_name='groupDetail_addMember_cell')
    )
    member_add_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_icon'),
        iOS=base.data_collation(type_kind='name', type_name='buttonIconPlus')
    )
    member_add_text = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='加入成员')
    )
    member_name_frist = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name', num=0),
        iOS=base.data_collation(type_kind='name', type_name='editMember_memberCell_name_label', num=0)
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
        iOS=base.data_collation(type_kind='name', type_name='editMember_edit_barButtonItem')
    )

    member_add_rule = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='加入成员'),
        iOS=base.data_collation(type_kind='name', type_name='加入成员')
    )
    member_search_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/search_content_et'),
        iOS=base.data_collation(type_kind='name', type_name='editMember_search_textField')
    )
    member_delete_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_delete', num=0),
        iOS=base.data_collation(type_kind='name', type_name='minus.circle.fill', num=0)
    )
    member_search_clear = base.check_device(
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
        iOS=base.data_collation(type_kind='name', type_name='groupDetail_blacklist_cell')
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
        iOS=base.data_collation(type_kind='name', type_name='groupDetail_admins_cell')
    )
    admin_ = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/btn_delete'),
        iOS=base.data_collation(type_kind='name', type_name='搜索')
    )
    rule_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='群组设定'),
        iOS=base.data_collation(type_kind='name', type_name='groupDetail_groupSettings_cell')
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
        Android=base.data_collation(type_kind='text', type_name='新增至通讯录'),
        iOS=base.data_collation(type_kind='name', type_name='新增至通讯录')
    )


class ChatSetupPage(Base):
    phone_platform = gl.get_value("PHONE_PLATFORM")

    def into_setting(self):
        if self.common.poco_exists(ChatSetupPageLocator.options_btn):
            self.common.poco_click(ChatSetupPageLocator.options_btn)
            if self.phone_platform.lower() == 'android':
                title = self.common.poco_get_text(ChatSetupPageLocator.detail_title)
            else:
                title = self.poco(type='NavigationBar').offspring(type='StaticText')[0].attr('label')
            assert title[-2:] == '详情', f'進入設定頁面有誤'

    def into_group_member_list(self):
        if self.common.poco_exists(ChatSetupPageLocator.member_count):
            self.common.poco_click(ChatSetupPageLocator.member_count)
        sleep(3)
        title = self.common.poco_get_text(ChatSetupPageLocator.options_title)
        assert title == '成员', f'進入成員列表有誤, 實際{title}'

    def search_block_member(self, target_member):
        if self.common.poco_exists(ChatSetupPageLocator.member_search_clear):
            self.common.poco_click(ChatSetupPageLocator.member_search_clear)
        self.common.poco_click(ChatSetupPageLocator.member_search_input)
        self.common.poco_send_text(ChatSetupPageLocator.member_search_input, target_member)
        assert self.common.poco_exists(ChatSetupPageLocator.member_empty)
        if self.common.poco_exists(ChatSetupPageLocator.member_search_clear):
            self.common.poco_click(ChatSetupPageLocator.member_search_clear)
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

        if self.common.poco_exists(ChatSetupPageLocator.member_search_clear):
            self.common.poco_click(ChatSetupPageLocator.member_search_clear)

        self.common.poco_click(ChatSetupPageLocator.member_search_input)
        self.common.poco_send_text(ChatSetupPageLocator.member_search_input, block_name)
        self.wait_loading_finish()
        self.common.poco_click(ChatSetupPageLocator.member_add_radio)
        self.common.poco_click(ChatSetupPageLocator.options_next)
        assert (self.common.poco_get_text(ChatSetupPageLocator.popup_message) ==
                f'将{block_name}加入黑名单吗？\n加入黑名單將被移除群组，並不可再次加入'), f'加入黑名單成員/文案錯誤'

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
        self.common.poco_click(ChatRoomPageLocator.add_function_btn)
        sleep(1)
        assert self.common.poco_exists(ChatRoomPageLocator.image_camera), f'沒有顯示相機/拍照按鈕'
        assert self.common.poco_exists(ChatRoomPageLocator.image_photo), f'沒有顯示相機/拍照按鈕'

    def check_add_user_rule(self, status):
        self.into_setting()
        sleep(1)

        if status == '1':
            if self.phone_platform.lower() == 'android':
                self.common.poco_click(ChatSetupPageLocator.member_btn)  # 群組詳情頁成員數btn

                self.common.sleep(1)
                assert self.common.poco_exists(ChatSetupPageLocator.member_add_btn), f'權限開啟 但沒有顯示 加入成員按鈕'
                assert self.common.poco_get_text(
                    ChatSetupPageLocator.member_name_frist) == '加入成员', f'權限開啟 加好友按鈕文案有誤'
            else:
                self.common.poco_click(ChatSetupPageLocator.member_count)

                # iOS 優化：使用動態等待替代固定 sleep(1)
                member_add_btn_found = False
                for i in range(2):  # 2 * 0.5 = 1 秒（最多等待，從 1.5 秒減少）
                    try:
                        if self.common.poco_exists(ChatSetupPageLocator.member_add_btn):
                            member_add_btn_found = True
                            break
                    except:
                        pass
                    sleep(0.5)
                
                assert member_add_btn_found, f'權限開啟 但沒有顯示 加入成員按鈕'
                assert self.common.poco_exists(ChatSetupPageLocator.member_add_text)

            self.common.poco_click(ChatRoomPageLocator.back_btn)  # 回到群組詳情頁

        else:
            if self.phone_platform.lower() == 'android':
                self.common.poco_click(ChatSetupPageLocator.member_btn)
            else:
                self.common.poco_click(ChatSetupPageLocator.member_count)

            # iOS 優化：使用動態等待替代固定 sleep(1)
            if self.phone_platform.lower() == 'ios':
                # 快速檢查按鈕不存在（最多等待 1 秒）
                for i in range(2):  # 2 * 0.5 = 1 秒
                    try:
                        if not self.common.poco_exists(ChatSetupPageLocator.member_add_btn):
                            break
                    except:
                        pass
                    sleep(0.5)
            else:
                self.common.sleep(1)
            
            assert not self.common.poco_exists(ChatSetupPageLocator.member_add_btn), f'權限關閉 但有顯示 加好友按鈕'

            self.common.poco_click(ChatRoomPageLocator.back_btn)  # 回到群組詳情頁

    def check_group_rule(self, rule):
        self.common.sleep(1.5)
        rule_list = list(rule)  # rule = [傳送訊息, 傳送圖片, 傳送影片, 傳送超連結, 傳送檔案, 加入新成員]
        if rule_list[0] == '1':  # 傳送訊息"開啟"
            self.send_message_for_rule_check('群組權限更改测试')
            self.check_image_rule()

            # 傳送圖片/影片
            if rule_list[1] == '1' or rule_list[2] == '1':
                self.send_media_for_rule_check("1")
            else:
                self.send_media_for_rule_check("0")

            # 傳送檔案
            self.send_file_for_rule_check(rule_list[4])

            # 傳送超連結
            if rule_list[3] == '1':
                self.send_url_message_for_rule_check()
            else:
                self.check_url_block()

        else:
            assert self.common.poco_get_text(ChatRoomPageLocator.message_input_block) == '此群组不允许传送讯息', f'權限開啟後 訊息框未開啟'

        self.check_add_user_rule(rule_list[5])

        self.common.poco_click(ChatSetupPageLocator.menu_back)  # 回到聊天室

    def send_url_message_for_rule_check(self):
        message = 'https://tw.yahoo.com/'
        self.send_message_for_rule_check(message)
        self.url_message_for_rule_check(message)

    def send_message_for_rule_check(self, message):
        # iOS 優化：使用已優化的發送邏輯
        # if self.phone_platform.lower() == 'ios':
        #     self.common.poco_click(ChatRoomPageLocator.message_input)
        #     self.common.poco_send_text(ChatRoomPageLocator.message_input, message)
        #     self.common.poco_click(ChatRoomPageLocator.send_message_btn)
        #     sleep(0.5)
        #     room_last_message = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
        #
        #     assert room_last_message == message, f'發送聊天訊息有誤, 預期: {message}, 實際:{room_last_message}'
        # else:
        if self.common.poco_exists(ChatRoomPageLocator.send_message_btn):
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
        self.common.poco_click(ChatRoomPageLocator.message_input)
        self.common.poco_send_text(ChatRoomPageLocator.message_input, message)
        self.common.poco_click(ChatRoomPageLocator.send_message_btn)
        sleep(0.5)
        room_last_message = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
        assert room_last_message == message, f'發送聊天訊息有誤, 預期: {message}, 實際:{room_last_message}'

    def send_media_for_rule_check(self, enable):
        while not self.common.poco_exists(ChatRoomPageLocator.image_photo):
            self.common.poco_click(ChatRoomPageLocator.add_function_btn)
        self.common.poco_click(ChatRoomPageLocator.image_photo)
        sleep(1)
        if enable == '1':
            assert self.common.poco_exists(ChatRoomPageLocator.device_photo_view)
            self.common.poco_click(ChatRoomPageLocator.photo_view_close_btn)
        else:
            assert not self.common.poco_exists(ChatRoomPageLocator.device_photo_view)

    def send_file_for_rule_check(self, enable):
        while not self.common.poco_exists(ChatRoomPageLocator.file_btn):
            self.common.poco_click(ChatRoomPageLocator.add_function_btn)
        self.common.poco_click(ChatRoomPageLocator.file_btn)
        sleep(1)
        if enable == '1':
            assert self.common.poco_exists(ChatRoomPageLocator.file_upload_view)

            if self.phone_platform.lower() == 'android':
                self.common.poco_click(ChatRoomPageLocator.folder_file_index(1))
                self.common.poco_click(ChatRoomPageLocator.confirm_msg_send_btn)
            else:  # ios part
                ele = self.poco(name='File View').child(type='Cell')[1]
                ele.click()
                self.common.poco_click(ChatRoomPageLocator.confirm_msg_send_btn)
        else:
            assert not self.common.poco_exists(ChatRoomPageLocator.file_upload_view)

    def url_message_for_rule_check(self, message):
        if self.common.poco_exists(ChatRoomPageLocator.send_message_btn):
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
        if self.common.poco_exists(ChatRoomPageLocator.message_locator(message)):
            self.common.poco_click(ChatRoomPageLocator.message_locator(message))
            
            # iOS 優化：使用動態等待替代固定 sleep(3)
            if self.phone_platform.lower() == 'ios':
                # 快速等待連結頁面載入（最多等待 1.5 秒，從 2 秒減少）
                url_loaded = False
                for i in range(3):  # 3 * 0.5 = 1.5 秒
                    try:
                        if self.common.poco_exists(ChatRoomPageLocator.url_check_point):
                            url_loaded = True
                            break
                    except:
                        pass
                    sleep(0.5)
                assert url_loaded, f'超連結沒有出現'
            else:
                self.common.sleep(3)
                assert self.common.poco_exists(ChatRoomPageLocator.url_check_point), f'超連結沒有出現'

            self.go_back()

    def check_url_block(self):
        url = 'https://google.com'
        last_msg_old = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)

        # iOS 優化：使用已優化的發送邏輯
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(ChatRoomPageLocator.message_input)
            sleep(0.15)  # iOS 優化：減少鍵盤彈出等待時間
            self.common.poco_send_text(ChatRoomPageLocator.message_input, url)
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)
            
            # iOS 優化：快速檢查訊息是否被阻擋（最多等待 1.5 秒）
            for i in range(3):  # 3 * 0.5 = 1.5 秒
                try:
                    last_msg_new = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
                    if last_msg_old == last_msg_new:
                        break  # 訊息被阻擋，符合預期
                except:
                    pass
                sleep(0.5)
            
            last_msg_new = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
            assert last_msg_old == last_msg_new, f'最後一筆訊息有誤'
        else:
            self.common.poco_click(ChatRoomPageLocator.message_input)
            self.common.poco_send_text(ChatRoomPageLocator.message_input, url)
            self.common.poco_click(ChatRoomPageLocator.send_message_btn)

            last_msg_new = self.common.poco_get_text(ChatRoomPageLocator.last_message_room)
            assert last_msg_old == last_msg_new, f'最後一筆訊息有誤'

    def check_admin_rule(self, rule):
        sleep(1)
        rule_list = list(rule)
        self.into_setting()

        # ====================================================================
        # 權限: 移除群組成員
        if rule_list[0] == '1':
            self.check_member_delete()
        # 權限: 黑名單
        if rule_list[1] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.black_btn), f'權限開啟沒有顯示黑名單選項'
        # 權限: 變更群組資料
        if rule_list[2] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.rule_btn), f'權限開啟沒有顯示變更群組資料選項'
        # 權限: 新增管理員
        if rule_list[3] == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.admin_btn), f'權限開啟沒有顯示新增管理員選項'
        # 權限: 加好友
        self.check_friend_add(rule_list[4])
        # ====================================================================

        self.common.poco_click(ChatSetupPageLocator.menu_back)

    def member_search(self, name):
        if self.common.poco_exists(ChatSetupPageLocator.member_search_input):
            self.common.poco_click(ChatSetupPageLocator.member_search_input)
            self.common.poco_send_text(ChatSetupPageLocator.member_search_input, name)
            self.wait_loading_finish()
            aaa = self.common.poco_get_text(ChatSetupPageLocator.member_text)
            if self.common.poco_get_text(ChatSetupPageLocator.member_text) != '成员 0/2300':
                if self.common.poco_get_text(ChatSetupPageLocator.member_name_frist) == name:
                    return True
                else:
                    self.common.poco_click(ChatSetupPageLocator.member_search_clear)
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
        if self.common.poco_get_text(ChatSetupPageLocator.detail_title) == "群组详情":
            self.common.poco_click(ChatSetupPageLocator.menu_back)
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
            sleep(1)

            if i == 0:
                self.into_group_member_list()
            elif i == 1:
                self.into_group_member_add()

            sleep(1)

            assert self.common.poco_get_text(ChatSetupPageLocator.member_edit_btn) == '编辑', f'權限開啟 成員列標沒有出現編輯'
            self.common.poco_click(ChatSetupPageLocator.member_edit_btn)

            assert self.common.poco_exists(ChatSetupPageLocator.member_delete_btn)
            self.common.poco_click(ChatSetupPageLocator.options_back)

    def check_friend_add(self, new='1'):
        sleep(1)
        self.common.poco_click(ChatSetupPageLocator.member_btn)  # 成員列表
        self.common.poco_click(ChatSetupPageLocator.member_search_input)
        self.common.poco_send_text(ChatSetupPageLocator.member_search_input, 'test1234')
        self.common.poco_click(ChatSetupPageLocator.member_name_frist)

        # 已加為好友則先刪好友
        if self.common.poco_exists(FriendPageLocator.friend_delete_button):
            self.common.poco_click(FriendPageLocator.friend_delete_button)
            sleep(1)
            if self.phone_platform.lower() == 'ios':
                self.poco(name='ScrollView')[-1].offspring(name='删除').click()
            else:
                self.common.poco_click(FriendPageLocator.friend_popup_submit)
            sleep(2)

        if new == '1':
            assert self.common.poco_exists(ChatSetupPageLocator.friend_add_btn)
        else:
            assert not self.common.poco_exists(ChatSetupPageLocator.friend_add_btn)
        self.common.poco_click(ChatSetupPageLocator.menu_back)
        self.common.poco_click(ChatSetupPageLocator.options_back)

