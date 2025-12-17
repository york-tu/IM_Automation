from airtest.core.api import *
from common.app.common import Common
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from decimal import Decimal, ROUND_DOWN, getcontext
class BaseLocator:
    base = Xpath_Base()

    close_grab_expire =  base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*抢单.*', action='parent().sibling()[2]'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    close_order_expire_confirm =  base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*订单确认.*', action='parent().sibling()[2]'),
        iOS = base.data_collation(type_kind='', type_name='')
    )
    

class Base(object):
    def __init__(self, poco='', wda_service='', skip_test_method=''):
        self.poco = poco
        self.wda = wda_service
        self.common = Common(self.poco, self.wda, skip_test_method)

    # 關閉搶單到期彈窗
    def skip_order_expire(self):
        self.common.sleep(1)
        if self.common.poco_exists(BaseLocator.close_grab_expire):
            self.common.poco_click(BaseLocator.close_grab_expire)
            self.common.sleep(1)


    # 關閉訂單確認彈窗(我要買)
    def skip_order_confirm(self):
        self.common.sleep(1)
        if self.common.poco_exists(BaseLocator.close_order_expire_confirm):
            self.common.poco_click(BaseLocator.close_order_expire_confirm)
            self.common.sleep(1)
    
    # 計算紅利(無條件捨去到小數點第二位，回傳型態為str)
    def calculate_bonus(self, money, rate):
        getcontext().prec = 6
        money = Decimal(money)
        rate = Decimal(rate) / 100
        result = (money * rate).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        return str(result)