from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import re
import math

class WithdrawGeneralPageLocator:
    # SEARCH AREA (查找條件區)
    input_member_account = (By.XPATH, '//input[@qa-input="member_login"]')          # 會員帳號
    btn_today = (By.XPATH, '//button[@qa-button="quick-time-today"]')            # 今日按鈕
    btn_yesterday = (By.XPATH, '//button[@qa-button="quick-time-yestoday"]')     # 昨日按鈕
    btn_this_week = (By.XPATH, '//button[@qa-button="quick-time-thisWeek"]')     # 本周按鈕
    btn_last_week = (By.XPATH, '//button[@qa-button="quick-time-lastWeek"]')     # 上周按鈕
    btn_this_month = (By.XPATH, '//button[@qa-button="quick-time-thisMonth"]')   # 本月按鈕
    btn_last_month = (By.XPATH, '//button[@qa-button="quick-time-lastMonth"]')   # 上月按鈕
    btn_search = (By.XPATH, '//button[@qa-button="search"]')
    input_agent = (By.XPATH, '//input[@qa-input="agent"]')                                              # 代理輸入框
    input_generalagent = (By.XPATH, '//input[@qa-input="generalagent"]')                                # 總代輸入框
    input_shareholder = (By.XPATH, '//div[@qa-select="sharelogin"]//input[@class="el-input__inner"]')   # 股東輸入框
    member_level1 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '一级会员')]") # 一級會員
    member_level2 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '二级会员')]") # 二級會員
    member_level4 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '四级会员')]") # 四級會員
    member_automated = (By.XPATH, "//label[text()='会员级别']//..//label[contains(. , 'automated_test')]")
    del_input_shareholder = (By.XPATH,"//div[@qa-select='sharelogin']//i[@class='el-tag__close el-icon-close']")    #刪除股東

    btn_start_time = (By.XPATH, "//input[@placeholder='开始时间']")     # 查找開始時間  
    btn_end_time = (By.XPATH, "//input[@placeholder='结束时间']")       # 查找結束時間 
    search_down = (By.XPATH,"//i[@class='el-icon-arrow-down']")

    # 總計
    total_table = (By.XPATH,"//div[contains(text(),'总计')]/../../td[@class='el-table_1_column_9 is-center ']")  # 含申請金額、实际出款金额
    sub_total = (By.XPATH,"//tbody/tr[last()]//div[contains(text(),'总计')]")     # 列表_共幾條紀錄 (ex:总计 (29))[4:-1]
    sum_withdraw = (By.XPATH,"//div[contains(text(),'总计')]/../..//*[contains(text(),'申请金额')]/span[2]")    # 实际出款金额總計
    sum_amount = (By.XPATH,"//div[contains(text(),'总计')]/../..//*[contains(text(),'申请金额')]/span[1]")      # 申請總計
   
   # RESULT AREA (搜尋結果區)
    member_check = (By.XPATH,"//td[contains(@class,'el-table_1_column_3')]") # 會員
    man_withdraw_check = (By.XPATH, "//td[contains(@class,'el-table_1_column_8')]//span[text()='人工提出']")    # 交易類別-人工提出
    withdraw_check = (By.XPATH, "//td[contains(@class,'el-table_1_column_8')]//span[text()='出款申请']")        # 交易類別-出款申請
    amount = (By.XPATH, "//td[contains(@class,'el-table_1_column_9')]//span[1]")            # 申請金額(含總計)
    tansfer_amount = (By.XPATH, "//td[contains(@class,'el-table_1_column_9')]//span[2]")    # 實際出款費用(含總計)
    detail = (By.XPATH, "//a[@qa-link='gowithdraw']") # 明細
    
    # 資料
    total_pages = (By.XPATH,"//span[@class='el-pagination__total']")        # 頁表_共幾條紀錄 (ex:共 4 条)[2:-2]
    page_size = (By.XPATH, "//span[contains(text(),'条/页')]")              # 每頁最多顯示筆數 個別
    page_size_500 = (By.XPATH, "//span[contains(text(),'500条/页')]")
    page_list = (By.XPATH,"//span[@class='el-pagination__sizes']")          # 每頁最多筆數 總下拉式選單
    last_page = (By.XPATH, "//li[contains(@class,'number')][last()]") 
    input_page_jump = (By.XPATH, "//span[@class='el-pagination__jump']//input")   #前往_頁
    rows = (By.XPATH, "//table[@class='el-table__body']//tr")        # 列(含總計)

    # 出款申請/人工提出流水號
    ledger_withdraw = (By.XPATH, "//input[contains(@data-bind,'filter.id')]") 
    ledger_manpower = (By.XPATH, "//input[contains(@data-bind,'filter.id')]")

