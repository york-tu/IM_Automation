from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_zzdw = base.data_collation(type_kind='name', type_name='btn_zzdw')
    btn_zzl_1 = base.data_collation(type_kind='name', type_name='btn_zzl_1')
    btn_fc3d_zzl_1_0 = base.data_collation(type_kind='name', type_name='btn_fc3d_zzl_1_0')
    btn_zzl_2 = base.data_collation(type_kind='name', type_name='btn_zzl_2')
    btn_fc3d_zzl_2_0 = base.data_collation(type_kind='name', type_name='btn_fc3d_zzl_2_0')
    btn_zzl_3 = base.data_collation(type_kind='name', type_name='btn_zzl_3')
    btn_fc3d_zzl_3_0 = base.data_collation(type_kind='name', type_name='btn_fc3d_zzl_3_0')

    # --------------------------------------新版-----------------------------------------------

    btn_zzdw_napp = base.data_collation(type_kind='text', type_name='一字定位')
    btn_zzdw_b = base.data_collation(type_kind='text', type_name='百')
    btn_zzdw_1 = base.data_collation(type_kind='text', type_name='1', num=-1)
    btn_zzdw_s = base.data_collation(type_kind='text', type_name='十')
    btn_zzdw_g = base.data_collation(type_kind='text', type_name='个')

    btn_zs = base.data_collation(type_kind='text', type_name='组选')
    btn_zs_2s = base.data_collation(type_kind='text', type_name='二星组选')
    btn_zs_1 = base.data_collation(type_kind='text', type_name='1', num=-1)
    btn_zs_2 = base.data_collation(type_kind='text', type_name='2', num=-1)
    btn_zs_3 = base.data_collation(type_kind='text', type_name='3', num=-1)
    btn_zs_3ss3 = base.data_collation(type_kind='text', type_name='三星组选三')
    btn_zs_3ss6 = base.data_collation(type_kind='text', type_name='三星组选六')

    btn_zcg = base.data_collation(type_kind='text', type_name='字串关')
    btn_zcg_b1 = base.data_collation(type_kind='text', type_name='1', num=-2)
    btn_zcg_s2 = base.data_collation(type_kind='text', type_name='2', num=-1)

    btn_hz = base.data_collation(type_kind='text', type_name='和值')
    btn_hz_lm = base.data_collation(type_kind='text', type_name='两面')
    btn_hz_lm_big = base.data_collation(type_kind='text', type_name='大')
    btn_hz_hm = base.data_collation(type_kind='text', type_name='号码')
    btn_hz_hm_01 = base.data_collation(type_kind='text', type_name='01')

    btn_hws = base.data_collation(type_kind='text', type_name='和尾数')
    btn_hws_01 = base.data_collation(type_kind='text', type_name='1', num=-1)

    btn_kd = base.data_collation(type_kind='text', type_name='跨度')
    btn_kd_01 = base.data_collation(type_kind='text', type_name='1', num=-1)

    btn_lhh = base.data_collation(type_kind='text', type_name='龙虎和')
    btn_lhh_l = base.data_collation(type_kind='text', type_name='龙')

    btn_ts = base.data_collation(type_kind='text', type_name='特殊')
    btn_ts_bz = base.data_collation(type_kind='text', type_name='豹子')

