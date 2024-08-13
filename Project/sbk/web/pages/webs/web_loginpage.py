from faulthandler import is_enabled
from tarfile import is_tarfile
from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re



class LoginPageLocator:
    #註冊按鈕
    register_btn = (By.XPATH, "//p[text()='注册新帐号']")
    
    #登入輸入欄位
    login_title = (By.XPATH, "//p[@class='form-entry__title__text']")
    login_account_input = (By.XPATH, "//input[@placeholder='请填写手机号码']")
    login_password_input = (By.XPATH, "//input[@placeholder='请填写密码']")
    login_btn = (By.XPATH, "//button[@class='btn btn-primary btn-md']")

    # 錯誤彈窗
    alert_danger = (By.XPATH, "//div[@class='alert -danger' and contains(@style,'flex')]")
    alert_message = (By.XPATH, "//p[@class='alert__text']")
    
    # login彈窗
    model_title = (By.XPATH, "//div[@class='common-modal__header']")
    model_btn = (By.XPATH, "//button[@class='btn btn-primary btn-md']")
    
    # 國家選擇
    nation_select_btn = (By.XPATH, "//div[@class='el-select']")
    nation_search_input = (By.XPATH, "//input[@placeholder='搜寻']")
    nation_search_frist = (By.XPATH, "(//div[@class='filter-search__list__item'])[1]")
    nation_show = (By.XPATH, "//div[@class='form-group']//p")




class LoginPage(BasePage):
    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查畫面上是否有注册鈕
        self.wait_login_finish()
        if self.is_element_finded(LoginPageLocator.model_title) is True:
            return True

        return False

    # 登入
    def login(self, account:str, password:str, nation:str):
        if self.check_login_status() is False:
            self.sleep(1)
            assert self.get_text(LoginPageLocator.login_title) == "登录", f'進入登入頁面有誤'

            self.select_nation(nation)
            self.type(LoginPageLocator.login_account_input, account)
            self.type(LoginPageLocator.login_password_input, password)

            if self.is_element_finded(LoginPageLocator.login_btn):            
                self.click(LoginPageLocator.login_btn)

            if self.is_element_finded(LoginPageLocator.alert_danger) is True:
                error_message = self.get_text(LoginPageLocator.alert_message)
                raise EOFError(f'登入失敗-{error_message}')
        else:
            pass

        self.wait_login_finish()
        self.get_text(LoginPageLocator.model_title) == '已成功连线', f'登入失敗'
        self.click(LoginPageLocator.model_btn)
