from selenium.webdriver.common.by import By
import pandas as pd
from common.web.common import Common

class BaseLocator:
    # LOADING 
    login_account = (By.XPATH, '//input[@placeholder="账号"]')
    login_password = (By.XPATH, '//input[@placeholder="密码"]')
    login_button = (By.XPATH, '//button//span')

    first_page = (By.XPATH, '//a[text()="首页"]')
    last_page = (By.XPATH, '//a[text()="尾页"]')
    record_total = (By.XPATH, '//span[@data-bind="text: pager.total"]')                     # 紀錄總數
    search_loading_mask = (By.XPATH, "//button[@class='btn btn-sm btn-primary']")
    last_page_v2 = (By.XPATH, "//li[contains(@class,'number')][last()]")
    record_total_v2 = (By.XPATH, "//span[@class='el-pagination__total']")                      # 共 * 条
    rows_total_v2 = (By.XPATH, "//table[@class='el-table__body']//tr//div[contains(text(),'总计')]")    # 紀錄總數


class BasePage(Common):
    # 等待搜尋Loading消失
    def wait_loading_finish(self):
        self.sleep(1)

        if self.is_element_finded(BaseLocator.search_loading_mask) is True:
            try:
                self.wait_invisibility(BaseLocator.search_loading_mask)
            except:
                raise Exception("讀取時間過長,請確認讀取屏蔽視窗")