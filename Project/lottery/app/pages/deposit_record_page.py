from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class DeopsitRecordPageLocator:
   base = Xpath_Base()

   record_icon = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/btnRight'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/btnRight')
   )

   company = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='公司入款'),
      iOS = base.data_collation(type_kind='name', type_name='公司入款')
   )
    
   online = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='在线入款'),
      iOS = base.data_collation(type_kind='name', type_name='在线入款')
   )

   status = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='已入款'),
      iOS = base.data_collation(type_kind='name', type_name='已入款')
   )

   status_success = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='充值成功'),
      iOS = base.data_collation(type_kind='name', type_name='充值成功')
   )

   @staticmethod
   def company_trading_type(bank):
      if bank == '公司入款':
         trading_type = 'BANK'
      elif bank == '支付宝面对面扫码':
         trading_type = 'qrcode'
      elif bank == '支付宝转帐':
         trading_type = 'ALIPAY'
      company_trading_type = DeopsitRecordPageLocator.base.check_device(
         Android = DeopsitRecordPageLocator.base.data_collation(type_kind='text', type_name=trading_type),
         iOS = DeopsitRecordPageLocator.base.data_collation(type_kind='name', type_name=trading_type)
      )

      return company_trading_type

   company_card_number = base.check_device(
      Android = base.data_collation(type_kind='textMatches', type_name='充值卡号 ： .*'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='充值卡号 ： .*')
   )

   back = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='充值详情', action='parent().child()'),
      iOS = base.data_collation(type_kind='name', type_name='充值详情')
   )

   loading = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='处理中...'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*处理中*')
   )
   
   today = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='本日'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='公司入款.*', action='offspring("Other").child()')
   )

   @staticmethod
   def new(amount):
      new = DeopsitRecordPageLocator.base.check_device(
        Android = DeopsitRecordPageLocator.base.data_collation(type_kind='textMatches', type_name=f'公司入款.*元'),
        iOS = DeopsitRecordPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{amount}.*',num=1)
      )

      return new
   
   @staticmethod
   def new_record(amount):
      new_record = DeopsitRecordPageLocator.base.check_device(
        Android = DeopsitRecordPageLocator.base.data_collation(type_kind='textMatches', type_name=f'充值金额.*元',num=0),
        iOS = DeopsitRecordPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'.*{amount}.*',num=0)
      )

      return new_record

class DeopsitRecordPage(Base):
   def check_deposit_record(self, sort, amount):
      if not sort == '公司入款':
         self.common.poco_click(DeopsitRecordPageLocator.company)
         self.common.poco_wait_exists(DeopsitRecordPageLocator.online)
         
      for i in range(0, 21):
         self.common.poco_wait_exists(DeopsitRecordPageLocator.today)
         self.common.poco_click(DeopsitRecordPageLocator.today)
         self.common.poco_wait_disappearance(DeopsitRecordPageLocator.loading)
         self.common.poco_click(DeopsitRecordPageLocator.new(amount))

         if self.common.poco_exists(DeopsitRecordPageLocator.status) is True:
            break
         else:
            if i == 20:
               assert self.common.poco_exists(DeopsitRecordPageLocator.status) == True , '儲值狀態顯示錯誤'
            
            self.common.poco_click(DeopsitRecordPageLocator.back)
            self.common.sleep(2)

   def check_deposit_record_napp(self, sort, bank, amount):
      for i in range(0, 21):
         self.common.poco_click(DeopsitRecordPageLocator.record_icon)
         if not sort == '公司入款':
            self.common.poco_click(DeopsitRecordPageLocator.company)
            self.common.poco_wait_exists(DeopsitRecordPageLocator.online)

         self.common.poco_wait_exists(DeopsitRecordPageLocator.today)
         self.common.poco_click(DeopsitRecordPageLocator.today)
         self.common.poco_click(DeopsitRecordPageLocator.new_record(amount))

         if self.common.poco_exists(DeopsitRecordPageLocator.status_success):
            if self.common.poco_exists(DeopsitRecordPageLocator.company_trading_type(bank)):
               if self.common.poco_exists(DeopsitRecordPageLocator.company_card_number):
                  company_card_number = self.common.poco_get_text(DeopsitRecordPageLocator.company_card_number)
                  if str(company_card_number).replace('充值卡号 ： ','').replace(' ','') != '':
                     break
         else:
            if i == 20:
               assert self.common.poco_exists(DeopsitRecordPageLocator.status_success) == True , '儲值狀態顯示錯誤'
         
         self.common.keyevent('BACK')
         
