from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class SharePageLocator:
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")
    header_text = (By.XPATH, "//span[@class='chat-setting-head__head-title__text']")

    share_url = (By.XPATH, "//p[@class='link-text']")
    share_btn = (By.XPATH, "//button[@class='btn btn-primary btn-sm']")


class SharePage(BasePage):
    def get_share_link(self):
        if self.get_text(SharePageLocator.header_title) == '分享':
            assert self.get_text(SharePageLocator.header_text) == '分享连结给好友，一起聊天吧！', f'分享提示文案有誤'
            url = self.get_text(SharePageLocator.share_url)
            
            self.click(SharePageLocator.share_btn)
            return url

