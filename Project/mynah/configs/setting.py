import os, sys
from common.utils.path_utils import PathUtils
from common.utils.config_loader import ConfigLoader

# 使用 PathUtils 添加專案根目錄到 sys.path
path_utils = PathUtils()
project_root = str(path_utils.get_project_root())
if project_root not in sys.path:
    sys.path.append(project_root)

# 使用 ConfigLoader 載入配置
config_loader = ConfigLoader()


class Setting:
    """Mynah 專案配置類（使用統一的 ConfigLoader）"""

    def get_yaml_conf(self):
        """獲取 Mynah 專案配置（使用 ConfigLoader）"""
        return config_loader.load_project_config('mynah', 'setting_mynah.yml')

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