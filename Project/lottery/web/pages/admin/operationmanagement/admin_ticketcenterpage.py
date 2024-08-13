from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

import datetime
import math

class TicketCenterPageLocator():
    # =============== 搜尋區 ==================
    ticket_number_input_box = (By.XPATH, "//div[@id='pane-tab-template-center']//input[@qa-input='number']")                                       # 訂單號碼輸入
    member_account_input_box = (By.XPATH, "//div[@id='pane-tab-template-center']//input[@qa-input='member_login']")                                # 會員帳號
    period_input_box = (By.XPATH, "//div[@id='pane-tab-template-center']//input[@qa-input='product_number']")                                      # 期數場次
    auto_refresh_check = (By.XPATH, "//div[@id='pane-tab-template-center']//label[@qa-checkbox='interval-auto']")                                  # 自動刷新勾選
    auto_refresh = (By.XPATH, "//div[@id='pane-tab-template-center']//input[@qa-input='interval-time']")                                           # 自動刷新秒數

    type_of_channel = (By.XPATH, "//select[contains(@data-bind,'channel_name') and @class='form-control select2me channelSelectHandle select2-offscreen']")      # 頻道類型
    class_of_channel = (By.XPATH, "//select[contains(@data-bind,'category_name') and @class='form-control select2me categorySelectHandle select2-offscreen']")   # 頻道分類
    type_of_product = (By.XPATH, "//select[contains(@data-bind,'product_type_name') and @class='form-control select2me prodcutSelectHandle select2-offscreen']") # 產品類型
    class_of_play = (By.XPATH, "//select[contains(@data-bind,'play_type_name') and @class='form-control select2me playTypeSelectHandle select2-offscreen']")     # 玩法類型

    #---------派彩狀態---------
    radio_btn_all = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='payout']/label[1]")                                                         # 全部
    radio_btn_already_payout = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='payout']/label[2]")                                              # 已派彩
    radio_btn_notyet_payout = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='payout']/label[3]")                                               # 未派彩

    #---------派彩時間---------
    payout_time_start = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//div[@qa-input='quick-time-date']/input[1]")              # 派彩起始時間
    payout_time_end = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//div[@qa-input='quick-time-date']/input[2]")                # 派彩結束時間
    btn_payout_today = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-today']")                   # 派彩-今日按鈕
    btn_payout_yesterday = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-yestoday']")            # 派彩-昨日按鈕
    btn_payout_thisweek = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-thisWeek']")             # 派彩-本周按鈕
    btn_payout_lastweek = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-lastWeek']")             # 派彩-上周按鈕
    btn_payout_thismonth = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-thisMonth']")           # 派彩-本月按鈕
    btn_payout_lastmonth = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-lastMonth']")           # 派彩-上月按鈕
    
    #---------下注時間---------
    bet_time_start = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//div[@qa-input='quick-time-date']/input[1]")          # 下注起始時間
    bet_time_end = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//div[@qa-input='quick-time-date']/input[2]")            # 下注結束時間
    btn_bet_today = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-today']")               # 下注-今日按鈕
    btn_bet_yesterday = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-yestoday']")        # 下注-昨日按鈕
    btn_bet_thisweek = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-thisWeek']")         # 下注-本周按鈕
    btn_bet_lastweek = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-lastWeek']")         # 下注-上周按鈕
    btn_bet_thismonth = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-thisMonth']")       # 下注-本月按鈕
    btn_bet_lastmonth = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-date-picker='added-time']//button[@qa-button='quick-time-lastMonth']")       # 下注-上月按鈕

    #---------查詢狀態---------
    input_shareholder = (By.XPATH, "//div[@qa-select='sharelogin']//input[@class='el-input__inner']")
    input_generalagent = (By.XPATH, "//input[@qa-input='generalagent']")                                                        # 總代輸入
    input_agent = (By.XPATH, "//input[@qa-input='agent']")                                                                      # 代理輸入

    #---------訂單狀態---------
    radio_btn_all_ticket = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='status']/label[1]")                                # 全部
    radio_btn_tobeconfirmed = (By.XPATH, "//div[@id='tab_1_1']//div[@class='col-md-7']/label[2]")                                               # 待確認
    radio_btn_confirmed = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='status']/label[2]")                                 # 已確認
    radio_btn_notsuccessful = (By.XPATH, "//div[@id='tab_1_1']//div[@class='col-md-7']/label[4]")                                               # 未成功
    radio_btn_abnormal = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='status']/label[3]")                                  # 有異常
    radio_btn_obsolete = (By.XPATH, "//div[@id='pane-tab-template-center']//div[@qa-radio='status']/label[4]")                                  # 已作廢

    btn_search = (By.XPATH, "//button[@qa-button='query']")                                                                     # 查找按鈕
    btn_export = (By.XPATH, "//button[@qa-button='export']")                                                                    # 匯出按鈕
    btn_export_confirm = (By.XPATH, "//p[contains(text(),'确定汇出吗？')]/..//span[contains(text(),'确定')]")                              # 匯出確認按鈕

    # ===============注單詳情===============
    order_time = (By.XPATH, "//td[@class='el-table_3_column_10 is-center ']//p[contains(text(),':')]/..")                           # 下注時間
    member_account = (By.XPATH, "//a[@qa-a='member_login']")                                                                        # 會員帳號    會多抓到小計與總計的空值
    type_of_game = (By.XPATH, "//td[@class='el-table_3_column_13 is-center ']")                                                     # 遊戲類別    會多抓到小計與總計的空值
    ticket_number = (By.XPATH, "//td[@class='el-table_3_column_14 is-center ']")                                                    # 單號    會多抓到小計與總計的空值
    period = (By.XPATH, "//td[@class='el-table_3_column_15 is-center ']")                                                           # 期數    會多抓到小計與總計的空值
    order_detail = (By.XPATH, "//td[@class='el-table_3_column_16 is-center ']//p[1]")                                               # 注單詳情 彩種
    order_detail_money = (By.XPATH, "//td[@class='el-table_3_column_16 is-center ']//p[2]")                                         # 注單詳情 金額
    lottery_result = (By.XPATH, "//td[@class='el-table_3_column_17 is-center ']//div[@class='product-result-content__scroll']")     # 開獎結果
    order_money = (By.XPATH, "//td[@class='el-table_3_column_18 is-center ']")                                                      # 注額    會多抓到小計與總計的值
    payout_money_amount = (By.XPATH, "//td[@class='el-table_3_column_19 is-center ']//p[1]")                                        # 派彩    會多抓到小計與總計的值
    payout_money_rebate = (By.XPATH, "//td[@class='el-table_3_column_19 is-center ']//p[2]")                                        # 返水    會多抓到小計與總計的值
    payout_income = (By.XPATH, "//td[@class='el-table_3_column_20 is-right ']")                                                     # 損益    會多抓到小計與總計的空值
    payout_point = (By.XPATH, "//td[@class='el-table_3_column_21 is-right ']")                                                      # 打碼/有效投注    會多抓到小計與總計的空值
    bonus = (By.XPATH, "//tbody[1]//tr//span[contains(@data-bind, 'bonus')][1]")                                                    # 獎金
    payout_settlement = (By.XPATH, "//td[@class='el-table_3_column_22 is-center ']/div/div/p[1]")                                   # 結算
    payout_date = (By.XPATH, "//td[@class='el-table_3_column_22 is-center ']/div/div/p[2]")                                         # 派彩日期
    payout_time = (By.XPATH, "//td[@class='el-table_3_column_22 is-center ']/div/div/p[3]")                                         # 派彩時間
    # 小計、總計
    total_count = (By.XPATH, "//p[contains(text(),'总计')]")                                                        # 總計 (ex:总计(4条))
    total_money = (By.XPATH, "//p[contains(text(),'总计')]/../../../td[9]")                                         # 總計-注額
    total_payout = (By.XPATH, "//p[contains(text(),'总计')]/../../..//p[contains(text(),'派彩:')]")                 # 總計-派彩 (ex:派彩: 1.98)
    total_rebate = (By.XPATH, "//p[contains(text(),'总计')]/../../..//p[contains(text(),'返水:')]")                 # 總計-返水 (ex:返水: 0.01)
    total_income = (By.XPATH, "//p[contains(text(),'总计')]/../../../td[11]")                                       # 總計-損益
    total_point = (By.XPATH, "//p[contains(text(),'总计')]/../../../td[12]")                                        # 總計-打碼/有效投注

    subtotal_money = (By.XPATH, "(//tr[@class='el-table__row'])[last()-1]//td[@class='el-table_3_column_18 is-center ']")               # 小計-注額
    subtotal_payout = (By.XPATH, "(//tr[@class='el-table__row'])[last()-1]//td[@class='el-table_3_column_19 is-center ']//p[1]")        # 小計-派彩
    subtotal_rebate = (By.XPATH, "(//tr[@class='el-table__row'])[last()-1]//td[@class='el-table_3_column_19 is-center ']//p[2]")        # 小計-返水
    subtotal_income = (By.XPATH, "(//tr[@class='el-table__row'])[last()-1]//td[@class='el-table_3_column_20 is-right ']")               # 小計-損益
    subtotal_point = (By.XPATH, "(//tr[@class='el-table__row'])[last()-1]//td[@class='el-table_3_column_21 is-right ']")                # 小計-打碼/有效投注

    operation_field_detail =  (By.XPATH, "//button[@qa-button='detail']")                                                               # 操作欄-明細
    # 明細內容
    detail_channel = (By.XPATH, "//div[@aria-hidden='false']/p[2]")                                                    # 明細-頻道
    detail_play = (By.XPATH, "//div[@aria-hidden='false']/p[4]")                                                       # 明細-玩法
    detail_shareholder = (By.XPATH, "//div[@aria-hidden='false']/p[5]")                                                # 明細-股東
    detail_generalagent = (By.XPATH, "//div[@aria-hidden='false']/p[6]")                                               # 明細-總代

    operation_field_repay =  (By.XPATH, "//button[@qa-button='repayout']")                                              # 操作欄-重派
    btn_repay_confirm = (By.XPATH, "//div[@aria-hidden='false']//span[contains(text(),'确定')]")
    operation_field_obsolete =  (By.XPATH, "//button[@qa-button='cancel']")                                             # 操作欄-作廢

    total_record = (By.XPATH, "//span[@class='el-pagination__total']")                                                  # 共幾條紀錄 (ex:共 4 条)
    amount_per_page = (By.XPATH, "//span[@class='el-pagination__sizes']//input")                                        # 每頁幾筆檢視
    btn_pages = (By.XPATH, "//div[@class='pull-right']//li[@class='active']")

    # ===============排序按鈕===============
    sort_bet_time = (By.XPATH, "//thead[@class='has-gutter']//span[contains(text(), '下注时间(美东)')]")        # 排序下注時間
    sort_order_money = (By.XPATH, "//thead[@class='has-gutter']//span[contains(text(), '注额')]")               # 排序注額
    sort_payout_money = (By.XPATH, "//thead[@class='has-gutter']//span[contains(text(), '派彩')]")              # 排序派彩
    empty_message = (By.XPATH, "//div[@id='pane-tab-template-center']//span[contains(text(),'暂无数据')]")      # 列表暫無數據訊息

