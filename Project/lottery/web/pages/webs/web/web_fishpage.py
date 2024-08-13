from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class FishPageLocator:
    game_menu = (By.XPATH, "//img[@alt='AG捕鱼王']") # 遊戲顯示
    game_menu_2 = (By.XPATH,"(//*[@alt='AG捕鱼王']/following::div[@class='btn'])[1]")
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]") # 維護監測
    into_game = (By.XPATH,"//div[text()='进入游戏']")

class FishPage(BasePage):
    def maintenance_check(self,Game_name,is_maintenance):
        for loop in range(0, 20):
            self.wait_loading_finish()

            try:
                self.click(FishPageLocator.game_menu)
                self.click(FishPageLocator.game_menu_2)
            except:
                pass
                
            self.wait_loading_finish()
            self.sleep(3)
            
            if is_maintenance == True:

                if self.is_element_finded(FishPageLocator.maintenance) is True or loop == 19:
                    assert self.is_element_finded(FishPageLocator.maintenance) is True, "後台已關閉,前台不應該顯示此遊戲"
                    return
                    
            else:
                assert self.is_element_finded(FishPageLocator.into_game) is True, "後台已開啟,前台應該顯示此遊戲"

            self.sleep(5)
            self.refresh_browser()