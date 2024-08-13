from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class BlackPageLocator:
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")

    search_input = (By.XPATH, "//div[@class='my-blacklist']//input[@placeholder='搜索']")
    search_clear = (By.XPATH, "//div[@class='my-blacklist']//div[contains(@class,'-clear')]")
    search_list_text = (By.XPATH, "//p[@class='chat-member-list__name__text']")
    
    block_name = (By.XPATH, "//p[@class='chat-info__name__text']")
    block_note = (By.XPATH, "//p[@class='note-info__text']")
    block_chat_btn = (By.XPATH, "//p[text()='传讯息']")

    message_mask = (By.XPATH, "//div[text()='解除封锁']")
    
class BlackPage(BasePage):
    def search_blocks(self, name):
        if self.is_element_finded(BlackPageLocator.search_clear) == True:
            self.click(BlackPageLocator.search_clear)
        
        if self.is_element_finded(BlackPageLocator.search_input) == True:
            self.type(BlackPageLocator.search_input, name)

    def into_blocker(self, name):
        self.search_blocks(name)
        assert self.get_text(BlackPageLocator.search_list_text) == name, f'搜尋結果有誤'

        self.click(BlackPageLocator.search_list_text)

    def check_block_info(self, neme):
        assert self.get_text(BlackPageLocator.block_name) == neme, f'黑名單名稱顯示有誤'
        assert self.get_text(BlackPageLocator.block_note) == '已加入黑名单，你将不再收到对方的讯息。', f'黑名單提示文案有誤'
        
        if self.is_element_finded(BlackPageLocator.block_chat_btn) == True:
            self.click(BlackPageLocator.block_chat_btn)
            assert self.is_element_finded(BlackPageLocator.message_mask) == True, f'文字輸入匡沒有被封鎖'
