from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


class BlackListPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = BlackListPageLocator.base.check_device(
            Android=BlackListPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=BlackListPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    black_seach_input = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='搜索'),
        iOS=base.data_collation(type_kind='type', type_name='TextField'),
    )

    black_nickname = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_name'),
        iOS=base.data_collation(type_kind='name', type_name='test1234', num=-1),
    )

    black_remark_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_set_note_title'),
        iOS=base.data_collation(type_kind='name', type_name='设定备注'),
    )

    black_note_button = base.check_device(
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
    chat_detail_note_content = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_note_content'),
        iOS=base.data_collation(type_kind='', type_name=''),
    )
    search_clear = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='清除文本'),
    )

    search_empty = base.check_device(
        Android=base.data_collation(type_kind='', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='空列表'),
    )

    remark_submit = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成'),
        iOS=base.data_collation(type_kind='name', type_name='完成'),
    )

    remark_back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_start_icon'),
        iOS=base.data_collation(type_kind='type', type_name='Button'),
    )

    setting_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_setting'),
        iOS=base.data_collation(type_kind='name', type_name='iconIconSettings'),
    )

    impeach_radio = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='传送色情讯息'),
        iOS=base.data_collation(type_kind='name', type_name='滥发广告讯息'),
    )

    impeach_agree = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='同意并传送'),
        iOS=base.data_collation(type_kind='name', type_name='同意并传送'),
    )

    impeach_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='检举'),
        iOS=base.data_collation(type_kind='name', type_name='检举'),
    )

    black_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/sw_block'),
        iOS=base.data_collation(type_kind='type', type_name='Switch', num=-1),
    )

    black_hint = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_hint_text'),
        iOS=base.data_collation(type_kind='nameMatches', type_name='已加入黑名单.*'),
    )

    black_popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView'),
    )

    black_popup_submit = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='type', type_name='ScrollView', num=1),
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='n', type_name=''),
        iOS=base.data_collation(type_kind='name', type_name='聊天详情'),
    )

class BlackListPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def into_block_setting(self):
        if self.phone_platform.lower() == 'ios':
            assert self.common.poco_get_attr(BlackListPageLocator.black_hint, 'value') == '已加入黑名单，你将不再收到对方的讯息。', f'黑名單提示文案有誤'
        else:
            assert self.common.poco_get_text(
                BlackListPageLocator.black_hint) == '已加入黑名单，你将不再收到对方的讯息。', f'黑名單提示文案有誤'
        self.common.poco_click(BlackListPageLocator.setting_button)

    def set_note(self, note):
        self.common.poco_click(BlackListPageLocator.black_remark_btn)  # 黑名單成員 > 聊天詳情頁 > 設定備註
        if self.phone_platform.lower() == 'ios':  # ios part
            # ========================= 變更描述 =========================
            self.common.poco_click(BlackListPageLocator.note_input)
            self.common.poco_send_text(BlackListPageLocator.note_input, note)
            self.common.poco_click(BlackListPageLocator.remark_submit)
            assert self.poco(name=f'{note}').exists()  # 確認詳情頁描述出現設定的文字
            # ========================= 刪除描述 =========================
            self.common.poco_click(BlackListPageLocator.black_note_button)
            while not self.poco(name='全选'):
                self.common.poco_long_click(BlackListPageLocator.note_input)
                sleep(1)
            self.poco(name='全选').click()
            self.poco(name='delete').click()
            self.common.poco_click(BlackListPageLocator.remark_submit)
            self.common.poco_click(BlackListPageLocator.black_remark_btn)
            assert self.poco(type='StaticText')[-1].attr('value') == '描述最长至300字', f'描述清空失敗'  # 確認描述預設文字

        else:  # android part
            # ========================= 變更描述 =========================
            self.common.poco_send_text(BlackListPageLocator.note_input, note)
            self.common.poco_click(BlackListPageLocator.remark_submit)
            assert self.common.poco_get_text(BlackListPageLocator.chat_detail_note_content) == note  # 詳情頁描述出現設定文字
            # ========================= 刪除描述 =========================
            self.common.poco_click(BlackListPageLocator.black_note_button)
            self.common.poco_send_text(BlackListPageLocator.note_input, '')
            self.common.poco_click(BlackListPageLocator.remark_submit)
            self.common.poco_click(BlackListPageLocator.black_remark_btn)
            assert self.common.poco_get_text(BlackListPageLocator.note_input) == '描述最长至300字...', f'描述清空失敗'

        self.common.poco_click(BlackListPageLocator.remark_back)  # 回到詳情頁

    def set_nickname(self, name):
        if self.phone_platform.lower() == 'ios':  # ios part
            # ============================= 更改原暱稱 =============================================
            self.common.poco_click(BlackListPageLocator.black_remark_btn)  # 黑名單成員 > 聊天詳情頁 > 設定備註
            self.common.poco_click(BlackListPageLocator.nickname_input)
            self.common.poco_click(BlackListPageLocator.search_clear)
            self.common.poco_send_text(BlackListPageLocator.nickname_input, name)
            self.common.poco_click(BlackListPageLocator.remark_submit)
            after_modified = self.poco(type='StaticText')[1].attr('value')
            assert after_modified == name, f'暱稱更換失敗'
            # ============================= 將暱稱刪除, 欄位留空, 使用預設暱稱 ==========================
            self.common.poco_click(BlackListPageLocator.black_remark_btn)
            self.common.poco_click(BlackListPageLocator.nickname_input)
            self.common.poco_click(BlackListPageLocator.search_clear)
            default_nickname = self.poco(type='TextField').attr('value')
            self.common.poco_click(BlackListPageLocator.remark_submit)
            after_modified = self.poco(type='StaticText')[1].attr('value')
            assert after_modified == default_nickname, f'暱稱預設失敗'

        else:  # android part
            # ============================= 更改原暱稱 =============================================
            self.common.poco_click(BlackListPageLocator.black_remark_btn)
            self.common.poco_send_text(BlackListPageLocator.nickname_input, name)
            self.common.poco_click(BlackListPageLocator.remark_submit)
            assert self.common.poco_get_text(BlackListPageLocator.black_nickname) == name, f'暱稱更換失敗'
            # ============================= 將暱稱刪除, 欄位留空, 使用預設暱稱 ==========================
            self.common.poco_click(BlackListPageLocator.black_remark_btn)
            self.common.poco_send_text(BlackListPageLocator.nickname_input, '')
            default_nickname = self.common.poco_get_text(BlackListPageLocator.nickname_input)
            self.common.poco_click(BlackListPageLocator.remark_submit)
            assert self.common.poco_get_text(BlackListPageLocator.black_nickname) == default_nickname, f'暱稱更換失敗'

    def impeach_friend(self):
        self.common.poco_click(BlackListPageLocator.impeach_button)
        self.common.poco_click(BlackListPageLocator.impeach_radio)
        self.common.poco_click(BlackListPageLocator.impeach_agree)

    def search_friend(self, name):
        if self.phone_platform.lower() == 'ios':
            self.common.poco_click(BlackListPageLocator.black_seach_input)
            self.common.poco_send_text(BlackListPageLocator.black_seach_input, name)
            self.common.sleep(1)
            assert not self.common.poco_exists(BlackListPageLocator.search_empty), f'找不到任何黑名單成員'
            self.common.poco_click(BlackListPageLocator.black_nickname)

        else:
            self.common.poco_send_text(BlackListPageLocator.black_seach_input, name)
            self.common.sleep(1)
            assert self.common.poco_get_text(BlackListPageLocator.black_nickname) == name, f'找不到任何黑名單成員'
            self.common.poco_click(BlackListPageLocator.black_nickname)

    def unblock_friend(self):
        if self.phone_platform.lower() == 'ios':
            self.common.poco_long_click(BlackListPageLocator.black_button)
            if self.common.poco_exists(BlackListPageLocator.black_popup_message):
                print('黑名單初始狀態有誤')

            self.common.poco_long_click(BlackListPageLocator.black_button)
            assert self.common.poco_exists(BlackListPageLocator.black_popup_message),f'未跳出黑名單二次確認彈窗'

            self.common.poco_click(BlackListPageLocator.black_popup_submit)
            assert self.common.poco_get_attr(BlackListPageLocator.black_button, 'value') == '1', f'未成功enable黑名單選項'
            self.common.poco_long_click(BlackListPageLocator.black_button)
            assert self.common.poco_get_attr(BlackListPageLocator.black_button,'value') == '0', f'未成功disable黑名單選項'

        else:
            self.common.poco_click(BlackListPageLocator.black_button)
            if self.common.poco_exists(BlackListPageLocator.black_popup_message):
                print('黑名單初始狀態有誤')

            self.common.poco_click(BlackListPageLocator.black_button)
            assert self.common.poco_exists(BlackListPageLocator.black_popup_message)

            self.common.poco_click(BlackListPageLocator.black_popup_submit)
            self.common.poco_click(BlackListPageLocator.black_button)
