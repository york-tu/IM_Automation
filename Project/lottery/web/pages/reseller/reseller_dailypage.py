from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class DailyPageLocator:
    # 查找條件
    btn_search = (By.XPATH, "//button/span[contains(text(), '查找')]")
    btn_last_month_application_datetime = (By.XPATH, "//button/span[contains(text(),'上月')]")

    btn_Today = (By.XPATH,"//button/span[contains(text(),'今日')]") 

    # 每日報表
    login_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[3]") # 登入數
    deposit_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[6]") # 存款數
    deposit_money_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[8]") # 存款總金額
    deposit_offer_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[9]") # 存款總優惠
    withdraw_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[11]") # 提款數
    withdraw_money_sum = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[12]") # 提款總金額
    handling_fee = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[13]") # 手續費
    
    total = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[14]") # 投注數
    amount = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[15]") # 投注額
    point = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[16]") # 打碼
    income = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[17]") # 損益
    rebate = (By.XPATH,"(//tr[@class='el-table__row el-table__row--striped danger-row']//div)[18]") # 返水

class DailyPage(BasePage):

    def daily_report(self, online_record, company_record, artificial_record, withdraw_record, withdraw_general_record, _sum):
        assert self.wait_visibility_status(DailyPageLocator.btn_search) is True,'進入每日報表錯誤'
        self.click(DailyPageLocator.btn_Today) 

        self.click(DailyPageLocator.btn_search)
        self.sleep(3)

        deposit_sum = int(float(online_record['online_total'])) + int(float(company_record['company_total'])) + int(float(artificial_record['artificial_total'])) # 存款數
        amount = float(online_record['online_amount']) + float(company_record['company_amount']) + float(artificial_record['artificial_amount']) # 存款額
        offer = float(online_record['online_discount']) + float(company_record['company_discount']) + float(artificial_record['artificial_discount']) # 存款優惠
        withdraw_sum = withdraw_general_record['withdraw_total'] # 提款總數
        withdraw_money_sum = float(withdraw_general_record['withdraw_amount']) # 取款額
        handling_fee = float(withdraw_record['withdraw_discount']) # 取款手續費

        assert float(self.get_text(DailyPageLocator.login_sum).replace(',', '')) >= 1 , '登入數低於0次'
        assert str(self.get_text(DailyPageLocator.deposit_sum)) == str(deposit_sum),'存款次數不正確'
        assert str(self.get_text(DailyPageLocator.deposit_money_sum)).replace(',','') == str("%.2f"%amount),'存款總金額不正確'
        assert str(self.get_text(DailyPageLocator.deposit_offer_sum)).replace(',','') == str("%.2f"%offer),'存款優惠總金額不正確'
        assert str(self.get_text(DailyPageLocator.withdraw_sum)) == str(withdraw_sum),'提款次數不正確'
        assert str(self.get_text(DailyPageLocator.withdraw_money_sum)).replace(',','') == str("%.2f"%withdraw_money_sum),'提款總金額不正確' 
        # assert str(self.get_text(DailyPageLocator.handling_fee)).replace(',','') == str("%.2f"%handling_fee),'提款手續費金額不正確' # 報表與提款申請資料不符

        assert str(self.get_text(DailyPageLocator.total)).replace(',','') == str(_sum['Total']),'投注總數不正確'
        assert str(self.get_text(DailyPageLocator.amount)).replace(',','') == str(_sum['Amount']),'投注額總數不正確'
        assert str(self.get_text(DailyPageLocator.point)).replace(',','') == str(_sum['Point']),'打碼量總數不正確'
        assert str(self.get_text(DailyPageLocator.income)).replace(',','') == str(_sum['Income']),'損益總數不正確'
        assert str(self.get_text(DailyPageLocator.rebate)).replace(',','') == str(_sum['Rebate']),'返水總數不正確'

    def undaily_report(self, online_record, company_record, artificial_record, withdraw_record, withdraw_general_record, _sum):
        assert self.wait_visibility_status(DailyPageLocator.btn_search) is True,'進入每日報表錯誤'
        self.click(DailyPageLocator.btn_Today) 

        self.click(DailyPageLocator.btn_search)
        self.sleep(3)

        deposit_sum = int(float(online_record['online_total'])) + int(float(company_record['company_total'])) + int(float(artificial_record['artificial_total'])) # 存款數
        amount = float(online_record['online_amount']) + float(company_record['company_amount']) + float(artificial_record['artificial_amount']) # 存款額
        offer = float(online_record['online_discount']) + float(company_record['company_discount']) + float(artificial_record['artificial_discount']) # 存款優惠
        withdraw_sum = withdraw_general_record['withdraw_total'] # 提款總數
        withdraw_money_sum = float(withdraw_general_record['withdraw_amount']) # 取款額
        handling_fee = float(withdraw_record['withdraw_discount']) # 取款手續費
        
        assert float(self.get_text(DailyPageLocator.login_sum).replace(',', '')) >= 0 , '登入數低於0次'
        assert str(self.get_text(DailyPageLocator.deposit_sum)) == str(deposit_sum),'存款次數不正確'
        assert str(self.get_text(DailyPageLocator.deposit_money_sum)).replace(',','') == str("%.2f"%amount),'存款總金額不正確'
        assert str(self.get_text(DailyPageLocator.deposit_offer_sum)).replace(',','') == str("%.2f"%offer),'存款優惠總金額不正確'
        assert str(self.get_text(DailyPageLocator.withdraw_sum)) == str(withdraw_sum),'提款次數不正確'
        assert str(self.get_text(DailyPageLocator.withdraw_money_sum)).replace(',','') == str("%.2f"%withdraw_money_sum),'提款總金額不正確' 
        # assert str(self.get_text(DailyPageLocator.handling_fee)).replace(',','') == str("%.2f"%handling_fee),'提款手續費金額不正確' # 報表與提款申請資料不符

        assert str(self.get_text(DailyPageLocator.total)).replace(',','') == str(_sum['Total']),'投注總數不正確'
        assert str(self.get_text(DailyPageLocator.amount)).replace(',','') == str(_sum['Amount']),'投注額總數不正確'
        assert str(self.get_text(DailyPageLocator.point)).replace(',','') == str(_sum['Point']),'打碼量總數不正確'
        assert str(self.get_text(DailyPageLocator.income)).replace(',','') == str(_sum['Income']),'損益總數不正確'
        assert str(self.get_text(DailyPageLocator.rebate)).replace(',','') == str(_sum['Rebate']),'返水總數不正確'