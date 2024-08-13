from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class WalletTransferLocator:
    # 查找條件
    member_account_input = (By.XPATH, '//input[@data-bind="value: filter.memberlogin"]')                                                # 會員帳號input
    order_id_input = (By.XPATH, '//input[@data-bind="value: filter.id"]')                                                               # 訂單號碼
    transacion_time_start = (By.XPATH, '//input[contains(@data-bind, "datetime: filter.starttime")]')
    transacion_time_end = (By.XPATH, '//input[contains(@data-bind, "datetime: filter.endtime")]')
    button_today = (By.XPATH, '//button[contains(text(), "今日")]')                                                                     # "今日"按鈕
    button_yesterday = (By.XPATH, '//button[contains(text(), "昨日")]')                                                                 # "昨日"按鈕
    button_this_week = (By.XPATH, '//button[contains(text(), "本周")]')                                                                 # "本周"按鈕
    button_last_week = (By.XPATH, '//button[contains(text(), "上周")]')                                                                 # "上周"按鈕
    button_this_month = (By.XPATH, '//button[contains(text(), "本月")]')                                                                # "本月"按鈕
    button_last_month = (By.XPATH, '//button[contains(text(), "上月")]')                                                                # "上月"按鈕
    transfer_out_span = (By.ID, 's2id_autogen1')                                                                                        # 轉出錢包
    transfer_out_input = (By.ID, 's2id_autogen2_search')                                                                                # 轉出錢包輸入
    transfer_in_span = (By.ID, 'select2-chosen-4')                                                                                      # 轉入錢包
    transfer_in_input = (By.ID, 's2id_autogen4_search')                                                                                 # 轉入錢包輸入
    shareholder_selector = (By.XPATH, '//textarea[contains(@data-bind, "shareLoginItems")]')                                  # 查詢帳號 股東
    generalagent_input = (By.XPATH, '//input[@data-bind="textInput: filter.generalagent"]')                                             # 查詢帳號 總代
    agent_input = (By.XPATH, '//input[@data-bind="textInput: filter.agent"]')                                                           # 查詢帳號 代理
    status_radio_box = (By.XPATH, '//div[@class="col-md-3"]/label')                                                                     # 狀態 radio box
    button_search = (By.ID, 'btnSearch')                                                                                                # 查找按鈕

    # 額度轉換
    shareholder_text = (By.XPATH, '//td[@data-bind="text: sharelogin"]')                                                                # 股東帳號
    generalagent_text = (By.XPATH, '//td[@data-bind="text: generalagent"]')                                                             # 總代帳號
    agent_text = (By.XPATH, '//td[@data-bind="text: agent"]')                                                                           # 代理帳號
    member_account_text = (By.XPATH, '//td[@data-bind="text: memberlogin"]')                                                            # 會員帳號
    order_id_text = (By.XPATH, '//td[@data-bind="text: id"]')                                                                           # 訂單號碼
    transfer_out_text = (By.XPATH, '//span[@data-bind="text: fromwalletname"]')                                                         # 轉出錢包
    transfer_in_text = (By.XPATH, '//span[@data-bind="text: towalletname"]')                                                            # 轉入錢包
    amount_text = (By.XPATH, '//td[@data-bind="money: amount"]')                                                                        # 金額
    status_text = (By.XPATH, '//div[contains(@data-bind, "text: status == 0")]')                                                        # 狀態
    apply_time_text = (By.XPATH, '//td[@data-bind="text: addedtime"]')                                                                  # 申請時間
    total_record = (By.XPATH, '//span[@data-bind="text: pager.total"]')                                                                 # 總紀錄數
    options_selector = (By.XPATH, '//select[@data-bind="value: pager.pageSize"]')                                                       # 每頁紀錄數下拉式選單

