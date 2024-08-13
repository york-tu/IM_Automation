from selenium.webdriver.common.by import By
import os, sys
from common.web.common import Common

class BasePageLocator:
    # ALL PAGE
    loading_mask = (By.XPATH, "//div[@class='loading__img']")
    login_mask = (By.XPATH, "//div[@class='launch-screen -show']")
    model_title = (By.XPATH, "//div[@class='common-modal__header']")
    message_loading = (By.XPATH, "//div[@class='wcr-system-loading'and @style ='display: none;']")


class BasePage(Common):
    def wait_login_finish(self):
        self.sleep(1)

        if self.is_element_finded(BasePageLocator.login_mask) is True:
            try:
                self.wait_visibility(BasePageLocator.model_title)
            except:
                raise Exception("讀取時間過長,請確認讀取屏蔽視窗")
    
    def wait_message_finish(self):
        self.sleep(1)

        if self.is_element_finded(BasePageLocator.message_loading) is False:
            try:
                self.is_element_displayed(BasePageLocator.message_loading)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")
    
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(BasePageLocator.loading_mask) is False:
            try:
                self.is_element_displayed(BasePageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")