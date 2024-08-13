from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import datetime,os,platform
import random, re
from retrying import retry

class LotteryGamePageLocator:
    
    # ------------------- 新版 -------------------
    ## ------------------ 玩法 ------------------
    game_play = (By.XPATH, '//div[contains(@class, "play-type__title")]')
    lm = (By.XPATH, '//div[text() = "连码" ]') # 連碼
    bravery_tow = (By.XPATH, '//div[text()="特串"]') # 特串
    bravery_tow_2 = (By.XPATH, '//li[text()="胆拖生肖"]') # 膽拖生肖
    nwap_check_p = (By.XPATH, "//span[@class='list-text']") # NWAP判斷點

    # 會員中心
    member_center_new = (By.XPATH, '//*[contains(@class, "item")]//*[contains(text(), "会员") or @href= "/m/member"]')
    # 投注紀錄
    betting_recode_new = (By.XPATH, '//*[contains(text(),"投注记录")]')
    # 彩票大廳
    lottery_hall_new = (By.XPATH, '//span[contains(text(), "彩票大厅")]')
    # 彩票遊戲
    lottery_game_new = (By.XPATH, '//div[contains(@class, "start")]//a[contains(@href, "/m/lottery")]')
    # 彩球定位
    bet_ball_new = (By.XPATH, '//div[contains(@class, "lottery-content")]//*[contains(@class, "bet-ball__column")]')
    # 香港六合彩定位
    hk6_game_new = (By.XPATH, '//*[@alt="香港六合彩"]/..')
    # 賠率定位
    bet_ball_odds = (By.XPATH, "//div[contains(@class, 'lottery-content')]//span[2]")
    # 拖碼定位
    bravery_tow_ball = (By.XPATH, '//li[@class="col3"]')
    #天天麻將首頁(彩票)
    lottery_menu = (By.XPATH, '//span[contains(text(), "彩票")]')
    #天天麻將最愛彩票
    lottery_fevery = (By.XPATH, '//span[text()="最爱"]')
    #天天麻將全部彩種
    lottery_all = (By.XPATH, '//div[contains(text(),"全部彩种")]')
    # 返回
    back = (By.XPATH, '//*[contains(@class,"back")]')
    home_back = (By.XPATH, '//div[@class="header__left"]')

    @staticmethod
    def lottery_link(self, name):
        return (By.XPATH, f'//p[text()= "{name}"]')

    def get_select_ball_xpath(self, index : int):
        return (By.XPATH, f'{self.bet_ball_new[1]}[{index}]')

    def get_bravery_tow_ball_by_index(self, index : int):
        return (By.XPATH, f'{self.bravery_tow[1]}[{index}]')

    def get_bravery_tow_ball_by_text(self, text : int):
        return (By.XPATH, f'//li[@class="col3" and text()="{text}"]')

    # 投注金額輸入框
    wager_input_box_new = (By.XPATH, '//div[@class="input"]/input')

    # 清除
    clear_selection_new = (By.XPATH, '//button[contains(@class, "btn-clear")]')
    # 投注
    bet_button_new = (By.XPATH, '//button[contains(@class, "btn-bet")]')

    # 期數
    period_new = (By.XPATH, '//p[@class="award-type__title-next"]')
    # 當期期數(已開獎)
    current_period_new = (By.XPATH, '//span[@class="award-type__number"]')
    # 上期期數
    last_period_new = (By.XPATH, '//table[@class="table table-striped"]//tr[2]//td[1]')
    # 下期期數(下注中)
    next_period_new = (By.XPATH, '//span[@class="award-type__number-next"]')

    # 彩種名稱
    bet_dialog_name_new = (By.XPATH, '(//div[@class="title"]//p[1])[last()]')
    # 玩法
    bet_dialog_rule_new = (By.XPATH, '//div[@class="title"]//p[2]')
    # 玩法子種類
    bet_dialog_sub_rule_new = (By.XPATH, '//span[@class="text-title"]')
    # 投注金額
    bet_dialog_wager_new = (By.XPATH, '//div[@class="money"]//span[1]')
    # 投注筆數
    bet_dialog_count_new = (By.XPATH, '//div[@class="money"]//span[2]')
    # 期數
    bet_dialog_period_new = (By.XPATH, '//p[@class="title" or @class="betting-periods"]//span')
    # 賠率
    bet_dialog_odds_new = (By.XPATH, '//div[@class="account-msg"]//span[2]')
    # 確認送出
    bet_dialog_submit_new = (By.XPATH, '//button[contains(text(),"送出")]')
    # 取消關閉
    bet_dialog_cancell_new = (By.XPATH, '//button[text()="取消关闭"]')
    # 封盤
    bet_sealed_mask_new = (By.XPATH, '//span[contains(text(), "封盘")]')
    # 投注結果確認
    bet_ok_new = (By.XPATH, "//button[@class='van-button van-button--default van-button--large van-dialog__confirm']")
    
    # --------------------- 助手 ---------------------- 
    help_button = (By.XPATH, '//span[text()="助手"]')
    check_help_button = (By.XPATH, '//div[@class="fab__main"]//*[@class="back"]')
    help_how_play_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="玩法"]')
    help_trend_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="走势"]')
    help_record_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="纪录"]')
    help_deposit_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="存款"]')
    help_service_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="客服"]')
    help_homepage_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="首页"]')
    help_withdrawal_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="取款"]')
    help_conversion_button = (By.XPATH, '//div[@class="fab__main"]/..//span[text()="額度"]')

    # --------------------- 玩法頁面 ---------------------- 
    how_play_page = (By.XPATH, "//*[text()='玩法']")

    # --------------------- 走势頁面 ---------------------- 
    trend_page = (By.XPATH, "//*[contains(text(),'走势')]")

    # --------------------- 纪录頁面 ---------------------- 
    record_page = (By.XPATH, "//*[text()='投注记录']")

    # --------------------- 存款頁面 ---------------------- 
    deposit_page = (By.XPATH, "//*[contains(text(),'充值')]")

    # --------------------- 客服頁面 ---------------------- 
    service_page = (By.XPATH, "//*[contains(text(),'客服')]")
    service_page_nwap = (By.XPATH, "//span[@class='logo-text'and text()='客服']")
    # --------------------- 首頁頁面 ---------------------- 
    home_page = (By.XPATH, "//*[@class='total_balance' or @class='user-info__wallet' or @class='fe-nav__balance']")

    # --------------------- 提款頁面 ---------------------- 
    withdrawal_page = (By.XPATH, "//*[contains(text(),'提款')]")

    # --------------------- 轉換頁面 ---------------------- 
    conversion_page = (By.XPATH, "//*[text()='转账' or text()='额度转换']")    

    # ------------------- 選彩種頁面 ------------------- 
    # 選彩種
    bet_choose_btn = (By.XPATH, '//span[text()="选彩种"]')
    # 選彩種中的六合彩標題
    bet_choose_menu_check = (By.XPATH, '//span[contains(text(),"六合彩")]')
    # 子玩法目錄確認
    subtype_menu = (By.XPATH, "//div[@class= 'play-type-contianer' and @style= 'display: none;']")
    # 主玩法目錄確認
    main_menu = (By.XPATH, "//div[@class= 'play-lottery-contianer']")
    # 下注頁上方玩法確認
    sub_navigation_bar1 = (By.XPATH, '//div[@aria-selected= "true"]/span')
    # 下注頁上方玩法確認
    sub_navigation_bar2 = (By.XPATH, '(//li[contains(@class,"col") and contains(@class,"active")])[last()]')
    # 第一次進彩種上方顯示彩種名稱提示
    popup = (By.XPATH, '//div[contains(@class, "van-popup")]')
    
    # 膽拖點擊確認
    @staticmethod
    def bet_choose_gallbladder_check(game):
        link = (By.XPATH, f'//li[@class= "col5 active" and text()= "{game}"]')
        return link

    # 膽拖點擊測試
    @staticmethod
    def bet_choose_gallbladder(game):
        link = (By.XPATH, f'//li[text()= "{game}"]')
        return link
    
    # 子玩法點擊確認
    @staticmethod
    def bet_choose_check(game):
        link = (By.XPATH, f'//span[text()="玩法"]/../..//div[contains(@class, "active") and text()= "{game}"]')
        return link

    # 子玩法點擊
    @staticmethod
    def bet_choose_play(game):
        link = (By.XPATH, f'//span[text()="玩法"]/../..//div[text()= "{game}"]')
        return link

    # 子玩法確認
    @staticmethod
    def bet_choose_subgame(game):
        link = (By.XPATH, f'//span[text()="子玩法"]/../..//div[text()= "{game}"]/..')
        return link

    # 選彩種 -> xxx 
    @staticmethod
    def bet_choose_game(game):
        link = (By.XPATH, f'//div[contains(@class, "btn")]/p[text()="{game}"]/..')
        return link
    
    # 抓取彩種
    @staticmethod
    def get_game_list(game):
        link = (By.XPATH, f'//span[contains(., "{game}")]/../..//div[contains(@class, "play-lottery__item")]')
        return link
    
    # 彩種類型名稱
    Game_title = (By.XPATH, "//div[@class='title']//span[contains(.,'')]")
    
    # ------------------- 新版 -------------------

    # ======================================== common utilties ========================================
    # current lottery
    current_lottery = "//div[@class='playtabs' or @class='playtabs pk10_ball_room' and not(@style='display: none;')]"
    current_open_betting_page = "//div[@class='game_content' and not(@style='display: none')]"

    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")

    # 封盤遮罩
    bet_sealed_mask = (By.XPATH, "//div[@class='game_time_out']")

    # 打開下注頁面
    btn_bet = (By.XPATH, current_lottery + "//div[@class='tittle']")
    old_btn_bet = (By.XPATH, current_lottery + "//div[@class='game_title']")

    # 第一顆彩球
    default_bet_ball = (By.XPATH, "//div[@class='lotto-medium-btn']")
    old_input_default_ball = (By.XPATH, current_lottery + current_open_betting_page + "//input")

    # 第一顆彩球(舊版除了cdd)
    old_other_brand_input_default_ball = (By.XPATH, "//div[@class='playtabs' and not(@style='display: none;')]//input")

    # 輸入金額
    input_default_bet_amount = (By.XPATH, "//input[@class='game_control_money']")

    # 添加注單
    btn_add_order = (By.XPATH, "//button[@id='game_submit']")
    
    # 送出注單
    btn_betting = (By.XPATH, "//div[@class='game_control_submit game_list_submit']//a/..")

    # BET DIALOG (下注後提示窗)
    bet_dialog = (By.XPATH, "//div[@role='dialog']")  # 下注後提示視窗
    bet_dialog_message = (By.XPATH, "//div[@class='swal2-header' or @class='swal2-contentwrapper']/h2")  # 下注提示窗訊息位置
    bet_dialog_ok_btn = (By.XPATH, "//button[@class='swal2-confirm swal2-styled']")  # 下注後提示視窗確認鈕
    bet_dialog_mask = (By.XPATH, "//div[@class='swal2-container swal2-center swal2-fade swal2-shown']")  # Dialog遮罩

    # 開獎區
    current_period = (By.XPATH, "//div[@class='game_info']/p[1]/i")  # 目前下注中期數
    lastest_period = (By.XPATH, "//p[@class='two_row_height' or @class='']/i")  # 最新已開獎期數

     # 投注清單
    record_box=(By.XPATH,"//div[@class='pop_list_box']")
    record_type = (By.XPATH, "//div[@class='pop_list_box']//td[@class='td1']")
    record_num = (By.XPATH, "//div[@class='pop_list_box']//td[@class='td1']/div")
    record_AMOUNT = (By.XPATH, "(//div[@class='pop_list_box']//th[@class='td3 color_m'])[1]")
    record_money = (By.XPATH, "(//div[@class='pop_list_box']//th[@class='td3 color_m'])[2]")
    #NEW
    record_type_new = (By.XPATH, "//tr[@class='title']//th")
    record_num_new = (By.XPATH, "//th//div[@class='ball-font']")
    record_amount_new = (By.XPATH, "(//th[@class='td3 color_m'])[1]")
    record_money_new = (By.XPATH, "(//th[@class='td3 color_m'])[2]")

    # =============================== 下注定位 ==============================
    # 香港六合彩
    hk_link = (By.XPATH, "//*[@alt='香港六合彩' or text()='香港六合彩']")
    hk_tema_link = (By.XPATH, "//option[text()='特码']")
    hk_lslw_link = (By.XPATH, "//option[text()='连肖连尾']")
    bet_zmlw2_num1 = (By.XPATH, current_lottery + "//div[text()='0尾']")
    bet_zmlw2_num2 = (By.XPATH, current_lottery + "//div[text()='1尾']")
    old_bet_zmlw2_num1 = (By.XPATH, current_lottery + current_open_betting_page + "//div[@class='rounded_edges ball_0尾']")
    old_bet_zmlw2_num2 = (By.XPATH, current_lottery + current_open_betting_page + "//div[@class='rounded_edges ball_1尾']")
    old_first_ball_input = (By.XPATH, "(//tbody//input[@type='number'])[1]")
    new_first_ball_input = (By.XPATH, "(//div[@class='ball-font'])[1]")
    # 極速11選5
    jisu_old_first_ball = (By.XPATH, "(//i[@class='icon-lottery-lotto-ball ball-color-blue'])[1]")

    # 下方單注金額
    single_bet_textarea = (By.XPATH, "//input[@class='game_control_money']")
    
    # 三分六和彩


    # MENU (彩票頁面上方連結)
    menu_betting_recording = (By.PARTIAL_LINK_TEXT, "投注纪录")  # 投注紀錄
    check_menu_betting_recording = (By.XPATH, "//div[contains(@class,'game_box')]")  # 投注紀錄

    #投注紀錄
    menu_record_list = (By.XPATH, "//div[@class='order-info']")  # 投注紀錄清單
    betting_record_win = (By.XPATH, "(//div[text()='输赢：']/../div/span)[1]") # 狀態 - 輸贏
    nwap_today = (By.XPATH, "//span[text()='本日']")  #本日
    nwap_week = (By.XPATH, "//span[text()='本周']")  #本周
    ticket_game_number = (By.XPATH, "//div[contains(text(),'期(局)号')]/..//div[@class='content__item']")  # 期號
    menu_record_null = (By.XPATH, "//div[@class='infinite-status-prompt' and @style='']//*[text()='无资料']") # 投注紀錄無資料
    status = (By.XPATH,"//div[@class='badge__text']") # 狀態

    #舊版上方下拉式選單
    lottery_select_old = (By.XPATH, "(//li[@class='select_box']//select)[1]")

    # 極速六合彩
    js6_link = (By.XPATH, "//option[text()='极速六合彩']")
    # 舊版上方搜尋列(下拉式選單)_極速六合彩
    # js6_link_old = (By.XPATH, "//select[contains(@onchange, 'location.href')]//..//option[@value='/m/lottery/js6']")

    # 急速時時彩
    jsssc_link = (By.XPATH, "//option[text()='极速时时彩']")
    jsssc_lm_link = (By.XPATH, "//option[text()='两面']")

    # 急速PK10
    jspk10_link = (By.XPATH, "//option[text()='极速PK拾']")
    jspk10_gyh_link = (By.XPATH, "//option[text()='冠亚和']")

    # PC蛋蛋
    pcball_link = (By.XPATH, "//option[text()='PC蛋蛋']")

    # 极速11选5
    jisu11x5_link = (By.XPATH, "//option[text()='极速11选5']")  # 极速11选5

    # 極速快三
    js3_link = (By.XPATH, "//option[text()='极速快3']")  # 極速快三

    # 福彩3D
    fu3d_link = (By.XPATH, "//option[text()='福彩3D']")  # 福彩3D

    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")

    # 封盤中
    closing = (By.XPATH, "//span[contains(text(), '封盘中')]")

    # =============================== 指數遊戲 ==============================
    #外層開獎數字
    def get_change_out(self, game):
        index = (By.XPATH, f'//p[text()="{game}"]/../../..//div[contains(@class,"stock__change")]')
        return index

    def stock_link(self, name):
        return (By.XPATH, f'//p[text()= "{name}" and @class="text-title"]')

    def stock_freq(self, frequency):
        return (By.XPATH, f'//a[@id="sidebar-btn-stock_index_{frequency}"]/span')

    #內層開獎數字
    get_change_in = (By.XPATH, '//div[contains(@class,"stock__change")]')
    stock_report = (By.XPATH, '//div[@class="lottery-time__content"]')  #歷史紀錄
    stock_report_button = (By.XPATH, '//div[@class="award-stock-group"]')
    stock_trend = (By.XPATH, '//span[text()="出仓走势"]')  #出倉走勢
    stock_result = (By.XPATH, '//span[text()="开奖结果"]')  #開獎結果
    stock_candle = (By.XPATH, '//span[text()="K线分析"]')  #K線分析
    next_period_aa = (By.XPATH, '//span[@class= "award-type__title__number"]')  #下期期數
    stock_tab_1 = (By.XPATH, '//span[text()="定位胆"]')  #定位玩法
    stock_tab_2 = (By.XPATH, '//span[text()="双面盘"]')  #雙面玩法

    stock_manual = (By.XPATH, '//span[@class="play-lottery__text"]')  #說明按鈕
    stock_manual_point = (By.XPATH, '//div[@class="rules-content"]')  #說明檢查點
    stock_bet_ok = (By.XPATH, '//button[@class="btn btn-primary" and text()=" 确认 "]')
    
