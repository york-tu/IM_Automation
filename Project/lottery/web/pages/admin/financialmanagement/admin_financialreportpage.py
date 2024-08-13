from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class FinancialReportPageLocator:
    # -- 查找條件 --
    button_today = (By.XPATH, '//button[@qa-button="quick-time-today"]')        # 今日按鈕
    button_yesterday = (By.XPATH, '//button[@qa-button="quick-time-yestoday"]')    # 昨日按鈕
    button_this_week = (By.XPATH, '//button[@qa-button="quick-time-thisWeek"]')    # 本周按鈕
    button_last_week = (By.XPATH, '//button[@qa-button="quick-time-lastWeek"]')    # 上周按鈕
    button_this_month = (By.XPATH, '//button[@qa-button="quick-time-thisMonth"]')   # 本月按鈕
    button_last_month = (By.XPATH, '//button[@qa-button="quick-time-lastMonth"]')   # 上月按鈕
    button_search = (By.XPATH, '//button[@qa-button="search"]')       # 查找按鈕
    button_export = (By.XPATH, '//button[@qa-button="export"]')       # 匯出按鈕
    button_condition = (By.XPATH, '//button[contains(@class,"ps-query-container")]')       # 條件收合按鈕
    button_down = (By.XPATH, "//i[@class='el-icon-arrow-down']")    # 條件展開
    textarea_agent = (By.XPATH, '//input[@qa-input="agent"]')       # 代理輸入框
    textarea_generalagent = (By.XPATH, '//input[@qa-input="generalagent"]')       # 總代輸入框

    # -- 財務報表 --
    company_deposit = (By.XPATH, '//div[contains(text(),"公司入款(含人工公司入款)")]/../..//span[@class="fn-income-text-color"]')             # 公司入款 >收入金額
    online_payment  = (By.XPATH, '//div[contains(text(),"线上支付入款(含人工在线入款)")]/../..//span[@class="fn-income-text-color"]')         # 線上入款 >收入金額
    online_payment_fee = (By.XPATH, '//div[contains(text(),"线上支付手续费")]/../..//span[@class="fn-income-text-color"]')                   # 線上支付手續費 >收入金額
    manual_deposit  = (By.XPATH, '//div[contains(text(),"人工存入")]/../..//span[@class="fn-income-text-color"]')                           # 人工存入 >收入金額
    member_payment_deducted = (By.XPATH, '//div[contains(text(),"会员出款被扣除金额")]/../..//span[@class="fn-income-text-color"]')          # 會員出款被扣除金額 >收入金額
    withdrawal_apply = (By.XPATH, '//span[contains(text(),"出款申请")]/../../..//span[@class="fn-expenses-text-color"]')                    # 出款申請 >支出金額
    give_discount = (By.XPATH, '//span[contains(text(),"给予优惠")]/../../..//span[@class="fn-expenses-text-color"]')                       # 給予優惠 >支出金額
    manual_withdrawal = (By.XPATH, '//span[contains(text(),"人工提出")]/../../..//span[@class="fn-expenses-text-color"]')                   # 人工提出 >支出金額
    give_back = (By.XPATH, '//span[contains(text(),"给予反水")]/../../..//span[@class="fn-expenses-text-color"]')                           # 給予返水 >支出金額
    
    detail_btn = (By.XPATH, "//button[contains(@qa-button, 'next-level')]")                       # 任意詳情按鍵
    deposit_detail_btn = (By.XPATH, '//button[@qa-button="next-level-deposit"]')                  # 公司入款 >詳情按鍵
    webdeposit_detail_btn = (By.XPATH, '//button[@qa-button="next-level-webdeposit"]')            # 線上入款 >詳情按鍵
    webdeposit_fee_detail_btn = (By.XPATH, '//button[@qa-button="next-level-webdeposit_fee"]')    # 線上支付手續費 >詳情按鍵
    manual_deposit_detail_btn = (By.XPATH, '//button[@qa-button="next-level-manual_deposit"]')    # 人工存入 >詳情按鍵
    withdraw_fee_detail_btn = (By.XPATH, '//button[@qa-button="next-level-withdraw_fee"]')        # 會員出款被扣除金額 >詳情按鍵
    withdraw_detail_btn = (By.XPATH, '//button[@qa-button="next-level-withdraw"]')                # 出款申請 >詳情按鍵
    discount_detail_btn = (By.XPATH, '//button[@qa-button="next-level-discount"]')                # 給予優惠 >詳情按鍵
    manual_withdraw_detail_btn = (By.XPATH, '//button[@qa-button="next-level-manual_withdraw"]')  # 人工提出 >詳情按鍵
    rebate_detail_btn = (By.XPATH, '//button[@qa-button="next-level-rebate"]')                    # 給予返水 >詳情按鍵
    totle = (By.XPATH, '//div[contains(text(),"帐目总计")]/span[@class="fn-income-text-color"]')   # 帳目總計
    
    detail_money = (By.XPATH, "//tr[contains(@class,'el-table__row')]/td[last()]")  #第二層金額欄
    back_btn = (By.XPATH, "//button[@qa-button='back']")                            #第二層返回第一層按鈕

