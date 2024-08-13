from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class FaqPageLocator :
    base = Xpath_Base()

    wechat = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='微信客服'),
        iOS = base.data_collation(type_kind='name', type_name='微信客服')
    )

    download_qrcode = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='点击下载二维码'),
        iOS = base.data_collation(type_kind='name', type_name='点击下载二维码')
    )

    qq = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='客服QQ'),
        iOS = base.data_collation(type_kind='name', type_name='客服QQ')
    )

    livechat = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='在线客服'),
        iOS = base.data_collation(type_kind='name', type_name='在线客服')
    )

    customer_service = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='站内客服'),
        iOS = base.data_collation(type_kind='name', type_name='站内客服')
    )

class FaqPage(Base):
    def wechat_exists(self):
        if self.common.poco_exists(FaqPageLocator.wechat):
            self.common.poco_click(FaqPageLocator.wechat)
        else:
            print('微信客服沒出現')
            return '微信客服沒出現'
            # raise EOFError('微信客服沒出現')
    
    def qq_exists(self):
        if self.common.poco_exists(FaqPageLocator.qq):
            self.common.poco_click(FaqPageLocator.qq)
        else:
            print('qq客服沒出現')
            return 'qq客服沒出現'
            # raise EOFError('QQ客服沒出現')

    def livechat_exists(self):
        if self.common.poco_exists(FaqPageLocator.livechat):
            self.common.poco_click(FaqPageLocator.livechat)
        else:
            print('在線客服沒出現')
            return '在線客服沒出現'
            # raise EOFError('在線客服沒出現')
    
    def customer_service_exists(self):
        if self.common.poco_exists(FaqPageLocator.customer_service):
            self.common.poco_click(FaqPageLocator.customer_service)
        else:
            print('站內客服沒出現')
            return '站內客服沒出現'
            # raise EOFError('站內客服沒出現')
    
    # --------------------------------新版-----------------------------------

    def wechat_exists_napp(self):
        if self.common.poco_exists(FaqPageLocator.wechat):
            self.common.poco_click(FaqPageLocator.wechat)
        else:
            print('微信客服沒出現')
            return False
        
        if self.common.poco_exists(FaqPageLocator.download_qrcode) == False:
            self.common.keyevent('BACK')
            return '未正常進入微信頁面'
        else:
            self.common.keyevent('BACK')
    
    def qq_exists_napp(self):
        if self.common.poco_exists(FaqPageLocator.qq):
            pass
        else:
            print('qq客服沒出現')
            return False

    def livechat_exists_napp(self):
        if self.common.poco_exists(FaqPageLocator.livechat):
            pass
        else:
            print('在線客服沒出現')
            return False
    
    def customer_service_exists_napp(self):
        if self.common.poco_exists(FaqPageLocator.customer_service):
            pass
        else:
            print('站內客服沒出現')
            return False
