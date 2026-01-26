# -*- coding: utf-8 -*-
"""
基礎頁面抽象類
定義所有頁面物件的通用接口和基礎功能
"""
from abc import ABC
from typing import Optional, Any


class BasePage(ABC):
    """基礎頁面抽象類"""
    
    def __init__(self, driver: Any, wait_sec: int, base_url: str, skip_test_method: Any = None):
        """
        初始化頁面物件
        
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
    
    def get_driver(self) -> Any:
        """獲取驅動實例"""
        return self.driver
    
    def get_base_url(self) -> str:
        """獲取基礎 URL"""
        return self.base_url
    
    def get_wait_time(self) -> int:
        """獲取等待時間"""
        return self.wait_sec







