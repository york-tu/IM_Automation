from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import datetime

class MessagePageLocator:
    status = (By.XPATH, '//div[@class="icon_read"]') # 已讀 未讀 狀態
    time = (By.XPATH, '//td[contains(@data-bind, "starttime")]') # 時間
    title = (By.XPATH, '//td[contains(@data-bind, "title")]') # 標題
    button_show_message = (By.XPATH, '//div[contains(@data-bind, "parent.show")]') # 查看內容
    button_delete_message = (By.XPATH, '//div[contains(@data-bind, "parent.remove")]') # 刪除訊息
    # ---------------------------------- 訊息 dialog ----------------------------------
    title_dialog = (By.XPATH, '//h6[contains(@data-bind, "title")]')
    content = (By.XPATH, '//div[contains(@data-bind, "html: content")]/p') # 訊息內容
    button_close = (By.XPATH, '//div[contains(@class, "hide-inbox-message btn")]') # 確認關閉

class MessagePage(BasePage):
    def check_message(self, data):
        self.wait_loading_finish()
        status = ['未读', '已读']

        for _ in range(0, 10):
            if self.is_element_finded(MessagePageLocator.status) is False:
                self.refresh_browser()
                self.sleep(1)
            else:
                break
        
        # 全層級發信有機會導致會員延遲多秒才收到信, 因此先行暫停90秒
        self.sleep(30)
        self.refresh_browser()

        for _ in range(0, 10):
            if self.is_element_finded(MessagePageLocator.time) == False:
                self.refresh_browser()
                self.sleep(5)
            else:
                break

        assert self.is_element_finded(MessagePageLocator.time) == True, "定位錯誤，無法查找到站內信的時間位置"
        time = (datetime.datetime.strptime(self.get_text(MessagePageLocator.time), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:00')

        assert self.get_text(MessagePageLocator.status) == status[0], \
            f'前台 訊息狀態錯誤 ... {self.get_text(MessagePageLocator.status)} 應為-> {status[0]}'
        assert time == data['start_time'], \
            f'前台 訊息時間錯誤 ... {time} 應為-> {data["start_time"]}'
        assert self.get_text(MessagePageLocator.title) == data['title'], \
            f'前台 訊息標題錯誤 ... {self.get_text(MessagePageLocator.title)} 應為-> {data["title"]}'

        self.click(MessagePageLocator.button_show_message)
        self.sleep(0.25)
        assert self.get_text(MessagePageLocator.title_dialog) == data['title'], \
            f'前台 訊息內容標題錯誤 ... {self.get_text(MessagePageLocator.title_dialog)} 應為-> {data["title"]}'
        assert self.get_text(MessagePageLocator.content) == data['content'], \
            f'前台 訊息內容錯誤 ... {self.get_text(MessagePageLocator.content)} 應為-> {data["content"]}'

        self.click(MessagePageLocator.button_close)
        self.sleep(0.25)
        assert self.get_text(MessagePageLocator.status) == status[1], \
            f'前台 訊息狀態錯誤 ... {self.get_text(MessagePageLocator.status)} 應為-> {status[1]}'
        self.click(MessagePageLocator.button_delete_message)
