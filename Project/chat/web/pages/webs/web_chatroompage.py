import sys
import pyautogui
import common.utils.globalvar as gl
import win32clipboard
import pyperclip
import os, random, re

from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
from Project.chat.web.pages.webs.web_friendpage import FriendPage, FriendPageLocator
from urllib.parse import urlparse

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)


class ChatRoomPageLocator:
    # --------------- 聊天室標題 詳情 ---------------
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
    detail_close = (By.XPATH, "//div[@class='header-close']/div[1]")
    detail_back = (By.XPATH, "//div[@class='header-back']/div[1]")
    detail_title = (By.XPATH, "(//div[@class='header-title'])[1]")
    detail_submit = (By.XPATH, "//div[@class='header-text']/div[1]")
    detail_edit = (By.XPATH, "//div[@class='header-text']/p[text()='编辑']")
    detail_done = (By.XPATH, "//div[@class='header-text']/p[text()='完成']")
    detail_search = (By.XPATH, "//div[@class='chat-view__item -show']//input[@placeholder='搜索']")
    room_title = (By.XPATH, "//p[@class='chat-detail__name__text']")
    setting_btn = (By.XPATH, "//div[@class='head-icon__img -more']")
    setting_title = (By.XPATH, "//div[@class='chat-setting-modal']//div[@class='header-title']")
    system_message = (By.XPATH, "(//p[@class='wcr-system-message__text'])[last()]")
    chat_room_last_msg = (By.XPATH, "(//div[@class='wcr-list__msg']//span[1])[last()]")
    # -------------------- 會員暱稱 --------------------
    friend_edit_btn = (By.XPATH, "//div[@class='text-edit']")
    friend_edit_text = (By.XPATH, "//p[@class='chat-info__name__text']")
    friend_edit_input = (By.XPATH, "//input[@class='user-name__input']")
    friend_edit_submit = (By.XPATH, "//p[text()='保存']/..")
    # -------------------- 會員備註 --------------------
    friend_remark_btn = (By.XPATH, "//p[@class='remark__text']")
    friend_remark_pen = (By.XPATH, "//p[@class='chat-info__desc__text']/../div[@class='text-edit']")
    friend_remark_text = (By.XPATH, "//p[@class='chat-info__desc__text']")
    friend_remark_hint = (By.XPATH, "//textarea[@placeholder='描述最长至300字']")
    friend_remark_input = (By.XPATH, "//textarea[@class='chat-info__textarea__input']")
    friend_remark_submit = (By.XPATH, "//div[@class='submit-btn__img']/..")
    # -------------------- 會員詳情設定 --------------------
    friend_delete = (By.XPATH, "//p[text()='删除好友']")
    friend_blocks = (By.XPATH, "//label[@for='blocks']")
    friend_notify = (By.XPATH, "//label[@for='notify']")
    # -------------------- 聊天室訊息輸入 --------------------
    message_mask = (By.XPATH, "//div[text()='该用户已被封锁']")
    message_input = (By.XPATH, "//div[@class='enter-message__input']")
    message_submit = (By.XPATH, "//div[@class='prepend__btn btn-send']")
    add_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]')
    chat_room_last_media = (By.XPATH, "(//div[@class='wcr-list__media max-w-half'])[last()]")
    chat_room_media_src = (By.XPATH, "//div[@class='wcr-list__media max-w-half']//div[@class='wcr-list']/@src")
    chat_room_total_media = (By.XPATH, "//div[@class='wcr-list__media max-w-half']")
    chat_room_last_media_is_video = (
        By.XPATH, "(//div[@class='wcr-list__media max-w-half'])//div[@class='wcr-list__media video-container'][last()]")
    # -------------------- 檔案訊息 -------------------------
    chatroom_last_filename = (By.XPATH, "(//div[@class='file-msg__fileName file-msg__fileName--spaced'])[last()]")
    # -------------------- 聊天室訊息操作 --------------------
    message_menu = (By.XPATH, "//div[@class='el-menu -show']")
    message_copy = (By.XPATH, "//p[@class='menu-text' and text() = '复制']")
    message_reply = (By.XPATH, "//p[@class='menu-text' and text() = '回复']")
    message_revoke = (By.XPATH, "//p[@class='menu-text' and text() = '撤回']")
    message_pin = (By.XPATH, "//p[@class='menu-text' and text() = '设为公告']")
    # -------------------- 訊息回覆框 --------------------
    reply_preview_title = (By.XPATH, "//div[@class='chat-detail__footer']//p[@class='reply-item__name__text']")
    reply_preview_text = (By.XPATH, "//div[@class='chat-detail__footer']//p[@class='reply-item__msg__text']")
    reply_file_preview_text = (By.XPATH, "//div[@class='chat-detail__footer']//div[@class='reply-file__text']")
    reply_view_title = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__name__text'])[last()]")
    reply_view_text = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__msg__text'])[last()]")
    reply_file_view_text = (By.XPATH, "(//div[@class='wcr-list__block']//div[@class='reply-file__text'])[last()]")
    reply_msg = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__msg__text'])[last()]")
    # -------------------- 二次確認彈窗 --------------------
    confirm_popup = (By.XPATH, "//div[@class='common-modal']")
    confirm_title = (By.XPATH, "//div[@class='common-modal__header']")
    confirm_text = (By.XPATH, "//p[@class='common-info__text']")
    confirm_submit = (By.XPATH, "//button[@class='btn btn-danger btn-md']")
    confirm_cancel = (By.XPATH, "//button[@class='btn btn-primary btn-md btn-outline']")
    # -------------------- 訊息置頂公告 --------------------
    pin_list = (By.XPATH, "//div[@class='announcement-list']")
    pin_list_show = (By.XPATH, "//div[@class='wcr-system-announcement -show']")
    pin_btn = (By.XPATH, "//div[@class='announcement-toggle']")
    pin_no_show = (By.XPATH, "(//p[@class='announcement-list__no-show'])[1]")
    pin_msg = (By.XPATH, "//p[@class='head-text']")
    pin_first_msg = (By.XPATH, "(//p[@class='head-text'])[1]")
    pin_popup = (By.XPATH, "//div[@class='wcr-system-alert']")
    pin_popup_close = (By.XPATH, "//div[@class='alert__close']")
    # -------------------- 表情符號 --------------------
    emoji_panel = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']")
    emoji_good = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][1]")
    emoji_funny = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][2]")
    emoji_love = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][3]")
    emoji_sad = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][4]")
    emoji_wow = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][5]")
    emoji_view = (By.XPATH, "//div[@class='el-emoji -emoji-view']")
    emoji_list = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']")
    # -------------------- 群組設定 --------------------
    group_name = (By.XPATH, "//p[@class='chat-info__name__text']")
    group_member_count = (By.XPATH, "//p[@class='rough-member-list__text']")
    group_user_add = (By.XPATH, "//div[@class='ui-tableviewcell__icon__img -user-add']")
    group_rule_btn = (By.XPATH, "//p[text()='群组设定']/..//div[contains(@class,'-arrow')]")
    group_rule_name = (By.XPATH, "//p[@class='chat-name__text']")
    group_rule_name_btn = (By.XPATH, "//p[@class='chat-name__text']/..//div[contains(@class,'-pencil')]")
    group_rule_input = (By.XPATH, "//input[@placeholder='填写群组名称']")
    group_rule_submit = (By.XPATH, "//p[text()='保存']/..")
    group_rule_count = (By.XPATH, "//p[text()='群组设定']/..//p[@class='ui-tableviewcell__num']")

    group_rule_text = (By.XPATH, "//label[@for='member-permission-can_send_messages']")  # 傳送訊息
    group_rule_img_gray = (By.XPATH, "//label[contains(@for,'_send_images')]/..//input[(@disabled)]")  # 傳送圖片鈕反灰
    group_rule_img_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_images')]")  # 傳送圖片鈕
    group_rule_video_gray = (By.XPATH, "//label[contains(@for,'_send_videos')]/..//input[(@disabled)]")  # 傳送影片鈕反灰
    group_rule_video_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_videos')]")  # 傳送影片鈕
    group_rule_link_gray = (By.XPATH, "//label[contains(@for,'_send_hyperlink')]/..//input[(@disabled)]")  # 傳送超連結鈕反灰
    group_rule_link_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_hyperlink')]")  # 傳送超連結鈕
    group_rule_file_gray = (By.XPATH, "//label[contains(@for,'_send_file')]/..//input[(@disabled)]")  # 傳送檔案鈕反灰
    group_rule_file_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_file')]")  # 傳送檔案鈕
    group_rule_user = (By.XPATH, "//label[@for='member-permission-can_invite_users']")  # 加入新成員

    group_ = (By.XPATH, "")
    group_admin_btn = (By.XPATH, "//p[text()='管理员']/..//div[contains(@class,'-arrow')]")
    group_admin_add = (By.XPATH, "//p[text()='新增管理员']")
    group_admin_list = (By.XPATH, "//div[@class='chat-member-list__group']")
    group_admin_search = (By.XPATH, "//p[contains(@class,'member-list')]")
    group_admin_remove = (By.XPATH, "//p[text()='gubot01']/../../..//div[@class='chat-member-list__remove']")

    group_block_btn = (By.XPATH, "//p[text()='黑名单']/..//div[contains(@class,'-arrow')]")
    group_block_count = (By.XPATH, "//span[contains(@class,'title__num')]")
    group_block_add = (By.XPATH, "//p[text()='加入黑名单']")
    group_block_text = (By.XPATH, "//div[@class='chat-setting-head'][2]//span")
    group_block_edit = (By.XPATH, "//p[text()='編輯']")
    group_block_list = (By.XPATH, "//div[@class='chat-member-list']//p")
    group_block_remove = (By.XPATH, "//div[@class='chat-member-list__remove']")
    group_block_popup_submit = (By.XPATH, "//button//p[text()='删除']")
    group_block_popup_text = (By.XPATH, "//p[@class='common-info__text']")

    # -------------------- 邀請碼 --------------------
    share_code_share_btn = (By.XPATH, "//p[text()='邀请码']")
    share_code_num = (By.XPATH,
                      "//*[@id='app']/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div/div/p")
    share_code_message_title = (By.XPATH,
                                "//*[@id='app']/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div[1]/div[2]/p")
    share_code_message_close_btn = (By.XPATH,
                                    "//*[@id='app']/div[1]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div[1]/div[1]/div")
    share_code_share_message_body = (By.XPATH,
                                     "//*[@id='app']/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/p/span")
    share_code_share_message_url = (By.XPATH,
                                    "//*[@id='app']/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/p")

    red_envelope = (
        By.XPATH, "(//div[@class='wcr-list__bubble -redEnvelope']/..//p[text()='领取红包'])[last()]")  # 紅包訊息
    envelope_modal_title = (By.XPATH, "//div[@class='modal__dialog']/..//p[@class='header-title__text']")  # 紅包標題
    envelope_modal_close_btn = (By.XPATH, "//div[@class='modal__dialog']/..//div[@class='header-close']")  # 關閉紅包訊息
    envelope_modal_open_btn = (By.XPATH, "//div[@class='modal__dialog']/..//div[@class='grab-action']")  # 紅包領取鍵
    envelope_grab_result_num = (
        By.XPATH, "//div[@class='modal__dialog']/..//p[@class='grab-envelope-result__result-text__num']")  # 領取金額
    system_message_text = (By.XPATH, "(//p[@class='wcr-system-message__text'])[last()]")

    # 特定訊息定位
    @staticmethod
    def message_locator(text, message_type='text'):
        if message_type == 'text':
            locator = (By.XPATH, f"(//span[text()='{text}'])[last()]")
        elif message_type == 'file':
            locator = (By.XPATH, f"(//div[text()='{text}'])[last()]")

        return locator

    # 特定訊息表情符號定位
    @staticmethod
    def message_emoji_locator(text):
        locator = (By.XPATH,
                   f"(//span[text()='{text}']/ancestor-or-self::div[contains(@class,'wcr-list__content')]//div[@class='open-emoji'])[last()]")
        return locator

    # 特定權限開關定位
    @staticmethod
    def switch_locator(num=int):
        locator = (By.XPATH, f"(//label[@class='el-switch-style'])[{num}]")
        return locator

    # 特定管理員刪除定位
    @staticmethod
    def admin_remove_locator(name):
        locator = (By.XPATH, f"//p[text()='{name}']/../../..//div[@class='chat-member-list__remove']")
        return locator

    # 特定管理員定位
    @staticmethod
    def admin_locator(name):
        locator = (By.XPATH, f"//p[@class='chat-member-list__name__text' and text()= '{name}']")
        return locator


