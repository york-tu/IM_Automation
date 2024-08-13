from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class SystemManagementPageLocator:
    # ------------系統管理--------------
    menu_system_management = (By.XPATH, "//span[text()='系统管理']/..")

    # *人員管理
    menu_personal_management = (By.XPATH, "//span[text()='人员管理']")

    account_management = (By.XPATH, "//span[text()='帐号管理']")
    agent_management = (By.XPATH, "//span[text()='体系管理']")
    character_management = (By.XPATH, "//span[text()='角色管理']")

    # *日誌查詢
    menu_log_inquire = (By.XPATH, "//span[text()='日志查询']")

    login_log = (By.XPATH, "//span[text()='登录日志']")
    operating_log = (By.XPATH, "//span[text()='操作日志']")
    deposits_log = (By.XPATH, "//span[text()='上下分日志']")

    # *頻道管理
    channel_management = (By.XPATH, "//span[text()='频道管理']")

    # *遊戲設定
    menu_game_setting = (By.XPATH, "//span[text()='游戏设定']")

    game_management = (By.XPATH, "//span[text()='游戏管理']")
    classification_management = (By.XPATH, "//span[text()='分类管理']")

    # *系統設定
    menu_system_setting = (By.XPATH, "//span[text()='系统设定']/..")

    website_setting = (By.XPATH, "//span[text()='网站设定']")
    ok_point_website_setting = (By.XPATH,"//ul[@class='page-breadcrumb']//a[contains(text(), '网站设定')]")
    copywriting_setting = (By.XPATH, "//span[text()='文案设定']")
    currency_setting = (By.XPATH, "//span[text()='币别设定']")
    bank_setting = (By.XPATH, "//span[text()='银行设定']")
    game_demo_setting = (By.XPATH, "//span[text()='试玩设定']")
    alert_setting = (By.XPATH, "//span[text()='警示设定']")
    app_setting = (By.XPATH, "//span[text()='APP设定']")

class SystemManagementPage(BasePage):
    # 系統管理
    def into_system_management(self):
        self.wait_loading_finish()
        for _ in range(2):
            if self.is_element_finded(SystemManagementPageLocator.menu_system_management) is True:
                break
            self.sleep(5)
            
        self.sleep(3)
        self.click(SystemManagementPageLocator.menu_system_management)
        
    # 系統管理 -> 人員管理
    def into_personal_management(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.menu_personal_management)
        
    # 系統管理 -> 人員管理 -> 帳號管理
    def into_account_management(self):
        self.into_personal_management()
        self.click(SystemManagementPageLocator.account_management)

    # 系統管理 -> 人員管理 -> 體系管理
    def into_agent_management(self):
        self.into_personal_management()
        self.click(SystemManagementPageLocator.agent_management)
        self.wait_loading_finish()
        
    # 系統管理 -> 人員管理 -> 角色管理
    def into_character_management(self):
        self.into_personal_management()
        self.click(SystemManagementPageLocator.character_management)
        
    # 系統管理 -> 日誌查詢
    def into_menu_log_inquire(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.menu_log_inquire)

    # 系統管理 -> 日誌查詢 -> 登入日誌
    def into_login_log(self):
        self.into_menu_log_inquire()
        self.click(SystemManagementPageLocator.login_log)
        
    # 系統管理 -> 日誌查詢 -> 操作日誌
    def into_operating_log(self):
        self.into_menu_log_inquire()
        self.click(SystemManagementPageLocator.operating_log)
        
    # 系統管理 -> 日誌查詢 -> 上下分日志
    def into_deposits_log(self):
        self.into_menu_log_inquire()
        self.click(SystemManagementPageLocator.deposits_log)

    # 系統管理 -> 頻道管理
    def into_channel_management(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.channel_management)

    # 系統管理 -> 遊戲設定
    def into_menu_game_setting(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.menu_game_setting)

    # 系統管理 -> 遊戲設定 -> 遊戲管理
    def into_game_management(self):
        self.into_menu_game_setting()
        self.click(SystemManagementPageLocator.game_management)

    # 系統管理 -> 遊戲設定 -> 分類管理
    def into_classification_management(self):
        self.into_menu_game_setting()
        self.click(SystemManagementPageLocator.classification_management)

    # 系統管理 -> 系統設定
    def into_system_setting(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.menu_system_setting)

    # 系統管理 -> 系統設定 -> 網站設定
    def into_admin_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.website_setting)
        self.wait_visibility(SystemManagementPageLocator.ok_point_website_setting)
        self.wait_loading_finish()

    # 系統管理 -> 系統設定 -> 文案設定
    def into_copywriting_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.copywriting_setting)

    # 系統管理 -> 系統設定 -> 幣別設定
    def into_currency_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.currency_setting)

    # 系統管理 -> 系統設定 -> 銀行設定
    def into_bank_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.bank_setting)

    # 系統管理 -> 系統設定 -> 試玩設定
    def into_game_demo_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.game_demo_setting)

    # 系統管理 -> 系統設定 -> 警示設定
    def into_alert_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.alert_setting)

    # 系統管理 -> 系統設定 -> APP設定
    def into_app_setting(self):
        self.into_system_setting()
        self.click(SystemManagementPageLocator.app_setting)