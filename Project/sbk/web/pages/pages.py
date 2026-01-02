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
        from Project.sbk.web.pages.webs.web_basepage import BasePage
        return BasePage(*self.pages_parameter)
    
    def main_page(self):
        from Project.sbk.web.pages.webs.web_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def login_page(self):
        from Project.sbk.web.pages.webs.web_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)

    def notification_page(self):
        from Project.sbk.web.pages.webs.web_notificationpage import NotificationPage
        return NotificationPage(*self.pages_parameter)

    def security_page(self):
        from Project.sbk.web.pages.webs.web_securitypage import SecurityPage
        return SecurityPage(*self.pages_parameter)

    def black_page(self):
        from Project.sbk.web.pages.webs.web_blackpage import BlackPage
        return BlackPage(*self.pages_parameter)

    def share_page(self):
        from Project.sbk.web.pages.webs.web_sharepage import SharePage
        return SharePage(*self.pages_parameter)

    def about_page(self):
        from Project.sbk.web.pages.webs.web_aboutpage import AboutPage
        return AboutPage(*self.pages_parameter)

    def friend_page(self):
        from Project.sbk.web.pages.webs.web_friendpage import FriendPage
        return FriendPage(*self.pages_parameter)

    # def sbkroomPage(self):
    #     from Project.sbk.web.pages.webs.web_sbkroompage import sbkRoomPage
    #     return sbkRoomPage(*self.pages_parameter)

    # def sbklistPage(self):
    #     from Project.sbk.web.pages.webs.web_sbklistpage import sbkListPage
    #     return sbkListPage(*self.pages_parameter)

class AdminPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method
    
    def common_page(self):
        from common.web.common import Common
        return Common(*self.pages_parameter)
    
    def base_page(self):
        from Project.sbk.web.pages.admin.admin_basepage import BasePage
        return BasePage(*self.pages_parameter)
    
    def login_page(self):
        from Project.sbk.web.pages.admin.admin_loginpage import LoginPage
        return LoginPage(*self.pages_parameter)
    
    def main_page(self):
        from Project.sbk.web.pages.admin.admin_mainpage import MainPage
        return MainPage(*self.pages_parameter)

    def groups_page(self):
        from Project.sbk.web.pages.admin.admin_groupspage import GroupsPage
        return GroupsPage(*self.pages_parameter)

    def logging_page(self):
        from Project.sbk.web.pages.admin.admin_mainpage import LoggingPage
        return LoggingPage(*self.pages_parameter)

    def member_page(self):
        from Project.sbk.web.pages.admin.admin_memberpage import MemberPage
        return MemberPage(*self.pages_parameter)

    def recode_page(self):
        from Project.sbk.web.pages.admin.admin_recodepage import RecodePage
        return RecodePage(*self.pages_parameter)

    def red_envelope_page(self):
        from Project.sbk.web.pages.admin.admin_redenvelopepage import RedEnvelopePage
        return RedEnvelopePage(*self.pages_parameter)

    def setting_page(self):
        from Project.sbk.web.pages.admin.admin_settingpage import SettingPage
        return SettingPage(*self.pages_parameter)

    def system_page(self):
        from Project.sbk.web.pages.admin.admin_systempage import SystemPage
        return SystemPage(*self.pages_parameter)
