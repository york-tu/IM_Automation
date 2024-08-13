import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class FgElectronicPageLocator:
    start_game = 'image/app/electronic/fg_start.png'
    start_game_2 = 'image/app/electronic/fg_start_2.png'
    go_home = 'image/app/go_home.png'

class FgElectronicPage(Base):
    def fg_electronic(self):
        self.enter_game('金瓶梅')
        if self.common.wait_image(FgElectronicPageLocator.start_game) is True:
            self.common.wait_touch(FgElectronicPageLocator.start_game)
        elif self.common.wait_image(FgElectronicPageLocator.start_game_2) is True:
            self.common.wait_touch(FgElectronicPageLocator.start_game_2)
        else:
            raise EOFError('找不到指定圖片,讀取超時')