class WithdrawGeneralPage(BasePage):
    def get_sum_info(self,reseller_account,time=''):
        self.type(WithdrawGeneralPageLocator.input_agent, reseller_account)
        # self.click(WithdrawGeneralPageLocator.btn_last_month_application_datetime) # 測試用
        
        if time == '':
            today_start = self.get_us_time().strftime("%Y-%m-%d 00:00")
            now=  self.get_us_time().strftime("%M")
        
            if int(now) > 29 : # 確保遊戲報表能回來
                today_end = self.get_us_time().strftime("%Y-%m-%d %H:29")
            else:
                today_end = (self.get_us_time() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:29")
                
            self.type(WithdrawGeneralPageLocator.btn_start_time, today_start)  # 因每小時的30分會更新,故搜尋31-29分
            self.type(WithdrawGeneralPageLocator.btn_end_time, today_end)  
        elif time == '1':
            self.click(WithdrawGeneralPageLocator.btn_today)
        elif time == '2':
            self.click(WithdrawGeneralPageLocator.btn_yesterday)
        elif time == '3':
            self.click(WithdrawGeneralPageLocator.btn_this_week)
        elif time == '4':
            self.click(WithdrawGeneralPageLocator.btn_last_week)
        elif time == '5':
            self.click(WithdrawGeneralPageLocator.btn_this_month)
        elif time == '6':
            self.click(WithdrawGeneralPageLocator.btn_last_month)

        # self.click(WithdrawGeneralPageLocator.status)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        self.sleep(3)
        
        if self.is_element_finded(WithdrawGeneralPageLocator.member_check) is False:
            withdraw_general_record = {
                'withdraw_amount': "0.00",
                'Withdraw_apply': "0.00",
                'withdraw_total': "0",
            }
            return withdraw_general_record

        withdraw_general_amount = float(str(self.get_text(WithdrawGeneralPageLocator.sum_withdraw)).replace(',', ''))
        withdraw_general_apply = float(str(self.get_text(WithdrawGeneralPageLocator.sum_amount)).replace(',', ''))
        withdraw_general_total = str(self.get_text(WithdrawGeneralPageLocator.sub_total))[4:-1].replace(',', '')
        
        withdraw_general_record = {
            'withdraw_amount': "%.2f" %withdraw_general_amount, # 出款
            'Withdraw_apply': "%.2f" %withdraw_general_apply, # 申請
            'withdraw_total': withdraw_general_total, # 總計*條
        }
        return withdraw_general_record
    
     
    def search_today_withdraw_general_by_member(self, account):
        self.type(WithdrawGeneralPageLocator.input_member_account, account)
        self.click(WithdrawGeneralPageLocator.btn_today)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        

     # 每頁最大筆數測試
    def page_range(self, web_account):
        self.type(WithdrawGeneralPageLocator.input_member_account, web_account)
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num_v2()

    # 頁數及尾頁餘數數量
    def check_pages(self):
        self.scroll_to_top()
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        self.scroll_to_bottom()
        self.check_page() 
    
    # 會員帳號查找
    def search_member(self, web_account):
        self.refresh_browser()
        self.sleep(1)
        self.type(WithdrawGeneralPageLocator.input_member_account, web_account)
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 股東/代理/總代
    def check_shareholder_generalagent_agent(self, shareholder, generalagent, agent):        
        self.refresh_browser()
        # 股東
        self.sleep(1)
        self.type(WithdrawGeneralPageLocator.input_shareholder, shareholder)
        dropdown_shareholder=(By.XPATH, "//span[contains(text(),'"+ shareholder+"')]")
        self.wait_visibility(dropdown_shareholder)
        self.click(dropdown_shareholder)
        self.click(WithdrawGeneralPageLocator.btn_today)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        shareholder_cnt = (self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2]  # 股東筆數
        assert shareholder_cnt != '0', '股東筆數為0'

        # 總代
        assert self.is_element_finded(WithdrawGeneralPageLocator.search_down) == False, "查找條件預設不應收合"
        self.wait_visibility(WithdrawGeneralPageLocator.input_shareholder)
        self.click(WithdrawGeneralPageLocator.del_input_shareholder)
        self.sleep(1)
        self.type(WithdrawGeneralPageLocator.input_generalagent, generalagent)   
        self.click(WithdrawGeneralPageLocator.btn_search)                        
        self.wait_loading_finish()
        generalagent_cnt = (self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2] # 總代筆數
        assert generalagent_cnt != '0', '總代筆數為0'

        # 代理
        assert self.is_element_finded(WithdrawGeneralPageLocator.search_down) == False, "查找條件預設不應收合"
        self.wait_visibility(WithdrawGeneralPageLocator.input_generalagent)
        self.type(WithdrawGeneralPageLocator.input_generalagent, "")
        self.sleep(1)
        self.type(WithdrawGeneralPageLocator.input_agent, agent)                 
        self.click(WithdrawGeneralPageLocator.btn_search)                        
        self.wait_loading_finish()
        agent_cnt = (self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2]        # 代理筆數
        assert agent_cnt != '0', '代理筆數為0'
        assert shareholder_cnt == generalagent_cnt == agent_cnt, '股東、總代、代理 筆數不相符'
    
    # 層級
    def search_via_level(self):
        # automated_test-無資料
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(1)
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.member_automated)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        assert ((self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2]) == '0', '會員層級中不應該找到該會員'

        # 一級&二級會員-有資料
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(WithdrawGeneralPageLocator.member_level1)
        self.click(WithdrawGeneralPageLocator.member_level2)
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        assert ((self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2]) != '0', '會員層級中應有資料'
        self.wait_loading_finish()
    
    # 出款申請明細
    def detail_withdraw(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawGeneralPageLocator.input_member_account, web_account)
        self.click(WithdrawGeneralPageLocator.btn_today)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.is_element_finded(WithdrawGeneralPageLocator.rows) == True, "下分總覽無資料"
        self.click(WithdrawGeneralPageLocator.page_list)
        self.click(WithdrawGeneralPageLocator.page_size_500)
        self.wait_loading_finish()
        self.scroll_to_top() 
        self.wait_loading_finish()
        withdraw = self.get_text(WithdrawGeneralPageLocator.withdraw_check)

        assert withdraw == '出款申请', r"交易类别錯誤, 應為'出款申请'"

        self.click(WithdrawGeneralPageLocator.detail)           
        self.sleep(1)
        self.switch_home_page()
    
    # 人工提出明細
    def detail_manpower(self, web_account):
        self.refresh_browser()
        self.type(WithdrawGeneralPageLocator.input_member_account, web_account)
        self.click(WithdrawGeneralPageLocator.btn_today)
        self.click(WithdrawGeneralPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.is_element_finded(WithdrawGeneralPageLocator.rows) == True, "下分總覽無資料"
        self.click(WithdrawGeneralPageLocator.page_list)
        self.click(WithdrawGeneralPageLocator.page_size_500)
        self.wait_loading_finish()
        self.scroll_to_top()  
        self.wait_loading_finish()
        # manwithdraw = self.get_text(WithdrawGeneralPageLocator.man_withdraw_check)
        man_withdraw = self.get_text(WithdrawGeneralPageLocator.man_withdraw_check)

        # assert manwithdraw == '人工出款'
        assert man_withdraw == "人工提出", r"交易类别錯誤, 應為'人工提出'"
        
        self.click(WithdrawGeneralPageLocator.detail)
        self.switch_home_page()

    # 總計
    def check_total_subtotal(self, web_account):

        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawGeneralPageLocator.input_member_account,web_account)
        self.click(WithdrawGeneralPageLocator.btn_last_month)
        self.click(WithdrawGeneralPageLocator.btn_search)

        self.click(WithdrawGeneralPageLocator.page_list)
        self.click(WithdrawGeneralPageLocator.page_size_500)

        self.wait_loading_finish()

        pages = math.ceil(int((self.get_text(WithdrawGeneralPageLocator.total_pages))[2:-2]) / 500) # 抓換500筆檢視 共有幾頁

        total_amount = 0
        total_tansfer_amount = 0

        for page in range(1,pages+1):
            if page > 1:
                self.type(WithdrawGeneralPageLocator.input_page_jump,str(page))
                self.type_enter(WithdrawGeneralPageLocator.input_page_jump)
                self.wait_loading_finish()
            sub_amount, sub_tansfer_amount = self.get_details()
            total_amount+=sub_amount
            total_tansfer_amount+=sub_tansfer_amount
        
        # 總計資料整理
        amount_money = float((self.get_text(WithdrawGeneralPageLocator.sum_amount)).replace(',',''))       #申請金額 總計
        withdraw_money = float((self.get_text(WithdrawGeneralPageLocator.sum_withdraw)).replace(',',''))   #實際出款金額 總計

        # 判斷總計跟每頁總計相同
        assert round(total_amount, 2) == amount_money, 'error number equal'
        assert round(total_tansfer_amount, 2) == withdraw_money, 'error number equal'


    # 資料的處理
    def get_details(self):
        amount_list=[]
        tansfer_amount_list=[]
    
        for ele in self.find_elements(WithdrawGeneralPageLocator.amount):
            amount_list.append(float(ele.text.replace(',', '')))
        amount_list.pop()   #去除總計

        for ele in self.find_elements(WithdrawGeneralPageLocator.tansfer_amount):
            tansfer_amount_list.append(float(ele.text.replace(',', '')))
        tansfer_amount_list.pop()   #去除總計

        return sum(amount_list), sum(tansfer_amount_list)

         

            




        


