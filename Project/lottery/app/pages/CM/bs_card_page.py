import os
from common.app.common import Common
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')

class BsCardPageLocator:
    easy_game = 'image/app/card/bs_easy_game.png'
    
class BsCardPage(Base):

    def bs_card(self):
        self.enter_game('炸金花')
        
        if self.common.wait_image(BsCardPageLocator.easy_game, timeout=20) is True:
            self.common.wait_touch(BsCardPageLocator.easy_game)
        else:
            raise EOFError('找不到指定圖片,讀取超時')