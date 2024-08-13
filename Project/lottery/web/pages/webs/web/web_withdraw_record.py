from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class WithdrawRecordPageLocator:
    withdraw_tab = (By.XPATH, "//li[contains(text(), '出款记录')]") # 出款記錄按鈕
    exchange_submit = (By.XPATH, "(//a[contains(text(), '确认收到')])[1]") # 確認收到
    pop_submit = (By.XPATH, "//div[text()='确认']") # 二次確認
    
class WithdrawRecordPage(BasePage):
    def exchange_submit(self):
        self.click(WithdrawRecordPageLocator.withdraw_tab)
        self.wait_loading_finish()
        self.click(WithdrawRecordPageLocator.exchange_submit)
        self.click(WithdrawRecordPageLocator.pop_submit)