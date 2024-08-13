from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.lottery.bet_lottery_basepage import BetLotteryBasePageLocator, BetLotteryBasePage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryLocator(BetLotteryBasePageLocator):
    base = Xpath_Base()
    btn_zh = base.data_collation(type_kind='name', type_name='btn_zh')
    btn_zh_big = base.data_collation(type_kind='name', type_name='btn_zh_big')
    btn_lm = base.data_collation(type_kind='name', type_name='btn_lm')
    btn_lm1_big = base.data_collation(type_kind='name', type_name='btn_lm1_big')
    btn_dm = base.data_collation(type_kind='name', type_name='btn_dm')
    btn_dm1_1 = base.data_collation(type_kind='name', type_name='btn_dm1_1')
    btn_rx = base.data_collation(type_kind='name', type_name='btn_rx')
    btn_rx1 = base.data_collation(type_kind='name', type_name='btn_rx1')
    btn_rx2 = base.data_collation(type_kind='name', type_name='btn_rx2')
    btn_rx3 = base.data_collation(type_kind='name', type_name='btn_rx3')
    btn_rx4 = base.data_collation(type_kind='name', type_name='btn_rx4')
    btn_rx5 = base.data_collation(type_kind='name', type_name='btn_rx5')
    btn_rx6 = base.data_collation(type_kind='name', type_name='btn_rx6')
    btn_rx7 = base.data_collation(type_kind='name', type_name='btn_rx7')
    btn_rx8 = base.data_collation(type_kind='name', type_name='btn_rx8')
    btn_rx1_1 = base.data_collation(type_kind='name', type_name='btn_rx1_1')
    btn_rx2_1 = base.data_collation(type_kind='name', type_name='btn_rx2_1')
    btn_rx2_2 = base.data_collation(type_kind='name', type_name='btn_rx2_2')
    btn_rx3_1 = base.data_collation(type_kind='name', type_name='btn_rx3_1')
    btn_rx3_2 = base.data_collation(type_kind='name', type_name='btn_rx3_2')
    btn_rx3_3 = base.data_collation(type_kind='name', type_name='btn_rx3_3')
    btn_rx4_1 = base.data_collation(type_kind='name', type_name='btn_rx4_1')
    btn_rx4_2 = base.data_collation(type_kind='name', type_name='btn_rx4_2')
    btn_rx4_3 = base.data_collation(type_kind='name', type_name='btn_rx4_3')
    btn_rx4_4 = base.data_collation(type_kind='name', type_name='btn_rx4_4')
    btn_rx5_1 = base.data_collation(type_kind='name', type_name='btn_rx5_1')
    btn_rx5_2 = base.data_collation(type_kind='name', type_name='btn_rx5_2')
    btn_rx5_3 = base.data_collation(type_kind='name', type_name='btn_rx5_3')
    btn_rx5_4 = base.data_collation(type_kind='name', type_name='btn_rx5_4')
    btn_rx5_5 = base.data_collation(type_kind='name', type_name='btn_rx5_5')
    btn_rx6_1 = base.data_collation(type_kind='name', type_name='btn_rx6_1')
    btn_rx6_1 = base.data_collation(type_kind='name', type_name='btn_rx6_1')
    btn_rx6_2 = base.data_collation(type_kind='name', type_name='btn_rx6_2')
    btn_rx6_3 = base.data_collation(type_kind='name', type_name='btn_rx6_3')
    btn_rx6_4 = base.data_collation(type_kind='name', type_name='btn_rx6_4')
    btn_rx6_5 = base.data_collation(type_kind='name', type_name='btn_rx6_5')
    btn_rx6_6 = base.data_collation(type_kind='name', type_name='btn_rx6_6')
    btn_rx7_1 = base.data_collation(type_kind='name', type_name='btn_rx7_1')
    btn_rx7_2 = base.data_collation(type_kind='name', type_name='btn_rx7_2')
    btn_rx7_3 = base.data_collation(type_kind='name', type_name='btn_rx7_3')
    btn_rx7_4 = base.data_collation(type_kind='name', type_name='btn_rx7_4')
    btn_rx7_5 = base.data_collation(type_kind='name', type_name='btn_rx7_5')
    btn_rx7_6 = base.data_collation(type_kind='name', type_name='btn_rx7_6')
    btn_rx7_7 = base.data_collation(type_kind='name', type_name='btn_rx7_7')
    btn_rx8_1 = base.data_collation(type_kind='name', type_name='btn_rx8_1')
    btn_rx8_2 = base.data_collation(type_kind='name', type_name='btn_rx8_2')
    btn_rx8_3 = base.data_collation(type_kind='name', type_name='btn_rx8_3')
    btn_rx8_4 = base.data_collation(type_kind='name', type_name='btn_rx8_4')
    btn_rx8_5 = base.data_collation(type_kind='name', type_name='btn_rx8_5')
    btn_rx8_6 = base.data_collation(type_kind='name', type_name='btn_rx8_6')
    btn_rx8_7 = base.data_collation(type_kind='name', type_name='btn_rx8_7')
    btn_rx8_8 = base.data_collation(type_kind='name', type_name='btn_rx8_8')
    btn_zux = base.data_collation(type_kind='name', type_name='btn_zux')
    btn_zux2 = base.data_collation(type_kind='name', type_name='btn_zux2')
    btn_zux2_1 = base.data_collation(type_kind='name', type_name='btn_zux2_1')
    btn_zux2_2 = base.data_collation(type_kind='name', type_name='btn_zux2_2')
    btn_zux3 = base.data_collation(type_kind='name', type_name='btn_zux3')
    btn_zux3_1 = base.data_collation(type_kind='name', type_name='btn_zux3_1')
    btn_zux3_2 = base.data_collation(type_kind='name', type_name='btn_zux3_2')
    btn_zux3_3 = base.data_collation(type_kind='name', type_name='btn_zux3_3')
    btn_zhx = base.data_collation(type_kind='name', type_name='btn_zhx')
    btn_zhx2 = base.data_collation(type_kind='name', type_name='btn_zhx2')
    btn_zhx_1_1 = base.data_collation(type_kind='name', type_name='btn_zhx_1_1')
    btn_zhx_2_2 = base.data_collation(type_kind='name', type_name='btn_zhx_2_2')
    btn_zhx_3_3 = base.data_collation(type_kind='name', type_name='btn_zhx_3_3')
    btn_zhx3 = base.data_collation(type_kind='name', type_name='btn_zhx3')

    # -----------------------------------新版-------------------------------------------

    btn_zh_napp = base.data_collation(type_kind='text', type_name='总和')
    btn_zh_big_napp = base.data_collation(type_kind='text', type_name='和大')
    
    btn_lm_napp = base.data_collation(type_kind='text', type_name='两面')
    btn_lm_1 = base.data_collation(type_kind='text', type_name='第一球')
    btn_lm_big = base.data_collation(type_kind='text', type_name='大')
    btn_lm_2 = base.data_collation(type_kind='text', type_name='第二球')
    btn_lm_3 = base.data_collation(type_kind='text', type_name='第三球')
    btn_lm_4 = base.data_collation(type_kind='text', type_name='第四球')
    btn_lm_5 = base.data_collation(type_kind='text', type_name='第五球')

    btn_dm_napp = base.data_collation(type_kind='text', type_name='单码')
    btn_dm_1 = base.data_collation(type_kind='text', type_name='第一球')
    btn_dm_01 = base.data_collation(type_kind='text', type_name='01', num=-1)
    btn_dm_2 = base.data_collation(type_kind='text', type_name='第二球')
    btn_dm_3 = base.data_collation(type_kind='text', type_name='第三球')
    btn_dm_4 = base.data_collation(type_kind='text', type_name='第四球')
    btn_dm_5 = base.data_collation(type_kind='text', type_name='第五球')

    btn_rx_napp = base.data_collation(type_kind='text', type_name='任选')
    btn_rx_1 = base.data_collation(type_kind='text', type_name='一中一')
    btn_rx_01 = base.data_collation(type_kind='text', type_name='01',num=-1)
    btn_rx_02 = base.data_collation(type_kind='text', type_name='02',num=-1)
    btn_rx_03 = base.data_collation(type_kind='text', type_name='03',num=-1)
    btn_rx_04 = base.data_collation(type_kind='text', type_name='04',num=-1)
    btn_rx_05 = base.data_collation(type_kind='text', type_name='05',num=-1)
    btn_rx_06 = base.data_collation(type_kind='text', type_name='06',num=-1)
    btn_rx_07 = base.data_collation(type_kind='text', type_name='07',num=-1)
    btn_rx_08 = base.data_collation(type_kind='text', type_name='08',num=-1)
    btn_rx_2 = base.data_collation(type_kind='text', type_name='二中二')
    btn_rx_3 = base.data_collation(type_kind='text', type_name='三中三')
    btn_rx_4 = base.data_collation(type_kind='text', type_name='四中四')
    btn_rx_5 = base.data_collation(type_kind='text', type_name='五中五')
    btn_rx_6 = base.data_collation(type_kind='text', type_name='六中五')
    btn_rx_7 = base.data_collation(type_kind='text', type_name='七中五')
    btn_rx_8 = base.data_collation(type_kind='text', type_name='八中五')

    btn_zux_napp = base.data_collation(type_kind='text', type_name='组选')
    btn_zux_c2 = base.data_collation(type_kind='text', type_name='前二')
    btn_zux_01 = base.data_collation(type_kind='text', type_name='01', num=-1)
    btn_zux_02 = base.data_collation(type_kind='text', type_name='02', num=-1)
    btn_zux_03 = base.data_collation(type_kind='text', type_name='03', num=-1)
    btn_zux_c3 = base.data_collation(type_kind='text', type_name='前三')

    btn_zx = base.data_collation(type_kind='text', type_name='直选')
    btn_zx_c2 = base.data_collation(type_kind='text', type_name='前二')
    btn_zx_c2_1_01 = base.data_collation(type_kind='text', type_name='01', num=-2)
    btn_zx_c2_2_02 = base.data_collation(type_kind='text', type_name='02', num=-1)
    btn_zx_c3 = base.data_collation(type_kind='text', type_name='前三')
    btn_zx_c3_1_01 = base.data_collation(type_kind='text', type_name='01', num=-3)
    btn_zx_c3_2_02 = base.data_collation(type_kind='text', type_name='02', num=-2)
    btn_zx_c3_3_03 = base.data_collation(type_kind='text', type_name='03', num=-1)

