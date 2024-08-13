import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class WebPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def messagePage(self):
        from pages.webs.web.web_messagepage import MessagePage
        return MessagePage(*self.pages_parameter)

    def basePage(self):
        from pages.webs.web.webs_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def mainPage(self):
        from pages.webs.web.web_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def lotteryPage(self):
        from pages.webs.web.web_lotterypage import LotteryPage
        return LotteryPage(*self.pages_parameter)

    def lotteryGamePage(self):
        from pages.webs.web.web_lotterygamepage import LotteryGamePage
        return LotteryGamePage(*self.pages_parameter)

    def memberPage(self):
        from pages.webs.web.web_memberpage import MemberPage
        return MemberPage(*self.pages_parameter)

    def menuPage(self):
        from pages.webs.web.web_menupage import MenuPage
        return MenuPage(*self.pages_parameter)

    def registerPage(self):
        from pages.webs.web.web_registerpage import RegisterPage
        return RegisterPage(*self.pages_parameter)

    def gameRecordPage(self):
        from pages.webs.web.web_order_recordpage import GameRecord
        return GameRecord(*self.pages_parameter)

    def chessPage(self):
        from pages.webs.web.web_chesspage import ChessPage
        return ChessPage(*self.pages_parameter)

    def fishPage(self):
        from pages.webs.web.web_fishpage import FishPage
        return FishPage(*self.pages_parameter)

    def sportPage(self):
        from pages.webs.web.web_sportpage import SportPage
        return SportPage(*self.pages_parameter)

    def electronicPage(self):
        from pages.webs.web.web_electronicpage import ElectronicPage
        return ElectronicPage(*self.pages_parameter)

    def casinoPage(self):
        from pages.webs.web.web_casinopage import CasinoPage
        return CasinoPage(*self.pages_parameter)

    def lotterylist(self):
        from pages.lotterylist import LotteryList
        return LotteryList(*self.pages_parameter)

    def apibasefunction(self):
        from Project.lottery.apis.function_layer.base_functions import BaseFunction
        return BaseFunction()

    def paybox_page(self):
        from Project.lottery.web.pages.webs.web.web_payboxpage import PayBoxPage
        # pages.webs.web.web_payboxpage import (PayBoxPage)
        return PayBoxPage(*self.pages_parameter)

    def withdraw_record_page(self):
        from pages.webs.web.web_withdraw_record import WithdrawRecordPage
        return WithdrawRecordPage(*self.pages_parameter)
class MobilePage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def basePage(self):
        from pages.webs.mobile.mobile_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def mainPage(self):
        from pages.webs.mobile.mobile_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def loginPage(self):
        from pages.webs.mobile.mobile_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def messagePage(self):
        from pages.webs.mobile.mobile_messagepage import MessagePage
        return MessagePage(*self.pages_parameter)

    def menuPage(self):
        from pages.webs.mobile.mobile_menupage import MenuPage
        return MenuPage(*self.pages_parameter)
    
    def servicePage(self):
        from pages.webs.mobile.mobile_servicepage import ServicePage
        return ServicePage(*self.pages_parameter)

    def redEnvelopePage(self):
        from pages.webs.mobile.mobile_redenvelopepage import RedEnvalope
        return RedEnvalope(*self.pages_parameter)

    def depositPage(self):
        from pages.webs.mobile.mobile_depositpage import DepositPage
        return DepositPage(*self.pages_parameter)

    def withdrawPage(self):
        from pages.webs.mobile.mobile_withdrawpage import WithDrawPage
        return WithDrawPage(*self.pages_parameter)

    def thirdPartyWalletPage(self):
        from pages.webs.mobile.mobile_thirdpartywalletpage import ThirdPartyWalletPage
        return ThirdPartyWalletPage(*self.pages_parameter)

    def registerPage(self):
        from pages.webs.mobile.mobile_registerpage import RegisterPage
        return RegisterPage(*self.pages_parameter)

    def memberCenterPage(self):
        from pages.webs.mobile.mobile_membercenterpage import MemberCenterPage
        return MemberCenterPage(*self.pages_parameter)

    def lotteryGamePage(self):
        from pages.webs.mobile.mobile_lotterygamepage import LotteryGamePage
        return LotteryGamePage(*self.pages_parameter)

    def chatRoomPage(self):
        from pages.webs.mobile.mobile_chatroompage import ChatRoomPage
        return ChatRoomPage(*self.pages_parameter)

    def memberInfoPage(self):
        from pages.webs.mobile.mobile_memberinfopage import MemberInfoPage
        return MemberInfoPage(*self.pages_parameter)

    def gameRecordPage(self):
        from pages.webs.mobile.mobile_order_recordpage import GameRecord
        return GameRecord(*self.pages_parameter)

    def Store_Record_Page(self):
        from pages.webs.mobile.mobile_stored_recordpage import Store_Record_Page
        return Store_Record_Page(*self.pages_parameter)

    def chessPage(self):
        from pages.webs.mobile.mobile_chesspage import ChessPage
        return ChessPage(*self.pages_parameter)

    def fishPage(self):
        from pages.webs.mobile.mobile_fishpage import FishPage
        return FishPage(*self.pages_parameter)

    def sportPage(self):
        from pages.webs.mobile.mobile_sportpage import SportPage
        return SportPage(*self.pages_parameter)

    def electronicPage(self):
        from pages.webs.mobile.mobile_electronicpage import ElectronicPage
        return ElectronicPage(*self.pages_parameter)

    def casinoPage(self):
        from pages.webs.mobile.mobile_casinopage import CasinoPage
        return CasinoPage(*self.pages_parameter)

    def feedback_page(self):
        from pages.webs.mobile.mobile_feedbackpage import FeedBackPage
        return FeedBackPage(*self.pages_parameter)

    def lotterylist(self):
        from pages.lotterylist import LotteryList
        return LotteryList(*self.pages_parameter)

    def apibasefunction(self):
        from Project.lottery.apis.function_layer.base_functions import BaseFunction
        return BaseFunction()

