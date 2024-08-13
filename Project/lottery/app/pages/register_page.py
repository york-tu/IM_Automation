import random
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class RegisterPageLocator:
    base = Xpath_Base()

    account = base.data_collation(type_kind='text', type_name='请设定您的账号')
    password = base.data_collation(type_kind='text', type_name='请设定您的密码')
    confirm_password = base.data_collation(type_kind='text', type_name='请再输入一次密码')
    account_name = base.data_collation(type_kind='text', type_name='请输入您的真实姓名')
    security_password = base.data_collation(type_kind='text', type_name='请设定交易提款密码')
    email = base.data_collation(type_kind='text', type_name='请输入邮箱地址')
    
    qq_account = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入QQ号码'),
        iOS = base.data_collation(type_kind='name', type_name='请输入QQ号码')
    )
    
    wechat_account = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请输入微信账号.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='请输入微信账号.*')
    )
    
    recommend_person = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入推荐人'),
        iOS = base.data_collation(type_kind='name', type_name='请输入推荐人')
    )

    phone_num = base.data_collation(type_kind='text', type_name='请输入手机号码')
    check_register = base.data_collation(type_kind='name', type_name='btnSendRegister')
    check_box = base.data_collation(type_kind='name', type_name='android.widget.ImageView', num=-1)
    
    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认'),
        iOS = base.data_collation(type_kind='name', type_name='确认')
    )
    
    phone_duplicate = base.data_collation(type_kind='text', type_name='号码已被注册')
    phone_confirm = base.data_collation(type_kind='text', type_name='确定')
    
    @staticmethod
    def phone_text(phone_number):
        phone_input = RegisterPageLocator.base.check_device(
            Android = RegisterPageLocator.base.data_collation(type_kind='text', type_name=phone_number),
            iOS = RegisterPageLocator.base.data_collation(type_kind='name', type_name=phone_number)
        )
        return phone_input

    account_napp = base.data_collation(type_kind='text', type_name='账号')
    password_napp = base.data_collation(type_kind='text', type_name='密码')
    confirm_password_napp = base.data_collation(type_kind='text', type_name='确认密码')
    account_name_napp = base.data_collation(type_kind='text', type_name='真实姓名')
    security_password_napp = base.data_collation(type_kind='text', type_name='提款密码')
    phone_num_napp = base.data_collation(type_kind='text', type_name='手机号码')
    email_napp = base.data_collation(type_kind='text', type_name='电子邮箱')
    
    qq_account_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='QQ号码'),
        iOS = base.data_collation(type_kind='name', type_name='QQ号码')
    )
    
    wechat_account_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='微信账号'),
        iOS = base.data_collation(type_kind='name', type_name='微信账号')
    )
    
    recommend_person_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='邀请码'),
        iOS = base.data_collation(type_kind='name', type_name='邀请码')
    )

    check_register_napp = base.data_collation(type_kind='nameMatches', type_name='.*tv_alert_hint')     # 錯誤提示
    close_popup = base.data_collation(type_kind='text', type_name='关闭')
    register_button = base.data_collation(type_kind='nameMatches', type_name='.*btn_submit_register')
    close_lucky_wheel = base.data_collation(type_kind='nameMatches', type_name='.*iv_close')
    go_homepage = base.data_collation(type_kind='nameMatches', type_name='.*id/btnRight')       # 前往遊戲
    homepage = base.data_collation(type_kind='text', type_name='首页')       # 前往遊戲

