from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class NewAgentSettlementPageLocator:
    # 查找條件
    
    today_btn = (By.XPATH, "//*[@id='search']/div/div[1]/button[1]")      # 今日按鈕
    yesterday_btn = (By.XPATH, "//*[@id='search']/div/div[1]/button[2]")  # 昨日按鈕
    month_btn = (By.XPATH, "//*[@id='search']/div/div[1]/button[5]")      # 本月按鈕
    last_month_btn = (By.XPATH, "//*[@id='search']/div/div[1]/button[6]") # 上月按鈕

    withdraw_input = (By.XPATH, "//input[contains(@placeholder,'提现会员')]") # 提現會員輸入欄位
    number_input = (By.XPATH, "//input[contains(@placeholder,'业务编号')]")   # 業務編號輸入欄位

    # radio_all = (By.XPATH, "//input[contains(@value,'')]")        # 不指定
    radio_failed = (By.XPATH, "//input[contains(@value,'0')]")      # 未達門檻
    radio_reached = (By.XPATH, "//input[contains(@value,'1')]")     # 已達門檻
    radio_processing = (By.XPATH, "//input[contains(@value,'2')]")  # 出款處理中
    radio_paid = (By.XPATH, "//input[contains(@value,'3')]")        # 已出款
    radio_already = (By.XPATH, "//input[contains(@value,'4')]")     # 已掛帳
    radio_accumulated = (By.XPATH, "//input[contains(@value,'5')]") # 已累積
    radio_cleared = (By.XPATH, "//input[contains(@value,'6')]")     # 已清帳

    search_btn = (By.XPATH, "//*[@id='btnSearch']") # 查詢按鈕

    # 結算列表
    data_table = (By.XPATH, "//table[contains(@class,'table-striped')]")

    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: id')]")                             # 業務編號
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: sharelogin')]")                     # 股東
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: generalagent')]")                   # 總代理
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: agent')]")                          # 代理
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: levelname')]")                      # 層級
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: bindingmember')]")                  # 提現會員
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: typename')]")                       # 類型
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: agreementname')]")                  # 占成/退傭方案
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: cyclename')]")                      # 周期
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: moment(agreementstarttime)')]")     # 起始時間
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: moment(agreementendtime)')]")       # 結算時間
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: statusname')]")                     # 狀態
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: income')]")                         # 收入
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: payout')]")                         # 支出
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: revenue')]")                        # 總收益
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: createdtime')]")                    # 生成時間
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: accepttime')]")                     # 確定時間
    # searching_number = (By.XPATH, "//span[contains(@data-bind,'text: updatedtime')]")                    # 更新時間

    dropdown_page = (By.XPATH, "//select[contains(@data-bind,'value: pager.pageSize')]")                 # 每頁幾筆
    dropdown_page_25 = (By.XPATH, "//select[contains(@data-bind,'value: pager.pageSize')]/option[text()='25']")                 # 每頁幾筆


    # 結算列表
    searching_data = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td") # 第一筆資料(最後下注的資料)
    
    detail = (By.XPATH, "(//a[contains(text(),'明细总览')])[1]") # 明細總攬按鈕
    detail_table_info = (By.XPATH, "//td") # table 格式

    channel_detail = (By.XPATH, "(//a[contains(text(),'频道明细总览')])[1]") # 頻道明細總攬按鈕
    channel_table_info = (By.XPATH, "//td") # table 格式
    back_button = (By.XPATH, "//a[contains(text(),'返回上一层')]") # 返回上一層按鈕

    rent_detail = (By.XPATH, "(//a[contains(text(),'第三方租金明细')])[1]") # 第三方租金明細按鈕
    rent_table_info = (By.XPATH, "//td") # table 格式

    total_record = (By.XPATH, "//span[contains(@data-bind, 'pager.total')]") # 總資料筆數
    the_first_page = (By.XPATH, "//a[contains(@href, 'javascript:void(0)') and text()='1']") # 第一頁按鈕
    last_page = (By.XPATH, "//a[contains(@href, 'javascript:void(0)') and text()='尾页']") # 尾頁按鈕

    # iframe
    frame = (By.XPATH, "//iframe[@id='dialog-content']") # 框
    close_btn = (By.XPATH, "//button[@class='close']") # 叉叉
    word_valid_member = (By.XPATH, "//*[contains(text(), '营收区间')]") # 營收區間
    word_create_time = (By.XPATH, "//*[contains(text(), '新增时间')]")  # 新增時間


