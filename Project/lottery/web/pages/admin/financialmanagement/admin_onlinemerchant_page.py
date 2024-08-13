from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random

class OnlineMerchantPageLocator(object):
    # 查找條件
    search_account = (By.XPATH, "//input[@data-bind = 'value: filter.account']")                 # 收款帳號
    search_name = (By.XPATH, "//input[@data-bind = 'value: filter.name']")                       # 商號名稱
    activate_all = (By.XPATH, "//input[@data-bind = 'radio: filter.status' and @value = '-1']")  # 啟用狀態 - 全部
    btn_search = (By.XPATH, "//button[@data-bind = 'click: function () { $root.reload(1) }']")   # 查找按鈕

    # 新增/修改
    btn_add = (By.XPATH, "//*[@class= 'btn btn-default btn-sm']")             # 新增
        # 必填
    add_name = (By.XPATH, "//input[@data-bind = 'value: name']")                       # 商号名称
    add_payment_code = (By.XPATH, "//input[@id='s2id_autogen6']")                      # 支付网关
    select_payment_code = (By.XPATH, "//li[@role='presentation']")                     # 支付网关_選項
    add_account = (By.XPATH, "//input[@data-bind = 'value: account']")                 # 商家编号
    add_code = (By.XPATH, "//input[@data-bind = 'value: appkey']")                     # 终端编码
    add_secret = (By.XPATH, "//input[@data-bind = 'value: appsecret']")                # 签名密钥
    
    def select_type(self, type_name):
        return (By.XPATH, f"//label[@class='radio-inline' and ./span[contains(text(),'{type_name} /')]]")

        # 選填
    add_public = (By.XPATH, "//input[@data-bind = 'value: apppubkey']")                # 签名公钥
    add_back_address = (By.XPATH, "//input[@data-bind = 'value: callback']")           # 回调地址
    add_shop_address = (By.XPATH, "//input[@data-bind = 'value: shopurl']")            # 商城地址

    add_enable = (By.XPATH, "//input[@data-bind = 'radio: status' and @value = '1']")  # 签名公钥
    add_disable = (By.XPATH, "//input[@data-bind = 'radio: status' and @value = '0']") # 签名公钥

    add_application_in = (By.XPATH, "//input[@value = '0' and @name = 'inout']")       # 商号用途 - 入款
    add_application_out = (By.XPATH, "//input[@value = '1' and @name = 'inout']")      # 商号用途 - 出款

    add_charge = (By.XPATH, "//input[@data-bind = 'value: charge']")                   # 手续费
    add_limit = (By.XPATH, "//input[@data-bind = 'value: limit']")                     # 收款限额
    add_min = (By.XPATH, "//input[@data-bind = 'value: minamount']")                   # 单次最低
    add_max = (By.XPATH, "//input[@data-bind = 'value: maxamount']")                   # 单次最高
    add_sort = (By.XPATH, "//input[@data-bind = 'value: sort']")                       # 排序

    def add_member_list(self, index):
        return (By.XPATH, "(//input[contains(@data-bind, 'levelcodes')])[{}]".format(index))    # 会员级别

    btn_save = (By.XPATH, "//*[text() = '保存']")  # 保存
    add_success = (By.XPATH, "//div[@id='toast-container']")  # 成功
    
    # 警示設定
    check_box = (By.XPATH, "//input[@data-bind = 'checked: autodisable']")
    success_template = (By.XPATH, "//div[@class = 'toast-success']")

    # 在線商號 - 入款商號
    in_account = (By.XPATH, "//a[@aria-expanded = 'true']") # 入款商號table
    in_row_count = (By.XPATH, "//tr[contains(@data-bind, '0') and contains(@data-bind, 'if: inout==')]") # 行數
    in_searching_data = (By.XPATH, "//tbody[contains(@data-bind, 'foreach: items')]/tr[1]/td") 

    
    def column_revise(self, column):            
        return (By.XPATH, "(//a[contains(@data-bind, 'encodeURIComponent')])[{}]".format(column)) # list of 修改按鈕

    def column_warning_setting(self, column):   
        return (By.XPATH, "(//a[contains(@data-bind, 'getNotify')])[{}]".format(column))                 # list of 警示設定

    def column_delete(self, column):            
        return (By.XPATH, "(//a[contains(@data-bind, 'del')])[{}]".format(column))                       # list of 刪除

    delete_submit = (By.LINK_TEXT, "确定")

    # 在線商號 - 出款商號
    out_account = (By.XPATH, "//a[@aria-expanded = 'false']")
    out_row_count = (By.XPATH, "//tr[contains(@data-bind, '1') and contains(@data-bind, 'if: inout==')]")



    page_count = (By.XPATH, "//div[contains(@class,'active in')]/*//span[@data-bind='text: pager.total']")   # 紀錄數量
    number_per_page = (By.XPATH, "//*[@class='input-sm']")                                       # 頁數dropdown