class ChatRoomPage(BasePage):
    brand = gl.get_value("BRAND")
    def into_setting(self):
        self.click(ChatRoomPageLocator.setting_btn)
        self.wait_loading_finish()
        assert self.get_text(ChatRoomPageLocator.detail_title).__contains__('详情'), f'進入設定頁面有誤'

    def into_group_rule(self):
        self.wait_loading_finish()
        if self.is_element_finded(ChatRoomPageLocator.group_rule_btn):
            self.click(ChatRoomPageLocator.group_rule_btn)

    def into_group_admin(self):
        self.wait_loading_finish()
        if self.is_element_finded(ChatRoomPageLocator.group_admin_btn):
            self.click(ChatRoomPageLocator.group_admin_btn)

    def into_group_block(self):
        self.wait_loading_finish()
        if self.is_element_finded(ChatRoomPageLocator.group_block_btn):
            self.click(ChatRoomPageLocator.group_block_btn)

    def edit_nickname(self, nickname):
        self.click(ChatRoomPageLocator.friend_edit_btn)
        self.type(ChatRoomPageLocator.friend_edit_input, nickname)
        self.click(ChatRoomPageLocator.friend_edit_submit)
        assert self.get_text(ChatRoomPageLocator.friend_edit_text) == nickname, f'暱稱修改有誤'

    def friend_nickname(self):
        user_name = self.get_text(ChatRoomPageLocator.friend_edit_text)
        name_list = ['testaaaa', user_name]

        for name in name_list:
            self.edit_nickname(name)
            self.click(ChatRoomPageLocator.detail_close)
            self.wait_loading_finish()
            assert self.get_text(
                ChatRoomPageLocator.room_title) == name, f'暱稱修改後沒有同步聊天室名稱'  # 名稱修改後列表名稱還沒去檢查

            self.into_setting()

    def friend_remark(self):
        text_list = ['測試TeSt12345!@#$%测试', '']
        for text in text_list:
            self.edit_remark(text)

            if text == '':
                assert self.is_element_finded(ChatRoomPageLocator.friend_remark_btn) is True
            else:
                assert self.get_text(ChatRoomPageLocator.friend_remark_text) == text, f'備註修改有誤'

    def edit_remark(self, text):
        if self.is_element_finded(ChatRoomPageLocator.friend_remark_btn) is True:
            self.click(ChatRoomPageLocator.friend_remark_btn)
            assert self.is_element_finded(ChatRoomPageLocator.friend_remark_hint) is True, f'輸入提示文案有誤'
        else:
            self.click(ChatRoomPageLocator.friend_remark_pen)

        self.type_delete(ChatRoomPageLocator.friend_remark_input)
        self.type(ChatRoomPageLocator.friend_remark_input, text)
        self.click(ChatRoomPageLocator.friend_remark_submit)

    def friend_block(self):
        self.click(ChatRoomPageLocator.friend_blocks)
        self.click(ChatRoomPageLocator.detail_close)
        self.sleep(1)
        assert self.is_element_finded(ChatRoomPageLocator.message_mask) is True, f'文字輸入匡沒有被封鎖'

    def friend_delete(self):
        self.click(ChatRoomPageLocator.friend_delete)
        sleep(1)
        if self.is_element_finded(ChatRoomPageLocator.confirm_popup) is True:
            assert self.get_text(ChatRoomPageLocator.confirm_text).__contains__(
                '同时删除与该联络人的聊天纪录。'), f'刪除好友彈窗標題有誤'
            self.click(ChatRoomPageLocator.confirm_submit)

    def send_message(self, message):
        if self.is_element_finded(ChatRoomPageLocator.message_input) is True:
            self.click(ChatRoomPageLocator.message_input)
            self.type(ChatRoomPageLocator.message_input, message)

        if self.is_element_finded(ChatRoomPageLocator.message_submit) is True:
            self.click(ChatRoomPageLocator.message_submit)

    def send_text_message(self):
        messages = '測試TeSt12345!@#$%测试'
        num = 0
        for _ in range(0, 6):
            text = str(messages) + '#' + str(num)
            self.send_message(text)
            self.sleep(0.5)
            num = num + 1

    def send_media(self, media_type=''):
        clip_path = ''
        random_file = ''
        if media_type == 'photo':
            clip_path = DIR_NAME + '\\test_medias\\360x360.png'
        elif media_type == 'video':
            clip_path = DIR_NAME + '\\test_medias\\ForBiggerMeltdowns.mp4'
        elif media_type == 'file':
            file_folder_path = f'{DIR_NAME}\\test_medias\\file_sample'
            files = [f for f in os.listdir(file_folder_path) if os.path.isfile(os.path.join(file_folder_path, f))]
            random_file = random.choice(files)
            clip_path = f'{DIR_NAME}\\test_medias\\file_sample\\{random_file}'

        self.wait_loading_finish()
        self.click(ChatRoomPageLocator.add_btn)
        sleep(1)
        self.copy_to_clipboard(clip_path)
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        if media_type == 'photo':
            while True:
                if self.get_last_media_src_link().find('http') == 0:
                    break
                else:
                    sleep(1)
                    continue
        elif media_type == 'video':
            while True:
                if self.get_last_media_src_link('video').find('https://') == 0:
                    break
                else:
                    sleep(1)
                    continue
        elif media_type == 'file':
            sleep(5)
            actual_chatroom_filename = self.get_text(ChatRoomPageLocator.chatroom_last_filename)
            assert actual_chatroom_filename == random_file, f'檔案名稱錯誤, 預期:{random_file},實際:{actual_chatroom_filename}'
            return random_file


    def copy_to_clipboard(self, text, retry=50, delay=2):
        for attempt in range(retry):
            try:
                win32clipboard.OpenClipboard()
                try:
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardText(text)
                    return
                finally:
                    win32clipboard.CloseClipboard()
            except OSError as e:
                sleep(delay)
        raise Exception('無法複製路徑')

    def get_last_media_src_link(self, media_type='img'):
        from selenium.webdriver.common.by import By
        sleep(5)
        total_elements = self.find_elements(ChatRoomPageLocator.chat_room_total_media)
        src_value = total_elements[-1].find_element(By.TAG_NAME, media_type).get_attribute("src")
        return src_value

    def get_random_medias_filename_from_target_folder(self, selected_num, target_folder_path):
        """
        獲取資料夾下隨機選取selected_num個的檔案的檔名(含副檔名), 檔名前後以雙引號tag, 檔名間以空格隔開, 組合輸出成一新字串
        """
        all_medias = os.listdir(target_folder_path)
        selected_medias = random.sample(all_medias, selected_num)
        selected_with_quotes = [f'"{file}"' for file in selected_medias]
        return ' '.join(selected_with_quotes)

    def random_send_medias_to_chatroom(self, select_num_each_time, target_folder_path):
        """
        從指定資料夾下選擇media並傳送到聊天室
        """
        self.click(ChatRoomPageLocator.add_btn)  # 點擊輸入框旁"+"鍵
        source_path_column = (900, 60)
        pyautogui.moveTo(source_path_column[0], source_path_column[1], duration=0.5)  # 滑鼠移動到視窗上方開啟路徑位置
        pyautogui.click()
        pyperclip.copy(target_folder_path)  # copy source路徑
        pyautogui.hotkey('ctrl', 'v')  # 貼上路徑
        pyautogui.press('enter')
        file_name_column = (900, 610)
        pyautogui.moveTo(file_name_column[0], file_name_column[1], duration=0.5)  # 滑鼠移動到視窗下方檔案名稱輸入欄位
        pyperclip.copy(self.get_random_medias_filename_from_target_folder(select_num_each_time, target_folder_path))
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        open_button_position = (1070, 640)
        pyautogui.moveTo(open_button_position[0], open_button_position[1], duration=0.5)  # 滑鼠移動到視窗下方"開啟"鍵
        pyautogui.click()

    def send_url_message(self):
        # google_news_url = 'https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
        messages_url = ['https://gu-chat.com',]

        for message in messages_url:
            # message_url = 'https://' + message + '/'
            self.send_message(message)
            self.check_url_message(message)

    def check_url_message(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(message)) is True:
            self.click(ChatRoomPageLocator.message_locator(message))

        self.switch_last_page()
        self.sleep(3)
        current_url = self.get_url()
        currentURL_domain = urlparse(current_url).netloc
        message_domain = urlparse(message).netloc
        assert currentURL_domain == message_domain, f'超連結訊息網頁開啟有誤'


        # if self.brand == 'gu':
        #     assert current_url.__contains__('gu-chat'), f'股聊超連結開啟有誤'
        # elif self.brand == 'meechat':
        #     assert current_url.__contains__('meechattop'), f'覓聊超連結開啟有誤'
        # elif self.brand == 'mingpin':
        #     assert current_url.__contains__('mingpin-vip'), f'名品會超連結開啟有誤, 實際:{current_url}'
        # elif self.brand == 'chitchat':
        #     assert current_url.__contains__('chitchatswebs'), f'趣聊超連結開啟有誤'
        # else:
        #     return False, f'超連結開啟有誤'

        # if message.__contains__('gu'):
        #     assert current_url.__contains__('gu-chat'), f'股聊超連結開啟有誤'
        # elif message.__contains__('meechat'):
        #     assert current_url.__contains__('meechattop'), f'覓聊超連結開啟有誤'
        # elif message.__contains__('chitchat'):
        #     assert current_url.__contains__('chitchatswebs'), f'趣聊超連結開啟有誤'
        # elif
        #     https: // mingpin - vip.com
        # else:
        #     assert current_url.__contains__(message), f'超連結開啟有誤'

        self.close_browser()
        self.switch_last_page()
        self.sleep(1)

    def message_copy(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(message)) is True:
            self.context_click(ChatRoomPageLocator.message_locator(message))
            self.click(ChatRoomPageLocator.message_copy)

        self.click(ChatRoomPageLocator.message_input)
        self.type_paste(ChatRoomPageLocator.message_input)

        self.wait_visibility(ChatRoomPageLocator.message_submit)
        self.click(ChatRoomPageLocator.message_submit)

    def message_reply(self, message, message_type='text'):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator().message_locator(message, message_type)) is True:
            self.context_click(ChatRoomPageLocator.message_locator(message, message_type))
            self.click(ChatRoomPageLocator.message_reply)

        reply_pre_title = self.get_text(ChatRoomPageLocator.reply_preview_title)

        reply_pre_msg = ''
        if message_type == 'text':
            reply_pre_msg = self.get_text(ChatRoomPageLocator.reply_preview_text)
        elif message_type == 'file':
            reply_pre_msg = self.get_text(ChatRoomPageLocator.reply_file_preview_text)

        assert reply_pre_title.__contains__('回复'), f'訊息回覆預覽標題有誤'
        assert reply_pre_msg == message, f'回覆訊息預覽有誤'

        self.click(ChatRoomPageLocator.message_input)
        self.type(ChatRoomPageLocator.message_input, '回覆訊息測試Test')

        if self.is_element_finded(ChatRoomPageLocator.message_submit) is True:
            self.click(ChatRoomPageLocator.message_submit)

        self.sleep(0.5)
        reply_title = self.get_text(ChatRoomPageLocator.reply_view_title)
        reply_msg = ''
        if message_type == 'text':
            reply_msg = self.get_text(ChatRoomPageLocator.reply_view_text)
        elif message_type == 'file':
            reply_msg = self.get_text(ChatRoomPageLocator.reply_file_view_text)

        assert reply_pre_title.__contains__(reply_title), f'訊息回覆標題有誤'
        assert reply_msg == message, f'回覆訊息預覽有誤 發送訊息顯示: {message} 回復訊息顯示 {reply_msg}'

    def check_reply_disappear(self, message):
        self.wait_message_finish()

        if self.get_text(ChatRoomPageLocator.chat_room_last_msg) == message:
            assert self.get_text(ChatRoomPageLocator.reply_msg) == '原始讯息已不存在', f'訊息遺失錯誤提示有誤'

    def message_revoke(self, message, message_type='text'):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(message, message_type)) is True:
            self.context_click(ChatRoomPageLocator.message_locator(message, message_type))

        self.click(ChatRoomPageLocator.message_revoke)

        if self.is_element_finded(ChatRoomPageLocator.confirm_popup) is True:
            assert self.get_text(ChatRoomPageLocator.confirm_title) == '撤回讯息', f'撤回訊息彈窗標題有誤'
            self.click(ChatRoomPageLocator.confirm_submit)

            self.wait_loading_finish()
            if self.get_text(ChatRoomPageLocator.system_message).__contains__('设定一笔讯息为公告'):
                if self.is_element_finded(ChatRoomPageLocator.pin_list_show) is False:
                    self.click(ChatRoomPageLocator.pin_btn)
                pin_list = self.get_pin_message()
                assert message not in pin_list, f'訊息撤回後，公告沒有消失'
            else:
                assert self.get_text(ChatRoomPageLocator.system_message).__contains__(
                    '你已撤收一则讯息'), f'撤回訊息系統訊息有誤'

    def delete_all_pin(self):
        while self.is_element_finded(ChatRoomPageLocator.pin_list):
            if self.is_element_finded(ChatRoomPageLocator.pin_list_show) is False:
                self.click(ChatRoomPageLocator.pin_btn)

            if self.is_element_finded(ChatRoomPageLocator.pin_no_show) is True:
                before_message = self.get_text(ChatRoomPageLocator.pin_first_msg)
                self.click(ChatRoomPageLocator.pin_no_show)
                self.sleep(1)

                if self.is_element_finded(ChatRoomPageLocator.pin_list_show) is True:
                    after_message = self.get_text(ChatRoomPageLocator.pin_first_msg)
                    assert before_message != after_message, f'公告取消失敗'
                else:
                    break
            else:
                print('角色權限不足')
                break

    def message_pin(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(message)) is True:
            self.context_click(ChatRoomPageLocator.message_locator(message))
            sleep(2)
            if self.is_element_finded(ChatRoomPageLocator.message_menu) is True:
                self.click(ChatRoomPageLocator.message_pin)

        if self.is_element_finded(ChatRoomPageLocator.pin_popup) is True:
            assert self.get_text(
                ChatRoomPageLocator.pin_popup) == '公告已满5则，无法新增，请取消欲替换的公告', f'彈窗訊息有誤'
            self.click(ChatRoomPageLocator.pin_popup_close)
            return False
        else:
            self.sleep(1)
            pin_first = self.get_text(ChatRoomPageLocator.pin_first_msg)
            assert pin_first == message, f'公告顯示有誤'
            assert self.get_text(ChatRoomPageLocator.system_message).__contains__(
                '设定一笔讯息为公告'), f'設定置頂公告系統訊息有誤'
            return True

    def pin_full_messages(self):
        message = '測試TeSt12345!@#$%测试#'
        pin_sort = [2, 0, 1, 3, 4, 5]

        times = 1
        expected_list = []
        for number in pin_sort:
            text = message + str(number)
            if times < 6:
                assert self.message_pin(text) is True
                expected_list.append(text)
            else:
                assert self.message_pin(text) is False
                break
            times = times + 1

        if self.is_element_finded(ChatRoomPageLocator.pin_list_show) is False:
            self.click(ChatRoomPageLocator.pin_btn)
        Reality_list = self.get_pin_message()
        Reality_list.reverse()

        assert Reality_list == expected_list, f'公告排序有誤'
        self.click(ChatRoomPageLocator.pin_btn)

    def get_pin_message(self):
        message_num = []
        for message in self.find_elements(ChatRoomPageLocator.pin_msg):
            message_num.append(message.text)

        return message_num

    def add_message_emoji(self, message):
        self.wait_message_finish()

        if self.is_element_finded(ChatRoomPageLocator.message_locator(message)):
            self.click(ChatRoomPageLocator.message_emoji_locator(message))

            assert self.is_element_finded(ChatRoomPageLocator.emoji_panel)

        self.click(ChatRoomPageLocator.emoji_wow)

    def change_group_name(self, name_old, name_new):
        self.wait_loading_finish()

        assert name_old == self.get_text(ChatRoomPageLocator.group_name), f'群組聊天 名稱顯示有誤'

        self.into_group_rule()
        if self.is_element_finded(ChatRoomPageLocator.group_rule_name) is True:
            assert name_old == self.get_text(ChatRoomPageLocator.group_rule_name), f'群組設定 名稱顯示有誤'

            self.click(ChatRoomPageLocator.group_rule_name_btn)
            self.type(ChatRoomPageLocator.group_rule_input, name_new)
            self.click(ChatRoomPageLocator.group_rule_submit)

            assert name_new == self.get_text(ChatRoomPageLocator.group_rule_name), f'群組設定 名稱修改後同步有誤'

            self.click(ChatRoomPageLocator.detail_back)
            assert name_new == self.get_text(ChatRoomPageLocator.group_name), f'群組聊天 名稱顯示有誤'

            self.click(ChatRoomPageLocator.detail_close)
            assert name_new == self.get_text(ChatRoomPageLocator.room_title), f'群組聊天室 名稱顯示有誤'

            system = self.get_text(ChatRoomPageLocator.system_message)
            msg_list = system.replace('「', ' ').replace('」', '').split(' ')
            assert msg_list[2] == name_new, f'聊天室系統訊息 名稱顯示有誤'

    def all_group_rule(self):
        for _ in range(0, 3):
            self.wait_loading_finish()

            rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
            num = rule_count.split('/')

            if int(num[0]) < 6:
                self.into_group_rule()
                self.sleep(1)
                # group_rule = [傳送訊息, 傳送圖片, 傳送影片, 傳送超連結, 傳送檔案, 加入新成員]
                if num[0] == '0':

                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_img)
                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_video)
                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_file)
                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_link)
                    self.click(ChatRoomPageLocator.group_rule_text)
                    self.click(ChatRoomPageLocator.group_rule_user)

                    self.sleep(1)
                    if self.is_element_finded(ChatRoomPageLocator.group_rule_img) \
                            and self.is_element_finded(ChatRoomPageLocator.group_rule_link) is True:

                        self.click(ChatRoomPageLocator.group_rule_img_btn)
                        self.click(ChatRoomPageLocator.group_rule_link_btn)

                    else:
                        print('群組權限 圖片及連結沒有連動防呆')
                    self.click(ChatRoomPageLocator.detail_back)

                elif num[0] == '1':
                    if self.is_element_finded(ChatRoomPageLocator.group_rule_img) is True:
                        self.click(ChatRoomPageLocator.group_rule_img_btn)
                        self.click(ChatRoomPageLocator.group_rule_link_btn)
                        self.click(ChatRoomPageLocator.group_rule_user)
                    else:
                        self.click(ChatRoomPageLocator.group_rule_text)

                        if self.is_element_finded(ChatRoomPageLocator.group_rule_img) and self.is_element_finded(
                                ChatRoomPageLocator.group_rule_link) is True:
                            self.click(ChatRoomPageLocator.group_rule_img_btn)
                            self.click(ChatRoomPageLocator.group_rule_link_btn)
                    self.click(ChatRoomPageLocator.detail_back)

                else:
                    self.click(ChatRoomPageLocator.group_rule_text)
                    self.click(ChatRoomPageLocator.detail_back)
            else:
                break

    def change_group_rule(self, data):
        data_list = list(data)
        original_rule_sum = 0
        for num in data_list:
            original_rule_sum += int(num)  # total群組設定數

        self.all_group_rule_close()
        self.wait_loading_finish()

        self.into_group_rule()
        self.sleep(1)

        if data_list[5] == '1':  # 加入新成員
            self.click(ChatRoomPageLocator.group_rule_user)

        if data_list[0] == '1':  # 傳送訊息
            self.click(ChatRoomPageLocator.group_rule_text)
            self.sleep(1)
            if data_list[1] == '1':  # 傳送圖片
                self.click(ChatRoomPageLocator.group_rule_img_btn)
                self.sleep(1)
            if data_list[2] == '1':  # 傳送影片
                self.click(ChatRoomPageLocator.group_rule_video_btn)
                self.sleep(1)
            if data_list[3] == '1':  # 傳送超連結
                self.click(ChatRoomPageLocator.group_rule_link_btn)
                self.sleep(1)
            if data_list[4] == '1':  # 傳送檔案
                self.click(ChatRoomPageLocator.group_rule_file_btn)
                self.sleep(1)
        else:
            assert self.is_element_finded(ChatRoomPageLocator.group_rule_img_gray), f'群組權限 圖片按鈕 沒有自動disable'
            assert self.is_element_finded(ChatRoomPageLocator.group_rule_video_gray), f'群組權限 影片按鈕 沒有自動disable'
            assert self.is_element_finded(ChatRoomPageLocator.group_rule_file_gray), f'群組權限 檔案按鈕 沒有自動disable'
            assert self.is_element_finded(ChatRoomPageLocator.group_rule_link_gray), f'群組權限 超連結按鈕 沒有自動disable'

            if data_list[1] == '1' or data_list[2] == '1' or data_list[3] == '1' or data_list[4] == '1':
                print('訊息發送權限沒有開啟, 無法開啟[傳圖][傳影片][傳超連結][傳檔案]權限')

        self.click(ChatRoomPageLocator.detail_back)
        after_rule_text = self.get_text(ChatRoomPageLocator.group_rule_count)
        after_rule_count = after_rule_text.split('/')
        assert str(original_rule_sum) == after_rule_count[0], f'設定權限後群組設定數字有誤'

        # ===============================================================
        # sum_data = 0
        # data_list = list(data)
        # for num in data_list:
        #     sum_data += int(num)
        #
        # self.wait_loading_finish()
        # if sum_data < 6:
        #     self.into_group_rule()
        #
        #     self.sleep(1)
        #     if data_list[5] == '1':  # 加入新成員
        #         self.click(ChatRoomPageLocator.group_rule_user)
        #
        #     if data_list[0] == '1':  # 傳送訊息
        #         self.click(ChatRoomPageLocator.group_rule_text)
        #         self.sleep(1)
        #
        #         if data_list[1] == '1':  # 傳送圖片
        #             self.click(ChatRoomPageLocator.group_rule_img_btn)
        #             self.sleep(1)
        #         if data_list[2] == '1':  # 傳送影片
        #             self.click(ChatRoomPageLocator.group_rule_video_btn)
        #             self.sleep(1)
        #         if data_list[3] == '1':  # 傳送超連結
        #             self.click(ChatRoomPageLocator.group_rule_link_btn)
        #             self.sleep(1)
        #         if data_list[4] == '1':  # 傳送檔案
        #             self.click(ChatRoomPageLocator.group_rule_file_btn)
        #             self.sleep(1)
        #     else:
        #         assert not self.is_element_finded(ChatRoomPageLocator.group_rule_img), f'群組權限 圖片按鈕 沒有自動disable'
        #         assert not self.is_element_finded(ChatRoomPageLocator.group_rule_video), f'群組權限 影片按鈕 沒有自動disable'
        #         assert not self.is_element_finded(ChatRoomPageLocator.group_rule_file), f'群組權限 檔案按鈕 沒有自動disable'
        #         assert not self.is_element_finded(ChatRoomPageLocator.group_rule_link), f'群組權限 超連結按鈕 沒有自動disable'
        #
        #         if data_list[1] == '1' or data_list[2] == '1' or data_list[3] == '1' or data_list[4] == '1':
        #             sum_data -= 1
        #             print('訊息發送權限沒有開啟, 無法開啟[傳圖][傳影片][傳超連結][傳檔案]權限')
        #
        #     self.click(ChatRoomPageLocator.detail_back)
        #     rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
        #     num = rule_count.split('/')
        #     assert str(sum_data) == num[0], f'開啟群組設定 權限有誤'
        # else:
        #     self.all_group_rule()

    def all_group_rule_close(self):

        for _ in range(0, 3):
            self.wait_loading_finish()

            rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
            num = rule_count.split('/')

            if int(num[0]) != 0:  # 有權限未關
                self.into_group_rule()
                self.sleep(1)

                if self.is_element_finded(ChatRoomPageLocator.group_rule_img_gray):
                    # 有權限未關 + 傳圖權限反灰(傳訊息disable) = 加入新成員enable
                    self.click(ChatRoomPageLocator.group_rule_user)
                else:
                    # 有權限未關 + 傳圖權限未反灰 >>> 先關傳訊息鍵
                    self.click(ChatRoomPageLocator.group_rule_text)



                # if int(num[0]) < 4:
                #     if self.is_element_finded(ChatRoomPageLocator.group_rule_img) is True:
                #         self.click(ChatRoomPageLocator.group_rule_text)
                #     else:
                #         self.click(ChatRoomPageLocator.group_rule_user)
                # else:
                #     self.click(ChatRoomPageLocator.group_rule_text)
                #     self.click(ChatRoomPageLocator.group_rule_user)
                #
                self.click(ChatRoomPageLocator.detail_back)
            else:
                break

    def check_admin_list(self, owner):
        self.wait_loading_finish()

        admin_list = []
        for admin in self.find_elements(ChatRoomPageLocator.group_admin_list):
            admin_list.append(admin.text)

        assert admin_list[0].replace('\n', '') == str(
            owner) + '拥有者', f'擁有者顯示有誤應該為 {owner} 顯示為{admin_list[0]}'

        pattern = r'([\u4e00-\u9fa5]+|[a-zA-Z0-9]+)'

        admin_id = []
        for admin_account in admin_list:
            matches = re.findall(pattern, admin_account)
            admin_id.append(matches[0])

            assert matches[1] == '拥有者' or matches[1] == '管理员', f'群組管理員名稱有誤'

        return admin_id

    def add_admin(self, name, owner):
        self.wait_loading_finish()
        self.into_group_admin()

        admin_old = self.check_admin_list(owner)
        if name in admin_old:
            print(f'會員{name}已成為管理員')
        else:
            self.click(ChatRoomPageLocator.group_admin_add)

            if self.is_element_finded(ChatRoomPageLocator.detail_search):
                self.type(ChatRoomPageLocator.detail_search, name)

            self.wait_loading_finish()

            if self.is_element_finded(ChatRoomPageLocator.group_admin_search):
                assert self.get_text(ChatRoomPageLocator.group_admin_search) == name, f'搜尋結果顯示有誤'

                self.click(ChatRoomPageLocator.group_admin_search)
                assert self.get_text(ChatRoomPageLocator.detail_title) == '新增 管理员设定', f'進入權限設定頁面有誤'

                self.click(ChatRoomPageLocator.detail_done)

            else:
                print(f'搜尋無結果 成員{name}沒有加入該群組內')

            self.click(ChatRoomPageLocator.detail_back)

    def change_admin_rule(self, name, situation_rule, expect_rule):
        self.wait_loading_finish()
        situation_list = list(situation_rule)
        expect_list = list(expect_rule)

        # 遍歷兩個陣列，比較相應位置的值是否相等
        diff_rule = []
        for rule, (x, y) in enumerate(zip(situation_list, expect_list)):
            if x != y:
                diff_rule.append(rule)

        if self.is_element_finded(ChatRoomPageLocator.admin_locator(name)):
            self.click(ChatRoomPageLocator.admin_locator(name))

        self.sleep(1)
        for num in diff_rule:
            num += 1
            self.click(ChatRoomPageLocator.switch_locator(num))
            self.sleep(0.5)

        self.click(ChatRoomPageLocator.detail_done)

    def delete_admin(self, account, owner):
        self.wait_loading_finish()
        if self.get_text(ChatRoomPageLocator.detail_title) == "群聊详情":
            self.click(ChatRoomPageLocator.group_admin_btn)

        if self.get_text(ChatRoomPageLocator.detail_edit) == '编辑':

            if account in self.check_admin_list(owner):
                self.click(ChatRoomPageLocator.detail_edit)
                self.sleep(0.5)
                self.click(ChatRoomPageLocator.admin_remove_locator(account))
                self.sleep(0.5)
                confirm_list = []
                for i in self.find_elements(ChatRoomPageLocator.confirm_text):
                    confirm_list.append(i.text)

                confirm_text = ''.join(confirm_list)
                assert confirm_text == '要把 %s 移除管理员吗?\\n移除管理员后，将无管理员权限' % account, f'二次彈窗文案有誤'
                self.sleep(0.5)
                self.click(ChatRoomPageLocator.confirm_submit)
                self.sleep(0.5)

                admin_list = self.check_admin_list(owner)
                assert account not in admin_list, f'管理員刪除失敗 {account} 還在列表中'

        else:
            print('此帳號並非 擁有者無法編輯 管理員權限')

    def remove_block(self, name):
        self.wait_loading_finish()

        if self.is_element_finded(ChatRoomPageLocator.group_block_btn) is True:
            self.click(ChatRoomPageLocator.group_block_btn)

    def add_block(self, name):
        self.wait_loading_finish()

        if self.is_element_finded(ChatRoomPageLocator.group_block_btn) is True:
            self.click(ChatRoomPageLocator.group_block_btn)

    def check_member_block(self, name):
        self.wait_loading_finish()

        block_list = []
        for block in self.find_elements(ChatRoomPageLocator.group_block_list):
            block_list.append(block.text)

        if name in block_list:
            return False
        else:
            return True

    def grab_red_envelope(self, grab_type):
        self.click(ChatRoomPageLocator.red_envelope)
        assert self.get_text(ChatRoomPageLocator.envelope_modal_title) == grab_type, f'紅包類型錯誤, 預期{grab_type}, 實際{self.get_text(ChatRoomPageLocator.envelope_modal_title)}'
        self.click(ChatRoomPageLocator.envelope_modal_open_btn)
        grab_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        grab_amount = self.get_text(ChatRoomPageLocator.envelope_grab_result_num)
        self.click(ChatRoomPageLocator.envelope_modal_close_btn)
        return grab_time, grab_amount

    def check_chatroom_system_message(self, grab_account, grab_amount):
        message = self.get_text(ChatRoomPageLocator.system_message_text)
        if grab_account is not None and grab_amount is not None:
            assert message == f'{grab_account} 领取了红包 {grab_amount}', f'聊天室訊息顯示錯誤'
        else:
            name = message.split()[0]
            amount = message.split()[-1]
            return name, amount

    def check_share_code_visible_when_permission_changed(self, share_code, group_name, account, permission=1):
        self.click(FriendPageLocator.friends_tab)
        self.type(FriendPageLocator.search_input, group_name)
        self.click(FriendPageLocator.search_name)
        self.click(ChatRoomPageLocator.setting_btn)
        self.wait_loading_finish()
        if permission == 1 or (permission == 3 and account == 'gubot03'):  # 當權限設定為一般成員 或 設為管理員且登入管理員gubot03帳號
            assert self.is_element_finded(ChatRoomPageLocator.share_code_share_btn)
            assert self.get_text(ChatRoomPageLocator.share_code_num) == share_code
            self.click(ChatRoomPageLocator.share_code_share_btn)
            self.wait_loading_finish()
            assert self.get_text(ChatRoomPageLocator.share_code_message_title) == "分享"
            assert self.get_text(ChatRoomPageLocator.share_code_share_message_body).__contains__(
                f'输入邀请码「{share_code}」')
            assert self.get_text(ChatRoomPageLocator.share_code_share_message_url).__contains__(f'g={share_code}')
            self.click(ChatRoomPageLocator.share_code_message_close_btn)
        else:
            assert not self.is_element_finded(ChatRoomPageLocator.share_code_share_btn)  # 看不到邀請碼欄位
        self.click(ChatRoomPageLocator.detail_close)
