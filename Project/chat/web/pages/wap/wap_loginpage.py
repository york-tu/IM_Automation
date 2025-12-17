from faulthandler import is_enabled
from tarfile import is_tarfile
from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
from Project.chat.web.pages.wap.wap_main_personal_settings import PersonalSettingPage
from Project.chat.web.pages.wap.wap_mainpage import MainPage, MainPageLocator
import os,random, re
import pandas as pd
import common.utils.globalvar as gl


class LoginPageLocator:
    # 導航欄
    mainPage_button = (By.XPATH, "//a[@href='/my-page']")  # 導航欄-主頁(已登入)
    guest_mode_mainPage_button = (By.XPATH, "(//div[@class='flex flex-col items-center py-[8rem]'])[last()]")  # 導航欄-訪客模式"主頁"鍵
    # 註冊
    register_text = (By.XPATH, "//span[text()='注册']")
    register_btn = (By.XPATH, "//button[text()='注册']")
    next_btn = (By.XPATH, "//button[text()='下一步']")
    input_code = (By.XPATH, "//input[@placeholder='请输入验证码']")
    input_code_next_btn = (By.XPATH, "//button[@class='el-button el-button--primary w-full h-[48rem] text-[16rem]']")
    input_account_id = (By.XPATH, "//input[@placeholder='填写帐号']")
    input_pw = (By.XPATH, "//input[@placeholder='设定密码']")
    input_confirm_pw = (By.XPATH, "//input[@placeholder='再次设定密码']")
    input_nickname = (By.XPATH, "//input[@placeholder='填写昵称']")
    input_note = (By.XPATH, "//input[contains(@placeholder, '填写帐号备注')]")
    skip_thumbnail = (By.XPATH, "//p[text()='略过']")
    # 登入鈕
    login_btn = (By.XPATH, "//span[text()='登录']")
    # ========== 登入頁 =================================
    # 登入輸入欄位
    # login_title = (By.XPATH, "//div[text()='手机号登录']")
    login_account_input = (By.XPATH, "//input[@placeholder='请填写手机号码']")
    login_email_input = (By.XPATH, "//input[@placeholder='请填写电子邮箱']")
    login_password_input = (By.XPATH, "//input[@placeholder='请填写密码']")

    login = (By.XPATH, "//button[text()='登录']")
    login_btn_enable = (By.XPATH, "//button[@class='el-button el-button--primary w-full h-[48rem] text-[16rem]']")
    login_btn_disable = (By.XPATH, "//button[@class='el-button el-button--primary is-disabled w-full h-[48rem] text-[16rem]']")
    email_filed_success = (By.XPATH, "//div[@class='el-form-item is-success is-required asterisk-left el-form-item--label-right']")
    email_field_error = (By.XPATH, "//div[@class='el-form-item is-error is-required asterisk-left el-form-item--label-right']")
    # 錯誤訊息
    alert_message = (By.XPATH, "//span[@class='el-alert__title']")
    
    # login彈窗
    model_title = (By.XPATH, "//p[@class='text-[16rem] font-bold flex flex-col items-center relative']")
    model_btn = (By.XPATH, "//button[@class='btn btn-primary btn-md']")

    # 新登入頁
    new_login_page_welcome_description = (By.XPATH, "//div[@class='text-[16rem] font-semibold mt-[16rem] text-grand-1']")
    new_login_page_use_cellphone_btn = (By.XPATH, "//button[text()=' 使用手机号继续']")
    new_login_page_use_email_btn = (By.XPATH, "//button[text()=' 使用电子邮箱继续']")
    new_login_page_agreement_hint = (By.XPATH, "//div[@class='text-[12rem] text-grand-1 mt-[24rem] mb-[72rem]']")
    new_login_page_close_btn = (By.XPATH, "//i[@class='van-badge__wrapper van-icon van-icon-cross van-action-sheet__close van-haptics-feedback']")

    # 國家選擇
    nation_select_btn = (By.XPATH, "//span[@class='text-[16rem] flex-1 text-left text-grand-1']")
    nation_search_input = (By.XPATH, "//input[@placeholder='搜索']")
    nation_search_first = (By.XPATH, "(//div[@class='el-dialog__body'])[last()]")
    nation_show = (By.XPATH, "(//label[@class='el-form-item__label'])")

    # ========== 忘記密碼頁 =================================
    forget_pw_btn = (By.XPATH, "//div[text()='忘记密码']")
    verify_code_input = (By.XPATH, "//input[@placeholder='请输入验证码']")

    # 登入後 - 出現發現icon & focus 推薦頁
    recommendPage_selected = (By.XPATH, "//p[@class='text-[20rem] font-semibold text-neutral-500 text-white-100']")  # focus 推荐tab
    discover_button = (By.XPATH, "//a[@href='/discover']")  # 導航欄-發現


