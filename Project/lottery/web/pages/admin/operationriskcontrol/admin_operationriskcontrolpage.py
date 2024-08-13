from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class OperationRiskControlPageLocator:
    # ------------運營風控--------------
    menu_business_analysis = (By.XPATH, "//span[text()='运营风控']")

    # *運營風控(新版)
    risk_new_page = (By.XPATH, "//span[text()='运营风控(新版)']")
    overview_deposits_withdrawals = (By.XPATH, "//span[text()='出入款总览']")
    ok_point_deposits_withdrawals = (By.XPATH, "//a[text()='出入款总览']")

    # SEARCH AREA (查找條件區)
    button_today = (By.XPATH, '//button[contains(text(), "今日")]')        # 今日按鈕
    button_yesterday = (By.XPATH, '//button[contains(text(), "昨日")]')    # 昨日按鈕
    button_seven_days = (By.XPATH, '//button[contains(text(), "7日")]')    # 7日按鈕
    button_fourteen_days = (By.XPATH, '//button[contains(text(), "14日")]')    # 14日按鈕
    button_thirty_days = (By.XPATH, '//button[contains(text(), "30日")]')   # 30日按鈕
    button_search = (By.XPATH, '//span[text()="查找"]')       # 查找按鈕
    textarea_shareholder = (By.XPATH, '//span[text()="股东"]/../input')       # 股東輸入框

    # 營運概況資料
    all_amount = (By.XPATH, '//h2/div/span')

class OperationRiskControlPage(BasePage):
    # 運營風控
    def click_operational_risk_control(self):
        self.wait_loading_finish()
        self.scroll_to_top()
        
        for loop in range(0,4):
            if self.wait_visibility_status(OperationRiskControlPageLocator.menu_business_analysis) is True:
                self.wait_loading_finish()
                self.click(OperationRiskControlPageLocator.menu_business_analysis)
                break
            else:
                if loop == 4:
                    assert self.is_element_finded(OperationRiskControlPageLocator.menu_business_analysis), "運營風控BTN錯誤, 無法搜尋到該BTN"
            
            if loop == 3:
                raise EOFError('找不到運營風控按鈕')

    # 運營風控 -> 運營風控(新版) -> 出入款總攬
    def into_overview_deposits_withdrawals(self):
        self.click_operational_risk_control()
        self.click(OperationRiskControlPageLocator.risk_new_page)
        self.wait_visibility(OperationRiskControlPageLocator.overview_deposits_withdrawals)
        self.click(OperationRiskControlPageLocator.overview_deposits_withdrawals)
        self.wait_visibility(OperationRiskControlPageLocator.ok_point_deposits_withdrawals)
        self.wait_loading_finish()

    # 查找時間
    def search_for_time(self, time):
        if time == 1:
            self.click(OperationRiskControlPageLocator.button_today)
        elif time == 2:
            self.click(OperationRiskControlPageLocator.button_yesterday)
        elif time == 3:
            self.click(OperationRiskControlPageLocator.button_seven_days)
        elif time == 4:
            self.click(OperationRiskControlPageLocator.button_fourteen_days)
        else:
            self.click(OperationRiskControlPageLocator.button_thirty_days)
        
        self.click(OperationRiskControlPageLocator.button_search)

        self.wait_loading_finish()

    # 查找股東
    def search_for_shareholder(self, account):
        self.type(OperationRiskControlPageLocator.textarea_shareholder, account)
        self.click(OperationRiskControlPageLocator.button_search)
        self.wait_loading_finish()

    # 取報表資料
    def get_report_data(self):
        all_amount = self.find_elements(OperationRiskControlPageLocator.all_amount)
        total_list = [(amount.text).replace(',','') for amount in all_amount]
        total_deposit = total_list[3:6]
        total_withdrawal = total_list[6:10]
        
        return total_deposit, total_withdrawal
    
    # 驗證資料
    def verify_data(self, company_dict, online_dict, artificial_amount, withdraw_dict, total_deposit, total_withdrawal):
        assert total_deposit[0] == company_dict['company_amount'], f"公司入款金額有誤，出入款總覽:{total_deposit[0]}，公司入款:{company_dict['company_amount']}"
        assert total_deposit[1] == online_dict['online_amount'], f"在線入款金額有誤，出入款總覽:{total_deposit[1]}，在線入款:{online_dict['online_amount']}"
        assert float(total_deposit[2]) == float(artificial_amount), f"人工入款金額有誤，出入款總覽:{float(total_deposit[2])}，人工入款:{float(artificial_amount)}"
        assert total_withdrawal[0] == withdraw_dict['withdraw_amount'], f"總出款金額有誤，出入款總覽:{total_withdrawal[0]}，出款申請(含人工提出_手动申请出款):{withdraw_dict['withdraw_amount']}"
        assert total_withdrawal[3] == withdraw_dict['withdraw_discount'], f"出款手續金額有誤，出入款總覽:{total_withdrawal[3]}，出款申請:{withdraw_dict['withdraw_discount']}"

