from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class DepositPageLocator:
    base = Xpath_Base()

    # amount = ('text','请输入充值金额')
    # name = ('text','请输入您的汇款卡姓名', -1)
    # confirm = ('text','确认送出')
    # submit_window = ('text','申请提交成功')
    # close_announcement = ('text','我知道了')
    close = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='complete_tutorial'),
        iOS=base.data_collation(type_kind='name', type_name='关闭')
    )

    amount = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入充值积分'),
        iOS=base.data_collation(type_kind='name', type_name='请输入充值积分')
    )

    deposit_name_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入您的汇款卡姓名'),
        iOS=base.data_collation(type_kind='name', type_name='请输入您的汇款卡姓名')
    )
    deposit_name = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入您的汇款卡姓名', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='请输入您的汇款卡姓名')
    )
    save_qrcode = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='保存到相册'),
        iOS=base.data_collation(type_kind='name', type_name='保存到相册')
    )

    confirm = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确认送出'),
        iOS=base.data_collation(type_kind='name', type_name='确认送出')
    )

    submit_window = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='申请提交成功'),
        iOS=base.data_collation(type_kind='name', type_name='申请提交成功')
    )

    close_announcement = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='我知道了'),
        iOS=base.data_collation(type_kind='name', type_name='我知道了')
    )

    tutorial_text = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='充值教程'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    grab_next_step = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='next_step'),
        iOS=base.data_collation(type_kind='name', type_name='点选空白处跳至下一步骤')
    )

    complete_grab_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成教程'),
        iOS=base.data_collation(type_kind='name', type_name='完成教程')
    )

    bonus = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='.*%.*', num=-1),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 充值資訊title
    recharge_title = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='recharge_title'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


class DepositPage(Base):
    def deposit(self, amount):
        self.common.sleep(1)

        if self.common.poco_exists(DepositPageLocator.amount):
            self.common.poco_click(DepositPageLocator.amount)
            self.common.poco_send_text(DepositPageLocator.amount, amount)
            self.common.poco_click(DepositPageLocator.bonus)
            self.common.sleep(2)
        if self.common.poco_exists(DepositPageLocator.deposit_name_title):
            self.common.poco_send_text(DepositPageLocator.deposit_name, '自動化充值')
        else:
            assert self.common.poco_wait_exists(DepositPageLocator.save_qrcode), f'未顯示充值二維碼'
        aaa = self.common.poco_get_text(DepositPageLocator.bonus)
        # bonus = float(((self.common.poco_get_text(DepositPageLocator.bonus)).split(' '))[0])
        bonus = float(self.common.poco_get_text(DepositPageLocator.bonus)[:-1])
        if self.common.poco_exists(DepositPageLocator.confirm):
            self.common.poco_click(DepositPageLocator.confirm)

        # 註冊成功視窗判斷
        if self.common.poco_wait_exists(DepositPageLocator.submit_window) is False:
            raise EOFError('充值失敗,請確認功能是否正常')

        return bonus

    # 完成充值教程
    def finish_deposit_tutorial(self, first=False):
        if first:
            if self.common.poco_wait_exists(DepositPageLocator.tutorial_text) is False:
                raise EOFError('沒有跳出充值教程')

        for loop in range(0, 5):
            if self.common.poco_exists(DepositPageLocator.grab_next_step):
                self.common.poco_click(DepositPageLocator.grab_next_step)
        if self.common.poco_exists(DepositPageLocator.complete_grab_tutorial):
            self.common.poco_click(DepositPageLocator.complete_grab_tutorial)
        if self.common.poco_exists(DepositPageLocator.close):
            self.common.poco_click(DepositPageLocator.close)

        self.common.sleep(3)
        assert self.common.poco_get_text(DepositPageLocator.recharge_title) == '充值资讯', f'充值頁顯示錯誤'

