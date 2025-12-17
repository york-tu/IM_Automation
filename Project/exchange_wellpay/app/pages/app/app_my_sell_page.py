from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class MySellPageLocator:
    base = Xpath_Base()

    confirm = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认款项'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    pop_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='敬请注意'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    success = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认完成'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    sell_record_tab = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='卖单记录'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 卖单记录 > 完成頁
    sell_done_page = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='done'),
        iOS=base.data_collation(type_kind='text', type_name='完成')
    )


    # 我知道了btn
    i_known_btn = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='我知道了 .*'),
        iOS=base.data_collation(type_kind='text', type_name='我知道了 .*')
    )
    # 确认完成订单
    confirm_finish_order_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='confirm_finish_order'),
        iOS=base.data_collation(type_kind='text', type_name='确认完成订单')
    )
    # 重要提示視窗
    important_hint_msg = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='.*重要提示.*'),
        iOS=base.data_collation(type_kind='text', type_name='确认完成订单')
    )

    # 重要提示視窗 > "我已了解，提示讯息" radio button
    order_info_sell_confirm_check = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='order_info_sell_confirm_check_desc'),
        iOS=base.data_collation(type_kind='text', type_name='我已了解，提示讯息')
    )

    #

    def order(self, money):
        money = f'{money:,.2f}'
        order = MySellPageLocator.base.check_device(
            Android=MySellPageLocator.base.data_collation(type_kind='text', type_name=money),
            iOS=MySellPageLocator.base.data_collation(type_kind='', type_name='')
        )
        return order

    def order_done(self, money, status='已完成'):
        money = f'{money:,.2f}'
        order = MySellPageLocator.base.check_device(
            Android=MySellPageLocator.base.data_collation(type_kind='text', type_name=money,
                                                          action=f'sibling(text="{status}")'),
            iOS=MySellPageLocator.base.data_collation(type_kind='', type_name='')
        )
        return order

    success = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认完成'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


class MySellPage(Base):
    # 賣家確認款項
    def confirm_order(self, money):
        if self.common.poco_wait_exists(MySellPageLocator.order(self, money)):
            if self.common.poco_wait_exists(MySellPageLocator.confirm):
                self.common.poco_click(MySellPageLocator.confirm)
                if self.common.poco_exists(MySellPageLocator.pop_title):
                    self.common.sleep(6)
                    self.common.poco_click(MySellPageLocator.i_known_btn)
                else:
                    raise EOFError("沒顯示敬請注意彈窗")
            else:
                raise EOFError("沒顯示確認款項按鈕")
        self.common.poco_click(MySellPageLocator.confirm_finish_order_btn)

        if self.common.poco_wait_exists(MySellPageLocator.order_info_sell_confirm_check):
            if self.common.poco_wait_exists(MySellPageLocator.order_info_sell_confirm_check):
                self.common.poco_click(MySellPageLocator.order_info_sell_confirm_check)
            if self.common.poco_wait_exists(MySellPageLocator.confirm_finish_order_btn):
                self.common.poco_click(MySellPageLocator.confirm_finish_order_btn)
        else:
            raise EOFError("沒顯示重要提示視窗")

        self.common.poco_click(MySellPageLocator.sell_record_tab)
        self.common.sleep(1)
        self.common.poco_click(MySellPageLocator.sell_done_page)
        assert self.common.poco_wait_exists(MySellPageLocator.order(self, money)), f"賣單記錄_沒顯示該賣單已完成紀錄"

        # if self.common.poco_wait_exists(MySellPageLocator.confirm):
        #     if self.common.poco_exists(MySellPageLocator.order(self, money)):
        #         self.common.poco_click(MySellPageLocator.confirm)
        #         if self.common.poco_exists(MySellPageLocator.pop_title):
        #             self.common.sleep(3)
        #             self.common.poco_click(MySellPageLocator.confirm)

        #             assert self.common.poco_wait_exists(MySellPageLocator.success), '沒出現 "确认完成" 彈窗'
        #             self.common.sleep(3)
        #     else:
        #         raise EOFError('沒有找到該金額訂單')
        # else:
        #     raise EOFError('沒有找到該金額訂單的確認款項按鈕')
