from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime,re

class CompanyDepositPageLocator(object):
    # SEARCH AREA (查找條件區)
    input_member_account = (By.XPATH, "//input[@qa-input='member_login']")
    btn_today_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-today'])[1]")
    btn_yesterday_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-yestoday'])[1]")
    btn_this_week_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-thisWeek'])[1]")    
    btn_last_week_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-lastWeek'])[1]")
    btn_this_month_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-thisMonth'])[1]")
    btn_last_month_application_datetime = (By.XPATH, "(//button[@qa-button='quick-time-lastMonth'])[1]")
    btn_today_operator_datetime = (By.XPATH, "(//button[@qa-button='quick-time-today'])[2]")
    btn_search = (By.XPATH, "//button[@qa-button='search']")
    status_ok = (By.XPATH, "//label[@role='radio']/span[text()='已确认']") # 確認狀態為已確認
    status_cancel = (By.XPATH, "//label[@role='radio']/span[text()='已取消']") # 確認狀態為已取消
    status_idle= (By.XPATH, "//label[@role='radio']/span[text()='待确认']") # 確認狀態為待確認
    btn_time_submit = (By.XPATH, "//button[contains(@class,'el-picker-panel__link-btn')]/span[contains(text(),'确定')]") # 查找時間選擇框確定 
    btn_start_time = (By.XPATH, "//div[@qa-date-picker='added-time']/input[@class='el-range-input'][1]") # 查找申請開始時間  
    btn_end_time = (By.XPATH, "//div[@qa-date-picker='added-time']/input[@class='el-range-input'][2]") # 查找申請結束時間 
    btn_start_time_operator = (By.XPATH, "//div[@qa-date-picker='transfer-time']/input[@class='el-range-input'][1]") # 查找操作開始時間  
    btn_end_time_operator = (By.XPATH, "//div[@qa-date-picker='transfer-time']/input[@class='el-range-input'][2]") # 查找操作結束時間 
    card_name = (By.XPATH, "//input[@qa-input='card_names']") # 匯款姓名
    ledger = (By.XPATH, "//input[@qa-input='deposit_id']") # 流水號
    refresh_raido = (By.XPATH, "//label[@qa-checkbox='interval-auto']") # 自動刷新開關
    refresh_sec = (By.XPATH, "//input[@qa-input='interval-time']") # 自動刷新秒數
    bank_card_number = (By.XPATH, "//div[@qa-select='account_numbers']//input[@class='el-input__inner']") # 銀行卡號
    operator = (By.XPATH, "//input[@qa-input='accept_login']") # 操作人員
    money_range_start = (By.XPATH, "//input[@qa-input='min_transfer_amount']") # 轉帳金額從
    money_range_end = (By.XPATH, "//input[@qa-input='max_transfer_amount']") # 轉帳金額至
    find_shareholder = (By.XPATH, "//div[@qa-select='sharelogin']//input[@class='el-input__inner']") # 股東
    find_generalagent = (By.XPATH, "//input[@qa-input='generalagent']") # 總代
    find_agent = (By.XPATH, "//input[@qa-input='agent']") # 代理
    member_level1 = (By.XPATH, "//label[@qa-checkbox='levelcode'][1]") # 一級會員
    member_level2 = (By.XPATH, "//label[@qa-checkbox='levelcode'][2]") # 二級會員
    member_level3 = (By.XPATH, "//label[@qa-checkbox='levelcode'][3]") # 三級會員
    export_btn = (By.XPATH, "//button[@qa-button='export']") # 匯出
    export_comfirm_btn = (By.XPATH, "//div[@class='el-popconfirm__action']//span[contains(text(),'确定')]")
    button_down = (By.XPATH, "//i[@class='el-icon-arrow-down']")    # 條件展開

    # RESULT AREA (搜尋結果區)
    btn_pass = (By.XPATH, "(//button[@qa-button='accept'])[1]")
    btn_cancel = (By.XPATH, "(//button[@qa-button='reject'])[1]")
    btn_second_confirm = (By.XPATH, "//div[@class='el-message-box__btns']//span[contains(text(),'确定')]")      # 二次彈窗-確定
    btn_second_cancel = (By.XPATH , "//div[@class='el-message-box__btns']//span[contains(text(),'取消')]")      # 二次彈窗-取消
    ok_point_confirm_deposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_11 is-center')])[1]")       # 第一筆狀態 確認狀態
    reject_point_confirm_deposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_11 is-center')])[2]")   # 第二筆狀態 拒絕狀態
    idle_point_confirm_deposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_11 is-center')])[3]")     # 第三筆狀態 待確認狀態
    tra_money = (By.XPATH, "//p[contains(text(),'转账: ')]/span") # 轉帳
    offer_money = (By.XPATH, "//p[contains(text(),'优惠: ')]/span") # 優惠
    total_money = (By.XPATH, "//p[contains(text(),'入账: ')]/span") # 入帳
    total_pages = (By.XPATH, "//span[@class='el-pagination__total']") # 總筆數 共_條
    pages_num = (By.XPATH, "//li[contains(@class,'number')]") # 總頁數
    page_size = (By.XPATH, "//div[@class='page-content-wrapper']/*//tfoot/*//select/option") # 每頁最多顯示筆數 個別
    page_list = (By.XPATH, "//div[@class='el-select-dropdown el-popper' and not(contains(@style,'display: none'))]//span[contains(text(),'条/页')]") # 每頁最多筆數 總下拉式選單 (抓到4項ex:100条/页)
    def page_num(self, num):
        return (By.XPATH, f"(//span[contains(text(),'条/页')])[{num}]")
    last_page = (By.XPATH, '//a[text()="尾页"]')

    page_change = (By.XPATH, "//span[@class='el-pagination__sizes']")     # 每頁顯示筆數
    page_size_last = (By.XPATH, "(//span[contains(text(),'条/页')])[last()]")   # 每頁顯示筆數 最後的項目


    # 第一筆資料
    time = (By.XPATH, "//p[text()='申请时间：']/span") # 申請時間
    level = (By.XPATH, "(//td[contains(@class,'el-table_1_column_2')]//span)[1]") # 層級
    member_name = (By.XPATH, "(//a[@qa-a='member_login'])[1]") # 會員
    agent = (By.XPATH, "(//td[contains(@class,'el-table_1_column_3')]//span)[1]")     # 代理
    generalagent = (By.XPATH, "(//p[contains(text(),'总代:')]/span)[last()]")   # 總代(明細內) 
    shareholder = (By.XPATH, "(//p[contains(text(),'股东:')]/span)[last()]")    # 股東(明細內)
    bank_message = (By.XPATH, "(//td[contains(@class,'el-table_1_column_5 is-center')]//p[2])[1]") # 收款信息
    member_message = (By.XPATH, "(//td[contains(@class,'el-table_1_column_7 is-center')]//p[1])[1]") # 會員匯款信息 
    operator_info = (By.XPATH, "(//p[contains(text(),'确认人员')]/span)[1]") # 確認人員
    operator_time = (By.XPATH, "(//p[contains(text(),'确认时间')]/span)[1]") # 确认时间
    detail_button = (By.XPATH, "(//button[@qa-button='detail'])[1]") # 明細按鈕
    pay_money = (By.XPATH, "(//p[contains(text(),'转账: ')]/span)[1]") # 轉帳金額

    # 整頁資料
    time_list = (By.XPATH, "//p[contains(text(),'申请时间')]/span") # 申請時間
    level_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_2')]//span") # 層級  (多總計&小計)
    member_name_list = (By.XPATH, "//a[@qa-a='member_login']") # 會員
    agent_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_3')]//span") # 代理  (多總計&小計)
    generalagent_list = (By.XPATH, "//p[contains(text(),'总代:')]/span") # 總代
    shareholder_list = (By.XPATH, "//p[contains(text(),'股东:')]/span") # 股東
    bank_message_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_5 is-center')]//p[2]") # 收款信息       (多總計&小計)
    # Excel Table變換, 定位添加，目前皆無資料可定位，故以下四個皆暫時相同
    paymentname_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_4')]") # 網關支付 (網關支付/ 備用網關支付)
    paymentname_backup_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_4')]") # 備用網關支付
    merchantname_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_4')]") # 關聯商號 (關聯商號/ 備用關聯商號)
    merchantname_backup_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_4')]") # 備用關聯商號
    # currency_list = (By.XPATH, "") # 幣別 **目前admin無該欄位, 但匯出時的excel有
    account_bank_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_5')]//p[1]") # 收款銀行名稱             (多總計&小計)
    account_name_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_5')]//p[2]") # 收款戶名(收款帳戶名稱)    (多總計&小計)
    account_number_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_5')]//p[3]") # 收款卡號               (多總計&小計)
    # account_bank_status_list = (By.XPATH, "") # 收款銀行狀態 **目前admin無該欄位, 但匯出時的excel有
    card_bank_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_7')]//p[1]") # 匯款銀行名稱
    card_name_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_7')]//p[2]") # 匯款帳戶名稱
    card_transfer_method_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_7')]//p[4]") # 匯款方式
    card_number_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_7')]//p[3]") # 匯款卡號/ 交易單號
    card_transfer_time_list = (By.XPATH, "(//p[contains(text(),'总代:')]/../../../td[2])[last()]") # 匯款到款時間   (明細內)
    transfer_money_list = (By.XPATH, "//span[contains(text(),'小计')]/../../../preceding-sibling::tr//p[contains(text(),'转账: ')]/span")           # 轉帳金額
    discountamount_money_list = (By.XPATH, "//span[contains(text(),'小计')]/../../../preceding-sibling::tr//p[contains(text(),'优惠: ')]/span")     # 優惠金額
    transfer_in_money_list = (By.XPATH, "//span[contains(text(),'小计')]/../../../preceding-sibling::tr//p[contains(text(),'入账:')]/span")         # 入账金額
    status_list = (By.XPATH, "//td[contains(@class,'el-table_1_column_11')]")       # 狀態          (多總計&小計)
    confirm_member_list = (By.XPATH, "//p[contains(text(),'确认人员')]/span")   # 確認人員
    confirm_time_list = (By.XPATH, "//p[contains(text(),'确认时间')]/span")     # 確認時間
    

    member_message_list = (By.XPATH, "//span[contains(@data-bind,'cardname')]/..") # 會員匯款信息 
    rows = (By.XPATH, "//div[contains(@class,'portlet-body')]/table/tbody[@data-bind='foreach: items']/tr[not(@data-bind)]") # 列
    detail = (By.XPATH, "//a[@class='btn default btn-xs green-stripe' and contains(text(),'明细')]") # 明細
    detail_buttons = (By.XPATH, "//button[text()='明细']") # 明細按鈕

    # 明細內容
    detail_windows = (By.XPATH, "//div[@class='popover-content']") # 明細視窗
    detail_accept_time_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'accepttime')]") # 確認時間
    detail_accept_time_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'accepttime')]") 

    detail_accept_login_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'acceptlogin')]") # 確認人員
    detail_accept_login_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'acceptlogin')]") 

    detail_transfer_auditrate_title = (By.XPATH, "//div[@class='popover-content']//dt[text()='存款稽核倍数']") # 存款稽核倍數
    detail_transfer_auditrate_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'transferauditrate')]") 

    detail_transfer_auditdue_title = (By.XPATH, "//div[@class='popover-content']//dt[text()='存款稽核放宽']") # 存款稽核放寬
    detail_transfer_auditdue_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'transferauditdue')]") 

    detail_transfer_auditcharge_title = (By.XPATH, "//div[@class='popover-content']//dt[text()='行政费用比例']") # 行政費用比例
    detail_transfer_auditcharge_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'transferauditcharge')]") 

    detail_discount_auditrate_title = (By.XPATH, "//div[@class='popover-content']//dt[text()='优惠稽核倍数']") # 優惠稽核倍數
    detail_discount_auditrate_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'discountauditrate')]") 

    detail_discount_auditdue_title = (By.XPATH, "//div[@class='popover-content']//dt[text()='优惠稽核放宽']") # 優惠稽核放寬
    detail_discount_auditdue_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'discountauditdue')]") 

    detail_discount_name_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'discountname')]") # 優惠名稱
    detail_discount_name_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'discountname')]") 

    detail_audit_time_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'audittime')]") # 稽核時間
    detail_audit_time_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'audittime')]") 

    detail_audit_login_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'auditlogin')]") # 稽核人員 
    detail_audit_login_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'auditlogin')]") 
    
    detail_withdraw_id_title = (By.XPATH, "//div[@class='popover-content']//dt[contains(@data-bind,'withdrawid')]") # 關聯提款
    detail_withdraw_id_info = (By.XPATH, "//div[@class='popover-content']//dd[contains(@data-bind,'withdrawid')]") 

    # 備註
    note_btn = (By.XPATH, "//button[@qa-button='remark']") # 備註按鈕
    note_info = (By.XPATH, "//div[@class='el-popover el-popper' and @aria-hidden='false']/img") # 備註內容
    

    # 排序
    added_time_sort = (By.XPATH, "//a[contains(@data-bind,'addedtime')]") # 申請時間排序
    levelcode_sort = (By.XPATH, "//a[contains(@data-bind,'levelcode')]") # 層級排序
    memberlogin_sort = (By.XPATH, "//a[contains(@data-bind,'memberlogin')]") # 會員排序
    agent_sort = (By.XPATH, "//a[contains(@data-bind,'agent')]") # 代理排序
    generalagent_sort = (By.XPATH, "//a[contains(@data-bind,'generalagent')]") # 總代排序
    sharelogin_sort = (By.XPATH, "//a[contains(@data-bind,'sharelogin')]") # 股東排序
    accountnumber_sort = (By.XPATH, "//a[contains(@data-bind,'accountnumber')]") # 收款信息排序
    cardnumber_sort = (By.XPATH, "//a[contains(@data-bind,'cardnumber')]") # 會員匯款信息排序
    depositamount_sort = (By.XPATH, "//a[contains(@data-bind,'depositamount')]") # 金額信息排序
    status_sort = (By.XPATH, "//a[contains(@data-bind,'status')]") # 確認狀態排序
    acceptlogin_sort = (By.XPATH, "//a[contains(@data-bind,'acceptlogin')]") # 操作者排序
    accepttime_sort = (By.XPATH, "//a[contains(@data-bind,'accepttime')]") # 操作時間排序

    # 小計
    # sub_total_table = (By.XPATH, "//span[text()='小计']/following::span[contains(@data-bind,'subdeposit')]") # 新版行未使用
    sub_amount = (By.XPATH, "//span[contains(text(),'小计')]/../../..//p[contains(text(),'转账:')]/span") # 轉帳小計
    sub_discount = (By.XPATH, "//span[contains(text(),'小计')]/../../..//p[contains(text(),'优惠:')]/span") # 優惠小計
    sub_charge = (By.XPATH, "//span[contains(text(),'小计')]/../../..//p[contains(text(),'入账:')]/span") # 入賬小計

    # 總計  
    # total_table = (By.XPATH, "//span[text()='总计']/following::span[contains(@data-bind,'deposit')]") # 新版行未使用
    amount = (By.XPATH, "//span[contains(text(),'总计')]/../../..//p[contains(text(),'转账:')]/span") # 轉帳總計
    discount = (By.XPATH, "//span[contains(text(),'总计')]/../../..//p[contains(text(),'优惠:')]/span") # 優惠總計
    charge = (By.XPATH, "//span[contains(text(),'总计')]/../../..//p[contains(text(),'入账:')]/span") # 入賬總計
    total = (By.XPATH, "//span[contains(text(),'总计')]") # 儲值總計筆數


