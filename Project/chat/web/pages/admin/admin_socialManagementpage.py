from time import sleep

from selenium.webdriver.common.by import By
import datetime
from Project.chat.web.pages.admin.admin_basepage import BasePage


class SocialManagementPageLocator:
    # 通用
    page_title = (By.XPATH, '//div[@class="page-title"]')
    search_btn = (By.XPATH, "//span[text()='搜寻']")

    # 搜尋欄位
    result_empty = (By.XPATH, '//span[@class="el-table__empty-text"]')
    member_ID = (By.XPATH, '//label[text()="会员帐号"]/..//input[@placeholder="请输入会员帐号"]')
    social_management = (By.XPATH, "//span[text()='社群管理']")  # 社群管理
    confirm_btn = (By.XPATH, '(//button[@class="el-button el-button--primary el-button--mini"])[last()]')  # 二次確認彈窗"確定"鍵
    confirm_black_btn = (By.XPATH, '(//button[@class="el-button el-button--primary el-button--mini"])[last()-1]')  # 二次確認彈窗"確定"鍵
    # =================================== 媒体审核 ==============================================
    media_audit = (By.XPATH, "//a[text()=' 媒体审核']")  # 媒体审核
    # 資料欄位
    data_media_audit_radio_btn = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    data_media_audit_post_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    data_media_audit_user_ID = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    data_media_audit_user_nickname = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")
    data_media_audit_post_content = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")
    data_media_audit_media_instruction = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")
    data_media_audit_viewing_permissions = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")
    data_media_audit_audit_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[8]")
    data_media_audit_update_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[9]")
    data_media_audit_operate_pass_btn = (By.XPATH, '//button[@class="el-button el-button--primary el-button--mini"]//span[text()="通 过"]')
    data_media_audit_operate_reject_btn = (By.XPATH, '//button[@class="el-button el-button--danger el-button--mini"]//span[text()="拒 绝"]')

    # =================================== 自動審核 ==============================================
    auto_audit = (By.XPATH, "//a[text()=' 自动审核']")  # 自動審核
    # 資料欄位
    data_auto_audit_radio_btn = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    data_auto_audit_user_ID = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    data_auto_audit_user_nickname = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    data_auto_audit_type = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")
    data_auto_audit_update_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")
    data_auto_audit_operate_black_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[7]//span[text()="黑名单"]')
    data_auto_audit_operate_white_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[7]//span[text()="白名单"]')
    data_auto_audit_operate_normal_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[7]//span[text()="一般会员"]')

    # =================================== 屏蔽字詞 ==============================================
    block_words = (By.XPATH, "//a[text()=' 屏蔽字词']")  # 屏蔽字词
    search_block_words_btn = (By.XPATH, "//span[text()='搜寻']")  # 搜尋
    add_block_words_btn = (By.XPATH, "//span[text()='新增']")  # 新增
    add_block_words_dialog_title = (By.XPATH, "//span[text()='新增屏蔽字词']")  # 新增屏蔽字词視窗
    add_block_words = (By.XPATH, '//div[@class="el-input el-input--small"]//input[@placeholder="请输入屏蔽字词"]')  # 新增屏蔽字词欄位
    search_block_words = (By.XPATH, '//div[@class="el-input el-input--mini"]//input[@placeholder="请输入屏蔽字词"]')  # 搜尋屏蔽字词欄位
    submit_btn = (By.XPATH, '//span[text()="确定"]')  # 確定button
    delete_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div/button')  # 刪除button
    data_block_words = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")  # 列表第一則第一欄

    # =================================== 檢舉內容 ==============================================
    # 搜尋欄位
    impeach = (By.XPATH, "//a[text()=' 检举内容']")  # 檢舉內容
    impeach_result_empty = (By.XPATH, '//span[@class="el-table__empty-text"]')
    input_informant_ID = (By.XPATH, '//label[text()="检举帐号"]/..//input[@placeholder="请输入会员帐号"]')  # 檢舉帳號
    input_defendant_ID = (By.XPATH, '//label[text()="被检举帐号"]/..//input[@placeholder="请输入会员帐号"]')  # 被檢舉帳號
    search_impeach_btn = (By.XPATH, "//span[text()='搜寻']")  # 搜尋
    # 資料欄位
    data_first_informant_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")  # 列表第一行: 第一次檢舉帳號
    data_informant_counts = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")  # 列表第一行: 檢舉人數(次數)
    data_defendant_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")  # 列表第一行: 被檢舉帳號
    data_impeach_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")  # 列表第一行: 檢舉狀態
    data_display_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[8]")  # 列表第一行: 前台顯示
    data_approve_btn = (By.XPATH, '//button[@class="el-button el-button--primary el-button--mini"]//span[text()="通过"]')  # 列表第一行: 操作 > 通過
    data_impeach_detail_behavior = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr/td[2]/div")  # 檢舉內容第一行: 行為
    data_impeach_detail_informant_id = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div")  # 檢舉內容第一行: 檢舉帳號
    data_impeach_detail_reason = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[3]/table/tbody/tr/td[4]/div")  # 檢舉內容第一行: 檢舉理由
    data_impeach_detail_close_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[4]/div/div[1]/button/i')  # 檢舉內容視窗關閉
    impeach_confirm_btn = (By.XPATH, '(//button[@class="el-button el-button--primary el-button--mini"]//span[text()="确定"])[1]')  # 二次確認彈窗"確定"鍵

    # =================================== 貼文數據 ==============================================
    # 搜尋欄位
    post_data = (By.XPATH, "//a[text()=' 贴文数据']")  # 貼文數據
    input_poster_ID = (By.XPATH, '//label[text()="发布帐号"]/..//input[@placeholder="请输入会员帐号"]')  # 發布帳號
    search_post_btn = (By.XPATH, "//span[text()='搜寻']")  # 搜尋
    # 資料欄位
    data_poster_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")  # 列表第一行: 會員帳號
    data_post_descriptions = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")  # 列表第一行: 貼文說明
    data_view_counts = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")  # 列表第一行: 觀看次數
    data_viewer_counts = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")  # 列表第一行: 觀看人數
    # =================================== 創作者數據 ==============================================
    # 搜尋欄位
    creator_data = (By.XPATH, "//a[text()=' 创作者数据']")  # 創作者數據
    input_creator_ID = (By.XPATH, '//label[text()="会员帐号"]/..//input[@placeholder="请输入会员帐号"]')  # 會員帳號
    search_creator_btn = (By.XPATH, "//span[text()='搜寻']")  # 搜尋
    # 資料欄位
    data_creator_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")  # 列表第一行: 會員帳號
    data_creator_view_counts = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")  # 列表第一行: 觀看次數
    data_creator_viewer_counts = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")  # 列表第一行: 觀看人數

    # =================================== 社群設定 ==============================================
    social_setting = (By.XPATH, "//a[text()=' 社群设定']")  # 社群设定
    set_post_URL_on = (By.XPATH, '(//label[text()="贴文评论超连结"]/..//span[text() = "开启"])')  # 貼文評論超連結: 開
    set_post_URL_off = (By.XPATH, '(//label[text()="贴文评论超连结"]/..//span[text() = "关闭"])')  # 貼文評論超連結: 關
    post_URL_off_checked = (By.XPATH,'(//label[text()="贴文评论超连结"]/..//label[@class = "el-radio is-checked"]//span[text() = "关闭"])')  # 貼文評論超連結"關閉"checked
    post_URL_on_checked = (By.XPATH,'(//label[text()="贴文评论超连结"]/..//label[@class = "el-radio is-checked"]//span[text() = "开启"])')  # 貼文評論超連結"開啟"checked
    post_URL_setting_tip = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div[1]/form/div[2]')  # 社群設定>URL評論tip
    save_btn = (By.XPATH, '//div[@class = "flex justify-end"]//span[text() = "储存"]')  # 保存
    save_confirm_btn = (By.XPATH, '//div[@class = "el-popconfirm__action"]//span[text() = "确定"]')  # 二次確認

