from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import re
class MenuPageLocator:
    btn_promo=(By.XPATH,"//*[text()='优惠活动' or @href='/m/promo' or text()='活动']")
    link_promo = (By.XPATH, "//div[@class='content-bg-yhhd promo']")
    check_point_promo = (By.XPATH, "//div[@class='box1' or @class='com-inner__content' or @class='content-bg-yhhd promo']")
    check_nwap_promo = (By.XPATH, "//div[@class='com-inner__content']")
    promo_nwap = (By.XPATH, "//span[@class='logo-text' and text()='活动']")
    promo = (By.XPATH, "//*[contains(@class, 'promo')]")
    promo_frame = (By.ID, 'promo-iframe')
    # 會員中心
    link_membercenter = (By.XPATH, '//*[contains(@class, "item")]//*[contains(text(), "会员") or @href= "/m/member"]')
    check_point_membercenter = (By.XPATH, "//*[text()='意见反馈']")

    # 額度轉換
    link_wallet_conversion=(By.XPATH, "//*[@id='nzc-menu-wallet' or text()= '转账']")
    check_point_wallet_conversion = (By.XPATH, "//*[text()= '一键归户']")
    member_center_deposit = (By.XPATH, "//a[@href='/m/deposit']")
    btn_deposit_withdraw = (By.PARTIAL_LINK_TEXT, "存/取款")
    link_deposit=(By.XPATH, "//*[@id='nzc-menu-wallet' or text()= '充值']")
    check_point_deposit = (By.XPATH, "//div[@class='deposit_portal' or @class='my_deposit' or @class='nav navimg-up-board']")
    # check_point_deposit_OLD = (By.XPATH, "//div[@class='my_deposit']")

    link_trend = (By.PARTIAL_LINK_TEXT, "开奖走势")
    check_point_trend = (By.XPATH, "//div[@class='trend_list' or @class='award']")

    btn_customer_service = (By.PARTIAL_LINK_TEXT, "客服")
    link_wechat = (By.PARTIAL_LINK_TEXT, "微信客服")
    link_qq = (By.PARTIAL_LINK_TEXT, "客服QQ")
    live_chat = (By.PARTIAL_LINK_TEXT, "在线客服")

    check_menu_deposit_report=(By.XPATH, "//div[@class='wallet_list']")

      # 帳戶餘額
    menu_member_balance_wallet = (By.XPATH, "//*[@id='nzc-header-balance' or @data-bind='text: balanceText' or \
        contains(@class, 'wallet')]")

    chess_btn = (By.XPATH,"//*[text()='棋牌游戏']/..") # 棋牌
    electronic_btn = (By.XPATH,"//*[text()='电子游戏' or text()='电子']/..") # 電子
    sport_btn = (By.XPATH,"//*[text()='体育投注']/..") # 體育
    casino_btn = (By.XPATH,"//*[text()='真人娱乐' or text()='真人视讯']/..") # 真人
    fish_btn = (By.XPATH,"//*[text()='捕鱼王']/..") # 捕魚
    close_ad_btn = (By.XPATH,"//div[@class='downloadbar__close']")
    
    # 紅包按鈕
    red_envelope = (By.XPATH, "(//*[@href='/m/hb' or text()= '红包' or contains(text(), '红包游戏')])[last()]")
    mine_sweeping = (By.XPATH, '//*[@class="hbgame--link" and contains(@data-bind,"hbsl") or text()= "扫雷"]')
    niu_niu = (By.XPATH, '//*[@class="hbgame--link" and contains(@data-bind,"hbnn") or text()= "牛牛"]')

    #天天麻將紅包
    red_envelope_nwap = (By.XPATH, "//span[text()='红包']")
    mine_sweeping_nwap = (By.XPATH, "//span[text()='扫雷']")
    niu_niu_nwap = (By.XPATH, "//span[text()='牛牛']")
    
    # 消息
    link_news = (By.XPATH, "//a[@class='message-info']")
    check_news = (By.XPATH, "//div[@class='com-inner']")
    message = (By.XPATH, '//a[@class="message-info" or @id="nzc-menu-inbox"]')

    #聊天室
    chatroom_btn = (By.XPATH, "//p[contains(text(),'聊天室')]")
    
