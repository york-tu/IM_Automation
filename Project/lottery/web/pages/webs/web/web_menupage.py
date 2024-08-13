from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage

class MenuPageLocator:
    # MENU (網站主選單)
    menu_index = (By.XPATH, "//*[@id='nzc-nav-index' or @class='home-sidebar']")
    check_point_index = (By.XPATH, "//div[@class='slider_main' or @class='layout-main ']")
    menu_lottery = (By.XPATH, "//div[@class='nav' or @class='home-sidebar']//a[contains(text(),'彩票') or @href='/lottery']/..")
    check_point_lottery = (By.XPATH, "//*[contains(@class, 'lottery')]")
    menu_game = (By.XPATH, "//a[contains(text(),'棋牌游戏') or @href='/qipai']/..")
    check_point_game = (By.XPATH, "//div[@class='search-dzyy' or @class='search' or @class='lottery_main']")
    menu_casino = (By.XPATH, "//a[contains(text(),'真人') or @href='/casino']/..")
    check_point_casino = (By.XPATH, "//img[contains(@alt,'视讯')]")
    menu_sport = (By.XPATH, "//a[contains(text(),'体育') or @href='/sport']/..")
    check_point_sport = (By.XPATH, "//*[@class='sports_item' or @class='sport-01']")
    menu_fish = (By.XPATH, "//a[contains(text(),'捕鱼') or @href='/fish']/..")
    check_point_fish = (By.XPATH, "//div[@class='fish_brand' or @class='fish-01']")
    menu_promo = (By.XPATH, "//a[contains(text(),'优惠') or contains(text(),'优势') or @href='/promo']/..")
    check_point_promo = (By.XPATH, "//div[@class='list-yh' or @class='content promo']")
    menu_electronic = (By.XPATH, "//a[contains(text(),'电子') or @href='/games']/..") # 電子遊戲
    message = (By.XPATH, '//a[contains(text(), "讯息")]') # 訊息
    menu_service = (By.XPATH, "//*[@id='nzc-nav-service' or (text()='在线客服' and @id='nzc-nav-faq') or @class='menu__item item-10']") # 在線客服

    
    # 帳戶餘額
    menu_member_balance_wallet = (By.XPATH, "//*[@id='nzc-header-balance' or @data-bind='text: balanceText']")

    # MEMBER MENU (會員專區選單)
    menu_member_deposit = (By.XPATH, "//a[@id='nzc-header-deposit' or text()='线上存款']")
    check_point_deposit = (By.XPATH, "//li[@class='active' and contains(text(),'线上存款')]")

    menu_member_withdraw = (By.XPATH, "//*[@id='nzc-header-withdraw' or text()='线上取款']")
    check_point_withdraw = (By.XPATH, "//li[@class='active' and contains(text(),'线上取款')]")
    menu_member_wallet = (By.XPATH, "//a[text()='额度转换' and @href]")
    check_point_wallet = (By.XPATH, "//li[@class='active' and contains(text(),'额度管理')]")
    menu_member_center = (By.XPATH, "//a[text()='会员中心']")
    check_point_center = (By.XPATH, "//*[@class='main-title info' and contains(text(),'我的资料')]")

    # 額度轉換
    menu_wallet = (By.ID, "nzc-wallet-nav-wallet")  # 額度管裡

class MenuPage(BasePage):
    def into_menu_index(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_index)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_index) is True

    def into_menu_lottery(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_lottery)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_lottery) is True,'進入彩票錯誤'

    def into_menu_game(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_game)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_game) is True,'進入棋牌錯誤'

    def into_menu_electronic(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_electronic)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_game) is True,'進入電子錯誤'

    def into_menu_casino(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_casino)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_casino) is True,'進入視訊錯誤'

    def into_menu_sport(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_sport)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_sport) is True,'進入體育賽事錯誤'

        # 全民捕魚
    def into_menu_fish(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_fish)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_fish) is True,'進入全民捕魚錯誤'

        # 優惠活動
    def into_menu_promo(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.menu_promo)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_promo) is True,'進入優惠活動錯誤'

        # 在線客服
    def into_menu_service(self):
        self.wait_loading_finish()
        self.open_wait_new_window(MenuPageLocator.menu_service) # 點擊在線客服開啟新分頁
        self.wait_loading_finish()
        self.sleep(2)
        service_url = self.get_url()
        assert ("mynah-client" in service_url) or ("chatroom?" in service_url) is True, f"在線客服導轉不為客服寶網址:{service_url}" 
        self.switch_home_page()

        # 線上存款
    def into_menu_member_deposit(self):
        self.wait_loading_finish()
        wallet = round(float(self.get_text(MenuPageLocator.menu_member_balance_wallet)),2)
        self.wait_visibility(MenuPageLocator.menu_member_deposit)
        self.click(MenuPageLocator.menu_member_deposit)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_deposit) is True,'進入線上存款錯誤'
        return wallet

        # 線上取款
    def into_menu_member_withdraw(self):
        self.wait_loading_finish()
        self.wait_visibility(MenuPageLocator.menu_member_withdraw)
        self.sleep(2)
        self.click(MenuPageLocator.menu_member_withdraw)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_withdraw) is True,'進入線上取款錯誤'

        # 額度轉換
    def into_menu_member_wallet(self):
        self.wait_loading_finish()
        self.sleep(1)
        
        if self.is_element_finded(MenuPageLocator.menu_member_wallet) is True:
            self.click(MenuPageLocator.menu_member_wallet)
        else:
            # CDD首頁沒有額度轉換,從線上存款進入
            self.click(MenuPageLocator.menu_member_deposit)
            self.wait_loading_finish()
            assert self.is_element_displayed(MenuPageLocator.check_point_deposit) is True,'進入額度轉換錯誤'
            self.click(MenuPageLocator.menu_wallet)
            
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_wallet) is True,'進入額度轉換錯誤'

        # 會員中心
    def into_menu_member_center(self):
        self.wait_loading_finish()
        self.wait_visibility(MenuPageLocator.menu_member_center)
        self.click(MenuPageLocator.menu_member_center)
        self.wait_loading_finish()
        assert self.wait_visibility_status(MenuPageLocator.check_point_center) is True,'進入會員中心錯誤'

    # 進入訊息中心
    def into_message_center(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.message)

        # 抓取帳戶餘額
    def get_balance_wallet(self):
        wallet = round(float(self.get_text(MenuPageLocator.menu_member_balance_wallet)), 2)
        return wallet