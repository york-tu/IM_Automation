from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
from pages.webs.mobile.mobile_menupage import MenuPage



class MemberCenterPageLocator:

    # 我的資料
    account_btn = (By.XPATH, "//*[contains(text(),'我的资料')]")
    board_nwap = (By.XPATH, "//div[@class='img-board img-board--auto']") # nwap 獨有上方區塊

    # 登出
    btn_logout = (By.XPATH, "//span[text()='登出'or text()='账号登出']")
    checkponint_logout = (By.XPATH, "//*[contains(text(), '登入') or text()='登录']")
    scroll_nwap_js = "com-inner__content"

    # 充值紀錄
    menu_deposit_in_report=(By.XPATH, "//*[@id='nzc-menu-deposit' or text()= '充值记录']")

    # 提款紀錄
    menu_deposit_out_report=(By.XPATH, "//*[@id='nzc-menu-withdraw' or text()= '提款记录']")
    check_menu_deposit_report=(By.XPATH, "//div[@class= 'com-inner__content' or @class= 'wallet_list']")

    # 投注紀錄
    menu_member_order_report=(By.XPATH, "//*[@id='nzc-menu-order' or text()='投注记录']")
    check_member_order_report=(By.XPATH, "//div[@class= 'order_list' or @class= 'com-inner__content']")

    # 額度管理
    link_wallet_conversion=(By.XPATH, "//*[@id='nzc-menu-wallet' or text()= '转账']")
    check_point_wallet_conversion = (By.XPATH, "//*[text()= '一键归户']")

    # 存款
    link_deposit=(By.XPATH, "//*[@id='nzc-menu-wallet' or text()= '充值']")
    check_point_deposit = (By.XPATH, "//span[contains(@class, 'logo') and text()= '充值']")

    #聊天室
    link_chatroom = (By.XPATH, "//a[@href='/m/stock/chatroom']")
    check_point_chatroom = (By.XPATH, "//div[@class='wcr-list']")

    # 交易流水
    link_wallet_report=(By.XPATH, "//*[@id='nzc-menu-history' or text()= '交易流水']")
    check_point_wallet_report = (By.XPATH, "//div[@class= 'wallet_list' or @class= 'mywallet']")

    # 玩法說明
    link_description = (By.XPATH, "//*[@id='nzc-menu-rule']")
    check_description = (By.XPATH, "//*[@class='rule']")

    # 消息
    link_news = (By.XPATH, "//*[@id='nzc-menu-inbox']")
    check_news = (By.XPATH, "//*[@class='main_content']")

    # 聯盟合作
    link_together = (By.XPATH, "//*[@id='nzc-menu-join']")
    check_together = (By.XPATH, "//*[@class='reseller']")

    # 提現
    link_withdraw = (By.XPATH, "//*[text()='提现' or text()='提款']") # 提現按鈕
    check_point_withdraw = (By.XPATH, "//div[@class='withdraw-entrance']") # 提現方式區塊

    # 餘額
    owner_total_money = (By.XPATH, "//span[@class='list-text price']")

    # 意見反饋
    feedback = (By.XPATH, "//*[text()= '意见反馈']")
    check_feedback = (By.XPATH, "//*[contains(text(), '提交反馈')]")
class MemberCenterPage(BasePage):
    # 點擊我的資料
    def into_member_info(self):
        MenuPage.into_member_center(self)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(MemberCenterPageLocator.account_btn)
        self.wait_loading_finish()

    # 登出
    def do_logout(self):
        self.wait_loading_finish()
        if self.is_element_finded(MemberCenterPageLocator.board_nwap) is True:
            self.scroll_bottom_java(MemberCenterPageLocator.scroll_nwap_js)
        self.click(MemberCenterPageLocator.btn_logout)
        self.wait_loading_finish()
        assert self.is_element_displayed(MemberCenterPageLocator.checkponint_logout) is True,'登出失敗'

    # 入款紀錄
    def into_deposit_in_report(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.menu_deposit_in_report)
        self.wait_loading_finish()
        self.sleep(1)
        assert self.is_element_finded(MemberCenterPageLocator.check_menu_deposit_report) is True

    # 出款紀錄
    def into_deposit_out_report(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.menu_deposit_out_report)
        self.wait_loading_finish()
        self.sleep(1)
        assert self.is_element_finded(MemberCenterPageLocator.check_menu_deposit_report) is True

    # AA聊天室
    def into_chatroom(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_chatroom)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_point_chatroom) is True

    # 額度管理
    def into_wallet_conversion(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_wallet_conversion)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_point_wallet_conversion) is True

    # 存款
    def into_deposit(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_deposit)
        self.sleep(1)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_point_deposit) is True

    # 交易流水
    def into_wallet_Report(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_wallet_report)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_point_wallet_report) is True

    # 玩法說明
    def into_description(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_description)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_description) is True

    # 消息
    def into_news(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_news)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_news) is True
    # 意見反饋
    def into_feedback(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.feedback)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_feedback) is True

    # 聯盟合作
    def into_together(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.link_together)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberCenterPageLocator.check_together) is True

    #  提現
    def into_withdraw(self):
        self.wait_loading_finish()
        self.wait_visibility(MemberCenterPageLocator.link_withdraw)
        self.click(MemberCenterPageLocator.link_withdraw)
        self.wait_visibility(MemberCenterPageLocator.check_point_withdraw)
        self.wait_loading_finish()

        assert self.is_element_finded(MemberCenterPageLocator.check_point_withdraw) is True

    #  投注紀錄
    def into_member_order(self):
        self.wait_loading_finish()
        self.click(MemberCenterPageLocator.menu_member_order_report)
        self.wait_loading_finish()
        self.sleep(1)
        assert self.is_element_finded(MemberCenterPageLocator.check_member_order_report) is True
    
    #  取得帳戶餘額
    def get_owner_money(self):
        owner_money = round( float(self.get_text(MemberCenterPageLocator.owner_total_money).replace(',', '').replace('元', '')) ,2)
        return owner_money
