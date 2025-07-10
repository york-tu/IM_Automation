import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class WebPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def commomPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def basePage(self):
        from Project.chat.web.pages.webs.web_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def mainPage(self):
        from Project.chat.web.pages.webs.web_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def loginPage(self):
        from Project.chat.web.pages.webs.web_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def integralPage(self):
        from Project.chat.web.pages.webs.web_integralpage import IntegralPage
        return IntegralPage(*self.pages_parameter)

    def notificationPage(self):
        from Project.chat.web.pages.webs.web_notificationpage import NotificationPage
        return NotificationPage(*self.pages_parameter)

    def securityPage(self):
        from Project.chat.web.pages.webs.web_securitypage import SecurityPage
        return SecurityPage(*self.pages_parameter)

    def blackPage(self):
        from Project.chat.web.pages.webs.web_blackpage import BlackPage
        return BlackPage(*self.pages_parameter)

    def sharePage(self):
        from Project.chat.web.pages.webs.web_sharepage import SharePage
        return SharePage(*self.pages_parameter)

    def aboutPage(self):
        from Project.chat.web.pages.webs.web_aboutpage import AboutPage
        return AboutPage(*self.pages_parameter)

    def friendPage(self):
        from Project.chat.web.pages.webs.web_friendpage import FriendPage
        return FriendPage(*self.pages_parameter)

    def chatroomPage(self):
        from Project.chat.web.pages.webs.web_chatroompage import ChatRoomPage
        return ChatRoomPage(*self.pages_parameter)

    def chatlistPage(self):
        from Project.chat.web.pages.webs.web_chatlistpage import ChatListPage
        return ChatListPage(*self.pages_parameter)

    def brandPage(self):
        from Project.chat.web.pages.webs.web_brandpage import BrandPage
        return BrandPage(*self.pages_parameter)

class AdminPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def commomPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def basePage(self):
        from Project.chat.web.pages.admin.admin_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def loginPage(self):
        from Project.chat.web.pages.admin.admin_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def mainPage(self):
        from Project.chat.web.pages.admin.admin_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def groupsPage(self):
        from Project.chat.web.pages.admin.admin_groupspage import GroupsPage
        return GroupsPage(*self.pages_parameter)

    def loggingPage(self):
        from Project.chat.web.pages.admin.admin_loggingpage import LoggingPage
        return LoggingPage(*self.pages_parameter)

    def memberPage(self):
        from Project.chat.web.pages.admin.admin_memberpage import MemberPage
        return MemberPage(*self.pages_parameter)

    def recodePage(self):
        from Project.chat.web.pages.admin.admin_recodepage import RecordPage
        return RecordPage(*self.pages_parameter)

    def redenvelopePage(self):
        from Project.chat.web.pages.admin.admin_redenvelopepage import RedEnvelopePage
        return RedEnvelopePage(*self.pages_parameter)

    def waterRecodePage(self):
        from Project.chat.web.pages.admin.admin_waterRecodepage import WaterRecodePage
        return WaterRecodePage(*self.pages_parameter)

    def waterControlPage(self):
        from Project.chat.web.pages.admin.admin_waterControlpage import WaterControlPage
        return WaterControlPage(*self.pages_parameter)

    def settingPage(self):
        from Project.chat.web.pages.admin.admin_settingpage import SettingPage
        return SettingPage(*self.pages_parameter)

    def systemPage(self):
        from Project.chat.web.pages.admin.admin_systempage import SystemPage
        return SystemPage(*self.pages_parameter)

    def socialManagementPage(self):
        from Project.chat.web.pages.admin.admin_socialManagementpage import SocialManagementPage
        return SocialManagementPage(*self.pages_parameter)

    def recordPage(self):
        from Project.chat.web.pages.admin.admin_recodepage import RecordPage
        return RecordPage(*self.pages_parameter)

class WapPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def commomPage(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def basePage(self):
        from Project.chat.web.pages.wap.wap_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def wapFirstPage(self):
        from Project.chat.web.pages.wap.wap_firstpage import FirstPage
        return FirstPage(*self.pages_parameter)

    def wapFriendsPage(self):
        from Project.chat.web.pages.wap.wap_friendspage import FriendsPage
        return FriendsPage(*self.pages_parameter)

    def wapMessagePage(self):
        from Project.chat.web.pages.wap.wap_messagepage import MessagePage
        return MessagePage(*self.pages_parameter)

    def wapMainPage(self):
        from Project.chat.web.pages.wap.wap_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def wapMainPersonalPage(self):
        from Project.chat.web.pages.wap.wap_main_personal_settings import PersonalSettingPage
        return PersonalSettingPage(*self.pages_parameter)

    def wapLoginPage(self):
        from Project.chat.web.pages.wap.wap_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def searchPage(self):
        from Project.chat.web.pages.wap.wap_searchpage import SearchPage
        return SearchPage(*self.pages_parameter)





