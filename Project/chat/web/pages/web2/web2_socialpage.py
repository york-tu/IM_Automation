from datetime import datetime, timedelta
from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.web2.web2_basepage import BasePage
import pyautogui
import win32clipboard
import os, random, re, sys
import common.utils.globalvar as gl

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)


class SocialLocator:
    # ============================= 左側導航欄 ===========================================================================
    firstPage_btn = (By.XPATH, "//span[text()='首页']")  # 首頁鍵
    mainPage_button = (By.XPATH, "//span[text()='主页']")  # 主頁鍵(已登入)
    more_btn = (By.XPATH, "//span[text()='更多']")  # 更多(已登入)
    # ==================== 主頁 > 下方貼文 ====================
    post_list_first_post = (By.XPATH, "(//div[@class='flex flex-col w-full'])[1]")  # 媒體區第一則貼文
    post_list_first_post_liked_icon = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-row']//button[@class='hover:cursor-pointer'])[1]")  # 媒體列表第一則貼文-贊鍵
    post_list_first_post_liked_counts = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-row']//span[@class='text-sm font-normal leading-5 text-neutral-400'])[1]")  # # 媒體列表第一則貼文-贊數
    comment_icon = (By.XPATH, "//button[@aria-label='查看評論']")  # 開啟評論
    comment_counts = (By.XPATH, '//button[@aria-label="查看評論"]//span')  # 評論數
    post_liked_icon = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-col']//button[contains(@class,'hover:cursor-pointer')])[1]")  # 貼文內-贊鍵
    post_liked_counts = (By.XPATH, "(//span[@class='text-white text-sm font-normal leading-5 [text-shadow:rgba(0,0,0,0.5)_0px_0px_6px]'])[1]")  # 貼文內-贊數
    post_collect_icon = (By.XPATH, "(//div[@class='flex flex-col justify-center items-center']//button[@class='hover:cursor-pointer'])[1]")  # 貼文內-收藏鍵
    post_collect_counts = (By.XPATH, "(//span[@class='text-white text-sm font-normal leading-5 [text-shadow:rgba(0,0,0,0.5)_0px_0px_6px]'])[2]")  # 收藏數
    post_page_close_btn = (By.XPATH, "//button[contains(@class,'absolute') and contains(@class,'left-4') and contains(@class,'rounded-full')]")  # 貼文內頁關閉鍵

    # ==================== 評論頁 ====================
    input_comment = (By.XPATH, "//textarea[@name='comment']")  # 輸入留言
    send_btn = (By.XPATH, "(//button[@class='flex-shrink-0 flex items-center justify-center bg-green-500 rounded-full p-2 hover:cursor-pointer disabled:bg-neutral-300 disabled:cursor-not-allowed transition-colors'])[last()]")  # 送出鍵

    # === 評輪頁 > 留言 ===
    # post_recent_comment_commenter = (By.XPATH, "(//h4[@class='text-sm text-neutral-500 break-words line-clamp-2'])[1]")  # 最新一則留言-留言者
    post_recent_comment_commenter = (By.XPATH, "(//span[@class='text-sm text-neutral-500 truncate'])[1]")  # 最新一則留言-留言者
    post_recent_comment_content = (By.XPATH, "(//p[@class='text-sm text-neutral-800 break-words whitespace-pre-wrap'])[1]")  # 最新一則留言-留言內容
    post_recent_comment_add_time = (By.XPATH, '(//div[contains(@class,"flex-shrink-0") and contains(@class,"space-x-2") and contains(@class,"text-xs") and contains(@class,"text-neutral-500")])[1]//span')  # 最新一則留言-留言時間
    post_recent_comment_reply_btn = (By.XPATH, "(//button[@class='font-semibold hover:cursor-pointer'])[1]")  # 最新一則留言-回覆鍵
    post_recent_comment_likes_icon = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-col']//button[contains(@class,'hover:cursor-pointer')])[2]")  # 最新一則留言-贊鍵
    post_recent_comment_liked_counts = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-col']//span[@class='text-sm font-normal leading-5 text-neutral-400'])[1]")  # 最新一則留言-贊數
    post_recent_comment_author = (By.XPATH, "")  # 創作者tag

    # === 評輪頁 > 留言 > 回覆留言 ===
    # post_recent_comment_recent_reply_commenter = (By.XPATH, "(//h4[@class='text-sm text-neutral-500 break-words line-clamp-2'])[2]")  # 最新一則留言的最新回覆留言-留言者
    post_recent_comment_recent_reply_commenter = (By.XPATH, "(//span[@class='text-sm text-neutral-500 truncate'])[2]")  # 最新一則留言的最新回覆留言-留言者
    post_recent_comment_recent_reply_add_time = (By.XPATH, '(//div[contains(@class,"flex-shrink-0") and contains(@class,"space-x-2") and contains(@class,"text-xs") and contains(@class,"text-neutral-500")])[2]//span')  # 最新一則留言的最新回覆留言-留言時間
    post_recent_comment_recent_reply_content = (By.XPATH, "(//p[@class='text-sm text-neutral-800 break-words whitespace-pre-wrap'])[2]")  # 最新一則留言的最新回覆留言-留言內容
    post_recent_comment_recent_reply_reply_btn = (By.XPATH, "(//button[@class='font-semibold hover:cursor-pointer'])[2]")  # 最新一則留言的最新回覆留言-回覆鍵
    post_recent_comment_recent_reply_likes_icon = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-col']//button[contains(@class,'hover:cursor-pointer')])[3]")  # 最新一則留言的最新回覆留言-贊鍵
    post_recent_comment_reply_liked_counts = (By.XPATH, "(//div[@class='flex justify-center items-center gap-1 flex-col']//span[contains(@class,'text-sm font-normal leading-5 text-neutral-400')])[2]")  # 最新一則留言的最新回覆留言-贊數
    reply_to_icon = (By.XPATH, "")  # [A>B]">"
    reply_to_target_nickname = (By.XPATH, "")  # [A>B]中的B

    @staticmethod
    def post_index(num=1):
        locator = (By.XPATH, f"(//div[@class='flex flex-col w-full'])[{num}]")
        return locator


