from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage

class NewSettlementPageLocator:

    search_commision = (By.XPATH, "//a[text()='代理结算查询']") # 查詢頁面
    add_commision = (By.XPATH, "//a[text()='代理结算生成']")    # 生成頁面

    # 代理結算生成
    commision_selection_adding = (By.XPATH, "//div[contains(@id,'add')]//select[contains(@data-bind, 'commItems')]") # 退傭方案
    today_btn_adding = (By.XPATH, "//div[contains(@id,'add')]//button[contains(text(), '今日')]")                    # 今日按鈕
    add_btn = (By.XPATH, "//button[contains(text(), '生成')]")                                                       # 生成按鈕

    # 代理結算查詢
    today_btn_searching = (By.XPATH, "//div[contains(@id,'search')]//button[contains(text(), '今日')]") # 今日按鈕
    month_btn_searching = (By.XPATH, "//div[contains(@id,'search')]//button[contains(text(), '本月')]") # 本月按鈕
    last_month_btn_searching = (By.XPATH, "//div[contains(@id,'search')]//button[contains(text(), '上月')]") # 上月按鈕
    commision_selection_searching = (By.XPATH, "//div[contains(@id, 'search')]//select[contains(@data-bind, 'commItems')]") # 退傭方案
    search_btn_searching = (By.XPATH, "//div[contains(@id, 'search')]//*[@id='btnSearch']") # 查找按鈕

    # 結算列表
    close_btn_searching = (By.XPATH, "//button[@class='close']") # 叉叉
    searching_data = (By.XPATH, "(//tr[contains(@data-bind, 'css: { info: checked }')])[1]/td") # 第一筆資料(最後下注的資料)
    
    detail = (By.XPATH, "(//a[contains(text(), '明细总览')])[1]") # 明細總攬按鈕
    detail_table_info = (By.XPATH, "//td") # table 格式

    channel_detail = (By.XPATH, "(//a[contains(text(), '频道明细总览')])[1]") # 頻道明細總攬按鈕
    channel_table_info = (By.XPATH, "//td") # table 格式
    back_button = (By.XPATH, "//a[contains(@href, '/agentsettlement/')]") # 返回上一層按鈕

    rent_detail = (By.XPATH, "(//a[contains(text(), '第三方租金明细')])[1]") # 第三方租金明細按鈕
    rent_table_info = (By.XPATH, "//td") # table 格式
    
    frame = (By.XPATH, "//iframe[@id='dialog-content']") # 框
    # 特定文字
    word_valid_member = (By.XPATH, "//*[contains(text(), '营收区间')]") # 營收區間
    word_create_time = (By.XPATH, "//*[contains(text(), '新增时间')]")  # 新增時間


