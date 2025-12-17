from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl
import locale


class MyOrderPageLocator:
    base = Xpath_Base()

    receive = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='我已收到.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # def order(self, money):
    #     order = MyOrderPageLocator.base.check_device(
    #         Android = MyOrderPageLocator.base.data_collation(type_kind='textMatches', type_name=f'.* {money}.*'),
    #         iOS = MyOrderPageLocator.base.data_collation(type_kind='', type_name='')
    #     )
    #     return order
    #
    #  # 搶單列表種類
    # def transfer(self, type):
    #     transfer = MyOrderPageLocator.base.check_device(
    #         Android = MyOrderPageLocator.base.data_collation(type_kind='text', type_name=type),
    #         iOS = MyOrderPageLocator.base.data_collation(type_kind='', type_name='')
    #     )
    #     return transfer

    # 搶單列表金額
    # def order_money(self, money):
    #     order_money = MyOrderPageLocator.base.check_device(
    #         Android = MyOrderPageLocator.base.data_collation(type_kind='text', type_name=money),
    #         iOS = MyOrderPageLocator.base.data_collation(type_kind='', type_name='')
    #     )
    #     return order_money

    # 搶單列表金額
    # def confirm(self, money):
    #     confirm = MyOrderPageLocator.base.check_device(
    #         Android = MyOrderPageLocator.base.data_collation(type_kind='text', type_name=f'我已收到{money}元'),
    #         iOS = MyOrderPageLocator.base.data_collation(type_kind='', type_name='')
    #     )
    #     return confirm

    # title:未到帐资讯
    pop_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='grab_detail_unsettled_order_info'),
        iOS=base.data_collation(type_kind='name', type_name='未到帐资讯')
    )
    # 交易状态
    transfer_status_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='grab_transfer_timeout'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 確認收到彈窗
    receive_popup = base.check_device(
        Android=base.data_collation(type_kind='nameMatches',type_name='确认收到.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # n筆訂單未處理"立即查看"
    check_now_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='check_now'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 進行中的搶單列表
    order_info_grab_amount = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='order_info_grab_amount'),
        iOS=base.data_collation(type_kind='name', type_name='未到帐资讯')
    )


class MyOrderPage(Base):
    def choose_order_first(self, name, money):
        self.common.sleep(5)
        order_info = self.common.poco_get_text(MyOrderPageLocator.order_info_grab_amount)
        assert order_info, f'搶單列表訊息有誤, 預期:+ {str(money)}.00  收款人：{name} 實際: {order_info}'
        self.common.poco_click(MyOrderPageLocator.order_info_grab_amount)

    def check_grap_order(self, money, transfer_type, bonus_money, bonus_rate):
        self.common.sleep(3)
        assert self.common.poco_get_text(MyOrderPageLocator.pop_title) == '未到账资讯', f'未到帳頁錯誤'
        assert self.poco(text=f'{transfer_type}').exists(), f'支付名稱錯誤'
        assert self.poco(text=f'{money}.00').exists(), f'支付積分錯誤'
        assert self.poco(text=f'{bonus_rate} %').exists(), f'紅利利率錯誤'
        assert self.poco(text=f'{bonus_money}').exists(), f'紅利積分錯誤'

        while self.common.poco_exists(MyOrderPageLocator.receive):
            self.common.poco_click(MyOrderPageLocator.receive)
            self.common.sleep(2)

