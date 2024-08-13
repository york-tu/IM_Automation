from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common


######## 會員列表 ########
class MemberListPageLocator:
    #### 搜尋
    button_search = (By.XPATH, "//button/span[text()='查询']")
    button_today = (By.XPATH, "//button/span[text()='当日']")
    button_yesterday = (By.XPATH, "//button/span[text()='前一天']")
    button_seven_days_ago = (By.XPATH, "//button/span[text()='前7天']")
    button_thirty_days_ago = (By.XPATH, "//button/span[text()='前30天']")
    input_member_number = (By.XPATH, "//textarea[@placeholder='请输入会员编号']")
    select_status = (By.XPATH, "//input[@placeholder='请选择状态']")
    select_level = (By.XPATH, "//input[@placeholder='请选择分组级别']")
    input_member_name = (By.XPATH, "//input[@placeholder='请输入会员姓名']")
    input_qq_account = (By.XPATH, "//input[@placeholder='请输入会员QQ号后四码']")
    input_phone = (By.XPATH, "//input[@placeholder='请输入手机号后四码']")
    input_address = (By.XPATH, "//input[@placeholder='请输入会员钱包后六码']")

    # 列表資料
    member_name = (By.XPATH, "//div[@class='memberInfo']/div/div")
    phone_eye = (By.XPATH, "//p[1]/i[@class='el-icon-view otp-eye'][1]")
    qq_account_eye = (By.XPATH, "//p[2]/i[@class='el-icon-view otp-eye'][1]")
    address_eye = (By.XPATH, "//p[3]/i[@class='el-icon-view otp-eye'][1]")

    # 列表操作
    button_change_data = (By.XPATH, "//button/span[text()='修改资料']")
    button_change_password = (By.XPATH, "//button/span[text()='修改密码']")
    button_info_note = (By.XPATH, "//button/span[text()='信息备注']")
    button_change_payment_password = (By.XPATH, "//button/span[text()='修改支付密码']")

    # 營運OTP驗證彈窗
    input_otp = (By.XPATH, "//input[@placeholder='请输入运营OTP']")
    button_otp_confirm = (By.XPATH, "//button[@class='el-button el-button--primary']/span[text()='确定']")
    otp_data = (By.XPATH, "//div[@class='']//div[@class='check-otp-text-main']")
    button_close_pop = (By.XPATH, "//i[@class='el-icon-close']")

    # 修改密碼彈窗
    input_new_password = (By.XPATH, "(//input[@type = 'password'])[1]")
    input_new_password_again = (By.XPATH, "(//input[@type = 'password'])[2]")
    button_change_password_confirm = (By.XPATH, "//div[@aria-label='修改密码']//span[text()='确定']")

    message_success = (By.XPATH, "//p[text()='执行成功']")

    def check_first_table(self, number):
        return (By.XPATH, f"//tr[1]/td/div[text()='{number}']")


class MemberListPage(BasePage):
    # 取得列表第一個會員姓名
    def get_member_name(self):
        self.wait_visibility(MemberListPageLocator.member_name)
        name = self.get_text(MemberListPageLocator.member_name)
        return name

    # 取得列表第一個會員手機號
    def get_member_phone(self):
        self.wait_visibility(MemberListPageLocator.phone_eye)
        self.click(MemberListPageLocator.phone_eye)
        self.wait_visibility(MemberListPageLocator.input_otp)
        self.type(MemberListPageLocator.input_otp, '1')
        self.click(MemberListPageLocator.button_otp_confirm)
        phone = self.get_text(MemberListPageLocator.otp_data)
        self.click(MemberListPageLocator.button_close_pop)
        return phone

    # 取得列表第一個QQ帳號
    def get_member_qqaccount(self):
        self.wait_visibility(MemberListPageLocator.qq_account_eye)
        self.click(MemberListPageLocator.qq_account_eye)
        self.wait_visibility(MemberListPageLocator.input_otp)
        self.type(MemberListPageLocator.input_otp, '1')
        self.click(MemberListPageLocator.button_otp_confirm)
        qqaccount = self.get_text(MemberListPageLocator.otp_data)
        self.click(MemberListPageLocator.button_close_pop)
        return qqaccount

    # 取得列表第一個錢包地址
    def get_member_address(self):
        self.wait_visibility(MemberListPageLocator.address_eye)
        self.click(MemberListPageLocator.address_eye)
        self.wait_visibility(MemberListPageLocator.input_otp)
        self.type(MemberListPageLocator.input_otp, '1')
        self.click(MemberListPageLocator.button_otp_confirm)
        address = self.get_text(MemberListPageLocator.otp_data)
        self.click(MemberListPageLocator.button_close_pop)
        return address

    # 取得列表第一個會員資料欄位
    def get_member_info(self, number):
        self.wait_visibility(MemberListPageLocator.button_search)
        self.type(MemberListPageLocator.input_member_number, number)
        self.click(MemberListPageLocator.button_search)

        phone = self.get_member_phone()
        qq = self.get_member_qqaccount()
        name = self.get_member_name()
        address = self.get_member_address()
        info = {
            "phone": phone,
            "qq": qq,
            "name": name,
            "address": address
        }
        return info

    # 修改會員密碼
    def change_member_password(self, number, new_password='11111111'):
        self.wait_visibility(MemberListPageLocator.button_search)
        self.type(MemberListPageLocator.input_member_number, number)
        self.click(MemberListPageLocator.button_search)
        self.wait_loading_finish()
        assert self.is_element_finded(
            MemberListPageLocator.check_first_table(self, number)), f"會員列表第一行為未顯示該會員 {number}"
        self.scroll_to_element(MemberListPageLocator.button_change_password)
        self.click(MemberListPageLocator.button_change_password)
        self.wait_visibility(MemberListPageLocator.button_change_password_confirm)
        self.type(MemberListPageLocator.input_new_password, new_password)
        self.type(MemberListPageLocator.input_new_password_again, new_password)
        self.click(MemberListPageLocator.button_change_password_confirm)

        if self.wait_visibility_status(MemberListPageLocator.message_success) is False:
            raise EOFError("修改會員密碼，未顯示執行成功")
