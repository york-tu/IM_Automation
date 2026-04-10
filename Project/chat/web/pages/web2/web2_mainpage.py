from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.web2.web2_basepage import BasePage
import common.utils.globalvar as gl
import os, random, re, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
import pyautogui
import win32clipboard


class MainPageLocator:
    # ==================== 左側導航欄 ====================
    firstPage_btn = (By.XPATH, "//span[text()='首页']")  # 首頁鍵
    post_btn = (By.XPATH, "//span[text()='发布']")  # 發布鍵
    mainPage_button = (By.XPATH, "//span[text()='主页']")  # 主頁鍵(已登入)
    more_btn = (By.XPATH, "//span[text()='更多']")  # 更多(已登入)
    # ==================== 主頁上方 ====================
    edit_profile_btn = (By.XPATH, "//button[text()='编辑主页']")  # 個人主頁-編輯主頁鍵
    share_self_profile_btn = (By.XPATH, "//button[text()='分享主页']")  # 個人主頁-分享主頁鍵
    nickname = (By.XPATH, "//h2[@class='text-xl font-semibold text-neutral-800 leading-7']")  # 個人主頁-暱稱
    self_id = (By.XPATH, "//p[@class='text-xs text-neutral-400 leading-4.5']")  # 個人主頁-id
    descriptions = (By.XPATH,"//div[@class='flex-1 py-4 text-sm text-neutral-800 leading-5 whitespace-pre-line']")  # 個人主頁-說明文字
    # ==================== 主頁下方 ====================
    counts_following = (By.XPATH, "//button[.//span[text()='已关注']]//span[1]")  # 主頁已關注數
    counts_fans = (By.XPATH, "//button[.//span[text()='粉丝']]//span[1]")  # 主頁粉絲數
    counts_likes = (By.XPATH, "//button[.//span[text()='赞']]//span[1]")  # 主頁點讚數
    # ==================== 編輯主頁視窗 ====================
    input_nickname = (By.XPATH, "//input[@placeholder='请输入昵称']")  # 編輯主頁-輸入暱稱
    input_descriptions = (By.XPATH, "//textarea[@placeholder='请输入个人简介']")  # 編輯主頁-輸入個人簡介
    save_btn = (By.XPATH, "//button[text()='保存']")
    # ==================== 發布頁 ====================
    upload_btn = (By.XPATH, "//button[text()='上传']")  # 發布>上傳鍵
    input_post_descriptions = (By.XPATH, "//textarea[@placeholder='输入正文描述']")  # 發布頁-撰寫說明
    privacy_list = (By.XPATH, "//span[@class='font-normal text-neutral-900']")  # 隱私設置下拉選單
    privacy_everyone = (By.XPATH, "//ul[@class='flex flex-col overflow-y-auto']//li[1]")  # 隱私設置-所有人
    privacy_mutual_followers = (By.XPATH, "//ul[@class='flex flex-col overflow-y-auto']//li[2]")  # 隱私設置-互關
    privacy_fans = (By.XPATH, "//ul[@class='flex flex-col overflow-y-auto']//li[3]")  # 隱私設置-粉絲
    privacy_self = (By.XPATH, "//ul[@class='flex flex-col overflow-y-auto']//li[4]")  # 隱私設置-自己
    post_confirm = (By.XPATH, "//button[text()='發佈']")
    # =================== 已關注/粉絲列表=============================
    focus_tab = (By.XPATH,"//button[@class='flex-1 text-center font-medium leading-6 hover:cursor-pointer text-neutral-900']")  # focus的關注/粉私列表
    list_first_member = (By.XPATH,"(//p[@class='text-base leading-6 text-neutral-900 font-normal truncate'])[1]")  # 列表第一位成員
    list_first_member_following_status = (By.XPATH, "(//div[@class='flex items-center space-x-2 px-6 py-2 w-full']//button//span)[1]")
    list_close_btn = (By.XPATH, "//button[@aria-label='關閉']")  # 關注/粉私列表"關閉"鍵
    list_follow_btn = (By.XPATH, '/html/body/div[3]/div/div[3]/div/div[1]/div[2]/button/span')  # 列表第一行關注/已關注鍵
    # ==================== 主頁 > 下方貼文 ====================
    post_page_poster = (By.XPATH, "//span[@class='text-neutral-800 line-clamp-2']")  # 貼文內頁作者
    post_page_descriptions = (By.XPATH, "//p[@class='text-sm text-neutral-800 leading-5 break-words']")  # 貼文內頁內容
    post_page_close_btn = (By.XPATH,"//button[contains(@class,'absolute') and contains(@class,'left-4') and contains(@class,'rounded-full')]")  # 貼文內頁關閉鍵
    # ==================== 主頁 > 下方媒體櫃 ====================
    public_library_tab = (By.XPATH, '(//div[contains(@class,"flex") and contains(@class,"items-center") and contains(@class,"py-2") and contains(@class,"shrink-0")]//button)[1]')  # 公開媒體區
    private_library_tab = (By.XPATH, '(//div[contains(@class,"flex") and contains(@class,"items-center") and contains(@class,"py-2") and contains(@class,"shrink-0")]//button)[2]')  # 私人媒體區
    collect_library_tab = (By.XPATH, '(//div[contains(@class,"flex") and contains(@class,"items-center") and contains(@class,"py-2") and contains(@class,"shrink-0")]//button)[3]')  # 收藏媒體區
    likes_library_tab = (By.XPATH, '(//div[contains(@class,"flex") and contains(@class,"items-center") and contains(@class,"py-2") and contains(@class,"shrink-0")]//button)[4]')  # 已贊媒體區
    # ==================== 搜索 ====================
    search_column = (By.XPATH, "//input[@placeholder='搜索']")  # 上方搜索框
    search_btn = (By.XPATH, "//button[@aria-label='搜尋']")  # 搜索框內"搜索"鍵
    user_result_tab = (By.XPATH, "//button[text()='用户']")  # 用戶tab
    user_icon = (By.XPATH, "//div[@class='relative rounded-full overflow-hidden flex-shrink-0 size-13 hover:cursor-pointer']")  # 用戶列表用戶頭像
    # ==================== 主頁 > 他人主頁 ====================
    following_btn = (By.XPATH, "//button[text()='关注']")  # 關注鍵
    followed_btn = (By.XPATH, "//button[text()='已关注']")  # 已關注鍵




    # ================================================================================================================
    # ================================================================================================================
    # ============================= 主頁 > 下方貼文 ======================================================================
    share_self_post_btn = (By.XPATH, "//div[@class='icon-wrapper dotIcon']")  # 個人貼文 > 分享鍵
    share_other_post_btn = (By.XPATH, "//div[@class='icon-wrapper share']")  # 他人貼文 > 分享鍵
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

    @staticmethod
    def post_index(num=1):
        locator = (By.XPATH, f"(//div[@class='flex flex-col w-full'])[{num}]")  # 貼文列表第幾則
        return locator

    @staticmethod
    def post_index_poster(num=1):
        locator = (By.XPATH, f"(//span[@class='text-sm text-neutral-500 font-normal truncate'])[{num}]")  # 貼文列表第幾則-貼文作者
        return locator

    @staticmethod
    def post_index_description(num=1):
        locator = (By.XPATH, f"(//h3[@class='line-clamp-2 overflow-hidden text-sm text-neutral-800 font-normal leading-5'])[{num}]")  # 貼文列表第幾則-貼文內容
        return locator


