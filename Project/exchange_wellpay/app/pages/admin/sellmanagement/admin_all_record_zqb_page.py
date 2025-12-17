from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange_wellpay.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common


######## 全部訂單-順付掛賣 ########
class AllRecordZqbPageLocator:
    # 搜尋
    btn_search = (By.XPATH, "//div[@class='query-action']//span[text()='查询']")
    btn_today = (By.XPATH, "//div[@class='el-form-item quick-time']//span[text()='当日']")
    btn_yesterday = (By.XPATH, "//div[@class='el-form-item quick-time']//span[text()='前一天']")
    btn_seven_day_ago = (By.XPATH, "//div[@class='el-form-item quick-time']//span[text()='前7天']")
    btn_thirty_day_ago = (By.XPATH, "//div[@class='el-form-item quick-time']//span[text()='前30天']")
    btn_export = (By.XPATH, "//div[@class='query-action']//span[contains(text(),'汇出')]")
    button_down = (By.XPATH, "//i[@class='el-icon-arrow-down']")  # 條件展開
    input_member_number = (By.XPATH, "//input[@placeholder='请输入会员编号']")
    input_member_level = (By.XPATH, "//input[@placeholder='请选择会员级别']")
    input_sell_status = (By.XPATH, "//label[text()='销售状态']//following::input[1]")
    input_code_type = (By.XPATH, "//label[text()='收款类别']//following::input[1]")
    input_sell_order_id = (By.XPATH, "//input[@placeholder='请输入我要卖订单号']")
    input_merchant_type = (By.XPATH, "//label[text()='商户下发']//following::input[1]")
    input_app_source = (By.XPATH, "//label[text()='App来源']//following::input[1]")
    input_sell_type = (By.XPATH, "//label[text()='銷售方式']//following::input[1]")
    btn_refresh = (By.XPATH, "//span[text()='刷新']")
    refresh_text = (By.XPATH, "//span[contains(text(),'页面更新时间:')]")
    refresh_raido = (By.XPATH, "//label[@qa-checkbox='interval-auto']")  # 自動刷新開關
    refresh_sec = (By.XPATH, "//input[@qa-input='interval-time']")  # 自動刷新秒數

    # 頁表定位
    total_pages = (By.XPATH, "//span[@class='el-pagination__total']")  # 總筆數 共_條
    page_change = (By.XPATH, "//span[@class='el-pagination__sizes']")  # 每頁顯示筆數
    page_list = (By.XPATH,
                 "//div[@class='el-select-dropdown el-popper' and not(contains(@style,'display: none'))]//span[contains(text(),'条/页')]")  # 每頁最多筆數 總下拉式選單 (抓到4項ex:100条/页)

    def page_num(self, num):
        return (By.XPATH, f"(//span[contains(text(),'条/页')])[{num}]")

    page_size_last = (By.XPATH, "(//span[contains(text(),'条/页')])[last()]")  # 每頁顯示筆數 最後的項目
    pages_num = (By.XPATH, "//li[contains(@class,'number')]")  # 總頁數 (ex:共8頁，抓到8項)

    # 列表
    # 第一列資料
    create_time = (By.XPATH, "(//td[@class='el-table_1_column_1 is-center ']/div)[1]")  # 建立時間
    update_time = (By.XPATH, "(//td[@class='el-table_1_column_2 is-center ']/div)[1]")  # 修改時間
    app_source = (By.XPATH, "(//td[@class='el-table_1_column_3 is-center ']/div)[1]")  # APP來源
    sell_type = (By.XPATH, "(//td[@class='el-table_1_column_4 is-center ']/div)[1]")  # 銷售方式
    sell_status = (By.XPATH, "(//td[@class='el-table_1_column_5 is-center ']/div/div)[1]")  # 銷售狀態
    transaction_inquiry_status = (By.XPATH, "(//td[@class='el-table_1_column_6 is-center ']/div)[1]")  # 交易詢問狀態
    order_status = (By.XPATH, "(//td[@class='el-table_1_column_7 is-center ']/div)[1]")  # 訂單狀態(-)
    btn_order_record = (By.XPATH, "")  # 查看紀錄按鈕
    sell_order_number = (By.XPATH, "(//td[@class='el-table_1_column_8 is-center ']/div)[1]")  # 我要賣訂單號
    total_price = (By.XPATH, "(//td[@class='el-table_1_column_9 is-center ']/div)[1]")  # 總販售金額
    principal_data = (By.XPATH, "(//td[@class='el-table_1_column_10 is-center ']/div/div)[1]")  # 剩餘本金/總販售本金
    bonus_last = (By.XPATH, "(//td[@class='el-table_1_column_11 is-center ']//span)[1]")  # 剩於紅利
    bonus_data = (By.XPATH, "(//td[@class='el-table_1_column_11 is-center ']/div/div)[1]")  # 剩於紅利/總紅利
    bonus_rate = (By.XPATH, "(//td[@class='el-table_1_column_12 is-center ']/div)[1]")  # 紅利%
    merchant_withdraw = (By.XPATH, "(//td[@class='el-table_1_column_14 is-center ']/div/div)[1]")  # 商戶下發
    fee_data = (By.XPATH, "(//td[@class='el-table_1_column_15 is-center ']/div)[1]")  # 下發手續費
    member_id = (By.XPATH, "(//td[@class='el-table_1_column_16 is-center ']/div)[1]")  # 會員編號
    member_level = (By.XPATH, "(//td[@class='el-table_1_column_17 is-center ']/div)[1]")  # 會員級別
    bank_type = (By.XPATH, "(//td[@class='el-table_1_column_18 is-center ']/div)[1]")  # 收款類別
    btn_bank_qrcode = (By.XPATH, "(//span[text()='查看二维码'])[1]")  # 查看二维码
    card_bank_name = (By.XPATH, "(//div[contains(text(),'收款姓名:')])[1]")  # 收款姓名
    card_bank = (By.XPATH, "(//div[contains(text(),'收款銀行:')])[1]")  # 收款銀行
    card_bank_account = (By.XPATH, "(//div[contains(text(),'收款账号')])[1]")  # 收款銀行
    note = (By.XPATH, "(//td[@class='el-table_1_column_20 is-left ']/div)[1]")  # 備註
    btn_cancel = (By.XPATH, "//td[@class='el-table_1_column_21 is-center ']//span[text()='取消']")  # 取消
    text_cancel = (By.XPATH, "//div[@aria-hidden='false']//p[contains(text(),'确定执行吗')]")
    btn_confirm = (
    By.XPATH, "//div[@aria-hidden='false']//p[contains(text(),'确定执行吗')]/..//span[contains(text(),'确定')]")

    # 整頁資料
    create_time_list = (By.XPATH, "//td[@class='el-table_1_column_1 is-center ']/div")
    update_time_list = (By.XPATH, "//td[@class='el-table_1_column_2 is-center ']/div")
    app_source_list = (By.XPATH, "//td[@class='el-table_1_column_3 is-center ']/div")
    sell_type_list = (By.XPATH, "//td[@class='el-table_1_column_4 is-center ']/div")
    sell_status_list = (By.XPATH, "//td[@class='el-table_1_column_5 is-center ']/div/div")
    order_status_list = (By.XPATH, "")
    sell_order_number_list = (By.XPATH, "")
    total_price_list = (By.XPATH, "")
    principal_data_list = (By.XPATH, "")
    bonus_data_list = (By.XPATH, "")
    bonus_rate_list = (By.XPATH, "")
    merchant_withdraw_list = (By.XPATH, "")
    fee_data_list = (By.XPATH, "")
    member_id_list = (By.XPATH, "")
    member_level_list = (By.XPATH, "")
    bank_type_list = (By.XPATH, "")  # 收款類別
    bank_data_list = (By.XPATH, "")
    note_list = (By.XPATH, "")
    btn_cancel_list = (By.XPATH, "")

    message_success = (By.XPATH, "//p[contains(text(),'执行成功')]")


