from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class DailyReportPageLocator:
    # SEARCH AREA (查找條件區)
    button_today = (By.XPATH, '//button/span[contains(text(), "今日")]')        # 今日按鈕
    button_yesterday = (By.XPATH, '//button/span[contains(text(), "昨日")]')    # 昨日按鈕
    button_this_week = (By.XPATH, '//button/span[contains(text(), "本周")]')    # 本周按鈕
    button_last_week = (By.XPATH, '//button/span[contains(text(), "上周")]')    # 上周按鈕
    button_this_month = (By.XPATH, '//button/span[contains(text(), "本月")]')   # 本月按鈕
    button_last_month = (By.XPATH, '//button/span[contains(text(), "上月")]')   # 上月按鈕
    button_search = (By.XPATH, '//button/span[contains(text(), "查找")]')       # 查找按鈕
    textarea_agent = (By.XPATH, '//input[@qa-input="agent"]')           # 代理輸入框
    button_expand = (By.XPATH, '//i[@class="el-icon-arrow-down"]')      # 查找區展開鈕

    # 總計定位
    all_total_amount = (By.XPATH, "//tr[contains(@class,'danger-row')]/td/div")


class DailyReportPage(BasePage):
    # 查找時間
    def search_for_time(self, time):
        if time == 1:
            self.click(DailyReportPageLocator.button_today)
        elif time == 2:
            self.click(DailyReportPageLocator.button_yesterday)
        elif time == 3:
            self.click(DailyReportPageLocator.button_this_week)
        elif time == 4:
            self.click(DailyReportPageLocator.button_last_week)
        elif time == 5:
            self.click(DailyReportPageLocator.button_this_month)
        else:
            self.click(DailyReportPageLocator.button_last_month)
        
        self.click(DailyReportPageLocator.button_search)

        self.wait_loading_finish()

        assert self.is_element_finded(DailyReportPageLocator.all_total_amount), "查找功能錯誤或查無資料"

    # 查找代理
    def search_for_agent(self, account):
        self.wait_loading_finish()
        assert self.is_element_finded(DailyReportPageLocator.button_expand) == False, "查找條件預設不應收合"
        self.type(DailyReportPageLocator.textarea_agent, account)
        self.click(DailyReportPageLocator.button_search)
        self.wait_loading_finish()

    # 取總計資料
    def get_total_data(self):
        self.sleep(1)
        all_total_amount = self.find_elements(DailyReportPageLocator.all_total_amount)

        total_list = [(amount.text).replace(',','') for amount in all_total_amount]
        total_dict_bet = {'order_count': total_list[13], 'bet_amount': total_list[14], 'earn_amount': total_list[16], 'valid_amount': total_list[15]}
        total_dict_fee = {'give_discount': total_list[8], 'withdrawal_amount': total_list[11], 'payment_deducted': total_list[12], 'give_back': total_list[17]}
        
        return total_dict_bet, total_dict_fee

    # 驗證資料
    def verify_data(self, financial_report, gereral_report, channel_report, daily_report_bet, daily_report_fee):
        assert round(float(financial_report[6]) + float(financial_report[8]),2) == round(float(daily_report_fee['give_discount']) + float(daily_report_fee['give_back']),2), \
            f"優惠+返水金額有誤，財務報表:{float(financial_report[6]) + float(financial_report[8])}，每日報表{float(daily_report_fee['give_discount']) + float(daily_report_fee['give_back'])}"

        withdrawal_amount = round(float(financial_report[5]) + float(financial_report[7]),2)
        assert float(withdrawal_amount) == float(daily_report_fee['withdrawal_amount']), f"取款額有誤，財務報表:{float(withdrawal_amount)}，每日報表{float(daily_report_fee['withdrawal_amount'])}"
        assert financial_report[4] == daily_report_fee['payment_deducted'], f"取款手續費有誤，財務報表:{financial_report[4]}，每日報表{daily_report_fee['payment_deducted']}"

        assert int(gereral_report['总计']['order_count']) == int(channel_report['order_count']) == int(float(daily_report_bet['order_count'])), \
            f"單量有誤，一般報表:{int(gereral_report['总计']['order_count'])}，頻道報表:{int(channel_report['order_count'])}，每日報表{int(float(daily_report_bet['order_count']))}"
        assert gereral_report['总计']['bet_amount'] == channel_report['bet_amount'] == daily_report_bet['bet_amount'], \
            f"投注額有誤，一般報表:{gereral_report['总计']['bet_amount']}，頻道報表:{channel_report['bet_amount']}，每日報表{daily_report_bet['bet_amount']}"
        assert gereral_report['总计']['earn_amount'] == channel_report['earn_amount'] == daily_report_bet['earn_amount'], \
            f"有效投注金額有誤，一般報表:{gereral_report['总计']['earn_amount']}，頻道報表:{channel_report['earn_amount']}，每日報表{daily_report_bet['earn_amount']}"
        assert gereral_report['总计']['valid_amount'] == channel_report['valid_amount'] == daily_report_bet['valid_amount'], \
            f"損益有誤，一般報表:{gereral_report['总计']['valid_amount']}，頻道報表:{channel_report['valid_amount']}，每日報表{daily_report_bet['valid_amount']}"