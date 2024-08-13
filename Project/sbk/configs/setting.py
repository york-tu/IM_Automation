import yaml
import os, sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
import common.utils.globalvar as gl


class SettingSbk:
    # conf's path setting
    testconf_path = 'sbk/configs/setting_sbk.yml'

    def get_yaml_conf(self):
        path = os.path.join(root_path, self.testconf_path)
        with open(path, 'r', encoding='utf-8') as ymlfile:
            ymlconf = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return ymlconf

    def get_account(self, env='', brand='', account_num=''):
        conf = self.get_yaml_conf()
        account_conf = {
            'web_url': conf[env][brand]['web_url'], 
            'web_account': conf[env][brand]['accounts'][account_num]['web_id'],
            'password': conf[env][brand]['accounts'][account_num]['password'],
        }
        
        if not env.__contains__('prod'):
            data ={
                'admin_url': conf[env][brand]['admin_url'],
                'admin_id': conf[env][brand]['admin_account'],
                'admin_pwd': conf[env][brand]['admin_password'],
                'admin_otp': conf[env][brand]['admin_otp']
            }

            account_conf.update(data)
        
        return account_conf