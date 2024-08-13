from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class DepositAilpayTransferPageLocator:
    base = Xpath_Base()

    @staticmethod
    def company_text(amount):
        company_text = DepositAilpayTransferPageLocator.base.check_device(
            Android = DepositAilpayTransferPageLocator.base.data_collation(type_kind='textMatches', type_name='.*公司入款.*', num=1),
            iOS = DepositAilpayTransferPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{amount}.*', num=1)
        )
        return company_text

    @staticmethod
    def bank_sort_napp(num):
        if num == 0:
            action = f'parent().child()[2].child()[{num}].child()[1]'
        else:
            action = f'parent().child()[2].child()[{num}].child()[0]'
        bank = DepositAilpayTransferPageLocator.base.check_device(
            Android = DepositAilpayTransferPageLocator.base.data_collation(type_kind='text', type_name='1.请选择转入银行并进行转账', action=action),
            iOS = DepositAilpayTransferPageLocator.base.data_collation(type_kind='name', type_name='1.请选择转入银行并进行转账', num=num)
        )
        return bank

    input_amount = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入存款金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入存款金额')
    )

    input_amount_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入转账金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入转账金额')
    )

    next_step = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='下一步'),
        iOS = base.data_collation(type_kind='name', type_name='下一步')
    )

    user_name = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请填写汇款人姓名'),
        iOS = base.data_collation(type_kind='name', type_name='请填写汇款人姓名')
    )

    user_name_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入真实姓名'),
        iOS = base.data_collation(type_kind='name', type_name='请输入真实姓名')
    )

    snapshot = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*transfer_snapshot_iv'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*transfer_snapshot_iv')
    )

    allow_camera = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*')
    )

    agree_camera = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='同意'),
        iOS = base.data_collation(type_kind='name', type_name='同意')
    )

    confirm_camera = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='確定'),
        iOS = base.data_collation(type_kind='name', type_name='確定')
    )

    take_from_camera = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='拍照'),
        iOS = base.data_collation(type_kind='name', type_name='拍照')
    )

    shutter_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*shutter_button.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*shutter_button.*')
    )

    camera_shutter = base.check_device(
        Android = base.data_collation(type_kind='desc', type_name='拍照'),
        iOS = base.data_collation(type_kind='desc', type_name='拍照')
    )

    done_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*done_button'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*done_button')
    )

    okay_button = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*okay'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*okay')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认提交'),
        iOS = base.data_collation(type_kind='name', type_name='确认提交')
    )
    
    success = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*成功.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*成功.*')
    )
    
    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='查看进度'),
        iOS = base.data_collation(type_kind='name', type_name='查看进度')
    )

    @staticmethod
    def company_text_napp():
        company_text = DepositAilpayTransferPageLocator.base.check_device(
            Android = DepositAilpayTransferPageLocator.base.data_collation(type_kind='textMatches', type_name='.*充值金额.*', num=0),
            iOS = DepositAilpayTransferPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*充值金额.*', num=0)
        )
        return company_text

    owner = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*开户人.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*开户人.*')
    )

    owner_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvAccountName'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvAccountName')
    )

    amount = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='amount'),
        iOS = base.data_collation(type_kind='name', type_name='amount')
    )
    
    name = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='name'),
        iOS = base.data_collation(type_kind='name', type_name='name')
    )
    
    record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='充值记录'),
        iOS = base.data_collation(type_kind='name', type_name='充值记录')
    )
    
    bank = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请选取您要转账的银行', action='parent().child()[2].child()'),
        iOS = base.data_collation(type_kind='name', type_name='请选取您要转账的银行', action='parent().child()[2].child()')
    )
    
    bank_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='1.请选择转入银行并进行转账', action='parent().child()[2].child()'),
        iOS = base.data_collation(type_kind='name', type_name='1.请选择转入银行并进行转账')
    )

    @staticmethod
    def deposit_sort(bank):
        deposit_sort = DepositAilpayTransferPageLocator.base.check_device(
            Android = DepositAilpayTransferPageLocator.base.data_collation(type_kind='textMatches', type_name=f'.*{bank}.*'),
            iOS = DepositAilpayTransferPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{bank}.*')
        )
        return deposit_sort

    @staticmethod
    def bank_sort(num):
        bank = DepositAilpayTransferPageLocator.base.check_device(
            Android = DepositAilpayTransferPageLocator.base.data_collation(type_kind='text', type_name='请选取您要转账的银行', action=f'parent().child()[2].child()[{num}]'),
            iOS = DepositAilpayTransferPageLocator.base.data_collation(type_kind='name', type_name='请选取您要转账的银行', num=num)
        )
        return bank

