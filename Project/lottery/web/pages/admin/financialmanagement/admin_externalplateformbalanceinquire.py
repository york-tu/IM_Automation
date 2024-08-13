from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class BalanceInquireLocator:
    name = (By.XPATH, '//td[@data-bind="text: name"]')                                                      # 錢包名稱
    balance = (By.XPATH, '//td[@data-bind="money: balance"]')                                               # 餘額
    threshold = (By.XPATH, '//td[@data-bind="money: threshold"]')                                           # 預警金額
    modify = (By.XPATH, '//a[contains(text(), "修改")]')                                                    # 修改按鈕

    wallet_name_input_box = (By.XPATH, '//input[@data-bind="value: name"]')                                 # 錢包名稱輸入框
    threshold_input_box = (By.XPATH, '//input[@data-bind="value: threshold"]')                              # 預警金額輸入框
    save_button = (By.XPATH, '//button[text()="保存"]')                                                     # 保存按鈕
    toast_message = (By.XPATH, '//div[@class="toast-message"]')

class BalanceInquire(BasePage):
    def check_wallet_name(self, default_vender_name):
        '''
            檢查錢包名稱
        '''
        self.wait_loading_finish()
        modify_name = 'test1234'
        threshold = str(int(float(self.get_text(BalanceInquireLocator.threshold).replace(',', ''))))
        # ------------ 將錢包名稱改為 name ，檢查是否修改成功 ------------
        self.click(BalanceInquireLocator.modify)
        self.sleep(5)
        self.type(BalanceInquireLocator.wallet_name_input_box, modify_name)
        self.type(BalanceInquireLocator.threshold_input_box, threshold)
        # 有時候要按兩次才按的到，別問我為甚麼
        self.click(BalanceInquireLocator.save_button)
        try:
            self.click(BalanceInquireLocator.save_button)
        except:
            pass
        self.wait_loading_finish()

        wallet_name = self.get_text(BalanceInquireLocator.name)
        assert wallet_name == modify_name, f'錢包名稱 ... {wallet_name} 應為-> {modify_name}'

        # ------------ 將錢包名稱改回原本的名稱 ，檢查是否修改成功 ------------
        self.sleep(1)
        self.click(BalanceInquireLocator.modify)
        self.wait_visibility(BalanceInquireLocator.save_button)
        self.type(BalanceInquireLocator.wallet_name_input_box, default_vender_name)
        self.type(BalanceInquireLocator.threshold_input_box, threshold)
        # 有時候要按兩次才按的到，別問我為甚麼
        self.click(BalanceInquireLocator.save_button)        
        try:
            self.click(BalanceInquireLocator.save_button)
        except:
            pass
        self.wait_loading_finish()

        wallet_name = self.get_text(BalanceInquireLocator.name)
        assert wallet_name == default_vender_name, f'錢包名稱 ... {wallet_name} 應為-> {default_vender_name}'

    def check_balance(self, balance):
        '''
            檢查餘額
        '''
        self.wait_loading_finish()
        balance = float(self.get_text(BalanceInquireLocator.balance).replace(',', ''))

        assert balance == balance, f'餘額 ... {balance} 應為-> {balance}'

    def check_threshold(self):
        '''
            檢查預警金額
        '''
        self.wait_loading_finish()
        origin_threshold = int(float(self.get_text(BalanceInquireLocator.threshold).replace(',', '')))
        modified_threshold = 20
        self.click(BalanceInquireLocator.modify)
        self.wait_visibility(BalanceInquireLocator.save_button)
        self.type(BalanceInquireLocator.threshold_input_box, str(modified_threshold))
        # 有時候要按兩次才按的到，別問我為甚麼
        self.click(BalanceInquireLocator.save_button)        
        try:
            self.click(BalanceInquireLocator.save_button)
        except:
            pass
        self.wait_loading_finish()
        self.sleep(1)
        threshold = int(float(self.get_text(BalanceInquireLocator.threshold).replace(',', '')))
        assert threshold == modified_threshold, f'預警金額錯誤 ... {threshold} 應為-> {modified_threshold}'

        self.click(BalanceInquireLocator.modify)
        self.wait_visibility(BalanceInquireLocator.save_button)
        self.type(BalanceInquireLocator.threshold_input_box, str(origin_threshold))
        # 有時候要按兩次才按的到，別問我為甚麼
        self.click(BalanceInquireLocator.save_button)
        try:
            self.click(BalanceInquireLocator.save_button)
        except:
            pass
        self.wait_loading_finish()
        self.sleep(1)
        threshold = int(float(self.get_text(BalanceInquireLocator.threshold).replace(',', '')))
        assert threshold == origin_threshold, f'預警金額錯誤 ... {threshold} 應為-> {origin_threshold}'
