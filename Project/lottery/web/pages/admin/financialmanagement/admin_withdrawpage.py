from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import re
import math


class WithdrawPageLocator:
    # SEARCH AREA (查找條件區)
    input_min_amount = (By.XPATH, "//input[@data-bind='value: filter.minamount' ]") # 申請金額最小值
    input_max_amount = (By.XPATH, "//input[@data-bind='value: filter.maxamount' ]") # 申請金額最大值
    input_member_account = (By.XPATH, "//input[@data-bind='value: filter.memberlogin']") # 會員帳號
    ledger = (By.XPATH, "//input[contains(@data-bind,'filter.id')]") # 流水號
    input_card_number = (By.XPATH, "//input[@data-bind='value: filter.cardnumber']") # 出款卡號
    input_wallet_address = (By.XPATH, "//input[@data-bind='value: filter.walletaddress']") # 錢包地址
    refresh_raido = (By.XPATH, "//div[text()='秒']/..//input[@type='checkbox']") # 自動刷新開關
    refresh_sec = (By.XPATH, "//input[contains(@data-bind,'nterval')]") # 自動刷新秒數
    input_lock_login = (By.XPATH, "//input[@data-bind='value: filter.locklogin']") # 鎖定人員
    input_audit_login = (By.XPATH, "//input[@data-bind='value: filter.auditlogin']") # 確定人員
    btn_today_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'今日')]")
    btn_yesterday_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'昨日')]")
    btn_this_week_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'本周')]")
    btn_last_week_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'上周')]")
    btn_this_month_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'本月')]")
    btn_last_month_application_datetime = (By.XPATH, "//span[text()='申请时间']/../following::button[contains(text(),'上月')]") # 上月
    find_shareholder = (By.XPATH, "//textarea[contains(@data-bind,'shareLoginItems')]") # 股東
    find_generalagent = (By.XPATH, "//input[contains(@data-bind,'generalagent')]") # 總代
    find_agent = (By.XPATH, "//input[@data-bind='textInput: filter.agent']") # 代理
    member_level1 = (By.XPATH, "//label[text()='会员级别']/..//input[@value='1']") # 一級會員
    member_level2 = (By.XPATH, "//label[text()='会员级别']/..//input[@value='2']") # 二級會員
    member_level4 = (By.XPATH, "//label[text()='会员级别']/..//input[@value='4']") # 四級會員
    member_automated = (By.XPATH, "//label[text()='会员级别']/..//div[@class='col-md-11']//label")
    status = (By.XPATH, "//label[@class='col-md-1 control-label' and text()='出款状态']/following::label[3]") # 確認狀態為已出帳
    status_cancel = (By.XPATH, "//label[@class='col-md-1 control-label' and text()='出款状态']/following::label[4]") # 確認狀態為已取消
    status_reject= (By.XPATH,"//label[@class='col-md-1 control-label' and text()='出款状态']/following::label[5]") # 確認狀態為已拒絕
    btn_start_time = (By.XPATH, "//input[contains(@data-bind,'starttime')]") # 查找開始時間  
    btn_end_time = (By.XPATH, "//input[contains(@data-bind,'endtime')]") # 查找結束時間
    btn_search = (By.XPATH, "//*[contains(text(),'查找')]")
    btn_export = (By.XPATH, "//button[contains(text(),'汇出')]") # //i[@class='glyphicon glyphicon-ok']
    btn_export_comfirm = (By.XPATH, "//i[@class='glyphicon glyphicon-ok']")

    # RESULT AREA (搜尋結果區)
    btn_lock_first = (By.XPATH, "(//div[@class='btn-group'])[1]/button[text()='锁定']")
    btn_withdraw = (By.XPATH, "(//div[@class='btn-group'])[1]/button[text()='出款']")
    btn_second_confirm = (By.XPATH, "//a[@class='btn btn-xs btn-primary']") # 確定
    btn_second_cancel = (By.XPATH, "//a[@class='btn btn-xs btn-default']") # 確認視窗的取消
    btn_online_withdraw = (By.XPATH, "(//div[@class='btn-group'])[1]/button[text()='在线出款']")
    # 點擊特定在線出款的立即出款按鈕
    def do_online_withdrew(self, name):
        online_withdrew = (By.XPATH, f"//td[text()='{name}']/..//a[@data-bind='click:$parent.submit']")
        return online_withdrew
    ok_point_confirm_withdraw = (By.XPATH, "//tbody[@data-bind='foreach: items']/tr[1]//span[contains(@data-bind,'待确认')]")
    ok_point_confirm_withdraw1 = (By.XPATH, "//tbody[@data-bind='foreach: items']/tr[2]//span[contains(@data-bind,'待确认')] ")
    ok_point_confirm_withdraw2 = (By.XPATH, "//tbody[@data-bind='foreach: items']/tr[3]//span[contains(@data-bind,'待确认')] ")
    member_check = (By.XPATH,"//td[contains(@data-bind,'text: memberlogin')]") # 確認會員欄位是否為空
    btn_lock_second = (By.XPATH, "(//div[@class='btn-group'])[2]/button[text()='锁定']")
    # btn_cancel = (By.XPATH, "(//div[@class='btn-group'])[2]/button[text()='取消']") # 取消
    btn_cancel = (By.XPATH, "(//div[@class='btn-group'])[2]/button[@data-bind='visible: locklogin() && status() === 0, prompt: $parent.cancel']") #取消 20/07/17
    btn_lock_third = (By.XPATH, "(//div[@class='btn-group'])[3]/button[text()='锁定']")
    # btn_reject = (By.XPATH, "(//div[@class='btn-group'])[3]/button[text()='拒绝']") # 拒绝
    btn_reject = (By.XPATH, "(//div[@class='btn-group'])[3]/button[@data-bind='visible: locklogin() && status() === 0, prompt: $parent.reject']") # 拒绝 20/07/17
    bank_card = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'银行卡号:')]") # 銀行卡號
    virtual_name = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'钱包名称: ')]") # 錢包名稱
    virtual_card_copy = (By.XPATH, "//span[contains(text(),'钱包名称: CGPay')]/..//button[text()='复制']") # 銀行卡號_複製btn
    amount = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'申请金额:')]") #  申請金額
    refund_discount_amount = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'扣除优惠:')]") # 扣除優惠
    audit_charge = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'行政费用:')]") # 行政費用
    charge = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'出款手续:')]") # 出款手續
    frozen_amount = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'冻结:')]") # 凍結
    transfer_amount = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr//td//span[contains(@data-bind,'应出:')]") # 應出
    toast_message = (By.XPATH, "//*[@class='toast-message']")                             # 右下角訊息

    # 整頁資料
    add_time = (By.XPATH, "//tbody[1]//tr//td[@data-bind='text: addedtime']") # 申請時間
    level_name_list = (By.XPATH, "//td[@data-bind='text: levelname']") # 層級
    member_login = (By.XPATH, "//td[@data-bind='text: memberlogin']") # 會員
    agent_list = (By.XPATH,"//span[@data-bind='text: agent']") # 代理
    generalagent_list = (By.XPATH,"//span[contains(@data-bind,'generalagent')]") # 總代
    shareholder_list = (By.XPATH,"//span[contains(@data-bind,'sharelogin')]") # 股東
    # warning_list = (By.XPATH, "//span[contains(@data-bind,'备注信息:')]") # 異常信息
    # warning_list = (By.XPATH, "//span[@class='text-danger']") # 異常信息
    warning_list = (By.XPATH, "//div[@class='text-danger']/../..") # 異常信息
    warning_copy_list = (By.XPATH, "//div[@class='text-danger']/div[@style='']//button[contains(text(),'复制')]") # 異常信息 複製按鈕
    bank_list = (By.XPATH, "//span[contains(@data-bind,'cardnumber')]/..") # 銀行信息
    apply_amount_list = (By.XPATH, "//span[contains(@data-bind,'申请金额')]") # 申請金額
    discount_amount_list = (By.XPATH, "//span[contains(@data-bind,'扣除优惠')]") # 申請金額
    administrative_costs_list = (By.XPATH, "//span[contains(@data-bind,'行政费用')]") # 行政费用
    withdrawal_procedures_list = (By.XPATH, "//span[contains(@data-bind,'出款手续')]") # 出款手续
    frozen_amount_list = (By.XPATH, "//span[contains(@data-bind,'冻结')]") # 凍結金額
    amount_due_list = (By.XPATH, "//span[contains(@data-bind,'应出')]") # 應出金額
    lock_personnel_list = (By.XPATH, "//span[contains(@data-bind,'锁定人员')]") # 鎖定人員
    confirm_personnel_list = (By.XPATH, "//span[contains(@data-bind,'确认人员')]") # 确认人員
    card_bank_name_list = (By.XPATH, "//span[contains(@data-bind,'开户银行') or contains(@data-bind,'钱包名称')]") # 開戶銀行 or 钱包名称
    card_name_list = (By.XPATH, "//span[contains(@data-bind,'开户姓名')]") # 开户姓名




    amount_list = (By.XPATH, "//span[contains(@data-bind,'申请金额')]/..") # 費用金額
    withdraw_list = (By.XPATH, "//span[contains(@data-bind,'frozen_amount')]/..") # 出款金額
    status_check = (By.XPATH, "//td[contains(@data-bind, '待确认')]") # 狀態
    operator_list = (By.XPATH, "//span[contains(@data-bind,' locklogin')]/..") # 操作者
    remark = (By.XPATH, "//td[contains(@data-bind,'remark()')]") # 備註    

    # 頁數
    total_pages = (By.XPATH, "//span[contains(@data-bind,'pager.total')]") # 總*條數
    page_size = (By.XPATH, "//*[contains(@data-bind,'pageSize')]//option") # 每頁最多顯示筆數 個別
    page_list = (By.XPATH, "//*[contains(@data-bind,'pageSize')]") # 每頁最多筆數 總下拉式選單
    last_page = (By.XPATH, '//a[text()="尾页"]') 
    rows = (By.XPATH, "//tbody[@data-bind='foreach: items']//tr") # 列  

    # 小計
    sub_total_table = (By.XPATH,"//span[text()='小计']/../..//td[@style='white-space: nowrap;']")
    sub_sum_amount = (By.XPATH, "//span[contains(@data-bind,'money: sum.subamount')]") # 申請小計
    sum_refund_discount_amount = (By.XPATH, "//span[contains(@data-bind,'money: sum.subdiscount')]") # 扣除優惠小計
    sub_sum_charge = (By.XPATH, "//span[contains(@data-bind,'money: sum.subcharge')]") # 手續費小計
    sub_sum_frozen_amount = (By.XPATH, "//span[@data-bind='money: sum.subfrozen']") # 凍結小計
    sub_sum_transfer_amount = (By.XPATH, "//span[@data-bind='money: sum.subwithdraw']") # 應出小計

    # 總計
    total_table = (By.XPATH, "//span[text()='总计']/../..//td[@style='white-space: nowrap;']")
    sub_total = (By.XPATH, "//span[contains(@data-bind,'sum.total')]") # 總計*條
    sum_amount = (By.XPATH, "//span[contains(@data-bind,'money: sum.amount')]") # 申請總計
    discount = (By.XPATH, "//span[@data-bind='money: sum.discount']") # 扣除優惠總金額 
    sum_charge = (By.XPATH, "//span[@data-bind='money: sum.charge']") # 手續費總金額
    sum_frozen_amount = (By.XPATH, "//span[@data-bind='money: sum.frozen']") # 凍結總金額
    sum_transfer_amount = (By.XPATH, "//span[@data-bind='money: sum.withdraw']") # 應出總計

    # 出款總攬 page
    btn_today_withdraw_datetime = (By.XPATH, "//button[@qa-button='quick-time-today']")
    btn_last_month_withdraw_datetime = (By.XPATH, "//button[@qa-button='quick-time-lastMonth']")
    withdraw_check = (By.XPATH, "//td[8]") # 交易類別
    detail = (By.XPATH, "//span[text()='明细']") # 明細
    input_member_account_general = (By.XPATH, "//input[@qa-input='member_login']") # 會員帳號
    downpage = (By.XPATH, "(//span[@class='el-input__suffix'])[last()]")    # 切換每頁筆數
    page_option = (By.XPATH,"//span[text()='500条/页']")

