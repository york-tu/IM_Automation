from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class PayoutStatisticsPageLocator:
    # ===============派彩統計頁面===============
    payout_statistics_page = (By.XPATH, "//div[contains(text(),'派彩统计')]")                                                 # 派彩統計頁面
    
    member_account_input_box = (By.XPATH, "//div[@id='pane-tab-template-payout']//input[@qa-input='member_login']")            # 會員帳號
    type_of_channel = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-select='channel_code']")                      # 頻道類型
    type_of_product = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-select='payout_product_type']")               # 產品類型
    select_item = (By.XPATH, "//span[@class='el-select__tags-text']")       # 下拉選單已選項目
    btn_payout_today = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-today']")               # 派彩-今日按鈕
    btn_payout_yesterday = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-yestoday']")        # 派彩-昨日按鈕
    btn_payout_thisweek = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-thisWeek']")         # 派彩-本周按鈕
    btn_payout_lastweek = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-lastWeek']")         # 派彩-上周按鈕
    btn_payout_thismonth = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-thisMonth']")       # 派彩-本月按鈕
    btn_payout_lastmonth = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//button[@qa-button='quick-time-lastMonth']")       # 派彩-上月按鈕
    btn_search_payoutpage = (By.XPATH, "//div[@id='pane-tab-template-payout']//button[@qa-button='submitForm']")                                                    # 派彩統計頁面-查找按鈕
    
    payout_time_start = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//div[@qa-input='quick-time-date']/input[1]")                  # 派彩起始時間
    payout_time_end = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@qa-date-picker='payout-time']//div[@qa-input='quick-time-date']/input[2]")                      # 派彩結束時間

    input_shareholder = (By.XPATH, "//div[@qa-select='share_login']//input[@class='el-input__inner']")                                                        # 股東輸入

    # ===============派彩列表===============
    payout_total = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[1]/div")                 # 單量
    payout_money_amount = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[2]")      # 注額
    payout_earning = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[3]//p[1]")          # 派彩
    payout_rebate = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[3]//p[2]")            # 返水
    payout_income = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[4]")            # 損益
    payout_valid_money_amount = (By.XPATH, "//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr/td[5]") # 有效投注額
    select_channel = (By.XPATH, "//div[@x-placement='bottom-start']//span[text()='极速彩种']")
    select_product = (By.XPATH, "//div[@x-placement='bottom-start']//span[contains(text(),'极速快3')]")
    payout_table = (By.XPATH,"//div[@id='pane-tab-template-payout']//div[@class='el-table__body-wrapper is-scrolling-none']//tr")

