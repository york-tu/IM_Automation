from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class AdminExternalPlateformPageLocator:
    # -- 查找條件 --
    # "今日"按鈕
    today_btn = (By.XPATH, '//button[contains(text(),"今日")]')
    # "昨日"按鈕
    yesterday_btn = (By.XPATH, '//button[contains(text(),"昨日")]')
    # "本周"按鈕
    this_week_btn = (By.XPATH, '//button[contains(text(),"本周")]')
    # "上周"按鈕
    last_week_btn = (By.XPATH, '//button[contains(text(),"上周")]')
    # "本月"按鈕
    this_month_btn = (By.XPATH, '//button[contains(text(),"本月")]')
    # "上月"按鈕
    last_month_btn = (By.XPATH, '//button[contains(text(),"上月")]')
    # 交易時間 開始日期
    transacion_time_start = (By.XPATH, '//input[contains(@data-bind, "datetime: filter.starttime")]')
    # 交易時間 結束日期
    transacion_time_end = (By.XPATH, '//input[contains(@data-bind, "datetime: filter.endtime")]')
    # 申請類型
    apply_type_radio_box = (By.XPATH, '//label[text()="申请类型"]/../div[@class="col-md-10"]/label')
    # 申請狀態
    apply_status_radio_box = (By.XPATH, '//label[text()="申请状态"]/../div[@class="col-md-10"]/label')
    # "查找"按鈕
    search_btn = (By.XPATH, '//button[@id="btnSearch"]')

    # -- 新增 --
    # "新增"按鈕
    append = (By.XPATH, '//div[@class="btn-group pull-right"]')
    # "類型"下拉是選單
    append_type = (By.XPATH, '//select[@data-bind="value: type"]')
    # "金額" textbox
    append_amount = (By.XPATH, '//input[@data-bind="value: amount"]')
    # "類型" 出入款選項
    append_type_options = (By.XPATH, '//select[@data-bind="value: type"]/option')
    # "備註" textbox
    remark = (By.XPATH, '//textarea[@data-bind="value: note"]')
    # "保存"按鈕
    save_button = (By.XPATH, '//button[text()="保存"]')

    # -- 充值紀錄 --
    # 申請類型
    apply_type_text = (By.XPATH, '//td[contains(@data-bind, "text: type() == 1 ?")]')
    # 金額
    amount_text = (By.XPATH, '//td[contains(@data-bind, "text: amount")]')
    # 備註
    remark_text = (By.XPATH, '//span[contains(@data-bind, "text: noteDisplay")]')
    # 申請狀態
    apply_status_text = (By.XPATH, '//td[contains(@data-bind, "root.getStatusText(status())")]')
    # 稽核狀態
    audit_status_text = (By.XPATH, '//td[contains(@data-bind, "auditstatus()")]')
    # "操作""確認"按鈕
    confirm_btn = (By.XPATH, '//a[contains(text(), "确认") and not(contains(@style, "display: none;"))]')
    # "操作""拒絕"按鈕
    reject_btn = (By.XPATH, '//a[contains(text(), "拒绝") and not(contains(@style, "display: none;"))]')
    # "確定"按鈕
    confirm_operate = (By.XPATH, '//div[@class= "btn-group"]//*[contains(., "确定")]')
    # "取消"按鈕
    cancel_operate = (By.XPATH, '//a[@data-dismiss="confirmation"]')