class OnlineMerchantPage(BasePage):
    # 點擊 入款/出款 商號
    def check_section(self, page='in'):
        if page == 'in':
            self.click(OnlineMerchantPageLocator.in_account)
        else:
            self.click(OnlineMerchantPageLocator.out_account)

    # 查詢特定銀行帳號行數
    def check_row(self, name, page='in'):
        
        if page == 'in':
            record = int(self.get_text_by_dom(self.find_element(OnlineMerchantPageLocator.page_count)))
        else:
            record = int(self.get_text_by_dom(self.find_element(OnlineMerchantPageLocator.page_count)))
        
        self.search_merchant(name=name)

        page_num = record / 25 + 1
        if page_num > int(page_num):
            page_num = page_num + 1

        page_num = int(page_num)

        if page == 'in':
            for j in range(1, page_num):
                if j > 1:
                    next_page = (By.XPATH, "(//a[contains(@data-bind,'text: label') and text()='{}'])[1]".format(j))
                    self.click(next_page)
                for i in range(0, len(self.find_elements(OnlineMerchantPageLocator.in_row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td[3]".format(i + 1))
                    if name == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)
        else:
            for j in range(1, page_num):
                if j > 1:
                    next_page = (By.XPATH, "(//a[contains(@data-bind,'text: label') and text()='{}'])[2]".format(j))
                    self.click(next_page)
                for i in range(0, len(self.find_elements(OnlineMerchantPageLocator.out_row_count))):
                    check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td[2]".format(i + 1))
                    if name == self.get_text_by_dom(self.find_element(check)):
                        return (i + 1)
            
        return -1

    # 查找特定在線商號
    def search_merchant(self, account='', name=''):
        self.wait_loading_finish()

        if account != '':
            self.click(OnlineMerchantPageLocator.search_account)
            self.type(OnlineMerchantPageLocator.search_account, account)
        if name != '':
            self.click(OnlineMerchantPageLocator.search_name)
            self.type(OnlineMerchantPageLocator.search_name, name)
        try:
            self.click(OnlineMerchantPageLocator.activate_all)
        except:
            pass
        self.click(OnlineMerchantPageLocator.btn_search)
        self.wait_loading_finish()
        self.sleep(1)
    
    # 新增銀行
    def add_online_marchant(self, name='', number='', code='', key='', count=8, page='in', type_name=''):
        self.wait_loading_finish()
        for loop in range(0, 4):
            if self.wait_visibility_status(OnlineMerchantPageLocator.btn_add) == True:
                self.click(OnlineMerchantPageLocator.btn_add)
                break
            if loop == 4:
                raise EOFError('點擊新增按鈕錯誤')
            self.sleep(2)
        self.wait_loading_finish()

        # Bot_Account = datetime.datetime.now().strftime('00000_bot%m%d_' + str(random.randrange(1, 10000)))
        self.wait_visibility(OnlineMerchantPageLocator.add_name) # 等待新增頁面開啟
        self.click(OnlineMerchantPageLocator.select_type(self, type_name))
        self.type(OnlineMerchantPageLocator.add_name, name)
        self.type(OnlineMerchantPageLocator.add_payment_code, "365支付网银")
        self.click(OnlineMerchantPageLocator.select_payment_code)
        self.type(OnlineMerchantPageLocator.add_account, number)
        self.type(OnlineMerchantPageLocator.add_code, code)
        self.type(OnlineMerchantPageLocator.add_secret, key)

        if page == 'in':
            self.click(OnlineMerchantPageLocator.add_application_in)
        else:
            self.click(OnlineMerchantPageLocator.add_application_out)

        for i in range (1, count):
            self.click(OnlineMerchantPageLocator.add_member_list(self, i))
        
        self.click(OnlineMerchantPageLocator.btn_save)

        for loop in range(0, 3):
            if self.is_element_finded(OnlineMerchantPageLocator.add_success):
                message = self.get_text(OnlineMerchantPageLocator.add_success)
                assert str(message).__contains__("已新增"), "Error:%s" % message
                break
            else:
                self.sleep(0.5)

            if loop == 2:
                raise EOFError('Toast message not found')

        self.wait_loading_finish()
        self.sleep(3)

        # return Bot_Account

    # 查詢功能
    def check_search(self, account, name, page='in'):
        
        self.check_section(page=page)
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        if page == 'in':
            assert row != -1, "入款查找發生錯誤"
        else:
            assert row != -1, "出款查找發生錯誤"

    # 修改銀行
    def change_merchant_info(self, account, name, page='in'):
        # 查詢並抓取所在列數
        self.check_section(page=page)        
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        # 抓修改前的資料
        info = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td".format(row))
        old_datas = self.find_elements(info)

        max_amount = (By.XPATH, "(//span[contains(@data-bind, '+ maxamount')])[{}]".format(row)) # 單次最高

        # 點擊修改
        self.click(OnlineMerchantPageLocator.column_revise(self, row))
        self.wait_loading_finish()

        # 改 收款額度
        if max_amount == '0':
            self.type(OnlineMerchantPageLocator.add_max, 10000)
        else:
            self.type(OnlineMerchantPageLocator.add_max, 0)

        # 改 啟用狀態
        if old_datas[7] == "已启用":
            self.click(OnlineMerchantPageLocator.add_disable)
        else:
            self.click(OnlineMerchantPageLocator.add_enable)
        
        # 改 會員級別
        self.click(OnlineMerchantPageLocator.add_member_list(self, 3))

        # 改 排序
        if old_datas[9] == "0":
            self.type(OnlineMerchantPageLocator.add_sort, 1)
        else:
            self.type(OnlineMerchantPageLocator.add_sort, 0)
        
        # 儲存修改
        self.click(OnlineMerchantPageLocator.btn_save) # 必填會讓它需要點兩下
        self.click(OnlineMerchantPageLocator.btn_save)

        self.wait_loading_finish()
        

        # 查詢並抓取所在列數
        self.check_section(page=page)        
        self.search_merchant(account=account)
        row = self.check_row(name, page)
        
        # 抓修改後的資料
        info = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td".format(row))
        new_datas = self.find_elements(info)
        
        # 判斷
        assert old_datas[6] != new_datas[6], "修改 收款額度 發生錯誤"
        assert old_datas[7] != new_datas[7], "修改 啟用狀態 發生錯誤"
        assert old_datas[8] != new_datas[8], "修改 會員級別 發生錯誤"
        assert old_datas[9] != new_datas[9], "修改 排序 發生錯誤"


    # 修改警示設定
    def change_merchant_warning_setting(self, account, name, page='in'):
        self.wait_loading_finish()

        # 查詢並抓取所在列數
        self.check_section(page=page)        
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        # 點擊修改
        self.click(OnlineMerchantPageLocator.column_warning_setting(self, row))
        self.wait_loading_finish()

        # 抓修改前的資料
        info = (By.XPATH, "//input[@data-bind='value: interval']")
        self.wait_visibility(info)
        old_datas = self.find_element(info).get_attribute('value')
        
        # 修改
        self.type(info, 1)
        self.click(OnlineMerchantPageLocator.btn_save)
        self.wait_loading_finish()

        # 查詢並抓取所在列數
        self.check_section(page=page)        
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)
        self.sleep(5)
        # 點擊修改
        self.click(OnlineMerchantPageLocator.column_warning_setting(self, row))
        self.wait_loading_finish()

        # 抓修改後的資料
        info = (By.XPATH, "//input[@data-bind='value: interval']")
        self.wait_visibility(info)
        new_datas = self.find_element(info).get_attribute('value')
        self.click(OnlineMerchantPageLocator.btn_save)
        self.wait_loading_finish()

        # 判斷
        assert new_datas != old_datas, "警示設定發生錯誤"

    # 刪除銀行
    def delete_merchant_sort(self, account, name, page='in'):
        self.wait_loading_finish()
        self.sleep(1)
        # 查詢並抓取所在列數
        self.check_section(page=page)        
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        # 刪除
        self.click(OnlineMerchantPageLocator.column_delete(self, row))
        self.click(OnlineMerchantPageLocator.delete_submit)
        
        self.wait_loading_finish()
        self.sleep(3)

    # 檢查刪除功能
    def check_delete(self, account, name, page='in'):
        self.check_section(page=page)        
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        assert row == -1, "刪除發生錯誤"

    # 讀取收款資訊 比較 存款前後的數值差異
    def get_withdraw_info(self, account, name, page='in'):

        # 查詢
        self.search_merchant(account=account, name=name)
        row = self.check_row(name, page)

        searching_data = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td".format(row))
        datas = self.find_elements(searching_data)
        
        bank_withdraw_count = self.get_text_by_dom(datas[4])
        bank_withdraw_number = self.get_text_by_dom(datas[5])

        return bank_withdraw_count, bank_withdraw_number