class TicketCenterPage(BasePage):

    def get_total_information_by_shareholder(self, search_account):
        '''
            取得所有總計的值
        '''
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.input_shareholder, search_account)
        dropdown_shareholder=(By.XPATH, "//div[@x-placement='bottom-start']//span[contains(text(),'"+ search_account+"')]")
        self.wait_visibility(dropdown_shareholder)      #lv股東太多導致下拉選單沒出現bot的股東，已開單處理 PFREQ-1985
        self.click(dropdown_shareholder)
        self.click(TicketCenterPageLocator.btn_payout_today)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        total_count = total_money = total_payout = total_rebate = total_income = total_point = 0.0

        if not self.is_element_finded(TicketCenterPageLocator.empty_message):
            total_count = float((self.get_text(TicketCenterPageLocator.total_count))[3:-2].replace(',', ''))
            total_money = float((self.get_text(TicketCenterPageLocator.total_money)).replace(',', ''))
            total_payout = float((self.get_text(TicketCenterPageLocator.total_payout))[4:].replace(',', ''))
            total_rebate = float((self.get_text(TicketCenterPageLocator.total_rebate))[4:].replace(',', ''))
            total_income = float((self.get_text(TicketCenterPageLocator.total_income)).replace(',', ''))
            total_point = float((self.get_text(TicketCenterPageLocator.total_point)).replace(',', ''))

        return [total_count, total_money, total_payout, total_rebate, total_income, total_point]

    def ticketnumber_memberaccount_period_check(self, record_hk, account):
        # 訂單號碼查詢
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.ticket_number_input_box, record_hk['ticket_name'])
        self.click(TicketCenterPageLocator.btn_bet_thisweek)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        detail = self.ticket_list_one()
        self.detail_record_compare(detail, record_hk, '訂單查詢')
        
        # 會員帳號查詢
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.member_account_input_box, account)
        self.click(TicketCenterPageLocator.btn_bet_thisweek)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        detail = self.ticket_list_one()
        self.detail_record_compare(detail, record_hk, '帳號查詢')
    
        # 期數場次查詢
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.period_input_box, record_hk['period'])
        self.click(TicketCenterPageLocator.btn_bet_thisweek)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        detail = self.ticket_list_one()
        self.detail_record_compare(detail, record_hk, '期數查詢')

    # 搜尋列表詳情(第一筆)
    def ticket_list_one(self):
        if len(self.find_elements(TicketCenterPageLocator.order_time)) > 0:
            record_order_time = self.get_text(TicketCenterPageLocator.order_time)
            record_order_time = datetime.datetime.strptime(record_order_time, '%Y-%m-%d %H:%M:%S')
            record_order_time = str(record_order_time + datetime.timedelta(hours=12))
            type_of_game = self.get_text(TicketCenterPageLocator.type_of_game)
            ticket_number = self.get_text(TicketCenterPageLocator.ticket_number)
            period = self.get_text(TicketCenterPageLocator.period)
            order_detail = self.get_text(TicketCenterPageLocator.order_detail)
            order_detail = order_detail + self.get_text(TicketCenterPageLocator.order_detail_money)
            order_money = self.get_text(TicketCenterPageLocator.order_money)
            detail = {'record_order_time': record_order_time,
                    'type_of_game': type_of_game,
                    'ticket_number': ticket_number,
                    'period': period,
                    'order_detail': order_detail,
                    'order_money': order_money}
            return detail
        else:
            return None

    # 比對搜尋結果、下注紀錄
    def detail_record_compare(self, detail, record, type_of_search=''):
        if detail != None:
            assert detail['order_detail'] == record['type'], '注單詳情不正確({})'.format(type_of_search)
            assert detail['ticket_number'] == record['ticket_name'], '單號不正確({})'.format(type_of_search)
            assert detail['type_of_game'] == '六合彩', '彩種不正確({})'.format(type_of_search)
            assert detail['period'] == record['period'], '期數不正確({})'.format(type_of_search)
            assert detail['order_money'] == '1', '注額不正確({})'.format(type_of_search)
            assert detail['record_order_time'][:-9] == record['time'], '下注時間不正確({})'.format(type_of_search)
        else:
            assert False, '查無資料({})'.format(type_of_search)
    
    # 頻道類型、產品類型、玩法類型 搜尋檢查
    def type_of_channel_check(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.select_by_text(TicketCenterPageLocator.type_of_channel, "极速彩种")
        self.select_by_text(TicketCenterPageLocator.type_of_product, "极速快3")
        self.select_by_text(TicketCenterPageLocator.class_of_play, "两面")
        self.click(TicketCenterPageLocator.btn_bet_thisweek)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()

        for element in (self.find_elements(TicketCenterPageLocator.type_of_game)):
            assert self.get_text_by_dom(element)=='极速快3', '產品類型錯誤'
        for element in (self.find_elements(TicketCenterPageLocator.order_detail)):
            assert "两面" in self.get_text_by_dom(element), '玩法類別錯誤'
    
    # 派彩狀態 搜尋檢查
    def payout_status_check(self):
        # 未派彩資料搜尋
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.radio_btn_notyet_payout) # 派彩狀態 - 未派彩
        self.click(TicketCenterPageLocator.btn_bet_today)
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        for element in self.find_elements(TicketCenterPageLocator.payout_settlement):
            assert self.get_text_by_dom(element)=='待派彩', '未派彩搜尋錯誤' 

        # 已派彩資料搜尋
        self.click(TicketCenterPageLocator.radio_btn_already_payout) # 派彩狀態 - 已派彩
        self.click(TicketCenterPageLocator.btn_search)
        self.wait_loading_finish()
        for element in self.find_elements(TicketCenterPageLocator.payout_settlement):
            assert self.get_text_by_dom(element)=='已派彩', '已派彩搜尋錯誤'

    # 股東、總代、代理 搜尋檢查
    def shareholder_generalagent_agent(self, shareholder, generalagent, agent):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.input_shareholder, shareholder)     # 輸入股東
        self.click(TicketCenterPageLocator.btn_bet_today)                     # 派彩時間
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()
        shareholder_cnt = (self.get_text(TicketCenterPageLocator.total_record))[2:-2]  # 股東筆數
        assert shareholder_cnt != 0, '股東筆數為0'

        self.type(TicketCenterPageLocator.input_shareholder, "")
        self.type(TicketCenterPageLocator.input_generalagent, generalagent)   # 輸入總代
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()
        generalagent_cnt = (self.get_text(TicketCenterPageLocator.total_record))[2:-2] # 總代筆數
        assert generalagent_cnt != 0, '總代筆數為0'

        self.type(TicketCenterPageLocator.input_generalagent, "")
        self.type(TicketCenterPageLocator.input_agent, agent)                 # 輸入代理 
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()
        agent_cnt = (self.get_text(TicketCenterPageLocator.total_record))[2:-2]        # 代理筆數
        assert agent_cnt != 0, '代理筆數為0'

        assert shareholder_cnt == generalagent_cnt == agent_cnt, '股東、總代、代理 筆數不相符'

    # 下注時間排序檢查
    def record_sort_check_bet_time(self):

        # 確認目前排序 (asc 小到大、 desc 大到小)
        def find_typeofsort():
            type_of_sort = ['-asc', '-desc']
            if self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[0]))):
                return 'asc'
            elif self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[1]))):
                return 'desc'
            else:
                return 'default'
        
        # 檢查資料排序是否正確           
        def check_list_sort(typesort):
            # 查找第一頁各筆資料下注時間
            bet_time_list = []
            for element in self.find_elements(TicketCenterPageLocator.order_time):
                time_str = self.get_text_by_dom(element)
                tmp = ''.join([char for char in time_str if char not in "- :"])  # 下注時間去掉不必要字元( -:)
                bet_time_list.append(int(tmp))                                   # 下注時間int型態存入 以便排序比較
            
            if typesort == 'asc':                                               # asc 為升序
                assert sorted(bet_time_list, reverse=False) == bet_time_list, '下注時間升序檢查錯誤'
            elif typesort == 'default' or typesort=='desc':                     # default desc 為降序
                assert sorted(bet_time_list, reverse=True) == bet_time_list, '下注時間降序檢查錯誤'

        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_bet_lastmonth)                 # 下注時間
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()

        self.click(TicketCenterPageLocator.sort_bet_time)                     # 按下注時間排序鈕 (第一下轉換為asc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())                                    # 排序檢查錯誤 (確認網頁目前的排序方式)

        self.click(TicketCenterPageLocator.sort_bet_time)                     # 按下注時間排序鈕 (第二下轉換為desc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())                                    # 排序檢查錯誤 (確認網頁目前的排序方式)
    
    # 注額排序檢查
    def record_sort_check_order_money(self):

        # 確認目前排序 (asc 小到大、 desc 大到小)
        def find_typeofsort():
            type_of_sort = ['-asc', '-desc']
            if self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[0]))):
                return 'asc'
            elif self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[1]))):
                return 'desc'
            else:
                return 'default'

        # 檢查資料排序是否正確           
        def check_list_sort(typesort):
            # 查找第一頁各筆資料注額
            order_money_list = []
            for element in self.find_elements(TicketCenterPageLocator.order_money):
                money_str = self.get_text_by_dom(element)
                order_money_list.append(float(money_str))                     # 注額float型態存入 以便排序比較

            if typesort == 'asc':                                               # asc 為升序
                assert sorted(order_money_list, reverse=False) == order_money_list, '注額升序檢查錯誤'
            elif typesort == 'default' or typesort == 'desc':                     # default desc 為降序
                assert sorted(order_money_list, reverse=True) == order_money_list, '注額降序檢查錯誤'

        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_bet_lastmonth)                 # 下注時間
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()

        self.click(TicketCenterPageLocator.sort_order_money)                  # 按注額排序鈕 (第一下轉換為asc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())                                    # 排序檢查錯誤 (確認網頁目前的排序方式)
        
        self.click(TicketCenterPageLocator.sort_order_money)                  # 按注額排序鈕 (第二下轉換為desc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())                                    # 排序檢查錯誤 (確認網頁目前的排序方式)

    # 派彩排序檢查
    def record_sort_check_payout_money(self):

        # 確認目前排序 (asc 小到大、 desc 大到小)
        def find_typeofsort():
            type_of_sort = ['-asc', '-desc']
            if self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[0]))):
                return 'asc'
            elif self.is_element_finded((By.XPATH, "//i[@class='fa fa-fw fa-sort{:}']".format(type_of_sort[1]))):
                return 'desc'
            else:
                return 'default'

        # 檢查資料排序是否正確           
        def check_list_sort(typesort):
            # 查找第一頁各筆資料注額
            payout_money_list = []
            for element in self.find_elements(TicketCenterPageLocator.payout_money_amount):
                money_str = self.get_text_by_dom(element)
                payout_money_list.append(float(money_str.lstrip('派彩：')))    # 派彩float型態存入 以便排序比較

            if typesort == 'asc':                                               # asc 為升序
                assert sorted(payout_money_list, reverse=False) == payout_money_list, '派彩升序檢查錯誤'
            elif typesort == 'default' or typesort == 'desc':                     # default desc 為降序
                assert sorted(payout_money_list, reverse=True) == payout_money_list, '派彩降序檢查錯誤'

        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_payout_lastmonth)              # 派彩時間
        self.click(TicketCenterPageLocator.btn_search)                        # 搜尋
        self.wait_loading_finish()

        self.click(TicketCenterPageLocator.sort_payout_money)                  # 按派彩排序鈕 (第一下轉換為asc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())

        self.click(TicketCenterPageLocator.sort_payout_money)                  # 按派彩排序鈕 (第二下轉換為desc)
        self.wait_loading_finish()
        check_list_sort(find_typeofsort())
    
    # 紀錄操作欄位檢查
    def operation_field_check(self, record_js3, shareholder='', generalagent=''):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.ticket_number_input_box, record_js3['ticket_name'])
        self.click(TicketCenterPageLocator.btn_bet_today)                                                       # 派彩時間
        self.click(TicketCenterPageLocator.btn_search)                                                          # 搜尋
        self.wait_loading_finish()
        
        # 點擊明細
        self.click(TicketCenterPageLocator.operation_field_detail)                                              # 展開明細
        channel = self.get_text(TicketCenterPageLocator.detail_channel)                                          # 頻道(record_js3 - 极速彩种)
        playtype = self.get_text(TicketCenterPageLocator.detail_play)                                            # 玩法(record_js3 - 两面)
        detail_shareholder = self.get_text(TicketCenterPageLocator.detail_shareholder)                           # 股東
        detail_generalagent = self.get_text(TicketCenterPageLocator.detail_generalagent)                         # 總代

        assert channel == '极速彩种', '頻道比對錯誤'
        assert playtype == '两面', '玩法比對錯誤'
        assert detail_shareholder == shareholder, '股東比對錯誤'
        assert detail_generalagent == generalagent, '總代比對錯誤'
        self.click(TicketCenterPageLocator.operation_field_detail)                                              # 關閉明細

        # 點擊重派
        self.click(TicketCenterPageLocator.operation_field_repay)                                               # 按重派鈕
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_repay_confirm)                                                   # 重派確認按鈕
        self.wait_loading_finish()
        assert self.get_text(TicketCenterPageLocator.payout_settlement) == '派彩中', '重派後結算欄位檢查錯誤'        # 按重派後 結算欄位會從已派彩至派彩中
        self.click(TicketCenterPageLocator.btn_search)                                                          # 搜尋
        self.wait_loading_finish()
        assert self.get_text(TicketCenterPageLocator.payout_settlement) == '已派彩', '重後再次搜尋結算欄位檢查錯誤'   # 重派後再次搜尋 結算欄位會從派彩中至已派彩

        # 點擊作廢
        self.click(TicketCenterPageLocator.operation_field_obsolete)                                            # 按作廢按鈕
        # self.wait_loading_finish()
        
        self.sendkey_alert('1') # 輸入OTP
        self.accept_alert()     # 輸入後按OK
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_search)                                                          # 作廢該筆資料後再已 訂單狀態-已確認(默認) 搜尋一次 確認找不到該筆資料
        self.wait_loading_finish()
        if not self.is_element_finded(TicketCenterPageLocator.order_time):                                        # 確認找不到該筆資料
            self.click(TicketCenterPageLocator.radio_btn_obsolete)                                              # 訂單狀態選擇 - 已作廢
            self.click(TicketCenterPageLocator.btn_search)                                                      # 再搜尋一次
            self.wait_loading_finish()
            # 檢查 已作廢狀態搜尋此單是否有資料、搜出資料之單號是否正確
            assert self.is_element_finded(TicketCenterPageLocator.ticket_number)\
                and self.get_text(TicketCenterPageLocator.ticket_number) == record_js3['ticket_name'], '搜尋單號 訂單狀態-已作廢 錯誤'          
        else:
            assert False, '作廢後還是查找到資料'

    # 檢查 分別已25、50、100、500筆 檢視是否正確
    def check_25_50_100_500(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_bet_lastmonth)         # 下注時間
        self.click(TicketCenterPageLocator.btn_search)                # 搜尋
        self.wait_loading_finish()

        amount_list = ['25', '50', '100', '500']                      # 檢查的筆數
        total_records = int((self.get_text(TicketCenterPageLocator.total_record))[2:-2]) # 搜尋總筆數          
        for amount in amount_list:
            self.select_by_text(TicketCenterPageLocator.amount_per_page, amount)  # 選擇已每頁幾筆檢視
            self.wait_loading_finish()
            # 總筆數若'大'於檢視比數 第一頁筆數應為檢視筆數
            if total_records > int(amount):
                assert len(self.find_elements(TicketCenterPageLocator.order_time)) == int(amount), '已{:}筆檢視，第一頁不足{:}筆'.format(amount, amount)
            # 總筆數若'小'於檢視比數 第一頁比數應為總筆數
            else:
                assert len(self.find_elements(TicketCenterPageLocator.order_time)) == total_records, '總筆數小於{:}檢視筆數，檢視結果應為{:}筆，卻為{:}筆'.format(amount, total_records,
                 len(self.find_elements(TicketCenterPageLocator.order_time)))
    
    # 注額、派彩、損益、打碼 小計與總量檢查
    def check_total_subtotal(self):

        def get_details():
            money = self.find_elements(TicketCenterPageLocator.order_money) # 注額
            payout = self.find_elements(TicketCenterPageLocator.payout_money_amount) # 派彩
            rebate = self.find_elements(TicketCenterPageLocator.payout_money_rebate) # 返水
            income = self.find_elements(TicketCenterPageLocator.payout_income) # 損益
            point = self.find_elements(TicketCenterPageLocator.payout_point) # 打碼
            
            return money, payout, rebate, income, point

        self.refresh_browser()
        self.wait_loading_finish()
        self.click(TicketCenterPageLocator.btn_payout_lastmonth)         # 派彩時間
        self.click(TicketCenterPageLocator.btn_search)                   # 搜尋
        self.wait_loading_finish()
        self.select_by_text(TicketCenterPageLocator.amount_per_page, '500')  # 選擇已每頁幾筆檢視
        self.wait_loading_finish()
        pages = math.ceil(int((self.get_text(TicketCenterPageLocator.total_record))[2:-2]) / 500) # 抓換500筆檢視 共有幾頁
        # 換頁
        if pages > 1:
            self.click((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(pages)))
            self.wait_loading_finish()

        money, payout, rebate, income, point = get_details()
        total_money = 0 # 每筆注額加總
        total_payout = 0 # 每筆派彩加總
        total_rebate = 0 # 每筆返水加總
        total_income = 0 # 每筆損益加總
        total_point = 0 # 每筆打碼加總
        
        page_cnt = 1
        # 遍歷這搜尋結果紀錄總筆數
        for idx in range(len(money)):
            # print(idx, ': ' ,self.get_text_by_dom(payout[idx - (page_cnt-1)*500]))
            total_payout += float(self.get_text_by_dom(payout[idx - (page_cnt-1)*500]).lstrip('派彩：').replace(',', '')) # 第 [idx] 筆派彩
            total_money += float(self.get_text_by_dom(money[idx - (page_cnt-1)*500]).replace(',', '')) # 第 [idx] 筆注額
            total_rebate += float(self.get_text_by_dom(rebate[idx - (page_cnt-1)*500]).lstrip('返水：').replace(',', '')) # 第 [idx] 筆返水
            total_income += float(self.get_text_by_dom(income[idx - (page_cnt-1)*500]).replace(',', '')) # 第 [idx] 筆損益
            total_point += float(self.get_text_by_dom(point[idx - (page_cnt-1)*500]).replace(',', '')) # 第 [idx] 筆打碼

            # 存當頁的 注額、派彩、返水、損益、打碼
            thispage_money = total_money
            thispage_payout = total_payout
            thispage_rebate = total_rebate
            thispage_income = total_income
            thispage_point = total_point

            if (idx + 1) % 500 == 0:
                break # 要抓取大於500筆 把break掉
                page_cnt += 1
                if self.is_element_finded((By.XPATH,"//div[@class='pull-right']//a[text()='{:}']".format(page_cnt))):
                    self.click((By.XPATH,"//div[@class='pull-right']//a[text()='{:}']".format(page_cnt)))
                    self.wait_loading_finish()
                    money, payout, rebate, income, point = get_details()

        # 跟當頁小計比對是否吻合
        assert round(thispage_money, 2) == float(self.get_text(TicketCenterPageLocator.subtotal_money).replace(',','')), '注額小計錯誤'
        assert round(thispage_payout, 2) == float(self.get_text(TicketCenterPageLocator.subtotal_payout).replace(',','')), '派彩小計錯誤'
        assert round(thispage_rebate, 2) == float(self.get_text(TicketCenterPageLocator.subtotal_rebate).replace(',','')), '返水小計錯誤'
        assert round(thispage_income, 2) == float(self.get_text(TicketCenterPageLocator.subtotal_income).replace(',','')), '損益小計錯誤'
        assert round(thispage_point, 2) == float(self.get_text(TicketCenterPageLocator.subtotal_point).replace(',','')), '打碼小計錯誤'

        # 比較小計與總計不同
        assert round(thispage_money, 2) != float((self.get_text(TicketCenterPageLocator.total_money)).replace(',','')), '注額 總計與小計比較錯誤'
        assert round(thispage_payout, 2) != float((self.get_text(TicketCenterPageLocator.total_payout))[4:].replace(',','')), '派彩 總計與小計比較錯誤'
        assert round(thispage_rebate, 2) != float((self.get_text(TicketCenterPageLocator.total_rebate))[4:].replace(',','')), '返水 總計與小計比較錯誤'
        assert round(thispage_income, 2) != float((self.get_text(TicketCenterPageLocator.total_income)).replace(',','')), '損益 總計與小計比較錯誤'
        assert round(thispage_point, 2) != float((self.get_text(TicketCenterPageLocator.total_point)).replace(',','')), '打碼 總計與小計比較錯誤'
    
    # 自動刷新檢查
    def autorefresh_check(self):
        self.refresh_browser()
        self.wait_loading_finish()

        self.click(TicketCenterPageLocator.btn_bet_thismonth) # 下注時間
        self.type(TicketCenterPageLocator.auto_refresh, '3') # 輸入刷新秒數
        self.click(TicketCenterPageLocator.auto_refresh_check) # 勾選自東刷新
        self.sleep(7)
        self.click(TicketCenterPageLocator.auto_refresh_check) # 取消自東刷新

        assert self.is_element_finded(TicketCenterPageLocator.order_time), '自東刷新查無資料'

    # 匯出後資料比對
    def check_export(self, memberaccount):

        self.refresh_browser()
        self.wait_loading_finish()
        self.type(TicketCenterPageLocator.member_account_input_box, memberaccount) # 輸入查詢之會員帳號
        self.click(TicketCenterPageLocator.btn_bet_yesterday)                # 下注時間
        self.click(TicketCenterPageLocator.btn_search)                   # 搜尋
        self.wait_loading_finish()

        self.click(TicketCenterPageLocator.btn_export)
        self.click(TicketCenterPageLocator.btn_export_confirm)
        self.wait_loading_finish()
        
        time = self.find_elements(TicketCenterPageLocator.order_time) # 下注時間
        member = self.find_elements(TicketCenterPageLocator.member_account) # 會員
        typeofgame = self.find_elements(TicketCenterPageLocator.type_of_game) # 遊戲類別
        ticketnubmer = self.find_elements(TicketCenterPageLocator.ticket_number) # 單號
        period = self.find_elements(TicketCenterPageLocator.period) # 期數
        detail = self.find_elements(TicketCenterPageLocator.order_detail) # 注單詳情
        detail_money = self.find_elements(TicketCenterPageLocator.order_detail_money) # 注單詳情-金額
        lotteryresult = self.find_elements(TicketCenterPageLocator.lottery_result) # 開獎結果
        money = self.find_elements(TicketCenterPageLocator.order_money) # 注額
        payout = self.find_elements(TicketCenterPageLocator.payout_money_amount) # 派彩
        rebate = self.find_elements(TicketCenterPageLocator.payout_money_rebate) # 返水
        income = self.find_elements(TicketCenterPageLocator.payout_income) # 損益
        point = self.find_elements(TicketCenterPageLocator.payout_point) # 打碼
        bonus = self.find_elements(TicketCenterPageLocator.bonus) # 獎金
        settlement = self.find_elements(TicketCenterPageLocator.payout_settlement) # 結算
        payouttime = self.find_elements(TicketCenterPageLocator.payout_time) # 派彩時間
        # df_read("C://Users//tim_lee//Downloads//order.xlsx")
        time_list = []
        member_list = []
        typeofgame_list = []
        ticketnubmer_list = []
        period_list = []
        detail_list = []
        lotteryresult_list = []
        money_list = []
        payout_rebate_list = []
        income_list = []
        point_list = []
        bonus_list =[]
        settlement_list = []

        excel_dict = self.read_excel(index_range=len(self.find_elements(TicketCenterPageLocator.order_time)))
        
        # 獲得個欄位資料，放進list以便比較
        for idx in range(len(self.find_elements(TicketCenterPageLocator.order_time))):
            time_list.append(self.get_text_by_dom(time[idx]))
            member_list.append(self.get_text_by_dom(member[idx]))
            typeofgame_list.append(self.get_text_by_dom(typeofgame[idx]))
            ticketnubmer_list.append(self.get_text_by_dom(ticketnubmer[idx]))
            period_list.append(int(self.get_text_by_dom(period[idx])))
            detail_list.append(self.get_text_by_dom(detail[idx]) + self.get_text_by_dom(detail_money[idx]))
            lotteryresult_list.append(self.get_text_by_dom(lotteryresult[idx]))
            money_list.append(self.get_text_by_dom(money[idx]))
            payout_rebate_list.append(self.get_text_by_dom(payout[idx]) + self.get_text_by_dom(rebate[idx]))
            income_list.append(self.get_text_by_dom(income[idx]))
            point_list.append(self.get_text_by_dom(point[idx]))
            bonus_list.append(self.get_text_by_dom(bonus[idx]))
            settlement_list.append(self.get_text_by_dom(settlement[idx]) + "：" +self.get_text_by_dom(payouttime[idx]))

        assert excel_dict['下注时间(美東)'] == time_list, '時間比對錯誤'
        assert excel_dict['会员'] == member_list, '會員比對錯誤'
        assert excel_dict['游戏类别'] == typeofgame_list, '遊戲類別比對錯誤'
        assert excel_dict['单号'] == ticketnubmer_list, '單號比對錯誤'
        assert excel_dict['期数（局号）'] == period_list, '期數比對錯誤'

        # 去掉'\n' ' '以便比較
        for idx in range(len(excel_dict['注单详情'])):
            assert excel_dict['注单详情'][idx].replace('\n', '').replace(' ', '') == detail_list[idx].replace(' ', ''), '注單詳情比對錯誤，錯誤之下注時間: {:}, 詳情: {:}'\
                .format(time_list[idx], detail_list[idx])
        assert excel_dict['开奖结果'] == lotteryresult_list, '開獎結果比對錯誤'
        assert excel_dict['注额'] == list(map(int, money_list)), '注額比對錯誤'
        # 去掉' , '以便比較
        for idx in range(len(excel_dict['派彩'])):
            assert excel_dict['派彩'][idx].replace(' , ','') == payout_rebate_list[idx], '派彩比對錯誤，錯誤之下注時間: {:}, 派彩內容: {:}'\
                .format(time_list[idx], payout_rebate_list[idx])
        # excel 裡的損益轉換為小數兩位
        compare_income = ['{:.2f}'.format(data) for data in excel_dict['损益']]
        assert compare_income == income_list, '損益比對錯誤'
        assert excel_dict['有效投注'] == list(map(int, point_list)), '有效投注比對錯誤'
        assert excel_dict['奖金'] == bonus_list, '獎金比對錯誤'
        assert excel_dict['结算'] == settlement_list, '結算比對錯誤'

        self.sleep(1)