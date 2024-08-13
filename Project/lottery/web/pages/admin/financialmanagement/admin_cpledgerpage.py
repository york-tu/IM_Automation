from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import numpy as np

class AdminCPLedgerPageLocator:
    # 查找條件
    account_input = (By.XPATH, '(//div[@class="el-input el-input--mini"]//input[@qa-input="member_login"])[1]')                             # 會員帳號 textbox
    today_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"今日")])[1]')                                               # "今日"按鈕
    yesterday_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"昨日")])[1]')                                           # "昨日"按鈕
    this_week_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"本周")])[1]')                                           # "本周"按鈕
    last_week_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"上周")])[1]')                                           # "上周"按鈕
    this_month_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"本月")])[1]')                                          # "本月"按鈕
    last_month_btn = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"上月")])[1]')                                          # "上月"按鈕
    transacion_time_start = (By.XPATH, '(//input[@placeholder="开始时间"])[1]')                    # 交易時間 開始日期
    transacion_time_end = (By.XPATH, '(//input[@placeholder="结束时间"])[1]')                        # 交易時間 結束日期
    search_btn = (By.XPATH, '(//button[@qa-button="search"])[1]')                                                               # "查找"按鈕
    export_btn = (By.XPATH, '(//button[@qa-button="export"])[1]')                                                      # "匯出"按鈕
    export_comfirm_btn = (By.XPATH, '//div[@aria-hidden="false"]//button[contains(@class,"primary")]')                                        # 確定匯出 按鈕
    find_agent = (By.XPATH,"(//div[text()='代理']/following::input[@qa-input='agent'])[1]")                              # 代理
    # *交易類型

    # 交易類型 checkbox
    def transaction_type_check_box(self, text):
        return (By.XPATH, f'(//div[@class="el-form-item__content"]//span[text()="{text}"])[1]')


    # 交易列表
    transaction_time = (By.XPATH, '//td[contains(@class,"el-table_1_column_1 ") and @colspan="1"]')                                  # 交易時間
    member_account = ( By.XPATH, '//td[contains(@class,"el-table_1_column_2")]')                                    # 會員帳號
    transaction_type = (By.XPATH, '//td[contains(@class,"el-table_1_column_3")]')                                   # 交易類型
    transaction_product = (By.XPATH, '//td[contains(@class,"el-table_1_column_4")]')                                # 交易產品
    business_number = (By.XPATH, '//td[contains(@class,"el-table_1_column_5")]/div/div/span')                       # 業務號碼
    current_amount = (By.XPATH, '//td[contains(@class,"el-table_1_column_6")]')                                     # 當前餘額
    transaction_amount = (By.XPATH, '//td[contains(@class,"el-table_1_column_7")]')                                 # 交易金額
    final_amount = (By.XPATH, '//td[contains(@class,"el-table_1_column_8")]')                                       # 最後餘額
    amount_per_page = (By.XPATH, '(//span[@class="el-pagination__sizes"]//input[@class="el-input__inner"])[1]')         # 每頁紀錄數
    amount_per_page_btn = (By.XPATH, '(//span[@class="el-input__suffix-inner"])[3]')                                # 每頁紀錄按鈕
    amount_per_page_options = (By.XPATH, '(//ul[contains(@class,"el-select-dropdown__list")])[last()]//li')         # 每頁紀錄數的所有選項
    system_remark = (By.XPATH, '//td[contains(@class,"el-table_1_column_9")]')                                      # 系統備註
    remark = (By.XPATH, '//td[contains(@class,"el-table_1_column_10")]')                                            # 備註
    operator = (By.XPATH, '//td[contains(@class,"el-table_1_column_11")]')                                          # 操作者

    total_record = (By.XPATH, '(//span[@class="el-pagination__total"])[1]')                                         # 總紀錄數
    total_amount = (By.XPATH, '(//span[@class="el-tag el-tag--danger el-tag--light"])[2]')                          # 總金額
    first_page = (By.XPATH, '(//ul[@class="el-pager"]/li[1])[1]')                                                   # "首頁"按鈕
    last_page = (By.XPATH, '(//ul[@class="el-pager"]/li[last()])[1]')                                               # "尾頁"按鈕

    # 業務號碼
    company_deposit = (By.XPATH, '(//span[contains(text(),"公司入款(优惠)")])[last()]')                                         # 公司入款(優惠)
    online_deposit = (By.XPATH, '(//span[contains(text(),"在线入款(优惠)")])[last()]')                                          # 在線入款(優惠)
    artificial_deposit = (By.XPATH, '(//span[contains(text(),"人工入款(优惠)")])[last()]')                                      # 人工入款(優惠)
    order_center = (By.XPATH, '(//span[contains(text(),"注单/返水")])[last()]')                                                 # 注單/返水
    online_withdraw = (By.XPATH, '(//span[contains(text(),"在线提现")])[last()]')                                               # 在線提現
    artificial_withdraw = (By.XPATH, '(//span[contains(text(),"人工提出")])[last()]')                                           # 人工提出
    wallet_transaction = (By.XPATH, '(//span[contains(text(),"额度转换")])[last()]')                                            # 額度轉換
    agent_settlement = (By.XPATH, '(//span[contains(text(),"代理结算")])[last()]')                                              # 代理結算

    # 跳轉頁面名稱
    company_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "公司")]')                     # 公司入款
    online_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "在线")]')                      # 在线入款
    artificial_deposit_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "人工存入")]')              # 人工存入
    order_center_page = (By.XPATH, '//span[@class="el-breadcrumb__inner"]//a[contains(text(), "注单中心")]')                    # 注单中心
    withdraw_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/withdraw"]')                                          # 出款申请
    artificial_withdraw_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/manwithdraw"]')                            # 人工提出
    wallet_transaction_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/wallettransfer"]')                          # 额度转换
    agent_settlement_page = (By.XPATH, '//ul[@class="page-breadcrumb"]//a[@href="/agentsettlement"]')                           # 代理结算(新版)

    toast_message = (By.XPATH, '(//span[@class="el-table__empty-text"])[1]')

