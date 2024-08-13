import datetime
import re
import copy
import pandas as pd
import os
import time
import getpass
import pyautogui
import platform

from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


def logged(func):
    def with_logging(*args, **kwargs):
        # print(func.__name__ + "  was called")
        return (func(*args, **kwargs))
    return with_logging

class ArtificialDepositPageLocator:
    # 系統時間(美東)
    system_time = (By.XPATH, "//span[contains(@data-bind, 'text: currentTime')]")

    # mandeposit tab mandeposit
    mandeposit_mandeposit = (By.XPATH, "//div[@id='tab-tab-man-deposit' and text()='人工存入']")    # 人工存入
    mandeposit_group = (By.XPATH, "//div[@id='tab-tab-group' and text()='款项审核']")               # 款項審核
    newadd_oneadd = (By.XPATH, "//button[@qa-button='add']")            # 新增
    newadd_batchadd = (By.XPATH, "//button[@qa-button='batch-add']")    # 批次新增
    button_down = (By.XPATH, "//div[@style='']//i[@class='el-icon-arrow-down']")    # 條件展開

    # 批次新增彈窗
    batch_select_file = (By.XPATH, "//button[@qa-button='batch-add-dialog-select-file']")       # 批次新增 -> 选取文件
    batch_select_choose_deposit = (By.XPATH, "//div[@qa-select='batch-add-dialog-actioncode']") # 批次新增 -> 下拉式選單
    batch_select_file_update = (By.XPATH, "//button[@qa-button='batch-add-dialog-upload']")     # 批次新增 -> 上传到服务器
    batch_note = (By.XPATH, "//button[@qa-button='batch-add-dialog-hints']")                    # 批次新增 -> 注意事項
    batch_submit = (By.XPATH, "//button[@qa-button='batch-add-dialog-submit']")                 # 批次新增 -> 送出

    # 單個新增
    newadd_oneadd_account = (By.XPATH, "//input[@qa-input='add-dialog-memberlogin']")   # 會員帳號
    newadd_oneadd_account_error = (By.XPATH, "//div[@class='el-form-item__error']")     # 會員帳號_警示
    newadd_deposit_items = (By.XPATH, "//div[@qa-select='actioncode']")                 # 存入項目
    newadd_deposit_comment = (By.XPATH, "//textarea[@qa-input='add-dialog-remark']")    # 存入備註
    newadd_deposit_money_textarea = (By.XPATH, "//input[@qa-input='add-dialog-transferamount']")            # 存入金額
    newadd_deposit_discount_textarea = (By.XPATH, "//input[@qa-input='add-dialog-discountamount']")         # 存款優惠
    newadd_discount_dama_textarea = (By.XPATH, "//input[@qa-input='add-dialog-discountauditpoint']")        # 优惠打码要求
    newadd_discount_auditdue_textarea = (By.XPATH, "//input[@qa-input='add-dialog-discountauditdue']")      # 优惠放宽额度
    newadd_transferauditrate = (By.XPATH, "//input[@qa-input='add-dialog-transferauditrate']")              # 存款稽核倍数
    newadd_transferauditdue = (By.XPATH, "//input[@qa-input='add-dialog-transferauditdue']")                # 存款放宽额度
    newadd_transferauditcharge = (By.XPATH, "//input[@qa-input='add-dialog-transferauditcharge']")          # 稽核行政费用
    newadd_bank_accountnumber = (By.XPATH, "//div[@qa-select='add-dialog-accountnumber']")      # 银行帐号(選擇人工公司入款時)
    newadd_merchantid = (By.XPATH, "//div[@qa-select='add-dialog-merchantid']")                 # 在线商号(選擇人工在線入款時)
    newadd_wallet_address = (By.XPATH, "//div[@qa-select='add-dialog-cryptodeposit']")          # 錢包地址(選擇人工虛擬幣入款時)
    newadd_save_button = (By.XPATH, "//button[@qa-button='add-dialog-submit']")                 # 送出
    newadd_close_button = (By.XPATH, "//button[@qa-button='add-dialog-cancel']")                # 取消
    newadd_success = (By.XPATH, "//div[@role='alert']//h2[text()='操作成功']")                   # 單個新增_操作成功

    # -----------------------------------------------------------------------------------------------------
    # 人工存入
    # SEARCH AREA (查找條件區)
    search_member_account = (By.XPATH, "//input[@qa-input='tab-man-deposit-member_login']")
    search_water_number = (By.XPATH, "//input[@qa-input='tab-man-deposit-id']")
    search_operator = (By.XPATH, "//input[@qa-input='tab-man-deposit-accept_login']")

    def search_type(self, type):
        return (By.XPATH, f"//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='{type}']")
        
    
    # 申請時間
    search_deposit_start = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//input[@placeholder='开始时间']")
    search_deposit_end = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//input[@placeholder='结束时间']")
    search_time_today = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-today']")
    search_time_yesterday = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-yestoday']")
    search_time_thisweek = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-thisWeek']")
    search_time_lastweek = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-lastWeek']")
    search_time_thismonth = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-thisMonth']")
    search_time_lastmonth = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-add-time']//button[@qa-button='quick-time-lastMonth']")

    # 操作時間
    search_operate_start = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//input[@placeholder='开始时间']")
    search_operate_end = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//input[@placeholder='结束时间']")
    search_operate_today = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-today']")
    search_operate_yesterday = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-yestoday']")
    search_operate_thisweek = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-thisWeek']")
    search_operate_lastweek = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-lastWeek']")
    search_operate_thismonth = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-thisMonth']")
    search_operate_lastmonth = (By.XPATH, "//div[@qa-date-picker='tab-madin-deposit-addaccept-time']//button[@qa-button='quick-time-lastMonth']")

    # 交易類型
    search_all_type = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='全选']")
    search_online_artificialdeposit = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='人工在线入款']")
    search_company_artificialdeposit = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='人工公司入款']")
    search_proxy_restart = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='代理退佣']")
    search_activity_discount = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='活动优惠']")
    search_pointreturn_discount = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='返点优惠']")
    search_other = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='其他']")
    search_deposit_cancel = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='取消出款']")
    search_deposit_discount = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='存款优惠']")
    search_negative_clear = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='负数额度归零']")
    search_artificialdeposit = (By.XPATH, "//div[@qa-checkbox='tab-man-deposit-action_codes']//span[text()='人工存入']")

    # 轉帳金額 & 銀行帳號
    search_transfer_money = (By.XPATH, "//input[@qa-input='tab-man-deposit-transfer_amount']")      # 轉帳金額
    search_account_entry_type = (By.XPATH, "//div[@qa-select='tab-man-deposit-currency_code']")     # 入账币别
    search_bank_account = (By.XPATH, "//div[@qa-select='tab-man-deposit-account_number']")          # 银行帐号
    search_online_business_number = (By.XPATH, "//div[@qa-select='tab-man-deposit-merchant_id']")   # 在线商号

    # 查詢帳號
    search_shareholder_textarea = (By.XPATH, "//div[@qa-select='sharelogin']")      # 股東
    search_generalagent_textarea = (By.XPATH, "//input[@qa-input='generalagent']")  # 總代
    search_agent_textarea = (By.XPATH, "//input[@qa-input='agent']")                # 代理

    # 入帳狀態 & 稽核狀態
    search_account_deposit_all = (By.XPATH, "//div[@qa-radio='tab-man-deposit-status']//span[text()='全部']")       # 全部
    search_account_deposit_in = (By.XPATH, "//div[@qa-radio='tab-man-deposit-status']//span[text()='已入帳']")      # 已入帳
    search_account_deposit_notyet = (By.XPATH, "//div[@qa-radio='tab-man-deposit-status']//span[text()='未入帳']")  # 未入帳
    search_account_deposit_cancel = (By.XPATH, "//div[@qa-radio='tab-man-deposit-status']//span[text()='已取消']")  # 已取消

    search_audit_all = (By.XPATH, "//div[@qa-radio='tab-man-deposit-audit_status']//span[text()='全部']")       # 全部
    search_audit_in = (By.XPATH, "//div[@qa-radio='tab-man-deposit-audit_status']//span[text()='已稽核']")      # 已稽核
    search_audit_notyet = (By.XPATH, "//div[@qa-radio='tab-man-deposit-audit_status']//span[text()='待稽核']")  # 待稽核

    # comment
    search_comment = (By.XPATH, "//input[@qa-input='tab-man-deposit-remark']")                  # 備註
    search_fuzzy_search = (By.XPATH, "//label[@qa-checkbox='tab-man-deposit-fuzzy_remark']")    # 備註 模糊搜尋

    # Search Button
    search_button = (By.XPATH, "//button[@qa-button='tab-man-deposit-search']")

    # Search toast message
    search_toast_message = (By.XPATH, "//div[@class='toast-message']")

    # -----------------------------------------------------------------------------------------------------

    # 人工存入 列表 (Table)
    deposit_time = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[1]")          # 申請時間
    deposit_modifitime = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[2]")    # 操作時間
    deposit_account = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[3]")       # 會員
    deposit_agent = (By.XPATH, "//p[text()='代理: ']/span")             # 体系_代理
    deposit_generalagent = (By.XPATH, "//p[text()='总代: ']/span")      # 体系_总代
    deposit_sharelogin = (By.XPATH, "//p[text()='股东: ']/span")        # 体系_股东
    # deposit_currencycode = (By.XPATH, "//td[@data-bind='text: currencycode']")
    deposit_bank_merchant_address = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[5]")   # 银行帐号/在线商号/钱包地址
    # deposit_merchantname = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[5]")  # 在線商號
    deposit_actionname = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[6]")    # 交易類別
    deposit_transferamount = (By.XPATH, "//td[@class='el-table_1_column_7  ']//span[not(contains(text(),'转帐:'))]")    # 转账金额
    deposit_discountamount = (By.XPATH, "//td[@class='el-table_1_column_8  ']//span[not(contains(text(),'优惠:'))]")    # 优惠金额
    deposit_depositamount = (By.XPATH, "//td[@class='el-table_1_column_9  ']//span[not(contains(text(),'入帐:'))]")    # 入账总额
    deposit_status = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[10]")         # 确认状态
    deposit_accept = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[11]")       # 操作者
    deposit_auditstatus = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[12]")    # 稽核状态
    deposit_remark = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]/../../../preceding-sibling::tr/td[13]")       # 備註
    deposit_detail = (By.XPATH, "//button[@qa-button='tab-man-deposit-detail']")                # 明細
    deposit_auditsearch = (By.XPATH, "//button[@qa-button='tab-man-deposit-audit-search']")     # 审核查询

    #  人工存入 data row
    deposit_data_rows = (By.XPATH, "//span[contains(text(),'小計')]/../../../preceding-sibling::tr")
    deposit_last_page = (By.XPATH, "//a[text()='尾页']")
    deposit_multi_page = "//a[@data-bind='text: label' and text()='{}']"

    # ArtificialDepositPage (Table)
    # Total and Detail
    deposit_smallcounter = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'小計')]")       # 小計 (小計 (x条))    
    deposit_smallcounter_subamount = (By.XPATH, "(//td//span[contains(text(),'转帐:')])[1]")                     # 小計_转帐 (转帐: xx,xxx.xx)
    deposit_smallcounter_subdiscount = (By.XPATH, "(//td//span[contains(text(),'优惠:')])[1]")                   # 小計_优惠 (优惠: xx,xxx.xx)
    deposit_smallcounter_subdeposit = (By.XPATH, "(//td//span[contains(text(),'入帐:')])[1]")                    # 小計_入帐 (入帐: xx,xxx.xx)
    deposit_totalcounter = (By.XPATH, "//div[@id='pane-tab-man-deposit']//span[contains(text(),'总计')]")       # 总计 (总计 (x条))
    deposit_totalcounter_amount = (By.XPATH, "(//td//span[contains(text(),'转帐:')])[2]")                        # 总计_转帐 (转帐: xx,xxx.xx)
    deposit_totalcounter_discount = (By.XPATH, "(//td//span[contains(text(),'优惠:')])[2]")                      # 总计_优惠 (优惠: xx,xxx.xx)
    deposit_totalcounter_deposit = (By.XPATH, "(//td//span[contains(text(),'入帐:')])[2]")                       # 总计_入帐 (入帐: xx,xxx.xx)

    # page Record and drop-down menu
    deposit_pager_recordnumber = (By.XPATH, "(//div[@class='ps-pager']//span[@class='el-pagination__total'])[1]") # 總筆數 共_條 
    deposit_pager_dropdown_menu_each = (By.XPATH,"//td[@colspan='15']//*[contains(@data-bind,'pageSize')]//option")
    deposit_pager_dropdown_menu = (By.XPATH, "(//span[@class='el-pagination__sizes'])[1]")

    # 有點擊開的明細資料
    detail_remark = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[2]")     # 备注信息
    detail_transferauditrate = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[3]")     # 存款稽核倍数
    detail_transferauditdue = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[4]")       # 存款稽核放宽
    detail_transferauditcharge = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[5]") # 行政费用比例
    detail_discountauditpoint = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[6]")   # 优惠稽核打码
    detail_discountauditdue = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[7]")       # 优惠稽核放宽
    detail_audittime = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[8]")     # 稽核时间(美東)
    detail_auditmember = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[9]")  # 审核人员
    detail_withdrawid = (By.XPATH, "//div[not(contains(@style,'display: none'))]/dl/dd[10]") # 审核编号

    # -----------------------------------------------------------------------------------------------------
    # 款項審核
    # SEARCH AREA (查找條件區)
    # Deposit Time
    group_deposit_from_application_starttime = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//input[@placeholder='开始时间']")
    group_deposit_from_application_endtime = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//input[@placeholder='结束时间']")
    group_deposit_from_operational_starttime = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//input[@placeholder='开始时间']")
    group_deposit_from_operational_endtime = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//input[@placeholder='结束时间']")

    group_deposit_from_application_today = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-today']")
    group_deposit_from_application_yesterday = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-yestoday']")
    group_deposit_from_application_thisweek = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-thisWeek']")
    group_deposit_from_application_lastweek = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-lastWeek']")
    group_deposit_from_application_thismonth = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-thisMonth']")
    group_deposit_from_application_lastmonth = (By.XPATH, "//div[@qa-date-picker='tab-group-add-time']//button[@qa-button='quick-time-lastMonth']")

    group_deposit_from_operational_today = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-today']")
    group_deposit_from_operational_yesterday = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-yestoday']")
    group_deposit_from_operational_thisweek = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-thisWeek']")
    group_deposit_from_operational_lastweek = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-lastWeek']")
    group_deposit_from_operational_thismonth = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-thisMonth']")
    group_deposit_from_operational_lastmonth = (By.XPATH, "//div[@qa-date-picker='tab-group-accept-time']//button[@qa-button='quick-time-lastMonth']")

    # 存入項目
    group_deposit_checkall = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='全选']")
    group_deposit_artificial_deposit = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='人工存入']")
    group_deposit_negative_clear = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='负数额度归零']")
    group_deposit_deposit_discount = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='存款优惠']")
    group_deposit_cancel_dispensing = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='取消出款']")
    group_deposit_other = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='其他']")
    group_deposit_point_discount = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='返点优惠']")
    group_deposit_event_discount = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='活动优惠']")
    group_deposit_agent_costreturn = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='代理退佣']")
    group_deposit_artificial_company_deposit = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='人工公司入款']")
    group_deposit_artificial_online_deposit = (By.XPATH, "//div[@qa-checkbox='tab-group-action_codes']//span[text()='人工在线入款']")

    # 狀態
    group_deposit_status_all = (By.XPATH, "//div[@qa-radio='tab-group-status']//span[text()='全部']")           # 全部
    group_deposit_status_notyet = (By.XPATH, "//div[@qa-radio='tab-group-status']//span[text()='未完成']")      # 未完成
    group_deposit_status_credit = (By.XPATH, "//div[@qa-radio='tab-group-status']//span[text()='已入帐']")      # 已入帳
    group_deposit_status_cancel = (By.XPATH, "//div[@qa-radio='tab-group-status']//span[text()='已取消']")      # 已取消


    group_deposit_checknumber = (By.XPATH, "//input[@qa-input='tab-group-id']")     # 審核編號
    group_deposit_addedlogin = (By.XPATH, "//input[@qa-input='tab-group-added_login']")         # 申請者
    group_deposit_auditedlogin = (By.XPATH, "//input[@qa-input='tab-group-audited_login']")     # 審核者
    group_deposit_canceledlogin = (By.XPATH, "//input[@qa-input='tab-group-canceled_login']")   # 取消者

    # button
    group_deposit_search_button = (By.XPATH, "//button[@qa-button='tab-group-search']")     # 查詢
    group_deposit_manyconfirm = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-confirm']")    # 批量入款
    group_deposit_manycancel = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-cancel']")      # 批量取消

    # 款項審核 列表 table
    group_deposit_table_firstrow = (By.XPATH, "(//p[text()='申请时间: ']/../../../..)[1]")    
    group_deposit_table_account = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr/td[2]//span")      # 會員帳號
    group_deposit_table_application_time = (By.XPATH, "//p[text()='申请时间: ']/span")      # 申請時間
    group_deposit_table_verify_time = (By.XPATH, "//p[text()='审核时间: ']/span")           # 審核時間
    group_deposit_table_cancel_time = (By.XPATH, "//p[text()='取消时间: ']/span")           # 取消時間
    group_deposit_table_checknumber = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr/td[4]//span")         # 審核編號
    group_deposit_table_audittotalamount = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr/td[5]//span")    # 存入總金額
    group_deposit_table_itemprogressrate = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr/td[6]//span")    # 項目處理進度
    # 以確認狀態為"以入賬"
    group_deposit_table_status = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr/td[7]//span")              # 狀態
    group_deposit_table_application_member = (By.XPATH, "//p[text()='申请: ']/span")
    group_deposit_table_verify_member = (By.XPATH, "//p[text()='审核: ']/span")
    group_deposit_table_cancel_member = (By.XPATH, "//p[text()='取消: ']/span")
    group_deposit_table_deposit = (By.XPATH, "//button[@qa-button='tab-group-confirm']")    # 入款
    group_deposit_table_reject = (By.XPATH, "//button[@qa-button='tab-group-cancel']")      # 取消
    group_deposit_table_confirmbutton = (By.XPATH, "//button[@qa-button='tab-group-detail-dialog-confirm']")    # 確認入款
    group_deposit_table_cancelbutton = (By.XPATH, "//button[@qa-button='tab-group-detail-dialog-cancel']")      # 取消

    # Deposit page record and drop-down menu
    group_deposit_page_recordnumber = (By.XPATH, "(//div[@class='ps-pager']//span[@class='el-pagination__total'])[2]") # 總筆數 共_條 
    group_deposit_page_dropdown_menu_each = (By.XPATH, "//td[@colspan='9']//*[contains(@data-bind,'pageSize')]//option")
    group_deposit_page_dropdown_menu = (By.XPATH, "(//span[@class='el-pagination__sizes'])[2]")

    # Deposit 款項審核 data row
    group_deposit_data_rows = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../preceding-sibling::tr")
    group_deposit_last_page = (By.XPATH, "//td[@colspan='9']//div[@class='pull-right']//a[text()='尾页']")
    group_deposit_multi_page = "//a[@data-bind='text: label' and text()='{}']"

    # Deposit 款項審核 data row (以勾選欄位)
    group_deposit_data_rows_clickup = (By.XPATH, "//div[@class='col-md-12']//tbody[@data-bind='foreach: items']//tr[@class='info']")
    group_deposit_check_first_checkbox = (By.XPATH, "(//tr[@class='el-table__row']//span[@class='el-checkbox__input'])[1]") # 款項審核_第一個checkbox
    # 批量checkbox
    group_deposit_checkall_checkbox = (By.XPATH, "(//thead//span[@class='el-checkbox__input'])[1]")

    # 批量入款Button(未啟用)
    group_deposit_multi_confirm_disable = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-confirm' and @disabled='disabled']")
    # 批量取消Button(未啟用)
    group_deposit_multi_cancel_disable = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-cancel' and @disabled='disabled']")

    # 批量入款Button(啟用)
    # group_deposit_multi_confirm_enable = (By.XPATH, "//button[contains(@data-bind, 'batchDepositConfirm')]")
    group_deposit_multi_confirm_enable = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-confirm' and not(contains(@class,'is-disabled'))]")
    # 批量取消Button(啟用)
    group_deposit_multi_cancel_enable = (By.XPATH, "//button[@qa-button='tab-group-batch-deposit-cancel' and not(contains(@class,'is-disabled'))]")

    # 批量MASK取消動作(操作成功)
    group_deposit_modifi_cancel = (By.XPATH, "//button[contains(@class, 'swal2-confirm swal2-styled')]")

    # 款項審核_小計_存入總金額
    group_deposit_subamount = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../td[5]//span")
    # 款項審核_小計_項目
    group_deposit_subitem = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'小计')]/../../../td[6]//span")

    # 款項審核_總計_存入總金額
    group_deposit_totalamount = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'总计')]/../../../td[5]//span")
    # 款項審核_總計_項目
    group_deposit_totalitem = (By.XPATH, "//div[@id='pane-tab-group']//span[contains(text(),'总计')]/../../../td[6]//span")

    # 款項審核通過
    group_deposit_toastmessage_success = (By.XPATH, "//div[@class='el-notification right']//*[text()='操作成功']")
    
    # 款項審核 批量入款or批量取消 確定按鈕
    group_deposit_pop_confirm = (By.XPATH, "//div[@class='el-message-box__btns']//span[contains(text(),'确定')]")


    # 批次新增Table
    # 選取(未選取)
    batch_select = (By.XPATH, "//div[contains(@class,'ps-dialog-container')]//th//label[@class='el-checkbox']")
    # 選取(已經選取)
    batch_selected = (By.XPATH, "//div[contains(@class,'ps-dialog-container')]//th//label[@class='el-checkbox is-checked']")
    # 會員帳號
    batch_member_account = (By.XPATH, "//td[@class='el-table_3_column_25  ']//span")
    # 存款優惠
    batch_discount_amount = (By.XPATH, "//td[@class='el-table_3_column_26  ']//span")
    # 優惠打碼要求
    batch_discount_auditpoint = (By.XPATH, "//td[@class='el-table_3_column_27  ']//span")
    # 優惠放寬額度
    batch_discount_auditdue = (By.XPATH, "//td[@class='el-table_3_column_28  ']//span")
    # 存入備註
    batch_remark = (By.XPATH, "//td[@class='el-table_3_column_29  ']//span")
    # 錯誤訊息
    batch_error_message = (By.XPATH, "//td[@class='el-table_3_column_30  ']//span")
    # Table一列
    batch_row_data = (By.XPATH, "//table[@class='el-table__body']//tr")
    # batch all select
    batch_all_select = (By.XPATH, "//button[@class='mod-btn-i slct-all put-mag-r']")
    # batch all cancel
    batch_all_cancel = (By.XPATH, "//button[@class='mod-btn-i cacl-all']")
    # 有項目格式錯誤
    batch_item_alert = (By.XPATH, "//div[@aria-labelledby='swal2-title' and @aria-describedby='swal2-content']")
    # 有項目格式錯誤_OK button
    batch_item_alert_ok = (By.XPATH, "//button[@class='swal2-confirm swal2-styled' and @type='button']")
    # 存入項目
    batch_deposit_items = (By.XPATH, "//div[@qa-select='batch-add-dialog-actioncode']")                 
    # 送出 可點擊
    batch_submit_enable = (By.XPATH, "//button[@qa-button='batch-add-dialog-submit' and not(@disabled='disabled')]")
    # 送出 反灰
    batch_submit_disabled = (By.XPATH, "//button[@qa-button='batch-add-dialog-submit' and @disabled='disabled']")
    # 取消
    batch_cancel = (By.XPATH, "//button[@qa-button='batch-add-dialog-cancel']")
    # 視窗檔案匯入用PATH
    excel_path = (By.XPATH, "//input[@type='file' and @class='el-upload__input']")

    # 下拉選單
    def dropdown_item(self, num):
        locator = (By.XPATH, f"//div[@class='el-select-dropdown el-popper' and not(contains(@style,'display: none'))]//li[{num+1}]")
        return locator
        