class AdminPage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def loginPage(self):
        from pages.admin.admin_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def basePage(self):
        from pages.admin.admin_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def companyDepositPage(self):
        from pages.admin.financialmanagement.admin_companydepositpage import CompanyDepositPage
        return CompanyDepositPage(*self.pages_parameter)

    def OnlineDepositPage(self):
        from pages.admin.financialmanagement.admin_onlinedepositpage import OnlineDepositPage
        return OnlineDepositPage(*self.pages_parameter)

    def withdrawPage(self):
        from pages.admin.financialmanagement.admin_withdrawpage import WithdrawPage
        return WithdrawPage(*self.pages_parameter)

    def operationmanagementPage(self):
        from pages.admin.operationmanagement.admin_operationmanagementpage import OperationManagementPage
        return OperationManagementPage(*self.pages_parameter)

    def hall_management_page(self):
        from pages.admin.operationmanagement.admin_hallmanagementpage import HallManagement
        return HallManagement(*self.pages_parameter)

    def PeriodManagementPage(self):
        from pages.admin.operationmanagement.admin_period_management_page import PeriodManagementPage
        return PeriodManagementPage(*self.pages_parameter)

    def OddsManagementPage(self):
        from pages.admin.operationmanagement.admin_Odds_management_page import OddsManagementPage
        return OddsManagementPage(*self.pages_parameter)

    def financialmanagementPage(self):
        from pages.admin.financialmanagement.admin_financialmanagementpage import FinancialManagementPage
        return FinancialManagementPage(*self.pages_parameter)

    def payoutstatiscticsPage(self):
        from pages.admin.operationmanagement.admin_payoutstatisticspage import PayoutStatisticsPage
        return PayoutStatisticsPage(*self.pages_parameter)

    def ticketcheckPage(self):
        from pages.admin.operationmanagement.admin_ticketcheckpage import TicketCheckPage
        return TicketCheckPage(*self.pages_parameter)
    
    def ticketcenterPage(self):
        from pages.admin.operationmanagement.admin_ticketcenterpage import TicketCenterPage
        return TicketCenterPage(*self.pages_parameter)

    def BettingLimitPage(self):
        from pages.admin.operationmanagement.admin_bettinglimitpage import BettingLimit
        return BettingLimit(*self.pages_parameter)

    def reportmanagementPage(self):
        from pages.admin.reportmanagement.admin_reportmanagementpage import ReportManagementPage
        return ReportManagementPage(*self.pages_parameter)

    def rebateandcommisionPage(self):
        from pages.admin.rebateandcommision.admin_rebateandcommisionpage import RebateAndCommisionPage
        return RebateAndCommisionPage(*self.pages_parameter)

    def generalReportPage(self):
        from pages.admin.reportmanagement.admin_generalreportpage import GeneralReportPage
        return GeneralReportPage(*self.pages_parameter)

    def channelReportPage(self):
        from pages.admin.reportmanagement.admin_channelreportpage import ChannelReportPage
        return ChannelReportPage(*self.pages_parameter)

    def dailyReportPage(self):
        from pages.admin.reportmanagement.admin_dailyreportpage import DailyReportPage
        return DailyReportPage(*self.pages_parameter)

    def Pay_Branch_Page(self):
        from pages.admin.financialmanagement.admin_bankaccount_page import Pay_Branch_Page
        return Pay_Branch_Page(*self.pages_parameter)

    def BankAcconut_PageLocator(self):
        from pages.admin.financialmanagement.admin_bankaccount_page import BankAcconut_PageLocator
        return BankAcconut_PageLocator(*self.pages_parameter)

    def OnlinePay_Branch_Page(self):
        from pages.admin.financialmanagement.admin_onlinebankaccount_page import OnlinePay_Branch_Page
        return OnlinePay_Branch_Page(*self.pages_parameter)

    def walletaddressPage(self):
        from pages.admin.financialmanagement.admin_wallet_address_page import WalletAddressPage
        return WalletAddressPage(*self.pages_parameter)

    def OnlineMerchantPage(self):
        from pages.admin.financialmanagement.admin_onlinemerchant_page import OnlineMerchantPage
        return OnlineMerchantPage(*self.pages_parameter)

    def HandingFeePage(self):
        from pages.admin.financialmanagement.admin_handing_fee_page import HandingFeePage
        return HandingFeePage(*self.pages_parameter)

    def DifferentReportPage(self):
        from pages.admin.financialmanagement.admin_different_report_page import DifferentReportPage
        return DifferentReportPage(*self.pages_parameter)

    def OnlineBankAcconut_PageLocator(self):
        from pages.admin.financialmanagement.admin_onlinebankaccount_page import OnlineBankAcconut_PageLocator
        return OnlineBankAcconut_PageLocator(*self.pages_parameter)
    
    def FinancialReportPage(self):
        from pages.admin.financialmanagement.admin_financialreportpage import FinancialReportPage
        return FinancialReportPage(*self.pages_parameter)

    def CheckRecord(self):
        from pages.admin.operationmanagement.admin_ticket_recordpage import CheckRecord
        return CheckRecord(*self.pages_parameter)

    def MemberList(self):
        from pages.admin.membermanagement.admin_memberlistpage import MemberList
        return MemberList(*self.pages_parameter)

    def levelmanagementPage(self):
        from pages.admin.membermanagement.admin_levelmanagementpage import LevelManagementPage
        return LevelManagementPage(*self.pages_parameter)

    def withdrawGeneralPage(self):
        from pages.admin.financialmanagement.admin_withdrawgeneralpage import WithdrawGeneralPage
        return WithdrawGeneralPage(*self.pages_parameter)

    def CPLedgerPage(self):
        from pages.admin.financialmanagement.admin_cpledgerpage import AdminCPLedgerPage
        return AdminCPLedgerPage(*self.pages_parameter)

    def ThirdPartyLedgerPage(self):
        from pages.admin.financialmanagement.admin_thirdpartyledgerpage import AdminThirdPartyLedgerPage
        return AdminThirdPartyLedgerPage(*self.pages_parameter)

    def ExternalPlateformLedgerPage(self):
        from pages.admin.financialmanagement.admin_externalplateformledgerpage import AdminExternalPlateformPage
        return AdminExternalPlateformPage(*self.pages_parameter)

    def ExternalPlateformBalanceInquire(self):
        from pages.admin.financialmanagement.admin_externalplateformbalanceinquire import BalanceInquire
        return BalanceInquire(*self.pages_parameter)

    def ExternalPlateformWalletPage(self):
        from pages.admin.financialmanagement.admin_wallettransferpage import WalletTransfer
        return WalletTransfer(*self.pages_parameter)

    def CommisionPage(self):
        from pages.admin.rebateandcommision.admin_commisionpage import CommisionPage
        return CommisionPage(*self.pages_parameter)

    def AgentPage(self):
        from pages.admin.rebateandcommision.admin_agentpage import AgentPage
        return AgentPage(*self.pages_parameter)

    def NewSettlementPage(self):
        from pages.admin.rebateandcommision.admin_new_settlementpage import NewSettlementPage
        return NewSettlementPage(*self.pages_parameter)

    def operationriskcontrolpage(self):
        from pages.admin.operationriskcontrol.admin_operationriskcontrolpage import OperationRiskControlPage
        return OperationRiskControlPage(*self.pages_parameter)

    def MarketCenterPage(self):
        from pages.admin.marketcenter.admin_marketcenterpage import MarketCenterPage
        return MarketCenterPage(*self.pages_parameter)

    def membermanagementpage(self):
        from pages.admin.membermanagement.admin_membermanagementpage import MemberManagementPage
        return MemberManagementPage(*self.pages_parameter)

    def ServiceAgentPage(self):
        from pages.admin.serviceagent.admin_serviceagentpage import ServiceAgentPage
        return ServiceAgentPage(*self.pages_parameter)

    def feedback_page(self):
        from pages.admin.serviceagent.admin_feedbackpage import FeedbackPage
        return FeedbackPage(*self.pages_parameter)
        
    def systemmanagementpage(self):
        from pages.admin.systemmanagement.admin_systemmanagementpage import SystemManagementPage
        return SystemManagementPage(*self.pages_parameter)

    def RealTimeOrderPage(self):
        from pages.admin.operationmanagement.admin_realtimelottery import RealTimeOrderPage
        return RealTimeOrderPage(*self.pages_parameter)
    
    def ManwithdrawPage(self):
        from pages.admin.financialmanagement.admin_manwithdraw_page import ManwithdrawPage
        return ManwithdrawPage(*self.pages_parameter)

    def GameManagement(self):
        from pages.admin.systemmanagement.admin_gamemanagementpage import GameManagementPage
        return GameManagementPage(*self.pages_parameter)

    def GameSetting(self):
        from pages.admin.operationmanagement.admin_gamesettingpage import GameSettingPage
        return GameSettingPage(*self.pages_parameter)

    def GameList(self):
        from pages.admin.operationmanagement.admin_gamelistpage import GameList
        return GameList(*self.pages_parameter)

    def ChannelSettingsPage(self):
        from pages.admin.operationmanagement.admin_channel_settings_page import ChannelSettingsPage
        return ChannelSettingsPage(*self.pages_parameter)

    def DepositeOverview(self):
        from pages.admin.financialmanagement.admin_depositeoverviewpage import DepositeOverviewPage
        return DepositeOverviewPage(*self.pages_parameter)

    def MemberWallet(self):
        from pages.admin.financialmanagement.admin_memberwalletpage import MemberWalletPage
        return MemberWalletPage(*self.pages_parameter)

    def WebsiteSetting(self):
        from pages.admin.systemmanagement.admin_websitesettingpage import WebsiteSettingPage
        return WebsiteSettingPage(*self.pages_parameter)

    def ManualDeposit(self):
        from pages.admin.financialmanagement.admin_manualdeposit_page import ManualDepositPage
        return ManualDepositPage(*self.pages_parameter)

    def ArtificialDeposit(self):
        from pages.admin.financialmanagement.admin_artificialdepositpage import ArtificialDepositPage
        return ArtificialDepositPage(*self.pages_parameter)

    def StationNews(self):
        from pages.admin.serviceagent.admin_stationnewspage import StationNewsPage
        return StationNewsPage(*self.pages_parameter)

    def LoginAnnouncement(self):
        from pages.admin.marketcenter.admin_loginAnnouncement import LoginAnnouncementPage
        return LoginAnnouncementPage(*self.pages_parameter)

    def FloatWindows(self):
        from pages.admin.marketcenter.admin_floatwindowspage import FloatWindowsPage
        return FloatWindowsPage(*self.pages_parameter)

