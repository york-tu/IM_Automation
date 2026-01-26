# -*- coding: utf-8 -*-
"""
路徑處理工具類
統一管理專案中的所有路徑計算，避免重複的 os.path.dirname() 鏈式調用
"""
import os
from pathlib import Path
from typing import Optional


class PathUtils:
    """路徑處理工具類（單例模式）"""
    
    _project_root: Optional[Path] = None
    _instance: Optional['PathUtils'] = None
    
    def __new__(cls):
        """單例模式實現"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_project_root(cls) -> Path:
        """
        獲取專案根目錄
        
        專案根目錄的標記檔案：requirements.txt 或 Pipfile
        
        Returns:
            Path: 專案根目錄路徑
            
        Raises:
            RuntimeError: 如果找不到專案根目錄
        """
        if cls._project_root is None:
            # 從當前檔案向上查找，直到找到根目錄標記
            current = Path(__file__).resolve()
            
            # 最多向上查找 10 層，避免無限循環
            max_levels = 10
            level = 0
            
            while current != current.parent and level < max_levels:
                # 檢查是否有標記檔案
                if (current / "requirements.txt").exists() or \
                   (current / "Pipfile").exists() or \
                   (current / "Pipfile.lock").exists():
                    cls._project_root = current
                    break
                current = current.parent
                level += 1
            else:
                # 如果找不到，使用當前檔案的向上 4 層作為後備方案
                current_file = Path(__file__).resolve()
                cls._project_root = current_file.parent.parent.parent.parent
                # 仍然記錄警告
                import warnings
                warnings.warn(
                    f"Cannot find project root with marker files, "
                    f"using fallback: {cls._project_root}",
                    RuntimeWarning
                )
        
        return cls._project_root
    
    @classmethod
    def get_relative_path(cls, *parts: str) -> Path:
        """
        獲取相對於專案根目錄的路徑
        
        Args:
            *parts: 路徑部分
            
        Returns:
            Path: 完整路徑
            
        Example:
            >>> PathUtils.get_relative_path("configs", "app", "config.yml")
            Path("/project/root/configs/app/config.yml")
        """
        return cls.get_project_root() / Path(*parts)
    
    @classmethod
    def get_config_path(cls, *parts: str) -> Path:
        """
        獲取配置檔案路徑
        
        Args:
            *parts: 配置檔案的相對路徑部分
            
        Returns:
            Path: 配置檔案完整路徑
            
        Example:
            >>> PathUtils.get_config_path("app", "config.yml")
            Path("/project/root/configs/app/config.yml")
        """
        return cls.get_relative_path("configs", *parts)
    
    @classmethod
    def get_test_report_path(cls, *parts: str) -> Path:
        """
        獲取測試報告路徑
        
        Args:
            *parts: 報告路徑的相對路徑部分
            
        Returns:
            Path: 報告完整路徑
            
        Example:
            >>> PathUtils.get_test_report_path("web", "uat", "gu")
            Path("/project/root/common/Test-Reports/web/uat/gu")
        """
        return cls.get_relative_path("common", "Test-Reports", *parts)
    
    @classmethod
    def get_driver_path(cls, *parts: str) -> Path:
        """
        獲取驅動程式路徑
        
        Args:
            *parts: 驅動程式路徑的相對路徑部分
            
        Returns:
            Path: 驅動程式完整路徑
        """
        return cls.get_relative_path("driver", "driver", *parts)
    
    @classmethod
    def get_image_path(cls, *parts: str) -> Path:
        """
        獲取圖片資源路徑
        
        Args:
            *parts: 圖片路徑的相對路徑部分
            
        Returns:
            Path: 圖片完整路徑
        """
        return cls.get_relative_path("image", *parts)
    
    @classmethod
    def get_project_path(cls, *parts: str) -> Path:
        """
        獲取專案測試路徑
        
        Args:
            *parts: 專案路徑的相對路徑部分
            
        Returns:
            Path: 專案完整路徑
            
        Example:
            >>> PathUtils.get_project_path("chat", "pages")
            Path("/project/root/Project/chat/pages")
        """
        return cls.get_relative_path("Project", *parts)
    
    @classmethod
    def ensure_dir(cls, path: Path) -> Path:
        """
        確保目錄存在，如果不存在則創建
        
        Args:
            path: 目錄路徑
            
        Returns:
            Path: 目錄路徑
        """
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    @classmethod
    def get_download_path(cls, brand: str) -> Path:
        """
        獲取下載目錄路徑（根據作業系統）
        
        Args:
            brand: 品牌名稱
            
        Returns:
            Path: 下載目錄路徑
        """
        import platform
        
        system = platform.system()
        
        if system == 'Windows':
            user = os.environ.get('HOMEPATH', os.environ.get('USERPROFILE', ''))
            if user.startswith('\\'):
                # 如果 HOMEPATH 是相對路徑，需要加上 C:
                download_path = Path(f"C:{user}") / "Downloads" / brand
            else:
                download_path = Path(user) / "Downloads" / brand
        else:
            # Linux 或 macOS
            user = os.environ.get('HOME', os.path.expanduser('~'))
            download_path = Path(user) / "Downloads" / brand
        
        return download_path
    
    @classmethod
    def calculate_levels_up(cls, from_file: str, target_file: str = "requirements.txt") -> int:
        """
        計算從當前檔案到專案根目錄需要向上多少層
        
        Args:
            from_file: 起始檔案路徑（通常使用 __file__）
            target_file: 目標標記檔案名稱
            
        Returns:
            int: 需要向上的層數
        """
        current = Path(from_file).resolve().parent
        level = 0
        max_levels = 10
        
        while current != current.parent and level < max_levels:
            if (current / target_file).exists():
                return level
            current = current.parent
            level += 1
        
        return -1  # 未找到


# 向後兼容的函數接口
def get_project_root() -> Path:
    """獲取專案根目錄（函數接口）"""
    return PathUtils.get_project_root()


def get_relative_path(*parts: str) -> Path:
    """獲取相對於專案根目錄的路徑（函數接口）"""
    return PathUtils.get_relative_path(*parts)


def get_config_path(*parts: str) -> Path:
    """獲取配置檔案路徑（函數接口）"""
    return PathUtils.get_config_path(*parts)


def get_test_report_path(*parts: str) -> Path:
    """獲取測試報告路徑（函數接口）"""
    return PathUtils.get_test_report_path(*parts)







