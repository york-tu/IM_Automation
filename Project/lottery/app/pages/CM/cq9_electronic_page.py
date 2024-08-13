import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class Cq9ElectronicPageLocator:
    open_game = 'image/app/electronic/cq9_swipe_up.png'
    start_game = 'image/app/electronic/cq9_start.png'
    get_money = 'image/app/electronic/cq9_get_money.png'
    go_home = 'image/app/go_home.png'

class Cq9ElectronicPage(Base):
   
    def cq9_electronic(self):
        self.enter_game('东方神起')

        # if self.common.wait_image(Cq9ElectronicPageLocator.cq9_open_game) is True:
            # self.common.go_up()
        if self.common.wait_image(Cq9ElectronicPageLocator.start_game) is True:
            self.common.wait_touch(Cq9ElectronicPageLocator.start_game)
            self.common.wait_touch(Cq9ElectronicPageLocator.get_money)
        else:
            raise EOFError('找不到指定圖片,讀取超時')