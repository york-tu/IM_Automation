from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
import random, re

class Red_EnvelopePageLocator:
    base = Xpath_Base()

    mine_sweeping = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='扫雷玩法.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='扫雷玩法.*')
    )

    mine_sweeping_hall = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='新建群组.*', action='parent().sibling()'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='新建群组.*', action='parent().sibling()')
    )

    niu_niu = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='牛牛玩法.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='牛牛玩法.*')
    )

    niu_niu_hall = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='牛牛.*', action='parent().sibling().sibling()'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='牛牛.*', action='parent().sibling().sibling()')
    )

    enter = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='确认进入.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='确认进入.*')
    )

    boss = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='发红包.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='发红包.*')
    )
    
    money = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='元.*', action='parent().children()'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='元.*', action='parent().children()')
    )

    mine = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='请输入雷号.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='请输入雷号.*')
    )

    red_go = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='塞钱进红包.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='塞钱进红包.*')
    )

    amount = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*个.*', action='parent().children()'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*个.*', action='parent().children()')
    )

    magnification = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='本厅最高赔率.*', action='parent().child()[1]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='本厅最高赔率.*', action='parent().child()[1]')
    )

class Red_EnvelopePage(Base):
    def mine_sweeping(self, num):
        self.common.poco_click(Red_EnvelopePageLocator.mine_sweeping)
        self.common.poco_wait_exists(Red_EnvelopePageLocator.mine_sweeping_hall)
        self.common.poco_click(Red_EnvelopePageLocator.mine_sweeping_hall)

        # 每個群組第一次進入時會有提示
        if self.common.poco_exists(Red_EnvelopePageLocator.enter):
            self.common.poco_click(Red_EnvelopePageLocator.enter)

        self.common.poco_wait_exists(Red_EnvelopePageLocator.boss)
        self.common.poco_click(Red_EnvelopePageLocator.boss)

        money = self.common.poco_get_text(Red_EnvelopePageLocator.money)
        money = str(money).replace(' ','').split('-')
        money_less = money[0]
        money_upper = money[1]
        bet_money = random.randint(int(money_less), int(money_less))
        amount =  re.search(r'\d', self.common.poco_get_text(Red_EnvelopePageLocator.amount)).group()

        self.common.poco_send_text(Red_EnvelopePageLocator.money, bet_money)
        self.common.poco_send_text(Red_EnvelopePageLocator.mine, num)
        self.common.sleep(1)
        self.common.poco_click(Red_EnvelopePageLocator.red_go)
        
        assert self.common.poco_wait_exists(Red_EnvelopePageLocator.boss), '發紅包失敗'

        return bet_money, num, amount

    def niu_niu(self):
        self.common.poco_click(Red_EnvelopePageLocator.niu_niu)
        self.common.poco_wait_exists(Red_EnvelopePageLocator.niu_niu_hall)
        self.common.poco_click(Red_EnvelopePageLocator.niu_niu_hall)

        # 每個群組第一次進入時會有提示
        if self.common.poco_exists(Red_EnvelopePageLocator.enter):
            self.common.poco_click(Red_EnvelopePageLocator.enter)
        
        self.common.poco_wait_exists(Red_EnvelopePageLocator.boss)
        self.common.poco_click(Red_EnvelopePageLocator.boss)
        
        magnification = self.common.poco_get_text(Red_EnvelopePageLocator.magnification)
        magnification = re.search(r'\d', magnification).group()

        money = self.common.poco_get_text(Red_EnvelopePageLocator.money)
        money = str(money).replace(' ','').split('-')
        money_less = money[0]
        money_upper = money[1]
        bet_money = random.randint(int(money_less),int(money_less) + 10)

        self.common.poco_send_text(Red_EnvelopePageLocator.money, bet_money)

        amount = self.common.poco_get_text(Red_EnvelopePageLocator.amount)
        amount = str(amount).split('-')
        amount_less = amount[0]
        amount_upper = amount[1]
        bet_amount = random.randint(int(amount_less)+1,int(amount_upper))

        self.common.poco_send_text(Red_EnvelopePageLocator.amount, bet_amount)
        self.common.poco_click(Red_EnvelopePageLocator.red_go)

        assert self.common.poco_wait_exists(Red_EnvelopePageLocator.boss), '發紅包失敗'

        return bet_money, bet_amount, magnification