class X5(BetLotteryBasePage):
    # 下注 總和 - 大
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zh(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zh)
        self.common.poco_click(BetLotteryLocator.btn_zh_big)
        self.bet_lottery(amount)
        
    # 下注 兩面 - 大
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_lm)
        self.common.poco_click(BetLotteryLocator.btn_lm1_big)
        self.bet_lottery(amount)
        
    # 下注 單碼 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_dm)
        self.common.poco_click(BetLotteryLocator.btn_dm1_1)
        self.bet_lottery(amount)

    # 下注 任選 - 一中一 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx1(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx1)
        self.common.poco_click(BetLotteryLocator.btn_rx1_1)
        self.bet_lottery(amount)
        
    # 下注 任選 - 二中二 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx2(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx2)
        self.common.poco_click(BetLotteryLocator.btn_rx2_1)
        self.common.poco_click(BetLotteryLocator.btn_rx2_2)
        self.bet_lottery(amount)
       
    # 下注 任選 - 三中三 - 
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx3(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx3)

        self.common.poco_click(BetLotteryLocator.btn_rx3_1)
        self.common.poco_click(BetLotteryLocator.btn_rx3_2)
        self.common.poco_click(BetLotteryLocator.btn_rx3_3)

        self.bet_lottery(amount)

    # 下注 任選 - 四中四 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx4(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx4)

        self.common.poco_click(BetLotteryLocator.btn_rx4_1)
        self.common.poco_click(BetLotteryLocator.btn_rx4_2)
        self.common.poco_click(BetLotteryLocator.btn_rx4_3)
        self.common.poco_click(BetLotteryLocator.btn_rx4_4)

        self.bet_lottery(amount)

    # 下注 任選 - 五中五 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx5(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx5)

        self.common.poco_click(BetLotteryLocator.btn_rx5_1)
        self.common.poco_click(BetLotteryLocator.btn_rx5_2)
        self.common.poco_click(BetLotteryLocator.btn_rx5_3)
        self.common.poco_click(BetLotteryLocator.btn_rx5_4)
        self.common.poco_click(BetLotteryLocator.btn_rx5_5)

        self.bet_lottery(amount)

    # 下注 任選 - 六中五 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx6(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx6)
        self.common.poco_click(BetLotteryLocator.btn_rx6_1)
        self.common.poco_click(BetLotteryLocator.btn_rx6_2)
        self.common.poco_click(BetLotteryLocator.btn_rx6_3)
        self.common.poco_click(BetLotteryLocator.btn_rx6_4)
        self.common.poco_click(BetLotteryLocator.btn_rx6_5)
        self.common.poco_click(BetLotteryLocator.btn_rx6_6)
        self.bet_lottery(amount)

    # 下注 任選 - 七中五 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx7(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx7)

        self.common.poco_click(BetLotteryLocator.btn_rx7_1)
        self.common.poco_click(BetLotteryLocator.btn_rx7_2)
        self.common.poco_click(BetLotteryLocator.btn_rx7_3)
        self.common.poco_click(BetLotteryLocator.btn_rx7_4)
        self.common.poco_click(BetLotteryLocator.btn_rx7_5)
        self.common.poco_click(BetLotteryLocator.btn_rx7_6)
        self.common.poco_click(BetLotteryLocator.btn_rx7_7)

        self.bet_lottery(amount)

    # 下注 任選 - 八中五 - 1
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx8(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)

        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_rx)
        self.common.poco_click(BetLotteryLocator.btn_rx8)

        self.common.poco_click(BetLotteryLocator.btn_rx8_1)
        self.common.poco_click(BetLotteryLocator.btn_rx8_2)
        self.common.poco_click(BetLotteryLocator.btn_rx8_3)
        self.common.poco_click(BetLotteryLocator.btn_rx8_4)
        self.common.poco_click(BetLotteryLocator.btn_rx8_5)
        self.common.poco_click(BetLotteryLocator.btn_rx8_6)
        self.common.poco_click(BetLotteryLocator.btn_rx8_7)
        self.common.poco_click(BetLotteryLocator.btn_rx8_8)

        self.bet_lottery(amount)
        
    # 下注 組選 - 前二 - 1,2
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zux2(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zux)
        self.common.poco_click(BetLotteryLocator.btn_zux2)
        self.common.poco_click(BetLotteryLocator.btn_zux2_1)
        self.common.poco_click(BetLotteryLocator.btn_zux2_2)
        self.bet_lottery(amount)
    
    # 下注 組選 - 前三 - 1,2,3
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zux3(self,amount):
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zux)
        self.common.poco_click(BetLotteryLocator.btn_zux3)
        self.common.poco_click(BetLotteryLocator.btn_zux3_1)
        self.common.poco_click(BetLotteryLocator.btn_zux3_2)
        self.common.poco_click(BetLotteryLocator.btn_zux3_3)
        self.bet_lottery(amount)
    
    # 下注 直選 - 前二 - 1,2
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zhx2(self,amount):
        if self.common.poco_exists(BetLotteryLocator.btn_cancel):
            self.common.poco_click(BetLotteryLocator.btn_cancel)
            
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhx)
        self.common.poco_click(BetLotteryLocator.btn_zhx2)
        self.common.poco_click(BetLotteryLocator.btn_zhx_1_1)

        for loop in range(0, 3):
            if self.common.poco_exists(BetLotteryLocator.btn_zhx_2_2):
                self.common.go_down()
                self.common.poco_click(BetLotteryLocator.btn_zhx_2_2)
                break
            else:
                self.common.go_down()
            
            if loop == 2:
                raise EOFError('點擊直選 - 前二錯誤')

        self.bet_lottery(amount)
    
    # 下注 直選 - 前三 - 1,2,3
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zhx3(self,amount):
        self.common.poco_click(BetLotteryLocator.bet_menu)
        self.common.poco_click(BetLotteryLocator.btn_zhx)
        self.common.poco_click(BetLotteryLocator.btn_zhx3)
        self.common.poco_click(BetLotteryLocator.btn_zhx_1_1)

        for loop in range(0, 3):
            if self.common.poco_exists(BetLotteryLocator.btn_zhx_2_2):
                self.common.go_down()
                self.common.poco_click(BetLotteryLocator.btn_zhx_2_2)
                break
            else:
                self.common.go_down()
            
            if loop == 2:
                raise EOFError('點擊直選 - 前三錯誤')

        for loop in range(0, 3):
            if self.common.poco_exists(BetLotteryLocator.btn_zhx_3_3):
                self.common.go_down()
                self.common.go_down() # 部分小手機要滑兩次才點的到
                self.common.poco_click(BetLotteryLocator.btn_zhx_3_3)
                break
            else:
                self.common.go_down()
                
            if loop == 2:
                raise EOFError('點擊直選 - 前三錯誤')

        self.bet_lottery(amount)

