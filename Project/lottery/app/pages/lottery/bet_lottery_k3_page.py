from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_lm = base.data_collation(type_kind='name', type_name='btn_lm')
    btn_lm_ODD = base.data_collation(type_kind='name', type_name='btn_lm_odd')
    btn_ds = base.data_collation(type_kind='name', type_name='btn_ds')
    btn_ds_4 = base.data_collation(type_kind='name', type_name='btn_ds_4')
    btn_sj = base.data_collation(type_kind='name', type_name='btn_sj')
    btn_sj_1 = base.data_collation(type_kind='name', type_name='btn_sj_1')
    btn_sz = base.data_collation(type_kind='name', type_name='btn_sz')
    btn_sz_1 = base.data_collation(type_kind='name', type_name='btn_sz_1')
    btn_cp = base.data_collation(type_kind='name', type_name='btn_cp')
    btn_cp_1_2 = base.data_collation(type_kind='name', type_name='btn_cp_1_2')
    btn_dp = base.data_collation(type_kind='name', type_name='btn_dp')
    btn_dp_1 = base.data_collation(type_kind='name', type_name='btn_dp_1')

    # --------------------------------新版---------------------------------------------
    btn_lm_napp = base.data_collation(type_kind='text', type_name='两面')
    btn_lm_odd = base.data_collation(type_kind='text', type_name='单', num=-1)

    btn_ds_napp = base.data_collation(type_kind='text', type_name='点数')
    btn_ds_04 = base.data_collation(type_kind='text', type_name='04')

    btn_sj_napp = base.data_collation(type_kind='text', type_name='三军')
    btn_sj_1_napp = base.data_collation(pos= [0.18,0.32])       # 骰子圖沒定位可以抓

    btn_wz = base.data_collation(type_kind='text', type_name='围骰/全骰')
    btn_wz_quz = base.data_collation(type_kind='text', type_name='全骰', num=-1)

    btn_cp_napp = base.data_collation(type_kind='text', type_name='长牌')
    btn_cp_1_2_napp = base.data_collation(pos= [0.18,0.32])

    btn_dp_napp = base.data_collation(type_kind='text', type_name='短牌')
    btn_dp_1_1 = base.data_collation(pos= [0.18,0.32])

class K3(BetLotteryBasePage):

    # 下注 兩面-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_lm)
        self.common.poco_click(BetLotteryLocator.btn_lm_ODD)
        return self.bet_lottery(amount)

    # 下注 點數-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_ds(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_ds)
        self.common.poco_click(BetLotteryLocator.btn_ds_4)
        return self.bet_lottery(amount)

    # 下注 三軍-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_sj(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_sj)
        self.common.poco_click(BetLotteryLocator.btn_sj_1)
        return self.bet_lottery(amount)

    # 下注 全骰-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_sz(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_sz)
        self.common.poco_click(BetLotteryLocator.btn_sz_1)
        return self.bet_lottery(amount)

    # 下注 長牌-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_cp(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_cp)
        self.common.poco_click(BetLotteryLocator.btn_cp_1_2)
        return self.bet_lottery(amount)

    # 下注 短牌-單
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dp(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_dp)
        self.common.poco_click(BetLotteryLocator.btn_dp_1)
        return self.bet_lottery(amount)
        
    # 快三全玩法下注
    def bet_k3_lottery(self,amount,lottery_kind):
        result_list = []
        
        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)
        
        game_dict = {
            'bet_cp': self.bet_cp, 
            'bet_ds': self.bet_ds,
            'bet_dp': self.bet_dp,
            'bet_sj': self.bet_sj, 
            'bet_sz': self.bet_sz,
            'bet_lm': self.bet_lm,
        }
        
        for game in game_dict.keys():
            self.in_draw()

            try:
                result = game_dict[game](amount)
            except:
                result = '下注出錯'

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')

    # ----------------------------新版-----------------------------

    # 下注 兩面
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lm_napp)
        self.common.poco_click(BetLotteryLocator.btn_lm_odd)
        return self.bet_lottery_napp(amount)

    # 下注 點數
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_ds_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_ds_napp)
        self.common.poco_click(BetLotteryLocator.btn_ds_04)
        return self.bet_lottery_napp(amount)

    # 下注 三軍
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_sj_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_sj_napp)
        self.common.poco_click(BetLotteryLocator.btn_sj_1_napp)
        return self.bet_lottery_napp(amount)

    # 下注 圍骰/全骰
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_wz_quz(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_wz)
        self.common.poco_click(BetLotteryLocator.btn_wz_quz)
        return self.bet_lottery_napp(amount)

    # 下注 長牌
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_cp_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_cp_napp)
        self.common.poco_click(BetLotteryLocator.btn_cp_1_2_napp)
        return self.bet_lottery_napp(amount)

    # 下注 短牌
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dp_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_dp_napp)
        self.common.poco_click(BetLotteryLocator.btn_dp_1_1)
        return self.bet_lottery_napp(amount)


    # 快三全玩法下注
    def bet_k3_lottery_napp(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()
        
        game_dict = {
            'bet_lm_napp': self.bet_lm_napp, 
            'bet_ds_napp': self.bet_ds_napp,
            'bet_sj_napp': self.bet_sj_napp,
            'bet_wz_quz': self.bet_wz_quz, 
            'bet_cp_napp': self.bet_cp_napp,
            'bet_dp_napp': self.bet_dp_napp,
        }
        
        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(10)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')