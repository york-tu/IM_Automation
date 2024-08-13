from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import math

class MemberListPageLocator:
    # 查找條件
    account_input = (By.XPATH, '//input[@type="text" and @class="form-control" and @data-y2="focus"]')  # 會員帳號 input
    search_btn = (By.XPATH, '//button[@id="btnSearch"]')                                                # "查找"按鈕

    # 會員列表
    account_text = (By.XPATH, '//td[@data-bind="text: login" and @class="text-left"]')                  # 帳號欄位
    general_agent_text = (By.XPATH, '//td[@data-bind="text: agentlogin" and @class="text-left"]')       # 總代欄位
    agent_text = (By.XPATH, '//td[@data-bind="text: parentlogin" and @class="text-left"]')              # 代理欄位
    available_balance_text = (By.XPATH, '//td[@data-bind="text: balance"]')                             # 可用餘額
    registration_time_text = (By.XPATH, '//td[@data-bind="text: addedtime"]')                           # 註冊時間
    detail = (By.XPATH, '//a[@class="btn btn-default btn-xs "]')                                        # 明細

    last_login_time_text = (By.XPATH, '//dt[contains(text(), "登录时间")]')                              # "最後登入時間" 字串
    last_login_time_data = (By.XPATH, '//dd[contains(@data-bind, "lastlogintime")]')                    # 最後登入時間 資料

    last_order_time_text = (By.XPATH, '//dt[contains(text(), "下注时间")]')                              # "最後下注時間" 字串
    last_order_time_data = (By.XPATH, '//dd[contains(@data-bind, "lastordertime")]')                    # 最後下注時間 資料

    last_order_product_name_text = (By.XPATH, '//dt[contains(text(), "操作游戏")]')                      # "最後操作時間" 字串
    last_order_product_name_data = (By.XPATH, '//dd[contains(@data-bind, "lastorderproductname")]')     # 最後操作時間 資料

    last_deposit_time_text = (By.XPATH, '//dt[contains(text(), "入款時間")]')                            # "最後入款時間" 字串
    last_deposit_time_data = (By.XPATH, '//dd[contains(@data-bind, "lastdeposittime")]')                 # 最後入款時間 資料

    last_withdraw_time_text = (By.XPATH, '//dt[contains(text(), "出款时间")]')                            # "最後出款時間" 字串
    last_withdraw_time_data = (By.XPATH, '//dd[contains(@data-bind, "lastwithdrawtime")]')               # 最後出款時間 資料

    order = (By.XPATH, '//a[@class="btn default btn-xs green-stripe" and contains(@href, "order")]')      # 注單
    ledger = (By.XPATH, '//a[@class="btn default btn-xs green-stripe" and contains(@href, "transaction")]') # 現金流水

    # 注單中心
    order_center = (By.XPATH, '//span[@class="el-breadcrumb__inner"]/a[text()="注单查询"]')                              # 注單中心

    # 現金流水
    transaction_time_ledger = (By.XPATH, '//td[contains(@class,"el-table_1_column_1 ") and @colspan="1"]')              # 交易時間
    account_text_ledger = (By.XPATH, '//td[contains(@class,"el-table_1_column_2")]')                                    # 會員帳號
    current_amount_ledger = (By.XPATH, '//td[contains(@class,"el-table_1_column_6")]')                                  # 當前餘額
    transaction_amount_ledger = (By.XPATH, '//td[contains(@class,"el-table_1_column_7")]')                              # 交易金額
    final_amount_ledger = (By.XPATH, '//td[contains(@class,"el-table_1_column_8")]')                                    # 最後餘額
    today_button_ledger = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"今日")])[1]')            # 今日 按鈕
    this_month_ledger = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"本月")])[1]')              # 本月 按鈕
    last_week_ledger = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"上周")])[1]')               # 上周 按鈕   
    last_month_ledger = (By.XPATH, '(//div[@class="quick-time el-row"]//span[contains(text(),"上月")])[1]')              # 上月 按鈕
    record_total = (By.XPATH, '(//span[@class="el-pagination__total"])[1]')                                             # 紀錄總數
    search_btn_ledger = (By.XPATH, '(//button[@qa-button="search"])[1]')                                                # "查找"按鈕

