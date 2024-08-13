from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class MailCenterPageLocator :
    base = Xpath_Base()
    
    center = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='通知中心'),
        iOS = base.data_collation(type_kind='name', type_name='通知中心')
    )

    my_mail = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='我的讯息'),
        iOS = base.data_collation(type_kind='name', type_name='我的讯息')
    )

    read_mail = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*id/tvHideMsgTitle'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/tvHideMsgTitle')
    )

    button_left = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*id/btnLeft'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/btnLeft')
    )

    delete_mail = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*id/ivHideRemoveIcon'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*id/ivHideRemoveIcon')
    )

    delete_confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认'),
        iOS = base.data_collation(type_kind='name', type_name='确认')
    )

class MailCenterPage(Base):
    def center_exists(self):
        if not self.common.poco_wait_exists(MailCenterPageLocator.center):
            raise EOFError('進入通知中心錯誤')
    
    def mail_center_exists(self):
        if not self.common.poco_wait_exists(MailCenterPageLocator.my_mail):
            raise EOFError('進入我的訊息錯誤')
    
    # 讀完刪除站內信，以免之後一直跳未讀彈窗
    def mail_read_delete(self):
        if self.common.poco_exists(MailCenterPageLocator.read_mail):
            self.common.poco_click(MailCenterPageLocator.read_mail)
            self.common.poco_click(MailCenterPageLocator.button_left)
        while self.common.poco_wait_exists(MailCenterPageLocator.delete_mail):
            self.common.poco_click(MailCenterPageLocator.delete_mail)
            self.common.poco_click(MailCenterPageLocator.delete_confirm)
