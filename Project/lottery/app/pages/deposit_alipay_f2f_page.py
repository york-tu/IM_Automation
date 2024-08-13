from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class DepositAilpayF2FPageLocator(Base):
    base = Xpath_Base()

    @staticmethod
    def company_text(amount):
        company_text = DepositAilpayF2FPageLocator.base.check_device(
            Android = DepositAilpayF2FPageLocator.base.data_collation(type_kind='textMatches', type_name='.*公司入款.*', num=1),
            iOS = DepositAilpayF2FPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{amount}.*', num=1)
        )
        return company_text

    next_step = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='下一步'),
        iOS = base.data_collation(type_kind='name', type_name='下一步')
    )

    input_amount = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入存款金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入存款金额')
    )

    input_amount_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入实际转账金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入实际转账金额')
    )

    input_order = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入交易单号后五码'),
        iOS = base.data_collation(type_kind='name', type_name='请输入交易单号后五码')
    )

    input_order_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入交易单号后5码'),
        iOS = base.data_collation(type_kind='name', type_name='请输入交易单号后5码')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='btnDepositSubmit'),
        iOS = base.data_collation(type_kind='name', type_name='btnDepositSubmit')
    )

    submit_napp = base.check_device(
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

    owner = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='owner'),
        iOS = base.data_collation(type_kind='name', type_name='owner')
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

    @staticmethod
    def deposit_sort(bank):
        deposit_sort = DepositAilpayF2FPageLocator.base.check_device(
            Android = DepositAilpayF2FPageLocator.base.data_collation(type_kind='textMatches', type_name=f'.*{bank}.*'),
            iOS = DepositAilpayF2FPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{bank}.*')
        )
        return deposit_sort

    @staticmethod
    def company_text_napp():
        company_text = DepositAilpayF2FPageLocator.base.check_device(
            Android = DepositAilpayF2FPageLocator.base.data_collation(type_kind='textMatches', type_name='.*充值金额.*', num=0),
            iOS = DepositAilpayF2FPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*充值金额.*', num=0)
        )
        return company_text

class DepositAilpayF2FPage(Base):
    def deposit_ailpay_f2f_amount(self, amount, order, name, bank):
        self.common.poco_click(DepositAilpayF2FPageLocator.deposit_sort(name))
        self.common.poco_wait_exists(DepositAilpayF2FPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositAilpayF2FPageLocator.deposit_sort(bank))
    
        self.common.poco_wait_exists(DepositAilpayF2FPageLocator.input_amount)
        self.common.poco_send_text(DepositAilpayF2FPageLocator.input_amount, amount)
        self.common.poco_send_text(DepositAilpayF2FPageLocator.input_order, order)
        self.common.poco_click(DepositAilpayF2FPageLocator.submit)

        if self.common.poco_exists(DepositAilpayF2FPageLocator.success):
            self.common.poco_click(DepositAilpayF2FPageLocator.confirm)
        else:
            raise EOFError('支付寶面對面入款失敗')

        # 比對入款記錄
        if self.common.poco_wait_exists(DepositAilpayF2FPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositAilpayF2FPageLocator.company_text(amount))
            record_amount = recrod_message.replace('公司入款','').replace('.00元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError('存款金額與存款記錄不符')
        else:
            raise EOFError('沒有導向存款記錄頁') 
        
    def deposit_ailpay_f2f_amount_napp(self, amount, order, name, bank):
        self.common.poco_click(DepositAilpayF2FPageLocator.deposit_sort(name))
        self.common.poco_wait_exists(DepositAilpayF2FPageLocator.deposit_sort(bank))
        self.common.poco_click(DepositAilpayF2FPageLocator.deposit_sort(bank))

        self.common.poco_click(DepositAilpayF2FPageLocator.next_step)
        self.common.sleep(0.5)

        self.common.poco_wait_exists(DepositAilpayF2FPageLocator.input_amount_napp)
        self.common.poco_send_text(DepositAilpayF2FPageLocator.input_amount_napp, amount)
        self.common.poco_send_text(DepositAilpayF2FPageLocator.input_order_napp, order)
        self.common.poco_click(DepositAilpayF2FPageLocator.submit_napp)

        if self.common.poco_wait_exists(DepositAilpayF2FPageLocator.success):
            self.common.poco_click(DepositAilpayF2FPageLocator.confirm)
        else:
            raise EOFError('支付寶面對面入款失敗')

        # 比對入款記錄
        if self.common.poco_wait_exists(DepositAilpayF2FPageLocator.record):
            recrod_message = self.common.poco_get_text(DepositAilpayF2FPageLocator.company_text_napp())
            record_amount = str(recrod_message).replace('充值金额 ','').replace('.00 元','')
            
            if not record_amount.__contains__(amount):
                raise EOFError(f'存款金額與存款記錄不符,實際存款金額:{record_amount}')
        else:
            raise EOFError('沒有導向存款記錄頁') 
        
        self.common.keyevent('BACK')