# class BBSPage:
#     def __init__(self, driver, wait_sec, base_url, skip_test_method):
#         self.pages_parameter = driver, wait_sec, base_url, skip_test_method

#     def mainPage(self):
#         from pages.BBS.bbs_mainpage import MainPage
#         return MainPage(*self.pages_parameter)

#     def basePage(self):
#         from pages.BBS.bbs_basepage import BasePage
#         return BasePage(*self.pages_parameter)

#     def memberPage(self):
#         from pages.BBS.bbs_memberpage import MemberPage
#         return MemberPage(*self.pages_parameter)

#     def informationPage(self):
#         from pages.BBS.bbs_informationpage import InformationPage
#         return InformationPage(*self.pages_parameter)

#     def balldatePage(self):
#         from pages.BBS.bbs_balldatepage import BallDatePage
#         return BallDatePage(*self.pages_parameter)

#     def historyPage(self):
#         from pages.BBS.bbs_historypage import HistoryPage
#         return HistoryPage(*self.pages_parameter)

#     def assistantPage(self):
#         from pages.BBS.bbs_assistantpage import AssistantPage
#         return AssistantPage(*self.pages_parameter)

#     def videoPage(self):
#         from pages.BBS.bbs_videopage import VideoPage
#         return VideoPage(*self.pages_parameter)

