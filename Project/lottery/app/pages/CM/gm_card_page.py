import os
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')

class GmCardPageLocator:
    easy_game = 'image/app/card/gm_easy_game.png'
    go_home = 'image/app/go_home.png'

class GmCardPage(Base):
    def gm_card(self):
        self.enter_game('炸金花')
        if self.common.wait_image(GmCardPageLocator.easy_game) is True:
            self.common.wait_touch(GmCardPageLocator.easy_game)
            self.common.sleep(3)
        else:
            raise EOFError('找不到指定圖片,讀取超時')