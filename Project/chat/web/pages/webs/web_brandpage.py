import random
import re
from time import sleep

import pyperclip
from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage

class BrandPageLocator:
    login_id_input = (By.XPATH, "//input[@placeholder='账号']")
    login_pw_input = (By.XPATH, "//input[@placeholder='密码']")
    login_verify_code_input = (By.XPATH, "//input[@placeholder='验证码']")
    login_btn = (By.XPATH, '//*[@id="nzc-header-login"]')
    popup_msg = (By.XPATH, "//span[text()='平台公告']")
    close_btn = (By.XPATH, '//*[@id="close"]')
    account_security_popup_msg = (By.XPATH, "//p[@class='header-title__text']")

    return_first_btn = (By.XPATH, "//a[text()='返回首页']")
    account_security_not_modify_btn = (By.XPATH, "//a[text()='暂不修改']")
    online_deposit_btn = (By.XPATH, "//a[text()='线上存款']")
    guchat_payment_btn = (By.XPATH, '//*[text()="股聊支付"]')
    input_amount = (By.XPATH, "//input[@placeholder='请填存入金额']")
    pay_type = (By.XPATH, "//li[text()='股聊積分兌換']")
    pay_immediately = (By.XPATH, '//*[@id="nzc-deposit-online-submit"]')

    exchange_address_copy_btn = (By.XPATH, "//span[@class='el-value__copy']")

    credit_manage_btn = (By.XPATH, "//a[text()='额度转换']")
    main_wallet_money = (By.XPATH, "//span[@class='cp_balance']")

    deposit_record_btn = (By.XPATH, "//*[@id='nzc-wallet-nav-walletdeposit']")
    select_type = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[2]/select")
    select_promo = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[2]/select/option[4]")

    result_list_type = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[3]/table/tbody[1]/tr[1]/td[2]")
    result_list_before_money = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[3]/table/tbody[1]/tr[1]/td[3]")
    result_list_deposit_amount = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[3]/table/tbody[1]/tr[1]/td[4]")
    result_list_after_money = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[3]/table/tbody[1]/tr[1]/td[5]")
    result_list_status = (By.XPATH, "/html/body/div[7]/div/div[2]/div[2]/div[3]/table/tbody[1]/tr[1]/td[6]")


class BrandPage(BasePage):

    def into_brand_page(self, brand, env):
        self.open_browser(f'http://{brand.lower()}-web-{env.lower()}.paradise-soft.com.tw/')
        self.wait_loading_finish()
        if self.is_element_finded(BrandPageLocator.popup_msg):
            self.click(BrandPageLocator.close_btn)
        self.type(BrandPageLocator.login_id_input, 'cmtest006')
        self.type(BrandPageLocator.login_pw_input, 'Heaven@4394')
        self.type(BrandPageLocator.login_verify_code_input, '1')
        self.click(BrandPageLocator.login_btn)
        self.wait_loading_finish()
        if self.get_text(BrandPageLocator.account_security_popup_msg) == '账户安全':
            self.click(BrandPageLocator.account_security_not_modify_btn)

    def online_deposit(self):
        self.wait_loading_finish()
        self.click(BrandPageLocator.online_deposit_btn)
        self.wait_loading_finish()
        self.scroll_to_bottom()
        self.click(BrandPageLocator.guchat_payment_btn)
        self.wait_loading_finish()
        random_amount = random.randint(1, 10)
        self.type(BrandPageLocator.input_amount, random_amount)
        self.click(BrandPageLocator.pay_type)
        self.click(BrandPageLocator.pay_immediately)
        self.wait_loading_finish()
        self.switch_last_page()
        sleep(3)
        self.click(BrandPageLocator.exchange_address_copy_btn)
        exchange_address = pyperclip.paste()
        return exchange_address, random_amount

    def get_main_wallet_money(self):
        if self.is_element_finded(BrandPageLocator.return_first_btn):
            self.click(BrandPageLocator.return_first_btn)
            self.wait_loading_finish()
        self.click(BrandPageLocator.credit_manage_btn)
        self.wait_loading_finish()
        main_wallet_money = self.get_text(BrandPageLocator.main_wallet_money)
        if self.is_element_finded(BrandPageLocator.return_first_btn):
            self.click(BrandPageLocator.return_first_btn)
            self.wait_loading_finish()
        return main_wallet_money

    def check_deposit_record(self, before_money, deposit_amount, after_money):
        if self.is_element_finded(BrandPageLocator.credit_manage_btn):
            self.click(BrandPageLocator.credit_manage_btn)
            self.wait_loading_finish()
        self.click(BrandPageLocator.deposit_record_btn)
        self.click(BrandPageLocator.select_type)
        self.click(BrandPageLocator.select_promo)
        self.wait_loading_finish()
        assert self.get_text(BrandPageLocator.result_list_type) == '优惠', f'入款類型錯誤'
        assert self.get_text(BrandPageLocator.result_list_before_money) == str(before_money), f'入款前原金額有誤, 預期:{before_money},實際:{self.get_text(BrandPageLocator.result_list_before_money)}'
        assert self.get_text(BrandPageLocator.result_list_deposit_amount) == str(deposit_amount), f'入款金額錯誤, 預期:{deposit_amount},實際:{self.get_text(BrandPageLocator.result_list_deposit_amount)}'
        assert float(before_money) + float(deposit_amount) == float(after_money), f'入款後金額有誤, 前:{before_money}+入:{deposit_amount}=後:{after_money}'
        assert self.get_text(BrandPageLocator.result_list_after_money) == str(after_money), f'入款後金額有誤, 預期:{after_money},實際:{self.get_text(BrandPageLocator.result_list_after_money)}'
