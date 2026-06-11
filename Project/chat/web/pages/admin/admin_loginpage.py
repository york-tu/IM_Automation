import re
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

from Project.chat.web.pages.admin.admin_basepage import BasePage


class LoginPageLocator:
    # ADMIN LOGIN PAGE (後台登入頁)
    login_input_account = (By.XPATH, "//input[@placeholder='请输入登录帐号']")  # 帳號欄
    login_input_password = (By.XPATH, "//input[@placeholder='请输入登录密码']")  # 密碼欄
    login_hide_otp = (By.XPATH, "//div[@class='el-overlay' and contains(@style,'display: none;')]")  # 隱藏OTP欄
    login_btn = (By.XPATH, "//span[text()='登录']/..")  # 登入按鈕
    login_check_point = (By.XPATH, "//div[@class='version']")  # 判斷已登入點
    login_deshboard = (By.XPATH, "//a[@href='/dashboard']")
    user_info_btn = (By.XPATH, "//*[@id='app']/div/header/div[2]/div[3]/div")  # 右上角user_info按鈕
    logout_btn = (By.XPATH, "//*[text()='登出']")  # 登出按鈕


class LoginPage(BasePage):
    # 登入動作
    def login(self, account, password):
        self.wait_loading_finish()
        if self.is_element_finded(LoginPageLocator.login_check_point):
            self.click(LoginPageLocator.login_deshboard)
            return

        # 改善 1: 用 explicit wait 給 OTP overlay 最多 5 秒 render 時間, 再判斷
        # (原本用 is_element_finded 是 implicitly_wait(0) 不等待, 容易因 render 慢誤判成需要 OTP)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(LoginPageLocator.login_hide_otp)
            )
            need_otp = False
        except Exception:
            need_otp = True

        if need_otp:
            # 改善 2: 不要 os._exit(15) 砍掉整個 regression process,
            # 改 raise SkipTest, 讓 unittest 把當前 case 標 skip, 後續 case / retry / Slack / Jira 回填都能正常進行
            print('需要 OTP 驗證 無法測試, skip 此 case')
            raise unittest.SkipTest('Admin 後台需要 OTP 驗證, 無法自動化登入')

        self.type(LoginPageLocator.login_input_account, account)
        self.type(LoginPageLocator.login_input_password, password)
        self.click(LoginPageLocator.login_btn)

        self.wait_loading_finish()
        self.wait_visibility(LoginPageLocator.login_check_point)

    # 登出
    def logout(self):
        self.click(LoginPageLocator.user_info_btn)
        self.wait_loading_finish()
        self.click(LoginPageLocator.logout_btn)
        self.wait_loading_finish()
