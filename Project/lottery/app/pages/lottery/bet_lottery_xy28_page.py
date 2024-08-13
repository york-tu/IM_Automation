from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_tm_HM = base.data_collation(type_kind='name', type_name='btn_tm_hm')
    btn_tm_HM_0 = base.data_collation(type_kind='name', type_name='btn_twxy28_tm_hm_0')

    bet_lm = base.data_collation(type_kind='text', type_name='两面')
    bet_lm_big = base.data_collation(type_kind='text', type_name='大')

    bet_sp = base.data_collation(type_kind='text', type_name='色波')
    bet_sp_green = base.data_collation(type_kind='text', type_name='绿波')

    bet_special = base.data_collation(type_kind='text', type_name='特殊')
    bet_leopard = base.data_collation(type_kind='text', type_name='豹子')

    bet_tm = base.data_collation(type_kind='text', type_name='特码')
    bet_tmhm = base.data_collation(type_kind='text', type_name='号码')
    bet_tm_hm_0 = base.data_collation(type_kind='text', type_name='00', num=-1)

    bet_tmb3 = base.data_collation(type_kind='text', type_name='包三')
    bet_tm_b3_0 = base.data_collation(type_kind='text', type_name='00', num=-1)
    bet_tm_b3_1 = base.data_collation(type_kind='text', type_name='01', num=-1)
    bet_tm_b3_2 = base.data_collation(type_kind='text', type_name='02', num=-1)
    
class Xy28(BetLotteryBasePage):

    # 下注 短牌-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tm_hm(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tm_HM)
        self.common.poco_click(BetLotteryLocator.btn_tm_HM_0)
        self.bet_lottery(amount)
    
    # 下注 兩面
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.bet_lm)
        self.common.poco_click(BetLotteryLocator.bet_lm_big)
        return self.bet_lottery_napp(amount)

    # 下注 色波
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_sp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.bet_sp)
        self.common.poco_click(BetLotteryLocator.bet_sp_green)
        return self.bet_lottery_napp(amount)
        
    # 下注 特殊
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_special(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.bet_special)
        self.common.poco_click(BetLotteryLocator.bet_leopard)
        return self.bet_lottery_napp(amount)

    # 下注 特碼-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tm_hm_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.bet_tm)
        self.common.poco_click(BetLotteryLocator.bet_tmhm)
        self.common.poco_click(BetLotteryLocator.bet_tm_hm_0)
        return self.bet_lottery_napp(amount)

    # 下注 特碼-包三
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tm_b3(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.bet_tm)
        self.common.poco_click(BetLotteryLocator.bet_tmb3)
        self.common.poco_click(BetLotteryLocator.bet_tm_b3_0)
        self.common.poco_click(BetLotteryLocator.bet_tm_b3_1)
        self.common.poco_click(BetLotteryLocator.bet_tm_b3_2)
        return self.bet_lottery_napp(amount)

    # 幸運28全玩法下注
    def bet_xy28_lottery(self,amount,lottery_kind):
        result_list = []

        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)

        game_dict = {
            'bet_tm_hm': self.bet_tm_hm,
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

    # 幸運28全玩法下注
    def bet_xy28_lottery_napp(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()
        
        game_dict = {
            'bet_lm': self.bet_lm,
            'bet_sp': self.bet_sp,
            'bet_special': self.bet_special,
            'bet_tm_hm': self.bet_tm_hm_napp,
            'bet_tm_b3': self.bet_tm_b3,
        }

        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(15)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')