class MemberListPage(BasePage):
    # 將 DOM 定位list 轉為text list
    def transfer_DOM_list_to_text_list(self, DOM_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for DOM in DOM_list:
            text.append(self.get_text_by_dom(DOM))
        return text

    # 檢查所有會員帳號
    def check_all_member_account_list(self, member_account_list, web_account, is_member_switchin):
        if not is_member_switchin:
            '''
                部分品牌的 test1234 不是代理帳號，因此改用 testaaaa
            '''
            assert web_account not in member_account_list, f'會員列表 > 帳號顯示錯誤 ... {web_account} 已移到 testaaaa 底下'
            return

        for index, Member_account in enumerate(member_account_list):
            Member_account_current = web_account.split('0')[0] + '0' + str(index+1)                       # web_account 為自動化測試的帳號，如:lvbot01
            # 確認頁面取得的帳號資訊
            assert Member_account == Member_account_current, \
                f'會員列表 > 帳號顯示錯誤 第 {index} 項 ... {Member_account} 應為-> {Member_account_current}'

    # 檢查會員的總代
    def check_member_general_agent_list(self, general_agent_list, general_agent_current):
        for index, General_agent in enumerate(general_agent_list):
            # 確認頁面取得的總代資訊
            assert General_agent == general_agent_current, \
                f'會員列表 > 總代顯示錯誤 第 {index} 項 ... {General_agent} 應為-> {general_agent_current}'

    # 檢查會員的代理
    def check_member_agent_list(self, agent_list, agent_current):
        for index, Agent in enumerate(agent_list):
            # 確認頁面取得的代理資訊
            assert Agent == agent_current, \
                f'會員列表 > 代理顯示錯誤 第 {index} 項 ... {Agent} 應為-> {agent_current}'

    # 檢查會員的註冊時間
    def check_member_registration_time_list(self, registration_time_list):
        for index, Registration_time in enumerate(registration_time_list):
            # 確認頁面取得的註冊時間資訊
            assert Registration_time is not ("" or None), f'會員列表 > 註冊時間顯示錯誤 第 {index} 項 ... '

    def check_all_member(self, web_account, general_agent, agent, is_member_switchin):
        '''
            檢查登入帳號旗下所有會員的資訊
        '''
        self.wait_loading_finish()                                                                                                # 等待一下R
        member_account_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.account_text))                # 頁面上的會員帳號
        general_agent_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.general_agent_text))           # 頁面上的總代資訊
        agent_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.agent_text))                           # 頁面上的代理資訊
        registration_time_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.registration_time_text))   # 頁面上的註冊時間資訊
        self.check_all_member_account_list(member_account_list, web_account, is_member_switchin)                                # 檢查所有會員帳號
        self.check_member_general_agent_list(general_agent_list, general_agent)                                                 # 檢查會員的總代
        self.check_member_agent_list(agent_list, agent)                                                                         # 檢查會員的代理
        self.check_member_registration_time_list(registration_time_list)                                                        # 檢查會員的註冊時間

    # 檢查搜尋會員的帳號
    def check_search_member_account_list(self, member_account_list, search_account):
        for index, member_account in enumerate(member_account_list):
            # 確認頁面取得的帳號資訊
            assert member_account == search_account, \
                f'會員列表 > 帳號顯示錯誤 第 {index} 項 ... {member_account} 應為-> {search_account}'

    # 檢查搜尋會員的餘額
    def check_search_member_available_balance_list(self, available_balance_list, available_balance_currect):
        for index, available_balance in enumerate(available_balance_list):
            # 確認頁面取得的可用餘額資訊
            assert float(available_balance) == float(available_balance_currect), \
                f'會員列表 > 可用餘額顯示錯誤 第 {index} 項 ... {available_balance} 應為-> {available_balance_currect}'

    def check_search_member(self, search_account, general_agent, agent, available_balance):
        '''
            檢查搜尋的會員資訊
        '''
        self.wait_loading_finish()                                                                                                # 等待一下R
        self.type(MemberListPageLocator.account_input, search_account)                                                          # 輸入要搜尋的帳號
        self.click(MemberListPageLocator.search_btn)                                                                            # 點擊"查找"按鈕
        self.wait_loading_finish()                                                                                                # 等待一下R
        member_account_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.account_text))                # 頁面上的會員帳號
        available_balance_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.available_balance_text))   # 頁面上的可用餘額
        general_agent_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.general_agent_text))           # 頁面上的總代資訊
        agent_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.agent_text))                           # 頁面上的代理資訊
        registration_time_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.registration_time_text))   # 頁面上的註冊時間資訊
        self.check_search_member_account_list(member_account_list, search_account)                                              # 檢查搜尋會員的帳號
        self.check_search_member_available_balance_list(available_balance_list, available_balance)                              # 檢查搜尋會員的餘額
        self.check_member_general_agent_list(general_agent_list, general_agent)                                                 # 檢查會員的總代
        self.check_member_agent_list(agent_list, agent)                                                                         # 檢查會員的代理
        self.check_member_registration_time_list(registration_time_list)                                                        # 檢查會員的註冊時間
    
    def check_search_member_switchout(self, search_account):
        '''
            檢查會員被切出去後搜尋的資訊
        '''
        self.wait_loading_finish()                                                                                                # 等待一下R
        self.type(MemberListPageLocator.account_input, search_account)                                                          # 輸入要搜尋的帳號
        self.click(MemberListPageLocator.search_btn)                                                                            # 點擊"查找"按鈕
        self.wait_loading_finish()                                                                                                # 等待一下R
        locator = (By.XPATH, '//*[contains(text(), "{0}")]'.format(search_account))
        assert self.is_element_finded(locator) == False, '列表顯示錯誤 > 列表應為空'

    # 檢查日期
    def check_date_list(self, date_list, date_verify):
        for index, date in enumerate(date_list):
            assert date.__contains__(str(date_verify)), f'時間錯誤 ... 第 {index} 項 {date.split(" ")[0]} 應為-> {date_verify}'

    def check_detail(self):
        '''
            檢查明細
        '''
        self.wait_loading_finish()                                                                                                # 等待一下R
        self.click(MemberListPageLocator.detail)
        self.wait_loading_finish()                                                                                                # 等待一下R
        assert self.is_element_displayed(MemberListPageLocator.last_login_time_text), '最後登入時間 未顯示'
        assert self.is_element_displayed(MemberListPageLocator.last_order_time_text), '最後下注時間 未顯示'
        assert self.is_element_displayed(MemberListPageLocator.last_order_product_name_text), '最後操作遊戲 未顯示'
        assert self.is_element_displayed(MemberListPageLocator.last_deposit_time_text), '最後入款時間 未顯示'
        assert self.is_element_displayed(MemberListPageLocator.last_withdraw_time_text), '最後出款時間 未顯示'

        date_list = self.transfer_DOM_list_to_text_list([self.find_element(MemberListPageLocator.last_login_time_data), 
                    self.find_element(MemberListPageLocator.last_order_time_data), 
                    self.find_element(MemberListPageLocator.last_deposit_time_data), 
                    self.find_element(MemberListPageLocator.last_withdraw_time_data), 
                    ])
                    
        self.check_date_list(date_list, self.get_us_time().strftime('%Y-%m-%d'))
        assert self.get_text(MemberListPageLocator.last_order_product_name_data) != '无资料', '最後操作遊戲 資料錯誤'
    
    # 檢查 點擊注單按鈕
    def check_click_order_button(self):
        self.wait_loading_finish()
        self.click(MemberListPageLocator.order)
        self.wait_loading_finish()
        assert self.get_text(MemberListPageLocator.order_center).__contains__('注单查询'), '注單按鈕未重新導向注单查询'
        self.back()

    # 檢查餘額
    def check_available_balance(self, current_amount_list, transaction_amount_list, final_amount_list):
        for i in range(len(current_amount_list)):
            current_amount_float = float(current_amount_list[i])
            transaction_amount_float = float(transaction_amount_list[i])
            final_amount_float = float(final_amount_list[i])
            error_message = f'餘額顯示錯誤... 當前:{current_amount_float} 交易:{transaction_amount_float} 最後:{final_amount_float}'
            assert final_amount_float == round(current_amount_float + transaction_amount_float, 2), error_message

    # 檢查現金流水的資料
    def check_transaction_list(self, admin_data, reseller_data):
   
        index = []
        for i in range(len(admin_data)):
            for j in range(len(admin_data[i])):
                if i == 0 and j < len(admin_data[i]) - 1 and admin_data[i][j] == admin_data[i][j+1]:
                    if j not in index:
                        index.append(j)

                    if j + 1 not in index:
                        index.append(j+1)
                
                if i > 1 and j in index:
                    assert reseller_data[i][j] in [admin_data[i][k] for k in index], f'現金流水 > 資料錯誤 第 {i} 行 第 {j} 列 ... {reseller_data[i][j]}'
                else:
                    assert admin_data[i][j] == reseller_data[i][j], f'現金流水 > 資料錯誤 第 {i} 行 第 {j} 列 ... {reseller_data[i][j]} 應為-> {admin_data[i][j]}'

    def check_click_ledger_button(self, search_account, admin_data):
        '''
            檢查現金流水
        '''
        self.wait_loading_finish()                                                                                                        # 等待一下R
        self.type(MemberListPageLocator.account_input, search_account)                                                                  # 輸入要搜尋的帳號
        self.click(MemberListPageLocator.search_btn)                                                                                    # 點擊"查找"按鈕
        self.wait_loading_finish()                                                                                                        # 等待一下R
        self.sleep(3)

        self.click(MemberListPageLocator.ledger)                                                                                        # 點擊現金流水按鈕
        self.wait_visibility(MemberListPageLocator.search_btn_ledger)                                                                    # 等待一下R
        self.wait_loading_finish()
        
        self.click(MemberListPageLocator.today_button_ledger)                                                                           # 點擊"今日"按鈕
        self.click(MemberListPageLocator.search_btn_ledger)                                                                             # 點擊"查找"按鈕
        self.wait_loading_finish()                                                                                                        # 等待一下R
        transaction_time_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.transaction_time_ledger))   # 交易時間的list
        member_account_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.account_text_ledger))         # 會員帳號的list
        current_amount_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.current_amount_ledger))       # 當前餘額的list
        transaction_amount_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.transaction_amount_ledger))   # 交易金額的list
        final_amount_list = self.transfer_DOM_list_to_text_list(self.find_elements(MemberListPageLocator.final_amount_ledger))           # 最後餘額的list
        reseller_data = [transaction_time_list, member_account_list, current_amount_list, transaction_amount_list, final_amount_list]   # 所有資料的list

        self.check_search_member_account_list(member_account_list, search_account)                                                      # 檢查會員帳號
        self.check_available_balance(current_amount_list, transaction_amount_list, final_amount_list)                                   # 檢查餘額
        self.check_transaction_list(admin_data, reseller_data)                                                                          # 檢查現金流水

        self.wait_visibility(locator=MemberListPageLocator.this_month_ledger)
        self.click(locator=MemberListPageLocator.this_month_ledger)                                              # 先點擊"本月"按鈕
        self.click(locator=MemberListPageLocator.search_btn_ledger)
        self.sleep(1)
        if int(self.get_text(locator=MemberListPageLocator.record_total)[2:-2]) <= 25:
            self.click(locator=MemberListPageLocator.last_week_ledger)                                          # 本月資料小於25則點擊"上周"按鈕
            self.click(locator=MemberListPageLocator.search_btn_ledger)
            self.sleep(1)
        if int(self.get_text(locator=MemberListPageLocator.record_total)[2:-2]) <= 25:                           # 若"上周"資料小於25則return
            self.back()
            return

        self.check_page_v2()
        self.back()
