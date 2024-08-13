import os
import sys

DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class AppPages:
    def __init__(self, parameter):
        self.pages_parameter = parameter

    def commomPage(self):
        from common.app.common import Common
        return Common(*self.pages_parameter)

    def basePage(self):
        from Project.chat.app.pages.base_page import Base
        return Base(*self.pages_parameter)

    def mainPage(self):
        from Project.chat.app.pages.main_page import MainPage
        return MainPage(*self.pages_parameter)

    def chatroomPage(self):
        from Project.chat.app.pages.chatroom_page import ChatRoomPage
        return ChatRoomPage(*self.pages_parameter)

    def chatlistPage(self):
        from Project.chat.app.pages.chatlist_page import ChatListPage
        return ChatListPage(*self.pages_parameter)

    def memberPage(self):
        from Project.chat.app.pages.member_page import MemberPage
        return MemberPage(*self.pages_parameter)

    def friendPage(self):
        from Project.chat.app.pages.friend_page import FriendPage
        return FriendPage(*self.pages_parameter)

    def aboutPage(self):
        from Project.chat.app.pages.about_page import AboutPage
        return AboutPage(*self.pages_parameter)

    def sharePage(self):
        from Project.chat.app.pages.share_page import SharePage
        return SharePage(*self.pages_parameter)

    def blacklistPage(self):
        from Project.chat.app.pages.blacklist_page import BlackListPage
        return BlackListPage(*self.pages_parameter)

    def securityPage(self):
        from Project.chat.app.pages.security_page import SecurityPage
        return SecurityPage(*self.pages_parameter)

    def chatsetupPage(self):
        from Project.chat.app.pages.chatsetup_page import ChatSetupPage
        return ChatSetupPage(*self.pages_parameter)

    def notificationPage(self):
        from Project.chat.app.pages.notification_page import NotificationPage
        return NotificationPage(*self.pages_parameter)

    def pointPage(self):
        from Project.chat.app.pages.point_page import PointPage
        return PointPage(*self.pages_parameter)

    def treadandgalleryPage(self):
        from Project.chat.app.pages.trend_gallery_page import TreadAndGalleryPage
        return TreadAndGalleryPage(*self.pages_parameter)

    def mediareleasePage(self):
        from Project.chat.app.pages.media_release_page import MediaReleasePage
        return MediaReleasePage(*self.pages_parameter)