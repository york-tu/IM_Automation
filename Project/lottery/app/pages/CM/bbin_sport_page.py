import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class BbinSportPageLocator:
    base = Xpath_Base()

    odds = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name=r'\d\.\d\d'),
        iOS = base.data_collation(type_kind='nameMatches', type_name=r'\d\.\d\d')
    )

    amount_edit = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android.widget.EditText'),
        iOS = base.data_collation(type_kind='name', type_name='android.widget.EditText')
    )

    bet_number_1 = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='MAX', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='text', type_name='MAX')
    )

    bet_number_0 = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='MAX', action='parent().child()[11]'),
        iOS = base.data_collation(type_kind='text', type_name='MAX')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='确定投注.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='确定投注.*')
    )

    confirm = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='继续投注.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='继续投注.*')
    )

    confirm_image = 'image/app/sport/bbin_confirm.png'

class BbinSportPage(Base):
    def bbin_sport(self):
        self.click_enter()
        
        for loop in range(0, 10):
            if self.common.poco_wait_exists(BbinSportPageLocator.odds, timeout=10):
                self.common.poco_click(BbinSportPageLocator.odds)
            
            if self.common.poco_wait_exists(BbinSportPageLocator.amount_edit):
                break
            
            if loop == 9:
                raise EOFError('找不到可下注的盤口')
        
        self.common.poco_click(BbinSportPageLocator.bet_number_1)
        self.common.poco_click(BbinSportPageLocator.bet_number_0)       # 最小注10塊
        
        if self.common.poco_wait_exists(BbinSportPageLocator.submit):
            self.common.poco_click(BbinSportPageLocator.submit)
        else:
            raise EOFError('確定投注點擊失敗')

        if not self.common.poco_wait_exists(BbinSportPageLocator.confirm, timeout=20):
            if not self.common.wait_image(BbinSportPageLocator.confirm_image):
                raise EOFError('下注失敗')

        