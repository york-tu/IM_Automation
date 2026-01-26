# -*- coding: utf-8 -*-
"""
基礎驅動抽象類
定義所有驅動類的通用接口和基礎功能
"""
from abc import ABC, abstractmethod
from typing import Optional, Any


class BaseDriver(ABC):
    """基礎驅動抽象類"""
    
    def __init__(self):
        """初始化驅動"""
        self.driver: Optional[Any] = None
    
    @abstractmethod
    def initialize(self, **kwargs) -> Any:
        """
        初始化驅動
        
        Args:
            **kwargs: 驅動初始化參數
            
        Returns:
            驅動實例
        """
        pass
    
    @abstractmethod
    def cleanup(self):
        """清理資源"""
        pass
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.cleanup()







