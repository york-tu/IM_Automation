import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
path1=os.path.abspath('.')

class SwElectronicPageLocator:
    enter = 'image/app/electronic/sw_enter.png'
    set_money = 'image/app/electronic/sw_set_money.png'
    decrease = 'image/app/electronic/sw_decrease.png'
    start_game = 'image/app/electronic/sw_start.png'
    go_home = 'image/app/go_home.png'

class SwElectronicPage(Base):
    def sw_electronic(self):
        self.enter_game('亚马逊美人')
        self.common.sleep(3)

        if self.common.wait_image(SwElectronicPageLocator.enter) is True:
            self.common.wait_touch(SwElectronicPageLocator.enter)
            # sw環境是真錢, 把注額設為最小
            self.common.wait_touch(SwElectronicPageLocator.set_money)
            for _ in range(7):
                self.common.wait_touch(SwElectronicPageLocator.decrease)

            self.common.wait_touch( SwElectronicPageLocator.start_game)
        else:
            raise EOFError('找不到指定圖片,讀取超時')