#     def chartroomPage(self):
#         from pages.BBS.bbs_chatroompage import ChatroomPage
#         return ChatroomPage(*self.pages_parameter)

#     def squarePage(self):
#         from pages.BBS.bbs_squarepage import SquarePage
#         return SquarePage(*self.pages_parameter)

#     def galleryPage(self):
#         from pages.BBS.bbs_gallerypage import GalleryPage
#         return GalleryPage(*self.pages_parameter)

# class BBSAdminPage:
#     def __init__(self, driver, wait_sec, base_url, skip_test_method):
#         self.pages_parameter = driver, wait_sec, base_url, skip_test_method

#     def menuPage(self):
#         from pages.BBS_admin.bbs_admin_menupage import MenuPage
#         return MenuPage(*self.pages_parameter)

#     def lotteryPage(self):
#         from pages.BBS_admin.bbs_admin_lotterypage import LotteryPage
#         return LotteryPage(*self.pages_parameter)

#     def announcementPage(self):
#         from pages.BBS_admin.bbs_admin_announcementpage import AnnouncementPage
#         return AnnouncementPage(*self.pages_parameter)

#     def memberPage(self):
#         from pages.BBS_admin.bbs_admin_memberpage import MemberPage
#         return MemberPage(*self.pages_parameter)

