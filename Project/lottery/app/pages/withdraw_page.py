from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class WithdrawPageLocator:
    base = Xpath_Base()

    bank_card =  base.check_device(
        Android = base.data_collation(type_kind='text', type_name='银行卡'),
        iOS = base.data_collation(type_kind='text', type_name='银行卡')
    )

    money = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='¥', action='parent().child()[1]'),
        iOS = base.data_collation(type_kind='name', type_name='¥', action='parent().child()[1]')
    )

    key = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请输入六位数字提款密码.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='请输入六位数字提款密码.*')
    )

    security_code = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android.widget.TextView'),
        iOS = base.data_collation(type_kind='name', type_name='android.widget.TextView')
    )

    edit_text = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android.widget.EditText'),
        iOS = base.data_collation(type_kind='name', type_name='android.widget.EditText')
    )

    edit_text_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入整数提款金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入整数提款金额')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认提交'),
        iOS = base.data_collation(type_kind='name', type_name='确认提交')
    )
    
    success = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='申请提交成功'),
        iOS = base.data_collation(type_kind='name', type_name='申请提交成功')
    )

    fail = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='申请提交失败'),
        iOS = base.data_collation(type_kind='name', type_name='申请提交失败')
    )

    fail_popup = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android:id/parentPanel'),
        iOS = base.data_collation(type_kind='name', type_name='android:id/parentPanel')
    )
    
    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认'),
        iOS = base.data_collation(type_kind='name', type_name='确认')
    )

    message = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='申请.*', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='申请.*', action='parent().child()[2]')
    )

    message_napp = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS = base.data_collation(type_kind='name', type_name='android:id/message')
    )

    withdraw_record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='在线提现'),
        iOS = base.data_collation(type_kind='name', type_name='在线提现')
    )

    withdraw_record_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='在线提款'),
        iOS = base.data_collation(type_kind='name', type_name='在线提款')
    )

    shortage = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*不足抵扣费用.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*不足抵扣费用.*')
    )

    above = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*提款限额.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*提款限额.*')
    )

    poor = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*余额不足.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*余额不足.*')
    )
    
    close_popup = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='关闭'),
        iOS = base.data_collation(type_kind='name', type_name='关闭')
    )

class WithdrawPage(Base):
    def bank_enter_click(self):
        self.wait_loading_finish()
        if self.common.poco_exists(WithdrawPageLocator.bank_card):
            self.common.poco_click(WithdrawPageLocator.bank_card)

    def withdraw(self, amount, secret):
        self.wait_loading_finish()
        self.common.poco_send_text(WithdrawPageLocator.edit_text, amount)
        self.common.go_bottom()
        
        if self.common.poco_exists(WithdrawPageLocator.key):
            self.common.poco_send_text(WithdrawPageLocator.key, secret)

        if self.common.poco_exists(WithdrawPageLocator.submit):
            self.common.poco_click(WithdrawPageLocator.submit)

        if self.common.poco_wait_exists(WithdrawPageLocator.confirm):
            # 申請成功
            if self.common.poco_wait_exists(WithdrawPageLocator.success):
                self.common.poco_click(WithdrawPageLocator.confirm)
                if not self.common.poco_exists(WithdrawPageLocator.withdraw_record):
                    raise EOFError('出款申請成功, 但頁面沒有倒轉至出款記錄頁')
                return amount
            # 申請失敗
            elif self.common.poco_exists(WithdrawPageLocator.fail):
                # 因為金額不足
                if self.common.poco_exists(WithdrawPageLocator.shortage):
                    message = self.common.poco_get_text(WithdrawPageLocator.shortage)
                    replace_1 = message.replace('提款金额', '')
                    replace_2 = replace_1.replace(str(amount), '', 1)
                    replace_3 = replace_2.replace('不足抵扣费用', '')
                    money = replace_3.replace('，无法申请', '')
                    amount = amount + int(float(money))
                    self.common.poco_click(WithdrawPageLocator.confirm)
                    self.withdraw(amount, secret)
                    return amount
                # 其他原因: 提款限额不符、主錢包錢不夠、不明原因
                else:
                    error_message = self.common.poco_get_text(WithdrawPageLocator.message)
                    raise EOFError(f'出款失敗-{error_message}')
            else:
                raise EOFError(f'彈窗訊息錯誤')
        
        else:
            raise EOFError('不明原因, 連彈窗都沒有')

    def withdraw_napp(self, amount, secret):
        self.wait_loading_finish()
        self.common.poco_send_text(WithdrawPageLocator.edit_text_napp, amount)
        self.common.go_bottom()
        
        if self.common.poco_exists(WithdrawPageLocator.edit_text):
            self.common.poco_send_text(WithdrawPageLocator.edit_text, secret)

        if self.common.poco_exists(WithdrawPageLocator.submit):
            self.common.poco_click(WithdrawPageLocator.submit)

        # 申請成功
        if self.common.poco_wait_exists(WithdrawPageLocator.withdraw_record_napp):
            return amount
        # 申請失敗
        elif self.common.poco_wait_exists(WithdrawPageLocator.fail_popup):
            # 因為金額不足
            if self.common.poco_exists(WithdrawPageLocator.poor):
                message = self.common.poco_get_text(WithdrawPageLocator.shortage)
                replace_1 = message.replace('提款金额', '')
                replace_2 = replace_1.replace(str(amount), '', 1)
                replace_3 = replace_2.replace('不足抵扣费用', '')
                money = replace_3.replace('，无法申请', '')
                amount = amount + int(float(money))
                self.common.poco_click(WithdrawPageLocator.close_popup)
                self.common.keyevent('BACK')
                self.bank_enter_click()
                self.withdraw_napp(amount, secret)
                return amount
            # 其他原因: 提款限额不符、主錢包錢不夠、不明原因
            else:
                error_message = self.common.poco_get_text(WithdrawPageLocator.message_napp)
                raise EOFError(f'出款失敗-{error_message}')
        else:
            raise EOFError(f'申請失敗或申請成功但沒有導頁')
        