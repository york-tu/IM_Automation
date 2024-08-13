from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random


class WalletAddressPageLocator(BasePage):
    # SEARCH AREA (查找條件區)
    search_wallet_address = (By.XPATH, "//input[@data-bind='value: filter.account']")                           # 錢包地址
    search_wallet_id = (By.XPATH, "//input[@data-bind='value: filter.number']")                                 # 錢包地址序號
    search_bankcode = (By.XPATH, "//select[contains(@data-bind,'filter.bankcode')]")                            # 交易所
    search_wallet_name = (By.XPATH, "//select[contains(@data-bind,'cryptocurrencywalletcode')]")                # 錢包名稱
    search_enable_state_using = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '1']")     # 啟用狀態 - 已啟用
    search_enable_state_disabled = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '0']")     # 啟用狀態 - 已禁用
    search_btn = (By.XPATH, "//button[contains(text(),'查找')]")                                           # 查找

    # 新增條件區
    crypto_add = (By.XPATH, "//a[@class='btn btn-default btn-sm']")  # 新增
    crypto_address = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'account')]")       # 錢包地址
    crypto_name = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'name')]")             # 開戶姓名
    crypto_bankcode = (By.XPATH, "//*[contains(@data-bind, 'value') and contains(@data-bind, 'branch')]")       # 交易所名稱
    crypto_wallet_name = (By.XPATH, "//*[contains(@data-bind, 'cryptocurrencyWalletList')]")                    # 錢包名稱
    crypto_limit = (By.XPATH, "//*[@class='form-control input-inline input-medium']")                           # 收款限額
    level = (By.XPATH, "(//*[@class='checkbox-inline  text-control'])[1]")                                      # 會員級別 全部
    crypto_submit = (By.XPATH, "//*[@class='btn blue']")                                                        # 保存送出
    submit_success = (By.XPATH, "//div[@id='toast-container']")                                                 # 成功
    
    sort_bank_in = (By.XPATH, "//label[text()='所属分类']/..//label[@class='radio-inline']") # 所屬分類
    def _sort_wallet_own(self, bank):
        for ele in range(1, len(self.find_elements(WalletAddressPageLocator.sort_bank_in)) + 1):
            sort_bank = (By.XPATH, "//label[text()='所属分类']/..//label[@class='radio-inline'][%d]" % ele)  # 所屬分類
            if self.get_text(sort_bank) == bank:
                self.click(sort_bank)
                break

    # 錢包地址資訊
    row_count = (By.XPATH, "//tbody[@data-bind='foreach: items']/tr[not(@data-bind)]")            # 本頁錢包地址個數
    # onlinepay_row_count = (By.XPATH, "//div[contains(@class,'active in')]/*//tbody/tr")            # 在線商號銀行個數
    searching_data = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td") # 第一行錢包地址所有資料
    revising_button = (By.XPATH, "//a[contains(text(), '修改')]")                           # 修改按鈕
    # warning_setting_button = (By.XPATH, "//a[contains(text(), '警示设定')]")                # 警示設定按鈕
    delete_all_sort = (By.LINK_TEXT, "删除")                                                # 刪除按鈕
    delete_sort_submit = (By.LINK_TEXT, "确定")                                              # 確認刪除
    wallet_number_page_count = (By.XPATH, "//span[@data-bind='text: pager.total']")           # 紀錄數量
    wallet_number_page = (By.XPATH, "//*[@class='input-sm']")                                 # 頁數dropdown
    
    def wallet_sort_name(self, name):
        name = (By.XPATH, "//*[contains(text(),'%s')]" % name)
        return name

    # def get_detail_info(self, RowNum):
    #     return (By.XPATH, f"//tbody[contains(@data-bind,'foreach: items')]/tr[(@data-bind)][{RowNum}]/td/table/tbody/tr/td")

    # def select_detail_button(self, RowNum):
    #     return (By.XPATH, f"(//button[text()='明细'])[{RowNum}]")
    
    # table_bank_name = (By.XPATH, "//a[text()='银行卡号']")          # 銀行卡號
    # table_open_name = (By.XPATH, "//a[text()='开户姓名']")          # 開戶姓名
    # table_open_bank = (By.XPATH, "//a[text()='开户银行']")          # 開戶銀行
    # table_withdraw_time = (By.XPATH, "//a[text()='收款次数']")      # 收款次數
    # table_withdraw_amount = (By.XPATH, "//a[text()='收款总额']")    # 收款總額
    # table_withdraw_limit = (By.XPATH, "//a[text()='收款限额']")     # 收款限額
    # table_deposit_discount = (By.XPATH, "//a[text()='存款优惠']")   # 存款優惠
    # table_active_state = (By.XPATH, "//a[text()='启用状态']")       # 啟用狀態
    # table_sort = (By.XPATH, "//a[text()='排序']")                   # 排序
    
    # def table_column_reader(self, column):                                 # 銀行帳號 column 資訊
    #     return (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr/td[{}]".format(column))

    # # 修改
    # enable_state = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '1']")  # 啟用狀態
    # disable_state = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '0']") # 禁用狀態
    # save_button = (By.XPATH, "//button[text()='保存']")                                   # 儲存

    # # 警示設定
    # check_box = (By.XPATH, "//input[@data-bind = 'checked: autodisable']") # 自動關閉checkbox
    # success_template = (By.XPATH, "//div[@class = 'toast-success']")       # 修改成功元件

    # # 在線商號欄位確認
    # def onlinepay_sort_name_check(self, name):
    #     self.wait_loading_finish()
    #     bank_sort_name = (By.XPATH, "//*[contains(text(),'%s')]" % name)
    #     self.wait_visibility(BankAcconut_PageLocator.onlinepay_row_count)
    #     message = self.get_text(bank_sort_name)
    #     assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name

    # # 錢包地址欄位確認
    # def bank_sort_name_check(self, name):
    #     self.wait_loading_finish()
    #     bank_sort_name = (By.XPATH, "//*[contains(text(),'%s')]" % name)
    #     self.wait_visibility(BankAcconut_PageLocator.wallet_sort_name(name))
    #     message = self.get_text(bank_sort_name)

    #     assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name

    # # 帳號類型
    # sort_bank_account = (By.XPATH, "//label[text()='帐号类型']/..//label[@class='radio-inline']")

    # def _sort_bank_c(self, bank):
    #     for ele in range(1, len(self.find_elements(BankAcconut_PageLocator.sort_bank_account)) + 1):
    #         sort_bank = (By.XPATH, "//label[text()='帐号类型']/..//label[@class='radio-inline'][%d]" % ele)  # 帳號類型
    #         if self.get_text(sort_bank) == bank:
    #             self.click(sort_bank)
    #             break

    

    # 會員級別 個別選
    def _level_click(self):
        i = 1
        for i in range(i, 8):
            level = (By.XPATH, "//*[@class='checkbox-inline  text-control'][%d]" % i)
            self.click(level)

    
    

