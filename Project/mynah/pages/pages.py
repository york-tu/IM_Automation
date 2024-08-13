import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)

class WebPages:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def webBasePage(self):
        from Project.mynah.pages.web.webs_basepage import WebBasePage
        return WebBasePage(*self.pages_parameter)

    def channelPage(self):
        from Project.mynah.pages.web.web_channelpage import WebChannelPage
        return WebChannelPage(*self.pages_parameter)

    def chatPage(self):
        from Project.mynah.pages.web.web_chatpage import WebChatPage
        return WebChatPage(*self.pages_parameter)

    def formPage(self):
        from Project.mynah.pages.web.web_formpage import WebFormPage
        return WebFormPage(*self.pages_parameter)

    def scorePage(self):
        from Project.mynah.pages.web.web_scorepage import WebScorePage
        return WebScorePage(*self.pages_parameter)


class AdminPage:
    def __init__(self, driver, wait_sec, base_url, skip_test_method):
        self.pages_parameter = driver, wait_sec, base_url, skip_test_method

    def adminBasePage(self):
        from Project.mynah.pages.admin.admin_basepage import AdminBasePage
        return AdminBasePage(*self.pages_parameter)

    def adminChatPage(self):
        from Project.mynah.pages.admin.admin_chatpage import AdminChatPage
        return AdminChatPage(*self.pages_parameter)

    # def adminDashboardPage(self):
    #     from mynah.pages.admin.admin_dashboardpage import AdminDashboardPage
    #     return AdminDashboardPage(*self.pages_parameter)

    def adminFormPage(self):
        from Project.mynah.pages.admin.admin_formpage import AdminFormPage
        return AdminFormPage(*self.pages_parameter)

    def adminAIResponsePage(self):
        from Project.mynah.pages.admin.admin_airesponsepage import AdminAIResponsePage
        return AdminAIResponsePage(*self.pages_parameter)

    def adminMenuPage(self):
        from Project.mynah.pages.admin.admin_menupage import AdminMenuPage
        return AdminMenuPage(*self.pages_parameter)

    def adminRulesPage(self):
        from Project.mynah.pages.admin.admin_rulespage import AdminRulesPage
        return AdminRulesPage(*self.pages_parameter)

    def adminHistoryPage(self):
        from Project.mynah.pages.admin.admin_historypage import AdminHistoryPage
        return AdminHistoryPage(*self.pages_parameter)

    def adminPromotionAdPage(self):
        from Project.mynah.pages.admin.admin_promotionadpage import AdminPromotionAdPage
        return AdminPromotionAdPage(*self.pages_parameter)
        
    def adminScorePage(self):
        from Project.mynah.pages.admin.admin_scorepage import AdminScorePage
        return AdminScorePage(*self.pages_parameter)

    def adminStatisticsPage(self):
        from Project.mynah.pages.admin.admin_statistics import AdminStatisticsPage
        return AdminStatisticsPage(*self.pages_parameter)