#     def chatPage(self):
#         from pages.BBS_admin.bbs_admin_chatpage import ChatPage
#         return ChatPage(*self.pages_parameter)


class ResellerPage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def loginPage(self):
        from pages.reseller.reseller_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def menuPage(self):
        from pages.reseller.reseller_menupage import MenuPage
        return MenuPage(*self.pages_parameter)

    def oldAgentSettlementPage(self):
        from pages.reseller.reseller_old_agent_settlementpage import OldAgentSettlePage
        return OldAgentSettlePage(*self.pages_parameter)

    def newAgentSettlementPage(self):
        from pages.reseller.reseller_new_agent_settlementpage import NewAgentSettlePage
        return NewAgentSettlePage(*self.pages_parameter)

    def memberListPage(self):
        from pages.reseller.reseller_memberlistpage import MemberListPage
        return MemberListPage(*self.pages_parameter)

    def agentListPage(self):
        from pages.reseller.reseller_agentlistpage import AgentListPage
        return AgentListPage(*self.pages_parameter)

    def genernalPage(self):
        from pages.reseller.reseller_genernalpage import GenernalPage
        return GenernalPage(*self.pages_parameter)

    def dailyPage(self):
        from pages.reseller.reseller_dailypage import DailyPage
        return DailyPage(*self.pages_parameter)

    def validmemberPage(self):
        from pages.reseller.reseller_validmemberpage import ValidMemberPage
        return ValidMemberPage(*self.pages_parameter)

    def notesearchPage(self):
        from pages.reseller.reseller_notesearchpage import NoteSearchPage
        return NoteSearchPage(*self.pages_parameter)

    def profilePage(self):
        from pages.reseller.reseller_profilepage import ProfilePage
        return ProfilePage(*self.pages_parameter)
    
    def basePage(self):
        from pages.reseller.reseller_basepage import BasePage
        return BasePage(*self.pages_parameter)


class CmWebPage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def login_page(self):
        from pages.cmweb.cmweb_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def systemmanagementpage(self):
        from pages.cmweb.systemmanagement.cmweb_systemmanagementpage import SystemManagementPage
        return SystemManagementPage(*self.pages_parameter)
    
    def game_list_page(self):
        from pages.cmweb.systemmanagement.cmweb_gamelistpage import GameListPage
        return GameListPage(*self.pages_parameter)

    def deposit_log_management(self):
        from pages.cmweb.depositlogmanagement.cmweb_depositlogmanagementpage import DepositLogManagementPage
        return DepositLogManagementPage(*self.pages_parameter)

    def recharge_management_page(self):
        from pages.cmweb.depositlogmanagement.cmweb_rechargemanagementpage import RechargeManagementPage
        return RechargeManagementPage(*self.pages_parameter)

    def vendor_wallet_page(self):
        from pages.cmweb.depositlogmanagement.cmweb_vendorwalletpage import VendorWalletPage
        return VendorWalletPage(*self.pages_parameter)    

    def basePage(self):
        from pages.cmweb.cmweb_basepage import BasePage
        return BasePage(*self.pages_parameter)