from Project.lottery.app.pages.base import Base
class AboutPageLocator:
    base = Xpath_Base()
    
    title = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='关于我们.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='关于我们.*')
    )

class AboutPage(Base):
    def about(self):
        if not self.common.poco_exists(AboutPageLocator.title):
            raise EOFError('進入關於我們頁面錯誤')