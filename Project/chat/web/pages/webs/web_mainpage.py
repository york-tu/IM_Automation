from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
from Project.chat.web.pages.webs.web_loginpage import LoginPageLocator
from Project.chat.web.pages.webs.web_chatroompage import ChatRoomPageLocator
from Project.chat.web.pages.webs.web_chatlistpage import ChatListPageLocator

import os, random, re


class MainPageLocator:
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")
    header_next = (By.XPATH, "(//div[@class='header-text'])[last()]")

    user_info_id = (By.XPATH, "//span[text()='ID:']/../span[@class='user-info__text']")
    user_info_name = (By.XPATH, "//p[@class='chat-name__head']")
    user_name_edit = (By.XPATH, "//div[contains(@class,'pencil')]")
    user_name_save = (By.XPATH, "//button[@class='btn btn-primary btn-sm']")
    user_name_input = (By.XPATH, "//input[@placeholder='填写昵称']")
    user_plat_account = (By.XPATH, "//span[text()='帐号备注:']/../span[@class='user-info__text']")

    friend_input = (By.XPATH, "//input[@placeholder='输入帐号ID/手机号进行搜寻']")
    friend_search = (By.XPATH, "//p[@class='chat-list-search__text']")
    friend_mainid = (By.XPATH, "//p[@class='my-account__result__text']")
    friend_add = (By.XPATH, "//p[@class='chat-member-action__text']")
    friend_danger = (By.XPATH, "//p[@class='chat-member-action__text -danger']")
    friend_empty = (By.XPATH, "//p[@class='search-result-empty__text']")
    friend_list = (By.XPATH, "//div[@class='chat-friend__content']")
    not_support_toast = (By.XPATH, "//p[@class='toast__text']")  # pop up toast
    chat_list = (By.XPATH, "//div[@class='chat-list']")
    chat_input = (By.XPATH, "//div[@class='enter-message__input' and @style='display: none;']")

    integral_btn = (By.XPATH, "//p[text()='积分']")
    remain_integral_amount = (By.XPATH, "//div[@class='my-content-list__name__left']//p[@class='my-content-list__name__text']")

    notification_btn = (By.XPATH, "//p[text()='讯息通知']")
    security_btn = (By.XPATH, "//p[text()='帐号与安全']")
    black_btn = (By.XPATH, "//p[text()='黑名单']")
    share_btn = (By.XPATH, "//p[text()='分享']")
    about_btn = (By.XPATH, "//p[contains(text(),'关于')]")
    friend_btn = (By.XPATH, "//p[text()='新增好友']")
    groups_btn = (By.XPATH, "//p[text()='新增群组']")
    tab_btn = (By.XPATH, "//div[@class='tabs__item' and not (contains(@class,'-active'))]")
    tab_active = (By.XPATH, "//div[@class='tabs__item -active']")

    group_add_search = (By.XPATH, "(//input[@placeholder='搜索'])[last()]")
    group_add_text = (By.XPATH, "//span[@class='chat-setting-head__head-title__text']")
    group_add_member_list = (By.XPATH, "//div[@class='chat-member-list__group']")
    group_add_member_selet = (By.XPATH, "//div[@class='chat-member-select__item']")
    group_add_member_btn = (By.XPATH, "//label[@class='el-checkbox-style']")
    group_add_name_input = (By.XPATH, "//input[@placeholder='填写群组名称']")
    group_add_member_owner = (By.XPATH, "//p[@class='chat-member-tag__head__text']")
    group_add_member_build = (By.XPATH, "//div[@class='chat-member-tag__icon']/..")
    group_add_submit = (By.XPATH, "//p[text()='建立']")


