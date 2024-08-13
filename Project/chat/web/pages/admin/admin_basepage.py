from selenium.webdriver.common.by import By
import os, sys
from common.web.common import Common

class BasePageLocator:
    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

class BasePage(Common):
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(BasePageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(BasePageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")