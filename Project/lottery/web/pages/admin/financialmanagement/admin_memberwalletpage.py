from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
import random


class MemberWallet_PageLocator(BasePage):
    # SEARCH AREA (查找條件區)
    member = (By.XPATH, "//input[contains(@data-bind, 'memberlogin')]")
    third_wallet = (By.XPATH, "//a[@class='select2-choice']")
    third_wallet_bar = (By.XPATH, "//ul[@class='select2-results']//text()[contains(.,'ag')]/..")
    wallet_money_down = (By.XPATH, "//input[contains(@data-bind, 'downbalance')]")
    wallet_money_up = (By.XPATH, "//input[contains(@data-bind, 'upbalance')]")
    day = (By.XPATH, "//input[contains(@data-bind, 'noupdatedday')]")
    search_btn = (By.XPATH, "//button[@id='btnSearch']")

    # 第一筆
    first_memebr = (By.XPATH, "(//td[contains(@data-bind, 'memberlogin')])[1]")
    first_wallet = (By.XPATH, "(//div[contains(@data-bind, 'walletname')])[1]")
    first_money = (By.XPATH, "(//td[contains(@data-bind, 'balance')])[1]")
    first_refresh_time = (By.XPATH, "(//td[contains(@data-bind, 'updatedtime')])[1]")
    first_refresh_btn = (By.XPATH, "(//i[@class= 'fa fa-refresh'])[1]")
    first_ledger_btn = (By.XPATH, "(//tbody[contains(@data-bind, 'foreach: items')]//a//text()[contains(.,'流水')]/..)[1]")
    ledger_title = (By.XPATH, "//*[@class='el-breadcrumb__inner']//*[text()='上下分流水']")

    # 整筆
    wallet = (By.XPATH, "//div[contains(@data-bind, 'walletname')]")
    money = (By.XPATH, "//td[contains(@data-bind, 'balance')]")

    # 總數
    total_pages = (By.XPATH, "//span[@data-bind='text: pager.total']")
    total_pages = (By.XPATH,"//span[contains(@data-bind,'pager.total')]") # 總頁數
    page_size = (By.XPATH,"//*[contains(@data-bind,'pageSize')]//option") # 每頁最多顯示筆數 個別
    page_list = (By.XPATH,"//*[contains(@data-bind,'pageSize')]") # 每頁最多筆數 總下拉式選單
    last_page = (By.XPATH, '//a[text()="尾页"]')
    rows = (By.XPATH,"//tbody[@data-bind='foreach: items']//tr") # 列

class MemberWalletPage(BasePage):
    # 所有查找方式
    def search_all(self, web_account, wallet_list_front):

        self.search_via_member_name(web_account, wallet_list_front)  # 透過會員帳號進行查找
        self.search_via_third_brand_name(web_account, wallet_list_front)  # 透過指定第三方進行查找
        self.search_via_money_range(web_account, wallet_list_front)  # 透過指定第三方進行查找
        self.search_via_day(web_account, wallet_list_front)  # 透過指定第三方進行查找

    def search_via_member_name(self, web_account, wallet_list_front):
        self.type(MemberWallet_PageLocator.member, web_account)
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()

        self.check_all_info(web_account, wallet_list_front)

    def search_via_third_brand_name(self, web_account, wallet_list_front):
        self.type(MemberWallet_PageLocator.member, web_account)
        self.click(MemberWallet_PageLocator.third_wallet)
        self.sleep(2)
        self.click(MemberWallet_PageLocator.third_wallet_bar)
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()

        self.check_all_info(web_account, wallet_list_front, reflash=True)

    def search_via_money_range(self, web_account, wallet_list_front):
        self.search_money(web_account, '1', '2')
        self.check_all_info(web_account, wallet_list_front, reflash=True)

        self.search_money(web_account, '0', '100000000000')
        self.check_all_info(web_account, wallet_list_front)

    def search_via_day(self, web_account, wallet_list_front):
        self.search_day(web_account, '10000')
        assert self.get_text(MemberWallet_PageLocator.total_pages) == '0', '不應該查到任何資料'

        self.search_day(web_account, '0')
        self.check_all_info(web_account, wallet_list_front)

    # 檢查各欄位名稱
    def check_all_info(self, web_account, wallet_list_front, reflash=False):
        today = self.get_us_time().strftime("%Y")
        name = []
        money_list = []

        self.wait_loading_finish()
        self.click(MemberWallet_PageLocator.first_refresh_btn)
        self.wait_loading_finish()

        self.type(MemberWallet_PageLocator.member, web_account)
        self.sleep(1)
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()

        for wallet in self.find_elements(MemberWallet_PageLocator.wallet):
            name.append(self.get_text_by_dom(wallet))

        for money in self.find_elements(MemberWallet_PageLocator.money):
            money_text = self.get_text_by_dom(money).replace(',', '')
            money_list.append(str(f'{float(money_text):.2f}'))

        wallet_list_back = list(zip(name, money_list))
        wallet_list_front = list(map(tuple, wallet_list_front))
        difference = set(wallet_list_front) - set(wallet_list_back)

        assert self.get_text(MemberWallet_PageLocator.first_memebr) == web_account, "找不到指定會員"
        
        if reflash == True:
            today = self.get_us_time().strftime("%Y-%m-%d %H")
            assert str(self.get_text(MemberWallet_PageLocator.first_refresh_time)).__contains__(today),'申請時間顯示不正確'
            assert self.get_text(MemberWallet_PageLocator.first_wallet) == 'AG', "找不到指定第三方品牌"
            assert self.get_text(MemberWallet_PageLocator.first_money) == '1', "可用餘額不正確 金額:{0}".format(self.get_text(MemberWallet_PageLocator.first_money))
        else:
            assert not difference, "差異的項目:{0}".format(difference)
            assert str(self.get_text(MemberWallet_PageLocator.first_refresh_time)).__contains__(today), '申請時間顯示不正確'

        self.click(MemberWallet_PageLocator.first_ledger_btn)
        self.switch_last_page()
        self.wait_loading_finish()
        self.sleep(2)
        assert self.is_element_finded(MemberWallet_PageLocator.ledger_title) == True, "導轉到上下分流水頁面錯誤"
        self.switch_home_page()

        self.refresh_browser()
        self.wait_loading_finish()
        self.scroll_to_top()

    # 每頁最大筆數測試
    def page_range(self):
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()

        self.max_num()
        self.scroll_to_top()

    def search_money(self, web_account, down, up):
        self.type(MemberWallet_PageLocator.member, web_account)
        self.type(MemberWallet_PageLocator.wallet_money_down, down)
        self.type(MemberWallet_PageLocator.wallet_money_up, up)
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()

    def search_day(self, web_account, day):
        self.type(MemberWallet_PageLocator.member, web_account)
        self.type(MemberWallet_PageLocator.day, day)
        self.click(MemberWallet_PageLocator.search_btn)
        self.wait_loading_finish()