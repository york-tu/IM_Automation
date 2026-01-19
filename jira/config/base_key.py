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


class BaseKey:
    """JIRA 配置基類（使用統一的 ConfigLoader）"""

    def get_yaml_conf(self):
        """獲取 JIRA 配置（使用 ConfigLoader）"""
        return config_loader.get_jira_config()

    def get_jira_data(self):
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        test_type = gl.get_value('TEST_TYPE')

        cycle_key = self.get_yaml_conf()['jira_conf'][env][brand][test_type]
        gl.set_value('CYCLE_KEY', cycle_key)


