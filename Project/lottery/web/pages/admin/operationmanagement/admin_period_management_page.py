from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class PeriodManagementPageLocator(BasePage):
    # 查找條件
    period = (By.XPATH, "//input[@data-bind = 'value: filter.number']")             # 期數
    drawn_date = (By.XPATH, "//input[@data-bind = 'datetime: filter.drawingtime']") # 開獎日期
    state_all = (By.XPATH, "//input[@value = '-1']")                                # 開盤狀態 - 全部
    state_ = (By.XPATH, "//input[@value = '0']")                                    # 開盤狀態 - 未開盤
    state_ = (By.XPATH, "//input[@value = '1']")                                    # 開盤狀態 - 已開盤
    state = (By.XPATH, "//input[@value = '2']")                                     # 開盤狀態 - 已封盤
    button_search = (By.XPATH, '//button[contains(text(), "查找")]')                # 查找按鈕
    message = (By.XPATH, "//*[@class='toast-message']")                             # 右下角訊息

    # 帳號列表
    row_count = (By.XPATH, '//tr[contains(@data-bind, "0")]')
    # button_revise = (By.XPATH, '//a[contains(text(), "修改")]')
    def beads_result(self,index):
        return (By.XPATH, f'(//td[contains(@data-bind, "hmresult")])[{index}]')     # 修改

    def button_revise(self,index):
        return (By.XPATH, f'(//a[contains(text(), "修改")])[{index}]')     # 修改
    
    def button_payout(self,index):
        return (By.XPATH, f'(//a[contains(text(), "派彩状态")])[{index}]') # 派對狀態
    
    def button_delete(self,index):
        return (By.XPATH, f'(//input[contains(@value, "删除")])[{index}]') # 刪除
    
    def button_seal(self,index):
        return (By.XPATH, f'(//input[contains(@value, "封盘")])[{index}]') # 封盤

    def button_unseal(self,index):
        return (By.XPATH, f'(//input[contains(@value, "开盘")])[{index}]') # 开盘
    
    def button_abolishment(self,index):
        return (By.XPATH, f'(//input[contains(@value, "作废")])[{index}]') # 作廢
    
    def button_make_up(self,index):
        return (By.XPATH, f'(//input[contains(@value, "补采")])[{index}]') # 補採
    
    
    button_confirm = (By.LINK_TEXT, "确定")  # 確定
    button_cancel = (By.LINK_TEXT, "取消")   # 取消
    
    # 帳號內容
    button_add = (By.CSS_SELECTOR, "a.btn.btn-default.btn-sm > i.fa.fa-plus") # 新增

    period_date = (By.XPATH, "//input[@data-bind = 'value: number']")         # 期數
    start_time = (By.XPATH, "//input[@data-bind = 'datetime: opentime']")     # 開盤時間
    end_time = (By.XPATH, "//input[@data-bind = 'datetime: closetime']")      # 封盤時間
    beads_date = (By.XPATH, "//input[@data-bind = 'datetime: drawingtime']")  # 攪珠日期

    beads_input = (By.XPATH, "//input[contains(@data-bind, 'value: hm')]")    # 攪珠結果

    def input_beads(self,index):
        return (By.XPATH, f"//input[@data-bind = 'value: hm{index}']")

    button_resend = (By.XPATH, '//input[contains(@value, "重派")]') # 重派
    button_send = (By.XPATH, '//input[contains(@value, "派彩")]') # 派彩
    button_save = (By.XPATH, '//button[contains(text(), "保存")]')  # 保存
    button_back = (By.XPATH, '//button[contains(text(), "返回")]')  # 返回

    notice_info = (By.XPATH, '//div[contains(@class, "toast-message")]')
    

