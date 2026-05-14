from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.web2.web2_basepage import BasePage
import os, random, re, sys
import common.utils.globalvar as gl
import pyautogui
import win32clipboard

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)


class SearchPageLocator:
    # ============================= 左側導航欄 ===========================================================================
    firstPage_btn = (By.XPATH, "//span[text()='首页']")  # 首頁鍵
    mainPage_button = (By.XPATH, "//span[text()='主页']")  # 主頁鍵(已登入)
    more_btn = (By.XPATH, "//span[text()='更多']")  # 更多(已登入)
    # ============================= 搜尋 ===============================================================================
    search_column = (By.XPATH, "//input[@placeholder='搜索']")  # 上方搜索框
    search_btn = (By.XPATH, "//button[@aria-label='搜尋']")  # 搜索框內"搜索"鍵
    search_clear_btn = (By.XPATH, "//button[@aria-label='清空']")  # 搜索框內"清除"鍵
    search_record_description = (By.XPATH, "//p[text() = '最近搜索']")  # 最近搜索紀錄頁標題
    video_result_tab = (By.XPATH, "//button[text()='视频']")  # 視頻tab
    user_result_tab = (By.XPATH, "//button[text()='用户']")  # 用戶tab
    # ===== 視頻搜索結果頁 =====
    video_result_post_description = (By.XPATH, "//h3[@class='line-clamp-2 overflow-hidden text-sm text-neutral-800 font-normal leading-5']")  # 貼文描述
    video_result_poster = (By.XPATH, "//span[@class='text-sm text-neutral-500 font-normal truncate']")  # 貼文作者
    # ===== 用戶搜索結果頁 =====
    user_result_poster = (By.XPATH, "//p[@class='text-base leading-6 text-neutral-900 font-normal truncate']")
    user_result_poster_info = (By.XPATH, "")
    user_result_follow_btn = (By.XPATH, "/html/body/div[2]/div/main/div[2]/div[1]/div[2]/button/span")

    @staticmethod
    def search_record_index(num):
        locator = (By.XPATH, f"(//span[@class='text-sm text-neutral-900 font-normal truncate'])[{num}]")
        return locator


class SearchPage(BasePage):
    brand = gl.get_value("BRAND")

    def search_post(self, keywords):
        self.type(SearchPageLocator.search_column, keywords)
        self.click(SearchPageLocator.search_btn)
        self.click(SearchPageLocator.video_result_tab)

    def check_search_post_result(self, nickname, description):
        assert self.get_text(SearchPageLocator.video_result_post_description) == description
        assert self.get_text(SearchPageLocator.video_result_poster) == nickname

    def search_poster(self, user_nickname):
        self.type(SearchPageLocator.search_column, user_nickname)
        self.click(SearchPageLocator.search_btn)
        self.click(SearchPageLocator.user_result_tab)

    def check_search_poster_result(self, user_nickname):
        sleep(3)
        _actual = self.get_text(SearchPageLocator.user_result_poster)
        assert _actual == user_nickname, f'預期:{user_nickname}, 實際:{_actual}'
        # actual_text = self.get_text(SearchPageLocator.user_result_poster_info)
        # assert "个粉丝" in actual_text
        # assert "个视频" in actual_text
        assert self.is_element_finded(SearchPageLocator.user_result_follow_btn)

    def check_recent_search_record(self, expected_history):
        self.click(SearchPageLocator.search_column)
        assert self.is_element_finded(SearchPageLocator.search_record_description)

        actual_history = []
        # 動態獲取所有的搜索紀錄
        for i in range(len(expected_history)):
            locator = SearchPageLocator.search_record_index(i+1)
            actual_history.append(self.get_text(locator))

        # 檢查實際的搜索紀錄是否與預期的一致
        for i, expected in enumerate(expected_history):
            assert actual_history[i] == expected, f"期望的搜索紀錄為: {expected}, 但實際為: {actual_history[i]}"