class NewAgentSettlePage(BasePage):

    def try_parse_string_to_float(self, data:str):
        try:
            data = float(data.replace(',', ''))
            return data
        except:
            return data

    # 檢查查詢列表資料筆數對應的頁數是否正常
    def check_page_total(self):
        assert self.wait_visibility_status(NewAgentSettlementPageLocator.last_month_btn) is True, "進入代理結算(新版)錯誤"
        # 查詢
        self.click(NewAgentSettlementPageLocator.last_month_btn)
        self.click(NewAgentSettlementPageLocator.search_btn)
        self.wait_loading_finish()
        self.scroll_to_bottom()
        self.sleep(5)
        assert self.wait_visibility_status(NewAgentSettlementPageLocator.total_record) is True, "顯示紀錄錯誤(無顯示紀錄數量)"
        record_count = int(self.get_text(NewAgentSettlementPageLocator.total_record))

        if record_count != 0:
            self.click(NewAgentSettlementPageLocator.dropdown_page)
            self.click(NewAgentSettlementPageLocator.dropdown_page_25)

            count_per_page = 25

            # 計算應該有幾頁
            if record_count % count_per_page == 0:
                page_count = int(record_count / count_per_page)
            else:
                page_count = int(record_count / count_per_page) + 1

            # 當總頁數大於2時的情況
            if page_count > 1:
                assert self.wait_visibility_status(NewAgentSettlementPageLocator.the_first_page) is True, "顯示紀錄錯誤(第一頁無顯示)"
                assert self.wait_visibility_status(NewAgentSettlementPageLocator.last_page) is True, "顯示頁數錯誤(末頁無顯示)"
                self.click(NewAgentSettlementPageLocator.last_page)
                self.wait_loading_finish()
                self.sleep(5)
                # assert self.wait_invisibility(NewAgentSettlementPageLocator.last_page) is True, "顯示頁數錯誤(末頁不該顯示)"
                the_last_page = (By.XPATH, "//a[contains(@href, 'javascript:void(0)') and text()='{}']".format(page_count))
                assert self.wait_visibility_status(the_last_page) is True, "顯示頁數錯誤(頁數和紀錄數量有誤)"

    # 查詢 並 取得查詢的資料
    def get_searching_data_list(self, program, number):
        # 查詢
        self.scroll_to_top()
        self.sleep(1)
        self.click(NewAgentSettlementPageLocator.month_btn)
        self.click(NewAgentSettlementPageLocator.search_btn)
        self.wait_loading_finish()
        
        # 列出第一行資料
        data_list = []
        datas = self.find_elements(NewAgentSettlementPageLocator.searching_data)

        for index, data in enumerate(datas):
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            if index != 0 and index < 14:
                data_list.append(data)
            elif index == 14:
                data_list.append(data.replace(' ', ''))
            
        return data_list

    # 取得該筆資料的明細總攬
    def get_detail_table_data(self):
        # 點擊明細總攬
        self.wait_loading_finish()
        self.click(NewAgentSettlementPageLocator.detail) 
        self.wait_visibility(NewAgentSettlementPageLocator.frame)
        self.switch_frame("dialog-content")
        for _ in range(0, 2):
            if self.wait_visibility(NewAgentSettlementPageLocator.word_valid_member) is True:
                break
            self.sleep(1)

        # 列出明細總攬資料
        data_list = []
        datas = self.find_elements(NewAgentSettlementPageLocator.detail_table_info)
        for _, data in enumerate(datas):
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            data_list.append(data)
        
        self.switch_default_frame()
        self.click(NewAgentSettlementPageLocator.close_btn)
        return data_list

    # 取得該筆資料的頻道明細總攬
    def get_channel_detail_table_data(self):
        # 點擊
        self.wait_loading_finish()
        self.sleep(2)
        self.click(NewAgentSettlementPageLocator.channel_detail)
        self.wait_visibility(NewAgentSettlementPageLocator.frame)
        self.switch_frame("dialog-content")

        for _ in range(0, 2):
            if self.wait_visibility(NewAgentSettlementPageLocator.word_create_time) is True:
                break
            self.sleep(1)

        # 列出頻道明細總攬資料
        data_list = []
        # 第一層資料
        datas = self.find_elements(NewAgentSettlementPageLocator.channel_table_info)

        for data in datas:
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            data_list.append(data)
        
        # 第二層資料
        channel_product_detail = (By.XPATH, "//a[contains(text(), '产品明细')]")
        length = len(self.find_elements(channel_product_detail))

        for i in range(2, length + 1):
            catch_button = (By.XPATH, f"(//a[contains(text(),'产品明细')])[{i}]")
            self.click(catch_button)
            self.wait_loading_finish()

            datas = self.find_elements(NewAgentSettlementPageLocator.channel_table_info)
            for data in datas: 
                data = self.try_parse_string_to_float(self.get_text_by_dom(data))
                data_list.append(data)

            self.click(NewAgentSettlementPageLocator.back_button)

            
        self.switch_default_frame()
        self.click(NewAgentSettlementPageLocator.close_btn)

        return data_list

    # 取得該筆資料的第三方租金明細
    def get_third_party_rent_table_data(self):
        # 點擊
        self.wait_loading_finish()
        self.sleep(2)
        self.click(NewAgentSettlementPageLocator.rent_detail)
        self.wait_visibility(NewAgentSettlementPageLocator.frame)
        self.switch_frame("dialog-content")
        for _ in range(0, 2):
            if self.wait_visibility_status(NewAgentSettlementPageLocator.word_create_time) is True:
                break
            self.sleep(1)

        # 列出第三方租金明細資料
        data_list = []
        datas = self.find_elements(NewAgentSettlementPageLocator.rent_table_info)
        for data in datas:
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            data_list.append(data)
    
        self.switch_default_frame()
        self.click(NewAgentSettlementPageLocator.close_btn)

        return data_list
