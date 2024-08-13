import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class KkElectronicPageLocator:
    kk_lobby = 'image/app/electronic/kk_lobby_game.png'
    go_home = 'image/app/go_home.png'

class KkElectronicPage(Base):
    def kk_electronic(self):
        self.click_enter()

        if self.common.wait_image(KkElectronicPageLocator.kk_lobby, timeout=20) is True:
            pass
        else:
            raise EOFError('找不到指定圖片,讀取超時')