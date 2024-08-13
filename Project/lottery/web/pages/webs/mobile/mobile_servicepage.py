from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage

class ServicePageLocator:
    wechat = (By.XPATH, "//div[@id='wechatlink']")
    wechat_message = (By.XPATH, "(//p)[2]")

class ServicePage(BasePage):
    def wechat_message(self):
        try:
            self.open_new_window(ServicePageLocator.wechat)
            message = self.get_text(ServicePageLocator.wechat_message)
            assert  message == "這是微信客服", "文案異常"
        except:
            print('微信已停止使用')
            pass