class CompanyDepositPage(BasePage):
    def search_today_deposit_by_member(self, account):
        self.type(CompanyDepositPageLocator.input_member_account, account)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

    def pass_first_deposit(self):
        for _ in range(1,4):
            if self.is_element_finded(CompanyDepositPageLocator.btn_pass) is True:
                self.click(CompanyDepositPageLocator.btn_pass)
                self.sleep(1)
                break
            else:
                self.sleep(3)            
        
        self.wait_visibility(CompanyDepositPageLocator.btn_second_confirm)
        self.click(CompanyDepositPageLocator.btn_second_confirm)
        self.wait_loading_finish()
        
        for _ in range(1,4):
            if self.is_element_finded(CompanyDepositPageLocator.ok_point_confirm_deposit) is True:
                message = self.get_text(CompanyDepositPageLocator.ok_point_confirm_deposit)
                assert message == "已确认", f'{message}，後台出款異常'
                break
            self.sleep(3)

    def get_money_info(self, correct_money):
        tra_money = self.get_text(CompanyDepositPageLocator.tra_money).replace(',', '')
        offer_money = self.get_text(CompanyDepositPageLocator.offer_money).replace(',', '')
        total_money = self.get_text(CompanyDepositPageLocator.total_money).replace(',', '')

        if offer_money == None or '' or 'null':
            offer_money = 0

        correct_money = format(float(correct_money), '.2f') # 前台爬取的金額保留兩位小數

        assert correct_money == tra_money, '前後台儲值金額顯示錯誤 前台:%s 後台:%s' %(correct_money, tra_money)
        return round(float(tra_money), 2), round(float(offer_money), 2), round(float(total_money), 2)

    # 抓取時段間的注單,須配合報表更新時間
    def get_sum_info(self, reseller_account, time=''):
        self.type(CompanyDepositPageLocator.find_agent, reseller_account)
        # self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)  # 測試用

        if time == '':
            today_start = self.get_us_time().strftime("%Y-%m-%d 00:00")
            now = self.get_us_time().strftime("%M")
        
            if int(now) > 29 : # 確保遊戲報表能回來
                today_end = self.get_us_time().strftime("%Y-%m-%d %H:29")
            else:
                today_end = (self.get_us_time() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:29")

            self.type(CompanyDepositPageLocator.btn_start_time, today_start)  # 因每小時的30分會更新,故搜尋31-29分
            self.type(CompanyDepositPageLocator.btn_end_time, today_end)
            self.click(CompanyDepositPageLocator.btn_time_submit)
        elif time == '1':
            self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        elif time == '2':
            self.click(CompanyDepositPageLocator.btn_yesterday_application_datetime)
        elif time == '3':
            self.click(CompanyDepositPageLocator.btn_this_week_application_datetime)
        elif time == '4':
            self.click(CompanyDepositPageLocator.btn_last_week_application_datetime)
        elif time == '5':
            self.click(CompanyDepositPageLocator.btn_this_month_application_datetime)
        elif time == '6':
            self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)

        self.click(CompanyDepositPageLocator.status_ok)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()
        self.sleep(3)
        
        if self.is_element_finded(CompanyDepositPageLocator.member_name) is False:
            company_record = {
                'company_amount': "0.00",
                'company_discount': "0.00",
                'company_deposit': "0.00",
                'company_total': "0",
            }
            return company_record

        company_amount = float(str(self.get_text(CompanyDepositPageLocator.amount)).replace(',', ''))
        company_discount = float(str(self.get_text(CompanyDepositPageLocator.discount)).replace(',', ''))
        company_deposit = float(str(self.get_text(CompanyDepositPageLocator.charge)).replace(',', ''))
        company_total = float(re.sub('\D+','',(str(self.get_text(CompanyDepositPageLocator.total)))))

        company_record = {
            'company_amount':"%.2f" %company_amount,
            'company_discount':"%.2f" %company_discount,
            'company_deposit': "%.2f" %company_deposit,
            'company_total': "%.2f" %company_total,
        }
        return company_record

    # 狀態確認
    def company_deposit_status(self):
        for _ in range(1,4):
            if self.is_element_finded(CompanyDepositPageLocator.btn_pass) is True:
                self.click(CompanyDepositPageLocator.btn_pass)
                break
            else:
                self.sleep(3)            

        self.wait_visibility(CompanyDepositPageLocator.btn_second_confirm)
        self.click(CompanyDepositPageLocator.btn_second_confirm)
        self.wait_loading_finish()
        self.wait_visibility(CompanyDepositPageLocator.btn_cancel)
        self.click(CompanyDepositPageLocator.btn_cancel)
        self.wait_visibility(CompanyDepositPageLocator.btn_second_confirm)
        self.click(CompanyDepositPageLocator.btn_second_confirm)
        self.wait_loading_finish()

        for _ in range(0,3):
            if self.wait_visibility_status(CompanyDepositPageLocator.ok_point_confirm_deposit) is True:
                message_log = self.get_text(CompanyDepositPageLocator.ok_point_confirm_deposit)
                message_log_reject = self.get_text(CompanyDepositPageLocator.reject_point_confirm_deposit)
                message_log_idle = self.get_text(CompanyDepositPageLocator.idle_point_confirm_deposit)
                assert message_log == '已确认', f'{message_log}，後台出款異常'
                assert message_log_reject == '已取消', f'{message_log_reject}，拒絕狀態不正確'
                assert message_log_idle == '待确认', f'{message_log_idle}，待確認狀態不正確'
            self.sleep(3)

    # 會員帳號搜尋
    def search_via_member_name(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 匯款姓名搜尋
    def search_via_transfer_name(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.card_name, bank_name[2])
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 自動刷新搜尋
    def search_via_auto_reflash(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.refresh_sec, 5)
        self.click(CompanyDepositPageLocator.refresh_raido)
        self.click(CompanyDepositPageLocator.btn_search)
        self.sleep(10)
        while True:
            try:
                assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
                self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
                self.click(CompanyDepositPageLocator.refresh_raido)
                break
            except:
                pass
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')
    
    # 操作人員搜尋
    def search_via_operator(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        self.type(CompanyDepositPageLocator.operator, admin_account)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')
    
    # 操作時間搜尋
    def search_via_operator_datetime(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_operator_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_today_operator_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')
    
    # 金額範圍搜尋
    def search_via_money_range(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        # 金額範圍內無資料
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.money_range_start)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.type(CompanyDepositPageLocator.money_range_start, 0)
        self.type(CompanyDepositPageLocator.money_range_end, 1)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.get_text(CompanyDepositPageLocator.total_pages)[2:-2] == '0', '取款範圍中不應該出現資料'

        # 金額範圍內有資料
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.money_range_start)
        self.type(CompanyDepositPageLocator.money_range_start, 299)
        self.type(CompanyDepositPageLocator.money_range_end, 305)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 股東搜尋
    def search_via_shareholder(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.find_shareholder, shareholder)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 總代搜尋
    def search_via_generalagent(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.find_generalagent, generalagent)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 代理搜尋
    def search_via_agent(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.find_agent, agent)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 層級搜尋
    def search_via_level(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        # 一級會員(無資料)
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_today_application_datetime)
        self.click(CompanyDepositPageLocator.member_level3)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.get_text(CompanyDepositPageLocator.total_pages)[2:-2] == '0', '會員層級中不應該找到該會員'

        # 二級會員(有資料)
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.member_level1)
        self.click(CompanyDepositPageLocator.member_level3) # 取消勾選
        self.click(CompanyDepositPageLocator.member_level1)
        self.click(CompanyDepositPageLocator.member_level2)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()
        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已确认')

    # 不同狀態測試
    def search_via_status(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        plan = [CompanyDepositPageLocator.status_ok, CompanyDepositPageLocator.status_cancel, CompanyDepositPageLocator.status_idle]
        message = ['已确认', '已取消', '待确认']
        data = ['self.enter_ticket_info(admin_account)', 'self.reject_ticket_info(admin_account)', 'self.idle_ticket_info(admin_account)']
        
        num = 0

        for status in plan:
            assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
            self.wait_visibility(CompanyDepositPageLocator.btn_today_application_datetime)
            self.type(CompanyDepositPageLocator.input_member_account, web_account)
            self.click(CompanyDepositPageLocator.btn_today_application_datetime)
            self.click(status)
            self.click(CompanyDepositPageLocator.btn_search)
            self.wait_loading_finish()
            data[num]
            
            self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, message[num])
            num += 1

    # 明細
    def enter_ticket_info(self, admin_account):
        self.click(CompanyDepositPageLocator.detail)
        assert self.wait_visibility_status(CompanyDepositPageLocator.detail_windows)
        assert self.get_text(CompanyDepositPageLocator.detail_accept_time_title) == '确认时间(美東)', "明細 '確認時間(美東)' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_accept_time_info) == self.get_text(CompanyDepositPageLocator.operator_time), "日期不正確"

        assert self.get_text(CompanyDepositPageLocator.detail_accept_login_title) == '确认人员', "明細 '確認人員' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_accept_login_info) == admin_account, "確認人員內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditrate_title) == '存款稽核倍数', "明細 '存款稽核倍数' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditrate_info) != '', "存款稽核倍数內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditdue_title) == '存款稽核放宽', "明細 '存款稽核放寬' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditdue_info) != '', "存款稽核放寬內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditcharge_title) == '行政费用比例', "明細 '行政费用比例' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_transfer_auditcharge_info) != '', "行政费用比例內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_discount_auditrate_title) == '优惠稽核倍数', "明細 '优惠稽核倍数' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_discount_auditrate_info) != '', "优惠稽核倍数內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_discount_auditdue_title) == '优惠稽核放宽', "明細 '优惠稽核放寬' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_discount_auditdue_info) != '', "优惠稽核放寬內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_discount_name_title) == '优惠名称', "明細 '優惠名稱' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_discount_name_info) == '公司入款', "優惠名稱內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_audit_time_title) == '稽核时间(美東)', "明細 '稽核时间(美東)' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_audit_time_info) == self.get_text(CompanyDepositPageLocator.operator_time), "稽核時間不正確"

        assert self.get_text(CompanyDepositPageLocator.detail_audit_login_title) == '稽核人员', "明細 '稽核人员' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_audit_login_info) == admin_account, "稽核人员內容顯示異常"

        assert self.get_text(CompanyDepositPageLocator.detail_withdraw_id_title) == '关联提款', "明細 '關聯提款' 顯示不正確"
        assert self.get_text(CompanyDepositPageLocator.detail_withdraw_id_info) != '', "關聯提款內容顯示異常"
    
    def reject_ticket_info(self, admin_account):
        self.click(CompanyDepositPageLocator.detail)
        assert self.wait_visibility_status(CompanyDepositPageLocator.detail_windows)

    def idle_ticket_info(self, admin_account):
        self.click(CompanyDepositPageLocator.detail)
        assert self.wait_visibility_status(CompanyDepositPageLocator.detail_windows)


    # 檢查各欄位名稱
    def check_all_info(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money, status=''):
        self.sleep(1)
        today = self.get_us_time().strftime("%Y-%m-%d")
        self.wait_loading_finish()
        self.wait_visibility(CompanyDepositPageLocator.member_name)
        # 展開第一筆資料的明細頁面
        # assert self.is_element_finded(CompanyDepositPageLocator.detail_button) == True, "明細BTN不存在"
        assert self.wait_visibility_status(CompanyDepositPageLocator.detail_button) == True, "明細BTN未顯示"
        self.click(CompanyDepositPageLocator.detail_button)
        self.sleep(1)
        self.wait_visibility(CompanyDepositPageLocator.generalagent)

        assert str(self.get_text(CompanyDepositPageLocator.time)).__contains__(today), '申請時間顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.level).__contains__('级会员'), '會員層級顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.member_name) == web_account, '會員名稱顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.agent) == agent, '代理名稱顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.generalagent) == generalagent, '總理名稱顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.shareholder) == shareholder, '股東名稱顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.bank_message) == bank_name[0], '收款信息戶名顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.member_message) == bank_name[1], '會員匯款信息戶名顯示不正確'
        assert self.get_text(CompanyDepositPageLocator.pay_money)[:-3] == money, '金額信息轉帳金額顯示不正確'
        
        if status == '已确认':
            assert self.get_text(CompanyDepositPageLocator.ok_point_confirm_deposit) == status, '狀態顯示不正確'
            assert self.get_text(CompanyDepositPageLocator.operator_info) == admin_account, '操作者顯示不正確'
            assert str(self.get_text(CompanyDepositPageLocator.operator_time)).__contains__(today), '操作時間顯示不正確'
        else:
            assert self.get_text(CompanyDepositPageLocator.ok_point_confirm_deposit) == status, '狀態顯示不正確'
            
        self.click(CompanyDepositPageLocator.note_btn)
    
        if self.wait_visibility_status(CompanyDepositPageLocator.note_info) is True:
            pass
        else:
            raise EOFError('點擊備註內容錯誤')

        self.refresh_browser()
        self.wait_loading_finish()
        self.scroll_to_top()

    # 所有查找方式
    def search_all(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
   
        self.search_via_member_name(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過會員帳號進行查找
        # self.search_via_transfer_name(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過匯款姓名進行查找 
        # self.search_via_auto_reflash(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過自動刷新進行查找
        # self.search_via_operator(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過操作者進行查找
        self.search_via_operator_datetime(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過操作者時間進行查找
        self.search_via_money_range(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過金額範圍進行查找
        self.search_via_shareholder(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過股東進行查找
        self.search_via_generalagent(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過總代進行查找
        self.search_via_agent(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過代理進行查找
        self.search_via_level(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過層級進行查找
        self.search_via_status(web_account, ['支付寶轉帳自動測試', '支付宝', "機器人測試"], admin_account, agent, generalagent, shareholder, money)  # 透過狀態進行查找

    # 排序比對
    def set_sort(self, button, data):
        sort_list = []
        sort_list_reverse = []

        length = len(self.find_elements(CompanyDepositPageLocator.page_size)) - 1
        self.select_by_index(CompanyDepositPageLocator.page_list, length)
        self.wait_loading_finish()
        self.scroll_to_top()
        self.click(button)
        self.wait_loading_finish()

        for loop in self.find_elements(data):
            sort_list.append(self.get_text_by_dom(loop))

        self.click(button)
        self.wait_loading_finish()
        
        for loop in self.find_elements(data):
            sort_list_reverse.append(self.get_text_by_dom(loop))

        assert len(sort_list) == len(sort_list_reverse), "排序前後長度不一致  排序方法1 長度:{0}  排序方法2 長度:{1}".format(len(sort_list), len(sort_list_reverse))


        if sort_list == sort_list_reverse:
            for loop in range(0,len(sort_list)):
                assert sort_list[loop] == sort_list_reverse[loop], ("排序相反後資料不正確: 排序方法1: {0} \n排序方法2: {1} ".format(sort_list[loop], sort_list_reverse[loop]))
        else:
            sort_list_reverse.reverse()
            for loop in range(0,len(sort_list)):
                assert sort_list[loop] == sort_list_reverse[loop], ("排序相反後資料不正確: \n排序方法1:\n {0} \n排序方法2:\n {1} ".format(sort_list[loop], sort_list_reverse[loop]))

    # 所有排序測試
    def other_sort(self, web_account):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()
        lists = []
        for loop in self.find_elements(CompanyDepositPageLocator.rows):
            lists.append(loop)

        self.set_sort(CompanyDepositPageLocator.added_time_sort, CompanyDepositPageLocator.rows)  # 申請時間排序測試
        self.set_sort(CompanyDepositPageLocator.levelcode_sort, CompanyDepositPageLocator.rows)  # 層級排序測試
        self.set_sort(CompanyDepositPageLocator.memberlogin_sort, CompanyDepositPageLocator.rows)  # 會員排序測試
        self.set_sort(CompanyDepositPageLocator.agent_sort, CompanyDepositPageLocator.rows)  # 代理排序測試
        self.set_sort(CompanyDepositPageLocator.generalagent_sort, CompanyDepositPageLocator.rows)  # 總代排序測試
        self.set_sort(CompanyDepositPageLocator.sharelogin_sort, CompanyDepositPageLocator.rows)  # 股東排序測試
        self.set_sort(CompanyDepositPageLocator.accountnumber_sort, CompanyDepositPageLocator.rows)  # 收款信息排序測試
        self.set_sort(CompanyDepositPageLocator.cardnumber_sort, CompanyDepositPageLocator.rows)  # 會員匯款信息排序測試
        self.set_sort(CompanyDepositPageLocator.depositamount_sort, CompanyDepositPageLocator.rows)  # 金額信息排序測試
        self.set_sort(CompanyDepositPageLocator.status_sort, CompanyDepositPageLocator.rows)  # 確認狀態排序測試
        self.set_sort(CompanyDepositPageLocator.acceptlogin_sort, CompanyDepositPageLocator.rows)  # 操作者排序測試
        self.set_sort(CompanyDepositPageLocator.accepttime_sort, CompanyDepositPageLocator.rows)  # 操作時間排序測試

        self.refresh_browser()
    
    # 每頁最大筆數測試
    def page_range(self, web_account):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num_v2()

    def subtotal_and_total(self, web_account):
        # 轉帳 & 優惠 & 入賬
        check_list = [CompanyDepositPageLocator.transfer_money_list, CompanyDepositPageLocator.discountamount_money_list, CompanyDepositPageLocator.transfer_in_money_list] # 金額信息三種金額
        check_name = ["tra_money", "offer_money", "total_money"] # 隨種類帶入變數
        check_subtotal = [CompanyDepositPageLocator.sub_amount, CompanyDepositPageLocator.sub_discount, CompanyDepositPageLocator.sub_charge] # 小計三種金額
        check_total = [CompanyDepositPageLocator.amount, CompanyDepositPageLocator.discount, CompanyDepositPageLocator.charge] # 總計三種金額
        pages_size_max = []
        order = 0

        # 上月查找
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.type(CompanyDepositPageLocator.input_member_account, web_account)
        self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        # 抓出該頁面最多筆數選擇
        self.click(CompanyDepositPageLocator.page_change)
        self.wait_visibility(CompanyDepositPageLocator.page_list)
        for quantity_loop in self.find_elements(CompanyDepositPageLocator.page_list):
            num =self.get_text_by_dom(quantity_loop)
            pages_size_max.append(num[:-3])
        self.click(CompanyDepositPageLocator.page_change)
        # length = len(self.find_elements(CompanyDepositPageLocator.page_size))

        # 每一種上限筆數測試
        for style_loop in range(0, len(pages_size_max)):
            self.click(CompanyDepositPageLocator.page_change)
            self.wait_visibility(CompanyDepositPageLocator.page_list)
            self.click(CompanyDepositPageLocator.page_num(self, style_loop+1))
            self.wait_loading_finish()

            # max_pages = int(pages_size_max[style_loop]) 
            total_pages = len(self.find_elements(CompanyDepositPageLocator.pages_num))
            order = 0

            # 轉帳 & 優惠 & 入賬 根據顯示欄位加總
            for detail_type_loop in check_list:
                _sum = 0
                sub_total = 0
                
                # 各種金額欄位總數金額加總
                for money in self.find_elements(detail_type_loop):
                    try:
                        check_name[order] = float(self.get_text_by_dom(money).replace(',', ''))
                        _sum = _sum + check_name[order]
                    except:
                        pass
                _sum = "{0:.2f}".format(_sum)
                
                # 抓取小計金額 
                sub_total = float(self.get_text(check_subtotal[order]).split(":")[0].replace(',', ''))
                sub_total = "{0:.2f}".format(sub_total)

                assert sub_total == _sum, '小計與列表加總後金額不相符 列相加:{0} 小計:{1}'.format(sub_total, _sum)

                # 比較小計與總計
                sub_total_table = float(self.get_text(check_subtotal[order]).split(":")[0].replace(',', ''))
                total_table = float(self.get_text(check_total[order]).split(":")[0].replace(',', ''))

                if (int(total_pages) <= 1) or (sub_total_table ==0.00 and total_table ==0.00):
                    assert  sub_total_table == total_table, '總計 & 小計加總後金額不相符 小計:{0} 總計:{1}'.format(sub_total_table, total_table)
                # else:     # 因不只確認轉帳金額，有多頁時不一定會不相同，故將此行隱藏
                #     assert  sub_total_table != total_table, '小計加總後金額不應該相同 小計:\n{0} \n總計:\n{1}'.format(sub_total_table, total_table)

                order += 1
        self.refresh_browser()
        self.wait_loading_finish()
        self.scroll_to_top()


    def check_pages(self):
        self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_page() 
        self.scroll_to_top()

    def check_export_report(self, brand):
        assert self.is_element_finded(CompanyDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.btn_last_month_application_datetime)
        self.click(CompanyDepositPageLocator.status_ok)
        self.click(CompanyDepositPageLocator.btn_search)
        self.wait_loading_finish()

        # 設定每頁顯示上限最高
        # page_size = self.find_elements(CompanyDepositPageLocator.page_size)
        # num = self.get_text_by_dom(page_size[-1]) # 每一頁顯示數量選擇按鈕
        # self.select_by_text(CompanyDepositPageLocator.page_list, num)
        # self.wait_loading_finish()

        self.click(CompanyDepositPageLocator.page_change)
        self.wait_visibility(CompanyDepositPageLocator.page_size_last)
        self.click(CompanyDepositPageLocator.page_size_last)
        self.wait_loading_finish()
        
        # 展開每一個ROW的detail page
        for detail_button in self.find_elements(CompanyDepositPageLocator.detail_buttons):
            self.click_by_dom(detail_button)
            for _ in range(0, 10):
                if detail_button.get_attribute('aria-expanded') == 'true':
                    break
                else:
                    self.click_by_dom(detail_button)

        # 匯出
        self.scroll_to_top()
        self.click(CompanyDepositPageLocator.export_btn)
        self.wait_visibility(CompanyDepositPageLocator.export_comfirm_btn)
        self.click(CompanyDepositPageLocator.export_comfirm_btn)

        title_name = [
                        CompanyDepositPageLocator.time_list,
                        CompanyDepositPageLocator.level_list,
                        CompanyDepositPageLocator.member_name_list,
                        CompanyDepositPageLocator.agent_list,
                        CompanyDepositPageLocator.generalagent_list,
                        CompanyDepositPageLocator.shareholder_list,
                        #  CompanyDepositPageLocator.bank_message_list,
                        CompanyDepositPageLocator.paymentname_list,
                        CompanyDepositPageLocator.merchantname_list,
                        CompanyDepositPageLocator.paymentname_backup_list,
                        CompanyDepositPageLocator.merchantname_backup_list,
                        CompanyDepositPageLocator.account_bank_list,
                        CompanyDepositPageLocator.account_name_list,
                        CompanyDepositPageLocator.account_number_list,
                        CompanyDepositPageLocator.card_bank_list,
                        CompanyDepositPageLocator.card_name_list,
                        CompanyDepositPageLocator.card_transfer_method_list,
                        CompanyDepositPageLocator.card_number_list,
                        CompanyDepositPageLocator.card_transfer_time_list,
                        CompanyDepositPageLocator.transfer_money_list,
                        CompanyDepositPageLocator.discountamount_money_list,
                        CompanyDepositPageLocator.status_list,
                        CompanyDepositPageLocator.confirm_member_list,
                        CompanyDepositPageLocator.confirm_time_list,
                    ]

        '''会员汇款信息 有問題'''
        info = [
                    '申请时间(美東)',
                    '层级', 
                    '会员', 
                    '代理', 
                    '总代', 
                    '股东', 
                    '支付网关', 
                    '关联商号', 
                    '备用支付网关', 
                    '备用关联商号', 
                    '收款银行',
                    '收款户名',
                    '收款卡号',
                    '汇款银行',
                    '汇款户名',
                    '汇款方式',
                    '汇款卡号/交易单号',
                    '汇款到款时间',
                    '转账金额',
                    '优惠金额',
                    '确认',
                    '确认人员',
                    '确认时间(美東)'
                ] 

        data = {}
        num = 0

        self.un_zip(brand)
        report = self.read_excel(500, brand) # 將Excel資料整理進來
        self.sleep(1)

        # 取出Web資料內容
        for loop in title_name:
            need_sort_list = []
            data_list = []
            # 多算總計與小計
            if (loop== CompanyDepositPageLocator.level_list or loop == CompanyDepositPageLocator.agent_list or loop == CompanyDepositPageLocator.bank_message_list or 
                        loop == CompanyDepositPageLocator.account_bank_list or loop == CompanyDepositPageLocator.account_name_list or loop == CompanyDepositPageLocator.account_number_list or
                        loop == CompanyDepositPageLocator.transfer_money_list or loop == CompanyDepositPageLocator.discountamount_money_list or loop == CompanyDepositPageLocator.status_list) :
                for loops in self.find_elements(loop):
                    message = str(self.get_text_by_dom(loops))
                    # 處理多帶欄位名稱
                    if message!='':
                        need_sort_list.append(message)
            elif (loop== CompanyDepositPageLocator.generalagent_list or loop == CompanyDepositPageLocator.shareholder_list) :
                for loops in self.find_elements(loop):
                    message = str(self.get_text_by_dom(loops))
                    # 處理多帶欄位名稱
                    if message!='':
                        need_sort_list.append(message)
            # 改二代前
            # if loop == CompanyDepositPageLocator.paymentname_list or loop == CompanyDepositPageLocator.merchantname_list:
            #     for loops in self.find_elements(loop):
            #         message = str(self.get_text_by_dom(loops))
            #         # 處理多帶欄位名稱
            #         if message!='':
            #             message = message[message.find("：")+1:]
            #         need_sort_list.append(message)
            # elif loop == CompanyDepositPageLocator.paymentname_backup_list or loop == CompanyDepositPageLocator.merchantname_backup_list:
            #     for loops in self.find_elements(loop):
            #         message = str(self.get_text_by_dom(loops))
            #         if message!='':
            #             message=message[message.find("：")+1:]
            #         data_list.append(message)
            # elif loop == CompanyDepositPageLocator.transfer_money_list or loop == CompanyDepositPageLocator.discountamount_money_list:
            #     for loops in self.find_elements(loop):
            #         message = str(self.get_text_by_dom(loops)).replace(",", "")
            #         message = float(message)
            #         data_list.append(message)
            
            else:
                for loops in self.find_elements(loop):
                    message = str(self.get_text_by_dom(loops))
                    data_list.append(message)

            if len(need_sort_list) > 0:
                data_list = need_sort_list[::2]
            # if num == 6:
            #     count = len(self.find_elements(CompanyDepositPageLocator.bank_name))
            #     for ele in range(0, count):
            #        message = str(self.get_text_by_dom(self.find_elements(CompanyDepositPageLocator.bank_name)[ele])).replace(': ', ':').replace('：',':') + ' ' + str(self.get_text_by_dom(self.find_elements(CompanyDepositPageLocator.account_name)[ele])).replace(': ', ':').replace('：',':')

            #        list.append(message)
            # elif num == 7:
            #     count = len(self.find_elements(CompanyDepositPageLocator.card_bank_name))
            #     for ele in range(0, count):
            #        message = str(self.get_text_by_dom(self.find_elements(CompanyDepositPageLocator.card_bank_name)[ele])).replace(': ', ':').replace('：',':') + ' ' + str(self.get_text_by_dom(self.find_elements(CompanyDepositPageLocator.card_name)[ele])).replace(': ', ':').replace('：',':')

            #        list.append(message)
            # elif num == 8 or num == 9:
            #     for loops in self.find_elements(loop):
            #         message = float((self.get_text_by_dom(loops)).replace(': ', ':').replace('：',':').replace(',', ''))

            #         list.append(message)
            # else:
            #     for loops in self.find_elements(loop):
            #         message = str(self.get_text_by_dom(loops)).replace(': ', ':').replace('：',':')
                    
            #         if '转账' in message:
            #             if '优惠' not in message:
            #                 message = message.replace('入账:', '优惠:0.00\n入账:')

            #         list.append(message)
                
            data.setdefault(info[num], data_list)
            num += 1
        
        
        # 字串整理
        # Bank_message_arrange_report = {'收款信息' : self.arrange_data(report['收款信息'], '收款信息')}
        # report.update(Bank_message_arrange_report)
        # Bank_message_arrange_data = {'收款信息' : self.arrange_data(data['收款信息'], '收款信息')}
        # data.update(Bank_message_arrange_data)
        # Member_message_arrange_report = {'汇款信息' : self.arrange_data(report['汇款信息'], '汇款信息')}
        # report.update(Member_message_arrange_report)
        # Member_message_arrange_data = {'汇款信息' : self.arrange_data(data['汇款信息'], '汇款信息')}
        # data.update(Member_message_arrange_data)
    
        # Excel 與 Web 資料比對
        for loop in info:
            # if loop == '会员汇款信息':
            #     continue
            # if loop == '转账金额' or loop == '优惠金额':
            #     report[loop] = list(map(str, report[loop]))
            assert report[loop] == data[loop], "\n類別: \n{0} \nReport: \n{1} \nData: \n{2}".format(loop, report[loop], data[loop])
        
    # 整理文字
    def arrange_data(self, list, info):
        message_list = []

        # 將文字與數字分開
        if info == '金额信息':
            for loop in list:
                loop = loop.replace(',', '')
                message = re.split(r'\n|:', loop)
                
                for text in message:
                    if text == '':
                        message.remove('')

                message_list.append(message)
        elif info == '收款信息':
            for loop in list:
                message = loop.replace('银行:', '').replace('户名:', '').replace('卡号:', '').replace('\n', ' ')

                message_list.append(message)
        elif info == '汇款信息':
            for loop in list:
                message = loop.replace('银行:', '').replace('户名:', '').replace('卡号:', '').replace('\n', ' ')

                message_list.append(message)

        return message_list

    # 取得第一筆資料的轉帳金額
    def get_pay_money(self, web_account):
        self.wait_loading_finish()
        self.search_today_deposit_by_member(web_account)

        assert (self.is_element_finded(CompanyDepositPageLocator.time) == True and self.is_element_finded(CompanyDepositPageLocator.member_name) == True), "公司入款無任何資料顯示"

        self.wait_visibility(CompanyDepositPageLocator.detail_button)
        
        money = self.get_text(CompanyDepositPageLocator.pay_money).replace(',', '')
        return money