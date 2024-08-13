from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class AdminThirdPartyLedgerPageLocator:
    # 第三方現金流水
    third_party_ledger = (By.XPATH, '//div[contains(text(), "第三方上下分流水")]')
    # 查找條件
    account_input = (By.XPATH, "//div[@id='pane-WallethistoryList']//input[@qa-input='memberlogin']")
    today_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-today']")                # "今日"按鈕
    yesterday_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-yestoday']")         # "昨日"按鈕
    this_week_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-thisWeek']")         # "本周"按鈕
    last_week_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-lastWeek']")         # "上周"按鈕
    this_month_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-thisMonth']")       # "本月"按鈕
    last_month_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='quick-time-lastMonth']")       # "上月"按鈕
    transacion_time_start = (By.XPATH, "//div[@id='pane-WallethistoryList']//input[@placeholder='开始时间']")           # 交易時間 開始日期
    transacion_time_end = (By.XPATH, "//div[@id='pane-WallethistoryList']//input[@placeholder='结束时间']")             # 交易時間 結束日期
    search_btn = (By.XPATH, "//div[@id='pane-WallethistoryList']//button[@qa-button='search']")                         # "查找"按鈕
    # message
    wallet_message = (By.XPATH, "//div[@class='el-form-item__error']")                                                  # 錢包代碼必填訊息
    empty_message = (By.XPATH, "//div[@id='pane-WallethistoryList']//span[contains(text(),'暂无数据')]")                # 列表暫無數據訊息      

    # 交易類型
    def transaction_type_check_box(self, text):
        return (By.XPATH, f'//div[@id="pane-WallethistoryList"]//label[contains(text(), "交易类型")]/..//label[contains(., "{text}")]')

    # 錢包代碼
    def wallet_code_check_box(self, text):
        return (By.XPATH, f'//div[@id="pane-WallethistoryList"]//div[@class="query-levelCheck"]//label[contains(., "{text}")]')

    # 交易列表
    transaction_time = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_12 is-center " and @colspan="1"]')     # 交易時間
    member_account = ( By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_13 is-center " and @colspan="1"]')      # 會員帳號
    wallet_code = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_14 is-center " and @colspan="1"]')          # 錢包代碼
    transaction_type = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_15 is-center " and @colspan="1"]')     # 交易類型
    business_number = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_16 is-left " and @colspan="1"]//span[@role="button"]')        # 業務號碼
    current_amount = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_17 is-right " and @colspan="1"]')        # 當前餘額
    transaction_amount = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_18 is-right " and @colspan="1"]')    # 交易餘額
    final_amount = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_19 is-right " and @colspan="1"]')          # 最後餘額
    amount_per_page = (By.XPATH, "(//div[@class='ps-pager'])[2]//span[@class='el-pagination__sizes']//input")                           # 每頁紀錄數
    amount_per_page_options = (By.XPATH, "(//ul[contains(@class,'el-select-dropdown__list')])[last()]//li")                             # 每頁紀錄數的所有選項
    per_page = (By.XPATH, "//div[@x-placement='top-start']//li[contains(@class,'selected')]//span[contains(text(),'条/页')]")
    remark = (By.XPATH, '//div[@id="pane-WallethistoryList"]//td[@class="el-table_2_column_20 is-center " and @colspan="1"]')           # 備註
    total_record = (By.XPATH, "//div[@id='pane-WallethistoryList']//span[@class='el-pagination__total']")                               # 總紀錄數 (ex:共 3 条)
    first_page = (By.XPATH, "//div[@id='pane-WallethistoryList']//ul[@class='el-pager']/li[1]")                                         # "首頁"按鈕
    last_page = (By.XPATH, "//div[@id='pane-WallethistoryList']//ul[@class='el-pager']/li[last()]")                                     # "尾頁"按鈕

    # 業務號碼
    company_deposit = (By.XPATH, '(//span[contains(text(),"公司入款(优惠)")])[last()]')                                         # 公司入款(優惠)
    online_deposit = (By.XPATH, '(//span[contains(text(),"在线入款(优惠)")])[last()]')                                          # 在線入款(優惠)
    artificial_deposit = (By.XPATH, '(//span[contains(text(),"人工入款(优惠)")])[last()]')                                      # 人工入款(優惠)
    order_center = (By.XPATH, '(//span[contains(text(),"注单/返水")])[last()]')                                           # 注單/返水
    online_withdraw = (By.XPATH, '(//span[contains(text(),"在线提现")])[last()]')                                         # 在線提現
    artificial_withdraw = (By.XPATH, '(//span[contains(text(),"人工提出")])[last()]')                                     # 人工提出
    wallet_transaction = (By.XPATH, '(//span[contains(text(),"额度转换")])[last()]')                                      # 額度轉換

    # 跳轉頁面名稱
    company_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "公司")]')                     # 公司入款
    online_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "在线")]')                      # 在线入款
    artificial_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "人工存入")]')              # 人工存入
    order_center_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "注单中心")]')                    # 注单中心
    withdraw_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/withdraw"]')                                          # 出款申请
    artificial_withdraw_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/manwithdraw"]')                            # 人工提出
    wallet_transaction_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/wallettransfer"]')                          # 额度转换
    agent_settlement_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/agentsettlement"]')                           # 代理结算(新版)

