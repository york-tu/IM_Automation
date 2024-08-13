from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from pages.admin.admin_basepage import BasePage
import datetime, re
import numpy as np

class OnlineDepositPageLocator(object):
    # SEARCH AREA (查找條件區)
    input_member_account = (By.XPATH, "//input[@qa-input='member_login']") # 輸入會員
    btn_today_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-today']")
    btn_yesterday_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-yestoday']")
    btn_this_week_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-thisWeek']")
    btn_last_week_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-lastWeek']")
    btn_this_month_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-thisMonth']")
    btn_last_month_application_datetime = (By.XPATH, "//label[contains(text(),'申請时间')]/..//button[@qa-button='quick-time-lastMonth']")
    btn_search = (By.XPATH, "//button[@qa-button='search']")
    status_ok = (By.XPATH,"//span[contains(text(),'已确认')]") # 確認狀態為已確認
    status_idle = (By.XPATH,"//span[contains(text(),'待确认')]") # 確認狀態為待確認
    btn_start_time = (By.XPATH, "//input[@placeholder='开始时间']") # 查找開始時間  
    btn_end_time = (By.XPATH, "//input[@placeholder='结束时间']") # 查找結束時間 
    application_search = (By.XPATH, "//input[@qa-input='id']") # 申請單號
    money_range_start = (By.XPATH,"//input[@qa-input='min_transfer_amount']") # 最低金額
    money_range_end = (By.XPATH,"//input[@qa-input='max_transfer_amount']") # 最高金額
    find_shareholder = (By.XPATH,"//input[@placeholder='股东列表']") # 股東
    find_generalagent = (By.XPATH,"//input[@qa-input='generalagent']") # 總代
    find_agent = (By.XPATH,"//input[@qa-input='agent']") # 代理
    member_level1 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '一级会员')]") # 一級會員
    member_level2 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '二级会员')]") # 二級會員
    member_level3 = (By.XPATH,"//label[text()='会员级别']//..//label[contains(. , '三级会员')]") # 三級會員
    export_btn = (By.XPATH, "//span[contains(text(),'汇出')]") # 匯出
    export_comfirm_btn = (By.XPATH, "//span[contains(text(),'确定')]")
    online_num_btn = (By.XPATH,"//div[@qa-select='merchant_id']//i") # 在線商號框
    online_num = (By.XPATH,"//div[@qa-select='merchant_id']//input") # 在線商號 輸入文字
    pay_sort_btn = (By.XPATH,"//div[@qa-select='payment_code']//i") # 支付方式框
    pay_sort = (By.XPATH,"//div[@qa-select='payment_code']//input") # 支付方式 輸入文字
    money_sort_btn = (By.XPATH,"//div[@qa-select='currency_code']//i") # 幣別框
    money_sort =  (By.XPATH,"//div[@qa-select='currency_code']//input") # 幣別 輸入文字
    button_down = (By.XPATH, "//i[@class='el-icon-arrow-down']")    # 條件展開
    
    def select_element(self,ele):
        return (By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//span[text()='%s']" % ele)

    # RESULT AREA (搜尋結果區)
    btn_pass = (By.XPATH, "(//button[@qa-button='accept'])[1]")
    btn_cancel = (By.XPATH, "(//button[@qa-button='reject'])[1]")
    btn_cancel_confirm = (By.XPATH, "//span[contains(text(),'确定取消')]")  # 二次彈窗提示 確定取消
    btn_second_confirm = (By.XPATH, "//a[@class='btn btn-xs btn-primary']")
    btn_second_cancel = (By.XPATH , "//a[@class='btn btn-xs btn-default']")
    tra_money = (By.XPATH, "//td[contains(@class,'el-table_1_column_12')]//span[1]")    # 轉帳信息(轉帳金額)
    handling_money = (By.XPATH,"//td[contains(@class,'el-table_1_column_12')]//span[2]")# 轉帳信息(轉帳手續費)
    offer_money = (By.XPATH, "//td[contains(@class,'el-table_1_column_12')]//span[3]")  # 轉帳信息(優惠金額))
    total_money = (By.XPATH, "//td[contains(@class,'el-table_1_column_11')]")           # 入賬總額
    ok_point_confirm_onlinedeposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[1])[1]")
    reject_point_confirm_onlinedeposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[1])[2]")
    idle_point_confirm_onlinedeposit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[1])[3]")
    application_num = (By.XPATH,"//td[contains(@class,'el-table_1_column_5')]") # 單號
    member_check = (By.XPATH,"//td[contains(@class,'el-table_1_column_3')]") # 確認會員欄位是否為空
    total_pages = (By.XPATH,"//li[contains(@class,'number')]") # 總頁數
    page_change = (By.XPATH, "//span[@class='el-pagination__sizes']")     # 每頁顯示筆數(點後會展開下拉選單)
    page_size_selected = (By.XPATH, "//li[contains(@class,'selected')]/span[contains(text(),'条/页')]") # 每頁最多顯示筆數 個別 (目前所選ex:100条/页)
    page_list = (By.XPATH, "//div[@class='el-select-dropdown el-popper' and not(contains(@style,'display: none'))]//span[contains(text(),'条/页')]") # 每頁最多筆數 總下拉式選單 (抓到4項ex:100条/页)
    def page_num(self, num):
        return (By.XPATH, f"(//span[contains(text(),'条/页')])[{num}]")
    last_page = (By.XPATH, '//a[text()="尾页"]')
    page_empty = (By.XPATH, "//span[@class='el-table__empty-text']") # 查無資料
    detail = (By.XPATH,"//button[@qa-button='last-operation']/span") # 明細
    operator_time = (By.XPATH,"(//td[contains(@class,'el-table_1_column_13')]//span[3])[1]") # 操作時間
    operator_info = (By.XPATH,"(//td[contains(@class,'el-table_1_column_13')]//span[2])[1]") # 操作者

    # 第一筆資料
    time = (By.XPATH, "(//td[contains(@class,'el-table_1_column_1 ')])[1]") # 申請時間
    level = (By.XPATH, "(//td[contains(@class,'el-table_1_column_2')])[1]") # 層級
    member_name = (By.XPATH, "(//td[contains(@class,'el-table_1_column_3')])[1]") # 會員
    agent = (By.XPATH, "(//td[contains(@class,'el-table_1_column_4')]//span[1])[1]") # 代理
    generalagent = (By.XPATH, "(//td[contains(@class,'el-table_1_column_4')]//span[2])[1]") # 總代
    shareholder = (By.XPATH, "(//td[contains(@class,'el-table_1_column_4')]//span[3])[1]") # 股東
    apply_number = (By.XPATH, "(//td[contains(@class,'el-table_1_column_5')])[1]") # 申請單號
    member_message = (By.XPATH,"(//td[contains(@class,'el-table_1_column_7')])[1]") # 在線商號
    pay_internet = (By.XPATH, "(//td[contains(@class,'el-table_1_column_8')])[1]") # 支付網關
    pay_style = (By.XPATH, "(//td[contains(@class,'el-table_1_column_9')])[1]") # 支付方式
    pay_money = (By.XPATH, "(//td[contains(@class,'el-table_1_column_11')])[1]") # 支付總額
    status = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[1])[1]") # 狀態
    operator_info = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[2])[1]") # 操作者
    operator_time = (By.XPATH, "(//td[contains(@class,'el-table_1_column_13')]//span[3])[1]") # 操作時間
    audit = (By.XPATH, "(//td[contains(@class,'el-table_1_column_14')])[1]") # 稽核
    pay_money = (By.XPATH, "(//td[contains(@class,'el-table_1_column_12')]//span[1])[1]") # 轉帳金額
    cancel_time = (By.XPATH, "(//td[contains(@class,'el-table_1_column_15')]/div)[1]") # 取消時間
    cancel_account = (By.XPATH, "(//td[contains(@class,'el-table_1_column_16')]/div)[1]") # 取消人員
    note = (By.XPATH, "(//td[contains(@class,'el-table_1_column_17')]/div)[1]") # 備注

    # 整頁資料
    time_list = (By.XPATH,"//td[@class='el-table_1_column_1 is-center' and @colspan='1']") # 申請時間
    level_list = (By.XPATH,               "//td[contains(@class,'el-table_1_column_2')]") # 層級
    member_name_list = (By.XPATH,         "//td[contains(@class,'el-table_1_column_3')]") # 會員
    agent_list = (By.XPATH,               "//td[contains(@class,'el-table_1_column_4')]//span[1]") # 代理
    generalagent_list = (By.XPATH,        "//td[contains(@class,'el-table_1_column_4')]//span[2]") # 總代
    shareholder_list = (By.XPATH,         "//td[contains(@class,'el-table_1_column_4')]//span[3]") # 股東
    apply_number_list = (By.XPATH,        "//td[contains(@class,'el-table_1_column_5')]") # 申請單號
    online_message_list = (By.XPATH,      "//td[contains(@class,'el-table_1_column_7')]") # 在線商號
    online_message_list_last = (By.XPATH, "(//span[@class='select2-match'])[last()]")  # 在線商號 下拉選單最後一個
    pay_internet_list = (By.XPATH,        "//td[contains(@class,'el-table_1_column_8')]") # 支付網關
    pay_style_list = (By.XPATH,           "//td[contains(@class,'el-table_1_column_9')]") # 支付方式
    currency_list = (By.XPATH,            "//td[contains(@class,'el-table_1_column_10')]") # 幣別
    pay_money_list = (By.XPATH,           "//td[contains(@class,'el-table_1_column_11')]") # 支付總額
    status_list = (By.XPATH,              "//td[contains(@class,'el-table_1_column_13')]//span[1]") # 狀態
    transfer_message_list =  (By.XPATH,   "//td[contains(@class,'el-table_1_column_12')]") # 轉帳信息
    audit_list = (By.XPATH,               "//td[contains(@class,'el-table_1_column_14')]") # 稽核
    rows = (By.XPATH,                     "//td[@colspan='1']/..") # 列
    detail = (By.XPATH,                   "//button[@qa-button='last-operation']/span") # 明細

    # otp彈窗
    otp_popup = (By.XPATH,"//div[@class='el-message-box']") # otp視窗
    otp_cancel = (By.XPATH,"//div[@class='el-message-box__btns']//span[contains(text(),'取消')]") # otp取消按鍵
    otp_ok = (By.XPATH,"//div[@class='el-message-box__btns']//span[contains(text(),'确定')]") # otp確定按鍵
    otp_title = (By.XPATH,"//span[contains(text(),'请输入运营OTP')]") # otp標題
    otp_input = (By.XPATH,"//div[@class='el-message-box__input']//input") # otp輸入框

    # 明細內容
    detail_windows = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']") # 明細視窗

    detail_application_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'申请单号')]") # 申請單號
    detail_application_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'申请单号')]/following-sibling::p[1]") 

    detail_accepttime_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'确认时间')]") # 確認時間
    detail_accepttime_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'确认时间')]/following-sibling::p[1]") 

    detail_acceptlogin_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'确认人员')]") # 確認人員
    detail_acceptlogin_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'确认人员')]/following-sibling::p[1]") 

    detail_transferauditrate_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'存款稽核倍数')]") # 存款稽核倍數
    detail_transferauditrate_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'存款稽核倍数')]/following-sibling::p[1]") 

    detail_transferauditdue_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'存款稽核放宽')]") # 存款稽核放寬
    detail_transferauditdue_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'存款稽核放宽')]/following-sibling::p[1]") 

    detail_transferauditcharge_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'行政费用比例')]") # 行政費用比例
    detail_transferauditcharge_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'行政费用比例')]/following-sibling::p[1]") 

    detail_discountauditrate_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠稽核倍数')]") # 優惠稽核倍數
    detail_discountauditrate_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠稽核倍数')]/following-sibling::p[1]") 

    detail_discountauditdue_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠稽核放宽')]") # 優惠稽核放寬
    detail_discountauditdue_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠稽核放宽')]/following-sibling::p[1]") 

    detail_discountname_title = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠名称')]") # 優惠名稱
    detail_discountname_info = (By.XPATH,"//div[@role='tooltip' and @aria-hidden='false']/strong[contains(text(),'优惠名称')]/following-sibling::p[1]") 

    # 整頁內容
    rows = (By.XPATH,"//td[@colspan='1']/..") # 列

    # 小計
    sub_total_table = (By.XPATH,"//span[contains(text(),'入账总额')]/span[1]")
    sub_amount = (By.XPATH,"//span[contains(text(),'转账金额')]/span[1]") # 轉帳小計
    sub_discount = (By.XPATH,"//span[contains(text(),'优惠金额')]/span[1]") # 優惠小計
    sub_charge = (By.XPATH,"//span[contains(text(),'转账手续费')]/span[1]") # 手續費小計

    # 總計  
    total_table = (By.XPATH,"//span[contains(text(),'入账总额')]/span[2]") # 儲值總計
    amount = (By.XPATH,"//span[contains(text(),'转账金额')]/span[2]") # 轉帳總計
    discount = (By.XPATH,"//span[contains(text(),'优惠金额')]/span[2]") # 優惠總計
    charge = (By.XPATH,"//span[contains(text(),'转账手续费')]/span[2]") # 手續費總計
    
    total_times = (By.XPATH,"//span[contains(text(),'总计')]") # 出款總次數 ex: 总计(3)

