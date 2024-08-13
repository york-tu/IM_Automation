from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class ChannelReportPageLocator:
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
    total_order_count = (By.XPATH, "(//td[@class='el-table_1_column_2  '])[last()]")    # 單量
    total_bet_count = (By.XPATH, "(//td[@class='el-table_1_column_3  '])[last()]")      # 投注金額
    total_earn_count = (By.XPATH, "(//td[@class='el-table_1_column_4  '])[last()]")      # 損益
    total_valid_count = (By.XPATH, "(//td[@class='el-table_1_column_5  '])[last()]")      # 有效投注

class ChannelReportPage(BasePage):
    # 查找時間
    def search_for_time(self, time):
        if time == 1:
            self.click(ChannelReportPageLocator.button_today)
        elif time == 2:
            self.click(ChannelReportPageLocator.button_yesterday)
        elif time == 3:
            self.click(ChannelReportPageLocator.button_this_week)
        elif time == 4:
            self.click(ChannelReportPageLocator.button_last_week)
        elif time == 5:
            self.click(ChannelReportPageLocator.button_this_month)
        else:
            self.click(ChannelReportPageLocator.button_last_month)
        
        self.click(ChannelReportPageLocator.button_search)

        self.wait_loading_finish()

        assert self.is_element_finded(ChannelReportPageLocator.total_order_count), "查找功能錯誤或查無資料"

    # 查找代理
    def search_for_agent(self, account):
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelReportPageLocator.button_expand) == False, "查找條件預設不應收合"
        self.type(ChannelReportPageLocator.textarea_agent, account)
        self.click(ChannelReportPageLocator.button_search)
        self.wait_loading_finish()

    # 取總計資料
    def get_total_data(self):
        total_dict = {}
        if self.is_element_displayed(ChannelReportPageLocator.total_order_count) is False:
            total_list = ['0', '0.00', '0.00', '0.00']
        else:
            total_order_count = self.find_element(ChannelReportPageLocator.total_order_count).text.split(' / ')[1]
            total_bet_count = self.find_element(ChannelReportPageLocator.total_bet_count).text.split(' / ')[1]
            total_earn_count = self.find_element(ChannelReportPageLocator.total_earn_count).text.split(' / ')[1]
            total_valid_count = self.find_element(ChannelReportPageLocator.total_valid_count).text.split(' / ')[1]
        
            total_list = [total_order_count, total_bet_count, total_earn_count, total_valid_count]
        total_dict = {'order_count': total_list[0], 'bet_amount': total_list[1], 'earn_amount': total_list[2], 'valid_amount': total_list[3]}
        
        return total_dict
