from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
class PromoPageLocator:
    base = Xpath_Base()

    promotions = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='优惠活动.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='优惠活动.*')
    )

    promotions_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='活动'),
        iOS = base.data_collation(type_kind='name', type_name='活动')
    )

    promo_request_a = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='优惠申请'),
        iOS = base.data_collation(type_kind='name', type_name='优惠申请')
    )
    
    promo_request_b = base.data_collation(type_kind='name', type_name='promo_request')
    promo_content_b = base.data_collation(type_kind='name', type_name='promo_content')
    promo_content_c = base.data_collation(type_kind='name', type_name='tabBarItem_promo_content')

class PromoPageA(Base):
    def promotions(self):
        if not self.common.poco_exists(PromoPageLocator.promotions):
            raise EOFError('進入優惠活動頁面錯誤')

    # def promo_content(self):
    #     if not self.common.poco_exists(PromoPageLocator.promo_content_a):
    #         raise EOFError('進入優惠活動頁面錯誤')

class PromoPageB(Base):
    def promo_request(self):
        if not self.common.poco_exists(PromoPageLocator.promo_content_a):
            raise EOFError('進入優惠活動頁面錯誤')

    def promo_content(self):
        if not self.common.poco_exists(PromoPageLocator.promo_content_b) and not self.common.poco_exists(PromoPageLocator.promo_content_c):
            try:
                try:
                    self.common.poco_click(PromoPageLocator.promo_content_b)
                except:
                    self.common.poco_click(PromoPageLocator.promo_content_c)
            except:
                raise EOFError('點擊選單內的優惠活動錯誤')

class PromoPage(Base):
    def promotions(self):
        if not self.common.poco_exists(PromoPageLocator.promotions_napp):
            raise EOFError('進入活動頁面錯誤')