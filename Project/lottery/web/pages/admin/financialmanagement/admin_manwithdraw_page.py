from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import re
import math

class ManwithdrawPageLocator:
    # SEARCH AREA (查找條件區)
    input_member_account = (By.XPATH, "//input[@data-bind='value: filter.memberlogin']") # 會員帳號
    ledger = (By.XPATH, "//input[contains(@data-bind,'filter.id')]") # 流水號
    operator = (By.XPATH,"//input[contains(@data-bind,'value: filter.addedlogin')]") # 操作者
    input_withdrawal_amount = (By.XPATH, "//input[contains(@data-bind,'value: filter.amount')]") # 提出金額
    btn_today_withdraw_datetime = (By.XPATH, "//button[contains(text(),'今日')]") # 提出時間
    btn_last_month_withdraw_datetime = (By.XPATH, "//button[contains(text(),'上月')]")
    find_shareholder = (By.XPATH,"//textarea[contains(@data-bind,'shareLoginItems')]") # 股東
    find_generalagent = (By.XPATH,"//input[contains(@data-bind,'generalagent')]") # 總代
    find_agent = (By.XPATH,"//span[text()='代理']/following::input[contains(@data-bind,'agent')]") # 代理  
    btn_search = (By.XPATH, "//*[contains(text(),'查找')]") # 查找
    btn_start_time = (By.XPATH, "//input[contains(@data-bind,'starttime')]") # 查找開始時間  
    btn_end_time = (By.XPATH, "//input[contains(@data-bind,'endtime')]") # 查找結束時間

    # RESULT AREA (搜尋結果區)
    member_check = (By.XPATH,"//*[contains(@data-bind,'text: memberlogin')]") # 會員
    actionname_check = (By.XPATH, "//*[contains(@data-bind,'text: actionname')]") # 交易類別
    current = (By.XPATH,"//*[contains(@class,'text-right')]") # 當前金額
    amount = (By.XPATH,"//*[contains(@data-bind,'text: amount')]") # 提出金額
    changed = (By.XPATH,"(//*[contains(@data-bind,'text: changed')])[1]") # 最後金額
    total_pages = (By.XPATH,"//span[contains(@data-bind,'pager.total')]") # 總頁數

    # 第一筆資料
    actionname_check_first = (By.XPATH, "(//*[contains(@data-bind,'text: actionname')])[1]") # 交易類別
    amount_first = (By.XPATH,"(//*[contains(@data-bind,'text: amount')])[1]") # 提出金額
    member_check_first = (By.XPATH,"(//*[contains(@data-bind,'text: memberlogin')])[1]") # 會員

    #  總計
    total_table = (By.XPATH,"//span[text()='总计']/../..//td[@style='white-space: nowrap;']")
    sub_total = (By.XPATH,"//span[contains(@data-bind,'sum.total')]") # 總計*條
    sum_amount = (By.XPATH, "//span[@data-bind='money: sum.amount']") # 提出總計

    # 小計
    sum_subamount = (By.XPATH,"//span[@data-bind='money: sum.subamount']") # 提出小計

    # 新增
    new_withdraw = (By.XPATH, "//a[@href='#dialog']")
    input_member_login = (By.XPATH, "//input[@data-bind='value: memberlogin']")
    input_amount = (By.XPATH, "//input[@data-bind='value: amount']")
    btn_acticnname = (By.XPATH, "//select[contains(@data-bind,'value: actioncode')]/option[text()='重复出款']")
    btn_acticnname1 = (By.XPATH, "//select[contains(@data-bind,'value: actioncode')]/option[text()='其他']")
    input_remark = (By.XPATH, "//textarea[@data-bind='value:remark']")
    btn_submit = (By.XPATH, "//button[text()='保存']")
    btn_close = (By.XPATH, "//button[text()='关闭']")
    # 選擇交易類別
    def option_locator(option_name):
        btn_acticnname = (By.XPATH,f"//select[contains(@data-bind,'value: actioncode')]/option[text()='{option_name}']")
        return btn_acticnname

    # 資料
    total_pages = (By.XPATH,"//span[contains(@data-bind,'pager.total')]") # 總頁數
    page_size = (By.XPATH,"//*[contains(@data-bind,'pageSize')]//option") # 每頁最多顯示筆數 個別
    page_list = (By.XPATH,"//*[contains(@data-bind,'pageSize')]") # 每頁最多筆數 總下拉式選單
    rows = (By.XPATH,"//tbody[@data-bind='foreach: items']//tr") # 列 
    last_page = (By.XPATH, '//a[text()="尾页"]') 

    btn_today_application_datetime = (By.XPATH, "//button[contains(text(),'今日')][1]")
    btn_yesterday_application_datetime = (By.XPATH, "//button[contains(text(),'昨日')][1]")
    btn_this_week_application_datetime = (By.XPATH, "//button[contains(text(),'本周')][1]")
    btn_last_week_application_datetime = (By.XPATH, "//button[contains(text(),'上周')][1]")
    btn_this_month_application_datetime = (By.XPATH, "//button[contains(text(),'本月')][1]")
    btn_last_month_application_datetime = (By.XPATH, "//button[contains(text(),'上月')][1]")
    # 取得特定交易類別金額
    def get_amount_locator(option_name):
        btn_amount = (By.XPATH,f"//td[text()='{option_name}']/../td[@data-bind='text: amount']")
        return btn_amount

    # 下分總攬 page
    btn_today_overview = (By.XPATH, "//button[@qa-button='quick-time-today']")
    man_withdraw_check = (By.XPATH, "//td[8]") # 交易類別
    detail = (By.XPATH, "//span[text()='明细']") # 明細
    input_member_account_overview = (By.XPATH,"//input[@qa-input='member_login']")
    downpage = (By.XPATH, "(//span[@class='el-input__suffix'])[last()]")    # 切換每頁筆數
    page_option = (By.XPATH,"//span[text()='500条/页']")

    # web 額度轉換-主錢包
    web_wellat = (By.XPATH, "(//span[contains(@class,'cp_balance')])[1]") # 主錢包
    transfer_back = (By.XPATH, "//div[contains(@data-bind,'click: transferBack')]") # 一鍵歸戶

