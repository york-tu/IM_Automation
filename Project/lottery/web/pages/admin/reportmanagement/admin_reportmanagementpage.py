from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class ReportManagementPageLocator:
    # ------------報表管理分類------------
    menu_report_management = (By.XPATH, "//span[text()='报表管理']")
    # *一般報表
    menu_general_report = (By.XPATH, "//span[contains(text(),'一般报表')]")
    ok_point_general_report = (By.XPATH, "//span[@class='el-breadcrumb__inner']//a[contains(text(), '一般报表')]")

    # *有效会员
    menu_effective_member_report = (By.XPATH, "//span[contains(text(),'有效会员')]")
    ok_point_effective_member_report = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '有效会员')]")

    # *毛利分析
    menu_gross_profit_analysis_report = (By.XPATH, "//span[contains(text(),'毛利分析')]")
    ok_point_gross_profit_analysis_report = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '毛利分析')]")

    # *频道报表
    menu_channel_report = (By.XPATH, "//span[contains(text(),'频道报表')]")
    ok_point_channel_report = (By.XPATH, "//span[@class='el-breadcrumb__inner']//span[contains(text(), '频道报表')]")

    # *每日报表
    menu_daily_report = (By.XPATH, "//span[contains(text(),'每日报表')]")
    ok_point_daily_report = (By.XPATH, "//span[@class='el-breadcrumb__inner']//span[contains(text(), '每日报表')]")

    # *水位报表
    menu_water_report = (By.XPATH, "//span[contains(text(),'水位报表')]")
    ok_point_water_report = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '水位报表')]")

    # *彩票分析
    menu_lottery_analysis_report = (By.XPATH, "//span[contains(text(),'彩票分析')]")
    ok_point_lottery_analysis_report = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '彩票分析')]")

class ReportManagementPage(BasePage):
    def click_report_management(self):
        self.wait_loading_finish()
        for _ in range(0,2):
            if self.is_element_finded(ReportManagementPageLocator.menu_report_management) is True:
                break
            self.sleep(5)
        self.sleep(3)
        self.click(ReportManagementPageLocator.menu_report_management)

    # 報表管理 -> 一般報表
    def into_general_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_general_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_general_report)
        self.wait_loading_finish()
    
    # 報表管理 -> 有效會員
    def into_effective_member_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_effective_member_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_effective_member_report)
        self.wait_loading_finish()

    # 報表管理 -> 毛利分析
    def into_gross_profit_analysis_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_gross_profit_analysis_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_gross_profit_analysis_report)
        self.wait_loading_finish()

    # 報表管理 -> 頻道報表
    def into_channel_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_channel_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_channel_report)
        self.wait_loading_finish()

    # 報表管理 -> 每日報表
    def into_daily_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_daily_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_daily_report)
        self.wait_loading_finish()
    
    # 報表管理 -> 水位報表
    def into_water_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_water_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_water_report)
        self.wait_loading_finish()

    # 報表管理 -> 彩票分析
    def into_lottery_analysis_report(self):
        self.click_report_management()
        self.click(ReportManagementPageLocator.menu_lottery_analysis_report)
        self.wait_visibility(ReportManagementPageLocator.ok_point_lottery_analysis_report)
        self.wait_loading_finish()
    