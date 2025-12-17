from time import sleep
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
from Project.exchange_wellpay.app.pages.app.app_deposit_page import DepositPageLocator
from Project.exchange_wellpay.app.pages.app.app_register_page import RegisterPageLocator, RegisterPage
import common.utils.globalvar as gl


class MainPageLocator:
    base = Xpath_Base()

    get_current_money = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='qa_available_points'),
        iOS=base.data_collation(type_kind='name', type_name='注')
    )

    get_current_money_for_sale = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='qa_sellable_points'),
        iOS=base.data_collation(type_kind='name', type_name='可贩售积分')
    )

    register = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='去注册'),
        iOS=base.data_collation(type_kind='name', type_name='注')
    )

    logout = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='复制', action='parent().sibling()[2]'),
        iOS=base.data_collation(type_kind='name', type_name='parent().sibling()[2]')
    )

    my_page_pos = base.check_device(
        Android=base.data_collation(pos=[0.9, 0.9]),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    hall_page_pos = base.check_device(
        Android=base.data_collation(pos=[0.1, 0.9]),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    env = base.check_device(
        Android=base.data_collation(type_kind='text', type_name=gl.get_value('ENV').upper()),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    version = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=f"my_current_version"),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_mobile'),
        iOS=base.data_collation(type_kind='value', type_name='请填入手机号码')
    )

    password = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_hint_password'),
        iOS=base.data_collation(type_kind='value', type_name='请填入密码')
    )

    login_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='login_login'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    register_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成注册'),
        iOS=base.data_collation(type_kind='name', type_name='完成注册')
    )

    hall = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='大厅'),
        iOS=base.data_collation(type_kind='name', type_name='大厅')
    )
    check_hall = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='抢单大厅'),
        iOS=base.data_collation(type_kind='name', type_name='抢单大厅')
    )

    my_buy = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_buy_lobby'),
        iOS=base.data_collation(type_kind='name', type_name='我要买')
    )

    my_sell = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='我要卖'),
        iOS=base.data_collation(type_kind='name', type_name='我要卖')
    )
    check_my_sell = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的挂单'),
        iOS=base.data_collation(type_kind='name', type_name='我的挂单')
    )

    promotions_pop = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='敬请注意'),
        iOS=base.data_collation(type_kind='name', type_name='优惠活动')
    )

    today_no_display = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='今日不再显示'),
        iOS=base.data_collation(type_kind='name', type_name='今日不再显示')
    )

    close_announcement = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=-7),
        iOS=base.data_collation(type_kind='name', type_name='我知道了')
    )

    grab_tutorial_text = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='抢单教程'),
        iOS=base.data_collation(type_kind='name', type_name='抢单教程')
    )

    grab_next_step = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='点选空白处跳至下一步骤'),
        iOS=base.data_collation(type_kind='name', type_name='点选空白处跳至下一步骤')
    )

    complete_grab_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成教程'),
        iOS=base.data_collation(type_kind='name', type_name='完成教程')
    )

    buy_tutorial_text = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='全新改款交易功能'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    deposit_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android.view.ViewGroup', num=2),
        iOS=base.data_collation(type_kind='name', type_name='充值')
    )

    want_buy_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_buy_lobby'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    want_sell_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_sell_lobby'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    check_want_buy = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='可用资产'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    service_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='客服'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    my_page_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='home_tab_title_my'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    check_my_page = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我的邀请码'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    back_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='back'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    receivecode_page = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='收款码'),
        iOS=base.data_collation(type_kind='name', type_name='收款码')
    )

    account_management_page = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号'),
        iOS=base.data_collation(type_kind='name', type_name='帐号')
    )

    # 绑定收付款方式
    bind_payment_page = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='my_bind_payment'),
        iOS=base.data_collation(type_kind='name', type_name='綁定收付款')
    )
    check_bind_payment = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='绑定收付款方式'),
        iOS=base.data_collation(type_kind='name', type_name='绑定收付款方式')
    )

    confirm_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成设置'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    set_pwd_message = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='支付密码设置成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    close = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='关闭'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    hints_see_immediately_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='立即查看'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    new_instructions_next_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='next_step'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    new_instructions_finish_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='complete_guide'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    new_logout_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='log_out'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    return_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='back'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    new_order_entry_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='订单入口'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    open_and_close_market_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='开市 / 休市切换'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 交易方式切换tutorial
    trade_switch_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='交易方式切换'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    # 下一个btn
    next_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='next'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


    place_order_immediately = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='.*开始挂单.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    i_known_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='ok'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    def set_deposit_pwd(self, num):
        set_deposit_pwd = MainPageLocator.base.check_device(
            Android=MainPageLocator.base.data_collation(type_kind='name', type_name='android.widget.EditText', num=num),
            iOS=MainPageLocator.base.data_collation(type_kind='', type_name='')
        )

        return set_deposit_pwd


