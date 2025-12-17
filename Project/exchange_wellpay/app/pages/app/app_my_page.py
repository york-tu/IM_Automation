from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
from Project.exchange_wellpay.app.pages.app.app_main_page import MainPageLocator, MainPage
import common.utils.globalvar as gl


class MyPageLocator:
    base = Xpath_Base()
    #### 我的
    my_invite_code = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的邀请码'),
        iOS=base.data_collation(type_kind='name', type_name='会员资料')
    )
    member_data = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='会员资料'),
        iOS=base.data_collation(type_kind='name', type_name='会员资料')
    )
    check_member_data = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='手机号码'),
        iOS=base.data_collation(type_kind='name', type_name='手机号')
    )

    my_order = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的抢单'),
        iOS=base.data_collation(type_kind='name', type_name='我的抢单')
    )
    check_my_order = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='进行中的抢单'),
        iOS=base.data_collation(type_kind='name', type_name='进行中的抢单')
    )

    my_sell = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的卖单'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    check_my_sell = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='进行中的卖单'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    wallet_address = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='钱包地址', action='sibling()[9].child()'),
        iOS=base.data_collation(type_kind='name', type_name='钱包地址', action='sibling()[9].child()')
    )

    # 收支明细
    pay_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='income_expense_detail'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    deposit_record = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='充值记录'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    payment＿method = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='綁定收付款'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    member_number = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=3),  # huawei_26:num=4
        iOS=base.data_collation(type_kind='', type_name='')
    )


class MyPage(Base):
    # 進入會員資料
    def into_member_data_page(self):
        self.common.sleep(1)
        if self.common.poco_exists(MyPageLocator.member_data):
            self.common.poco_click(MyPageLocator.member_data)
        assert self.common.poco_wait_exists(MyPageLocator.check_member_data, timeout=3), f"APP進入_會員資料_頁面失敗"

    # 進入我的搶單
    def into_my_order_page(self):
        self.common.sleep(1)
        if self.common.poco_exists(MyPageLocator.my_invite_code):
            self.common.poco_click(MainPageLocator.check_hall)
        self.common.sleep(1)
        for _ in range(3):
            if self.common.poco_exists(MyPageLocator.my_order):
                self.common.poco_click(MyPageLocator.my_order)
                self.common.sleep(1)
                if self.common.poco_exists(MyPageLocator.check_my_order):
                    break
        assert self.common.poco_wait_exists(MyPageLocator.check_my_order, timeout=3), f"APP進入_我的搶單_頁面失敗"

    # 進入我的賣單
    def into_my_sell_page(self):
        # self.common.sleep(1)
        # self.common.go_down()
        # if self.common.poco_exists(MyPageLocator.my_sell):
        #     self.common.poco_click(MyPageLocator.my_sell)
        # self.common.go_bottom()
        self.common.sleep(1)
        for _ in range(3):
            if self.common.poco_exists(MyPageLocator.my_sell):
                self.common.poco_click(MyPageLocator.my_sell)
                self.common.sleep(1)
                if self.common.poco_exists(MyPageLocator.check_my_sell):
                    break
        assert self.common.poco_wait_exists(MyPageLocator.check_my_sell, timeout=3), f"APP進入_我的賣單_頁面失敗"

    # 進入收支明細
    def into_pay_info_page(self):
        self.common.sleep(1)
        if self.common.poco_exists(MyPageLocator.pay_info):
            self.common.poco_click(MyPageLocator.pay_info)

    # 進入充值紀錄
    def into_deposit_record_page(self):
        self.common.sleep(1)
        if self.common.poco_exists(MyPageLocator.deposit_record):
            self.common.poco_click(MyPageLocator.deposit_record)

    # # 進入綁定收款方式
    # def into_deposit_record_page(self):
    #     self.common.sleep(1)
    #     if self.common.poco_exists(MyPageLocator.payment_method):
    #         self.common.poco_click(MyPageLocator.payment_method)

    # 取得會員編號
    def get_member_number(self):
        self.common.sleep(1)
        number = self.common.poco_get_text(MyPageLocator.member_number)
        return number
