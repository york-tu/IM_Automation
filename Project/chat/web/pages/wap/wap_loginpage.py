from faulthandler import is_enabled
from tarfile import is_tarfile
from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
from Project.chat.web.pages.wap.wap_mainpage import MainPage, MainPageLocator
import os,random, re


class LoginPageLocator:
    # 註冊鈕
    register_btn = (By.XPATH, "//span[text()='注册']")
    # 登入鈕
    login_btn = (By.XPATH, "//span[text()='登录']")
    # ========== 登入頁 =================================
    # 登入輸入欄位
    login_title = (By.XPATH, "//div[text()='手机号登录']")
    login_account_input = (By.XPATH, "//input[@placeholder='请填写手机号码']")
    login_password_input = (By.XPATH, "//input[@placeholder='请填写密码']")
    login = (By.XPATH, "//span[text()='登录']")

    # 錯誤訊息
    alert_message = (By.XPATH, "//span[@class='el-alert__title']")
    
    # login彈窗
    model_title = (By.XPATH, "//p[@class='text-[16rem] font-bold flex flex-col items-center relative']")
    model_btn = (By.XPATH, "//button[@class='btn btn-primary btn-md']")
    
    # 國家選擇
    nation_select_btn = (By.XPATH, "//span[@class='text-[16rem] flex-1 text-left']")
    nation_search_input = (By.XPATH, "//input[@placeholder='搜索']")
    nation_search_first = (By.XPATH, "//div[@class='el-dialog__body']")
    nation_show = (By.XPATH, "(//label[@class='el-form-item__label'])")

    # 登入後 - focus 首頁 & 推薦
    firstPage_button_selected = (By.XPATH, "//a[contains(@class, 'router-link-active') and @href='/home']")  # 導航欄-首页
    recommendPage_selected = (By.XPATH, '//a[contains(@class, "router-link-active") and @href="/home/recommend"]')  # 推荐tab


class LoginPage(BasePage):
    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查畫面上是否有注册鈕
        self.wait_login_finish()
        if self.is_element_finded(LoginPageLocator.register_btn) or self.is_element_finded(LoginPageLocator.login_title):
            return False
        return True

    # 登入
    def login(self, account: str, password: str, nation: str):
        if self.check_login_status() is False:
            self.sleep(1)
            if not self.is_element_finded(LoginPageLocator.login_title):
                self.click(LoginPageLocator.login_btn)
                self.wait_login_finish()
                assert self.is_element_finded(LoginPageLocator.login_title), f'進入登入頁面有誤'

            self.select_nation(nation)
            self.type(LoginPageLocator.login_account_input, account)
            self.type(LoginPageLocator.login_password_input, password)

            if self.is_element_finded(LoginPageLocator.login):
                self.click(LoginPageLocator.login)

            if self.is_element_finded(LoginPageLocator.alert_message) is True:
                error_message = self.get_text(LoginPageLocator.alert_message)
                raise EOFError(f'登入失敗-{error_message}')

            sleep(3)
            assert self.is_element_finded(LoginPageLocator.firstPage_button_selected)
            assert self.is_element_finded(LoginPageLocator.recommendPage_selected)
        else:
            pass

    # 國家選擇
    def select_nation(self, nation):
        nation_show = self.get_text(LoginPageLocator.nation_show).strip("+")
        
        if nation == 'CN':
            if nation_show == '86':
                pass
            else:
                self.click(LoginPageLocator.nation_select_btn)
                self.type(LoginPageLocator.nation_search_input,'86')
                self.click(LoginPageLocator.nation_search_first)
                assert self.get_text(LoginPageLocator.nation_show).strip("+") == '86'
        elif nation == 'TW':
            if nation_show == '886':
                pass
            else:
                self.click(LoginPageLocator.nation_select_btn)
                self.type(LoginPageLocator.nation_search_input,'886')
                self.click(LoginPageLocator.nation_search_first)
                assert self.get_text(LoginPageLocator.nation_show).strip("+") == '886'
        elif nation == 'JP':
            if nation_show == '81':
                pass
            else:
                self.click(LoginPageLocator.nation_select_btn)
                self.type(LoginPageLocator.nation_search_input,'81')
                self.click(LoginPageLocator.nation_search_first)
                assert self.get_text(LoginPageLocator.nation_show).strip("+") == '81'
    