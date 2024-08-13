from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class AboutPageLocator:
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")

    service_button = (By.XPATH, "//p[text()='服务条款']/..//div[contains(@class,'arrow')]")
    service_check = (By.XPATH, "//div[@class='terms-list__item']/p[1]")
    service_sub_text = (By.XPATH, "//div[@class='terms-list__item']/p[2]")

    privacy_link = (By.XPATH, "//li[@class='dots-list__item']/a")
    privacy_button = (By.XPATH, "//p[text()='隐私权政策']/..//div[contains(@class,'arrow')]")
    privacy_check = (By.XPATH, "//div[@class='privacy-content']")


class AboutPage(BasePage):
    def check_service(self, brand):
        self.click(AboutPageLocator.service_button)
        self.switch_last_page()

        brand_text = str(brand.capitalize())
        sub_text = self.get_text(AboutPageLocator.service_sub_text)
        chat_link = self.get_text(AboutPageLocator.privacy_link)

        if brand == 'gu':
            chat_text = ''.join(re.findall(r'[A-Za-z]', sub_text)) 
            
            assert chat_text == (brand_text + 'Chat')*2
            assert self.get_text(AboutPageLocator.service_check) == '服务条款', f'服务条款頁面顯示錯誤'
            assert chat_link == 'Gu Chat隐私权政策', f'隱私權連結顯示錯誤'
        
        elif brand == 'meet':
            
            assert '觅聊' in sub_text
            assert self.get_text(AboutPageLocator.service_check) == '服务条款', f'服务条款頁面顯示錯誤'
            assert chat_link == '觅聊隐私权政策', f'隱私權連結顯示錯誤'

        elif brand == 's365':
            chat_text = ''.join(re.findall(r'\d+\.?\d*', sub_text))
            brand_text = ''.join(re.findall(r'\d+\.?\d*', brand))

            assert chat_text == (brand_text)*2
            assert self.get_text(AboutPageLocator.service_check) == '服务条款', f'服务条款頁面顯示錯誤'
            assert chat_link == '365隐私权政策', f'隱私權連結顯示錯誤'

        self.close_browser()
        self.switch_last_page()

    def check_privacy(self):
        self.click(AboutPageLocator.privacy_button)
        self.switch_last_page()
        assert self.is_element_finded(AboutPageLocator.privacy_check) == True, f'隱私權政策頁面顯示錯誤'
        
        self.close_browser()
        self.switch_last_page()
