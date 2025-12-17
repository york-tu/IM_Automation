from time import sleep
from common.app.common import Common
from Project.exchange_wellpay.app.pages.app.base import Base
from Project.exchange_wellpay.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl
from random import choice, randint


class BindPaymentPageLocator:
    base = Xpath_Base()

    account_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='账号'),
        iOS=base.data_collation(type_kind='name', type_name='帐号')
    )

    check_account_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='绑定收款银行帐号'),
        iOS=base.data_collation(type_kind='name', type_name='绑定收款银行帐号')
    )

    qrcode_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='二维码'),
        iOS=base.data_collation(type_kind='name', type_name='二维码')
    )

    point_qrcode_tab = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='固定积分二维码'),
        iOS=base.data_collation(type_kind='name', type_name='固定积分二维码')
    )

    bank_transfer = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='银行转账'),
        iOS=base.data_collation(type_kind='name', type_name='银行转账')
    )

    wechat_transfer = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='微信转账', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='微信转账')
    )

    alipay_transfer = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='支付宝转账'),
        iOS=base.data_collation(type_kind='name', type_name='支付宝转账')
    )

    qq_transfer = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='QQ转账'),
        iOS=base.data_collation(type_kind='name', type_name='QQ转账')
    )

    unionpay_transfer = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='云闪付转账'),
        iOS=base.data_collation(type_kind='name', type_name='云闪付转账')
    )

    # 新增账号
    add_account = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='bind_payment_create_account'),
        iOS=base.data_collation(type_kind='name', type_name='新增帐号')
    )

    # 选择银行
    select_bank = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='account_manager_select_bank'),
        iOS=base.data_collation(type_kind='name', type_name='选择银行')
    )

    # 搜尋銀行: 请输入关键字或银行名称
    search_bank = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='bank_list_search'),
        iOS=base.data_collation(type_kind='name', type_name='搜寻银行')
    )

    # 銀行卡號欄位: 请填写银行卡号
    bank_card_input = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='account_manager_enter_bank_number'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    first_bank = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请选择', action='parent().parent().sibling()[1]'),
        iOS=base.data_collation(type_kind='name', type_name='请选择')
    )

    china_farming_bank = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='中国农业银行'),
        iOS=base.data_collation(type_kind='name', type_name='中国农业银行')
    )

    account = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号', num=-1),
        iOS=base.data_collation(type_kind='name', type_name='帐号')
    )

    # 微信绑定手机号
    wechat_number = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='account_manager_enter_wx'),
        iOS=base.data_collation(type_kind='name', type_name='微信绑定手机号')
    )

    account_number = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='account_manager_enter_other'),
        iOS=base.data_collation(type_kind='name', type_name='帐号')
    )

    store = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='储存'),
        iOS=base.data_collation(type_kind='name', type_name='储存')
    )

    bind_succeed_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='绑定成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    delete_succeed_msg = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='删除成功'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    verify = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='verify'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # "修改"
    transfer_modify = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='edit', num=0),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    # 綁定銀行"刪除"
    transfer_delete = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='delete'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    false_window_1 = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='帐号重复，请重新选择'),
        iOS=base.data_collation(type_kind='name', type_name='帐号重复，请重新选择')
    )
    false_window_2 = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='绑定数量超过可用银行卡数'),
        iOS=base.data_collation(type_kind='name', type_name='绑定数量超过可用银行卡数')
    )

    pop_pay_password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全密码'),
        iOS=base.data_collation(type_kind='', type_name='')
    )

    input_pay_password_1st = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[0]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )
    input_pay_password_2nd = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[1]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )
    input_pay_password_3rd = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[2]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )
    input_pay_password_4th = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[3]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )
    input_pay_password_5th = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[4]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )
    input_pay_password_6th = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请输入安全支付密码',
                                    action='sibling(name="android.widget.EditText")[5]'),
        iOS=base.data_collation(type_kind='name', type_name='输入安全支付密码')
    )

    security_code = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='code_input'),
        iOS=base.data_collation(type_kind='name', type_name='')
    )

    send_pay_password = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='送出'),
        iOS=base.data_collation(type_kind='name', type_name='送出')
    )
    pop_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='name', type_name='android:id/message')
    )
    bind_account_tutorial = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='选择默认账号'),
        iOS=base.data_collation(type_kind='', type_name='')
    )
    i_know_btn = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='知道了'),
        iOS=base.data_collation(type_kind='', type_name='')
    )



