import os
import sys
from time import sleep

import pyautogui
from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
from Project.chat.web.pages.wap.wap_messagepage import MessagePageLocator
import common.utils.globalvar as gl

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)


class FriendsPageLocator:
    # ============================= 導航欄 ==============================================================================
    message_button = (By.XPATH, "//a[@href='/chat']")  # 導航欄-信息

    # ============================= 好友-新增 ===========================================================================
    friends_btn = (By.XPATH, '//svg[@class="min-w-[28rem] h-[28rem] mr-[6rem]"]')
    add_friend_btn = (By.XPATH, '//div[@class="add-icon"]')  # "新增好友"鍵
    search_new_friend_input = (By.XPATH, '//input[@placeholder="输入帐号ID进行搜寻"]')  # 搜尋欄位
    search_btn = (By.XPATH, "//span[text()='搜寻：']")  # "搜尋"
    add_to_address_book_btn = (By.XPATH, "//p[text()='新增至通讯录']")  # "新增至通訊錄"鍵
    add_btn = (By.XPATH, '')  # 新增好友-編輯暱稱-"新增"鍵
    result_nickname = (By.XPATH, '//*[@id="app"]/div/div[4]/div/div/header/div[3]/div/div[2]')  # 搜尋結果-暱稱
    back_btn = (By.XPATH, '//i[@class="el-icon text-[18rem]"]')  # 返回鍵

    # ============================= 好友-好友名單 =========================================================================
    chatlist_friend_btn = (By.XPATH, "(//div[contains(@class,'cursor-pointer')]//*[name()='svg'])[2]")  # 聊天列表-好友名單鍵
    header_title = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div')  # 頁面標題
    search_friend_input = (By.XPATH, '//input[@placeholder="搜索"]')  # 搜尋欄位
    search_clear_btn = (By.XPATH, '//div[@class="cursor-pointer w-[16rem] h-[16rem] cross-icon bg-white-100"]')  # 清除搜尋鍵
    result_first = (By.XPATH, '//span[@class="bg-transparent text-primary-500"]')  # 搜尋結果第一筆
    userDetail_back_btn = (By.XPATH, "(//div[contains(@class,'cursor-pointer')]//*[name()='svg'])[last()]")  # 用戶詳情-返回鍵

    # ============================= 聊天詳情 =============================================================================
    chatroom_back_btn = (By.XPATH, "(//div[contains(@class,'cursor-pointer')]//*[name()='svg'])[1]")  # 聊天室-返回鍵

    chatroom_detail = (By.XPATH, "//div[@class='cursor-pointer icon more-icon w-[24rem] h-[24rem]']")  # 聊天室右上角"聊天詳情"鍵
    user_detail_remark_title = (By.XPATH, '//p[@class="text-[16rem] font-semibold whitespace-nowrap text-grand-1"]')  # "描述"
    user_detail_remark_display = (By.XPATH, '//p[@class="flex-1 min-w-0 ml-[8rem] text-[16rem] font-semibold text-neutral-400 line-clamp-2 break-all"]')  # 備註內容
    remark_btn = (By.XPATH, '//div[@class="w-full flex flex-col items-center p-[16rem] mt-[8rem] bg-neutral-50"]')  # 設定備註鍵
    nickname_input = (By.XPATH, '//input[@class="flex-1 text-[14rem] bg-transparent text-grand-1"]')  # 設定備註-暱稱
    note_input = (By.XPATH, '//textarea[@placeholder="描述最长至字"]')  # 設定備註-描述
    remark_submit = (By.XPATH, "//p[text()='完成']")  # 設定備註-完成鍵
    chat_detail_nickname = (By.XPATH, '//p[@class="max-w-full my-[16rem] text-[20rem] font-semibold overflow-hidden whitespace-pre text-ellipsis text-neutral-800"]')  # 聊天詳情頁-暱稱
    chat_detail_note = (By.XPATH, '//p[@class="flex-1 min-w-0 ml-[8rem] text-[16rem] font-semibold text-grand-2 line-clamp-2 break-all"]')  # 聊天詳情頁-描述

    profile_btn = (By.XPATH, "//p[text()='个人页面']")  # "个人页面"鍵
    send_msg_btn = (By.XPATH, "//p[text()='传讯息']")  # "傳訊息"鍵
    friend_block_button = (By.XPATH, "//p[text()='加入黑名单']/..//span[@class='el-switch__core']")  # 聊天詳情-加入黑名單鍵
    block_dialog_content = (By.XPATH, '//p[@class="text-[14rem] font-medium break-all neutral-400"]')  # 加入黑名單二次確認彈窗
    block_confirm_btn = (By.XPATH, "(//p[text()='确定'])[last()]")  # 加入黑名單二次確認彈窗-確定鍵
    detail_page_block_note = (By.XPATH, "//p[text()='已加入黑名单，你将不再收到对方的讯息。']")  # 用戶詳情-黑名單文字提示

    input_block_msg = (By.XPATH, "//div[text()='该用户已被封锁']")  # 聊天室輸入框blocks
    back_to_chatroom = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/i/svg')

    report_button = (By.XPATH, "//p[text()='检举']")  # 聊天詳情頁-檢舉鍵
    report_page_description = (By.XPATH, "//p[text()='请选择检举理由']")  # 檢舉頁-內文
    report_harassment_content_btn = (By.XPATH, "//p[text()='骚扰行为']")  # 檢舉頁-"骚扰内容"選項
    report_send_btn = (By.XPATH, "//button[text()='同意并传送']")  # 檢舉頁-送出鍵
    popup_toast = (By.XPATH, '//p[@class="el-message__content"]')  # toast標題

    user_detail_setting_delete_btn = (By.XPATH, "(//p[text()='删除'])[last()]")  # 聊天詳情頁-刪除鍵
    delete_confirm_popup = (By.XPATH, "(//div[@class='text-center'])[last()]")  # 刪除二次確認彈窗
    delete_confirm_btn = (By.XPATH, "(//p[text()='删除'])[last()]")  # 刪除二次確認彈窗-刪除鍵