class AdminExternalPlateformPage(BasePage):
    # 將 dom 定位list 轉為text list
    def get_text_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    def get_apply_type_text(self, lens):
        '''
            取得特定長度的 "申請類型"字串
        '''
        dom_list = self.find_elements(AdminExternalPlateformPageLocator.apply_type_text)
        return self.get_text_by_dom_list(dom_list[:lens])

    def get_amount_text(self, lens):
        '''
            取得特定長度的 "金額"字串
        '''
        dom_list = self.find_elements(AdminExternalPlateformPageLocator.amount_text)
        return self.get_text_by_dom_list(dom_list[:lens])

    def get_apply_status_text(self, lens):
        '''
            取得特定長度的 "申請狀態"字串
        '''
        dom_list = self.find_elements(AdminExternalPlateformPageLocator.apply_status_text)
        return self.get_text_by_dom_list(dom_list[:lens])

    def get_audit_status_text(self, lens):
        '''
            取得特定長度的 "稽核狀態"字串
        '''
        dom_list = self.find_elements(AdminExternalPlateformPageLocator.audit_status_text)
        return self.get_text_by_dom_list(dom_list[:lens])

    def get_remark_text(self, lens):
        '''
            取得特定長度的 "備註"字串
        '''
        dom_list = self.find_elements(AdminExternalPlateformPageLocator.remark_text)
        return self.get_text_by_dom_list(dom_list[:lens])

    # 檢查以日或周為單位的交易時間 開始及結束時間
    def check_time_period_days_week(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(AdminExternalPlateformPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminExternalPlateformPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == today - datetime.timedelta(days=time_delta_start), \
            f'{error_message_date} 時間錯誤 ... 開始時間錯誤 ... {start_time} 應為-> {today - datetime.timedelta(days=time_delta_start)}'
        assert end_time == today - datetime.timedelta(days=time_delta_end), \
            f'{error_message_date} 時間錯誤 ... 結束時間錯誤 ... {end_time} 應為-> {today - datetime.timedelta(days=time_delta_end)}'

    def add_months(self, sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        return datetime.date(year, month, 1)

    # 檢查以月為單位的交易時間 開始及結束時間
    def check_time_period_month(self, today, time_delta_start, time_delta_end, error_message_date):
        start_time = datetime.datetime.strptime(self.get_attribute(AdminExternalPlateformPageLocator.transacion_time_start, 'value').split(' ')[0], '%Y-%m-%d').date()
        end_time = datetime.datetime.strptime(self.get_attribute(AdminExternalPlateformPageLocator.transacion_time_end, 'value').split(' ')[0], '%Y-%m-%d').date()
        assert start_time == self.add_months(sourcedate=today, months=time_delta_start),  \
            f'{error_message_date} 時間錯誤 ... 開始時間錯誤 ... {start_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_start)}'
        assert end_time == self.add_months(sourcedate=today, months=time_delta_end), \
            f'{error_message_date} 時間錯誤 ... 結束時間錯誤 ... {end_time} 應為-> {self.add_months(sourcedate=today, months=time_delta_end)}'

    def check_select_transaction_time(self):
        '''
            檢查交易時間
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        today = self.get_us_time().date()
        week_day = today.weekday()

        self.click(AdminExternalPlateformPageLocator.today_btn)
        self.check_time_period_days_week(today=today, time_delta_start=0, time_delta_end=-1, error_message_date='今日')

        self.click(AdminExternalPlateformPageLocator.yesterday_btn)
        self.check_time_period_days_week(today=today, time_delta_start=1, time_delta_end=0, error_message_date='昨日')

        self.click(AdminExternalPlateformPageLocator.this_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day, time_delta_end=week_day-7, error_message_date='本週')

        self.click(AdminExternalPlateformPageLocator.last_week_btn)
        self.check_time_period_days_week(today=today, time_delta_start=week_day+7, time_delta_end=week_day, error_message_date='上週')

        self.click(AdminExternalPlateformPageLocator.this_month_btn)
        self.check_time_period_month(today=today, time_delta_start=0, time_delta_end=1, error_message_date='本月')

        self.click(AdminExternalPlateformPageLocator.last_month_btn)
        self.check_time_period_month(today=today, time_delta_start=-1, time_delta_end=0, error_message_date='上月')

    def append_new_data(self, type_option=1, amount=5, remark=''):
        '''
            新增充值紀錄
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminExternalPlateformPageLocator.append)
        self.wait_visibility(AdminExternalPlateformPageLocator.append_type)

        self.click(AdminExternalPlateformPageLocator.append_type)
        self.sleep(0.5)
        self.click((AdminExternalPlateformPageLocator.append_type_options[0], AdminExternalPlateformPageLocator.append_type_options[1] + f'[{type_option}]'))
        assert self.is_element_finded(AdminExternalPlateformPageLocator.append_amount) == True, "Can't find input textarea"
        self.type(AdminExternalPlateformPageLocator.append_amount, str(amount))
        self.type(AdminExternalPlateformPageLocator.remark, remark)
        self.click(AdminExternalPlateformPageLocator.save_button)
        self.sleep(0.5)

    def check_apply_type_amount_remark(self, apply_type, amount, remark):
        '''
            檢查新增資料的申請類型、金額
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminExternalPlateformPageLocator.today_btn)
        self.click(AdminExternalPlateformPageLocator.search_btn)
        self.wait_loading_finish()
        
        lens = len(apply_type)
        apply_type_text = self.get_apply_type_text(lens)
        amount_text = self.get_amount_text(lens)
        remark_text = self.get_remark_text(lens)
        self.sleep(1)

        for i in range(lens):
            assert apply_type[i] == apply_type_text[i], f'充值紀錄 ... 申請類型錯誤 ... 第 {i + 1} 項 {apply_type_text[i]} 應為-> {apply_type[i]}'
            assert amount[i] == amount_text[i], f'充值紀錄 ... 金額錯誤 ... 第 {i + 1} 項 {amount_text[i]} 應為-> {amount[i]}'
            assert remark[i] == remark_text[i], f'充值紀錄 ... 備註錯誤 ... 第 {i + 1} 項 {remark_text[i]} 應為-> {remark[i]}'

    def check_search_apply_type(self):
        '''
            檢查申請類型的搜尋
        '''
        apply_type_radio_box_locator = AdminExternalPlateformPageLocator.apply_type_radio_box
        apply_type_list = ['入款', '出款']
        index = 2
        for apply_type in apply_type_list:
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(AdminExternalPlateformPageLocator.today_btn)
            self.click((apply_type_radio_box_locator[0], apply_type_radio_box_locator[1] + f'[{index}]'))
            self.click(AdminExternalPlateformPageLocator.search_btn)
            self.wait_loading_finish()
            if self.is_element_finded(AdminExternalPlateformPageLocator.apply_type_text):
                apply_text = self.get_text_by_dom_list(dom_list=self.find_elements(AdminExternalPlateformPageLocator.apply_type_text))
                for text in apply_text:
                    assert apply_type == text, f'申請狀態錯誤 ... {text} 應為-> {apply_type}'
            index += 1

    def check_search_apply_status(self):
        '''
            檢查申請狀態的搜尋
        '''
        index = 2
        apply_status_locator = AdminExternalPlateformPageLocator.apply_status_radio_box
        apply_status_list = ['已建单', '成功', '驳回']
        for apply_status in apply_status_list:
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(AdminExternalPlateformPageLocator.today_btn)
            self.wait_loading_finish()
            self.click((apply_status_locator[0], apply_status_locator[1] + f'[{index}]'))
            self.click(AdminExternalPlateformPageLocator.search_btn)
            if self.is_element_finded(AdminExternalPlateformPageLocator.apply_status_text):
                apply_text = self.get_text_by_dom_list(dom_list=self.find_elements(AdminExternalPlateformPageLocator.apply_status_text))
                for text in apply_text:
                    assert apply_status == text, f'申請狀態錯誤 ... {text} 應為-> {apply_status}'
            index += 1

    def check_audit_status(self):
        '''
            檢查修改後的稽核狀態
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(AdminExternalPlateformPageLocator.today_btn)
        self.click(AdminExternalPlateformPageLocator.search_btn)
        self.wait_loading_finish()

        self.click(AdminExternalPlateformPageLocator.confirm_btn)
        self.wait_visibility(AdminExternalPlateformPageLocator.confirm_operate)
        self.click(AdminExternalPlateformPageLocator.confirm_operate)
        self.wait_loading_finish()
        
        self.click(AdminExternalPlateformPageLocator.reject_btn)
        self.wait_visibility(AdminExternalPlateformPageLocator.confirm_operate)
        self.click(AdminExternalPlateformPageLocator.confirm_operate)
        self.wait_loading_finish()

        audit_status_text = self.get_text_by_dom_list(self.find_elements(AdminExternalPlateformPageLocator.audit_status_text))
        result = ['已确认', '已拒绝', '待稽核']
        for i in range(len(result)):
            assert audit_status_text[i] == result[i], f'稽核狀態錯誤 ... {audit_status_text[i]} 應為-> {result[i]}'

    def check_apply_status(self, apply_status:list):
        '''
            檢查申請狀態
            apply_type 為申請狀態的 string list
        '''
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(10)
        self.click(AdminExternalPlateformPageLocator.today_btn)
        self.click(AdminExternalPlateformPageLocator.search_btn)
        self.wait_loading_finish()

        lens = len(apply_status)
        apply_status_text = self.get_text_by_dom_list(self.find_elements(AdminExternalPlateformPageLocator.apply_status_text))[:lens]
        for i in range(lens):
            assert apply_status[i] == apply_status_text[i], f'充值紀錄 ... 申請狀態錯誤 ... 第 {i + 1} 項 {apply_status_text[i]} 應為-> {apply_status[i]}'