class AllRecordZqbPage(BasePage):
    # 取消(下架訂單)
    def cancel_sell_order(self, member_id):
        self.wait_visibility(AllRecordZqbPageLocator.input_member_number)
        self.type(AllRecordZqbPageLocator.input_member_number, member_id)
        self.click(AllRecordZqbPageLocator.btn_search)

        assert self.wait_visibility_status(AllRecordZqbPageLocator.btn_cancel), f'未顯示取消按鈕'
        self.scroll_to_element(AllRecordZqbPageLocator.btn_cancel)
        self.click(AllRecordZqbPageLocator.btn_cancel)
        assert self.wait_visibility_status(AllRecordZqbPageLocator.text_cancel), f'點擊取消，未顯示確定執行二次彈窗'
        self.click(AllRecordZqbPageLocator.btn_confirm)

        assert self.wait_visibility_status(AllRecordZqbPageLocator.message_success), f'未顯示執行成功訊息'

    def check_order_data(self, member_id, app_brand, money, bonus_rate=0, sell_status='1', sell_type='0'):
        self.refresh_browser()
        self.wait_visibility(AllRecordZqbPageLocator.input_member_number)
        self.type(AllRecordZqbPageLocator.input_member_number, member_id)
        self.click(AllRecordZqbPageLocator.btn_search)
        assert self.wait_visibility_status(AllRecordZqbPageLocator.create_time), f'列表無資料'

        # 抓取第一列資料
        data_app_source = self.get_text(AllRecordZqbPageLocator.app_source)
        data_sell_type = self.get_text(AllRecordZqbPageLocator.sell_type)
        data_sell_status = self.get_text(AllRecordZqbPageLocator.sell_status)
        data_order_status = self.get_text(AllRecordZqbPageLocator.order_status)
        data_sell_order_number = self.get_text(AllRecordZqbPageLocator.sell_order_number)
        data_total_price = self.get_text(AllRecordZqbPageLocator.total_price).replace(',', '')
        data_principal_data = self.get_text(AllRecordZqbPageLocator.principal_data)
        data_bonus_data = self.get_text(AllRecordZqbPageLocator.bonus_data)
        data_bonus_rate = self.get_text(AllRecordZqbPageLocator.bonus_rate).replace('%', '').replace(',', '')
        data_merchant_withdraw = self.get_text(AllRecordZqbPageLocator.merchant_withdraw)
        data_fee_data = self.get_text(AllRecordZqbPageLocator.fee_data)
        data_member_id = self.get_text(AllRecordZqbPageLocator.member_id)
        data_member_level = self.get_text(AllRecordZqbPageLocator.member_level)
        data_bank_type = self.get_text(AllRecordZqbPageLocator.bank_type)
        data_card_bank_name = self.get_text(AllRecordZqbPageLocator.card_bank_name)
        data_note = self.get_text(AllRecordZqbPageLocator.note)

        app_name_dict = {'zqb': '顺付', 'zab': '速付'}
        sell_status_dict = {'0': '取消', '1': '販售中', '2': '已售出'}
        sell_type_dict = {'0': '全额购买', '1': '自定义购买'}

        assert data_member_id == member_id, f'列表"會員編號"有誤, 應為{member_id}, 顯示為{data_member_id}'
        assert data_app_source == app_name_dict[
            app_brand], f'列表"App來源"有誤, 應為{app_name_dict[app_brand]}, 顯示為{data_app_source}'
        assert data_total_price == format(money,
                                          '.2f'), f'列表"總販售金額"有誤, 應為{(format(money, ".2f"))}, 顯示為{data_total_price}'
        if bonus_rate == 0:
            bonus_rate = '-'
        assert data_bonus_rate == str(bonus_rate), f'列表"紅利%"有誤, 應為{bonus_rate}, 顯示為{data_bonus_rate}'
        assert data_sell_status == sell_status_dict[
            sell_status], f'列表"銷售狀態"有誤, 應為{sell_status_dict[sell_status]}, 顯示為{data_sell_status}'
        assert data_sell_type == sell_type_dict[
            sell_type], f'列表"銷售方式"有誤, 應為{sell_type_dict[sell_type]}, 顯示為{data_sell_type}'
