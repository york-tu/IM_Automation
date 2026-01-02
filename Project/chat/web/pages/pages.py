import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class WebPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def common_page(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def base_page(self):
        from Project.chat.web.pages.webs.web_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def main_page(self):
        from Project.chat.web.pages.webs.web_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def login_page(self):
        from Project.chat.web.pages.webs.web_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def integral_page(self):
        from Project.chat.web.pages.webs.web_integralpage import IntegralPage
        return IntegralPage(*self.pages_parameter)

    def notification_page(self):
        from Project.chat.web.pages.webs.web_notificationpage import NotificationPage
        return NotificationPage(*self.pages_parameter)

    def security_page(self):
        from Project.chat.web.pages.webs.web_securitypage import SecurityPage
        return SecurityPage(*self.pages_parameter)

    def black_page(self):
        from Project.chat.web.pages.webs.web_blackpage import BlackPage
        return BlackPage(*self.pages_parameter)

    def share_page(self):
        from Project.chat.web.pages.webs.web_sharepage import SharePage
        return SharePage(*self.pages_parameter)

    def about_page(self):
        from Project.chat.web.pages.webs.web_aboutpage import AboutPage
        return AboutPage(*self.pages_parameter)

    def friend_page(self):
        from Project.chat.web.pages.webs.web_friendpage import FriendPage
        return FriendPage(*self.pages_parameter)

    def chatroom_page(self):
        from Project.chat.web.pages.webs.web_chatroompage import ChatRoomPage
        return ChatRoomPage(*self.pages_parameter)

    def chatlist_page(self):
        from Project.chat.web.pages.webs.web_chatlistpage import ChatListPage
        return ChatListPage(*self.pages_parameter)

    def brand_page(self):
        from Project.chat.web.pages.webs.web_brandpage import BrandPage
        return BrandPage(*self.pages_parameter)

class AdminPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def common_page(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def base_page(self):
        from Project.chat.web.pages.admin.admin_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def login_page(self):
        from Project.chat.web.pages.admin.admin_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def main_page(self):
        from Project.chat.web.pages.admin.admin_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def groups_page(self):
        from Project.chat.web.pages.admin.admin_groupspage import GroupsPage
        return GroupsPage(*self.pages_parameter)

    def logging_page(self):
        from Project.chat.web.pages.admin.admin_loggingpage import LoggingPage
        return LoggingPage(*self.pages_parameter)

    def member_page(self):
        from Project.chat.web.pages.admin.admin_memberpage import MemberPage
        return MemberPage(*self.pages_parameter)

    def recode_page(self):
        from Project.chat.web.pages.admin.admin_recodepage import RecordPage
        return RecordPage(*self.pages_parameter)

    def red_envelope_page(self):
        from Project.chat.web.pages.admin.admin_redenvelopepage import RedEnvelopePage
        return RedEnvelopePage(*self.pages_parameter)

    def water_recode_page(self):
        from Project.chat.web.pages.admin.admin_water_recode_page import WaterRecodePage
        return WaterRecodePage(*self.pages_parameter)

    def water_control_page(self):
        from Project.chat.web.pages.admin.admin_water_control_page import WaterControlPage
        return WaterControlPage(*self.pages_parameter)

    def setting_page(self):
        from Project.chat.web.pages.admin.admin_settingpage import SettingPage
        return SettingPage(*self.pages_parameter)

    def system_page(self):
        from Project.chat.web.pages.admin.admin_systempage import SystemPage
        return SystemPage(*self.pages_parameter)

    def social_management_page(self):
        from Project.chat.web.pages.admin.admin_social_management_page import SocialManagementPage
        return SocialManagementPage(*self.pages_parameter)

    def record_page(self):
        from Project.chat.web.pages.admin.admin_recodepage import RecordPage
        return RecordPage(*self.pages_parameter)

class WapPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def common_page(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)

    def base_page(self):
        from Project.chat.web.pages.wap.wap_basepage import BasePage
        return BasePage(*self.pages_parameter)

    def wap_first_page(self):
        from Project.chat.web.pages.wap.wap_firstpage import FirstPage
        return FirstPage(*self.pages_parameter)

    def wap_friends_page(self):
        from Project.chat.web.pages.wap.wap_friendspage import FriendsPage
        return FriendsPage(*self.pages_parameter)

    def wap_message_page(self):
        from Project.chat.web.pages.wap.wap_messagepage import MessagePage
        return MessagePage(*self.pages_parameter)

    def wap_main_page(self):
        from Project.chat.web.pages.wap.wap_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def wap_main_personal_page(self):
        from Project.chat.web.pages.wap.wap_main_personal_settings import PersonalSettingPage
        return PersonalSettingPage(*self.pages_parameter)

    def wap_login_page(self):
        from Project.chat.web.pages.wap.wap_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def search_page(self):
        from Project.chat.web.pages.wap.wap_searchpage import SearchPage
        return SearchPage(*self.pages_parameter)





