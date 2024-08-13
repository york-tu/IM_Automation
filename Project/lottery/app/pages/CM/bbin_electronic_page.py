import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class BbinElectronicPageLocator:
    base = Xpath_Base()
    cancel =  'image/app/electronic/bbin_cancel.png'
    enter = 'image/app/electronic/bbin_enter.png'
    start_game = 'image/app/electronic/bbin_start.png'
    go_home = 'image/app/go_home.png'

    cancel = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='fullclose_div'),
        iOS = base.data_collation(type_kind='name', type_name='fullclose_div')
    )

class BbinElectronicPage(Base):
    def bbin_electronic(self):
        self.enter_game('Staronic')

        # 大手機上會有上滑提示, 但小手機上沒有, 不知道為什麼, 而且有可能會重複跳出
        while self.common.poco_wait_exists(BbinElectronicPageLocator.cancel, timeout=10):
            self.common.poco_click(BbinElectronicPageLocator.cancel)

        # 此款遊戲有時會需要點擊兩次才能進入
        for i in range(3):
            self.common.wait_touch(BbinElectronicPageLocator.enter)
            if self.common.wait_image(BbinElectronicPageLocator.start_game) is True:
                break
            if i == 2:
                raise EOFError('找不到指定圖片,讀取超時')

        self.common.wait_touch(BbinElectronicPageLocator.start_game)
        self.common.sleep(3)