class AdminCPLedgerPage(BasePage):
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
        elements = self.find_elements(AdminCPLedgerPageLocator.transaction_time)
        return self.get_text_list_by_dom_list(elements)

    def get_member_account_list(self):
        '''
            取得所有會員帳號
        '''
        elements = self.find_elements(AdminCPLedgerPageLocator.member_account)
        return self.get_text_list_by_dom_list(elements)

    def get_current_amount_list(self):
        '''
            取得所有當前餘額
        '''
        elements = self.find_elements(AdminCPLedgerPageLocator.current_amount)
        return self.get_text_list_by_dom_list(elements)

    def get_transaction_amount_list(self):
        '''
            取得所有交易金額
        '''
        elements = self.find_elements(AdminCPLedgerPageLocator.transaction_amount)
        return self.get_text_list_by_dom_list(elements)

    def get_final_amount_list(self):
        '''
            取得所有最後餘額
        '''
        elements = self.find_elements(AdminCPLedgerPageLocator.final_amount)
        return self.get_text_list_by_dom_list(elements)

    def search_account(self, account):
        '''
            搜尋帳號，參數 account 為要做搜尋帳號
        '''
        self.wait_loading_finish()                                                                                                        # 等待一下R
        self.type(AdminCPLedgerPageLocator.account_input, account)                                                                      # 輸入要搜尋的帳號
        self.click(AdminCPLedgerPageLocator.search_btn)                                                                                 # 點擊"查找"按鈕

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
        self.click(AdminCPLedgerPageLocator.last_week_btn)                                                                             # 點擊"上周"按鈕
        self.search_account(search_account)
        member_account_list = self.get_member_account_list()                                                                            # 頁面上的會員帳號
        self.check_search_member_account_list(member_account_list, search_account)                                                      # 檢查搜尋會員的帳號

    def check_transaction_type(self):
        '''
            檢查交易類型
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        check_box_total_text = '全选'
        check_box_transaction_type_text = ['公司入款', '在线入款', '人工入款(含人工公司,虚拟币/在线入款)', '在线提现', '人工提出', '注单', '系统存入优惠', 
                                '人工存入优惠', '返水', '额度转换', '退佣', '退款']

        for check_box_text in check_box_transaction_type_text:
            self.refresh_browser()
            self.wait_loading_finish()

            self.click(AdminCPLedgerPageLocator.transaction_type_check_box(AdminCPLedgerPageLocator, check_box_total_text))
            self.click(AdminCPLedgerPageLocator.transaction_type_check_box(AdminCPLedgerPageLocator, check_box_text))
            self.click(AdminCPLedgerPageLocator.last_week_btn)
            self.click(AdminCPLedgerPageLocator.search_btn)
            self.wait_loading_finish()
            self.sleep(0.5)

            if self.is_element_displayed(AdminCPLedgerPageLocator.toast_message):
                assert self.get_text(AdminCPLedgerPageLocator.toast_message).__contains__('暂无数据'), 'CP現金流水 -> Toast message 訊息顯示錯誤'
            else:
                transaction_type_text = self.get_text_list_by_dom_list(self.find_elements(AdminCPLedgerPageLocator.transaction_type))
                for index, transaction_type in enumerate(transaction_type_text):
                    if check_box_text == '在线提现':   #目前在线提现類別會包含虚拟币提现的資料
                        assert transaction_type in check_box_text or transaction_type == '虚拟币提现', f'交易列表 > 交易類型顯示錯誤 ... 第 {index} 筆 {transaction_type} 應為-> {check_box_text} or 虚拟币提现'
                    else:
                        assert transaction_type in check_box_text, f'交易列表 > 交易類型顯示錯誤 ... 第 {index} 筆 {transaction_type} 應為-> {check_box_text}'

    # 檢查以日或周為單位的交易時間 開始及結束時間
    def check_time_period_days_week(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(AdminCPLedgerPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminCPLedgerPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
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
        start_time = datetime.datetime.strptime(self.get_attribute(AdminCPLedgerPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminCPLedgerPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
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
        today = self.get_us_time().date()
        week_day = today.weekday()
        self.click(AdminCPLedgerPageLocator.today_btn)
        self.check_time_period_days_week(today=today, time_delta_start=0, time_delta_end=-1, error_message_date='今日')

        self.click(AdminCPLedgerPageLocator.yesterday_btn)
        self.check_time_period_days_week(today=today, time_delta_start=1, time_delta_end=0, error_message_date='昨日')

        self.click(AdminCPLedgerPageLocator.this_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day, time_delta_end=week_day-7, error_message_date='本週')

        self.click(AdminCPLedgerPageLocator.last_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day+7, time_delta_end=week_day, error_message_date='上週')

        self.click(AdminCPLedgerPageLocator.this_month_btn)
        self.check_time_period_month(today=today, time_delta_start=0, time_delta_end=1, error_message_date='本月')

        # self.click(AdminCPLedgerPageLocator.last_month_btn)   # TiDB無法查找上月，有時間範圍限制
        # self.check_time_period_month(today=today, time_delta_start=-1, time_delta_end=0, error_message_date='上月')

    def check_export_report(self, brand):
        '''
            檢查匯出資料
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        abandom_list = ['注单', '系统存入优惠', '人工存入优惠', '返水', '退佣']

        for abandom_text in abandom_list:
            self.click(AdminCPLedgerPageLocator.transaction_type_check_box(AdminCPLedgerPageLocator, abandom_text))                     # 把會造成時間相同的部分取消

        option = AdminCPLedgerPageLocator.amount_per_page_options
        self.click(AdminCPLedgerPageLocator.last_week_btn)
        self.click(AdminCPLedgerPageLocator.search_btn)
        self.sleep(1)
        self.click(AdminCPLedgerPageLocator.export_btn)
        self.sleep(1)
        self.click(AdminCPLedgerPageLocator.export_comfirm_btn)
        self.sleep(5)

        # 取得每頁紀錄數的最後一個選項
        option = (option[0], option[1] + f'[{len(self.find_elements(option))}]/span')
        self.click(AdminCPLedgerPageLocator.amount_per_page)
        self.sleep(0.5)
        last_page_option = self.get_text(option)
        self.click(option)
        self.wait_loading_finish()

        total_record = int(self.get_text(AdminCPLedgerPageLocator.total_record)[1:-1])
        last_page_option = int(last_page_option[0:-3])
        if total_record > last_page_option:
            self.click(AdminCPLedgerPageLocator.last_page)
        amount_per_page = total_record % last_page_option

        transaction_form_locator = [
            AdminCPLedgerPageLocator.transaction_time, 
            AdminCPLedgerPageLocator.member_account, 
            AdminCPLedgerPageLocator.transaction_type, 
            AdminCPLedgerPageLocator.transaction_product, 
            AdminCPLedgerPageLocator.business_number, 
            AdminCPLedgerPageLocator.current_amount, 
            AdminCPLedgerPageLocator.transaction_amount, 
            AdminCPLedgerPageLocator.final_amount, 
            AdminCPLedgerPageLocator.system_remark, 
            AdminCPLedgerPageLocator.remark, 
            AdminCPLedgerPageLocator.operator, 
        ]

        self.un_zip(brand)
        transaction_form_excel = self.read_excel(amount_per_page, brand)
        keys = list(transaction_form_excel.keys())
        
        for index, _ in enumerate(transaction_form_locator):
            transaction_form_column = self.find_elements(transaction_form_locator[index])
            transaction_form_column_data = []
            for j in range(amount_per_page):
                if index > 4 and index < 8:                                                                                                     # 判斷是否為金額
                    transaction_form_column_data.append(float(self.get_text_by_dom(transaction_form_column[j]).replace(',', '')))
                else:
                    transaction_form_column_data.append(self.get_text_by_dom(transaction_form_column[j]))

            array = np.array(transaction_form_column_data)
            transaction_form_column_data = list(array[::-1])
            data_len = len(transaction_form_excel[keys[index]])

            assert transaction_form_excel[keys[index]] == transaction_form_column_data[:data_len], f'匯出資料錯誤 ... 第 {index + 1} 行資料不同'

    # 檢查第一頁紀錄長度
    def check_record_len_first_page(self, select_record_len):
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(AdminCPLedgerPageLocator.transaction_time))
        total_record_len = int(self.get_text(AdminCPLedgerPageLocator.total_record)[1:-1])

        if total_record_len > select_record_len:
            assert form_record_len == select_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {select_record_len}'
        else:
            assert form_record_len == total_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {total_record_len}'

    # 檢查最後一頁紀錄長度
    def check_record_len_last_page(self, select_record_len):
        self.click(AdminCPLedgerPageLocator.last_page)
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(AdminCPLedgerPageLocator.transaction_time))
        total_record_len = int(self.get_text(AdminCPLedgerPageLocator.total_record)[1:-1])
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
        self.click(AdminCPLedgerPageLocator.last_week_btn)
        self.click(AdminCPLedgerPageLocator.search_btn)
        self.wait_loading_finish()

        options_locator = AdminCPLedgerPageLocator.amount_per_page_options
        options = self.find_elements(options_locator)

        for i, _ in enumerate(options):
            self.click(AdminCPLedgerPageLocator.amount_per_page)
            self.sleep(1)
            option_locator = (options_locator[0], options_locator[1] + f'[{i+1}]/span')
            select_record_len = int(self.get_text(option_locator)[0:-3])
            self.click(option_locator)

            self.check_record_len_first_page(select_record_len)
            self.check_page_v2(record_per_page=select_record_len)
            self.check_record_len_last_page(select_record_len)

    # 檢查頁面連結是否正常
    def check_link(self, link_locator, page_name_locator, page_name):
        self.click(AdminCPLedgerPageLocator.business_number)
        self.sleep(1)
        self.open_wait_new_window(link_locator)
        self.wait_loading_finish()                                                                                       # 開啟並等待新分頁
        assert self.get_text(page_name_locator).__contains__(f'{page_name}'), f'未正確跳轉到"{page_name}"頁面'
        self.switch_home_page()

    def check_business_number_link(self):
        '''
            檢查業務號碼的連結
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminCPLedgerPageLocator.last_week_btn)
        self.click(AdminCPLedgerPageLocator.search_btn)
        self.wait_loading_finish()

        self.check_link(AdminCPLedgerPageLocator.company_deposit, AdminCPLedgerPageLocator.company_deposit_page, '公司')
        self.check_link(AdminCPLedgerPageLocator.online_deposit, AdminCPLedgerPageLocator.online_deposit_page, '在线')
        self.check_link(AdminCPLedgerPageLocator.artificial_deposit, AdminCPLedgerPageLocator.artificial_deposit_page, '人工存入')
        self.check_link(AdminCPLedgerPageLocator.order_center, AdminCPLedgerPageLocator.order_center_page, '注单中心')
        self.check_link(AdminCPLedgerPageLocator.online_withdraw, AdminCPLedgerPageLocator.withdraw_page, '下分申请')
        self.check_link(AdminCPLedgerPageLocator.artificial_withdraw, AdminCPLedgerPageLocator.artificial_withdraw_page, '人工提出')
        self.check_link(AdminCPLedgerPageLocator.wallet_transaction, AdminCPLedgerPageLocator.wallet_transaction_page, '额度转换')
        self.check_link(AdminCPLedgerPageLocator.agent_settlement, AdminCPLedgerPageLocator.agent_settlement_page, '代理结算(新版)')

    # 取得比對財務報表的資料
    def get_back_data(self, reseller_account, type, time=''):
        self.refresh_browser()
        self.wait_loading_finish()
        for t in type:
            self.click(AdminCPLedgerPageLocator.transaction_type_check_box(AdminCPLedgerPageLocator, t))

        self.wait_visibility(AdminCPLedgerPageLocator.today_btn)
        if time == '' or time == '1':
            self.click(AdminCPLedgerPageLocator.today_btn)
        elif time == '2':
            self.click(AdminCPLedgerPageLocator.yesterday_btn)
        elif time == '3':
            self.click(AdminCPLedgerPageLocator.this_week_btn)
        elif time == '4':
            self.click(AdminCPLedgerPageLocator.last_week_btn)
        elif time == '5':
            self.click(AdminCPLedgerPageLocator.this_month_btn)   
        elif time == '6':
            self.click(AdminCPLedgerPageLocator.last_month_btn)     
                            
        self.wait_visibility(AdminCPLedgerPageLocator.find_agent)
        self.type(AdminCPLedgerPageLocator.find_agent, reseller_account)
        self.wait_visibility(AdminCPLedgerPageLocator.search_btn)
        self.click(AdminCPLedgerPageLocator.search_btn)
        self.wait_loading_finish()
        self.sleep(0.5)

        if self.is_element_displayed(AdminCPLedgerPageLocator.toast_message):
            assert self.get_text(AdminCPLedgerPageLocator.toast_message).__contains__('暂无数据'), 'CP現金流水 -> Toast message 訊息顯示錯誤'
            return '0.00'

        back_amount = self.get_text(AdminCPLedgerPageLocator.total_amount).replace(',', '')
        
        return back_amount