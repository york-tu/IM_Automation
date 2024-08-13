from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import os
from retrying import retry

class LoginPageLocator:
    # ADMIN LOGIN PAGE (後台登入頁)
    login_input_account = (By.NAME, "username")  # 帳號欄
    login_input_password = (By.NAME, "password")  # 密碼欄
    login_input_otp = (By.NAME, "securitycode")  # OTP欄
    login_btn = (By.XPATH, "//button[@class='btn btn-primary']")  # 登入按鈕
    login_ok_point = (By.XPATH, "//td[text()='代理帐号']")  # 判斷已登入點
    login_error=(By.XPATH,"//*[contains(text(),'密码有误') or contains(text(),'被锁定')]")

    logout_dropdown_user = (By.XPATH, '//li[@class="dropdown dropdown-user"]/a[@class="dropdown-toggle"]')
    # logout_dropdown_user = (By.XPATH, '//div[@class="top-menu"]')
    logout = (By.XPATH, '//a[@href="/logout"]')
    profile = (By.XPATH, '//a[@href="/my"]')

@retry(stop_max_attempt_number=3, wait_fixed=3000)
class LoginPage(BasePage):
    # 登入動作
    def login(self, account, passowrd, otp):
        self.wait_loading_finish()
        
        # 判斷是否已經登入
        if self.is_element_finded(LoginPageLocator.login_ok_point) is True:
            return

        self.type(LoginPageLocator.login_input_account, account)
        self.type(LoginPageLocator.login_input_password, passowrd)
        self.type(LoginPageLocator.login_input_otp, otp)
        self.click(LoginPageLocator.login_btn)
        self.sleep(1)

        if self.is_element_finded(LoginPageLocator.login_error):
            print(self.get_text(LoginPageLocator.login_error))
            self.driver.quit()
            os._exit(15)

        self.wait_visibility(LoginPageLocator.login_ok_point)
    
    # 登出動作
    def logout(self):
        # 判斷是否已經登入
        if self.is_element_finded(LoginPageLocator.login_ok_point) is True:
            self.wait_loading_finish()
            self.click(LoginPageLocator.logout_dropdown_user)
            self.click(LoginPageLocator.logout_dropdown_user)
            self.wait_visibility(LoginPageLocator.logout)
            self.click(LoginPageLocator.logout)

    # 我的資料
    def into_profile(self):
        # 判斷是否已經登入
        if self.is_element_finded(LoginPageLocator.login_ok_point) is True:
            self.wait_loading_finish()
            self.click(LoginPageLocator.logout_dropdown_user)
            self.click(LoginPageLocator.logout_dropdown_user)
            self.wait_visibility(LoginPageLocator.profile)
            self.click(LoginPageLocator.profile)
    
    # 登出成功與否判斷
    def logout_checker(self):
        self.wait_loading_finish()
        assert self.is_element_finded(LoginPageLocator.login_input_account) is True

