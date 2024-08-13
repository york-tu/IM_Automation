from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class MenuLocator:
    menu_dashboard = (By.XPATH, "//div[@class='el-scrollbar__view']//span[text()='仪表板']")            #左側導航 儀錶板
    menu_dashboard_check = (By.XPATH, "//div[@class='dashboard-text' and text()='欢迎使用客服宝']")
    menu_chat = (By.XPATH, "//a[@href='/chat/board']")                                          #左側導航 會話板
    menu_chat_check = (By.XPATH, "//div[@class='ly-rgt']/p[text()='请选择聊天群组']")
    menu_history = (By.XPATH, "//a[@href='/history/serviceHistory']")                                   #左側導航 接待信息
    menu_history_check = (By.XPATH, "//h2[@class='title' and text()='接待信息']")

    menu_statistics = (By.XPATH, "//div[@class='el-submenu__title']//*[contains(text(),'数据统计')]")    #左側導航 数据统计
    menu_statistics_group = (By.XPATH, "//a[@href='/statistics/csr_group_statistics']")                 #左側導航 客服組数据统计
    menu_statistics_group_check = (By.XPATH, "//div[@class='cell' and text()='平均每日接待量']")

    menu_setting = (By.XPATH, "//div[@class='el-submenu__title']//*[contains(text(),'设置')]")          #左側導航 設置
    menu_sh = (By.XPATH, "//div[@class='el-submenu__title']//*[contains(text(),'商号管理')]")           #左側導航 商號管理
    menu_rules = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'对话规则')]")                #左側導航 對話規則
    menu_rules_check = (By.XPATH, "//h2[text()='对话规则']")
    menu_sh_list = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'商号帐号列表')]")          #左側導航 商号帐号列表
    menu_sh_list_check = (By.XPATH, "//h2[@class='title' and text()='商号帐号列表']")
    menu_sh_authority = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'商号权限管理')]")     #左側導航 商号权限管理
    menu_sh_authority_check = (By.XPATH, "//h2[@class='title' and text()='商号权限管理']")

    menu_site = (By.XPATH, "//div[@class='el-submenu__title']//*[contains(text(),'站点管理')]")         #左側導航 站点管理
    menu_site_list = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'站点列表')]")            #左側導航 站点列表
    menu_site_list_check = (By.XPATH, "//h2[@class='title' and text()='站点列表']")
    menu_form = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'询前表单')]")                 #左側導航 詢前表單 
    menu_form_check = (By.XPATH, "//h2[@class='title' and text()='询前表单']")
    menu_auto_response = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'自动回复')]")        #左側導航 自动回复 
    menu_auto_response_check = (By.XPATH, "//h2[@class='title' and text()='自动回复']")
    menu_ai_response = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'智能回复')]")        #左側導航 智能回复
    menu_ai_response_check = (By.XPATH, "//div[@class='aside-title' and text()='智能回复']")
    menu_promotion_ad = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'推广广告')]")         #左側導航 推广广告 
    menu_promotion_ad_check = (By.XPATH, "//h2[@class='title' and text()='推广广告']")
    menu_score_item = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'客服评分项目')]")       #左側導航 客服评分项目 
    menu_score_item_check = (By.XPATH, "//h2[@class='title' and text()='客服评分项目']")

    menu_cs = (By.XPATH, "//div[@class='el-submenu__title']//*[contains(text(),'客服管理')]")            #左側導航 客服管理
    menu_cs_list = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'客服列表')]")              #左側導航 客服列表
    menu_cs_list_check = (By.XPATH, "//h2[@class='title' and text()='客服列表']")
    menu_cs_authority = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'客服权限管理')]")     #左側導航 客服权限管理 
    menu_cs_authority_check = (By.XPATH, "//h2[@class='title' and text()='客服权限管理']")
    menu_score_statistics = (By.XPATH, "//div[@class='nest-menu']//*[contains(text(),'客服评分统计')]") #左側導航 客服评分统计 
    menu_score_statistics_check = (By.XPATH, "//h2[@class='title' and text()='客服评分统计']")

