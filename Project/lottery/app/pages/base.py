from airtest.core.api import *
from common.app.common import Common
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class BaseLocator:
    base = Xpath_Base()

    member = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='tabBarItem_member'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_member')
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

    home = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='首页'),
        iOS = base.data_collation(type_kind='name', type_name='首页')
    )

    loading = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='处理中...'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*处理中.*')
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
        self.wait_loading_finish()
        self.common.keyevent('BACK')
        self.wait_loading_finish()
        self.common.keyevent('BACK')

    def enter_game(self, game):
        self.wait_loading_finish()
        self.common.poco_wait_exists(BaseLocator.search)
        self.common.poco_send_text(BaseLocator.search, game)
        self.wait_loading_finish()

        if self.common.poco_wait_exists(BaseLocator.game_icon(game), timeout=15):
            self.common.poco_click(BaseLocator.game_icon(game))
        else:
            raise EOFError(f'找不到指定遊戲,遊戲名稱:{game}')
        
        self.click_enter()

        if self.common.poco_wait_exists(BaseLocator.return_home, timeout=5):
            raise EOFError(f'此遊戲暫時性維護中,遊戲名稱:{game}')
    
    def click_enter(self):
        for _ in range(0, 5):
            self.wait_loading_finish()
            try:
                self.common.poco_click(BaseLocator.enter_game)
                break
            except:
                pass

    def wait_loading_finish(self):
        self.common.sleep(2)
        while self.common.poco_exists(BaseLocator.loading):
            self.common.sleep(2)
    