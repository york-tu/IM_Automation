from selenium.webdriver.common.by import By
from Project.chat.web.pages.admin.admin_basepage import BasePage
import os, re
from bs4 import BeautifulSoup
import pandas as pd


class LoginPageLocator:
    # ADMIN LOGIN PAGE (後台登入頁)
    login_input_account = (By.XPATH, "//input[@placeholder='请输入登录帐号']")  # 帳號欄
    login_input_password = (By.XPATH, "//input[@placeholder='请输入登录密码']")  # 密碼欄
    login_hide_otp = (By.XPATH, "//div[@class='el-overlay' and contains(@style,'display: none;')]")  # 隱藏OTP欄
    login_btn = (By.XPATH, "//span[text()='登录']/..")  # 登入按鈕
    login_check_point = (By.XPATH, "//div[@class='version']")  # 判斷已登入點
    login_deshboard = (By.XPATH, "//a[@href='/dashboard']")
    user_info_btn = (By.XPATH, "//*[@id='app']/div/header/div[2]/div[2]/div")  # 右上角user_info按鈕
    logout_btn = (By.XPATH, "//*[text()='登出']/..")  # 登出按鈕


class LoginPage(BasePage):
    # 登入動作
    def login(self, account, passowrd):
        self.wait_loading_finish()
        if self.is_element_finded(LoginPageLocator.login_check_point) == True:
            self.click(LoginPageLocator.login_deshboard)
            return

        if self.is_element_finded(LoginPageLocator.login_hide_otp) == True:
            self.type(LoginPageLocator.login_input_account, account)
            self.type(LoginPageLocator.login_input_password, passowrd)
            self.click(LoginPageLocator.login_btn)
        else:
            print('需要 OTP 驗證 無法測試')
            self.driver.quit()
            os._exit(15)

        self.wait_loading_finish()
        self.wait_visibility(LoginPageLocator.login_check_point)

    # 登出
    def logout(self):
        self.click(LoginPageLocator.user_info_btn)
        self.wait_loading_finish()
        self.click(LoginPageLocator.logout_btn)
        self.wait_loading_finish()
