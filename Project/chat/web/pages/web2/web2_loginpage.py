from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.web2.web2_basepage import BasePage
from Project.chat.web.pages.web2.web2_firstpage import FirstPage, FirstPageLocator
import pandas as pd
import common.utils.globalvar as gl


class LoginPageLocator:
    # ========== 左側導航欄 ==========
    firstPage_btn = (By.XPATH, "//span[text()='首页']")  # 首頁鍵
    login_btn = (By.XPATH, "//button[text()='登录']")  # 登录鍵
    mainPage_button = (By.XPATH, "//span[text()='主页']")  # 主頁鍵(已登入)
    more_btn = (By.XPATH, "//span[text()='更多']")  # 更多(已登入)

    # ========== 新登入頁 ==========
    new_login_page_welcome_description = (By.XPATH,
                                          "//h2[@class='mt-4 text-base font-semibold text-center text-[#111111]']")
    new_login_page_use_cellphone_btn = (By.XPATH, "//span[text()='使用手机号继续']")
    new_login_page_use_email_btn = (By.XPATH, "//span[text()='使用电子邮件继续']")
    new_login_page_use_google_btn = (By.XPATH, "//span[text()='使用 Google 繼續']")
    new_login_page_agreement_hint = (By.XPATH, "//p[@class='my-auto text-xs text-center text-neutral-900 leading-[20px]']")
    new_login_page_close_btn = (By.XPATH, "//button[@aria-label='關閉']")

    # ========== 手機號登錄 ==========
    # 國家選擇
    nation_select_btn = (By.XPATH, "//button[@class='flex items-center justify-between w-full overflow-clip rounded-none hover:cursor-pointer']")
    nation_search_input = (By.XPATH, "//input[@id='search-country']")
    nation_search_first = (By.XPATH, "//span[@class='text-sm text-neutral-900 font-normal truncate']")
    nation_show = (By.XPATH, "(//label[@for='phone'])")
    login_account_input = (By.XPATH, "//input[@placeholder='请填写手机号码']")
    login_password_input = (By.XPATH, "//input[@placeholder='请填写密码']")

    login_btn_enable = (By.XPATH, '(//button[normalize-space()="登录" and not(@disabled)])[last()]')
    login_btn_disable = (By.XPATH, '//button[normalize-space()="登录" and @disabled]')

    # ========== Email登錄 ==========
    login_email_input = (By.XPATH, "//input[@placeholder='请填写电子邮箱']")
    # ===== 註冊 =====
    login_page_register_btn = (By.XPATH, "//button[text()='註冊']")
    register_btn = (By.XPATH, "//button[text()='注册']")
    next_btn = (By.XPATH, "(//button[text()='下一步' and not(@disabled)])[last()]")
    get_verifycode_btn = (By.XPATH, "//button[text()='获取验证码']")
    input_code = (By.XPATH, "//input[@id='verificationCode']")
    # 資料填寫頁
    input_account_id = (By.XPATH, "//input[@placeholder='填写帐号']")
    input_pw = (By.XPATH, "//input[@placeholder='设定密码']")
    input_confirm_pw = (By.XPATH, "//input[@placeholder='再次设定密码']")
    input_nickname = (By.XPATH, "//input[@placeholder='填写昵称']")
    input_note = (By.XPATH, "//input[contains(@placeholder, '填写帐号备注')]")

    # ========== 登出 ==========
    logout_btn = (By.XPATH, "//*[normalize-space(text())='登出']")


class LoginPage(BasePage):
    brand = gl.get_value("BRAND")
    env = gl.get_value("ENV")

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查頁面是否為"訪客模式"首頁(確認無發現鍵)
        self.wait_login_finish()
        if self.is_element_finded(LoginPageLocator.mainPage_button) and self.is_element_finded(LoginPageLocator.more_btn):
            # 出現"主頁"鍵與"更多"鍵 → 表示已登入
            return True
        else:
            # 未出現"主頁"鍵與"更多"鍵 → 表示已登入
            return False

    # 登入
    def login(self, account: str, password: str, nation='CN', login_method='phone'):
        if not self.check_login_status():
            self.click(LoginPageLocator.login_btn)
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

            assert self.is_element_finded(LoginPageLocator.login_btn_enable)
            self.click(LoginPageLocator.login_btn_enable)
            assert self.check_login_status()

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
        env = self.env.lower()

        suffix = "_UAT" if env == 'uat' else ""
        product_info = {
            "gu": f"GuChat{suffix}",
            "chit": f"ChitChat{suffix}",
        }
        # 預設值，可避免 key 不存在報錯
        product = product_info.get(brand, "UnknownProduct")
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
        if self.is_element_finded(LoginPageLocator.login_btn):
            self.click(LoginPageLocator.login_btn)
        self.check_new_login_page()
        self.click(LoginPageLocator.new_login_page_use_email_btn)  # email登入
        self.click(LoginPageLocator.login_page_register_btn)  # 註冊鍵
        self.type(LoginPageLocator.login_email_input, email)  # 輸入email
        self.click(LoginPageLocator.next_btn)
        sleep(0.5)
        if self.is_element_finded(LoginPageLocator.input_code):
            self.click(LoginPageLocator.get_verifycode_btn)
            sleep(10)
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

    def logout(self):
        if self.is_element_finded(LoginPageLocator.more_btn):
            self.click(LoginPageLocator.more_btn)
            self.click(LoginPageLocator.logout_btn)
            self.wait_loading_finish()
        assert self.is_element_finded(LoginPageLocator.login_btn)  # 登出後見"登錄"鍵
        assert self.is_element_finded(FirstPageLocator.btn_following)  # 登出後自動切回[首頁], 可見右側"已關注"tab
        assert self.is_element_finded(FirstPageLocator.btn_recommend)  # 登出後自動切回[首頁], 可見右側"推薦"tab
        assert self.is_element_finded(FirstPageLocator.multiple_post_mode)   # 登出後右側自動切到多貼文模式
        self.click(FirstPageLocator.btn_following)
        self.click(LoginPageLocator.new_login_page_close_btn)
