from selenium import webdriver
import configparser, os, sys, yaml, platform
import os
import sys
import yaml

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class Setting:
    # conf's path setting
    testconf_path = 'lottery/configs/setting.yml'

    def get_yaml_conf(self):
        yamlfile = open(os.path.join(root_path, self.testconf_path))
        ymlconf = yaml.safe_load(yamlfile)
        return ymlconf

    def get_test_data(self, env='', brand='', account_num=''):
        conf = self.get_yaml_conf()['test_env_conf']
        
        if 'new' in brand:
            brand = brand.replace('_new','')

        data = {
            'web_url': conf[env][brand]['web_url'], 
            'mobile_url': conf[env][brand]['mobile_url'], 
            'web_id': conf[env][brand]['accounts'][account_num]['web_id'], 
            'web_pwd': conf[env][brand]['accounts'][account_num]['web_pwd'], 
            'mobile_ui_mode': conf[env][brand]['accounts'][account_num]['mobile_ui_mode'], 
            'bank_card': conf[env][brand]['accounts'][account_num]['bank_card'],
            'web_captcha': conf[env]['common']['accounts']['web_captcha'], 
            'withdraw_pwd': conf[env]['common']['accounts']['withdraw_pwd'],  
        }

        if not env.__contains__('prod'):
            data2 = {
                'reseller_url': conf[env][brand]['reseller_url'], 
                'admin_url': conf[env][brand]['admin_url'], 
                'reseller_id': conf[env][brand]['structure'][1]['agent'], 
                'shareholder': conf[env][brand]['structure'][1]['shareholder'], 
                'generalagent': conf[env][brand]['structure'][1]['generalagent'], 
                'commision_program': conf[env][brand]['structure'][1]['commision_program'], 
                'reseller_pwd': conf[env]['common']['accounts']['reseller_pwd'], 
                'reseller_otp': conf[env]['common']['accounts']['reseller_otp'], 
                'admin_otp': conf[env]['common']['accounts']['admin_otp'],
                'admin_id': conf[env]['common']['accounts']['admin_id'], 
                'admin_pwd': conf[env]['common']['accounts']['admin_pwd'], 
                'cmweb_url': conf[env]['common']['cmweb_url'], 
                'cmweb_id' : conf[env]['common']['accounts']['cmweb_id'], 
                'cmweb_pwd' : conf[env]['common']['accounts']['cmweb_pwd'], 
                'dwhweb_url': conf[env]['common']['dwhweb_url'], 
                'dwhweb_id' : conf[env]['common']['accounts']['dwhweb_id'], 
                'dwhweb_pwd' : conf[env]['common']['accounts']['dwhweb_pwd'], 
                'fileserver_url': conf[env]['common']['fileserver_url'],
                'port' : conf[env]['common']['port'], 
                'host_ip' : conf[env][brand]['host_ip'], 
                'mynah_admin_url': conf[env]['common']['mynah_admin_url'],
                'mynah_web_url': conf[env]['common']['mynah_web_url'],
                'mynah_id': conf[env]['common']['accounts']['mynah_id'], 
                'mynah_pwd': conf[env]['common']['accounts']['mynah_pwd'], 
                'zqb_merchant_id': conf[env][brand]['zqb_merchant_id'],
                'zqb_private_sign': conf[env][brand]['zqb_private_sign'],
                'zqb_deposit_callback': conf[env][brand]['zqb_deposit_callback'],
            }

            data.update(data2)

        # 不跑 dev regression
        # if os.path.basename(sys.argv[0] != 'prod_regression.py'):
        #     data3 = {
        #         'admin_url': conf[env][brand]['admin_url'], 
        #         'reseller_url': conf[env][brand]['reseller_url'], 
        #         'admin_id': conf[env]['common']['accounts']['admin_id'], 
        #         'admin_pwd': conf[env]['common']['accounts']['admin_pwd'], 
        #         'cmweb_url': conf[env]['common']['reseller_url'], 
        #         'cmweb_id' : conf[env]['common']['accounts']['cmweb_id'], 
        #         'cmweb_pwd' : conf[env]['common']['accounts']['cmweb_pwd'], 
        #     }

        #     data.update(data3)

        return data

if __name__ == '__main__':
    pass