class MainPage(BasePage):
    def return_web_version(self):  # 查看Web版本號
        self.open_base_url()
        git_version = self.driver.execute_script("return VITE_LAST_HASH;")
        official_version = self.driver.execute_script("return VITE_APP_VERSION;")
        return f'{official_version} ({git_version})'

    def open_user_info(self):
        if not self.get_text(MainPageLocator.header_title) == '个人资讯':
            self.refresh_browser()
            self.sleep(0.5)
            self.click(LoginPageLocator.model_btn)
            self.click(MainPageLocator.menu_icon)
            self.sleep(0.5)
        assert self.get_text(MainPageLocator.header_title) == '个人资讯', f'開啟個人資訊頁面有誤'

    def into_integral_page(self):
        remain_integral_amount = self.get_text(MainPageLocator.remain_integral_amount)
        self.click(MainPageLocator.integral_btn)
        self.sleep(0.5)
        header_title=self.get_text(MainPageLocator.header_title)
        assert header_title == '积分详情', f'進入積分頁面有誤, 實際:{header_title}'
        return remain_integral_amount

    def into_notification_page(self):
        self.click(MainPageLocator.notification_btn)
        assert self.get_text(MainPageLocator.header_title) == '讯息通知', f'進入訊息通知頁面有誤'

    def into_security_page(self):
        self.click(MainPageLocator.security_btn)
        sleep(1)
        assert self.get_text(MainPageLocator.header_title) == '帐号与安全', f'進入帳號與安全頁面有誤'

    def into_black_page(self):
        self.click(MainPageLocator.black_btn)
        self.wait_loading_finish()
        current_page_title = self.get_text(MainPageLocator.header_title)
        assert current_page_title == '黑名单', f'進入黑名單頁面有誤'

    def into_share_page(self):
        self.click(MainPageLocator.share_btn)
        assert self.get_text(MainPageLocator.header_title) == '分享', f'進入分享頁面有誤'

    def into_about_page(self):
        about_text = self.get_text(MainPageLocator.about_btn)
        self.click(MainPageLocator.about_btn)
        assert self.get_text(MainPageLocator.header_title) == about_text, f'進入關於聊天頁面有誤'

    def into_friend_add(self):
        self.open_user_info()
        self.click(MainPageLocator.friend_btn)
        assert self.get_text(MainPageLocator.header_title) == '新增好友', f'新增好友頁面有誤'

    def check_friend_add_disabled(self):
        assert self.is_element_finded(MainPageLocator.friend_btn) is False, f'新增好友選項可見'

    def check_friend_add_enabled(self):
        assert self.is_element_finded(MainPageLocator.friend_btn) is True, f'新增好友選項不可見'

    def change_nickname(self, before_name, after_name):
        assert self.get_text(MainPageLocator.user_info_name) == before_name, f'名稱變更前有誤'
        self.click(MainPageLocator.user_name_edit)
        self.type(MainPageLocator.user_name_input, after_name)
        self.click(MainPageLocator.user_name_save)

        assert self.get_text(MainPageLocator.user_info_name) == after_name, f'名稱變更後有誤'

    def get_user_info(self, id_name):
        old_name = self.get_text(MainPageLocator.user_info_name)
        user_id = self.get_text(MainPageLocator.user_info_id)

        assert user_id == id_name, f'會員帳號有誤'

        return old_name

    def close_modal(self, times):
        for _ in range(0, times):
            self.click(MainPageLocator.header_back)
            self.wait_login_finish()

    def add_friend(self, name: str, toast_expect_msg=None):

        self.wait_loading_finish()
        self.search_member(name)

        if name == '8613141010103':
            name = 'inwhite02'
        elif name == '8613141010102':
            name = 'outwhite02'

        if self.is_element_finded(MainPageLocator.friend_add):
            if self.get_text(MainPageLocator.friend_add) == '新增至通讯录':
                self.click(MainPageLocator.friend_add)
                # assert self.get_text(MainPageLocator.friend_add) == '打招呼' or '传讯息', f'新增後按鈕顯示錯誤'
                self.wait_loading_finish()

                assert self.get_text(ChatRoomPageLocator.room_title) == name, f'當下聊天室非該新好友聊天室'
            else:
                print(f"{name}已經為好友")
                return False
        elif self.is_element_finded(MainPageLocator.not_support_toast):
            actual_msg = self.get_text(MainPageLocator.not_support_toast)
            assert actual_msg == toast_expect_msg, f'warning訊息錯誤, 預期;{toast_expect_msg}, 實際:{actual_msg}'
        else:
            if self.is_element_finded(MainPageLocator.friend_danger):
                raise EOFError(f'{name}被加入黑名單')
            elif self.is_element_finded(MainPageLocator.friend_empty):
                raise EOFError('找不到相關帳號')

    def search_member(self, name):
        self.type(MainPageLocator.friend_input, name)
        self.click(MainPageLocator.friend_search)
        self.wait_login_finish()

    def switch_tab_to(self, page):
        self.wait_login_finish()
        if self.get_text(MainPageLocator.tab_active) == page:
            pass
        else:
            self.click(MainPageLocator.tab_btn)

        if page == '聊天':
            assert self.is_element_finded(MainPageLocator.chat_list) == True, f'進入聊天列表有誤'
        elif page == '好友':
            assert self.is_element_finded(MainPageLocator.friend_list) == True, f'進入好友列表有誤'

    def unblock_member(self):
        if self.is_element_finded(MainPageLocator.friend_danger) == True:
            self.click(MainPageLocator.friend_danger)

        assert self.get_text(MainPageLocator.friend_add) == '打招呼' or '传讯息', f'新增後按鈕顯示錯誤'
        self.click(MainPageLocator.friend_add)
        self.sleep(3)

        assert self.is_element_finded(MainPageLocator.chat_input) == False, f'解除黑名單有誤'

    def check_groups_build(self, status=''):
        self.wait_loading_finish()

        if status == True:
            assert self.is_element_finded(MainPageLocator.groups_btn) == True, f'建立群組按鈕未出現'
        elif status == False:
            assert self.is_element_finded(MainPageLocator.groups_btn) == False, f'建立群組按鈕未消失'
        else:
            if self.is_element_finded(MainPageLocator.groups_btn) == True:
                pass
            else:
                self.test_skip("建立群組功能未開啟 無法測試建立群組")

    def groups_build(self, user_id, name):
        self.wait_loading_finish()

        self.click(MainPageLocator.groups_btn)
        if self.is_element_finded(MainPageLocator.header_title) == True:
            assert self.get_text(MainPageLocator.header_title).__contains__('新增成员'), f'建立群組 彈窗開啟有誤'

        self.type(MainPageLocator.group_add_search, 'bot0')

        group_add_text = self.get_text(MainPageLocator.group_add_text)
        assert group_add_text == '您最多可以邀请2300位好友加入群组。请在此选择您要邀请的好友。在他们加入群组后，即可开始聊'

        self.wait_loading_finish()
        member_search_list = []
        member_select_list = []
        for member in self.find_elements(MainPageLocator.group_add_member_list):
            member_search_list.append(member.text)

        self.click_all(MainPageLocator.group_add_member_btn)

        self.sleep(1)
        for member in self.find_elements(MainPageLocator.group_add_member_selet):
            member_select_list.append(member.text)

        assert member_search_list == member_select_list, f'建立成員選取有誤'

        self.click(MainPageLocator.header_next)

        self.type(MainPageLocator.group_add_name_input, name)
        member_build_list = []
        member_list = []
        for member in self.find_elements(MainPageLocator.group_add_member_owner):
            member_build_list.append(member.text)

        for member in self.find_elements(MainPageLocator.group_add_member_build):
            member_list.append(member.text)

        owner = member_build_list.pop(0)
        assert owner == user_id
        assert member_build_list == member_select_list, f'第二步驟 建立成員有誤'
        assert member_build_list == member_list, f'群組建立擁有者 出現刪除按鈕'

        self.click(MainPageLocator.group_add_submit)

    def build_hundred_groups(self):
        for i in range(797,1000):
            self.wait_loading_finish()

            self.click(MainPageLocator.groups_btn)

            self.type(MainPageLocator.group_add_search, f'auto_test_222')

            self.wait_loading_finish()
            member_search_list = []
            member_select_list = []
            for member in self.find_elements(MainPageLocator.group_add_member_list):
                member_search_list.append(member.text)

            self.click_all(MainPageLocator.group_add_member_btn)

            self.sleep(0.5)
            for member in self.find_elements(MainPageLocator.group_add_member_selet):
                member_select_list.append(member.text)


            self.click(MainPageLocator.header_next)
            self.type(MainPageLocator.group_add_name_input, f"22xx_group_{i}")
            member_build_list = []
            member_list = []
            for member in self.find_elements(MainPageLocator.group_add_member_owner):
                member_build_list.append(member.text)

            for member in self.find_elements(MainPageLocator.group_add_member_build):
                member_list.append(member.text)

            self.click(MainPageLocator.group_add_submit)
            self.sleep(0.5)
            self.click(MainPageLocator.menu_icon)
