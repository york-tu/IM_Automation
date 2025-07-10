from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage


class RecordPageLocator:
    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')
    search_chat_member_ID = (By.XPATH, '//input[@placeholder="请输入会员帐号ID"]')
    add_chat_start_time = (By.XPATH, '//label[text()="查詢时间"]/..//input[@placeholder="开始日期"]')
    add_chat_end_time = (By.XPATH, '//label[text()="查詢时间"]/..//input[@placeholder="结束日期"]')
    today = (By.XPATH, "//td[contains(@class,'available today')]")
    search_btn = (By.XPATH, "//span[text()='搜寻']")
    check_btn = (By.XPATH, "//span[text()='查看']")
    last_message = (By.XPATH, '(//div[@class="wcr-list__msg"])[last()]')

class RecordPage(BasePage):
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(RecordPageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(RecordPageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")

    def check_chat_record(self, chat_user_id, message):
        self.wait_loading_finish()
        self.type(RecordPageLocator.search_chat_member_ID, chat_user_id)
        self.click(RecordPageLocator.add_chat_start_time)
        sleep(1)
        self.click(RecordPageLocator.today)  # 開始時間: 今天
        self.click(RecordPageLocator.today)  # 結束時間: 今天
        sleep(1)
        self.click(RecordPageLocator.search_btn)
        sleep(1)
        self.click(RecordPageLocator.check_btn)

        assert self.get_text(RecordPageLocator.last_message) == str(message), f'expect:{message}, actual:{self.get_text(RecodePageLocator.last_message)}'
