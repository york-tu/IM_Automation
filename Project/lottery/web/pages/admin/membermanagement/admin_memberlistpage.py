from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


class MemberListPageLocator:
    # SEARCH AREA (查找條件區)
    member = (By.XPATH, "//div[@class='col-md-10']/textarea")
    btn_search = (By.XPATH, "//button[contains(text(), '查找')]")

    # RESULT AREA (搜尋結果區)
    more_option = (By.XPATH, "//a[contains(text(), '更多')]")
    structure_change = (By.XPATH, "//a[contains(text(), '修改代理')]")
    structure_title= (By.XPATH, "//*[@class='modal-title' and text()='修改代理']")
    structure_accuont = (By.XPATH, "//label[text()='代理帐号']/following::div/input[contains(@data-bind, 'agentlogin')]")
    structure_otp = (By.XPATH, "//*[@class='modal-title' and text()='修改代理']/following::div/input[contains(@data-bind,'otp')]")
    structure_save_btn = (By.XPATH, "//*[@class='modal-title' and text()='修改代理']/following::button[@class='btn blue' and text()='保存']")
    deposit_otp_btn = (By.XPATH, "//a[contains(text(),'入款OTP')]")  #入款OTP
    deposit_otp_code = (By.XPATH, "//span[@id='otp']")  #OTP碼
    level_name = (By.XPATH, "(//span[@data-bind='text: levelname'])[1]") # 級別
    agent = (By.XPATH, "(//span[@data-bind='visible:agentlogin'])[1]") # 體系關係
    info_change = (By.XPATH, "//a[contains(text(), '修改信息')]")
    info_contact = (By.XPATH, "//a[contains(text(),'联系方式')]")
    delete_bankcards_btn = (By.XPATH, "//label[text()='绑定出款帐号列表']/..//a[@class='btn default btn-xs red-stripe']") # 刪除銀行卡按鈕
    delete_virtualwallet_btn = (By.XPATH, "//label[text()='绑定虚拟钱包列表']/..//a[@class='btn default btn-xs red-stripe']") # 刪除虛擬錢包按鈕
    confirm_delete_btn = (By.XPATH, "//a[@class='btn btn-xs btn-primary']") # 確認刪除按鈕
    save_btn = (By.XPATH, "//button[@class='btn blue' and text()='保存']") # 保存按鈕
    virtualwallet_message = (By.XPATH, "//label[text()='绑定虚拟钱包列表']/..//*[contains(text(),'无资料')]")  # 虛擬錢包無資料
    info_phone = (By.XPATH, "//div[@data-bind='validationElement: mobile']//input")
    button_confirm = (By.XPATH, "//button[text()='确定修改']")
    toast_message = (By.XPATH, "//div[@class='toast-message']")