class AdminMenuPage(AdminBasePage):

    # 回到 儀錶板
    def into_dashBoard_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_dashboard)
            self.click(MenuLocator.menu_dashboard)
            self.wait_visibility(MenuLocator.menu_dashboard_check)
        except:
            raise EOFError("後台進入會話板失敗")


    # 進入 會話板
    def into_chatBoard_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_chat)
            self.click(MenuLocator.menu_chat)
            self.wait_visibility(MenuLocator.menu_chat_check)
        except:
            raise EOFError("後台進入會話板失敗")


    # 進入 接待信息
    def into_history_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_history)            
            self.click(MenuLocator.menu_history)
            self.wait_visibility(MenuLocator.menu_history_check)
        except:
            raise EOFError("後台進入接待信息失敗")


    # 進入 對話規則
    def into_rules_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)    #導航欄 設置
            self.wait_visibility(MenuLocator.menu_sh)
            self.click(MenuLocator.menu_sh)         #導航欄 商號管理
            self.wait_visibility(MenuLocator.menu_rules)
            self.click(MenuLocator.menu_rules)      #導航欄 對話規則
            self.wait_visibility(MenuLocator.menu_rules_check)
        except:
            raise EOFError("後台進入對話規則失敗")
    
    
    # 進入 詢前表單
    def into_form_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)        #導航欄 設置
            self.wait_visibility(MenuLocator.menu_site)
            self.click(MenuLocator.menu_site)           #導航欄 站點管理
            self.wait_visibility(MenuLocator.menu_form)
            self.click(MenuLocator.menu_form)           #導航欄 詢前表單
            self.wait_visibility(MenuLocator.menu_form_check)
        except:
            raise EOFError("後台進入詢前表單失敗")


    # 進入 智能回覆
    def into_ai_response_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)        #導航欄 設置
            self.wait_visibility(MenuLocator.menu_site)
            self.click(MenuLocator.menu_site)           #導航欄 站點管理
            self.wait_visibility(MenuLocator.menu_ai_response)
            self.click(MenuLocator.menu_ai_response)           #導航欄 智能回覆
            self.wait_visibility(MenuLocator.menu_ai_response_check)
        except:
            raise EOFError("後台進入智能回覆失敗")


    # 進入 推廣廣告
    def into_promotion_ad_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)                #導航欄 設置
            self.wait_visibility(MenuLocator.menu_site)
            self.click(MenuLocator.menu_site)                   #導航欄 站點管理
            self.wait_visibility(MenuLocator.menu_promotion_ad)
            self.click(MenuLocator.menu_promotion_ad)           #導航欄 推廣廣告
            self.wait_visibility(MenuLocator.menu_promotion_ad_check)
        except:
            raise EOFError("後台進入推廣廣告失敗")
    # 進入 客服評分項目
    def into_score_item_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)        #導航欄 設置
            self.wait_visibility(MenuLocator.menu_site)
            self.click(MenuLocator.menu_site)           #導航欄 站點管理
            self.wait_visibility(MenuLocator.menu_score_item)
            self.click(MenuLocator.menu_score_item)           #導航欄 詢前表單
            self.wait_visibility(MenuLocator.menu_score_item_check)
        except:
            raise EOFError("後台進入客服評分項目失敗")

    # 進入 客服評分統計
    def into_score_statistics_page(self):
        self.sleep(2)
        try:
            self.wait_visibility(MenuLocator.menu_setting)            
            self.click(MenuLocator.menu_setting)        #導航欄 設置
            self.wait_visibility(MenuLocator.menu_cs)
            self.click(MenuLocator.menu_cs)           #導航欄 客服管理
            self.wait_visibility(MenuLocator.menu_score_statistics)
            self.click(MenuLocator.menu_score_statistics)           #導航欄 客服評分統計
            self.wait_visibility(MenuLocator.menu_score_statistics_check)
        except:
            raise EOFError("後台進入客服評分統計失敗")
