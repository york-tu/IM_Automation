from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class ElectronicPageLocator:
    lgd_game = (By.XPATH, "//span[text()='LGD电子']") # LGD電子
    search_bar = (By.XPATH, "//div[@class='search-dzyy' or @class='search' or @class='lottery_main']//following::input") # 搜尋輸入欄位
    search_btn = (By.XPATH, "//*[contains(@data-bind,'search')]") # 搜尋按鈕    
    game_menu = (By.XPATH, "//div[@class='game-list' or @class='col-5 dt_game']") # 遊戲顯示
    into_game = (By.XPATH,"//div[text()='进入游戏']")
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]") # 維護監測


class ElectronicPage(BasePage):
    def maintenance_check(self,is_maintenance):
        self.wait_loading_finish()
        self.click(ElectronicPageLocator.lgd_game)

        for loop in range(0, 20):
            self.wait_loading_finish()
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

        



