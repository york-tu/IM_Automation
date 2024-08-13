import os
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')
class VgCardPageLocator:
    easy_game = 'image/app/card/vg_easy_game.png'
    go_home = 'image/app/go_home.png'

class VgCardPage(Base):
    def vg_card(self):
        self.enter_game('炸金花')
        if self.common.wait_image(VgCardPageLocator.easy_game) is True:
            self.common.wait_touch(VgCardPageLocator.easy_game)
            self.common.sleep(3)
        else:
            raise EOFError('找不到指定圖片,讀取超時')