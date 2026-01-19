import os
import sys
from common.utils.path_utils import PathUtils

# 使用 PathUtils 添加專案根目錄到 sys.path
path_utils = PathUtils()
project_root = str(path_utils.get_project_root())
if project_root not in sys.path:
    sys.path.append(project_root)

# 使用新的統一 PageFactory（向後兼容）
from common.framework.compat_pages import AppPages as BaseAppPages


class AppPages(BaseAppPages):
    """Chat App 頁面工廠（使用新的 PageFactory）"""
    
    def __init__(self, parameter: tuple):
        """初始化 App 頁面工廠"""
        super().__init__(parameter, project='chat')
