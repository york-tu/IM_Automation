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

    def privacyPage(self):
        from Project.chat.app.pages.privacy_page import PrivacyPage
        return PrivacyPage(*self.pages_parameter)

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
    def socialhomePage(self):
        from Project.chat.app.pages.social_homepage import SocialHomePage
        return SocialHomePage(*self.pages_parameter)
    def socialmediapostPage(self):
        from Project.chat.app.pages.social_media_post_page import SocialMediaPostPage
        return SocialMediaPostPage(*self.pages_parameter)
    def socialmedialibraryPage(self):
        from Project.chat.app.pages.social_media_library_page import SocialMediaLibraryPage
        return SocialMediaLibraryPage(*self.pages_parameter)
    def socialsharePage(self):
        from Project.chat.app.pages.social_sharepage import SocialSharePage
        return SocialSharePage(*self.pages_parameter)
    def socialsearchPage(self):
        from Project.chat.app.pages.social_search_page import SocialSearchPage
        return SocialSearchPage(*self.pages_parameter)

    def discoverPages(self):
        from Project.chat.app.pages.discover_page import DiscoverPage
        return DiscoverPage(*self.pages_parameter)

    def freeupspacePage(self):
        from Project.chat.app.pages.free_up_spcae_page import FreeUpSpacePage
        return FreeUpSpacePage(*self.pages_parameter)