class FriendsPage(BasePage):
    brand = gl.get_value("BRAND")

    # =========================== 好友名單頁 ======================================
    def into_friend_list(self):
        self.click(FriendsPageLocator.message_button)
        sleep(2)
        # button_img_path = ''
        # if self.brand.lower() == "gu":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'friend_btn.jpg')
        # elif self.brand.lower() == "mingpin":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'friend_btn_mingpin.jpg')
        # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        # pyautogui.click(location)
        self.click(FriendsPageLocator.chatlist_friend_btn)
        sleep(3)
        current_page_title = self.get_text(FriendsPageLocator.header_title)
        assert current_page_title == '好友名单', f'非好友名單頁, 預期:好友名单, 實際:{current_page_title}'

    def add_friend(self, friend_nickname):  # 新增好友頁添加好友
        self.click(FriendsPageLocator.add_to_address_book_btn)
        self.wait_loading_finish()
        assert self.get_text(MessagePageLocator.chatroom_title) == friend_nickname
        # button_img_path = ''
        # if self.brand.lower() == "gu":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back.jpg')
        # elif self.brand.lower() == "mingpin":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back_mingpin.jpg')
        # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        # pyautogui.click(location)
        self.click(FriendsPageLocator.chatroom_back_btn)
        self.wait_loading_finish()

    def back_to_friend_list_page(self):
        while not self.get_text(FriendsPageLocator.header_title) == '好友名单':
            self.click(FriendsPageLocator.back_btn)

    def back_to_message_page(self):
        self.refresh_browser()
        sleep(2)
        while not self.get_text(FriendsPageLocator.header_title) == 'Chat':
            # button_img_path = ''
            # if self.brand.lower() == "gu":
            #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back.jpg')
            # elif self.brand.lower() == "mingpin":
            #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back_mingpin.jpg')
            # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
            # pyautogui.click(location)
            self.click(FriendsPageLocator.chatroom_back_btn)
            sleep(1)

    # =========================== 新增好友頁 ======================================
    def is_new_friend(self, name):  # 新增好友頁進行搜尋
        # self.click(FriendsPageLocator.add_friend_btn)
        self.wait_loading_finish()
        self.type(FriendsPageLocator.search_new_friend_input, name)
        self.click(FriendsPageLocator.search_btn)
        self.wait_loading_finish()
        if self.is_element_finded(FriendsPageLocator.add_to_address_book_btn):
            return True
        else:
            return False

    def list_friend_search(self, friend_nickname):  # 好友名單頁搜尋好友
        self.type(FriendsPageLocator.search_friend_input, friend_nickname)
        if self.is_element_finded(FriendsPageLocator.result_first):
            self.wait_loading_finish()
            assert self.get_text(FriendsPageLocator.result_first) == friend_nickname, f'第一筆搜尋結果非好友'
            self.click(FriendsPageLocator.result_first)
            return True
        else:
            return False

    # =========================== 好友聊天詳情頁 ======================================
    def set_remark_note(self, note):
        sleep(2)
        original_note = self.get_text(FriendsPageLocator.user_detail_remark_display)
        self.click(FriendsPageLocator.remark_btn)
        self.type(FriendsPageLocator.note_input, note)
        self.click(FriendsPageLocator.remark_submit)
        self.wait_loading_finish()
        assert self.get_text(FriendsPageLocator.user_detail_remark_display) == note, f'設定描述失敗'

        self.click(FriendsPageLocator.remark_btn)
        self.type(FriendsPageLocator.note_input, original_note)
        self.click(FriendsPageLocator.remark_submit)
        self.wait_loading_finish()
        assert self.get_text(FriendsPageLocator.user_detail_remark_display) == original_note, f'設定原描述失敗'

    def set_remark_nickname(self, nickname):
        original_nickname = self.get_text(FriendsPageLocator.chat_detail_nickname)
        self.click(FriendsPageLocator.remark_btn)
        self.type(FriendsPageLocator.nickname_input, nickname)
        self.click(FriendsPageLocator.remark_submit)
        self.wait_loading_finish()
        actual_nickname = self.get_text(FriendsPageLocator.chat_detail_nickname)
        assert actual_nickname == nickname, f'設定暱稱失敗'

        self.click(FriendsPageLocator.remark_btn)
        self.type(FriendsPageLocator.nickname_input, original_nickname)
        self.click(FriendsPageLocator.remark_submit)
        self.wait_loading_finish()
        actual_nickname = self.get_text(FriendsPageLocator.chat_detail_nickname)
        assert actual_nickname == original_nickname, f'設定原暱稱失敗'

    def into_personal_profile(self):
        self.wait_loading_finish()
        self.click(FriendsPageLocator.chatroom_detail)
        self.wait_loading_finish()
        self.click(FriendsPageLocator.profile_btn)

    def into_chatroom_from_userDetail(self):
        if self.is_element_finded(FriendsPageLocator.send_msg_btn):
            self.click(FriendsPageLocator.send_msg_btn)

    def into_chatroom_from_addToAddressBook(self):
        if self.is_element_finded(FriendsPageLocator.add_to_address_book_btn):
            self.click(FriendsPageLocator.add_to_address_book_btn)

    def block_friend(self):
        self.wait_loading_finish()
        self.click(FriendsPageLocator.chatroom_detail)
        self.wait_loading_finish()
        self.click(FriendsPageLocator.friend_block_button)
        sleep(1)
        assert self.get_text(FriendsPageLocator.block_dialog_content) == '加入黑名单，你将不再收到对方的讯息，对方也无法查看你。', f'加入黑名單未跳通知'
        self.click(FriendsPageLocator.block_confirm_btn)
        sleep(1)
        assert self.is_element_finded(FriendsPageLocator.detail_page_block_note)
        # button_img_path = ''
        # if self.brand.lower() == "gu":
        #     button_img_path = DIR_NAME + '\\element_icon\\back.jpg'
        # elif self.brand.lower() == "mingpin":
        #     button_img_path = DIR_NAME + '\\element_icon\\back_mingpin.jpg'
        # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        # pyautogui.click(location)
        self.refresh_browser()
        self.wait_loading_finish()
        assert self.is_element_finded(FriendsPageLocator.input_block_msg)

    def report(self):
        self.wait_loading_finish()
        self.click(FriendsPageLocator.chatroom_detail)
        self.wait_loading_finish()
        self.click(FriendsPageLocator.report_button)
        assert self.is_element_finded(FriendsPageLocator.report_page_description)
        self.click(FriendsPageLocator.report_harassment_content_btn)
        self.click(FriendsPageLocator.report_send_btn)
        self.wait_visibility(FriendsPageLocator.popup_toast)
        assert self.get_text(FriendsPageLocator.popup_toast) == '检举成功'

    def delete_friend_from_UserDetail(self, friend_nickname):  # 好友名單 > 用戶詳情 > 刪除
        self.click(FriendsPageLocator.user_detail_setting_delete_btn)
        self.wait_visibility(FriendsPageLocator.delete_confirm_popup)  # 二次刪除確認框
        pops_msg = self.get_text(FriendsPageLocator.delete_confirm_popup)
        assert pops_msg == f'将联络人「{friend_nickname}」删除，同时删除与该联络人的聊天纪录。', f'彈窗有誤'
        self.click(FriendsPageLocator.delete_confirm_btn)
        self.wait_loading_finish()
        assert self.is_element_finded(FriendsPageLocator.add_to_address_book_btn), f"未出現[新增至通讯录]選項"
        # 返回上一頁
        # button_img_path = ''
        # if self.brand.lower() == "gu":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back.jpg')
        # elif self.brand.lower() == "mingpin":
        #     button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back_mingpin.jpg')
        # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        for _ in range(2):
            # pyautogui.click(location)
            self.click(FriendsPageLocator.userDetail_back_btn)
            self.wait_loading_finish()