class BindPaymentPagePage(Base):

    def click_account_tab(self):
        if self.common.poco_exists(BindPaymentPageLocator.account_tab):
            self.common.poco_click(BindPaymentPageLocator.account_tab)
        self.common.sleep(1)
        if self.common.poco_exists(BindPaymentPageLocator.bind_account_tutorial):
            self.common.poco_click(BindPaymentPageLocator.i_know_btn)
        assert self.common.poco_exists(BindPaymentPageLocator.bank_transfer), f'轉帳頁未看到"银行转账"選項'
        assert self.common.poco_exists(BindPaymentPageLocator.wechat_transfer), f'轉帳頁未看到"微信转账"選項'
        assert self.common.poco_exists(BindPaymentPageLocator.alipay_transfer), f'轉帳頁未看到"支付宝转账"選項'
        # assert self.common.poco_exists(BindPaymentPageLocator.check_account_tab), f'進入绑定收款银行帐号tab失敗'

    def add_bank_transfer(self, pay_pwd, bank_name):
        # 因會阻擋重複卡號，固須不定時更新
        back_card_list = ['4870130722479460', '5459471640426639', '5183645798877403', '4041172759262348',
                          '5588947234652585', '4270284631804957', '5482594835309046', '4270393127549594',
                          '5309805207184812', '5105299620300385', '4270386176555751', '4910408596094702',
                          '4367689703106350', '4270280161924090', '4518048023803311', '5200820407522588',
                          '6227512304274432', '5583603053267592', '4910401884271306', '6858038501639587']
        bank_card = choice(back_card_list)

        if self.common.poco_exists(BindPaymentPageLocator.bank_transfer):
            self.common.poco_click(BindPaymentPageLocator.bank_transfer)
        else:
            raise EOFError('沒長出此項目, 檢查後台收款類型是否開啟')
        if self.common.poco_exists(BindPaymentPageLocator.add_account):  # 新增帳號
            self.common.poco_click(BindPaymentPageLocator.add_account)
        if self.common.poco_exists(BindPaymentPageLocator.select_bank):  # bank下拉選單
            self.common.poco_click(BindPaymentPageLocator.select_bank)
        if self.common.poco_exists(BindPaymentPageLocator.search_bank):
            self.common.poco_send_text(BindPaymentPageLocator.search_bank, bank_name) # 搜尋銀行
            sleep(3)
            self.poco(text=f'{bank_name}')[-1].click()
        # if self.common.poco_exists(BindPaymentPageLocator.first_bank):
        #     self.common.poco_click(BindPaymentPageLocator.first_bank)
        # self.common.poco_send_text(BindPaymentPageLocator.account, bank_card)
        self.common.poco_send_text(BindPaymentPageLocator.bank_card_input, bank_card)
        if self.common.poco_exists(BindPaymentPageLocator.verify):
            self.common.poco_click(BindPaymentPageLocator.verify)
        self.pay_password(pay_pwd)

        # 新增銀行卡成功視窗判斷
        for i in range(3):
            save_status = self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg)
            if save_status is True:
                break
            else:
                assert self.common.poco_exists(BindPaymentPageLocator.false_window_1) is False, "新增銀行帳號失敗: 銀行卡帐号重复，请重新选择"
                assert self.common.poco_exists(BindPaymentPageLocator.false_window_2) is False, "新增銀行帳號失敗: 绑定数量超过可用银行卡数"
                self.common.sleep(1)
        if save_status is False:
            raise EOFError('新增銀行帳號失敗,請確認功能是否正常')
        sleep(5)
        return bank_card

    def delete_recent_add_bank_transfer(self, pay_pwd, bank_card):
        if self.common.poco_exists(BindPaymentPageLocator.bank_transfer):
            self.common.poco_click(BindPaymentPageLocator.transfer_modify)
            if self.common.poco_exists(BindPaymentPageLocator.transfer_delete):
                self.common.poco_click(BindPaymentPageLocator.transfer_delete)
                self.pay_password(pay_pwd)
            self.common.sleep(3)
            assert not self.poco(text=f'{bank_card}').exists()
