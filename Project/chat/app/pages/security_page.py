from time import sleep
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.base_page import Base
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from Project.chat.app.pages.locators.base_locator import BaseLocator
import logging
import common.utils.globalvar as gl


class SecurityPageLocator(BaseLocator):
    """安全頁面 Locator，繼承 BaseLocator 以減少重複代碼"""
    # 明確引用基類屬性，確保 IDE/linter 能正確識別
    base = BaseLocator.base
    app_package = BaseLocator.app_package

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
        iOS=base.data_collation(type_kind='name', type_name='accountSecurity_id_label'),
    )

    contact_info = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/tv_contact_info'),
        iOS=base.data_collation(type_kind='name', type_name='accountSecurity_phone_label'),
    )

    password_button = base.check_device(
        Android=base.data_collation(type_kind='name', type_name=str(app_package) + ':id/iv_setting_chevron'),
        iOS=base.data_collation(type_kind='name', type_name='accountSecurity_password_cell'),
    )

    password_input_old = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写旧密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_originalPassword_textField'),
    )

    password_input_new = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请填写新密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_newPassword_textField'),
    )

    password_input_check = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='请再次填写新密码'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_confirmPassword_textField'),
    )

    submit_button = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='完成'),
        iOS=base.data_collation(type_kind='name', type_name='changePassword_submit_button'),
    )


class SecurityPage(Base):
    phone_platform = gl.get_value('PHONE_PLATFORM')

    def change_password(self, old_pwd, new_pwd):
        self.common.poco_click(SecurityPageLocator.password_button)

        if self.phone_platform.lower() == 'android':
            self.common.poco_send_text(SecurityPageLocator.password_input_old, old_pwd)

            self.common.poco_send_text(SecurityPageLocator.password_input_new, new_pwd)

            self.common.poco_send_text(SecurityPageLocator.password_input_check, new_pwd)

            self.common.poco_click(SecurityPageLocator.submit_button)
            sleep(5)
            assert self.common.poco_get_text(SecurityPageLocator.popup_message) == '密码重设成功', f'沒有跳出"密码重设成功"toast'
            self.common.poco_click(SecurityPageLocator.popup_button)
        else:  # ios
            self.common.poco_click(SecurityPageLocator.password_input_old)
            self.common.poco_send_text(SecurityPageLocator.password_input_old, old_pwd)
            
            self.common.poco_click(SecurityPageLocator.password_input_new)
            self.common.poco_send_text(SecurityPageLocator.password_input_new, new_pwd)
            
            self.common.poco_click(SecurityPageLocator.password_input_check)
            self.common.poco_send_text(SecurityPageLocator.password_input_check, new_pwd)

            self.common.poco_click(SecurityPageLocator.submit_button)
            sleep(5)
            assert self.common.poco_exists(SecurityPageLocator.popup_message), f'沒有跳出"密码重设成功"toast'
            self.common.poco_click(SecurityPageLocator.popup_button)

    def check_value(self, phone_mail, account_id, nation='CN', account_type='phone'):

        id_value = self.common.poco_get_text(SecurityPageLocator.id_value)
        contact_info = self.common.poco_get_text(SecurityPageLocator.contact_info)

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