class PayoutStatisticsPage(BasePage):

    # 檢查以日或周為單位的交易時間 開始及結束時間
    def check_time_period_days_week(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(PayoutStatisticsPageLocator.payout_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(PayoutStatisticsPageLocator.payout_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == today - datetime.timedelta(days=time_delta_start), error_message_date + '時間錯誤 ... 開始時間錯誤 ... ' \
            + str(start_time) + ' 應為-> ' + str(today - datetime.timedelta(days=time_delta_start))
        assert end_time == today - datetime.timedelta(days=time_delta_end), error_message_date + '時間錯誤 ... 結束時間錯誤 ... ' \
            + str(end_time) + ' 應為-> ' + str(today - datetime.timedelta(days=time_delta_end))

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        return datetime.date(year, month, 1)

    # 檢查以月為單位的交易時間 開始及結束時間
    def check_time_period_month(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(PayoutStatisticsPageLocator.payout_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(PayoutStatisticsPageLocator.payout_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == self.add_months(sourcedate=today, months=time_delta_start),  \
            f'{error_message_date} 時間錯誤 ... 開始時間錯誤 ... {start_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_start)}'
        assert end_time == self.add_months(sourcedate=today, months=time_delta_end), \
            f'{error_message_date} 時間錯誤 ... 結束時間錯誤 ... {end_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_end)}'

    # 進入派彩統計
    def into_payout_statistic(self):
        self.click(PayoutStatisticsPageLocator.payout_statistics_page)

    def check_select_transaction_time(self):
        '''
            檢查交易時間
        '''
        self.wait_visibility(PayoutStatisticsPageLocator.btn_payout_today)
        today = self.get_us_time().date()
        week_day = today.weekday()

        self.click(PayoutStatisticsPageLocator.btn_payout_today)
        self.check_time_period_days_week(today=today, time_delta_start=0, time_delta_end=-1, error_message_date='今日')

        self.click(PayoutStatisticsPageLocator.btn_payout_yesterday)
        self.check_time_period_days_week(today=today, time_delta_start=1, time_delta_end=0, error_message_date='昨日')

        self.click(PayoutStatisticsPageLocator.btn_payout_thisweek)
        self.check_time_period_days_week(today=today, time_delta_start=week_day, time_delta_end=week_day-7, error_message_date='本週')

        self.click(PayoutStatisticsPageLocator.btn_payout_lastweek)
        self.check_time_period_days_week(today=today, time_delta_start=week_day+7, time_delta_end=week_day, error_message_date='上週')

        self.click(PayoutStatisticsPageLocator.btn_payout_thismonth)
        self.check_time_period_month(today=today, time_delta_start=0, time_delta_end=1, error_message_date='本月')

        self.click(PayoutStatisticsPageLocator.btn_payout_lastmonth)
        self.check_time_period_month(today=today, time_delta_start=-1, time_delta_end=0, error_message_date='上月')

    def check_total_record_by_shareholder(self, search_account, record):
        '''
            查找股東後，檢查派彩統計 總計資訊
        '''
        self.wait_visibility(PayoutStatisticsPageLocator.btn_search_payoutpage)
        self.type(PayoutStatisticsPageLocator.input_shareholder, search_account)
        dropdown_shareholder=(By.XPATH, "//div[@x-placement='bottom-start']//span[contains(text(),'"+ search_account+"')]")
        self.wait_visibility(dropdown_shareholder)
        self.click(dropdown_shareholder)
        self.click(PayoutStatisticsPageLocator.btn_payout_today)
        self.click(PayoutStatisticsPageLocator.btn_search_payoutpage)
        self.wait_loading_finish()
        self.sleep(1)
        total_name = ['单量', '注额', '派彩', '返水', '损益', '打码']

        self.wait_visibility(PayoutStatisticsPageLocator.payout_table)
        
        total = float(self.get_text(PayoutStatisticsPageLocator.payout_total).replace(',', ''))     # 單量
        money_amount = float((self.get_text(PayoutStatisticsPageLocator.payout_money_amount))[4:].replace(',', '')) # 注額
        earning = float((self.get_text(PayoutStatisticsPageLocator.payout_earning))[4:].replace(',', ''))   # 派彩
        rebate = float((self.get_text(PayoutStatisticsPageLocator.payout_rebate))[4:].replace(',', ''))     # 返水
        income = float((self.get_text(PayoutStatisticsPageLocator.payout_income))[4:].replace(',', ''))     # 損益
        valid_money_amount = float((self.get_text(PayoutStatisticsPageLocator.payout_valid_money_amount))[4:].replace(',', '')) # 打碼(有效投注額)

        payout_list = [total, money_amount, earning, rebate, income, valid_money_amount]
        for i in range(len(payout_list)):
            assert payout_list[i] == record[i], f'派彩總計錯誤 ... {total_name[i]}錯誤 ... {payout_list[i]} 應為-> {record[i]}'

    # 輸入產品名稱 回傳該產品的注單數量、總下注金額、派彩、輸贏及返水
    def sort_out_web_record_by_product(self, product_name, web_record_list):
        # 單量、金額、派彩、返水、損益、有效投注
        count = amount = payout = rebate = win_lose = effectbet = 0.0

        for web_record in web_record_list:
            if web_record['ticket_name'] == product_name and (web_record['status'] != '投注成功' or web_record['status'] != '待结算'):  # ttmj狀態會顯示 "待结算"、"已结算"
                count += 1
                amount += float(web_record['money'])
                payout += float(web_record['status']['payout']) # ttmj 前台抓到的資料格式不一樣
                rebate += float(web_record['status']['rebate'])
                # 前台贏的錢相當於後臺輸的錢，所以用減的
                win_lose -= float(web_record['status']['win_lose'])
                effectbet += float(web_record['effectBet'])

        return [round(count, 2), round(amount, 2), round(payout, 2), round(rebate, 2), round(win_lose, 2), round(effectbet, 2)]
        
    def check_total_record_by_member(self, search_account, web_record:list):
        '''
            查找會員帳號及產品後，檢查總計資訊
        '''
        self.wait_loading_finish()
        product_name = '极速快3'
        # 前台的時間為台灣時間，後台查找時間採前一天的 12:00 到今天的 12:00
        time_end = datetime.date.today()
        time_start = time_end - datetime.timedelta(days=1)
        self.type(PayoutStatisticsPageLocator.payout_time_start, time_start.strftime('%Y-%m-%d 12:00'))
        self.type(PayoutStatisticsPageLocator.payout_time_end, time_end.strftime('%Y-%m-%d 12:00'))

        self.type(PayoutStatisticsPageLocator.member_account_input_box, search_account)
        self.click(PayoutStatisticsPageLocator.type_of_channel) # 點擊 產品類型        
        self.wait_visibility(PayoutStatisticsPageLocator.select_channel)       
        self.click(PayoutStatisticsPageLocator.select_channel) # 選擇 產品
        self.wait_loading_finish()
        self.wait_visibility(PayoutStatisticsPageLocator.select_item)
        self.click(PayoutStatisticsPageLocator.type_of_product) # 點擊 產品類型
        self.wait_visibility(PayoutStatisticsPageLocator.select_product)
        self.click(PayoutStatisticsPageLocator.select_product) # 選擇 產品
        self.wait_loading_finish()
        self.click(PayoutStatisticsPageLocator.btn_search_payoutpage)
        self.wait_loading_finish()
        self.sleep(1)
        total_name = ['单量', '注额', '派彩', '返水', '损益', '打码']

        total = float(self.get_text(PayoutStatisticsPageLocator.payout_total).replace(',', '')) # 單量
        money_amount = float((self.get_text(PayoutStatisticsPageLocator.payout_money_amount))[4:].replace(',', '')) # 注額
        earning = float((self.get_text(PayoutStatisticsPageLocator.payout_earning))[4:].replace(',', '')) # 派彩
        rebate = float((self.get_text(PayoutStatisticsPageLocator.payout_rebate))[4:].replace(',', '')) # 返水
        income = float((self.get_text(PayoutStatisticsPageLocator.payout_income))[4:].replace(',', '')) # 損益
        valid_money_amount = float((self.get_text(PayoutStatisticsPageLocator.payout_valid_money_amount))[4:].replace(',', '')) # 打碼

        payout_list = [total, money_amount, earning, rebate, income, valid_money_amount]
        record = self.sort_out_web_record_by_product(product_name, web_record)

        return total_name, payout_list, record
        
        # for i in range(len(payout_list)):
        #     try:
        #         assert payout_list[i] == record[i], f'派彩總計錯誤 ... {total_name[i]} 錯誤 ... {payout_list[i]} 應為-> {record[i]}'
        #     except AssertionError as e:
        #         mark += 1
        #         if mark > 1:
                        
    def compare_data(self, total_name:list, payout_list:list, record:list, mark):
        while mark < 2:
            try:
                for index in range(len(payout_list)):
                    assert payout_list[index] == record[index], f'派彩總計錯誤 ... {total_name[index]} 錯誤 ... {payout_list[index]} 應為-> {record[index]}'
                break
            except AssertionError as e:
                if mark >= 2:
                    raise e
                mark += 1
                return mark

                    