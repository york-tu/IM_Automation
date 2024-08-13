import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class FgCardPageLocator:
    easy_game = 'image/app/card/fg_easy_game.png'
    check_icon = 'image/app/card/fg_check_icon.png'
    go_home = 'image/app/go_home.png'

class FgCardPage(Base):
    def fg_card(self):
        self.enter_game('经典炸金花')
        if self.common.wait_image(FgCardPageLocator.easy_game) is True:
            self.common.wait_touch(FgCardPageLocator.easy_game)
            self.common.wait_image(FgCardPageLocator.check_icon)
            self.common.sleep(3)
        else:
            raise EOFError('找不到指定圖片,讀取超時')