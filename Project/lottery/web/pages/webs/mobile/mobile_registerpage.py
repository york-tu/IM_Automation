from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import random


class RegisterPageLocator:
    member_id_input = (By.XPATH, "//input[contains(@data-bind,'value: login')]")
    member_pwd_inpud = (By.XPATH, "//input[contains(@data-bind,'value: passwd')]")
    member_pwd_confirm_input = (By.XPATH, "//input[contains(@data-bind,'value: passwd2')]")
    member_name_input = (By.XPATH, "//input[contains(@data-bind,'value: name')]")
    member_withdraw_pwd_input = (By.XPATH, "//input[contains(@data-bind,'value: securitycode')]")
    member_mail_input = (By.XPATH, "//input[contains(@data-bind,'value: email')]")
    member_qq_input = (By.XPATH, "//input[contains(@data-bind,'value: qq')]")
    member_wechat_input = (By.XPATH, "//input[contains(@data-bind,'value: wechat')]")
    member_phone_input = (By.XPATH, "//input[contains(@data-bind,'value: mobile')]")
    member_referrer_input = (By.XPATH, "//input[contains(@data-bind, 'value: agentlogin')]")
    member_captcha_input=(By.XPATH, "//input[@placeholder='验证码' or contains(@data-bind, 'captcha')]")
    member_captcha_img = (By.XPATH, "//img[contains(@src,'image')]")
    member_submit_btn = (By.XPATH, "//*[contains(@data-bind, 'submit')]")
    #----------------------------NWAP-----------------------------------
    member_submit_btn_nwap = (By.XPATH, "//*[@class='btn btn-primary btn-ripple' and text()='注册']")
    member_id_nwap = (By.XPATH, "//input[@placeholder='账号']")
    member_pwd_nwap = (By.XPATH, "//input[@placeholder='密码']")
    member_pwd_confirm_nwap = (By.XPATH, "//input[@placeholder='确认密码']")
    member_user_id = (By.XPATH, "//div[@class='user-id']")
    into_game = (By.XPATH, "//span[contains(text(),'前往游戏')]")

class RegisterPage(BasePage):
    def do_register(self, _id, pwd, withdraw_pwd, name='自動化測試', email='autotest@qq.com', qq='123456', wechat='123456'):
        phone = '13' + str(random.randrange(100000000, 999999999, 9))
        if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
            if self.is_element_finded(RegisterPageLocator.member_captcha_img) is False:
                # raise EOFError('驗證碼圖片沒出現')
                self.test_skip('滑動驗證開啟，無法測試')
            self.test_skip('註冊驗證碼開啟，無法測試')

        assert len(withdraw_pwd) == 6, '提款密碼不足六碼'
        self.wait_loading_finish()
        # 輸入帳、密、名、提款密
        self.type(RegisterPageLocator.member_id_input, _id)
        self.type(RegisterPageLocator.member_pwd_inpud, pwd)
        self.type(RegisterPageLocator.member_pwd_confirm_input, pwd)
        self.type(RegisterPageLocator.member_name_input, name)
        self.type(RegisterPageLocator.member_withdraw_pwd_input, withdraw_pwd)
        # 會員資料，無欄位則不需填
        if self.is_element_displayed(RegisterPageLocator.member_mail_input):
            self.type(RegisterPageLocator.member_mail_input, email)
        if self.is_element_displayed(RegisterPageLocator.member_qq_input):
            self.type(RegisterPageLocator.member_qq_input, qq)
        if self.is_element_displayed(RegisterPageLocator.member_wechat_input):
            self.type(RegisterPageLocator.member_wechat_input, wechat)
        if self.is_element_displayed(RegisterPageLocator.member_phone_input):
            self.type(RegisterPageLocator.member_phone_input, phone)
        if self.is_element_displayed(RegisterPageLocator.member_referrer_input):
            self.type(RegisterPageLocator.member_referrer_input, "QA_Bot")
        # 滑至底部
        # self.scroll_to_bottom()
        self.scroll_to_element(RegisterPageLocator.member_submit_btn)
        # 送出註冊
        self.click(RegisterPageLocator.member_submit_btn)
        # Alert處理
        self.wait_alert_present()
        message = self.get_alert_message()
        assert '注册成功' in message, message
        self.accept_alert()
        # 註冊完回首頁需Loading
        self.wait_loading_finish()

    def do_register_nwap(self, t_id, t_pwd, t_withdraw_pwd, t_name='自動化測試'):

        if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
            if self.is_element_finded(RegisterPageLocator.member_captcha_img) is False:
                raise EOFError('驗證碼圖片沒出現')

            self.test_skip('註冊驗證碼開啟，無法測試')

        assert len(t_withdraw_pwd) == 6, '提款密碼不足六碼'
        self.wait_loading_finish()
        # 輸入帳、密、名、提款密
        self.type(RegisterPageLocator.member_id_input, t_id)
        self.type(RegisterPageLocator.member_pwd_inpud, t_pwd)
        self.type(RegisterPageLocator.member_pwd_confirm_input, t_pwd)
        self.type(RegisterPageLocator.member_name_input, t_name)
        self.type(RegisterPageLocator.member_withdraw_pwd_input, t_withdraw_pwd)

        # 滑至底部
        # self.scroll_to_bottom()
        self.scroll_to_element(RegisterPageLocator.member_submit_btn_nwap)
        # 送出註冊
        self.click(RegisterPageLocator.member_submit_btn_nwap)
        # Alert處理
        self.wait_loading_finish()
        assert self.is_element_finded(RegisterPageLocator.member_user_id) == t_id, f'註冊帳號有誤'
        self.click(RegisterPageLocator.into_game)
             
        # 註冊完回首頁需Loading
        self.wait_loading_finish()