class SocialManagementPage(BasePage):

    def into_media_audit_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.media_audit, '媒体审核', first_enter)

    def into_auto_audit_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.auto_audit, '自动审核', first_enter)

    def into_block_words_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.block_words, '屏蔽字词', first_enter)

    def into_impeach_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.impeach, '检举内容', first_enter)

    def into_post_data_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.post_data, '贴文数据', first_enter)

    def into_creator_data_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.creator_data, '创作者数据', first_enter)

    def into_social_setting_page(self, first_enter=False):
        self._into_sub_social_management_page(SocialManagementPageLocator.social_setting, '社群设定', first_enter)

    def _into_sub_social_management_page(self, page_locator, page_title, first_enter=False):

        self.click(SocialManagementPageLocator.social_management)
        if not self.is_element_finded(page_locator):
            self.click(SocialManagementPageLocator.social_management)
        self.click(page_locator)
        self.wait_loading_finish()

        assert self.get_text(SocialManagementPageLocator.page_title) == page_title, f'未成功進入{page_title}頁'
        if first_enter:
            assert self.is_element_finded(SocialManagementPageLocator.result_empty), '進入頁面預設不顯示列表'

    def check_post_viewing_permission(self, user_id, privacy_index, audit_page='媒体审核'):
        assert self.get_text(SocialManagementPageLocator.page_title) == audit_page, f"未在{audit_page}頁面"
        self.refresh_browser()
        self.type(SocialManagementPageLocator.member_ID, user_id)
        self.click(SocialManagementPageLocator.search_btn)

        viewing_permission_text = self.get_text(SocialManagementPageLocator.data_media_audit_viewing_permissions)
        expected_viewing_permission = {0: '所有人', 1: '互关', 2: '粉丝', 3: '仅自己'}[privacy_index]
        assert viewing_permission_text == expected_viewing_permission, f'預期: {expected_viewing_permission}, 實際: {viewing_permission_text}'  # 觀看權限

    def search_audit_result(self, user_id, instructions, user_audit_type=0, audit_page='媒体审核'):
        assert self.get_text(SocialManagementPageLocator.page_title) == audit_page, f"未在{audit_page}頁面"
        self.type(SocialManagementPageLocator.member_ID, user_id)
        self.click(SocialManagementPageLocator.search_btn)

        # 驗證媒體審核結果
        assert self.get_text(SocialManagementPageLocator.data_media_audit_user_ID) == user_id  # 會員帳號
        current_description = self.get_text(SocialManagementPageLocator.data_media_audit_media_instruction)
        assert current_description == instructions, f'預期:{instructions}, 實際:{current_description}'  # 媒體說明

        status_text = self.get_text(SocialManagementPageLocator.data_media_audit_audit_status)
        expected_status = {0: '待审核', 1: '已通过', 2: '已拒绝'}[user_audit_type]
        assert status_text == expected_status, f'預期: {expected_status}, 實際: {status_text}'  # 審查狀態

    def set_audit_privacy(self, user_id, audit_type=0):
        audit_types = {
            1: ('白名单', SocialManagementPageLocator.data_auto_audit_operate_white_btn),
            2: ('黑名单', SocialManagementPageLocator.data_auto_audit_operate_black_btn),
            0: ('一般会员', SocialManagementPageLocator.data_auto_audit_operate_normal_btn)
        }

        if self.get_text(SocialManagementPageLocator.page_title) == '自动审核':
            self.type(SocialManagementPageLocator.member_ID, user_id)
            self.click(SocialManagementPageLocator.search_btn)
            self.wait_loading_finish()

            expected_type, operate_btn = audit_types.get(audit_type, ('一般会员', SocialManagementPageLocator.data_auto_audit_operate_normal_btn))
            if self.is_element_finded(operate_btn):
                self.click(operate_btn)
                self.click(
                    SocialManagementPageLocator.confirm_btn if audit_type != 2 else SocialManagementPageLocator.confirm_black_btn)
                self.wait_loading_finish()

            assert self.get_text(SocialManagementPageLocator.data_auto_audit_user_ID) == user_id, f'會員暱稱錯誤'
            assert self.get_text(
                SocialManagementPageLocator.data_auto_audit_type) == expected_type, f'會員自動審核類型錯誤'

            # 確認其他按鈕存在
            other_buttons = {
                '白名单': SocialManagementPageLocator.data_auto_audit_operate_black_btn,
                '黑名单': SocialManagementPageLocator.data_auto_audit_operate_white_btn,
                '一般会员': SocialManagementPageLocator.data_auto_audit_operate_white_btn
            }
            assert self.is_element_finded(other_buttons[expected_type]), f'未看到操作鍵'

    def add_block_words(self, block_words):
        self.click(SocialManagementPageLocator.add_block_words_btn)
        self.wait_loading_finish()
        # 確認跳出新增屏蔽字詞彈窗
        assert self.get_text(SocialManagementPageLocator.add_block_words_dialog_title) == '新增屏蔽字词'
        self.type(SocialManagementPageLocator.add_block_words, block_words)
        self.click(SocialManagementPageLocator.submit_btn)

        # 確認列表第一則為稍早新增的屏蔽字詞
        assert self.get_text(SocialManagementPageLocator.data_block_words) == block_words, '屏蔽字詞未新增成功'

    def delete_block_words(self, block_words):
        self.type(SocialManagementPageLocator.search_block_words, block_words)
        self.click(SocialManagementPageLocator.search_block_words_btn)

        # 確認列表第一則為稍早新增的屏蔽字詞
        assert self.get_text(SocialManagementPageLocator.data_block_words) == block_words
        self.click(SocialManagementPageLocator.delete_btn)
        self.click(SocialManagementPageLocator.confirm_btn)
        self.wait_loading_finish()

        # 確認屏蔽字詞已被成功刪除
        self.click(SocialManagementPageLocator.search_block_words_btn)
        self.wait_loading_finish()
        assert self.is_element_finded(SocialManagementPageLocator.result_empty), '暫無數據'

    # 搜尋檢舉貼文
    def search_impeach_content(self, informant_id, defendant_id, request_reason):
        self.type(SocialManagementPageLocator.input_informant_ID, informant_id)
        self.type(SocialManagementPageLocator.input_defendant_ID, defendant_id)
        self.click(SocialManagementPageLocator.search_impeach_btn)
        self.wait_loading_finish()

        # 確認檢舉內容列表
        _data_first_informant_id = self.get_text(SocialManagementPageLocator.data_first_informant_id)
        _data_defendant_id = self.get_text(SocialManagementPageLocator.data_defendant_id)
        _data_impeach_status = self.get_text(SocialManagementPageLocator.data_impeach_status)
        _data_display_status = self.get_text(SocialManagementPageLocator.data_display_status)
        assert _data_first_informant_id == informant_id, '檢舉人錯誤'
        assert _data_defendant_id == defendant_id, '被檢舉人錯誤'
        assert _data_impeach_status == '待处理', '檢舉狀態錯誤'
        assert _data_display_status == '正常', '前台顯示狀態錯誤'

        # 檢舉人數 > 確認檢舉內容
        self.click(SocialManagementPageLocator.data_informant_counts)
        self.wait_loading_finish()
        _detail_impeach_behavior = self.get_text(SocialManagementPageLocator.data_impeach_detail_behavior)
        _detail_impeach_informant_id = self.get_text(SocialManagementPageLocator.data_impeach_detail_informant_id)
        _detail_impeach_reason = self.get_text(SocialManagementPageLocator.data_impeach_detail_reason)
        assert _detail_impeach_behavior == '检举', '行為顯示錯誤'
        assert _detail_impeach_informant_id == informant_id, '檢舉人錯誤'
        assert _detail_impeach_reason == request_reason, '檢舉理由錯誤'
        self.click(SocialManagementPageLocator.data_impeach_detail_close_btn)

    # approve檢舉貼文request
    def impeach_request_approve(self):
        self.click(SocialManagementPageLocator.data_approve_btn)
        self.click(SocialManagementPageLocator.impeach_confirm_btn)
        self.wait_loading_finish()
        _data_impeach_status = self.get_text(SocialManagementPageLocator.data_impeach_status)
        _data_display_status = self.get_text(SocialManagementPageLocator.data_display_status)
        assert _data_impeach_status == '已下架', '檢舉狀態錯誤'
        assert _data_display_status == '隐藏', '前台顯示狀態錯誤'

    def check_post_view_and_viewers(self, poster_id, post_descriptions):
        self.into_post_data_page()
        self.type(SocialManagementPageLocator.input_poster_ID, poster_id)
        self.click(SocialManagementPageLocator.search_post_btn)
        self.wait_loading_finish()
        _data_poster_id = self.get_text(SocialManagementPageLocator.data_poster_id)
        _data_post_descriptions = self.get_text(SocialManagementPageLocator.data_post_descriptions)
        _data_view_counts = self.get_text(SocialManagementPageLocator.data_view_counts)
        _data_viewer_counts = self.get_text(SocialManagementPageLocator.data_viewer_counts)
        assert _data_poster_id == poster_id
        assert _data_post_descriptions == post_descriptions
        return _data_view_counts, _data_viewer_counts

    def check_creator_view_and_viewers(self, creator_id):
        self.into_creator_data_page()
        self.type(SocialManagementPageLocator.input_creator_ID, creator_id)
        self.click(SocialManagementPageLocator.search_creator_btn)
        self.wait_loading_finish()
        _data_creator_id = self.get_text(SocialManagementPageLocator.data_creator_id)
        _data_creator_view_counts = self.get_text(SocialManagementPageLocator.data_creator_view_counts)
        _data_creator_viewer_counts = self.get_text(SocialManagementPageLocator.data_creator_viewer_counts)
        return _data_creator_view_counts, _data_creator_viewer_counts

    def enable_post_url_setting(self):
        if not self.is_element_finded(SocialManagementPageLocator.page_title) or not self.get_text(SocialManagementPageLocator.page_title) == '社群设定':
            self.into_social_setting_page()
        self.click(SocialManagementPageLocator.set_post_URL_on)
        self.click(SocialManagementPageLocator.save_btn)
        self.click(SocialManagementPageLocator.save_confirm_btn)
        assert self.is_element_finded(SocialManagementPageLocator.post_URL_on_checked), '貼文評論超連結選項未開啟'
        assert not self.is_element_finded(SocialManagementPageLocator.post_URL_off_checked), '貼文評論超連結選項未開啟'

    def disable_post_url_setting(self):
        if not self.is_element_finded(SocialManagementPageLocator.page_title) or not self.get_text(SocialManagementPageLocator.page_title) == '社群设定':
            self.into_social_setting_page()
        self.click(SocialManagementPageLocator.set_post_URL_off)
        self.click(SocialManagementPageLocator.save_btn)
        self.click(SocialManagementPageLocator.save_confirm_btn)
        assert self.is_element_finded(SocialManagementPageLocator.post_URL_off_checked), '貼文評論超連結選項未關閉'
        assert not self.is_element_finded(SocialManagementPageLocator.post_URL_on_checked), '貼文評論超連結選項未關閉'