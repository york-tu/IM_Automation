from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.trend_page import TrendPage
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry

class BetLotteryBasePageLocator:
    base = Xpath_Base()

    loading = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='处理中...'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*处理中.*')
    )

    processing = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='注单确认中'),
        iOS = base.data_collation(type_kind='name', type_name='注单确认中')
    )

    in_draw = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请稍候下注或选择其它彩种'),
        iOS = base.data_collation(type_kind='name', type_name='请稍候下注或选择其它彩种')
    )

    in_closing = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='封盘中'),
        iOS = base.data_collation(type_kind='name', type_name='封盘中')
    )

    maintenance = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='选择其它彩种'),
        iOS = base.data_collation(type_kind='name', type_name='选择其它彩种')
    )

    maintenance_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='彩票维护中'),
        iOS = base.data_collation(type_kind='name', type_name='彩票维护中')
    )

    btn_lottery_back = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='btnLottoBack'),
        iOS = base.data_collation(type_kind='name', type_name='btnLottoBack')
    )

    bet_menu = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='btnGameBettingMenu'),    # 玩法選單
        iOS = base.data_collation(type_kind='name', type_name='btnGameBettingMenu')
    )

    @staticmethod
    def bet_menu_napp(num=1):
        bet_menu = BetLotteryBasePageLocator.base.check_device(
            Android = BetLotteryBasePageLocator.base.data_collation(type_kind='text', type_name='玩法', action=f'parent().child()[{num}]'),
            iOS = BetLotteryBasePageLocator.base.data_collation(type_kind='name', type_name='玩法')
        )
        return bet_menu

    btn_menu_back = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='选择玩法', action='parent().child()[0]'),
        iOS = base.data_collation(type_kind='name', type_name='选择玩法', action='parent().child()[0]')
    )

    off_time = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='投注截止', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='name', type_name='投注截止', action='parent().child()[2]')
    )

    off_time_2 = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='投注截止', action='parent().child()[1]'),
        iOS = base.data_collation(type_kind='name', type_name='投注截止', action='parent().child()[3]')
    )

    btn_trend = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='开奖走势'),
        iOS = base.data_collation(type_kind='name', type_name='开奖走势')
    )

    btn_add_bet = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='btnAddBet'),
        iOS = base.data_collation(type_kind='name', type_name='btnAddBet')
    )

    btn_add_bet_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='投注'),
        iOS = base.data_collation(type_kind='name', type_name='投注')
    )

    btn_add_bet_2 = base.check_device(
        Android = base.data_collation(pos=[0.88, 0.97]),
        iOS = base.data_collation(pos=[0.88, 0.97])
    )

    btn_confirm = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='btnConfirmBet'),
        iOS = base.data_collation(type_kind='name', type_name='btnConfirmBet')
    )

    btn_confirm_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确定送出'),
        iOS = base.data_collation(type_kind='text', type_name='确定送出')
    )
    
    btn_cancel = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='取消'),
        iOS = base.data_collation(type_kind='name', type_name='取消')
    )

    btn_cancel_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='取消关闭'),
        iOS = base.data_collation(type_kind='name', type_name='取消关闭')
    )
    
    btn_finish = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认'),
        iOS = base.data_collation(type_kind='name', type_name='btnFinishBet')
    )

    input_bet_amount = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='inputBetAmount'),
        iOS = base.data_collation(type_kind='name', type_name='inputBetAmount')
    )

    input_bet_amount_napp = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android.widget.EditText'),
        iOS = base.data_collation(type_kind='name', type_name='android.widget.EditText')
    )

