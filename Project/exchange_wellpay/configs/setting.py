from selenium import webdriver
import configparser, os, sys, yaml, platform
import os
import sys
import yaml

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class Setting:
    # conf's path setting
    testconf_path = ''

    def get_yaml_conf(self):
        yamlfile = open(os.path.join(root_path, self.testconf_path))
        ymlconf = yaml.safe_load(yamlfile)
        return ymlconf

    def get_test_data(self, env='', brand='', account_num=''):
        self.testconf_path = 'lottery/configs/setting.yml'
        conf = self.get_yaml_conf()['test_env_conf']

        data = {
            'web_url': conf[env][brand]['web_url'], 
            'admin_url': conf[env][brand]['admin_url'], 
            'web_id': conf[env][brand]['accounts'][account_num]['web_id'], 
            'web_pwd': conf[env][brand]['accounts'][account_num]['web_pwd'], 
            'admin_id': conf[env]['common']['accounts']['admin_id'], 
            'admin_pwd': conf[env]['common']['accounts']['admin_pwd'], 
            'admin_otp': conf[env]['common']['accounts']['admin_otp'],
            'web_captcha': conf[env]['common']['accounts']['web_captcha'], 
            'withdraw_pwd': conf[env]['common']['accounts']['withdraw_pwd'],  
        }

        return data

    def get_test_data_exchange(self, env='', brand='', account_num=''):
        self.testconf_path = 'exchange_wellpay/configs/setting.yml'
        conf = self.get_yaml_conf()['test_env_conf']

        data = {
            'admin_url': conf[env][brand]['admin_url'], 
            'paybox_url': conf[env][brand]['paybox_url'], 
            'paybox_id': conf[env][brand]['paybox_id'],
            'paybox_pwd': conf[env][brand]['paybox_pwd'],
            'admin_id': conf[env][brand]['zqb_id'],
            'admin_pwd': conf[env][brand]['zqb_pwd'],
            'app_id': conf[env][brand]['accounts'][account_num]['app_id'], 
            'app_pwd': conf[env][brand]['accounts'][account_num]['app_pwd'], 
            'app_number': conf[env][brand]['accounts'][account_num]['app_number'], 
        }

        return data

if __name__ == '__main__':
    pass