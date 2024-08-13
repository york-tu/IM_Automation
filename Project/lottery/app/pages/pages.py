import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)

class AppPages:
    def __init__(self, parameter):
        self.pages_parameter = parameter

    def commonPage(self):
        from common.app.common import Common
        return Common(*self.pages_parameter)
    
    def basePage(self):
        from Project.lottery.app.pages.base import Base
        return Base(*self.pages_parameter)

    def memberPage(self):
        from Project.lottery.app.pages.member_page import MemberPage
        return MemberPage(*self.pages_parameter)

    def mainPage(self):
        from Project.lottery.app.pages.main_page import MainPage
        return MainPage(*self.pages_parameter)

    def systeminfoPage(self):
        from Project.lottery.app.pages.system_info_page import SystemInfoPage
        return SystemInfoPage(*self.pages_parameter)
    
    def fgcardPage(self):
        from Project.lottery.app.pages.CM.fg_card_page import FgCardPage
        return FgCardPage(*self.pages_parameter)
    
    def vgcardPage(self):
        from Project.lottery.app.pages.CM.vg_card_page import VgCardPage
        return VgCardPage(*self.pages_parameter)

    def kycardPage(self):
        from Project.lottery.app.pages.CM.ky_card_page import KyCardPage
        return KyCardPage(*self.pages_parameter)

    def bscardPage(self):
        from Project.lottery.app.pages.CM.bs_card_page import BsCardPage
        return BsCardPage(*self.pages_parameter)

    def gmcardPage(self):
        from Project.lottery.app.pages.CM.gm_card_page import GmCardPage
        return GmCardPage(*self.pages_parameter)

    def lscardPage(self):
        from Project.lottery.app.pages.CM.lc_card_page import LcCardPage
        return LcCardPage(*self.pages_parameter)

    def kkcardPage(self):
        from Project.lottery.app.pages.CM.kk_card_page import KkCardPage
        return KkCardPage(*self.pages_parameter)

    def cq9electronicPage(self):
        from Project.lottery.app.pages.CM.cq9_electronic_page import Cq9ElectronicPage
        return Cq9ElectronicPage(*self.pages_parameter)

    def swelectronicPage(self):
        from Project.lottery.app.pages.CM.sw_electronic_page import SwElectronicPage
        return SwElectronicPage(*self.pages_parameter)

    def dtelectronicPage(self):
        from Project.lottery.app.pages.CM.dt_electronic_page import DtElectronicPage
        return DtElectronicPage(*self.pages_parameter)

    def ptelectronicPage(self):
        from Project.lottery.app.pages.CM.pt_electronic_page import PtElectronicPage
        return PtElectronicPage(*self.pages_parameter)

    def fgelectronicPage(self):
        from Project.lottery.app.pages.CM.fg_electronic_page import FgElectronicPage
        return FgElectronicPage(*self.pages_parameter)

    def bbinelectronicPage(self):
        from Project.lottery.app.pages.CM.bbin_electronic_page import BbinElectronicPage
        return BbinElectronicPage(*self.pages_parameter)

    def kkelectronicPage(self):
        from Project.lottery.app.pages.CM.kk_electronic_page import KkElectronicPage
        return KkElectronicPage(*self.pages_parameter)

    def sbsportPage(self):
        from Project.lottery.app.pages.CM.sb_sport_page import SbSportPage
        return SbSportPage(*self.pages_parameter)

    def bbinsportPage(self):
        from Project.lottery.app.pages.CM.bbin_sport_page import BbinSportPage
        return BbinSportPage(*self.pages_parameter)
    
    def sssportPage(self):
        from Project.lottery.app.pages.CM.ss_sport_page import SsSportPage
        return SsSportPage(*self.pages_parameter)

    def hgsportPage(self):
        from Project.lottery.app.pages.CM.hg_sport_page import HgSportPage
        return HgSportPage(*self.pages_parameter)

    def transformPage(self):
        from Project.lottery.app.pages.transform_amount_page import TransformPage
        return TransformPage(*self.pages_parameter)

    def depositcompanyPage(self):
        from Project.lottery.app.pages.deposit_company_page import DepositCompanyPage
        return DepositCompanyPage(*self.pages_parameter)

    def depositailpayf2Page(self):
        from Project.lottery.app.pages.deposit_alipay_f2f_page import DepositAilpayF2FPage
        return DepositAilpayF2FPage(*self.pages_parameter)

    def depositailplaytransferPage(self):
        from Project.lottery.app.pages.deposit_alipay_transfer_page import DepositAilpayTransferPage
        return DepositAilpayTransferPage(*self.pages_parameter)

    def withdrawPage(self):
        from Project.lottery.app.pages.withdraw_page import WithdrawPage
        return WithdrawPage(*self.pages_parameter)

    def promoPageA(self):
        from Project.lottery.app.pages.promo_page import PromoPageA
        return PromoPageA(*self.pages_parameter)
    
    def promoPageB(self):
        from Project.lottery.app.pages.promo_page import PromoPageB
        return PromoPageB(*self.pages_parameter)
    
    def promoPage(self):
        from Project.lottery.app.pages.promo_page import PromoPage
        return PromoPage(*self.pages_parameter)

    def registerPage(self):
        from Project.lottery.app.pages.register_page import RegisterPage
        return RegisterPage(*self.pages_parameter)

    def lotteryPageA(self):
        from Project.lottery.app.pages.lottery_page import LotteryPageA
        return LotteryPageA(*self.pages_parameter)

    def lotteryPageB(self):
        from Project.lottery.app.pages.lottery_page import LotteryPageB
        return LotteryPageB(*self.pages_parameter)

    def lotteryPage(self):
        from Project.lottery.app.pages.lottery_page import LotteryPage
        return LotteryPage(*self.pages_parameter)

    def k3Page(self):
        from Project.lottery.app.pages.lottery.bet_lottery_k3_page import K3
        return K3(*self.pages_parameter)

    def hkPage(self):
        from Project.lottery.app.pages.lottery.bet_lottery_hk_page import Hk
        return Hk(*self.pages_parameter)

    def x5Page(self):
        from Project.lottery.app.pages.lottery.bet_lottery_11x5_page import X5
        return X5(*self.pages_parameter)

    def fc3dPage(self):
        from Project.lottery.app.pages.lottery.bet_lottery_fc3d_page import Fc3D
        return Fc3D(*self.pages_parameter)

    def pk10Page(self):
        from Project.lottery.app.pages.lottery.bet_lottery_pk10_page import Pk10
        return Pk10(*self.pages_parameter)

    def sscPage(self):
        from Project.lottery.app.pages.lottery.bet_lottery_ssc_page import Ssc
        return Ssc(*self.pages_parameter)

    def xy28Page(self):
        from Project.lottery.app.pages.lottery.bet_lottery_xy28_page import Xy28
        return Xy28(*self.pages_parameter)

    def faqPage(self):
        from Project.lottery.app.pages.faq_page import FaqPage
        return FaqPage(*self.pages_parameter)
    
    def mailcenterPage(self):
        from Project.lottery.app.pages.mail_center_page import MailCenterPage
        return MailCenterPage(*self.pages_parameter)

    def ledgerPage(self):
        from Project.lottery.app.pages.ledger_page import LedgerPage
        return LedgerPage(*self.pages_parameter)

    def myinfoPage(self):
        from Project.lottery.app.pages.myinfo_page import MyInfoPage
        return MyInfoPage(*self.pages_parameter)

    def depositrecordPage(self):
        from Project.lottery.app.pages.deposit_record_page import DeopsitRecordPage
        return DeopsitRecordPage(*self.pages_parameter)

    def withfrawrecordPage(self):
        from Project.lottery.app.pages.withdraw_record_page import ＷithdrawRecordPage
        return ＷithdrawRecordPage(*self.pages_parameter)
    
    def betrecordPage(self):
        from Project.lottery.app.pages.bet_record_page import BetRecordPage
        return BetRecordPage(*self.pages_parameter)

    def feedbackPage(self):
        from Project.lottery.app.pages.feedback_page import FeedbackPage
        return FeedbackPage(*self.pages_parameter)

    def agentPage(self):
        from Project.lottery.app.pages.agent_page import AgentPage
        return AgentPage(*self.pages_parameter)

    def aboutPage(self):
        from Project.lottery.app.pages.about_page import AboutPage
        return AboutPage(*self.pages_parameter)

    def redenvelopePage(self):
        from Project.lottery.app.pages.red_envelope_page import Red_EnvelopePage
        return Red_EnvelopePage(*self.pages_parameter)

    def trendPage(self):
        from Project.lottery.app.pages.trend_page import TrendPage
        return TrendPage(*self.pages_parameter)