# -------------------------------------------新版------------------------------------------------
    # 下注 總和
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zh_napp(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zh_napp)
        self.common.poco_click(BetLotteryLocator.btn_zh_big_napp)
        return self.bet_lottery_napp(amount)
        
    # 下注 兩面-第一球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_1(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_lm_napp)
        self.common.poco_click(BetLotteryLocator.btn_lm_1)
        self.common.poco_click(BetLotteryLocator.btn_lm_big)
        return self.bet_lottery_napp(amount)

    # 下注 兩面-第二球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_2(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_lm_2)
        self.common.poco_click(BetLotteryLocator.btn_lm_big)
        return self.bet_lottery_napp(amount)
    
    # 下注 兩面-第三球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_lm_3)
        self.common.poco_click(BetLotteryLocator.btn_lm_big)
        return self.bet_lottery_napp(amount)
    
    # 下注 兩面-第四球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_4(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_lm_4)
        self.common.poco_click(BetLotteryLocator.btn_lm_big)
        return self.bet_lottery_napp(amount)
    
    # 下注 兩面-第五球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_lm_5(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_lm_5)
        self.common.poco_click(BetLotteryLocator.btn_lm_big)
        return self.bet_lottery_napp(amount)
        
    # 下注 單碼-第一球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm_1(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_dm_napp)
        self.common.poco_click(BetLotteryLocator.btn_dm_1)
        self.common.poco_click(BetLotteryLocator.btn_dm_01)
        return self.bet_lottery_napp(amount)

    # 下注 單碼-第二球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm_2(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_dm_2)
        self.common.poco_click(BetLotteryLocator.btn_dm_01)
        return self.bet_lottery_napp(amount)

    # 下注 單碼-第三球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm_3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_dm_3)
        self.common.poco_click(BetLotteryLocator.btn_dm_01)
        return self.bet_lottery_napp(amount)
    
    # 下注 單碼-第四球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm_4(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_dm_4)
        self.common.poco_click(BetLotteryLocator.btn_dm_01)
        return self.bet_lottery_napp(amount)
    
    # 下注 單碼-第五球
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_dm_5(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_dm_5)
        self.common.poco_click(BetLotteryLocator.btn_dm_01)
        return self.bet_lottery_napp(amount)

    # 下注 任選-一中一
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_1(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_rx_napp)
        self.common.poco_click(BetLotteryLocator.btn_rx_1)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-二中二
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_2(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_2)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-三中三
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_3)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        return self.bet_lottery_napp(amount)

    # 下注 任選-四中四
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_4(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_4)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        self.common.poco_click(BetLotteryLocator.btn_rx_04)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-五中五
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_5(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_5)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        self.common.poco_click(BetLotteryLocator.btn_rx_04)
        self.common.poco_click(BetLotteryLocator.btn_rx_05)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-六中五
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_6(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_6)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        self.common.poco_click(BetLotteryLocator.btn_rx_04)
        self.common.poco_click(BetLotteryLocator.btn_rx_05)
        self.common.poco_click(BetLotteryLocator.btn_rx_06)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-七中五
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_7(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_7)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        self.common.poco_click(BetLotteryLocator.btn_rx_04)
        self.common.poco_click(BetLotteryLocator.btn_rx_05)
        self.common.poco_click(BetLotteryLocator.btn_rx_06)
        self.common.poco_click(BetLotteryLocator.btn_rx_07)
        return self.bet_lottery_napp(amount)
    
    # 下注 任選-八中五
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_rx_8(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_rx_8)
        self.common.poco_click(BetLotteryLocator.btn_rx_01)
        self.common.poco_click(BetLotteryLocator.btn_rx_02)
        self.common.poco_click(BetLotteryLocator.btn_rx_03)
        self.common.poco_click(BetLotteryLocator.btn_rx_04)
        self.common.poco_click(BetLotteryLocator.btn_rx_05)
        self.common.poco_click(BetLotteryLocator.btn_rx_06)
        self.common.poco_click(BetLotteryLocator.btn_rx_07)
        self.common.poco_click(BetLotteryLocator.btn_rx_08)
        return self.bet_lottery_napp(amount)

    # 下注 組選-前二
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zux_c2(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zux_napp)
        self.common.poco_click(BetLotteryLocator.btn_zux_c2)
        self.common.poco_click(BetLotteryLocator.btn_zux_01)
        self.common.poco_click(BetLotteryLocator.btn_zux_02)
        return self.bet_lottery_napp(amount)
    
    # 下注 組選-前三
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zux_c3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zux_c3)
        self.common.poco_click(BetLotteryLocator.btn_zux_01)
        self.common.poco_click(BetLotteryLocator.btn_zux_02)
        self.common.poco_click(BetLotteryLocator.btn_zux_03)
        return self.bet_lottery_napp(amount)
    
    
    # 下注 直選-前二
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zx_c2(self,amount):
        self.bet_menu()
        self.common.poco_click(BetLotteryLocator.btn_zx)
        self.common.poco_click(BetLotteryLocator.btn_zx_c2)
        self.common.poco_click(BetLotteryLocator.btn_zx_c2_1_01)
        self.common.poco_click(BetLotteryLocator.btn_zx_c2_2_02)
        return self.bet_lottery_napp(amount)
    
    # 下注 直選-前三
    @retry(stop_max_attempt_number=3, wait_fixed=10000)
    def bet_zx_c3(self,amount):
        self.common.poco_click(BetLotteryLocator.btn_zx_c3)
        data = {'pos':(0.5, 0.5, 0.5, 0.41)}
        self.common.swipe(data)
        self.common.poco_click(BetLotteryLocator.btn_zx_c3_1_01)
        self.common.poco_click(BetLotteryLocator.btn_zx_c3_2_02)
        self.common.poco_click(BetLotteryLocator.btn_zx_c3_3_03)
        return self.bet_lottery_napp(amount)

    # 11選5全玩法下注
    def bet_x5_lottery(self,amount,lottery_kind):
        result_list = []

        self.maintenance()
        self.in_draw()
        self.trend_check(lottery_kind)

        game_dict = {
            'bet_zh': self.bet_zh,
            'bet_lm': self.bet_lm,
            'bet_dm': self.bet_dm,
            'bet_rx1': self.bet_rx1,
            'bet_rx2': self.bet_rx2,
            'bet_rx3': self.bet_rx3,
            'bet_rx4': self.bet_rx4,
            'bet_rx5': self.bet_rx5,
            'bet_rx6': self.bet_rx6,
            'bet_rx7': self.bet_rx7,
            'bet_rx8': self.bet_rx8,
            'bet_zux2': self.bet_zux2,
            'bet_zhx2': self.bet_zhx2, 
            'bet_zhx3': self.bet_zhx3,
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

    # 11選5全玩法下注
    def bet_11x5_lottery(self,amount):
        result_list = []
        self.maintenance_napp()
        self.in_closing()

        game_dict = {
            'bet_zh': self.bet_zh_napp,
            'bet_lm_1': self.bet_lm_1,
            'bet_lm_2': self.bet_lm_2,
            'bet_lm_3': self.bet_lm_3,
            'bet_lm_4': self.bet_lm_4,
            'bet_lm_5': self.bet_lm_5,
            'bet_dm_1': self.bet_dm_1,
            'bet_dm_2': self.bet_dm_2,
            'bet_dm_3': self.bet_dm_3,
            'bet_dm_4': self.bet_dm_4,
            'bet_dm_5': self.bet_dm_5,
            'bet_rx_1': self.bet_rx_1,
            'bet_rx_2': self.bet_rx_2, 
            'bet_rx_3': self.bet_rx_3,
            'bet_rx_4': self.bet_rx_4,
            'bet_rx_5': self.bet_rx_5,
            'bet_rx_6': self.bet_rx_6,
            'bet_rx_7': self.bet_rx_7,
            'bet_rx_8': self.bet_rx_8, 
            'bet_zux_c2': self.bet_zux_c2,
            'bet_zux_c3': self.bet_zux_c3,
            'bet_zx_c2': self.bet_zx_c2, 
            'bet_zx_c3': self.bet_zx_c3,
        }
        
        for game in game_dict.keys():
            self.in_closing()
            self.off_time_check(30)

            result = game_dict[game](amount)

            if result != None:
                result_list.append(f'{game}:{result}')

        if result_list != []:
            raise EOFError(f'{result_list}')