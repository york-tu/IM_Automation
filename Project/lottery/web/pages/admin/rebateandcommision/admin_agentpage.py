from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class AgentPageLocator(BasePage):
    account_name = (By.XPATH, "//input[contains(@placeholder,'只能接受数字与小写英文字母')]") # 登入帳號
    search_button = (By.ID, "btnSearch") # 查詢按鈕
    revise_button = (By.XPATH, "//a[contains(text(),'修改') and contains(@href,'agent')]") # 修改按鈕
    commision_dropdown = (By.XPATH, "//label[text()='退佣方案']/..//b") # 退傭方案
    # commision_select = (By.XPATH, "//div[contains(@class,'select2-result-label')]") # 
    commision_save = (By.XPATH, "//button[contains(@data-y2,'submit')]") # 保存按鈕



class AgentPage(BasePage):
    # 設定會員的退傭方案
    def set_commision_program(self, account, program):
        # 查詢會員
        self.type(AgentPageLocator.account_name, account)
        self.click(AgentPageLocator.search_button)
        self.sleep(1)

        # 修改其退傭方案
        self.click(AgentPageLocator.revise_button)
        self.wait_loading_finish()
        self.click(AgentPageLocator.commision_dropdown)
        self.wait_loading_finish()
        string = (By.XPATH, "//div[contains(@class,'select2-result-label') and contains(text(),'{}')]".format(program)) # 找到下拉選單中的指定方案
        self.click(string)
        self.sleep(1)
        self.click(AgentPageLocator.commision_save)

        self.wait_loading_finish()