class PeriodManagementPage(BasePage):
    # 查找
    def search_period(self, period='', date=''):
        self.wait_loading_finish()
        self.wait_visibility(PeriodManagementPageLocator.period)
        assert self.is_element_finded(PeriodManagementPageLocator.period) == True, "期數欄位未找到."
        self.type(PeriodManagementPageLocator.period, period)
        # self.type(PeriodManagementPageLocator.drawn_date, date)
        self.wait_visibility(PeriodManagementPageLocator.button_search)
        assert self.is_element_finded(PeriodManagementPageLocator.button_search) == True, "查找/ 搜尋BTN未找到."
        self.click(PeriodManagementPageLocator.button_search)
        self.wait_loading_finish()

        # return len( self.find_elements(PeriodManagementPageLocator.button_revise) )
    

    # 尋找查找期數位置
    def check_row(self, period):
        self.wait_loading_finish()
        self.search_period(period=period)
        self.sleep(2)
        
        for i in range(0, len(self.find_elements(PeriodManagementPageLocator.row_count))):
            check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td[1]".format(i + 1))
            if str(period) == self.get_text_by_dom(self.find_element(check)):
                return (i + 1)
        return -1


    # 新增
    def add_period(self, period='', start='', end='', beads=''):
        self.wait_loading_finish()
        self.click(PeriodManagementPageLocator.button_add)
        self.wait_loading_finish()
        
        self.click(PeriodManagementPageLocator.start_time)
        self.type_enter(PeriodManagementPageLocator.start_time)
        self.click(PeriodManagementPageLocator.end_time)
        self.type_enter(PeriodManagementPageLocator.end_time)
        self.click(PeriodManagementPageLocator.beads_date)
        self.type_enter(PeriodManagementPageLocator.beads_date)
        self.type(PeriodManagementPageLocator.period_date, period)
        self.click(PeriodManagementPageLocator.button_save)
        self.wait_loading_finish()

        row = self.check_row(period)
        assert row != -1, "新增功能異常"
        

    # 修改
    def revise_period(self, period='', start='', end='',breads='', results=[]):
        self.wait_loading_finish()
        row = self.check_row(period)
        self.wait_loading_finish()
        self.click(PeriodManagementPageLocator.button_revise(self,row))
        self.wait_loading_finish()

        self.type(PeriodManagementPageLocator.start_time, start)
        self.type(PeriodManagementPageLocator.end_time, end)
        self.type(PeriodManagementPageLocator.beads_date, breads)
        self.click(PeriodManagementPageLocator.start_time)
        self.click(PeriodManagementPageLocator.end_time)
        self.click(PeriodManagementPageLocator.beads_date)

        number = len( self.find_elements(PeriodManagementPageLocator.beads_input) )
        for i in range(number):
            self.type( PeriodManagementPageLocator.input_beads(self,i+1), results[i] )

        self.click(PeriodManagementPageLocator.button_save)

        try:
            self.click(PeriodManagementPageLocator.button_save)
        except:
            pass

        self.wait_loading_finish()
        self.check_revise(number, period)


    # 確認修改功能
    def check_revise(self, number, period):
        row = self.check_row(period)
        assert row != -1, "查詢功能異常(修改後指定期數消失)"

        # 檢查攬珠結果
        len_number = number if number < 10 else (2 * (number - 9) + 9)
        check_results = self.get_text_by_dom(self.find_element((By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td[5]"))).replace(', ', '')
        assert len(check_results) != number, "修改功能異常(攬珠結果和修改內容不一致)"

        # 檢查開盤狀態
        check_state = self.get_text_by_dom(self.find_element((By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td[6]")))
        assert check_state == "已封盘", "修改功能異常(有攬珠結果卻未封盤)"


    # 確認 "派彩狀態" 頁面
    def check_payout_state(self, period, time):
        self.wait_loading_finish()
        row = self.check_row(period)

        try:
            self.wait_invisibility(PeriodManagementPageLocator.message)
            self.click( PeriodManagementPageLocator.button_payout(self, row) )
        except:
            raise EOFError('找不到派彩狀態按鈕')

        self.wait_loading_finish()

        if time == 'before':
            for i in range(10):
                if i == 9:
                    assert self.get_text_by_dom(self.find_element((By.XPATH, "//p[contains(@data-bind, 'text: payoutcount')]"))) != '0', f"作廢前, \"{period}\"期數的派彩頁面中,\"已派彩\"異常"
                else:
                    if self.get_text_by_dom(self.find_element((By.XPATH, "//p[contains(@data-bind, 'text: payoutcount')]"))) != '0':
                        break
                    else:
                        self.sleep(3)
                        self.refresh_browser()
                        self.wait_loading_finish()
                
        if time == 'after':
            assert self.get_text_by_dom(self.find_element((By.XPATH, "//p[contains(@data-bind, 'text: payoutcount')]"))) == '0', f"作廢後, \"{period}\"期數的派彩頁面中,\"已派彩\"異常"
        
        self.sleep(1)
        self.click( PeriodManagementPageLocator.button_back )
        self.wait_loading_finish()
        

    # 刪除期數 且 確認刪除
    def delete_period(self, period):
        self.wait_loading_finish()
        row = self.check_row(period)
        self.wait_loading_finish()

        if row != -1:
            try:
                self.wait_invisibility(PeriodManagementPageLocator.message)
                self.click( PeriodManagementPageLocator.button_delete(self,row) )
                self.wait_visibility( PeriodManagementPageLocator.button_confirm )
                self.click( PeriodManagementPageLocator.button_confirm )
                self.wait_loading_finish()
            except:
                raise EOFError('找不到刪除按鈕')

    def check_delete(self, period):
        row = self.check_row(period)
        assert row == -1, "刪除功能異常"


    # 取toast message來判斷對錯
    def get_toast_message(self, text):
        info = self.get_text_by_dom(self.find_element(PeriodManagementPageLocator.notice_info))

        assert str(info).__contains__(text), f"toast message 應該包含 {text}"


    # 確認 "封盤" / "开盘" 功能
    def check_seal_and_unseal(self, period):
        self.wait_loading_finish()
        row = self.check_row(period)
        self.wait_loading_finish()
        
        Seal_State = self.get_text_by_dom(self.find_element((By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[1]/td[6]")))

        if Seal_State == "已封盘":
            self.click( PeriodManagementPageLocator.button_unseal(self,row) )
            self.get_toast_message("已开盘")
        else: # "" or "已开盘"
            self.click( PeriodManagementPageLocator.button_seal(self,row) )
            self.get_toast_message("已封盘")


    # 確認 "作廢" 功能
    def check_abolishment(self, period):
        self.wait_loading_finish()
        row = self.check_row(period)
        
        self.wait_loading_finish()
        self.click( PeriodManagementPageLocator.button_abolishment(self,row) )
        self.wait_alert_present()
        message = self.get_alert_message()
        self.sleep(1)
        assert str(message).__contains__('请输入欲作废之期数做重复确认')
        self.sendkey_alert(str(period))
        self.accept_alert()
        self.wait_loading_finish() 
        self.get_toast_message("已提交，请稍后查询结果。")

    def check_beads_result(self, period):
        while True:
            row = self.check_row(period=period)
            self.click(PeriodManagementPageLocator.button_make_up(self,row))
            self.click(PeriodManagementPageLocator.button_confirm)
            if self.get_text_by_dom(self.find_element(PeriodManagementPageLocator.button_revise(self,row))) != "":
                break
        
        number_first = self.get_text_by_dom(self.find_element(PeriodManagementPageLocator.button_revise(self,row))).split(" , ")[0]
        if number_first == "1":
            return True

        return False
