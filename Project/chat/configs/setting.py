import os, sys
from common.utils.path_utils import PathUtils
from common.utils.config_loader import ConfigLoader
import common.utils.globalvar as gl

# 使用 PathUtils 添加專案根目錄到 sys.path
path_utils = PathUtils()
project_root = str(path_utils.get_project_root())
if project_root not in sys.path:
    sys.path.append(project_root)

# 使用 ConfigLoader 載入配置
config_loader = ConfigLoader()


class SettingChat:
    """Chat 專案配置類（使用統一的 ConfigLoader）"""

    def get_yaml_conf(self):
        """獲取 Chat 專案配置（使用 ConfigLoader）"""
        return config_loader.load_project_config('chat', 'setting_chat.yml')

    def get_account(self, env='', brand='', account_num=''):
        conf = self.get_yaml_conf()
        account_conf = {
            'web_url': conf[env][brand]['web_url'], 
            'app_url': conf[env][brand]['app_url'],
            'wap_url': conf[env][brand]['wap_url'],
            'web2_url': conf[env][brand]['web2_url'],
            'web_account': conf[env][brand]['accounts'][account_num]['web_id'],
            'web2_account': conf[env][brand]['accounts'][account_num]['web2_id'],
            'app_account': conf[env][brand]['accounts'][account_num]['app_id'],
            'wap_account': conf[env][brand]['accounts'][account_num]['wap_id'],
            'mail_account': conf[env][brand]['accounts'][account_num]['mail_id'],
            'password': conf[env][brand]['accounts'][account_num]['password'],
            'web_phone': conf[env][brand]['accounts'][account_num]['web_phone'],
            'web2_phone': conf[env][brand]['accounts'][account_num]['web2_phone'],
            'app_phone': conf[env][brand]['accounts'][account_num]['app_phone'],
            'wap_phone': conf[env][brand]['accounts'][account_num]['wap_phone'],
            'mail_address': conf[env][brand]['accounts'][account_num]['mail_address'],
            'nation': conf[env][brand]['accounts'][account_num]['nation'],
            'operate_account': conf[env][brand]['operate_id'],
            'operate_phone': conf[env][brand]['operate_phone'],
        }
        
        if not env.__contains__('prod'):
            data ={
                'admin_url': conf[env][brand]['admin_url'],
                'admin_id': conf[env][brand]['admin_account'],
                'admin_pwd': conf[env][brand]['admin_password'],
                'admin_otp': conf[env][brand]['admin_otp'],
                'low_rights_admin_id': conf[env][brand]['low_permission_admin_account'],
                'low_rights_admin_pwd': conf[env][brand]['low_permission_admin_password'],

            }

            account_conf.update(data)
        
        return account_conf