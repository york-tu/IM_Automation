from selenium.webdriver.common.by import By
from copy import deepcopy
import math,os,getpass,platform
import pandas as pd
import os,platform,getpass,glob, os, sys

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
from common.web.common import Common

class BasePageLocator:
    # LOADING
    first_page = (By.XPATH, '//a[text()="首页"]')
    last_page = (By.XPATH, '//a[text()="尾页"]')
    record_total = (By.XPATH, '//span[@data-bind="text: pager.total"]')                      # 紀錄總數
    search_loading_mask = (By.XPATH, "//div[@class='loading_mask']")

class BasePage(Common):
    # 等待搜尋Loading消失
    def wait_loading_finish(self):
        self.sleep(1)

        if self.is_element_finded(BasePageLocator.search_loading_mask) is True:
            try:
                self.wait_invisibility(BasePageLocator.search_loading_mask)
            except:
                raise Exception("讀取時間過長,請確認讀取屏蔽視窗")
