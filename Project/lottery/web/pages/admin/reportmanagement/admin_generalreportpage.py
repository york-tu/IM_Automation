from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class GeneralReportPageLocator:
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

    # 各頻道總計定位
    all_channel_name = (By.XPATH, "//div[@class='report-item__title']/span")
    total_order_count = (By.XPATH, "//tr[3]/th[2]")
    total_bet_amount = (By.XPATH, "//tr[3]/th[3]")
    total_earn_amount = (By.XPATH, "//tr[3]/th[4]")
    total_valid_bet_amount = (By.XPATH, "//tr[3]/th[5]")

class GeneralReportPage(BasePage):
    # 查找時間
    def search_for_time(self, time):
        if time == 1:
            self.click(GeneralReportPageLocator.button_today)
        elif time == 2:
            self.click(GeneralReportPageLocator.button_yesterday)
        elif time == 3:
            self.click(GeneralReportPageLocator.button_this_week)
        elif time == 4:
            self.click(GeneralReportPageLocator.button_last_week)
        elif time == 5:
            self.click(GeneralReportPageLocator.button_this_month)
        else:
            self.click(GeneralReportPageLocator.button_last_month)
        
        self.click(GeneralReportPageLocator.button_search)

        self.wait_loading_finish()

        assert self.is_element_finded(GeneralReportPageLocator.all_channel_name), "查找功能錯誤或查無資料"

    # 查找代理
    def search_for_agent(self, account):
        self.wait_loading_finish()
        assert self.is_element_finded(GeneralReportPageLocator.button_expand) == False, "查找條件預設不應收合"
        self.type(GeneralReportPageLocator.textarea_agent, account)
        self.click(GeneralReportPageLocator.button_search)
        self.wait_loading_finish()

    # 取總計資料
    def get_total_data(self):
        total_dict = {}
        channel_name = []
        order_count = []
        bet_amount = []
        earn_amount = []
        valid_amount = []
        if self.is_element_finded(GeneralReportPageLocator.all_channel_name) is False:
            channel_name.append('总计')
            order_count.append('0')
            bet_amount.append('0.00')
            earn_amount.append('0.00')
            valid_amount.append('0.00')
        else:
            for ele in self.find_elements(GeneralReportPageLocator.all_channel_name):
                channel_name.append(ele.text)
            for ele in self.find_elements(GeneralReportPageLocator.total_order_count):
                order_count.append(ele.text)
            for ele in self.find_elements(GeneralReportPageLocator.total_bet_amount):
                bet_amount.append(ele.text)
            for ele in self.find_elements(GeneralReportPageLocator.total_earn_amount):
                earn_amount.append(ele.text)
            for ele in self.find_elements(GeneralReportPageLocator.total_valid_bet_amount):
                valid_amount.append(ele.text)

        for num in range(0, len(channel_name)):
            total_dict[channel_name[num]] = {'order_count': order_count[num], 'bet_amount': bet_amount[num],
                                             'earn_amount': earn_amount[num], 'valid_amount': valid_amount[num]}
        # print(total_dict)
        return total_dict