class ManwithdrawPage(BasePage):
    def search_today_manpower_by_member(self, account):
        self.wait_loading_finish()
        self.type(ManwithdrawPageLocator.input_member_account, account)
        self.click(ManwithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    
    def pass_manpower(self, account, amount, option = ManwithdrawPageLocator.btn_acticnname):
        self.sleep(1)
        self.click(ManwithdrawPageLocator.new_withdraw)
        self.wait_visibility(ManwithdrawPageLocator.input_member_login)
        self.type(ManwithdrawPageLocator.input_member_login, account)
        self.type(ManwithdrawPageLocator.input_amount, amount)
        self.click(option)
        self.type(ManwithdrawPageLocator.input_remark, "1")
        self.click(ManwithdrawPageLocator.btn_submit)
        self.wait_loading_finish()
    
    def do_all_option(self, account):
        option_list=['重复出款','公司入款误存','会员负数回冲','手动申请出款','扣除非法下注派彩','放弃存款优惠','其他','接入平台余额']
        amount = 10
        # 新增所有人工出款選項
        for option in option_list:
            self.pass_manpower(account, amount, ManwithdrawPageLocator.option_locator(option))
            self.check_option(account, amount, option)
            amount+=10
    
    def check_option(self, account, amount, option):
        self.refresh_browser()
        self.sleep(1)
        self.type(ManwithdrawPageLocator.input_member_account, account)
        self.click(ManwithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        first_option = self.get_text(ManwithdrawPageLocator.actionname_check_first)
        first_amount = self.get_text(ManwithdrawPageLocator.amount_first)
        first_member = self.get_text(ManwithdrawPageLocator.member_check_first)
        assert str(first_member) == str(account), f'第一筆會員應為 {account}, 顯示 {first_member}'
        assert str(first_option) == str(option), f'第一筆交易類別應為 {option}, 顯示 {first_option}'
        assert str(first_amount) == str(amount), f'第一筆提出金額應為 {amount}, 顯示 {first_amount}'

    # 取的當前金額
    def get_wallet(self, web_account):            
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(ManwithdrawPageLocator.input_member_account, web_account)
        self.click(ManwithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        pattern = re.compile(r"(\d+(\.\d+)?)")            
        get_wallet = self.get_text(ManwithdrawPageLocator.changed)
        wallet = float(pattern.search(get_wallet).group())
        return wallet

 
    # 每頁最大筆數測試
    def page_range(self, web_account):
        self.refresh_browser()
        self.type(ManwithdrawPageLocator.input_member_account, web_account)
        self.click(ManwithdrawPageLocator.btn_last_month_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num()

    # 頁數及尾頁餘數數量
    def check_pages(self):
        self.scroll_to_top()
        self.click(ManwithdrawPageLocator.btn_last_month_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.scroll_to_bottom()
        self.check_page() 
    
    # 會員帳號查找
    def search_member(self, web_account):
        self.refresh_browser()
        self.sleep(1)
        self.type(ManwithdrawPageLocator.input_member_account, web_account)
        self.click(ManwithdrawPageLocator.btn_last_month_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()

    # 申請金額查找
    def search_amount(self):
        self.refresh_browser()
        self.type(ManwithdrawPageLocator.input_withdrawal_amount, "300")
        self.click(ManwithdrawPageLocator.btn_last_month_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()

     # 股東/代理/總代
    def check_shareholder_generalagent_agent(self, shareholder, generalagent, agent):        
        self.refresh_browser()
        # 股東
        self.sleep(1)
        self.type(ManwithdrawPageLocator.find_shareholder,shareholder)
        self.click(ManwithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        shareholder_cnt = self.get_text(ManwithdrawPageLocator.total_table)  # 股東筆數
        assert shareholder_cnt != 0, '股東筆數為0'

        # 總代
        self.type(ManwithdrawPageLocator.find_shareholder, "")
        self.sleep(1)
        self.type(ManwithdrawPageLocator.find_generalagent, generalagent)   
        self.click(ManwithdrawPageLocator.btn_search)                        
        self.wait_loading_finish()
        generalagent_cnt = self.get_text(ManwithdrawPageLocator.total_table) # 總代筆數
        assert generalagent_cnt != 0, '總代筆數為0'

        # 代理
        self.type(ManwithdrawPageLocator.find_generalagent, "")
        self.sleep(1)
        self.type(ManwithdrawPageLocator.find_agent, agent)                 
        self.click(ManwithdrawPageLocator.btn_search)                        
        self.wait_loading_finish()
        agent_cnt = self.get_text(ManwithdrawPageLocator.total_table)        # 代理筆數
        assert agent_cnt != 0, '代理筆數為0'
        assert shareholder_cnt == generalagent_cnt == agent_cnt, '股東、總代、代理 筆數不相符'

    # 下分總攬
    def ledger_manpower(self, web_account):
        self.refresh_browser()
        self.type(ManwithdrawPageLocator.input_member_account_overview, web_account)
        self.sleep(0.5)
        self.click(ManwithdrawPageLocator.btn_today_overview)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.click(ManwithdrawPageLocator.downpage)
        self.click(ManwithdrawPageLocator.page_option)
        self.wait_loading_finish()
        self.scroll_to_top()
        manwithdraw = self.get_text(ManwithdrawPageLocator.man_withdraw_check)
        assert manwithdraw == '人工提出', '下分總攬第一筆資料交易類別不為人工提出'
        self.click(ManwithdrawPageLocator.detail)
        self.switch_last_page()
        self.wait_loading_finish()
        self.sleep(2)
        assert self.is_element_finded(ManwithdrawPageLocator.rows) is True, '未自動查找，查無資料'
        self.type(ManwithdrawPageLocator.input_member_account, web_account)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.switch_home_page()
    
    # 總計跟小計
    def check_total_subtotal(self, web_account):
        # 資料的處理
        def get_details():
            pattern = re.compile(r"(\d+(\.\d+)?)")
            total_data = list()
            record_number = int(self.get_text(ManwithdrawPageLocator.total_pages))
            for index in range(record_number):                
                amount_path = (By.XPATH, "(//*[contains(@data-bind,'text: amount')])[{}]".format(index+1))
                get_amount = self.get_text(amount_path)
                amount = float(pattern.search(get_amount).group())

                data = {
                    "amount": amount
                }
                total_data.append(data)
            return total_data
        
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(ManwithdrawPageLocator.input_member_account, web_account)
        self.click(ManwithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        pages = math.ceil(int(self.get_text(ManwithdrawPageLocator.total_pages)) / 500) # 抓換500筆檢視 共有幾頁
        # 換頁
        if pages > 1:
            self.click((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(pages)))
            self.wait_loading_finish()
        
        # 提出加總
        total_data = get_details()
        total_amount = 0
        page_cnt = 1
        for i in range(len(total_data)):
            total_amount = total_data[i]["amount"] + total_amount

            # 存當頁的 提出金額
            this_page_amount = total_amount

            if (i+1)%500 == 0:
                break # 要抓取大於500筆 把break掉
                page_cnt += 1
                if self.is_element_finded((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(page_cnt))):
                    self.click((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(page_cnt)))
                    self.wait_loading_finish()
                    total_data = get_details()
            
        # 小計資料整理
        sum_subamount = self.get_text(ManwithdrawPageLocator.sum_subamount)
        sum_subamount = float((sum_subamount).replace(',', ''))

        # 總計資料整理
        amount = self.get_text(ManwithdrawPageLocator.sum_amount)
        amount = float((amount).replace(',', ''))

        # 判斷小計資料是否相同
        assert round(this_page_amount, 2) == sum_subamount, 'error number equal'

        # 判斷總計跟小計相同
        assert round(this_page_amount, 2) == amount, 'error number equal'

    # 取得比對財務報表所需的資料
    def get_withdrawal_data(self, reseller_account, time=''):
        self.wait_visibility(ManwithdrawPageLocator.btn_today_application_datetime)
        if time == '' or time == '1':
            self.click(ManwithdrawPageLocator.btn_today_application_datetime)
        elif time == '2':
            self.click(ManwithdrawPageLocator.btn_yesterday_application_datetime)
        elif time == '3':
            self.click(ManwithdrawPageLocator.btn_this_week_application_datetime) 
        elif time == '4':
            self.click(ManwithdrawPageLocator.btn_last_week_application_datetime)  
        elif time == '5':
            self.click(ManwithdrawPageLocator.btn_this_month_application_datetime) 
        elif time == '6':
            self.click(ManwithdrawPageLocator.btn_last_month_application_datetime)  

        self.wait_visibility(ManwithdrawPageLocator.find_agent)
        self.type(ManwithdrawPageLocator.find_agent, reseller_account)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        if self.is_element_finded(ManwithdrawPageLocator.member_check) is False:
            sum_amount = "0.00"
            return sum_amount
        
        sum_amount = str(self.get_text(ManwithdrawPageLocator.sum_amount)).replace(',', '')
        
        return  sum_amount

    # 取得特定交易類別金額
    def get_option_withdraw(self, shareholder, time='1', option='手动申请出款'):
        self.wait_visibility(ManwithdrawPageLocator.btn_today_application_datetime)
        if time == '' or time == '1':
            self.click(ManwithdrawPageLocator.btn_today_application_datetime)
        elif time == '2':
            self.click(ManwithdrawPageLocator.btn_yesterday_application_datetime)
        elif time == '3':
            self.click(ManwithdrawPageLocator.btn_this_week_application_datetime) 
        elif time == '4':
            self.click(ManwithdrawPageLocator.btn_last_week_application_datetime)  
        elif time == '5':
            self.click(ManwithdrawPageLocator.btn_this_month_application_datetime) 
        elif time == '6':
            self.click(ManwithdrawPageLocator.btn_last_month_application_datetime)  

        self.wait_visibility(ManwithdrawPageLocator.find_shareholder)
        self.type(ManwithdrawPageLocator.find_shareholder,shareholder)
        self.click(ManwithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        
        total_amount = 0
        amounts = self.find_elements(ManwithdrawPageLocator.get_amount_locator(option))
        for idx in range(len(amounts)):
            total_amount += float(self.get_text_by_dom(amounts[idx]))

        return total_amount





