import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)

class WebPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method
        
    def webPage(self):
        from Project.lottery.web.pages.pages import WebPages
        return WebPages(*self.pages_parameter)

    def commonPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)
class AppPages:
    def __init__(self, parameter):
        self.pages_parameter = parameter

    def commonPage(self):
        from common.app.common import Common
        return Common(*self.pages_parameter)

    def mainPage(self):
        from Project.exchange_wellpay.app.pages.app.app_main_page import MainPage
        return MainPage(*self.pages_parameter)
    
    def registerPage(self):
        from Project.exchange_wellpay.app.pages.app.app_register_page import RegisterPage
        return RegisterPage(*self.pages_parameter)
    
    def wantbuyPage(self):
        from Project.exchange_wellpay.app.pages.app.app_want_buy_page import WantBuyPage
        return WantBuyPage(*self.pages_parameter)

    def depositPage(self):
        from Project.exchange_wellpay.app.pages.app.app_deposit_page import DepositPage
        return DepositPage(*self.pages_parameter)
    
    def customerservicePage(self):
        from Project.exchange_wellpay.app.pages.app.app_customer_service_page import CustomerServicePage
        return CustomerServicePage(*self.pages_parameter)
    
    def bindpaymentPage(self):
        from Project.exchange_wellpay.app.pages.app.app_bind_payment_page import BindPaymentPagePage
        return BindPaymentPagePage(*self.pages_parameter)
  
    def myPage(self):
        from Project.exchange_wellpay.app.pages.app.app_my_page import MyPage
        return MyPage(*self.pages_parameter)

    def graporderPage(self):
        from Project.exchange_wellpay.app.pages.app.app_grap_order_page import GrapOrderPage
        return GrapOrderPage(*self.pages_parameter)
    
    def myorderPage(self):
        from Project.exchange_wellpay.app.pages.app.app_my_order_page import MyOrderPage
        return MyOrderPage(*self.pages_parameter)

    def mysellPage(self):
        from Project.exchange_wellpay.app.pages.app.app_my_sell_page import MySellPage
        return MySellPage(*self.pages_parameter)

    def myinfoPage(self):
        from Project.exchange_wellpay.app.pages.app.app_my_info_page import MyInfoPage
        return MyInfoPage(*self.pages_parameter)

    def customerservicePage(self):
        from Project.exchange_wellpay.app.pages.app.app_customer_service_page import CustomerServicePage
        return CustomerServicePage(*self.pages_parameter)

    def wantbuyPage(self):
        from Project.exchange_wellpay.app.pages.app.app_want_buy_page import WantBuyPage
        return WantBuyPage(*self.pages_parameter)

    def wantsellPage(self):
        from Project.exchange_wellpay.app.pages.app.app_want_sell_page import WantSellPage
        return WantSellPage(*self.pages_parameter)
    
    def payinfoPage(self):
        from Project.exchange_wellpay.app.pages.app.app_pay_info_page import PayInfoPage
        return PayInfoPage(*self.pages_parameter)

    def depositrecordPage(self):
        from Project.exchange_wellpay.app.pages.app.app_deposit_record_page import DepositRecordPage
        return DepositRecordPage(*self.pages_parameter)


class AdminEPage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method
    
    def commonPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)
    
    def loginPage(self):
        from Project.exchange_wellpay.app.pages.admin.admin_login_page import LoginPage
        return LoginPage(*self.pages_parameter)
    
    def menuPage(self):
        from Project.exchange_wellpay.app.pages.admin.admin_menu_page import MenuPage
        return MenuPage(*self.pages_parameter)

    def rechargeauditPage(self):
        from Project.exchange_wellpay.app.pages.admin.rechargemanagement.admin_recharge_audit_page import RechargeAuditPage
        return RechargeAuditPage(*self.pages_parameter)

    def orderrecordbrandPage(self):
        from Project.exchange_wellpay.app.pages.admin.buymanagement.admin_order_record_brand_page import OrderRecordBrandPage
        return OrderRecordBrandPage(*self.pages_parameter)
    
    def allrecordzqbPage(self):
        from Project.exchange_wellpay.app.pages.admin.sellmanagement.admin_all_record_zqb_page import AllRecordZqbPage
        return AllRecordZqbPage(*self.pages_parameter)
    
    def memberlistPage(self):
        from Project.exchange_wellpay.app.pages.admin.membermanagement.admin_member_list_page import MemberListPage
        return MemberListPage(*self.pages_parameter)
    
    def systemmanagementPage(self):
        from Project.exchange_wellpay.app.pages.admin.systemmanagement.admin_system_management_page import SystemManagementPage
        return SystemManagementPage(*self.pages_parameter)


class AdminPage(AdminEPage):
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method
    
    def commonPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def adminPage(self):
        from Project.lottery.web.pages.pages import AdminPage
        return AdminPage(*self.pages_parameter)
