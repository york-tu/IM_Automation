from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
from Project.chat.web.pages.webs.web_loginpage import LoginPageLocator
import os, random, re, sys
import common.utils.globalvar as gl
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
import pyautogui
import platform
import pyperclip

_IS_WINDOWS = platform.system().lower().startswith("win")
if _IS_WINDOWS:
    import win32clipboard

class SearchPageLocator:
    # ============================= 導航欄 ==============================================================================
    firstPage_button = (By.XPATH, "//a[@href='/home']")  # 導航欄-首页
    mainPage_button = (By.XPATH, "//a[@href='/my-page']")  # 導航欄-主頁
    # 右上角搜尋圖示外層是 <a href="/search">，點外層比點 svg/path 穩定
    mainPage_search_btn = (By.XPATH, "//a[@href='/search']")  # 主頁-貼文搜索鍵
    # ============================= 搜尋頁 ===============================================================================
    searchPage_description = (By.XPATH, "//p[text() = '最近搜索']")
    search_column = (By.XPATH, "//input[@class='text-[16rem] bg-transparent my-[6rem] flex-1 border-none outline-0 text-grand-1']")
    search_btn = (By.XPATH, "//p[text()='搜索']")
    search_clear_btn = (By.XPATH, "//div[@class='cursor-pointer w-[16rem] h-[16rem] cross-icon bg-white-100']")
    video_result_post_description = (By.XPATH, "//p[@class='text-[16rem] line-clamp-2 mt-[8rem] text-neutral-800 break-words']")
    video_result_poster = (By.XPATH, "//div[@class='text-[14rem] font-normal text-grand-2 truncate flex-1 min-w-0']")
    video_result_tab = (By.XPATH, "//span[text()='视频']")
    user_result_tab = (By.XPATH, "//span[text()='用户']")
    user_result_poster = (By.XPATH, "//p[@class='w-full text-[16rem] text-grand-1 overflow-hidden text-ellipsis whitespace-pre']")
    user_result_poster_info = (By.XPATH, "//div[@class='text-[14rem] text-grand-2']")
    user_result_follow_btn = (By.XPATH, "//div[@class='ml-auto text-[14rem] text-neutral-80 rounded-[4rem] py-[7rem] w-[74rem] text-center text-white-100 gradient-primary bg-primary-500']")
    @staticmethod
    def search_record_index(num):
        locator = (By.XPATH, f"(//p[@class='flex-1 overflow-hidden text-ellipsis text-neutral-800'])[{num}]")
        return locator


class SearchPage(BasePage):
    brand = gl.get_value("BRAND")

    def into_search_page(self):
        el = self.find_element(SearchPageLocator.mainPage_search_btn)
        # WAP 上此按鈕常出現「可見但 click 不觸發」，改用 JS click 提升穩定性
        self.driver.execute_script("arguments[0].click();", el)
        self.wait_loading_finish()

    def search_from_search_page(self, keywords):
        self.into_search_page()
        self.type(SearchPageLocator.search_column, keywords)
        self.click(SearchPageLocator.search_btn)

    def check_search_post_result(self, nickname, description):
        assert self.get_text(SearchPageLocator.video_result_post_description) == description
        assert self.get_text(SearchPageLocator.video_result_poster) == nickname

    def search_post(self, keywords, search_by_switch_tab=True):
        if search_by_switch_tab:
            self.type(SearchPageLocator.search_column, keywords)
            self.click(SearchPageLocator.video_result_tab)
        else:
            self.click(SearchPageLocator.video_result_tab)
            self.type(SearchPageLocator.search_column, keywords)
            self.click(SearchPageLocator.search_btn)

    def search_poster(self, user_nickname, search_by_switch_tab=True):
        if search_by_switch_tab:
            self.type(SearchPageLocator.search_column, user_nickname)
            self.click(SearchPageLocator.user_result_tab)
        else:
            self.click(SearchPageLocator.user_result_tab)
            self.type(SearchPageLocator.search_column, user_nickname)
            self.click(SearchPageLocator.search_btn)

    def check_search_poster_result(self, user_nickname):
        sleep(3)
        assert self.get_text(SearchPageLocator.user_result_poster) == user_nickname
        actual_text = self.get_text(SearchPageLocator.user_result_poster_info)
        assert "个粉丝" in actual_text
        assert "个视频" in actual_text
        assert self.is_element_finded(SearchPageLocator.user_result_follow_btn)

    def check_recent_search_record(self, expected_history):
        button_img_path = ''
        if self.brand.lower() == "gu":
            button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back.jpg')
        elif self.brand.lower() == "mingpin":
            button_img_path = os.path.join(DIR_NAME, 'element_icon', 'back_mingpin.jpg')
        location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        pyautogui.click(location)
        self.wait_loading_finish()
        assert self.is_element_finded(SearchPageLocator.searchPage_description)

        actual_history = []
        # 動態獲取所有的搜索紀錄
        for i in range(len(expected_history)):
            locator = SearchPageLocator.search_record_index(i+1)
            actual_history.append(self.get_text(locator))

        # 檢查實際的搜索紀錄是否與預期的一致
        for i, expected in enumerate(expected_history):
            assert actual_history[i] == expected, f"期望的搜索紀錄為: {expected}, 但實際為: {actual_history[i]}"





    # =========================== 發布 ========================================
    # def select_media(self, media_type='photo'):
    #     self.click(MainPageLocator.post_btn)
    #     sleep(1)
    #
    #     post_media_folder_path = ''
    #     if media_type == 'photo':
    #         post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\photo'
    #     elif media_type == 'video':
    #         post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\video'
    #
    #     medias = [f for f in os.listdir(post_media_folder_path) if os.path.isfile(os.path.join(post_media_folder_path, f))]
    #     random_media = random.choice(medias)
    #     file_path = f'{post_media_folder_path}\\{random_media}'
    #
    #     self.copy_to_clipboard(file_path)
    #     sleep(1)
    #     pyautogui.hotkey('ctrl', 'v')
    #     pyautogui.press('enter')
    #
    # def copy_to_clipboard(self, text, retry=50, delay=2):
    #     for attempt in range(retry):
    #         try:
    #             win32clipboard.OpenClipboard()
    #             try:
    #                 win32clipboard.EmptyClipboard()
    #                 win32clipboard.SetClipboardText(text)
    #                 return
    #             finally:
    #                 win32clipboard.CloseClipboard()
    #         except OSError as e:
    #             sleep(delay)
    #     raise Exception('無法複製路徑')
    #
    # def into_post_settings(self, descriptions):
    #     sleep(3)
    #     assert self.is_element_finded(MainPageLocator.input_post_descriptions)
    #     assert self.is_element_finded(MainPageLocator.post_confirm)
    #     self.type(MainPageLocator.input_post_descriptions, descriptions)
    #     self.click(MainPageLocator.post_confirm)
    #
    # def check_post(self, poster, descriptions):
    #     sleep(5)
    #     actual_poster = self.get_text(MainPageLocator.poster)
    #     actual_post_descriptions = self.get_text(MainPageLocator.post_descriptions)
    #     assert actual_poster == poster, f'發布者錯誤, 預期為:{poster}, 實際為:{actual_poster}'
    #     assert actual_post_descriptions == descriptions, f'貼文內容錯誤, 預期為:{descriptions}, 實際為:{actual_post_descriptions}'
    #     button_img_path = DIR_NAME + '\\element_icon\\post_back_btn.jpg'
    #     location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
    #     pyautogui.click(location)
    #     self.wait_loading_finish()
