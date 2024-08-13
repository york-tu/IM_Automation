from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage

class MemberPageLocator:
    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

class MemberPage(BasePage):
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(MemberPageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(MemberPageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")