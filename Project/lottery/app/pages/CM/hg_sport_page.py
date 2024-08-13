import os
from airtest.core.api import *
from datetime import datetime
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class HgSportPageLocator:
    base = Xpath_Base()

    bet_frame = 'image/app/sport/hg_bet_frame.png'
    bet_frame_dark = 'image/app/sport/hg_bet_frame_dark.png'
    soccer = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='足球'),
        iOS = base.data_collation(type_kind='text', type_name='足球')
    )
    amount_edit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='输入下注金额'),
        iOS = base.data_collation(type_kind='text', type_name='输入下注金额')
    )
    btn_2 = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='num_2'),
        iOS = base.data_collation(type_kind='name', type_name='num_2')
    )
    submit = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='order_bet'),
        iOS = base.data_collation(type_kind='name', type_name='order_bet')
    )
    transaction_id = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='您已成功投注.*'),
        iOS = base.data_collation(type_kind='textMatches', type_name='您已成功投注.*')
    )

    accept_change = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='接受变化'),
        iOS = base.data_collation(type_kind='text', type_name='接受变化')
    )

class HgSportPage(Base):
    def hg_sport(self):
        self.click_enter()

        self.common.poco_wait_exists(HgSportPageLocator.soccer)
        self.common.sleep(5)    # 已經找到首頁文字但頁面可能還沒載完

        for loop in range(0, 10):
            self.common.go_down() # 滑動一下頁面, 確保有找到圖片
            if 6 <= int(datetime.now().strftime('%H')) < 18:    # 晚上的背景和白天不一樣
                if self.common.exists_image(HgSportPageLocator.bet_frame):        
                    self.common.touch_image(HgSportPageLocator.bet_frame)
                    if self.common.poco_wait_exists(HgSportPageLocator.amount_edit):
                        break
            else:
                if self.common.exists_image(HgSportPageLocator.bet_frame_dark):
                    self.common.touch_image(HgSportPageLocator.bet_frame_dark)
                    if self.common.poco_wait_exists(HgSportPageLocator.amount_edit):
                        break
            
            if loop == 9:
                raise EOFError('找不到可下注的盤口')

            self.common.sleep(1)    # 停一下以防止太快做第二次滑動造成APP滑掉
        
        self.common.poco_click(HgSportPageLocator.amount_edit)
        self.common.poco_click(HgSportPageLocator.btn_2) # 最小注2塊
        self.common.poco_click(HgSportPageLocator.submit)
        
        if not self.common.poco_wait_exists(HgSportPageLocator.transaction_id):
            if not self.common.poco_wait_exists(HgSportPageLocator.accept_change):
                raise EOFError('下注失敗')