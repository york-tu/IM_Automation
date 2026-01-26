# -*- coding: utf-8 -*-
"""
統一的頁面工廠類
支援動態註冊和獲取頁面物件，提供快取機制和向後兼容性
"""
from typing import Dict, Type, Any, Optional, Callable, Tuple
from common.framework.base_page import BasePage


class PageFactory:
    """
    統一的頁面工廠類
    
    支援：
    - 動態註冊頁面類別
    - 頁面物件快取
    - 向後兼容的方法調用（如 `base_page()`）
    - 不同專案和類型的頁面管理
    """
    
    def __init__(self, driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None):
        """
        初始化頁面工廠
        
        Args:
            driver: WebDriver 或 AppDriver 實例
            wait_sec: 等待時間（秒）
            base_url: 基礎 URL
            skip_test_method: 跳過測試的方法（可選）
        """
        self.driver = driver
        self.wait_sec = wait_sec
        self.base_url = base_url
        self.skip_test_method = skip_test_method
        self.pages_parameter = (driver, wait_sec, base_url, skip_test_method)
        
        # 頁面類別註冊表：{page_name: (page_class, import_path)}
        self._page_registry: Dict[str, Tuple[Type[BasePage], str]] = {}
        
        # 頁面物件快取：{page_name: page_instance}
        self._page_cache: Dict[str, BasePage] = {}
        
        # 動態方法快取：用於向後兼容
        self._dynamic_methods: Dict[str, Callable] = {}
    
    def register_page(self, name: str, page_class: Type[BasePage], import_path: Optional[str] = None):
        """
        註冊頁面類別
        
        Args:
            name: 頁面名稱（如 'base_page', 'main_page'）
            page_class: 頁面類別
            import_path: 可選的導入路徑（用於延遲導入）
        """
        self._page_registry[name] = (page_class, import_path or '')
    
    def register_page_lazy(self, name: str, import_path: str):
        """
        註冊頁面類別（延遲導入）
        
        Args:
            name: 頁面名稱
            import_path: 導入路徑（如 'Project.chat.web.pages.webs.web_basepage'）
        """
        self._page_registry[name] = (None, import_path)
    
    def get_page(self, name: str) -> BasePage:
        """
        獲取頁面物件（支援快取）
        
        Args:
            name: 頁面名稱
            
        Returns:
            BasePage: 頁面物件實例
            
        Raises:
            ValueError: 如果頁面未註冊
        """
        # 檢查快取
        if name in self._page_cache:
            return self._page_cache[name]
        
        # 檢查是否已註冊
        if name not in self._page_registry:
            raise ValueError(
                f"Page '{name}' is not registered. "
                f"Available pages: {list(self._page_registry.keys())}"
            )
        
        page_class, import_path = self._page_registry[name]
        
        # 如果是延遲導入，先導入類別
        if page_class is None:
            if not import_path:
                raise ValueError(f"Page '{name}' is registered but no import path or class provided")
            
            # 動態導入（支援完整路徑如 'module.path.ClassName'）
            if '.' in import_path:
                parts = import_path.split('.')
                class_name = parts[-1]
                module_path = '.'.join(parts[:-1])
            else:
                raise ValueError(f"Invalid import path format: {import_path}. Expected 'module.path.ClassName'")
            
            module = __import__(module_path, fromlist=[class_name])
            page_class = getattr(module, class_name)
        
        # 創建頁面實例
        # 判斷參數格式：App pages 使用 tuple 參數，Web pages 使用展開的參數
        try:
            # 檢查是否是 App pages 的參數格式 (poco, wda_service, skipTest)
            # App pages 的 Base.__init__ 需要三個獨立參數，不是 tuple
            if isinstance(self.pages_parameter, tuple) and len(self.pages_parameter) == 3:
                # App pages 格式：解包 tuple 為三個獨立參數
                poco, wda_service, skip_test_method = self.pages_parameter
                page_instance = page_class(poco, wda_service, skip_test_method)
            elif isinstance(self.pages_parameter, tuple) and len(self.pages_parameter) == 4:
                # Web pages 格式：解包 tuple 為四個獨立參數
                page_instance = page_class(*self.pages_parameter)
            else:
                # 其他格式，嘗試展開
                page_instance = page_class(*self.pages_parameter)
        except (TypeError, AttributeError) as e:
            # 如果展開失敗，嘗試直接傳遞（用於特殊情況）
            if isinstance(self.pages_parameter, tuple) and len(self.pages_parameter) == 1:
                # 單元素 tuple，可能是特殊格式
                page_instance = page_class(self.pages_parameter[0])
            else:
                raise TypeError(
                    f"Failed to instantiate {page_class.__name__} with parameters: {self.pages_parameter}. "
                    f"Error: {e}"
                )
        
        # 存入快取
        self._page_cache[name] = page_instance
        
        return page_instance
    
    def clear_cache(self):
        """清空頁面物件快取"""
        self._page_cache.clear()
    
    def clear_cache_for_page(self, name: str):
        """清空特定頁面的快取"""
        if name in self._page_cache:
            del self._page_cache[name]
    
    def __getattr__(self, name: str) -> Callable:
        """
        動態方法生成（向後兼容）
        
        允許像 `pages.base_page()` 或 `pages.webBasePage()` 這樣調用，
        自動轉換為 `pages.get_page('base_page')` 或 `pages.get_page('webBasePage')`
        
        Args:
            name: 方法名稱（可以以 '_page' 或 '_pages' 結尾，或是 camelCase 格式）
            
        Returns:
            Callable: 返回頁面物件的方法
        """
        # 先檢查是否在註冊的頁面中（優先處理，支援所有已註冊的頁面名稱）
        if name in self._page_registry:
            if name not in self._dynamic_methods:
                # 創建動態方法
                page_name = name
                def get_page_method():
                    return self.get_page(page_name)
                self._dynamic_methods[name] = get_page_method
            
            return self._dynamic_methods[name]
        
        # 檢查是否是頁面方法（以 _page 或 _pages 結尾或 camelCase 格式）
        is_snake_case = name.endswith('_page') or name.endswith('_pages')
        is_camel_case = (name and name[0].islower() and any(c.isupper() for c in name))
        
        if is_snake_case or is_camel_case:
            # 如果符合命名規則但未註冊，拋出錯誤
            raise AttributeError(
                f"'{self.__class__.__name__}' has no attribute '{name}'. "
                f"Available pages: {list(self._page_registry.keys())}"
            )
        
        # 如果不是頁面方法，拋出 AttributeError
        raise AttributeError(
            f"'{self.__class__.__name__}' has no attribute '{name}'. "
            f"Available pages: {list(self._page_registry.keys())}"
        )
    
    def register_from_dict(self, page_dict: Dict[str, str]):
        """
        從字典批量註冊頁面（延遲導入）
        
        Args:
            page_dict: 頁面名稱到導入路徑的映射
            
        Example:
            factory.register_from_dict({
                'base_page': 'Project.chat.web.pages.webs.web_basepage.BasePage',
                'main_page': 'Project.chat.web.pages.webs.web_mainpage.MainPage'
            })
        """
        for name, import_path in page_dict.items():
            self.register_page_lazy(name, import_path)
    
    def list_registered_pages(self) -> list:
        """列出所有已註冊的頁面名稱"""
        return list(self._page_registry.keys())
    
    def is_registered(self, name: str) -> bool:
        """檢查頁面是否已註冊"""
        return name in self._page_registry


class PageFactoryBuilder:
    """
    頁面工廠建構器
    提供便利的方法來建立和配置 PageFactory
    """
    
    @staticmethod
    def create(
        driver: Any,
        wait_sec: int,
        base_url: str,
        skip_test_method: Any = None,
        page_config: Optional[Dict[str, str]] = None
    ) -> PageFactory:
        """
        創建並配置 PageFactory
        
        Args:
            driver: 驅動實例
            wait_sec: 等待時間
            base_url: 基礎 URL
            skip_test_method: 跳過測試的方法
            page_config: 可選的頁面配置字典
            
        Returns:
            PageFactory: 配置好的頁面工廠實例
        """
        factory = PageFactory(driver, wait_sec, base_url, skip_test_method)
        
        if page_config:
            factory.register_from_dict(page_config)
        
        return factory

