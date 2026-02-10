import os, sys, random
import uuid
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


class Setting:
    def get_yaml_conf(self):
        """獲取 App 通用配置（使用 ConfigLoader）"""
        return config_loader.get_app_config()

    @staticmethod
    def get_slack_webhook_url():
        """獲取 Slack Webhook URL（用於發送測試報告通知）"""
        try:
            conf = config_loader.get_app_config()
            return (conf.get('slack') or {}).get('webhook_url') or ''
        except Exception:
            return ''
    
    def get_device_conf(self):
        """獲取手機配置（使用 ConfigLoader）"""
        return config_loader.get_phone_config()

    def get_phone_connect_link(self, phone_name, ip='', connect_type='local'):
        conf = self.get_device_conf()['Phone_conf']
        phone_platform = gl.get_value('PHONE_PLATFORM')
        
        # 檢查是否有動態設置的 WDA 端口（如果端口被占用時自動切換）
        wda_port = gl.get_value('WDA_PORT')
        
        if connect_type == 'remote':
            if phone_platform == 'Android':
                connection = f'Android://127.0.0.1:5037/{ip}'
            elif phone_platform == 'iOS':
                # 使用動態端口或配置的端口
                port = wda_port if wda_port else conf[phone_name].get('port', 8100)
                connection = f'ios:///http://{ip}:{port}'
        else:
            if phone_platform == 'Android':
                connection = f'Android:///{conf[phone_name]["udid"]}'
            elif phone_platform == 'iOS':
                # 使用 usbmux 連接時，端口信息通過環境變數傳遞
                # 如果設置了動態端口，通過環境變數傳遞給 WDA
                if wda_port:
                    import os
                    os.environ['WDA_PORT'] = str(wda_port)
                
                connection = f'ios:///http+usbmux://{conf[phone_name]["udid"]}'  # 主機端預設位置_iPhone15Pro_ios18
                # connection = f'ios:///http://10.200.8.76:{conf[phone_name]["port"]}'  # 主機端預設位置_ios15

                # connection = f'ios:///http://127.0.0.1:{conf[phone_name]["port"]}' # 主機端預設位置
                # connection = f'ios:///http://10.200.8.30:{conf[phone_name]["port"]}'  # 主機端預設位置_ios16.1.1
        return connection

    def get_package_name(self, brand, env='uat'):
        phone_platform = gl.get_value('PHONE_PLATFORM')
        if phone_platform == 'Android':
            package_type = 'package'
        elif phone_platform == 'iOS':
            package_type = 'bundle_id'
        package_name = self.get_yaml_conf()['channel'][brand][env][package_type]

        return package_name
    
    def get_poco_name(self):
        poco_name = self.get_yaml_conf()['channel']['common']['poco']['package']

        return poco_name

    def correct_phone_name(self, phone_name_fuzzy):
        conf = self.get_device_conf()['Phone_conf']
        phone_name_list = conf.keys()
        phone_name_fuzzy = phone_name_fuzzy.split('_')[-1]
        for name in phone_name_list:
            if phone_name_fuzzy == name.split('_')[-1]:
                correct_phone_name = name

        return correct_phone_name
    
    def get_phone_device_id(self, phone_name='', multiple=False):
        if multiple == True:
            conf = self.get_device_conf()['Phone_conf']
            device_id = conf[phone_name]['udid']
        else:
            device_id = uuid.uuid4()

        return str(device_id)
  