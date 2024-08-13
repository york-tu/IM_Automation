import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class SsSportPageLocator:
    base = Xpath_Base()

    soccer = base.data_collation(type_kind='text', type_name='足球')

    soccer_ball = 'image/app/sport/ss_soccer_ball.png'
    ss_confirm = 'image/app/sport/ss_confirm.png'

    odds = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name=r'\d\.\d\d'),
        iOS = base.data_collation(type_kind='nameMatches', type_name=r'\d\.\d\d')
    )

    amount_edit = base.data_collation(type_kind='name', type_name='bet_gold_bg')
    bet_6 = base.data_collation(type_kind='name', type_name='num_6')
    submit = base.data_collation(type_kind='name', type_name='bet_btn_area')
    transaction_id = base.data_collation(type_kind='name', type_name='bet_finish_tid')

class SsSportPage(Base):
    def ss_sport(self):
        self.click_enter()

        if self.common.poco_wait_exists(SsSportPageLocator.soccer):
            self.common.poco_click(SsSportPageLocator.soccer)
        else:
            self.common.touch_image(SsSportPageLocator.soccer_ball)

        for loop in range(0, 10):
            if self.common.poco_wait_exists(SsSportPageLocator.odds, timeout=10):
                self.common.poco_click(SsSportPageLocator.odds)
            
            if self.common.poco_exists(SsSportPageLocator.amount_edit):
                break
            
            if loop == 9:
                raise EOFError('找不到可下注的盤口')
            
        self.common.poco_click(SsSportPageLocator.amount_edit)
        self.common.poco_click(SsSportPageLocator.bet_6) # 最小注5塊 數字5的位置有可能被返回鈕遮住
        self.common.poco_click(SsSportPageLocator.submit)

        if self.common.poco_wait_exists(SsSportPageLocator.transaction_id):
            pass
        else:
            if not self.common.wait_image(SsSportPageLocator.ss_confirm):
                raise EOFError('下注失敗')