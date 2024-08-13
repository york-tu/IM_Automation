from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class NotificationPageLocator:
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")
    header_text = (By.XPATH, "//span[@class='chat-setting-head__head-title__text']")
    
    notify_switch = (By.XPATH, "//p[text()='讯息通知']/..//label")   
    detile_switch = (By.XPATH, "//p[text()='通知显示讯息详情']/..//label")
    detile_switch_disabled = (By.XPATH, "//p[text()='通知显示讯息详情']/..//input[@disabled]")
    voice_switch = (By.XPATH,  "//p[text()='声音']/..//label")
    voice_switch_disabled = (By.XPATH,  "//p[text()='声音']/..//input[@disabled]")



class NotificationPage(BasePage):
    
    def check_header_text(self):
        text = self.get_text(NotificationPageLocator.header_text)
        assert text == '浏览器的通知设定会影响该功能的执行', f'提示文案有誤'
    
    def check_switch_logic(self):
        if self.is_element_finded(NotificationPageLocator.detile_switch_disabled) == False:
            self.click(NotificationPageLocator.notify_switch)
        
        assert self.is_element_finded(NotificationPageLocator.voice_switch_disabled) == True, f'聲音開關 連動有誤'
        assert self.is_element_finded(NotificationPageLocator.detile_switch_disabled) == True, f'聲音開關 連動有誤'

        # 開啟 訊息通知
        self.click(NotificationPageLocator.notify_switch)

        assert self.is_element_finded(NotificationPageLocator.voice_switch_disabled) == False, f'聲音開關 連動有誤'
        assert self.is_element_finded(NotificationPageLocator.detile_switch_disabled) == False, f'聲音開關 連動有誤' 
        