class WalletAddressPage(BasePage): 
    # 查詢特定錢包地址行數
    def check_row(self, wallet_account='', wallet_number=''):

        self.search_wallet_address(wallet_account = wallet_account, wallet_number=wallet_number)

        record = self.get_text_by_dom(self.find_element(WalletAddressPageLocator.wallet_number_page_count))

        page = ( int(record) / 500 )
        if page > int(page):
            page = int(page) + 1
        
        if wallet_account != "":
            for j in range(1, int(page) + 1):
                for i in range(0, len(self.find_elements(WalletAddressPageLocator.row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[not(@data-bind)][{}]/td[4]/span[2]".format(i + 1))

                    if wallet_account == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)

                if j > 1:
                    next_page = (By.XPATH, "//a[contains(@data-bind,'text: label') and text()='{}']".format(j))
                    self.click(next_page)
        elif wallet_number != "":
            for j in range(1, int(page) + 1):
                for i in range(0, len(self.find_elements(WalletAddressPageLocator.row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[not(@data-bind)][{}]/td[4]/span[1]".format(i + 1))

                    if wallet_number == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)

                if j > 1:
                    next_page = (By.XPATH, "//a[contains(@data-bind,'text: label') and text()='{}']".format(j))
                    self.click(next_page)

        return -1

    # 查詢錢包地址
    def search_wallet_address(self, wallet_account='', wallet_number='', status='1'):
        self.wait_loading_finish()
        self.wait_visibility(WalletAddressPageLocator.search_wallet_address)
        self.sleep(1)
        self.type(WalletAddressPageLocator.search_wallet_address, wallet_account)
        self.type(WalletAddressPageLocator.search_wallet_id, wallet_number)
        if status == '0':
            self.click(WalletAddressPageLocator.search_enable_state_disabled)
        else:
            self.click(WalletAddressPageLocator.search_enable_state_using)
        self.sleep(1)
        self.click(WalletAddressPageLocator.search_btn)
        self.wait_loading_finish()
    
    # 錢包地址欄位確認
    def wallet_sort_check(self, category, walletname, name, address, bankname):
        self.wait_loading_finish()
        datas = self.find_elements(WalletAddressPageLocator.searching_data)
        wallet_data = {
            'wallet_type' : self.get_text_by_dom(datas[1]),
            'wallet_name' : self.get_text_by_dom(datas[2]),
            'wallet_address': self.get_text_by_dom(datas[4]),
            'exchange':self.get_text_by_dom(datas[5]),
        }
        # self.wait_visibility(WalletAddressPageLocator.wallet_sort_name(name))
        # message = self.get_text(WalletAddressPageLocator.wallet_sort_name(name))

        # assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name
        a = str(name + ' / ' + address)
        assert wallet_data['wallet_type'] == category, f"新增資料分類有誤: {wallet_data['wallet_type']}, 應顯示{category}"
        assert wallet_data['wallet_name'] == walletname, f"新增資料錢包名稱有誤: {wallet_data['wallet_name']}, 應顯示{walletname}"
        assert wallet_data['wallet_address'] == str(name + ' / ' + address), f"新增資料錢包地址有誤: {wallet_data['wallet_address']}, 應顯示{str(name + ' / ' + address)}"
        assert wallet_data['exchange'] == bankname, f"新增資料交易所有誤: {wallet_data['exchange']}, 應顯示{bankname}"
  
    # 新增銀行
    def add_sort_wallet_address(self, name, style, bank_sort, wallet_name, money):
        self.wait_loading_finish()
    
        self.wait_presence(WalletAddressPageLocator.crypto_add)
        self.click(WalletAddressPageLocator.crypto_add)
        self.wait_loading_finish()

        # bot_id = datetime.datetime.now().strftime('00000_bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))
        # 新增對應的錢包地址
        wallet_address = datetime.datetime.now().strftime('0walletxxbot%Y%m%d%H%M%Sxx' + str(random.randrange(1, 10000)))

        for loop in range(0,3):
            self.sleep(2)
            if self.wait_visibility_status(WalletAddressPageLocator.crypto_address) is True:
                self.type(WalletAddressPageLocator.crypto_address, wallet_address)  #錢包地址
                self.type(WalletAddressPageLocator.crypto_name, name)   #開戶姓名
                self.type(WalletAddressPageLocator.crypto_bankcode, style) # 交易所名稱  #币安
                WalletAddressPageLocator._sort_wallet_own(self, bank_sort) # 所屬分類   #USDT / USDT(ERC) ( 虚拟币 )   or  USDT / USDT(TRC) ( 虚拟币 ) 
                self.type(WalletAddressPageLocator.crypto_wallet_name, wallet_name) # 錢包名稱  #USDT(ERC20)/ USDT(TRC20)
                assert self.is_element_finded(WalletAddressPageLocator.crypto_limit) == True, "收款限額欄位未找到."
                self.type(WalletAddressPageLocator.crypto_limit, money)
                self.click(WalletAddressPageLocator.level)
                self.click(WalletAddressPageLocator.crypto_submit)
                break
            else:
                if loop == 2:
                    raise EOFError('找不到新增錢包地址頁面輸入欄位')

                self.refresh_browser()
                self.wait_loading_finish()
                
        for loop in range(0,4):
            
            if self.is_element_finded(WalletAddressPageLocator.submit_success) is True:
                message = self.get_text(WalletAddressPageLocator.submit_success)

                assert str(message).__contains__("已新增"), f'狀態錯誤: {message}'
            else:
                if loop == 3:
                    raise EOFError('找不到狀態欄位資訊')
                
                self.sleep(1)
                
        self.wait_loading_finish()
        self.sleep(1)

        return wallet_address

    # # 查詢功能
    # def check_search(self, bank_number, branch):
    #     self.wait_loading_finish()
    #     self.search_bank(bank_number=bank_number, branch=branch)
    #     row = self.check_row(bank_id=bank_number)
        
    #     assert row != -1, "查找發生錯誤"

    # # 修改銀行
    # def change_bank_info(self, bank_number):
    #     self.wait_loading_finish()

    #     # 查詢
    #     self.search_bank(bank_number=bank_number)

    #     # 抓修改前的資料
    #     datas = self.find_elements(BankAcconut_PageLocator.searching_data)
    #     old = self.get_text_by_dom(datas[8])

    #     # 修改
    #     self.click(BankAcconut_PageLocator.revising_button)
    #     self.wait_loading_finish()
    #     if old == "已启用":
    #         self.click(BankAcconut_PageLocator.disable_state)
    #     else:
    #         self.click(BankAcconut_PageLocator.enable_state)
        
    #     self.click(BankAcconut_PageLocator.save_button)
    #     self.wait_loading_finish()

    #     # 查詢
    #     self.search_bank(bank_number=bank_number)
        
    #     # 抓修改後的資料
    #     datas = self.find_elements(BankAcconut_PageLocator.searching_data)
    #     new = self.get_text_by_dom(datas[8])
    #     self.wait_loading_finish()

    #     # 判斷
    #     if old == "已启用":
    #         assert new == "已禁用", f"修改銀行發生錯誤, {new}"
    #     else:
    #         assert new == "已启用", f"修改銀行發生錯誤, {new}"

    
    # 刪除錢包地址
    def delete_wallet_address_sort(self, wallet_account='', wallet_number=''):
        self.search_wallet_address(wallet_account = wallet_account, wallet_number = wallet_number)
        self.sleep(1)
        
        if self.is_element_finded(WalletAddressPageLocator.delete_all_sort) is False:
            return

        for _ in range(len(self.find_elements(WalletAddressPageLocator.delete_all_sort))):
            self.wait_visibility(WalletAddressPageLocator.delete_all_sort)
            assert self.is_element_finded(WalletAddressPageLocator.delete_all_sort) == True, "刪除按鈕BTN未找到"
            self.click(WalletAddressPageLocator.delete_all_sort)
            self.wait_visibility(WalletAddressPageLocator.delete_sort_submit)
            assert self.is_element_finded(WalletAddressPageLocator.delete_sort_submit) == True, "確認刪除BTN未找到"
            self.sleep(1)
            self.click(WalletAddressPageLocator.delete_sort_submit)
            self.search_wallet_address(wallet_account = wallet_account, wallet_number = wallet_number)

        row = self.check_row(wallet_account = wallet_account)

        assert row == -1, "刪除發生錯誤"

    # # 讀取指定銀行資訊 比較 線上存款前後的數值差異
    # def get_withdraw_info(self, bank_number):

    #     # 查詢
    #     self.search_bank(bank_number=bank_number)

    #     # row num
    #     row_num = self.check_row(bank_id=bank_number)

    #     datas = self.find_elements(BankAcconut_PageLocator().get_detail_info(row_num))

    #     # 點擊指定的明細按鈕
    #     self.click(BankAcconut_PageLocator().select_detail_button(row_num))
        
    #     bank_withdraw_count = self.get_text_by_dom(datas[0]).replace('总收款次数： ', '').replace('当天收款次数(北京)：', ' ').replace(' ','')
    #     bank_withdraw_number = self.get_text_by_dom(datas[1]).replace('总收款总额： ', '').replace('当天收款总额(北京)：', ' ').replace(' ','')
    #     all_count = bank_withdraw_count.split('\n')[0]
    #     today_count = bank_withdraw_count.split('\n')[1]
    #     all_number = bank_withdraw_number.split('\n')[0]
    #     today_number = bank_withdraw_number.split('\n')[1]

    #     # 轉型態
    #     all_count, today_count, all_number, today_number = int(all_count), int(today_count), int(all_number), int(today_number)

    #     return all_count, today_count, all_number, today_number