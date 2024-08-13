import math
from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import datetime

class WithDrawPageLocator:
    # WITHDRAW PAGE (線上取款)
    withdraw_amount_input = (By.XPATH, "//input[@placeholder='请输入整数提款金额']")
    withdraw_password = (By.XPATH, "//input[@type='password' or @class='withdraw-code__input']")
    withdraw_submit_btn_1 = (By.XPATH, "//button[contains(@class, 'submit')]")
    withdraw_submit_btn_2 = (By.XPATH, "//a[text()='我要取款']")

    withdraw_submit_btn_3 = (By.XPATH, "//a[text()='我要取款']")
    withdraw_submit_btn_nwap = (By.XPATH, "//button[@type='button']")
    withdraw_submit_btn_disabled = (By.XPATH, "//button[@type='button' and contains(@class,'btn--disabled')]")
    withdraw_status_pop = (By.XPATH,"//h2[@class='swal2-title']")
    withdraw_ok_btn = (By.XPATH,"//*[text()='OK']")

    withdraw_refunddiscount = (By.XPATH, "//span[@data-bind='text: refunddiscount']") # 折扣
    withdraw_charge = (By.XPATH, "//span[@data-bind='text: charge']") # 手續費
    withdraw_administrative = (By.XPATH, "//span[@data-bind='text: auditcharge']") # 行政費用
    withdraw_message = (By.XPATH, "//div[contains(text(),'申请提交成功，请耐心等待') and @style='']")
    withdraw_detial = (By.XPATH, "//div[@class='show_withdraw_list_btn']") # 顯示明細
    withdraw_money_in = (By.XPATH,"(//td[contains(@data-bind,'transferamount')])[1]")
    withdraw_time = (By.XPATH,"(//td[contains(@data-bind,'starttime')])[1]")

    withdraw_min = (By.XPATH,"//td[contains(text(),'最低提款限额')]/following-sibling::td[1]")
    withdraw_Max = (By.XPATH,"//td[contains(text(),'最高提款限额')]/following-sibling::td[1]")
    withdraw_refunddiscount_nwap = (By.XPATH, "//td[contains(text(),'需扣除优惠金额')]/following-sibling::td[1]") # 折扣
    withdraw_charge_nwap =         (By.XPATH, "//td[contains(text(),'手续费')]/following-sibling::td[1]") # 手續費
    withdraw_administrative_nwap = (By.XPATH, "//td[contains(text(),'需扣除行政费用')]/following-sibling::td[1]") # 行政費用
    withdraw_check_point_nwap = (By.XPATH, "//span[@class='logo-text']") # 導轉提款紀錄

    withdraw_bank_name = (By.XPATH, "//div[@class='passbook']")     #當前所選收款帳號
    withdraw_account = (By.XPATH, "//div[@class='el-input no-arrow']")    #選擇收款帳號
    withdraw_account_bank = (By.XPATH, "//select[@class='el-input__select']/option[contains(text(),'银行')]")   #收款帳號 銀行選項

    withdraw_bank_name_nwap = (By.XPATH, "//h3[@class='info-bank']")        #當前所選收款帳號
    withdeaw_bank_info_nwap = (By.XPATH,"//div[@class='info-account']")     
    withdraw_account_bank_nwap = (By.XPATH, "(//div[@class='van-ellipsis'])[last()]")   #收款帳號 銀行選項
    withdraw_account_cgpay_nwap = (By.XPATH, "//div[@class='van-ellipsis' and contains(text(),'CGPay')]")   #收款帳號 CGPay選項
    confirm_btn_nwap =  (By.XPATH, "//button[text()='确定']")               #確定按鈕
    success = (By.XPATH, "//*[contains(text(),'申请提交成功')]")
    account_manager_btn = (By.XPATH, "//div[@class='btn-default btn-md -primary -amount']")     # 收款帳號/地址管理
    account_manager_btn_nwap = (By.XPATH, "//a[@class='btn btn-secondary rounded-pill btn-ripple account-btn']")    # 收款帳號/地址管理

    # 選擇提款方式頁
    withdraw_bank =  (By.XPATH, "//p[contains(text(),'银行卡')]")
    withdraw_wallet = (By.XPATH, "//p[contains(text(),'虚拟钱包')]")

