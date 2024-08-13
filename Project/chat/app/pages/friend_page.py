from time import sleep, time

from airtest.core.api import assert_exists, assert_not_exists
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
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
        Android=base.data_collation(type_kind='text', type_name='搜索'),
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

    back_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_back'),
        iOS=base.data_collation(type_kind='type', type_name='Button'),
    )

    add_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_add_user'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconUserAdd'),
    )

    add_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='搜索'),
    )

    add_friend_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='输入帐号ID/手机号进行搜寻'),
        iOS=base.data_collation(type_kind='name', type_name='TextField'),
    )

    add_friend_search = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_search_id'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='搜寻：.*'),
    )

    add_friend_btn = base.check_device(
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
        Android=base.data_collation(type_kind='text', type_name='设定备注'),
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
        iOS=base.data_collation(type_kind='name', type_name='删除'),
    )

    friend_popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='将联络人.*'),
    )

    friend_popup_submit = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='type', type_name='ScrollView', num=1),
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
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_block'),
        iOS=base.data_collation(type_kind='name', type_name='Switch', num=0),
    )

    page_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='name'),
        iOS=base.data_collation(type_kind='name', type_name='好友名单', num=0),
    )
class FriendPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def check_add_friend_btn_display(self):
        assert self.common.poco_exists(FriendPageLocator.add_button), '新增好友鍵未顯示'

    def check_add_to_address_book_non_display(self):
        assert not self.common.poco_exists(FriendPageLocator.add_friend_btn), f"預期不該顯示卻顯示'新增至通訊錄'選項"

    def check_add_to_address_book_display(self):
        assert self.common.poco_exists(FriendPageLocator.add_friend_btn), "預期該顯示但未顯示'新增至通訊錄'選項"

    def return_previous_page(self, count=1):
        for i in range(0, count):
            self.common.poco_click(FriendPageLocator.back_button)

    def search_new_friend(self, name):
        if self.common.poco_exists(FriendPageLocator.search_clear):
            self.common.poco_click(FriendPageLocator.search_clear)

        self.common.poco_click(FriendPageLocator.add_button)

        if self.common.poco_exists(FriendPageLocator.add_friend_input):
            if self.phone_platform.lower() == 'ios':
                self.common.poco_click(FriendPageLocator.add_friend_input)
            self.common.poco_send_text(FriendPageLocator.add_friend_input, name)
            self.common.poco_click(FriendPageLocator.add_friend_search)
        self.wait_loading_finish()

        if self.common.poco_exists(FriendPageLocator.add_friend_btn):
            return True
        else:
            return False

    def search_friend(self, name):
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

    def add_myself(self, number, nation):
        full_number = ''
        if nation == "TW":
            full_number = '886' + str(number)
        elif nation == "CN":
            full_number = '86' + str(number)
        elif nation == "JP":
            full_number = '81' + str(number)
        if self.common.poco_exists(FriendPageLocator.add_button):
            self.common.poco_click(FriendPageLocator.add_button)
            self.wait_loading_finish()
        if self.common.poco_exists(FriendPageLocator.add_friend_input):
            if self.phone_platform.lower() == 'android':
                self.common.poco_send_text(FriendPageLocator.add_friend_input, full_number)
                self.common.poco_click(FriendPageLocator.add_friend_search)
            else:
                self.common.poco_click(FriendPageLocator.add_friend_input)
                self.common.poco_send_text(FriendPageLocator.add_friend_input, 'gubot03')
                self.poco(name='Search').click()
        assert self.common.poco_exists(FriendPageLocator.add_myself_popup), f'未顯示增加自己好友錯誤彈窗'
        self.common.poco_click(FriendPageLocator.add_myself_button)

    def search_clear(self, number):
        self.common.poco_click(FriendPageLocator.add_button)

        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(FriendPageLocator.add_friend_input)
            self.common.poco_send_text(FriendPageLocator.add_friend_input, 'clear')
            self.common.poco_click(FriendPageLocator.search_clear)
            default_text = self.poco(type='StaticText')[1].attr('value')
            assert '我的 IM ID：' in default_text, f'新增好友頁未清空'

        else:
            self.common.poco_send_text(FriendPageLocator.add_friend_input, number)
            assert self.common.poco_exists(FriendPageLocator.add_friend_search), f'未顯示搜查按鍵'
            self.common.poco_click(FriendPageLocator.search_clear)

    def set_note(self, note):
        self.common.poco_click(FriendPageLocator.friend_remark_btn)

        if self.phone_platform.lower() == 'ios':  # ios part
            self.common.poco_click(FriendPageLocator.note_input)
            self.common.poco_send_text(FriendPageLocator.note_input, note)
            # self.poco(name='delete').click()
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

    def set_nickname(self):
        if self.phone_platform.lower() == 'ios':  # ios part
            original_set_nick_name = self.poco(type='StaticText')[1].attr('value')

            # ============================= 更改原暱稱 =============================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_send_text(FriendPageLocator.nickname_input, 'tengyuntech_騰雲科技')
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.poco(type='StaticText')[1].attr('value') == 'tengyuntech_騰雲科技', f'暱稱更換失敗'

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
            self.common.poco_send_text(FriendPageLocator.nickname_input, 'tengyuntech_騰雲科技')
            self.common.poco_click(FriendPageLocator.remark_submit)
            assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == 'tengyuntech_騰雲科技', f'暱稱更換失敗'

            # ============================= 將暱稱刪除, 欄位留空, 使用預設暱稱 ==========================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, '')
            default_nickname = self.common.poco_get_text(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.remark_submit)
            aaa = self.common.poco_get_text(FriendPageLocator.friend_nickname)
            assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == default_nickname, f'暱稱預設失敗'

            # ============================= 將預設暱稱改為原暱稱 =======================================
            self.common.poco_click(FriendPageLocator.friend_remark_btn)
            self.common.poco_send_text(FriendPageLocator.nickname_input, original_nick_name)
            self.common.poco_click(FriendPageLocator.remark_submit)
            if self.common.poco_exists(FriendPageLocator.friend_nickname):
                assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == original_nick_name, f'暱稱更換失敗'

    def add_friend(self):
        original_nickname = self.common.poco_get_text(FriendPageLocator.friend_nickname)
        self.common.poco_click(FriendPageLocator.add_friend_btn)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
        self.common.poco_send_text(FriendPageLocator.nickname_input, 'tengyuntech_騰雲科技')
        self.common.poco_click(FriendPageLocator.add_friend_submit)
        self.wait_loading_finish()
        assert self.common.poco_exists(FriendPageLocator.friend_first_chat), f'新好友沒有出現打招呼選項'
        assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == 'tengyuntech_騰雲科技', f'暱稱更換失敗'

        self.common.poco_click(FriendPageLocator.friend_remark_btn)  # 設定備註

        if self.phone_platform.lower() == 'android':
            while not self.poco(text='全选').exists():
                self.common.poco_long_click(FriendPageLocator.nickname_input)
            self.poco(text='全选').click()
            sleep(1)
            self.poco(text='剪切').click()
        else:
            self.common.poco_click(FriendPageLocator.nickname_input)
            self.common.poco_click(FriendPageLocator.search_clear)
        self.common.poco_click(FriendPageLocator.remark_submit)
        assert self.common.poco_get_text(FriendPageLocator.friend_nickname) == original_nickname, f'暱稱預設失敗'
        self.wait_loading_finish()

        for _ in range(2):
            self.common.poco_click(FriendPageLocator.back_button)

    def delete_friend(self, name):
        self.search_friend(name)
        self.common.poco_click(FriendPageLocator.friend_setting_button)
        self.common.poco_click(FriendPageLocator.friend_delete_button)  # 好友詳情 > 設定 > 刪除

        if self.common.poco_exists(FriendPageLocator.friend_popup_message): # 二次刪除確認框
            if self.phone_platform.lower() == 'ios':
                popup_message = self.common.poco_get_attr(FriendPageLocator.friend_popup_message, 'value')
                assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'

                self.poco(type='Other')[39].child(name='删除').click()
                self.common.poco_click(FriendPageLocator.search_input)
                self.common.poco_click(FriendPageLocator.search_clear)

            else:
                popup_message = self.common.poco_get_text(FriendPageLocator.friend_popup_message)
                assert popup_message == f'将联络人「{name}」删除，同时删除与该联络人的聊天记录', f'刪除彈窗訊息有誤'

                self.common.poco_click(FriendPageLocator.friend_popup_submit)
                self.common.poco_click(FriendPageLocator.search_clear)

        self.search_friend(name)
        assert self.common.poco_exists(FriendPageLocator.search_none_check), f'好友刪除失敗'

    def block_friend(self):
        self.wait_loading_finish()
        self.common.poco_click(FriendPageLocator.friend_setting_button)
        if self.phone_platform.lower() == 'ios':
            self.common.poco_long_click(FriendPageLocator.friend_block_button)
            assert self.poco(name='ScrollView')[0].children()[0].children()[0].children()[0].children()[0].attr(
                'name') == '加入黑名单，你将不再收到对方的讯息，对方也无法查看你。', f'黑名單彈窗訊息有誤'
            self.common.poco_click(FriendPageLocator.friend_popup_submit)
            assert self.poco(type='Switch')[0].attr('value') == '1', f'未成功加入黑名單'

        else:  # android parts
            self.common.poco_click(FriendPageLocator.friend_block_button)
            assert self.common.poco_get_text(
                FriendPageLocator.friend_popup_message) == '加入黑名单，你将不再收到对方的讯息，对方也无法查看你。', f'黑名單彈窗訊息有誤'
            self.common.poco_click(FriendPageLocator.friend_popup_submit)

    def impeach_friend(self):
        self.common.poco_click(FriendPageLocator.friend_impeach_button)
        self.common.poco_click(FriendPageLocator.impeach_radio)
        self.common.poco_click(FriendPageLocator.impeach_agree)

    def add_friend_frist_chat(self):
        self.common.poco_click(FriendPageLocator.add_friend_btn)
        self.common.poco_click(FriendPageLocator.add_friend_submit)
        self.wait_loading_finish()

        if self.common.poco_exists(FriendPageLocator.friend_frist_chat):
            self.common.poco_click(FriendPageLocator.friend_frist_chat)

    def back_to_friends_page(self):
        for _ in range(2):
            self.common.poco_click(FriendPageLocator.back_button)