class FinancialReportPage(BasePage):
    # 查找時間
    def search_for_time(self, time):
        if time == 1:
            self.click(FinancialReportPageLocator.button_today)
        elif time == 2:
            self.click(FinancialReportPageLocator.button_yesterday)
        elif time == 3:
            self.click(FinancialReportPageLocator.button_this_week)
        elif time == 4:
            self.click(FinancialReportPageLocator.button_last_week)
        elif time == 5:
            self.click(FinancialReportPageLocator.button_this_month)
        else:
            self.click(FinancialReportPageLocator.button_last_month)
        
        self.click(FinancialReportPageLocator.button_search)

        self.wait_loading_finish()

        assert self.is_element_finded(FinancialReportPageLocator.company_deposit), "查找功能錯誤或查無資料"
    
    # 查找代理
    def search_for_agent(self, account):
        assert self.is_element_finded(FinancialReportPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(FinancialReportPageLocator.textarea_agent)
        self.type(FinancialReportPageLocator.textarea_agent, account)
        self.click(FinancialReportPageLocator.button_search)
        self.wait_loading_finish()
        for _ in range(3):
            if self.is_element_finded(FinancialReportPageLocator.company_deposit) is False:
                self.click(FinancialReportPageLocator.button_search)
                self.wait_loading_finish()

    # 爬取資料
    def get_data(self):
        self.wait_loading_finish()
        self.sleep(1)
        assert self.is_element_finded(FinancialReportPageLocator.detail_btn), "財務報表無資料"

        company_deposit = self.get_text(FinancialReportPageLocator.company_deposit).replace(',', '')
        online_payment = self.get_text(FinancialReportPageLocator.online_payment).replace(',', '')
        online_payment_fee = self.get_text(FinancialReportPageLocator.online_payment_fee).replace(',', '')        # 無可比對資料
        manual_deposit = self.get_text(FinancialReportPageLocator.manual_deposit).replace(',', '')
        member_payment_deducted = self.get_text(FinancialReportPageLocator.member_payment_deducted).replace(',', '')
        withdrawal_apply = self.get_text(FinancialReportPageLocator.withdrawal_apply).replace(',', '')
        give_discount = self.get_text(FinancialReportPageLocator.give_discount).replace(',', '')
        manual_withdrawal = self.get_text(FinancialReportPageLocator.manual_withdrawal).replace(',', '')
        give_back = self.get_text(FinancialReportPageLocator.give_back).replace(',', '')

        assert company_deposit != '0.00' , "財務報表_公司入款 金額為 0"        
        return [company_deposit, online_payment, online_payment_fee, manual_deposit, member_payment_deducted, withdrawal_apply, give_discount, manual_withdrawal, give_back]

    # 驗證財務報表資料
    def verify_data(self, data_list, for_company, withdraw_dict, for_online, list_for_give_discount, list_for_manual_deposit, for_manual_withdrawal, for_give_back):
        assert float(data_list[0]) == float(for_company), f'公司入款金額有誤，財務報表:{float(data_list[0])}，公司入款:{float(for_company)}'
        assert float(data_list[1]) == float(for_online), f'線上支付金額有誤，財務報表:{float(data_list[1])}，在線入款:{float(for_online)}'
        assert data_list[3] == list_for_manual_deposit[0], f'人工存入金額有誤，財務報表:{data_list[3]}，人工存入報表:{list_for_manual_deposit[0]}'
        assert data_list[4] == withdraw_dict['withdraw_discount'], f'會員出款被扣除金額有誤，財務報表:{data_list[4]}，出款申請報表:{withdraw_dict["withdraw_discount"]}'
        assert data_list[5] == withdraw_dict['withdraw_amount'], f'出款申请金額有誤，財務報表:{data_list[5]}，出款申請:{withdraw_dict["withdraw_amount"]}'
        assert float(data_list[6]) == float(list_for_give_discount[1]), f'給予優惠金額有誤，財務報表:{float(data_list[6])}，人工存入報表:{float(list_for_give_discount[1])}'
        assert data_list[7] == for_manual_withdrawal, f'人工提出金額有誤，財務報表:{data_list[7]}，人工提出報表:{for_manual_withdrawal}'
        assert float(data_list[8]) == float(for_give_back), f'給予反水金額有誤，財務報表:{float(data_list[8])}，人工提出報表:{float(for_give_back)}'


    # 比對 第一層與第二層金額
    def verify_detail_data(self,data_list):
        deposit = self.get_detail_data_sum(FinancialReportPageLocator.deposit_detail_btn)                   # 公司入款
        webdeposit = self.get_detail_data_sum(FinancialReportPageLocator.webdeposit_detail_btn)             # 線上支付
        webdeposit_fee = self.get_detail_data_sum(FinancialReportPageLocator.webdeposit_fee_detail_btn)     # 线上支付手续费
        manual_deposit = self.get_detail_data_sum(FinancialReportPageLocator.manual_deposit_detail_btn)     # 人工存入
        withdraw_fee = self.get_detail_data_sum(FinancialReportPageLocator.withdraw_fee_detail_btn)         # 会员出款被扣除金额

        withdraw = self.get_detail_data_sum(FinancialReportPageLocator.withdraw_detail_btn)                 # 出款申请
        discount = self.get_detail_data_sum(FinancialReportPageLocator.discount_detail_btn)                 # 给予优惠
        manual_withdraw = self.get_detail_data_sum(FinancialReportPageLocator.manual_withdraw_detail_btn)   # 人工提出
        rebate = self.get_detail_data_sum(FinancialReportPageLocator.rebate_detail_btn)                     # 给予反水

        assert float(data_list[0]) == deposit , f'公司入款內外層金額不一致，外層:{float(data_list[0])}，內層總和:{deposit}'
        assert float(data_list[1]) == webdeposit , f'線上支付內外層金額不一致，外層:{float(data_list[1])}，內層總和:{webdeposit}'
        assert float(data_list[2]) == webdeposit_fee , f'线上支付手续费內外層金額不一致，外層:{float(data_list[2])}，內層總和:{webdeposit_fee}'
        assert float(data_list[3]) == manual_deposit , f'人工存入內外層金額不一致，外層:{float(data_list[3])}，內層總和:{manual_deposit}'
        assert float(data_list[4]) == withdraw_fee , f'会员出款被扣除金额內外層金額不一致，外層:{float(data_list[4])}，內層總和:{withdraw_fee}'

        assert float(data_list[5]) == withdraw , f'出款申请內外層金額不一致，外層:{float(data_list[5])}，內層總和:{withdraw}'
        assert float(data_list[6]) == discount , f'给予优惠內外層金額不一致，外層:{float(data_list[6])}，內層總和:{discount}'
        assert float(data_list[7]) == manual_withdraw , f'人工提出內外層金額不一致，外層:{float(data_list[7])}，內層總和:{manual_withdraw}'
        assert float(data_list[8]) == rebate , f'给予反水內外層金額不一致，外層:{float(data_list[8])}，內層總和:{rebate}'


    # 取得第二層金額總和
    def get_detail_data_sum(self, item_locator):
        sum = 0.0
        if self.is_element_finded(item_locator) is False:
            return sum

        self.click(item_locator)
        for money in self.find_elements(FinancialReportPageLocator.detail_money):
            sum += float((money.text).replace(',', ''))
        self.click(FinancialReportPageLocator.back_btn)
        return round(sum, 2)
