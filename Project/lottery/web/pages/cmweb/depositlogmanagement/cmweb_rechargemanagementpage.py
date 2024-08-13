from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage

class RechargeManagementPageLocator:
    amount_text = (By.XPATH, "//td[4]")                     # 金額
    type_text = (By.XPATH, "//td[6]")                       # 類型
    confirm_btn = (By.XPATH, "//span[text()='确认']")       # "確認"按鈕
    reject_btn = (By.XPATH, "//span[text()='拒绝']")        # "拒絕"按鈕

class RechargeManagementPage(BasePage):
    # 點擊確認並回傳金額
    def click_confirm_get_amount(self, apply_status, button_locator, index):
        self.click_by_dom(button_locator)
        type_text_locator = self.find_elements(RechargeManagementPageLocator.type_text)
        amount_text_locator = self.find_elements(RechargeManagementPageLocator.amount_text)
        
        apply_status[index] = '成功'
        type_ = 1 if self.get_text_by_dom(type_text_locator[index]) == '存入' else -1
        return float(self.get_text_by_dom(amount_text_locator[index]).replace(',', '')) * type_

    # 點擊拒絕並回傳金額 0
    def click_reject_get_zero(self, apply_status, button_locator, index):
        self.click_by_dom(button_locator)
        
        apply_status[index] = '驳回'
        return 0

    def click_confirm_reject_and_get_difference(self, actions:list, apply_status:list):
        '''
            選擇點擊確認、拒絕或不點擊，並回傳最後金額的變化量
            actions 輸入 boolean list : 
                True 點擊確認
                False 點擊拒絕
                None 不點擊
        '''
        difference = 0
        button_index = 0

        for i in range(len(actions)):

            self.sleep(1)
            confirm_btn_locator = self.find_elements(RechargeManagementPageLocator.confirm_btn)
            reject_btn_locator = self.find_elements(RechargeManagementPageLocator.reject_btn)

            if actions[i] == True:
                difference += self.click_confirm_get_amount(apply_status, confirm_btn_locator[button_index], i)
                button_index -= 1
            elif actions[i] == False:
                difference += self.click_reject_get_zero(apply_status, reject_btn_locator[button_index], i)
                button_index -= 1

            button_index += 1

        return difference