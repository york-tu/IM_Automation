from selenium.webdriver.common.by import By
from common.web.common import Common

class BasePageLocator:
    # ALL PAGE
    loading_mask = (By.XPATH,"//span[contains(text(),'Load') or contains(text(),'加载中') or @id='jqueryEasyOverlayDiv' or @id='icon-loading']")
    login_billboard_btn = (By.XPATH, "//*[@class='bulletin-close__img' or @class='btn-billboard' and text()[contains(., '我知道了')]]")  # 登入公告確定鈕 
    login_billboard_nwap = (By.XPATH, "//a[@class='bulletin-close']")
    login_chagnepwd_btn = (By.XPATH, "//a[contains(text(),'暂不修改')]")  # 更換密碼彈窗按鈕
    
    mail_dialog_lay = (By.XPATH, "//button[text()='稍后阅读']")
    # 第三方遊戲搜尋
    search_bar = (By.XPATH, "//li[@class='search_games']/input") # 搜尋輸入欄位
    search_btn = (By.XPATH, "//*[contains(@data-bind,'search')]") # 搜尋按鈕
    game_be_search = (By.XPATH, "//div[@data-bind='text: name']") # 搜尋到遊戲

    # 額度轉換框
    loading_text = (By.XPATH, "//span[text()='Loading...']") # 讀取中
    transfer_input = (By.XPATH, "//input[@class='money-frame__input']") # 輸入金額
    transfer_submit = (By.XPATH, "//a[@class='money-submit']") # 確定轉入
    input_text = (By.XPATH, "//span[text()='请输入存款金额']") # 請輸入金額訊息
    success_text = (By.XPATH, "//span[@class='success-message__text' and contains(text(),'额度转换已成功')]") # 轉換成功訊息
    wallet_from = (By.XPATH, "//select[@class='amount-select']") # 轉出錢包
    wallet_to = (By.XPATH, "//select[@class='amount-select amount-select--disabled']/option[@selected='selected']") # 轉入錢包
    wallet_refresh = (By.XPATH, "//a[@class='refresh']") # 刷新餘額
    enter_game = (By.XPATH, "//a[text()='进入游戏']") # 進入遊戲
    
    # 遊戲維護頁
    maintain_to_home = (By.XPATH, "//a[text()='返回首页']") # 返回首页