# pyautogui
class AutoGUIAction(object):

    @classmethod
    def allSelect(self):
        pyautogui.hotkey("ctrl", "a")

    @classmethod
    def filePathSelect(self):
        pyautogui.press("f4")

    @classmethod
    def delete(self):
        pyautogui.press("delete")

    @classmethod
    def typeWrite(self, text):
        try:
            path = str(text)
            pyautogui.typewrite(path)
        except Exception as e:
            print(e)
            print("Can't covert {0} object to 'str'".format(type(text)))

    @classmethod
    def fileInput(self):
        pyautogui.hotkey("altleft", "n")

    @classmethod
    def opening(self):
        pyautogui.hotkey("altleft", "o")

    @classmethod
    def pressEnter(self):
        pyautogui.press("enter")

    @classmethod
    def pressShiftLeft(self):
        pyautogui.press("shiftleft")



class ArtificialDepositPage(BasePage):
    # Website wallet balance get action
    @logged
    def get_wallet_balance_action(self, brand):
        self.brand = brand
        category_1 = ["lv", "ls", "bh", "sc", "cdd", "xpj"]
        category_2 = ["hy", "c7", "c8", "tz", "3h"]

        for index in category_1:
            if index == self.brand:
                wallet_balance_path = (By.XPATH, "//span[@id='nzc-header-balance']")
            else:
                # print("Category_1: ", index)
                pass

        for index in category_2:
            if index == self.brand:
                wallet_balance_path = (By.XPATH, "//b[@id='nzc-header-balance']")
            else:
                # print("Category_2: ", index)
                pass

        assert self.is_element_finded(wallet_balance_path) == True, "前台Web首頁的錢包資訊尋找失敗"
        wallet_balance = self.get_text(wallet_balance_path)

        return float(wallet_balance)


    # -----------------------------------------------------------------------------------------------------------
    # Add New deposit action
    @logged
    def add_new_deposit_action(self, web_account):
        self.click(ArtificialDepositPageLocator.newadd_oneadd)
        self.wait_loading_finish()
        account_id = web_account
        # deposit_items = self.newadd_deposit_items()
        # deposit_items = copy.deepcopy(self.newadd_deposit_items())
        items_num = 0   # 存入項目
        deposit_cash = 0
        dicount = 0
        newadd_items_info_list = list()
        for _ in range(11):
            if self.is_element_finded(ArtificialDepositPageLocator.newadd_oneadd_account_error) == True:
                self.type(ArtificialDepositPageLocator.newadd_oneadd_account_error, account_id)
                self.click(ArtificialDepositPageLocator.newadd_deposit_items)
                self.click(ArtificialDepositPageLocator.dropdown_item(self, items_num))
                # self.select_by_index(ArtificialDepositPageLocator.newadd_deposit_items, items_num)
                comment_temp = "Automatic deposit item00"
                comment_text = comment_temp + str(items_num + 1)
                items_num += 1
                deposit_cash += 1
                deposit_cash_temp = str(deposit_cash)
                dicount += 1
                dicount_temp = str(dicount)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_comment)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_comment) == True, "存款註解欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_deposit_comment, comment_text)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_money_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_money_textarea) == True, "存款金額填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_deposit_money_textarea, deposit_cash_temp)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_discount_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_discount_textarea) == True, "存款優惠填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_deposit_discount_textarea, dicount_temp)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_discount_dama_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_dama_textarea) == True, "優惠打碼填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_discount_dama_textarea, "1")
                self.wait_visibility(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea) == True, "優惠放寬額度填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea, "1")
                self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditrate)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditrate) == True, "存款稽核額度填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_transferauditrate, "1")
                self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditdue)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditdue) == True, "存款放寬額度填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_transferauditdue, "1")
                self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditcharge)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditcharge) == True, "稽核行政費用填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_transferauditcharge, "1")
                self.newadd_alert()
                if items_num == 10:
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_bank_accountnumber)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_bank_accountnumber) == True, "bankaccountnumber can't find"
                    self.click(ArtificialDepositPageLocator.newadd_bank_accountnumber)
                    self.click(ArtificialDepositPageLocator.dropdown_item(self, 0))
                elif items_num == 11:
                    # self.select_by_text(ArtificialDepositPageLocator.newadd_merchantid, "automatic_bot001")
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_merchantid)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_merchantid) == True, "merchantid can't find"
                    self.click(ArtificialDepositPageLocator.newadd_merchantid)
                    self.click(ArtificialDepositPageLocator.dropdown_item(self, 0))
                self.wait_visibility(ArtificialDepositPageLocator.newadd_save_button)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_save_button) == True, "新增入款_保存BTN未找到."
                self.click(ArtificialDepositPageLocator.newadd_save_button)
                self.wait_loading_finish()
                self.sleep(1)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_success) == True, "未找到操作成功彈窗"
                self.refresh_browser()
                self.wait_loading_finish()
                if items_num == 11:
                    pass
                else:
                    self.sleep(1)
                    self.click(ArtificialDepositPageLocator.newadd_oneadd)
                    self.wait_loading_finish()
            else:
                self.type(ArtificialDepositPageLocator.newadd_oneadd_account, account_id)
                # item = self.popout_list(deposit_items)
                self.click(ArtificialDepositPageLocator.newadd_deposit_items)
                self.click(ArtificialDepositPageLocator.dropdown_item(self, items_num))
                # self.select_by_index(ArtificialDepositPageLocator.newadd_deposit_items, items_num)
                comment_temp = "Automatic deposit item00"
                comment_text = comment_temp + str(items_num + 1)
                items_num += 1
                deposit_cash += 1
                deposit_cash_temp = str(deposit_cash)
                dicount += 1
                dicount_temp = str(dicount)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_comment)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_comment) == True, "存款註解欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_deposit_comment, comment_text)
                # self.click(ArtificialDepositPageLocator.newadd_deposit_money_checkbox)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_money_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_money_textarea) == True, "存款金額填寫欄位未找到."
                try:
                    self.type(ArtificialDepositPageLocator.newadd_deposit_money_textarea, deposit_cash_temp)
                except:
                    pass
                # self.click(ArtificialDepositPageLocator.newadd_deposit_discount_checkbox)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_deposit_discount_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_discount_textarea) == True, "存款優惠填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_deposit_discount_textarea, dicount_temp)
                # self.click(ArtificialDepositPageLocator.newadd_discount_dama_checkbox)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_discount_dama_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_dama_textarea) == True, "優惠打碼填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_discount_dama_textarea, "1")
                # self.click(ArtificialDepositPageLocator.newadd_discount_auditdue_checkbox)
                self.wait_visibility(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea) == True, "優惠放寬額度填寫欄位未找到."
                self.type(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea, "1")
                if items_num != 4 and items_num != 7 and items_num != 8:
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditrate)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditrate) == True, "存款稽核額度填寫欄位未找到."
                    self.type(ArtificialDepositPageLocator.newadd_transferauditrate, "1")
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditdue)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditdue) == True, "存款放寬額度填寫欄位未找到."
                    self.type(ArtificialDepositPageLocator.newadd_transferauditdue, "1")
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_transferauditcharge)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditcharge) == True, "稽核行政費用填寫欄位未找到."
                    self.type(ArtificialDepositPageLocator.newadd_transferauditcharge, "1")
                self.newadd_alert()
                if items_num == 10:
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_bank_accountnumber)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_bank_accountnumber) == True, "bankaccountnumber can't find"
                    self.click(ArtificialDepositPageLocator.newadd_bank_accountnumber)
                    self.click(ArtificialDepositPageLocator.dropdown_item(self, 0))
                elif items_num == 11:
                    # self.select_by_text(ArtificialDepositPageLocator.newadd_merchantid, "automatic_bot001")
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_merchantid)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_merchantid) == True, "merchantid can't find"
                    self.click(ArtificialDepositPageLocator.newadd_merchantid)
                    self.click(ArtificialDepositPageLocator.dropdown_item(self, 0))
                elif items_num == 1:
                    self.wait_visibility(ArtificialDepositPageLocator.newadd_wallet_address)
                    assert self.is_element_finded(ArtificialDepositPageLocator.newadd_wallet_address) == True, "wallet_address can't find"
                    self.click(ArtificialDepositPageLocator.newadd_wallet_address)
                    self.click(ArtificialDepositPageLocator.dropdown_item(self, 0))
                self.wait_visibility(ArtificialDepositPageLocator.newadd_save_button)                    
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_save_button) == True, "新增入款_保存BTN未找到."
                self.click(ArtificialDepositPageLocator.newadd_save_button)
                self.wait_loading_finish()
                self.sleep(1)
                assert self.is_element_finded(ArtificialDepositPageLocator.newadd_success) == True, "未找到操作成功彈窗"
                self.refresh_browser()
                self.wait_loading_finish()
                if items_num == 11:
                    pass
                else:
                    self.sleep(1)
                    self.click(ArtificialDepositPageLocator.newadd_oneadd)
                    self.wait_loading_finish()


    @logged
    def add_bill(self, web_account, money):
        self.wait_loading_finish()
        self.click(ArtificialDepositPageLocator.newadd_oneadd)
        self.wait_visibility(ArtificialDepositPageLocator.newadd_oneadd_account)

        self.type(ArtificialDepositPageLocator.newadd_oneadd_account, web_account)
        self.click(ArtificialDepositPageLocator.newadd_deposit_items)
        self.click(ArtificialDepositPageLocator.dropdown_item(self, 1)) #存入項目：人工存入
        self.type(ArtificialDepositPageLocator.newadd_deposit_money_textarea, money)
        self.click(ArtificialDepositPageLocator.newadd_save_button)
        
        self.wait_presence(ArtificialDepositPageLocator.group_deposit_toastmessage_success)
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_toastmessage_success) == True, "Can't find modifi success message"

        self.wait_loading_finish()
        self.click(ArtificialDepositPageLocator.group_deposit_from_application_today)
        self.click(ArtificialDepositPageLocator.group_deposit_search_button)
        self.wait_loading_finish()
        self.click(ArtificialDepositPageLocator.group_deposit_checkall_checkbox)
        self.click(ArtificialDepositPageLocator.group_deposit_multi_confirm_enable)
        self.wait_visibility(ArtificialDepositPageLocator.group_deposit_pop_confirm)
        self.click(ArtificialDepositPageLocator.group_deposit_pop_confirm)
        
        self.wait_presence(ArtificialDepositPageLocator.group_deposit_toastmessage_success)
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_toastmessage_success) == True, "新增人工存入錯誤"


    @logged
    def popout_list(self, list_type):
        item = list_type.pop(0)
        return item


    @logged
    def newadd_alert(self):     #可調整為帶入items_num，各項目做判斷
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_oneadd_account) == True, "member account button can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_items) == True, "deposit items drop-down menu can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_comment) == True, "deposit comment textarea can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_money_checkbox) == True, "deposit money checkbox can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_money_textarea) == True, "deposit money textarea can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_discount_checkbox) == True, "deposit discount checkbox can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_deposit_discount_textarea) == True, "deposit discount textarea can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_dama_checkbox) == True, "discount dama checkbox can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_dama_textarea) == True, "discount dama textarea can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_auditdue_checkbox) == True, "discount auditdue checkbox can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_discount_auditdue_textarea) == True, "discount auditdue textarea can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditrate) == True, "transferauditrate can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditdue) == True, "transferauditdue can't find"
        # assert self.is_element_finded(ArtificialDepositPageLocator.newadd_transferauditcharge) == True, "transferauditcharge can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_save_button) == True, "Save button can't find"
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_close_button) == True, "Close button can't find"


    # -----------------------------------------------------------------------------------------------------------
    # Basic search action (like search init)
    @logged
    def basic_search_setting_action(self):
        self.refresh_browser()
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.mandeposit_mandeposit)
        self.wait_loading_finish()
        self.wait_visibility(ArtificialDepositPageLocator.search_time_today)
        self.click(ArtificialDepositPageLocator.search_time_today)
        self.wait_loading_finish()
        self.wait_visibility(ArtificialDepositPageLocator.search_account_deposit_all)
        self.click(ArtificialDepositPageLocator.search_account_deposit_all)
        self.wait_loading_finish()
        self.click(ArtificialDepositPageLocator.search_audit_all)
        self.wait_loading_finish()
        self.click(ArtificialDepositPageLocator.search_button)
        self.wait_loading_finish()
        self.sleep(1)


    # -----------------------------------------------------------------------------------------------------------
    # Collect and Compare Table current yes or not action(Not use)
    @logged
    def table_check_action(self, all_info_record):
        num = self.get_text(ArtificialDepositPageLocator.deposit_pager_recordnumber)[2:-2]
        num = int(num)
        assert num != 0, "尚未存入金額筆數"

        if num != 0:
            self.total_record_compare(all_info_record)
        

    # -----------------------------------------------------------------------------------------------------------
    # First table data mutil get
    @logged
    def after_search_get_all_data(self, maxnum=500):
        deposit_time = ArtificialDepositPageLocator.deposit_time
        deposit_modifitime = ArtificialDepositPageLocator.deposit_modifitime
        deposit_account = ArtificialDepositPageLocator.deposit_account
        deposit_agent = ArtificialDepositPageLocator.deposit_agent
        deposit_generalagent = ArtificialDepositPageLocator.deposit_generalagent
        deposit_sharelogin = ArtificialDepositPageLocator.deposit_sharelogin
        # deposit_currencycode = ArtificialDepositPageLocator.deposit_currencycode
        deposit_bank_merchant_address = ArtificialDepositPageLocator.deposit_bank_merchant_address
        # deposit_merchantname = ArtificialDepositPageLocator.deposit_merchantname
        deposit_actionname = ArtificialDepositPageLocator.deposit_actionname
        deposit_transferamount = ArtificialDepositPageLocator.deposit_transferamount
        deposit_discountamount = ArtificialDepositPageLocator.deposit_discountamount
        deposit_depositamount = ArtificialDepositPageLocator.deposit_depositamount
        deposit_status = ArtificialDepositPageLocator.deposit_status
        deposit_accept = ArtificialDepositPageLocator.deposit_accept
        deposit_auditstatus = ArtificialDepositPageLocator.deposit_auditstatus
        deposit_remark = ArtificialDepositPageLocator.deposit_remark

        # type(str)
        deposit_page = ArtificialDepositPageLocator.deposit_multi_page
        

        info_list = [deposit_time, deposit_modifitime, deposit_account, deposit_agent, deposit_generalagent, deposit_sharelogin, # deposit_currencycode, 
                    deposit_bank_merchant_address, deposit_actionname, deposit_transferamount, deposit_discountamount, deposit_depositamount, deposit_status, deposit_accept, deposit_auditstatus, deposit_remark]

        all_info_record = list()

        all_time_list = list()
        all_modifitime_list = list()
        all_account_list = list()
        all_agent_list = list()
        all_generalagent_list = list()
        all_sharelogin_list = list()
        # all_currencycode_list = list()
        all_bank_merchant_address_list = list()
        # all_merchantname_list = list()
        all_actionname_list = list()
        all_transferamount_list = list()
        all_discountamount_list = list()
        all_depositamount_list = list()
        all_status_list = list()
        all_accept_list = list()
        all_auditstatus_list = list()
        all_remark_list = list()
        
        total_num_record = self.get_text(ArtificialDepositPageLocator.deposit_pager_recordnumber)[2:-2]
        # self.max_num_v2()   # 因小計尚未改為簡體字顧暫時隱藏
        max_num = str(maxnum)
        if maxnum == 25:
            page_option = 0
        elif maxnum == 50:
            page_option = 1
        elif maxnum == 100:
            page_option = 2
        else:
            page_option = 3    
        self.click(ArtificialDepositPageLocator.deposit_pager_dropdown_menu)
        self.click(ArtificialDepositPageLocator.dropdown_item(self, page_option))
        page_count = 0
        self.wait_loading_finish()
        
        if int(total_num_record) > int(max_num):
            page_switch_total_num = int(total_num_record) // int(max_num)
            for index in range(page_switch_total_num + 1):
                page_count += 1
                page_address = deposit_page.format(page_count)
                deposit_pages = (By.XPATH, page_address)
                self.sleep(1)
                self.click(deposit_pages)
                self.wait_loading_finish()
                self.sleep(2)
                for index in info_list:
                    self.sleep(2)
                    self.wait_visibility(self.find_elements(index))
                    for element in (self.find_elements(index)):
                        table_text = self.get_text_by_dom(element)
                        if index == deposit_time:
                            all_time_list.append(table_text)
                        elif index == deposit_modifitime:
                            all_modifitime_list.append(table_text)
                        elif index == deposit_account:
                            all_account_list.append(table_text)
                        elif index == deposit_agent:
                            all_agent_list.append(table_text)
                        elif index == deposit_generalagent:
                            all_generalagent_list.append(table_text)
                        elif index == deposit_sharelogin:
                            all_sharelogin_list.append(table_text)
                        # elif index == deposit_currencycode:
                            # all_currencycode_list.append(table_text)
                        elif index == deposit_bank_merchant_address:
                            all_bank_merchant_address_list.append(table_text)
                        # elif index == deposit_merchantname:
                        #     all_merchantname_list.append(table_text)
                        elif index == deposit_actionname:
                            all_actionname_list.append(table_text)
                        elif index == deposit_transferamount:
                            all_transferamount_list.append(table_text)
                        elif index == deposit_discountamount:
                            all_discountamount_list.append(table_text)
                        elif index == deposit_depositamount:
                            all_depositamount_list.append(table_text)
                        elif index == deposit_status:
                            all_status_list.append(table_text)
                        elif index == deposit_accept:
                            all_accept_list.append(table_text)
                        elif index == deposit_auditstatus:
                            all_auditstatus_list.append(table_text)
                        elif index == deposit_remark:
                            all_remark_list.append(table_text)

            for index in range(int(total_num_record)):
                record = {
                    "deposit_time": all_time_list[index],
                    "deposit_modifi_time": all_modifitime_list[index],
                    "deposit_account": all_account_list[index],
                    "deposit_agent": all_agent_list[index],
                    "deposit_generalagent": all_generalagent_list[index],
                    "deposit_sharelogin": all_sharelogin_list[index],
                    # "deposit_currency_code": all_currencycode_list[index],
                    "deposit_bank_merchant_address": all_bank_merchant_address_list[index],
                    # "deposit_merchant_name": all_merchantname_list[index],
                    "deposit_action_name": all_actionname_list[index],
                    "deposit_transfer_amount": all_transferamount_list[index],
                    "deposit_discount_amount": all_discountamount_list[index],
                    "deposit_amount": all_depositamount_list[index],
                    "deposit_status": all_status_list[index],
                    "deposit_accept": all_accept_list[index],
                    "deposit_audit_status": all_auditstatus_list[index],
                    "deposit_remark": all_remark_list[index]
                }
                all_info_record.append(record)
                    
        else:
            for index in info_list:
                self.sleep(1)
                for element in (self.find_elements(index)):
                    table_text = self.get_text_by_dom(element)
                    if index == deposit_time:
                        all_time_list.append(table_text)
                    elif index == deposit_modifitime:
                        all_modifitime_list.append(table_text)
                    elif index == deposit_account:
                        all_account_list.append(table_text)
                    elif index == deposit_agent:
                        all_agent_list.append(table_text)
                    elif index == deposit_generalagent:
                        all_generalagent_list.append(table_text)
                    elif index == deposit_sharelogin:
                        all_sharelogin_list.append(table_text)
                    # elif index == deposit_currencycode:
                        # all_currencycode_list.append(table_text)
                    elif index == deposit_bank_merchant_address:
                        all_bank_merchant_address_list.append(table_text)
                    # elif index == deposit_merchantname:
                    #     all_merchantname_list.append(table_text)
                    elif index == deposit_actionname:
                        all_actionname_list.append(table_text)
                    elif index == deposit_transferamount:
                        all_transferamount_list.append(table_text)
                    elif index == deposit_discountamount:
                        all_discountamount_list.append(table_text)
                    elif index == deposit_depositamount:
                        all_depositamount_list.append(table_text)
                    elif index == deposit_status:
                        all_status_list.append(table_text)
                    elif index == deposit_accept:
                        all_accept_list.append(table_text)
                    elif index == deposit_auditstatus:
                        all_auditstatus_list.append(table_text)
                    elif index == deposit_remark:
                        all_remark_list.append(table_text)

            for index in range(int(total_num_record)):
                record = {
                    "deposit_time": all_time_list[index],
                    "deposit_modifi_time": all_modifitime_list[index],
                    "deposit_account": all_account_list[index],
                    "deposit_agent": all_agent_list[index],
                    "deposit_generalagent": all_generalagent_list[index],
                    "deposit_sharelogin": all_sharelogin_list[index],
                    # "deposit_currency_code": all_currencycode_list[index],
                    "deposit_bank_account": all_bank_merchant_address_list[index],
                    # "deposit_merchant_name": all_merchantname_list[index],
                    "deposit_action_name": all_actionname_list[index],
                    "deposit_transfer_amount": all_transferamount_list[index],
                    "deposit_discount_amount": all_discountamount_list[index],
                    "deposit_amount": all_depositamount_list[index],
                    "deposit_status": all_status_list[index],
                    "deposit_accept": all_accept_list[index],
                    "deposit_audit_status": all_auditstatus_list[index],
                    "deposit_remark": all_remark_list[index]
                }
                all_info_record.append(record)

        assert len(all_info_record) == int(total_num_record), "record count wrong"
        return all_info_record


    # compare Total record equal each counter
    # all_info_record = [{}, {}]
    @logged
    def total_record_compare(self, all_info_record):
        total_record_num = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter)[4:-2]
        total_amount = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_amount)[4:]
        total_discount = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_discount)[4:]
        total_deposit = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_deposit)[4:]

        total_amount = total_amount.replace(",", "")
        total_discount = total_discount.replace(",", "")
        total_deposit = total_deposit.replace(",", "")

        pattern = re.compile(r"(\d+(\.\d+)?)")
        total_amount = float(pattern.search(total_amount).group())
        total_discount = float(pattern.search(total_discount).group())
        total_deposit = float(pattern.search(total_deposit).group())

        counter_record_num = len(all_info_record)

        assert int(total_record_num) == counter_record_num, "總紀錄條數錯誤"

        counter_amount = 0
        counter_discount = 0
        counter_deposit = 0
        for index in range(len(all_info_record)):
            counter_amount = counter_amount + float(all_info_record[index]["deposit_transfer_amount"])
            counter_discount = counter_discount + float(all_info_record[index]["deposit_discount_amount"])
            counter_deposit = counter_deposit + float(all_info_record[index]["deposit_amount"])

        counter_amount = float(format(counter_amount, '.2f'))
        counter_discount = float(format(counter_discount, '.2f'))
        counter_deposit = float(format(counter_deposit, '.2f'))

        assert float(total_amount) == counter_amount, "總紀錄轉帳錯誤"
        assert float(total_discount) == counter_discount, "總紀錄優惠錯誤"
        assert float(total_deposit) == counter_deposit, "總紀錄入賬錯誤"


    # -----------------------------------------------------------------------------------------------------------
    # 測試看看能不能由另外的method取用這個值
    total_record_list = None
    payment_record_list = None


    # switch to Mandeposit & another action
    @logged
    def mandeposit_group_normal_action(self, all_info_record):
        ArtificialDepositPage.total_record_list = all_info_record
        self.scroll_to_top()
        self.click(ArtificialDepositPageLocator.mandeposit_group)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.group_deposit_from_application_today)
        self.click(ArtificialDepositPageLocator.group_deposit_checkall)
        # self.click(ArtificialDepositPageLocator.group_deposit_status_all)
        self.click(ArtificialDepositPageLocator.group_deposit_status_notyet)
        self.click(ArtificialDepositPageLocator.group_deposit_search_button)
        self.wait_loading_finish()
        self.sleep(1)
        # self.max_num_v2(tab=2, sort='online_deposit') #暫時先隱藏
        self.status_datanum_check()
        ArtificialDepositPage.payment_record_list = self.payment_check_table_data()
        self.amount_and_item_compare(ArtificialDepositPage.payment_record_list)
        # self.mandeposit_data_check(ArtificialDepositPage.total_record_list, ArtificialDepositPage.payment_record_list)
        amount = self.known_amount_item_added()
        self.select_checkall_deposit_in_and_out()
        self.sleep(1)

        return amount


    # 未完成操作之入款資料條數
    @logged
    def status_datanum_check(self, zerocheck=True):
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_page_recordnumber)
        if zerocheck == True:
            num = self.get_text(ArtificialDepositPageLocator.group_deposit_page_recordnumber)[2:-2]
            num = int(num)
            assert num != 0, "data rows should not be zero"
        elif zerocheck == False:
            num = self.get_text(ArtificialDepositPageLocator.group_deposit_page_recordnumber)[2:-2]
            num = int(num)
            assert num == 0, "data rows should be zero"
        else:
            assert (zerocheck != True and zerocheck != False), "型態錯誤"


    # 審核款項頁面資料收集
    @logged
    def payment_check_table_data(self, maxnum=500):
        deposit_account = ArtificialDepositPageLocator.group_deposit_table_account
        deposit_application_time = ArtificialDepositPageLocator.group_deposit_table_application_time
        deposit_verify_time = ArtificialDepositPageLocator.group_deposit_table_verify_time
        deposit_cancel_time = ArtificialDepositPageLocator.group_deposit_table_cancel_time
        deposit_checknumber = ArtificialDepositPageLocator.group_deposit_table_checknumber
        deposit_audittotalamount = ArtificialDepositPageLocator.group_deposit_table_audittotalamount
        deposit_itemprogressrate = ArtificialDepositPageLocator.group_deposit_table_itemprogressrate
        deposit_status = ArtificialDepositPageLocator.group_deposit_table_status
        deposit_application_member = ArtificialDepositPageLocator.group_deposit_table_application_member
        deposit_verfiy_member = ArtificialDepositPageLocator.group_deposit_table_verify_member
        deposit_cancel_member = ArtificialDepositPageLocator.group_deposit_table_cancel_member
        deposit_access = ArtificialDepositPageLocator.group_deposit_table_deposit
        deposit_reject = ArtificialDepositPageLocator.group_deposit_table_reject

        #type(str)
        deposit_page = ArtificialDepositPageLocator.group_deposit_multi_page

        info_list = [deposit_account, deposit_application_time, deposit_verify_time, deposit_cancel_time, 
                    deposit_checknumber, deposit_audittotalamount, deposit_itemprogressrate,
                    deposit_status, deposit_application_member, deposit_verfiy_member, deposit_cancel_member]
        
        all_info_record = list()

        all_account_list = list()
        all_application_time_list = list()
        all_verify_time_list = list()
        all_cancel_time_list = list()
        all_checknumber_list = list()
        all_audittotalamount_list = list()
        all_itemprogressrate_list = list()
        all_status_list = list()
        all_application_member_list = list()
        all_verfiy_member_list = list()
        all_cancel_member_list = list()

        total_num_record = self.get_text(ArtificialDepositPageLocator.group_deposit_page_recordnumber)[2:-2]
        max_num = str(maxnum)
        if maxnum == 25:
            page_option = 0
        elif maxnum == 50:
            page_option = 1
        elif maxnum == 100:
            page_option = 2
        else:
            page_option = 3    
        self.click(ArtificialDepositPageLocator.group_deposit_page_dropdown_menu)
        self.click(ArtificialDepositPageLocator.dropdown_item(self, page_option))
        max_num = str(maxnum)
        page_count = 0
        self.wait_loading_finish()

        if int(total_num_record) > int(max_num):
            page_switch_total_num = int(total_num_record) // int(max_num)
            for index in range(page_switch_total_num + 1):
                page_count += 1
                page_address = deposit_page.format(page_count)
                deposit_pages = (By.XPATH, page_address)
                self.sleep(1)
                self.click(deposit_pages)
                self.wait_loading_finish()
                for index in info_list:
                    self.sleep(1)
                    for element in (self.find_elements(index)):
                        table_text = self.get_text_by_dom(element)
                        if index == deposit_account:
                            all_account_list.append(table_text)
                        elif index == deposit_application_time:
                            all_application_time_list.append(table_text)
                        elif index == deposit_verify_time:
                            all_verify_time_list.append(table_text)
                        elif index == deposit_cancel_time:
                            all_cancel_time_list.append(table_text)
                        elif index == deposit_checknumber:
                            all_checknumber_list.append(table_text)
                        elif index == deposit_audittotalamount:
                            all_audittotalamount_list.append(table_text)
                        elif index == deposit_itemprogressrate:
                            all_itemprogressrate_list.append(table_text)
                        elif index == deposit_status:
                            all_status_list.append(table_text)
                        elif index == deposit_application_member:
                            all_application_member_list.append(table_text)
                        elif index == deposit_verfiy_member:
                            all_verfiy_member_list.append(table_text)
                        elif index == deposit_cancel_member:
                            all_cancel_member_list.append(table_text)

            for index in range(int(total_num_record)):
                record = {
                    "account": all_account_list[index],
                    "application_time": all_application_time_list[index],
                    "verify_time": all_verify_time_list[index],
                    "cancel_time": all_cancel_time_list[index],
                    "check_number": all_checknumber_list[index],
                    "audit_total_amount": all_audittotalamount_list[index],
                    "item_progress_rate": all_itemprogressrate_list[index],
                    "status": all_status_list[index],
                    "application_member": all_application_member_list[index],
                    "verfiy_member": all_verfiy_member_list[index],
                    "cancel_member": all_cancel_member_list[index],
                }
                all_info_record.append(record)

        else:
            for index in info_list:
                self.sleep(1)
                for element in (self.find_elements(index)):
                    table_text = self.get_text_by_dom(element)
                    if index == deposit_account:
                        all_account_list.append(table_text)
                    elif index == deposit_application_time:
                        all_application_time_list.append(table_text)
                    elif index == deposit_verify_time:
                        all_verify_time_list.append(table_text)
                    elif index == deposit_cancel_time:
                        all_cancel_time_list.append(table_text)
                    elif index == deposit_checknumber:
                        all_checknumber_list.append(table_text)
                    elif index == deposit_audittotalamount:
                        all_audittotalamount_list.append(table_text)
                    elif index == deposit_itemprogressrate:
                        all_itemprogressrate_list.append(table_text)
                    elif index == deposit_status:
                        all_status_list.append(table_text)
                    elif index == deposit_application_member:
                        all_application_member_list.append(table_text)
                    elif index == deposit_verfiy_member:
                        all_verfiy_member_list.append(table_text)
                    elif index == deposit_cancel_member:
                        all_cancel_member_list.append(table_text)

            for index in range(int(total_num_record)):
                record = {
                    "account": all_account_list[index],
                    "application_time": all_application_time_list[index],
                    "verify_time": all_verify_time_list[index],
                    "cancel_time": all_cancel_time_list[index],
                    "check_number": all_checknumber_list[index],
                    "audit_total_amount": all_audittotalamount_list[index],
                    "item_progress_rate": all_itemprogressrate_list[index],
                    "status": all_status_list[index],
                    "application_member": all_application_member_list[index],
                    "verfiy_member": all_verfiy_member_list[index],
                    "cancel_member": all_cancel_member_list[index],
                }
                all_info_record.append(record)

        assert len(all_info_record) == int(total_num_record), "record count wrong"
        return all_info_record


    # 審核頁面的總計、小計 counter & alert
    @logged
    def amount_and_item_compare(self, allinforecord):
        self.wait_loading_finish()
        total_expect = 0
        total_items = 0
        total_amount = 0
        pattern = re.compile(r'\d+')
        for index in allinforecord:
            progress = index["item_progress_rate"]
            temp = pattern.findall(progress)
            item = int(temp[0])
            expect = int(temp[1])
            amount = index["audit_total_amount"]
            amount = float(amount)
            total_items = total_items + item
            total_expect = total_expect + expect
            total_amount = total_amount + amount

        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_subamount) == True, "審核頁小計金額位置找不到"
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_subitem) == True, "審核頁小計項目位置找不到"

        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_totalamount) == True, "審核頁總計金額位置找不到"
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_totalitem) == True, "審核頁總計項目位置找不到"

        group_subamount = float(self.get_text(ArtificialDepositPageLocator.group_deposit_subamount).replace(',', ''))
        group_subitem = self.get_text(ArtificialDepositPageLocator.group_deposit_subitem)
        group_sub_temp = pattern.findall(group_subitem)
        group_subitems = int(group_sub_temp[0])
        group_subexpect = int(group_sub_temp[1])

        group_totalamount = float(self.get_text(ArtificialDepositPageLocator.group_deposit_totalamount).replace(',', ''))
        group_totalitem = self.get_text(ArtificialDepositPageLocator.group_deposit_totalitem)
        group_temp = pattern.findall(group_totalitem)
        group_totalitems = int(group_temp[0])
        group_totalexpect = int(group_temp[1])
        
        if int(self.get_text(ArtificialDepositPageLocator.group_deposit_page_recordnumber)[2:-2]) > 500:
            assert total_amount == group_totalamount, "審核頁總計金額與計算過後的金額有出入"
            assert total_items == group_totalitems, "審核頁總計實際項目與計算過後的項目有出入"
            assert total_expect == group_totalexpect, "審核頁總計項目預期值與計算過後的項目有出入"
        else:
            assert group_totalamount == group_subamount, "審核頁總計金額與小計金額不相同"
            assert group_totalitems == group_subitems, "審核頁總計項目與小計項目不相同"
            assert group_totalexpect == group_subexpect, "審核頁總計項目預期直與小計項目預期值不相同"
            assert total_amount == group_totalamount, "審核頁總計金額與計算過後的金額有出入"
            assert total_items == group_totalitems, "審核頁總計實際項目與計算過後的項目有出入"
            assert total_expect == group_totalexpect, "審核頁總計項目預期值與計算過後的項目有出入"
            assert total_amount == group_subamount, "審核頁小計金額與計算過後的金額有出入"
            assert total_items == group_subitems, "審核頁小計實際項目與計算過後的項目有出入"
            assert total_expect == group_subexpect, "審核頁小計項目預期值與計算過後的項目有出入"


    # 比對兩頁資料是否一致, 僅能使用申請時間最比對
    @logged
    def mandeposit_data_check(self, total_record_list, payment_record_list):
        self.all_record_list = total_record_list
        self.payment_reocrd_list = payment_record_list
        for index in range(len(self.payment_reocrd_list)):
            payment_time = self.payment_reocrd_list[index]["application_time"]
            all_record_time = self.all_record_list[index]["deposit_time"]
            assert payment_time == all_record_time, "申請時間不一致有錯誤"


    # 批量入款勾選並存入
    @logged
    def select_checkall_deposit_in_and_out(self, status=0):
        if status == 0:
            assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_checkall_checkbox) == True, "cant finded CheckBox(member_all_select)"
            self.click(ArtificialDepositPageLocator.group_deposit_checkall_checkbox)
            self.wait_loading_finish()
            assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_confirm_enable) == True, "勾選後, 批量入款未啟用"
            assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_cancel_enable) == True, "勾選後, 批量取消未啟用"
            # assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_confirm_disable) == False, "勾選後, 批量入款未啟用"
            # assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_cancel_disable) == False, "勾選後, 批量取消未啟用"
            if self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_confirm_enable) == True:
                self.sleep(1)
                self.click(ArtificialDepositPageLocator.group_deposit_multi_confirm_enable)
                self.wait_visibility(ArtificialDepositPageLocator.group_deposit_pop_confirm)
                self.click(ArtificialDepositPageLocator.group_deposit_pop_confirm)
                self.wait_loading_finish()
                self.wait_presence(ArtificialDepositPageLocator.group_deposit_toastmessage_success)
                assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_toastmessage_success) == True, "Can't find modifi success message"
                
        

    # System time sort
    # return 整理過後的str(字串) and int(最尾數秒數)
    @logged
    def system_time_return_action(self):
        origin_system_time = self.get_text(ArtificialDepositPageLocator.system_time)
        # pattern = re.compile(r"(\d+\W)")
        # time_sort = pattern.findall(origin_system_time)
        # assert type(time_sort) == list, "System time sort error"
        # maxnum = len(time_sort)
        # maxnum -= 1
        # system_sec = time_sort[maxnum]
        # system_sec = system_sec.replace(" ", "")
        # time_sort[maxnum] = system_sec
        # system_sec = int(system_sec)
        # time_sort = tuple(time_sort)
        # strsys = ""
        # system_time = strsys.join(time_sort)

        time_list = origin_system_time.split()
        system_time = time_list[0] + ' ' + time_list[1]
        sec_list = time_list[1].split(':')
        system_sec = int(sec_list[2])

        return system_time, system_sec


    # -----------------------------------------------------------------------------------------------------------
    # switch to mandeposit[1] & another action
    @logged
    def mandeposit_check_action(self):
        self.scroll_to_top()
        self.click(ArtificialDepositPageLocator.mandeposit_mandeposit)
        self.wait_loading_finish()
        self.sleep(1)
        system_time, system_sec = self.system_time_return_action()
        pattern = re.compile(r'(\d+)')
        timelist = pattern.findall(system_time)
        if int(timelist[3]) == 23:
            assert int(timelist[4]) < 58, "鄰近美東時間天數切換, 請確保測試資料完整"
            assert (int(timelist[4]) >= 2 or int(timelist[4]) < 5), "鄰近美東時間天數切換, 請確保測試資料完整"
        assert self.is_element_finded(ArtificialDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(ArtificialDepositPageLocator.search_time_today)
        self.click(ArtificialDepositPageLocator.search_time_today)
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.search_all_type)
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.search_account_deposit_all)
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.search_button)
        self.wait_loading_finish()
        # self.max_num_v2()    # 因小計尚未改為簡體字顧暫時隱藏
        new_add_list = self.record_list_compare()
        all_new_record_list = self.newadd_and_depositdown_confirm(new_add_list)
        # self.depositTime_check(system_time, system_sec, all_new_record_list)
        case_down_record = self.after_search_get_all_data()
        modifi_down_list = self.deposit_Amount_Checkin(all_new_record_list, case_down_record)
        self.three_col_check_table(all_new_record_list, modifi_down_list)
        self.sleep(1)

            
    
    # 拉出Total_record_list剛新增之項目
    @logged
    def record_list_compare(self):
        notmodifi_list = copy.deepcopy(ArtificialDepositPage.total_record_list)
        payment_list = copy.deepcopy(ArtificialDepositPage.payment_record_list)
        new_add_list = []

        for index in range(len(payment_list)):
            if ((notmodifi_list[index]["deposit_time"] == payment_list[index]["application_time"]) and (notmodifi_list[index]["deposit_amount"] == payment_list[index]["audit_total_amount"])):
                new_add_list.append(notmodifi_list[index])

        assert len(new_add_list) != 0, "新增之項目有誤"

        return new_add_list


    # 找到剛拉出之新增項目, 並重新爬蟲該record, 以newAdd_list長度做for迴圈查找
    @logged
    def newadd_and_depositdown_confirm(self, newadd):
        new_add_list = newadd

        deposit_time = ArtificialDepositPageLocator.deposit_time
        deposit_modifitime = ArtificialDepositPageLocator.deposit_modifitime
        deposit_account = ArtificialDepositPageLocator.deposit_account
        deposit_agent = ArtificialDepositPageLocator.deposit_agent
        deposit_generalagent = ArtificialDepositPageLocator.deposit_generalagent
        deposit_sharelogin = ArtificialDepositPageLocator.deposit_sharelogin
        deposit_bank_merchant_address = ArtificialDepositPageLocator.deposit_bank_merchant_address
        # deposit_merchantname = ArtificialDepositPageLocator.deposit_merchantname
        deposit_actionname = ArtificialDepositPageLocator.deposit_actionname
        deposit_transferamount = ArtificialDepositPageLocator.deposit_transferamount
        deposit_discountamount = ArtificialDepositPageLocator.deposit_discountamount
        deposit_depositamount = ArtificialDepositPageLocator.deposit_depositamount
        deposit_status = ArtificialDepositPageLocator.deposit_status
        deposit_accept = ArtificialDepositPageLocator.deposit_accept
        deposit_auditstatus = ArtificialDepositPageLocator.deposit_auditstatus
        deposit_remark = ArtificialDepositPageLocator.deposit_remark

        # type(str)
        deposit_page = ArtificialDepositPageLocator.deposit_multi_page

        info_list = [deposit_time, deposit_modifitime, deposit_account, deposit_agent, deposit_generalagent, deposit_sharelogin, # deposit_currencycode, 
                    deposit_bank_merchant_address, deposit_actionname, deposit_transferamount, deposit_discountamount, deposit_depositamount, deposit_status, deposit_accept, deposit_auditstatus, deposit_remark]

        all_info_record_new = list()

        all_time_list = list()
        all_modifitime_list = list()
        all_account_list = list()
        all_agent_list = list()
        all_generalagent_list = list()
        all_sharelogin_list = list()
        # all_currencycode_list = list()
        all_bank_merchant_address_list = list()
        # all_merchantname_list = list()
        all_actionname_list = list()
        all_transferamount_list = list()
        all_discountamount_list = list()
        all_depositamount_list = list()
        all_status_list = list()
        all_accept_list = list()
        all_auditstatus_list = list()
        all_remark_list = list()

        self.click(ArtificialDepositPageLocator.deposit_pager_dropdown_menu)
        self.click(ArtificialDepositPageLocator.dropdown_item(self, 3))
        self.wait_loading_finish()

        for index in info_list:
            self.sleep(1)
            for element in self.find_elements(index):
                table_text = self.get_text_by_dom(element)
                if index == deposit_time:
                    all_time_list.append(table_text)
                elif index == deposit_modifitime:
                    all_modifitime_list.append(table_text)
                elif index == deposit_account:
                    all_account_list.append(table_text)
                elif index == deposit_agent:
                    all_agent_list.append(table_text)
                elif index == deposit_generalagent:
                    all_generalagent_list.append(table_text)
                elif index == deposit_sharelogin:
                    all_sharelogin_list.append(table_text)
                elif index == deposit_bank_merchant_address:
                    all_bank_merchant_address_list.append(table_text)
                # elif index == deposit_merchantname:
                #     all_merchantname_list.append(table_text)
                elif index == deposit_actionname:
                    all_actionname_list.append(table_text)
                elif index == deposit_transferamount:
                    all_transferamount_list.append(table_text)
                elif index == deposit_discountamount:
                    all_discountamount_list.append(table_text)
                elif index == deposit_depositamount:
                    all_depositamount_list.append(table_text)
                elif index == deposit_status:
                    all_status_list.append(table_text)
                elif index == deposit_accept:
                    all_accept_list.append(table_text)
                elif index == deposit_auditstatus:
                    all_auditstatus_list.append(table_text)
                elif index == deposit_remark:
                    all_remark_list.append(table_text)

        for index in range(len(new_add_list)):
            record = {
                "deposit_time": all_time_list[index],
                "deposit_modifi_time": all_modifitime_list[index],
                "deposit_account": all_account_list[index],
                "deposit_agent": all_agent_list[index],
                "deposit_generalagent": all_generalagent_list[index],
                "deposit_sharelogin": all_sharelogin_list[index],
                "deposit_bank_account": all_bank_merchant_address_list[index],
                # "deposit_merchant_name": all_merchantname_list[index],
                "deposit_action_name": all_actionname_list[index],
                "deposit_transfer_amount": all_transferamount_list[index],
                "deposit_discount_amount": all_discountamount_list[index],
                "deposit_amount": all_depositamount_list[index],
                "deposit_status": all_status_list[index],
                "deposit_accept": all_accept_list[index],
                "deposit_audit_status": all_auditstatus_list[index],
                "deposit_remark": all_remark_list[index]        
            }
            all_info_record_new.append(record)

        return all_info_record_new


    
    # 重新抓取最新入帳之數據資料(預計10筆)
    @logged
    def deposit_Amount_Checkin(self, newadd_and_depositdown_confirm, casedown_record):
        length = len(newadd_and_depositdown_confirm)
        modifi_down_list = []
        for index in range(length):
            modifi_down_list.append(casedown_record[index])

        return modifi_down_list

    
    # 抓取申請時間做比對
    @logged
    def depositTime_check(self, system_time, system_sec, newconfirm_list):
        record_list = copy.deepcopy(newconfirm_list)
        systemtime = system_time
        # 寫死 預設系統時間位置在轉換為list時, min location is [-2]
        pattern_sort = re.compile(r"\d+")
        systemtime = pattern_sort.findall(systemtime)
        system_min = int(systemtime[-2].replace(" ", ""))
        system_sec = system_sec
        pattern = re.compile(r"\d+\W|\d+")
        for index in range(len(record_list)):
            time_sort = pattern.findall(record_list[index]["deposit_time"])
            assert type(time_sort) == list, "System time sort error"
            maxnum = len(time_sort)
            maxnum -= 1
            sort_sec = time_sort[maxnum]
            sort_min = time_sort[maxnum-1]
            sort_sec = sort_sec.replace(" ", "")
            sort_min = sort_min.replace(" ", "")
            sort_sec = sort_sec.replace(":", "")
            sort_min = sort_min.replace(":", "")
            sort_sec = int(sort_sec)
            assert type(sort_sec) == int, "sec不是int型態"
            sort_min = int(sort_min)
            assert type(sort_min) == int, "min不是int型態"
            assert ((system_min - sort_min == 0) or (system_min - sort_min == 1) or (system_min - sort_min == 2) or (system_min - sort_min <= 5)), "申請時間系統'分鐘'有誤"
            # if system_min - sort_min ==3:
            #     systemSec = systemSec + (60 * 3)                
            #     assert systemSec - sort_sec <= 180, "申請時間系統'秒數'有誤"
            # elif system_min - sort_min == 2:
            #     systemSec = systemSec + (60 * 2)
            #     assert systemSec - sort_sec <= 120, "申請時間系統'秒數'有誤"
            # elif system_min - sort_min == 1:
            #     systemSec = systemSec + 60
            #     assert systemSec - sort_sec <= 60, "申請時間系統'秒數'有誤"
            # elif system_min - sort_min == 0:
            #     assert systemSec - sort_sec <= 20, "申請時間系統'秒數'有誤"


    # 抓取並確認操作時間 & 操作者 & 確認狀態
    @logged
    def three_col_check_table(self, not_confirm, last_tabel_data):
        payment_list = not_confirm
        amount_checkin_list = last_tabel_data
        # assert len(payment_list) >= 1 and len(payment_list) < 11, "新增入款數目錯誤"
        # assert len(amount_checkin_list) >= 1 and len(amount_checkin_list) < 11, "新增入款數目錯誤"

        for index in range(len(payment_list)):
            if payment_list[index]["deposit_time"] == amount_checkin_list[index]["deposit_time"]:
                assert amount_checkin_list[index]["deposit_status"] == "已入账", "確認狀態欄位錯誤"
                assert amount_checkin_list[index]["deposit_accept"] == "test1234", "操作者欄位錯誤"


    # -----------------------------------------------------------------------------------------------------------
    # 全部的總計金額
    @logged
    def known_amount_item_added(self):
        group_total_amount = float(self.get_text(ArtificialDepositPageLocator.group_deposit_totalamount).replace(',', ''))

        return group_total_amount


    # Wallet_balance diff
    @logged
    def wallet_balance_diff(self, wallet, add_amount, new_wallet):
        wallet_balance = float(wallet)
        amount = float(add_amount)
        expect_wallet = float(format(wallet_balance + amount, '.2f'))
        new_wallet_balance = float(new_wallet)
        assert expect_wallet == new_wallet_balance, "預期人工存入金額與Web端現行錢包金額不符合"


    # 取消流程開始
    @logged
    def mandeposit_cancel_action(self):
        self.scroll_to_top()
        self.click(ArtificialDepositPageLocator.mandeposit_group)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.group_deposit_from_application_today)
        self.click(ArtificialDepositPageLocator.group_deposit_checkall)
        self.click(ArtificialDepositPageLocator.group_deposit_status_notyet)
        self.click(ArtificialDepositPageLocator.group_deposit_search_button)
        # self.max_num_v2()    # 因小計尚未改為簡體字顧暫時隱藏
        self.wait_loading_finish()
        self.group_cancel()
        self.switch_deposit()

    
    # Table取消處理
    @logged
    def group_cancel(self):
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_checkall_checkbox) == True, "批量checkbox not enable"
        self.click(ArtificialDepositPageLocator.group_deposit_checkall_checkbox)
        self.sleep(1)
        assert self.is_element_finded(ArtificialDepositPageLocator.group_deposit_multi_cancel_enable) == True, "批量取消Button not enable"
        self.click(ArtificialDepositPageLocator.group_deposit_multi_cancel_enable)
        self.wait_visibility(ArtificialDepositPageLocator.group_deposit_pop_confirm)
        self.click(ArtificialDepositPageLocator.group_deposit_pop_confirm)
        # self.wait_loading_finish()
        # self.click(ArtificialDepositPageLocator.group_deposit_modifi_cancel)
    

    # switch to 人工存入
    @logged
    def switch_deposit(self):
        self.refresh_browser()
        self.sleep(1)
        self.scroll_to_top()
        self.click(ArtificialDepositPageLocator.mandeposit_mandeposit)
        assert self.is_element_finded(ArtificialDepositPageLocator.button_down) == False, "查找條件預設不應收合"
        self.wait_visibility(ArtificialDepositPageLocator.search_time_today)
        self.click(ArtificialDepositPageLocator.search_time_today)
        self.click(ArtificialDepositPageLocator.search_all_type)
        self.click(ArtificialDepositPageLocator.search_account_deposit_cancel)
        self.click(ArtificialDepositPageLocator.search_button)
        # self.max_num_v2()    # 因小計尚未改為簡體字顧暫時隱藏

        for element in self.find_elements(ArtificialDepositPageLocator.group_deposit_table_status):
            table_text = self.get_text_by_dom(element)
            assert table_text == "已取消", "狀態應為'已取消'"       


    # 取得全部紀錄的轉帳金額(今日、人工公司入款、已入帳)
    @logged
    def get_all_amount_money(self, member_account, type):
        self.wait_visibility(ArtificialDepositPageLocator.search_member_account)
        self.type(ArtificialDepositPageLocator.search_member_account, member_account)
        
        self.wait_visibility(ArtificialDepositPageLocator.search_operate_today)
        self.click(ArtificialDepositPageLocator.search_operate_today)
        
        self.wait_visibility(ArtificialDepositPageLocator.search_type(self, type))
        self.click(ArtificialDepositPageLocator.search_type(self, type))
        
        self.wait_visibility(ArtificialDepositPageLocator.search_button)
        self.click(ArtificialDepositPageLocator.search_button)
        
        self.wait_loading_finish()

        self.wait_visibility(ArtificialDepositPageLocator.deposit_pager_recordnumber)
        record_number = self.get_text(ArtificialDepositPageLocator.deposit_pager_recordnumber)[2:-2]
        
        if record_number != '0':
            self.wait_visibility(ArtificialDepositPageLocator.deposit_totalcounter_amount)
            total_amount = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_amount).replace(',', '')[4:]
        else:
            total_amount = 0
        return total_amount
    
    # 取得比對財務報表所需的資料
    @logged
    def get_amount_data(self, reseller_account, type, time=''):
        self.refresh_browser()
        self.wait_visibility(ArtificialDepositPageLocator.search_operate_today)
        if time == '1':
            self.click(ArtificialDepositPageLocator.search_operate_today)
        elif time == '2':
            self.click(ArtificialDepositPageLocator.search_operate_yesterday)
        elif time == '3':
            self.click(ArtificialDepositPageLocator.search_operate_thisweek)
        elif time == '4':
            self.click(ArtificialDepositPageLocator.search_operate_lastweek)
        elif time == '5':
            self.click(ArtificialDepositPageLocator.search_operate_thismonth)
        elif time == '6':
            self.click(ArtificialDepositPageLocator.search_operate_lastmonth)
        for t in type:
            self.wait_visibility(ArtificialDepositPageLocator.search_type(self, t))
            self.click(ArtificialDepositPageLocator.search_type(self, t))

        self.wait_visibility(ArtificialDepositPageLocator.search_agent_textarea)
        self.type(ArtificialDepositPageLocator.search_agent_textarea, reseller_account)
        self.wait_visibility(ArtificialDepositPageLocator.search_button)
        self.click(ArtificialDepositPageLocator.search_button)
        self.wait_loading_finish()
        
        if self.is_element_finded(ArtificialDepositPageLocator.deposit_data_rows) is False:
            total_amount = "0.00"
            total_discount = "0.00"
            return [total_amount, total_discount]

        total_amount = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_amount).replace(',', '')[4:]
        total_discount = self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_discount).replace(',', '')[4:]

        return [total_amount, total_discount]

    # 取得每日報表所需的資料
    @logged
    def get_sum_info(self, reseller_account, type, time=''):
        self.refresh_browser()
        self.wait_visibility(ArtificialDepositPageLocator.search_operate_today)
        if time == '1':
            self.click(ArtificialDepositPageLocator.search_operate_today)
        elif time == '2':
            self.click(ArtificialDepositPageLocator.search_operate_yesterday)
        elif time == '3':
            self.click(ArtificialDepositPageLocator.search_operate_thisweek)
        elif time == '4':
            self.click(ArtificialDepositPageLocator.search_operate_lastweek)
        elif time == '5':
            self.click(ArtificialDepositPageLocator.search_operate_thismonth)
        elif time == '6':
            self.click(ArtificialDepositPageLocator.search_operate_lastmonth)
        for t in type:
            self.wait_visibility(ArtificialDepositPageLocator.search_type(self, t))
            self.click(ArtificialDepositPageLocator.search_type(self, t))

        self.wait_visibility(ArtificialDepositPageLocator.search_agent_textarea)
        self.type(ArtificialDepositPageLocator.search_agent_textarea, reseller_account)
        self.wait_visibility(ArtificialDepositPageLocator.search_button)
        self.click(ArtificialDepositPageLocator.search_button)
        self.wait_loading_finish()
        
        if self.is_element_finded(ArtificialDepositPageLocator.deposit_data_rows) is False:
            artificial_record = {
                'artificial_amount': "0.00",
                'artificial_discount': "0.00",
                'artificial_deposit': "0.00",
                'artificial_total': "0",
            }
            return artificial_record

        artificial_amount = float(self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_amount).replace(',', '')[4:])
        artificial_discount = float(self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_discount).replace(',', '')[4:])
        artificial_deposit = float(self.get_text(ArtificialDepositPageLocator.deposit_totalcounter_deposit).replace(',', '')[4:])
        artificial_total = float(self.get_text(ArtificialDepositPageLocator.deposit_totalcounter).replace(',', '')[4:-2])

        artificial_record = {
            'artificial_amount':"%.2f" %artificial_amount,
            'artificial_discount':"%.2f" %artificial_discount,
            'artificial_deposit': "%.2f" %artificial_deposit,
            'artificial_total': "%.2f" %artificial_total,
        }
        return artificial_record
    
    # 批次新增流程
    @logged
    def batchAddDepositAction(self, account, brand):
        self.account = account
        self.scroll_to_top()
        self.sleep(1)
        assert self.is_element_finded(ArtificialDepositPageLocator.newadd_batchadd) == True, "批次新增紐無顯示"
        self.click(ArtificialDepositPageLocator.newadd_batchadd)
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_select_file) == True, "選擇檔案紐無顯示"
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_select_choose_deposit) == True, "下拉式選單無顯示"
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_select_file_update) == True, "檔案上傳鈕無顯示"
        # self.click(ArtificialDepositPageLocator.batch_select_file)
        self.sleep(1)
        # selenium 直接打路徑進去
        self.updataExcelAction(brand, current=False)
        self.wait_visibility(ArtificialDepositPageLocator.batch_select_file_update)
        self.click(ArtificialDepositPageLocator.batch_select_file_update)
        self.click(ArtificialDepositPageLocator.batch_deposit_items)
        self.click(ArtificialDepositPageLocator.dropdown_item(self, 1)) #存入項目：人工存入
        self.sleep(1)
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_submit_disabled) == True, "送出(反灰)無顯示"
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_select) == True, "選取(未選取)無顯示"
        self.wait_visibility(ArtificialDepositPageLocator.batch_select)
        self.click(ArtificialDepositPageLocator.batch_select)
        self.sleep(1)
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_submit_enable) == True, "送出(可點擊)無顯示"
        assert self.is_element_finded(ArtificialDepositPageLocator.batch_selected) == True, "選取(已經選取)無顯示"

        all_info_error = self.errorMessageCompare(self.account, current=False)
        self.click(ArtificialDepositPageLocator.batch_cancel)
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.newadd_batchadd)
        self.updataExcelAction(brand, current=True)
        self.wait_visibility(ArtificialDepositPageLocator.batch_select_file_update)
        self.click(ArtificialDepositPageLocator.batch_select_file_update)
        self.sleep(1)
        all_info_current = self.errorMessageCompare(self.account, current=True)
        self.click(ArtificialDepositPageLocator.batch_select)
        self.click(ArtificialDepositPageLocator.batch_submit_enable)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.mandeposit_group)
        self.click(ArtificialDepositPageLocator.group_deposit_from_application_today)
        self.click(ArtificialDepositPageLocator.group_deposit_status_notyet)
        self.click(ArtificialDepositPageLocator.group_deposit_search_button)
        self.wait_loading_finish()
        self.sleep(1)
        self.wait_visibility(ArtificialDepositPageLocator.group_deposit_table_audittotalamount)
        depositAmount = self.get_text(ArtificialDepositPageLocator.group_deposit_table_audittotalamount)
        assert str(depositAmount) == "15.55", "存入總金額錯誤"
        depositStatus = self.get_text(ArtificialDepositPageLocator.group_deposit_table_status)
        assert str(depositStatus) == "待审核", "暫未入款，狀態錯誤"
        self.click(ArtificialDepositPageLocator.group_deposit_table_deposit)
        self.wait_loading_finish()
        self.sleep(1)
        self.wait_visibility(ArtificialDepositPageLocator.group_deposit_table_confirmbutton)
        self.click(ArtificialDepositPageLocator.group_deposit_table_confirmbutton)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(ArtificialDepositPageLocator.mandeposit_group)
        self.click(ArtificialDepositPageLocator.group_deposit_from_application_today)
        self.click(ArtificialDepositPageLocator.group_deposit_status_credit)
        self.click(ArtificialDepositPageLocator.group_deposit_search_button)
        self.wait_loading_finish()
        self.sleep(1)
        temp = 0
        for index in range(len(all_info_current)):
            temp = temp + float(all_info_current[index]["discount_amount"])

        return float(temp)


    # 製作批次新增所需要的excel檔案於/financialmanagment/artificial_batch.excel
    @logged
    def excelMadeForBatchAdd(self, account, brand, current=False):
        self.account = str(account)
        if current == False:
            if platform.system() == "Windows":
                user = os.environ['HOMEPATH']
                self.filePath = (r'{0}\\Downloads\\{1}\\batchadd_error.xlsx'.format(user, brand))
            
            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_error.xlsx'.format(user, brand))
            
            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_error.xlsx'.format(user, brand))

            data = [
                [self.account, 0.551, 1, 1, 1],
                [self.account, 1.555, 0, 1, 2],
                [self.account, 0, 1, 0, 3],
                [self.account, 0, 0, 0, 4],
                [self.account, -1, 0, 0, 5],
                [self.account, "測試", "測試", "測試", 6],
                [self.account, 0.22, 0, 1, 7],
                [self.account, 1, 1, -1, 8],
                [self.account, 1, -1, 0, 9],
                [self.account, "test", "-", -1, 10],
                [self.account, -1.563, 0.55, "test", 11],
                [self.account, -1.563, 0, 0, 12],
                [self.account, 1, "test", "test", 13],
                [self.account, 1, 0, "-", 14],
                [self.account, "00.121", "01.001", 1, 15]
            ]
            dataFrame = pd.DataFrame(data, columns=["会员帐号", "存款优惠", "优惠打码要求", "优惠放宽额度", "存入备注"])
            dataFrame.to_excel(self.filePath, sheet_name='批次新增', index=False)
        elif current == True:
            if platform.system() == "Windows":
                user = os.environ['HOMEPATH']
                self.filePath = (r'{0}\\Downloads\\{1}\\batchadd_current.xlsx'.format(user, brand))
            
            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_current.xlsx'.format(user, brand))
            
            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_current.xlsx'.format(user, brand))

            data = [
                [self.account, 1, 1, 1, 1],
                [self.account, 2, 2, 2, 2],
                [self.account, 3, 3, 3, 3],
                [self.account, 4, 4, 4, 4],
                [self.account, 5.55, 5.55, 5.55, 5],
            ]
            dataFrame = pd.DataFrame(data, columns=["会员帐号", "存款优惠", "优惠打码要求", "优惠放宽额度", "存入备注"])
            dataFrame.to_excel(self.filePath, sheet_name='批次新增', index=False)

    
    # 錯誤訊息比對(輸入錯誤excel,是否可以正確輸入錯誤訊息)
    @logged
    def errorMessageCompare(self, account, current=False):
        self.account = account
        account_xpath = ArtificialDepositPageLocator.batch_member_account
        discountAmount_xpath = ArtificialDepositPageLocator.batch_discount_amount
        discountAuditpoint_xpath = ArtificialDepositPageLocator.batch_discount_auditpoint
        discountAuditdue_xpath = ArtificialDepositPageLocator.batch_discount_auditdue
        remark_xpath = ArtificialDepositPageLocator.batch_remark
        errorMessage_xpath = ArtificialDepositPageLocator.batch_error_message

        # 會員帳號
        account = []
        # 存款優惠
        discountAmount = []
        # 優惠打碼要求
        discountAuditpoint = []
        # 優惠放寬額度
        discountAuditdue = []
        # 存入備註
        remark = []
        # 錯誤訊息
        errorMessage = []
        # 自定義資訊欄
        inFo = [account_xpath, discountAmount_xpath, discountAuditpoint_xpath, discountAuditdue_xpath, remark_xpath, errorMessage_xpath]
        # dict形式的資料總覽 e.g.[{}, {}, {}]
        self.allInfo = []

        for index in inFo:
            for element in self.find_elements(index):
                tableText = self.get_text_by_dom(element)
                if index == account_xpath:
                    account.append(tableText)
                elif index == discountAmount_xpath:
                    discountAmount.append(tableText)
                elif index == discountAuditpoint_xpath:
                    discountAuditpoint.append(tableText)
                elif index == discountAuditdue_xpath:
                    discountAuditdue.append(tableText)
                elif index == remark_xpath:
                    remark.append(tableText)
                elif index == errorMessage_xpath:
                    errorMessage.append(tableText)

        for index in range(len(account)):
            record = {
                "member_account": account[index],
                "discount_amount": discountAmount[index],
                "discount_audit_point": discountAuditpoint[index],
                "discount_auditdue": discountAuditdue[index],
                "remark": remark[index],
                "error_message": errorMessage[index]
            }
            self.allInfo.append(record)

        # 錯誤訊息對照
        for index in range(len(self.allInfo)):
            assert self.allInfo[index]["member_account"] == self.account, "會員帳號錯誤"
        # spec附註：Excel没填的值，后端都会以0写入；Excel填数字的值若超过小数第2位，上传完选取送出后一律四舍五入至第2位
        if current == False:
            assert self.allInfo[0]["discount_amount"] == "0.551", "存款优惠錯誤輸入"
            assert self.allInfo[0]["remark"] == "1", "存入备注錯誤輸入"
            assert self.allInfo[0]["error_message"] == "", "错误讯息顯示錯誤"
            assert self.allInfo[1]["discount_amount"] == "1.555", "存款优惠錯誤輸入"
            assert self.allInfo[1]["remark"] == "2", "存入备注錯誤輸入"
            assert self.allInfo[1]["error_message"] == "", "错误讯息顯示錯誤"
            assert self.allInfo[2]["discount_amount"] == "0", "存款优惠錯誤輸入"
            assert self.allInfo[2]["remark"] == "3", "存入备注錯誤輸入"
            assert self.allInfo[2]["error_message"] == "存款优惠必填", "错误讯息顯示錯誤"
            assert self.allInfo[3]["discount_amount"] == "0", "存款优惠錯誤輸入"
            assert self.allInfo[3]["remark"] == "4", "存入备注錯誤輸入"
            assert self.allInfo[3]["error_message"] == "存款优惠必填", "错误讯息顯示錯誤"
            assert self.allInfo[4]["discount_amount"] == "-1", "存款优惠錯誤輸入"
            assert self.allInfo[4]["remark"] == "5", "存入备注錯誤輸入"
            assert self.allInfo[4]["error_message"] == "存款优惠不可小于0", "错误讯息顯示錯誤"
            assert self.allInfo[5]["discount_amount"] == "測試", "存款优惠錯誤輸入"
            assert self.allInfo[5]["remark"] == "6", "存入备注錯誤輸入"
            assert self.allInfo[5]["error_message"] == "存款优惠仅限>0的数字\n存款优惠必填\n优惠打码要求仅限>0的数字\n优惠放宽额度仅限>0的数字", "错误讯息顯示錯誤"
            assert self.allInfo[6]["discount_amount"] == "0.22", "存款优惠錯誤輸入"
            assert self.allInfo[6]["remark"] == "7", "存入备注錯誤輸入"
            assert self.allInfo[6]["error_message"] == "", "错误讯息顯示錯誤"
            assert self.allInfo[7]["discount_amount"] == "1", "存款优惠錯誤輸入"
            assert self.allInfo[7]["remark"] == "8", "存入备注錯誤輸入"
            assert self.allInfo[7]["error_message"] == "优惠放宽额度不可小于0", "错误讯息顯示錯誤"
            assert self.allInfo[8]["discount_amount"] == "1", "存款优惠錯誤輸入"
            assert self.allInfo[8]["remark"] == "9", "存入备注錯誤輸入"
            assert self.allInfo[8]["error_message"] == "优惠打码要求不可小于0", "错误讯息顯示錯誤"
            assert self.allInfo[9]["discount_amount"] == "test", "存款优惠錯誤輸入"
            assert self.allInfo[9]["remark"] == "10", "存入备注錯誤輸入"
            assert self.allInfo[9]["error_message"] == "存款优惠仅限>0的数字\n存款优惠必填\n优惠打码要求仅限>0的数字\n优惠放宽额度不可小于0", "错误讯息顯示錯誤"
            assert self.allInfo[10]["discount_amount"] == "-1.563", "存款优惠錯誤輸入"
            assert self.allInfo[10]["remark"] == "11", "存入备注錯誤輸入"
            assert self.allInfo[10]["error_message"] == "存款优惠不可小于0\n优惠放宽额度仅限>0的数字", "错误讯息顯示錯誤"
            assert self.allInfo[11]["discount_amount"] == "-1.563", "存款优惠錯誤輸入"
            assert self.allInfo[11]["remark"] == "12", "存入备注錯誤輸入"
            assert self.allInfo[11]["error_message"] == "存款优惠不可小于0", "错误讯息顯示錯誤"
            assert self.allInfo[12]["discount_amount"] == "1", "存款优惠錯誤輸入"
            assert self.allInfo[12]["remark"] == "13", "存入备注錯誤輸入"
            assert self.allInfo[12]["error_message"] == "优惠打码要求仅限>0的数字\n优惠放宽额度仅限>0的数字", "错误讯息顯示錯誤"
            assert self.allInfo[13]["discount_amount"] == "1", "存款优惠錯誤輸入"
            assert self.allInfo[13]["remark"] == "14", "存入备注錯誤輸入"
            assert self.allInfo[13]["error_message"] == "优惠放宽额度仅限>0的数字", "错误讯息顯示錯誤"
            assert self.allInfo[14]["discount_amount"] == "00.121", "存款优惠錯誤輸入"
            assert self.allInfo[14]["remark"] == "15", "存入备注錯誤輸入"
            assert self.allInfo[14]["error_message"] == "", "错误讯息顯示錯誤"
        elif current == True:
            assert self.allInfo[0]["discount_amount"] == "1", "存款优惠錯誤輸入"
            assert self.allInfo[0]["discount_audit_point"] == "1", "优惠打码要求錯誤輸入"
            assert self.allInfo[0]["discount_auditdue"] == "1", "优惠放宽额度錯誤輸入"
            assert self.allInfo[0]["remark"] == "1", "存入备注錯誤輸入"
            assert self.allInfo[0]["error_message"] == "", "错误讯息顯示錯誤"

            assert self.allInfo[1]["discount_amount"] == "2", "存款优惠錯誤輸入"
            assert self.allInfo[1]["discount_audit_point"] == "2", "优惠打码要求錯誤輸入"
            assert self.allInfo[1]["discount_auditdue"] == "2", "优惠放宽额度錯誤輸入"
            assert self.allInfo[1]["remark"] == "2", "存入备注錯誤輸入"
            assert self.allInfo[1]["error_message"] == "", "错误讯息顯示錯誤"

            assert self.allInfo[2]["discount_amount"] == "3", "存款优惠錯誤輸入"
            assert self.allInfo[2]["discount_audit_point"] == "3", "优惠打码要求錯誤輸入"
            assert self.allInfo[2]["discount_auditdue"] == "3", "优惠放宽额度錯誤輸入"
            assert self.allInfo[2]["remark"] == "3", "存入备注錯誤輸入"
            assert self.allInfo[2]["error_message"] == "", "错误讯息顯示錯誤"

            assert self.allInfo[3]["discount_amount"] == "4", "存款优惠錯誤輸入"
            assert self.allInfo[3]["discount_audit_point"] == "4", "优惠打码要求錯誤輸入"
            assert self.allInfo[3]["discount_auditdue"] == "4", "优惠放宽额度錯誤輸入"
            assert self.allInfo[3]["remark"] == "4", "存入备注錯誤輸入"
            assert self.allInfo[3]["error_message"] == "", "错误讯息顯示錯誤"

            assert self.allInfo[4]["discount_amount"] == "5.55", "存款优惠錯誤輸入"
            assert self.allInfo[4]["discount_audit_point"] == "5.55", "优惠打码要求錯誤輸入"
            assert self.allInfo[4]["discount_auditdue"] == "5.55", "优惠放宽额度錯誤輸入"
            assert self.allInfo[4]["remark"] == "5", "存入备注錯誤輸入"
            assert self.allInfo[4]["error_message"] == "", "错误讯息顯示錯誤"

        return self.allInfo


    # AutoGui_action
    # @logged
    # def updataExcelAction(self, brand, current=False):
    #     if current == False:
    #         if platform.system() == "Windows":
    #             # homedrive = os.environ['HOMEDRIVE']
    #             user = os.environ['HOMEPATH']
    #             self.filePath = (r"{0}\Downloads\{1}".format(user, brand))
            
    #         elif platform.system() == 'Linux':
    #             user = os.environ['HOME']
    #             self.filePath = (r'{0}/Downloads/{1}/'.format(user, brand))
            
    #         elif platform.system() == 'Darwin':
    #             user = os.environ['HOME']
    #             self.filePath = (r'{0}/Downloads/{1}/'.format(user, brand))
    #         AutoGUIAction.filePathSelect()
    #         self.sleep(1)
    #         AutoGUIAction.allSelect()
    #         AutoGUIAction.delete()
    #         AutoGUIAction.typeWrite(self.filePath)
    #         self.sleep(1)
    #         AutoGUIAction.pressEnter()
    #         AutoGUIAction.fileInput()
    #         AutoGUIAction.delete()
    #         AutoGUIAction.pressShiftLeft()
    #         AutoGUIAction.typeWrite("{0}_error.xlsx".format("batchadd"))
    #         self.sleep(1)
    #         AutoGUIAction.opening()
    #     elif current == True:
    #         if platform.system() == "Windows":
    #             # homedrive = os.environ['HOMEDRIVE']
    #             user = os.environ['HOMEPATH']
    #             self.filePath = (r'{0}\Downloads\{1}'.format(user, brand))
            
    #         elif platform.system() == 'Linux':
    #             user = os.environ['HOME']
    #             self.filePath = (r'{0}/Downloads/{1}/'.format(user, brand))
            
    #         elif platform.system() == 'Darwin':
    #             user = os.environ['HOME']
    #             self.filePath = (r'{0}/Downloads/{1}/'.format(user, brand))
    #         AutoGUIAction.filePathSelect()
    #         self.sleep(1)
    #         AutoGUIAction.allSelect()
    #         AutoGUIAction.delete()
    #         AutoGUIAction.typeWrite(self.filePath)
    #         self.sleep(1)
    #         AutoGUIAction.pressEnter()
    #         AutoGUIAction.fileInput()
    #         AutoGUIAction.delete()
    #         AutoGUIAction.pressShiftLeft()
    #         AutoGUIAction.typeWrite("{0}_current.xlsx".format("batchadd"))
    #         self.sleep(1)
    #         AutoGUIAction.opening()


    # selenium 處理檔案上傳的視窗
    @logged
    def updataExcelAction(self, brand, current=False):
        if current == False:
            if platform.system() == "Windows":
                user = os.environ['HOMEPATH']
                self.filePath = (r"C:\\{0}\\Downloads\\{1}\\batchadd_error.xlsx".format(user, brand))
            
            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_error.xlsx'.format(user, brand))
            
            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_error.xlsx'.format(user, brand))

            excel_path = ArtificialDepositPageLocator.excel_path
            self.type(excel_path, self.filePath)
            self.sleep(3)
        

        elif current == True:
            if platform.system() == "Windows":
                user = os.environ['HOMEPATH']
                self.filePath = (r"C:\\{0}\\Downloads\\{1}\\batchadd_current.xlsx".format(user, brand))
            
            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_current.xlsx'.format(user, brand))
            
            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                self.filePath = (r'{0}/Downloads/{1}/batchadd_current.xlsx'.format(user, brand))

            excel_path = ArtificialDepositPageLocator.excel_path
            self.type(excel_path, self.filePath)
            self.sleep(3)