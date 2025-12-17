from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange_wellpay.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common

class LoginPageLocator:
    login_account = (By.XPATH, '//input[@placeholder="账号"]')
    login_password = (By.XPATH, '//input[@placeholder="密码"]')
    login_button = (By.XPATH, '//button//span')

    logged_in = (By.XPATH, "//span[text()='顺付 - Well Pay']")

class LoginPage(BasePage):
    def login_click(self, account, password):
        self.sleep(1)
        if self.is_element_finded(LoginPageLocator.logged_in) is False:
            self.type(LoginPageLocator.login_account, account)
            self.type(LoginPageLocator.login_password, password)
            self.click(LoginPageLocator.login_button)
        assert self.wait_visibility_status(LoginPageLocator.logged_in), f"後台登入失敗"


