from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random


class BankAcconut_PageLocator(BasePage):
    # SEARCH AREA (查找條件區)
    search_bank_number = (By.XPATH, "//input[@data-bind='value: filter.account']")                          # 銀行卡號
    search_name = (By.XPATH, "//input[@data-bind='value: filter.name']")                                   # 開戶姓名
    search_branch = (By.XPATH, "//input[@data-bind='value: filter.branch']")                               # 開戶支行 
    search_bank_sort = (By.XPATH, "//select[contains(@data-bind,'categoryOptions')]")                      # 所屬分類
    search_enable_state_using = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '1']") # 啟用狀態 - 已啟用
    search_enable_state_disabled = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '0']") # 啟用狀態 - 禁用
    search_all_sort = (By.XPATH, "//button[contains(text(),'查找')]")                                      # 查找

    # 新增條件區
    bank_account_add = (By.CSS_SELECTOR, "a.btn.btn-default.btn-sm > i.fa.fa-plus")  # 新增
    bank_number = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'account')]")                      # 銀行卡號 / UPI地址
    bank_name = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'name')]")                          # 開戶姓名
    bank_branch = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'branch')]")                      # 開戶支行
    bank_limit = (By.XPATH, "//*[text()='收款限额']/..//*[@class='form-control input-inline input-medium']")  # 收款限額
    bank_submit = (By.XPATH, "//*[@class='btn blue']")                                # 保存送出
    submit_success = (By.XPATH, "//div[@id='toast-container']")                       # 成功

    # 銀行帳號資訊
    row_count = (By.XPATH, "//tbody[@data-bind='foreach: items']/tr[not(@data-bind)]")            # 本頁銀行個數
    onlinepay_row_count = (By.XPATH, "//div[contains(@class,'active in')]/*//tbody/tr")            # 在線商號銀行個數
    searching_data = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td") # 第一行銀行所有資料
    revising_button = (By.XPATH, "//a[contains(text(), '修改')]")                           # 修改按鈕
    warning_setting_button = (By.XPATH, "//a[contains(text(), '警示设定')]")                # 警示設定按鈕
    delete_all_sort = (By.LINK_TEXT, "删除")                                                # 刪除按鈕
    delete_sort_submit = (By.LINK_TEXT, "确定")                                              # 確認刪除
    bank_number_page_count = (By.XPATH, "//span[@data-bind='text: pager.total']")           # 紀錄數量
    bank_number_page = (By.XPATH, "//*[@class='input-sm']")                                 # 頁數dropdown
    
    def get_detail_info(self, RowNum):
        return (By.XPATH, f"//tbody[contains(@data-bind,'foreach: items')]/tr[(@data-bind)][{RowNum}]/td/table/tbody/tr/td")

    def select_detail_button(self, RowNum):
        return (By.XPATH, f"(//button[text()='明细'])[{RowNum}]")
    
    table_bank_name = (By.XPATH, "//a[text()='银行卡号']")          # 銀行卡號
    table_open_name = (By.XPATH, "//a[text()='开户姓名']")          # 開戶姓名
    table_open_bank = (By.XPATH, "//a[text()='开户银行']")          # 開戶銀行
    table_withdraw_time = (By.XPATH, "//a[text()='收款次数']")      # 收款次數
    table_withdraw_amount = (By.XPATH, "//a[text()='收款总额']")    # 收款總額
    table_withdraw_limit = (By.XPATH, "//a[text()='收款限额']")     # 收款限額
    table_deposit_discount = (By.XPATH, "//a[text()='存款优惠']")   # 存款優惠
    table_active_state = (By.XPATH, "//a[text()='启用状态']")       # 啟用狀態
    table_sort = (By.XPATH, "//a[text()='排序']")                   # 排序
    
    def table_column_reader(self, column):                                 # 銀行帳號 column 資訊
        return (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr/td[{}]".format(column))

    # 修改
    enable_state = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '1']")  # 啟用狀態
    disable_state = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '0']") # 禁用狀態
    save_button = (By.XPATH, "//button[text()='保存']")                                   # 儲存

    # 警示設定
    warning_check_box = (By.XPATH, "//div[@class='modal fade in']//input[@data-bind = 'checked: autodisable']") # 自動關閉checkbox
    warning_save_button =  (By.XPATH, "//div[@class='modal fade in']//button[text()='保存']")  
    success_template = (By.XPATH, "//div[@class = 'toast-success']")       # 修改成功元件

    # 在線商號欄位確認
    def onlinepay_sort_name_check(self, name):
        self.wait_loading_finish()
        bank_sort_name = (By.XPATH, "//*[contains(text(),'%s')]" % name)
        self.wait_visibility(BankAcconut_PageLocator.onlinepay_row_count)
        message = self.get_text(bank_sort_name)
        assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name

    # 銀行欄位確認
    def bank_sort_name_check(self, name):
        self.wait_loading_finish()
        bank_sort_name = (By.XPATH, "//*[contains(text(),'%s')]" % name)
        self.wait_visibility(BankAcconut_PageLocator.row_count)
        message = self.get_text(bank_sort_name)

        assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name

    # 帳號類型
    sort_bank_account = (By.XPATH, "//label[text()='帐号类型']/..//label[@class='radio-inline']")

    def _sort_bank_c(self, bank):
        for ele in range(1, len(self.find_elements(BankAcconut_PageLocator.sort_bank_account)) + 1):
            sort_bank = (By.XPATH, "//label[text()='帐号类型']/..//label[@class='radio-inline'][%d]" % ele)  # 帳號類型
            if self.get_text(sort_bank) == bank:
                self.click(sort_bank)
                break

    # 所屬分類
    sort_bank_in = (By.XPATH, "//label[text()='所属分类']/..//label[@class='radio-inline']")

    def _sort_bank_own(self, bank):
        for ele in range(1, len(self.find_elements(BankAcconut_PageLocator.sort_bank_in)) + 1):
            sort_bank = (By.XPATH, "//label[text()='所属分类']/..//label[@class='radio-inline'][%d]" % ele)  # 所屬分類
            if self.get_text(sort_bank) == bank:
                self.click(sort_bank)
                break

    # 會員級別 個別選
    def _level_click(self):
        i = 1
        for i in range(i, 8):
            level = (By.XPATH, "//*[@class='checkbox-inline  text-control'][%d]" % i)
            self.click(level)

    level = (By.XPATH, "(//*[@class='checkbox-inline  text-control'])[1]") # 會員級別 全部
    
