import math
from time import sleep

from Project.exchange_wellpay.app.pages.app.app_want_sell_page import WantSellPageLocator
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
from Project.exchange_wellpay.app.pages.app.app_main_page import MainPage, MainPageLocator
import common.utils.globalvar as gl

class WantBuyPageLocator:
    base = Xpath_Base()
    #### 我要買
    # grab_next_step = base.check_device(
    #     Android = base.data_collation(type_kind='text', type_name='点选空白处跳至下一步骤'),
    #     iOS = base.data_collation(type_kind='name', type_name='点选空白处跳至下一步骤')
    # )

    # buy_tutorial_text = base.check_device(
    #     Android = base.data_collation(type_kind='text', type_name='我要买教程'),
    #     iOS = base.data_collation(type_kind='', type_name='')
    # )

    # complete_grab_tutorial = base.check_device(
    #     Android = base.data_collation(type_kind='text', type_name='完成教程'),
    #     iOS = base.data_collation(type_kind='name', type_name='完成教程')
    # )

    buy_now = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='立即购买'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    close = base.check_device(
        Android=base.data_collation(pos=[0.5, 0.6239316239316239]),  # HUAWEI_26: pos=[0.5, 0.595]
        iOS=base.data_collation(type_kind='', type_name='')
    )

    add_photo = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='upload_img'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    albuma = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*相片.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    albumb = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*册.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    albumc = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*簿.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    albumd = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*图.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    image = base.check_device(
        Android=base.data_collation(pos=[0.2037037037037037, 0.42905982905982903] ), # HUAWEI_26: pos=[0.2, 0.5]
        iOS=base.data_collation(type_kind='', type_name='')
    )
    image2 = base.check_device(
        Android=base.data_collation(pos=[0.5, 0.42905982905982903]),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    image_submit = base.check_device(
        Android=base.data_collation(type_kind='desc', type_name='确定'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    finish = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='buy_order_detail_complete_pay'),
        iOS=base.data_collation(type_kind='text', type_name='完成付款')
    )

    pop_submit = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='buy_lobby_transfer_already'),
        iOS=base.data_collation(type_kind='text', type_name='我已转账')
    )

    success = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='上传成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    bonus = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*%', num=1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    bonus_0 = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='--'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    bonus_money = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.widget.TextView', num=2),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # '是否允許"順付wellPay"訪問媒體? >>> "允許"鍵
    permission_allow_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='com.android.permissioncontroller:id/permission_allow_button'),
        iOS=base.data_collation(type_kind='text', type_name='允許')
    )

    # '是否允许“顺付 WellPay”访问相机? >>>"仅使用期间允许"鍵
    permission_allow_foreground_only_btn = base.check_device(
        Android=base.data_collation(type_kind='name',
                                    type_name='com.android.permissioncontroller:id/permission_allow_foreground_only_button'),
        iOS=base.data_collation(type_kind='text', type_name='仅使用期间允许')
    )

    # "敬请贵宾留意"視窗
    confirm_warning_msg = base.check_device(
        Android=base.data_collation(type_kind='text',type_name='敬请贵宾留意'),
        iOS=base.data_collation(type_kind='text', type_name='敬请贵宾留意')
    )

    # "敬请贵宾留意"確認鍵
    confirm_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='确认'),
        iOS=base.data_collation(type_kind='name', type_name='确认')
    )

    # "完成付款"視窗
    complete_purchase_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成付款'),
        iOS=base.data_collation(type_kind='text', type_name='完成付款')
    )

    # "完成付款"視窗 > "返回大厅"鍵
    purchase_return_to_lobby_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='purchase_return_to_lobby'),
        iOS=base.data_collation(type_kind='text', type_name='返回大厅')
    )
    # "完成付款"視窗 > "關閉"鍵
    purchase_close_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭'),
        iOS=base.data_collation(type_kind='text', type_name='关闭')
    )

    # 導航欄:我要買
    i_want_buy = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_buy_lobby'),
        iOS=base.data_collation(type_kind='text', type_name='我要买')
    )

    # 導航欄:我要賣
    i_want_sell = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_sell_lobby'),
        iOS=base.data_collation(type_kind='text', type_name='我要卖')
    )

    # 购买询问鍵
    create_buy_order_inquiry = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='create_buy_order_inquiry'),
        iOS=base.data_collation(type_kind='text', type_name='购买询问')
    )

    # 确认询问視窗
    confirm_ask_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认询问'),
        iOS=base.data_collation(type_kind='text', type_name='确认询问')
    )

    # 交易询问視窗
    inquiry_count_down_msg = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='inquiry_count_down_title'),
        iOS=base.data_collation(type_kind='text', type_name='交易询问')
    )

    # 回复交易询问
    inquiry_response_transaction_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='inquiry_respone_transaction'),
        iOS=base.data_collation(type_kind='text', type_name='回复交易询问')
    )

    # 确认贩售
    inquiry_confirm_sell_btn = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='inquiry_confirm_sell'),
        iOS=base.data_collation(type_kind='text', type_name='确认贩售')
    )

    back_btn = base.check_device(
        Android=base.data_collation(pos=[0.07777777777777778, 0.9085470085470085]), # HUAWEI_26: pos=[0.06037414965986394, 0.9175]
        iOS=base.data_collation(type_kind='text', type_name='确认贩售')
    )
    # 右下角提示訊息:订单购买计时
    order_count_down_msg = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='order_count_down'),
        iOS=base.data_collation(type_kind='text', type_name='订单购买计时')
    )


    def order(self, money):
        money = f'{money:,.2f}'
        order = WantBuyPageLocator.base.check_device(
            Android=WantBuyPageLocator.base.data_collation(type_kind='text', type_name=money),
            iOS=WantBuyPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return order


class WantBuyPage(Base):
    # 我要買-立即購買並完成上傳圖片
    def get_order(self, money):
        for i in range(3):
            if self.common.poco_wait_exists(WantBuyPageLocator.order(self, money)):
                self.common.poco_click(WantBuyPageLocator.order(self, money))
                self.common.sleep(0.5)
                if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
                    self.close_please_note_msg()
                if self.common.poco_wait_exists(WantBuyPageLocator.buy_now):
                    break
        # assert self.common.poco_wait_exists(WantBuyPageLocator.buy_now), f"APP我要買大廳_沒有找到該筆交易單 ${money}"

        if self.common.poco_exists(WantBuyPageLocator.buy_now):
            if self.common.poco_exists(WantBuyPageLocator.bonus_0):
                bonus_rate = 0
                get_bonus_money = self.common.poco_get_text(WantBuyPageLocator.bonus_money)
                assert get_bonus_money == '--', f'紅利積分有誤，顯示為{get_bonus_money}, 應顯示 --(無紅利)'
                bonus_money = 0
            else:
                bonus_rate = float(self.common.poco_get_text(WantBuyPageLocator.bonus)[:-1])
                bonus_money = float(self.common.poco_get_text(WantBuyPageLocator.bonus_money))
                count_bonus_money = self.calculate_bonus(money, bonus_rate)
                assert float(bonus_money) == float(
                    count_bonus_money), f'紅利積分計算有誤，商品金額:{money} * 紅利{bonus_rate}%，紅利積分計算為{count_bonus_money}，顯示為{bonus_money}'

            self.common.poco_click(WantBuyPageLocator.buy_now)  # 商品詳情頁點"立即購買"

            if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
                self.close_please_note_msg()

        else:
            raise EOFError('我要買流程錯誤')
        self.upload_photo_complete_order(money)
        self.common.sleep(2)
        return bonus_money

    def upload_photo_complete_order(self, money):
        if self.common.poco_wait_exists(WantBuyPageLocator.order(self, money)):
            self.common.sleep(1)

            # 獲取賣單頁上的紅利積分
            if self.common.poco_wait_exists(WantSellPageLocator.bonus, timeout=3):
                # bonus_rate = self.common.poco_get_text(WantSellPageLocator.bonus)[:-1]
                # aaa = self.poco(nameMatches='.*%')[0][:-1]
                bonus_rate = float(self.common.poco_get_text(WantSellPageLocator.bonus)[:-1])
                count_bonus_money = self.calculate_bonus(money, bonus_rate)
                assert self.common.poco_exists(WantSellPageLocator.bonus_money(self, count_bonus_money))
                bonus_money = float(self.common.poco_get_text(WantSellPageLocator.bonus_money(self, count_bonus_money)))

            for i in range(2):
                self.common.go_down()
                self.common.go_down()
                self.common.go_down()
                self.common.go_down()
                self.common.sleep(1)

                if self.common.poco_exists(WantBuyPageLocator.add_photo):
                    self.common.poco_click(WantBuyPageLocator.add_photo)
                    if self.common.poco_exists(
                            WantBuyPageLocator.permission_allow_btn):  # 裝置跳出'是否允許"順付wellPay"訪問媒體? > "允許"鍵
                        self.common.poco_click(WantBuyPageLocator.permission_allow_btn)
                    if self.common.poco_exists(
                            WantBuyPageLocator.permission_allow_foreground_only_btn):  # '是否允许“顺付 WellPay”访问相机? >"仅使用期间允许"鍵
                        self.common.poco_click(WantBuyPageLocator.permission_allow_foreground_only_btn)

                    if self.common.poco_exists(WantBuyPageLocator.albuma):
                        self.common.poco_click(WantBuyPageLocator.albuma)
                        break
                    elif self.common.poco_exists(WantBuyPageLocator.albumb):
                        self.common.poco_click(WantBuyPageLocator.albumb)
                        break
                    elif self.common.poco_exists(WantBuyPageLocator.albumc):
                        self.common.poco_click(WantBuyPageLocator.albumc)
                        break
                    elif self.common.poco_exists(WantBuyPageLocator.albumd):
                        self.common.poco_click(WantBuyPageLocator.albumd)
                        break

                if i == 2:
                    raise EOFError('沒有找到對應的相簿應用程式')

            self.common.sleep(3)

            for _ in range(3):
                self.common.poco_click(WantBuyPageLocator.image)
                self.common.sleep(0.5)

            if self.common.poco_exists(WantBuyPageLocator.image_submit):
                self.common.poco_click(WantBuyPageLocator.image_submit)

            if self.common.poco_wait_exists(WantBuyPageLocator.finish):
                self.common.poco_click(WantBuyPageLocator.finish)

            self.common.sleep(3)

            if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
                self.common.poco_click(WantBuyPageLocator.confirm_btn)

            if self.common.poco_wait_exists(WantBuyPageLocator.complete_purchase_msg):
                if self.common.poco_exists(WantBuyPageLocator.purchase_close_btn):
                    self.common.poco_click(WantBuyPageLocator.purchase_close_btn)
                pass
            else:
                raise EOFError('沒出現完成付款彈窗')

            if self.common.poco_exists(WantBuyPageLocator.purchase_return_to_lobby_btn):
                self.common.poco_click(WantBuyPageLocator.purchase_return_to_lobby_btn)

        return bonus_money

    def close_please_note_msg(self):  # 關閉敬请贵宾留意視窗
        for _ in range(3):
            if self.common.poco_wait_exists(WantBuyPageLocator.confirm_warning_msg):
                sleep(5)
                self.common.poco_click(WantBuyPageLocator.close)
                if not self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
                    break

    def buyer_contact_seller(self, buyer_account, buyer_pwd, seller_account, seller_pwd, money):
        # 買方搶單 > 聯繫賣方 > 登出
        if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
            self.close_please_note_msg()
        if self.common.poco_wait_exists(WantBuyPageLocator.order(self, money)):
            self.common.poco_click(WantBuyPageLocator.order(self, money))
            if self.common.poco_wait_exists(WantBuyPageLocator.create_buy_order_inquiry):
                self.common.poco_click(WantBuyPageLocator.create_buy_order_inquiry)
            if self.common.poco_wait_exists(WantBuyPageLocator.confirm_ask_msg):
                self.common.poco_click(WantBuyPageLocator.confirm_btn)
            if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
                self.close_please_note_msg()
        self.logout()

        # 賣方登入 > 回覆買方 > 登出
        self.login(seller_account, seller_pwd)
        self.common.poco_click(WantBuyPageLocator.i_want_sell)
        if self.common.poco_wait_exists(WantBuyPageLocator.inquiry_response_transaction_info):
            self.common.poco_click(WantBuyPageLocator.inquiry_response_transaction_info)
            if self.common.poco_wait_exists(WantBuyPageLocator.inquiry_count_down_msg):
                self.common.poco_click(WantBuyPageLocator.inquiry_confirm_sell_btn)
        self.logout()

        # 買方登入 > 接續搶單流程
        self.login(buyer_account, buyer_pwd)
        self.common.poco_click(WantBuyPageLocator.i_want_buy)
        if self.common.poco_wait_exists(WantBuyPageLocator.order_count_down_msg):
            self.common.poco_click(WantBuyPageLocator.order_count_down_msg)
        if self.common.poco_exists(WantBuyPageLocator.confirm_warning_msg):
            self.close_please_note_msg()

    def logout(self):
        sleep(1)
        self.common.poco_click(WantBuyPageLocator.back_btn)
        self.poco(name='我的').click()
        self.poco.swipe([0.5, 0.5], [0.5, 0.1], duration=0.5)
        if self.common.poco_wait_exists(MainPageLocator.new_logout_btn):
            self.common.poco_click(MainPageLocator.new_logout_btn)

    def login(self, account, password):
        if self.common.poco_exists(MainPageLocator.account):
            self.common.poco_send_text(MainPageLocator.account, account)
        if self.common.poco_exists(MainPageLocator.password):
            self.common.poco_send_text(MainPageLocator.password, password)
        if self.common.poco_exists(MainPageLocator.login_button):
            self.common.poco_click(MainPageLocator.login_button)
