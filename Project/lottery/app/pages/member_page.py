from time import sleep
from common.app.common import Common
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base

class MemberPageLocator:
    base = Xpath_Base()

    deposit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='充值'),
        iOS = base.data_collation(type_kind='name', type_name='充值')
    )

    withdraw = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='提现'),
        iOS = base.data_collation(type_kind='name', type_name='提现')
    )

    share = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='分享'),
        iOS = base.data_collation(type_kind='name', type_name='分享')
    )

    transform = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='额度转换'),
        iOS = base.data_collation(type_kind='name', type_name='额度转换')
    )

    transform_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='转账'),
        iOS = base.data_collation(type_kind='name', type_name='转账')
    )

    ledger = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='交易流水'),
        iOS = base.data_collation(type_kind='name', type_name='交易流水')
    )

    page_title = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*tvTitle'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*tvTitle')
    )
  
    myinfo = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='我的资料'),
        iOS = base.data_collation(type_kind='name', type_name='我的资料')
    )

    bet_record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='投注记录'),
        iOS = base.data_collation(type_kind='name', type_name='投注记录')
    )

    deposit_record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='充值记录'),
        iOS = base.data_collation(type_kind='name', type_name='充值记录')
    )

    withdraw_record = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='提款记录'),
        iOS = base.data_collation(type_kind='name', type_name='提款记录')
    )

    message = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='讯息'),
        iOS = base.data_collation(type_kind='name', type_name='讯息')
    )

    agent_cooperation = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='代理合作'),
        iOS = base.data_collation(type_kind='name', type_name='代理合作')
    )

    logout = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='登出'),
        iOS = base.data_collation(type_kind='name', type_name='登出')
    )

    about = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='关于我们'),
        iOS = base.data_collation(type_kind='name', type_name='关于我们')
    )

    feedback = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='意见反馈'),
        iOS = base.data_collation(type_kind='name', type_name='意见反馈')
    )

    system = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='系统资讯'),
        iOS = base.data_collation(type_kind='name', type_name='系统资讯')
    )

class MemberPage(Base):
    # 充值
    def deposit_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.deposit):
                self.common.poco_click(MemberPageLocator.deposit)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊充值頁面錯誤')

    # 分享
    def share_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.share):
                self.common.poco_click(MemberPageLocator.share)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊分享頁面錯誤')

    # 額度轉換
    def transform_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.transform):
                self.common.poco_click(MemberPageLocator.transform)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊額度轉換頁面錯誤')

    # 額度轉換
    def transform_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.transform_napp):
            self.common.poco_click(MemberPageLocator.transform_napp)
        else:
            raise EOFError('點擊額度轉換頁面錯誤')

    # 交易流水
    def ledger_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.ledger):
                self.common.poco_click(MemberPageLocator.ledger)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊交易流水頁面錯誤')
    
    # 交易流水
    def ledger_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.ledger):
            self.common.poco_click(MemberPageLocator.ledger)
        else:
            raise EOFError('點擊交易流水頁面錯誤')
            
        self.common.poco_wait_exists(MemberPageLocator.page_title)
        if self.common.poco_get_text(MemberPageLocator.page_title) != '交易流水':
            raise EOFError('進入交易流水頁面錯誤')

    # 提款
    def withdraw_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.withdraw):
                self.common.poco_click(MemberPageLocator.withdraw)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊提款頁面錯誤')

    # 投注記錄
    def bet_record_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.bet_record):
                self.common.poco_click(MemberPageLocator.bet_record)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊投注記錄頁面錯誤')

    # 充值紀錄
    def deposit_record_click(self):
        self.common.poco_click(MemberPageLocator.deposit_record)
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.deposit_record):
                self.common.poco_click(MemberPageLocator.deposit_record)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊充值紀錄頁面錯誤')
    
    # 充值紀錄
    def deposit_record_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.deposit_record):
            self.common.poco_click(MemberPageLocator.deposit_record)
        else:
            raise EOFError('點擊充值紀錄頁面錯誤')

        if self.common.poco_get_text(MemberPageLocator.page_title) != '充值记录':
            raise EOFError('進入充值紀錄頁面錯誤')

    # 提款記錄
    def withdraw_record_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.withdraw_record):
                self.common.poco_click(MemberPageLocator.withdraw_record)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊提款記錄頁面錯誤')
    
    # 提款記錄
    def withdraw_record_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.withdraw_record):
            self.common.poco_click(MemberPageLocator.withdraw_record)
        else:
            raise EOFError('點擊提款記錄頁面錯誤')
        
        if self.common.poco_get_text(MemberPageLocator.page_title) != '提款记录':
            raise EOFError('進入提款記錄頁面錯誤')

    # 訊息
    def message_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.message):
                self.common.poco_click(MemberPageLocator.message)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊訊息頁面錯誤')

    # 代理合作
    def agent_cooperation_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.agent_cooperation):
                self.common.poco_click(MemberPageLocator.agent_cooperation)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊代理合作頁面錯誤')

    # 代理合作
    def agent_cooperation_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.agent_cooperation):
            self.common.poco_click(MemberPageLocator.agent_cooperation)
        else:
            raise EOFError('點擊代理合作頁面錯誤')
        
        if self.common.poco_get_text(MemberPageLocator.page_title) != '代理合作':
            raise EOFError('進入代理合作頁面錯誤')

    # 登出
    def logout_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.logout):
                self.common.poco_click(MemberPageLocator.logout)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊登出頁面錯誤')

    # 關於我們
    def about_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.about):
                self.common.poco_click(MemberPageLocator.about)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊關於我們頁面錯誤')
    
    # 關於我們
    def about_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.about):
            self.common.poco_click(MemberPageLocator.about)
        else:
            raise EOFError('點擊關於我們頁面錯誤')
        
        if self.common.poco_get_text(MemberPageLocator.page_title) != '关于我们':
            raise EOFError('進入關於我們頁面錯誤')

    # 意見反饋
    def feedback_cooperation_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.feedback):
                self.common.poco_click(MemberPageLocator.feedback)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊意見反饋頁面錯誤')
    
    # 意見反饋
    def feedback_cooperation_click_napp(self):
        self.common.go_bottom()
        if self.common.poco_exists(MemberPageLocator.feedback):
            self.common.poco_click(MemberPageLocator.feedback)
        else:
            raise EOFError('點擊意見反饋頁面錯誤')
        
        if self.common.poco_get_text(MemberPageLocator.page_title) != '意⾒反馈':
            raise EOFError('進入意見反饋頁面錯誤')

    # 系統
    def system_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.system):
                self.common.poco_click(MemberPageLocator.system)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊系統頁面錯誤')

    # 我的資料
    def myinfo_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MemberPageLocator.myinfo):
                self.common.poco_click(MemberPageLocator.myinfo)
                return
            else:
                self.common.go_down()

                if loop == 2:
                    raise EOFError('點擊我的資訊頁面錯誤')

    # 我的資料
    def myinfo_click_napp(self):
        if self.common.poco_exists(MemberPageLocator.myinfo):
            self.common.poco_click(MemberPageLocator.myinfo)
        else:
            raise EOFError('點擊我的資料頁面錯誤')
        
        if self.common.poco_get_text(MemberPageLocator.page_title) != '我的资料':
            raise EOFError('進入我的資料頁面錯誤')