class AdminThirdPartyLedgerPage(BasePage):
    # 將 dom 定位list 轉為text list
    def get_text_list_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    def get_transaction_time_list(self):
        '''
            取得所有交易時間
        '''
        elements = self.find_elements(AdminThirdPartyLedgerPageLocator.transaction_time)
        return self.get_text_list_by_dom_list(elements)

    def get_member_account_list(self):
        '''
            取得所有會員帳號
        '''
        elements = self.find_elements(AdminThirdPartyLedgerPageLocator.member_account)
        return self.get_text_list_by_dom_list(elements)

    def get_current_amount_list(self):
        '''
            取得所有當前餘額
        '''
        elements = self.find_elements(AdminThirdPartyLedgerPageLocator.current_amount)
        return self.get_text_list_by_dom_list(elements)

    def get_transaction_amount_list(self):
        '''
            取得所有交易金額
        '''
        elements = self.find_elements(AdminThirdPartyLedgerPageLocator.transaction_amount)
        return self.get_text_list_by_dom_list(elements)

    def get_final_amount_list(self):
        '''
            取得所有最後餘額
        '''
        elements = self.find_elements(AdminThirdPartyLedgerPageLocator.final_amount)
        return self.get_text_list_by_dom_list(elements)

    def search_account(self, account):
        '''
            搜尋帳號，參數 account 為要做搜尋帳號
        '''
        self.wait_loading_finish()                                                                                                          # 等待一下R
        self.type(AdminThirdPartyLedgerPageLocator.account_input, account)                                                                # 輸入要搜尋的帳號
        self.click(AdminThirdPartyLedgerPageLocator.search_btn)                                                                           # 點擊"查找"按鈕

    # 檢查搜尋會員的帳號
    def check_search_member_account_list(self, member_account_list, search_account):
        for member_account in member_account_list:
            # 確認頁面取得的帳號資訊
            assert member_account == search_account, '交易列表 > 帳號顯示錯誤...' + member_account + ' 應為-> ' + search_account
    
    def check_search_member(self, search_account):
        '''
            檢查搜尋的會員資訊
        '''
        self.refresh_browser()
        self.wait_loading_finish()                                                                                                        # 等待一下R
        self.sleep(1)
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        self.wait_loading_finish()
        self.sleep(1)
        # 點擊"全選"
        self.click(AdminThirdPartyLedgerPageLocator.wallet_code_check_box(AdminThirdPartyLedgerPageLocator, '全选'))                                                         
        self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)                                                                     # 點擊"上月"按鈕
        self.search_account(search_account)
        member_account_list = self.get_member_account_list()                                                                            # 頁面上的會員帳號
        self.check_search_member_account_list(member_account_list, search_account)                                                      # 檢查搜尋會員的帳號

    def check_transaction_type(self):
        '''
            檢查交易類型
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        transaction_type_check_box_text = ['第三方注单', '第三方额度转换', '第三方优惠类型']

        for index, text in enumerate(transaction_type_check_box_text):
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)                                                             # 進入第三方現金流水
            self.wait_loading_finish()
            self.sleep(1)
            # 點擊"全選"checkbox
            self.click(AdminThirdPartyLedgerPageLocator.wallet_code_check_box(AdminThirdPartyLedgerPageLocator, '全选'))

            self.click(AdminThirdPartyLedgerPageLocator.transaction_type_check_box(AdminThirdPartyLedgerPageLocator, '第三方注单'))
            self.click(AdminThirdPartyLedgerPageLocator.transaction_type_check_box(AdminThirdPartyLedgerPageLocator, text))
            self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
            self.click(AdminThirdPartyLedgerPageLocator.search_btn)
            self.wait_loading_finish()
            self.sleep(0.5)
            
            # 交易類型 為 第三方注單 時，才會有資料
            if self.is_element_finded(AdminThirdPartyLedgerPageLocator.empty_message):
                assert self.get_text(AdminThirdPartyLedgerPageLocator.empty_message).__contains__('暂无数据'), \
                    f'交易列表 > 交易類型顯示錯誤 ... 應產生 Toast message "暂无数据"'
            else:
                transaction_type = self.get_text_list_by_dom_list(self.find_elements(AdminThirdPartyLedgerPageLocator.transaction_type))
                for transaction_type in transaction_type:
                    assert transaction_type in text, f'交易列表 > 交易類型顯示錯誤 ... 第 {index} 項 {transaction_type} 應為-> {text}'
                        
    
    def check_wallet_code(self):
        '''
            檢查錢包代碼
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        self.sleep(0.5)
        self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
        self.click(AdminThirdPartyLedgerPageLocator.search_btn)
        self.sleep(1)
        wallet_message = self.get_text(AdminThirdPartyLedgerPageLocator.wallet_message)
        # assert wallet_message.__contains__('至少要选一个钱包代码'), '錢包代碼查找錯誤 ... 應顯示  message "至少要选一个钱包代码"'

        wallet_code_text = {'主钱包', 'AG', 'MG', 'SB', 'BBIN', 'LGD', '3S', 'GC', 'KY', 'VG', 'SW', 'PT', 'KX', 'GM', 'FG', 'CQ9', 'BSP'}

        for _, text in enumerate(wallet_code_text):
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
            self.sleep(1)
            self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
            self.click(AdminThirdPartyLedgerPageLocator.wallet_code_check_box(AdminThirdPartyLedgerPageLocator, text))
            self.click(AdminThirdPartyLedgerPageLocator.search_btn)
            self.wait_loading_finish()
            self.sleep(0.5)

            if self.is_element_finded(AdminThirdPartyLedgerPageLocator.empty_message):
                assert self.get_text(AdminThirdPartyLedgerPageLocator.empty_message).__contains__('暂无数据'), '錢包代碼查找錯誤 ... 應顯示  message "暂无数据"'
            else:
                wallet_codes = self.get_text_list_by_dom_list(self.find_elements(AdminThirdPartyLedgerPageLocator.wallet_code))
                for index, wallet_code in enumerate(wallet_codes):
                    assert wallet_code == text, f'錢包代碼查找錯誤 ... 第 {index} 項 {wallet_code} 應為-> {text}'
                        

    # 檢查以日或周為單位的交易時間 開始及結束時間
    def check_time_period_days_week(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(AdminThirdPartyLedgerPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminThirdPartyLedgerPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == today - datetime.timedelta(days=time_delta_start), \
            f'{error_message_date} 時間錯誤 ... 開始時間錯誤 ... {start_time} 應為-> {today - datetime.timedelta(days=time_delta_start)}'
        assert end_time == today - datetime.timedelta(days=time_delta_end), \
            f'{error_message_date} 時間錯誤 ... 結束時間錯誤 ... {end_time} 應為-> {today - datetime.timedelta(days=time_delta_end)}'

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        return datetime.date(year, month, 1)

    # 檢查以月為單位的交易時間 開始及結束時間
    def check_time_period_month(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(AdminThirdPartyLedgerPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminThirdPartyLedgerPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == self.add_months(sourcedate=today, months=time_delta_start),  \
            f'{error_message_date} 時間錯誤 ... 開始時間錯誤 ... {start_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_start)}'
        assert end_time == self.add_months(sourcedate=today, months=time_delta_end), \
            f'{error_message_date} 時間錯誤 ... 結束時間錯誤 ... {end_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_end)}'

    def check_select_transaction_time(self):
        '''
            檢查交易時間
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        self.wait_loading_finish()
        today = self.get_us_time().date()
        week_day = today.weekday()

        self.click(AdminThirdPartyLedgerPageLocator.today_btn)
        self.check_time_period_days_week(today=today, time_delta_start=0, time_delta_end=-1, error_message_date='今日')

        self.click(AdminThirdPartyLedgerPageLocator.yesterday_btn)
        self.check_time_period_days_week(today=today, time_delta_start=1, time_delta_end=0, error_message_date='昨日')

        self.click(AdminThirdPartyLedgerPageLocator.this_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day, time_delta_end=week_day-7, error_message_date='本週')

        self.click(AdminThirdPartyLedgerPageLocator.last_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day+7, time_delta_end=week_day, error_message_date='上週')

        self.click(AdminThirdPartyLedgerPageLocator.this_month_btn)
        self.check_time_period_month(today=today, time_delta_start=0, time_delta_end=1, error_message_date='本月')

        self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
        self.check_time_period_month(today=today, time_delta_start=-1, time_delta_end=0, error_message_date='上月')

    # 檢查第一頁紀錄長度
    def check_record_len_first_page(self, select_record_len):
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(AdminThirdPartyLedgerPageLocator.transaction_time))
        total_record_len = int((self.get_text(AdminThirdPartyLedgerPageLocator.total_record))[2:-2])
        self.wait_loading_finish()

        if total_record_len > select_record_len:
            assert form_record_len == select_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {select_record_len}'
        else:
            assert form_record_len == total_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {total_record_len}'

    # 檢查最後一頁紀錄長度
    def check_record_len_last_page(self, select_record_len):
        self.click(AdminThirdPartyLedgerPageLocator.last_page)
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(AdminThirdPartyLedgerPageLocator.transaction_time))
        total_record_len = int((self.get_text(AdminThirdPartyLedgerPageLocator.total_record))[2:-2])
        if total_record_len > select_record_len*1000:        # 超過1000頁後的資料不顯示
            return

        if form_record_len == select_record_len:
            assert (total_record_len % select_record_len) % select_record_len == 0, f'紀錄數量錯誤 ... 應為-> {total_record_len % select_record_len}'
        else:   
            assert form_record_len == total_record_len % select_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {total_record_len % select_record_len}'

    def check_record_per_page(self):
        '''
            檢查每頁記錄數
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
        self.click(AdminThirdPartyLedgerPageLocator.wallet_code_check_box(AdminThirdPartyLedgerPageLocator, '全选'))
        self.click(AdminThirdPartyLedgerPageLocator.search_btn)
        self.wait_loading_finish()

        options_locators = AdminThirdPartyLedgerPageLocator.amount_per_page_options
        options = self.find_elements(options_locators)
        self.sleep(1)

        if self.is_element_finded(AdminThirdPartyLedgerPageLocator.empty_message) and \
            self.get_text(AdminThirdPartyLedgerPageLocator.empty_message).__contains__('暂无数据'):
            return
            
        for i in range(len(options)):
            self.click(AdminThirdPartyLedgerPageLocator.amount_per_page)
            self.sleep(1)
            option_locator = (options_locators[0], options_locators[1] + f'[{i+1}]'+'/span')
            self.click(option_locator)
            self.sleep(1)
            self.click(AdminThirdPartyLedgerPageLocator.amount_per_page)
            self.wait_loading_finish()
            self.sleep(1)
            per_page_num = int(self.get_text(AdminThirdPartyLedgerPageLocator.per_page)[:-3])
            self.check_record_len_first_page(per_page_num)
            self.check_page_v2(tab_page=1, record_per_page = per_page_num)
            self.check_record_len_last_page(per_page_num)

    # 檢查頁面連結是否正常
    def check_link(self, link_locator, page_name_locator, page_name):
        self.click(AdminThirdPartyLedgerPageLocator.business_number)
        self.sleep(0.5)
        self.open_wait_new_window(link_locator)
        self.wait_loading_finish()                                                                                        # 開啟並等待新分頁
        assert self.get_text(page_name_locator).__contains__('{}'.format(page_name)), '未正確跳轉到"{}"頁面'.format(page_name)
        self.switch_home_page()

    def check_business_number_link(self):
        '''
            檢查業務號碼的連結
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.third_party_ledger)
        self.wait_loading_finish()
        self.click(AdminThirdPartyLedgerPageLocator.last_month_btn)
        self.click(AdminThirdPartyLedgerPageLocator.wallet_code_check_box(AdminThirdPartyLedgerPageLocator, '全选'))
        self.click(AdminThirdPartyLedgerPageLocator.search_btn)
        self.wait_loading_finish()
        self.sleep(0.5)

        if self.is_element_finded(AdminThirdPartyLedgerPageLocator.empty_message) and \
            self.get_text(AdminThirdPartyLedgerPageLocator.empty_message).__contains__('暂无数据'):
            return

        self.check_link(AdminThirdPartyLedgerPageLocator.company_deposit, AdminThirdPartyLedgerPageLocator.company_deposit_page, '公司')
        self.check_link(AdminThirdPartyLedgerPageLocator.online_deposit, AdminThirdPartyLedgerPageLocator.online_deposit_page, '在线')
        self.check_link(AdminThirdPartyLedgerPageLocator.artificial_deposit, AdminThirdPartyLedgerPageLocator.artificial_deposit_page, '人工存入')
        self.check_link(AdminThirdPartyLedgerPageLocator.order_center, AdminThirdPartyLedgerPageLocator.order_center_page, '注单中心')
        self.check_link(AdminThirdPartyLedgerPageLocator.online_withdraw, AdminThirdPartyLedgerPageLocator.withdraw_page, '下分申请')
        self.check_link(AdminThirdPartyLedgerPageLocator.artificial_withdraw, AdminThirdPartyLedgerPageLocator.artificial_withdraw_page, '人工提出')
        self.check_link(AdminThirdPartyLedgerPageLocator.wallet_transaction, AdminThirdPartyLedgerPageLocator.wallet_transaction_page, '额度转换')
