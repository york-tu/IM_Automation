from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_tema = base.data_collation(type_kind='name', type_name='btn_tema')
    btn_tema_ball = base.data_collation(type_kind='name', type_name='btn_temaball')
    btn_tm_01 = base.data_collation(type_kind='name', type_name='btn_tm_01')
    btn_tema_boduan = base.data_collation(type_kind='name', type_name='btn_temaboduan')
    btn_tm_big = base.data_collation(type_kind='name', type_name='btn_tm_big')
    btn_tema_shengxiao = base.data_collation(type_kind='name', type_name='btn_temashengxiao')
    btn_tx_mouse = base.data_collation(type_kind='name', type_name='btn_tx_mouse')  
    btn_tema_hx = base.data_collation(type_kind='name', type_name='btn_temahx')
    btn_beast = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='野兽'),
        iOS = base.data_collation(type_kind='name', type_name='野兽')
    )
    btn_tema_touwei = base.data_collation(type_kind='name', type_name='btn_tematouwei')
    btn_t_t_0 = base.data_collation(type_kind='name', type_name='btn_t_t_0')
    btn_tmwx = base.data_collation(type_kind='name', type_name='btn_tmwx')
    btn_metal = base.data_collation(type_kind='name', type_name='btn_metal')
    btn_zhengma = base.data_collation(type_kind='name', type_name='btn_zhengma')
    btn_zmball = base.data_collation(type_kind='name', type_name='btn_zmball')
    btn_z_01 = base.data_collation(type_kind='name', type_name='btn_z_01')
    btn_zmzh = base.data_collation(type_kind='name', type_name='btn_zmzh')
    btn_zm_zh_odd = base.data_collation(type_kind='name', type_name='btn_zm_zh_odd')
    btn_zmsx = base.data_collation(type_kind='name', type_name='btn_zmsx')
    btn_yx_mouse = base.data_collation(type_kind='name', type_name='btn_yx_mouse')
    btn_zx = base.data_collation(type_kind='name', type_name='btn_zx')
    btn_zx_234 = base.data_collation(type_kind='name', type_name='btn_zx_234')

    btn_tema_napp = base.data_collation(type_kind='textMatches', type_name='特码.*',num=1)
    btn_tema_homa = base.data_collation(type_kind='text', type_name='号码')
    btn_tm_01_napp = base.data_collation(type_kind='text', type_name='01',num=-1)

    btn_tema_luman = base.data_collation(type_kind='text', type_name='两面')
    btn_tm_big_napp = base.data_collation(type_kind='text', type_name='大')
    
    btn_tema_texiao = base.data_collation(type_kind='text', type_name='特肖')
    btn_tm_mouse = base.data_collation(type_kind='text', type_name='鼠',num=-1)

    btn_tema_hx = base.data_collation(type_kind='text', type_name='合肖')
    btn_beast_napp = base.data_collation(type_kind='text', type_name='野兽')

    btn_tema_tou = base.data_collation(type_kind='text', type_name='头数')
    btn_tm_0tou = base.data_collation(type_kind='text', type_name='0头')

    btn_tema_wei = base.data_collation(type_kind='text', type_name='尾数')
    btn_tm_0wei = base.data_collation(type_kind='text', type_name='0尾')

    btn_tmwx_napp = base.data_collation(type_kind='text', type_name='五行')
    btn_gold = base.data_collation(type_kind='text', type_name='金')

    btn_zhengma_napp = base.data_collation(type_kind='text', type_name='正码')
    btn_zhengma_homa = base.data_collation(type_kind='text', type_name='号码')
    btn_zm_01 = base.data_collation(type_kind='text', type_name='01',num=-1)

    btn_zhengma_zmzh = base.data_collation(type_kind='text', type_name='总和')
    btn_zm_zh_odd_napp = base.data_collation(type_kind='text', type_name='总单')

    btn_zmsx_napp = base.data_collation(type_kind='text', type_name='正肖')
    btn_zm_mouse = base.data_collation(type_kind='text', type_name='鼠',num=-1)

    btn_zmzx = base.data_collation(type_kind='text', type_name='总肖')
    btn_zm_234s = base.data_collation(type_kind='text', type_name='234肖')


