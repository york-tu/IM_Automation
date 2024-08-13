from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os, random, re


class FriendPageLocator:
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")

    search_input = (By.XPATH, "//div[@class='chat-room__start']//input[@placeholder='搜索']")
    search_clear = (By.XPATH, "//div[@class='chat-room__start']//div[contains(@class,'clear')]")
    search_name = (By.XPATH, "//*[@class='chat-member-list__name']")
    search_list_text = (By.XPATH, "//p[@class='chat-member-list__name__text']")

    groups_btn = (By.XPATH, "//p[text()='群组']/../div[@class='head-icon']")
    groups_show = (By.XPATH, "//div[@class='chat-friend__item -show']//p[text()='群组']")

    friends_tab = (By.XPATH, "//p[text()='好友']")
    friends_btn = (By.XPATH, "//p[text()='好友']/../div[@class='head-icon']")
    friends_show = (By.XPATH, "//div[@class='chat-friend__item -show']//p[text()='好友']")

    room_title = (By.XPATH, "//p[@class='chat-detail__name__text']")


class FriendPage(BasePage):
    def search_friend(self, name):
        self.click(FriendPageLocator.friends_tab)
        if self.is_element_finded(FriendPageLocator.search_clear) == True:
            self.click(FriendPageLocator.search_clear)

        if self.is_element_finded(FriendPageLocator.search_input) == True:
            self.type(FriendPageLocator.search_input, name)

        if self.is_element_finded(FriendPageLocator.search_name) == True:
            assert self.get_text(FriendPageLocator.search_list_text).__contains__(name), f'好友列表中 無此好友: {name}'

    def into_chatroom(self):
        self.sleep(0.5)
        search_result = self.get_text(FriendPageLocator.search_name)
        self.click(FriendPageLocator.search_name)
        self.wait_message_finish()

        assert search_result == self.get_text(FriendPageLocator.room_title), f'進入聊天室有誤'

    def check_show_btn(self):
        self.wait_loading_finish()
        self.click(FriendPageLocator.groups_btn)
        assert self.is_element_finded(FriendPageLocator.groups_show) == False, f'群組列表顯示按鈕 隱藏有誤'
        self.click(FriendPageLocator.groups_btn)
        assert self.is_element_finded(FriendPageLocator.groups_show) == True, f'群組列表顯示按鈕 顯示有誤'
        self.wait_loading_finish()
        self.click(FriendPageLocator.friends_btn)
        assert self.is_element_finded(FriendPageLocator.friends_show) == False, f'好友列表顯示按鈕 隱藏有誤'
        self.click(FriendPageLocator.friends_btn)
        assert self.is_element_finded(FriendPageLocator.friends_btn) == True, f'好友列表顯示按鈕 顯示有誤'

    def check_friend(self, name):
        self.search_friend(name)

        self.sleep(0.5)
        friends = self.find_elements(FriendPageLocator.search_list_text)

        if len(friends) < 1:
            return False
        else:
            for friend in friends:
                if friend == name :
                    assert self.get_text(FriendPageLocator.search_name).__contains__(name), f'搜尋結果有誤'
                    return True

    def check_notexist(self, name):
        assert self.check_friend(name) is False, f'該好友未正常刪除'
