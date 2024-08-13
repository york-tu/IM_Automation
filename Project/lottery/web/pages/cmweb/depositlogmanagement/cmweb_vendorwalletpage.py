from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage

class VendorWalletPageLocator:
    amount = (By.XPATH, "//td[3]")          # 金額
    name = (By.XPATH, "//td[1]")            # 名稱

class VendorWalletPage(BasePage):
    def get_amount(self):
        '''
            取得金額
        '''
        return float(self.get_text(VendorWalletPageLocator.amount).replace(',', ''))

    def get_vender_name(self):
        '''
            取得廠商名稱
        '''
        return self.get_text(VendorWalletPageLocator.name)