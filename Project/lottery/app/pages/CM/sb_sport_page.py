import os
from airtest.core.api import *
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
path1=os.path.abspath('.')

class SbSportPageLocator:
    base = Xpath_Base()

    page_style_popup = base.data_collation(type_kind='text', type_name='选择好了!立即开始')       # 版本樣式選擇彈窗

    style_remind_button = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='我知道了'),
        iOS = base.data_collation(type_kind='text', type_name='我知道了')
    )

    soccer = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*足球.*'),
        iOS = base.data_collation(type_kind='textMatches', type_name='.*足球.*')
    )
    
    odds = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name=r'\d*\.\d*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name=r'\d*\.\d*')
    )

    submit = 'image/app/sport/sb_submit.png'
    
    success = 'image/app/sport/sb_success.png'

    odds_adjustment = 'image/app/sport/sb_odds_adjustment'

class SbSportPage(Base):
    def sb_sport(self):
        self.click_enter()
        
        if self.common.poco_wait_exists(SbSportPageLocator.page_style_popup, timeout=30):      
            self.common.poco_click(SbSportPageLocator.page_style_popup)
        
        if self.common.poco_wait_exists(SbSportPageLocator.soccer, timeout=10):
                self.common.poco_click(SbSportPageLocator.soccer)
        else:
            raise EOFError('找不到足球遊戲')

        if self.common.poco_wait_exists(SbSportPageLocator.style_remind_button):      
            self.common.poco_click(SbSportPageLocator.style_remind_button)

        for loop in range(0, 10): 
            self.common.go_down() # 滑動一下頁面, 確保poco有擷取到頁面的element
            self.common.go_up() # 滑回來以免定位到頁面上方無法點擊
            if self.common.poco_wait_exists(SbSportPageLocator.odds, timeout=10):
                self.common.poco_click(SbSportPageLocator.odds)
            
            if self.common.wait_image(SbSportPageLocator.submit, timeout=10):
                break

            if loop == 9:
                raise EOFError('找不到可下注的盤口')
        
        # sb體育投注器點擊提交會自動帶入最小注額, 不用自己輸入
        self.common.touch_image(SbSportPageLocator.submit)
        self.common.sleep(1)
        self.common.touch_image(SbSportPageLocator.submit)
        
        if not self.common.wait_image(SbSportPageLocator.odds_adjustment, timeout=10):
            if not self.common.wait_image(SbSportPageLocator.success):
                raise EOFError('下注失敗')