class WithdrawPage(BasePage):
    def search_today_withdraw_by_member(self, account):
        self.type(WithdrawPageLocator.input_member_account, account)
        self.click(WithdrawPageLocator.btn_today_application_datetime)
        # self.click(WithdrawPageLocator.status) # 測是已出款選項
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()

    # 解鎖→出款
    def pass_first_withdraw(self, account):
        self.scroll_to(500)
        self.click(WithdrawPageLocator.btn_lock_first)
        self.wait_loading_finish()

        for _ in range(0,4):
            if self.is_element_finded(WithdrawPageLocator.btn_withdraw) is True:
                self.click(WithdrawPageLocator.btn_withdraw)
                break
            else:
                self.sleep(5)
                self.search_today_withdraw_by_member(account)
                self.wait_loading_finish()
                self.click(WithdrawPageLocator.btn_lock_first)

        self.wait_loading_finish()
        self.click(WithdrawPageLocator.btn_second_confirm)
        for _ in range(0,2):
            self.wait_visibility(WithdrawPageLocator.ok_point_confirm_withdraw) 
            message = self.get_text(WithdrawPageLocator.ok_point_confirm_withdraw) 

            if message == '已出款':
                break
            self.sleep(3)

        assert message == "已出款", f'{message}，後台出款異常'   

    # 解鎖→取消
    def cancel_second_withdraw(self, account):
        self.sleep(1)
        self.click(WithdrawPageLocator.btn_lock_second)
        self.wait_loading_finish()

        for _ in range(0,4):
            if self.is_element_finded(WithdrawPageLocator.btn_cancel) is True:
                self.sleep(1)
                self.click(WithdrawPageLocator.btn_cancel)
                break
            else:
                self.sleep(5)
                self.search_today_withdraw_by_member(account)
                self.wait_loading_finish()
                self.sleep(1)
                self.click(WithdrawPageLocator.btn_lock_second)

        self.wait_alert_present()
        message = self.get_alert_message()
        assert str(message).__contains__('请输入取消原因')
        self.sendkey_alert('測試')
        self.accept_alert()
        self.wait_loading_finish()       

        self.sleep(3)

        for _ in range(0,2):
            self.wait_visibility(WithdrawPageLocator.ok_point_confirm_withdraw1) 
            message = self.get_text(WithdrawPageLocator.ok_point_confirm_withdraw1) 

            if message == '已取消':
                break
            self.sleep(3)

        assert message == "已取消", f'{message}，後台出款異常'

    # 解鎖→拒絕
    def reject_third_withdraw(self, account):
        self.click(WithdrawPageLocator.btn_lock_third)
        self.wait_loading_finish()

        for _ in range(0, 4):
            if self.is_element_finded(WithdrawPageLocator.btn_reject) is True:
                self.click(WithdrawPageLocator.btn_reject)
                break
            else:
                self.sleep(5)
                self.search_today_withdraw_by_member(account)
                self.wait_loading_finish()
                self.click(WithdrawPageLocator.btn_lock_third)

        self.wait_alert_present()
        message = self.get_alert_message()
        assert str(message).__contains__('请输入拒绝原因')        
        self.sendkey_alert('測試')
        self.accept_alert()
        self.wait_loading_finish() 

        for _ in range(0, 2):
            self.wait_visibility(WithdrawPageLocator.ok_point_confirm_withdraw2) 
            message = self.get_text(WithdrawPageLocator.ok_point_confirm_withdraw2)

            if message == '已拒绝':
                break
            self.sleep(3)

        assert message == "已拒绝", f'{message}，後台出款異常'
    
    # 在線出款
    def pass_first_online_withdraw(self, account, online_withdrew):
        self.scroll_to(500)
        self.click(WithdrawPageLocator.btn_online_withdraw)
        self.wait_loading_finish()
        self.wait_visibility(WithdrawPageLocator.do_online_withdrew(self, online_withdrew)) #在在線商號彈窗尋找指定出款方式
        self.click(WithdrawPageLocator.do_online_withdrew(self, online_withdrew))

        self.wait_loading_finish()
        assert self.is_element_finded(WithdrawPageLocator.toast_message) == False, f"在線出款失敗：{self.get_text(WithdrawPageLocator.toast_message)}"


    def get_sum_info(self, reseller_account, time=''):
        self.type(WithdrawPageLocator.find_agent, reseller_account)
        # self.click(WithdrawPageLocator.btn_last_month_application_datetime) # 測試用

        if time == '':
            today_start = self.get_us_time().strftime("%Y-%m-%d 00:00")
            now = self.get_us_time().strftime("%M")
        
            if int(now) > 29 : # 確保遊戲報表能回來
                today_end = self.get_us_time().strftime("%Y-%m-%d %H:29")
            else:
                today_end = (self.get_us_time() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:29")
                
            self.type(WithdrawPageLocator.btn_start_time, today_start)  # 因每小時的30分會更新,故搜尋31-29分
            self.type(WithdrawPageLocator.btn_end_time, today_end)  
        elif time == '1':
            self.click(WithdrawPageLocator.btn_today_application_datetime)
        elif time == '2':
            self.click(WithdrawPageLocator.btn_yesterday_application_datetime)
        elif time == '3':
            self.click(WithdrawPageLocator.btn_this_week_application_datetime)
        elif time == '4':
            self.click(WithdrawPageLocator.btn_last_week_application_datetime)
        elif time == '5':
            self.click(WithdrawPageLocator.btn_this_month_application_datetime)
        elif time == '6':
            self.click(WithdrawPageLocator.btn_last_month_application_datetime)

        self.click(WithdrawPageLocator.status)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        if self.is_element_finded(WithdrawPageLocator.member_check) is False:
            withdraw_record = {
                'withdraw_amount': "0.00",
                'Withdraw_apply': "0.00",
                'withdraw_total': "0",
                'withdraw_discount': "0.00",
            }
            return withdraw_record

        withdraw_amount = float(str(self.get_text(WithdrawPageLocator.sum_transfer_amount)).replace(',', ''))
        Withdraw_apply = float(str(self.get_text(WithdrawPageLocator.sum_amount)).replace(',', ''))
        withdraw_total = float(str(self.get_text(WithdrawPageLocator.sub_total)).replace(',', ''))
        withdraw_discount = round(float(str(self.get_text(WithdrawPageLocator.sum_amount)).replace(',', '')) - float(str(self.get_text(WithdrawPageLocator.sum_transfer_amount)).replace(',', '')), 2)
        
        withdraw_record={
            'withdraw_amount': "%.2f" %withdraw_amount, # 應出
            'Withdraw_apply': "%.2f" %Withdraw_apply, # 申請
            'withdraw_total': withdraw_total, # 總計*條
            'withdraw_discount': "%.2f" %withdraw_discount, # 優惠
        }
        return withdraw_record

    # 每頁最大筆數測試
    def page_range(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num()

    # 頁數及尾頁餘數數量
    def check_pages(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.scroll_to_bottom()
        self.check_page() 
        
    # 總計跟小計
    def check_total_subtotal(self, web_account):
        # 資料的處理
        def get_details():
            pattern = re.compile(r"(\d+(\.\d+)?)")
            total_data = list()
            record_number = int(self.get_text(WithdrawPageLocator.total_pages))
            for index in range(record_number):
                amount_path = (By.XPATH, "(//span[contains(@data-bind,'申请金额:')])[{}]".format(index+1))
                refunddiscountamount_path = (By.XPATH, "(//span[contains(@data-bind,'扣除优惠:')])[{}]".format(index+1))
                auditcharge_path = (By.XPATH, "(//span[contains(@data-bind,'行政费用:')])[{}]".format(index+1))
                charge_path = (By.XPATH, "(//span[contains(@data-bind,'出款手续:')])[{}]".format(index+1))
                frozenamount_path = (By.XPATH, "(//span[contains(@data-bind,'冻结:')])[{}]".format(index+1))
                transferamount_path = (By.XPATH, "(//span[contains(@data-bind,'应出:')])[{}]".format(index+1))
                get_amount = self.get_text(amount_path)
                get_refunddiscountamount = self.get_text(refunddiscountamount_path) 
                get_auditcharge = self.get_text(auditcharge_path) 
                get_charge = self.get_text(charge_path) 
                get_frozenamount = self.get_text(frozenamount_path) 
                get_transferamount = self.get_text(transferamount_path)                
                amount = float(pattern.search(get_amount).group())
                refund_discount_amount = float(pattern.search(get_refunddiscountamount).group())
                audit_charge = float(pattern.search(get_auditcharge).group())
                charge = float(pattern.search(get_charge).group())
                frozen_amount = float(pattern.search(get_frozenamount).group())
                transfer_amount = float(pattern.search(get_transferamount).group())
                
                data = {
                    "amount": amount,
                    "refund_discount_amount": refund_discount_amount, 
                    "audit_charge": audit_charge,
                    "charge": charge,
                    "frozen_amount": frozen_amount,
                    "transfer_amount": transfer_amount
                }
                total_data.append(data)
                
            return total_data
        
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.select_by_text(WithdrawPageLocator.page_list, '500')
        self.wait_loading_finish()
        pages = math.ceil(int(self.get_text(WithdrawPageLocator.total_pages)) / 500) # 抓換500筆檢視 共有幾頁
        # 換頁
        if pages > 1:
            self.click((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(pages)))
            self.wait_loading_finish()

        # 各欄位加總       
        total_data = get_details()
        total_amount = 0 
        total_refund_discount_amount = 0 
        total_audit_charge = 0 
        total_charge = 0 
        total_frozen_amount = 0 
        total_transfer_amount = 0 
        page_cnt = 1
        for i in range(len(total_data)):
            total_amount = total_data[i]["amount"] + total_amount
            total_refund_discount_amount = total_data[i]["refund_discount_amount"] + total_refund_discount_amount
            total_audit_charge = total_data[i]["audit_charge"] + total_audit_charge
            total_charge = total_data[i]["charge"] + total_charge 
            total_frozen_amount = total_data[i]["frozen_amount"] + total_frozen_amount
            total_transfer_amount = total_data[i]["transfer_amount"] + total_transfer_amount
        
            # 存當頁的 申請金額、扣除優惠、行政費用、手續費、凍結、應出
            this_page_amount = total_amount
            this_page_refund_discount_amount = total_refund_discount_amount
            this_page_expenditure = total_audit_charge + total_charge
            this_page_frozen_amount = total_frozen_amount
            this_page_transfer_amount = total_transfer_amount

            if (i+1)%500 == 0:
                break # 要抓取大於500筆 把break掉           
                page_cnt += 1
                if self.is_element_finded((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(page_cnt))):
                    self.click((By.XPATH, "//div[@class='pull-right']//a[text()='{:}']".format(page_cnt)))
                    self.wait_loading_finish()
                    total_data = get_details()

        # 小計資料整理
        sum_amount = self.get_text(WithdrawPageLocator.sub_sum_amount)
        sum_refund_discount_amount = self.get_text(WithdrawPageLocator.sum_refund_discount_amount)
        sum_charge = self.get_text(WithdrawPageLocator.sub_sum_charge)
        sum_frozen_amount = self.get_text(WithdrawPageLocator.sub_sum_frozen_amount)
        sum_transfer_amount = self.get_text(WithdrawPageLocator.sub_sum_transfer_amount)
        sum_amount = float((sum_amount).replace(',', ''))
        sum_refund_discount_amount = float((sum_refund_discount_amount).replace(',', ''))
        sum_charge = float((sum_charge).replace(',', ''))
        sum_frozen_amount = float((sum_frozen_amount).replace(',', ''))
        sum_transfer_amount = float((sum_transfer_amount).replace(',', ''))

        # 總計資料整理
        amount = self.get_text(WithdrawPageLocator.sum_amount)
        rund_discount_amount = self.get_text(WithdrawPageLocator.discount)
        charge = self.get_text(WithdrawPageLocator.sum_charge)
        frozen_amount = self.get_text(WithdrawPageLocator.sum_frozen_amount)
        transfer_amount = self.get_text(WithdrawPageLocator.sum_transfer_amount)
        amount = float((amount).replace(',', ''))
        rund_discount_amount = float((rund_discount_amount).replace(',', ''))
        charge = float((charge).replace(',',''))
        frozen_amount = float((frozen_amount).replace(',',''))
        transfer_amount = float((transfer_amount).replace(',',''))

        # 判斷小計資料是否相同
        assert round(this_page_amount, 2) == sum_amount, 'error number equal'
        assert round(this_page_refund_discount_amount, 2) == sum_refund_discount_amount, 'error number equal'
        assert round(this_page_expenditure, 2) == sum_charge, 'error number equal'
        assert round(this_page_frozen_amount, 2) == sum_frozen_amount, 'error number equal'
        assert round(this_page_transfer_amount, 2) == sum_transfer_amount, 'error number equal'

        # 判斷總計跟小計相同
        assert round(this_page_amount, 2) == amount, 'error number equal'
        assert round(this_page_refund_discount_amount, 2) == rund_discount_amount, 'error number equal'
        assert round(this_page_expenditure, 2) == charge, 'error number equal'
        assert round(this_page_frozen_amount, 2) == frozen_amount, 'error number equal'
        assert round(this_page_transfer_amount, 2) == transfer_amount, 'error number equal'
    
    # 申請金額查找
    def search_minamount(self):
        self.refresh_browser()
        self.type(WithdrawPageLocator.input_min_amount, "100")
        self.type(WithdrawPageLocator.input_max_amount, "300")
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 會員帳號查找
    def search_member(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(1)
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        
    
    # 出款卡號查找
    def search_cardnumber(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        bank_card = self.get_text(WithdrawPageLocator.bank_card)
        pattern = re.compile(r"\d+")   
        card_number = pattern.search(bank_card).group()
        self.refresh_browser()
        self.type(WithdrawPageLocator.input_card_number, card_number)
        self.sleep(1)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()

        
    # 錢包地址查找
    def search_walletaddress(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.find_element(WithdrawPageLocator.virtual_name), '上月記錄中沒有使用虛擬錢包方式出款'
        virtual_card = self.get_attribute(WithdrawPageLocator.virtual_card_copy, 'data-clipboard-text')
        self.refresh_browser()
        self.type(WithdrawPageLocator.input_wallet_address, virtual_card)
        self.sleep(1)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    

    # 自動刷新
    def check_autorefresh(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(WithdrawPageLocator.refresh_raido)
        self.type(WithdrawPageLocator.refresh_sec, "20")
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.sleep(5)
        self.click(WithdrawPageLocator.refresh_raido)
        assert self.is_element_finded(WithdrawPageLocator.add_time), '自動刷新查無資料'
    
    # 鎖定人員
    def check_locklogin(self, admin_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.type(WithdrawPageLocator.input_lock_login, admin_account)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 確定人員
    def check_auditlogin(self, admin_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.type(WithdrawPageLocator.input_audit_login, admin_account)
        self.click(WithdrawPageLocator.btn_today_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 股東/代理/總代
    def check_shareholder_generalagent_agent(self, shareholder, generalagent, agent):        
        self.refresh_browser()
        self.wait_loading_finish()
        # 股東
        self.sleep(0.5)
        self.type(WithdrawPageLocator.find_shareholder, shareholder)
        self.click(WithdrawPageLocator.btn_today_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        shareholder_cnt = self.get_text(WithdrawPageLocator.total_table)  # 股東筆數
        assert shareholder_cnt != 0, '股東筆數為0'

        # 總代
        self.type(WithdrawPageLocator.find_shareholder, "")
        self.sleep(1)
        self.type(WithdrawPageLocator.find_generalagent, generalagent)   
        self.click(WithdrawPageLocator.btn_search)                        
        self.wait_loading_finish()
        generalagent_cnt = self.get_text(WithdrawPageLocator.total_table) # 總代筆數
        assert generalagent_cnt != 0, '總代筆數為0'

        # 代理
        self.type(WithdrawPageLocator.find_generalagent, "")
        self.sleep(1)
        self.type(WithdrawPageLocator.find_agent, agent)                 
        self.click(WithdrawPageLocator.btn_search)                        
        self.wait_loading_finish()
        agent_cnt = self.get_text(WithdrawPageLocator.total_table)        # 代理筆數
        assert agent_cnt != 0, '代理筆數為0'
        assert shareholder_cnt == generalagent_cnt == agent_cnt, '股東、總代、代理 筆數不相符'
    
    # 層級
    def search_via_level(self):
        # 四級會員-無資料
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(1)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        # self.click(WithdrawPageLocator.member_level4)
        # self.click(WithdrawPageLocator.btn_search)
        # self.wait_loading_finish()
        # 先行comment, 推測為想找到空的資料所以選擇層級4然後定義說一定為空.......
        level_list = self.find_elements(WithdrawPageLocator.member_automated)
        for index in range(len(level_list)):
            if level_list[index].text == "automated_test":
                current_num = index+1
        current_level = r"//label[text()='会员级别']/..//input[@value='{0}']".format(current_num)
        current_level_xpath = (By.XPATH, current_level)
        self.click(current_level_xpath)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.get_text(WithdrawPageLocator.total_pages) == '0', '會員層級中不應該找到該會員'
        # assert self.get_text(WithdrawPageLocator.total_pages) == '0', '會員層級中不應該找到該會員'
        self.sleep(3)
        # self.click(WithdrawPageLocator.member_level4)

        # 一級&二級會員-有資料
        self.refresh_browser()
        self.click(WithdrawPageLocator.member_level1)
        self.click(WithdrawPageLocator.member_level2)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
    
    # 出款狀態
    def check_payout_status(self):
        # 已出款
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.status)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        for element in self.find_elements(WithdrawPageLocator.status_check):
            assert self.get_text_by_dom(element) == '已出款', '已出款搜尋錯誤'
        
        # 已取消
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.status_cancel)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        for element in self.find_elements(WithdrawPageLocator.status_check):
            assert self.get_text_by_dom(element) == '已取消', '已取消搜尋錯誤'
        
        # 已拒絕
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.status_reject)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        for element in self.find_elements(WithdrawPageLocator.status_check):
            assert self.get_text_by_dom(element) == '已拒绝', '已拒绝搜尋錯誤'
    
    # 下分總攬 
    def ledger_withdraw(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawPageLocator.input_member_account_general, web_account)
        self.click(WithdrawPageLocator.btn_today_withdraw_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.click(WithdrawPageLocator.downpage)
        self.click(WithdrawPageLocator.page_option)
        self.wait_loading_finish()
        self.scroll_to_top()        
        withdraw = self.get_text(WithdrawPageLocator.withdraw_check)
        assert withdraw == '出款申请', '下分總攬第一筆資料交易類別不為出款申请'
        self.click(WithdrawPageLocator.detail)
        self.switch_last_page()
        self.wait_loading_finish()
        self.sleep(2)
        assert self.is_element_finded(WithdrawPageLocator.rows) is True, '未自動查找，查無資料'
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.switch_home_page()

        # 確認資料
        for status_check in self.find_elements(WithdrawPageLocator.status_check):
            assert self.get_text_by_dom(status_check) == '已出款', '無此資料'

    # 備註操作
    def remark(self, web_account):
        self.refresh_browser()
        self.wait_loading_finish()
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.click(WithdrawPageLocator.remark)

        self.wait_alert_present()
        message = self.get_alert_message()
        assert str(message).__contains__('请输入新的备注')        
        self.sendkey_alert('測試')
        self.accept_alert()
        self.wait_loading_finish() 

    # 匯出
    def check_export_report(self, web_account, brand):
        self.refresh_browser()
        self.type(WithdrawPageLocator.input_member_account, web_account)
        self.sleep(1)
        self.click(WithdrawPageLocator.btn_last_month_application_datetime)
        self.click(WithdrawPageLocator.btn_search)
        self.wait_loading_finish()
        self.select_by_text(WithdrawPageLocator.page_list, '500')
        self.wait_loading_finish()
        # self.scroll_to_top()
        # self.sleep(0.5)
        self.click(WithdrawPageLocator.btn_export)
        self.click(WithdrawPageLocator.btn_export_comfirm)
        self.wait_loading_finish()

        time = self.find_elements(WithdrawPageLocator.add_time) # 申請時間
        level = self.find_elements(WithdrawPageLocator.level_name_list) # 層級
        member = self.find_elements(WithdrawPageLocator.member_login) # 會員
        agent = self.find_elements(WithdrawPageLocator.agent_list) # 代理
        generalagent = self.find_elements(WithdrawPageLocator.generalagent_list) # 總代
        shareholder = self.find_elements(WithdrawPageLocator.shareholder_list) # 股東
        warning = self.find_elements(WithdrawPageLocator.warning_list) # 異常信息
        apply_amount = self.find_elements(WithdrawPageLocator.apply_amount_list) # 申請金額
        discount_amount = self.find_elements(WithdrawPageLocator.discount_amount_list) # 扣除優惠
        administrative_costs = self.find_elements(WithdrawPageLocator.administrative_costs_list) # 行政费用
        withdrawal_procedures = self.find_elements(WithdrawPageLocator.withdrawal_procedures_list) # 出款手續
        frozen_amount = self.find_elements(WithdrawPageLocator.frozen_amount_list) # 凍結金額
        amount_due = self.find_elements(WithdrawPageLocator.amount_due_list) # 應出金額
        status = self.find_elements(WithdrawPageLocator.status_check) # 狀態
        lock_personnel = self.find_elements(WithdrawPageLocator.lock_personnel_list) # 锁定人员
        confirm_personnel = self.find_elements(WithdrawPageLocator.confirm_personnel_list) # 確認人员
        remark = self.find_elements(WithdrawPageLocator.remark) # 備註
        card_bank_name = self.find_elements(WithdrawPageLocator.card_bank_name_list) # 开户银行
        card_name = self.find_elements(WithdrawPageLocator.card_name_list) # 开户姓名
      

        time_list = []
        level_list = []
        member_list = []
        agent_list = []
        generalagent_list = []
        shareholder_list = []
        warning_list = []
        apply_amount_list = []
        discount_amount_list = []
        administrative_costs_list = []
        withdrawal_procedures_list = []
        frozen_amount_list= []
        amount_due_list = []
        status_list = []
        lock_personnel_list = []
        confirm_personnel_list = []
        remark_list = []
        index_range = len(self.find_elements(WithdrawPageLocator.add_time))
        excel_dict = self.read_excel(index_range, brand)
        bank_list = []

        # 獲得個欄位資料，放進list以便比較
        for idx in range(len(self.find_elements(WithdrawPageLocator.add_time))):
            time_list.append(self.get_text_by_dom(time[idx]))
            level_list.append(self.get_text_by_dom(level[idx]))
            member_list.append(self.get_text_by_dom(member[idx]))
            agent_list.append(self.get_text_by_dom(agent[idx]))
            generalagent_list.append(self.get_text_by_dom(generalagent[idx]))
            shareholder_list.append(self.get_text_by_dom(shareholder[idx]))
            # warning_list.append(self.get_text_by_dom(warning[idx]).replace('\n', '').replace('复制', '').replace('详细', ''))
            if "上次提款钱包地址" in self.get_text_by_dom(warning[idx]):
                warning_copy = (By.XPATH, f"(//div[@class='text-danger']/div[2]//button[contains(text(),'复制')])[{idx+1}]") # 異常信息 複製按鈕
                warning_message = "上次提款钱包地址：" + str(self.get_attribute(warning_copy, 'data-clipboard-text'))
                warning_list.append(warning_message)
            elif "上次提款卡号" in self.get_text_by_dom(warning[idx]):
                warning_copy = (By.XPATH, f"(//div[@class='text-danger']/div[2]//button[contains(text(),'复制')])[{idx+1}]") # 異常信息 複製按鈕
                warning_message = "上次提款卡号：" + str(self.get_attribute(warning_copy, 'data-clipboard-text'))
                warning_list.append(warning_message)
            else:
                warning_list.append(self.get_text_by_dom(warning[idx]).replace('\n', '').replace('复制', ''))

            apply_amount_list.append(float(self.get_text_by_dom(apply_amount[idx]).replace('申请金额: ', '')))
            discount_amount_list.append(float(self.get_text_by_dom(discount_amount[idx]).replace('扣除优惠: ', '')))
            administrative_costs_list.append(float(self.get_text_by_dom(administrative_costs[idx]).replace('行政费用: ', '')))
            withdrawal_procedures_list.append(float(self.get_text_by_dom(withdrawal_procedures[idx]).replace('出款手续: ', '')))
            frozen_amount_list.append(float(self.get_text_by_dom(frozen_amount[idx]).replace('冻结: ', '').replace(' RMB','')))
            amount_due_list.append(float(self.get_text_by_dom(amount_due[idx]).replace('应出: ', '').replace(' RMB','')))
            status_list.append(self.get_text_by_dom(status[idx]))
            lock_personnel_list.append(self.get_text_by_dom(lock_personnel[idx]).replace('锁定人员: ', ''))
            confirm_personnel_list.append(self.get_text_by_dom(confirm_personnel[idx]).replace('确认人员: ', ''))
            remark_list.append(self.get_text_by_dom(remark[idx]))
            if "开户银行" in self.get_text_by_dom(card_bank_name[idx]):
                bank_list.append(self.get_text_by_dom(card_bank_name[idx]).replace('开户银行: ', ''))
            else:
                bank_list.append(self.get_text_by_dom(card_bank_name[idx]).replace('钱包名称: ', ''))
            # bank_list.append(self.get_text_by_dom(card_bank_name[idx]).replace('开户银行: ', '') + ' ' + self.get_text_by_dom(card_name[idx]).replace('开户姓名: ', ''))

        assert excel_dict['申请时间(美東)'] == time_list, '申请时间錯誤'
        assert excel_dict['層級'] == level_list, '層級錯誤'
        assert excel_dict['会员'] == member_list, '会员錯誤'
        assert excel_dict['代理'] == agent_list, '代理錯誤'
        assert excel_dict['总代'] == generalagent_list, '總代錯誤'
        assert excel_dict['股东'] == shareholder_list, '股东錯誤'
        assert excel_dict['异常信息'] == warning_list, f'异常信息錯誤  \nexcel:{excel_dict["异常信息"]} \nlist:{warning_list}'
        assert excel_dict['申请金额'] == apply_amount_list, '申请金额錯誤'
        assert excel_dict['扣除优惠'] == discount_amount_list, '扣除优惠錯誤'
        assert excel_dict['行政费用'] == administrative_costs_list, '行政费用錯誤'
        assert excel_dict['出款手续'] == withdrawal_procedures_list, '出款手续錯誤'
        assert excel_dict['冻结金额'] == frozen_amount_list, '冻结金额錯誤'
        assert excel_dict['应出金额'] == amount_due_list, '应出金额錯誤'
        assert excel_dict['状态'] == status_list, '状态錯誤'
        assert excel_dict['锁定人员'] == lock_personnel_list, '锁定人员錯誤'
        assert excel_dict['确认人员'] == confirm_personnel_list, '确认人员錯誤'
        assert excel_dict['备注'] == remark_list, '备注錯誤'
        assert excel_dict['开户银行'] == bank_list, '開戶銀行錯誤'

        # 去\n 跟空白
        # for idx in range(len(excel_dict['银行信息'])):
        #     assert excel_dict['银行信息'][idx].replace('\n', '').replace(' ', '') == bank_list[idx].replace('\n', '').replace(' ', ''), '银行信息錯誤'
