from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class CommisionPageLocator:
    # 退傭方案
    add_program = (By.XPATH, "//a[contains(@href,'#dialog')]") # 新增退傭方案
    program_name = (By.XPATH, "//input[contains(@type,'text') and contains(@title,'必填字段')]") # 方案名稱
    save_btn = (By.XPATH, "//button[text()='保存']") # 保存按鈕
    close_btn = (By.XPATH, "//button[text()='关闭']") # 關閉按鈕
    exist_close_btn =(By.XPATH,"//*[@class='toast-close-button']") # 叉叉
    exist_message =(By.XPATH,"//*[@class='toast-message' and contains(text(),'已存在')]") # 已存在警示

    # 盈虧區間
    earn_from_input = (By.XPATH, "//tbody[contains(@data-bind,'items')]//td[contains(@data-bind,'earnfrom')]/input")
    earn_to_input = (By.XPATH, "//tbody[contains(@data-bind,'items')]//td[contains(@data-bind,'earnto')]/input")

    # 有效會員
    member_from_input = (By.XPATH, "//tbody[contains(@data-bind,'items')]//td[contains(@data-bind,'memfrom')]/input")
    member_to_input = (By.XPATH, "//tbody[contains(@data-bind,'items')]//td[contains(@data-bind,'memto')]/input")

    # 公司入款
    company_deposit_input = (By.XPATH, "//td[contains(@data-bind,': depositpercent')]/input")

    # 在線入款
    online_deposit_input = (By.XPATH, "//td[contains(@data-bind,'webdepositpercent')]/input")

    # 階梯設定
    add_stair = (By.XPATH, "//a/i[contains(@class,'fa-plus')]") # 新增階梯設定
    setting_channel = (By.XPATH, "//a[contains(text(), '设置频道退佣')]") # 設定頻道退傭
    save_setting_btn = (By.XPATH, "//a[contains(text(),'保存阶梯')]") # 保存階梯設定
    channel_setting_list = (By.XPATH, "//input[contains(@data-bind,'value: rebatepercent')]") # 階梯設定頻道列表
    save_img = (By.XPATH, "//a[contains(@data-bind, 'click:submit')]/..") # 保存按鈕

class CommisionPage(BasePage):
    # 新增退傭方案
    def add_commision_program(self, program):
        # 點擊新增
        self.wait_loading_finish()
        self.click(CommisionPageLocator.add_program)
        self.wait_loading_finish()
        self.sleep(1)
        self.wait_visibility(CommisionPageLocator.program_name)
        self.type(CommisionPageLocator.program_name, program)
        self.click(CommisionPageLocator.save_btn)

        # 判斷是否已有此方案
        if self.wait_visibility_status(CommisionPageLocator.exist_message) is True:
            self.click(CommisionPageLocator.close_btn)

        self.wait_invisibility(CommisionPageLocator.save_btn)
    
    # 進入退傭方案裡 並 設定
    def into_setting_commision_program(self, program):
        # 尋找指定方案 並 點擊設定
        self.wait_loading_finish()
        self.sleep(1)
        all_program_xpath = (By.XPATH, "//input[contains(@data-bind,'value: name')]")
        programs = self.find_elements(all_program_xpath)
        self.wait_loading_finish()
        
        for index, program_tmp in enumerate(programs):
            if (index > 0) and (program_tmp.get_attribute("value") == program):
                button = (By.XPATH, "(//*[contains(text(),'设置阶梯')])[{}]".format(index))
                self.click(button)
                break

        self.wait_loading_finish()

    # 進入階梯設定 並 設定
    def add_setting_stair(self):
        self.wait_loading_finish()
        # 判斷是否已有階梯設定
        if self.is_element_finded(CommisionPageLocator.setting_channel) is False:
            self.click(CommisionPageLocator.add_stair)
            self.click(CommisionPageLocator.save_btn)
        
        self.wait_loading_finish()
        # 設定區間
        self.type(CommisionPageLocator.earn_from_input, 0)
        self.type(CommisionPageLocator.earn_to_input, 100000)
        self.type(CommisionPageLocator.member_from_input, 1)
        self.type(CommisionPageLocator.member_to_input, 5)
        self.type(CommisionPageLocator.company_deposit_input, 10)
        self.type(CommisionPageLocator.online_deposit_input, 10)
        self.click(CommisionPageLocator.save_setting_btn)

        # 設定頻道退傭
        self.sleep(2)
        self.click(CommisionPageLocator.setting_channel)
        self.wait_loading_finish()
        for i in range(1, (len(self.find_elements(CommisionPageLocator.channel_setting_list)) + 1)):
            input_tmp = (By.XPATH, "(//input[contains(@data-bind,'value: rebatepercent')])[{}]".format(i))
            self.type(input_tmp, 10)
        self.scroll_to_top() # 至最上層
        self.click(CommisionPageLocator.save_img)
        self.wait_loading_finish()