class BasePage(Common):
    def wait_loading_finish(self):
        self.sleep(1)

        if self.is_element_finded(BasePageLocator.loading_mask) is True :
            try:
                self.wait_invisibility(BasePageLocator.loading_mask)
            except:
                raise Exception("讀取時間過長, 請確認讀取屏蔽視窗")

    # 關閉天天麻將登入公告
    def nwap_close_login_board(self):
        
        for _ in range(3):
            while True:

                if self.is_element_finded(BasePageLocator.login_billboard_nwap) is True :
                    self.click(BasePageLocator.login_billboard_nwap)
                else:
                    break
                
            self.sleep(0.5)
    
    # 關閉登入公告
    def close_login_board(self):
        for _ in range(3):
            while True:
                
                if self.is_element_displayed(BasePageLocator.login_billboard_btn) is True:
                    self.click(BasePageLocator.login_billboard_btn)
                else:
                    break
                    
            self.sleep(0.5)
    
    # 關閉站內信公告
    def close_message_dialog(self):
        for _ in range(3):
            while True:
                
                if self.is_element_displayed(BasePageLocator.mail_dialog_lay) is True:
                    self.click(BasePageLocator.mail_dialog_lay)
                else:
                    break
                    # 
            self.sleep(0.5)

    # 關閉更換密碼彈窗
    def close_change_pwd(self):        
        for _ in range(3):
            while True:
                
                if self.is_element_displayed(BasePageLocator.login_chagnepwd_btn) is True:
                    self.click(BasePageLocator.login_chagnepwd_btn)
                else:
                    break
                    
            self.sleep(0.5)

    # 處理遊戲列表參數
    def game_list_preprocessing(self, game_list):
        channel_game = game_list.split(',')
        channel_game = [game.strip() for game in channel_game]
        third_channel = channel_game[0]
        game_type = channel_game[1]
        game_code = channel_game[2::2]
        game_list = channel_game[3::2]
        return third_channel, game_type, game_code, game_list

    # 整理頻道定位
    def channel_locate(self, third_channel, game_type):
        if third_channel == 'SB':
            third_channel = '沙巴'
        elif third_channel == 'KY':
            third_channel = '开元'
        elif third_channel == 'BS':
            third_channel = '百胜'
        electronic_game = (By.XPATH, f"//img[@alt='{third_channel + game_type}']") 
        chess_game = (By.XPATH, f"(//img[@alt='{third_channel + game_type}'])[1]") 
        if game_type == '电子':
            self.click(electronic_game)
        elif game_type == '棋牌':
            self.click(chess_game)
        return electronic_game, chess_game

    # 檢查遊戲下架
    def game_remove_check(self, third_channel, game_type, game_list):
        self.wait_loading_finish()
        wap_name_list = []
        for name in game_list:
            self.type(BasePageLocator.search_bar, name)
            self.click(BasePageLocator.search_btn)
            try:
                self.wait_alert_present()
                self.accept_alert()
                self.sleep(1)
            except:
                self.wait_loading_finish()
                if self.is_element_finded(BasePageLocator.game_be_search) == True:
                    games_be_search = self.find_elements(BasePageLocator.game_be_search)
                    games = [game.text for game in games_be_search if game.text != name]
                    if len(games) != len(games_be_search):
                        wap_name_list.append(name)
                    games = []
                    # assert len(games) == len(games_be_search), '遊戲未下架'        
        return list(set(wap_name_list))

    # 檢查遊戲上架
    def game_add_check(self, third_channel, game_type, game_list):
        self.wait_loading_finish()
        wap_name_list = []
        fail_transfer_game = []
        for name in game_list:
            self.type(BasePageLocator.search_bar, name)
            self.click(BasePageLocator.search_btn)
            self.sleep(1)
            try:
                self.wait_loading_finish()
                if self.is_element_finded(BasePageLocator.game_be_search) == True:
                    games_be_search = self.find_elements(BasePageLocator.game_be_search)
                    games = [game for game in games_be_search if game.text == name]
                    if len(games) == 1:
                        for game in games:
                            self.click_by_dom(game)
                            self.sleep(1)
                            if self.is_element_finded(BasePageLocator.maintain_to_home) == True:
                                self.back()
                                self.wait_loading_finish()
                                break
                            fail = self.game_transfer_pop()
                            if fail != None:
                                fail_transfer_game.append(name)
                    else:
                        wap_name_list.append(name)
                    games = []
            except:
                self.wait_alert_present()
                self.accept_alert()
                self.sleep(1)
                wap_name_list.append(name)
        assert fail_transfer_game == [], f'{fail_transfer_game}{fail}'
        return list(set(wap_name_list))

    #測試額度轉換彈窗
    def game_transfer_pop(self):
        self.wait_loading_finish()
        try:
            self.wait_invisibility(BasePageLocator.loading_text)
            self.wait_visibility(BasePageLocator.transfer_input)
        except:
            raise EOFError('額度轉換框未出現')
        money_before = self.find_element(BasePageLocator.wallet_to).text
        money_before = money_before.split('￥')[1]
        self.type(BasePageLocator.transfer_input, 2)
        self.click(BasePageLocator.transfer_submit)
        if self.is_element_finded(BasePageLocator.input_text) == True:  # 若type失敗就再試一次
            self.type(BasePageLocator.transfer_input, 3)
            self.click(BasePageLocator.transfer_submit)
        self.wait_visibility(BasePageLocator.success_text)
        self.wait_visibility(BasePageLocator.transfer_submit)  # 多等待一次確定轉帳結束
        self.click(BasePageLocator.wallet_refresh)
        self.sleep(3)
        self.click(BasePageLocator.wallet_refresh)
        self.sleep(1)
        money_after = self.find_element(BasePageLocator.wallet_to).text
        money_after = money_after.split('￥')[1]
        if float(money_after) - float(money_before) != 2:
            return '額度轉換失敗'
        else:
            self.click(BasePageLocator.enter_game)
            self.sleep(1)
            self.back()
            self.wait_loading_finish()

    #檢查遊戲維護
    def game_maintain_check(self, game_list, admin_name_list):
        maintain_list = []
        for name in game_list:
            if name not in admin_name_list:
                self.type(BasePageLocator.search_bar, name)
                self.click(BasePageLocator.search_btn)
                try:
                    self.wait_loading_finish()
                    if self.is_element_finded(BasePageLocator.game_be_search) == True:
                        games_be_search = self.find_elements(BasePageLocator.game_be_search)
                        for game in games_be_search:
                            if game.text == name:
                                self.click_by_dom(game)
                                self.wait_loading_finish()
                            if self.is_element_finded(BasePageLocator.maintain_to_home) == True:
                                self.back()
                                self.wait_loading_finish()
                                break
                            else:
                                maintain_list.append(name)
                                self.refresh_browser()
                                break
                except:
                    self.wait_alert_present()
                    self.accept_alert()
                    self.sleep(1)
        return maintain_list
    
    # 比對未上下架遊戲
    def compare_game_status(self, web_name_list, admin_name_list, cm_name_list, maintain_list, status=0):
        if status == 0:
            balance = '移除'
        elif status == 1:
            balance = '新增'
        if web_name_list == admin_name_list == cm_name_list:
            assert web_name_list == [], f"wap,admin,cmweb未{balance}遊戲:{web_name_list}"
        else:
            if web_name_list != []:
                if admin_name_list != []:
                    if cm_name_list != []:
                        assert cm_name_list == [], f"\nwap未{balance}遊戲:{web_name_list}\nadmin未{balance}遊戲:{admin_name_list}\ncmweb未{balance}遊戲:{cm_name_list}"
                    else:
                        assert admin_name_list == [], f"\nwap未{balance}遊戲:{web_name_list}\nadmin未{balance}遊戲:{admin_name_list}"
                else:
                    if cm_name_list != []:
                        assert web_name_list == [], f"\nwap未{balance}遊戲:{web_name_list}\ncmweb未{balance}遊戲:{cm_name_list}"
                    else:
                        assert web_name_list == [], f"\nwap未{balance}遊戲:{web_name_list}"
            else:
                if admin_name_list != []:
                    if cm_name_list != []:
                        assert cm_name_list == [], f"\nadmin未{balance}遊戲:{admin_name_list}\ncmweb未{balance}遊戲:{cm_name_list}"
                    else:
                        assert admin_name_list == [], f"\nadmin未{balance}遊戲:{admin_name_list}"
                else:
                    if cm_name_list != []:
                        assert cm_name_list == [], f"\ncmweb未{balance}遊戲:{cm_name_list}"
        assert maintain_list == [], f'{maintain_list}遊戲未進入維護'