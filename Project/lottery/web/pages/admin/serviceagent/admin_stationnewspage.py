from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime, random, string

class StationNewsPageLocator:
    add = (By.XPATH, "//a[contains(@href,'message/add')]")

    # 新增頁面
    title = (By.XPATH, "//input[contains(@data-bind, 'title')]")
    agent_system = (By.XPATH, '//label[@class="radio-inline" and contains(., "指定级别")]/input')
    start_time = (By.XPATH, "//input[contains(@data-bind, 'starttime')]")
    end_time = (By.XPATH, "//input[contains(@data-bind, 'endtime')]")
    detial = (By.XPATH, "//html[@dir='ltr']//p")
    save = (By.XPATH, "//button[text()= '保存']")

class StationNewsPage(BasePage):

    def get_message_data(self):
        data = {
            'title': ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)),
            'start_time': self.get_us_time(),
            'end_time': (self.get_us_time() + datetime.timedelta(minutes=7)).strftime('%Y-%m-%d %H:%M:%S'),
        }

        return data

    # 客服中心
    def add_message(self, data):
        self.wait_loading_finish()
        self.click(StationNewsPageLocator.add)
        self.wait_loading_finish()
        
        self.type(StationNewsPageLocator.title, data['title'])
        self.click(StationNewsPageLocator.agent_system)
        self.type(StationNewsPageLocator.start_time, data['start_time'])
        self.type(StationNewsPageLocator.end_time, data['end_time'])

        self.switch_frame(0)
        self.type(StationNewsPageLocator.detial, data['content'])
        self.switch_default_frame()

        self.click(StationNewsPageLocator.save)