class RegisterPage(Base):
    # 註冊
    def register(self, account:str, password:str):
        phone_number = str(135) + str(random.randrange(10000000, 99999999))
        for loop in range(0, 15):
            self.common.sleep(1)
            
            if self.common.poco_exists(RegisterPageLocator.account):
                self.common.poco_send_text(RegisterPageLocator.account,account)
            if self.common.poco_exists(RegisterPageLocator.password):
                self.common.poco_send_text(RegisterPageLocator.password,password)
            if self.common.poco_exists(RegisterPageLocator.confirm_password):
                self.common.poco_send_text(RegisterPageLocator.confirm_password,password)
            if self.common.poco_exists(RegisterPageLocator.account_name):
                self.common.poco_send_text(RegisterPageLocator.account_name, '我')
            if self.common.poco_exists(RegisterPageLocator.security_password):
                self.common.poco_send_text(RegisterPageLocator.security_password, '111111')
            if self.common.poco_exists(RegisterPageLocator.email):
                self.common.poco_send_text(RegisterPageLocator.email, 'test1234@paradise-soft.com.tw')
            if self.common.poco_exists(RegisterPageLocator.qq_account):
                self.common.poco_send_text(RegisterPageLocator.qq_account, '12345')
            if self.common.poco_exists(RegisterPageLocator.wechat_account):
                self.common.poco_send_text(RegisterPageLocator.wechat_account, 'test1234')
            if self.common.poco_exists(RegisterPageLocator.recommend_person):
                self.common.poco_send_text(RegisterPageLocator.recommend_person, 'APP測試')
            if self.common.poco_exists(RegisterPageLocator.phone_num):
                self.common.poco_send_text(RegisterPageLocator.phone_num, phone_number)
 
            
            # 勾選服務條款
            if self.common.poco_exists(RegisterPageLocator.check_register):
                self.common.poco_click(RegisterPageLocator.check_box)

                if self.common.poco_exists(RegisterPageLocator.check_register):
                    self.common.poco_click(RegisterPageLocator.check_register)
                    self.phone_number_duplicate(phone_number)
                    break
                else:
                    self.common.go_down()
                    self.common.poco_click(RegisterPageLocator.check_register)
                    self.phone_number_duplicate(phone_number)
                    break
            else:
                self.common.go_down()

                if loop == 14:
                    raise EOFError('註冊失敗')
        
        # 註冊成功視窗判斷
        if self.common.poco_wait_exists(RegisterPageLocator.confirm):
            self.common.poco_click(RegisterPageLocator.confirm)
        else:
            raise EOFError('沒有出現註冊成功彈窗')

    # 遇到手機號碼重複時重給一組號碼
    def phone_number_duplicate(self, phone_number):
        while self.common.poco_exists(RegisterPageLocator.phone_duplicate):
            self.common.poco_click(RegisterPageLocator.phone_confirm)
            self.common.sleep(1)
            phone_number_new = str(135) + str(random.randrange(10000000, 99999999))
            self.common.poco_send_text(RegisterPageLocator.phone_text(phone_number), phone_number_new)
            phone_number = phone_number_new
            self.common.poco_click(RegisterPageLocator.check_register)
    
    # 註冊
    def register_napp(self, account:str, password:str):
        phone_number = str(13) + str(random.randrange(100000000, 999999999))
        for loop in range(0, 10):
            self.common.sleep(1)
            
            if self.common.poco_exists(RegisterPageLocator.account_napp):
                self.common.poco_send_text(RegisterPageLocator.account_napp,account)
            if self.common.poco_exists(RegisterPageLocator.password_napp):
                self.common.poco_send_text(RegisterPageLocator.password_napp,password)
            if self.common.poco_exists(RegisterPageLocator.confirm_password_napp):
                self.common.poco_send_text(RegisterPageLocator.confirm_password_napp,password)
            if self.common.poco_exists(RegisterPageLocator.account_name_napp):
                self.common.poco_send_text(RegisterPageLocator.account_name_napp, '我')
            if self.common.poco_exists(RegisterPageLocator.security_password_napp):
                self.common.poco_send_text(RegisterPageLocator.security_password_napp, '111111')
            if self.common.poco_exists(RegisterPageLocator.phone_num_napp):
                # self.common.swipe(RegisterPageLocator.phone_num_napp)
                self.common.poco_send_text(RegisterPageLocator.phone_num_napp, phone_number)
            data = {'pos':(0.5, 0.5, 0.5, 0.2)}
            self.common.swipe(data)
            if self.common.poco_exists(RegisterPageLocator.email_napp):
                self.common.poco_send_text(RegisterPageLocator.email_napp, 'test1234@paradise-soft.com.tw')
            if self.common.poco_exists(RegisterPageLocator.qq_account_napp):
                # self.common.swipe(RegisterPageLocator.qq_account_napp)
                self.common.poco_send_text(RegisterPageLocator.qq_account_napp, '12345')
            if self.common.poco_exists(RegisterPageLocator.wechat_account_napp):
                self.common.poco_send_text(RegisterPageLocator.wechat_account_napp, 'test1234')
            if self.common.poco_exists(RegisterPageLocator.recommend_person_napp):
                self.common.poco_send_text(RegisterPageLocator.recommend_person_napp, 'default_agent')
            if self.common.poco_exists(RegisterPageLocator.register_button):
                self.common.poco_click(RegisterPageLocator.register_button)

            if self.common.poco_exists(RegisterPageLocator.check_register_napp):
                pass
            elif self.common.poco_exists(RegisterPageLocator.close_popup):
                if self.common.poco_exists(RegisterPageLocator.phone_duplicate):
                    self.phone_number_duplicate(phone_number)
                    break
                else:
                    self.common.poco_click(RegisterPageLocator.close_popup)
                    account = str(random.randrange(00000, 999999999))
            elif self.common.poco_exists(RegisterPageLocator.close_lucky_wheel):
                self.common.poco_click(RegisterPageLocator.close_lucky_wheel)
                break
            elif self.common.poco_exists(RegisterPageLocator.go_homepage):
                self.common.poco_click(RegisterPageLocator.go_homepage)
                break
            elif self.common.poco_exists(RegisterPageLocator.homepage):
                self.common.poco_click(RegisterPageLocator.homepage)
                break

            self.common.go_up()
            if loop == 9:
                raise EOFError('註冊失敗')

    # 遇到手機號碼重複時重給一組號碼
    def phone_number_duplicate_napp(self, phone_number):
        while self.common.poco_exists(RegisterPageLocator.phone_duplicate):
            self.common.poco_click(RegisterPageLocator.close_popup)
            self.common.sleep(1)
            phone_number_new = str(13) + str(random.randrange(100000000, 999999999))
            self.common.poco_send_text(RegisterPageLocator.phone_text(phone_number), phone_number_new)
            phone_number = phone_number_new
            self.common.poco_click(RegisterPageLocator.register_button)