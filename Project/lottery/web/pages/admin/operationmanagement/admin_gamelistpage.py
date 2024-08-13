from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class GameListLocator:

    # 遊戲名稱
    game_name_input_box = (By.XPATH, '//input[contains(@data-bind, "value: filter.name")]')

    # ----------------------- 啟用狀態 -----------------------
    opening_status_all = (By.XPATH, '//input[contains(@data-bind, "status")]/parent::label[contains(., "全部")]')
    opening_status_open = (By.XPATH, '//label[contains(., "已启用")]')
    opening_status_close = (By.XPATH, '//label[contains(., "已禁用")]')

    # ----------------------- 推薦狀態 -----------------------
    recommendation_status_all = (By.XPATH, '//input[contains(@data-bind, "recommend")]/parent::label[contains(., "全部")]')
    recommendation_status_recommended = (By.XPATH, '//label[contains(., "已推荐")]')
    recommendation_status_not_recommended = (By.XPATH, '//label[contains(., "未推荐")]')

    search_button = (By.ID, 'btnSearch')

    # 遊戲名稱
    game_name_text = (By.XPATH, '//td[contains(@data-bind, "text: name")]')

    # 是否啟用的勾勾
    opening_open = (By.XPATH, '//span[contains(@data-bind, "status") and contains(@style, "display: none;")]')
    opening_close = (By.XPATH, '//span[contains(@data-bind, "status") and not(contains(@style, "display: none;")) and contains(text(), "-")]')

    # 是否推薦的讚
    recommendation_recommended = (By.XPATH, '//span[contains(@data-bind, "recommend") and contains(@style, "display: none;")]')
    recommendation_not_recommended = (By.XPATH, '//span[contains(@data-bind, "recommend") and not(contains(@style, "display: none;")) and contains(text(), "-")]')

    # AG
    game_list_ag = (By.XPATH, "//h3[contains(text(), 'AG')]")
    popup_ag = (By.XPATH, "//h4[contains(text(), 'AG')]")
    game_list_ag_electronics = (By.XPATH, "//a[@class='btn btn-default btn-sm' and text()='AG-电子']")
    ok_game_list_ag_electronics = (By.XPATH, "//span[contains(@data-bind, 'channelname') and text()='AG-电子']/../..//*[text()='游戏列表']")

class GameList(BasePage):

    def get_text_list(self, dom_list):
        return [self.get_text_by_dom(dom) for dom in dom_list]

    def search_game_name(self, name):
        self.wait_loading_finish()

        self.type(GameListLocator.game_name_input_box, name)
        self.click(GameListLocator.search_button)

    def check_game_name(self):        
        self.refresh_browser()
        self.wait_loading_finish()

        max_range = 3
        game_name_for_search = self.get_text_list(self.find_elements(GameListLocator.game_name_text))
        
        for index, game_name in enumerate(game_name_for_search):
            # 最多搜尋三次，否則太浪費時間
            if index >= max_range:
                break

            self.refresh_browser()
            self.wait_loading_finish()

            self.search_game_name(game_name)
            self.wait_loading_finish()
            searched_game_name = self.get_text_list(self.find_elements(GameListLocator.game_name_text))

            assert searched_game_name.__contains__(game_name), f'外接平台 -> 遊戲列表  搜尋遊戲名稱異常 {searched_game_name} 應為-> {game_name}'

    def check_game_opening(self, opening_status):
        self.wait_loading_finish()

        self.click(opening_status)
        self.click(GameListLocator.search_button)
        self.wait_loading_finish()

        if self.get_text(opening_status).__contains__('已启用'):
            assert not self.is_element_finded(GameListLocator.opening_close), f'遊戲列表 查找啟用狀態 為 已启用，查找結果有誤'
        else:
            assert not self.is_element_finded(GameListLocator.opening_open), f'遊戲列表 查找啟用狀態 為 已禁用，查找結果有誤'

    def check_all_opening_status(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.check_game_opening(GameListLocator.opening_status_open)
        
        self.refresh_browser()
        self.wait_loading_finish()
        self.check_game_opening(GameListLocator.opening_status_close)

    def check_game_recommend(self, recommendation_status):
        self.wait_loading_finish()

        self.click(recommendation_status)
        self.click(GameListLocator.search_button)
        self.wait_loading_finish()

        if self.get_text(recommendation_status).__contains__('已推荐'):
            assert not self.is_element_finded(GameListLocator.recommendation_not_recommended), f'遊戲列表 查找推薦狀態 為 已推荐，查找結果有誤'
        else:
            assert not self.is_element_finded(GameListLocator.recommendation_recommended), f'遊戲列表 查找推薦狀態 為 未推荐，查找結果有誤'

    def check_all_recommendation_status(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.check_game_recommend(GameListLocator.recommendation_status_recommended)
        
        self.refresh_browser()
        self.wait_loading_finish()
        self.check_game_recommend(GameListLocator.recommendation_status_not_recommended)

    def into_game_list_ag_electronics(self):
        self.wait_visibility(GameListLocator.game_list_ag)
        self.click(GameListLocator.game_list_ag)
        self.wait_loading_finish()
        assert self.is_element_finded(GameListLocator.popup_ag), f'點擊第三方，未顯示該第三方遊戲類別popup'

        self.click(GameListLocator.game_list_ag_electronics)
        self.wait_loading_finish()
        assert self.is_element_finded(GameListLocator.ok_game_list_ag_electronics), f'未成功進入外接平台_遊戲列表'