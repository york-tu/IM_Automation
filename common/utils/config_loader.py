# -*- coding: utf-8 -*-
"""
配置載入器
統一管理專案中的所有配置檔案載入，支援快取機制
"""
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from common.utils.path_utils import PathUtils


class ConfigLoader:
    """配置載入器（單例模式）"""
    
    _instance: Optional['ConfigLoader'] = None
    _config_cache: Dict[str, Any] = {}
    
    def __new__(cls):
        """單例模式實現"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def load_yaml(self, config_path: Path) -> Dict[str, Any]:
        """
        載入 YAML 配置檔案
        
        Args:
            config_path: 配置檔案路徑
            
        Returns:
            Dict[str, Any]: 配置字典
            
        Raises:
            FileNotFoundError: 如果配置檔案不存在
            yaml.YAMLError: 如果 YAML 解析失敗
        """
        config_key = str(config_path)
        
        # 檢查快取
        if config_key not in self._config_cache:
            if not config_path.exists():
                raise FileNotFoundError(f"Config file not found: {config_path}")
            
            with open(config_path, 'r', encoding='utf-8') as f:
                try:
                    self._config_cache[config_key] = yaml.safe_load(f)
                except yaml.YAMLError as e:
                    raise yaml.YAMLError(f"Failed to parse YAML file {config_path}: {e}")
        
        return self._config_cache[config_key]
    
    def load_config(self, *parts: str) -> Dict[str, Any]:
        """
        載入配置檔案（相對於 configs 目錄）
        
        Args:
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Dict[str, Any]: 配置字典
            
        Example:
            >>> loader = ConfigLoader()
            >>> config = loader.load_config("app", "config.yml")
        """
        config_path = PathUtils.get_config_path(*parts)
        return self.load_yaml(config_path)
    
    def load_project_config(self, project: str, *parts: str) -> Dict[str, Any]:
        """
        載入專案特定配置檔案
        
        Args:
            project: 專案名稱（如 'chat', 'sbk'）
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Dict[str, Any]: 配置字典
            
        Example:
            >>> loader = ConfigLoader()
            >>> config = loader.load_project_config("chat", "setting_chat.yml")
        """
        config_path = PathUtils.get_project_path(project, "configs", *parts)
        return self.load_yaml(config_path)
    
    def get_app_config(self) -> Dict[str, Any]:
        """
        獲取 App 通用配置（configs/app/config.yml）
        
        Returns:
            Dict[str, Any]: App 配置字典
        """
        return self.load_config("app", "config.yml")
    
    def get_phone_config(self) -> Dict[str, Any]:
        """
        獲取手機配置（configs/app/phone_config.yml）
        
        Returns:
            Dict[str, Any]: 手機配置字典
        """
        return self.load_config("app", "phone_config.yml")
    
    def get_chrome_config(self) -> Dict[str, Any]:
        """
        獲取 Chrome 配置（configs/web/setting_chrome.yml）
        
        Returns:
            Dict[str, Any]: Chrome 配置字典
        """
        return self.load_config("web", "setting_chrome.yml")
    
    def get_jira_config(self) -> Dict[str, Any]:
        """
        獲取 JIRA 配置（jira/config/jira_key.yml）
        
        Returns:
            Dict[str, Any]: JIRA 配置字典
        """
        config_path = PathUtils.get_relative_path("jira", "config", "jira_key.yml")
        return self.load_yaml(config_path)
    
    def clear_cache(self):
        """清空配置快取"""
        self._config_cache.clear()
    
    def reload_config(self, *parts: str) -> Dict[str, Any]:
        """
        重新載入配置檔案（清除快取後重新載入）
        
        Args:
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Dict[str, Any]: 配置字典
        """
        config_path = PathUtils.get_config_path(*parts)
        config_key = str(config_path)
        
        # 清除該配置的快取
        if config_key in self._config_cache:
            del self._config_cache[config_key]
        
        # 重新載入
        return self.load_config(*parts)


# 向後兼容的函數接口
def load_config(*parts: str) -> Dict[str, Any]:
    """載入配置檔案（函數接口）"""
    return ConfigLoader().load_config(*parts)


def load_project_config(project: str, *parts: str) -> Dict[str, Any]:
    """載入專案配置檔案（函數接口）"""
    return ConfigLoader().load_project_config(project, *parts)







