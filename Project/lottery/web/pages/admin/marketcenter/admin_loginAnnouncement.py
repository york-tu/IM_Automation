from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random, string

class LoginAnnouncementPageLocator:
    add = (By.XPATH, "//a[contains(@href,'loginBillboard/add')]")

    # 新增頁面
    agent_system = (By.XPATH, "//label[@class='radio-inline' and contains(., '指定级别')]")
    start_time = (By.XPATH, "//input[contains(@data-bind, 'publishedtime')]")
    end_time = (By.XPATH, "//input[contains(@data-bind, 'endtime')]")
    detail = (By.XPATH, "//html[@dir='ltr']//p")
    save = (By.XPATH, "//button[text()= '保存']")

class LoginAnnouncementPage(BasePage):

    def get_message_data(self):
        data = {
            'start_time': self.get_us_time(),
            'end_time': (self.get_us_time() + datetime.timedelta(minutes=3)).strftime('%Y-%m-%d %H:%M:%S'),
        }

        return data

    def add_message(self, data):
        self.wait_loading_finish()
        self.click(LoginAnnouncementPageLocator.add)
        self.wait_loading_finish()

        self.click(LoginAnnouncementPageLocator.agent_system)
        self.type(LoginAnnouncementPageLocator.start_time, data['start_time'])
        self.type(LoginAnnouncementPageLocator.end_time, data['end_time'])
        
        self.switch_frame(0)
        self.type(LoginAnnouncementPageLocator.detail, data['content'])
        self.switch_default_frame()

        self.click(LoginAnnouncementPageLocator.save)
        self.wait_loading_finish()