class Fc3D(BetLotteryBasePage):
    #一字定位 － 百 - 0
    # @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzl_1(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zzdw)
        self.common.poco_click(BetLotteryLocator.btn_zzl_1)
        self.common.poco_click(BetLotteryLocator.btn_fc3d_zzl_1_0)
        self.bet_lottery(amount)

    #一字定位 － 十 - 0
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzl_2(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zzdw)
        self.common.poco_click(BetLotteryLocator.btn_zzl_2)
        self.common.poco_click(BetLotteryLocator.btn_fc3d_zzl_2_0)
        self.bet_lottery(amount)

    #一字定位 － 個 - 0
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzl(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zzdw)
        self.common.poco_click(BetLotteryLocator.btn_zzl_3)
        self.common.poco_click(BetLotteryLocator.btn_fc3d_zzl_3_0)
        self.bet_lottery(amount)

    # 快三全玩法下注
    def bet_fc3d_lottery(self,amount,lottery_kind):
        result_list = []
        
        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)
        
        game_dict = {
            'bet_zzl_1': self.bet_zzl_1, 
            'bet_zzl_2': self.bet_zzl_2,
            'bet_zzl': self.bet_zzl,
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

    # ---------------------------新版----------------------------
    # 一字定位-百
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzdw_b(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zzdw_napp)
        self.common.poco_click(BetLotteryLocator.btn_zzdw_b)
        self.common.poco_click(BetLotteryLocator.btn_zzdw_1)
        return self.bet_lottery_napp(amount)

    #一字定位-十
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzdw_s(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zzdw_s)
        self.common.poco_click(BetLotteryLocator.btn_zzdw_1)
        return self.bet_lottery_napp(amount)

    #一字定位-個
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zzdw_g(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zzdw_g)
        self.common.poco_click(BetLotteryLocator.btn_zzdw_1)
        return self.bet_lottery_napp(amount)

    #組選-二星組選
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_2s(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zs)
        self.common.poco_click(BetLotteryLocator.btn_zs_2s)
        self.common.poco_click(BetLotteryLocator.btn_zs_1)
        self.common.poco_click(BetLotteryLocator.btn_zs_2)
        return self.bet_lottery_napp(amount)
    
    #組選-三星組選三
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_3ss3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zs_3ss3)
        self.common.poco_click(BetLotteryLocator.btn_zs_1)
        self.common.poco_click(BetLotteryLocator.btn_zs_2)
        return self.bet_lottery_napp(amount)
    
    #組選-三星組選六
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_3ss6(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zs_3ss6)
        self.common.poco_click(BetLotteryLocator.btn_zs_1)
        self.common.poco_click(BetLotteryLocator.btn_zs_2)
        self.common.poco_click(BetLotteryLocator.btn_zs_3)
        return self.bet_lottery_napp(amount)
    
    #字串關
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zcg(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zcg)
        self.common.poco_click(BetLotteryLocator.btn_zcg_b1)
        self.common.poco_click(BetLotteryLocator.btn_zcg_s2)
        return self.bet_lottery_napp(amount)
    
    #和值-兩面
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_hzlm(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_hz)
        self.common.poco_click(BetLotteryLocator.btn_hz_lm)
        self.common.poco_click(BetLotteryLocator.btn_hz_lm_big)
        return self.bet_lottery_napp(amount)
    
    #和值-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_hzhm(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_hz_hm)
        self.common.poco_click(BetLotteryLocator.btn_hz_hm_01)
        return self.bet_lottery_napp(amount)

    #和尾數
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_hws(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_hws)
        self.common.poco_click(BetLotteryLocator.btn_hws_01)
        return self.bet_lottery_napp(amount)    
    
    #跨度
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_kd(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_kd)
        self.common.poco_click(BetLotteryLocator.btn_kd_01)
        return self.bet_lottery_napp(amount)   

    #龍虎和
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lhh(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lhh)
        self.common.poco_click(BetLotteryLocator.btn_lhh_l)
        return self.bet_lottery_napp(amount)   

    #特殊
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_ts(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_ts)
        self.common.poco_click(BetLotteryLocator.btn_ts_bz)
        return self.bet_lottery_napp(amount)   

    # 福彩3D全玩法下注
    def bet_fc3d_lottery_napp(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()
        
        game_dict = {
            'bet_zzdw_b': self.bet_zzdw_b, 
            'bet_zzdw_s': self.bet_zzdw_s,
            'bet_zzdw_g': self.bet_zzdw_g,
            'bet_2s': self.bet_2s, 
            'bet_3ss3': self.bet_3ss3,
            'bet_3ss6': self.bet_3ss6,
            'bet_zcg': self.bet_zcg, 
            'bet_hzlm': self.bet_hzlm,
            'bet_hzhm': self.bet_hzhm,
            'bet_hws': self.bet_hws, 
            'bet_kd': self.bet_kd,
            'bet_lhh': self.bet_lhh,
            'bet_ts': self.bet_ts,
        }
        
        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(10)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')
            