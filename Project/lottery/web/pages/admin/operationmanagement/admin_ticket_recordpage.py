from time import sleep
from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
from retrying import retry

class RecordPageLocator:
    # SEARCH AREA (查找條件區)
    ticketnum = (By.XPATH, "(//label[text()='订单号码']/..//input[@qa-input='number'])[1]")
    btn_today_application_datetime = (By.XPATH, "//div[@qa-date-picker='added-time']/..//button[@qa-button='quick-time-today']")
    btn_hiding = (By.XPATH, '(//button[contains(@class,"container__collapseBtn")])[1]')
    check_hiding = (By.XPATH, '//div[contains(@class,"container__optional") and @style="display: none;"]')
    btn_search = (By.XPATH, "//button[@qa-button='query']/span[text()='查询']")

    # RESULT AREA (搜尋結果區)
    ticketnum_result = (By.XPATH, "(//td[contains(@class,'_column_14')])[1]")
    periods = (By.XPATH, "(//td[contains(@class,'_column_15')])[1]")
    ticketinfo = (By.XPATH, "(//td[contains(@class,'_column_16')]//li[@class='result-list__item'])[1]")
    ticketstake = (By.XPATH, "(//td[contains(@class,'_column_16')]//li[@class='result-list__item'])[2]")
    ticketmoney = (By.XPATH, "(//td[contains(@class,'_column_18')])[1]")
    time = (By.XPATH, "(//td[contains(@class,'_column_10')])[1]")

    # AA stock RESULT AREA (搜尋結果區)
    ticketnum_result_aa = (By.XPATH, "(//td[contains(@class,'_column_15')])[1]")
    periods_aa = (By.XPATH, "(//td[contains(@class,'_column_16')])[1]")
    ticketinfo_aa = (By.XPATH, "(//td[contains(@class,'_column_17')]//li[@class='result-list__item'])[1]")
    ticketmoney_aa = (By.XPATH, "(//td[contains(@class,'_column_19')])[1]")

    # 總數
    total_num = (By.XPATH, "//tr[contains(@class,'el-table__row')]")

class CheckRecord(BasePage):

    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def check_result(self, records):
        self.wait_loading_finish()
        
        for record in records:
            self.click(RecordPageLocator.ticketnum)
            self.type(RecordPageLocator.ticketnum, record['ticket_name'])
            self.sleep(1.5)
            if self.is_element_finded(RecordPageLocator.check_hiding) is True:
                self.click(RecordPageLocator.btn_hiding)
                self.sleep(1)
            else:
                pass
            self.click(RecordPageLocator.btn_today_application_datetime)
            self.click(RecordPageLocator.btn_search)
            self.wait_loading_finish()

            assert len(self.find_elements(RecordPageLocator.total_num)) != '0', '查無此注單詳情,請確認後端Server狀態'

            ticket_number = self.get_text(RecordPageLocator.ticketnum_result)
            period = self.get_text(RecordPageLocator.periods)
            ticket_money = self.get_text(RecordPageLocator.ticketmoney)
            order_detail = self.get_text(RecordPageLocator.ticketinfo).replace(' \n', '').replace('\n', '')
            detail = self.get_text(RecordPageLocator.ticketstake) + order_detail

            assert record['ticket_name'] == ticket_number, f'單號錯誤 ... {ticket_number} 應為-> {record["ticket_name"]}'
            assert record['period'] == period, f'期數錯誤 ... {period} 應為-> {record["period"]}'
            assert record['type'] == detail, f'注單詳情錯誤 ... {detail} 應為-> {record["type"]}'
            assert record['money'].__contains__(ticket_money), f'投注金額錯誤 ... {ticket_money} 應為-> {record["money"]}'

    def check_red_envelope_record(self, records):
        self.wait_loading_finish()
        
        for record in records:
            self.type(RecordPageLocator.ticketnum, record['ticket_number'])
            self.sleep(1.5)
            if self.is_element_finded(RecordPageLocator.check_hiding) is True:
                self.click(RecordPageLocator.btn_hiding)
                self.sleep(1)
            else:
                pass
            self.click(RecordPageLocator.btn_today_application_datetime)
            self.click(RecordPageLocator.btn_search)
            self.wait_loading_finish()

            assert self.get_text(RecordPageLocator.total_num) != '0', f'查無此注單詳情, 請確認後端Server狀態'

            ticket_number = self.get_text(RecordPageLocator.ticketnum_result)
            period = self.get_text(RecordPageLocator.periods)
            ticket_money = self.get_text(RecordPageLocator.ticketmoney)
            detail = self.get_text(RecordPageLocator.ticketinfo).replace(' \n', '').replace('\n', '')

            assert record['ticket_number'] == ticket_number, f'單號錯誤 ... {ticket_number} 應為-> {record["ticket_number"]}'
            assert record['period'] == period, f'期數錯誤 ... {period} 應為-> {record["period"]}'
            assert record['detail'] == detail, f'注單詳情錯誤 ... {detail} 應為-> {record["detail"]}'
            assert record['amount'].__contains__(ticket_money), f'投注金額錯誤 ... {ticket_money} 應為-> {record["amount"]}'

    def check_stock_recode(self, records):
        self.wait_loading_finish()
        
        for record in records:
            self.type(RecordPageLocator.ticketnum, record['ticket_name'])
            self.sleep(1.5)
            if self.is_element_finded(RecordPageLocator.check_hiding) is True:
                self.click(RecordPageLocator.btn_hiding)
                self.sleep(1)
            else:
                pass
            self.click(RecordPageLocator.btn_today_application_datetime)
            self.click(RecordPageLocator.btn_search)
            self.wait_loading_finish()

            assert self.get_text(RecordPageLocator.total_num) != '0', '查無此注單詳情,請確認後端Server狀態'

            ticket_number = self.get_text(RecordPageLocator.ticketnum_result_aa)
            period = self.get_text(RecordPageLocator.periods_aa)
            ticket_money = self.get_text(RecordPageLocator.ticketmoney_aa)
            detail = self.get_text(RecordPageLocator.ticketinfo_aa).replace(' \n', '').replace('\n', '')

            assert record['ticket_name'] == ticket_number, f'單號錯誤 ... {ticket_number} 應為-> {record["ticket_name"]}'
            assert record['period'] == period, f'期數錯誤 ... {period} 應為-> {record["period"]}'
            assert record['type'].__contains__(detail), f'注單詳情錯誤 ... {detail} 應為-> {record["type"]}'
            assert record['money'].__contains__(ticket_money), f'投注金額錯誤 ... {ticket_money} 應為-> {record["money"]}'