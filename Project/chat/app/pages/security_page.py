from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import logging
import common.utils.globalvar as gl


class SecurityPageLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    @staticmethod
    def env(env):
        env = SecurityPageLocator.base.check_device(
            Android=SecurityPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=SecurityPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )

        return env

    popup_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS=base.data_collation(type_kind='name', type_name='ScrollView', pos=[0.5, 0.5474330357142857]),
    )

    popup_message = base.check_device(
        Android=base.data_collation(type_kind='name', type_name='android:id/message'),
        iOS=base.data_collation(type_kind='name', type_name='密码重设成功'),
    )

    id_value = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_id'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=2),
    )

    contact_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_contact_info'),
        iOS=base.data_collation(type_kind='type', type_name='StaticText', num=4),
    )

    password_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_setting_chevron'),
        iOS=base.data_collation(type_kind='name', type_name='更改密码'),
    )

    password_input_old = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写旧密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_originalPassword_textfield'),
    )

    password_input_new = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写新密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_newPassword_textfield'),
    )

    password_input_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请再次填写新密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_confirmPassword_textfield'),
    )

    submit_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成'),
        iOS=base.data_collation(type_kind='name', type_name='完成'),
    )


class SecurityPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def change_password(self, old_pwd, new_pwd):
        self.common.poco_click(SecurityPageLocator.password_button)

        if self.phone_platform.lower() == 'android':
            self.common.poco_send_text(SecurityPageLocator.password_input_old, old_pwd)
            self.common.poco_send_text(SecurityPageLocator.password_input_new, new_pwd)
            self.common.poco_send_text(SecurityPageLocator.password_input_check, new_pwd)
            self.common.poco_wait_exists(SecurityPageLocator.submit_button)
            assert self.common.poco_get_attr(SecurityPageLocator.submit_button, 'enabled'), f'更換密碼完成鍵disabled'
            self.common.poco_click(SecurityPageLocator.submit_button)
            self.common.poco_wait_exists(SecurityPageLocator.popup_message)
            assert self.common.poco_get_text(SecurityPageLocator.popup_message) == '密码重设成功', f'沒有跳出"密码重设成功"toast'
            self.common.poco_click(SecurityPageLocator.popup_button)
        else:  # ios
            self.common.poco_click(SecurityPageLocator.password_input_old)
            self.common.poco_send_text(SecurityPageLocator.password_input_old, old_pwd)
            self.common.poco_click(SecurityPageLocator.password_input_new)
            self.common.poco_send_text(SecurityPageLocator.password_input_new, new_pwd)
            self.common.poco_click(SecurityPageLocator.password_input_check)
            self.common.poco_send_text(SecurityPageLocator.password_input_check, new_pwd)
            self.common.poco_wait_exists(SecurityPageLocator.submit_button)
            assert self.common.poco_get_attr(SecurityPageLocator.submit_button, 'isEnabled') == '1', f'更換密碼完成鍵disabled'
            self.common.poco_click(SecurityPageLocator.submit_button)
            assert self.common.poco_get_attr(SecurityPageLocator.popup_message, 'value') == '密码重设成功', f'沒有跳出"密码重设成功"toast'
            self.common.poco_wait_exists(SecurityPageLocator.popup_message)
            assert self.common.poco_get_text(SecurityPageLocator.popup_message) == '密码重设成功', f'沒有跳出"密码重设成功"toast'
            self.common.poco_click(SecurityPageLocator.popup_button)

    def check_value(self, phone_mail, account_id, nation='CN', account_type='phone'):

        id_value = self.common.poco_get_text(SecurityPageLocator.id_value)
        contact_info = self.common.poco_get_text(SecurityPageLocator.contact_info)

        # if self.phone_platform.lower() == 'android':
        #
        # # ======================= ios scenario ==========================================
        # else:
        #     self.common.sleep(6)
        #     id_value = self.poco(type="StaticText")[1].attr('name')  # ID 值
        #     phone_value_and = self.common.poco_get_text(SecurityPageLocator.phone_value)
        #     phone_value = self.poco(type="StaticText")[3].attr('name')  # 手機號 值

        if account_type.lower() == 'phone':
            phone = ''
            if nation == 'TW':
                phone = '+886' + str(phone_mail)
            elif nation == "CN":
                phone = '+86' + str(phone_mail)
            elif nation == "JP":
                phone = '+81' + str(phone_mail)
            assert phone == contact_info, f'手機號有誤, 實際:{contact_info}, 預期:{phone_mail}'
        elif account_type.lower() == 'mail':
            assert phone_mail == contact_info, f'手機號有誤'
        assert account_id == id_value, f'會員帳號有誤'
