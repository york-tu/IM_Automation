from distutils.log import error
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class PayInfoPageLocator:
    base = Xpath_Base()

    all = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='全部'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    deposit_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='充值'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    grap_order_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='抢单', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    want_buy_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我要买', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    want_sell_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我要卖', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    qr_pay_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='扫码支付', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    money_in_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='钱包入款', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    deposit_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='充值红利.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    grap_order_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='抢单-确认.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    want_buy_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='我要买.*', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    want_sell_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='我要卖.*', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    qr_pay_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='扫码支付', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    money_in_info = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='钱包入款.*', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 關閉
    close = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.view.ViewGroup', num=-1),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 返回
    back = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='back', num=-1),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 收支詳細資訊
    title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='收支明细资讯'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


class PayInfoPage(Base):
    error_list = []

    def pay_sort(self):
        tab_list = (
            (PayInfoPageLocator.all, "尚无资料"),
            (PayInfoPageLocator.deposit_tab, self.deposit_info),
            (PayInfoPageLocator.grap_order_tab, self.grap_order_info),
            (PayInfoPageLocator.want_buy_tab, self.want_buy_info),
            (PayInfoPageLocator.want_sell_tab, self.want_sell_info),
            (PayInfoPageLocator.qr_pay_tab, "尚无资料"),
            (PayInfoPageLocator.money_in_tab, self.money_in_info)
        )

        self.common.sleep(1)
        for i in tab_list:
            if self.common.poco_exists(i[0]):
                pos = self.common.poco_position(i[0])
                data = {
                    'pos': (pos[0] + 0.1, pos[1], pos[0], pos[1])  # a點[x, y] 往 b點[x, y] 滑
                }
                self.common.swipe(data)
                self.common.poco_click(i[0])

                if i[1] != "尚无资料":
                    i[1]()
            else:
                self.error_list.append(f"找不到上方分類:{i[0]['type_name']}")

        if self.error_list != []:
            raise EOFError(f'{self.error_list}')

    def deposit_info(self):
        self.common.poco_click(PayInfoPageLocator.deposit_info)

        if self.common.poco_exists(PayInfoPageLocator.title):
            self.common.poco_click(PayInfoPageLocator.back)
        else:
            self.error_list.append('充值:收支明细资讯視窗錯誤')

    def grap_order_info(self):
        self.common.poco_click(PayInfoPageLocator.grap_order_info)

        if self.common.poco_exists(PayInfoPageLocator.title):
            self.common.poco_click(PayInfoPageLocator.back)
        else:
            self.error_list.append('搶單:收支明细资讯視窗錯誤')

    def want_buy_info(self):
        self.common.poco_click(PayInfoPageLocator.want_buy_info)

        if self.common.poco_exists(PayInfoPageLocator.title):
            self.common.poco_click(PayInfoPageLocator.back)
        else:
            self.error_list.append('我要買:收支明细资讯視窗錯誤')

    def want_sell_info(self):
        self.common.poco_click(PayInfoPageLocator.want_sell_info)

        if self.common.poco_exists(PayInfoPageLocator.title):
            self.common.poco_click(PayInfoPageLocator.back)
        else:
            self.error_list.append('我要賣:收支明细资讯視窗錯誤')

    def money_in_info(self):
        self.common.poco_click(PayInfoPageLocator.money_in_info)

        if self.common.poco_exists(PayInfoPageLocator.title):
            self.common.poco_click(PayInfoPageLocator.back)
        else:
            self.error_list.append('入款:收支明细资讯視窗錯誤')
