from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class HandingFeePageLocator(BasePage):
    # 會員設定 - 出款設定
    withdraw_hour = (By.XPATH, "//input[@data-bind = 'value: withdrawhours']")                       # 出款時長
    withdraw_free_time = (By.XPATH, "//input[@data-bind = 'value: withdrawtimes']")                  # 免費次數
    withdraw_charge = (By.XPATH, "//input[@data-bind = 'value: withdrawcharge']")                    # 出款手續
    max_withdraw_charge_count = (By.XPATH, "//input[@data-bind = 'value: withdrawchargemax']")       # 手續上限
    max_withdraw_value = (By.XPATH, "//input[@data-bind = 'value: withdrawmin']")                    # 最小出款
    min_withdraw_value = (By.XPATH, "//input[@data-bind = 'value: withdrawmax']")                    # 最大出款
    withdraw_charge_count_limit = (By.XPATH,"//input[@name='withdrawchargemax_status' and @value='1']")         #手續上限 - 有上限
    withdraw_charge_count_unlimited = (By.XPATH,"//input[@name='withdrawchargemax_status' and @value='0']")     #手續上限 - 無上限
    # withdraw_exchange_charge = (By.XPATH, "//input[@data-bind = 'value: withdrawchargestatement']")  # 轉帳手續(此功能已拔除)

    # 會員設定 - 稽核設定
    audit_status_on = (By.XPATH, "//input[@data-bind = 'radio: auditstatus' and @value = '1']")  # 常态稽核 - 已启用
    audit_status_off = (By.XPATH, "//input[@data-bind = 'radio: auditstatus' and @value = '0']") # 常态稽核 - 已禁用
    audit_charge = (By.XPATH, "//input[@data-bind = 'value: auditcharge']")                      # 稽核費用
    audit_rate = (By.XPATH, "//input[@data-bind = 'value: auditrate']")                          # 稽核倍數
    audit_limit = (By.XPATH, "//input[@data-bind = 'value: auditdue']")                          # 放寬額度

    # 會員設定 - 有效會員
    min_member_amount = (By.XPATH, "//input[@data-bind = 'value: memberminamount']") # 最小投注額
    min_member_point = (By.XPATH, "//input[@data-bind = 'value: memberminpoint']")   # 有效投注

    # 代理設定
    reseller_deposit_charge = (By.XPATH, "//input[@data-bind = 'value: resellerdepositcharge']")   # 入款手續
    max_reseller_deposit = (By.XPATH, "//input[@data-bind = 'value: resellerdepositchargemax']")   # 入款上限
    reseller_withdraw_charge = (By.XPATH, "//input[@data-bind = 'value: resellerwithdrawcharge']") # 出款手續
    max_reseller_withdraw = (By.XPATH, "//input[@data-bind = 'value: resellerwithdrawchargemax']") # 出款上限

    # 儲存
    audit_save = (By.XPATH, "//div[@data-context = 'fee']//button[contains(text(), '保存')]")                                       # 會員設定 - 保存
    reseller_save = (By.XPATH, "//div[@data-context = 'resellerfee']//button[contains(text(), '保存')]")                            # 代理設定 - 保存
    operation_save = (By.XPATH, "//div[(@class = 'row') and not(contains(@data-context,'fee'))]//button[contains(text(), '保存')]") # 營運設定 - 保存
    
    # 返回
    btn_back = (By.XPATH, "//button[contains(text(), '保存')]")


