from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common

######## 買單紀錄-品牌出款 ########
class OrderRecordBrandPageLocator:
    button_transfer_pass = (By.XPATH, "//button/span[contains(text(),'确认转账')]")
    button_transfer_cancel = (By.XPATH, "//button/span[contains(text(),'订单取消')]")
    
    button_confirm_pass = (By.XPATH, '(//span[contains(text(), "确定")])[last()]')

class OrderRecordBrandPage(BasePage):
    # 確認轉帳
    def brand_order_transfer_confirm(self):
        self.wait_visibility(OrderRecordBrandPageLocator.button_transfer_pass)
        self.click(OrderRecordBrandPageLocator.button_transfer_pass)
        self.click(OrderRecordBrandPageLocator.button_confirm_pass)
