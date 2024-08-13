from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common

######## 站點管理 ########
class SystemManagementPageLocator:
    # 滑動驗證
    swipe_close = (By.XPATH, "//div[@class='container swipe-verify']//span[text()='关']")
    swipe_open = (By.XPATH, "//div[@class='container swipe-verify']//span[text()='开']")
    swipe_save = (By.XPATH, "//div[@class='container swipe-verify']//span[contains(text(), '储存')]")


    # 短信驗證
    sms_close = (By.XPATH, "//div[@class='container sms-verify']//span[text()='关']")
    sms_open = (By.XPATH, "//div[@class='container ']//span[text()='开']")
    sms_save = (By.XPATH, "//div[@class='container sms-verify']//span[contains(text(), '储存')]")

    message_success = (By.XPATH, "//p[text()='执行成功']")
    confirm = (By.XPATH, "//div[@aria-hidden='false']//span[contains(text(),'确定')]")


class SystemManagementPage(BasePage):
    # 關閉滑動驗證所有項目
    def initialize_swipeverify_setting(self):
        self.wait_visibility(SystemManagementPageLocator.swipe_save)
        self.sleep(1)
        for swipe_closes in self.find_elements(SystemManagementPageLocator.swipe_close):
              self.click_by_dom(swipe_closes) 
        self.wait_visibility(SystemManagementPageLocator.swipe_save)
        self.click(SystemManagementPageLocator.swipe_save)
        self.wait_visibility(SystemManagementPageLocator.confirm)
        self.click(SystemManagementPageLocator.confirm)

        if self.wait_visibility_status(SystemManagementPageLocator.message_success) is False:
            raise EOFError("修改關閉滑動驗證，未顯示執行成功")

    # 關閉短信驗證所有項目
    def initialize_smsverify_setting(self):
        self.wait_visibility(SystemManagementPageLocator.sms_save)
        self.sleep(1)
        for sms_closes in self.find_elements(SystemManagementPageLocator.sms_close):
              self.click_by_dom(sms_closes) 
        self.wait_visibility(SystemManagementPageLocator.sms_save)
        self.click(SystemManagementPageLocator.sms_save)
        self.wait_visibility(SystemManagementPageLocator.confirm)
        self.click(SystemManagementPageLocator.confirm)

        if self.wait_visibility_status(SystemManagementPageLocator.message_success) is False:
            raise EOFError("修改關閉短信驗證，未顯示執行成功")
