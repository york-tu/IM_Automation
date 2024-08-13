from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class TicketCheckPageLocator:
    # ===============注單校驗頁面===============
    note_check_page = (By.XPATH, "//a[contains(text(),'注单校验')]") # 注單校驗頁面

    ticket_number_input_box = (By.XPATH, "//div[@id='tab_1_2']//input[@data-bind='value: filter.number']")         # 訂單號碼輸入
    validation_id_input_box = (By.XPATH, "//div[@id='tab_1_2']//input[@data-bind='value: filter.validationid']")   # 校驗碼輸入
    btn_search_checkpage = (By.XPATH, "//div[@id='tab_1_2']//button[@id='btnSearch']")                             # 注單校驗頁面-查找按鈕

    # ===============列表區===============
    add_time = (By.XPATH, "//td[@data-bind='text: addedtime']")         # 下注時間
    ticket_number = (By.XPATH, "//td[@data-bind='text: number']")       # 單號
    validation_id = (By.XPATH, "//td[@data-bind='text: validationid']") # 驗證碼

    btn_valid = (By.XPATH, "//a[@data-bind='confirm: function() { $parent.checkValidation($data.number); }']") # 操作-驗證按鈕
    btn_confirm = (By.XPATH, "//a[@data-apply='confirmation']")                                                # 操作-驗證-確定按鈕

    valid_success_message = (By.XPATH, "//div[contains(text(), '效验成功')]")

class TicketCheckPage(BasePage):

    # ============注單校驗頁面============
    def ticket_number_check(self, ticketnumber): # 輸入單號查詢
        self.click(TicketCheckPageLocator.note_check_page)
        self.wait_loading_finish()
        self.type(TicketCheckPageLocator.ticket_number_input_box, ticketnumber)
        self.click(TicketCheckPageLocator.btn_search_checkpage)
        self.wait_loading_finish()
        addtime = self.get_text(TicketCheckPageLocator.add_time)
        ticketnumber_list = self.get_text(TicketCheckPageLocator.ticket_number)
        validationid = self.get_text(TicketCheckPageLocator.validation_id)
        assert ticketnumber_list == ticketnumber, "單號比對錯誤"
        
        self.validationid_check(validationid) # 輸入校驗碼查詢

    def validationid_check(self, valid_id):  # 輸入校驗碼查詢
        self.type(TicketCheckPageLocator.ticket_number_input_box, "")
        self.type(TicketCheckPageLocator.validation_id_input_box, "")
        self.click(TicketCheckPageLocator.btn_search_checkpage)
        
        self.type(TicketCheckPageLocator.validation_id_input_box, valid_id)
        self.click(TicketCheckPageLocator.btn_search_checkpage)
        self.wait_loading_finish()
        validationid = self.get_text(TicketCheckPageLocator.validation_id)
        assert valid_id == validationid, "校驗碼比對錯誤"
        
        self.click_valid() # 對該筆資料作驗證操作

    def click_valid(self): # 操作驗證
        self.click(TicketCheckPageLocator.btn_valid)
        self.wait_loading_finish()
        self.click(TicketCheckPageLocator.btn_confirm)
        self.wait_loading_finish()
        assert self.is_element_finded(TicketCheckPageLocator.valid_success_message), "沒出現驗證成功訊息"