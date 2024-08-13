from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage
from selenium.common.exceptions import TimeoutException


class DepositLogManagementPageLocator:
    # 出入款管理
    deposit_log_management = (By.XPATH, '//*[text()="出入款管理"]')

    recharge_management = (By.XPATH, "//div[@class='nest-menu']//span[text()='充值管理']")      # 充值管理
    vender_wallet = (By.XPATH, "//div[@class='nest-menu']//span[text()='厂商钱包']")            # 廠商錢包
    check_vender_wallet = (By.XPATH, "//span[@class='tags-view-item router-link-exact-active router-link-active active' and contains(text(),'厂商钱包')]")

class DepositLogManagementPage(BasePage):
    def into_recharge_page(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.wait_visibility(DepositLogManagementPageLocator.deposit_log_management)
        self.click(DepositLogManagementPageLocator.deposit_log_management)
        self.wait_visibility(DepositLogManagementPageLocator.recharge_management)
        self.click(DepositLogManagementPageLocator.recharge_management)

    def into_vender_wallet(self):
        try:
            # self.refresh_browser()       # 測試"出入款管理"點擊失敗
            self.wait_loading_finish()
            self.wait_visibility(DepositLogManagementPageLocator.deposit_log_management)
        except TimeoutException:
            print(r"can't find 出入款管理")
        
        for loop in range(0, 4):
            self.click(DepositLogManagementPageLocator.deposit_log_management)

            if self.wait_visibility_status(DepositLogManagementPageLocator.vender_wallet) is True:
                self.click(DepositLogManagementPageLocator.vender_wallet)
                self.wait_loading_finish()
                break
            
            if loop == 3:
                raise EOFError("點擊出入款管理錯誤")
        
        assert self.wait_visibility_status(DepositLogManagementPageLocator.check_vender_wallet) is True, '進入CM厂商钱包有誤'