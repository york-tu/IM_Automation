from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime


class LotteryPageLocator:
    # LOTTERY GAME LINK (各彩種選擇頁)
    hk_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                         "//*[@class='lottery1-hk' or @class='lottery2-hk' or contains(@data-bind,'/hk')]")  # 香港六合彩
                         
    jsssc_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                            "//*[@class='lottery1-jsssc' or @class='lottery2-jsssc' or contains(@data-bind,'/jsssc')]")  # 極速拾拾彩
    js6_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                          "//*[@class='lottery1-js6' or @class='lottery2-js6' or contains(@data-bind,'/js6')]")  # 極速六合彩
    jspk10_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                             "//*[@class='lottery1-jspk10' or @class='lottery2-jspk10' or contains(@data-bind,'/jspk10')]")  # 極速PK拾
    pcegg_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                            "//*[@class='lottery1-fcxy28' or @class='lottery2-fcxy28' or contains(@data-bind,'/fcxy28')]")  # PC蛋蛋
    jisu11to5_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                            "//*[@class='lottery1-jisu11x5' or @class='lottery2-jisu11x5' or contains(@data-bind,'/jisu11x5')]")  # 極速11选5
    js3_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                          "//*[@class='lottery1-jisuk3' or @class='lottery2-jisuk3' or contains(@data-bind,'/jisuk3')]")  # 极速快3
    fu3d_link = (By.XPATH, "//div[contains(@class,'lottery_1') or contains(@class,'lottery_2') or contains(@class,'lottery-01')]"
                           "//*[@class='lottery2-fc3d' or @class='lottery1-fc3d' or contains(@data-bind,'/fc3d')]")  # 福彩3D
    sf6_link = (By.XPATH, '//div[contains(@class, "lottery_1") or contains(@class, "lottery_2") or contains(@class, "lottery-01")]'
                            '//*[@class="lottery2-sf6" or @class="lottery1-sf6" or contains(@data-bind, "/sf6")]')  # 三分六合彩
    
    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")
    # 封盤中
    closing = (By.XPATH, "//span[contains(text(), '封盘中')]")
    loading = (By.XPATH, "//div[@id='jqueryEasyOverlayDiv' and (@style!='z-index: 99999; display: none;')]")

class LotteryPage(BasePage):
    time = datetime.datetime.now()
    today = datetime.date.today()

    # 香港六合彩
    def into_hk(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.hk_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # 三分六合彩
    def into_sf6(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.sf6_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # 極速時時彩
    def into_jsssc(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.jsssc_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # 極速六合彩
    def into_js6(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.js6_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # 極速PK10
    def into_jspk10(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.jspk10_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # PC蛋蛋
    def into_pcegg(self, is_maintenance = False):
        self.wait_loading_finish()

        start = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=9, minute=5, second=0)
        stop = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=23, minute=55, second=0)

        if self.time < start or self.time > stop:
            self.test_skip('遊戲關閉中，開啟時間: 9:05-23:55')

        self.open_wait_new_window(LotteryPageLocator.pcegg_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)
    
    # 極速11选5
    def into_jisu11to5(self, is_maintenance = False):
        self.wait_loading_finish()

        start = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=9, minute=30, second=0)
        stop = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=23, minute=10, second=0)

        if self.time < start or self.time > stop:
            self.test_skip('遊戲關閉中，開啟時間: 9:30-23:10')

        self.open_wait_new_window(LotteryPageLocator.jisu11to5_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)


    # 極速快3
    def into_jisuk3(self, is_maintenance = False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.js3_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)

    # 福彩3D
    def into_fu3d(self,is_maintenance=False):
        self.wait_loading_finish()
        self.open_wait_new_window(LotteryPageLocator.fu3d_link)
        self.check_loading()
        self._check_maintenance(is_maintenance)
        
    # 測試維護
    def _check_maintenance(self, is_maintenance = False):
        if is_maintenance is True:
            assert self.is_element_finded(LotteryPageLocator.maintenance) is True, "後台已關閉, 前台不應該顯示此遊戲"
            return
            
        if self.is_element_finded(LotteryPageLocator.maintenance) is True:
            self.test_skip('系統維護中')

        # if self.is_element_displayed(LotteryPageLocator.closing) is True:
        #     raise EOFError('不正常封盤中')

    def check_loading(self):
        for _ in range(0, 2):
            try:
                assert self.is_element_finded(LotteryPageLocator.loading) is False
                return
            except:
                self.sleep(5)
                self.refresh_browser()
                pass

    def into_my_order(self):
        self.wait_loading_finish()
        self.sleep(1)
        self.click((By.XPATH, "//a[contains(@id, 'nzc-nav-order')]"))