import os
import sys

DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class AppPages:
    def __init__(self, parameter):
        self.pages_parameter = parameter

    def common_page(self):
        from common.app.common import Common
        return Common(*self.pages_parameter)

    def base_page(self):
        from Project.chat.app.pages.base_page import Base
        return Base(*self.pages_parameter)

    def main_page(self):
        from Project.chat.app.pages.main_page import MainPage
        return MainPage(*self.pages_parameter)

    def chatroom_page(self):
        from Project.chat.app.pages.chatroom_page import ChatRoomPage
        return ChatRoomPage(*self.pages_parameter)

    def chatlist_page(self):
        from Project.chat.app.pages.chatlist_page import ChatListPage
        return ChatListPage(*self.pages_parameter)

    def member_page(self):
        from Project.chat.app.pages.member_page import MemberPage
        return MemberPage(*self.pages_parameter)

    def friend_page(self):
        from Project.chat.app.pages.friend_page import FriendPage
        return FriendPage(*self.pages_parameter)

    def about_page(self):
        from Project.chat.app.pages.about_page import AboutPage
        return AboutPage(*self.pages_parameter)

    def share_page(self):
        from Project.chat.app.pages.share_page import SharePage
        return SharePage(*self.pages_parameter)

    def blacklist_page(self):
        from Project.chat.app.pages.blacklist_page import BlackListPage
        return BlackListPage(*self.pages_parameter)

    def security_page(self):
        from Project.chat.app.pages.security_page import SecurityPage
        return SecurityPage(*self.pages_parameter)

    def privacy_page(self):
        from Project.chat.app.pages.privacy_page import PrivacyPage
        return PrivacyPage(*self.pages_parameter)

    def chatsetup_page(self):
        from Project.chat.app.pages.chatsetup_page import ChatSetupPage
        return ChatSetupPage(*self.pages_parameter)

    def notification_page(self):
        from Project.chat.app.pages.notification_page import NotificationPage
        return NotificationPage(*self.pages_parameter)

    def point_page(self):
        from Project.chat.app.pages.point_page import PointPage
        return PointPage(*self.pages_parameter)

    def treadandgallery_page(self):
        from Project.chat.app.pages.trend_gallery_page import TreadAndGalleryPage
        return TreadAndGalleryPage(*self.pages_parameter)
    def socialhome_page(self):
        from Project.chat.app.pages.social_homepage import SocialHomePage
        return SocialHomePage(*self.pages_parameter)
    def socialmediapost_page(self):
        from Project.chat.app.pages.social_media_post_page import SocialMediaPostPage
        return SocialMediaPostPage(*self.pages_parameter)
    def socialmedialibrary_page(self):
        from Project.chat.app.pages.social_media_library_page import SocialMediaLibraryPage
        return SocialMediaLibraryPage(*self.pages_parameter)
    def socialshare_page(self):
        from Project.chat.app.pages.social_sharepage import SocialSharePage
        return SocialSharePage(*self.pages_parameter)
    def socialsearch_page(self):
        from Project.chat.app.pages.social_search_page import SocialSearchPage
        return SocialSearchPage(*self.pages_parameter)

    def discover_pages(self):
        from Project.chat.app.pages.discover_page import DiscoverPage
        return DiscoverPage(*self.pages_parameter)

    def freeupspace_page(self):
        from Project.chat.app.pages.free_up_spcae_page import FreeUpSpacePage
        return FreeUpSpacePage(*self.pages_parameter)
