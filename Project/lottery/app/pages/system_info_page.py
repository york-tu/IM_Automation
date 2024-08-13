from time import sleep
from common.app.common import Common
from Project.lottery.app.pages.base import Base
import re
import common.utils.globalvar as gl
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class SystemInfoPageLocator:
    base = Xpath_Base()
    
    @staticmethod
    def version(num):
        if num == 1:
            action = 'parent().child()[3]'
        elif num == 2:
            action = 'parent().child()[4]'
        version = SystemInfoPageLocator.base.check_device(
            Android = SystemInfoPageLocator.base.data_collation(type_kind='textMatches', type_name='一般信息.*', action=action),
            iOS = SystemInfoPageLocator.base.data_collation(type_kind='nameMatches', type_name='一般信息.*', num=-1, action=action)
        )

        return version

    version_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*version_tv'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*version_tv')
    )

    location = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='地区设置信息.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='地区设置信息.*')
    )

    @staticmethod
    def env(env):
        env = SystemInfoPageLocator.base.check_device(
            Android = SystemInfoPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS = SystemInfoPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        
        return env
    
class SystemInfoPage(Base):
    def change_env(self, env):
        for loop in range(0, 3):
            if self.common.poco_exists(SystemInfoPageLocator.location):
                self.common.poco_click(SystemInfoPageLocator.location, times=8)

                if self.common.poco_exists(SystemInfoPageLocator.env(env)):
                    self.common.poco_click(SystemInfoPageLocator.env(env))
                    break
            
            else:
                self.common.go_down()
        
    def version(self, correct_version=''):
        for loop in range(0, 3):
            if self.common.poco_exists(SystemInfoPageLocator.version(1)):
                info = self.common.poco_get_text(SystemInfoPageLocator.version(1)).split('\n')
                app_version = info[0].replace(' ','').split(':')[1]
                # os_version = info[1].replace(' ','').split(':')[1]
                
                if app_version == '':
                    info = self.common.poco_get_text(SystemInfoPageLocator.version(2)).split('\n')
                    app_version = info[0].replace(' ','').split(':')[1]

                if correct_version != app_version:
                    message = f'版本錯誤, 目前版本: {app_version} 正確版本: {correct_version}'
                    gl.set_value('VERSION_MESSAGE', message)
                    raise EOFError(message)
                else:
                    break
            else:
                self.common.go_down()

            if loop == 2:
                message = '找不到版本號碼'
                raise EOFError(message)
    
    def version_napp(self, correct_version=''):
        for loop in range(0, 3):
            if self.common.poco_exists(SystemInfoPageLocator.version_napp):
                app_version = self.common.poco_get_text(SystemInfoPageLocator.version_napp)

                if correct_version != app_version:
                    message = f'版本錯誤, 目前版本: {app_version} 正確版本: {correct_version}'
                    gl.set_value('VERSION_MESSAGE', message)
                    raise EOFError(message)
                else:
                    break

            if loop == 2:
                message = '找不到版本號碼'
                raise EOFError(message)
