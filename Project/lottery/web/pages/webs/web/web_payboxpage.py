from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class PayBoxPageLocator:
     # pyabox
    pay_box_order = (By.ID, 'orderCode')
    pay_box_money = (By.XPATH, "//span[text()= '转账金额(元):']/following::span")
    pay_box_title = (By.XPATH, "//h2[text()= '收银台']")
    pay_box_user = (By.XPATH, "(//*[text() = '复制']/..//span)[1]")
    pay_box_account = (By.XPATH, "(//*[text() = '复制']/..//span)[2]")
    success = (By.XPATH, "//span[text()='本次转账已完成']")
    name = (By.XPATH, f"//span[text()='蛊惑江湖']")   
    pay_box_wait_status = (By.XPATH, "//span[text()='订单排队中，请耐心等待...']")
    pay_box_show_status = (By.XPATH, "//div[contains(text(),'扫一扫')]")

    def user_name(self, name):
        name = (By.XPATH, f"//span[text()='{name}']") 
        return name

class PayBoxPage(BasePage):
    def get_info(self, money):
        money = '%.2f'%float(money)
        self.wait_visibility(PayBoxPageLocator.pay_box_title)
        order = self.get_text(PayBoxPageLocator.pay_box_order)
        pay_box_money = self.get_text(PayBoxPageLocator.pay_box_money)
        
        assert str(pay_box_money) == str(money), "金額錯誤"
        # assert self.is_element_finded(PayBoxPageLocator.pay_box_wait_status), "收銀台彈窗顯示狀態異常, 應為订单排队中"
        
        return order
    
    def check_order(self, name):
        result = self.is_element_finded(PayBoxPageLocator.user_name(self, name))
        self.switch_home_page()
        if result is False:
            raise EOFError('收款人名稱不對')
        
    def check_qrcode_show(self):
        result = self.is_element_finded(PayBoxPageLocator.pay_box_show_status)
        self.switch_home_page()
        if result is False:
            raise EOFError('收銀台彈窗，固定積分二維碼未顯示')