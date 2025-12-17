from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange_wellpay.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common

######## 充值管理 ########
class RechargeAuditPageLocator:

    audit = (By.XPATH, '//tr[1]//div[@class="cell"]//button[@class="el-button el-button--primary el-button--mini"]')
    audit_pass = (By.XPATH, '//button[@class="el-button el-button--primary el-button--mini el-popover__reference"]')
    confirm_audit_pass = (By.XPATH, '(//span[contains(text(), "确定")])[last()]')

class RechargeAuditPage(BasePage):
    def recharge_audit_confirm(self):
        self.click(RechargeAuditPageLocator.audit)
        self.click(RechargeAuditPageLocator.audit_pass)
        self.click(RechargeAuditPageLocator.confirm_audit_pass)
