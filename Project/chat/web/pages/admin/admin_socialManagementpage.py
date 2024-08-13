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
    data_media_audit_audit_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")
    data_media_audit_update_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[8]")
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
    data_auto_audit_operate_black_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[6]//span[text()="黑名单"]')
    data_auto_audit_operate_white_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[6]//span[text()="白名单"]')
    data_auto_audit_operate_normal_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[6]//span[text()="一般会员"]')

class SocialManagementPage(BasePage):

    def into_media_audit_page(self):
        self.click(SocialManagementPageLocator.social_management)
        if not self.is_element_finded(SocialManagementPageLocator.media_audit):
            self.click(SocialManagementPageLocator.social_management)
        self.click(SocialManagementPageLocator.media_audit)
        self.wait_loading_finish()
        assert self.get_text(SocialManagementPageLocator.page_title) == '媒体审核', f'未成功進入媒體审核頁'
        assert self.is_element_finded(SocialManagementPageLocator.result_empty)  # 進入頁面預設不顯示列表

    def into_auto_audit_page(self):
        self.click(SocialManagementPageLocator.social_management)
        if not self.is_element_finded(SocialManagementPageLocator.auto_audit):
            self.click(SocialManagementPageLocator.social_management)
        self.click(SocialManagementPageLocator.auto_audit)
        self.wait_loading_finish()
        assert self.get_text(SocialManagementPageLocator.page_title) == '自动审核', f'未成功進入自动审核頁'
        assert self.is_element_finded(SocialManagementPageLocator.result_empty)  # 進入頁面預設不顯示列表

    def search_media_audit_result(self, user_id, instructions, user_audit_type=0):
        if self.get_text(SocialManagementPageLocator.page_title) == '媒体审核':
            self.type(SocialManagementPageLocator.member_ID, user_id)
            self.click(SocialManagementPageLocator.search_btn)
            # self.set_audit_privacy(user_id, user_audit_type)
            assert self.get_text(SocialManagementPageLocator.data_media_audit_user_ID) == user_id
            assert self.get_text(SocialManagementPageLocator.data_media_audit_media_instruction) == instructions
            if user_audit_type == 1:
                assert self.get_text(SocialManagementPageLocator.data_media_audit_audit_status) == '已通过'
            elif user_audit_type == 2:
                assert self.get_text(SocialManagementPageLocator.data_media_audit_audit_status) == '已拒绝'
            else:
                assert self.get_text(SocialManagementPageLocator.data_media_audit_audit_status) == '待审核'

    def set_audit_privacy(self, user_id, audit_type=0):
        if self.get_text(SocialManagementPageLocator.page_title) == '自动审核':
            self.type(SocialManagementPageLocator.member_ID, user_id)
            self.click(SocialManagementPageLocator.search_btn)

            if audit_type == 1:  # 白名單
                self.wait_loading_finish()
                if self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_white_btn):
                    self.click(SocialManagementPageLocator.data_auto_audit_operate_white_btn)
                    self.click(SocialManagementPageLocator.confirm_btn)
                    self.wait_loading_finish()

                assert self.get_text(SocialManagementPageLocator.data_auto_audit_user_ID) == user_id, f'會員暱稱錯誤'
                assert self.get_text(SocialManagementPageLocator.data_auto_audit_type) == '白名单', f'會員自動審核類型錯誤'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_black_btn), f'未看到_操作_黑名單鍵'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_normal_btn), f'未看到_操作_一般成員鍵'

            elif audit_type == 2:  # 黑名單
                self.wait_loading_finish()
                if self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_black_btn):
                    self.click(SocialManagementPageLocator.data_auto_audit_operate_black_btn)
                    self.click(SocialManagementPageLocator.confirm_black_btn)
                    self.wait_loading_finish()

                assert self.get_text(SocialManagementPageLocator.data_auto_audit_user_ID) == user_id, f'會員暱稱錯誤'
                assert self.get_text(SocialManagementPageLocator.data_auto_audit_type) == '黑名单', f'會員自動審核類型錯誤'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_white_btn), f'未看到_操作_白名單鍵'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_normal_btn), f'未看到_操作_一般成員鍵'

            else:  # 一般會員
                self.wait_loading_finish()
                if self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_normal_btn):
                    self.click(SocialManagementPageLocator.data_auto_audit_operate_normal_btn)
                    self.click(SocialManagementPageLocator.confirm_btn)
                    self.wait_loading_finish()

                assert self.get_text(SocialManagementPageLocator.data_auto_audit_user_ID) == user_id, f'會員暱稱錯誤'
                assert self.get_text(SocialManagementPageLocator.data_auto_audit_type) == '一般会员', f'會員自動審核類型錯誤'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_white_btn), f'未看到_操作_白名單鍵'
                assert self.is_element_finded(SocialManagementPageLocator.data_auto_audit_operate_black_btn), f'未看到_操作_黑名單鍵'



    def search_point_recode(self, condition):
        self.wait_loading_finish()
        assert self.get_text(WaterRecodePageLocator.page_title) == '积分使用纪录', f'頁面標題有誤'
        self.type(WaterRecodePageLocator.member_name, '積分測試')
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.click(WaterRecodePageLocator.search_start_time)
        self.type(WaterRecodePageLocator.search_start_time, time)
        self.click(WaterRecodePageLocator.search_end_time)
        self.type(WaterRecodePageLocator.search_end_time, time)
        self.click(WaterRecodePageLocator.use_type)
        sleep(0.5)
        if condition == 'success':
            self.click(WaterRecodePageLocator.exchange_success)
        elif condition == 'fail':
            self.click(WaterRecodePageLocator.exchange_fail)
        self.click(WaterRecodePageLocator.search_btn)

    def check_exchange_recode(self, condition):
        self.wait_loading_finish()
        assert self.get_text(WaterRecodePageLocator.data_member_name) == '積分測試', f'暱稱有誤'
        if condition == 'success':
            assert self.get_text(WaterRecodePageLocator.data_use_type) == '顺付出金', f'媒介有誤'
            assert self.get_text(WaterRecodePageLocator.data_point) == '-1', '積分有誤'
            # assert self.get_text(WaterRecodePageLocator.data_total_line) == '共 2 条', f'總數有誤'
            assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'狀態有誤'
        elif condition == 'fail':
            assert self.get_text(WaterRecodePageLocator.data_use_type) == '顺付返还', f'媒介有誤'
            assert self.get_text(WaterRecodePageLocator.data_point) == '1', '積分有誤'
            # assert self.get_text(WaterRecodePageLocator.data_total_line) == '共 1 条', f'總數有誤'
            assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'狀態有誤'

    def check_current_exchange_record(self, grab_account, grab_time, grab_amount, grab_type, source_group,
                                      total_remain_amount):
        self.wait_loading_finish()
        aaa = self.get_text(WaterRecodePageLocator.data_member_ID)
        assert self.get_text(WaterRecodePageLocator.data_member_ID) == grab_account, f'積分使用紀錄: 會員ID錯誤'
        if grab_time is not None:
            assert self.get_text(WaterRecodePageLocator.data_use_time)[:-3] == grab_time, f'積分使用紀錄: 使用時間錯誤'
        assert self.get_text(WaterRecodePageLocator.data_point) == grab_amount, f'積分使用紀錄: 使用積分錯誤'
        assert self.get_text(WaterRecodePageLocator.data_use_type) == grab_type, f'積分使用紀錄: 使用媒介錯誤'
        assert self.get_text(
            WaterRecodePageLocator.data_red_envelope_source) == source_group, f'積分使用紀錄: 紅包來源錯誤'
        assert self.get_text(
            WaterRecodePageLocator.data_remain_point) == total_remain_amount, f'積分使用紀錄: 剩餘積分錯誤'
        assert self.get_text(WaterRecodePageLocator.data_state) == '成功', f'積分使用紀錄: 狀態錯誤'
