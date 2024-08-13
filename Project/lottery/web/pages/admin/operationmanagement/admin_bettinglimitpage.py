from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class BettingLimitLocator:

    # --------------------------------- 玩法列表 ---------------------------------
    # 遊戲玩法
    game_rule = (By.XPATH, '//td[contains(@data-bind, "typecodename")]')
    # 單向限額
    total_amount = (By.XPATH, '//td[contains(@data-bind, "totalamount")]')
    # 單注限額
    per_amount = (By.XPATH, '//td[contains(@data-bind, "peramount")]')
    # 操作
    button_modify = (By.XPATH, '//a[contains(@data-bind, "encodeURIComponent(typecode)")]')

    # --------------------------------- 修改頁面 ---------------------------------
    # 單項限額
    input_box_total_amount = (By.XPATH, '//input[contains(@data-bind, "totalamount")]')
    # 單注限額
    input_box_per_amount = (By.XPATH, '//input[contains(@data-bind, "peramount")]')
    # 保存
    button_save = (By.XPATH, '//button[contains(., "保存")]')
    # 返回
    button_cancel = (By.XPATH, '//button[contains(., "返回")]')
    # toast 訊息
    toast_message = (By.XPATH, '//div[@class="toast-message"]')

class BettingLimit(BasePage):
    
    # 將 dom 定位list 轉為text list
    def get_text_list_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    # 檢查修改後的 單項限額 及 單注限額
    def check_modify_amount(self, index:int, limits:tuple):
        self.wait_loading_finish()
        self.wait_visibility(BettingLimitLocator.button_modify)
        self.wait_loading_finish()
        total_amount = self.get_text_by_dom(self.find_elements(BettingLimitLocator.total_amount)[index])
        per_amount = self.get_text_by_dom(self.find_elements(BettingLimitLocator.per_amount)[index])

        if total_amount != limits[0]:
            raise AssertionError(f'單項限額 第 {index+1} 項錯誤 ... {total_amount} 應為-> {limits[0]}')

        if per_amount != limits[1]:
            raise AssertionError(f'單項限額 第 {index+1} 項錯誤 ... {per_amount} 應為-> {limits[1]}')

    # 修改 單項限額 及 單注限額
    def modify_amount(self, index, limits:tuple):
        self.click_by_dom(self.find_elements(BettingLimitLocator.button_modify)[index])
        self.wait_loading_finish()
        self.type(BettingLimitLocator.input_box_total_amount, limits[0])
        self.type(BettingLimitLocator.input_box_per_amount, limits[1])
        self.click(BettingLimitLocator.button_save)
        self.click(BettingLimitLocator.button_save)

    def check_modify_function(self):
        '''
            檢查修改限額功能
        '''
        self.wait_loading_finish()

        if not self.is_element_finded(BettingLimitLocator.game_rule):
            return

        limits = ('10', '5')
        lens = len(self.find_elements(BettingLimitLocator.game_rule))
        total_amount_for_modify = self.find_elements(BettingLimitLocator.total_amount)[:min(3, lens)]
        per_amount_for_modify = self.find_elements(BettingLimitLocator.per_amount)[:min(3, lens)]
        # 紀錄 單向限額 及 單注限額 原本的資料
        total_amount_for_modify_text = self.get_text_list_by_dom_list(total_amount_for_modify)
        per_amount_for_modify_text = self.get_text_list_by_dom_list(per_amount_for_modify)

        for index in range(min(3, lens)):
            limits_origin = (total_amount_for_modify_text[index], per_amount_for_modify_text[index])
            try:
                self.modify_amount(index, limits)
                self.check_modify_amount(index, limits)
                self.modify_amount(index, limits_origin)
                self.check_modify_amount(index, limits_origin)
            except AssertionError as e:
                self.modify_amount(index, limits_origin)
                raise e
