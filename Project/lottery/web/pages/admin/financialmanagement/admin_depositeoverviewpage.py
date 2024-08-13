from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, re

class DepositeOverviewPageLocator:
    # SEARCH AREA (查找條件區)
    input_member_account = (By.XPATH, '//input[@qa-input="member_login"]')          # 會員帳號
    btn_today = (By.XPATH, '//button[@qa-button="quick-time-today"]')            # 今日按鈕
    btn_yesterday = (By.XPATH, '//button[@qa-button="quick-time-yestoday"]')     # 昨日按鈕
    btn_this_week = (By.XPATH, '//button[@qa-button="quick-time-thisWeek"]')     # 本周按鈕
    btn_last_week = (By.XPATH, '//button[@qa-button="quick-time-lastWeek"]')     # 上周按鈕
    btn_this_month = (By.XPATH, '//button[@qa-button="quick-time-thisMonth"]')   # 本月按鈕
    btn_last_month = (By.XPATH, '//button[@qa-button="quick-time-lastMonth"]')   # 上月按鈕
    btn_search = (By.XPATH, '//button[@qa-button="search"]')                        # 查找按鈕
    input_agent = (By.XPATH, '//input[@qa-input="agent"]')                          # 代理輸入框
    input_generalagent = (By.XPATH, '//input[@qa-input="generalagent"]')            # 總代輸入框
    input_shareholder = (By.XPATH, '//div[@qa-select="sharelogin"]//input[@class="el-input__inner"]')   # 股東輸入框

    member_level = (By.XPATH,"//div[@class='ps-query-container__optional']")    #會員級別區
    member_level1 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '一级会员')]") # 一級會員
    member_level2 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '二级会员')]") # 二級會員
    member_level3 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '三级会员')]") # 三級會員
    search_down = (By.XPATH,"//i[@class='el-icon-arrow-down']")

    # 上分總攬 RESULT AREA (搜尋結果區)
    total_record = (By.XPATH,"//span[@class='el-pagination__total']")     # 共幾條紀錄 (ex:共 4 条)
    # 第一筆資料
    time = (By.XPATH, "(//td[contains(@class,'el-table_1_column_1')])[1]") # 申請時間
    level = (By.XPATH, "(//td[contains(@class,'el-table_1_column_2')])[1]") # 層級
    member_name = (By.XPATH, "(//td[contains(@class,'el-table_1_column_3')])[1]") # 會員
    agent = (By.XPATH, "(//td[contains(@class,'el-table_1_column_4')])[1]") # 代理
    generalagent = (By.XPATH, "(//td[contains(@class,'el-table_1_column_5')])[1]") # 總代
    shareholder = (By.XPATH, "(//td[contains(@class,'el-table_1_column_6')])[1]") # 股東
    pay_money = (By.XPATH, "(//*[contains(text(),'转账金额')]/span[1])[1]") # 轉帳金額
    currency_code = (By.XPATH, "(//td[contains(@class,'el-table_1_column_7')])[1]") # 幣別
    category_code_name = (By.XPATH, "(//td[contains(@class,'el-table_1_column_8')])[1]") # 交易類別


