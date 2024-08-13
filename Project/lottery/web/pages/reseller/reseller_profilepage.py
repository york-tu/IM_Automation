from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class ProfilePageLocator:
    # 密碼修改
    old_password = (By.XPATH, '//input[@data-bind="value:oldpasswd"]')
    new_password = (By.XPATH, '//input[@data-bind="value:newpasswd"]')
    new_password_confirm = (By.XPATH, '//input[@data-bind="value:newpasswd2"]')
    Button_save_password = (By.XPATH, '//form[@data-context="my.passwd"]//button[contains(@data-bind, "submit")]')

    # 安全碼
    new_security_code = (By.XPATH, '//input[@data-bind="value:newsecuritycode"]')
    new_security_code_confirm = (By.XPATH, '//input[@data-bind="value:newsecuritycode2"]')
    Button_save_security_code = (By.XPATH, '//form[@data-context="my.securitycode"]//button[contains(@data-bind, "submit")]')

    # 訊息
    old_password_message = (By.XPATH, '//input[@data-bind="value:oldpasswd"]/../span')
    new_password_message = (By.XPATH, '//input[@data-bind="value:newpasswd"]/../span')
    new_password_confirm_message = (By.XPATH, '//input[@data-bind="value:newpasswd2"]/../span')
    new_security_code_message = (By.XPATH, '//input[@data-bind="value:newsecuritycode"]/../span')
    new_security_code_confirm_message = (By.XPATH, '//input[@data-bind="value:newsecuritycode2"]/../span')
    toast_message = (By.XPATH, '//div[@class="toast-message"]')

class ProfilePage(BasePage):
    # 檢查密碼全為空
    def check_all_password_empty(self):
        self.wait_loading_finish()
        self.sleep(1)
        self.click(ProfilePageLocator.Button_save_password)
        self.sleep(1)

        assert self.get_text(ProfilePageLocator.old_password_message) == '必填字段', '舊的密碼 未顯示"必填字段"'
        assert self.get_text(ProfilePageLocator.new_password_message) == '必填字段', '新的密碼 未顯示"必填字段"'
        assert self.get_text(ProfilePageLocator.new_password_confirm_message) == '必填字段', '確認密碼 未顯示"必填字段"'
    
    # 檢查輸入錯誤就舊密碼
    def check_input_error_old_password(self):
        self.wait_loading_finish()
        self.type(ProfilePageLocator.old_password, '00')
        self.type(ProfilePageLocator.new_password, '000000')
        self.type(ProfilePageLocator.new_password_confirm, '000000')
        self.click(ProfilePageLocator.Button_save_password)
        self.click(ProfilePageLocator.Button_save_password)

        self.wait_visibility(ProfilePageLocator.toast_message)
        assert self.get_text(ProfilePageLocator.toast_message).__contains__('帐号/密码有误'), '未顯示 錯誤密碼訊息'

    # 更新密碼並檢查是否更新成功
    def change_password(self, old_password, new_password, new_password_confirm):
        self.wait_loading_finish()
        self.type(ProfilePageLocator.old_password, old_password)
        self.type(ProfilePageLocator.new_password, new_password)
        self.type(ProfilePageLocator.new_password_confirm, new_password_confirm)
        self.click(ProfilePageLocator.Button_save_password)
        self.click(ProfilePageLocator.Button_save_password)

        if new_password != new_password_confirm:
            self.wait_visibility(ProfilePageLocator.new_password_confirm_message)
            if not self.get_text(ProfilePageLocator.new_password_confirm_message).__contains__('输入值不一样'):
                raise AssertionError(f'確認密碼 未顯示"输入值不一样"')
        else:
            self.sleep(1)
            if not self.get_text(ProfilePageLocator.toast_message).__contains__('密码已更新'):
                raise AssertionError(f'未顯示 密碼更新訊息')

    # 檢查安全碼訊息
    def check_all_security_code_empty(self):
        self.wait_loading_finish()
        self.click(ProfilePageLocator.Button_save_security_code)

        self.wait_visibility(ProfilePageLocator.new_security_code_message)
        assert self.get_text(ProfilePageLocator.new_security_code_message) == '必填字段', '新的安全碼 未顯示"必填字段"'
        assert self.get_text(ProfilePageLocator.new_security_code_confirm_message) == '必填字段', '確認安全碼 未顯示"必填字段"'

    # 更新安全碼
    def change_security_code(self, new_security_code, new_security_code_confirm):

        self.wait_loading_finish()
        self.type(ProfilePageLocator.new_security_code, new_security_code)
        self.type(ProfilePageLocator.new_security_code_confirm, new_security_code_confirm)
        self.click(ProfilePageLocator.Button_save_security_code)
        self.click(ProfilePageLocator.Button_save_security_code)

    # 檢查是否更新成功
    def check_change_security_code(self, new_security_code, new_security_code_confirm):

        if len(new_security_code) < 4:
            self.wait_visibility(ProfilePageLocator.new_security_code_message)
            if not self.get_text(ProfilePageLocator.new_security_code_message).__contains__('至少输入 4 个字符'):
                raise AssertionError(f'新的安全碼 未顯示"至少输入 4 个字符"')

        if len(new_security_code_confirm) < 4:
            self.wait_visibility(ProfilePageLocator.new_security_code_confirm_message)
            if not self.get_text(ProfilePageLocator.new_security_code_confirm_message).__contains__('至少输入 4 个字符'):
                raise AssertionError(f'確認安全碼 未顯示"至少输入 4 个字符"')

        if len(new_security_code) > 4:
            self.wait_visibility(ProfilePageLocator.new_security_code_message)
            if not self.get_text(ProfilePageLocator.new_security_code_message).__contains__('输入的字符数不能超过 4 个'):
                raise AssertionError(f'新的安全碼 未顯示"输入的字符数不能超过 4 个"')

        if len(new_security_code_confirm) > 4:
            self.wait_visibility(ProfilePageLocator.new_security_code_confirm_message)
            if not self.get_text(ProfilePageLocator.new_security_code_confirm_message).__contains__('输入的字符数不能超过 4 个'):
                raise AssertionError(f'確認安全碼 未顯示"输入的字符数不能超过 4 个"')

        if len(new_security_code) == len(new_security_code_confirm) == 4:
            if new_security_code != new_security_code_confirm:
                self.wait_visibility(ProfilePageLocator.new_security_code_confirm_message)
                if not self.get_text(ProfilePageLocator.new_security_code_confirm_message).__contains__('输入值不一样'):
                    raise AssertionError(f'確認安全碼 未顯示"输入值不一样"')
            else:
                self.sleep(1)
                if not self.get_text(ProfilePageLocator.toast_message).__contains__('安全码已更新。'):
                    raise AssertionError(f'未顯示 安全碼更新訊息')
