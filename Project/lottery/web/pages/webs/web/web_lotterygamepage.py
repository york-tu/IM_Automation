from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import time,datetime,os,platform
from retrying import retry
import random

# add_xpath_or_num = int, 則產單注下注欄位
def bettingXpath(add_xpath_or_num, is_defaultgametype, is_defaultgamerule):
    xpath = ""
    chane_game_type = ""
    chane_game_rule = ""
    if is_defaultgametype is False:
        chane_game_type = " and contains(@style,'block')"  # 若非預設玩法會有此區塊
    if is_defaultgamerule is False:
        chane_game_rule = "//*[contains(@style,'block')]"  # 若非預設規則會有此區塊
    if isinstance(add_xpath_or_num, int):
        num = str(add_xpath_or_num)
        xpath = "(//div[@class='ball_table_room'" + chane_game_type + "]" + chane_game_rule + "//input)[" + num + "]"
    if isinstance(add_xpath_or_num, str):
        xpath = "//div[@class='ball_table_room'" + chane_game_type + "]" + chane_game_rule + "//" + add_xpath_or_num
    result = (By.XPATH, xpath)
    return result

class LotteryGamePageLocator:
    # LOADING
    bet_loading = (By.ID, "betAreaLoading")  # 開盤Loading遮罩
    bet_area_check_point = (By.XPATH, "//div[@class='bettingBox']")  # 等待下注區出現
    bet_sealed_mask = (By.XPATH, "//div[@class='time_out_hk']")

    # MENU (彩票頁面上方連結)
    menu_betting_recording = (By.ID, "nzc-nav-order")  # 投注紀錄
    betting_record_win = (By.XPATH, "(//span[contains(text(),'输赢')]/span)[1]")

    # 開獎區
    current_period = (By.XPATH, "//strong[@class='gameperiod']/span")  # 目前下注中期數
    lastest_period = (By.XPATH, "//span[@class='drawNoticePeriod']")  # 最新已開獎期數

    # BET DIALOG (下注後提示窗)
    bet_dialog = (By.XPATH, "//div[@role='dialog']")  # 下注後提示視窗
    bet_dialog_message = (By.ID, "swal2-title")  # 下注提示窗訊息位置
    bet_dialog_ok_btn = (By.XPATH, "//button[@class='swal2-confirm swal2-styled']")  # 下注後提示視窗確認鈕
    bet_dialog_mask = (By.XPATH, "//div[@class='swal2-container swal2-center swal2-fade swal2-shown']")  # Dialog遮罩


    # =============================== 下注定位 ==============================
    btn_add_order = "*[@class='game_control_subimt']"  # 注單添加鈕
    input_bet_amount = "div[@class='tooltip_group']/input"  # 注額輸入欄

    # BET AREA (彩票下注區)
    list_order = (By.XPATH, "//dl/dd")  # 訂單區內注單
    btn_betting = (By.XPATH, "//a[@class='betting_Btn active']")  # 投注鈕
    btn_ok = (By.XPATH, "//button[text()='OK']")
    # 投注清單
    record_TYPE = (By.XPATH, "//dd//span[1]")
    record_num = (By.XPATH, "//dd//span[2]")
    record_money = (By.XPATH, "//dd//span[4]")

    # 六合彩 (香港六合彩&極速六合彩頁面)
    #   特碼
    input_tema_num1 = bettingXpath(1, True, True)  # 1號球
    odds = (By.XPATH, "(//div[contains(@class,'js_ball new_ball ball_01')]/../..//span)[1]")  #第一格賠率
    btn_add_tema_order = bettingXpath(btn_add_order, True, True)  # 六合彩添加鈕
    #   連肖連尾
    btn_hk_game_lslw = (By.XPATH, "//span[@class='gameMenu-active-tab' and text()='连肖连尾']")  # 切換連肖連尾玩法
    #   二尾碰
    bet_zmlw2_num1 = (By.XPATH, "(//ul[@class='clearfix']//a[@class='js_ball'])[1]")  # 1尾
    bet_zmlw2_num2 = (By.XPATH, "(//ul[@class='clearfix']//a[@class='js_ball'])[2]")  # 2尾
    input_zmlw2_bet_amount = bettingXpath(input_bet_amount, True, True)  # 2尾碰輸入框
    btn_zmlw2_add_order = bettingXpath(btn_add_order, True, True)  # 2尾碰添加鈕

    # 極速時時彩
    #   兩面
    input_lm_num1 = bettingXpath(1, True, True)
    btn_lm_add_order = bettingXpath(btn_add_order, True, True)  # 兩面添加鈕

    # 極速PK10
    #   冠亞和
    byn_choice_game_gyh = (By.XPATH, "//span[@class='gameMenu-active-tab' and text()='冠亚和']")
    input_gyh_num1 = (By.XPATH, "(//div[@class='ball_table_room']//input)[1]")
    btn_gyh_add_order = (By.XPATH, "//div[@class='ball_table_room']//*[@class='game_control_subimt']")

    # PC蛋蛋
    input_egg_num1 = (By.XPATH, "//table[@class='vertical_box']//input")
    btn_egg_add_order = (By.XPATH, "(//input[contains(@value,'添加') ])[1]")

    # 極速11选5
    input_jisu_num1 = (By.XPATH, "//table[@class='vertical_box']//input")
    btn_jisu_order = (By.XPATH, "(//input[contains(@value,'添加') ])[1]")

    # 極速快三
    input_js3_num1 = (By.XPATH, "(//*[@class='ball_table ball_table_v col_1']//input)[1]")
    btn_js3_order = (By.XPATH, "(//input[contains(@value,'添加') ])[1]")
    now_period= (By.XPATH, "//strong[@class='gameperiod']/span[1]")
    now_time = (By.XPATH, "//p[contains(@class, 'betTimer')]//em[3]")
    sj_link = (By.XPATH, "//ul[@class='gameMenu tabs']//*[contains(text(),'三军')]")

    # 福彩3D
    input_fu3d_num1 = (By.XPATH, "(//*[@class='ball_table']//input)[1]")
    btn_fu3d_order = (By.XPATH, "(//input[contains(@value,'添加') ])[1]")

    # 三分六合彩
    button_add_bravery_tow_zodiac_sign_sf6 = (By.XPATH, '//div[@class="ballarea  clearfix ball_table_room"]//input[contains(@value, "添加")][1]') # 膽拖生肖 輸入金額
    input_amount_bravery_tow_zodiac_sign_sf6 = (By.XPATH, '//div[@class="ballarea  clearfix ball_table_room"]//input[contains(@placeholder, "填入金额")][1]')
    button_lm_sf6 = (By.XPATH, '//span[@class="gameMenu-active-tab" and text()="连码"]') # 連碼
    button_bravery_tow_zodiac_sign_sf6 = (By.XPATH, '//a[text()="胆拖生肖"]') # 膽拖生肖

    # 頁面彩種名稱
    lottery_title = (By.XPATH, "//div[@class= 'clearfix titleBox']//a")

    ## 膽碼彩球
    def get_bravery_tow(self, num):
        return (By.XPATH, f'(//div[@class="redBallBox"]//a)[{num}]')

    ## 拖碼彩球
    def get_zodiac_sign(self, num):
        return (By.XPATH, f'(//div[@class="blueBallBox"]//a)[{num}]')

    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")

    game_sort = (By.XPATH, "//ol[@class= 'more-games-list']")

    # 彩種類型名稱
    @staticmethod
    def get_game_title(num):
        return (By.XPATH, f"(//ol[@class= 'more-games-list'])[{num}]/../a")
    
    # 抓取彩種
    @staticmethod
    def get_game_list(Game, num): 
        return (By.XPATH, f"//a[text()= '{Game}']/..//ol[@class= 'more-games-list'][{num}]//a")

    # 滑鼠移動到指定位置
    @staticmethod
    def lottery_menu(name):
        return (By.XPATH, f"//div[@class= 'header-nav']//a[contains(text(), '{name}')]")

    
