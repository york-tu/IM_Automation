from Project.lottery.app.pages.base import Base
class AgentPageLocator:
    base = Xpath_Base()

    title = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='代理合作.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='代理合作.*')
    )

class AgentPage(Base):
    def bet_record(self):
        if not self.common.poco_exists(AgentPageLocator.title):
            raise EOFError('進入代理合作頁面錯誤')