class MainPage(Base):
    # 關閉登入公告/優惠活動
    def skip_announcement(self):
        for _ in range(3):
            if self.common.poco_exists(MainPageLocator.promotions_pop):
                self.common.poco_click(MainPageLocator.today_no_display)
                self.common.sleep(0.5)
                self.common.poco_click(MainPageLocator.close_announcement)
                break
            else:
                self.common.sleep(1)

    # 完成搶單教程
    def finish_grab_tutorial(self):
        self.common.poco_wait_exists(MainPageLocator.grab_next_step)
        for loop in range(0, 5):
            self.common.sleep(1)
            if self.common.poco_exists(MainPageLocator.grab_next_step):
                self.common.poco_click(MainPageLocator.grab_next_step)

        if self.common.poco_wait_exists(MainPageLocator.complete_grab_tutorial):
            self.common.poco_click(MainPageLocator.complete_grab_tutorial)

    # 完成我要買教程
    def finish_buy_tutorial(self):
        if self.common.poco_wait_exists(MainPageLocator.buy_tutorial_text) is False:
            raise EOFError('沒有跳出我要買教程')
        self.common.sleep(1)
        for loop in range(0, 5):
            if self.common.poco_exists(MainPageLocator.grab_next_step):
                self.common.poco_click(MainPageLocator.grab_next_step)
                self.common.sleep(0.5)
        if self.common.poco_exists(MainPageLocator.complete_grab_tutorial):
            self.common.poco_click(MainPageLocator.complete_grab_tutorial)

    def skip_buy_tutorial(self):
        if self.common.poco_wait_exists(MainPageLocator.buy_tutorial_text):
            self.common.sleep(1)
            for loop in range(0, 5):
                if self.common.poco_exists(MainPageLocator.grab_next_step):
                    self.common.poco_click(MainPageLocator.grab_next_step)
                    self.common.sleep(0.5)
            if self.common.poco_exists(MainPageLocator.complete_grab_tutorial):
                self.common.poco_click(MainPageLocator.complete_grab_tutorial)

    def check_version(self, version):
        now_version = self.common.poco_get_text(MainPageLocator.version)
        now_version = now_version.split('V')

        if version in now_version[1]:
            gl.set_value('version', True)
        else:
            gl.set_value('version', False)
            raise EOFError(f'版本錯誤, 目前版本:{now_version[1]}, 正確版本:{version}')

    # 設定安全密碼
    def set_first_deposit_pwd(self):
        if self.common.poco_exists(MainPageLocator.hall):
            self.common.poco_click(MainPageLocator.hall)
        self.common.sleep(1)
        if self.common.poco_wait_exists(MainPageLocator.confirm_btn):
            for i in range(0, 14):
                try:
                    self.common.poco_send_text(MainPageLocator.set_deposit_pwd(self, i), 0)
                except:
                    if i < 11:
                        raise EOFError('沒出現設置安全支付密碼頁面')
                    else:
                        break

        self.common.go_up()  # 為了關閉鍵盤
        self.common.go_up()  # 為了關閉鍵盤
        self.common.poco_click(MainPageLocator.confirm_btn)

        if self.common.poco_wait_exists(MainPageLocator.set_pwd_message):
            self.common.poco_click(MainPageLocator.close)
        else:
            raise EOFError('沒出現設置成功支付密碼頁面')

    # 確認熱更重啟
    # def app_update_and_restart(self):
    # if self.common.poco_exists(MainPageLocator.update):
    #         self.common.poco_click(MainPageLocator.update)

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查畫面上是否為登入
        self.common.sleep(2)
        if self.common.poco_exists(MainPageLocator.return_btn):
            self.common.poco_click(MainPageLocator.return_btn)
        self.common.sleep(2)
        if self.common.poco_exists(RegisterPageLocator.not_bind_payment_immediately_btn):
            self.common.poco_click(RegisterPageLocator.not_bind_payment_immediately_btn)

        if self.common.poco_exists(RegisterPageLocator.member_id):
            return True
        else:
            return False
        # for _ in range(3):
        #     if self.common.poco_exists(MainPageLocator.check_hall):
        #         return True
        #     elif self.common.poco_exists(MainPageLocator.login_button):
        #         return False
        #     else:
        #         self.skip_announcement()

    def check_open_app(self, status):
        self.check_login_status()

    def logout(self):
        # if self.common.poco_exists(MainPageLocator.return_btn):
        #     self.common.poco_click(MainPageLocator.return_btn)
        # if self.common.poco_exists(MainPageLocator.login_button):
        #     return
        # sleep(3)
        self.back_click()
        if self.common.poco_exists(MainPageLocator.hints_see_immediately_btn):
            self.common.poco_click(MainPageLocator.hints_see_immediately_btn)
        if self.common.poco_exists(RegisterPageLocator.not_bind_payment_immediately_btn):
            self.common.poco_click(RegisterPageLocator.not_bind_payment_immediately_btn)

        self.common.poco_click(MainPageLocator.my_page_pos)  # 我的 的位置，避免有彈窗遮住
        # if self.common.poco_exists(MainPageLocator.check_hall) is False:
        #     return
        sleep(1)
        if self.common.poco_exists(MainPageLocator.hints_see_immediately_btn):
            self.common.poco_click(MainPageLocator.hints_see_immediately_btn)

        # skip 全新改款交易說明所有頁面
        self.finish_new_change_transaction_instructions()

        self.poco.swipe([0.5, 0.5], [0.5, 0.1], duration=0.5)
        sleep(1)
        if self.common.poco_exists(MainPageLocator.new_logout_btn):
            self.common.poco_click(MainPageLocator.new_logout_btn)
        sleep(1)
        assert self.common.poco_exists(MainPageLocator.login_button), f"登出失敗"

        # if self.check_login_status():
        #     self.common.sleep(1)
        #     if self.common.poco_exists(MainPageLocator.grab_tutorial_text):
        #         self.finish_grab_tutorial()
        #
        #     # self.skip_announcement()
        #
        #     for i in range(2):
        #         if self.common.poco_wait_exists(MainPageLocator.my_page_btn):
        #             if self.common.poco_exists(MainPageLocator.logout):
        #                 self.common.poco_click(MainPageLocator.logout)
        #                 break
        #             else:
        #                 self.common.poco_click(MainPageLocator.my_page_btn)
        #                 if self.common.poco_wait_exists(MainPageLocator.logout):
        #                     self.common.sleep(1)
        #                     self.common.poco_click(MainPageLocator.logout)
        #                     break
        #
        #         if i == 2:
        #             raise EOFError('登出-點擊登出錯誤')
        # self.common.sleep(2)

    # 登入
    def login(self, account, password):
        self.common.sleep(1)
        if self.common.poco_exists(MainPageLocator.account):
            self.common.poco_send_text(MainPageLocator.account, account)
            sleep(1)
        if self.common.poco_exists(MainPageLocator.password):
            self.common.poco_send_text(MainPageLocator.password, password)
        if self.common.poco_exists(MainPageLocator.login_button):
            self.common.poco_click(MainPageLocator.login_button)
            sleep(2)

        if self.common.poco_exists(MainPageLocator.new_order_entry_tutorial):  # 當"訂單入口"tutorial跳出
            RegisterPage().finish_app_first_use_tutorial()

        # if self.common.poco_exists(MainPageLocator.grab_tutorial_text):
        #     self.finish_grab_tutorial()
        # self.skip_announcement()
        # self.skip_order_expire()

        if self.check_login_status() is False:
            raise EOFError('登入失敗')
        self.common.sleep(1)

    def into_register(self):
        if self.check_login_status() is True:
            self.logout()
        if self.common.poco_wait_exists(MainPageLocator.register):
            self.common.poco_click(MainPageLocator.register)
        else:
            raise EOFError('找不到註冊按鈕')

    # 進入大廳
    def hall_click(self):
        # self.skip_announcement()
        # self.skip_order_expire()
        # self.skip_order_confirm()
        # self.common.poco_click(MainPageLocator.hall_page_pos)
        self.common.poco_click(MainPageLocator.check_hall)
        self.common.sleep(1)
        for _ in range(2):
            if self.common.poco_exists(MainPageLocator.check_hall):
                break
            if self.common.poco_exists(MainPageLocator.hall):
                self.common.poco_click(MainPageLocator.hall)
                # self.common.sleep(1)
                # self.skip_announcement()
                # self.skip_order_expire()
                # self.skip_order_confirm()
        assert self.common.poco_wait_exists(MainPageLocator.check_hall, timeout=3), f"APP進入_搶單大廳_頁面失敗"
        if self.common.poco_exists(MainPageLocator.open_and_close_market_tutorial):
            self.finish_open_and_close_market_tutorial()
        # for i in range(3):
        #     if self.common.poco_exists(MainPageLocator.hall):
        #         self.common.poco_click(MainPageLocator.hall)
        #         self.common.sleep(3)
        #         self.skip_order_expire()
        #     else:
        #         if i == 2:
        #             raise EOFError('點擊大廳失敗')
        #         else:
        #             self.common.sleep(1)

    # 進入我要賣頁
    def sell_click(self, first=False):
        if self.common.poco_exists(MainPageLocator.want_sell_btn):
            self.common.poco_click(MainPageLocator.want_sell_btn)
            self.common.sleep(5)
        if not first:
            assert self.common.poco_wait_exists(MainPageLocator.check_my_sell, timeout=3), f"APP進入_我要賣_頁面失敗"

    # 進入存款頁
    def deposit_click(self, first=False):
        if self.common.poco_exists(MainPageLocator.deposit_btn):
            self.common.poco_click(MainPageLocator.deposit_btn)
        if self.common.poco_exists(MainPageLocator.promotions_pop):
            sleep(5)
            self.common.poco_click(MainPageLocator.close_announcement)
        if not first:
            assert self.common.poco_get_text(DepositPageLocator.recharge_title) == '充值资讯', f'充值頁顯示錯誤'
        # if self.common.poco_exists(DepositPageLocator.close):
        #     self.common.poco_click(DepositPageLocator.close)

    # 進入我要買頁
    def buy_click(self, first=False):
        if self.common.poco_exists(MainPageLocator.want_buy_btn):
            self.common.poco_click(MainPageLocator.want_buy_btn)
            self.common.sleep(1)
        # self.skip_order_confirm()
        if not first:
            self.finish_new_change_transaction_instructions()
            self.finish_trade_switch_tutorial()

            # assert self.common.poco_wait_exists(MainPageLocator.check_want_buy, timeout=3), f"APP進入_我要買_頁面失敗"

    # 進入客服
    def service_click(self):
        if self.common.poco_exists(MainPageLocator.service_btn):
            self.common.poco_click(MainPageLocator.service_btn)

    # 進入我的頁面
    def my_click(self):
        # self.common.poco_click(MainPageLocator.my_page_pos)  # 我的 的位置，避免有彈窗遮住
        if self.common.poco_exists(MainPageLocator.check_my_page):
            pass
        elif self.common.poco_exists(MainPageLocator.my_page_btn):
            self.common.poco_click(MainPageLocator.my_page_btn)
        assert self.common.poco_wait_exists(MainPageLocator.check_my_page, timeout=3), f"APP進入'我的'頁面失敗"

    # 返回
    def back_click(self, times=1):
        self.common.sleep(1)
        if self.common.poco_exists(MainPageLocator.back_btn):
            for _ in range(times):
                self.common.poco_click(MainPageLocator.back_btn)
                self.common.sleep(2)

    # 進入綁定收付款方式頁
    def bind_payment_click(self):
        if self.common.poco_exists(MainPageLocator.my_page_btn):
            self.common.poco_click(MainPageLocator.my_page_btn)
        if self.common.poco_exists(MainPageLocator.bind_payment_page):
            self.common.poco_click(MainPageLocator.bind_payment_page)
        self.common.sleep(1)
        assert self.common.poco_exists(MainPageLocator.check_bind_payment), f'進入綁定收付款方式頁失敗'

    def get_current_money(self):
        # self.skip_announcement()
        self.skip_order_confirm()
        self.common.poco_wait_exists(MainPageLocator.get_current_money, timeout=3)
        for i in range(3):
            current_money_str = self.common.poco_get_text(MainPageLocator.get_current_money)
            current_money_float = float(current_money_str.replace(",", ""))
            if current_money_float > 0:
                break
            else:
                print(f'第{i + 1}次，可用積分顯示{current_money_float}')
                self.my_click()
                self.hall_click()
                self.common.sleep(1)
        return current_money_float

    def check_money_correct(self, before_money, bonus, money):
        # bonus = (bonus + 100) /100
        # money = bonus * money
        count_bonus_money = self.calculate_bonus(money, bonus)
        self.my_click()
        self.hall_click()
        after_money = self.get_current_money()
        if format(after_money, '.2f') != format(before_money + float(count_bonus_money) + money, '.2f'):
            raise EOFError(
                f'充值金額不正確,請確認功能是否正常，充值前{before_money}，充值積分{money}，充值紅利{bonus}% {count_bonus_money}，充值後積分計算為{before_money + float(count_bonus_money) + money}，顯示為{after_money}')

    def get_current_money_for_sale(self):
        # self.skip_order_confirm()
        self.common.poco_wait_exists(MainPageLocator.get_current_money_for_sale, timeout=3)
        current_money_for_sale_str = self.common.poco_get_text(MainPageLocator.get_current_money_for_sale)
        current_money_for_sale_float = float(current_money_for_sale_str.replace(",", ""))
        return current_money_for_sale_float

    def check_money_for_sale_correct(self, before_money, trade_money):
        after_money = self.get_current_money_for_sale()
        if float(after_money) != float(before_money) + float(trade_money):
            raise EOFError(
                f'可用販售積分不正確, 請確認功能是否正常:  順付交易前:{before_money},  轉入金額:{trade_money},  交易後:{after_money}')

    def finish_new_change_transaction_instructions(self, first=False):  # finish全新改款交易功能說明
        if first:
            assert self.common.poco_exists(MainPageLocator.buy_tutorial_text), f'沒有跳出"全新改款交易功能"說明'
        if self.common.poco_exists(MainPageLocator.hints_see_immediately_btn):
            self.common.poco_click(MainPageLocator.hints_see_immediately_btn)
        while self.common.poco_exists(MainPageLocator.new_instructions_next_btn):
            self.common.poco_click(MainPageLocator.new_instructions_next_btn)
            sleep(0.5)
        if self.common.poco_exists(MainPageLocator.new_instructions_finish_btn):
            self.common.poco_click(MainPageLocator.new_instructions_finish_btn)

    def finish_open_and_close_market_tutorial(self, first=False):  # 開市/休市切換說明
        if first:
            assert self.common.poco_exists(
                MainPageLocator.open_and_close_market_tutorial), f'沒有跳出"開市/休市切換說明"說明'

        for _ in range(3):
            if self.common.poco_exists(MainPageLocator.new_instructions_next_btn):
                self.common.poco_click(MainPageLocator.new_instructions_next_btn)
                sleep(1)
        if self.common.poco_exists(MainPageLocator.place_order_immediately):
            sleep(1)
            self.common.poco_click(MainPageLocator.i_known_btn)

    def finish_trade_switch_tutorial(self):
        if self.common.poco_exists(MainPageLocator.trade_switch_tutorial):
            for _ in range(2):
                if self.common.poco_exists(MainPageLocator.next_btn):
                    self.common.poco_click(MainPageLocator.next_btn)
            if self.common.poco_exists(MainPageLocator.i_known_btn):
                self.common.poco_click(MainPageLocator.i_known_btn)