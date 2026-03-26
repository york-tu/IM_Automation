from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage
from Project.chat.web.pages.webs.web_loginpage import LoginPageLocator
import common.utils.globalvar as gl
import os, random, re, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
import pyautogui
import platform
import pyperclip

_IS_WINDOWS = platform.system().lower().startswith("win")
if _IS_WINDOWS:
    import win32clipboard


class MainPageLocator:
    # ============================= 導航欄 ==============================================================================
    firstPage_button = (By.XPATH, "//a[@href='/home']")  # 導航欄-首页
    message_button = (By.XPATH, "//a[@href='/chat']")  # 導航欄-信息
    post_btn = (By.XPATH, "//label[@for='customFileInput']")  # 導航欄-發布
    discover_button = (By.XPATH, "//a[@href='/discover']")  # 導航欄-發現
    mainPage_button = (By.XPATH, "//a[@href='/my-page']")  # 導航欄-主頁
    # ============================= 頁籤  ===============================================================================
    followed_tab = (By.XPATH, "//p[@class='text-[16rem] font-semibold text-[#FFFFFF66] text_shadow' and text()='已关注']")  # 頁籤-已關注
    recommend_tab = (By.XPATH, "//p[@class='text-[16rem] font-semibold text-[#FFFFFF66] text_shadow' and text()='推荐']")  # 頁籤-推薦
    search_post_tab = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/a[3]')  # 導航欄-主頁

    # ============================= 主頁 > 個人主頁 ======================================================================
    nickname = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/h1')  # 個人主頁-暱稱
    descriptions = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[2]')  # 個人主頁-說明文字
    main_page_followed_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-neutral-800'])[1]")
    main_page_fans_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-neutral-800'])[2]")
    main_page_thumb_up_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-neutral-800'])[3]")
    edit_profile_btn = (By.XPATH, "//button[text()='编辑主页']")  # 個人主頁-編輯主頁鍵
    share_self_profile_btn = (By.XPATH, "//button[text()='分享主页']")  # 個人主頁-分享主頁鍵
    clear_btn = (By.XPATH, "//i[@class='van-badge__wrapper van-icon van-icon-clear van-field__clear']")
    input_nickname = (By.XPATH, "//input[@placeholder='填写昵称']")  # 編輯主頁-暱稱
    input_descriptions = (By.XPATH, "//textarea[@placeholder='请输入个人简介']")  # 編輯主頁-個人簡介
    save_btn = (By.XPATH, "//button[text()='保存']")

    # ============================= 主頁 > 個人主頁 > 關注列表 =============================================================
    followed_list = (By.XPATH, "(//span[@class='van-tab__text van-tab__text--ellipsis'])[1]")  # 已關注列表
    fans_list = (By.XPATH, "(//span[@class='van-tab__text van-tab__text--ellipsis'])[2]")  # 粉絲列表
    list_first_member = (By.XPATH, "(//div[@class='grow px-[8rem] truncate w-[200rem] text-grand-1 whitespace-pre'])[1]")  # 列表第一位成員
    list_first_member_following_btn = (By.XPATH, '(//div[text()="关注"])[last()]')
    list_first_member_followed_btn = (By.XPATH, '(//div[text()="已关注"])[last()]')
    search_user = (By.XPATH, "//input[@placeholder='搜索用户']")  # 搜索用戶
    no_data = (By.XPATH, '//div[text()="目前无会员"]')  # 搜索無資料
    # ============================= 主頁 > 他人主頁 ======================================================================
    following_btn = (By.XPATH, '//button[//div[text()="关注"]]')  # 關注鍵
    followed_btn = (By.XPATH, '//button[//div[text()="已关注"]]')  # 已關注鍵
    others_main_page_followed_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-grand-1'])[1]")
    others_main_page_fans_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-grand-1'])[2]")
    others_main_page_thumb_up_counts = (By.XPATH, "(//div[@class='text-[20rem] font-semibold text-grand-1'])[3]")
    share_others_profile_btn = (By.XPATH, "//div[@class='pr-[16rem] flex items-center absolute right-0 cursor-pointer z-10']")  # 他人主頁-分享主頁鍵
    # ============================= 主頁 > 發布 =========================================================================
    post_via_photo = (By.XPATH, '//div[text()="照片"]')  # 發布 > 照片
    post_via_video = (By.XPATH, '//div[text()="视频"]')  # 發布 > 視頻
    input_post_descriptions = (By.ID, "post-introduction")  # 發布頁-撰寫說明
    post_confirm = (By.XPATH, "//button[text()='发布']")
    poster = (By.XPATH, "//p[@class='mb-[12rem] truncate text_shadow whitespace-pre']")  # 貼文作者
    post_descriptions = (By.XPATH, "//div[@class='whitespace-pre-wrap max-h-[313rem] break-words line-clamp-2']")  # 貼文內容
    post_back_btn = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[3]/div/svg')  # 貼文>返回鍵
    # ============================= 主頁 > 下方貼文 ======================================================================
    share_self_post_btn = (By.XPATH, "//div[@class='icon-wrapper dotIcon']")  # 個人貼文 > 分享鍵
    share_other_post_btn = (By.XPATH, "//div[@class='icon-wrapper share']")  # 他人貼文 > 分享鍵
    first_post = (By.XPATH, "(//div[@class='el-col el-col-8'])[1]")  # 媒體區第一則貼文
    post_author_name = (By.XPATH, "//p[@class='text-white-100 text-[14rem] mb-[12rem] truncate text_shadow']")  # 貼文作者
    post_description = (By.XPATH, "//p[@class='whitespace-pre-wrap max-h-[313rem] line-clamp-2']")  # 貼文描述
    # ============================= 發送給彈窗 ===========================================================================
    share_popup_title = (By.XPATH, "//div[@class='van-action-sheet__header']")  # 發送給彈窗標題
    share_close_btn = (By.XPATH, "//i[@class='van-badge__wrapper van-icon van-icon-cross van-action-sheet__close van-haptics-feedback']")  # x關閉鍵
    share_more_btn = (By.XPATH, '//div[text()="更多"]')  # 發送給彈窗 > 更多鍵
    share_search_column = (By.XPATH, "//input[@placeholder='搜索']")  # 發送給彈窗 > 更多 > 搜索框
    share_list_first = (By.XPATH, "//div[@class='flex items-center h-[60rem] border-b-[1px] border-neutral-0']")  # 發送給彈窗 > 更多 > 列表第一位
    share_input_message = (By.XPATH, "//textarea[@placeholder='有什么想和朋友说的...']")  # 分享訊息輸入框
    share_send_btn = (By.XPATH, '(//div[text()="发送"])[last()]')  # 發送鍵

    # ============================= toast ===========================================================================
    toast_msg = (By.XPATH, "(//p[@class='el-message__content'])[last()]")


