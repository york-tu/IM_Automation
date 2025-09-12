import os, sys, glob, platform, shutil
from selenium import webdriver
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from Project.chat.configs.setting import SettingChat
import common.utils.globalvar as gl
from jira.module.base_module import UnittestModule


class BaseTestCase(UnittestModule):
    # CHROME SETTING
    wait_time = 20
    implicitly_wait_time = 35
    # driver = ''
    withdraw = '500'

    # TEST SETTING
    env = ''
    brand = ''
    user = ''
    account_type = ''

    # ACCOUNT SETTING
    web_url = ''
    web_account = ''
    web_password = ''
    web_phone = ''
    web_nation = ''
    wap_url = ''
    wap_account = ''
    wap_password = ''
    wap_phone = ''
    wap_nation = ''
    operate_account = ''
    operate_phone = ''
    admin_url = ''
    admin_account = ''
    admin_password = ''
    admin_otp = ''
    mail_account = ''
    mail_password = ''

    @classmethod
    def setting_test_data(cls):
        cls.env = gl.get_value('ENV')
        cls.brand = gl.get_value('BRAND')
        cls.user = gl.get_value('USER')
        cls.account_type = gl.get_value('ACCOUNT_TYPE')
        cls.wap_version = gl.get_value('PHONE_PLATFORM')

    # 登入帳號
        cls.web_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_url']
        cls.web_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_account']
        cls.web_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.web_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['web_phone']
        cls.web_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']

        cls.wap_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_url']
        cls.wap_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_account']
        cls.wap_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.wap_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['wap_phone']
        cls.wap_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']

        cls.app_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_account']
        cls.app_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']
        cls.app_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['app_phone']
        cls.app_nation = SettingChat().get_account(cls.env, cls.brand, cls.user)['nation']

        cls.mail_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['mail_account']
        cls.mail_address = SettingChat().get_account(cls.env, cls.brand, cls.user)['mail_address']
        cls.mail_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['password']

        cls.operate_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['operate_account']
        cls.operate_phone = SettingChat().get_account(cls.env, cls.brand, cls.user)['operate_phone']

        if not cls.env.__contains__('prod'):
            cls.admin_url = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_url']
            cls.admin_account = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_id']
            cls.admin_password = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_pwd']
            cls.admin_otp = SettingChat().get_account(cls.env, cls.brand, cls.user)['admin_otp']
            cls.low_rights_adm_id = SettingChat().get_account(cls.env, cls.brand, cls.user)['low_rights_admin_id']
            cls.low_rights_adm_pwd = SettingChat().get_account(cls.env, cls.brand, cls.user)['low_rights_admin_pwd']
