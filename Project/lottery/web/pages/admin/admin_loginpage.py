from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import os, re
from bs4 import BeautifulSoup
import pandas as pd

class LoginPageLocator(object):
    # ADMIN LOGIN PAGE (後台登入頁)
    login_input_account = (By.ID, "login")  # 帳號欄
    login_input_password = (By.ID, "password")  # 密碼欄
    login_input_otp = (By.XPATH, "//input[@name='otp']")  # OTP欄
    login_btn = (By.XPATH, "//button[@class='btn btn-primary']")  # 登入按鈕
    login_ok_point = (By.XPATH, "//div[@class='top-menu']")  # 判斷已登入點
    login_error = (By.XPATH, "//*[contains(text(),'密码有误') or contains(text(),'已锁定')]")
    login_security = (By.XPATH, "//*[@class='swal2-confirm swal2-styled']")

class testclass():
    pass
    
class LoginPage(BasePage):
    # 登入動作
    def login(self, account, passowrd, otp):
        self.wait_loading_finish()
        
        # 判斷是否已經登入
        if self.is_element_finded(LoginPageLocator.login_ok_point) is True:
            if self.is_element_finded(LoginPageLocator.login_security) is True:
                self.click(LoginPageLocator.login_security)
            return

        self.wait_visibility(LoginPageLocator.login_input_account)
        self.type(LoginPageLocator.login_input_account, account)
        self.type(LoginPageLocator.login_input_password, passowrd)
        self.type(LoginPageLocator.login_input_otp, otp)
        self.click(LoginPageLocator.login_btn)
        self.sleep(1)

        if self.is_element_finded(LoginPageLocator.login_error):
            print(self.get_text(LoginPageLocator.login_error))
            self.driver.quit()
            os._exit(15)

        self.sleep(2)
        if self.is_element_finded(LoginPageLocator.login_security) is True:
            self.click(LoginPageLocator.login_security)

        self.wait_visibility(LoginPageLocator.login_ok_point)

    # logout
    def logout(self):
        self.wait_loading_finish()
        logout_address = self.base_url + r"logout"
        self.open_browser(logout_address)
    
    # 登出成功與否判斷
    def logout_checker(self):
        self.wait_loading_finish()
        assert self.is_element_finded(LoginPageLocator.login_input_account) is True, "Admin登出失敗"

    def language(self):
        message = []

        source = self.get_page_source()
        re_words = re.findall(u"[\u4e00-\u9fa5]+", source)
      
        for word in re_words:
            simplified = self.font('t2s', word)
            if simplified != word and word != '三昇体育' and word != '機器人':
                message.append(word)

        if len(message) != 0:
            return message
        