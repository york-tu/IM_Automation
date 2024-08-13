from airtest.core.api import *
from common.app.common import Common
from configs.app.setting import Setting
from Project.chat.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl
class BaseLocator:
    base = Xpath_Base()
    env = gl.get_value('ENV')
    brand = gl.get_value('BRAND')
    app_package = Setting().get_package_name(brand, env)

    member = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='tabBarItem_member'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_member')
    )

    go_back = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android.widget.ImageView', action='parent().parent()'),
        iOS = base.data_collation(type_kind='name', type_name='首页')
    )

    cancel = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='取消'),
        iOS = base.data_collation(type_kind='name', type_name='取消')
    )

    return_home = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='返回首頁'),
        iOS = base.data_collation(type_kind='name', type_name='返回首頁')
    )

    enter_game = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='进入游戏'),
        iOS = base.data_collation(type_kind='name', type_name='进入游戏')
    )

    search = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='搜寻...'),
        iOS = base.data_collation(type_kind='name', type_name='搜寻...')
    )

    login_rush = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='登录状态已过期, 请重新登录'),
        iOS = base.data_collation(type_kind='name', type_name='搜寻...')
    )

    login_rush_ok = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS = base.data_collation(type_kind='name', type_name='搜寻...')
    )

    home = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='首页'),
        iOS = base.data_collation(type_kind='name', type_name='首页')
    )

    loading = base.check_device(
        Android = base.data_collation(type_kind='name', type_name= str(app_package) + ':id/lottie_view'),
        iOS = base.data_collation(type_kind='name', type_name='.*处理中.*')
    )

    @staticmethod
    def game_icon(game_name):
        game_icon = BaseLocator.base.check_device(
            Android = BaseLocator.base.data_collation(type_kind='text', type_name=game_name, num=1),
            iOS = BaseLocator.base.data_collation(type_kind='name', type_name=game_name, num=1)
        )
        return game_icon


class Base(object):
    def __init__(self, poco='', wda_service='', skip_test_method=''):
        self.poco = poco
        self.wda = wda_service
        self.common = Common(self.poco, self.wda, skip_test_method)

    def go_home(self):
        self.common.poco_click(BaseLocator.member)
        self.common.poco_click(BaseLocator.home)
    
    def go_back(self):
        self.common.keyevent("BACK")

    def skip_login_rush(self):
        self.common.sleep(2)
        
        if self.common.poco_exists(BaseLocator.login_rush):
            self.common.poco_click(BaseLocator.login_rush_ok)
        
        self.common.sleep(0.5)

    def wait_loading_finish(self):  
        for loop in range(0, 3):
            if self.common.poco_exists(BaseLocator.loading):
                try:
                    self.common.poco_wait_disappearance(BaseLocator.loading)
                    return
                except:
                     if loop == 3:
                        raise Exception("讀取時間過長,請確認讀取屏蔽視窗")

            self.common.sleep(0.5)
            if BaseLocator.env == 'prod':
                self.common.sleep(1)