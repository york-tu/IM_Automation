from common.app.common import Common
from Project.exchange.app.pages.app.base import Base
from Project.exchange.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl
from Project.exchange.app.pages.app.app_bind_payment_page import BindPaymentPageLocator, BindPaymentPagePage


class MyInfoPageLocator:
    base = Xpath_Base()

    # 頁面title
    title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='会员资料'),
        iOS=base.data_collation(type_kind='name', type_name='会员资料')
    )

    # 手機號
    phone_number = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=4),  # HUAWEI_24: 5
        iOS=base.data_collation(type_kind='name', type_name='手机号')
    )

    # QQ帳號
    qq_account = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=6),  # HUAWEI_24: 7
        iOS=base.data_collation(type_kind='name', type_name='QQ账号')
    )

    # 姓名
    user_name = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=8),  # HUAWEI_24: 9
        iOS=base.data_collation(type_kind='name', type_name='姓名')
    )

    # 錢包地址
    wallet_address = base.check_device(
        Android=base.data_collation(type_kind='type', type_name='android.widget.TextView', num=10),  # HUAWEI_24: 11
        iOS=base.data_collation(type_kind='name', type_name='钱包地址')
    )

    # 修改登入密碼btn
    change_password_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='modify_password'),
        iOS=base.data_collation(type_kind='name', type_name='修改登入密码')
    )

    # 修改安全密码btn
    change_pay_password_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='modify_safe_password'),
        iOS=base.data_collation(type_kind='name', type_name='修改安全支付密码')
    )

    # 版本更新btn
    version_update_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='member_info_version_update'),
        iOS=base.data_collation(type_kind='name', type_name='版本更新')
    )

    # 舊的密碼
    old_password_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='modify_password_please_enter_old_password'),
        iOS=base.data_collation(type_kind='name', type_name='请输入旧密码')
    )

    # 新的密碼
    new_password_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_hint_password'),
        iOS=base.data_collation(type_kind='name', type_name='请输入8-16个字符')
    )

    # 再次輸入新的密碼
    new_password_again_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_hint_password', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='请输入8-16个字符')
    )

    # 舊的安全密碼
    old_pay_password_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input',num=0),
        iOS=base.data_collation(type_kind='name', type_name='请输旧的支付密码')
    )

    # 新的安全密碼
    new_pay_password_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input',num=1),
        iOS=base.data_collation(type_kind='name', type_name='请输入6个数字')
    )

    # 再次輸入新的安全密碼
    new_pay_password_again_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input',num=-1),
        iOS=base.data_collation(type_kind='name', type_name='请输入6个数字')
    )

    # 確定
    confirm_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='confirm_submit'),
        iOS=base.data_collation(type_kind='name', type_name='确认送出')
    )
    # 關閉彈窗
    close_pop_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='确定', action='parent().sibling()[0].child()'),
        iOS=base.data_collation(type_kind='name', type_name='确定')
    )
    # 密碼錯誤彈窗
    wrong_pwd_msg = base.check_device(
        Android=base.data_collation(type_kind='nameMatches', type_name='密码错误.*'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    error_null = base.check_device(
        Android=base.data_collation(type_kind='textMatches', type_name='请填写.*'),
        iOS=base.data_collation(type_kind='name', type_name='请填写.*')
    )
    error_ps = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号/密码错误'),
        iOS=base.data_collation(type_kind='name', type_name='帐号/密码错误')
    )

    error_pay_ps = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='原密码错误'),
        iOS=base.data_collation(type_kind='name', type_name='原密码错误')
    )

    #### logo page
    check_version = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='正在检查更新'),
        iOS=base.data_collation(type_kind='name', type_name='正在检查更新')
    )
    # 修改成功toast
    modify_succeed_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='修改成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