class LotteryGamePage(BasePage):
    # 等待期數Loading結束
    def waitPeriodLoadingFinish(self):
        if self.is_element_finded(LotteryGamePageLocator.bet_loading) is True:
            self.wait_invisibility(LotteryGamePageLocator.bet_loading)

    def wait_betting_sealed_finish(self):
        if self.is_element_finded(LotteryGamePageLocator.bet_sealed_mask) is True:
            self.wait_invisibility(LotteryGamePageLocator.bet_sealed_mask)

    # 進入投注記錄
    def into_menu_betting_recording(self):
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.menu_betting_recording)

    # 期數檢查
    def periods_checker(self, num,Lottery_name=''):
        Time_now = datetime.datetime.now().strftime("%H%M")
        retry_time = 0
        
        if Lottery_name == 'Jisu11to5' and int(Time_now) < 1000:
           return

        while True:
            try:
                self.wait_loading_finish()
                self.waitPeriodLoadingFinish()
                self.wait_visibility(LotteryGamePageLocator.bet_area_check_point)  # 等待下注區出現
                self.wait_betting_sealed_finish()  # 等封盤消失

                self.wait_visibility(LotteryGamePageLocator.current_period)
                big_period = int(self.get_text(LotteryGamePageLocator.current_period))

                self.wait_visibility(LotteryGamePageLocator.lastest_period)
                small_period = int(self.get_text(LotteryGamePageLocator.lastest_period))

                period = big_period -1 - small_period 
            except BaseException as e:
                retry_time += 1
                if retry_time == 2:
                    print("疑似封盤or其他問題,Retry " + str(retry_time) + " 次")
                    raise e
                print(e)
                time.sleep(10)
                self.refresh_browser()
                continue
            break

        assert period <= num, "ERROR, 期數已相差 " + str(period) + " 期"

    # 下注並檢查是否成功
    def _add_order_and_betting(self, xpath):
        self.click(xpath)  # 下注添加
        assert self.is_element_enable(LotteryGamePageLocator.list_order) is True  # 確認下注添加
        self.scroll_to_bottom()  # 畫面滑至底部
        record = self._getrecord()
        self.click(LotteryGamePageLocator.btn_betting)  # 點擊投注鈕
        self.wait_visibility(LotteryGamePageLocator.bet_dialog)  # 等待下注後Dialog出現
        assert self.find_element(LotteryGamePageLocator.bet_dialog_message).text == '成功订单','訂單失敗'  # 確認下注成功
        self.click(LotteryGamePageLocator.bet_dialog_ok_btn)  # 點擊Dialog OK鈕
        # self.wait_not_presence(LotteryGamePageLocator.bet_dialog_mask)
        self.sleep(1)
        self.scroll_to_top()  # 滾動回頂部
        return record

    # 下注重複外框，參數method放下注function 
    def betting_game(self, method=None):
        retry_time = 0
        while True:
            try:
                self.wait_loading_finish()
                self.waitPeriodLoadingFinish()
                self.wait_visibility(LotteryGamePageLocator.bet_area_check_point)  # 等待下注區出現
                self.wait_betting_sealed_finish()  # 等封盤消失
                if method is not None:
                    return method()
            except BaseException as e:
                retry_time += 1
                if retry_time == 2:
                    print("疑似封盤or其他問題,Retry " + str(retry_time) + " 次")
                    raise e
                print(e)
                time.sleep(10)
                self.refresh_browser()
                continue
            break

    # 六合彩-特碼-號碼下注
    def betting_hk(self):
        self.type(LotteryGamePageLocator.input_tema_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_add_tema_order)
        return record
        
    # 六合彩-連肖連尾-二尾碰下注
    def betting_hk_lslw(self):
        self.click(LotteryGamePageLocator.btn_hk_game_lslw)
        self.click(LotteryGamePageLocator.bet_zmlw2_num1)
        self.click(LotteryGamePageLocator.bet_zmlw2_num2)
        self.type(LotteryGamePageLocator.input_zmlw2_bet_amount, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_zmlw2_add_order)
        return record
        
    # 三分六合彩-連碼-膽拖生肖下注
    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def betting_sf6_bravery_tow_zodiac_sign(self, bravery_tow, zodiac_sign):
        self.waitPeriodLoadingFinish()
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.button_lm_sf6)
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.button_bravery_tow_zodiac_sign_sf6)
        self.wait_loading_finish()

        self.click(LotteryGamePageLocator.get_bravery_tow(LotteryGamePageLocator, bravery_tow))
        self.click(LotteryGamePageLocator.get_zodiac_sign(LotteryGamePageLocator, zodiac_sign))
        self.type(LotteryGamePageLocator.input_amount_bravery_tow_zodiac_sign_sf6, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.button_add_bravery_tow_zodiac_sign_sf6)
        return record

    # 極速時時彩-兩面
    def betting_jsssc(self):
        self.type(LotteryGamePageLocator.input_lm_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_lm_add_order)
        return record

    # 極速PK10-冠亞和
    def betting_jspk10(self):
        self.click(LotteryGamePageLocator.byn_choice_game_gyh)
        self.type(LotteryGamePageLocator.input_gyh_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_gyh_add_order)
        return record

    def pcegg(self):
        self.type(LotteryGamePageLocator.input_egg_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_egg_add_order)
        return record

    def jisu11to5(self):
        self.type(LotteryGamePageLocator.input_jisu_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_jisu_order)
        return record

    def js3(self):
        self.type(LotteryGamePageLocator.input_js3_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_js3_order)
        return record

    def fu3d(self):
        self.type(LotteryGamePageLocator.input_fu3d_num1, '1')
        record = self._add_order_and_betting(LotteryGamePageLocator.btn_fu3d_order)
        return record

    def _getrecord(self):
        record_LIST={'period':'','type':'','num':'','money':''}
        record_LIST['period']=(self.get_text(LotteryGamePageLocator.current_period))
        record_LIST['type']=(self.get_text(LotteryGamePageLocator.record_TYPE))
        record_LIST['num']=(self.get_text(LotteryGamePageLocator.record_num))
        record_LIST['money']=(self.get_text(LotteryGamePageLocator.record_money))

        return record_LIST

    def image_check(self, Lottery, Sort=''):
        X,Y = 0,0
        
        if platform.system() == 'Linux': 
            self.wait_loading_finish()
            self.sleep(3)

            # 資料夾如果有兩層分類可使用
            if Sort == '':
                dir_path = '{0}/image/web/lottery/{1}/'.format(os.path.abspath(__file__).split('/Project')[0], Lottery)
            else:
                dir_path = '{0}/image/web/lottery/{1}/{2}/'.format(os.path.abspath(__file__).split('/Project')[0], Lottery, Sort)

            items = os.listdir(dir_path)
            newlist = []

            for names in items:
                if names.endswith(".png"):
                    newlist.append(names)

            # 圖形辨識
            for loop in range(0,len(newlist)):
                image_path = "{0}{1}_{2}.png".format(dir_path, Lottery, loop + 1)
            
                for _ in range(0,3):
                    try:
                        X,Y = self.image_search(image_path, 0.3) #  精準度最高為1
                        if X != 0 and Y != 0:
                            break
                    except:
                        self.sleep(1)

                assert X != 0 and Y != 0,'網頁找不指定圖片 X: {0} Y: {1}'.format(X,Y)
            
    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def get_odds_info(self):
        self.wait_loading_finish()
        Info = self.get_text_by_dom(self.find_element(LotteryGamePageLocator.odds))
        return Info

    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def js3_bet(self):
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.sj_link)
        self.sleep(2)

        if self.get_text_by_dom(self.find_element(LotteryGamePageLocator.now_time)) == "0": # 確定有無封盤
            self.sleep(20)
            
        period = self.get_text_by_dom(self.find_element(LotteryGamePageLocator.now_period))
        self.type(LotteryGamePageLocator.input_js3_num1, 10)

        self.click(LotteryGamePageLocator.btn_js3_order)
        self.click(LotteryGamePageLocator.btn_betting)
        self.sleep(3)
        self.click(LotteryGamePageLocator.btn_ok)

        return period
    
    def get_js3_bet_result(self, period):
        # 在 投注紀錄 頁面
        return self.get_text_by_dom(self.find_element(LotteryGamePageLocator.betting_record_win)) # 狀態 - 輸贏
        
    # 所有彩種比對
    def check_game_list_name(self, Lotterylist):
        Search_list = []
        Dict = {}
        game_sort = len(self.find_elements(LotteryGamePageLocator.game_sort))

        
        # 抓取彩種大種類名稱
        for Index in range(1, game_sort + 1):
            name = self.get_text(LotteryGamePageLocator.get_game_title(Index))
            Search_list.append(name)

        # 依據大種類找子類別
        for Search_name in Search_list:
            sort = []
            self.move_mouse(LotteryGamePageLocator.lottery_menu(Search_name))

            # 抓取種類名稱
            for game in self.find_elements(LotteryGamePageLocator.get_game_list(Search_name, 1)):
                Game_name = self.get_text_by_dom(game)
                sort.append(Game_name)

            # 組成字典 + 陣列
            Dict[Search_name] = sort

        # 比對後轉list傳出
        result = set(Dict) - set(Lotterylist)
        result = list(result)

        # 如果不為空,傳出錯誤
        if result:
            raise EOFError(f'彩種資料異常 差異彩種: {result}')

    # 進入香港又合彩並確認
    def into_and_checkhk(self, Hk_game: dict, Hk_data: list):
        self.wait_loading_finish()
        self.waitPeriodLoadingFinish()

        for Name_data in Hk_game.keys():
            for Game_name in Hk_game[Name_data]:
                self.move_mouse(LotteryGamePageLocator.lottery_menu(Name_data))
                self.wait_presence(LotteryGamePageLocator.lottery_menu(Game_name))
                self.click(LotteryGamePageLocator.lottery_menu(Game_name))

                assert self.get_text(LotteryGamePageLocator.lottery_title) == Game_name, f"倒轉至指定彩種錯誤 應為:{Game_name}"
                
                # if self.wait_visibility_status(LotteryGamePageLocator.main_menu) is True:
                #     self.click(LotteryGamePageLocator.bet_choose_game(Game_name))

                # self.check_subtype(Hk_data, Game_name)

    
    # 進入某彩種並確認
    def into_and_checkall(self, Main_game, Lottery_data: list, Game_data: list):
        self.wait_loading_finish()
        self.waitPeriodLoadingFinish()

        for Game_name in Lottery_data:
            if Game_name == '香港六合彩':
                continue
            
            self.move_mouse(LotteryGamePageLocator.lottery_menu(Main_game))
            self.wait_presence(LotteryGamePageLocator.lottery_menu(Game_name))
            self.click(LotteryGamePageLocator.lottery_menu(Game_name))

            # self.wait_visibility(LotteryGamePageLocator.bet_choose_btn)
            # self.click(LotteryGamePageLocator.bet_choose_btn)
            # self.wait_visibility(LotteryGamePageLocator.bet_choose_menu_check)

            # if self.wait_visibility_status(LotteryGamePageLocator.main_menu) is True:
            #     self.click(LotteryGamePageLocator.bet_choose_game(Game_name))
            
    #         assert self.wait_visibility_status(LotteryGamePageLocator.Popup) is True, f"上方彩種提示沒出現 彩種名稱:{Game_name}"
    #         assert self.get_text(LotteryGamePageLocator.Popup) == f"当前采种: {Game_name}", f"上方彩種提示沒出現 彩種名稱:{Game_name}"

    #         self.check_subtype(Game_data, Game_name)


    # 比對子彩種
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def check_subtype(self, Game_data: list, Game_name: str):
        for sort in Game_data:
            for sort_name in sort.keys():
                self.wait_betting_sealed_finish_new()
                
                for _ in range(0,2):
                    self.sleep(0.5)

                #     if self.is_element_finded(LotteryGamePageLocator.subtype_menu) is True:
                #         self.click(LotteryGamePageLocator.game_play)
                #         self.sleep(0.5)
                    
                #     if self.wait_visibility_status(LotteryGamePageLocator.bet_choose_play(sort_name)):
                #         self.click(LotteryGamePageLocator.bet_choose_play(sort_name))
                #         break                        
                
                # assert self.wait_visibility_status(LotteryGamePageLocator.bet_choose_check(sort_name)) is True, f"點擊彩種玩法錯誤, 彩種: {Game_name} 子玩法: {sort_name}"

                # for data in sort[sort_name]:
                #     # 連碼膽拖測試
                #     if isinstance(sort[sort_name][0], list) is True and sort_name == "连码":
                #         self.gallbladder_list(sort[sort_name], Game_name, sort_name, data)
                #         break

                #     # 因正碼特為二維陣列,故另外處理
                #     if isinstance(sort[sort_name][0], list) is True:
                #         self.hk_handicap_list(sort[sort_name], Game_name, sort_name, data) 
                #         break
                #     else:
                #         self.base_check(sort_name, Game_name, data) # 避免出現封盤,故另外開一個method包retry