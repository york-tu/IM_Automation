import os
import sys
from common.utils.path_utils import PathUtils

# 使用 PathUtils 添加專案根目錄到 sys.path
path_utils = PathUtils()
project_root = str(path_utils.get_project_root())
if project_root not in sys.path:
    sys.path.append(project_root)

# 使用新的統一 PageFactory（向後兼容）
from common.framework.compat_pages import CompatiblePages, AppPages as BaseAppPages


class WebPages(CompatiblePages):
    """Exchange WellPay Web 頁面工廠（使用新的 PageFactory）"""
    
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        """初始化 Web 頁面工廠"""
        super().__init__(driver, wait_sec, base_url, skip_test_method, project='exchange_wellpay', page_type='web')
        
        # 特殊處理：註冊 web_page
        self.register_page_lazy('web_page', 'Project.lottery.web.pages.pages.WebPages')


class AppPages(BaseAppPages):
    """Exchange WellPay App 頁面工廠（使用新的 PageFactory）"""
    
    def __init__(self, parameter: tuple):
        """初始化 App 頁面工廠"""
        super().__init__(parameter, project='exchange_wellpay')


class AdminEPage(CompatiblePages):
    """Exchange WellPay Admin 頁面工廠（使用新的 PageFactory）"""
    
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        """初始化 Admin 頁面工廠"""
        super().__init__(driver, wait_sec, base_url, skip_test_method, project='exchange_wellpay', page_type='admin')


class AdminPage(AdminEPage):
    """Exchange WellPay Admin 頁面工廠（繼承自 AdminEPage）"""
    
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        """初始化 Admin 頁面工廠"""
        super().__init__(driver, wait_sec, base_url, skip_test_method)
        
        # 特殊處理：註冊 admin_page
        self.register_page_lazy('admin_page', 'Project.lottery.web.pages.pages.AdminPage')