class MemberList(BasePage):

    # 修改代理
    def change_member_structure(self, member_account, reseller_agent, otp):
        self.wait_loading_finish()
        self.type(MemberListPageLocator.member, member_account)
        self.click(MemberListPageLocator.btn_search)

        self.wait_visibility(MemberListPageLocator.more_option)
        self.click(MemberListPageLocator.more_option)

        self.wait_visibility(MemberListPageLocator.structure_change)
        self.click(MemberListPageLocator.structure_change)

        self.wait_visibility(MemberListPageLocator.structure_title)
        self.type(MemberListPageLocator.structure_accuont, reseller_agent)
        self.type(MemberListPageLocator.structure_otp,otp)
        self.click(MemberListPageLocator.structure_save_btn)
        self.wait_visibility(MemberListPageLocator.toast_message)
        
        assert str(self.get_text(MemberListPageLocator.toast_message)).__contains__("代理修改成功"), self.get_text(MemberListPageLocator.toast_message)
    
    # 確認會員資訊
    def check_member(self, member_account, brand):
        self.wait_loading_finish()
        self.type(MemberListPageLocator.member, member_account)       
        self.click(MemberListPageLocator.btn_search)        
        self.scroll_to_bottom()
        level_name = self.get_text(MemberListPageLocator.level_name)
        agent = self.get_text(MemberListPageLocator.agent)
        # assert level_name == "二级会员", "級別名稱錯誤"
        assert level_name == "一级会员", r"查找帳號級別應為: '一級會員'"
        self.brand = brand
        agent_name = brand + "bot_agent"
        assert agent == '代理：' + agent_name, "代理名稱錯誤"
    
    # 刪除銀行卡
    def delete_bank_cards(self, member_account):
        self.wait_loading_finish()
        self.type(MemberListPageLocator.member, member_account)
        self.click(MemberListPageLocator.btn_search)

        self.wait_visibility(MemberListPageLocator.info_change)
        self.click(MemberListPageLocator.info_change)
        self.wait_loading_finish()

        delete_card_btns = self.find_elements(MemberListPageLocator.delete_bankcards_btn)
        for btn in delete_card_btns:
            self.click_by_dom(btn)
            self.wait_visibility(MemberListPageLocator.confirm_delete_btn)
            self.click(MemberListPageLocator.confirm_delete_btn)
            self.wait_visibility(MemberListPageLocator.toast_message)

            assert str(self.get_text(MemberListPageLocator.toast_message)).__contains__("刪除成功"), self.get_text(MemberListPageLocator.toast_message)
        
        self.click(MemberListPageLocator.save_btn)
        self.wait_visibility(MemberListPageLocator.toast_message)
        self.sleep(1)
        self.wait_loading_finish()

    
    # 刪除虛擬錢包
    def delete_virtual_wallet(self, member_account):
        self.wait_loading_finish()
        self.type(MemberListPageLocator.member, member_account)
        self.click(MemberListPageLocator.btn_search)

        self.wait_visibility(MemberListPageLocator.info_change)
        self.click(MemberListPageLocator.info_change)
        self.wait_loading_finish()

        if self.is_element_finded(MemberListPageLocator.virtualwallet_message) is False:
            for _ in range(len(self.find_elements(MemberListPageLocator.delete_virtualwallet_btn))):
                self.click(MemberListPageLocator.delete_virtualwallet_btn)
                self.wait_visibility(MemberListPageLocator.confirm_delete_btn)
                self.click(MemberListPageLocator.confirm_delete_btn)
                self.wait_visibility(MemberListPageLocator.toast_message)
                assert str(self.get_text(MemberListPageLocator.toast_message)).__contains__("刪除成功"), self.get_text(MemberListPageLocator.toast_message)
            
            self.click(MemberListPageLocator.save_btn)
            self.wait_visibility(MemberListPageLocator.toast_message)
            self.sleep(1)
            self.wait_loading_finish()

    # 會員帳號查找
    def search_member(self, member_account):
        self.refresh_browser()
        self.sleep(1)
        self.type(MemberListPageLocator.member, member_account)
        self.click(MemberListPageLocator.btn_search)
        self.wait_loading_finish()

    def get_member_otp(self):
        self.click(MemberListPageLocator.more_option)
        self.wait_visibility(MemberListPageLocator.deposit_otp_btn)
        self.click(MemberListPageLocator.deposit_otp_btn)
        self.wait_loading_finish()
        self.sleep(1)
        otp_code = self.get_text(MemberListPageLocator.deposit_otp_code)
        return otp_code

    # 修改會員联系方式_手機號碼
    def change_member_phone(self, member_account, phone, otp):
        self.wait_loading_finish()
        self.type(MemberListPageLocator.member, member_account)
        self.click(MemberListPageLocator.btn_search)

        self.wait_visibility(MemberListPageLocator.more_option)
        self.click(MemberListPageLocator.more_option)
        self.wait_visibility(MemberListPageLocator.info_contact)
        self.click(MemberListPageLocator.info_contact)
        self.sendkey_alert(otp)
        self.accept_alert()
        
        self.type(MemberListPageLocator.info_phone, phone)
        self.click(MemberListPageLocator.save_btn)
        self.sendkey_alert(otp)
        self.accept_alert()
        if self.is_element_finded(MemberListPageLocator.button_confirm):
            self.click(MemberListPageLocator.button_confirm)
            
        