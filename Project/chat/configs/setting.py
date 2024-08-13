import yaml
import os, sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
import common.utils.globalvar as gl


class SettingChat:
    # conf's path setting
    testconf_path = 'chat/configs/setting_chat.yml'

    def get_yaml_conf(self):
        path = os.path.join(root_path, self.testconf_path)
        with open(path, 'r', encoding='utf-8') as ymlfile:
            ymlconf = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return ymlconf

    def get_account(self, env='', brand='', account_num=''):
        conf = self.get_yaml_conf()
        account_conf = {
            'web_url': conf[env][brand]['web_url'], 
            'app_url': conf[env][brand]['app_url'],
            'web_account': conf[env][brand]['accounts'][account_num]['web_id'],
            'app_account': conf[env][brand]['accounts'][account_num]['app_id'],
            'password': conf[env][brand]['accounts'][account_num]['password'],
            'web_phone': conf[env][brand]['accounts'][account_num]['web_phone'],
            'app_phone': conf[env][brand]['accounts'][account_num]['app_phone'],
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