def copy_to_clipboard(text, retry=50, delay=2):
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


class MainPage(BasePage):
    brand = gl.get_value("BRAND")

    def return_web2_version(self):  # 查看Web版本號
        self.open_base_url()
        git_version = self.driver.execute_script("return LAST_COMMIT_HASH;")
        official_version = self.driver.execute_script("return APP_VERSION;")
        return f'{official_version} ({git_version})'

    def into_first_page(self):
        self.click(MainPageLocator.firstPage_btn)
        self.wait_loading_finish()

    # =========================== 主頁 ========================================
    def into_main_page(self):
        self.click(MainPageLocator.mainPage_button)
        self.wait_loading_finish()
        # assert self.is_element_finded(MainPageLocator.share_self_profile_btn)
        assert self.is_element_finded(MainPageLocator.edit_profile_btn)

    def into_public_library(self):
        self.click(MainPageLocator.public_library_tab)
        self.wait_loading_finish()

    def into_collect_library(self):
        self.click(MainPageLocator.collect_library_tab)
        self.wait_loading_finish()

    def into_likes_library(self):
        self.click(MainPageLocator.likes_library_tab)

    def get_nickname(self):
        return self.get_text(MainPageLocator.nickname)

    def get_descriptions(self):
        return self.get_text(MainPageLocator.descriptions)

    def get_social_data(self):
        main_page_followed_counts = self.get_text(MainPageLocator.counts_following)
        main_page_fans_counts = self.get_text(MainPageLocator.counts_fans)
        main_page_likes_counts = self.get_text(MainPageLocator.counts_likes)
        return main_page_followed_counts, main_page_fans_counts, main_page_likes_counts

    def change_nickname(self, new_nickname):
        self.click(MainPageLocator.edit_profile_btn)
        self.click(MainPageLocator.input_nickname)
        self.type(MainPageLocator.input_nickname, new_nickname)
        self.click(MainPageLocator.save_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.nickname) == new_nickname

    def change_descriptions(self, new_descriptions):
        self.click(MainPageLocator.edit_profile_btn)
        self.type(MainPageLocator.input_descriptions, new_descriptions)
        self.click(MainPageLocator.save_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.descriptions).__contains__(new_descriptions), f'個人簡介顯示有誤'

    def search_user(self, user_nickname):  # 搜索用戶
        self.type(MainPageLocator.search_column, user_nickname)
        self.click(MainPageLocator.search_btn)
        self.click(MainPageLocator.user_result_tab)
        self.click(MainPageLocator.user_icon)
        sleep(1)

    def follow_member_from_main_page(self, follow_who, who_follow):
        self.search_user(follow_who)
        original_fans_counts = int(self.get_text(MainPageLocator.counts_fans))
        self.click(MainPageLocator.following_btn)
        sleep(1)
        after_fans_counts = int(self.get_text(MainPageLocator.counts_fans))
        # ========= 關注對方後確認對方主頁粉絲數與關注狀態 =========
        assert after_fans_counts == original_fans_counts + 1, f'粉絲數錯誤, 實際:{after_fans_counts}, 預期為{original_fans_counts}+1'
        assert self.is_element_finded(MainPageLocator.followed_btn) is True
        # ========= 關注對方後確認對方粉絲列表第一條成員 =========
        self.click(MainPageLocator.counts_fans)
        sleep(1)
        list_first_member = self.get_text(MainPageLocator.list_first_member)
        assert list_first_member == who_follow, f'預期:{who_follow}, 實際:{list_first_member}'
        after_counts_fans = self.get_text(MainPageLocator.focus_tab).split()[1]
        assert int(after_counts_fans) == after_fans_counts
        self.click(MainPageLocator.list_close_btn)

        return after_fans_counts

    def check_followed_list(self, follow_who, main_page_counts_following):
        # =============================確認頁籤數字====================================
        self.click(MainPageLocator.counts_following)
        followed_counts = self.get_text(MainPageLocator.focus_tab).split()[1]
        assert int(followed_counts) == int(main_page_counts_following)
        # =============================確認列表第一位關注成員 & 關注狀態 ==================
        assert self.get_text(MainPageLocator.list_first_member) == follow_who
        assert self.get_text(MainPageLocator.list_first_member_following_status) == '已关注'
        self.click(MainPageLocator.list_close_btn)

    def check_fans_list(self, who_follow, main_page_counts_fans):
        self.click(MainPageLocator.counts_fans)
        fans_counts = self.get_text(MainPageLocator.focus_tab).split()[1]
        assert int(fans_counts) == main_page_counts_fans
        assert self.get_text(MainPageLocator.list_first_member) == who_follow
        self.click(MainPageLocator.list_close_btn)

    def check_list_first_member(self, member, main_page_counts, tab='0'):
        if tab == '0':  # 已關注列表
            self.click(MainPageLocator.counts_following)
        else:  # 粉絲列表
            self.click(MainPageLocator.counts_fans)

        assert self.get_text(MainPageLocator.focus_tab).split()[1] == main_page_counts
        if self.get_text(MainPageLocator.list_first_member) == member:
            self.click(MainPageLocator.list_close_btn)
            return True
        else:
            self.click(MainPageLocator.list_close_btn)
            return False

    def unfollow_first_member_from_followed_list(self, user_nickname):
        self.click(MainPageLocator.counts_following)
        if self.get_text(MainPageLocator.list_first_member) == user_nickname:
            original_counts_following = self.get_text(MainPageLocator.focus_tab).split()[1]
            self.click(MainPageLocator.list_follow_btn)
            sleep(1)
            assert self.get_text(MainPageLocator.list_first_member_following_status) == '回关'
            after_counts_following = self.get_text(MainPageLocator.focus_tab).split()[1]
            assert int(after_counts_following) == int(original_counts_following) - 1
        else:
            assert False
        self.click(MainPageLocator.list_close_btn)

    # =========================== 發布 ========================================
    def select_media(self, media_type='photo'):
        self.click(MainPageLocator.post_btn)
        self.click(MainPageLocator.upload_btn)
        sleep(5)
        post_media_folder_path = ''
        if media_type == 'photo':
            post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\photo'
        elif media_type == 'video':
            post_media_folder_path = f'{DIR_NAME}\\test_medias\\post_media\\video'

        medias = [f for f in os.listdir(post_media_folder_path) if os.path.isfile(os.path.join(post_media_folder_path, f))]
        random_media = random.choice(medias)
        file_path = f'{post_media_folder_path}\\{random_media}'

        copy_to_clipboard(file_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def into_post_settings_and_confirm(self, descriptions, privacy=0):
        sleep(3)
        assert self.is_element_finded(MainPageLocator.input_post_descriptions)
        assert self.is_element_finded(MainPageLocator.post_confirm)
        # ========== 設定隱私權 ==========
        if privacy == 1:
            self.click(MainPageLocator.privacy_list)
            self.click(MainPageLocator.privacy_mutual_followers)
        elif privacy == 2:
            self.click(MainPageLocator.privacy_list)
            self.click(MainPageLocator.privacy_fans)
        elif privacy == 3:
            self.click(MainPageLocator.privacy_list)
            self.click(MainPageLocator.privacy_self)
        else:
            self.click(MainPageLocator.privacy_list)
            self.click(MainPageLocator.privacy_everyone)
        # ==============================
        self.type(MainPageLocator.input_post_descriptions, descriptions)
        self.click(MainPageLocator.post_confirm)
        sleep(7)

    def check_post(self, poster, descriptions, is_post=True, post_index=0):
        try:
            # ================= 確認貼文列表第一則 =============
            post_list_poster = self.get_text(MainPageLocator.post_index_poster(post_index+1))
            post_list_descriptions = self.get_text(MainPageLocator.post_index_description(post_index+1))
            assert post_list_poster == poster, f'發布者錯誤, 預期為:{poster}, 實際為:{post_list_poster}'
            assert post_list_descriptions == descriptions, f'貼文內容錯誤, 預期為:{descriptions}, 實際為:{post_list_descriptions}'
            # ================= 進到第一則貼文確認內容 =================
            self.click(MainPageLocator.post_index(post_index+1))
            sleep(1)

            post_page_poster = self.get_text(MainPageLocator.post_page_poster)
            post_page_descriptions = self.get_text(MainPageLocator.post_page_descriptions)
            assert post_page_poster == poster, f'發布者錯誤, 預期為:{poster}, 實際為:{post_page_poster}'
            assert post_page_descriptions == descriptions, f'貼文內容錯誤, 預期為:{descriptions}, 實際為:{post_page_descriptions}'
            # =========================================================
            self.click(MainPageLocator.post_page_close_btn)
            return True
        except AssertionError:
            if is_post:
                raise
            return False
        except Exception:
            # 如果你也希望「找不到元素 / click 失敗」在 is_post=False 時也回 False
            if is_post:
                raise
            return False

    # =========================== 發送給 ========================================
    # def into_share_to_window(self, share_type=0):  # 0=self_main_page, 1=other_main_page, 2=self_post,3=other_post
    #     if share_type == 0:
    #         self.click(MainPageLocator.share_self_profile_btn)
    #     elif share_type == 1:
    #         self.click(MainPageLocator.share_others_profile_btn)
    #     elif share_type == 2:
    #         self.click(MainPageLocator.share_self_post_btn)
    #     elif share_type == 3:
    #         self.click(MainPageLocator.share_other_post_btn)
    #     sleep(1)
    #     assert self.get_text(MainPageLocator.share_popup_title) == '发送给', '分享彈窗錯誤'

    # def share_to_group(self, share_target_group, share_message='', share_main_page=True):
    #     sleep(1)
    #     self.click(MainPageLocator.share_more_btn)
    #     sleep(1)
    #     self.type(MainPageLocator.share_search_column, share_target_group)
    #     self.click(MainPageLocator.share_list_first)
    #     sleep(1)
    #     assert self.is_element_finded(MainPageLocator.share_input_message), f'未發現留言欄位'
    #     self.type(MainPageLocator.share_input_message, share_message)
    #     self.click(MainPageLocator.share_send_btn)
    #     self.wait_visibility(MainPageLocator.toast_msg)
    #     assert self.get_text(MainPageLocator.toast_msg) == '分享成功'
    #     self.refresh_browser()
        # if not share_main_page:
            # button_img_path = DIR_NAME + '\\element_icon\\post_back_btn.jpg'
            # location = pyautogui.locateCenterOnScreen(button_img_path, confidence=0.8)
            # pyautogui.click(location)

    # def into_first_post(self, user_nickname=None, instructions=None):
    #     """進入第一篇帖子並檢查作者名稱和媒體說明"""
    #     self.click(MainPageLocator.first_post)
    #     if user_nickname and instructions:
    #         self._check_post_author_and_content(user_nickname, instructions)
    #
    # def _check_post_author_and_content(self, user_nickname, instructions):
    #     """檢查創作者暱稱和媒體說明是否正確"""
    #     current_post_author_name = self.get_text(MainPageLocator.post_author_name)
    #     current_post_description = self.get_text(MainPageLocator.post_description)
    #     assert current_post_author_name == user_nickname, '創作者暱稱錯誤'
    #     assert current_post_description == instructions, f'媒體說明有誤, 預期:{instructions},實際:{current_post_description}'