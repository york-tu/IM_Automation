from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class OrderCenterPageLocator:
    # SEARCH AREA (查找條件區)
    btn_yesterday_application_datetime = (By.XPATH, "//p[text()='查找时间']/../following::button[contains(text(),'昨日')]")
    btn_search = (By.XPATH, "//button[contains(text(),'查找')]")

    all_channel_name = (By.XPATH, "//*[@data-bind='text: channelname']")
    total_order_count = (By.XPATH, "//tr[3]/th[2]")
    total_bet_amount = (By.XPATH, "//tr[3]/th[3]")
    total_earn_amount = (By.XPATH, "//tr[3]/th[4]")
    total_valid_bet_amount = (By.XPATH, "//tr[3]/th[5]")

    channel_id = (By.XPATH, "//*[@data-bind='text: channelname' and text() ='总计']/../..//tbody//td[1]")
    order_count = (By.XPATH, "//*[@data-bind='text: channelname' and text() ='总计']/../..//tbody//td[4]")
    bet_amount = (By.XPATH, "//*[@data-bind='text: channelname' and text() ='总计']/../..//tbody//td[5]")
    earn_amount = (By.XPATH, "//*[@data-bind='text: channelname' and text() ='总计']/../..//tbody//td[6]")
    valid_bet_amount = (By.XPATH, "//*[@data-bind='text: channelname' and text() ='总计']/../..//tbody//td[7]")


class OrderCenterPage(BasePage):
    def do_search_yesterday(self):
        self.wait_loading_finish()
        self.click(OrderCenterPageLocator.btn_yesterday_application_datetime)
        self.click(OrderCenterPageLocator.btn_search)
        self.wait_loading_finish()

    def get_total_data(self):
        total_dict = {}
        channel_name = []
        order_count = []
        bet_amount = []
        earn_amount = []
        valid_amount = []
        for ele in self.find_elements(OrderCenterPageLocator.all_channel_name):
            channel_name.append(ele.text)
        for ele in self.find_elements(OrderCenterPageLocator.total_order_count):
            order_count.append(ele.text)
        for ele in self.find_elements(OrderCenterPageLocator.total_bet_amount):
            bet_amount.append(ele.text)
        for ele in self.find_elements(OrderCenterPageLocator.total_earn_amount):
            earn_amount.append(ele.text)
        for ele in self.find_elements(OrderCenterPageLocator.total_valid_bet_amount):
            valid_amount.append(ele.text)

        for num in range(0, len(channel_name)):
            total_dict[channel_name[num]] = {'order_count': order_count[num], 'bet_amount': bet_amount[num],
                                             'earn_amount': earn_amount[num], 'valid_amount': valid_amount[num]}
        print(total_dict)
        return total_dict
