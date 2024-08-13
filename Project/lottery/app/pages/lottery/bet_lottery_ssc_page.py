from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_lm = base.data_collation(type_kind='name', type_name='btn_lm')
    btn_lm_1_BIG = base.data_collation(type_kind='name', type_name='btn_wfssc_lm_1_big')

    btn_lm_napp = base.data_collation(type_kind='text', type_name='两面')
    btn_lm_number = base.data_collation(type_kind='text', type_name='万千百十个')
    btn_lm_wan_big = base.data_collation(type_kind='text', type_name='两面 - 万', action='parent().parent().child()[2].child()')

    btn_lm_zh = base.data_collation(type_kind='text', type_name='总和')
    btn_lm_zh_big = base.data_collation(type_kind='text', type_name='大', num=-1)

    btn_lm_lhh = base.data_collation(type_kind='text', type_name='龙虎和')
    btn_lm_lon = base.data_collation(type_kind='text', type_name='龙')


class Ssc(BetLotteryBasePage):

    # 下注 短牌-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_lm)
        self.common.poco_click(BetLotteryLocator.btn_lm_1_BIG)
        result = self.bet_lottery(amount)

        return result

    # 下注 兩面-萬千百十個
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_number(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lm_napp)
        self.common.poco_click(BetLotteryLocator.btn_lm_number)
        self.common.poco_click(BetLotteryLocator.btn_lm_wan_big)
        result = self.bet_lottery_napp(amount)

        return result

    # 下注 兩面-總和
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lmzh(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lm_napp)
        self.common.poco_click(BetLotteryLocator.btn_lm_zh)
        self.common.poco_click(BetLotteryLocator.btn_lm_zh_big)
        result = self.bet_lottery_napp(amount)

        return result

    # 下注 兩面-龍虎和
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lmlhh(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lm_napp)
        self.common.poco_click(BetLotteryLocator.btn_lm_lhh)
        self.common.poco_click(BetLotteryLocator.btn_lm_lon)
        result = self.bet_lottery_napp(amount)

        return result
        
    # 時時彩全玩法下注
    def bet_ssc_lottery(self,amount,lottery_kind):
        result_list = []
        
        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)

        game_dict = {
            'bet_lm': self.bet_lm, 
        }
        
        for game in game_dict.keys():
            self.in_draw()

            try:
                result = game_dict[game](amount)
            except:
                result = '下注失敗'

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')
    
    # 時時彩全玩法下注
    def bet_ssc_lottery_napp(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()

        game_dict = {
            'bet_lm_number': self.bet_lm_number, 
            'bet_lmzh': self.bet_lmzh,
            'bet_lmlhh': self.bet_lmlhh,
        }
        
        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(10)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')
