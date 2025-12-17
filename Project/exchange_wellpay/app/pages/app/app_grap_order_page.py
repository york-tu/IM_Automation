import math
from time import sleep
from turtle import tracer
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class GrapOrderPageLocator:
    base = Xpath_Base()

    # 确认抢单
    confirm = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='confirm_grab_confirm'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 搶單中
    wait_order = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='revenue_grab_ing'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 成功搶到訊息
    success_order = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='revenue_grab_success'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 繼續搶單
    next_order = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='继续抢单'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 確認二次彈窗_紅利積分
    bonus = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*红利积分.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


    # 確認二次彈窗
    def double_check(self, money):
        message = GrapOrderPageLocator.base.check_device(
            Android=GrapOrderPageLocator.base.data_collation(type_kind='textMatches', type_name=f'抢单积分{money}，.*'),
            iOS=GrapOrderPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return message

    # 搶單列表種類
    def transfer(self, type):
        transfer = GrapOrderPageLocator.base.check_device(
            Android=GrapOrderPageLocator.base.data_collation(type_kind='text', type_name=type),
            iOS=GrapOrderPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return transfer

    # 搶單列表金額
    def order_money(self, money):
        order_money = GrapOrderPageLocator.base.check_device(
            Android=GrapOrderPageLocator.base.data_collation(type_kind='text', type_name=str(money)+'.00'),
            iOS=GrapOrderPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return order_money

    def order_transfer_money(self, type, money):
        type_text = f'sibling(text="{type}")'
        order_transfer_money = GrapOrderPageLocator.base.check_device(
            Android=GrapOrderPageLocator.base.data_collation(type_kind='text', type_name=money, action=type_text),
            iOS=GrapOrderPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return order_transfer_money


class GrapOrderPage(Base):
    # 完成搶單流程
    def grap_order(self, money, transfer_type):

        for times in range(4):
            if not self.poco(text = f'{transfer_type}').exists:
            # if self.common.poco_wait_exists(GrapOrderPageLocator.order_transfer_money(self, transfer_type, str(money))) is False:
                self.common.sleep(3)
            else:
                break
            if times == 3:
                raise EOFError(f'沒有出現搶單單子 {transfer_type}_{money}')
        # self.common.poco_click(GrapOrderPageLocator.order_transfer_money(self, transfer_type, str(money)))
        self.poco(text=f'{transfer_type}').click()
        if self.common.poco_wait_exists(GrapOrderPageLocator.confirm) is False:
            raise EOFError('沒顯示確認搶單視窗')
        else:
            # if self.common.poco_wait_exists(GrapOrderPageLocator.order_money(self, money)) is False:
            #     raise EOFError('確認搶單視窗積分顯示錯誤')
            # 取得紅利
            if self.common.poco_wait_exists(GrapOrderPageLocator.bonus) is True:
                bonus_money = self.poco(type='android.widget.TextView')[-3].attr('text')
                bonus_rate = self.poco(type='android.widget.TextView')[-4].attr('text')[:-1]
                # order_money = self.poco(type='android.widget.TextView')[-7].attr('text')

                # bonus_text = self.common.poco_get_text(GrapOrderPageLocator.bonus).split('， ')
                # bonus_rate = float(bonus_text[0][bonus_text[0].find("利") + 1:-1])
                # bonus_money = float(bonus_text[1][bonus_text[1].find("分") + 1:])
                # count_bonus_money = math.floor(money * bonus_rate) / 100.0
                # count_bonus_money = format(money * (bonus_rate/100.0),".2f")
                count_bonus_money = self.calculate_bonus(money, bonus_rate)
                # assert format(bonus_money,'.2f') == count_bonus_money, f'紅利積分計算有誤，搶單金額:{money} * 紅利{
                # bonus_rate}%，計算為{count_bonus_money}，紅利積分顯示為{bonus_money}'
                assert bonus_money == count_bonus_money, f'紅利積分計算有誤，搶單金額:{money} * 紅利{bonus_rate}%，計算為{count_bonus_money}，紅利積分顯示為{bonus_money}'
            else:
                bonus_money = 0

            self.common.poco_click(GrapOrderPageLocator.confirm)

        assert self.common.poco_wait_exists(GrapOrderPageLocator.wait_order), f'未顯示"搶單中"'
        assert self.common.poco_wait_exists(GrapOrderPageLocator.success_order), f'未顯示"成功搶到訊息"'

        # assert self.common.poco_exists(GrapOrderPageLocator.order_money(self, str(money))) is True, '搶單中金額錯誤'
        self.common.poco_click(GrapOrderPageLocator.next_order)
        return bonus_money, bonus_rate
