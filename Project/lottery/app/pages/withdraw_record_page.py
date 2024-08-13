from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class WithdrawRecordPageLocator:
   base = Xpath_Base()

   today = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='本日'),
      iOS = base.data_collation(type_kind='name', type_name='本日')
   )

   week = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='本周'),
      iOS = base.data_collation(type_kind='name', type_name='本周')
   )

   company = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='公司入款'),
      iOS = base.data_collation(type_kind='name', type_name='公司入款')
   )

   online = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='在线入款'),
      iOS = base.data_collation(type_kind='name', type_name='在线入款')
   )
   
   new = base.check_device(
      Android = base.data_collation(type_kind='textMatches', type_name='在线提现.*元'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='在线提现.*元')
   )

   new_record = base.check_device(
      Android = base.data_collation(type_kind='textMatches', type_name='在线提款.*元'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='在线提款.*元')
   )

   status = base.check_device(
      Android = base.data_collation(type_kind='textMatches', type_name='出款成功.*'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='出款成功.*')
   )

   first_status = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvStatusLabel'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvStatusLabel')
   )

   withdraw_status = base.check_device(
      Android = base.data_collation(type_kind='textMatches', type_name='提现状态.*', action='parent().child()[1]'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='提现状态.*', action='parent().child()[1]')
   )

   back = base.check_device(
      Android = base.data_collation(type_kind='text', type_name='提款详情', action='parent().child()'),
      iOS = base.data_collation(type_kind='name', type_name='提款详情')
   )

   before_charge = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandBeforeChargeAmountValue'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandBeforeChargeAmountValue')
   )

   after_charge = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandAfterChargeAmountValue'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandAfterChargeAmountValue')
   )

   withdraw_type = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandTransTypeValue'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandTransTypeValue')
   )

   withdraw_card = base.check_device(
      Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandChargeCardNumber'),
      iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvExpandChargeCardNumber')
   )

class WithdrawRecordPage(Base):
   def check_withdraw_record(self):      
      for i in range(0, 21):
         self.common.poco_wait_exists(WithdrawRecordPageLocator.today)
         self.common.poco_click(WithdrawRecordPageLocator.today)
         self.common.poco_click(WithdrawRecordPageLocator.new)

         if self.common.poco_exists(WithdrawRecordPageLocator.status) is True:
            break
         else:
            if i == 20:
               assert self.common.poco_exists(WithdrawRecordPageLocator.status) == True , '出款狀態顯示錯誤'
            
            self.common.keyevent('BACK')
            self.common.sleep(2)
   
   def check_withdraw_record_napp(self):      
      for i in range(0, 21):
         if self.common.poco_exists(WithdrawRecordPageLocator.first_status) == True:      # 有時候紀錄不會馬上出現
            if self.common.poco_get_text(WithdrawRecordPageLocator.first_status) == '出款成功':
               break
            else:
               if i == 20:
                  assert self.common.poco_get_text(WithdrawRecordPageLocator.first_status) == '出款成功', '出款狀態顯示錯誤'
            
         self.common.sleep(2)
         self.common.poco_click(WithdrawRecordPageLocator.week)
         self.common.poco_click(WithdrawRecordPageLocator.today)
         
      self.common.poco_click(WithdrawRecordPageLocator.new_record)
      assert self.common.poco_get_text(WithdrawRecordPageLocator.before_charge) != '', '提款前金額未顯示'
      assert self.common.poco_get_text(WithdrawRecordPageLocator.after_charge) != '', '提款後金額未顯示'
      assert self.common.poco_get_text(WithdrawRecordPageLocator.withdraw_type) != '', '提款銀行未顯示'
      assert self.common.poco_get_text(WithdrawRecordPageLocator.withdraw_card) != '', '提款銀行未顯示'