class BetLotteryBasePage(Base):
    def __init__(self, poco='', wda_service='', skip_test_method=''):
        Base.__init__(self, poco, wda_service, skip_test_method)
        self.trend = TrendPage(self.poco, self.wda, skip_test_method)

    def bet_lottery(self, amount):
        self.common.poco_send_text(BetLotteryBasePageLocator.input_bet_amount, amount)
        self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_add_bet)
        self.common.poco_click(BetLotteryBasePageLocator.btn_add_bet)
        self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_confirm)
        self.common.poco_click(BetLotteryBasePageLocator.btn_confirm)

        if self.common.poco_exists(BetLotteryBasePageLocator.loading):
            if self.common.poco_wait_disappearance(BetLotteryBasePageLocator.loading):
                pass
            else:
                return 'Loading畫面沒有消失'

        if self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_finish):
            self.common.poco_click(BetLotteryBasePageLocator.btn_finish)
        else:
            if self.common.poco_exists(BetLotteryBasePageLocator.btn_cancel):
                self.common.poco_click(BetLotteryBasePageLocator.btn_cancel)

            return '沒出現完成按鈕'
        
        return None

    def bet_lottery_napp(self, amount):
        try:
            self.common.poco_wait_appearance(BetLotteryBasePageLocator.input_bet_amount_napp)
            self.common.poco_send_text(BetLotteryBasePageLocator.input_bet_amount_napp, amount)
        except:
            return '投注不完全'
        if self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_add_bet_napp):
            self.common.poco_click(BetLotteryBasePageLocator.btn_add_bet_napp)
        else:
            self.common.poco_click(BetLotteryBasePageLocator.btn_add_bet_2)
        self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_confirm_napp)
        self.common.poco_click(BetLotteryBasePageLocator.btn_confirm_napp)

        if self.common.poco_exists(BetLotteryBasePageLocator.processing):
            if self.common.poco_wait_disappearance(BetLotteryBasePageLocator.processing):
                pass
            else:
                return '注單確認中沒有消失'

        if self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_finish, timeout=30):
            self.common.poco_click(BetLotteryBasePageLocator.btn_finish)
        else:
            if self.common.poco_exists(BetLotteryBasePageLocator.btn_cancel_napp):
                self.common.poco_click(BetLotteryBasePageLocator.btn_cancel_napp)

            return '沒出現完成按鈕'
        
        return None

    def in_draw(self):
        for loop in range(0, 5):
            if self.common.poco_exists(BetLotteryBasePageLocator.in_draw) is True:
                self.common.sleep(5)
            else:
                break

            if loop == 4:
                raise EOFError(f'開獎中,請確認彩票是否正常,已重新確認次數: {loop}')

    def in_closing(self):
        for loop in range(0, 5):
            if self.common.poco_exists(BetLotteryBasePageLocator.in_closing) is True:
                self.common.sleep(5)
            else:
                break

            if loop == 4:
                raise EOFError(f'開獎中,請確認彩票是否正常,已重新確認次數: {loop}')
    
    # 截止時間小於X秒不下注
    def off_time_check(self, second):
        current_off_time = self.common.poco_get_text(BetLotteryBasePageLocator.off_time)
        try:
            if int(current_off_time[-5:-3]) == 0:
                if int(current_off_time[-2:]) <= int(second):
                    self.common.sleep(int(second))
        except:
            current_off_time = self.common.poco_get_text(BetLotteryBasePageLocator.off_time_2)      # 有些裝置定位不一樣
            if int(current_off_time[-5:-3]) == 0:
                if int(current_off_time[-2:]) <= int(second):
                    self.common.sleep(int(second))
        finally:
            self.in_closing()

    def maintenance(self):
        self.common.sleep(1)

        if self.common.poco_exists(BetLotteryBasePageLocator.maintenance) is True:
            self.common.skip_test('該彩種維護中')

    def maintenance_napp(self):
        self.common.sleep(1)

        if self.common.poco_exists(BetLotteryBasePageLocator.maintenance_napp) is True:
            self.common.skip_test('該彩票維護中')
    
    # @retry(stop_max_attempt_number=5, wait_fixed=2000)
    def trend_check(self, lottery_kind):
        self.wait_loading_finish()
        for i in range(3):
            if self.common.poco_wait_exists(BetLotteryBasePageLocator.bet_menu):
                self.common.poco_click(BetLotteryBasePageLocator.bet_menu)

            if self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_menu_back):
                try:
                    self.common.poco_click(BetLotteryBasePageLocator.btn_menu_back)
                    break
                except:
                    pass

            if i == 2:
                raise EOFError('找不到子玩法目錄')

        if self.common.poco_wait_exists(BetLotteryBasePageLocator.btn_trend):
            self.common.poco_click(BetLotteryBasePageLocator.btn_trend)
        
        self.trend.trend(lottery_kind)
    
    # 點擊玩法選單
    def bet_menu(self):
        self.common.poco_click(BetLotteryBasePageLocator.bet_menu_napp())
        self.common.poco_click(BetLotteryBasePageLocator.bet_menu_napp(num=0))      # 有些裝置定位不一樣，要再點擊一次