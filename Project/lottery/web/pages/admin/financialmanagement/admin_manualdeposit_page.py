from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import random


class ManualDeposit_PageLocator(BasePage):
    # SEARCH AREA (查找條件區)
    add_bill = (By.XPATH, "//a[@class= 'btn btn-default btn-sm']//..//*[contains(.,'单个新增')]")
    add_member = (By.XPATH, "//div[@class='modal-content']//input[contains(@data-bind, 'memberlogin')]")
    money_radio = (By.XPATH, "//input[@type='checkbox' and contains(@data-bind, 'transferamountCheck')]")
    money_input = (By.XPATH, "//input[contains(@data-bind, 'transferamount') and contains(@placeholder, '金额')]")
    save_btn = (By.XPATH, "//button[@class= 'btn blue' and text() = '保存']")
    success = (By.XPATH, "//div[@class= 'toast-message']")
    review = (By.XPATH, "//a[contains(text(), '款项审核')]/..")
    today = (By.XPATH, "//div[@id='mandeposit-tab-group']//button[contains(text(), '今日')]")
    search = (By.XPATH, "//div[@id='mandeposit-tab-group']//button[contains(text(), '查找')]")

    # 搜尋資料區
    check_radio = (By.XPATH, "//input[@class='checkbox-inline']")
    batch_review = (By.XPATH, "//button[contains(., '批量入款')]")


class ManualDepositPage(BasePage):
    def add_bill(self, web_account, money):
        self.wait_loading_finish()
        self.click(ManualDeposit_PageLocator.add_bill)
        self.wait_visibility(ManualDeposit_PageLocator.add_member)

        self.type(ManualDeposit_PageLocator.add_member, web_account)
        self.type(ManualDeposit_PageLocator.money_input, money)
        self.click(ManualDeposit_PageLocator.save_btn)
        
        assert self.get_text(ManualDeposit_PageLocator.success).__contains__('新增成功') or \
            self.get_text(ManualDeposit_PageLocator.success).__contains__('已新增'), '新增人工存入錯誤'

        self.wait_loading_finish()
        self.click(ManualDeposit_PageLocator.today)
        self.click(ManualDeposit_PageLocator.search)
        self.wait_loading_finish()
        self.click(ManualDeposit_PageLocator.check_radio)
        self.click(ManualDeposit_PageLocator.batch_review)
        self.wait_visibility(ManualDeposit_PageLocator.success)
        
        assert self.get_text(ManualDeposit_PageLocator.success).__contains__('成功'), '新增人工存入錯誤'