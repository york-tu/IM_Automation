import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class DtElectronicPageLocator:
    skip = 'image/app/electronic/dt_skip.png'
    start_game = 'image/app/electronic/dt_start.png'
    go_home = 'image/app/go_home.png'

class DtElectronicPage(Base):
    def lgd_electronic(self):
        self.enter_game('赛亚烈战')
        if self.common.wait_image(DtElectronicPageLocator.skip, timeout=20) is True:
            self.common.touch_image(DtElectronicPageLocator.skip)
            self.common.wait_touch(DtElectronicPageLocator.start_game)
        else:
            raise EOFError('找不到指定圖片,讀取超時')
       