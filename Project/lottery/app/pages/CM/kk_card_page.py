import os
from Project.lottery.app.pages.base import Base
from airtest.core.api import *
path1=os.path.abspath('.')

class KkCardPageLocator:
    kk_lobby = 'image/app/card/kk_lobby_card.png'
    go_home = 'image/app/go_home.png'
class KkCardPage(Base):
    def kk_card(self):
        self.click_enter()

        for i in range(3):
            if self.common.wait_image(KkCardPageLocator.kk_lobby) is True:      # 某些手機不吃timeout時間，改用迴圈多等幾次
                break
            if i == 2:
                raise EOFError('找不到指定圖片,讀取超時')