class NewSettlementPage(BasePage):

    def try_parse_string_to_float(self, data:str):
        try:
            data = float(data.replace(',', ''))
            return data
        except:
            return data

    # 生成代理結算
    def add_agent_settlement(self, program):
        self.wait_loading_finish()
        assert self.wait_visibility_status(NewSettlementPageLocator.add_commision), "進入頁面錯誤"
        self.click(NewSettlementPageLocator.add_commision)
        self.click(NewSettlementPageLocator.commision_selection_adding)
        option = (By.XPATH, "//div[contains(@id, 'add')]//option[text()='{}']".format(program))
        self.sleep(1)
        self.click(option)
        self.click(NewSettlementPageLocator.today_btn_adding)
        self.click(NewSettlementPageLocator.add_btn)

    # 查詢 並 取得查詢的資料
    def get_searching_data_list(self, program):
        # 查詢
        self.wait_loading_finish()
        assert self.wait_visibility_status(NewSettlementPageLocator.search_commision), "進入頁面錯誤"
        self.click(NewSettlementPageLocator.search_commision)
        self.click(NewSettlementPageLocator.month_btn_searching)
        self.click(NewSettlementPageLocator.commision_selection_searching)
        option = (By.XPATH, "//div[contains(@id, 'search')]//option[text()='{}']".format(program))
        self.click(option)
        self.click(NewSettlementPageLocator.search_btn_searching)
        self.wait_loading_finish()
        
        # 列出第一行資料
        first_list = []
        datas = self.find_elements(NewSettlementPageLocator.searching_data)

        for index, data in enumerate(datas):
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            # if index != 0 and index != 12 and index < 16:
            if index != 0 and index != 11 and index < 15:
                if index == 10:
                    data = data.split( )[0]
                first_list.append(data)
            elif index == 15:
                data = str(data)
                first_list.append(data.replace('(美东)', '').replace(' ', ''))

        assert len(first_list) > 0, "沒有取得到遊戲的注單"
            
        return first_list, first_list[0]

    # 取得該筆資料的明細總攬
    def get_detail_table_data(self):
        # 點擊明細總攬
        self.wait_loading_finish()
        self.click(NewSettlementPageLocator.detail) 
        self.wait_visibility(NewSettlementPageLocator.frame)
        self.switch_frame("dialog-content")
        for loop in range(0, 2):
            if self.wait_visibility_status(NewSettlementPageLocator.word_valid_member) is True:
                break
            self.sleep(1)

            if loop == 1:
                raise EOFError("取得該筆資料的明細總攬錯誤")

        # 列出明細總攬資料
        detail_list = []
        datas = self.find_elements(NewSettlementPageLocator.detail_table_info)
        for data in datas:
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            detail_list.append(data)
        
        self.switch_default_frame()
        self.click(NewSettlementPageLocator.close_btn_searching)
        return detail_list

    # 取得該筆資料的頻道明細總攬
    def get_channel_detail_table_data(self):
        # 點擊
        self.wait_loading_finish()
        self.sleep(2)
        self.click(NewSettlementPageLocator.channel_detail)
        self.wait_visibility(NewSettlementPageLocator.frame)
        self.switch_frame("dialog-content")

        for loop in range(0, 2):
            if self.wait_visibility_status(NewSettlementPageLocator.word_create_time) is True:
                break
            self.sleep(1)

            if loop == 1:
                raise EOFError('取得該筆資料的頻道明細總攬錯誤')

        # 列出頻道明細總攬資料
        channel_detail_list = []
        # 第一層資料
        datas = self.find_elements(NewSettlementPageLocator.channel_table_info)

        for data in datas: 
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            channel_detail_list.append(data)
        
        # 第二層資料
        channel_product_detail = (By.XPATH, "//a[contains(text(), '产品明细')]")
        length = len(self.find_elements(channel_product_detail))

        for i in range(2, length + 1):
            catch_button = (By.XPATH, f"(//a[contains(text(), '产品明细')])[{i}]")
            self.click(catch_button)
            self.wait_loading_finish()

            datas = self.find_elements(NewSettlementPageLocator.channel_table_info)
            for data in datas: 
                data = self.try_parse_string_to_float(self.get_text_by_dom(data))
                channel_detail_list.append(data)

            self.click(NewSettlementPageLocator.back_button)

        self.switch_default_frame()
        self.click(NewSettlementPageLocator.close_btn_searching)

        return channel_detail_list

    # 取得該筆資料的第三方租金明細
    def get_third_party_rent_table_data(self):
        # 點擊
        self.wait_loading_finish()
        self.click(NewSettlementPageLocator.rent_detail)
        self.wait_visibility(NewSettlementPageLocator.frame)
        self.switch_frame("dialog-content")

        for loop in range(0,2):
            if self.wait_visibility_status(NewSettlementPageLocator.word_create_time) is True:
                break

            self.sleep(1)

            if loop == 1:
                raise EOFError('取得該筆資料的第三方租金明細錯誤')

        # 列出第三方租金明細資料
        third_side_list = []
        datas = self.find_elements(NewSettlementPageLocator.rent_table_info)
        for data in datas:
            data = self.try_parse_string_to_float(self.get_text_by_dom(data))
            third_side_list.append(data)
    
        self.switch_default_frame()
        self.click(NewSettlementPageLocator.close_btn_searching)
        return third_side_list