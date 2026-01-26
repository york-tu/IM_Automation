# -*- coding: utf-8 -*-
"""
基礎測試用例類
提供統一的測試用例基礎功能，整合路徑工具和配置載入器
"""
import unittest
import os
import sys
from typing import Dict, Any, Optional
from pathlib import Path

# 添加專案根目錄到 sys.path
from common.utils.path_utils import PathUtils
from common.utils.config_loader import ConfigLoader
import common.utils.globalvar as gl
from jira.module.base_module import UnittestModule


class BaseTestCase(UnittestModule):
    """
    基礎測試用例類
    
    整合了：
    - 路徑處理工具 (PathUtils)
    - 配置載入器 (ConfigLoader)
    - JIRA 整合 (UnittestModule)
    """
    
    # 類別變數（將在 setUpClass 中初始化）
    config_loader: ConfigLoader = None
    path_utils: PathUtils = None
    
    # 測試設置
    env: str = ''
    brand: str = ''
    user: str = ''
    
    @classmethod
    def setUpClass(cls):
        """
        類別級別設置
        初始化工具類和基礎配置
        """
        super().setUpClass()
        
        # 初始化工具類（單例模式，確保全局唯一）
        if cls.path_utils is None:
            cls.path_utils = PathUtils()
        if cls.config_loader is None:
            cls.config_loader = ConfigLoader()
        
        # 確保專案根目錄在 sys.path 中
        project_root = cls.path_utils.get_project_root()
        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))
        
        # 從環境變數或 globalvar 獲取基礎配置
        cls.env = gl.get_value('ENV') or os.getenv('TEST_ENV', 'uat')
        cls.brand = gl.get_value('BRAND') or os.getenv('TEST_BRAND', '')
        cls.user = gl.get_value('USER') or os.getenv('TEST_USER', '')
    
    @classmethod
    def get_project_root(cls) -> Path:
        """
        獲取專案根目錄
        
        Returns:
            Path: 專案根目錄路徑
        """
        return cls.path_utils.get_project_root()
    
    @classmethod
    def get_config_path(cls, *parts: str) -> Path:
        """
        獲取配置檔案路徑
        
        Args:
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Path: 配置檔案完整路徑
        """
        return cls.path_utils.get_config_path(*parts)
    
    @classmethod
    def load_config(cls, *parts: str) -> Dict[str, Any]:
        """
        載入配置檔案
        
        Args:
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Dict[str, Any]: 配置字典
        """
        return cls.config_loader.load_config(*parts)
    
    @classmethod
    def load_project_config(cls, project: str, *parts: str) -> Dict[str, Any]:
        """
        載入專案特定配置檔案
        
        Args:
            project: 專案名稱
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Dict[str, Any]: 配置字典
        """
        return cls.config_loader.load_project_config(project, *parts)
    
    @classmethod
    def get_test_report_path(cls, *parts: str) -> Path:
        """
        獲取測試報告路徑
        
        Args:
            *parts: 報告路徑的相對路徑部分
            
        Returns:
            Path: 報告完整路徑
        """
        return cls.path_utils.get_test_report_path(*parts)

