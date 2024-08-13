from time import sleep
from common.app.common import Common
from Project.exchange.app.pages.app.base import Base
from Project.exchange.app.pages.xpath.xpath_base import Xpath_Base
import common.utils.globalvar as gl


class CustomerServicePageLocator:
    base = Xpath_Base()

    service_title = base.check_device(
        Android=base.data_collation(type_kind='text', type_name='站内客服'),
        iOS=base.data_collation(type_kind='', type_name='')
    )


class CustomerServicePage(Base):
    # 確認客服彈窗
    def check_customer_service(self):
        if self.common.poco_wait_exists(CustomerServicePageLocator.service_title) is False:
            raise EOFError('沒有跳出站內客服')