class MainPage(BasePage):
    brand = gl.get_value("BRAND")

    def return_wap_version(self):  # 查看Web版本號
        self.open_base_url()
        git_version = self.driver.execute_script("return VITE_LAST_HASH;")
        official_version = self.driver.execute_script("return VITE_APP_VERSION;")
        return f'{official_version} ({git_version})'

    # =========================== 主頁 ========================================
    def into_main_page(self):
        self.click(MainPageLocator.mainPage_button)
        self.wait_loading_finish()
        assert self.is_element_finded(MainPageLocator.share_self_profile_btn)
        assert self.is_element_finded(MainPageLocator.edit_profile_btn)

    def get_nickname(self):
        return self.get_text(MainPageLocator.nickname)

    def get_descriptions(self):
        return self.get_text(MainPageLocator.descriptions)

    def get_self_social_data(self):
        if self.is_element_finded(MainPageLocator.mainPage_button):
            self.click(MainPageLocator.mainPage_button)
            sleep(1)
        main_page_followed_counts = self.get_text(MainPageLocator.main_page_followed_counts)
        main_page_fans_counts = self.get_text(MainPageLocator.main_page_fans_counts)
        main_page_thumb_up_counts = self.get_text(MainPageLocator.main_page_thumb_up_counts)
        return main_page_followed_counts, main_page_fans_counts, main_page_thumb_up_counts

    def get_others_social_data(self):
        others_main_page_followed_counts = self.get_text(MainPageLocator.others_main_page_followed_counts)
        others_main_page_fans_counts = self.get_text(MainPageLocator.others_main_page_fans_counts)
        others_main_page_thumb_up_counts = self.get_text(MainPageLocator.others_main_page_thumb_up_counts)
        return others_main_page_followed_counts, others_main_page_fans_counts, others_main_page_thumb_up_counts

    def change_nickname(self, new_nickname):
        self.click(MainPageLocator.edit_profile_btn)
        self.click(MainPageLocator.input_nickname)
        self.click(MainPageLocator.clear_btn)
        self.type(MainPageLocator.input_nickname, new_nickname)
        self.click(MainPageLocator.save_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.nickname) == new_nickname

    def change_descriptions(self, new_descriptions):
        self.click(MainPageLocator.edit_profile_btn)
        sleep(0.5)
        self.type(MainPageLocator.input_descriptions, new_descriptions)
        sleep(0.5)
        self.click(MainPageLocator.save_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.descriptions).__contains__(new_descriptions), f'個人簡介顯示有誤'

    def into_followed_list(self):
        self.click(MainPageLocator.main_page_followed_counts)
        sleep(1)
        assert self.get_text(MainPageLocator.followed_list).__contains__('已关注')
        assert self.get_text(MainPageLocator.fans_list).__contains__('粉丝')

    def into_fans_list(self):
        self.click(MainPageLocator.main_page_fans_counts)
        sleep(1)
        assert self.get_text(MainPageLocator.followed_list).__contains__('已关注')
        assert self.get_text(MainPageLocator.fans_list).__contains__('粉丝')

    def into_others_fans_list(self):
        self.click(MainPageLocator.others_main_page_fans_counts)
        sleep(1)
        assert self.get_text(MainPageLocator.followed_list).__contains__('已关注')
        assert self.get_text(MainPageLocator.fans_list).__contains__('粉丝')

    # =========================== 關注列表 ======================================
    def unfollow_member(self, user_nickname, main_page_followed_counts):
        self.type(MainPageLocator.search_user, user_nickname)
        sleep(1)
        self.click(MainPageLocator.list_first_member_followed_btn)
        sleep(1)
        assert self.is_element_finded(MainPageLocator.list_first_member_following_btn)
        followed_counts = self.get_text(MainPageLocator.followed_list).split()[1]
        assert int(followed_counts) == int(main_page_followed_counts) - 1

    def check_followed_list(self, user_nickname, main_page_followed_counts, add_follow=True):
        # =============================確認頁籤數字====================================
        followed_counts = self.get_text(MainPageLocator.followed_list).split()[1]
        assert followed_counts == main_page_followed_counts
        self.type(MainPageLocator.search_user, user_nickname)
        sleep(1)
        # =============================確認列表第一位關注成員 & 關注狀態 ==================
        if add_follow:
            assert self.get_text(MainPageLocator.list_first_member) == user_nickname
            assert self.is_element_finded(MainPageLocator.list_first_member_followed_btn)
        else:
            assert self.is_element_finded(MainPageLocator.no_data)

    # =========================== 粉絲列表 ======================================
    def check_fans_list(self, user_nickname, main_page_fans_counts, add_fans=False):
        # =============================確認頁籤數字====================================
        fans_counts = self.get_text(MainPageLocator.fans_list).split()[1]
        assert fans_counts == main_page_fans_counts
        # =============================確認列表第一位關注成員============================
        if add_fans:
            assert self.get_text(MainPageLocator.list_first_member) == user_nickname
        else:
            assert not self.get_text(MainPageLocator.list_first_member) == user_nickname

    # =========================== 他人主頁 =====================================
    def follow_user(self):
        self.wait_loading_finish()
        original_fans = int(self.get_text(MainPageLocator.others_main_page_fans_counts))
        self.click(MainPageLocator.following_btn)
        sleep(3)
        after_fans = int(self.get_text(MainPageLocator.others_main_page_fans_counts))
        assert after_fans == original_fans + 1, f'粉絲數錯誤, 實際:{after_fans}, 預期為{original_fans}+1'
        assert self.is_element_finded(MainPageLocator.followed_btn) is True
        return after_fans

    # =========================== 發布 ========================================
    def select_media(self, media_type='photo'):
        self.click(MainPageLocator.post_btn)
        sleep(1)

        post_media_folder_path = ''
        if media_type == 'photo':
            self.click(MainPageLocator.post_via_photo)
            post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\photo'
        elif media_type == 'video':
            self.click(MainPageLocator.post_via_video)
            post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\video'

        medias = [f for f in os.listdir(post_media_folder_path) if os.path.isfile(os.path.join(post_media_folder_path, f))]
        random_media = random.choice(medias)
        file_path = f'{post_media_folder_path}\\{random_media}'

        self.copy_to_clipboard(file_path)
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def copy_to_clipboard(self, text, retry=50, delay=2):
        if not _IS_WINDOWS:
            pyperclip.copy(text)
            return
        for attempt in range(retry):
            try:
                win32clipboard.OpenClipboard()
                try:
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardText(text)
                    return
                finally:
                    win32clipboard.CloseClipboard()
            except OSError as e:
                sleep(delay)
        raise Exception('無法複製路徑')

    def into_post_settings(self, descriptions):
        sleep(3)
        assert self.is_element_finded(MainPageLocator.input_post_descriptions)
        assert self.is_element_finded(MainPageLocator.post_confirm)
        self.type(MainPageLocator.input_post_descriptions, descriptions)
        self.click(MainPageLocator.post_confirm)

    def check_post(self, poster, descriptions):
        sleep(5)
        actual_poster = self.get_text(MainPageLocator.poster)
        actual_post_descriptions = self.get_text(MainPageLocator.post_descriptions)
        assert actual_poster == poster, f'發布者錯誤, 預期為:{poster}, 實際為:{actual_poster}'
        assert actual_post_descriptions == descriptions, f'貼文內容錯誤, 預期為:{descriptions}, 實際為:{actual_post_descriptions}'
        button_img_path = DIR_NAME + '\\element_icon\\post_back_btn.jpg'
        location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
        pyautogui.click(location)
        self.wait_loading_finish()

    def back_to_previous_page(self, counts=1):
        button_img_path = ''
        if self.brand.lower() == "gu":
            button_img_path = DIR_NAME + '\\element_icon\\back.jpg'
        elif self.brand.lower() == "mingpin":
            button_img_path = DIR_NAME + '\\element_icon\\back_mingpin.jpg'

        for i in range(counts):
            location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
            pyautogui.click(location)
            self.wait_loading_finish()

    # =========================== 發送給 ========================================
    def into_share_to_window(self, share_type=0):  # 0=self_main_page, 1=other_main_page, 2=self_post,3=other_post
        if share_type == 0:
            self.click(MainPageLocator.share_self_profile_btn)
        elif share_type == 1:
            self.click(MainPageLocator.share_others_profile_btn)
        elif share_type == 2:
            self.click(MainPageLocator.share_self_post_btn)
        elif share_type == 3:
            self.click(MainPageLocator.share_other_post_btn)
        sleep(1)
        assert self.get_text(MainPageLocator.share_popup_title) == '发送给', '分享彈窗錯誤'

    def share_to_group(self, share_target_group, share_message='', share_main_page=True):
        sleep(1)
        self.click(MainPageLocator.share_more_btn)
        sleep(1)
        self.type(MainPageLocator.share_search_column, share_target_group)
        self.click(MainPageLocator.share_list_first)
        sleep(1)
        assert self.is_element_finded(MainPageLocator.share_input_message), f'未發現留言欄位'
        self.type(MainPageLocator.share_input_message, share_message)
        self.click(MainPageLocator.share_send_btn)
        self.wait_visibility(MainPageLocator.toast_msg)
        assert self.get_text(MainPageLocator.toast_msg) == '分享成功'
        self.refresh_browser()
        # if not share_main_page:
            # button_img_path = DIR_NAME + '\\element_icon\\post_back_btn.jpg'
            # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
            # pyautogui.click(location)

    def into_first_post(self, user_nickname=None, instructions=None):
        """進入第一篇帖子並檢查作者名稱和媒體說明"""
        self.click(MainPageLocator.first_post)
        if user_nickname and instructions:
            self._check_post_author_and_content(user_nickname, instructions)

    def _check_post_author_and_content(self, user_nickname, instructions):
        """檢查創作者暱稱和媒體說明是否正確"""
        current_post_author_name = self.get_text(MainPageLocator.post_author_name)
        current_post_description = self.get_text(MainPageLocator.post_description)
        assert current_post_author_name == user_nickname, '創作者暱稱錯誤'
        assert current_post_description == instructions, f'媒體說明有誤, 預期:{instructions},實際:{current_post_description}'