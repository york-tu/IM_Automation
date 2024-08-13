from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
from datetime import datetime, timezone, timedelta

class FeedbackPageLocator:
    search = (By.XPATH, "//button[@id= 'btnSearch']")
    first_time = (By.XPATH, "(//div[@class= 'table-responsive']//tbody//tr//td[contains(@data-bind, 'createdtime')])[1]")
    first_account = (By.XPATH, "(//div[@class= 'table-responsive']//tbody//tr//td[contains(@data-bind, 'memberlogin')])[1]")
    first_title = (By.XPATH, "(//div[@class= 'table-responsive']//tbody//tr//td[contains(@data-bind, 'title')])[1]")
    first_content = (By.XPATH, "(//div[@class= 'table-responsive']//tbody//tr//td[contains(@data-bind, 'content')])[1]")
    

class FeedbackPage(BasePage):
    def check_feedback(self, account, title, content):
        tz = timezone(timedelta(hours=-4))
        today = str(datetime.now(tz).strftime("%Y-%m-%d"))

        self.click(FeedbackPageLocator.search)
        admin_time = self.get_text(FeedbackPageLocator.first_time)
        admin_account = self.get_text(FeedbackPageLocator.first_account)
        admin_title = self.get_text(FeedbackPageLocator.first_title)
        admin_content = self.get_text(FeedbackPageLocator.first_content)
        self.sleep(1)

        assert admin_time.__contains__(today), '意見反饋列表顯示時間錯誤'
        assert admin_account.__contains__(account), '意見反饋列表顯示帳號錯誤'
        assert admin_title.__contains__(title), '意見反饋列表顯示標題錯誤'
        assert admin_content.__contains__(content), '意見反饋列表顯示內容錯誤'