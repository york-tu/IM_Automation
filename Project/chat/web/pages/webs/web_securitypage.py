from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class SecurityPageLocator:
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")

    logout_btn = (By.XPATH, "//p[text()='登出']")
    logout_check = (By.XPATH, "//p[text()='手机号登录']")

    security_id = (By.XPATH, "(//p[@class='detail__text'])[1]")
    security_phone = (By.XPATH, "(//p[@class='detail__text'])[2]")
    
    # -------------------- 二次確認彈窗 --------------------
    confirm_popup = (By.XPATH, "//div[@class='common-modal']")
    confirm_text = (By.XPATH, "//p[@class='common-info__text']")
    confirm_title = (By.XPATH, "//div[@class='common-modal__header']")
    confirm_danger = (By.XPATH, "//button[@class='btn btn-danger btn-md']")
    confirm_primary = (By.XPATH, "(//button[@class='btn btn-primary btn-md'])[last()]")
    confirm_cancel = (By.XPATH, "//button[@class='btn btn-primary btn-md btn-outline']")
        
    # -------------------- 修改密碼彈窗 -------------------- 
    changepwd_btn = (By.XPATH, "//p[text()='更改密码']/..//div[@class='ui-tableviewcell__icon']")
    changepwd_id = (By.XPATH, "//p[@class='detail__text']")
    changepwd_old_input = (By.XPATH, "//input[@placeholder='请填写旧密码']")
    changepwd_new_input = (By.XPATH, "//input[@placeholder='请填写新的密码']")
    changepwd_new_check_input = (By.XPATH, "//input[@placeholder='请再次填写新的密码']")
    changepwd_note = (By.XPATH, "//div[@class='com-cell-info__text -note']")
    changepwd_cancel = (By.XPATH, "//button[@class='btn btn-primary btn-md btn-outline']")
    changepwd_submit = (By.XPATH, "//button[@class='btn btn-primary btn-md']")




class SecurityPage(BasePage):
    def check_mysecurity(self, account, phone, nation):
        if self.get_text(SecurityPageLocator.header_title) == '帐号与安全':
            my_id = self.get_text(SecurityPageLocator.security_id)
            my_phone = self.get_text(SecurityPageLocator.security_phone)
            
            if nation == 'TW':
                phone = '886' + str(phone)
            elif nation == "CN":
                phone = '86' + str(phone)
            elif nation == "JP":
                phone = '81' + str(phone)

            assert my_id == account, f'帳號顯示有誤'
            assert my_phone == phone, f'手機號碼顯示有誤'

    def change_password(self, old_pwd, new_pwd, brand):
        product_name = ''
        if brand == 'gu':
            product_name = '股聊'
        elif brand == 'mingpin':
            product_name = '名品会'
        elif brand == 'chit':
            product_name = '趣聊'

        if self.get_text(SecurityPageLocator.header_title) == '帐号与安全':
            my_id = self.get_text(SecurityPageLocator.security_id)
            self.click(SecurityPageLocator.changepwd_btn)
            self.wait_login_finish()
            assert self.get_text(SecurityPageLocator.header_title) == f'设定{product_name}密码', f'開啟變更密碼彈窗有誤'
            assert self.get_text(SecurityPageLocator.changepwd_id) == my_id, f'重設密碼頁ＩＤ顯示有誤'
            assert self.get_text(SecurityPageLocator.changepwd_note) == '提醒密码必须为8-16位英文+数字', f'重設密碼頁提醒有誤'

            self.type(SecurityPageLocator.changepwd_old_input, old_pwd)
            self.type(SecurityPageLocator.changepwd_new_input, new_pwd)
            self.type(SecurityPageLocator.changepwd_new_check_input, new_pwd)
            
            if self.is_element_finded(SecurityPageLocator.changepwd_submit):
                self.click(SecurityPageLocator.changepwd_submit)
            
            self.sleep(3)
            if self.is_element_finded(SecurityPageLocator.confirm_popup):
                assert self.get_text(SecurityPageLocator.confirm_title) == '密码重设成功', f'密碼重設失敗'
                self.click(SecurityPageLocator.confirm_primary)
            
    def logout(self):
        if self.get_text(SecurityPageLocator.header_title) == '帐号与安全':
            self.wait_loading_finish()
            self.click(SecurityPageLocator.logout_btn)

            if self.is_element_finded(SecurityPageLocator.confirm_popup):
                assert self.get_text(SecurityPageLocator.confirm_text) == '登出后不会删除任何资料纪录，下次登入依然可以使用本帐号。', f'登出帳號文案有誤'
                self.click(SecurityPageLocator.confirm_danger)

                self.sleep(1)
                assert self.is_element_finded(SecurityPageLocator.logout_check), f'登出失敗'


