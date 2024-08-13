from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException
import datetime
import sys


class ChessPageLocator:
    ky_game = (By.XPATH, "//span[text()='开元棋牌']") # KY棋牌
    search_bar = (By.XPATH, "//div[@class='search-dzyy' or @class='search' or @class='lottery_main']//following::input") # 搜尋輸入欄位
    search_btn = (By.XPATH, "//*[contains(@data-bind,'search')]") # 搜尋按鈕
    game_menu = (By.XPATH, "//div[@class='game-list' or @class='col-5 ky_qipai']") # 遊戲顯示
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]") # 維護監測
    transfer_pop = (By.XPATH, "//div[@class='popup']") # 額度轉換框
    pop_title = (By.XPATH, "//p[@class='header-title' and text()='额度转换']") # 額度轉換框標題
    into_game = (By.XPATH,"//button[@data-bind='click: playGame']")
    pop_closed = (By.XPATH, "//div[@class='dialog__close__img']") # 關閉額度轉換框
    game = (By.XPATH, "(//img[@data-bind='attr:{src: imgreSrc}'])[2]") # 列表第一個遊戲
    wallet = (By.XPATH, "//select[@class='amount-select amount-select--disabled']/option") # KY - ￥4.40

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
                assert self.is_element_finded(ChessPageLocator.into_game) is True, "後台已開啟,前台應該顯示此遊戲"
            
            self.sleep(5)
            self.refresh_browser()

    def check_transferstatus(self, setting=0):
        self.wait_loading_finish()
        self.click(ChessPageLocator.ky_game)
        wallet = '0'
        try:
            if self.is_element_finded(ChessPageLocator.transfer_pop):
                self.click(ChessPageLocator.game)
                self.wait_loading_finish()
                if setting == 0:
                    assert self.is_element_finded(ChessPageLocator.pop_title) is True, f'未顯示額度轉換彈窗'
                    wallet_text = self.get_text(ChessPageLocator.wallet).replace(',','')
                    wallet = wallet_text[wallet_text.find('￥')+1:]
                    self.wait_click_able_click(ChessPageLocator.pop_closed)

                elif setting == 1:  
                    self.open_new_window(ChessPageLocator.game) #第三方遊戲，開新視窗
                
        except UnexpectedAlertPresentException as e:
                # print("Unexpected error(未知錯誤)", sys.exc_info()[0])
                print("KY_GAME未知警告彈出: ", str(e))
                self.accept_alert()
                self.switch_home_page()
        except:
            print("Unexpected error(未知錯誤)", sys.exc_info()[0])
            self.accept_alert()
            self.switch_home_page()
        finally:
            self.switch_home_page()
        
        return float(wallet)