class MenuPage(BasePage):
    def into_promo(self, brand):
        self.wait_loading_finish()
        if self.is_element_finded(MenuPageLocator.btn_promo) is False:
            self.test_skip('無優惠活動連結')

        self.click(MenuPageLocator.btn_promo)
        self.wait_loading_finish()
        if self.is_element_finded(MenuPageLocator.promo_nwap) is True:
            self.wait_loading_finish()
            assert self.is_element_finded(MenuPageLocator.check_nwap_promo) is True    
        else:
            self.switch_frame(MenuPageLocator.promo_frame)
            assert self.is_element_finded(MenuPageLocator.check_point_promo) is True
            self.switch_default_frame()

    def into_red_envelope(self):
        self.wait_loading_finish()
        self.wait_visibility(MenuPageLocator.red_envelope)
        self.click(MenuPageLocator.red_envelope)

        self.wait_visibility(MenuPageLocator.mine_sweeping)
        self.wait_visibility(MenuPageLocator.niu_niu)

        assert self.is_element_finded(MenuPageLocator.mine_sweeping) is True, '找不到掃雷遊戲'
        assert self.is_element_finded(MenuPageLocator.niu_niu) is True, '找不到牛牛遊戲'

    def into_mine_sweeping(self):
        self.wait_loading_finish()
        self.into_red_envelope()
        self.wait_visibility(MenuPageLocator.mine_sweeping)
        self.sleep(1)
        self.click(MenuPageLocator.mine_sweeping)

    def into_niu_niu(self):
        self.wait_loading_finish()
        self.into_red_envelope()
        self.wait_visibility(MenuPageLocator.niu_niu)
        self.sleep(1)
        self.click(MenuPageLocator.niu_niu)
  
    def into_member_center(self):
        self.wait_loading_finish()
        self.sleep(1)
        self.click(MenuPageLocator.link_membercenter)
        self.wait_loading_finish()
        self.sleep(1)

        assert self.wait_visibility_status(MenuPageLocator.check_point_membercenter) is True

    def into_message(self):
        self.into_member_center()
        self.wait_loading_finish()
        self.click(MenuPageLocator.message)

    def into_wallet_conversion(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.link_wallet_conversion)
        self.wait_loading_finish()

        assert self.is_element_finded(MenuPageLocator.check_point_wallet_conversion) is True

    def into_deposit(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.link_membercenter)
        self.wait_loading_finish()
        self.wait_visibility(MenuPageLocator.link_deposit)
        self.click(MenuPageLocator.link_deposit)
        self.wait_loading_finish()

        for loop in range(0,7):
            self.sleep(2)
            
            if self.is_element_finded(MenuPageLocator.check_point_deposit) is True:
                return
            else:
                if loop == 6:
                    raise EOFError('進入存款頁面錯誤')

    def into_rend(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.link_trend)
        self.wait_loading_finish()

        assert self.is_element_finded(MenuPageLocator.check_point_trend) is True
    
    def into_news_nwap(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.link_news)
        self.wait_loading_finish()
        assert self.is_element_finded(MenuPageLocator.check_news) is True

    def into_wechat(self):
        try:
            self.wait_loading_finish()
            self.click(MenuPageLocator.btn_customer_service)
            self.click(MenuPageLocator.link_wechat)
        except:
            print('微信已停止使用')
            pass

    def into_qq(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.btn_customer_service)
        self.click(MenuPageLocator.link_qq)

    def into_live_chat(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.btn_customer_service)
        self.click(MenuPageLocator.live_chat)

    def get_balance_wallet(self):
        wallet = round(float(re.sub("[^0-9.]", "", (self.get_text(MenuPageLocator.menu_member_balance_wallet)))), 2)
        return wallet

    def into_menu_game(self):
        self.wait_loading_finish()
        self.close_ad_and_click(MenuPageLocator.chess_btn)
        self.wait_loading_finish()

    def into_menu_electronic(self):
        self.wait_loading_finish()
        self.close_ad_and_click(MenuPageLocator.electronic_btn)
        self.wait_loading_finish()

    def into_menu_fish(self):
        self.wait_loading_finish()
        self.close_ad_and_click(MenuPageLocator.fish_btn)
        self.wait_loading_finish()

    def into_menu_sport(self):
        self.wait_loading_finish()
        self.close_ad_and_click(MenuPageLocator.sport_btn)
        self.wait_loading_finish()

    def into_menu_casino(self):
        self.wait_loading_finish()
        self.close_ad_and_click(MenuPageLocator.casino_btn)
        self.wait_loading_finish()

    def into_chatroom(self):
        self.wait_loading_finish()
        self.click(MenuPageLocator.chatroom_btn)
        self.wait_loading_finish()

    def close_ad_and_click(self,Btn):
        try:
            self.click(MenuPageLocator.close_ad_btn)
        except:
            pass
        
        self.sleep(2)
        
        try:
            self.click(Btn)
        except:
            self.scroll_to_bottom()
            self.click(Btn)