class OnlineDepositPage(BasePage):
    def search_today_deposit_by_member(self, account):
        self.type(OnlineDepositPageLocator.input_member_account, account)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

    def pass_first_deposit(self, admin_otp):
        for _ in range(1,4):
            if self.is_element_finded(OnlineDepositPageLocator.btn_pass) is True:
                self.click(OnlineDepositPageLocator.btn_pass)
                break
            
            #三方建單失敗，將自動壓拒絕，無法繼續操作入款流程
            elif self.get_text(OnlineDepositPageLocator.status) == '已拒绝':
                print('三方建單失敗，改為檢查失敗狀態...')
                assert self.get_text(OnlineDepositPageLocator.cancel_account) == '$auto', f'三方建單失敗，取消人員有誤'
                assert self.get_text(OnlineDepositPageLocator.note) == '三方建单失败', f'三方建單失敗，備注顯示有誤'
                assert self.get_text(OnlineDepositPageLocator.cancel_time) != '', f'三方建單失敗，未顯示取消時間'
                return False
            else:
                self.sleep(3)

        try:
            self.wait_visibility(OnlineDepositPageLocator.otp_popup)
            message = self.get_text(OnlineDepositPageLocator.otp_title)
        except:
            raise EOFError('沒出現輸入認證碼視窗')

        assert str(message).__contains__('请输入运营OTP'), "未顯示輸入OTP視窗"
        self.type(OnlineDepositPageLocator.otp_input,admin_otp)
        self.click(OnlineDepositPageLocator.otp_ok)
        self.wait_loading_finish()
        
        for _ in range(1,4):
            if self.wait_visibility_status(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit) is True:
                message_log = self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit)
                assert message_log == '已确认', f'{message_log}，後台出款異常'
                break               
            self.sleep(3)

        return True
        
    # 確認第三方件單失敗，會自動將狀態壓為已拒絕
    def check_deposit_auto_reject(self):
        for _ in range(1,4):
            if self.get_text(OnlineDepositPageLocator.status) == '已拒绝':
                assert self.get_text(OnlineDepositPageLocator.cancel_account) == '$auto', f'三方建單失敗，取消人員有誤'
                assert self.get_text(OnlineDepositPageLocator.note) == '三方建单失败', f'三方建單失敗，備注顯示有誤'
                assert self.get_text(OnlineDepositPageLocator.cancel_time) != '', f'三方建單失敗，未顯示取消時間'
                return False
            else:
                self.sleep(5)
                self.click(OnlineDepositPageLocator.btn_search)
        raise EOFError('第三方應建單失敗，後台狀態顯示有誤')


    def get_money_info(self, correct_money):
        tra_money = self.get_text(OnlineDepositPageLocator.tra_money).replace(',', '')
        offer_money = self.get_text(OnlineDepositPageLocator.offer_money).replace(',', '')
        total_money = self.get_text(OnlineDepositPageLocator.total_money).replace(',', '')
        handling_money = self.get_text(OnlineDepositPageLocator.handling_money).replace(',', '')

        tra_money = str(tra_money).lstrip('转账金额:')
        offer_money = str(offer_money).lstrip('优惠金额:')
        handling_money = str(handling_money).lstrip('转账手续费:')

        if offer_money == None or '' or 'null':
            offer_money = 0
        if handling_money == None or '' or 'null':
            handling_money = 0

        assert correct_money == tra_money, '前後台儲值金額顯示錯誤: 實際轉帳金額:%s 後臺轉帳金額: %s'%(correct_money, tra_money)
        return round(float(tra_money), 2), round(float(offer_money), 2), round(float(total_money), 2), round(float(handling_money), 2)


    def get_sum_info(self, reseller_account, time=''):
        self.type(OnlineDepositPageLocator.find_agent, reseller_account)
        # self.click(OnlineDepositPageLocator.btn_last_month_application_datetime) # 測試用

        if time == '':
            today_start = self.get_us_time().strftime("%Y-%m-%d 00:00")
            now = self.get_us_time().strftime("%M")
        
            if int(now) > 29 : # 確保遊戲報表能回來
                today_end = self.get_us_time().strftime("%Y-%m-%d %H:29")
            else:
                today_end = (self.get_us_time() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:29")
                
            self.type(OnlineDepositPageLocator.btn_start_time,today_start)  # 因每小時的30分會更新,故搜尋31-29分
            self.type(OnlineDepositPageLocator.btn_end_time,today_end)  
        elif time == '1':
            self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        elif time == '2':
            self.click(OnlineDepositPageLocator.btn_yesterday_application_datetime)
        elif time == '3':
            self.click(OnlineDepositPageLocator.btn_this_week_application_datetime)
        elif time == '4':
            self.click(OnlineDepositPageLocator.btn_last_week_application_datetime)
        elif time == '5':
            self.click(OnlineDepositPageLocator.btn_this_month_application_datetime)
        elif time == '6':
            self.click(OnlineDepositPageLocator.btn_last_month_application_datetime)

        self.click(OnlineDepositPageLocator.status_ok)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()
        self.sleep(3)
        
        if self.is_element_finded(OnlineDepositPageLocator.member_check) is False:
            online_record={
                'online_amount': "0.00",
                'online_discount': "0.00",
                'online_charge': "0.00",
                'online_total': "0",
            }
            return online_record
            
        online_amount = float(str(self.get_text(OnlineDepositPageLocator.amount)).replace(',', ''))
        online_discount = float(str(self.get_text(OnlineDepositPageLocator.discount)).replace(',', ''))
        online_charge = float(str(self.get_text(OnlineDepositPageLocator.charge)).replace(',', ''))
        online_total = float(str(self.get_text(OnlineDepositPageLocator.total_times)).replace(',', '')[3:-1])

        online_record={
            'online_amount': "%.2f"%online_amount,
            'online_discount': "%.2f"%online_discount,
            'online_charge': "%.2f"%online_charge,
            'online_total': online_total,
        }
        return online_record

    def online_deposit_status(self, admin_otp):
        if self.get_text(OnlineDepositPageLocator.status) == '待确认':
            for _ in range(1,4):
                if self.is_element_finded(OnlineDepositPageLocator.btn_pass) is True:
                    self.click(OnlineDepositPageLocator.btn_pass)
                    break
                else:
                    self.sleep(3)
            try:
                self.wait_visibility(OnlineDepositPageLocator.otp_popup)
                message = self.get_text(OnlineDepositPageLocator.otp_title)
            except:
                raise EOFError('沒出現輸入認證碼視窗')
        
            assert str(message).__contains__('请输入运营OTP'), "未顯示輸入OTP視窗"
            self.type(OnlineDepositPageLocator.otp_input,admin_otp)
            self.click(OnlineDepositPageLocator.otp_ok)
            self.wait_loading_finish()
        
            self.click(OnlineDepositPageLocator.btn_cancel)
            self.wait_loading_finish()
            self.click(OnlineDepositPageLocator.btn_cancel_confirm)
            self.wait_loading_finish()

            for _ in range(1,4):
                if self.wait_visibility_status(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit) is True:
                    message_log = self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit)
                    message_log_reject = self.get_text(OnlineDepositPageLocator.reject_point_confirm_onlinedeposit)
                    message_log_idle = self.get_text(OnlineDepositPageLocator.idle_point_confirm_onlinedeposit)
                    assert message_log == '已确认', f'{message_log}，後台出款異常'
                    assert message_log_reject == '已拒绝', f'{message_log_reject}，拒絕狀態不正確'
                    assert message_log_idle == '待确认', f'{message_log_idle}，待確認狀態不正確'
                    break               
                self.sleep(3)
        else:
            #三方建單失敗，將自動壓拒絕，無法繼續操作入款流程
            print('三方建單失敗，改為檢查失敗狀態...')
            message_log = self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit)
            message_log_reject = self.get_text(OnlineDepositPageLocator.reject_point_confirm_onlinedeposit)
            message_log_idle = self.get_text(OnlineDepositPageLocator.idle_point_confirm_onlinedeposit)
            assert message_log == '已拒绝', f'{message_log}，後台出款三方建單失敗，狀態未自動壓成拒絕'
            assert message_log_reject == '已拒绝', f'{message_log_reject}，後台出款三方建單失敗，狀態未自動壓成拒絕'
            assert message_log_idle == '已拒绝', f'{message_log_idle}，後台出款三方建單失敗，狀態未自動壓成拒絕'
            
            assert self.get_text(OnlineDepositPageLocator.cancel_account) == '$auto', f'三方建單失敗，取消人員有誤'
            assert self.get_text(OnlineDepositPageLocator.note) == '三方建单失败', f'三方建單失敗，備注顯示有誤'
            assert self.get_text(OnlineDepositPageLocator.cancel_time) != '', f'三方建單失敗，未顯示取消時間'
    

    def online_deposit_confirm_once(self, admin_otp):
        self.sleep(15)  # 待第三方建單失敗，自動拒絕
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        if self.get_text(OnlineDepositPageLocator.status) == '已拒绝':
            print('三方建單失敗，改為檢查失敗狀態...')
            assert self.get_text(OnlineDepositPageLocator.cancel_account) == '$auto', f'三方建單失敗，取消人員有誤'
            assert self.get_text(OnlineDepositPageLocator.note) == '三方建单失败', f'三方建單失敗，備注顯示有誤'
            assert self.get_text(OnlineDepositPageLocator.cancel_time) != '', f'三方建單失敗，未顯示取消時間'
            return False
        else:
            self.click(OnlineDepositPageLocator.btn_pass)

            try:
                self.wait_visibility(OnlineDepositPageLocator.otp_popup)
                message = self.get_text(OnlineDepositPageLocator.otp_title)
            except:
                raise EOFError('沒出現輸入認證碼視窗')

            assert str(message).__contains__('请输入运营OTP'), "未顯示輸入OTP視窗"
            self.type(OnlineDepositPageLocator.otp_input,admin_otp)
            self.click(OnlineDepositPageLocator.otp_ok)
            self.wait_loading_finish()

            message_log = self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit)
            assert message_log == '已确认', f'{message_log}，後台出款異常'
 
    # 會員帳號搜尋
    def search_via_member_name(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.input_member_account)
        self.type(OnlineDepositPageLocator.input_member_account, web_account)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        application_num = self.get_text(OnlineDepositPageLocator.application_num)
        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

        return application_num

    # 申請單號搜尋
    def search_via_application(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money, application_num):
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"     
        self.wait_visibility(OnlineDepositPageLocator.application_search)
        self.type(OnlineDepositPageLocator.application_search, application_num)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money,'已拒绝')
 

    # 在線商號搜尋
    def search_via_online_name(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        online_items = OnlineDepositPageLocator().select_element("自動市_京东支付") 
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.online_num_btn)
        self.click(OnlineDepositPageLocator.online_num_btn)
        self.type(OnlineDepositPageLocator.online_num,"自動市_京东支付")
        self.click(online_items)
        self.click(OnlineDepositPageLocator.online_num_btn)
        self.click(OnlineDepositPageLocator.btn_search)

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')
    
    # 支付網關
    def search_via_pay(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        online_gateway = OnlineDepositPageLocator().select_element("365支付网银") 
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.pay_sort_btn)
        self.click(OnlineDepositPageLocator.pay_sort_btn)
        self.sleep(3)
        self.type(OnlineDepositPageLocator.pay_sort, '365支付网银')
        self.click(online_gateway)
        self.click(OnlineDepositPageLocator.pay_sort_btn)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')
    
    # 幣別搜尋
    def search_via_currency(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        online_currency = OnlineDepositPageLocator().select_element("RMB | 人民币") 
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.money_sort_btn)
        self.click(OnlineDepositPageLocator.money_sort_btn)
        self.sleep(3)
        self.type(OnlineDepositPageLocator.money_sort, 'RMB | 人民币')
        self.click(online_currency)
        self.click(OnlineDepositPageLocator.money_sort_btn)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')
    
    # 金額範圍搜尋
    def search_via_money_range(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        # 金額範圍內無資料
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.input_member_account)
        self.type(OnlineDepositPageLocator.input_member_account, web_account)
        self.type(OnlineDepositPageLocator.money_range_start, 0)
        self.type(OnlineDepositPageLocator.money_range_end, 1)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.is_element_finded(OnlineDepositPageLocator.page_empty) == True, '取款範圍中不應該出現資料'

        # 金額範圍內有資料
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.type(OnlineDepositPageLocator.money_range_start, 299)
        self.type(OnlineDepositPageLocator.money_range_end, 305)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

    # 股東搜尋
    def search_via_shareholder(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.find_shareholder)
        self.type(OnlineDepositPageLocator.find_shareholder, shareholder)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

    # 總代搜尋
    def search_via_generalagent(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.find_generalagent)
        self.type(OnlineDepositPageLocator.find_generalagent, generalagent)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

    # 代理搜尋
    def search_via_agent(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.find_agent)
        self.type(OnlineDepositPageLocator.find_agent, agent)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

    # 層級搜尋
    def search_via_level(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        # 一級會員(無資料)
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.input_member_account)
        self.type(OnlineDepositPageLocator.input_member_account, web_account)
        self.click(OnlineDepositPageLocator.btn_today_application_datetime)
        self.click(OnlineDepositPageLocator.member_level3)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()
        assert self.is_element_finded(OnlineDepositPageLocator.page_empty) == True, '會員層級中不應該找到該會員'

        # 二級會員(有資料)
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.click(OnlineDepositPageLocator.member_level1)
        self.click(OnlineDepositPageLocator.member_level2)
        self.click(OnlineDepositPageLocator.member_level3)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()
        self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, '已拒绝')

    
    # 不同狀態測試
    def search_via_status(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
        plan = [OnlineDepositPageLocator.status_ok, OnlineDepositPageLocator.status_idle]
        message = ['已确认', '待确认']
        data = ['self.enter_ticket_info(admin_account)','self.idle_ticket_info(admin_account)']
        
        num= 0

        for status in plan:
            self.type(OnlineDepositPageLocator.input_member_account, web_account)
            self.click(OnlineDepositPageLocator.btn_today_application_datetime)
            self.click(status)
            self.click(OnlineDepositPageLocator.btn_search)
            self.wait_loading_finish()
            if self.is_element_finded(OnlineDepositPageLocator.page_empty):
                num += 1
                pass
            else:
                data[num]
                
                self.check_all_info(web_account, bank_name, admin_account, agent, generalagent, shareholder, money, message[num])
                num += 1
    
    # 已確認狀態 明細
    def enter_ticket_info(self,admin_account):
        self.click(OnlineDepositPageLocator.detail)
        assert self.wait_visibility_status(OnlineDepositPageLocator.detail_windows)
        assert self.get_text(OnlineDepositPageLocator.detail_accepttime_title) == '确认时间(美東)', "明細 '確認時間(美東)' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_accepttime_info) == self.get_text(OnlineDepositPageLocator.operator_time), "日期不正確"

        assert self.get_text(OnlineDepositPageLocator.detail_acceptlogin_title) == '确认人员', "明細 '確認人員' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_acceptlogin_info) == admin_account, "確認人員內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_transferauditrate_title) == '存款稽核倍数', "明細 '存款稽核倍数' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_transferauditrate_info) != '', "存款稽核倍数內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_transferauditdue_title) == '存款稽核放宽', "明細 '存款稽核放寬' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_transferauditdue_info) != '', "存款稽核放寬內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_transferauditcharge_title) == '行政费用比例', "明細 '行政费用比例' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_transferauditcharge_info) != '', "行政费用比例內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_discountauditrate_title) == '优惠稽核倍数', "明細 '优惠稽核倍数' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_discountauditrate_info) != '', "优惠稽核倍数內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_discountauditdue_title) == '优惠稽核放宽', "明細 '优惠稽核放寬' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_discountauditdue_info) != '', "优惠稽核放寬內容顯示異常"

        assert self.get_text(OnlineDepositPageLocator.detail_discountname_title) == '优惠名称', "明細 '優惠名稱' 顯示不正確"
        assert self.get_text(OnlineDepositPageLocator.detail_discountname_info) == '在線入款', "優惠名稱內容顯示異常"

    # 待確認狀態 明細
    def idle_ticket_info(self, admin_account):
        self.click(OnlineDepositPageLocator.detail)
        assert self.wait_visibility_status(OnlineDepositPageLocator.detail_windows)

    # 檢查各欄位名稱
    def check_all_info(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money, status=''):
        today = self.get_us_time().strftime("%Y-%m-%d")

        assert str(self.get_text(OnlineDepositPageLocator.time)).__contains__(today), '申請時間顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.level).__contains__('级会员'), '會員層級顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.member_name) == web_account, '會員名稱顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.agent) == agent, '代理名稱顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.generalagent) == generalagent, '總理名稱顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.shareholder) == shareholder, '股東名稱顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.member_message) == bank_name, '在線商號顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.pay_internet) == '365支付网银', '支付網關顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.tra_money) == '转账金额:' + money, '金額信息轉帳金額顯示不正確'
        assert self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit) == status, '狀態顯示不正確'

        if status =='已确认':
            assert self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit) == status, '狀態顯示不正確'
            assert self.get_text(OnlineDepositPageLocator.operator_info) == admin_account, '操作者顯示不正確'
            assert str(self.get_text(OnlineDepositPageLocator.operator_time)).__contains__(today), '操作時間顯示不正確'
        else:
            assert self.get_text(OnlineDepositPageLocator.ok_point_confirm_onlinedeposit) == status, '狀態顯示不正確'

        self.refresh_browser()
        self.wait_loading_finish()
        self.scroll_to_top()

    # 每頁最大筆數測試
    def page_range(self, web_account):
        self.type(OnlineDepositPageLocator.input_member_account, web_account)
        self.click(OnlineDepositPageLocator.btn_last_month_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.max_num_v2()

    # 所有查找方式
    def search_all(self, web_account, bank_name, admin_account, agent, generalagent, shareholder, money):
   
        application_num = self.search_via_member_name(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過會員帳號進行查找
        self.search_via_application(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money, application_num)  # 透過匯款姓名進行查找 
        self.search_via_online_name(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過自動刷新進行查找
        self.search_via_pay(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過操作者進行查找
        self.search_via_currency(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過操作者時間進行查找
        self.search_via_money_range(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過金額範圍進行查找
        self.search_via_shareholder(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過股東進行查找
        self.search_via_generalagent(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過總代進行查找
        self.search_via_agent(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過代理進行查找
        self.search_via_level(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過層級進行查找
        self.search_via_status(web_account, '自動市_京东支付', admin_account, agent, generalagent, shareholder, money)  # 透過狀態進行查找


    def subtotal_and_total(self, web_account):
        #入帳總額、轉帳信息(轉帳金額、轉帳手續費、優惠金額)
        check_list = [OnlineDepositPageLocator.total_money, OnlineDepositPageLocator.tra_money,OnlineDepositPageLocator.handling_money, OnlineDepositPageLocator.offer_money] # 金額信息三種金額
        check_name = ["totalMoney", "traMoney", "handlingmoney", "offermoney"] # 隨種類帶入變數
        check_subtotal = [OnlineDepositPageLocator.sub_total_table, OnlineDepositPageLocator.sub_amount, OnlineDepositPageLocator.sub_discount, OnlineDepositPageLocator.sub_charge] # 小計三種金額
        check_total = [OnlineDepositPageLocator.total_table, OnlineDepositPageLocator.amount, OnlineDepositPageLocator.discount, OnlineDepositPageLocator.charge] # 總計三種金額
        pages_size_max = []
        order = 0

        # 上月查找 -> 轉換為"當天"查找
        assert self.is_element_finded(OnlineDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(OnlineDepositPageLocator.btn_last_month_application_datetime)
        self.type(OnlineDepositPageLocator.input_member_account, web_account)
        self.click(OnlineDepositPageLocator.btn_last_month_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        # 抓出該頁面最多筆數選擇
        self.click(OnlineDepositPageLocator.page_change)
        self.wait_visibility(OnlineDepositPageLocator.page_list)
        for quantity_loop in self.find_elements(OnlineDepositPageLocator.page_list):
            num = self.get_text_by_dom(quantity_loop)
            pages_size_max.append(num[:-3])
        self.click(OnlineDepositPageLocator.page_change)
        # length = len(self.find_elements(OnlineDepositPageLocator.page_size_selected))

        # 每一種上限筆數測試
        for style_loop in range(0, len(pages_size_max)):
            self.click(OnlineDepositPageLocator.page_change)
            self.wait_visibility(OnlineDepositPageLocator.page_list)
            self.click(OnlineDepositPageLocator.page_num(self, style_loop+1))
            self.wait_loading_finish()

            # max_pages = pages_size_max[style_loop] 
            total_pages = len(self.find_elements(OnlineDepositPageLocator.total_pages))
            order = 0

            # 轉帳 & 優惠 & 入賬 根據顯示欄位加總
            for detail_type_loop in check_list:
                total_sum = 0
                sub_total = 0
                
                # 各種金額欄位總數金額加總
                for money in self.find_elements(detail_type_loop):
                    try:
                        check_name[order] = float((self.get_text_by_dom(money).split(':'))[1])
                        total_sum = total_sum + check_name[order]
                    except:
                        check_name[order] = float(self.get_text_by_dom(money).replace(',', ''))
                        total_sum = total_sum + check_name[order]

          
                total_sum = "{0:.2f}".format(total_sum)
              
                # 抓取小計金額 
                sub_total = float(self.get_text(check_subtotal[order]).split(":")[0].replace(',', ''))
                sub_total = "{0:.2f}".format(sub_total)

                assert sub_total == total_sum , '小計與列表加總後金額不相符 列相加:{0} 小計:{1}'.format(sub_total, total_sum)

                # 比較小計與總計
                sub_total_table = float(self.get_text(check_subtotal[order]).split(":")[0].replace(',', ''))
                total_table = float(self.get_text(check_total[order]).split(":")[0].replace(',', ''))

                if (int(total_pages) <= 1) or (sub_total_table ==0.00 and total_table ==0.00):
                    assert  sub_total_table == total_table, '總計 & 小計加總後金額不相符 小計:{0} 總計:{1}'.format(sub_total_table, total_table)
                # else:   # 因不只確認轉帳金額，有多頁時不一定會不相同，故將此行隱藏
                #     assert  sub_total_table != total_table , '小計加總後金額不應該相同 小計:\n{0} \n總計:\n{1}'.format(sub_total_table, total_table)

                order += 1

        self.refresh_browser()
        self.wait_loading_finish()

    def check_pages(self):
        self.click(OnlineDepositPageLocator.btn_last_month_application_datetime)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        self.check_page() 
        self.scroll_to_top()

    def check_export_report(self, brand):
        self.click(OnlineDepositPageLocator.btn_last_month_application_datetime)
        self.click(OnlineDepositPageLocator.status_ok)
        self.click(OnlineDepositPageLocator.btn_search)
        self.wait_loading_finish()

        # 設定每頁顯示上限最高
        page_size_selected = self.find_elements(OnlineDepositPageLocator.page_size_selected)
        num = self.get_text_by_dom(page_size_selected[-1]) # 每一頁顯示數量選擇按鈕
        self.select_by_text(OnlineDepositPageLocator.page_list, num)
        self.wait_loading_finish()
        
        # 匯出
        self.scroll_to_top()
        self.click(OnlineDepositPageLocator.export_btn)
        self.wait_visibility(OnlineDepositPageLocator.export_comfirm_btn)
        self.click(OnlineDepositPageLocator.export_comfirm_btn)

        title_name = [
                     OnlineDepositPageLocator.time_list,
                     OnlineDepositPageLocator.level_list,
                     OnlineDepositPageLocator.member_name_list,
                     OnlineDepositPageLocator.agent_list,
                     OnlineDepositPageLocator.generalagent_list,
                     OnlineDepositPageLocator.shareholder_list,
                     OnlineDepositPageLocator.apply_number_list,
                     OnlineDepositPageLocator.online_message_list,
                     OnlineDepositPageLocator.pay_internet_list,
                     OnlineDepositPageLocator.currency_list,
                     OnlineDepositPageLocator.pay_money_list,
                    #  OnlineDepositPageLocator.transfer_message_list,
                     OnlineDepositPageLocator.status_list,
                     OnlineDepositPageLocator.audit_list,
                     ]

        # info = ['申请时间(美東)','层级','帐号','代理','总代','股东','申請单号','在线商号','支付网关','币别','入账总额','转账信息','确认状态','稽核状态'] # 轉帳信息有問題
        info = ['申请时间(美東)', '层级', '帐号', '代理', '总代', '股东', '申請单号', '在线商号', '支付网关', '币别', '入账总额', '确认状态', '稽核状态']  
        data = {}
        num = 0

        # 取出Web資料內容
        for loop in title_name:
            data_list = []

            if loop == OnlineDepositPageLocator.pay_money_list:
                for loops in self.find_elements(loop):
                    message = str(self.get_text_by_dom(loops)).replace(",", "")
                    message = float(message)
                    data_list.append(message)
            else:
                for loops in self.find_elements(loop):
                    message = str(self.get_text_by_dom(loops)).replace(': ', ':')

                    # 某些品牌匯出檔案會自動帶入.0,與pm確認中
                    # if str(locals()['loop']).__contains__('depositamount'):
                    #     if not message.__contains__('.'):
                    #         message = str(float(message))

                    data_list.append(message)
                    
            data.setdefault(info[num], data_list)
            num += 1

        report = self.read_excel(500, brand) # 將Excel資料整理進來
        
        # 字串整理
        # to_string = np.array(report['入账总额'], dtype=str) # 將list全部轉為str型態
        to_string = np.array(report['入账总额'], dtype=float) # 將list全部轉為float型態
        money_message_arrange_report = {'入账总额': to_string}
        report.update(money_message_arrange_report)

        # money_message_arrange_report = {'转账信息' : self.arrange_data(report['转账信息'])}
        # report.update(money_message_arrange_report)
        
        # money_message_arrange_data = {'转账信息' : self.arrange_data(data['转账信息'])}
        # data.update(money_message_arrange_data)

        # Excel 與 Web 資料比對
        for loop in info:
            assert np.all(report[loop] == data[loop]) == True, "\n類別: \n{0} \nReport: \n{1} \nData: \n{2}".format(loop,report[loop],data[loop])

    # 整理文字
    def arrange_data(self, list):
        message_list = []

        
        # 將文字與數字分開
        for loop in list:
            message = re.split(r'\n|:', loop)
            
            for text in message:
                if text == '':
                    message.remove('')

            message_list.append(message)
            

        # message_list = np.array(message_list,dtype=str)
        # 給予小數點後兩位
        # for Arrange_i in range(0, len(message_list)):
        #     for Arrange_j in range(0, len(message_list[Arrange_i])):
    
        #         if Arrange_j % 2 == 1:
        #             message_list[Arrange_i][Arrange_j] = "{0:.2f}".format(float(message_list[Arrange_i][Arrange_j]))

        return message_list

    # 取得第一筆資料的轉帳金額
    def get_pay_money(self, web_account):
        self.wait_loading_finish()
        self.search_today_deposit_by_member(web_account)

        assert self.wait_visibility_status(OnlineDepositPageLocator.detail) is True, "在線入款無轉帳資料"

        return str('%.2f' %float(self.get_text(OnlineDepositPageLocator.pay_money).replace('转账金额:', '').replace(',', '')))