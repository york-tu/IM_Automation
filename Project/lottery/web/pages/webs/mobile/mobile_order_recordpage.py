from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import datetime
import time, re

class GameRecordLocator:
    # 注單紀錄
    first_order = (By.XPATH, '//div[@style="--order-item:1;"][1]')
    order_detail_arrow = (By.XPATH, '//div[@class="order-info__status__arrow"]')
    order_detail = (By.XPATH, '//div[@style="--order-item: 1;"][1]//li[@class="result-list__item"]') # 第一筆注單的注單詳情
    order_detail_lottery = (By.XPATH, '(//div[@class="order-list__item order-list__item--open"]//li[@class="result-list__item"])[1]')  # 注單詳情 彩種
    order_detail_lottery_money = (By.XPATH, '(//div[@class="order-list__item order-list__item--open"]//li[@class="result-list__item"])[2]')  # 注單詳情 金額
    amount = (By.XPATH, "//div[@class='list__text__result' and contains(text(),'注')]")  # 金額
    status = (By.XPATH,"//div[@class='badge__text']") # 狀態
    today = (By.XPATH, "//li[@class='select_2']//select[contains(@data-bind,'time')]")  #今日
    nwap_today = (By.XPATH, "//span[text()='本日']")  #本日
    nwap_week = (By.XPATH, "//span[text()='本周']")  #本周
    game_type = (By.XPATH, "(//span[@class='order-info__status__name'])[1]")  # 彩種
    game_all_type = (By.XPATH, "//span[@class='order-info__status__name']")  # 彩種
    time = (By.XPATH, "//h4[@class='order-head']")  # 時間
    ticket_game_number = (By.XPATH, "//div[contains(text(),'期(局)号')]/..//div[@class='content__item']")  # 期號
    ticket_number = (By.XPATH, "//div[contains(text(),'单号')]/..//div[@class='content__item']") #單號
    win_lost = (By.XPATH,"//div[@class='list__text__title' and contains(text(),'输赢：')]/../div[2]")    # 輸贏 
    payout = (By.XPATH,"//div[@class='list__text__title' and contains(text(),'派彩：')]/../div[2]")    # 派彩
    rebate = (By.XPATH,"//div[@class='list__text__title' and contains(text(),'返水：')]/../div[2]")      # 返水
    # 彩票選單
    nwap_picker_lottery = (By.XPATH, "//div[@class='van-ellipsis' and (text()='彩票' or text()='指数')]")  # 彩票按鈕
    button_select = (By.XPATH, "//li[@class='select_1']//select[contains(@data-bind,'producttype')]")  # 投注記錄下拉選單
    picker_red_nwap = (By.XPATH, "//div[@class='van-ellipsis' and contains(text(),'红包')]")  # 紅包按鈕
    picker_nwap = (By.XPATH, "//input[@class='order-select__sel']")
    nwap_picker_submit = (By.XPATH, "//button[text()='确定']")
    # AA股止注單類型
    autonomy_stock = (By.XPATH, "//span[contains(text(),'自行下注')]")  # 自行下注按鈕
    follow_stock = (By.XPATH, "//span[contains(text(),'专家跟投')]")  # 跟投按鈕
    hosting_stock = (By.XPATH, "//span[contains(text(),'理财托管')]")  # 托管按鈕

    total_record_nwap = (By.XPATH, "//div[@class='order-list__item']")
    ticket_effect_bet_nwap = (By.XPATH, "//div[contains(text(),'有效投注：')]/..//div[@class='list__text__result']")

