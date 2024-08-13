from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class MarketCenterPageLocator:
    # ------------營銷中心------------
    menu_market_center = (By.XPATH, "//span[text()='营销中心']")

    # *幫助系統
    help_system = (By.XPATH, "//span[text()='帮助系统']")

    # *公告管理
    menu_announcement_management = (By.XPATH, "//span[text()='公告管理']")
    main_page_announcement = (By.XPATH, "//span[text()='首页公告']")
    login_announcement = (By.XPATH, "//span[text()='登入公告']")

    # *優惠公告
    offer_announcement = (By.XPATH, "//span[text()='优惠公告']")

    # *跑馬公告
    scrolling_text_announcement = (By.XPATH, "//span[text()='跑马公告']")

    # *介面管理
    menu_interface_management = (By.XPATH, "//span[text()='介面管理']")

    internal_link_management = (By.XPATH, "//span[text()='内部连结管理']")
    float_window_management = (By.XPATH, "//span[text()='浮窗管理']")
    shortcut_option_management = (By.XPATH, "//span[text()='快捷选项管理']")
    recommand_list_management = (By.XPATH, "//span[text()='推荐清单管理']")    
    navigation_bar_management = (By.XPATH, "//span[text()='导航栏管理']")
    carousel_management = (By.XPATH, "//span[text()='轮播管理']")
    activity_management = (By.XPATH, "//span[text()='活动管理']")

    # *自助優惠
    menu_self_service_offer = (By.XPATH, "//span[text()='自助优惠']")

    activity_list = (By.XPATH, "//span[text()='活动列表']")

    # *會員中心
    menu_member_center = (By.XPATH, "//span[text()='会员中心']")

    online_deposit = (By.XPATH, "//span[text()='线上充值']")
    deposit_tutorial_manegement = (By.XPATH, "//span[text()='充值教程管理']")

class MarketCenterPage(BasePage):
    # 營銷中心
    def into_market_center(self):
        self.wait_loading_finish()
        for _ in range(2):
            if self.is_element_finded(MarketCenterPageLocator.menu_market_center):
                break
            self.sleep(5)
        self.sleep(3)
        self.click(MarketCenterPageLocator.menu_market_center)

    # 營銷中心 -> 幫助系統
    def into_help_system(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.help_system)

    # 營銷中心 -> 公告管理
    def into_announce_management(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.menu_announcement_management)

    # 營銷中心 -> 公告管理 -> 首頁登入
    def into_mainpage_announcement(self):
        self.into_announce_management()
        self.click(MarketCenterPageLocator.main_page_announcement)

    # 營銷中心 -> 公告管理 -> 登入公告
    def into_login_announcement(self):
        self.into_announce_management()
        self.click(MarketCenterPageLocator.login_announcement)

    # 營銷中心 -> 優惠公告
    def into_offer_announcement(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.offer_announcement)

    # 營銷中心 -> 跑馬公告
    def into_scrolling_text_announcement(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.scrolling_text_announcement)

    # 營銷中心 -> 介面管理
    def into_interface_management(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.menu_interface_management)

    # 營銷中心 -> 介面管理 -> 內部連結管理
    def into_internal_link_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.internal_link_management)

    # 營銷中心 -> 介面管理 -> 浮窗管理
    def into_float_window_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.float_window_management)

    # 營銷中心 -> 介面管理 -> 快捷選項管理
    def into_shortcut_option_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.shortcut_option_management)

    # 營銷中心 -> 介面管理 -> 推薦清單管理
    def into_recommand_list_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.recommand_list_management)

    # 營銷中心 -> 介面管理 -> 導航欄管理
    def into_navigation_bar_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.navigation_bar_management)

    # 營銷中心 -> 介面管理 -> 輪播管理
    def into_carousel_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.carousel_management)

    # 營銷中心 -> 介面管理 -> 活動管理
    def into_activity_management(self):
        self.into_interface_management()
        self.click(MarketCenterPageLocator.activity_management)

    # 營銷中心 -> 自助優惠
    def into_self_service_offer(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.menu_self_service_offer)

    # 營銷中心 -> 自助優惠 -> 活動列表
    def intoActivityList(self):
        self.into_self_service_offer()
        self.click(MarketCenterPageLocator.activity_list)

    # 營銷中心 -> 會員中心
    def into_member_center(self):
        self.into_market_center()
        self.click(MarketCenterPageLocator.menu_member_center)

    # 營銷中心 -> 會員中心 -> 線上充值
    def into_online_deposit(self):
        self.into_member_center()
        self.click(MarketCenterPageLocator.online_deposit)

    # 營銷中心 -> 會員中心 -> 充值教程管理
    def into_deposit_tutorial_management(self):
        self.into_member_center()
        self.click(MarketCenterPageLocator.deposit_tutorial_manegement)