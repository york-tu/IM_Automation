import os
import random
import sys
from time import sleep

import pyautogui
import win32clipboard
from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
import common.utils.globalvar as gl
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)

class MessagePageLocator:
    # ============================= 導航欄 ==============================================================================
    message_button = (By.XPATH, "//a[@href='/chat']")  # 導航欄-信息

    # ============================= 聊天列表頁 ===========================================================================
    header_title = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div')  # 頁面標題
    search_input = (By.XPATH, '//input[@placeholder="搜索"]')  # 搜尋欄位
    # first_chatroom = (By.XPATH, '(//div[@class="flex items-center w-full overflow-hidden text-[16rem] font-medium black-text"])[1]')  # 搜尋結果第一則聊天室

    # ============================= 聊天室 ==============================================================================
    chatroom_title = (By.XPATH, '//div[@class="truncate"]')
    input_message = (By.XPATH, '//div[@placeholder="输入讯息..."]')  # 訊息輸入框

    send_btn = (By.XPATH, '//div[@class="btn-send w-[24rem] h-[24rem]"]')  # 發送btn
    chatroom_latest_message = (By.XPATH, '(//div[@class="flex flex-col relative min-w-0"])[last()]')  # 聊天室內最新一則訊息
    back_btn = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/svg')  # 返回鍵
    chat_list_chatroom_last_message = (By.XPATH, '//div[@class="flex items-center w-full mt-[4rem]"]')  # 聊天列表聊天室最後一則訊息
    system_message = (By.XPATH, "(//div[@class='text-[12rem] font-medium text-grand-2 text-center mx-auto bg-neutral-900 rounded-full px-[12rem] py-[3rem] break-all w-fit mt-[8rem]'])[last()]")
    # ------------------------ 語音訊息 ----------------------------
    add_function_btn = (By.XPATH, '//div[@class="w-[40rem] h-[40rem] btn-add"]')  # 新增鍵
    mic_btn = (By.XPATH, "//div[text()='语音']")  # 錄音鍵
    popup_title = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[1]/div[1]')  # 語音介面標題
    record_voice_btn = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div')  # 語音介面-開始錄音
    close_btn = (By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[2]')  # 語音介面-關閉鍵
    chatroom_latest_voice_message = (By.XPATH, '(//div[@class="time-display"])[last()]')  # 聊天室最新一筆語音訊息
    # ------------------------ 檔案訊息 ----------------------------
    file_btn = (By.XPATH, "//div[text()='档案']")  # 檔案鍵
    send_confirm_content = (By.XPATH, "//div[@class='w-full py-[14px] text-[13px] text-center text-[#8f8f8f]']")  #傳送檔案確認彈窗文字
    send_confirm_submit = (By.XPATH, "//button[text()='传送']")  # 確認傳送
    chatroom_last_filename = (By.XPATH, "(//div[@class='text-[14px] font-semibold text-grand-1 leading-[20px] mb-[4px]'])[last()]")  #聊天室內最新一則檔案訊息名稱
    reply_file_text = (By.XPATH, "(//div[@class='text-[12px]'])[last()]")  # 聊天室內最後一則檔案訊息的回覆框"原檔案訊息名稱"
    # ============================= 社群化分享文 =========================================================================
    chat_share_author_name = (By.XPATH, "(//div[@class='min-w-0 flex-1 truncate font-semibold text-white-100'])[last()]")  # 最新一則個人頁分享文作者
    chat_share_post_author_name = (By.XPATH, "(//p[@class='overflow-hidden text-ellipsis whitespace-nowrap text-[12rem] text-white-100'])[last()]")  # 最新一則個人頁分享文作者
    chat_share_post_1 = (By.XPATH, "(//div[@class='flex-1 flex items-center w-[70rem] justify-center bg-slate-200'])[1]")  # 個人頁分享文第一則貼文縮圖
    chat_share_post_2 = (By.XPATH, "(//div[@class='flex-1 flex items-center w-[70rem] justify-center bg-slate-200'])[2]")  # 個人頁分享文第一則貼文縮圖
    chat_share_post_3 = (By.XPATH, "(//div[@class='flex-1 flex items-center w-[70rem] justify-center bg-slate-200'])[3]")  # 個人頁分享文第一則貼文縮圖
    chat_share_post_thumbnail = (By.XPATH, "(//div[@class='max-w-[80%] flex flex-col rounded-[4rem] overflow-hidden'])[last()]")  # 貼文分享文縮圖
    chat_share_self_page_message = (By.XPATH, "(//div[@class='py-[8rem] px-[12rem] text-[16rem] text-grand-1 break-all whitespace-pre-wrap'])[last()]")  # 個人頁分享文留言
    chat_share_post_message = (By.XPATH, "(//p[@class='text-[16rem] text-grand-1 whitespace-pre-wrap break-all px-[10rem] py-[12rem]'])[last()]")  # 貼文分享文留言
    # ============================= 右鍵選單 ============================================================================
    message_menu = (By.XPATH, "//div[@class='flex flex-col w-full rounded-[4rem] overflow-x-hidden menu-list']")
    menu_copy = (By.XPATH, "//p[text() = '复制']")
    menu_reply = (By.XPATH, "//p[text() = '回复']")
    menu_revoke = (By.XPATH, "//p[text() = '撤回']")
    menu_delete = (By.XPATH, "//p[text() = '刪除']")
    menu_pin = (By.XPATH, "//p[text() = '设为公告']")
    # menu_copy = (By.XPATH,
    #              "//div[@class='px-[16rem] py-[12rem] flex items-center justify-center min-h-[48rem] cursor-pointer menu-item']//p[text() = '复制']")
    # menu_reply = (By.XPATH,
    #               "//div[@class='px-[16rem] py-[12rem] flex items-center justify-center min-h-[48rem] cursor-pointer menu-item']//p[text() = '回复']")
    # menu_revoke = (By.XPATH,
    #                "//div[@class='px-[16rem] py-[12rem] flex items-center justify-center min-h-[48rem] cursor-pointer menu-item']//p[text() = '撤回']")
    # menu_delete = (By.XPATH,
    #                "//div[@class='px-[16rem] py-[12rem] flex items-center justify-center min-h-[48rem] cursor-pointer menu-item']//p[text() = '刪除']")
    # menu_pin = (By.XPATH, "//div[@class='px-[16rem] py-[12rem] flex items-center justify-center min-h-[48rem] cursor-pointer menu-item']//p[text() = '设为公告']")
    # -------------------- 二次確認彈窗 --------------------
    confirm_popup = (By.XPATH,"//div[@class='neutral-50 relative rounded-[8rem] max-h-[90%] flex-col m-auto max-w-[360rem] p-[40rem] w-full']")
    confirm_popup_title = (By.XPATH, "(//div[@class='text-center'])[last()-1]")
    confirm_content = (By.XPATH, "(//div[@class='text-center'])[last()]")
    confirm_submit = (By.XPATH, "//button[@class='px-[16rem] py-[14rem] h-[48rem] rounded-[4rem] w-full gradient-primary bg-primary-500 text-white-100']")

    # ============================= 回覆訊息 ============================================================================
    reply_preview_nickname = (By.XPATH, "//div[@class='flex px-[8rem] flex-col overflow-hidden']")  # 輸入框原訊息標題
    # reply_preview_text = (By.XPATH, "//div[@class='flex overflow-hidden items-center']")  # 輸入框原訊息內容
    reply_view_nickname = (By.XPATH, "(//div[@class='flex items-center w-full'])[last()]")  # 聊天室內最後一則訊息的回覆框"原訊息暱稱"
    reply_view_text = (By.XPATH, "(//div[@class='overflow-hidden flex items-center'])[last()]")  # 聊天室內最後一則訊息的回覆框"原訊息內容"
    reply_voice_text = (By.XPATH, "(//div[@class='text-neutral-900-25 text-[12px] font-normal'])[last()]") # 聊天室內最後一則語音訊息的回覆框"原語音訊息內容"
    reply_msg = (By.XPATH, "(//div[@class='px-[8rem] py-[12rem] text-[16rem] text-grand-1 break-all whitespace-pre-wrap'])[last()]")  # 回覆文字
    reply_item_msg = (By.XPATH, "(//div[@class='reply-item__msg'])[last()]")  # 原訊息

    # ============================= 表情符號 ==============================================================================
    emoji_btn = (By.XPATH, "(//div[@class='relative'])[last()]")
    emoji_panel = (By.XPATH, "//div[@class='hidden -emoji-view !flex z-10 absolute top-[-24rem]']")
    emoji_astonished = (By.XPATH, '(//img[@class="w-[16rem] transition-all duration-100 shrink-0 w-[40rem]"])[last()]')
    emoji_view = (By.XPATH, "//div[contains(@class,'hidden absolute left-[8rem] bottom-[-12rem] !flex')]")

    # ============================= 公告 ================================================================================
    pin_list_show = (By.XPATH, "//div[@class='flex flex-col w-full overflow-hidden overflow-y-auto overflow-x-hidden']")
    pin_first_msg = (By.XPATH, "//p[@class='text-grand-1 m-0 text-[14rem] font-semibold overflow-hidden whitespace-nowrap text-ellipsis']")
    pin_msg = (By.XPATH, "//p[@class='text-grand-1 m-0 text-[14rem] font-semibold overflow-hidden whitespace-nowrap text-ellipsis']")
    pin_expand_btn = (By.XPATH, "//div[@class='w-[24rem] h-[24rem] arrow']")
    pin_collapse_btn = (By.XPATH, "//div[@class='w-[24rem] h-[24rem] arrow rotate-180']")
    pin_no_show = (By.XPATH, "//p[text()='不再显示']")

    pin_alert_popup = (By.XPATH, "//div[@class='px-[44px] py-[12px]']")
    pin_popup_close = (By.XPATH, "//button[text()='确认']")

    # ============================= 聊天室 > 聊天詳情頁 ===================================================================

    @staticmethod
    def message_locator(text, message_type='text'):
        if message_type == 'text':
            locator = (By.XPATH, f"(//span[text()='{text}'])[last()]")
        else:
            locator = (By.XPATH, f"(//div[text()='{text}'])[last()]")
        return locator

    @staticmethod
    def first_result(text):
        locator = (By.XPATH, f"(//span[text()='{text}'])[last()]")
        return locator


class MessagePage(BasePage):
    brand = gl.get_value("BRAND")

    # =========================== Chat 頁 ======================================
    def into_chat_page(self):
        self.click(MessagePageLocator.message_button)
        sleep(0.5)
        assert self.get_text(MessagePageLocator.header_title) == 'Chat'

    def into_chat_room(self, room):
        self.into_chat_page()
        self.type(MessagePageLocator.search_input, room)
        sleep(1)
        self.click(MessagePageLocator.first_result(room))
        self.wait_loading_finish()
        room_title = self.get_text(MessagePageLocator.chatroom_title).split('\n')[0]
        assert room_title == room, f'預期:{room}, 實際:{room_title}'

    def send_text_message(self):
        message = 'mWeb發訊息TeSt!@#$%'
        num = 0
        text = ''
        for _ in range(0, 6):
            text = f'{str(message)}_{str(num)}'
            self.send_message(text)
            sleep(0.5)
            current = self.get_text(MessagePageLocator.chatroom_latest_message)
            assert current == text
            num += 1
        return text

    def send_message(self, message):
        if self.is_element_finded(MessagePageLocator.input_message):
            self.click(MessagePageLocator.input_message)
            self.type(MessagePageLocator.input_message, message)
        if self.is_element_finded(MessagePageLocator.send_btn):
            self.click(MessagePageLocator.send_btn)

    def send_voice_message(self, record_length):
        length = int(record_length)
        if length < 9:
            expect_result = f"00:0{length}"
        else:
            expect_result = f"00:{length}"

        if self.is_element_finded(MessagePageLocator.mic_btn):
            self.click(MessagePageLocator.mic_btn)
        else:
            self.click(MessagePageLocator.add_function_btn)
            self.click(MessagePageLocator.mic_btn)
        popup_title = self.get_text(MessagePageLocator.popup_title)
        assert popup_title == "点击以进行录音", f'錄音初始介面有誤, 實際:{popup_title}'
        self.click(MessagePageLocator.record_voice_btn)
        # ---------- 瀏覽器跳出麥克風權限時點擊允許-----------------
        sleep(1)
        location_mic_allow = pyautogui.locateCenterOnScreen(DIR_NAME + '\\element_icon\\mic_allow_permission.jpg', confidence=0.8)
        if location_mic_allow:
            pyautogui.click(location_mic_allow)
        else:
            if length < 9:
                expect_result = f"00:0{length+1}"
            else:
                expect_result = f"00:{length+1}"
        # ----------------------------------------------------
        sleep(length)
        button_img_path = ''
        if self.brand.lower() == "gu":
            button_img_path = DIR_NAME + '\\element_icon\\send.jpg'
        elif self.brand.lower() == "mingpin":
            button_img_path = DIR_NAME + '\\element_icon\\send_mingpin.jpg'
        pyautogui.click(pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8))
        sleep(3)
        self.click(MessagePageLocator.close_btn)
        self.wait_loading_finish()

        actual_voice_msg_length = self.get_text(MessagePageLocator.chatroom_latest_voice_message)
        assert actual_voice_msg_length == expect_result, f'聊天室內語音長度有誤, 預期:{expect_result}, 實際:{actual_voice_msg_length}'

    def send_file_message(self):
        if self.is_element_finded(MessagePageLocator.file_btn):
            self.click(MessagePageLocator.file_btn)
        else:
            self.click(MessagePageLocator.add_function_btn)
            self.click(MessagePageLocator.file_btn)

        file_folder_path = f'{DIR_NAME}\\test_medias\\file_sample'
        files = [f for f in os.listdir(file_folder_path) if os.path.isfile(os.path.join(file_folder_path, f))]
        random_file = random.choice(files)
        file_path = f'{DIR_NAME}\\test_medias\\file_sample\\{random_file}'

        self.copy_to_clipboard(file_path)
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        confirm_msg_content = self.get_text(MessagePageLocator.send_confirm_content)
        assert confirm_msg_content == f'您要传送『{random_file}』吗？'

        self.click(MessagePageLocator.send_confirm_submit)
        sleep(5)
        actual_chatroom_filename = self.get_text(MessagePageLocator.chatroom_last_filename)
        assert actual_chatroom_filename == random_file, f'檔案名稱錯誤, 預期:{random_file},實際:{actual_chatroom_filename}'

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

    def send_url_message(self):
        message_url = 'https://gu-chat.com'
        brand = 'gu-chat'
        self.send_message(message_url)
        self.check_url_message(brand)

        button_img_path = ''
        if self.brand.lower() == "gu":
            button_img_path = DIR_NAME + '\\element_icon\\back.jpg'
        elif self.brand.lower() == "mingpin":
            button_img_path = DIR_NAME + '\\element_icon\\back_mingpin.jpg'
        location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        pyautogui.click(location)

        self.wait_login_finish()
        return message_url

    def check_url_message(self, brand):
        self.wait_message_finish()
        self.click(MessagePageLocator.chatroom_latest_message)
        self.switch_last_page()
        current_url = self.get_url()
        assert current_url.__contains__(brand), f'股聊網站超連結開啟有誤'
        self.close_browser()
        self.switch_last_page()

    def check_chatroom_list_last_message(self, text):
        # if self.is_element_finded(MessagePageLocator.back_btn):
        #     self.click(MessagePageLocator.back_btn)
        button_img_path = ''
        if self.brand.lower() == "gu":
            button_img_path = DIR_NAME + '\\element_icon\\back.jpg'
        elif self.brand.lower() == "mingpin":
            button_img_path = DIR_NAME + '\\element_icon\\back_mingpin.jpg'
        location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        pyautogui.click(location)
        self.wait_login_finish()
        current_last_message = self.get_text(MessagePageLocator.chat_list_chatroom_last_message)
        assert current_last_message.__contains__(text), f'最後一筆訊息有誤, 預期:{text}, 實際:{current_last_message}'

    def get_chatroom_last_message(self, message_type='text'):
        sleep(3)
        if message_type == 'voice':
            return self.get_text(MessagePageLocator.chatroom_latest_voice_message)
        elif message_type == 'file':
            return self.get_text(MessagePageLocator.chatroom_last_filename)
        else:
            return self.get_text(MessagePageLocator.chatroom_latest_message)

    def check_reply_msg(self, message):
        assert self.get_text(MessagePageLocator.reply_item_msg) == message

    def message_copy(self, message):
        self.wait_message_finish()
        if self.is_element_finded(MessagePageLocator.message_locator(message)) is True:
            self.long_press(MessagePageLocator.message_locator(message))
            self.menu_click(MessagePageLocator.menu_copy)

        self.click(MessagePageLocator.input_message)
        self.type_paste(MessagePageLocator.input_message)

        if self.is_element_finded(MessagePageLocator.send_btn) is True:
            self.click(MessagePageLocator.send_btn)
            sleep(0.5)

    def message_reply(self, original_message, reply_text, message_type='text'):
        self.wait_message_finish()
        if self.is_element_finded(MessagePageLocator.message_locator(original_message, message_type)) is True:
            self.long_press(MessagePageLocator.message_locator(original_message, message_type))
            self.menu_click(MessagePageLocator.menu_reply)
            sleep(1)
        else:
            return False
        sleep(3)
        reply_preview_contents = self.get_text(MessagePageLocator.reply_preview_nickname).split('\n')
        reply_preview_nickname = reply_preview_contents[0]
        reply_preview_text = reply_preview_contents[1]

        assert reply_preview_nickname.__contains__('回复'), f'訊息回覆框預覽標題有誤'
        assert reply_preview_text == original_message, f'訊息回覆框預覽內文有誤'

        self.click(MessagePageLocator.input_message)
        self.type(MessagePageLocator.input_message, reply_text)
        sleep(0.5)
        self.click(MessagePageLocator.send_btn)
        self.sleep(0.5)

        reply_view_nickname = self.get_text(MessagePageLocator.reply_view_nickname)

        assert reply_preview_nickname[3:] == reply_view_nickname, f'聊天室內原訊息暱稱有誤'

        if message_type == 'voice':
            reply_msg_original_msg = self.get_text(MessagePageLocator.reply_voice_text)
        elif message_type == 'file':
            reply_msg_original_msg = self.get_text(MessagePageLocator.reply_file_text)
        else:
            reply_msg_original_msg = self.get_text(MessagePageLocator.reply_view_text)

        assert reply_msg_original_msg == original_message, f'聊天室內原訊息內文有誤'

    def message_revoke(self, message, pin_revoke=False, message_type='text'):
        self.wait_message_finish()
        if self.is_element_finded(MessagePageLocator.message_locator(message, message_type)) is True:
            # while not self.is_element_finded(MessagePageLocator.menu_revoke):
            self.long_press(MessagePageLocator.message_locator(message, message_type))
            self.menu_click(MessagePageLocator.menu_revoke)
            sleep(1)
        else:
            return False

        if self.is_element_finded(MessagePageLocator.confirm_popup) is True:
            popup_title = self.get_text(MessagePageLocator.confirm_popup_title)
            assert popup_title == '撤回讯息', f'撤回訊息彈窗有誤'
            self.click(MessagePageLocator.confirm_submit)
            self.wait_loading_finish()
            current_system_msg = self.get_text(MessagePageLocator.system_message)
            if pin_revoke:
                assert current_system_msg.__contains__('设定一笔讯息为公告'), f"最後一筆系統訊息有誤,設公告後撤回系統訊息預期為設公告"
            else:
                assert current_system_msg.__contains__('你已撤收一则讯息'), f"撤回系統訊息有誤"

        last_message = self.get_text(MessagePageLocator.chatroom_latest_message)
        return last_message

    def add_message_emoji(self, message):
        self.wait_message_finish()
        if self.is_element_finded(MessagePageLocator.message_locator(message)):
            self.click(MessagePageLocator.emoji_btn)
            assert self.is_element_finded(MessagePageLocator.emoji_panel)
            self.click(MessagePageLocator.emoji_astonished)
            sleep(1)
            assert self.is_element_finded(MessagePageLocator.emoji_view)
        else:
            return False

    def message_pin(self, message):
        # self.refresh_browser()
        # self.sleep(1)
        self.wait_message_finish()
        if self.is_element_finded(MessagePageLocator.message_locator(message)) is True:
            self.long_press(MessagePageLocator.message_locator(message))
            self.sleep(0.5)
            self.menu_click(MessagePageLocator.menu_pin)
        else:
            return False

        if self.is_element_finded(MessagePageLocator.pin_alert_popup) is True:
            assert self.get_text(MessagePageLocator.pin_alert_popup) == '公告已满5则，无法新增，请取消欲替换的公告', f'彈窗訊息有誤'
            self.click(MessagePageLocator.pin_popup_close)
            return False
        else:
            self.sleep(0.5)
            pin_show = self.get_text(MessagePageLocator.pin_first_msg)
            assert pin_show == message, f'公告顯示有誤'
            assert self.get_text(MessagePageLocator.system_message).__contains__('设定一笔讯息为公告'), f'設定置頂公告系統訊息有誤'
            return True

    def pin_full_messages(self):
        message = 'mWeb發訊息TeSt!@#$%'
        pin_sort = [2, 0, 1, 3, 4, 5]

        times = 1
        expected_list = []
        for number in pin_sort:
            text = f'{str(message)}_{str(number)}'

            if times < 6:
                assert self.message_pin(text) is True
                expected_list.append(text)
            else:
                assert self.message_pin(text) is False
                break
            times = times + 1

        if not self.is_element_finded(MessagePageLocator.pin_list_show):
            self.click(MessagePageLocator.pin_expand_btn)
        Reality_list = self.get_pin_message()
        Reality_list.reverse()

        assert Reality_list == expected_list, f'公告排序有誤'
        sleep(1)
        self.click(MessagePageLocator.pin_collapse_btn)

    def get_pin_message(self):
        message_num = []
        for message in self.find_elements(MessagePageLocator.pin_msg):
            message_num.append(message.text)

        return message_num

    def delete_all_pin(self):
        while self.is_element_finded(MessagePageLocator.pin_msg):

            if not self.is_element_finded(MessagePageLocator.pin_list_show):
                self.sleep(0.5)
                self.click(MessagePageLocator.pin_expand_btn)

            if self.is_element_finded(MessagePageLocator.pin_no_show):
                before_message = self.get_text(MessagePageLocator.pin_first_msg)
                self.click(MessagePageLocator.pin_no_show)
                self.sleep(0.5)

                if self.is_element_finded(MessagePageLocator.pin_list_show):
                    after_message = self.get_text(MessagePageLocator.pin_first_msg)
                    assert before_message != after_message, f'公告取消失敗'
                else:
                    break
            else:
                print('角色權限不足')
                break

    def check_pin_message(self, message):
        assert self.get_text(MessagePageLocator.pin_first_msg) == message

    def check_chat_share_info(self, content_creator, share_message='', share_main_page=True):
        sleep(1)
        if share_main_page:  # 當分享文為個人主頁
            actual_creator = self.get_text(MessagePageLocator.chat_share_author_name)
            assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'

            assert self.is_element_finded(MessagePageLocator.chat_share_post_1)
            assert self.is_element_finded(MessagePageLocator.chat_share_post_2)
            assert self.is_element_finded(MessagePageLocator.chat_share_post_3)

            if share_message != '':
                try:
                    actual_share_message = self.get_text(MessagePageLocator.chat_share_self_page_message)
                    assert actual_share_message == share_message, f'分享貼文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                except Exception:
                    assert False, '分享文沒有含留言'
        else:  # 當分享文為貼文
            assert self.is_element_finded(MessagePageLocator.chat_share_post_thumbnail)

            actual_creator = self.get_text(MessagePageLocator.chat_share_author_name)
            assert actual_creator == content_creator, f'作者錯誤, 預期:{content_creator}, 實際:{actual_creator}'

            if share_message != '':
                try:
                    actual_share_message = self.get_text(MessagePageLocator.chat_share_post_message)
                    assert actual_share_message == share_message, f'分享貼文留言與實際留言不同, 預期:{share_message}, 實際:{actual_share_message}'
                except Exception:
                    assert False, '分享文沒有含留言'