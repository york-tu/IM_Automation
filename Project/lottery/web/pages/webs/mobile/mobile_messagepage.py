from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime

class MessagePageLocator:
    status = (By.XPATH, '//div[contains(@class, "m-inboxheader")]/span') # 已讀 未讀 狀態
    time = (By.XPATH, '//span[contains(@data-bind, "starttime")]') # 時間
    title = (By.XPATH, '//span[contains(@data-bind, "title")]') # 標題
    button_show_message = (By.XPATH, '//a[contains(@data-bind, "parent.show")]') # 查看內容
    button_delete_message = (By.XPATH, '//a[contains(@data-bind, "parent.delete")]') # 刪除訊息
    # ---------------------------------- 訊息 dialog ----------------------------------
    title_dialog = (By.XPATH, '//h6[contains(@data-bind, "title")]')
    content = (By.XPATH, '//div[contains(@data-bind, "html: content")]/p') # 訊息內容
    button_close = (By.XPATH, '//a[contains(@class, "hide-inbox-message btn")]') # 確認關閉

    mail = (By.XPATH, "//div[@class='message-cell__content']")
    mail_delete_first = (By.XPATH, "(//div[@class='message-delete'])[1]")
    mail_delete_submit = (By.XPATH, "//span[text()='确认']/../..")
    mail_delete_cancel = (By.XPATH, "//span[text()='取消']/../..")
    
    mail_empty = (By.XPATH, "//h3[@class='empty-title']")
    mail_title = (By.XPATH, "(//h3[@class='message-title'])[1]")
    mail_readed = (By.XPATH, "//div[contains(@class,'message-cell__item--open')]")
    mail_time = (By.XPATH, "(//h4[@class='message-date'])[1]")
    mail_text = (By.XPATH, "(//div[@class='message-description']/p)[1]")
    mail_arrow = (By.XPATH, "(//div[@class='message-arrow'])[1]")
    mail_back = (By.XPATH, "//a[@class='btn-return']")

class MessagePage(BasePage):
    def check_message(self, data):
        status = ['未读', '已读']
        self.wait_loading_finish()
        self.sleep(30)
        self.refresh_browser()
        self.wait_loading_finish()
    
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

    def delete_messages(self):
        self.wait_loading_finish()

        num = len(self.find_elements(MessagePageLocator.mail))

        if num > 0:
            for _ in range(0,num):
                self.click(MessagePageLocator.mail_delete_first)

                if self.is_element_finded(MessagePageLocator.mail_delete_submit) == True:
                    self.sleep(1)
                    self.click(MessagePageLocator.mail_delete_submit)

                self.sleep(1)

            assert self.is_element_finded(MessagePageLocator.mail_empty) == True, f'訊息 未刪除完畢'
        else:
            pass
        
    def messages_check_nwap(self, data):
        
        self.wait_loading_finish()
        self.sleep(30)
        self.refresh_browser()
        self.wait_loading_finish()

        for _ in range(0, 10):
            if self.is_element_finded(MessagePageLocator.mail_time) == False:
                self.refresh_browser()
                self.sleep(1)
            else:
                break
        
        # 全層級發信有機會導致會員延遲多秒才收到信, 因此先行暫停90秒
        self.sleep(30)
        self.refresh_browser()
        for _ in range(0, 10):
            if self.is_element_finded(MessagePageLocator.mail_title) == False:
                self.refresh_browser()
                self.sleep(10)
            else:
                break
        
        assert self.is_element_finded(MessagePageLocator.mail_time) == True, "定位錯誤，無法查找到站內信的時間位置"
        
        mail_time = self.get_text(MessagePageLocator.mail_time).replace(' 年 ','-').replace('月','-').replace('日','')
        
        time = (datetime.datetime.strptime(mail_time, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:00')
       
        assert self.is_element_finded(MessagePageLocator.mail_readed) == False, \
            f'前台 訊息狀態錯誤 ... 已讀 應為-> 未讀'
        assert time == data['start_time'], \
            f'前台 訊息時間錯誤 ... {time} 應為-> {data["start_time"]}'
        assert self.get_text(MessagePageLocator.mail_title) == data['title'], \
            f'前台 訊息標題錯誤 ... {self.get_text(MessagePageLocator.mail_title)} 應為-> {data["title"]}'
        
        self.click(MessagePageLocator.mail_title)
        self.sleep(1)

        assert self.get_text(MessagePageLocator.mail_title) == data['title'], \
            f'前台 訊息內容標題錯誤 ... {self.get_text(MessagePageLocator.mail_title)} 應為-> {data["title"]}'
        assert self.get_text(MessagePageLocator.mail_text) == data['content'], \
            f'前台 訊息內容錯誤 ... {self.get_text(MessagePageLocator.mail_text)} 應為-> {data["content"]}'

        self.click(MessagePageLocator.mail_back)
        self.sleep(1)

        assert self.is_element_finded(MessagePageLocator.mail_readed) == True, \
            f'前台 訊息狀態錯誤 ... 未讀 應為-> 已讀'
        
        self.click(MessagePageLocator.mail_delete_first)
        
        if self.is_element_finded(MessagePageLocator.mail_delete_submit) == True:
            self.sleep(1)
            self.click(MessagePageLocator.mail_delete_submit)
        