import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class PtElectronicPageLocator:
    base = Xpath_Base()
    start_game = 'image/app/electronic/pt_start.png'
    go_home = 'image/app/electronic/go_home.png'
    pt_screen_icon = 'image/app/electronic/pt_screen_icon.png'

    ok = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确定'),
        iOS = base.data_collation(type_kind='name', type_name='确定')
    )

class PtElectronicPage(Base):
    def pt_electronic(self):
        self.enter_game('丛林巨人')

        # 只要有轉錢到PT錢包, 進入遊戲時就會跳訊息，按到完為止
        if self.common.poco_wait_exists(PtElectronicPageLocator.ok, timeout=30):
            while self.common.poco_exists(PtElectronicPageLocator.ok):
                self.common.poco_click(PtElectronicPageLocator.ok)

        if self.common.wait_image(PtElectronicPageLocator.start_game) is True:
            self.common.wait_touch(PtElectronicPageLocator.start_game)
        elif self.common.wait_image(PtElectronicPageLocator.pt_screen_icon) is True:
            pass
        else:
            raise EOFError('找不到指定圖片,讀取超時')