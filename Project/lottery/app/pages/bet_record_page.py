from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
import datetime
class BetRecordPageLocator:
    base = Xpath_Base()

    # 由於注單詳情有時候定位不一樣,故暫時先以兩個都裝
    detail_a = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注单详情.*', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='name', type_name='公司入款')
    )
    
    detail_b = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注单详情.*', action='parent().child()[3]'),
        iOS = base.data_collation(type_kind='name', type_name='公司入款')
    )
    
    list_number = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注单详情.*', action='parent().child()[7]'),
        iOS = base.data_collation(type_kind='name', type_name='公司入款')
    )
    
    period = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注单详情.*', action='parent().child()[10]'),
        iOS = base.data_collation(type_kind='name', type_name='公司入款')
    )
    
    money = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注单详情.*', action='parent().child()[13]'),
        iOS = base.data_collation(type_kind='name', type_name='公司入款')
    )

    filter_btn = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='筛选'),
        iOS = base.data_collation(type_kind='name', type_name='进程暂停 筛选', num=-1)
    )

class BetRecordPage(Base):
    def bet_mine_record(self, money, num, amount):
        if self.common.poco_wait_exists(BetRecordPageLocator.detail_a):
            for i in range(0, 2):
                try:
                    detial_a = self.common.poco_get_text(BetRecordPageLocator.detail_a)
                    detial_b = self.common.poco_get_text(BetRecordPageLocator.detail_b)
                    list_number = self.common.poco_get_text(BetRecordPageLocator.list_number)
                    period = self.common.poco_get_text(BetRecordPageLocator.period)
                    money_record = str(self.common.poco_get_text(BetRecordPageLocator.money)).split(']')
                    break
                except:
                    self.common.go_down()

                if i == 1:
                    raise EOFError('抓取記錄錯誤')

            assert detial_a.__contains__('扫雷:发包') or detial_b.__contains__('扫雷:发包'), f'投注記錄沒顯示 掃雷:發包, 單號:{period} 期數:{list_number} 紅包數量:{amount}'
            assert detial_a.__contains__(f'{num}@') or detial_b.__contains__(f'{num}@'), f'投注記錄雷好錯誤,應該為雷號:{num}, 單號:{period} 期數:{list_number} 紅包數量:{amount}'
            assert money_record[1].__contains__(f'{money}'), f'金額錯誤:{money_record[0][1:]}{money_record[1]}, 應該為:{money} \
                , 單號:{period} 期數:{list_number} 紅包數量:{amount}'
        
    def bet_niu_niu_record(self, money, amount, magnification):
        if self.common.poco_wait_exists(BetRecordPageLocator.detail_a):
            for i in range(0, 2):
                try:
                    detial_a = self.common.poco_get_text(BetRecordPageLocator.detail_a)
                    detial_b = self.common.poco_get_text(BetRecordPageLocator.detail_b)
                    list_number = self.common.poco_get_text(BetRecordPageLocator.list_number)
                    period = self.common.poco_get_text(BetRecordPageLocator.period)
                    money_record = str(self.common.poco_get_text(BetRecordPageLocator.money)).split(']') 
                    total_money = f'{str(money)}*{str(magnification)}'
                    break
                except:
                    self.common.go_down()
                
                if i == 1:
                    raise EOFError('抓取記錄錯誤')

            assert detial_a.__contains__('牛牛:发包') or detial_b.__contains__('牛牛:发包'), f'投注記錄沒顯示 牛牛:发包, 單號:{period} 期數:{list_number} 紅包數量:{amount}'
            assert detial_a.__contains__(f'{money}') or detial_b.__contains__(f'{money}'), f'投注金額不對, 金額:{money} 單號:{period} 期數:{list_number} 紅包數量:{amount}'
            
            # 因為賠率只抓最高的,如果牛牛賠率不是最高的話,開紅包內的賠率會異常,故暫時不比對
            # assert detial.__contains__(f'{total_money}'), f'投注記錄金額倍率錯誤,應為:{total_money} 單號:{period} 期數:{list_number} 紅包數量:{amount}'
            # assert money_record[1].__contains__(f'{money}'), f'金額錯誤:{money_record[0][1:]}{money_record[1]}, 應該為:{money} \
                # , 單號:{period} 期數:{list_number} 紅包數量:{amount}'

    def filter_data(self):
        self.common.poco_click(BetRecordPageLocator.filter_btn)
        pass