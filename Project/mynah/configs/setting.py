from selenium import webdriver
import configparser, os, sys, yaml, platform
import os
import sys
import yaml

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class Setting:
    # conf's path setting
    testconf_path = 'mynah/configs/setting_mynah.yml'

    def get_yaml_conf(self):
        yamlfile = open(os.path.join(root_path, self.testconf_path), encoding='utf-8')
        ymlconf = yaml.safe_load(yamlfile)
        return ymlconf

    def get_test_data(self, env, test_brand, main):
        conf = self.get_yaml_conf()['test_env_conf']
        account_num = main
        if main > 3:
            account_num = 3
        data = {
                'web_url1': conf[env]['guest_web'][main]['URL_Site1'], 
                'web_url2': conf[env]['guest_web'][main]['URL_Site2'],
                'site_name1': conf[env]['guest_web'][main]['site_name1'],
                'site_name2': conf[env]['guest_web'][main]['site_name2'],
                'channel_url': conf[env]['channel_web'][test_brand]['URL_Channel'],
                'web_account': conf[env]['channel_web'][test_brand]['accounts'][account_num]['account'],
                'web_password': conf[env]['channel_web'][test_brand]['accounts'][account_num]['password'],
                'admin_url': conf[env]['admin']['admin_url'], 
                'cs_account1': conf[env]['admin']['cs_account'][main]['account1'],
                'cs_password1': conf[env]['admin']['cs_account'][main]['password1'],
                'cs_account2': conf[env]['admin']['cs_account'][main]['account2'],
                'cs_password2': conf[env]['admin']['cs_account'][main]['password2'],
                'bs_account': conf[env]['admin']['bs_account'][main]['account'],
                'bs_password': conf[env]['admin']['bs_account'][main]['password'],
            }

        return data

if __name__ == '__main__':
    # a = Setting().get_test_data(env='uat',main=2)
    # print(a)
    pass