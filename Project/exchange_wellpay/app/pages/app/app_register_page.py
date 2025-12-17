from time import sleep
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class RegisterPageLocator:
    base = Xpath_Base()

    # phone_number = ('text','请输入手机号码')
    # qq_account = ('text','请输入QQ帐号，验证需要')
    # name = ('text','请输入真实姓名，验证需要')
    # password = ('text','请输入8-16个字符')
    # confirm_password = ('name','请输入8-16个字符')
    # invite_number = ('text','请输入邀请码(选填)')
    # register_button = ('text','完成注册')
    # check_register = ('text','帐户有资产后，可立即进行抢单。')
    # next_step = ('text','点选空白处跳至下一步骤')
    # complete_tutorial = ('text','完成教程')

    phone_number = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='手机号码'),
        iOS=base.data_collation(type_kind='name', type_name='手机号码')
    )

    next_step_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='下一步'),
        iOS=base.data_collation(type_kind='name', type_name='下一步')
    )

    qq_account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_qq'),
        iOS=base.data_collation(type_kind='name', type_name='请输入QQ帐号，验证需要')
    )

    name = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入真实姓名，验证需要'),
        iOS=base.data_collation(type_kind='name', type_name='请输入真实姓名，验证需要')
    )

    password = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='enter_hint_password'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    confirm_password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入 8-16 个字符'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    invite_number = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='signup_invite_code'),
        iOS=base.data_collation(type_kind='name', type_name='请输入邀请码(选填)')
    )

    register_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成注册'),
        iOS=base.data_collation(type_kind='name', type_name='完成注册')
    )

    check_register = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='注册成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    next_step = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='点选空白处跳至下一步骤'),
        iOS=base.data_collation(type_kind='name', type_name='点选空白处跳至下一步骤')
    )

    complete_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成教程'),
        iOS=base.data_collation(type_kind='name', type_name='完成教程')
    )

    sub_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='欢迎成为我们的会员'),
        iOS=base.data_collation(type_kind='name', type_name='欢迎成为我们的会员')
    )
    security_code = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    security_code_confirm = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    finish_setting_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='finish_setting'),
        iOS=base.data_collation(type_kind='name', type_name='安全設置')
    )
    # hint - 訂單入口 - 下一個
    hint_next_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='next'),
        iOS=base.data_collation(type_kind='text', type_name='下一个')
    )

    # 立即綁定出款方式彈窗 - "先不"鍵
    not_bind_payment_immediately_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='先不'),
        iOS=base.data_collation(type_kind='name', type_name='先不')
    )

    # 登入後首頁 - 會員編號
    member_id = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='member_id'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    trade_type_i_know_btn = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='ok'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )


class RegisterPage(Base):
    # 註冊
    def register(self, phone_number: str, password: str, invite_code=None, security_code=''):
        # for loop in range(0, 15):
        self.common.sleep(1)

        if self.common.poco_exists(RegisterPageLocator.phone_number):
            self.common.poco_send_text(RegisterPageLocator.phone_number, phone_number)
        self.common.sleep(0.5)
        if self.common.poco_exists(RegisterPageLocator.next_step_button):
            self.common.poco_click(RegisterPageLocator.next_step_button)
        self.common.sleep(1)

        # 註冊第二頁判斷
        if self.common.poco_exists(RegisterPageLocator.register_button) is False:
            raise EOFError('註冊沒有進入輸入資料頁')

        if self.common.poco_exists(RegisterPageLocator.qq_account):
            self.common.poco_send_text(RegisterPageLocator.qq_account, phone_number)
        self.common.sleep(0.5)
        if self.common.poco_exists(RegisterPageLocator.name):
            self.common.poco_send_text(RegisterPageLocator.name, '自動化測試註冊')
            self.common.sleep(0.5)
        if self.common.poco_exists(RegisterPageLocator.password):
            self.common.poco_send_text(RegisterPageLocator.password, password)
            self.common.sleep(0.5)
        if self.common.poco_exists(RegisterPageLocator.confirm_password):
            self.common.poco_send_text(RegisterPageLocator.confirm_password, password)
            self.common.sleep(0.5)

        # if self.common.poco_exists(RegisterPageLocator.invite_number):
        #     if invite_code is None:
        #         self.common.poco_click(RegisterPageLocator.invite_number)
        #         self.common.keyevent("ENTER")
        #     else:
        #         self.common.poco_send_text(RegisterPageLocator.invite_number, invite_code)

        if self.common.poco_exists(RegisterPageLocator.register_button):
            self.common.poco_click(RegisterPageLocator.register_button)

        # 設置安全密碼頁
        self.common.poco_click(RegisterPageLocator.security_code)
        self.common.poco_send_text(RegisterPageLocator.security_code, security_code)
        self.common.poco_click(RegisterPageLocator.security_code_confirm)
        self.common.poco_send_text(RegisterPageLocator.security_code_confirm, security_code)
        self.common.poco_click(RegisterPageLocator.finish_setting_btn)
        sleep(3)

        # skip所有說明
        self.finish_app_first_use_tutorial()

        # 註冊成功視窗判斷 - 看到會員帳號首頁
        if self.common.poco_wait_exists(RegisterPageLocator.member_id, timeout=5) is False:
            raise EOFError('沒有出現會員帳號首頁')

    def finish_app_first_use_tutorial(self):  # skip所有說明
        for _ in range(5):
            if self.common.poco_exists(RegisterPageLocator.hint_next_btn):
                self.common.poco_click(RegisterPageLocator.hint_next_btn)
                sleep(0.5)
        if self.common.poco_click(RegisterPageLocator.trade_type_i_know_btn):
            self.common.poco_click(RegisterPageLocator.trade_type_i_know_btn)
        if self.common.poco_click(RegisterPageLocator.not_bind_payment_immediately_btn):
            self.common.poco_click(RegisterPageLocator.not_bind_payment_immediately_btn)
            sleep(0.5)
