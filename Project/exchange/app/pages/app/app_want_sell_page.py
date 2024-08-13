import math
from time import sleep
from common.app.common import Common
from Project.exchange.app.pages.app.base import Base
from Project.exchange.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class WantSellPageLocator:
    base = Xpath_Base()

    #### 我要賣
    def add(self, num=''):
        if num != '':
            num = f'[{num}]'
        add = WantSellPageLocator.base.check_device(
            Android=WantSellPageLocator.base.data_collation(type_kind='text', type_name='我的挂单',
                                                            action=f'sibling(){num}'),
            iOS=WantSellPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return add

    my_order = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的挂单'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    order_now_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='立即挂单'),
        iOS=base.data_collation(type_kind='text', type_name='立即挂单')
    )

    bonus_popup = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确定'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    sell_point = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='贩售积分'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    sell_input = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='请输入.*~.*数量'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    bank = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=-9),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # choose_bank = base.check_device(
    #     Android = base.data_collation(type_kind='name', type_name='android.widget.ScrollView', action='child("android.view.ViewGroup")[0]'),
    #     iOS = base.data_collation(type_kind='', type_name='')
    # )

    choose_bank = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*银行.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    submit = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='create_sell_order_confirm_order'),
        iOS=base.data_collation(type_kind='text', type_name='确认挂单')
    )

    bonus = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*%', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    _bonus_money = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='红利积分'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    total_money = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='贩售积分', action='sibling()[8].child()'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    success = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='挂单成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    def order_money(self, money):
        money = f'{money:,.2f}'
        order_money = WantSellPageLocator.base.check_device(
            Android=WantSellPageLocator.base.data_collation(type_kind='text', type_name=money),
            iOS=WantSellPageLocator.base.data_collation(type_kind='', type_name='')
        )
        return order_money

    def bonus_money(self, count_bonus_money):
        bonus_money = WantSellPageLocator.base.check_device(
            Android=WantSellPageLocator.base.data_collation(type_kind='text', type_name=count_bonus_money),
            iOS=WantSellPageLocator.base.data_collation(type_kind='', type_name='')
        )
        return bonus_money

    def order(self, money):
        money = f'{money:,.2f}'
        order = WantSellPageLocator.base.check_device(
            Android=WantSellPageLocator.base.data_collation(type_kind='text', type_name=money),
            iOS=WantSellPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return order


class WantSellPage(Base):
    def sell_order(self, money):
        total_money = money
        # if self.common.poco_wait_exists(WantSellPageLocator.my_order):
        #     add_len = self.common.len_poco(WantSellPageLocator.add(self))
        #     self.common.poco_click(WantSellPageLocator.add(self, add_len - 1))
        # else:
        #     raise EOFError('沒找立即掛單')
        #
        # if self.common.poco_wait_exists(WantSellPageLocator.bonus_popup, timeout=3):
        #     self.common.poco_click(WantSellPageLocator.bonus_popup)

        if self.common.poco_wait_exists(WantSellPageLocator.order_now_btn):
            self.common.poco_click(WantSellPageLocator.order_now_btn)

        if self.common.poco_wait_exists(WantSellPageLocator.sell_point):
            self.common.poco_send_text(WantSellPageLocator.sell_input, money)
            self.common.poco_click(WantSellPageLocator.bank)
            self.common.poco_click(WantSellPageLocator.choose_bank)
            sleep(3)
        else:
            raise EOFError('沒倒轉到掛單頁面')

        self.common.sleep(1)
        bonus_rate = 0
        if self.common.poco_wait_exists(WantSellPageLocator._bonus_money, timeout=3):
            bonus_rate = float(self.common.poco_get_text(WantSellPageLocator.bonus).replace('%', ''))
            count_bonus_money = self.calculate_bonus(money, bonus_rate)
            bonus_money = float(self.common.poco_get_text(WantSellPageLocator.bonus_money(self, count_bonus_money)))
            total_money = float(self.common.poco_get_text(WantSellPageLocator.order_money(self, money)))

            assert format(bonus_money,
                          '.2f') == count_bonus_money, f'紅利積分計算有誤，商品金額:{money} * 紅利{bonus_rate}%，紅利積分計算為{count_bonus_money}，顯示為{bonus_money}'
            assert total_money == (
                        money + bonus_money), f'總販售積分有誤，商品金額:{money} + 紅利積分{bonus_money}，總販售積分計算為{money + bonus_money}，顯示為{total_money}'

        self.common.poco_click(WantSellPageLocator.submit)
        if self.common.poco_wait_exists(WantSellPageLocator.success, timeout=3) is False:
            if self.common.poco_exists(WantSellPageLocator.submit) is True:
                raise EOFError('仍在交易掛單頁，我要賣掛單失敗')
            if self.common.poco_wait_exists(WantSellPageLocator.order(self, total_money), timeout=3) is False:
                raise EOFError('我要賣找不到掛單，掛單失敗')
        return total_money, bonus_rate

