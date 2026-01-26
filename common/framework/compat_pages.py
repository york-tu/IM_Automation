# -*- coding: utf-8 -*-
"""
向後兼容的頁面工廠包裝類
保持與舊版 pages.py 相同的接口，內部使用新的 PageFactory
"""
from typing import Any
from common.framework.page_factory import PageFactory, PageFactoryBuilder
from common.framework.page_registry import register_pages_to_factory


class CompatiblePages(PageFactory):
    """
    向後兼容的頁面工廠類
    
    保持與舊版 WebPages, AdminPages 等相同的接口，
    內部使用新的 PageFactory 實現
    """
    
    def __init__(self, driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None, 
                 project: str = '', page_type: str = ''):
        """
        初始化兼容頁面工廠
        
        Args:
            driver: 驅動實例
            wait_sec: 等待時間
            base_url: 基礎 URL
            skip_test_method: 跳過測試的方法
            project: 專案名稱（如 'chat', 'sbk'）
            page_type: 頁面類型（如 'web', 'admin', 'app', 'wap'）
        """
        super().__init__(driver, wait_sec, base_url, skip_test_method)
        
        # 如果提供了專案和類型，自動註冊頁面
        if project and page_type:
            register_pages_to_factory(self, project, page_type)


# 向後兼容的類別別名
class WebPages(CompatiblePages):
    """Web 頁面工廠（向後兼容）"""
    pass


class AdminPages(CompatiblePages):
    """Admin 頁面工廠（向後兼容）"""
    pass


class WapPages(CompatiblePages):
    """WAP 頁面工廠（向後兼容）"""
    pass


class AppPages:
    """
    App 頁面工廠（向後兼容）
    
    注意：App pages 使用不同的參數格式 (parameter tuple: poco, wda_service, skipTest)
    """
    
    def __init__(self, parameter: tuple, project: str = 'chat'):
        """
        初始化 App 頁面工廠
        
        Args:
            parameter: 參數元組 (poco, wda_service, skipTest)
            project: 專案名稱，預設為 'chat'
        """
        self.parameter = parameter
        self.pages_parameter = parameter
        
        # App pages 使用特殊的參數格式
        # 創建一個自定義的工廠實例，重寫 pages_parameter
        self._factory = PageFactory(None, 0, '', None)
        # 強制設置 pages_parameter 為 App pages 的格式
        self._factory.pages_parameter = parameter
        
        # 註冊頁面
        register_pages_to_factory(self._factory, project, 'app')
    
    def __getattr__(self, name: str):
        """委派給內部工廠，支援動態方法生成"""
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        
        # 先檢查名稱是否在頁面註冊表中（支援 _page 和 _pages 結尾）
        if hasattr(self._factory, '_page_registry') and name in self._factory._page_registry:
            def get_page_method():
                return self._factory.get_page(name)
            return get_page_method
        
        # 如果是頁面方法調用，直接委派給工廠
        if hasattr(self._factory, name):
            attr = getattr(self._factory, name)
            if callable(attr):
                return attr
            return attr
        
        # 嘗試動態方法生成（用於向後兼容，支援 _page 和 _pages 結尾）
        if name.endswith('_page') or name.endswith('_pages'):
            def get_page_method():
                return self._factory.get_page(name)
            return get_page_method
        
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")


def create_web_pages(driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None,
                     project: str = 'chat') -> CompatiblePages:
    """
    創建 Web 頁面工廠（便利函數）
    
    Args:
        driver: 驅動實例
        wait_sec: 等待時間
        base_url: 基礎 URL
        skip_test_method: 跳過測試的方法
        project: 專案名稱
        
    Returns:
        CompatiblePages: Web 頁面工廠實例
    """
    return CompatiblePages(driver, wait_sec, base_url, skip_test_method, project, 'web')


def create_admin_pages(driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None,
                       project: str = 'chat') -> CompatiblePages:
    """
    創建 Admin 頁面工廠（便利函數）
    
    Args:
        driver: 驅動實例
        wait_sec: 等待時間
        base_url: 基礎 URL
        skip_test_method: 跳過測試的方法
        project: 專案名稱
        
    Returns:
        CompatiblePages: Admin 頁面工廠實例
    """
    return CompatiblePages(driver, wait_sec, base_url, skip_test_method, project, 'admin')


def create_wap_pages(driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None,
                     project: str = 'chat') -> CompatiblePages:
    """
    創建 WAP 頁面工廠（便利函數）
    
    Args:
        driver: 驅動實例
        wait_sec: 等待時間
        base_url: 基礎 URL
        skip_test_method: 跳過測試的方法
        project: 專案名稱
        
    Returns:
        CompatiblePages: WAP 頁面工廠實例
    """
    return CompatiblePages(driver, wait_sec, base_url, skip_test_method, project, 'wap')

