from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class GameManagementPageLocator:
    # 查找條件
    game_search = (By.XPATH,"//input[contains(@data-bind,'filter.name')]") # 遊戲名稱搜尋
    channel_search = (By.XPATH,"//div[@class='select2-container form-control select2me']") # 頻道名稱搜尋
    channel_input = (By.XPATH,"//div[@class='select2-search']//input[@id='s2id_autogen2_search']") # 頻道打字欄位
    btn_search = (By.XPATH,"//button[@id='btnSearch']") # 查找
    radio_on  = (By.XPATH,"//label[text()='推荐状态']/preceding-sibling::div//input[@value='1'] ") # 開啟
    radio_off = (By.XPATH,"//label[text()='推荐状态']/preceding-sibling::div//input[@value='0'] ") # 關閉

    # 列表
    status_radio = (By.XPATH,"//th//input[contains(@data-bind,'statusChecked')]") # 啟用開關
    save_all = (By.XPATH,"//button[contains(@data-bind,'updateAllProduct')]") # 全部保存
    success_message = (By.XPATH,"//div[@class='toast-message']") # 修改成功
    game_lists = (By.XPATH,"//tbody[@data-bind='foreach: items']/tr") # 遊戲列表
    game_names = (By.XPATH,"//tbody[@data-bind='foreach: items']/tr/td[2]") # 遊戲名稱

class GameManagementPage(BasePage):
    
    # 關閉遊戲至維護狀態
    def game_status_close(self, game_list, is_maintenance):
        for name in game_list:

            if name == "GC-视讯":
                self.refresh_browser()
                self.wait_loading_finish()
                self.click(GameManagementPageLocator.channel_search)
                self.type(GameManagementPageLocator.channel_input, name)
                self.type_enter(GameManagementPageLocator.channel_input)

            else:
                self.type(GameManagementPageLocator.game_search, name)
            
            self.sleep(1)

            if is_maintenance == True:
                self.click(GameManagementPageLocator.radio_on)
            else:
                self.click(GameManagementPageLocator.radio_off)

            self.click(GameManagementPageLocator.btn_search)
            self.wait_loading_finish()
            self.click(GameManagementPageLocator.status_radio)
            self.sleep(1)
            self.click(GameManagementPageLocator.save_all)
            
            message = self.get_text(GameManagementPageLocator.success_message)
            assert message == '修改成功', '保存異常 狀態: {0}'.format(message)

            self.sleep(5)

    # 檢查遊戲下架
    def game_status_check(self, third_channel, game_type, game_list):
        admin_name_list = []
        # 改寫頻道格式
        if third_channel == 'KX':
            channel_name = third_channel + game_type
        elif third_channel == 'BS':
            channel_name = '百胜' + game_type
        elif third_channel == 'KY':
             channel_name = '开元' + game_type
        else:
            channel_name = third_channel + '-' + game_type
        # 查找遊戲
        for name in game_list:
            self.type(GameManagementPageLocator.game_search, name)
            self.sleep(1)
            self.click(GameManagementPageLocator.btn_search)
            self.wait_loading_finish()
            if self.is_element_finded(GameManagementPageLocator.game_lists) == False:
                pass
            else:
                self.click(GameManagementPageLocator.channel_search)
                self.type(GameManagementPageLocator.channel_input, channel_name)
                self.type_enter(GameManagementPageLocator.channel_input)
                self.sleep(1)
                self.click(GameManagementPageLocator.btn_search)
                self.wait_loading_finish()
                if self.is_element_finded(GameManagementPageLocator.game_lists) == False:
                    pass
                else:
                    games = self.find_elements(GameManagementPageLocator.game_names)
                    for game in games:
                        if len(game.text) == len(name):
                            admin_name_list.append(name)
        return list(set(admin_name_list))
        # assert name_list == [], f"{name_list} 遊戲未下架"

    # 檢查遊戲上架
    def game_add_status_check(self, third_channel, game_type, game_list):
        admin_name_list = []
        # 改寫頻道格式
        if third_channel == 'KX':
            channel_name = third_channel + game_type
        elif third_channel == 'BS':
            channel_name = '百胜' + game_type
        elif third_channel == 'KY':
             channel_name = '开元' + game_type
        else:
            channel_name = third_channel + '-' + game_type
        # 查找遊戲
        for name in game_list:
            self.wait_loading_finish()
            self.type(GameManagementPageLocator.game_search, name)
            self.click(GameManagementPageLocator.channel_search)
            self.type(GameManagementPageLocator.channel_input, channel_name)
            self.type_enter(GameManagementPageLocator.channel_input)
            self.sleep(1)
            self.click(GameManagementPageLocator.btn_search)
            self.wait_loading_finish()
            self.sleep(1)
            # 驗證遊戲是否啟用
            if self.is_element_finded(GameManagementPageLocator.game_lists) == False:
                admin_name_list.append(name)
            else:
                game_names = self.find_elements(GameManagementPageLocator.game_names)
                games = [game.text for game in game_names if game.text == name]
                if len(games) == 1:
                    self.click(GameManagementPageLocator.radio_on)
                    self.click(GameManagementPageLocator.btn_search)
                    self.wait_loading_finish()
                    self.sleep(1)
                    enable_game_names = self.find_elements(GameManagementPageLocator.game_names)
                    enable_games = [enable_game.text for enable_game in enable_game_names if enable_game.text == name]
                    if name not in enable_games:
                        admin_name_list.append(name)
                    enable_games = []
                else:
                    admin_name_list.append(name)
                games = []
            # 關閉遊戲以測維護
            if name not in admin_name_list:
                self.click(GameManagementPageLocator.radio_on)
                self.click(GameManagementPageLocator.btn_search)
                self.wait_loading_finish()
                self.click(GameManagementPageLocator.status_radio)
                self.sleep(1)
                self.click(GameManagementPageLocator.save_all)
            self.refresh_browser()
        return list(set(admin_name_list))
    
    # 恢復啟用遊戲
    def game_enable(self, game_list, admin_name_list):
        for name in game_list:
            if name not in admin_name_list:
                self.type(GameManagementPageLocator.game_search, name)
                self.click(GameManagementPageLocator.radio_off)
                self.click(GameManagementPageLocator.btn_search)
                self.wait_loading_finish()
                self.sleep(1)
                self.click(GameManagementPageLocator.status_radio)
                self.sleep(1)
                self.click(GameManagementPageLocator.save_all)
                self.wait_loading_finish()
                