class Pay_Branch_Page(BasePage):
    # 查詢特定銀行帳號行數
    def check_row(self, bank_id='', name=''):

        self.search_bank(bank_number=bank_id, search_name=name)

        record = self.get_text_by_dom(self.find_element(BankAcconut_PageLocator.bank_number_page_count))

        page = ( int(record) / 500 )
        if page > int(page):
            page = int(page) + 1
        
        if bank_id != "":
            for j in range(1, int(page) + 1):
                for i in range(0, len(self.find_elements(BankAcconut_PageLocator.row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[not(@data-bind)][{}]/td[4]/span[2]".format(i + 1))

                    if bank_id == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)

                if j > 1:
                    next_page = (By.XPATH, "//a[contains(@data-bind,'text: label') and text()='{}']".format(j))
                    self.click(next_page)
        elif name != "":
            for j in range(1, int(page) + 1):
                for i in range(0, len(self.find_elements(BankAcconut_PageLocator.row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[not(@data-bind)][{}]/td[4]/span[1]".format(i + 1))

                    if name == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)

                if j > 1:
                    next_page = (By.XPATH, "//a[contains(@data-bind,'text: label') and text()='{}']".format(j))
                    self.click(next_page)

        return -1

    # 查詢銀行
    def search_bank(self, bank_number='', search_name='', branch='', status='1'):
        # status為狀態搜尋條件，已啟用=1；已禁用=0，預設啟用
        self.wait_loading_finish()
        self.wait_visibility(BankAcconut_PageLocator.search_bank_number)
        self.sleep(1)
        self.type(BankAcconut_PageLocator.search_bank_number, bank_number)
        self.type(BankAcconut_PageLocator.search_name, search_name)
        self.type(BankAcconut_PageLocator.search_branch, branch)
        if status == '0':
            self.wait_visibility(BankAcconut_PageLocator.search_enable_state_disabled)
            self.click(BankAcconut_PageLocator.search_enable_state_disabled)
        else:
            self.wait_visibility(BankAcconut_PageLocator.search_enable_state_using)
            self.click(BankAcconut_PageLocator.search_enable_state_using)
        self.sleep(1)
        self.click(BankAcconut_PageLocator.search_all_sort)
        self.wait_loading_finish()
  
    # 新增銀行
    def add_sort_bank(self, name, branch, money, style, bank_sort=''):
        self.wait_loading_finish()
        if bank_sort == '':
            bank_sort = style

        self.wait_presence(BankAcconut_PageLocator.bank_account_add)
        self.click(BankAcconut_PageLocator.bank_account_add)
        self.wait_loading_finish()

        if branch =='upi':
            bot_id = datetime.datetime.now().strftime('00000' + str(random.randrange(1000000, 9999999))+'@bot_%Y%m%d%H%M%S')
        else:
            bot_id = datetime.datetime.now().strftime('00000_bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))
        
        for loop in range(0,3):
            self.sleep(2)
            if self.wait_visibility_status(BankAcconut_PageLocator.bank_number) is True:
                BankAcconut_PageLocator._sort_bank_c(self, style) # 帳號類型
                self.type(BankAcconut_PageLocator.bank_number, bot_id)
                self.type(BankAcconut_PageLocator.bank_name, name)
                if branch != 'upi':
                    self.type(BankAcconut_PageLocator.bank_branch, branch)
                BankAcconut_PageLocator._sort_bank_own(self, bank_sort) # 所屬分類
                assert self.is_element_finded(BankAcconut_PageLocator.bank_limit) == True, "收款限額欄位未找到."
                self.type(BankAcconut_PageLocator.bank_limit, money)
                self.click(BankAcconut_PageLocator.level)
                self.click(BankAcconut_PageLocator.bank_submit)
                break
            else:
                if loop == 2:
                    raise EOFError('找不到新增銀行頁面輸入欄位')

                self.refresh_browser()
                self.wait_loading_finish()
                

        for loop in range(0,4):
            
            if self.is_element_finded(BankAcconut_PageLocator.submit_success) is True:
                message = self.get_text(BankAcconut_PageLocator.submit_success)

                assert str(message).__contains__("已新增"), f'狀態錯誤: {message}'
            else:
                if loop == 3:
                    raise EOFError('找不到狀態欄位資訊')
                
                self.sleep(1)
                

        

        self.wait_loading_finish()
        self.sleep(1)

        return bot_id

    # 查詢功能
    def check_search(self, bank_number, branch):
        self.wait_loading_finish()
        self.search_bank(bank_number=bank_number, branch=branch)
        row = self.check_row(bank_id=bank_number)
        
        assert row != -1, "查找發生錯誤"

    # 修改銀行
    def change_bank_info(self, bank_number):
        self.wait_loading_finish()

        # 查詢
        self.search_bank(bank_number=bank_number)

        # 抓修改前的資料
        datas = self.find_elements(BankAcconut_PageLocator.searching_data)
        old = self.get_text_by_dom(datas[8])

        # 修改
        self.click(BankAcconut_PageLocator.revising_button)
        self.wait_loading_finish()
        if old == "已启用":
            self.click(BankAcconut_PageLocator.disable_state)
        else:
            self.click(BankAcconut_PageLocator.enable_state)
        
        self.click(BankAcconut_PageLocator.save_button)
        self.wait_loading_finish()

        # 查詢
        self.search_bank(bank_number=bank_number, status='0')
        
        # 抓修改後的資料
        datas = self.find_elements(BankAcconut_PageLocator.searching_data)
        new = self.get_text_by_dom(datas[8])
        self.wait_loading_finish()

        # 判斷
        if old == "已启用":
            assert new == "已禁用", f"修改銀行發生錯誤, {new}"
        else:
            assert new == "已启用", f"修改銀行發生錯誤, {new}"

    # 修改警示設定
    def change_bank_warning_setting(self, bank_number):
        self.wait_loading_finish()

        # 查詢
        self.search_bank(bank_number=bank_number, status='0')

        # 抓修改前的資料
        datas = self.find_elements(BankAcconut_PageLocator.searching_data)
        old = self.get_text_by_dom(datas[6])

        # 修改
        self.click(BankAcconut_PageLocator.warning_setting_button)
        self.wait_loading_finish()
        self.wait_visibility(BankAcconut_PageLocator.delete_all_sort)
        self.click(BankAcconut_PageLocator.warning_check_box)
        self.click(BankAcconut_PageLocator.warning_save_button)
        self.wait_loading_finish()

        # 查詢
        self.search_bank(bank_number=bank_number, status='0')
        
        # 抓修改後的資料
        datas = self.find_elements(BankAcconut_PageLocator.searching_data)
        new = self.get_text_by_dom(datas[6])
        
        # 判斷
        assert new != old, "警示設定已設定，但後台頁面尚未變化"

    # 刪除銀行
    def delete_bank_sort(self, bank_number='', name='', branch='', bank_sort='',status='1'):
        self.search_bank(bank_number=bank_number, search_name=name, branch=branch, status=status)
        self.sleep(1)
        
        if self.is_element_finded(BankAcconut_PageLocator.delete_all_sort) is False:
            return

        for _ in range(len(self.find_elements(BankAcconut_PageLocator.delete_all_sort))):
            self.wait_visibility(BankAcconut_PageLocator.delete_all_sort)
            assert self.is_element_finded(BankAcconut_PageLocator.delete_all_sort) == True, "刪除按鈕BTN未找到"
            self.click(BankAcconut_PageLocator.delete_all_sort)
            self.wait_visibility(BankAcconut_PageLocator.delete_sort_submit)
            assert self.is_element_finded(BankAcconut_PageLocator.delete_sort_submit) == True, "確認刪除BTN未找到"
            self.sleep(1)
            self.click(BankAcconut_PageLocator.delete_sort_submit)
            self.search_bank(bank_number=bank_number, search_name=name, branch=branch, status=status)

        row = self.check_row(bank_id=bank_number)

        assert row == -1, "刪除發生錯誤"

    # 讀取指定銀行資訊 比較 線上存款前後的數值差異
    def get_withdraw_info(self, bank_number):

        # 查詢
        self.search_bank(bank_number=bank_number)

        # row num
        row_num = self.check_row(bank_id=bank_number)

        datas = self.find_elements(BankAcconut_PageLocator().get_detail_info(row_num))

        # 點擊指定的明細按鈕
        self.click(BankAcconut_PageLocator().select_detail_button(row_num))
        
        bank_withdraw_count = self.get_text_by_dom(datas[0]).replace('总收款次数： ', '').replace('当天收款次数(北京)：', ' ').replace(' ','')
        bank_withdraw_number = self.get_text_by_dom(datas[1]).replace('总收款总额： ', '').replace('当天收款总额(北京)：', ' ').replace(' ','')
        all_count = bank_withdraw_count.split('\n')[0]
        today_count = bank_withdraw_count.split('\n')[1]
        all_number = bank_withdraw_number.split('\n')[0]
        today_number = bank_withdraw_number.split('\n')[1]

        # 轉型態
        all_count, today_count, all_number, today_number = int(all_count), int(today_count), int(all_number), int(today_number)

        return all_count, today_count, all_number, today_number