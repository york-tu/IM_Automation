from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random


class OnlineBankAcconut_PageLocator(BasePage):
    # SEARCH AREA (查找條件區)
    bank_account_add = (By.CSS_SELECTOR, "a.btn.btn-default.btn-sm > i.fa.fa-plus")
    bank_name = (By.XPATH, "//*[@data-bind='value: name']")  # 開戶商號
    search_allsort = (By.XPATH, "//button[contains(text(),'查找')]")  # 查找
    search_branch = (By.XPATH, "//input[@data-bind='value: filter.name']")  # 開戶支行搜尋關鍵字
    bank_limit = (By.XPATH, "//*[@class='form-control input-inline input-medium']")  # 收款金額
    bank_submit = (By.XPATH, "//*[@class='btn blue']")  # 保存送出
    delete_allsort = (By.LINK_TEXT, "删除")  # 移除銀行類型
    delete_sort_submit = (By.LINK_TEXT, "确定")  # 確認刪除
    submit_success = (By.XPATH, "//div[@id='toast-container']")
    bank_number_page = (By.XPATH, "//*[@class='input-sm']")
    check_bank_sort_name = (By.XPATH,"//tbody[@data-bind='foreach: items']//tr")

    # 新增條件區
    search_bank_sort = (By.XPATH, "//select[contains(@data-bind,'categoryOptions')]")  # 所屬分類
    transfermethod = (By.XPATH, "//*[@class='select2-chosen' and @id='select2-chosen-4']") # 支付方式
    transfermethod_searchbox = (By.XPATH, "//*[@class='select2-search']//input[@id='s2id_autogen4_search']") # 支付方式搜尋框
    pay_gateway = (By.XPATH, "//*[@class='select2-container form-control select2me' and @id = 's2id_autogen5']")  # 支付網關
    pay_gateway_searchbox = (By.XPATH, "//*[@class='select2-search']//input[@id='s2id_autogen6_search']")  # 支付網關搜尋框
    store_number = (By.XPATH, "//*[@class='form-control' and @data-bind='value: account']")  # 商家編號
    terminal = (By.XPATH, "//*[@class='form-control' and @data-bind='value: appkey']")  # 終端機
    private_sign = (By.XPATH, "//*[@class='form-control' and @data-bind='value: appsecret']")  # 簽名密鑰
    public_sign = (By.XPATH, "//*[@class='form-control' and @data-bind='value: apppubkey']")  # 簽名公鑰
    callback_address = (By.XPATH, "//*[@class='form-control' and @data-bind='value: callback']")  # 回調地址
    available_amount = (By.XPATH, "//div[@class='row']/div[@class='col-md-2'][1]//input")  # 可用金額的第一格
    range_amount = (By.XPATH, "//div[@data-bind='foreach: depositRangeAmountList']//input") # 入款金额区间设定
    iframe_1 = (By.XPATH, "//iframe[@title='所见即所得编辑器, editor1']")  # 入款金额区间说明
    iframe_2 = (By.XPATH, "//iframe[@title='所见即所得编辑器, editor2']")  # 入款金额选取说明
    iframe_3 = (By.XPATH, "//iframe[@title='所见即所得编辑器, editor3']")  # 确认入款二次弹窗说明
    iframe_body = (By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")


    # 銀行欄位確認
    def bank_sort_name_check(self, name):
        self.wait_loading_finish()
        bank_sort_name = (By.XPATH, "//td[contains(text(),'%s')]" % name)
        self.wait_visibility(OnlineBankAcconut_PageLocator.check_bank_sort_name)
        message = self.get_text(bank_sort_name)
        assert str(message).__contains__(name), '新增失敗,欄位無:%s 類別' % name

    # 帳號類型
    sort_bank = (By.XPATH, "//div[@data-bind='foreach: subitems']/*[@class='radio-inline']")
    sort_bank_all = (By.XPATH, "//div[@data-bind='foreach: subitems']")
    def _sort_bank_c(self, bankname):
        for ele in range(1, len(self.find_elements(OnlineBankAcconut_PageLocator.sort_bank))+1):
            sort_bank = (By.XPATH, "//div[@data-bind='foreach: subitems']/*[@class='radio-inline'][%d]" % ele)  # 帳號類型

            if self.get_text(sort_bank) == bankname:
                self.click(sort_bank)
                break
        message = self.get_text(OnlineBankAcconut_PageLocator.sort_bank_all)
        assert str(message).__contains__(bankname), '切換商號類型時，所屬分類未成功切換'
    
    # 商號類型
    store_type = (By.XPATH, "//label[text()='商号类型']/../div/label")
    def _store_type(self,store_type_name):
        for ele in range(1, len(self.find_elements(OnlineBankAcconut_PageLocator.store_type))+1):
            store_type = (By.XPATH, "//label[text()='商号类型']/../div/label[%d]" % ele)  # 帳號類型

            if store_type_name in self.get_text(store_type):
                self.click(store_type)
                break

    # 會員級別
    def _level_click(self):
        level = (By.XPATH, "//label[text()= '会员级别']/..//*[@class='checkbox-inline  text-control']")
        for i in self.find_elements(level):
            self.click_by_dom(i)

class OnlinePay_Branch_Page(BasePage):
    # 分類搜尋
    def search_bank(self, bank_sort, branch, status='2'):
        self.wait_loading_finish()
        self.sleep(1)
        
        for loop in range(0,3):
            try:
                self.select_by_text(OnlineBankAcconut_PageLocator.search_bank_sort, bank_sort)
                break
            except:
                pass

            if loop == 2:
                raise EOFError('頁面找不到所屬分類下拉式選單')

        self.type(OnlineBankAcconut_PageLocator.search_branch, branch)
        self.click((By.XPATH, f"(//label[text()='启用状态']/../div[1]//input)[{status}]"))
        self.wait_loading_finish()
        self.wait_visibility(OnlineBankAcconut_PageLocator.search_allsort)
        self.sleep(1)
        self.click(OnlineBankAcconut_PageLocator.search_allsort)
        self.wait_loading_finish()
        # self.select_by_index(OnlineBankAcconut_PageLocator.bank_number_page, 3)
        # self.scroll_to_top()


    # 刪除銀行
    def delete_bank_sort(self, bank_sort, branch):
        OnlinePay_Branch_Page.search_bank(self, bank_sort, branch, status='1')
        self.sleep(1)

        if self.is_element_finded(OnlineBankAcconut_PageLocator.delete_allsort) is False:
            return
            
        for _ in range(len(self.find_elements(OnlineBankAcconut_PageLocator.delete_allsort))):
            self.wait_visibility(OnlineBankAcconut_PageLocator.delete_allsort)

            assert self.is_element_finded(OnlineBankAcconut_PageLocator.delete_allsort) == True, "移除銀行類型欄位未找到."
           
            self.click(OnlineBankAcconut_PageLocator.delete_allsort)
            self.wait_visibility(OnlineBankAcconut_PageLocator.delete_sort_submit)
            
            assert self.is_element_finded(OnlineBankAcconut_PageLocator.delete_sort_submit) == True, "確認刪除BTN未找到."

            self.click(OnlineBankAcconut_PageLocator.delete_sort_submit)
            self.sleep(1)
            OnlinePay_Branch_Page.search_bank(self, bank_sort, branch, status='1')


    # 新增銀行
    def add_sort_bank(self, name, money, style, pay_gateway, private_key, public_key='', bot_id='', callback_address='', transfermethod='', store_type='线上支付', available_amount='', range_amount=''):
        self.wait_loading_finish()
        self.wait_visibility(OnlineBankAcconut_PageLocator.bank_account_add)
        self.wait_loading_finish()
        self.click(OnlineBankAcconut_PageLocator.bank_account_add)
        self.wait_loading_finish()
        self.wait_visibility(OnlineBankAcconut_PageLocator.bank_name)
        self.sleep(1)
        
        if bot_id == '':
            bot_id = datetime.datetime.now().strftime('00000_bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))

        for loop in range(0,3):
            self.sleep(2)
            if self.is_element_finded(OnlineBankAcconut_PageLocator.bank_name) is True:
                OnlineBankAcconut_PageLocator._store_type(self, store_type)
                self.wait_loading_finish()
                OnlineBankAcconut_PageLocator._sort_bank_c(self, style)
                self.wait_loading_finish()
                self.click(OnlineBankAcconut_PageLocator.transfermethod)
                self.type(OnlineBankAcconut_PageLocator.transfermethod_searchbox, transfermethod)
                self.type_enter(OnlineBankAcconut_PageLocator.transfermethod_searchbox)
                self.type(OnlineBankAcconut_PageLocator.bank_name, name)
                self.click(OnlineBankAcconut_PageLocator.pay_gateway)
                self.type(OnlineBankAcconut_PageLocator.pay_gateway_searchbox, pay_gateway)
                self.type_enter(OnlineBankAcconut_PageLocator.pay_gateway_searchbox)
                self.type(OnlineBankAcconut_PageLocator.store_number, bot_id)
                self.type(OnlineBankAcconut_PageLocator.terminal, bot_id)
                self.type(OnlineBankAcconut_PageLocator.private_sign, private_key)
                self.type(OnlineBankAcconut_PageLocator.public_sign, public_key)
                self.type(OnlineBankAcconut_PageLocator.callback_address, callback_address)

                # 可用金额
                if available_amount != '':
                    self.type(OnlineBankAcconut_PageLocator.available_amount, available_amount)
               
                if store_type == '顺付WellPay-我要买':
                    # 入款金额区间设定
                    amounts_inputs = self.find_elements(OnlineBankAcconut_PageLocator.range_amount)
                    for i in range(0, len(amounts_inputs)):
                        self.type_by_dom(amounts_inputs[i], range_amount[i])
                    # 入款說明
                    self.switch_frame(OnlineBankAcconut_PageLocator.iframe_1)
                    self.type(OnlineBankAcconut_PageLocator.iframe_body, name + " 入款金额区间说明")
                    self.switch_default_frame()
                    self.switch_frame(OnlineBankAcconut_PageLocator.iframe_2)
                    self.type(OnlineBankAcconut_PageLocator.iframe_body, name + " 入款金额选取说明")
                    self.switch_default_frame()
                    self.switch_frame(OnlineBankAcconut_PageLocator.iframe_3)
                    self.type(OnlineBankAcconut_PageLocator.iframe_body, name + " 确认入款二次弹窗说明")
                    self.switch_default_frame()

                self.type(OnlineBankAcconut_PageLocator.bank_limit, money)
                OnlineBankAcconut_PageLocator._level_click(self)
                self.click(OnlineBankAcconut_PageLocator.bank_submit)
                break
            else:
                if loop == 2:
                    raise EOFError('找不到新增銀行頁面輸入欄位')

                self.refresh_browser()
                self.wait_loading_finish()
                
                
        # message = self.get_text(OnlineBankAcconut_PageLocator.submit_success)
        # assert str(message).__contains__("已新增"), "Error:%s" % message

        self.wait_loading_finish()

