from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class ElectronicPageLocator:
    lgd_game = (By.XPATH, "//*[@alt='LGD电子' or text()='LGD电子']/..//img") # LGD電子
    search_bar = (By.XPATH, "//li[@class='search_games']/input") # 搜尋輸入欄位
    search_btn = (By.XPATH, "//*[contains(@data-bind,'search')]") # 搜尋按鈕
    game_menu = (By.XPATH, "//div[@class='game_item_img' or @class='list-item']") # 遊戲顯示
    into_game = (By.XPATH,"//div[@style='' or @class='dialog-mask']//*[contains(text(),'进入游戏')]")
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中') or (@aria-labelledby='游戏例行维护中' and not(contains(@style,'display: none;')))]") # 維護監測


class ElectronicPage(BasePage):
    def maintenance_check(self,is_maintenance):
        self.wait_loading_finish()
        self.scroll_to_element(ElectronicPageLocator.lgd_game)
        self.click(ElectronicPageLocator.lgd_game)

        for loop in range(0, 20):
            self.wait_loading_finish()
            if self.is_element_finded(ElectronicPageLocator.maintenance) is False:
                self.click(ElectronicPageLocator.game_menu)
            self.wait_loading_finish()
            self.sleep(3)
            
            if is_maintenance == True:

                if self.is_element_finded(ElectronicPageLocator.maintenance) is True or loop == 19:
                    assert self.is_element_finded(ElectronicPageLocator.maintenance) is True, "後台已關閉,前台不應該顯示此遊戲"
                    return
                    
            else:
                assert self.is_element_finded(ElectronicPageLocator.into_game) is True, "後台已開啟,前台應該顯示此遊戲"
            
            self.sleep(5)
            self.refresh_browser()