class HandingFeePage(BasePage):
    def change_value(self, location, first_value, second_value):
        self.wait_visibility(location)
        if self.find_element(location).get_attribute('value') == str(first_value):
            self.type(location, second_value)
        else:
            self.type(location, first_value)


    def check_save(self):
        # 除錯用的 list
        with_draw_word_list = ['出款時長', '免費次數', '出款手續', '手續上限', '最小出款', '最大出款', '轉帳手續']
        audit_word_list = ['稽核費用', '稽核倍數', '放寬額度']
        member_word_list = ['最小投注額', '有效投注']
        reseller_word_list = ['入款手續', '入款上限', '出款手續', '出款上限']

        
        old_withdraw_list = []
        old_audit_list = []
        old_member_list = []
        old_reseller_list = []

        # 讀 出款時長, 免費次數, 出款手續, 手續上限, 最小出款, 最大出款, 轉帳手續 值
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_hour).get_attribute('value'))
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_free_time).get_attribute('value'))
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_charge).get_attribute('value'))
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.max_withdraw_charge_count).get_attribute('value'))
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.max_withdraw_value).get_attribute('value'))
        old_withdraw_list.append(self.find_element(HandingFeePageLocator.min_withdraw_value).get_attribute('value'))
        # old_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_exchange_charge).get_attribute('value'))

        # 讀 稽核費用, 稽核倍數, 放寬額度 值
        old_audit_list.append(self.find_element(HandingFeePageLocator.audit_charge).get_attribute('value'))
        old_audit_list.append(self.find_element(HandingFeePageLocator.audit_rate).get_attribute('value'))
        old_audit_list.append(self.find_element(HandingFeePageLocator.audit_limit).get_attribute('value'))

        # 讀 最小投注額, 有效投注 值
        old_member_list.append(self.find_element(HandingFeePageLocator.min_member_amount).get_attribute('value'))
        old_member_list.append(self.find_element(HandingFeePageLocator.min_member_point).get_attribute('value'))

        # 讀 入款手續, 入款上限, 出款手續, 出款上限 值
        old_reseller_list.append(self.find_element(HandingFeePageLocator.reseller_deposit_charge).get_attribute('value'))
        old_reseller_list.append(self.find_element(HandingFeePageLocator.max_reseller_deposit).get_attribute('value'))
        old_reseller_list.append(self.find_element(HandingFeePageLocator.reseller_withdraw_charge).get_attribute('value'))
        old_reseller_list.append(self.find_element(HandingFeePageLocator.max_reseller_withdraw).get_attribute('value'))
        
        # 改 出款時長, 免費次數, 出款手續, 手續上限, 最小出款, 最大出款, 轉帳手續 值
        self.click(HandingFeePageLocator.withdraw_charge_count_limit)
        HandingFeePage.change_value(self, HandingFeePageLocator.withdraw_hour, 24, 12)
        HandingFeePage.change_value(self, HandingFeePageLocator.withdraw_free_time, 0, 1)
        HandingFeePage.change_value(self, HandingFeePageLocator.withdraw_charge, 10, 20)
        HandingFeePage.change_value(self, HandingFeePageLocator.max_withdraw_charge_count, 50, 25)
        HandingFeePage.change_value(self, HandingFeePageLocator.max_withdraw_value, 0, 1)
        HandingFeePage.change_value(self, HandingFeePageLocator.min_withdraw_value, 100001, 100000)
        # HandingFeePage.change_value(self, HandingFeePageLocator.withdraw_exchange_charge, 0, 10)

        # 改 稽核費用, 稽核倍數, 放寬額度 值
        HandingFeePage.change_value(self, HandingFeePageLocator.audit_charge, 0, 10)
        HandingFeePage.change_value(self, HandingFeePageLocator.audit_rate, 1, 2)
        HandingFeePage.change_value(self, HandingFeePageLocator.audit_limit, 0, 10)

        # 改 最小投注額, 有效投注 值
        HandingFeePage.change_value(self, HandingFeePageLocator.min_member_amount, 0, 10)
        HandingFeePage.change_value(self, HandingFeePageLocator.min_member_point, 0, 10)

        # 儲存
        self.click(HandingFeePageLocator.audit_save)
        self.wait_loading_finish()
        self.sleep(3)

        # 改 入款手續, 入款上限, 出款手續, 出款上限 值
        HandingFeePage.change_value(self, HandingFeePageLocator.reseller_deposit_charge, 6, 10)
        HandingFeePage.change_value(self, HandingFeePageLocator.max_reseller_deposit, 6, 10)
        HandingFeePage.change_value(self, HandingFeePageLocator.reseller_withdraw_charge, 4, 5)
        HandingFeePage.change_value(self, HandingFeePageLocator.max_reseller_withdraw, 4, 5)

        # 儲存
        self.click(HandingFeePageLocator.reseller_save)
        self.click(HandingFeePageLocator.reseller_save)
        self.wait_loading_finish()
        self.sleep(3)
        self.refresh_browser()


        new_withdraw_list = []
        new_audit_list = []
        new_member_list = []
        new_reseller_list = []

        # 讀 出款時長, 免費次數, 出款手續, 手續上限, 最小出款, 最大出款, 轉帳手續 值
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_hour).get_attribute('value'))
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_free_time).get_attribute('value'))
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_charge).get_attribute('value'))
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.max_withdraw_charge_count).get_attribute('value'))
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.max_withdraw_value).get_attribute('value'))
        new_withdraw_list.append(self.find_element(HandingFeePageLocator.min_withdraw_value).get_attribute('value'))
        # new_withdraw_list.append(self.find_element(HandingFeePageLocator.withdraw_exchange_charge).get_attribute('value'))

        # 確認 出款時長, 免費次數, 出款手續, 手續上限, 最小出款, 最大出款, 轉帳手續 是否修改
        for i in range(0, len(old_withdraw_list)):
            assert old_withdraw_list[i] != new_withdraw_list[i], "Error in {}".format(with_draw_word_list[i])

        # 讀 稽核費用, 稽核倍數, 放寬額度 值
        new_audit_list.append(self.find_element(HandingFeePageLocator.audit_charge).get_attribute('value'))
        new_audit_list.append(self.find_element(HandingFeePageLocator.audit_rate).get_attribute('value'))
        new_audit_list.append(self.find_element(HandingFeePageLocator.audit_limit).get_attribute('value'))

        # 確認 稽核費用, 稽核倍數, 放寬額度 是否修改
        for i in range(0, len(old_audit_list)):
            assert old_audit_list[i] != new_audit_list[i], "Error in {}".format(audit_word_list[i])

        # 讀 最小投注額, 有效投注 值
        new_member_list.append(self.find_element(HandingFeePageLocator.min_member_amount).get_attribute('value'))
        new_member_list.append(self.find_element(HandingFeePageLocator.min_member_point).get_attribute('value'))

        # 確認 最小投注額, 有效投注 是否修改
        for i in range(0, len(old_member_list)):
            assert old_member_list[i] != new_member_list[i], "Error in {}".format(member_word_list[i])

        # 讀 入款手續, 入款上限, 出款手續, 出款上限 值
        new_reseller_list.append(self.find_element(HandingFeePageLocator.reseller_deposit_charge).get_attribute('value'))
        new_reseller_list.append(self.find_element(HandingFeePageLocator.max_reseller_deposit).get_attribute('value'))
        new_reseller_list.append(self.find_element(HandingFeePageLocator.reseller_withdraw_charge).get_attribute('value'))
        new_reseller_list.append(self.find_element(HandingFeePageLocator.max_reseller_withdraw).get_attribute('value'))

        # 確認 入款手續, 入款上限, 出款手續, 出款上限 是否修改
        for i in range(0, len(old_reseller_list)):
            assert old_reseller_list[i] != new_reseller_list[i], "Error in {}".format(reseller_word_list[i])

        return new_withdraw_list, with_draw_word_list