def _get_current_time():
    """獲取當前時間"""
    return datetime.now().strftime("%H:%M")


def convert_chinese_time_to_24h(time_string):
    time_string = time_string.strip()
    if time_string.startswith("上午"):
        time_str = time_string.replace("上午", "").strip()
        t = datetime.strptime(time_str, "%I:%M").strftime("%H:%M")
    elif time_string.startswith("下午"):
        time_str = time_string.replace("下午", "").strip()
        t_obj = datetime.strptime(time_str, "%I:%M")
        if t_obj.hour < 12:
            t_obj = t_obj.replace(hour=t_obj.hour + 12)
        t = t_obj.strftime("%H:%M")
    else:
        t = datetime.strptime(time_string, "%H:%M").strftime("%H:%M")
    return t


class SocialPage(BasePage):
    brand = gl.get_value("BRAND")

    def into_post_comment_page(self, post_index=1):
        """進入第index則貼文評論頁"""
        self.click(SocialLocator.post_index(post_index))
        self.click(SocialLocator.comment_icon)
        sleep(0.5)

    # ================== 評論留言 ==================
    def post_add_comment(self, commenter, comment, post_url=False, self_post=False):
        """添加評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)
        self._input_and_send_comment(comment)

        if not post_url and re.match(r'^https?://', comment):
            get_comment_text = self.get_text(SocialLocator.input_comment)
            assert get_comment_text == comment, f'URL留言未保留'
        else:
            comment_send_time = _get_current_time()
            self._verify_comment_details(commenter, comment, comment_send_time)
            self._verify_comment_count_updated(original_comment_count, self_post)

            # if self_post:
            #     self._verify_creator_label(SocialLocator.post_recent_comment_author)

    def _get_original_comment_count(self, self_post):
        """獲取原始評論數"""
        original_comment_count = self.get_text(SocialLocator.comment_counts)
        return int(original_comment_count)

    def _input_and_send_comment(self, comment):
        """輸入評論並送出"""
        self.click(SocialLocator.input_comment)
        self.type(SocialLocator.input_comment, comment)
        self.click(SocialLocator.send_btn)
        sleep(1)

    def _verify_comment_details(self, commenter, comment, send_time):
        """驗證評論的詳細資訊"""

        recent_comment_commenter = self.get_text(SocialLocator.post_recent_comment_commenter)
        recent_comment_content = self.get_text(SocialLocator.post_recent_comment_content)
        recent_comment_add_time = self.get_text(SocialLocator.post_recent_comment_add_time)

        # recent_comment_add_time = convert_chinese_time_to_24h(recent_comment_add_time)

        assert recent_comment_commenter == commenter, f'留言者暱稱顯示錯誤, 預期:{commenter},實際:{recent_comment_commenter}'
        assert recent_comment_content == comment, '留言內容顯示錯誤'
        # --------------------------------------------------------------
        # 轉成 datetime 物件（日期不重要，用同一天就好）
        # t1 = datetime.strptime(recent_comment_add_time, "%H:%M")
        # t2 = datetime.strptime(send_time, "%H:%M")
        # 判斷是否相等 或 t2 + 1分鐘相等
        # assert t1 == t2 or t1 == t2 + timedelta(minutes=1) or t1 == t2 - timedelta(minutes=1), f'留言時間有誤'
        # --------------------------------------------------------------
        assert self.is_element_finded(SocialLocator.post_recent_comment_reply_btn), '留言未出現回覆鍵'
        assert self.is_element_finded(SocialLocator.post_recent_comment_likes_icon), '留言未出現點贊icon'

    def _verify_comment_count_updated(self, original_count, self_post):
        """驗證評論數量是否更新"""
        updated_count = self._get_original_comment_count(self_post)
        assert updated_count == original_count + 1, f'評論數錯誤, 預期:{original_count + 1}, 實際:{updated_count}'

    def _verify_creator_label(self, author_locator):
        """驗證創作者標籤是否正確顯示"""
        assert self.is_element_finded(author_locator), '創作者標籤未顯示'
        assert self.get_text(author_locator) == '创作者', '創作者標籤顯示錯誤'

    # ================== 評論留言上回覆留言 ==================
    def post_recent_comment_add_reply(self, recent_commenter, replier, reply_content, self_post=True):
        """回覆評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)

        self.click(SocialLocator.post_recent_comment_reply_btn)
        self._verify_reply_target(recent_commenter)

        self._send_reply(reply_content)
        self._verify_reply(replier, reply_content, self_post, SocialLocator.post_recent_comment_recent_reply_commenter)

        self._verify_comment_count_updated(original_comment_count, self_post)
        # if self_post:
        #     self._verify_creator_label(SocialMediaLibraryPageLocator.post_recent_comment_recent_reply_author)
        self.click(SocialLocator.post_page_close_btn)  # 關閉評論頁

    def _verify_reply_target(self, recent_commenter):
        """驗證回覆目標"""
        reply_hint = self.get_attribute(SocialLocator.input_comment, 'placeholder')
        assert reply_hint == f'回复 {recent_commenter}...', '留言輸入框內的回覆對象錯誤'

    def _send_reply(self, reply_content):
        # 輸入回覆內容並送出
        self.type(SocialLocator.input_comment, reply_content)
        self.click(SocialLocator.send_btn)
        sleep(1)

    def _verify_reply(self, replier, reply_content, self_post, replier_locator):
        """送出回覆並驗證回覆訊息"""

        send_time = _get_current_time()
        post_recent_comment_recent_reply_commenter = self.get_text(replier_locator)  # 回覆訊息者暱稱
        post_recent_comment_recent_reply_add_time = self.get_text(SocialLocator.post_recent_comment_recent_reply_add_time)  # 回覆訊息留言者留言時間
        post_recent_comment_recent_reply_content = self.get_text(SocialLocator.post_recent_comment_recent_reply_content)
        assert self.is_element_finded(SocialLocator.post_recent_comment_recent_reply_reply_btn), '最新一則留言的回覆留言未出現[回覆]鍵'
        assert self.is_element_finded(SocialLocator.post_recent_comment_recent_reply_likes_icon), '最新一則留言的回覆留言未出現[贊]icon'

        # post_recent_comment_recent_reply_add_time = convert_chinese_time_to_24h(post_recent_comment_recent_reply_add_time)
        # --------------------------------------------------------------
        # 轉成 datetime 物件（日期不重要，用同一天就好）
        # t1 = datetime.strptime(post_recent_comment_recent_reply_add_time, "%H:%M")
        # t2 = datetime.strptime(send_time, "%H:%M")
        # 判斷是否相等 或 t2 + 1分鐘相等
        # assert t1 == t2 or t1 == t2 + timedelta(minutes=1) or t1 == t2 - timedelta(minutes=1), f'最新一則留言的回覆留言[時間]有誤, t1:{t1}, t2:{t2}'
        # --------------------------------------------------------------
        assert post_recent_comment_recent_reply_commenter == replier, '最新一則留言的回覆留言[留言者]有誤'
        assert post_recent_comment_recent_reply_content == reply_content, '最新一則留言的回覆留言[內容]有誤'

    def check_post_recent_comment(self, comment, commenter):
        """確認貼文最近的評論內容"""
        recent_comment = self.get_text(SocialLocator.post_recent_comment_content)
        recent_commenter = self.get_text(SocialLocator.post_recent_comment_commenter)
        assert recent_comment == comment, f'最新的評論內容不符, 預期:{comment}, 實際:{recent_comment}'
        assert recent_commenter == commenter, f'最新的評論留言者不符'

    def check_post_recent_reply(self, reply_comment, reply_commenter):
        """確認貼文最近的回覆內容"""
        recent_reply_comment = self.get_text(SocialLocator.post_recent_comment_recent_reply_content)
        recent_reply_commenter = self.get_text(SocialLocator.post_recent_comment_recent_reply_commenter)
        assert recent_reply_comment == reply_comment, '最近的回覆內容不符'
        assert recent_reply_commenter == reply_commenter, '最近的回覆留言者不符'

    def post_recent_comment_recent_reply_add_reply(self, recent_comment_recent_replier, sub_replier,
                                                   reply_reply_content, self_post=True):
        """回覆子評論並確認相關資訊"""
        original_comment_count = self._get_original_comment_count(self_post)

        self.click(SocialLocator.post_recent_comment_recent_reply_reply_btn)
        self._verify_reply_target(recent_comment_recent_replier)

        self._send_reply(reply_reply_content)
        self._verify_reply(sub_replier, reply_reply_content, self_post, SocialLocator.post_recent_comment_recent_reply_commenter)

        self._verify_reply_chain(sub_replier, recent_comment_recent_replier)
        self._verify_comment_count_updated(original_comment_count, self_post)

    def _verify_reply_chain(self, sub_replier, recent_comment_recent_replier):
        """確認回覆鏈中的暱稱和回覆對象"""

        post_recent_comment_recent_reply_commenter = self.get_text(SocialLocator.post_recent_comment_recent_reply_commenter)  # 回覆者A (A>B)
        # assert self.is_element_finded(SocialLocator.reply_to_icon), '未出現回覆鏈中的">"符號'
        # reply_target_nickname = self.get_text(SocialLocator.reply_to_target_nickname)  # 被回覆者B (A>B)

        assert post_recent_comment_recent_reply_commenter == sub_replier, '回覆者暱稱顯示錯誤'
        # assert reply_target_nickname == recent_comment_recent_replier, '回覆對象顯示錯誤'

    def post_recent_comment_add_like(self):
        """給最近的評論點贊並確認贊數更新"""
        return self._add_like_to_recent_comment(SocialLocator.post_recent_comment_likes_icon, self.check_recent_comment_liked_counts)

    def _add_like_to_recent_comment(self, like_icon, check_liked_counts_method):
        """給最近的評論或回覆點贊並確認贊數更新"""
        original_liked_counts = check_liked_counts_method() or 0
        self.click(like_icon)
        sleep(1)
        after_liked_counts = check_liked_counts_method()
        assert int(after_liked_counts) == int(original_liked_counts) + 1, '贊數未正確更新'
        return after_liked_counts

    def check_recent_comment_liked_counts(self):
        recent_comment_liked_counts = self.get_text(SocialLocator.post_recent_comment_liked_counts)
        return recent_comment_liked_counts

    def post_recent_reply_add_like(self):
        """給最近的回覆點贊並確認贊數更新"""
        after_reply_liked_counts = self._add_like_to_recent_comment(SocialLocator.post_recent_comment_recent_reply_likes_icon, self.check_recent_reply_liked_counts)
        self._close_comment_page()
        return after_reply_liked_counts

    def check_recent_reply_liked_counts(self):
        """獲取最近的回覆贊數"""
        recent_reply_liked_counts = self.get_text(SocialLocator.post_recent_comment_reply_liked_counts)
        return recent_reply_liked_counts

    def _close_comment_page(self):
        """關閉評論頁"""
        self.click(SocialLocator.post_page_close_btn)

    def first_post_add_remove_like(self, is_add=True):
        """貼文點贊/取消贊並確認贊數更新"""
        count = 1 if is_add else -1
        if is_add:
            # =========== 公開貼文列表上第一則貼文: 點贊 > 確認贊數 ===========
            post_list_original_liked_counts = self.get_text(SocialLocator.post_list_first_post_liked_counts)  # 公開貼文列表第一則貼文贊數
            self.click(SocialLocator.post_list_first_post_liked_icon)
            sleep(0.5)
            post_list_after_liked_counts = self.get_text(SocialLocator.post_list_first_post_liked_counts)  # 公開貼文列表第一則貼文贊數
            assert int(post_list_after_liked_counts) == int(post_list_original_liked_counts) + count, '贊數未正確更新'  # 確認贊數+1
            # =========== 進入第一則貼文: 確認贊數 > 取消贊 > 確認贊數 > 回到貼文列表 ===========
            self.into_post_comment_page(1)
            post_liked_counts = self.get_text(SocialLocator.post_liked_counts)  # 貼文內贊數
            assert post_liked_counts == post_list_after_liked_counts, f'贊數錯誤, 預期:{post_list_after_liked_counts},實際:{post_liked_counts}'  # 確認貼文內贊數同貼文列表上顯示
            self.click(SocialLocator.post_liked_icon)  # 取消贊
            sleep(0.5)
            post_liked_counts_after = self.get_text(SocialLocator.post_liked_counts)  # 貼文內贊數
            assert int(post_liked_counts_after) == int(post_liked_counts) - count, f'贊數錯誤,實際{post_liked_counts_after}=預期{post_liked_counts}-{count}未正確更新'  # 確認贊數-1
            self._close_comment_page()
            self.refresh_browser()
            sleep(0.5)
            # =========== 公開貼文列表上第一則貼文: 確認贊數 > 點贊  ===========
            post_list_liked_counts = self.get_text(SocialLocator.post_list_first_post_liked_counts)  # 公開貼文列表第一則貼文贊數
            assert post_list_liked_counts == post_liked_counts_after, f'贊數錯誤, 預期:{post_liked_counts_after},實際:{post_list_liked_counts}'  # 確認貼文列表上贊數同貼文內
            self.click(SocialLocator.post_list_first_post_liked_icon)
            sleep(0.5)
            self.refresh_browser()
        else:  # 取消贊
            # =========== 公開貼文列表上第一則貼文: 取消贊 > 確認贊數 ===========
            post_list_original_liked_counts = self.get_text(SocialLocator.post_list_first_post_liked_counts)  # 公開貼文列表第一則貼文贊數
            self.click(SocialLocator.post_list_first_post_liked_icon)
            sleep(0.5)
            post_list_after_liked_counts = self.get_text(SocialLocator.post_list_first_post_liked_counts)  # 公開貼文列表第一則貼文贊數
            assert int(post_list_after_liked_counts) == int(post_list_original_liked_counts) + count, '贊數未正確更新'  # 確認贊數+1
            self.refresh_browser()

    def post_add_remove_collect(self, is_add=True):
        """新增/取消收藏並確認收藏數更新"""
        count = 1 if is_add else -1
        original_collected_counts = self.get_text(SocialLocator.post_collect_counts)
        self.click(SocialLocator.post_collect_icon)
        sleep(1)
        after_collect_counts = self.get_text(SocialLocator.post_collect_counts)
        assert int(after_collect_counts) == int(original_collected_counts) + count, '收藏數未更新'
        self._close_comment_page()
        return after_collect_counts
