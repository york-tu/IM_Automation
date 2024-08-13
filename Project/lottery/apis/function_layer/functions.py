import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)

class Functions:
    def __init__(self, skip_test_method=''):
        self.pages_parameter = skip_test_method

    def ui_web_register(self):
        from function_layer.uiapi.web.help.register import Register
        return Register(self.pages_parameter)

    def ui_base_function(self):
        from function_layer.base_functions import BaseFunction
        return BaseFunction(self.pages_parameter)

    def ui_web_my_wallet(self):
        from function_layer.uiapi.web.member_panel.my_wallet import MyWallet
        return MyWallet(self.pages_parameter)

    def ui_web_my_profile(self):
        from function_layer.uiapi.web.member_panel.my_profile import MyProfile
        return MyProfile(self.pages_parameter)

    def ui_web_my_news(self):
        from function_layer.uiapi.web.member_panel.my_news import MyNews
        return MyNews(self.pages_parameter)

    def ui_web_third_party(self):
        from function_layer.uiapi.web.third_party.third_party import ThirdParty
        return ThirdParty(self.pages_parameter)

    def ui_web_utils(self):
        from function_layer.uiapi.web.utils.uiapi_utils import Utils
        return Utils(self.pages_parameter)

    def ui_admin_betting_center(self):
        from function_layer.uiapi.admin.operation_management.betting_center import BettingCenter
        return BettingCenter(self.pages_parameter)

    def ui_admin_handicap(self):
        from function_layer.uiapi.admin.operation_management.handicap import Handicap
        return Handicap(self.pages_parameter)

    def ui_admin_redenvelope(self):
        from function_layer.uiapi.admin.operation_management.red_envelope import RedEnvelope
        return RedEnvelope(self.pages_parameter)

    def ui_admin_account_management(self):
        from function_layer.uiapi.admin.financial_management.account_management import AccountManagement
        return AccountManagement(self.pages_parameter)

    def ui_admin_fin_scale_setting(self):
        from function_layer.uiapi.admin.financial_management.scale_setting import ScaleSetting
        return ScaleSetting(self.pages_parameter)

    def ui_admin_deposit_management(self):
        from function_layer.uiapi.admin.financial_management.deposit_management import DepositManagement
        return DepositManagement(self.pages_parameter)

    def ui_admin_withdraw_management(self):
        from function_layer.uiapi.admin.financial_management.withdraw_management import WithdrawManagement
        return WithdrawManagement(self.pages_parameter)

    def ui_admin_cash_system(self):
        from function_layer.uiapi.admin.financial_management.cash_system import CashSystem
        return CashSystem(self.pages_parameter)
    
    def ui_admin_manual_deposit(self):
        from function_layer.uiapi.admin.financial_management.manual_deposit import ManualDeposit
        return ManualDeposit(self.pages_parameter)

    def ui_admin_external_platform(self):
        from function_layer.uiapi.admin.financial_management.external_platform import ExternalPlatform
        return ExternalPlatform(self.pages_parameter)

    def ui_admin_rebate_scale_setting(self):
        from function_layer.uiapi.admin.rebate_and_commision.scale_setting import ScaleSetting
        return ScaleSetting(self.pages_parameter)

    def ui_admin_member_list(self):
        from function_layer.uiapi.admin.member_management.member_list import MemberList
        return MemberList(self.pages_parameter)
    
    def ui_admin_game_setting(self):
        from function_layer.uiapi.admin.system_management.game_setting import GameSetting
        return GameSetting(self.pages_parameter)
    
    def ui_admin_system_list(self):
        from function_layer.uiapi.admin.system_management.system_list import SystemList
        return SystemList(self.pages_parameter)

    def ui_admin_station_news(self):
        from function_layer.uiapi.admin.customer_service.station_news import StationNews
        return StationNews(self.pages_parameter)

    def ui_admin_member_analysis(self):
        from function_layer.uiapi.admin.operational_risk_control.member_analysis import MemberAnalysis
        return MemberAnalysis(self.pages_parameter)

    def ui_admin_general_report(self):
        from function_layer.uiapi.admin.report_management.general_report import GeneralReport
        return GeneralReport(self.pages_parameter)

    def ui_admin_channel_report(self):
        from function_layer.uiapi.admin.report_management.channel_report import ChannelReport
        return ChannelReport(self.pages_parameter)

    def ui_admin_daily_report(self):
        from function_layer.uiapi.admin.report_management.daily_report import DailyReport
        return DailyReport(self.pages_parameter)

    def mynah_web_customer_service(self):
        from function_layer.uiapi.mynah.mynah_web_customer_service import MynahWebService
        return MynahWebService(self.pages_parameter)
    
    def ui_admin_deposit_offer(self):
        from function_layer.uiapi.admin.financial_management.deposit_offer import DepositOffer
        return DepositOffer(self.pages_parameter)

    def ui_admin_float_window(self):
        from function_layer.uiapi.admin.market_center.float_window import FloatingWindow
        return FloatingWindow(self.pages_parameter)
    
    def ui_admin_event_managment(self):
        from function_layer.uiapi.admin.market_center.event_management import EventManagement
        return EventManagement(self.pages_parameter)

    def ui_admin_bank_account(self):
        from function_layer.uiapi.admin.financial_management.bank_account import BankAccount
        return BankAccount(self.pages_parameter)

    def ui_admin_handling_fee(self):
        from function_layer.uiapi.admin.financial_management.handling_fee import HandlingFee
        return HandlingFee(self.pages_parameter)

    def ui_admin_interface_management(self):
        from function_layer.uiapi.admin.financial_management.interface_management import InterfaceManagement
        return InterfaceManagement(self.pages_parameter)
    
    def ui_admin_maintain_setting(self):
        from function_layer.uiapi.admin.operation_management.maintain_setting import MaintainSetting
        return MaintainSetting(self.pages_parameter)

    def ui_admin_period_management(self):
        from function_layer.uiapi.admin.operation_management.period_management import PeriodManagement
        return PeriodManagement(self.pages_parameter)

    def ui_admin_deposit_limit(self):
        from function_layer.uiapi.admin.financial_management.deposit_limit import DepositLimit
        return DepositLimit(self.pages_parameter)