class WalletTransfer(BasePage):    

    # 將 dom 定位list 轉為text list
    def get_text_list_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    # 檢查以日或周為單位的交易時間 開始及結束時間
    def check_time_period_days_week(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(WalletTransferLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(WalletTransferLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
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
        start_time = datetime.datetime.strptime(self.get_attribute(WalletTransferLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(WalletTransferLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
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

        self.click(WalletTransferLocator.button_today)
        self.check_time_period_days_week(today=today, time_delta_start=0, time_delta_end=-1, error_message_date='今日')

        self.click(WalletTransferLocator.button_yesterday)
        self.check_time_period_days_week(today=today, time_delta_start=1, time_delta_end=0, error_message_date='昨日')

        self.click(WalletTransferLocator.button_this_week)
        self.check_time_period_days_week(today=today, time_delta_start=week_day, time_delta_end=week_day-7, error_message_date='本週')

        self.click(WalletTransferLocator.button_last_week)
        self.check_time_period_days_week(today=today, time_delta_start=week_day+7, time_delta_end=week_day, error_message_date='上週')

        self.click(WalletTransferLocator.button_this_month)
        self.check_time_period_month(today=today, time_delta_start=0, time_delta_end=1, error_message_date='本月')

        self.click(WalletTransferLocator.button_last_month)
        self.check_time_period_month(today=today, time_delta_start=-1, time_delta_end=0, error_message_date='上月')

    def input_account(self, shareholder, member_account = '', generalagent = '', agent = ''):
        '''
            刷新頁面及搜尋帳號
            member_account、generalagent 及 agent 為空字串時，則不做輸入
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WalletTransferLocator.shareholder_selector, shareholder)

        if member_account != '':
            self.type(WalletTransferLocator.member_account_input, member_account)
        if generalagent != '':
            self.type(WalletTransferLocator.generalagent_input, generalagent)
        if agent != '':
            self.type(WalletTransferLocator.agent_input, agent)

    # 檢查第一頁紀錄長度
    def check_record_len_first_page(self, option):
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(WalletTransferLocator.amount_text))
        total_record_len = int(self.get_text(WalletTransferLocator.total_record))
        select_record_len = int(option)

        if total_record_len > select_record_len:
            assert form_record_len == select_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {select_record_len}'
        else:
            assert form_record_len == total_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {total_record_len}'

    # 檢查最後一頁紀錄長度
    def check_record_len_last_page(self, option):
        self.wait_loading_finish()
        form_record_len = len(self.find_elements(WalletTransferLocator.amount_text))
        total_record_len = int(self.get_text(WalletTransferLocator.total_record))
        select_record_len = int(option)

        if form_record_len == select_record_len:
            assert (total_record_len % select_record_len) % select_record_len == 0, f'紀錄數量錯誤 ... 應為-> {total_record_len % select_record_len}'
        else:   
            assert form_record_len == total_record_len % select_record_len, f'紀錄數量錯誤 ... {form_record_len} 應為-> {total_record_len % select_record_len}'

    def check_search_member_account(self, member_account, shareholder, generalagent, agent):
        '''
            檢查搜尋會員帳號、下方頁數顯示及每頁紀錄數
        '''
        self.input_account(shareholder=shareholder, member_account=member_account, generalagent=generalagent, agent=agent)
        self.click(WalletTransferLocator.button_last_month)
        self.sleep(1)
        self.click(WalletTransferLocator.button_search)
        self.wait_loading_finish()
        shareholder_list = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.shareholder_text))
        generalagent_list = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.generalagent_text))
        agent_list = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.agent_text))
        member_account_list = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.member_account_text))

        for i in range(len(shareholder_list)):
            assert shareholder_list[i] == shareholder, '額度轉換 -> 股東帳號錯誤 ... ' + shareholder_list[i] + ' 應為-> ' + shareholder
            assert generalagent_list[i] == generalagent, '額度轉換 -> 總代帳號錯誤 ... ' + generalagent_list[i] + ' 應為-> ' + generalagent
            assert agent_list[i] == agent, '額度轉換 -> 代理帳號錯誤 ... ' + agent_list[i] + ' 應為-> ' + agent
            assert member_account_list[i] == member_account, '額度轉換 -> 會員帳號錯誤 ... ' + member_account_list[i] + ' 應為-> ' + member_account
            
        options = ['25', '50', '100', '500']
        for option in options:
            self.select_by_text(WalletTransferLocator.options_selector, option)
            self.check_record_len_first_page(option)
            self.check_page(record_per_page=int(option))
            self.check_record_len_last_page(option)

    def check_search_order_id(self, shareholder):
        '''
            檢查搜尋訂單號碼
        '''
        self.input_account(shareholder=shareholder)
        self.click(WalletTransferLocator.button_last_month)
        self.click(WalletTransferLocator.button_search)
        self.wait_loading_finish()
        self.wait_visibility(WalletTransferLocator.order_id_text)
        order_search = self.get_text(WalletTransferLocator.order_id_text)
        self.type(WalletTransferLocator.order_id_input, order_search)
        self.click(WalletTransferLocator.button_search)
        self.wait_loading_finish()
        order = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.order_id_text))
        assert len(order) == 1, '額度轉換 -> 訂單號碼錯誤 ... 應該只能搜尋到一筆訂單'
        assert order[0] == order_search, '額度轉換 -> 訂單號碼錯誤 ... ' + order[0] + ' 應為-> ' + order_search

    def check_wallet_transfer(self, shareholder):
        '''
            檢查轉出錢包及轉入錢包
        '''
        transfer_out = 'vg|VG'
        transfer_in = 'ag|AG'
        self.input_account(shareholder=shareholder)
        self.click(WalletTransferLocator.transfer_out_span)
        self.type(WalletTransferLocator.transfer_out_input, transfer_out)
        self.type_enter(WalletTransferLocator.transfer_out_input)
        self.click(WalletTransferLocator.button_last_month)
        self.click(WalletTransferLocator.button_search)
        self.wait_loading_finish()
        transfer_out_wallet = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.transfer_out_text))

        self.input_account(shareholder=shareholder)
        self.click(WalletTransferLocator.transfer_in_span)
        self.type(WalletTransferLocator.transfer_in_input, transfer_in)
        self.type_enter(WalletTransferLocator.transfer_in_input)
        self.click(WalletTransferLocator.button_last_month)
        self.click(WalletTransferLocator.button_search)
        self.wait_loading_finish()
        transfer_in_wallet = self.get_text_list_by_dom_list(self.find_elements(WalletTransferLocator.transfer_in_text))
        
        for i in range(len(transfer_out_wallet)):
            assert transfer_out_wallet[i] in transfer_out, '額度轉換 -> 轉出錢包錯誤 ... 搜尋結果與條件不符'
            assert transfer_in_wallet[i] in transfer_in, '額度轉換 -> 轉出錢包錯誤 ... 搜尋結果與條件不符'
