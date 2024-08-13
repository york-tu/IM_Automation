import os
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')

class KyCardPageLocator:
    easy_game = 'image/app/card/ky_easy_game.png'
    check_icon = 'image/app/card/ky_check_icon.png'
    go_home = 'image/app/go_home.png'

class KyCardPage(Base):
    def ky_card(self):
        self.enter_game('炸金花')

        if self.common.wait_image(KyCardPageLocator.easy_game, timeout=20) is True:
            self.common.wait_touch(KyCardPageLocator.easy_game)
        else:
            raise EOFError('找不到指定圖片,讀取超時')

        for i in range(5):
            if self.common.wait_image(KyCardPageLocator.check_icon) is True:
                self.common.wait_touch(KyCardPageLocator.check_icon)
                break
            elif i == 4:
                raise EOFError('找不到指定圖片,讀取超時')
