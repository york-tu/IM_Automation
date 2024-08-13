from time import sleep

from selenium.webdriver.common.by import By
import datetime
from Project.chat.web.pages.admin.admin_basepage import BasePage


class WaterRecodePageLocator:
    # 通用
    page_title = (By.XPATH, '//div[@class="page-title"]')
    search_btn = (By.XPATH, "//span[text()=' 搜寻 ']")

    # 搜尋欄位
    member_ID = (By.XPATH, '//label[text()="会员ID"]/..//input[@placeholder="请输入"]')
    member_name = (By.XPATH, '//label[text()="会员昵称"]/..//input[@placeholder="请输入"]')

    search_start_time = (By.XPATH, '//input[@placeholder="开始日期"]')
    search_end_time = (By.XPATH, '//input[@placeholder="结束日期"]')

    use_type = (By.XPATH, '//label[text()="使用媒介"]/..//span[@class="el-input__suffix-inner"]')

    exchange_success = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="顺付出金"]')
    exchange_fail = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="顺付返还"]')

    # 資料欄位
    data_member_ID = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    data_member_name = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    data_use_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    data_point = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")
    data_use_type = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")
    data_red_envelope_source = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")
    data_remain_point = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")
    data_state = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[8]")

    data_total_line = (By.XPATH, "//span[@class='el-pagination__total']")


class WaterRecodePage(BasePage):
    def search_point_recode(self, condition):
        self.wait_loading_finish()
        assert self.get_text(WaterRecodePageLocator.page_title) == '积分使用纪录', f'頁面標題有誤'
        self.type(WaterRecodePageLocator.member_name, '積分測試')
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.click(WaterRecodePageLocator.search_start_time)
        self.type(WaterRecodePageLocator.search_start_time, time)
        self.click(WaterRecodePageLocator.search_end_time)
        self.type(WaterRecodePageLocator.search_end_time, time)
        self.click(WaterRecodePageLocator.use_type)
        sleep(0.5)
        if condition == 'success':
            self.click(WaterRecodePageLocator.exchange_success)
        elif condition == 'fail':
            self.click(WaterRecodePageLocator.exchange_fail)
        self.click(WaterRecodePageLocator.search_btn)

    def check_exchange_recode(self, condition):
        self.wait_loading_finish()
        assert self.get_text(WaterRecodePageLocator.data_member_name) == '積分測試', f'暱稱有誤'
        if condition == 'success':
            assert self.get_text(WaterRecodePageLocator.data_use_type) == '顺付出金', f'媒介有誤'
            assert self.get_text(WaterRecodePageLocator.data_point) == '-1', '積分有誤'
            # assert self.get_text(WaterRecodePageLocator.data_total_line) == '共 2 条', f'總數有誤'
            assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'狀態有誤'
        elif condition == 'fail':
            assert self.get_text(WaterRecodePageLocator.data_use_type) == '顺付返还', f'媒介有誤'
            assert self.get_text(WaterRecodePageLocator.data_point) == '1', '積分有誤'
            # assert self.get_text(WaterRecodePageLocator.data_total_line) == '共 1 条', f'總數有誤'
            assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'狀態有誤'

    def check_current_exchange_record(self, grab_account, grab_time, grab_amount, grab_type, source_group,
                                      total_remain_amount):
        self.wait_loading_finish()
        aaa = self.get_text(WaterRecodePageLocator.data_member_ID)
        assert self.get_text(WaterRecodePageLocator.data_member_ID) == grab_account, f'積分使用紀錄: 會員ID錯誤'
        if grab_time is not None:
            assert self.get_text(WaterRecodePageLocator.data_use_time)[:-3] == grab_time, f'積分使用紀錄: 使用時間錯誤'
        assert self.get_text(WaterRecodePageLocator.data_point) == grab_amount, f'積分使用紀錄: 使用積分錯誤'
        assert self.get_text(WaterRecodePageLocator.data_use_type) == grab_type, f'積分使用紀錄: 使用媒介錯誤'
        if source_group is not None:
            assert self.get_text(WaterRecodePageLocator.data_red_envelope_source) == source_group, f'積分使用紀錄: 紅包來源錯誤'
        assert self.get_text(WaterRecodePageLocator.data_remain_point) == total_remain_amount, f'積分使用紀錄: 剩餘積分錯誤'
        assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'積分使用紀錄: 狀態錯誤'
