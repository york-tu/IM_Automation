from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_hm_1_1 = base.data_collation(type_kind='name', type_name='btn_wfpk10_hm_1_1')
    btn_dh1d5 = base.data_collation(type_kind='name', type_name='btn_dh1d5')

    btn_hm = base.data_collation(type_kind='text', type_name='号码')
    btn_hm_1d5 = base.data_collation(type_kind='text', type_name='1-5')
    btn_hm_1st_1 = base.data_collation(type_kind='text', type_name='冠军',action='parent().parent().child()[2].child()')

    btn_hm_6d10 = base.data_collation(type_kind='text', type_name='6-10')
    btn_hm_6st_1 = base.data_collation(type_kind='text', type_name='第六名',action='parent().parent().child()[2].child()')
    
class Pk10(BetLotteryBasePage):

    # 下注 單號1-5 
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dh1d5(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_dh1d5)
        self.common.poco_click(BetLotteryLocator.btn_hm_1_1)
        self.bet_lottery(amount)

    # 下注 號碼1-5 
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_hm1d5(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_hm)
        self.common.poco_click(BetLotteryLocator.btn_hm_1d5)
        self.common.poco_click(BetLotteryLocator.btn_hm_1st_1)
        return self.bet_lottery_napp(amount)

    # 下注 號碼6-10 
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_hm6d10(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_hm)
        self.common.poco_click(BetLotteryLocator.btn_hm_6d10)
        self.common.poco_click(BetLotteryLocator.btn_hm_6st_1)
        return self.bet_lottery_napp(amount)
        
    # 快三全玩法下注
    def bet_pk10_lottery(self,amount,lottery_kind):
        result_list = []
        
        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)
        
        game_dict = {
            'bet_dh1d5': self.bet_dh1d5, 
        }
        
        for game in game_dict.keys():
            self.in_draw()

            try:
                result = game_dict[game](amount)
            except:
                pass

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')

    # PK拾玩法下注
    def bet_pk10_lottery_napp(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()
        
        game_dict = {
            'bet_hm1d5': self.bet_hm1d5, 
            'bet_hm6d10': self.bet_hm6d10,
        }

        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(10)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')
                print(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')