class WithDrawPage(BasePage):
    def do_withdraw(self, amount, withdraw_pwd, brand):
        self.wait_loading_finish()
        self.click(WithDrawPageLocator.withdraw_bank)
        self.wait_loading_finish()
        assert '-****-' in self.get_text(WithDrawPageLocator.withdraw_bank_name), '選擇銀行卡失敗'
        assert '收款账号管理' in self.get_text(WithDrawPageLocator.account_manager_btn), '收款帳號管理按鈕有誤'

        self.type(WithDrawPageLocator.withdraw_amount_input, str(amount)) # 輸入金額

        refunddiscount = self.get_text(WithDrawPageLocator.withdraw_refunddiscount)
        charge = self.get_text(WithDrawPageLocator.withdraw_charge)
        administrative = self.get_text(WithDrawPageLocator.withdraw_administrative)
        new_amount = float(amount) + (float(charge) + float(refunddiscount) + float(administrative)) # 實際加上手續費等等後金額

        self.type(WithDrawPageLocator.withdraw_amount_input, str(int(new_amount))) # 輸入金額
        amount_out = float(amount) - (float(charge) + float(refunddiscount) + float(administrative))
        sum_ = float(charge) + float(refunddiscount) + float(administrative)

        self.type(WithDrawPageLocator.withdraw_password, str(withdraw_pwd)) # 輸入密碼
        self.click(WithDrawPageLocator.withdraw_submit_btn_1)
        self.wait_visibility(WithDrawPageLocator.withdraw_ok_btn)
        self.click(WithDrawPageLocator.withdraw_ok_btn)

        return amount_out,sum_

    
    def do_cgpay_withdraw(self, amount, withdraw_pwd, brand):
        self.wait_loading_finish()
        self.click(WithDrawPageLocator.withdraw_wallet)
        self.wait_loading_finish()
        self.wait_visibility(WithDrawPageLocator.withdraw_account)  # 等待長出出款選項
        assert 'CGPay' in self.get_text(WithDrawPageLocator.withdraw_bank_name), '未新增虛擬錢包'
        assert '收款地址管理' in self.get_text(WithDrawPageLocator.account_manager_btn), '收款地址管理按鈕有誤'

        self.type(WithDrawPageLocator.withdraw_amount_input, str(amount)) # 輸入金額

        refunddiscount = self.get_text(WithDrawPageLocator.withdraw_refunddiscount)
        charge = self.get_text(WithDrawPageLocator.withdraw_charge)
        administrative = self.get_text(WithDrawPageLocator.withdraw_administrative)
        new_amount = float(amount) + (float(charge) + float(refunddiscount) + float(administrative)) # 實際加上手續費等等後金額

        self.type(WithDrawPageLocator.withdraw_amount_input, str(int(new_amount))) # 輸入金額
        amount_out = float(amount) - (float(charge) + float(refunddiscount) + float(administrative))
        sum_ = float(charge) + float(refunddiscount) + float(administrative)

        self.type(WithDrawPageLocator.withdraw_password, str(withdraw_pwd)) # 輸入密碼
        self.click(WithDrawPageLocator.withdraw_submit_btn_1)
        self.wait_visibility(WithDrawPageLocator.withdraw_ok_btn)
        self.click(WithDrawPageLocator.withdraw_ok_btn)

        return amount_out,sum_


    def do_nwap_withdraw(self, amount, withdraw_pwd, brand):
        self.wait_loading_finish()
        self.click(WithDrawPageLocator.withdraw_bank)
        self.wait_loading_finish()
        assert '账户' in self.get_text(WithDrawPageLocator.withdeaw_bank_info_nwap), '選擇銀行卡失敗'
        assert '收款账户管理' in self.get_text(WithDrawPageLocator.account_manager_btn_nwap), '收款帳號管理按鈕有誤'
        
        self.type(WithDrawPageLocator.withdraw_amount_input, str(amount)) # 輸入金額

        refunddiscount_nwap = self.get_text(WithDrawPageLocator.withdraw_refunddiscount_nwap).replace('元', '')
        charge_nwap = self.get_text(WithDrawPageLocator.withdraw_charge_nwap).replace('元', '')
        administrative_nwap = self.get_text(WithDrawPageLocator.withdraw_administrative_nwap).replace('元', '')
        new_amount_nwap = float(amount) + (float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap)) # 實際加上手續費等等後金額
        self.type(WithDrawPageLocator.withdraw_amount_input, str(int(new_amount_nwap))) # 輸入金額

        amount_out = float(amount) - (float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap))
        sum_ = float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap)

        self.type(WithDrawPageLocator.withdraw_password, str(withdraw_pwd)) # 輸入密碼
        if self.is_element_finded(WithDrawPageLocator.withdraw_submit_btn_disabled) is False:
            self.click(WithDrawPageLocator.withdraw_submit_btn_nwap)
        
        self.wait_loading_finish()
        self.wait_visibility(WithDrawPageLocator.success)
        assert self.get_text(WithDrawPageLocator.withdraw_check_point_nwap) == '提款记录', f'沒有導轉紀錄頁'

        return amount_out,sum_


    def do_nwap_cgpay_withdraw(self, amount, withdraw_pwd, brand):
        self.wait_loading_finish()
        self.click(WithDrawPageLocator.withdraw_wallet)
        self.wait_loading_finish()
        assert 'CGPay' in self.get_text(WithDrawPageLocator.withdraw_bank_name_nwap), '選擇虛擬錢包CGPay失敗'
        assert '收款地址管理' in self.get_text(WithDrawPageLocator.account_manager_btn_nwap), '收款地址管理按鈕有誤'
        
        self.type(WithDrawPageLocator.withdraw_amount_input, str(amount))  # 輸入金額

        refunddiscount_nwap = self.get_text(WithDrawPageLocator.withdraw_refunddiscount_nwap).replace('元', '')
        charge_nwap = self.get_text(WithDrawPageLocator.withdraw_charge_nwap).replace('元', '')
        administrative_nwap = self.get_text(WithDrawPageLocator.withdraw_administrative_nwap).replace('元', '')
        new_amount_nwap = float(amount) + (float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap)) # 實際加上手續費等等後金額

        self.type(WithDrawPageLocator.withdraw_amount_input, str(int(new_amount_nwap))) # 輸入金額
        amount_out = float(amount) - (float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap))
        sum_ = float(charge_nwap) + float(refunddiscount_nwap) + float(administrative_nwap)

        self.type(WithDrawPageLocator.withdraw_password, str(withdraw_pwd)) # 輸入密碼
        if self.is_element_finded(WithDrawPageLocator.withdraw_submit_btn_disabled) is False:
            self.click(WithDrawPageLocator.withdraw_submit_btn_nwap)
        
        self.wait_loading_finish()
        self.wait_visibility(WithDrawPageLocator.success)
        assert self.get_text(WithDrawPageLocator.withdraw_check_point_nwap) == '提款记录', f'沒有導轉紀錄頁'

        return amount_out,sum_


    
    # 抓取 線上取款 之值(進入銀行卡出款確認)
    def get_withdraw_info(self):
        self.wait_loading_finish()
        self.click(WithDrawPageLocator.withdraw_bank)
        self.wait_loading_finish()
        if self.is_element_finded(WithDrawPageLocator.withdraw_amount_input) is True:
            self.type(WithDrawPageLocator.withdraw_amount_input, 100000)

        charge = self.get_text(WithDrawPageLocator.withdraw_charge_nwap).replace('元', '').replace(' ','')         # 取得提款手續
        min_ = self.get_text(WithDrawPageLocator.withdraw_min).replace('元', '').replace(',', '').replace('.00', '').replace(' ','')  # 取得最小出款
        Max = self.get_text(WithDrawPageLocator.withdraw_Max).replace('元', '').replace(',', '').replace('.00', '').replace(' ','')   # 取得最大出款

        return charge, min_, Max
