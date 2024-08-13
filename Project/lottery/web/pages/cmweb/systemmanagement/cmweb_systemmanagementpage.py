from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage

class SystemManagementPageLocator:
    # ------------系統管理--------------
    menu_system_management = (By.XPATH, "//span[text()='系统管理']/..")

    # *游戏列表
    menu_game_list = (By.XPATH, "//span[text()='游戏列表']")


class SystemManagementPage(BasePage):
    # 系統管理
    def into_system_management(self):
        self.wait_loading_finish()
        for _ in range(2):
            if self.is_element_finded(SystemManagementPageLocator.menu_system_management) is True:
                break
            self.sleep(5)
            
        self.sleep(3)
        self.click(SystemManagementPageLocator.menu_system_management)
        
    # 系統管理 -> 遊戲列表
    def into_menu_game_list(self):
        self.into_system_management()
        self.click(SystemManagementPageLocator.menu_game_list)



