from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class OldAgentSettlementPageLocator:
  # 查找條件
  input_commission_type = (By.XPATH, "//input[contains(@value,'c')]")                     # 退佣類型
  input_occupy_type = (By.XPATH, "//input[contains(@value,'s')]")                         # 占成類型
  settletime_input = (By.XPATH, "//input[contains(@data-bind,'date: filter.starttime')]") # 結算時間
  search_btn = (By.XPATH, "//*[@id='btnSearch']")                                         # 查詢按鈕

  # 結算列表
  Counting_date = (By.XPATH, "//*[text()='结算周期']") # 結算週期



class OldAgentSettlePage(BasePage):
  # 尋找特定目標
  def check_special_target(self):
    assert self.wait_visibility_status(OldAgentSettlementPageLocator.input_commission_type) is True, "頁面顯示錯誤(退傭類型)"
    assert self.wait_visibility_status(OldAgentSettlementPageLocator.input_occupy_type) is True, "頁面顯示錯誤(占成類型)"
    assert self.wait_visibility_status(OldAgentSettlementPageLocator.settletime_input) is True, "頁面顯示錯誤(結算時間)"
    assert self.wait_visibility_status(OldAgentSettlementPageLocator.search_btn) is True, "頁面顯示錯誤(查找按鈕)"
    assert self.wait_visibility_status(OldAgentSettlementPageLocator.Counting_date) is True, "頁面顯示錯誤(結算週期)"
