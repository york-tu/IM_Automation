import os, random, base64
from io import BytesIO
from PIL import Image
from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

class FeedBackPageLocator:
    # WITHDRAW PAGE (線上取款)
    types = (By.XPATH, "//select[@class= 'input-select__select']")
    title = (By.XPATH, "//input[@class= 'input-title__input']")
    message = (By.XPATH, "//textarea[contains(@placeholder, '请输入内容')]")
    upload = (By.XPATH, "//img[@class= 'upload-img__addicon']")
    sumit = (By.XPATH, "//button[contains(text(), '提交反馈')]")

    types_nwap = (By.XPATH, "//div[@class= 'form-select']")
    types_nwap_js = "input[placeholder='请选择']"
    scroll_nwap_js = "com-inner"

    def type_list_nwap(num):
        type_list_nwap = (By.XPATH, f"(//div[text()= '出入款项问题']/../..//div)[{num}]/..")
        return type_list_nwap

    current = (By.XPATH, "//*[text()= '确定']")
    title_nwap = (By.XPATH, "//input[@placeholder= '请简述问题']")
    message_nwap = (By.XPATH, "//textarea[contains(@placeholder, '请详细描述您遇到的问题，内容不得少于20字')]")
    upload_nwap = (By.XPATH, "//input[@class= 'form-uploader__input']")
    message_win = (By.XPATH, "//div[contains(text(), '提交成功')]")
    sumit_nwap = (By.XPATH, "//a[contains(text(), '提交反馈')]")
    
    
class FeedBackPage(BasePage):
    def feedback_message(self, title, text):
        self.wait_loading_finish()
        self.select_by_index(FeedBackPageLocator.types, random.randint(1, 6))
        self.type(FeedBackPageLocator.title, title)
        self.type(FeedBackPageLocator.message, text)
        self.click(FeedBackPageLocator.sumit)

        # check success alert
        self.wait_alert_present()
        message = self.get_alert_message()

        if message == '谢谢您的反馈':
            self.accept_alert()
        else:
            raise EOFError('沒出現彈窗訊息')


        # base64
        # data_path = f"{dir_name}/image/wap/data/{data}"
        # img = Image.open(data_path)
        # output_buffer = BytesIO()
        # img.save(output_buffer, format='JPEG')
        # byte_data = output_buffer.getvalue()
        # base64_str = str(base64.b64encode(byte_data))[2:]

    def feedback_message＿nwap(self, title, text):
        self.wait_loading_finish()
        self.click_js(FeedBackPageLocator.types_nwap_js)
        self.click(FeedBackPageLocator.type_list_nwap(random.randint(1, 6)))
        self.sleep(1)
        self.click(FeedBackPageLocator.current)
        self.type(FeedBackPageLocator.title_nwap, title)
        self.type(FeedBackPageLocator.message_nwap, text)
        self.scroll_bottom_java(FeedBackPageLocator.scroll_nwap_js)
        self.click(FeedBackPageLocator.sumit_nwap)
        self.sleep(1)

        # check success alert
        assert self.is_element_finded(FeedBackPageLocator.message_win), '提交失敗'
