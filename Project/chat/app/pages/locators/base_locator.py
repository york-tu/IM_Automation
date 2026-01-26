"""
Locator 基類
提供統一的 Locator 初始化邏輯，減少代碼重複
"""
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
from configs.app.setting import Setting
import common.utils.globalvar as gl


class BaseLocator:
    """Locator 基類，提供統一的初始化邏輯"""
    
    # 類屬性初始化（與現有 Locator 類的模式保持一致）
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)
    
    def __init_subclass__(cls, **kwargs):
        """當子類被定義時，確保子類也有這些類屬性"""
        super().__init_subclass__(**kwargs)
        # 確保子類繼承基類的類屬性
        if not hasattr(cls, 'base'):
            cls.base = BaseLocator.base
        if not hasattr(cls, 'env'):
            cls.env = BaseLocator.env
        if not hasattr(cls, 'brand'):
            cls.brand = BaseLocator.brand
        if not hasattr(cls, 'app_package'):
            cls.app_package = BaseLocator.app_package
    
    @staticmethod
    def env(env):
        """獲取環境相關的 Locator（通用方法，與現有 Locator 類的方法名保持一致）"""
        base = Xpath_Base()
        env_locator = base.check_device(
            Android=base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS=base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        return env_locator
    
    @staticmethod
    def get_env_locator(env):
        """獲取環境相關的 Locator（通用方法，別名方法）"""
        return BaseLocator.env(env)

