from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage

class RedEnvelopePageLocator:
    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

class RedEnvelopePage(BasePage):
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(RedEnvelopePageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(RedEnvelopePageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")