class LotteryGamePage(BasePage):
    time=datetime.datetime.now()
    today = datetime.date.today()

    def wait_betting_sealed_finish(self):
        self.wait_invisibility(LotteryGamePageLocator.bet_sealed_mask)

    def back_home_page(self):
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.home_back)
        assert self.is_element_displayed(LotteryGamePageLocator.home_page) is True, "未返回至首頁"

    def into_hk6(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'香港六合彩')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

        if is_maintenance == False:
            self.click(LotteryGamePageLocator.hk_tema_link)
            self.wait_loading_finish()
    
    def into_js6(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'极速六合彩')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

        if is_maintenance == False:
            self.click(LotteryGamePageLocator.hk_tema_link)
            self.wait_loading_finish()

    def into_jsssc(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'极速时时彩')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

    def into_jspk10(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'极速PK拾')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)
        
        if is_maintenance == False:
            self.click(LotteryGamePageLocator.jspk10_gyh_link)
            self.wait_loading_finish()

    # def into_cqssc(self, is_maintenance=False):
    #     self.wait_loading_finish()

    #     start1 = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=0, minute=30, second=0)
    #     stop = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=3, minute=10, second=0)
    #     start2 = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=7, minute=30, second=0)
    #     Stop2 = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=23, minute=50, second=0)

    #     if self.time < start1 and self.time > stop or self.time < start2 and self.time > Stop2 :
    #             print('遊戲關閉中，開啟時間: 00:30-03:10 or 07:30-23:50')
    #             self.test_skip('遊戲關閉中，開啟時間: 00:30-03:10 or 07:30-23:50')

    #     self.click(LotteryGamePageLocator.cqssc_link)
    #     self.wait_loading_finish()
    #     self._check_maintenance(is_maintenance)

    #     if  is_maintenance == False:
    #         self.click(LotteryGamePageLocator.cqssc_lm_link)
    #         self.wait_loading_finish()

    def into_pcball(self, is_maintenance=False):
        self.wait_loading_finish()
        
        start = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=9, minute=5, second=0)
        Stop = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=23, minute=55, second=0)

        if self.time < start or self.time > Stop:
            print('遊戲關閉中，開啟時間: 9:05-23:55')
            self.test_skip('遊戲關閉中，開啟時間: 9:05-23:55')

        self.click(LotteryGamePageLocator.pcball_link)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

    def into_jisu11to5(self, is_maintenance=False):
        self.wait_loading_finish()

        start = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=9, minute=30, second=0)
        Stop = datetime.datetime(year=self.today.year, month=self.today.month, day=self.today.day, hour=23, minute=10, second=0)

        if self.time < start or self.time > Stop:
            print('遊戲關閉中，開啟時間: 9:30-23:10')
            self.test_skip('遊戲關閉中，開啟時間: 9:30-23:10')

        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'极速11选5')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

    def into_jisuk3(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'极速快3')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)

    def into_fu3d(self, is_maintenance=False):
        self.wait_loading_finish()
        self.select_by_text(LotteryGamePageLocator.lottery_select_old,'福彩3D')
        self.type_page_down(LotteryGamePageLocator.lottery_select_old)
        self.type_page_up(LotteryGamePageLocator.lottery_select_old)
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)
            
    # 測試維護
    def _check_maintenance(self, is_maintenance):
        if is_maintenance == True:
            assert self.is_element_finded(LotteryGamePageLocator.maintenance) is True, "系統沒顯示維護狀態"
            return     
              
        if self.is_element_finded(LotteryGamePageLocator.maintenance) is True:
            print("系統維護中")
            self.test_skip('系統維護中')

        if self.is_element_finded(LotteryGamePageLocator.closing) == True:
            if self.is_element_displayed(LotteryGamePageLocator.closing) is True:
                raise EOFError('不正常封盤中')


    # 進入投注記錄
    def into_menu_betting_recording(self):
        self.wait_loading_finish()
        sum=0
        while True:
            sum+=1
            try:
                self.click(LotteryGamePageLocator.menu_betting_recording)
                break
            except BaseException as e:
                if sum==6:
                    print('投注紀錄按鈕失效:%d次'%sum)
                    raise e
                self.refresh_browser()
                self.sleep(5)

        self.is_element_finded(LotteryGamePageLocator.menu_record_list)
        self.wait_loading_finish()

    # 下注並檢查是否成功
    def _add_order_and_betting(self):
        period=self.get_text(LotteryGamePageLocator.current_period)
        self.click(LotteryGamePageLocator.btn_add_order)  # 下注添加
        self.wait_visibility(LotteryGamePageLocator.record_box)

        if self.is_element_finded(LotteryGamePageLocator.record_type):
            record = self._getrecord(period)
        else:
            record = self._getrecord_new(period)

        self.click(LotteryGamePageLocator.btn_betting)  # 點擊投注鈕
        self.wait_visibility(LotteryGamePageLocator.bet_dialog)  # 等待下注後Dialog出現
        assert self.find_element(LotteryGamePageLocator.bet_dialog_message).text == '成功订单'  # 確認下注成功
        self.click(LotteryGamePageLocator.bet_dialog_ok_btn)  # 點擊Dialog OK鈕
        return record

    # 期數檢查
    def periods_checker(self, num,lottery_name=''):
        for loop in range(1, 4):
            self.wait_loading_finish()
            big_period = self.find_element(LotteryGamePageLocator.current_period).text
            small_period = self.find_element(LotteryGamePageLocator.lastest_period).text
            time_now = datetime.datetime.now().strftime("%H%M")

            if big_period != '' and small_period != '':
                break
            if loop == 2:
                raise Exception('抓取期數錯誤:%d次 最新期數:%s 上一期期數:%s'%(loop,big_period,small_period))
            self.sleep(5)
            self.refresh_browser()

        if lottery_name == 'Jisu11to5' and int(time_now) < 1000:
            return

        period = int(big_period) - 1 - int(small_period)
        assert period <= num, "ERROR, 期數已相差 " + str(period) + " 期"

    # ----------------------------------------- 新版 wap -----------------------------------------    


    def wait_betting_sealed_finish_new(self):
        try:
            self.wait_invisibility(LotteryGamePageLocator.bet_sealed_mask_new)
        except:
            raise EOFError("封盤屏蔽畫面沒有消失")

    # 期數檢查
    # @retry(stop_max_attempt_number=10, wait_fixed=3000)
    def check_periods_new(self, num, lottery_name=''):
        time_now = datetime.datetime.now().strftime("%H%M")
        if lottery_name == 'Jisu11to5' and int(time_now) < 1000:
            return

        for loop in range(1, 4):
            self.wait_loading_finish()
            self.sleep(1)
            if self.is_element_finded(LotteryGamePageLocator.last_period_new) is False:
                self.click(LotteryGamePageLocator.current_period_new)

            current_period = self.get_text(LotteryGamePageLocator.current_period_new)
            last_period = self.get_text(LotteryGamePageLocator.last_period_new)
            now_period = self.get_text(LotteryGamePageLocator.next_period_new)

            if current_period != '' and last_period != '' and now_period !='':
                next_period = int(now_period) - int(current_period)
                try:
                    assert next_period <= int(num), f"未開盤期數不正確 已開:{current_period} 未開:{now_period} 期數差: {next_period}"
                    break
                except:
                    pass
            if loop == 2:
                raise Exception(f'抓取期數錯誤: {loop} 次 最新期數: {current_period}  上一期期數: {last_period}')

            self.sleep(5)
            self.refresh_browser()


    # 進入新版投注記錄
    @retry(stop_max_attempt_number=3, wait_fixed=3000)
    def into_menu_betting_record_new(self):
        self.refresh_browser()
        self.close_message_dialog()
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.member_center_new)  
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.betting_recode_new)

    def get_record_new(self, bet_ball_text):
        '''
            取得投注時的投注資料
        '''
        record = {}
        name = self.get_text(LotteryGamePageLocator.bet_dialog_name_new)
        rule = self.get_text(LotteryGamePageLocator.bet_dialog_rule_new).split('-')
        wager = self.get_text(LotteryGamePageLocator.bet_dialog_wager_new)
        count = self.get_text(LotteryGamePageLocator.bet_dialog_count_new)
        period = self.get_text(LotteryGamePageLocator.bet_dialog_period_new)
        odds = self.get_text(LotteryGamePageLocator.bet_dialog_odds_new).replace('x', '')

        if self.is_element_finded(LotteryGamePageLocator.bet_dialog_sub_rule_new):
            sub_rule = self.get_text(LotteryGamePageLocator.bet_dialog_sub_rule_new)

        if len(rule) == 3:
            detail = f'[{rule[1]}] - {rule[0]}-{rule[2]} [共{count}注]{bet_ball_text}'
            if rule[1] == '1':
                bet_ball_text = int(bet_ball_text)
                detail = f'{sub_rule} [共{count}注]{bet_ball_text}' 
        else: 
            detail = f'{self.get_text(LotteryGamePageLocator.bet_dialog_rule_new)}'
            if self.is_element_finded(LotteryGamePageLocator.bet_dialog_sub_rule_new):
                if '[' not in detail:
                    if ' ' in sub_rule:
                        sub_rule = sub_rule.split(" ")[0]
        
                    if sub_rule == bet_ball_text:
                        detail = f'{detail} [共{count}注]{bet_ball_text}'
                    elif '军' in sub_rule :
                        detail = f'{"[A盘]"} - {sub_rule.split(" ")[0]} [共{count}注]{bet_ball_text}'
                    else:
                        detail = f'{(detail.split("-")[0])} - {sub_rule.split(" ")[0]} [共{count}注]{bet_ball_text}'
                
        record['name'] = f'{name}'
        record['money'] = f'{count}注 {wager}元'
        record['num'] = f'{bet_ball_text}'
        record['period'] = f'{period}'
        record['type'] = f'{detail}' 
  
        return record

    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def betting_game_new(self):
        '''點擊任一該頁面可下注的'''
        self.wait_loading_finish()
        self.refresh_browser()
        self.wait_loading_finish()
        # 計算第一區彩球的數量
        
        wager = random.randint(1, 10)
        all_ball = self.find_elements(LotteryGamePageLocator.bet_ball_new)
        bet_ball_num = random.randint(0, len(all_ball))
        if bet_ball_num > 10:
            bet_ball_num = random.randint(0, 10)
        bet_ball = all_ball[bet_ball_num]

        self.click_by_dom(bet_ball)
        bet_ball_text = self.get_text_by_dom(bet_ball).split('\n')[0]

        self.type(LotteryGamePageLocator.wager_input_box_new, wager)
        self.click(LotteryGamePageLocator.bet_button_new)
        self.sleep(1)
        record = self.get_record_new(bet_ball_text)

        self.click(LotteryGamePageLocator.bet_dialog_submit_new)
        self.wait_visibility(LotteryGamePageLocator.bet_ok_new)
        self.click(LotteryGamePageLocator.bet_ok_new)

        return record

    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def betting_bravery_tow_new(self):

        '''膽拖下注'''
        self.wait_loading_finish()

        bet_ball = random.choice(self.find_elements((By.XPATH, f'({LotteryGamePageLocator.bet_ball_new[1]}/..)[1]/*//span[1]' )))
        bravery_tow_ball = random.choice(self.find_elements(LotteryGamePageLocator.bravery_tow_ball))
        self.click_by_dom(bet_ball)
        self.sleep(0.5)
        self.click_by_dom(bravery_tow_ball)

        wager = random.randint(1, 10)
        bet_ball_text = self.get_text_by_dom(bet_ball)

        self.type(LotteryGamePageLocator.wager_input_box_new, wager)
        self.click(LotteryGamePageLocator.bet_button_new)
        self.sleep(1)
        record = self.get_record_new(bet_ball_text)

        self.click(LotteryGamePageLocator.bet_dialog_submit_new)
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.bet_ok_new)

        return record

    def into_nwap_lottery_game(self, game_xpath, Lottery, is_maintenance = False):
        self.wait_loading_finish()

        self.click(LotteryGamePageLocator.lottery_menu)
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.lottery_fevery)
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.lottery_all)
        for _ in range(0, 2):
            try:
                self.click(game_xpath)
                break
            except:
                pass
        
        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)


    def into_lottery_game_new(self, game_xpath, Lottery, item_check = False, is_maintenance = False):
        self.wait_loading_finish()
          
        if self.is_element_finded(LotteryGamePageLocator.lottery_hall_new ):
            self.click(LotteryGamePageLocator.lottery_hall_new )

        elif self.is_element_finded(LotteryGamePageLocator.lottery_game_new):
            self.click(LotteryGamePageLocator.lottery_game_new)

        # 部分彩票遊戲不會出現在彩票大廳
        # 未出現的就統一先進 香港六合彩，再透過選採種來選擇要進的遊戲
        if self.is_element_finded(game_xpath):
            for _ in range(0, 2):
                try:
                    self.click(game_xpath)
                    break
                except:
                    pass
        else:
            try:
                self.click(LotteryGamePageLocator.hk6_game_new)
            except:
                raise EOFError('找不到彩種icon')

            self.wait_visibility(LotteryGamePageLocator.bet_choose_btn)
            self.click(LotteryGamePageLocator.bet_choose_btn)
            self.wait_visibility(LotteryGamePageLocator.lottery_all)
            self.click(LotteryGamePageLocator.lottery_all)
            self.click(game_xpath)

        self.wait_loading_finish()
        self._check_maintenance(is_maintenance)


        if item_check == True:
            for loop in range(0,3):
                self.refresh_browser()
                try:
                    assert self.is_element_displayed(LotteryGamePageLocator.popup) is True, "上方彩種提示沒出現 彩種名稱: 香港六合彩"
                    assert self.get_text(LotteryGamePageLocator.popup).__contains__("当前彩种: 香港六合彩"), "上方彩種提示沒出現 彩種名稱:香港六合彩"
                    break
                except:
                    self.sleep(0.5)

                if loop == 2:
                    assert self.is_element_displayed(LotteryGamePageLocator.popup) is True, "上方彩種提示沒出現 彩種名稱: 香港六合彩"
                    assert self.get_text(LotteryGamePageLocator.popup).__contains__("当前彩种: 香港六合彩"), "上方彩種提示沒出現 彩種名稱:香港六合彩"

    def into_other_game_play(self, game_play, sub_game_play='', sub_game_play_2=''):
        self.wait_loading_finish()
        for _ in range(3):
            if self.wait_visibility_status(LotteryGamePageLocator.game_play):
                self.click(LotteryGamePageLocator.game_play)
                break
            else:
                self.sleep(0.5)
        assert self.is_element_displayed(game_play), '未正確進入子玩法'
        self.sleep(0.5)
        self.click(game_play)

        if sub_game_play:
            self.sleep(0.5)
            self.click(sub_game_play)
            self.sleep(0.5)
            self.click(sub_game_play_2)

    def into_sf6_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '三分六合彩'), '三分六合彩', is_maintenance = is_maintenance)

    def into_hk6_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '香港六合彩'), '香港六合彩', item_check = True, is_maintenance = is_maintenance)

    def into_jisuk3_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '极速快3'), '极速快3', is_maintenance = is_maintenance)

    def into_js6_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '极速六合彩'), '极速六合彩', is_maintenance = is_maintenance)

    def into_jsssc_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '极速时时彩'), '极速时时彩', is_maintenance = is_maintenance)

    def into_jspk10_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '极速PK拾'), '极速PK拾', is_maintenance = is_maintenance)

    def into_fu3d_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '福彩3D'), '福彩3D', is_maintenance = is_maintenance)

    def into_pcegg_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, 'PC蛋蛋'), 'PC蛋蛋', is_maintenance = is_maintenance)
    
    def into_jisu11to5_new(self, is_maintenance = False):
        self.into_lottery_game_new(LotteryGamePageLocator.lottery_link(self, '极速11选5'), '极速11选5', is_maintenance = is_maintenance)    

    def into_sf6_bravery_tow_new(self, is_maintenance = False):
        self.into_sf6_new(is_maintenance)
        self.into_other_game_play(LotteryGamePageLocator.lm, LotteryGamePageLocator.bravery_tow, LotteryGamePageLocator.bravery_tow_2)
        self.wait_visibility(LotteryGamePageLocator.bravery_tow_2)
        self.click(LotteryGamePageLocator.bravery_tow_2)
        self.sleep(5)
    
    # ----------------------------------------- 天天麻將彩票 ----------------------------------------- 
    
    def into_hk_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '香港六合彩'), '香港六合彩', is_maintenance)

    def into_sf6_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '三分六合彩'), '三分六合彩', is_maintenance)

    def into_jisuk3_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '极速快3'), '极速快3', is_maintenance)
    
    def into_js6_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '极速六合彩'), '极速六合彩', is_maintenance)
    
    def into_jsssc_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '极速时时彩'), '极速时时彩', is_maintenance)
    
    def into_jspk10_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '极速PK拾'), '极速PK拾', is_maintenance)
    
    def into_fu3d_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '福彩3D'), '福彩3D', is_maintenance)
    
    def into_pcegg_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, 'PC蛋蛋'), 'PC蛋蛋', is_maintenance)

    def into_jisu11to5_nwap(self, is_maintenance = False):
        self.into_nwap_lottery_game(LotteryGamePageLocator.lottery_link(self, '极速11选5'), '极速11选5', is_maintenance)

    def into_sf6_bravery_tow_nwap(self, is_maintenance = False):
        self.into_sf6_nwap(is_maintenance)
        self.into_other_game_play(LotteryGamePageLocator.lm, LotteryGamePageLocator.bravery_tow, LotteryGamePageLocator.bravery_tow_2)
        self.wait_visibility(LotteryGamePageLocator.bravery_tow_2)
        self.click(LotteryGamePageLocator.bravery_tow_2)
        self.sleep(5)

    def click_help(self):
        if self.is_element_displayed(LotteryGamePageLocator.help_button) is True:
            self.click(LotteryGamePageLocator.help_button)
            assert self.is_element_finded(LotteryGamePageLocator.check_help_button) is True, "展開助手錯誤"
            self.sleep(1)

    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def help_items(self):
        service = []
        service_error = []
        self.wait_loading_finish()

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_how_play_button) is True:
            self.click(LotteryGamePageLocator.help_how_play_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.how_play_page) is False:
                service_error.append("開啟玩法頁面錯誤")
            self.click(LotteryGamePageLocator.back)
            self.wait_loading_finish()
        else:
            service.append('玩法按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_trend_button) is True:
            self.click(LotteryGamePageLocator.help_trend_button)
            self.wait_loading_finish()
    
            if self.is_element_finded(LotteryGamePageLocator.trend_page) is False:
                service_error.append("開啟走势頁面錯誤")
            self.click(LotteryGamePageLocator.back)
            self.wait_loading_finish()
        else:
            service.append('走勢按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_record_button) is True:
            self.click(LotteryGamePageLocator.help_record_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.record_page) is False:
                service_error.append("開啟纪录頁面錯誤")
            self.back()
            self.wait_loading_finish()
        else:
            service.append('紀錄按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_deposit_button) is True:
            self.click(LotteryGamePageLocator.help_deposit_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.deposit_page) is False:
                service_error.append("開啟存款頁面錯誤")
            self.back()
            self.wait_loading_finish()
        else:
            service.append('存款按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_service_button) is True:
            self.click(LotteryGamePageLocator.help_service_button)
            self.wait_loading_finish()
            
            if self.is_element_finded(LotteryGamePageLocator.nwap_check_p) is False:
                if self.is_element_finded(LotteryGamePageLocator.service_page) is False:
                    service_error.append("開啟客服頁面錯誤")
                self.switch_home_page()
            else:
                if self.is_element_finded(LotteryGamePageLocator.service_page_nwap) is False:
                    service_error.append("開啟客服頁面錯誤")
                self.back()
            self.wait_loading_finish()
        else:
            service.append('客服按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_withdrawal_button) is True:
            self.click(LotteryGamePageLocator.help_withdrawal_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.withdrawal_page) is False:
                service_error.append("開啟提款頁面錯誤")
            self.back()
            self.wait_loading_finish()
        else:
            service.append('提款按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_conversion_button) is True:
            self.click(LotteryGamePageLocator.help_conversion_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.conversion_page) is False:
                service_error.append("開啟額度轉換頁面錯誤")
            self.back()
            self.wait_loading_finish()
        else:
            service.append('額度轉換按紐沒開啟')

        self.click_help()
        if self.is_element_finded(LotteryGamePageLocator.help_homepage_button) is True:
            self.click(LotteryGamePageLocator.help_homepage_button)
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.home_page) is False:
                service_error.append("開啟首頁頁面錯誤")
            self.switch_home_page()
            self.wait_loading_finish()
        else:
            service.append('首頁按紐沒開啟')

        if service != []:
            print(service)
        
        assert len(service_error) == 0, f'下列導轉頁面有誤 : {service_error}'
            
    # 檢查大彩種名稱
    def into_game_list(self):
        self.wait_loading_finish()

        if self.is_element_finded(LotteryGamePageLocator.lottery_hall_new) is True:
            self.click(LotteryGamePageLocator.lottery_hall_new)
        
        self.wait_visibility(LotteryGamePageLocator.bet_choose_btn)
        self.click(LotteryGamePageLocator.bet_choose_btn)
        self.wait_visibility(LotteryGamePageLocator.bet_choose_menu_check)

    # 進入香港又合彩並確認
    def into_and_checkhk(self, hk_game: dict, hk_data: list):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for name_data in hk_game.keys():
            for game_name in hk_game[name_data]:
                self.wait_visibility(LotteryGamePageLocator.bet_choose_btn)
                self.click(LotteryGamePageLocator.bet_choose_btn)
                self.wait_visibility(LotteryGamePageLocator.bet_choose_menu_check)
                
                if self.wait_visibility_status(LotteryGamePageLocator.main_menu) is True:
                    self.click(LotteryGamePageLocator.bet_choose_game(game_name))

                self.check_subtype(hk_data, game_name)


    # 進入某彩種並確認
    def into_and_checkall(self, lottery_data: list, game_data: list):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for game_name in lottery_data:
            if game_name == '香港六合彩':
                continue

            self.wait_visibility(LotteryGamePageLocator.bet_choose_btn)
            self.click(LotteryGamePageLocator.bet_choose_btn)
            self.wait_visibility(LotteryGamePageLocator.bet_choose_menu_check)

            if self.wait_visibility_status(LotteryGamePageLocator.main_menu) is True:
                self.click(LotteryGamePageLocator.bet_choose_game(game_name))
            
            assert self.wait_visibility_status(LotteryGamePageLocator.popup) is True, f"上方彩種提示沒出現 彩種名稱:{game_name}"
            assert self.get_text(LotteryGamePageLocator.popup) == f"当前采种: {game_name}", f"上方彩種提示沒出現 彩種名稱:{game_name}"

            self.check_subtype(game_data, game_name)

    # 比對子彩種
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def check_subtype(self, game_data: list, game_name: str):
        for sort in game_data:
            for sort_name in sort.keys():
                self.wait_betting_sealed_finish_new()
                
                for _ in range(0,2):
                    self.sleep(0.5)

                    if self.is_element_finded(LotteryGamePageLocator.subtype_menu) is True:
                        self.click(LotteryGamePageLocator.game_play)
                        self.sleep(0.5)
                    
                    if self.wait_visibility_status(LotteryGamePageLocator.bet_choose_play(sort_name)):
                        self.click(LotteryGamePageLocator.bet_choose_play(sort_name))
                        break                        
                
                assert self.wait_visibility_status(LotteryGamePageLocator.bet_choose_check(sort_name)) is True, f"點擊彩種玩法錯誤, 彩種: {game_name} 子玩法: {sort_name}"

                for data in sort[sort_name]:
                    # 連碼膽拖測試
                    if isinstance(sort[sort_name][0], list) is True and sort_name == "连码":
                        self.gallbladder_list(sort[sort_name], game_name, sort_name, data)
                        break

                    # 因正碼特為二維陣列,故另外處理
                    if isinstance(sort[sort_name][0], list) is True:
                        self.hk_handicap_list(sort[sort_name], game_name, sort_name, data) 
                        break
                    else:
                        self.base_check(sort_name, game_name, data) # 避免出現封盤,故另外開一個method包retry
    
    # 一般子玩法確認
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def base_check(self, sort_name, game_name, data):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for _ in range(0,2):
            if self.is_element_finded(LotteryGamePageLocator.subtype_menu) is True:
                self.click(LotteryGamePageLocator.game_play)
                break

        if data != "只有一种":
            if self.wait_visibility_status(LotteryGamePageLocator.bet_choose_subgame(data)) is True:
                self.sleep(0.1)
                self.click(LotteryGamePageLocator.bet_choose_subgame(data))
                
                # 因只有一種子玩法,但還是要選號碼,邏輯上有衝突,故例外處理
                if any(re.findall(r'B|C', sort_name, re.IGNORECASE)) is False:
                    assert self.get_text(LotteryGamePageLocator.sub_navigation_bar1) == data, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {data}"
                
                elif any(re.findall(r'特码-B盘|特码-C盘', sort_name, re.IGNORECASE)) is False:
                    assert self.get_text(LotteryGamePageLocator.sub_navigation_bar1) == data.split("-")[0], f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {data}"
                
                assert any(re.findall(f'{sort_name}|{data}', self.get_text(LotteryGamePageLocator.game_play), re.IGNORECASE)) is True, f"玩法顯示內容不正確, 彩種: {game_name} 子玩法: {sort_name} -> {data}"
            else:
                raise EOFError(f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {data}")

    # 連碼處理
    def gallbladder_list(self, game_list, game_name, sort_name, data):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for name in game_list[0]:
            self.gallbladder_check(game_list[1], name, game_name, sort_name, data) # 避免出現封盤,故另外開一個method包retry

    # 連碼確認
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def gallbladder_check(self, game_list, name, game_name, sort_name, data):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for _ in range(0,2):
            if self.is_element_finded(LotteryGamePageLocator.subtype_menu) is True:
                self.click(LotteryGamePageLocator.game_play)
                break

        if self.wait_visibility_status(LotteryGamePageLocator.bet_choose_subgame(name)) is True:
            self.sleep(0.1)
            self.click(LotteryGamePageLocator.bet_choose_subgame(name)) 
            self.refresh_browser()
            self.wait_loading_finish()

        for handicap in game_list:
            self.click(LotteryGamePageLocator.bet_choose_gallbladder(handicap))

            assert any(re.findall(f'{sort_name}|{name}', self.get_text(LotteryGamePageLocator.game_play), re.IGNORECASE)) is True, f"玩法顯示內容不正確, 彩種: {game_name} 子玩法: {sort_name} -> {name} -> {handicap}"
            assert self.wait_visibility_status(LotteryGamePageLocator.bet_choose_gallbladder_check(handicap)) is True, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {name} -> {handicap}"
            assert self.get_text(LotteryGamePageLocator.sub_navigation_bar1) == name, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {name} -> {handicap}"
            assert self.get_text(LotteryGamePageLocator.sub_navigation_bar2) == handicap, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {name} -> {handicap}"
            
    # 正碼特處理
    def hk_handicap_list(self, game_list, game_name, sort_name, data):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for name in game_list[0]:
            for handicap in game_list[1]:
                self.hk_handicap_check(name, handicap, game_name, sort_name, data) # 避免出現封盤,故另外開一個method包retry

    # 正碼特確認
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def hk_handicap_check(self, name, handicap, game_name, sort_name, data):
        self.wait_loading_finish()
        self.wait_betting_sealed_finish_new()

        for _ in range(0,2):
            if self.is_element_finded(LotteryGamePageLocator.subtype_menu) is True:
                self.sleep(0.1)
                self.click(LotteryGamePageLocator.game_play)
                break

        if self.wait_visibility_status(LotteryGamePageLocator.bet_choose_subgame(name + handicap)) is True:
            self.sleep(0.1)
            self.click(LotteryGamePageLocator.bet_choose_subgame(name + handicap))
            
            self.refresh_browser()
            self.wait_loading_finish()
            self.sleep(0.5)

            handicap = str(handicap).replace("-","")
            assert self.get_text(LotteryGamePageLocator.sub_navigation_bar1) == name, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {handicap}"
            assert self.get_text(LotteryGamePageLocator.sub_navigation_bar2) == handicap, f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {sort_name} -> {handicap}"
            assert any(re.findall(f'{sort_name}|{name}|{handicap}', self.get_text(LotteryGamePageLocator.game_play), re.IGNORECASE)) is True, f"玩法顯示內容不正確, 彩種: {game_name} 子玩法: {sort_name} -> {handicap}"
        else:
            raise EOFError(f"點擊彩種錯誤, 彩種: {game_name} 子玩法: {name}{handicap}")

    # 所有彩種比對
    def check_game_list_name(self, Lotterylist):
        search_list = []
        dict_ = {}

        # 抓取彩種大種類名稱
        for name in self.find_elements(LotteryGamePageLocator.Game_title):
            # 排除空白的部分
            if self.get_text_by_dom(name) != '':
                search_list.append(self.get_text_by_dom(name))

        # 依據大種類找子類別
        for search_name in search_list:
            sort = []

            # 抓取種類名稱
            for game in self.find_elements(LotteryGamePageLocator.get_game_list(search_name)):
                game_name = self.get_text_by_dom(game)

                # 排除空白的部分
                if game_name != '':
                    sort.append(game_name)

            # 組成字典 + 陣列
            dict_[search_name] = sort

        del dict_['最爱彩种']

        # 比對後轉list傳出
        result = set(dict_) - set(Lotterylist)
        result = list(result)

        # 如果不為空,傳出錯誤
        if result:
            raise EOFError(f'彩種資料異常 差異彩種: {result}')
        
        # 回到香港六合彩頁面
        self.click(LotteryGamePageLocator.bet_choose_game("香港六合彩"))

    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def get_odds_info(self):
        self.wait_loading_finish()
        Info = self.get_text_by_dom(self.find_element(LotteryGamePageLocator.bet_ball_odds))
        return Info

    def get_js3_bet_result(self, period):
        # 在 投注紀錄 頁面
        self.wait_loading_finish()
        for _ in range(0,4):
            self.click(LotteryGamePageLocator.nwap_today)
            self.wait_loading_finish()
            self.sleep(1)
            if self.is_element_finded(LotteryGamePageLocator.ticket_game_number) is True:
                ticket_number = self.get_text(LotteryGamePageLocator.ticket_game_number)
                assert ticket_number == period, f'投注紀錄期數有誤,應為:{period}，投注紀錄顯示為:{ticket_number}'
                break
            else:
                self.click(LotteryGamePageLocator.nwap_week)
                self.sleep(10)

        assert self.is_element_finded(LotteryGamePageLocator.menu_record_null)==False, f'投注紀錄查無資料'
        for _ in range(0,4):
            if self.get_text(LotteryGamePageLocator.status) == '待结算':
                self.click(LotteryGamePageLocator.nwap_week)
                self.sleep(10)
                self.click(LotteryGamePageLocator.nwap_today)
            else:
                break
        return self.get_text_by_dom(self.find_element(LotteryGamePageLocator.betting_record_win)) # 狀態 - 輸贏
    
    #檢查作廢後，投注紀錄不應查找到指定期數
    def check_abolishment_record(self, period):
        # 在 投注紀錄 頁面
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.nwap_today)
        self.wait_loading_finish()
        self.sleep(2)
        if self.is_element_finded(LotteryGamePageLocator.menu_record_null):
            pass
        else:
            for number in self.find_elements(LotteryGamePageLocator.ticket_game_number):
                ticket_number = self.get_text_by_dom(number)
                assert ticket_number != period, f'投注紀錄仍有顯示作廢期數'

    # ----------------------------------------- 新版 wap -----------------------------------------
    # 下注重複外框，參數method放下注function
    def betting_game(self, method=None):
        retry_time = 0
        while True:
            try:
                self.wait_loading_finish()
                self.wait_betting_sealed_finish()  # 等封盤消失
                if method is not None:
                    return method()
            except BaseException as e:
                retry_time += 1
                if retry_time == 2:
                    print("疑似封盤or其他問題,Retry " + str(retry_time) + " 次")
                    raise e
                # print(e)
                self.sleep(10)
                self.refresh_browser()
                continue
            break

    def betting_hk_lslw(self):
        if self.is_element_finded(LotteryGamePageLocator.hk_lslw_link) is True:
            self.click(LotteryGamePageLocator.hk_lslw_link)
            if self.is_element_finded(LotteryGamePageLocator.btn_bet) is True:
                self.click(LotteryGamePageLocator.btn_bet)
                self.wait_loading_finish()
                self.click(LotteryGamePageLocator.bet_zmlw2_num1)
                self.click(LotteryGamePageLocator.bet_zmlw2_num2)
                self.type(LotteryGamePageLocator.input_default_bet_amount, '1')
                record = self._add_order_and_betting()
                return record
            else:
                return self.old_betting_hk_lslw()

    # PC蛋蛋&極速11選5&極速快三(舊_新版(only cdd))
    def betting_2(self):
        if self.is_element_finded(LotteryGamePageLocator.new_first_ball_input) is True:
            self.click(LotteryGamePageLocator.new_first_ball_input)
            self.wait_loading_finish()
            self.sleep(1)
            self.type(LotteryGamePageLocator.single_bet_textarea, '1')
            self.wait_loading_finish()
            self.sleep(1)
            record = self._add_order_and_betting()
            return record
        else:
            return self.old_betting_2()
    """    
    def betting_hk(self):
        self.click(LotteryGamePageLocator.btn_bet)
        self.type(LotteryGamePageLocator.INPUT_BET_AMOUNT, '1')
        # self.type(LotteryGamePageLocator.input_default_bet_amount, '1')
        self.click(LotteryGamePageLocator.btn_add_order)
        self.click(LotteryGamePageLocator.btn_betting)
        self.click(LotteryGamePageLocator.BTN_CHECKING)
    """

    def betting(self):    #新版彩票走betting_game_new，舊版彩票走old_Betting，此function除了當舊版跳板之外，只有cdd適用
        try:
            if self.is_element_displayed(LotteryGamePageLocator.default_bet_ball) is False:
                if self.is_element_finded(LotteryGamePageLocator.btn_bet) is True:
                    self.click(LotteryGamePageLocator.btn_bet)
                else:
                    raise EOFError

            self.wait_loading_finish()
            self.type(LotteryGamePageLocator.input_default_bet_amount, '1')
            self.sleep(1)
            self.click(LotteryGamePageLocator.default_bet_ball)
            self.wait_loading_finish()
            self.sleep(1)
            record = self._add_order_and_betting()
            return record
        except:
            return self.old_Betting()

    def old_Betting(self):
        if self.is_element_displayed(LotteryGamePageLocator.old_input_default_ball) is False:
            if self.is_element_finded(LotteryGamePageLocator.old_btn_bet) is True:
                self.click(LotteryGamePageLocator.old_btn_bet)
            else:
                raise EOFError('點擊彩票遊戲子類型錯誤')

        self.wait_loading_finish()
        self.sleep(1)
        self.type(LotteryGamePageLocator.old_input_default_ball, '1')
        self.wait_loading_finish()
        self.sleep(1)
        record = self._add_order_and_betting()

        return record

    def old_betting_hk_lslw(self):
        self.click(LotteryGamePageLocator.hk_lslw_link)
        self.click(LotteryGamePageLocator.old_btn_bet)
        self.click(LotteryGamePageLocator.old_bet_zmlw2_num1)
        self.click(LotteryGamePageLocator.old_bet_zmlw2_num2)
        self.type(LotteryGamePageLocator.old_input_default_ball, '1')
        record = self._add_order_and_betting()

        return record

    # PC蛋蛋&極速11選5&極速快三
    def old_betting_2(self):
        self.wait_loading_finish()
        self.sleep(1)
        self.type(LotteryGamePageLocator.old_other_brand_input_default_ball, "1")
        self.wait_loading_finish()
        self.sleep(1)
        record = self._add_order_and_betting()

        return record

    def _getrecord(self, period):
        self.wait_loading_finish()
        record_list={'period':'','type':'','num':'','money':''}
        record_list['period']=period
        record_list['type']=(self.get_text(LotteryGamePageLocator.record_type)).replace(']', '] -').replace('\n', ' [共1注]')
        record_list['money']=(self.get_text(LotteryGamePageLocator.record_AMOUNT)+' '+self.get_text(LotteryGamePageLocator.record_money))

        return record_list

    def _getrecord_new(self, period):
        self.wait_loading_finish()
        record_list = {'period':'', 'type':'', 'num':'', 'money':''}
        record_list['period']=period
        record_list['type'] = (self.get_text(LotteryGamePageLocator.record_type_new)).replace(']', '] -') + ' [共1注]'
        record_list['num'] = (self.get_text(LotteryGamePageLocator.record_num_new))
        record_list['money'] = (self.get_text(LotteryGamePageLocator.record_amount_new) + ' ' + self.get_text(LotteryGamePageLocator.record_money_new))

        return record_list

    def image_check(self, Lottery):
        X, Y = 0, 0
        
        if platform.system() == 'Linux': 
            self.wait_loading_finish()
            self.sleep(3)
                
            # 資料夾如果有兩層分類可使用
            # dir_path = f'{os.path.split(os.path.realpath(__file__))[0]}/lottery_num_image/{Lottery}/'
            # dir_path = '{0}/image/wap/lottery/{1}/'.format(os.path.split(os.path.realpath(__file__))[0], Lottery)
            folder_path = os.path.abspath(__file__).split('\Project')[0]
            dir_path = "{0}/image/wap/lottery/{1}".format(folder_path, Lottery)

            items = os.listdir(dir_path)
            newlist = []

            for names in items:
                if names.endswith(".png"):
                    newlist.append(names)

            # 圖形辨識
            for _ in range(0,len(newlist)):
                image_path = f"{dir_path}{Lottery}.png".format(dir_path, Lottery)

                for _ in range(0,3):
                    try:
                        X, Y = self.image_search(image_path, 0.3) #  精準度最高為1
                        if X != 0 and Y != 0:
                            break           
                    except:
                        self.sleep(1)

                assert X != 0 and Y != 0,'網頁找不指定圖片 X: {0} Y: {1}'.format(X, Y)

    def check_manual_aa(self, stock):
        self.wait_loading_finish()

        self.click(LotteryGamePageLocator.stock_manual)
        if self.is_element_finded(LotteryGamePageLocator.stock_manual_point) is True:
            pass
        else:
            print(f'{stock}... 說明有誤')
        
        self.click(LotteryGamePageLocator.back)

    def into_stock_index(self, game_xpath, stock ,frequency):
        self.wait_loading_finish()
        self.click(LotteryGamePageLocator.stock_freq(self, frequency))
        self.wait_loading_finish()
        stock_change_out = self.get_text(LotteryGamePageLocator.get_change_out(self, stock))

        for _ in range(0, 2):
            try:
                self.click(game_xpath)
                break
            except:
                self.scroll_bottom_java()
                pass
        self.wait_loading_finish()
        stock_change_in = self.get_text(LotteryGamePageLocator.get_change_in)

        assert stock_change_in == stock_change_out , f'開獎漲跌幅錯誤  首頁顯示: {stock_change_out}, 股指頁顯示: {stock_change_in}'

    def check_periods_aa(self, num, stock_name):
        time_aa = datetime.datetime.now().strftime("%H%M")
        if stock_name == 'hkhszs':  #香港股指開獎時間 9:30 ~ 16:00
            if int(time_aa) < 930 or int(time_aa) > 1600:
                return
        elif stock_name == 'btcusd':  #比特幣 開獎24小時 第一期00:05
            pass
        elif int(time_aa) < 930 or int(time_aa) > 1500:  #中國股指開獎時間 9:30 ~ 15:00
            return

        for loop in range(1, 4):
            self.wait_loading_finish()

            if self.is_element_finded(LotteryGamePageLocator.stock_report) is False:
                self.wait_loading_finish()
                self.click(LotteryGamePageLocator.stock_report_button)
                self.wait_loading_finish()
                self.click(LotteryGamePageLocator.stock_result)
                    
            current_period = self.get_text(LotteryGamePageLocator.current_period_new)  #當前期數
            last_period = self.get_text(LotteryGamePageLocator.last_period_new)  #上期期數
            now_period = self.get_text(LotteryGamePageLocator.next_period_aa)  #下期期數

            if current_period != '' and last_period != '' and now_period !='':
                break
            if loop == 2:
                raise Exception(f'抓取期數錯誤: {loop} 次 最新期數: {current_period}  上一期期數: {last_period}')

            self.sleep(5)
            self.refresh_browser()
        
        next_period = int(now_period) - int(current_period)
        if next_period >= 500 :
            pass
        else:    
            assert next_period <= int(num), f"未開盤期數不正確 已開:{current_period} 未開:{now_period} 期數差: {next_period}"

    def stock_tab(self, van):
        self.wait_loading_finish()
        self.refresh_browser()
        if van == 1:
            self.click(LotteryGamePageLocator.stock_tab_1)
        elif van == 2:
            self.click(LotteryGamePageLocator.stock_tab_2)

    @retry(stop_max_attempt_number=4, wait_fixed=3000)
    def stock_game(self):
        '''點擊任一該頁面可下注的'''
        self.wait_loading_finish()
        # 計算第一區彩球的數量
        
        wager = random.randint(1, 10)
        all_ball = self.find_elements(LotteryGamePageLocator.bet_ball_new)
        bet_ball_num = random.randint(0, len(all_ball))
        if bet_ball_num > 10:
            bet_ball_num = random.randint(0, 10)
        bet_ball = all_ball[bet_ball_num]

        self.click_by_dom(bet_ball)
        bet_ball_text = self.get_text_by_dom(bet_ball).split('\n')[0]

        self.type(LotteryGamePageLocator.wager_input_box_new, wager)
        self.click(LotteryGamePageLocator.bet_button_new)
        self.sleep(1)
        record = self.get_record_new(bet_ball_text)

        self.click(LotteryGamePageLocator.bet_dialog_submit_new)
        self.wait_visibility(LotteryGamePageLocator.stock_bet_ok)
        self.click(LotteryGamePageLocator.stock_bet_ok)

        return record

    def into_shez100_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '深证100'), '深证100', 1)

    def into_hs300_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '沪深300'), '沪深300', 1)

    def into_szzs_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '上证指数'), '上证指数', 1)

    def into_szbqsf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '上证市值百强'), '上证市值百强', 3)

    def into_shez1000sf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '深证1000'), '深证1000', 3)

    def into_szagzssf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '上证A股指数'), '上证A股指数', 3)

    def into_hkhszswf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '香港恒生指数'), '香港恒生指数', 5)

    def into_btcusd_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '比特币'), '比特币', 5)

    def into_szsyzsbf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '上证商业指数'), '上证商业指数', 8)

    def into_shezazbf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '深证A指'), '深证A指', 8)

    def into_cdpshf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '超大盘'), '超大盘', 10)

    def into_kc50shf_stock(self):
        self.into_stock_index(LotteryGamePageLocator.stock_link(self, '科创50'), '科创50', 10)