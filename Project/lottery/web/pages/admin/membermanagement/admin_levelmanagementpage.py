from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class LevelManagementPageLocator:
    level_name = (By.XPATH, '//input[@data-bind="value: name"]')  #級別名稱
    level_pointtotal = (By.XPATH, '//input[@data-bind="numberInput: pointtotal"]')  #升級條件 >有效投注
    level_deposittotal = (By.XPATH, '//input[@data-bind="numberInput: deposittotal"]')  #升級條件 >存款總額
    level_deposittime = (By.XPATH, '//input[@data-bind="numberInput: deposittime"]')  #升級條件 >存款次數
    level_numcheck_norm = (By.XPATH, '//input[@data-bind="numCheck: feature" and @value="0"]')  #功能 >正常
    level_numcheck_beta = (By.XPATH, '//input[@data-bind="numCheck: feature" and @value="1"]')  #功能 >內測
    level_numcheck_tryo = (By.XPATH, '//input[@data-bind="numCheck: feature" and @value="2"]')  #功能 >試用
    level_numcheck_swab = (By.XPATH, '//input[@data-bind="numCheck: feature" and @value="3"]')  #功能 >刷水
    level_numcheck_bklt = (By.XPATH, '//input[@data-bind="numCheck: feature" and @value="4"]')  #功能 >黑名單
    level_type_on = (By.XPATH,  '//input[(@data-bind="numCheck: locked") and @value="0"]')  #狀態 >未鎖定
    level_type_off = (By.XPATH, '//input[(@data-bind="numCheck: locked") and @value="1"]')  #狀態 >已鎖定
    deposit_otp_off  = (By.XPATH, '//input[@data-bind="numCheck: enabledepositotp" and @value="0"]')  #入款OTP >關閉
    deposit_otp_on = (By.XPATH, '//input[@data-bind="numCheck: enabledepositotp" and @value="1"]')  #入款OTP >開啟
    level_member = (By.XPATH, '//a[contains(@data-bind,"member")]')  #會員數量
    level_balance = (By.XPATH, '//td[@data-bind="text: balance"]')  #會員餘額
    level_credit = (By.XPATH, '//td[@data-bind="text: credit"]')  #會員信用

    btn_submit = (By.XPATH, '//button[@data-y2="submit"]')  #保存按鈕
    btn_esc = (By.XPATH, '//button[@data-y2="esc"]')  #返回按鈕

class LevelManagementPage(BasePage):
    def turn_off_deposit_otp(self):
        self.wait_loading_finish()    
        self.click_all(LevelManagementPageLocator.deposit_otp_off)
        self.click(LevelManagementPageLocator.btn_submit)

    def turn_on_deposit_otp(self):
        self.wait_loading_finish()    
        self.click_all(LevelManagementPageLocator.deposit_otp_on)
        self.click(LevelManagementPageLocator.btn_submit)