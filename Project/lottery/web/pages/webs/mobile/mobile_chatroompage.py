from Project.lottery.web.pages.admin.financialmanagement.admin_bankaccount_page import BankAcconut_PageLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import _find_element
from pages.webs.mobile.mobile_basepage import BasePage
import datetime,os,platform
from retrying import retry

class ChatRoomPageLocator:
    analyst = (By.XPATH, '(//span[@class="stock-user__text"])[last()]')  #分析師
    analysis_name = (By.XPATH, '(//div[@class="header-type"])[last()]')  #分析彩種名稱
    analysis_period = (By.XPATH, '(//div[@class="periods-item__text" and contains(text(),"期")])[last()]')  #分析彩種期數
    analysis_rule = (By.XPATH, '(//div[@class="periods-item__text" and contains(text(),"军")])[last()]')  #分析彩種玩法
    analysis_option = (By.XPATH, '(//div[contains(@class,"periods-item__text ")])[last()]')  #分析彩種選項
    analysis_list = (By.XPATH, '//div[@class="wcr-list__item"]')  #分析篇數
    analysis_time = (By.XPATH, '//span[@class="time-text"]')  #分析時間

    bet_analyst = (By.XPATH, '//span[@class="item-result__text" and contains(text(),"分")]')  #注單推送會員
    bet_name = (By.XPATH, '(//span[@class="item-title__text"])[2]')  #注單股種
    bet_period = (By.XPATH, '//span[@class="item-result__text" and contains(text(),"期")]')  #注單期數
    bet_option = (By.XPATH, '//span[@class="item-result__text" and contains(text(),"军")]')  #注單投資內容
    bet_amount = (By.XPATH, '//div[@class="result-number"]')  #注單下注金額
    bet_input = (By.XPATH, '//input[@class="van-stepper__input"]')  #注單單注金額

    follow_up_button = (By.XPATH, '(//a[@class="stock-btn__item -primary rounded-pill btn-ripple"])[last()]')  #跟投按鍵
    follow_up_submit = (By.XPATH, '//div[@class="add-icon"]/..')  #跟投送出
    follow_up_status = (By.XPATH, '//span[contains(@class,"item-title__text -text-")]')  #跟投狀態
    follow_up_ok = (By.XPATH, '//button[@class="btn btn-primary"]')  #跟投確認按鈕
    follow_up_option = (By.XPATH, '//div[@class="item-result"]')  #跟投內容
    chatroom_back_buttom = (By.XPATH, '//a[@class="return"]')

class ChatRoomPage(BasePage):
    time=datetime.datetime.now()
    today = datetime.date.today()
 
    def check_analysis_amount(self):
        self.wait_loading_finish()
        analysis_list_amount = self.find_elements(ChatRoomPageLocator.analysis_list)
        assert len(analysis_list_amount) == 3, f'聊天室初始分析跟投數量錯誤..只有顯示{analysis_list_amount}則'
    
    def chatroom_back(self):
        self.wait_loading_finish()
        self.click(ChatRoomPageLocator.chatroom_back_buttom)
    
    def check_auto_analysis(self):
        self.wait_loading_finish()

        for _ in range(0, 2):
            try:
                assert len(self.find_elements(ChatRoomPageLocator.analysis_list)) > 3
            except:
                self.sleep(30)
                pass
        
        time_list = [self.get_text(ChatRoomPageLocator.analysis_time).replace(':', '').replace(' PM', '')]
        for i in range(len(time_list)-1):
            T = time_list[i+1] - time_list[i] 
            assert T > 0, '聊天室時間顯示有誤'

        assert self.is_element_finded(ChatRoomPageLocator.follow_up_button) is True, f'聊天室未自動刷新分析'
     
    def check_bet_record(self,money = '10'):
        self.wait_loading_finish()
        
        record = {}
        man = self.get_text(ChatRoomPageLocator.analyst)  #分析師
        name = self.get_text(ChatRoomPageLocator.analysis_name)  #股種
        period = self.get_text(ChatRoomPageLocator.analysis_period).replace('期', '')  #期數
        rule = self.get_text(ChatRoomPageLocator.analysis_rule).replace(' ', '-')  #玩法
        option = self.get_text(ChatRoomPageLocator.analysis_option)  #選項

        bet_man = self.get_text(ChatRoomPageLocator.bet_analyst)  #分析師
        bet_name = self.get_text(ChatRoomPageLocator.bet_name).replace('：', '')  #彩種
        bet_period = self.get_text(ChatRoomPageLocator.bet_period).replace('期', '')  #期數
        bet_option = self.get_text(ChatRoomPageLocator.bet_option)  #玩法選項
        bet_amount = self.get_text(ChatRoomPageLocator.bet_amount)  #金額

        assert bet_man == man, f'推送會員有誤...分析頁面為{man} 投注頁面為{bet_man}'
        assert bet_name == name, f'跟投股種有誤...分析頁面為{name} 投注頁面為{bet_name}'
        assert bet_period == period, f'跟投期數有誤...分析頁面為{period} 投注頁面為{bet_period}'
        assert bet_option == rule + '-' + option, f'跟投內容有誤...'
        assert bet_amount == money, f'投注金額有誤... 投注金額應為{money} 現在為{bet_amount}'

        record['analyst'] = f'{bet_man}'
        record['name'] = f'{bet_name}'
        record['period'] = f'{bet_period}'
        record['type'] = f'{rule}'
        record['money'] = f'1注 {bet_amount}元'
        record['opiton'] = f'{option}'

        return record
    
    def follow_up(self,money = '10'):
        self.wait_loading_finish()

        for _ in range(0, 2):
            try:
                if self.is_element_finded(ChatRoomPageLocator.follow_up_button) is True:
                    self.click(ChatRoomPageLocator.follow_up_button)

                    record = {}
                    self.type(ChatRoomPageLocator.bet_input,money)
                    record = self.check_bet_record(money)
                    self.click(ChatRoomPageLocator.follow_up_submit)
                    assert self.get_text(ChatRoomPageLocator.follow_up_status) == '成功订单', f'嘗試兩次投注失敗...'

                    self.click(ChatRoomPageLocator.follow_up_ok)

                    return record   
            except:
                self.sleep(5)
                pass