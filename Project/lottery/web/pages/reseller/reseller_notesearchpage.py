from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

import datetime

class NoteSearchPageLocator:

    order_number_input_box = (By.XPATH, "//input[@qa-input='number']")                 #訂單號碼
    member_account_input_box = (By.XPATH, "//input[@qa-input='member_login']")          #會員帳號
    product_number_input_box = (By.XPATH, "//input[@qa-input='product_number']")        #期數場次

    search_button = (By.XPATH, "//button[@qa-button='query']")

    bet_time_today = (By.XPATH, "//div[@qa-date-picker='added-time']//span[contains(text(), '今日')]") #下注時間 - 今日

    type_of_channel = (By.XPATH, "(//div[@class='el-select el-select--mini']//input[@class='el-input__inner'])[2]")
    type_of_product = (By.XPATH, "(//div[@class='el-select el-select--mini']//input[@class='el-input__inner'])[4]")
    type_of_play = (By.XPATH, "(//div[@class='el-select el-select--mini']//input[@class='el-input__inner'])[5]")

    # ===============注單詳情===============
    order_detail = (By.XPATH, "//td[7]//li[1]")                        # 注單詳情 彩種
    order_detail_money = (By.XPATH, "//td[7]//li[2]")                  # 注單詳情 金額
    order_money = (By.XPATH, "//td[9]//span")                              # 注額
    prize_money = (By.XPATH, "//td[10]//p[1]")                             # 派彩
    return_money = (By.XPATH, "//td[10]//p[2]")                            # 返水
    profit_and_loss = (By.XPATH, "//td[11]//span")                         # 損益
    type_of_game = (By.XPATH, "//td[4]//span[1]")                          # 遊戲類別
    period = (By.XPATH, "//td[6]//div")                                    # 期數
    order_time = (By.XPATH, "//td[1]//div[1]")                             # 下注時間
    member_account = (By.XPATH, "//td[2]//a")                              # 會員帳號
    ticket_number = (By.XPATH, "//td[5]//div[1]")                          # 單號
    settlement_time = (By.XPATH, "//td[13]//p[2]")                         # 派彩時間
 
class NoteSearchPage(BasePage):

    def order_number_search(self, order_number):
        self.type(NoteSearchPageLocator.order_number_input_box, order_number)
        self.sleep(1)
        self.click(NoteSearchPageLocator.bet_time_today)                                              #下注時間選擇今日
        self.sleep(1)
        self.click(NoteSearchPageLocator.search_button)                                               #按下查找
        self.sleep(0.4)

    def member_account_search(self, member_account):
        self.type(NoteSearchPageLocator.member_account_input_box, member_account)
        self.sleep(1)
        self.click(NoteSearchPageLocator.bet_time_today) 
        self.sleep(1)      
        self.click(NoteSearchPageLocator.search_button)
        self.sleep(0.4)
    
    def period_search(self, product_number):
        self.type(NoteSearchPageLocator.product_number_input_box, product_number)
        self.sleep(1)
        self.click(NoteSearchPageLocator.bet_time_today)
        self.sleep(1)
        self.click(NoteSearchPageLocator.search_button)
        self.sleep(0.4)

    def dropdown_list_locate(self, type_name):
        dropdown_list_locate = (By.XPATH, f"//div[contains(@class, 'el-select-dropdown el-popper')]//li/span[contains(text(), '{type_name}')]")
        return dropdown_list_locate

    def choice_channel_product_play(self):
        self.wait_loading_finish()
        # 選擇頻道類型
        dropdown_list_locate = self.dropdown_list_locate("极速彩种")
        self.type(NoteSearchPageLocator.type_of_channel, "极速彩种")
        self.wait_visibility(dropdown_list_locate)
        self.click(dropdown_list_locate)                                                        
        self.sleep(0.5)

        # 選擇產品類型
        dropdown_list_locate = self.dropdown_list_locate("极速快3")
        self.type(NoteSearchPageLocator.type_of_product, "极速快3")
        self.wait_visibility(dropdown_list_locate)
        self.click(dropdown_list_locate)                                                      
        self.sleep(0.5)

        # 選擇玩法
        dropdown_list_locate = self.dropdown_list_locate("两面")
        self.click(NoteSearchPageLocator.type_of_play) 
        self.wait_visibility(dropdown_list_locate)
        self.click(dropdown_list_locate)

    # 爬取注單結果
    def search_record(self, record, is_structure_switchin, web_account):
        self.wait_loading_finish()
        
        if is_structure_switchin:
            if self.is_element_finded(NoteSearchPageLocator.member_account):
                record_account = self.get_text(NoteSearchPageLocator.member_account)
                if record_account == str(web_account):
                    record_order_time = self.get_text(NoteSearchPageLocator.order_time)
                    
                    type_of_game = self.get_text(NoteSearchPageLocator.type_of_game)
                    ticket_number = self.get_text(NoteSearchPageLocator.ticket_number)
                    period = self.get_text(NoteSearchPageLocator.period)
                    order_detail = self.get_text(NoteSearchPageLocator.order_detail)
                    order_detail = self.get_text(NoteSearchPageLocator.order_detail_money) + order_detail
                    order_money = self.get_text(NoteSearchPageLocator.order_money)
                    prize_money = self.get_text(NoteSearchPageLocator.prize_money)
                    return_money = self.get_text(NoteSearchPageLocator.return_money)
                    profit_loss = self.get_text(NoteSearchPageLocator.profit_and_loss)
                    settlement_time = self.get_text(NoteSearchPageLocator.settlement_time)

                    assert order_detail==record['type'], '注單詳情不正確'
                    assert ticket_number==record['ticket_name'], '單號不正確'
                    assert type_of_game=='极速快3', '彩種不正確'
                    assert period==record['period'], '期數不正確'
                    assert order_money==record['money'], '注額不正確'
                    
                    record_order_time = datetime.datetime.strptime(record_order_time, '%Y-%m-%d %H:%M:%S')
                    record_order_time = str(record_order_time + datetime.timedelta(hours=12))
                    assert record_order_time[:-9] == record['time'], '下注時間不正確'

                    # search_records = {"oreder_time": record_order_time, "record_account": record_account, "type of game": type_of_game,
                    #                  "ticket number": ticket_number, "period": period, "ordet detail": order_detail,
                    #                  "order money": order_money, "prize money": prize_money, "return money": return_money,
                    #                  "profit and loss": profit_loss, "settlement time": settlement_time}
                else:
                    assert False, '在代理內卻無找到該會員帳號注單'
            else:
                assert False, '在代理內卻無找到該會員帳號注單'
        else:
            if self.is_element_finded(NoteSearchPageLocator.member_account):
                record_account = self.get_text(NoteSearchPageLocator.member_account)
                if record_account == str(web_account):
                    assert False, '在代理外卻查到該會員帳號注單'      
    
    def check_pages(self):
        self.check_page()