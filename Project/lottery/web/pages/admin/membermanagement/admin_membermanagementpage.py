from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class MemberManagementPageLocator:
    # ------------會員管理分類------------
    menu_member_management = (By.XPATH, "//span[text()='会员管理']")  # 會員管理

    # *會員管理
    member_management = (By.XPATH, "//a//span[text()='会员管理']/..")  # 會員管理-會員管理

    level_management = (By.XPATH, "//span[text()='层级管理']")
    ok_point_level_management = (By.XPATH, "//ul[@class='page-breadcrumb']//a[text()='层级管理']")

    member_list = (By.XPATH, "//span[text()='会员列表']/..")  # 會員管理-會員管理-會員列表
    two_level_domain_name_setting = (By.XPATH, "//span[text()='二级域名设定']")
    ok_point_member_list = (By.XPATH, "//i[@class='fa fa-list']")   # 確認進入會員列表\

    # *會員分析
    member_analysis = (By.XPATH, "//li[@permission-id='member.betAnalysis']//span[text()='会员分析']")

    # *輸贏監控
    gaming_surveillance = (By.XPATH, "//span[text()='输赢监控']")

class MemberManagementPage(BasePage):
    # 會員管理
    def into_menu_member_management(self):
        self.wait_loading_finish()
        for _ in range(2):
            if self.is_element_finded(MemberManagementPageLocator.menu_member_management):
                break
            self.sleep(5)
        self.sleep(3)
        self.click(MemberManagementPageLocator.menu_member_management)

    # 會員管理 -> 會員管理
    def into_member_management(self):
        self.into_menu_member_management()
        self.click(MemberManagementPageLocator.member_management)

    # 會員管理 -> 會員管理 -> 層級管理
    def into_level_management(self):
        self.into_member_management()
        self.click(MemberManagementPageLocator.level_management)
        self.wait_visibility(MemberManagementPageLocator.ok_point_level_management)
        self.wait_loading_finish()
    
    # 會員管理 -> 會員管理 -> 會員列表
    def into_member_list(self):
        self.into_member_management()
        self.click(MemberManagementPageLocator.member_list)
        self.wait_visibility(MemberManagementPageLocator.ok_point_member_list)
        self.wait_loading_finish()

    # 會員管理 -> 會員管理 -> 二級域名設定
    def into_twolevel_domain_name_setting(self):
        self.into_member_management()
        self.click(MemberManagementPageLocator.two_level_domain_name_setting)

    # 會員管理 -> 會員分析
    def into_member_analysis(self):
        self.into_menu_member_management()
        self.click(MemberManagementPageLocator.member_analysis)

    # 會員管理 -> 輸贏監控
    def into_gaming_surveillance(self):
        self.into_menu_member_management()
        self.click(MemberManagementPageLocator.gaming_surveillance)
