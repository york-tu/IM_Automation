from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage
import os

class LoginPageLocator(object):
    # ADMIN LOGIN PAGE (後台登入頁)
    login_input_account = (By.XPATH, "//input[@placeholder='Username']")  # 帳號欄
    login_input_password = (By.XPATH, "//input[@placeholder='Password']")  # 密碼欄
    login_btn = (By.XPATH, "//span[text()= 'Login']")  # 登入按鈕
    login_ok_point = (By.XPATH, "//div[@class='right-menu-user-name']")  # 判斷已登入點
    login_error = (By.XPATH, "//*[contains(text(),'错误') or contains(text(),'已锁定')]")
    
class testclass():
    pass
    
class LoginPage(BasePage):
    # 登入動作
    def login(self, account, passowrd):
        
        self.wait_loading_finish()
        # 判斷是否已經登入
        if self.is_element_finded(LoginPageLocator.login_ok_point) is True:
            return

        self.wait_visibility(LoginPageLocator.login_input_account)
        self.type(LoginPageLocator.login_input_account, account)
        self.type(LoginPageLocator.login_input_password, passowrd)
        self.click(LoginPageLocator.login_btn)
        self.sleep(3)

        if self.is_element_finded(LoginPageLocator.login_error):
            print(self.get_text(LoginPageLocator.login_error))
            self.driver.quit()
            os._exit(15)

        self.wait_visibility(LoginPageLocator.login_ok_point)