class LoginPage(BasePage):
    brand = gl.get_value("BRAND")
    PASS_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_PASS.xlsx"
    FAIL_email_file_path = r"C:\Users\york_tu\Desktop\email_regex_testcases_FAIL.xlsx"

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查頁面是否為"訪客模式"首頁(確認無發現鍵)
        self.wait_login_finish()
        if self.is_element_finded(LoginPageLocator.guest_mode_mainPage_button):
            # 出現訪客模式主頁鍵的xpath → 表示未登入
            return False
        else:
            # 無訪客模式主頁鍵的xpath → 表示已登入
            return True

    # 登入
    def login(self, account: str, password: str, nation='CN', login_method='phone'):
        if self.check_login_status() is False:
            self.click(LoginPageLocator.guest_mode_mainPage_button)
            self.check_new_login_page()

            if login_method == 'phone':
                self.click(LoginPageLocator.new_login_page_use_cellphone_btn)
                self.select_nation(nation)
                self.type(LoginPageLocator.login_account_input, account)
                self.type(LoginPageLocator.login_password_input, password)
            else:  # 透過email登入
                self.click(LoginPageLocator.new_login_page_use_email_btn)
                self.type(LoginPageLocator.login_email_input, account)
                self.type(LoginPageLocator.login_password_input, password)

            if self.is_element_finded(LoginPageLocator.login):
                self.click(LoginPageLocator.login)

            if self.is_element_finded(LoginPageLocator.alert_message) is True:
                error_message = self.get_text(LoginPageLocator.alert_message)
                raise EOFError(f'登入失敗-{error_message}')

            sleep(3)
            assert self.is_element_finded(LoginPageLocator.mainPage_button)
        else:
            pass

    def check_new_login_page(self):
        sleep(1)
        welcome_description = self.get_text(LoginPageLocator.new_login_page_welcome_description)
        assert ('欢迎来到' in welcome_description) and (self.get_product_name() in welcome_description)
        agreement_hint = self.get_text(LoginPageLocator.new_login_page_agreement_hint)
        assert agreement_hint == '如果您继续操作，即表示您同意《服务条款》并确认已阅读《隐私权政策》。'

    def get_product_name(self):
        brand = self.brand.lower()
        product = ''
        if brand == 'gu':
            product = '股聊'
        elif brand == 'mingpin':
            product = '名品会'
        return product

    # 國家選擇
    def select_nation(self, nation):
        sleep(1)
        nation_show = self.get_text(LoginPageLocator.nation_show).strip("+")
        
        if nation == 'CN':
            if nation_show == '86':
                pass
            else:
                self.click(LoginPageLocator.nation_select_btn)
                self.type(LoginPageLocator.nation_search_input,'86')
                self.click(LoginPageLocator.nation_search_first)
                nation_show = self.get_text(LoginPageLocator.nation_show)
                assert nation_show.strip("+") == '86'
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

    def register_by_email(self, account, email, pw):
        self.click(LoginPageLocator.guest_mode_mainPage_button)
        self.check_new_login_page()
        self.click(LoginPageLocator.new_login_page_use_email_btn)  # email登入
        self.wait_loading_finish()
        self.click(LoginPageLocator.register_text)  # 註冊鍵
        self.type(LoginPageLocator.login_email_input, email)  # 輸入email
        self.click(LoginPageLocator.next_btn)
        sleep(15)
        if self.is_element_finded(LoginPageLocator.input_code):
            code = self.get_verification_code_from_mail(self.brand)  # 獲得驗證碼
            self.type(LoginPageLocator.input_code, code)  # 輸入驗證碼
            self.click(LoginPageLocator.next_btn)
            sleep(3)
        # 資料填寫頁
        self.type(LoginPageLocator.input_account_id, account)
        self.type(LoginPageLocator.input_pw, pw)
        self.type(LoginPageLocator.input_confirm_pw, pw)
        self.type(LoginPageLocator.input_nickname, account)
        if self.is_element_finded(LoginPageLocator.input_note):
            self.type(LoginPageLocator.input_note,'AutoTest')  # 輸入帳號備注
        self.click(LoginPageLocator.register_btn)
        self.wait_loading_finish()

    # 登入頁email欄位檢核
    def email_field_check_in_login(self):
        self.click(LoginPageLocator.guest_mode_mainPage_button)
        sleep(1)
        self.click(LoginPageLocator.new_login_page_use_email_btn)
        self.type(LoginPageLocator.login_password_input, '000111abc')

        df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
        for idx, row in df1.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_field_error)
            assert self.is_element_displayed(LoginPageLocator.login_btn_disable)

        df2 = pd.read_excel(self.PASS_email_file_path, header=None)
        for idx, row in df2.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_filed_success)
            assert self.is_element_displayed(LoginPageLocator.login_btn_enable)

        self.refresh_browser()

    # 註冊頁email欄位檢核
    def email_field_check_in_registration(self):
        self.click(LoginPageLocator.guest_mode_mainPage_button)
        sleep(1)
        self.click(LoginPageLocator.new_login_page_use_email_btn)
        self.click(LoginPageLocator.register_btn)  # 註冊鍵

        df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
        for idx, row in df1.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_field_error)
            assert self.is_element_displayed(LoginPageLocator.login_btn_disable)

        df2 = pd.read_excel(self.PASS_email_file_path, header=None)
        for idx, row in df2.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_filed_success)
            assert self.is_element_displayed(LoginPageLocator.login_btn_enable)
        self.refresh_browser()

    # 忘記密碼頁email欄位檢核
    def email_field_check_in_forget_pw(self):
        self.click(LoginPageLocator.guest_mode_mainPage_button)
        sleep(1)
        self.click(LoginPageLocator.new_login_page_use_email_btn)
        self.click(LoginPageLocator.forget_pw_btn)  # 忘記密碼鍵
        sleep(1)
        self.type(LoginPageLocator.verify_code_input, '000111')

        df1 = pd.read_excel(self.FAIL_email_file_path, header=None)
        for idx, row in df1.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_field_error)
            assert self.is_element_displayed(LoginPageLocator.login_btn_disable)

        df2 = pd.read_excel(self.PASS_email_file_path, header=None)
        for idx, row in df2.iterrows():
            email = str(row[0]).strip()
            self.type(LoginPageLocator.login_email_input, email)
            sleep(0.25)
            assert self.is_element_displayed(LoginPageLocator.email_filed_success)
            assert self.is_element_displayed(LoginPageLocator.login_btn_enable)