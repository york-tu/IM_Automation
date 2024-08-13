from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class MenuPageLocator:
    # LOADING
    seach_loading_mask = (By.XPATH, "//button[@class='btn btn-sm btn-primary']")

    # RESELLER MENU (後台主選單)
    agent_info = (By.XPATH, "//td[contains(@data-bind, 'userAccount')]")  # 代理帳號
    exclusive_domain_info = (By.XPATH, "//td[text()='专属域名']/..//span[@class='domain']") #專屬域名
    promote_domain_info = (By.XPATH, "//td[text()='推广域名']/..//span[@class='domain']") # 推廣域名
    system_time = (By.XPATH,"//span[contains(@data-bind,'currentTime')]") # 系統時間

    def check_agent_name(self,Agent):
        agent_name = (By.XPATH,"//a[@class='dropdown-toggle']//span[contains(text(),'%s')]"%Agent) # 右上方代理帳號
        return agent_name


    # RESELLER 財務管理
    financial_management = (By.XPATH, "//h3[text()='财务查询']")
    agent_settlement = (By.XPATH, "//a[contains(@href,'/statement')]")
    new_agent_settlement = (By.XPATH, "//a[contains(@href,'/agentsettlement')]")

    structure_inquiry = (By.XPATH, '//h3[text()="体系查询"]')   # 體系查詢
    member_list = (By.XPATH, '//span[text()="会员列表"]')   # 會員列表
    agent_list = (By.XPATH, '//span[text()="代理列表"]')    # 代理列表
    
    # 有效會員頁面
    operational_Inquiry = (By.XPATH, "//h3[text()='运营查询']")
    valid_Member = (By.XPATH, "//span[text()='有效会员']")
    # 注單查詢頁面
    note_search = (By.XPATH, "//span[text()='注单查询']")
    financial_inquiry = (By.XPATH, "//h3[text()='财务查询']")  # 財務查詢
    general_report = (By.XPATH, "//span[text()='一般报表']/..")  # 一般報表
    daily_report = (By.XPATH, "//span[text()='每日报表']/..")  # 每日報表


class MenuPage(BasePage):

    # 檢查首頁資訊
    def check_agentinfo(self,Agent,Domain):
        self.wait_loading_finish()
        today= self.get_us_time().strftime("%Y-%m-%d")

        assert self.get_text(MenuPageLocator.agent_info) == Agent,'主頁代理帳號顯示錯誤'
        assert self.get_text(MenuPageLocator.exclusive_domain_info) == "%s.com"%Domain,'主頁專屬域名顯示錯誤'
        assert self.get_text(MenuPageLocator.promote_domain_info) == "https://%s.com/reg"%Domain,'主頁推廣域名顯示錯誤'
        assert str(self.get_text(MenuPageLocator.system_time)).__contains__(today),'主頁系同時間日期顯示錯誤'
        assert self.get_text(MenuPageLocator.check_agent_name(self,Agent)) == Agent,'主頁右上代理帳號顯示錯誤'

    # 進入代理結算(舊版)
    def into_old_agent_settlementpage(self):
        self.wait_loading_finish()

        for _ in range(0,2):
            if self.wait_visibility(MenuPageLocator.financial_management) is True:
                break
            self.sleep(1)

        self.click(MenuPageLocator.financial_management)
        self.click(MenuPageLocator.agent_settlement)

        self.wait_loading_finish()

    # 進入代理結算(新版)
    def into_new_agent_settlementpage(self):
        self.wait_loading_finish()

        for _ in range(0,2):
            if self.wait_visibility(MenuPageLocator.financial_management) is True:
                break
            self.sleep(1)

        self.click(MenuPageLocator.financial_management)
        self.click(MenuPageLocator.new_agent_settlement)

        self.wait_loading_finish()
    
    # 進入一般報表
    def into_general_report(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.financial_inquiry)
        self.click(MenuPageLocator.general_report)

    # 點擊體系查詢
    def click_on_structure_inquiry(self):
        self.click(MenuPageLocator.structure_inquiry)
    
    # 點擊會員列表
    def click_on_member_list(self):
        self.wait_loading_finish()
        self.click_on_structure_inquiry()    # 點擊體系查詢
        self.click(MenuPageLocator.member_list)

    # 點擊代理列表
    def click_on_agent_list(self):
        self.wait_loading_finish()
        self.click_on_structure_inquiry()    # 點擊體系查詢
        self.click(MenuPageLocator.agent_list)

    # 進入每日報表
    def into_daily_report(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.financial_inquiry)
        self.click(MenuPageLocator.daily_report)

    # 到有效會員頁面
    def check_validmember(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.operational_Inquiry)
        self.click(MenuPageLocator.valid_Member)
        
    # 到注單查詢頁面
    def check_notesearch(self):
        self.wait_loading_finish()       
        self.click(MenuPageLocator.operational_Inquiry)
        self.click(MenuPageLocator.note_search) 
    