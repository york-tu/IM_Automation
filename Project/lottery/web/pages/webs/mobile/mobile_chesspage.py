from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class ChessPageLocator:
    ky_game = (By.XPATH, "//*[@alt='开元棋牌']") # KY棋牌
    search_bar = (By.XPATH, "//li[@class='search_games']/input") # 搜尋輸入欄位
    search_btn = (By.XPATH, "//*[contains(@data-bind,'search')]") # 搜尋按鈕
    game_menu = (By.XPATH, "//div[@class='game_item_img']") # 遊戲顯示
    Into_game = (By.XPATH,"//div[text()='进入游戏']")
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]") # 維護監測

class ChessPage(BasePage):
    def maintenance_check(self,is_maintenance):
        self.wait_loading_finish()
        self.click(ChessPageLocator.ky_game)

        for loop in range(0, 20):
            self.wait_loading_finish()
            self.click(ChessPageLocator.game_menu)
            self.wait_loading_finish()
            self.sleep(3)
            
            if is_maintenance == True:

                if self.is_element_finded(ChessPageLocator.maintenance) is True or loop == 19:
                    assert self.is_element_finded(ChessPageLocator.maintenance) is True, "後台已關閉,前台不應該顯示此遊戲"
                    return
            else:
                assert self.is_element_finded(ChessPageLocator.Into_game) is True, "後台已開啟,前台應該顯示此遊戲"
            
            self.sleep(5)
            self.refresh_browser()