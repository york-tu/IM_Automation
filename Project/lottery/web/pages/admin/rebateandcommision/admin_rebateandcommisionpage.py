from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class RebateAndCommisionPageLocator:
    # ------------返水/退佣分類------------
    menu_rebate_and_commision = (By.XPATH, "//span[text()='返水/退佣']") # 返水/退傭

    # *比例设置
    menu_porpotion_setting = (By.XPATH, "//li[contains(@permission-id,'rebate') and contains(@class,'heading')]//span[text()='比例设置']")
    # 占成方案
    profit_plan = (By.XPATH, "//span[contains(text(), '占成方案')]") # 返水/退佣 -> 比例設置 -> 占成方案
    ok_point_profit_plan = (By.XPATH, "//a[contains(text(), '占成方案')]")
    # 退佣方案
    refund_plan = (By.XPATH, "//span[contains(text(), '退佣方案')]") # 返水/退佣 -> 比例設置 -> 退佣方案
    ok_point_refund_plan = (By.XPATH, "//a[contains(text(), '退佣方案')]")
    # 返水設置
    rebate_setting = (By.XPATH, "//span[contains(text(), '返水设置')]") # 返水/退佣 -> 比例設置 -> 返水設置
    # 返水設置-實時返水
    timely_rebate = (By.XPATH, "//span[contains(text(), '实时返水')]") # 返水/退佣 -> 比例設置 -> 返水設置 -> 實時返水
    ok_point_timely_rebate = (By.XPATH, "//a[contains(text(), '实时返水')]")
    # 返水設置-階梯返水
    ladder_rebate = (By.XPATH, "//span[contains(text(), '阶梯返水')]") # 返水/退佣 -> 比例設置 -> 返水設置 -> 階梯返水
    ok_point_ladder_rebate = (By.XPATH, "//a[contains(text(), '阶梯返水')]")
    # 返水設置-會員返水
    member_rebate = (By.XPATH, "//span[contains(text(), '会员返水')]") # 返水/退佣 -> 比例設置 -> 返水設置 -> 會員返水
    ok_point_member_rebate = (By.XPATH, "//a[contains(text(), '会员返水')]")

    # *批次返水
    menu_batch_rakeback_center = (By.XPATH, "//span[text()='批次返水']") # 返水/退傭 -> 批次返水
    ok_point_batch_water_center = (By.XPATH, "//a[contains(text(), '批次返水')]")

    # *阶梯返水
    menu_ladder_rakeback_center = (By.XPATH, "//span[text()='阶梯返水']") # 返水/退傭 -> 階梯返水
    ok_point_ladder_rakeback_center = (By.XPATH, "//a[contains(text(), '阶梯返水')]")

    # *代理退佣
    menu_agent_commision = (By.XPATH, "//span[contains(text(),'代理退佣')]") # 返水/退傭 -> 代理退傭
    # 代理結算
    settlement = (By.XPATH, "//span[contains(text(),'代理結算')]") # 返水/退傭 -> 代理退傭 -> 代理結算
    ok_point_settlement = (By.XPATH, "//a[contains(text(), '代理结算')]")
    # 代理結算(新版)
    menu_new_settlement = (By.XPATH, "//span[contains(text(),'代理结算(新版)')]") # 返水/退傭 -> 代理退傭 -> 代理結算(新版)
    ok_point_menu_new_settlement = (By.XPATH, "//a[contains(text(), '代理结算(新版)')]")
    # menu_rebate_and_commision_management = (By.XPATH, "//li[contains(@permission-id,'rebate') and contains(@class,'heading')]")
    # menu_porpotion_setting = (By.XPATH, "//li[contains(@permission-id,'rebate') and contains(@class,'heading')]//span[text()='比例设置']") # 返水/退傭 - 比例設定
    # menu_commision_program = (By.XPATH, "//span[text()='退佣方案']") # 返水/退傭 - 比例設定 - 退傭方案
    

class RebateAndCommisionPage(BasePage):
    # 返水/退傭    
    def click_commision_refund(self):
        self.wait_loading_finish()
        for loop in range(0,2):
            if self.wait_visibility(RebateAndCommisionPageLocator.menu_rebate_and_commision) is True:
                break
            self.sleep(5)
        self.sleep(3)
        self.click(RebateAndCommisionPageLocator.menu_rebate_and_commision)

    # 返水/退傭 -> 比例設置 -> 占成方案
    def into_profit_plan(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_porpotion_setting)
        self.click(RebateAndCommisionPageLocator.profit_plan)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_profit_plan)
        self.wait_loading_finish()

    # 返水/退傭 -> 比例設置 -> 退傭方案
    def into_commision_refund_program(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_porpotion_setting)
        self.click(RebateAndCommisionPageLocator.refund_plan)
        self.wait_loading_finish()
    
    # 返水/退傭 -> 比例設置 -> 返水設置 -> 實時返水
    def into_timely_rebate(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_porpotion_setting)
        self.click(RebateAndCommisionPageLocator.rebate_setting)
        self.click(RebateAndCommisionPageLocator.timely_rebate)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_timely_rebate)
        self.wait_loading_finish()

    # 返水/退傭 -> 比例設置 -> 返水設置 -> 階梯返水
    def into_ladder_rebate(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_porpotion_setting)
        self.click(RebateAndCommisionPageLocator.rebate_setting)
        self.click(RebateAndCommisionPageLocator.ladder_rebate)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_ladder_rebate)
        self.wait_loading_finish()

    # 返水/退傭 -> 比例設置 -> 返水設置 -> 會員返水
    def into_member_rebate(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_porpotion_setting)
        self.click(RebateAndCommisionPageLocator.rebate_setting)
        self.click(RebateAndCommisionPageLocator.member_rebate)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_member_rebate)
        self.wait_loading_finish()

    # 返水/退傭 -> 批次返水
    def into_batch_rakeback_center(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_batch_rakeback_center)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_batch_water_center)
        self.wait_loading_finish()

    # 返水/退傭 -> 階梯返水
    def into_ladder_rakeback_center(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_ladder_rakeback_center)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_ladder_rakeback_center)
        self.wait_loading_finish()

    # 返水/退傭 -> 代理退傭 -> 代理結算
    def into_settlement(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_agent_commision)
        self.click(RebateAndCommisionPageLocator.settlement)
        self.wait_visibility(RebateAndCommisionPageLocator.ok_point_settlement)
        self.wait_loading_finish()
    
    # 返水/退傭 -> 代理退傭 -> 代理結算(新版)
    def into_new_settlement(self):
        self.click_commision_refund()
        self.click(RebateAndCommisionPageLocator.menu_agent_commision)
        self.click(RebateAndCommisionPageLocator.menu_new_settlement)
        self.wait_loading_finish()
    