1
    def add_wechat_transfer(self, pay_pwd, wechat_number):

        if self.common.poco_exists(BindPaymentPageLocator.wechat_transfer):
            self.common.poco_click(BindPaymentPageLocator.wechat_transfer)
        else:
            raise EOFError('沒長出此項目, 檢查後台收款類型是否開啟')

        for _ in range(5):
            self.poco.swipe([0.5, 0.8], [0.5, 0.2], duration=0.5)
            # sleep(0.5)

        if self.common.poco_exists(BindPaymentPageLocator.add_account):
            self.common.poco_click(BindPaymentPageLocator.add_account)
        self.common.poco_send_text(BindPaymentPageLocator.wechat_number, wechat_number)
        if self.common.poco_exists(BindPaymentPageLocator.verify):
            self.common.poco_click(BindPaymentPageLocator.verify)
        self.pay_password(pay_pwd)

        # 新增銀行卡成功視窗判斷
        for i in range(3):
            save_status = self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg)
            if save_status is True:
                break
            else:
                self.common.sleep(1)
        if save_status is False:
            raise EOFError('新增微信轉帳失敗,請確認功能是否正常')
        sleep(5)

    def add_alipay_transfer(self, pay_pwd, alipay_number):
        if self.common.poco_exists(BindPaymentPageLocator.alipay_transfer):
            self.common.poco_click(BindPaymentPageLocator.alipay_transfer)
        else:
            raise EOFError('沒長出此項目, 檢查後台收款類型是否開啟')
        if self.common.poco_exists(BindPaymentPageLocator.add_account):
            self.common.poco_click(BindPaymentPageLocator.add_account)
        self.common.poco_send_text(BindPaymentPageLocator.account_number, alipay_number)
        if self.common.poco_exists(BindPaymentPageLocator.verify):
            self.common.poco_click(BindPaymentPageLocator.verify)
        self.pay_password(pay_pwd)

        # 新增銀行卡成功視窗判斷
        for i in range(3):
            save_status = self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg)
            if save_status is True:
                break
            else:
                self.common.sleep(1)
        if save_status is False:
            raise EOFError('新增支付寶轉帳失敗,請確認功能是否正常')
        sleep(5)

    def delete_recent_add_alipay_transfer(self, pay_pwd, alipay_number):
        if self.common.poco_exists(BindPaymentPageLocator.alipay_transfer):
            self.common.poco_click(BindPaymentPageLocator.transfer_modify)
            if self.common.poco_exists(BindPaymentPageLocator.transfer_delete):
                self.common.poco_click(BindPaymentPageLocator.transfer_delete)
                self.pay_password(pay_pwd)
            self.common.sleep(3)
            assert not self.poco(text=f'{alipay_number}').exists()

    def add_qq_transfer(self, pay_pwd, qq_number):
        if self.common.poco_exists(BindPaymentPageLocator.qq_transfer):
            self.common.poco_click(BindPaymentPageLocator.qq_transfer)
        else:
            raise EOFError('沒長出此項目, 檢查後台收款類型是否開啟')
        if self.common.poco_exists(BindPaymentPageLocator.add_account):
            self.common.poco_click(BindPaymentPageLocator.add_account)
        self.common.poco_send_text(BindPaymentPageLocator.account_number, qq_number)
        if self.common.poco_exists(BindPaymentPageLocator.store):
            self.common.poco_click(BindPaymentPageLocator.store)
        self.pay_password(pay_pwd)

        # 新增銀行卡成功視窗判斷
        for i in range(3):
            save_status = self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg)
            if save_status is True:
                break
            else:
                self.common.sleep(1)
        if save_status is False:
            raise EOFError('新增QQ轉帳失敗,請確認功能是否正常')

    def add_unionpay_transfer(self, pay_pwd, unionpay_number):
        if self.common.poco_exists(BindPaymentPageLocator.unionpay_transfer):
            self.common.poco_click(BindPaymentPageLocator.unionpay_transfer)
        else:
            raise EOFError('沒長出此項目, 檢查後台收款類型是否開啟')
        if self.common.poco_exists(BindPaymentPageLocator.add_account):
            self.common.poco_click(BindPaymentPageLocator.add_account)
        self.common.poco_send_text(BindPaymentPageLocator.account_number, unionpay_number)
        if self.common.poco_exists(BindPaymentPageLocator.store):
            self.common.poco_click(BindPaymentPageLocator.store)
        self.pay_password(pay_pwd)

        # 新增銀行卡成功視窗判斷
        for i in range(3):
            save_status = self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg)
            if save_status is True:
                break
            else:
                self.common.sleep(1)
        if save_status is False:
            raise EOFError('新增雲閃付轉帳失敗,請確認功能是否正常')

    # 輸入安全支付密碼彈窗
    def pay_password(self, pay_password):
        if self.common.poco_exists(BindPaymentPageLocator.pop_pay_password):
            # pay_password = str(pay_password)
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_1st, pay_password[0])
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_2nd, pay_password[1])
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_3rd, pay_password[2])
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_4th, pay_password[3])
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_5th, pay_password[4])
            # self.common.poco_send_text(BindPaymentPageLocator.input_pay_password_6th, pay_password[5])
            # self.common.poco_click(BindPaymentPageLocator.send_pay_password)
            self.common.poco_send_text(BindPaymentPageLocator.security_code, pay_password)
            # if not self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg):
            #     self.common.poco_wait_exists(BindPaymentPageLocator.bind_succeed_msg)
            #     assert self.common.poco_exists(BindPaymentPageLocator.bind_succeed_msg), f'銀行卡綁定失敗'

            if self.common.poco_exists(BindPaymentPageLocator.pop_message):
                message = self.common.poco_get_text(BindPaymentPageLocator.pop_message)
                raise EOFError(f'安全支付密碼驗證失敗, {message}')
        else:
            raise EOFError('未顯示輸入安全支付密碼彈窗')