class Hk(BetLotteryBasePage):
    # 下注 特碼-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temaball(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tema_ball)
        self.common.poco_click(BetLotteryLocator.btn_tm_01)
        self.bet_lottery(amount)

    # 下注 特碼-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temaball_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_homa)
        self.common.poco_click(BetLotteryLocator.btn_tm_01_napp)
        return self.bet_lottery_napp(amount)

    # 下注 特碼-兩面
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temaboduan(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tema_boduan)
        self.common.poco_click(BetLotteryLocator.btn_tm_big)
        self.bet_lottery(amount)
    
    # 下注 特碼-兩面
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temaluman(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_luman)
        self.common.poco_click(BetLotteryLocator.btn_tm_big_napp)
        return self.bet_lottery_napp(amount)

    # 下注 特碼-特肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temashengxiao(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tema_shengxiao)
        self.common.poco_click(BetLotteryLocator.btn_tx_mouse)
        self.bet_lottery(amount)
    
    # 下注 特碼-特肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tematexiao(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_texiao)
        self.common.poco_click(BetLotteryLocator.btn_tm_mouse)
        return self.bet_lottery_napp(amount)
    
    # 下注 特碼-合肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temahx(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tema_hx)
        self.common.poco_click(BetLotteryLocator.btn_beast)
        self.bet_lottery(amount)
    
    # 下注 特碼-合肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temahx_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_hx)
        self.common.poco_click(BetLotteryLocator.btn_beast_napp)
        return self.bet_lottery_napp(amount)

    # 下注 特碼-頭尾數
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tematouwei(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tema_touwei)
        self.common.poco_click(BetLotteryLocator.btn_t_t_0)
        self.bet_lottery(amount)

    # 下注 特碼-頭數
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_tematou(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_tou)
        self.common.poco_click(BetLotteryLocator.btn_tm_0tou)
        return self.bet_lottery_napp(amount)
    
    # 下注 特碼-尾數
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_temawei(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tema_wei)
        self.common.poco_click(BetLotteryLocator.btn_tm_0wei)
        return self.bet_lottery_napp(amount)
    
    # 下注 特碼-五行
    def bet_tmwx(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_tema)
        self.common.poco_click(BetLotteryLocator.btn_tmwx)
        self.common.poco_click(BetLotteryLocator.btn_metal)
        self.bet_lottery(amount)

    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    # 下注 特碼-五行
    def bet_tmwx_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_tema_napp)
        self.common.poco_click(BetLotteryLocator.btn_tmwx_napp)
        self.common.poco_click(BetLotteryLocator.btn_gold)
        return self.bet_lottery_napp(amount)

    # 下注 正碼-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zmball(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhengma)
        self.common.poco_click(BetLotteryLocator.btn_zmball)
        self.common.poco_click(BetLotteryLocator.btn_z_01)
        self.bet_lottery(amount)
    
    # 下注 正碼-號碼
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zmball_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zhengma_napp)
        self.common.poco_click(BetLotteryLocator.btn_zhengma_homa)
        self.common.poco_click(BetLotteryLocator.btn_zm_01)
        return self.bet_lottery_napp(amount)

    # 下注 正碼-總和
    def bet_zmzh(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhengma)
        self.common.poco_click(BetLotteryLocator.btn_zmzh)
        self.common.poco_click(BetLotteryLocator.btn_zm_zh_odd)
        self.bet_lottery(amount)
    
    # 下注 正碼-總和
    def bet_zmzh_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zhengma_napp)
        self.common.poco_click(BetLotteryLocator.btn_zhengma_zmzh)
        self.common.poco_click(BetLotteryLocator.btn_zm_zh_odd_napp)
        return self.bet_lottery_napp(amount)
    
    # 下注 正碼-正肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zmsx(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhengma)
        self.common.poco_click(BetLotteryLocator.btn_zmsx)
        self.common.poco_click(BetLotteryLocator.btn_yx_mouse)
        self.bet_lottery(amount)
    
    # 下注 正碼-正肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zmsx_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zhengma_napp)
        self.common.poco_click(BetLotteryLocator.btn_zmsx_napp)
        self.common.poco_click(BetLotteryLocator.btn_zm_mouse)
        return self.bet_lottery_napp(amount)

    # 下注 正碼-總肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zx(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhengma)
        self.common.poco_click(BetLotteryLocator.btn_zx)
        self.common.poco_click(BetLotteryLocator.btn_zx_234)
        self.bet_lottery(amount)
    
    # 下注 正碼-總肖
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zmzx(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zhengma_napp)
        self.common.poco_click(BetLotteryLocator.btn_zmzx)
        self.common.poco_click(BetLotteryLocator.btn_zm_234s)
        return self.bet_lottery_napp(amount)
        
    # 六合彩全玩法下注
    def bet_hk_lottery(self,amount,lottery_kind):
        result_list = []
        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)
        
        game_dict = {
            'bet_temaball': self.bet_temaball, 
            'bet_temaboduan': self.bet_temaboduan,
            'bet_temashengxiao': self.bet_temashengxiao,
            'bet_temahx': self.bet_temahx,
            'bet_tematouwei': self.bet_tematouwei,
            'bet_tmwx': self.bet_tmwx,
            'bet_zmball': self.bet_zmball,
            'bet_zmzh': self.bet_zmzh,
            'bet_zmsx': self.bet_zmsx,
            'bet_zx': self.bet_zx,
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

    # 六合彩玩法下注
    def bet_mark6_lottery(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()
        
        game_dict = {
            'bet_temaball': self.bet_temaball_napp, 
            'bet_temaboduan': self.bet_temaluman,
            'bet_temashengxiao': self.bet_tematexiao,
            'bet_temahx': self.bet_temahx_napp,
            'bet_tematou': self.bet_tematou,
            'bet_temawei': self.bet_temawei,
            'bet_tmwx': self.bet_tmwx_napp,
            'bet_zmball': self.bet_zmball_napp,
            'bet_zmzh': self.bet_zmzh_napp,
            'bet_zmsx': self.bet_zmsx_napp,
            'bet_zx': self.bet_zmzx,
        }

        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(10)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')