from selenium.webdriver.common.by import By
from copy import deepcopy
import math, os, sys

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
from common.web.common import Common

class BasePageLocator:
    # LOADING
    search_loading_mask = (By.XPATH, "//button[@class='btn btn-sm btn-primary']")

    first_page = (By.XPATH, '//a[text()="首页"]')
    last_page = (By.XPATH, '//a[text()="尾页"]')
    today_button = (By.XPATH, '//button[contains(@data-bind, "today")]')                     # 今日 按鈕
    this_month = (By.XPATH, '//button[contains(@data-bind, "showThisMonth")]')               # 本月 按鈕
    last_month = (By.XPATH, '//button[contains(@data-bind, "showLastMonth")]')               # 上月 按鈕
    record_total = (By.XPATH, '//span[@data-bind="text: pager.total"]')                      # 紀錄總數
    search_btn = (By.XPATH, '//button[@id="btnSearch"]')                                     # "查找"按鈕

class BasePage(Common):
    # 等待搜尋Loading消失
    def wait_loading_finish(self):
        self.sleep(1)

        if self.is_element_finded(BasePageLocator.search_loading_mask) is True:
            try:
                self.waitInvisibility(BasePageLocator.search_loading_mask)
            except:
                raise Exception("讀取時間過長,請確認讀取屏蔽視窗")

    # 檢查頁數
    def check_page(self, tab_page=0, record_per_page=25):
        '''
            檢查頁數顯示是否正確
            Args : 
                tab_page : 欲選擇的tab，輸入0或不輸入則不做選擇tab的動作
                record_per_page : 每頁紀錄數下拉式選單的值
        '''
        common = Common(self.driver, self.sec, self.base_url, self.test_skip_method)
        
        self.wait_loading_finish()
        if not common.is_element_finded(BasePageLocator.first_page):
            return

        firstPage = deepcopy(BasePageLocator.first_page)
        lastPage = deepcopy(BasePageLocator.last_page)
        recordTotal = deepcopy(BasePageLocator.record_total)

        if tab_page != 0:
            firstPage = (firstPage[0], '//div[@id="tab_{}"]'.format(tab_page) + firstPage[1])
            lastPage = (lastPage[0], '//div[@id="tab_{}"]'.format(tab_page) + lastPage[1])
            recordTotal = (recordTotal[0], '//div[@id="tab_{}"]'.format(tab_page) + recordTotal[1])
            
        common.sleep(5)
        common.click(locator=lastPage)
        common.sleep(1)
        totalPage = math.ceil(float(common.getText(locator=recordTotal)) / record_per_page)       # 取得總頁數
        totalPage = (By.XPATH, '//a[text()="{}"]'.format(str(totalPage)))
        assert common.isElementDisplayed(totalPage), '頁數顯示錯誤'
