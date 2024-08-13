from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime



class ValidMemberPageLocator:
    member_account_input_box = (By.XPATH, "//input[@data-bind='value: filter.member']")
    search_button = (By.XPATH, "//button[@id='btnSearch']")
    today_button = (By.XPATH, "//button[contains(text(),'今日')]")
    start_time_input = (By.XPATH, "//input[@data-bind='datetime: filter.starttime']")  # 查找時間-開始
    end_time_input = (By.XPATH, "//input[@data-bind='datetime: filter.endtime']")      # 查找時間-結束

    #今日
    btn_Today = (By.XPATH,"//button[contains(text(),'今日')]") 

    #上週按鈕測試用
    last_week_button = (By.XPATH, "//button[contains(text(),'上周')]")
    yesterday_button = (By.XPATH, "//button[contains(text(),'昨日')]")
    
    type_of_membership_All = (By.XPATH, "//input[@value='-1']")
    type_of_membership_Official = (By.XPATH, "//input[@value='0']")
    type_of_membership_Try = (By.XPATH, "//input[@value='1']")
    
    # ===============會員詳情===============
    member_account = (By.XPATH, "//tbody//tr//td[1]")                                  # 會員帳號
    member_agent = (By.XPATH, "//tbody//tr//td[2]")                                    # 會員代理
    member_generalagent = (By.XPATH, "//tbody//tr//td[3]")                             # 會員總代
    member_shareholder = (By.XPATH, "//tbody//tr//td[4]")                              # 會員股東
    order_quantity = (By.XPATH, "//tbody//tr//td[5]")                                  # 單量
    order_amount = (By.XPATH, "//tbody//tr//td[6]")                                    # 投注額
    profit_and_loss = (By.XPATH, "//tbody//tr//td[7]")                                 # 損益
    effective_bet_amount = (By.XPATH, "//tbody//tr//td[8]")                            # 有效投注

    member_account_cnt = (By.XPATH, "//tbody//tr")                                     # 計數有幾組有效會員下注
    #總計
    total_order_quantity = (By.XPATH, "//thead//tr[3]//th[5]")                         # 總單量
    total_order_amount = (By.XPATH, "//thead//tr[3]//th[6]")                           # 總投注額
    total_profit_and_loss = (By.XPATH, "//thead//tr[3]//th[7]")                        # 總損益
    total_effective_bet_amount = (By.XPATH, "//thead//tr[3]//th[8]")                   # 總有效投注

class ValidMemberPage(BasePage):
    def member_account_search(self, account):
        # us = self.get_us_time()
        # today_start= datetime.datetime.now(us).strftime("%Y-%m-%d 00:00")
        # Now=  datetime.datetime.now(us).strftime("%M")
    
        # if int(Now) > 29 : # 確保遊戲報表能回來
        #     today_end= datetime.datetime.now(us).strftime("%Y-%m-%d %H:29")
        # else:
        #     today_end= (datetime.datetime.now(us) - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:29")
        
        self.click(ValidMemberPageLocator.btn_Today)
        self.type(ValidMemberPageLocator.member_account_input_box, account)   # 輸入會員帳號
        # self.click(ValidMemberPageLocator.last_week_button)                 # 上週按鈕(測試用)
        # self.type(ValidMemberPageLocator.start_time_input, today_start)       # 輸入開始時間
        # self.type(ValidMemberPageLocator.end_time_input, today_end)           # 輸入結束時間

        self.click(ValidMemberPageLocator.search_button)                      # 按搜尋鈕
        self.sleep(0.5)

    def choose_type_of_member_official(self):
        self.wait_loading_finish()
        self.click(ValidMemberPageLocator.type_of_membership_Official)        # 選擇正式-會員類型

    # 爬取搜尋會員結果
    def search_record(self, record, is_structure_switchin):
        if is_structure_switchin:
            if self.is_element_finded(ValidMemberPageLocator.member_account):
                member_account = self.get_text(ValidMemberPageLocator.member_account)
                member_agent = self.get_text(ValidMemberPageLocator.member_agent)
                member_generalagent = self.get_text(ValidMemberPageLocator.member_generalagent)
                member_shareholder = self.get_text(ValidMemberPageLocator.member_shareholder)
                order_quantity = self.get_text(ValidMemberPageLocator.order_quantity)
                order_amount = self.get_text(ValidMemberPageLocator.order_amount)
                profit_loss = self.get_text(ValidMemberPageLocator.profit_and_loss)
                effective_bet_amount = self.get_text(ValidMemberPageLocator.effective_bet_amount)

                assert order_quantity==str(record['Total']), '單量不正確'
                assert order_amount==record['Amount'], '投注額不正確'
                assert effective_bet_amount==record['Point'], '有效投注不正確'
                assert profit_loss==record['Income'], '損益不正確'

                # search_records = {"member_account": member_account, "member_agent": member_agent, "member_generalagent": member_generalagent,
                #                 "member_shareholder": member_shareholder, "order_quantity": order_quantity, "order_amount": order_amount,
                #                 "profit_loss": profit_loss, "effective_bet_amount": effective_bet_amount}
                # print(search_records)
            else:
                if record['Total']==0:
                    pass
                else:
                    assert False, "報表有值, 在代理內卻查無資料"

        else:
            if not self.is_element_finded(ValidMemberPageLocator.member_account):
                pass
            else:
                assert False, '在代理外卻查到資料'

    def total_check(self, is_structure_switchin):
        self.wait_loading_finish()
        self.click(ValidMemberPageLocator.today_button)                                         # 今日按鈕
        self.click(ValidMemberPageLocator.search_button)                                        # 按搜尋鈕
        self.sleep(0.5)
        if is_structure_switchin:
            if self.is_element_finded(ValidMemberPageLocator.member_account):
                quantities_cnt = 0
                amounts_cnt = 0
                profit_loss_cnt = 0
                effective_amounts_cnt = 0

                quantities = self.find_elements(ValidMemberPageLocator.order_quantity)                   # 單量
                amounts = self.find_elements(ValidMemberPageLocator.order_amount)                        # 投注額
                profit_loss = self.find_elements(ValidMemberPageLocator.profit_and_loss)                 # 損益
                effective_amounts = self.find_elements(ValidMemberPageLocator.effective_bet_amount)      # 有效投注額

                for idx in range(len(quantities)):
                    quantities_cnt += int(self.get_text_by_dom(quantities[idx]))
                    amounts_cnt += float(self.get_text_by_dom(amounts[idx]))
                    profit_loss_cnt += float(self.get_text_by_dom(profit_loss[idx]))
                    effective_amounts_cnt += float(self.get_text_by_dom(effective_amounts[idx]))
                

                assert quantities_cnt==int(self.get_text(ValidMemberPageLocator.total_order_quantity)), '加總單量不正確'
                assert amounts_cnt==float(self.get_text(ValidMemberPageLocator.total_order_amount)), '加總投注額不正確'
                assert profit_loss_cnt==float(self.get_text(ValidMemberPageLocator.total_profit_and_loss)), '加總損益不正確'
                assert effective_amounts_cnt==float(self.get_text(ValidMemberPageLocator.total_effective_bet_amount)), '加總有效投注額不正確'
            else:
                assert False, '會員帳號在代理內，但沒查找到今日資料'
        else:
            if self.is_element_finded(ValidMemberPageLocator.member_account):
                assert False, '會員帳號不在代理內，卻有資料'
            else:
                pass