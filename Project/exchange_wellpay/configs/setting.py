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
    """Exchange WellPay 專案配置類（使用統一的 ConfigLoader）"""

    def get_yaml_conf_exchange(self):
        """獲取 Exchange WellPay 專案配置（使用 ConfigLoader）"""
        return config_loader.load_project_config('exchange_wellpay', 'setting.yml')
    
    def get_yaml_conf(self, project: str = 'exchange_wellpay'):
        """
        獲取專案配置（使用 ConfigLoader）
        
        Args:
            project: 專案名稱，預設為 'exchange_wellpay'
                    也可以為 'lottery'（用於 get_test_data）
        """
        if project == 'lottery':
            # Lottery 專案的配置（如果存在）
            return config_loader.load_project_config('lottery', 'setting.yml')
        else:
            return self.get_yaml_conf_exchange()

    def get_test_data(self, env='', brand='', account_num=''):
        """獲取 Lottery 專案測試資料（向後兼容）"""
        conf = self.get_yaml_conf('lottery')['test_env_conf']

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
        """獲取 Exchange WellPay 專案測試資料"""
        conf = self.get_yaml_conf_exchange()['test_env_conf']

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