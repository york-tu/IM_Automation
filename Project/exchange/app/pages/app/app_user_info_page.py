from common.app.common import Common
from Project.exchange.app.pages.app.base import Base
from Project.exchange.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl

class UserInfoPageLocator:
    base = Xpath_Base()

    title = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='会员资料'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    phone = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='手机号'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    QQ = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='QQ账号'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    name = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='姓名'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    address = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='钱包地址'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    login_password = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='修改登入密码'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    security_password = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='修改安全支付密码'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

    version_update = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='版本更新'),
        iOS = base.data_collation(type_kind='', type_name='')
    )

class UserInfoPage(Base):

    def check_user_info(self):
        if self.common.poco_wait_exists(UserInfoPageLocator.title):
            if self.common.poco_exists(UserInfoPageLocator.phone) != True:
                raise EOFError('找不到手機號標題')
            if self.common.poco_exists(UserInfoPageLocator.phone) != True:
                raise EOFError('找不到QQ帳號標題')
            if self.common.poco_exists(UserInfoPageLocator.phone) != True:
                raise EOFError('找不到姓名標題')
            if self.common.poco_exists(UserInfoPageLocator.phone) != True:
                raise EOFError('找不到錢包地址標題')

    def change_login_password(self):
        if self.common.poco_wait_exists(UserInfoPageLocator.title):
            if self.common.poco_exists(UserInfoPageLocator.login_password) == True:
                pass
            else:
                raise EOFError('找不到修改登入密碼按鈕')
    
    def change_security_password(self):
        if self.common.poco_wait_exists(UserInfoPageLocator.title):
            if self.common.poco_exists(UserInfoPageLocator.security_password) == True:
                pass
            else:
                raise EOFError('找不到修改安全支付密碼按鈕')
    
    def version_update(self):
        if self.common.poco_wait_exists(UserInfoPageLocator.title):
            if self.common.poco_exists(UserInfoPageLocator.version_update) == True:
                pass
            else:
                raise EOFError('找不到版本更新按鈕')