import os
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')

class LcCardPageLocator:
    easy_game = 'image/app/card/lc_easy_game.png'
    go_home = 'image/app/go_home.png'

class LcCardPage(Base):
    def lc_card(self):
        self.enter_game('炸金花')
        if self.common.wait_image(LcCardPageLocator.easy_game, timeout=20) is True:
            self.common.wait_touch(LcCardPageLocator.easy_game)
        else:
            raise EOFError('找不到指定圖片,讀取超時')