class GameRecord(BasePage):
    # 將 DOM 定位list 轉為text list
    def get_text_by_dom_list(self, dom_list):
        self.wait_loading_finish()                       
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text
    
    #彩票記錄頁面比對
    def game_lottery(self, record):
        
        self.wait_loading_finish()
        self.sleep(1)
        if self.is_element_finded(GameRecordLocator.button_select) == False:
            for counter in range(1, 4):
                if self.is_element_finded(GameRecordLocator.button_select) == False:
                    self.sleep(1)
                    print("彩票按鈕第 {0} 次未找到".format(counter))
                elif self.is_element_finded(GameRecordLocator.button_select) == True:
                    break
                break

        self.sleep(3)
        assert self.is_element_finded(GameRecordLocator.button_select) == True, "彩票按鈕無法點擊選擇"
        
        self.select_by_text(GameRecordLocator.button_select, '彩票')
        self.wait_loading_finish()
        self.select_by_text(GameRecordLocator.today, '本日')
        self.wait_loading_finish()
        self.click(GameRecordLocator.order_detail_arrow)

        self.wait_visibility(GameRecordLocator.order_detail_lottery)
        handicap = self.get_text(GameRecordLocator.order_detail_lottery).replace(' \n', '').replace('\n', '')
        subject = self.get_text(GameRecordLocator.order_detail_lottery_money)
        subject_1 = subject[:subject.index('@')]
        detail = handicap+subject_1
        ticketname = self.get_text(GameRecordLocator.ticket_number)
        period = self.get_text(GameRecordLocator.ticket_game_number)
        money = self.get_text(GameRecordLocator.amount)
        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(int(datetime.datetime.now().strftime('%m')))
        day = str(datetime.datetime.now().strftime('%d'))
        nowtime = f'{year} 年 {month}月{day}日'
        time = self.get_text(GameRecordLocator.time)[:-9]
        status = self.get_text(GameRecordLocator.status)

        assert time == nowtime, f'投注紀錄時間錯誤 當下時間: {nowtime}, 投注記錄時間: {time}'
        assert period == record['period'], f'期數錯誤 投注紀錄 -> {period}，下注資料 -> {record["period"]}'
        assert money.replace('【', '').replace('】', ' ').__contains__(record['money'][:-1]), '下單金額不正確'
        assert detail.__contains__(record['type']), f'注單詳情資料錯誤 投注紀錄: {detail}  投注頁面: {record["type"]}'

        if self.get_text(GameRecordLocator.win_lost) == '':
            assert status == '待结算','投注狀態不正確 狀態:{0}'.format(status)
        else:
            assert str(status).__contains__('已结算'),'投注狀態不正確 狀態:{0}'.format(status)

        self.back()
        self.wait_loading_finish()
        record = {'money':record['money'].split(' ')[1].replace('元', ''), 'ticket_name':ticketname, 'period':period, 'type':detail}
        return record
    
    #天天麻將 彩票記錄頁面比對 & 回傳注單資料
    def game_lottery_nwap(self, record):
        self.wait_loading_finish()
        self.click(GameRecordLocator.picker_nwap)
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_picker_lottery)
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_picker_submit)
        self.wait_loading_finish()
        for _ in range(0,4):
            self.click(GameRecordLocator.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(GameRecordLocator.game_type) is True:
                assert record['name'].__contains__(self.get_text(GameRecordLocator.game_type))
                break
            else:
                self.click(GameRecordLocator.nwap_week)
                self.sleep(10)
        
        self.click(GameRecordLocator.order_detail_arrow)

        self.wait_visibility(GameRecordLocator.order_detail_lottery)
        handicap = self.get_text(GameRecordLocator.order_detail_lottery).replace(' \n', '').replace('\n', '')
        subject = self.get_text(GameRecordLocator.order_detail_lottery_money)
        subject_1 = subject[:subject.index('@')]
        detail_wap = handicap+subject_1
        detail = subject + handicap
        ticketname = self.get_text(GameRecordLocator.ticket_number)
        period = self.get_text(GameRecordLocator.ticket_game_number)
        money = self.get_text(GameRecordLocator.amount)
        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(int(datetime.datetime.now().strftime('%m')))
        day = str(datetime.datetime.now().strftime('%d'))
        nowtime = f'{year} 年 {month}月{day}日'  # 整理時間格式 到前台比對
        _time = f'{year}-{month}-{day}'     # 整理時間格式 到後台比對
        time = self.get_text(GameRecordLocator.time)[:-9]
        status = self.get_text(GameRecordLocator.status)

        assert time == nowtime, f'投注紀錄時間錯誤 當下時間: {nowtime}, 投注記錄時間: {time}'
        assert period == record['period'], f'期數錯誤 投注紀錄 -> {period}，下注資料 -> {record["period"]}'
        assert money.replace('【', '').replace('】', ' ').__contains__(record['money'][:-1]), '下單金額不正確'
        assert detail_wap.__contains__(record['type']), f'注單詳情資料錯誤 投注紀錄: {detail}  投注頁面: {record["type"]}'
        
        if self.get_text(GameRecordLocator.win_lost) == '':
            assert status == '待结算','投注狀態不正確 狀態:{0}'.format(status)
        else:
            assert str(status).__contains__('已结算'),'投注狀態不正確 狀態:{0}'.format(status)
        
        self.back()
        self.wait_loading_finish()
        record = {'money':record['money'].split(' ')[1].replace('元', ''), 'ticket_name':ticketname, 'period':period, 'type':detail, 'time':_time}
        return record

    # AA切換股指住單來源 Teb.
    def switch_stock_order_type(self, order_type):
        self.wait_loading_finish()
        if order_type == 1:
            self.click(GameRecordLocator.follow_stock)
        elif order_type == 2:
            self.click(GameRecordLocator.hosting_stock)

    # 將 DOM 定位list 轉為text list
    def get_text_list_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text
        
    # 比對前台紅包注單 & 回傳注單資料
    def check_record_front_end(self, record):
        self.wait_loading_finish()
        self.select_by_text(GameRecordLocator.button_select, record['game_name'])
        self.wait_loading_finish()
        self.click(GameRecordLocator.today)
        self.wait_loading_finish()

        self.click(GameRecordLocator.order_detail_arrow)
        # detail_list = ''
        detail = self.get_text(GameRecordLocator.order_detail_lottery).replace(' \n', '').replace('\n', '')
        ticket_number = self.get_text(GameRecordLocator.ticket_number)
        period = self.get_text(GameRecordLocator.ticket_game_number)
        money = (self.get_text(GameRecordLocator.amount)).split('】')[-1]
        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(int(datetime.datetime.now().strftime('%m')))
        day = str(datetime.datetime.now().strftime('%d'))
        nowtime = f'{year} 年 {month}月{day}日'
        time = self.get_text(GameRecordLocator.time)[:-9]
        status = self.get_text(GameRecordLocator.status)

        # for detail in self.get_text_list_by_dom_list(self.find_elements(GameRecordLocator.order_detail)):
            # detail_list += detail

        assert time == nowtime, f'投注紀錄時間錯誤 當下時間: {nowtime}, 投注記錄時間: {time}'
        assert str(money).__contains__(str(record['amount'])), f'下單金額錯誤 ... {money} 應為-> {record["amount"]}'

        if self.get_text(GameRecordLocator.win_lost) == '':
            assert status == '待结算','投注狀態不正確 狀態:{0}'.format(status)
        else:
            assert str(status).__contains__('已结算'),'投注狀態不正確 狀態:{0}'.format(status)

        record = {'amount':money, 'ticket_number':ticket_number, 'period':period, 'detail': detail}
        return record


    def check_record_front_end_nwap(self, record):
        self.wait_loading_finish()
        self.click(GameRecordLocator.picker_nwap)
        self.wait_loading_finish()
        self.click(GameRecordLocator.picker_red_nwap)
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_picker_submit)
        self.wait_loading_finish()
        for _ in range(0,3):
            self.click(GameRecordLocator.nwap_today)
            self.wait_loading_finish() 
            if self.is_element_finded(GameRecordLocator.game_type) is True:
                assert record['name'].__contains__(self.get_text(GameRecordLocator.game_type))
                break
            else:
                self.click(GameRecordLocator.nwap_week)
                self.sleep(10)

        self.click(GameRecordLocator.order_detail_arrow)
        
        detail = self.get_text(GameRecordLocator.order_detail_lottery).replace(' \n', '').replace('\n', '')
        ticket_number = self.get_text(GameRecordLocator.ticket_number)
        money = (self.get_text(GameRecordLocator.amount)).split('】')[-1]
        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(int(datetime.datetime.now().strftime('%m')))
        day = str(datetime.datetime.now().strftime('%d'))
        nowtime = f'{year} 年 {month}月{day}日'
        time = self.get_text(GameRecordLocator.time)[:-9]
        status = self.get_text(GameRecordLocator.status)
        period = self.get_text(GameRecordLocator.ticket_game_number)
        
        assert time == nowtime, f'投注紀錄時間錯誤 當下時間: {nowtime}, 投注記錄時間: {time}'
        assert str(money).__contains__(str(record['amount'])), f'下單金額錯誤 ... {money} 應為-> {record["amount"]}'
        
        if self.get_text(GameRecordLocator.win_lost) == '':
            assert status == '待结算','投注狀態不正確 狀態:{0}'.format(status)
        else:
            assert str(status).__contains__('已结算'),'投注狀態不正確 狀態:{0}'.format(status)
        
        self.back()
        self.wait_loading_finish()
        record = {'amount':money, 'ticket_number':ticket_number, 'period':period, 'detail':detail}
        return record
    
    # 把狀態欄位整理成 dict
    def sort_out_status(self):
        status_dict = {}
        status_keys = ['status', 'payout', 'win_lose', 'rebate']
        status_keys_index = 0
        status_detail_list = []

        status_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.status))
        payout_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.payout))
        win_lost_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.win_lost))
        rebate_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.rebate))
        
        for i in range(len(status_list)):
            if status_list[i]=='':
                break
            status_detail_list.append(dict(zip(status_keys,(status_list[i],payout_list[i],win_lost_list[i],rebate_list[i]))))
            if status_detail_list[i]['status'] == '待结算':
                status_detail_list[i]=status_detail_list[i]['status']

        return status_detail_list
    

    def get_nwap_record_detail(self):
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_today)
        self.wait_loading_finish()
        self.click(GameRecordLocator.picker_nwap)
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_picker_lottery)
        self.wait_loading_finish()
        self.click(GameRecordLocator.nwap_picker_submit)
        self.wait_loading_finish()
        self.sleep(2)

        for _ in range(0,3):
            self.click(GameRecordLocator.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(GameRecordLocator.game_type) is True:
                break
            else:
                self.click(GameRecordLocator.nwap_week)
                self.sleep(10)
        '''
            取得前台注單詳情
            回傳格式:
                all_record = [
                    {
                        "ticket_name": 彩種 str, 
                        "ticket_period": 期數 str, 
                        "ticket_number": 單號 str,
                        "bets": 投注數 str, 
                        "money": 金額 str, 
                        "effectBet": 有效投注 str, 
                        "status": 狀態 "投注成功" 或 dict {'payout' : float, 'win_lose' : float, 'rebate' : float}
                    }
                ]
        '''
        assert self.is_element_finded(GameRecordLocator.total_record_nwap) is True, "投注紀錄為空"
        total_record = self.find_elements(GameRecordLocator.total_record_nwap)
        total_record_1 = len(total_record)+1

        bets_list= []
        detail_money_list = []
        all_record = []

        for i in range(1):

            # 整理狀態的資料
            ticket_status_list = self.sort_out_status()  #注單狀態  含payout、win_lose、rebate
            ticket_number_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.ticket_number))  #投注單號
            ticket_name_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.game_all_type))  #投注彩種
            ticket_period_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.ticket_game_number))  #投注期數
            effect_bet_list = self.get_text_by_dom_list(self.find_elements(GameRecordLocator.ticket_effect_bet_nwap))  #有效投注
                    
            for element in self.get_text_by_dom_list(self.find_elements(GameRecordLocator.amount)):
                element_1 = element.replace('【','')
                table_text = re.split('】', element_1)
                bets_list.append(table_text[0])
                # 取得投注金額
                detail_money_list.append(table_text[1])

            for index in range(len(total_record)):
                record = {"ticket_name": ticket_name_list[index], 
                        "ticket_period": ticket_period_list[index],
                        "ticket_number": ticket_number_list[index],
                        "bets": bets_list[index],
                        "money": detail_money_list[index],
                        "effectBet": effect_bet_list[index], 
                        "status": ticket_status_list[index],
                        }
                all_record.append(record)
        
        return all_record
