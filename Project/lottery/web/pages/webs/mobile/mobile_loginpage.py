from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import os
from retrying import retry

class LoginPageLocator:

    # LOGIN PAGE
    m_login_uid_input = (By.XPATH, "//input[contains(@placeholder,'账号')]")
    m_login_pwd_input = (By.XPATH, "//input[contains(@placeholder,'密码')]")
    m_login_captcha = (By.XPATH, "//input[contains(@placeholder,'验证码')]")
    m_login_btn = (By.ID, "login-button")
    m_login_btn_nwap = (By.XPATH, "//a[contains(text(),'会员登录')]")
    m_login_check_point = (By.XPATH, "//span[@class='total_balance' or @class='fe-nav__balance']")
    m_login_check_nwap = (By.XPATH, "//div[@class='user-info__id']")
    m_login_type_nwap = (By.XPATH, "//div[@class='com-cell__form -filled']")
    link_login_page = (By.XPATH, "//a[contains(text(), '登入')]")

class LoginPage(BasePage):
    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def login(self, uid, pwd, captcha=''):
        self.wait_loading_finish()

        if self.is_element_finded(LoginPageLocator.m_login_check_point) is True:
            return
        else: 
            if self.is_element_finded(LoginPageLocator.link_login_page) is True:
                self.wait_visibility(LoginPageLocator.link_login_page) 
                self.click(LoginPageLocator.link_login_page)
            else:
                pass
        
        if self.is_element_finded(LoginPageLocator.m_login_type_nwap) is True:
            return False
        else:
            pass

        if self.is_element_finded(LoginPageLocator.m_login_uid_input) is True:
            self.wait_loading_finish()
            self.wait_visibility(LoginPageLocator.m_login_uid_input)
            self.sleep(1)
            
            self.type(LoginPageLocator.m_login_uid_input, uid)
            self.type(LoginPageLocator.m_login_pwd_input, pwd)
            
            if self.is_element_displayed(LoginPageLocator.m_login_captcha) is True:
                self.type(LoginPageLocator.m_login_captcha, captcha)
            else:
                return False
            self.sleep(1)
            #self.click(LoginPageLocator.m_login_btn)
            
            if self.is_element_finded(LoginPageLocator.m_login_btn_nwap) is True:
                self.click(LoginPageLocator.m_login_btn_nwap) 
            else:
                self.click(LoginPageLocator.m_login_btn)
            
            self.sleep(1)

        
        if self.is_element_finded(LoginPageLocator.m_login_check_nwap) is True:
            pass
            #assert str(self.findElement(LoginPageLocator.m_login_check_nwap)) == uid
        else:    
            try:
                if str(self.get_alert_message()).__contains__('密码有误') or str(self.get_alert_message()).__contains__('密码错误') or str(self.get_alert_message()).__contains__('冻结'):
                    print(self.get_alert_message())
                    self.accept_alert()
                    self.driver.quit()
                    os._exit(13)
            except:
                assert self.is_element_enable(LoginPageLocator.m_login_check_point) is True
    
    # api登入後把cookie加到driver
    def add_cookie_wap(self, res):
        cookies = res.cookies.get_dict()
        keys = [k for k in cookies.keys()][0]
        value = cookies['.xy-web']
        self.driver.add_cookie({"name":f"{keys}","value":f"{value}","path":"/"})

           
            
            
            
            
            
        
        
            