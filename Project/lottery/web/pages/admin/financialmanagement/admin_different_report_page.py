from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class DifferentReportPageLocator(object):
    # 查找條件
    input_start_time = (By.XPATH, "//input[contains(@data-bind,'starttime')]") # 查找申請開始時間  
    input_end_time = (By.XPATH, "//input[contains(@data-bind,'endtime')]") # 查找申請結束時間 
    button_today = (By.XPATH, '//button[contains(text(), "今日")]')        # 今日按鈕
    button_yesterday = (By.XPATH, '//button[contains(text(), "昨日")]')    # 昨日按鈕
    button_this_week = (By.XPATH, '//button[contains(text(), "本周")]')    # 本周按鈕
    button_last_week = (By.XPATH, '//button[contains(text(), "上周")]')    # 上周按鈕
    button_this_month = (By.XPATH, '//button[contains(text(), "本月")]')   # 本月按鈕
    button_last_month = (By.XPATH, '//button[contains(text(), "上月")]')   # 上月按鈕
    button_search = (By.XPATH, '//button[contains(text(), "查找")]')       # 查找按鈕

    # 公司入款列
    company_apply = (By.XPATH, '//td[@data-bind = "money: deposit.amountbyaddedtime"]')
    company_accept = (By.XPATH, '//td[@data-bind = "money: deposit.amountbyaccepttime"]')
    company_diff = (By.XPATH, '//span[@data-bind = "money: deposit.amountdiff"]')
    company_diff_count = (By.XPATH, '//span[@data-bind = "text: deposit.countdiff"]')
    company_btn = (By.XPATH, '//a[@data-bind = "money: deposit.amountbyaccepttime"]/..//a[contains(@data-bind, "deposit")]')
    
    # 在線入款列
    online_apply = (By.XPATH, '//td[@data-bind = "money: webdeposit.amountbyaddedtime"]')
    online_accept = (By.XPATH, '//td[@data-bind = "money: webdeposit.amountbyaccepttime"]')
    online_diff = (By.XPATH, '//span[@data-bind = "money: webdeposit.amountdiff"]')
    online_diff_count = (By.XPATH, '//span[@data-bind = "text: webdeposit.countdiff"]')
    online_btn = (By.XPATH, '//a[contains(@data-bind, "webdeposit")]')

    # 出款申請列
    out_apply = (By.XPATH, '//td[@data-bind = "money: withdraw.amountbyaddedtime"]')
    out_accept = (By.XPATH, '//td[@data-bind = "money: withdraw.amountbyaccepttime"]')
    out_diff = (By.XPATH, '//span[@data-bind = "money: withdraw.amountdiff"]')
    out_diff_count = (By.XPATH, '//span[@data-bind = "text: withdraw.countdiff"]')
    out_btn = (By.XPATH, '//a[contains(@data-bind, "withdraw")]')

    back_btn = (By.XPATH, "//i[@class='fa fa-reply btn btn-primary']")
    notice_info = (By.XPATH, '//div[contains(@class, "toast-message")]')
    


class DifferentReportPage(BasePage):

    def search_for_time(self, time):
        if time == 1:
            self.click(DifferentReportPageLocator.button_today)
        elif time == 2:
            self.click(DifferentReportPageLocator.button_yesterday)
        elif time == 3:
            self.click(DifferentReportPageLocator.button_this_week)
        elif time == 4:
            self.click(DifferentReportPageLocator.button_last_week)
        elif time == 5:
            self.click(DifferentReportPageLocator.button_this_month)
        else:
            self.click(DifferentReportPageLocator.button_last_month)
        
        self.click(DifferentReportPageLocator.button_search)

        self.wait_loading_finish()

        try:
            info = self.get_text_by_dom(self.find_element(DifferentReportPageLocator.notice_info))
        except:
            info = ""
        if str(info).__contains__("报表数据同步中!"):
            self.test_skip("报表数据同步中!")

        assert self.is_element_finded(DifferentReportPageLocator.company_accept), "查找功能錯誤或查無資料"
    

    def check_data(self):
        # 讀取資料
        company_apply = self.get_text(DifferentReportPageLocator.company_apply).replace(',', '')
        company_accept = self.get_text(DifferentReportPageLocator.company_accept).replace(',', '')
        company_diff = self.get_text(DifferentReportPageLocator.company_diff).replace(',', '')
        company_diff_count = self.get_text(DifferentReportPageLocator.company_diff_count)
        assert abs(float(company_apply) - float(company_accept)) == abs(float(company_diff)), "公司入款的差异金额有誤"

        online_apply = self.get_text(DifferentReportPageLocator.online_apply).replace(',', '')
        online_accept = self.get_text(DifferentReportPageLocator.online_accept).replace(',', '')
        online_diff = self.get_text(DifferentReportPageLocator.online_diff).replace(',', '')
        online_diff_count = self.get_text(DifferentReportPageLocator.online_diff_count)
        assert abs(float(online_apply) - float(online_accept)) == abs(float(online_diff)), "在线入款的差异金额有誤"
        
        out_apply = self.get_text(DifferentReportPageLocator.out_apply).replace(',', '')
        out_accept = self.get_text(DifferentReportPageLocator.out_accept).replace(',', '')
        out_diff = self.get_text(DifferentReportPageLocator.out_diff).replace(',', '')
        out_diff_count = self.get_text(DifferentReportPageLocator.out_diff_count)
        assert abs(float(out_apply) - float(out_accept)) == abs(float(out_diff)), "出款申请的差异金额有誤"
        

        if float(company_diff) != 0:
            self.different_check(1, company_diff_count)
        if float(online_diff) != 0:
            self.different_check(2, online_diff_count)
        if float(out_diff) != 0:
            self.different_check(3, out_diff_count)
        
        return [company_apply, company_accept, online_apply, online_accept, out_apply, out_accept]

    def different_check(self, number, diff_count):

        text_list = ["公司入款", "在线入款", "出款申请"]
        button = (By.XPATH, "(//i[@class='fa fa-search-plus'])[{}]".format(number))
        record_count = (By.XPATH, "(//span[@data-bind = 'text: pager.total'])[{}]".format(number))
        self.click(button)
        self.sleep(1)
        assert int(self.get_text(record_count)) == int(diff_count), "差額報表中{}的差異資料錯誤".format(text_list[number])
        self.click(DifferentReportPageLocator.back_btn)