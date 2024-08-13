from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl

class DepositCompanyPageLocator(Base):
    base = Xpath_Base()
    device_os = gl.get_value('PHONE_PLATFORM')
    
    @staticmethod
    def company_text(amount):
        company_text = DepositCompanyPageLocator.base.check_device(
            Android = DepositCompanyPageLocator.base.data_collation(type_kind='textMatches', type_name='.*公司入款.*', num=1),
            iOS = DepositCompanyPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{amount}.*', num=1)
        )
        return company_text

    owner = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='owner'),
        iOS = base.data_collation(type_kind='name', type_name='owner')
    )

    owner_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvAccountName'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvAccountName')
    )

    name = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='name'),
        iOS = base.data_collation(type_kind='name', type_name='name')
    )

    name_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入真实姓名'),
        iOS = base.data_collation(type_kind='name', type_name='请输入真实姓名')
    )

    amount = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='amount'),
        iOS = base.data_collation(type_kind='name', type_name='amount')
    )

    amount_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入实际转账金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入实际转账金额')
    )

    record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='充值记录'),
        iOS = base.data_collation(type_kind='name', type_name='充值记录')
    )

    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='查看进度'),
        iOS = base.data_collation(type_kind='name', type_name='Other', action='offspring("Other")[2]')
    )

    success = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*成功.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*成功.*')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*确认提交.*'),
        iOS = base.data_collation(type_kind='name', type_name=' 确认提交')
    )

    bank = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请填写您的转账资料', action='parent().child()[2].child()'),
        iOS = base.data_collation(type_kind='name', type_name='请填写您的转账资料')
    )

    bank_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='1.请选择转入银行并进行转账', action='parent().child()[2].child()'),
        iOS = base.data_collation(type_kind='name', type_name='1.请选择转入银行并进行转账')
    )

    next_step = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='下一步'),
        iOS = base.data_collation(type_kind='name', type_name='下一步')
    )

    @staticmethod
    def deposit_sort(bank):
        deposit_sort = DepositCompanyPageLocator.base.check_device(
            Android = DepositCompanyPageLocator.base.data_collation(type_kind='textMatches', type_name=f'.*{bank}.*'),
            iOS = DepositCompanyPageLocator.base.data_collation(type_kind='name', type_name=bank)
        )
        return deposit_sort
    
    @staticmethod
    def bank_sort(num):
        bank = DepositCompanyPageLocator.base.check_device(
            Android = DepositCompanyPageLocator.base.data_collation(type_kind='text', type_name='请填写您的转账资料', action=f'parent().child()[2].child()[{num}]'),
            iOS = DepositCompanyPageLocator.base.data_collation(type_kind='name', type_name='请填写您的转账资料', num=num)
        )
        return bank

    @staticmethod
    def bank_sort_napp(num):
        if num == 0:
            action = f'parent().child()[2].child()[{num}].child()[1]'
        else:
            action = f'parent().child()[2].child()[{num}].child()[0]'
        bank = DepositCompanyPageLocator.base.check_device(
            Android = DepositCompanyPageLocator.base.data_collation(type_kind='text', type_name='1.请选择转入银行并进行转账', action=action),
            iOS = DepositCompanyPageLocator.base.data_collation(type_kind='name', type_name='1.请选择转入银行并进行转账', num=num)
        )
        return bank

    @staticmethod
    def company_text_napp():
        company_text = DepositCompanyPageLocator.base.check_device(
            Android = DepositCompanyPageLocator.base.data_collation(type_kind='textMatches', type_name='.*充值金额.*', num=0),
            iOS = DepositCompanyPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*充值金额.*', num=0)
        )
        return company_text


class DepositCompanyPage(Base):
    def deposit_company_amount(self, amount, name, bank):
        self.common.poco_click(DepositCompanyPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositCompanyPageLocator.deposit_sort(bank))

        self.common.poco_wait_exists(DepositCompanyPageLocator.bank)
        len_bank = self.common.len_poco(DepositCompanyPageLocator.bank)

        for i in range(0, len_bank):
            self.common.poco_click(DepositCompanyPageLocator.bank_sort(i))

            if DepositCompanyPageLocator.device_os == 'iOS':
                break
            if self.common.poco_get_text(DepositCompanyPageLocator.owner) == '开户人：銀行自動測試':
                break
            
            if i == (len_bank-1):
                raise EOFError('找不到對應銀行')

        # 銀行入款的畫面比較長，先下拉到送出鈕後再回頭填資料，避免在小手機上找不到欄位
        for i in range(0, 5):
            if self.common.poco_exists(DepositCompanyPageLocator.submit):
                break

            self.common.go_down()

            if i == 4:
                raise EOFError('找不到送出按鈕')
            
        self.common.poco_send_text(DepositCompanyPageLocator.amount, amount)
        self.common.poco_send_text(DepositCompanyPageLocator.name, name)
        self.common.poco_click(DepositCompanyPageLocator.submit)

        if self.common.poco_wait_exists(DepositCompanyPageLocator.success):
            self.common.poco_click(DepositCompanyPageLocator.confirm)
        else:
            raise EOFError('公司入款失敗')

        # 比對入款記錄
        if self.common.poco_wait_exists(DepositCompanyPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositCompanyPageLocator.company_text(amount))
            record_amount = recrod_message.replace('公司入款','').replace('.00元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError('存款金額與存款記錄不符')
        else:
            raise EOFError('沒有導向存款記錄頁')

    def deposit_company_amount_napp(self, amount, name, bank):
        self.common.poco_click(DepositCompanyPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositCompanyPageLocator.deposit_sort(bank))

        self.common.poco_wait_exists(DepositCompanyPageLocator.bank_napp)
        len_bank = self.common.len_poco(DepositCompanyPageLocator.bank_napp)

        for i in range(0, len_bank):
            self.common.poco_click(DepositCompanyPageLocator.bank_sort_napp(i))
            self.common.sleep(0.5)

            if DepositCompanyPageLocator.device_os == 'iOS':
                break
            if self.common.poco_get_text(DepositCompanyPageLocator.owner_napp) == '开户人：銀行自動測試':
                break
            
            if i == (len_bank-1):
                raise EOFError('找不到對應銀行')

        self.common.poco_click(DepositCompanyPageLocator.next_step)
        self.common.sleep(0.5)
            
        self.common.poco_send_text(DepositCompanyPageLocator.amount_napp, amount)
        self.common.poco_send_text(DepositCompanyPageLocator.name_napp, name)
        self.common.poco_click(DepositCompanyPageLocator.submit)

        if self.common.poco_wait_exists(DepositCompanyPageLocator.success):
            self.common.poco_click(DepositCompanyPageLocator.confirm)
        else:
            raise EOFError('公司入款失敗')

        # 比對入款記錄
        if self.common.poco_wait_exists(DepositCompanyPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositCompanyPageLocator.company_text_napp())
            record_amount = str(recrod_message).replace('充值金额 ','').replace('.00 元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError(f'存款金額與存款記錄不符,實際存款金額:{record_amount}')
        else:
            raise EOFError('沒有導向存款記錄頁')
        
        self.common.keyevent('BACK')
