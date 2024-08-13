from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sikuli.sikuliX import Sikuli
from selenium import webdriver
from common.utils_folder import common.utils
import time
import traceback


class Scripts:
    chrome_path = utils.get_web_driver()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--window-size=1920,1000')
    # chrome_options.add_argument('--no-sandbox')
    prefs = {'profile.default_content_setting_values.plugins': 1,
             'profile.content_settings.plugin_whitelist.adobe-flash-player': 1,
             'profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player': 1}
    chrome_options.add_experimental_option('prefs', prefs)

    base_url = "http://lv-web-uat.paradise-soft.com.tw/"
    loginaccount = 'cmtest003'
    loginpassword ='Heaven@4394'

    s = Sikuli()
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_path)
    wait = WebDriverWait(driver, 20)
    a = ActionChains(driver)

    def web_login(self, driver, account, password, captcha):
        wait = WebDriverWait(driver, 20)
        driver.find_element(By.ID, "nzc-header-account").send_keys(account)
        driver.find_element(By.ID, "nzc-header-password").send_keys(password)
        driver.find_element(By.ID, "nzc-header-captcha").send_keys(captcha)
        driver.find_element(By.ID, "nzc-header-login").send_keys(Keys.ENTER)
        wait.until(EC.invisibility_of_element_located((By.ID, "main-loading-mask")))

    def web_choice_egame(self, driver, gamebrand, gamename):
        wait = WebDriverWait(driver, 20)
        driver.find_element(By.ID, "nzc-nav-game").click()
        driver.find_element(By.XPATH, "//li[contains(@data-bind,'"+gamebrand+"')]").click()
        wait.until(EC.invisibility_of_element_located((By.ID, "main-loading-mask")))
        driver.find_element(By.XPATH, "//div[@class='search-dzyy']/input").send_keys(gamename)
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@class='search-dzyy']/input").send_keys(Keys.ENTER)
        wait.until(EC.invisibility_of_element_located((By.XPATH, "id('main-loading-mask')/div")))
        time.sleep(1)

    def web_enter_egame(self, driver, s, LOGO, LOADING_FINISH):
        wait = WebDriverWait(driver, 20)
        window_count = driver.window_handles
        s.click_(LOGO)
        wait.until(EC.new_window_is_opened(window_count))
        driver.switch_to.window(driver.window_handles[1])
        print("開啟遊戲")

        maxtries = 0
        while maxtries <= 3:
            try:
                s.wait_(LOADING_FINISH, 50)
                break
            except Exception as e:
                print('等待超時')
                driver.refresh()
                maxtries += 1
                if maxtries == 3:
                    raise e
        print("進入遊戲")

    def ag_egame_fruitslot(self):
        from sikuli.imgs.egame.ag_fruitslot import fruitslot
        s = self.s
        wait = self.wait
        driver = self.driver
        driver.maximize_window()

        try:
            driver.get(self.base_url)
            driver.get(self.base_url)

            self.web_login(driver, self.loginaccount, self.loginpassword, 1)
            self.web_choice_egame(driver, 'ag_game', '水果拉霸')
            #
            # s.click_(fruitslot.LOGO)
            # wait.until(EC.new_window_is_opened(driver.window_handles))
            # driver.switch_to.window(driver.window_handles[1])
            # print("開啟遊戲")
            #
            # maxtries = 0
            # while maxtries <= 3:
            #     try:
            #         s.wait_(fruitslot.LOADING_FINISH, 50)
            #         break
            #     except Exception as e:
            #         print('等待超時')
            #         driver.refresh()
            #         maxtries += 1
            #         if maxtries == 3:
            #             raise e
            # print("進入遊戲")
            self.web_enter_egame(driver, s, fruitslot.LOGO, fruitslot.LOADING_FINISH)

            s.click_(fruitslot.BETTING_BUTTON)
            print("下注")

            s.click_(fruitslot.START_BUTTON)
            print("開始")
            time.sleep(10)

            driver.close()
            print("關閉遊戲")

        finally:
            driver.quit()
            s.closeGateway()

    def mg_egame_coolbuck(self):
        from sikuli.imgs.egame.mg_coolbuck import coolbuck
        s = self.s
        wait = self.wait
        driver = self.driver
        driver.maximize_window()

        try:
            driver.get(self.base_url)
            driver.get(self.base_url)

            self.web_login(driver, self.loginaccount, self.loginpassword, 1)
            self.web_choice_egame(driver, 'mg_game', '运财酷儿-5卷轴')
            #
            # s.click_(coolbuck.LOGO)
            # wait.until(EC.new_window_is_opened(driver.window_handles))
            # driver.switch_to.window(driver.window_handles[1])
            # print("開啟遊戲")
            #
            # maxtries = 0
            # while maxtries <= 3:
            #     try:
            #         s.wait_(coolbuck.LOADING_FINISH, 50)
            #         break
            #     except Exception as e:
            #         print('等待超時')
            #         driver.refresh()
            #         maxtries += 1
            #         if maxtries == 3:
            #             raise e
            # print("進入遊戲")
            self.web_enter_egame(driver, s, coolbuck.LOGO, coolbuck.LOADING_FINISH)

            result = s.waitVanish_(coolbuck.LESS_BETTING, 0, similarily=0.99)
            while result is False:
                print("非最小注額，減注中")
                s.click_(coolbuck.LESS_BETTING, similarily=0.99)
                result = s.waitVanish_(coolbuck.LESS_BETTING, 0, similarily=0.99)

            s.click_(coolbuck.START_BUTTON)
            print("開始")

            driver.close()
            print("關閉遊戲")
        finally:
            driver.quit()
            s.closeGateway()

    def dt_egame_gundam(self):
        from sikuli.imgs.egame.dt_gundam import gundam
        s = self.s
        wait = self.wait
        driver = self.driver
        driver.maximize_window()

        try:
            driver.get(self.base_url)
            driver.get(self.base_url)

            self.web_login(driver, self.loginaccount, self.loginpassword, 1)
            self.web_choice_egame(driver, 'dt_game', '高达')
            self.web_enter_egame(driver, s, gundam.LOGO, gundam.LOADING_FINISH)

            result = s.waitVanish_(gundam.LESSEST_BET, 0, similarily=0.80)
            while result is True:
                print("非最小注額，減注中")
                try:
                    s.click_(gundam.LESS_BET_BUTTON, 0.90, -340, -15)  # 減注
                    s.click_(gundam.LESS_BET_BUTTON_01, 0.90, -600, -15)  # 減線
                    result = s.waitVanish_(gundam.LESSEST_BET, 0, similarily=0.80)
                except Exception as e:
                    traceback.print_tb(e.__traceback__)
                    continue
            print("已達最小注額")

            s.click_(gundam.START_BUTTON)
            print("開始")
            time.sleep(5)

            driver.close()
            print("關閉遊戲")
        finally:
            driver.quit()
            s.closeGateway()

    def bbin_egame_chuantong(self):
        from sikuli.imgs.egame.bbin_chuantong import chuantong
        s = self.s
        wait = self.wait
        driver = self.driver
        driver.maximize_window()

        try:
            driver.get(self.base_url)
            driver.get(self.base_url)

            self.web_login(driver, self.loginaccount, self.loginpassword, 1)
            self.web_choice_egame(driver, 'bbin_game', '传统')
            self.web_enter_egame(driver, s, chuantong.LOGO, chuantong.LOADING_FINISH)

            s.click_(chuantong.SETP1)
            s.click_(chuantong.SETP2, 0.99)
            s.click_(chuantong.SETP3, 0.60)
            s.click_(chuantong.SETP4, 0.60)
            s.click_(chuantong.SETP5, 0.99)
            s.click_(chuantong.SETP6, 0.99)

            s.click_(chuantong.START_BUTTON, 0.99)
            print("開始")
            time.sleep(5)

            driver.close()
            print("關閉遊戲")
        finally:
            driver.quit()
            s.closeGateway()

    def sb_egame_roulettepro(self):
        from sikuli.imgs.egame.sb_roulettepro import roulettepro
        s = self.s
        a = self.a
        wait = self.wait
        driver = self.driver
        driver.maximize_window()

        try:
            driver.get(self.base_url)
            driver.get(self.base_url)

            self.web_login(driver, self.loginaccount, self.loginpassword, 1)
            driver.get(self.base_url+'games/sb_game')
            wait.until(EC.presence_of_element_located((By.XPATH, "id('main-loading-mask')[contains(@style,'none')]")))
            window_count = driver.window_handles
            driver.find_element(By.XPATH, "//div[@class='game-item sb_game']").click()
            wait.until(EC.new_window_is_opened(window_count))
            window_count = driver.window_handles
            driver.switch_to.window(driver.window_handles[-1])
            print('開啟SB大廳')

            driver.maximize_window()
            s.wait_(roulettepro.LOGO, 50)
            s.click_(roulettepro.LOGO)
            # wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "id('frmGame')")))
            # driver.switch_to.frame('frmGame')
            # wait.until(EC.element_to_be_clickable((By.ID, 'GLR0010')))
            # driver.find_element(By.ID, 'GLR0010').click()
            wait.until(EC.new_window_is_opened(window_count))
            driver.switch_to.window(driver.window_handles[-1])
            print('開啟遊戲')

            s.wait_(roulettepro.LOADING_FINISH, 50)
            print('進入遊戲')

            s.click_(roulettepro.BETTING, 0.99)
            s.click_(roulettepro.START_BUTTON, 0.99)
            print('開始')
            time.sleep(6)

            driver.close()
            print("關閉遊戲")

            driver.close()
            print('關閉大廳')

        finally:
            driver.quit()
            s.closeGateway()

if __name__ == "__main__":
    Scripts().sb_egame_roulettepro()