class MyInfoPage(Base):
    # 取得錢包地址
    def get_wallet_address(self):
        self.common.sleep(2)
        address = self.common.poco_get_text(MyInfoPageLocator.wallet_address)
        return address

    # 取得姓名
    def get_user_name(self):
        self.common.sleep(2)
        # phone_num = self.poco(type='android.widget.TextView')[4].attr('text')
        # QQ_num = self.poco(type='android.widget.TextView')[6].attr('text')
        # real_name = self.poco(type='android.widget.TextView')[8].attr('text')
        # address = self.poco(type='android.widget.TextView')[10].attr('text')
        name = self.common.poco_get_text(MyInfoPageLocator.user_name)
        return name

    # 取得手機號
    def get_phone_number(self):
        self.common.sleep(2)
        phone = self.common.poco_get_text(MyInfoPageLocator.phone_number)
        return phone

    # 取得QQ帳號
    def get_qq_account(self):
        self.common.sleep(2)
        qq_account = self.common.poco_get_text(MyInfoPageLocator.qq_account)
        return qq_account

    # 取得所有會員資料
    def get_all_info(self):
        phone = self.get_phone_number()
        qq = self.get_qq_account()
        name = self.get_user_name()
        address = self.get_wallet_address()
        info = {
            "phone": phone,
            "qq": qq,
            "name": name,
            "address": address
        }
        return info

    # 修改登入密碼
    def change_login_password(self, old_ps, new_ps, pay_password):
        self.common.sleep(2)
        self.common.poco_click(MyInfoPageLocator.change_password_btn)
        self.common.sleep(1)
        if self.common.poco_exists(BindPaymentPageLocator.pop_pay_password):
            BindPaymentPagePage.pay_password(self, pay_password)
            self.common.sleep(3)
        self.common.poco_send_text(MyInfoPageLocator.old_password_input, old_ps)
        self.common.poco_send_text(MyInfoPageLocator.new_password_input, new_ps)
        self.common.poco_send_text(MyInfoPageLocator.new_password_again_input, new_ps)
        self.common.poco_click(MyInfoPageLocator.confirm_button)
        assert self.common.poco_exists(MyInfoPageLocator.modify_succeed_msg)
        assert not self.common.poco_exists(MyInfoPageLocator.wrong_pwd_msg), f'未成功更改密碼'
        self.common.sleep(3)

        if self.common.poco_exists(MyInfoPageLocator.error_null):
            error_message = self.common.poco_get_text(MyInfoPageLocator.error_null)
            raise EOFError(f'修改登入密碼失敗 - {error_message}')
        if self.common.poco_exists(MyInfoPageLocator.error_ps):
            error_message = self.common.poco_get_text(MyInfoPageLocator.error_ps)
            raise EOFError(f'修改登入密碼失敗 - {error_message}')
        if self.common.poco_wait_exists(MyInfoPageLocator.version_update_btn) is False:
            raise EOFError('變更後未回到會員資料頁')

    # 修改安全支付密碼(目前僅確認顯示欄位)
    def change_pay_password(self, old_pay_ps, new_pay_ps):

        # if self.common.poco_exists(MyInfoPageLocator.old_pay_password_input) is False:
        #     raise EOFError(f'未顯示舊的安全支付密碼')
        # if self.common.poco_exists(MyInfoPageLocator.new_pay_password_input) is False:
        #     raise EOFError(f'未顯示新的安全支付密码')
        # if self.common.poco_exists(MyInfoPageLocator.new_pay_password_again_input) is False:
        #     raise EOFError(f'未顯示再次输入新的安全支付密码')

        for _ in range(3):
            self.common.poco_click(MyInfoPageLocator.change_pay_password_btn)
            self.common.sleep(2)
            self.common.poco_send_text(MyInfoPageLocator.old_pay_password_input, old_pay_ps)
            self.common.poco_send_text(MyInfoPageLocator.new_pay_password_input, new_pay_ps)
            self.common.poco_send_text(MyInfoPageLocator.new_pay_password_again_input, new_pay_ps)
            self.common.poco_click(MyInfoPageLocator.confirm_button)
            if self.common.poco_exists(MyInfoPageLocator.modify_succeed_msg):
                self.common.sleep(3)
                break

        # self.common.poco_click(MyInfoPageLocator.close_pop_button)

    # 版本更新
    def version_update(self):
        self.common.sleep(2)
        if self.common.poco_get_attr(MyInfoPageLocator.version_update_btn, 'enabled') == 'True':
            self.common.poco_click(MyInfoPageLocator.version_update_btn)
            self.common.poco_wait_exists(MyInfoPageLocator.check_version)
        else:
            return
