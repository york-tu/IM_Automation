from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime
import re

class GameRecord(BasePage):
    # 注單紀錄
    order_detail = (By.XPATH, "(//ul[@class='result-list'][1]/li[@class='result-list__item'])[1]")  # 注單詳情 彩種
    order_detail_money = (By.XPATH, "(//ul[@class='result-list'][1]/li[@class='result-list__item'])[2]")  # 注單詳情 金額
    # order_detail = (By.XPATH, '(//div[contains(@data-bind, "foreach: productresult.play")])[1]/span')

    order_money = (By.XPATH, "//td[contains(text(),'注')]")  # 金額
    order_detail_result = (By.XPATH,"(//tr[1]/td[6])[1]") # 狀態
    today = (By.XPATH, "//*[@class='top-nav-right']/a[text()='今天']")  #今日    
    This_week = (By.XPATH, "//*[@class='top-nav-right']/a[text()='本周']")  # 本周
    periods = (By.XPATH, "//tr[1]/td[2]/span[2]")  # 期數
    time = (By.XPATH, "//tr[1]/td[1]/span[2]")  # 時間
    ticket_num = (By.XPATH, "//tr[1]/td[1]/span[1]")  # 單號
    effective_bet = (By.XPATH,"(//tr[1]/td[5])[1]") # 有效投注
    
    order_status_detail = (By.XPATH, "//p[@class='error']/..")      # 所有注單狀態
    ticket_number = (By.XPATH, "//tr/td[1]/span[1]")                # 所有注單單號
    ticket_productname = (By.XPATH, "//tr/td[2]/span[1]")           # 所有注單彩種
    ticket_productperiod = (By.XPATH, "//tr/td[2]/span[2]")         # 所有注單期數
    detail_money = (By.XPATH, "//td[contains(text(),'注')]")        # 所有注單期數
    effect_bet = (By.XPATH, "//div[@class='product-result-content__scroll order -v2-ttmj']/../../td[5]")    # 所有注單有效投注
    total_record_xpath = (By.XPATH, "//span[contains(@class, 'pager_total')]")
    
    # 彩票
    lotterybtn=(By.XPATH, "//li[@class='active' and text()='彩票']")  # 彩票按鈕


    def game_lottery(self,record):
        self.wait_loading_finish()
        self.click(GameRecord.lotterybtn)
        self.wait_loading_finish()
        self.click(GameRecord.today)

        ticket_name=str(self.get_text(GameRecord.ticket_num))
        period=self.get_text(GameRecord.periods)
        _type =self.get_text(GameRecord.order_detail_money)
        money=str(self.get_text(GameRecord.order_money))
        now_time=datetime.datetime.now().strftime('%Y-%m-%d')
        time=self.get_text(GameRecord.time)[:-9]
        status=self.get_text(GameRecord.order_detail_result)

        for detail in self.find_elements(GameRecord.order_detail):
            _type += self.get_text_by_dom(detail)

        assert time==now_time,'投注紀錄時間不正確'
        assert period==record['period'],'期數不正確'
        assert money==record['money'][:-1],'下單金額不正確'
        
        if self.get_text(GameRecord.effective_bet) == '0':
            assert status=='投注成功','投注狀態不正確 狀態:{0}'.format(status)
        else:
            assert status=='已结算','投注狀態不正確 狀態:{0}'.format(status)

        self.back()
        money = (money.split(']'))[1].lstrip()
        record = {'ticket_name':ticket_name,'period':period,'type':_type, 'time': time,'money': money}
        return record

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    # 將 DOM 定位list 轉為text list
    def get_text_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    # 把狀態欄位整理成 dict
    def sort_out_status(self):
        status_dict = {}
        status_keys = ['payout', 'win_lose', 'rebate']
        status_keys_index = 0
        status_detail_list = []

        for table_text in self.get_text_by_dom_list(self.find_elements(GameRecord.order_status_detail)):        
            if(table_text == "" or table_text == "投注成功"):
                table_text = "投注成功"
                # table_text = status_for_notyet_list.pop(0)
                status_detail_list.append(table_text)
            table_text = re.split('\\n|： |：',table_text)
            for i in range(len(table_text)):
                if self.is_float(table_text[i]):
                    status_dict.update({'{}'.format(status_keys[status_keys_index]): float(table_text[i])})
                    status_keys_index += 1
                    status_keys_index %= 3
                if len(status_dict) == 3:
                    status_detail_list.append(status_dict)
                    status_dict = {}  

        return status_detail_list      

    def get_game_record_detail(self):
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
        self.wait_loading_finish()

        total_record = self.get_text(GameRecord.total_record_xpath)                                                              # 總紀錄數
        assert total_record != '', "投注紀錄為空"
        total_record = int(total_record)

        # 資料筆數為 25 的倍數時，總頁數為 資料數//25，反之，則為 資料數//25+1
        page_total = total_record // 25 + 1 if total_record % 25 else total_record // 25

        bets_list= []
        detail_money_list = []
        all_record = []

        for i in range(page_total):            
            
            if i > 0:
                self.click((By.XPATH, f"//a[contains(@data-bind, 'text: label') and text()='{i+1}']"))
                self.wait_loading_finish()

            # 整理狀態的資料
            status_detail_list = self.sort_out_status()
            ticket_number_list = self.get_text_by_dom_list(self.find_elements(GameRecord.ticket_number))
            ticket_productname_list = self.get_text_by_dom_list(self.find_elements(GameRecord.ticket_productname))
            ticket_productperiod_list = self.get_text_by_dom_list(self.find_elements(GameRecord.ticket_productperiod))
            effect_bet_list = self.get_text_by_dom_list(self.find_elements(GameRecord.effect_bet))

            for element in self.get_text_by_dom_list((self.find_elements(GameRecord.detail_money))):
                table_text = re.split(' ', element)
                bets_list.append(table_text[0])
                # 取得投注金額
                detail_money_list.append(table_text[1])
            
            for index in range(len(status_detail_list)):
                record = {"ticket_name": ticket_productname_list[index], 
                        "ticket_period": ticket_productperiod_list[index],
                        "ticket_number": ticket_number_list[index],
                        "bets": bets_list[index],
                        "money": detail_money_list[index],
                        "effectBet": effect_bet_list[index], 
                        "status": status_detail_list[index],
                        }
                all_record.append(record)
        
        return all_record
        