class DepositeOverviewPage(BasePage):
    def search_today_deposit_by_member(self, account):
        self.type(DepositeOverviewPageLocator.input_member_account, account)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 所有查找方式
    def search_all(self, web_account, admin_account, agent, generalagent, shareholder, money):
   
        # self.search_via_member_name(web_account, admin_account, agent, generalagent, shareholder, money)  # 透過會員帳號進行查找
        self.search_via_shareholder(web_account, admin_account, agent, generalagent, shareholder, money)  # 透過股東進行查找   #lv股東太多導致下拉選單沒出現bot的股東，已開單處理 PFREQ-1985
        self.search_via_generalagent(web_account, admin_account, agent, generalagent, shareholder, money)  # 透過總代進行查找
        self.search_via_agent(web_account, admin_account, agent, generalagent, shareholder, money)  # 透過代理進行查找
        self.search_via_level(web_account, admin_account, agent, generalagent, shareholder, money)  # 透過層級進行查找

    def search_via_member_name(self, web_account, admin_account, agent, generalagent, shareholder, money):
        self.type(DepositeOverviewPageLocator.input_member_account, web_account)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, admin_account, agent, generalagent, shareholder, money)

    # 股東搜尋
    def search_via_shareholder(self, web_account, admin_account, agent, generalagent, shareholder, money):
        self.type(DepositeOverviewPageLocator.input_shareholder, shareholder)
        dropdown_shareholder=(By.XPATH, "//span[contains(text(),'"+ shareholder+"')]")
        self.wait_visibility(dropdown_shareholder)
        self.click(dropdown_shareholder)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, admin_account, agent, generalagent, shareholder, money)

    # 總代搜尋
    def search_via_generalagent(self, web_account, admin_account, agent, generalagent, shareholder, money):
        self.type(DepositeOverviewPageLocator.input_generalagent, generalagent)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, admin_account, agent,generalagent, shareholder, money)

    # 代理搜尋
    def search_via_agent(self, web_account, admin_account, agent, generalagent, shareholder, money):
        self.type(DepositeOverviewPageLocator.input_agent, agent)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, admin_account, agent, generalagent, shareholder, money)

    # 層級搜尋
    def search_via_level(self, web_account, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(DepositeOverviewPageLocator.search_down) == False, "查找條件預設不應收合"
        # 一級會員(無資料)
        self.type(DepositeOverviewPageLocator.input_member_account,web_account)
        self.click(DepositeOverviewPageLocator.btn_today)
        self.click(DepositeOverviewPageLocator.member_level3)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()
        assert (self.get_text(DepositeOverviewPageLocator.total_record))[2:-2] == '0', '會員層級中不應該找到該會員'
        self.click(DepositeOverviewPageLocator.member_level3)

        # 二級會員(有資料)
        self.click(DepositeOverviewPageLocator.member_level1)
        self.click(DepositeOverviewPageLocator.member_level2)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()
        self.check_all_info(web_account, admin_account, agent, generalagent, shareholder, money)


    # 檢查各欄位名稱
    def check_all_info(self, web_account, admin_account, agent, generalagent, shareholder, money):
        today = self.get_us_time().strftime("%Y-%m-%d")

        assert str(self.get_text(DepositeOverviewPageLocator.time)).__contains__(today), '入款時間顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.level).__contains__('级会员'), '會員層級顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.member_name) == web_account, '會員名稱顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.agent) == agent, '代理名稱顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.generalagent) == generalagent, '總理名稱顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.shareholder) == shareholder, '股東名稱顯示不正確'
        
        assert self.get_text(DepositeOverviewPageLocator.pay_money).replace(',', '') == money[self.get_text(DepositeOverviewPageLocator.category_code_name)], '金額信息轉帳金額顯示不正確'
        
        assert self.get_text(DepositeOverviewPageLocator.currency_code ) == 'RMB', '幣別顯示不正確'
        assert self.get_text(DepositeOverviewPageLocator.category_code_name ) == '在线入款' or \
            self.get_text(DepositeOverviewPageLocator.category_code_name ) == '公司入款' or \
            self.get_text(DepositeOverviewPageLocator.category_code_name ) == '人工存入', '交易類別顯示不正確'

        self.refresh_browser()
        self.wait_loading_finish()
        self.scroll_to_top()

    # 每頁最大筆數測試
    def page_range(self,web_account):
        self.type(DepositeOverviewPageLocator.input_member_account, web_account)
        self.click(DepositeOverviewPageLocator.btn_last_month)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num_v2()
        self.scroll_to_top()

    def check_pages(self):
        self.click(DepositeOverviewPageLocator.btn_last_month)
        self.click(DepositeOverviewPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_page() 
        self.scroll_to_top()