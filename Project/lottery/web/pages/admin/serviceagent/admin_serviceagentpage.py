from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class ServiceAgentPageLocator:
    # ------------客服中心-------------
    menu_service_agent = (By.XPATH, "//span[text()='客服中心']")

    # *站內消息
    station_message = (By.XPATH, "//span[text()='站内消息']")

    # *推播通知
    push_notification = (By.XPATH, "//span[text()='推播通知']")

    # *推播通知
    feedback = (By.XPATH, "//span[text()='意见反馈']")

class ServiceAgentPage(BasePage):
    # 客服中心
    def into_service_agent(self):
        self.wait_loading_finish()
        for _ in range(2):
            if self.is_element_finded(ServiceAgentPageLocator.menu_service_agent):
                break
            self.sleep(5)
        self.sleep(3)
        self.click(ServiceAgentPageLocator.menu_service_agent)

    # 客服中心 -> 站內消息
    def into_station_message(self):
        self.into_service_agent()
        self.click(ServiceAgentPageLocator.station_message)

    # 客服中心 -> 推播通知
    def into_push_notification(self):
        self.into_service_agent()
        self.click(ServiceAgentPageLocator.push_notification)

    # 客服中心 -> 意見反饋
    def into_feedback(self):
        self.into_service_agent()
        self.click(ServiceAgentPageLocator.feedback)