class DepositAilpayTransferPage(Base):
    def deposit_ailpay_transfer_amount(self, amount, name, bank):
        self.common.poco_click(DepositAilpayTransferPageLocator.deposit_sort(name))
        self.common.poco_wait_exists(DepositAilpayTransferPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositAilpayTransferPageLocator.deposit_sort(bank))
        
        self.common.poco_wait_exists(DepositAilpayTransferPageLocator.bank)
        len_bank = self.common.len_poco(DepositAilpayTransferPageLocator.bank)

        for i in range(0, len_bank):
            self.common.poco_click(DepositAilpayTransferPageLocator.bank_sort(i))

            if self.common.poco_get_text(DepositAilpayTransferPageLocator.owner) == '开户人：支付寶轉帳自動測試':
                break
            
            if i == (len_bank-1):
                raise EOFError('找不到對應銀行')

        self.common.poco_send_text(DepositAilpayTransferPageLocator.input_amount, amount)
        self.common.poco_click(DepositAilpayTransferPageLocator.next_step)
        self.common.poco_send_text(DepositAilpayTransferPageLocator.user_name, '機器人')

        for i in range(0, 5):
            if self.common.poco_exists(DepositAilpayTransferPageLocator.submit):
                self.common.poco_click(DepositAilpayTransferPageLocator.submit)
                break

            self.common.go_down()

            if i == 4:
                raise EOFError('找不到送出按鈕')
        
        if self.common.poco_exists(DepositAilpayTransferPageLocator.success):
            self.common.poco_click(DepositAilpayTransferPageLocator.confirm)
        else:
            raise EOFError('支付寶轉賬失敗')
       
        # 比對入款記錄
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositAilpayTransferPageLocator.company_text(amount))
            record_amount = recrod_message.replace('公司入款','').replace('.00元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError('存款金額與存款記錄不符')
        else:
            raise EOFError('沒有導向存款記錄頁') 
        
    def deposit_ailpay_transfer_amount_napp(self, amount, name, bank):
        self.common.poco_click(DepositAilpayTransferPageLocator.deposit_sort(name))
        self.common.poco_wait_exists(DepositAilpayTransferPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositAilpayTransferPageLocator.deposit_sort(bank))
        
        self.common.poco_wait_exists(DepositAilpayTransferPageLocator.bank_napp)
        len_bank = self.common.len_poco(DepositAilpayTransferPageLocator.bank_napp)

        for i in range(0, len_bank):
            self.common.poco_click(DepositAilpayTransferPageLocator.bank_sort_napp(i))
            self.common.sleep(0.5)

            if self.common.poco_get_text(DepositAilpayTransferPageLocator.owner_napp) == '开户人：支付寶轉帳自動測試':
                break
            
            if i == (len_bank-1):
                raise EOFError('找不到對應銀行')

        self.common.poco_send_text(DepositAilpayTransferPageLocator.input_amount_napp, amount)
        self.common.go_bottom()
        self.common.poco_click(DepositAilpayTransferPageLocator.next_step)
        self.common.poco_send_text(DepositAilpayTransferPageLocator.user_name_napp, '機器人')

        # 拍照
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.snapshot):
            self.common.poco_click(DepositAilpayTransferPageLocator.snapshot)
            
        while self.common.poco_wait_exists(DepositAilpayTransferPageLocator.allow_camera):
                self.common.poco_click(DepositAilpayTransferPageLocator.allow_camera)
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.confirm_camera):
            self.common.poco_click(DepositAilpayTransferPageLocator.confirm_camera)
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.take_from_camera):
            self.common.poco_click(DepositAilpayTransferPageLocator.take_from_camera)
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.agree_camera):
            self.common.poco_click(DepositAilpayTransferPageLocator.agree_camera)
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.allow_camera):
            self.common.poco_click(DepositAilpayTransferPageLocator.allow_camera)

        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.shutter_button):
            self.common.poco_click(DepositAilpayTransferPageLocator.shutter_button)
        if self.common.poco_exists(DepositAilpayTransferPageLocator.camera_shutter):
            self.common.poco_click(DepositAilpayTransferPageLocator.camera_shutter)

        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.done_button):
            self.common.poco_click(DepositAilpayTransferPageLocator.done_button)
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.okay_button):
            self.common.poco_click(DepositAilpayTransferPageLocator.okay_button)

        if self.common.poco_exists(DepositAilpayTransferPageLocator.submit):
            self.common.poco_click(DepositAilpayTransferPageLocator.submit)
        else:
            raise EOFError('拍照失敗')
        
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.success):
            self.common.poco_click(DepositAilpayTransferPageLocator.confirm)
        else:
            raise EOFError('支付寶轉賬失敗')
       
        # 比對入款記錄
        if self.common.poco_wait_exists(DepositAilpayTransferPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositAilpayTransferPageLocator.company_text_napp())
            record_amount = str(recrod_message).replace('充值金额 ','').replace('.00 元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError(f'存款金額與存款記錄不符,實際存款金額:{record_amount}')
        else:
            raise EOFError('沒有導向存款記錄頁') 

        self.common.keyevent('BACK')