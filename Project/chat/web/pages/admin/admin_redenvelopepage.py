import random
import re
from time import sleep
import pandas as pd
import pyautogui
import win32clipboard
from selenium.webdriver.common.by import By
import os, sys, datetime
from Project.chat.web.pages.admin.admin_basepage import BasePage
import common.utils.globalvar as gl

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)

class RedEnvelopePageLocator:
    # 通用
    page_title = (By.XPATH, '//div[@class="page-title"]')
    search_btn = (By.XPATH, "//span[text()='搜寻']")
    redenvelope_type = (By.XPATH, '//label[text()="红包种类"]/..//span[@class="el-input__suffix-inner"]')

    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

    # 搜尋欄位
    search_start_time = (By.XPATH, '//input[@placeholder="开始日期"]')
    search_end_time = (By.XPATH, '//input[@placeholder="结束日期"]')
    search_initiate_member = (By.XPATH, '//input[@placeholder="请输入ID"]')
    
    redenvelope_type_normal = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="发红包"]')
    redenvelope_type_lucky = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="手气红包"]')

    add_redenvelope_btn = (By.XPATH, "//span[text()='新增红包']")

    # 資料欄位
    data_drop_menu = (By.XPATH, "//tr[1]//td[1]//i")
    data_redenvelope_type = (By.XPATH, "//tr[1]//td[1]")
    data_start_time = (By.XPATH, "//tr[1]//td[2]")
    data_end_time = (By.XPATH, "//tr[1]//td[3]")
    data_red_package = (By.XPATH, "//tr[1]//td[4]")
    data_red_amount = (By.XPATH, "//tr[1]//td[5]")
    data_red_type = (By.XPATH, "//tr[1]//td[6]")
    data_chatroom = (By.XPATH, "//tr[1]//td[7]")
    data_initiate_member = (By.XPATH, "//tr[1]//td[8]")
    data_detail = (By.XPATH, "//tr[1]//span[text()='详情']")  # 列表第一行
    data_copy = (By.XPATH, "//tr[1]//span[text()='复制']")  # 列表第一行
    data_edit = (By.XPATH, "//tr[1]//span[text()='编辑']")  # 列表第一行
    data_cancel =(By.XPATH, "//tr[1]//span[text()='取消']")  # 列表第一行

    # 红包详情
    detail_search_ID = (By.XPATH, '//input[@placeholder="输入ID"]')
    detail_search_name = (By.XPATH, '//input[@placeholder="输入昵称"]')
    #redenvelope_type_ = (By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='未领取']") # 前端做好領取紅包後更新
    #redenvelope_type_done = (By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='已领取']")
    detail_red_type = (By.XPATH, '(//div[@class="section"]//div[3]//span[@class="mr-5"])[1]')
    detail_red_total_amount = (By.XPATH, '(//div[@class="section"]//div[3]//span[@class="mr-5"])[2]')
    detail_red_package = (By.XPATH, '(//div[@class="section"]//div[3]//span[@class="mr-5"])[3]')
    detail_red_type_info = (By.XPATH, '(//div[@class="section"]//span[@class="mr-5"])[1]')  # 红包种类:xxxx
    detail_initiate_member = (By.XPATH, '(//div[@class="section"]//span)[last()]')

    detail_list_ID = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    detail_list_name = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    detail_list_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    detail_list_type = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")
    detail_type_sort_caret_descending = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div[2]/table/thead/tr/th[4]/div/span/i[2]')
    detail_list_award = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")
    detail_list_point = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")
    detail_total_line = (By.XPATH, "//span[@class='el-pagination__total']")

    detail_back_btn = (By.XPATH, "//span[text()=' 返回 ']")

    # 新增紅包
    add_initiate_ID = (By.XPATH, '//label[text()="请选择发布帐号"]/..//input')
    add_initiate_ID_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot01"]')
    add_chatroom = (By.XPATH, '//label[text()="请选择发布聊天室"]/..//input[@placeholder="请选择"]')
    # add_chatroom_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="QA_bot_only"]')

    add_red_type = (By.XPATH, '//label[text()="红包种类"]/..//input[@placeholder="请选择"]')
    add_red_type_arrow = (By.XPATH, '//label[text()="红包种类"]/..//span[@class="el-input__suffix"]')
    add_red_start_time = (By.XPATH, '//label[text()="开始时间"]/..//input[@placeholder="开始日期"]')
    add_red_end_time = (By.XPATH, '//label[text()="开始时间"]/..//input[@placeholder="结束日期"]')
    add_red_confirm_time = (By.XPATH, '//span[text()="确定"]')
    add_red_package = (By.XPATH, '//label[text()="设定红包数量"]/..//input[@placeholder="请输入数量"]')
    add_red_amount = (By.XPATH, '//label[text()="设定红包金额"]/..//input[@placeholder="请输入金额"]')
    add_red_select_member = (By.XPATH, '//label[text()="请选择指定名单"]/..//span[@class="el-input__suffix-inner"]')
    add_red_select_all = (By.XPATH, '//span[text()="全选"]')
    add_auto_grad_member = (By.XPATH, '//label[text()="请选择自动领取"]/..//span[@class="el-input__suffix-inner"]')
    add_red_select_member_select = (By.XPATH, '(//div[@aria-hidden="false"]//li[@class="el-select-dropdown__item"])[1]')
    add_red_select_member_select_first = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot02"]')
    add_red_remind = (By.XPATH, '//p[text()=" 确定执行？"]')

    add_red_add_btn = (By.XPATH, '//span[text()="新增"]')
    add_red_confirm_btn = (By.XPATH, '//div[@class="el-popconfirm"]//span[text()="确定"]')
    # '//div[@class="el-popconfirm"]//span[text()="确定"]'
    add_envelope_fail_toast = (By.XPATH, '//div[@class="el-message el-message--error"]')  # 新增紅包失敗toast
    add_envelope_pass_toast = (By.XPATH, '//div[@class="el-message el-message--success"]')  # 新增紅包成功toast

    add_red_lucky = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="拼手气红包"]')

    # 手氣紅包
    luck_package = (By.XPATH, '//label[text()="包数"]/..//input[@placeholder="请输入包数"]')
    luck_detail_title = (By.XPATH, "//div[@aria-label='明细']//span[text()='明细']")
    luck_detail_expand = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[3]/div/div[5]/div/div[2]/div[2]/div')
    luck_award_high = (By.XPATH, '//label[text()="最高"]/..//input[@placeholder="请输入最高"]')
    luck_award_1_member = (By.XPATH, "//label[text()='奖项 1']/..//label[text()='成员名单']/..//i")
    luck_award_2_member = (By.XPATH, "//label[text()='奖项 2']/..//label[text()='成员名单']/..//i")
    luck_award_3_member = (By.XPATH, "//label[text()='奖项 3']/..//label[text()='成员名单']/..//i")
    luck_award_1_member_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot02"]')
    luck_award_2_member_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot03"]')
    luck_award_3_member_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot04"]')
    luck_award_1 = (By.XPATH, "//div[@class='my-3 px-2 mt-0'][1]//input[@placeholder='请输入金额']")
    luck_award_2 = (By.XPATH, "//div[@class='my-3 px-2'][1]//input[@placeholder='请输入金额']")
    luck_award_3 = (By.XPATH, "//div[@class='my-3 px-2 mb-0'][1]//input[@placeholder='请输入金额']")
    luck_statement_total_amount = (By.XPATH, "(//p[text()='总计']/../p[@class='text-container totals'])[2]")

    luck_add_award = (By.XPATH, "//span[text()='设置下一奖项']")
    luck_now_initial = (By.XPATH, "//span[text()='即刻发布']/..//span[@class='el-checkbox__inner']")
    luck_select_all = (By.XPATH, "//span[text()='全选']")
    luck_delete_btn = (By.XPATH, "//span[text()='删除奖项']")
    luck_award_calculate = (By.XPATH, "//span[text()='奖项计算']")
    luck_award_calculate_results = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div')
    luck_detail = (By.XPATH, "//span[text()='明细']")

    luck_single_picture = (By.XPATH, '//label[text()="单图"]/..//span[@class="el-radio__input"]')
    luck_detail_save = (By.XPATH, "//span[text()='储存']")
    luck_detail_close = (By.XPATH, "(//span[text()='关闭'])[2]")

    #批量上傳
    bulk_upload_tab = (By.XPATH, "(//div[@class='el-tabs__nav-scroll']/..//div[contains(@class,'el-tabs__item is-top')])[last()]")
    red_envelope_data_type_fixed_amount_radio_btn = (By.XPATH, "//span[text()='固定金额']")
    red_envelope_data_type_random_amount_radio_btn = (By.XPATH, "//span[text()='随机金额']")
    file_import_btn = (By.XPATH, "//span[text()='档案汇入']")
    preview_window_title = (By.XPATH, '//div[@class="el-dialog__header"]')
    preview_window_member_id_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    preview_window_confirm_btn = (By.XPATH, '//*[@id="pane-batch"]/div/div/div[3]/div/button[2]')
    upload_filename = (By.XPATH, '//*[@id="pane-batch"]/form/div[4]/span')
    # ------固定金額預覽彈窗欄位----------
    preview_window_fix_amount_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    preview_window_fix_winning_message_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    # ------隨機金額預覽彈窗欄位----------
    preview_window_random_min_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    preview_window_random_max_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    preview_window_random_winning_message_first = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")

    @staticmethod
    def add_chatroom_select(brand):
        text = "QA bot only" if brand.lower() == "mingpin" else "QA_bot_only"
        return By.XPATH, f'//div[@aria-hidden="false"]//span[text()="{text}"]'

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


class RedEnvelopePage(BasePage):

    def add_redenvelope(self):
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            self.click(RedEnvelopePageLocator.add_redenvelope_btn)
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.page_title) == '新增红包', f'進入新增紅包頁面失敗'
            self.click(RedEnvelopePageLocator.add_red_start_time)
            start_time = (datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
            self.type(RedEnvelopePageLocator.add_red_start_time, start_time)
            self.click(RedEnvelopePageLocator.add_red_end_time)
            end_time = (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
            self.type(RedEnvelopePageLocator.add_red_end_time, end_time)
            self.click(RedEnvelopePageLocator.add_auto_grad_member)
            self.click(RedEnvelopePageLocator.add_initiate_ID)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_initiate_ID_select)
            self.click(RedEnvelopePageLocator.add_chatroom)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
            self.click(RedEnvelopePageLocator.add_red_package)
            self.type(RedEnvelopePageLocator.add_red_package, '1')
            self.click(RedEnvelopePageLocator.add_red_amount)
            self.type(RedEnvelopePageLocator.add_red_amount, '1')
            self.sleep(1)
            self.click(RedEnvelopePageLocator.add_red_select_member)
            self.click(RedEnvelopePageLocator.add_red_select_member_select_first)
            self.click(RedEnvelopePageLocator.add_red_add_btn)
            self.wait_loading_finish()
            if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                self.click(RedEnvelopePageLocator.add_red_confirm_btn)

    def add_random_amount_red_envelope(self):
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            self.click(RedEnvelopePageLocator.add_redenvelope_btn)
            sleep(1)
            self.click(RedEnvelopePageLocator.add_red_start_time)
            start_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
            self.type(RedEnvelopePageLocator.add_red_start_time, start_time)
            self.click(RedEnvelopePageLocator.add_auto_grad_member)
            self.click(RedEnvelopePageLocator.add_initiate_ID)
            sleep(1)
            self.click(RedEnvelopePageLocator.add_initiate_ID_select)
            self.click(RedEnvelopePageLocator.add_chatroom)
            sleep(1)
            self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
            self.click(RedEnvelopePageLocator.add_red_package)
            self.type(RedEnvelopePageLocator.add_red_package, str(random.randint(10,20)))
            self.click(RedEnvelopePageLocator.add_red_amount)
            self.type(RedEnvelopePageLocator.add_red_amount, str(random.randint(10,100)))
            self.sleep(1)
            self.click(RedEnvelopePageLocator.add_red_select_all)
            self.click(RedEnvelopePageLocator.add_red_add_btn)
            sleep(1)
            if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                self.click(RedEnvelopePageLocator.add_red_confirm_btn)
        sleep(60)
    # def add_bulk_upload_luck_red_envelope(self):

    def random_red_envelope_data_type_bulk_upload(self):
        self.wait_loading_finish()
        self.click(RedEnvelopePageLocator.add_redenvelope_btn)  # 新增紅包鍵
        sleep(2)
        self.click(RedEnvelopePageLocator.redenvelope_type)  # 紅包種類
        self.click(RedEnvelopePageLocator.add_red_lucky)  # 拚手氣紅包
        self.click(RedEnvelopePageLocator.add_chatroom)  # 選聊天室
        self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))  # 指定QA_bot_only
        self.click(RedEnvelopePageLocator.add_initiate_ID)  # 發布帳號
        self.click(RedEnvelopePageLocator.add_initiate_ID_select)  # 指定gubot01
        sleep(0.5)
        self.click(RedEnvelopePageLocator.bulk_upload_tab)

        random_choice_type = random.randint(1, 2)
        # ===================== 選擇紅包資料類別 ===========================
        if random_choice_type == 1:  # 點固定金額 radio button
            self.click(RedEnvelopePageLocator.red_envelope_data_type_fixed_amount_radio_btn)
        else:  # 點隨機金額 radio button
            self.click(RedEnvelopePageLocator.red_envelope_data_type_random_amount_radio_btn)
        # ===================== 獲取excel檔案路徑 ==============================
        folder_path = f'{DIR_NAME}\\test_medias\\red_envelope_bulk_upload'
        mapping = {1: 'fix_amount', 2: "random_amount"}
        select = mapping[random_choice_type]
        filename = ''
        for f in os.listdir(folder_path):
            if select in f and f.endswith(".xlsx"):
                filename = f
                break
        file_path = os.path.join(folder_path,filename)
        # ===================== 讀取excel內資料 =========================
        df = pd.read_excel(file_path)
        excel_amount_first = ''
        excel_amount_min_first = ''
        excel_amount_max_first = ''
        if random_choice_type == 1:
            excel_member_id_first = df.loc[0, "member_id"]
            excel_amount_first = df.loc[0, "amount"]
            excel_winning_message_first = df.loc[0, "winning_message"]
        else:
            excel_member_id_first = df.loc[0, "member_id"]
            excel_amount_min_first = df.loc[0, "minimum"]
            excel_amount_max_first = df.loc[0, "maximum"]
            excel_winning_message_first = df.loc[0, "winning_message"]
        # ===================== excel檔上傳 =============================
        self.click(RedEnvelopePageLocator.file_import_btn)
        sleep(1)
        copy_to_clipboard(file_path)
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        sleep(3)
        # ===================== 確認預覽視窗 =============================
        preview_window_member_id_first = self.get_text(RedEnvelopePageLocator.preview_window_member_id_first)
        assert excel_member_id_first == preview_window_member_id_first

        if random_choice_type == 1:
            preview_window_amount_first = self.get_text(RedEnvelopePageLocator.preview_window_fix_amount_first)
            preview_window_winning_message_first = self.get_text(RedEnvelopePageLocator.preview_window_fix_winning_message_first)
            assert str(excel_amount_first) == preview_window_amount_first
            assert str(excel_winning_message_first) == preview_window_winning_message_first
        else:
            preview_window_random_min_first = self.get_text(RedEnvelopePageLocator.preview_window_random_min_first)
            preview_window_random_max_first = self.get_text(RedEnvelopePageLocator.preview_window_random_max_first)
            preview_window_random_winning_message_first = self.get_text(RedEnvelopePageLocator.preview_window_random_winning_message_first)
            assert str(excel_amount_min_first) == preview_window_random_min_first
            assert str(excel_amount_max_first) == preview_window_random_max_first
            assert str(excel_winning_message_first) == preview_window_random_winning_message_first
        # ===================== 確認並關閉預覽視窗 =============================
        self.click(RedEnvelopePageLocator.preview_window_confirm_btn)
        sleep(1)
        upload_filename = self.get_text(RedEnvelopePageLocator.upload_filename)
        assert upload_filename == filename
        # ==================================================================
        self.click(RedEnvelopePageLocator.luck_now_initial)
        self.click(RedEnvelopePageLocator.luck_award_calculate)
        sleep(0.5)
        result_text = self.get_text(RedEnvelopePageLocator.luck_award_calculate_results)
        total_cost = re.search(r"金额\s*([0-9]+(?:\.[0-9]+)?)", result_text).group(1)

        if random_choice_type == 1:
            assert float(total_cost) == float(excel_amount_first)
        else:
            assert float(excel_amount_min_first) <= float(total_cost) <= float(excel_amount_max_first)
        self.click(RedEnvelopePageLocator.add_red_add_btn)
        sleep(1)
        if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
            self.click(RedEnvelopePageLocator.add_red_confirm_btn)
        sleep(60)
        return str(float(total_cost))

    def add_random_amount_luck_red_envelope(self):
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            self.click(RedEnvelopePageLocator.add_redenvelope_btn)
            sleep(1)
            self.click(RedEnvelopePageLocator.redenvelope_type)
            sleep(1)
            self.click(RedEnvelopePageLocator.add_red_lucky)
            sleep(1)
            if self.is_element_finded(RedEnvelopePageLocator.luck_delete_btn):
                self.click(RedEnvelopePageLocator.add_chatroom)
                sleep(1)
                self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
                self.click(RedEnvelopePageLocator.add_initiate_ID)
                sleep(1)
                self.click(RedEnvelopePageLocator.add_initiate_ID_select)
                self.click(RedEnvelopePageLocator.add_red_select_all)
                self.type(RedEnvelopePageLocator.luck_award_high, str(random.randint(10,100)))
                self.click(RedEnvelopePageLocator.luck_now_initial)
                self.click(RedEnvelopePageLocator.luck_award_calculate)
                sleep(1)
                self.click(RedEnvelopePageLocator.luck_single_picture)
                self.click(RedEnvelopePageLocator.add_red_add_btn)
                sleep(1)
                if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                    self.click(RedEnvelopePageLocator.add_red_confirm_btn)
        sleep(60)

    def add_red_envelope_for_auto_grad(self):
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            self.click(RedEnvelopePageLocator.add_redenvelope_btn)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_red_start_time)
            start_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")
            self.type(RedEnvelopePageLocator.add_red_start_time, start_time)
            self.click(RedEnvelopePageLocator.add_auto_grad_member)
            self.click(RedEnvelopePageLocator.add_initiate_ID)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_initiate_ID_select)
            self.click(RedEnvelopePageLocator.add_chatroom)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
            self.click(RedEnvelopePageLocator.add_red_package)
            self.type(RedEnvelopePageLocator.add_red_package, '1')
            self.click(RedEnvelopePageLocator.add_red_amount)
            self.type(RedEnvelopePageLocator.add_red_amount, '1')
            self.sleep(1)
            self.click(RedEnvelopePageLocator.add_red_select_all)
            self.click(RedEnvelopePageLocator.add_auto_grad_member)  # 自動領取下拉選單
            self.click(RedEnvelopePageLocator.add_red_select_member_select_first)  # 設定自動領取人員為gubot02
            self.click(RedEnvelopePageLocator.add_red_add_btn)
            self.wait_loading_finish()
            if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                self.click(RedEnvelopePageLocator.add_red_confirm_btn)

    def add_luck_red_envelope_for_auto_grad(self):
        result_text = ''
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            add_envelope_success_flag = False
            while add_envelope_success_flag is False:
                self.click(RedEnvelopePageLocator.add_redenvelope_btn)
                self.wait_loading_finish()
                self.click(RedEnvelopePageLocator.redenvelope_type)
                self.wait_loading_finish()
                self.click(RedEnvelopePageLocator.add_red_lucky)
                self.wait_loading_finish()
                if self.is_element_finded(RedEnvelopePageLocator.luck_delete_btn):
                    self.click(RedEnvelopePageLocator.add_chatroom)
                    self.wait_loading_finish()
                    self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
                    self.click(RedEnvelopePageLocator.add_initiate_ID)
                    self.wait_loading_finish()
                    self.click(RedEnvelopePageLocator.add_initiate_ID_select)
                    self.click(RedEnvelopePageLocator.add_red_select_all)
                    self.type(RedEnvelopePageLocator.luck_award_high, '1')
                    self.click(RedEnvelopePageLocator.add_auto_grad_member)  # 自動領取下拉選單
                    self.click(RedEnvelopePageLocator.add_red_select_member_select)  # 設定自動領取人員為gubot02
                    self.click(RedEnvelopePageLocator.luck_award_high)
                    self.click(RedEnvelopePageLocator.luck_now_initial)
                    self.click(RedEnvelopePageLocator.luck_award_calculate)
                    self.wait_loading_finish()
                    result_text = self.get_text(RedEnvelopePageLocator.luck_award_calculate_results)

                    self.click(RedEnvelopePageLocator.luck_single_picture)
                    self.click(RedEnvelopePageLocator.add_red_add_btn)

                    if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                        self.click(RedEnvelopePageLocator.add_red_confirm_btn)

                    sleep(3)
                    if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn):
                        add_envelope_success_flag = True
                    else:
                        self.refresh_browser()
                        self.wait_loading_finish()
        total_cost = re.search(r"金额\s*([0-9]+(?:\.[0-9]+)?)", result_text).group(1)
        # total_cost = re.search(r"金額 (\d+\.\d+)", result_text).group(1)
        # total_cost_format = str(total_cost).rstrip('0').rstrip('.')
        return str(float(total_cost))

    def redenvelope_detail(self, wait_time_seconds):
        self.sleep(wait_time_seconds)
        self.refresh_browser()
        self.wait_loading_finish()
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.click(RedEnvelopePageLocator.search_start_time)
        self.type(RedEnvelopePageLocator.search_start_time, time)
        self.click(RedEnvelopePageLocator.search_end_time)
        self.type(RedEnvelopePageLocator.search_end_time, time)
        self.click(RedEnvelopePageLocator.redenvelope_type)
        self.click(RedEnvelopePageLocator.redenvelope_type_normal)
        self.click(RedEnvelopePageLocator.search_initiate_member)
        self.type(RedEnvelopePageLocator.search_initiate_member, 'gubot01')
        self.click(RedEnvelopePageLocator.search_btn)    
        if self.is_element_finded(RedEnvelopePageLocator.data_detail) is True:
            self.click(RedEnvelopePageLocator.data_detail)
            self.switch_last_page()
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.detail_red_type) == '红包种类:发红包', f'紅包種類顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_red_total_amount) == '红包总额:1', f'總額顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_red_package) == '红包总数:1', f'總數顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_initiate_member) == '发包者:gubot01', f'發包者顯示錯誤'
            self.click(RedEnvelopePageLocator.detail_search_ID)
            self.type(RedEnvelopePageLocator.detail_search_ID, 'gubot02')
            self.click(RedEnvelopePageLocator.detail_search_name)
            self.type(RedEnvelopePageLocator.detail_search_name, 'gubot02')
            self.click(RedEnvelopePageLocator.search_btn)
            assert self.get_text(RedEnvelopePageLocator.detail_list_ID) == 'gubot02', f'會員ID有誤'  # 未來補上時間
            assert self.get_text(RedEnvelopePageLocator.detail_list_name) == 'gubot02', f'會員暱稱有誤' 
            assert self.get_text(RedEnvelopePageLocator.detail_list_point) == '1', f'獲得積分有誤'
            assert self.get_text(RedEnvelopePageLocator.detail_total_line) == '共 1 条', f'條數有誤'

    def add_luck_redenvelope(self):
        self.wait_loading_finish()
        if self.is_element_finded(RedEnvelopePageLocator.add_redenvelope_btn) is True:
            self.click(RedEnvelopePageLocator.add_redenvelope_btn)
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.page_title) == '新增红包', f'進入新增紅包頁面失敗'
            self.click(RedEnvelopePageLocator.redenvelope_type)
            self.wait_loading_finish()
            self.click(RedEnvelopePageLocator.add_red_lucky)
            self.wait_loading_finish()
            if self.is_element_finded(RedEnvelopePageLocator.luck_delete_btn):
                self.click(RedEnvelopePageLocator.add_chatroom)
                self.wait_loading_finish()
                self.click(RedEnvelopePageLocator.add_chatroom_select(gl.get_value("BRAND")))
                self.click(RedEnvelopePageLocator.add_initiate_ID)
                self.wait_loading_finish()
                self.click(RedEnvelopePageLocator.add_initiate_ID_select)
                self.click(RedEnvelopePageLocator.luck_award_1_member)
                self.click(RedEnvelopePageLocator.luck_award_1_member_select)
                self.click(RedEnvelopePageLocator.luck_add_award)
                self.click(RedEnvelopePageLocator.luck_award_2_member)
                self.click(RedEnvelopePageLocator.luck_award_2_member_select)
                self.click(RedEnvelopePageLocator.luck_add_award)
                self.click(RedEnvelopePageLocator.luck_award_3_member)
                self.click(RedEnvelopePageLocator.luck_award_3_member_select)                
                self.click(RedEnvelopePageLocator.luck_now_initial)
                self.click(RedEnvelopePageLocator.luck_award_calculate)
                self.click(RedEnvelopePageLocator.luck_detail)
                self.wait_loading_finish()
                if self.is_element_finded(RedEnvelopePageLocator.luck_detail_title) is True:
                    self.click(RedEnvelopePageLocator.luck_detail_expand)
                    self.type(RedEnvelopePageLocator.luck_award_1, '0.1')
                    self.type(RedEnvelopePageLocator.luck_award_2, '0.1')
                    self.type(RedEnvelopePageLocator.luck_award_3, '0.1')
                    assert self.get_text(RedEnvelopePageLocator.luck_statement_total_amount) == '0.30', f'總計有誤'
                    self.click(RedEnvelopePageLocator.luck_detail_save)
                    self.click(RedEnvelopePageLocator.luck_detail_close)
                    self.click(RedEnvelopePageLocator.luck_single_picture)

                    self.click(RedEnvelopePageLocator.luck_now_initial)
                    sleep(0.5)
                    self.click(RedEnvelopePageLocator.luck_now_initial)
                    self.click(RedEnvelopePageLocator.luck_award_calculate)

                    self.click(RedEnvelopePageLocator.add_red_add_btn)
                    self.wait_loading_finish()
                    if self.is_element_finded(RedEnvelopePageLocator.add_red_remind) is True:
                        self.click(RedEnvelopePageLocator.add_red_confirm_btn)

    def luck_red_envelope_detail(self, wait_time_second):
        self.sleep(wait_time_second)
        self.refresh_browser()
        self.wait_loading_finish()
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.click(RedEnvelopePageLocator.search_start_time)
        self.type(RedEnvelopePageLocator.search_start_time, time)
        self.click(RedEnvelopePageLocator.search_end_time)
        self.type(RedEnvelopePageLocator.search_end_time, time)
        self.click(RedEnvelopePageLocator.redenvelope_type)
        self.click(RedEnvelopePageLocator.redenvelope_type_lucky)
        self.click(RedEnvelopePageLocator.search_initiate_member)
        self.type(RedEnvelopePageLocator.search_initiate_member, 'gubot01')
        self.click(RedEnvelopePageLocator.search_btn)    
        if self.is_element_finded(RedEnvelopePageLocator.data_detail) is True:
            self.click(RedEnvelopePageLocator.data_detail)
            self.switch_last_page()
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.detail_total_line) == '共 3 条', f'條數有誤'
            assert self.get_text(RedEnvelopePageLocator.detail_red_type) == '红包种类:手气红包', f'紅包種類顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_red_total_amount) == '红包总额:0.3', f'總額顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_red_package) == '红包总数:3', f'總數顯示錯誤'
            assert self.get_text(RedEnvelopePageLocator.detail_initiate_member) == '发包者:gubot01', f'發包者顯示錯誤'
            self.click(RedEnvelopePageLocator.detail_search_ID)
            self.type(RedEnvelopePageLocator.detail_search_ID, 'gubot04')
            self.click(RedEnvelopePageLocator.detail_search_name)
            self.type(RedEnvelopePageLocator.detail_search_name, 'gubot04')
            self.click(RedEnvelopePageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.detail_list_ID) == 'gubot04', f'會員ID有誤'  # 未來補上 時間
            assert self.get_text(RedEnvelopePageLocator.detail_list_name) == 'gubot04', f'會員暱稱有誤' 
            assert self.get_text(RedEnvelopePageLocator.detail_list_award) == '3', f'獎項有誤'
            assert self.get_text(RedEnvelopePageLocator.detail_list_point) == '0.1', f'獲得積分有誤'
            self.click(RedEnvelopePageLocator.detail_search_ID)
            self.type(RedEnvelopePageLocator.detail_search_ID, 'gubot03')
            self.click(RedEnvelopePageLocator.detail_search_name)
            self.type(RedEnvelopePageLocator.detail_search_name, 'gubot03')
            self.click(RedEnvelopePageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.detail_list_ID) == 'gubot03', f'會員ID有誤'  # 未來補上 時間
            assert self.get_text(RedEnvelopePageLocator.detail_list_name) == 'gubot03', f'會員暱稱有誤' 
            assert self.get_text(RedEnvelopePageLocator.detail_list_award) == '2', f'獎項有誤'
            assert self.get_text(RedEnvelopePageLocator.detail_list_point) == '0.1', f'獲得積分有誤'
            self.click(RedEnvelopePageLocator.detail_search_ID)
            self.type(RedEnvelopePageLocator.detail_search_ID, 'gubot02')
            self.click(RedEnvelopePageLocator.detail_search_name)
            self.type(RedEnvelopePageLocator.detail_search_name, 'gubot02')
            self.click(RedEnvelopePageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(RedEnvelopePageLocator.detail_list_ID) == 'gubot02', f'會員ID有誤'  # 未來補上 時間
            assert self.get_text(RedEnvelopePageLocator.detail_list_name) == 'gubot02', f'會員暱稱有誤' 
            assert self.get_text(RedEnvelopePageLocator.detail_list_award) == '1', f'獎項有誤'
            assert self.get_text(RedEnvelopePageLocator.detail_list_point) == '0.1', f'獲得積分有誤'

    def red_envelope_detail_check(self, grab_account, grab_amount, grab_type, grab_time):
        self.type(RedEnvelopePageLocator.search_initiate_member, 'gubot01')
        self.click(RedEnvelopePageLocator.search_btn)
        self.wait_loading_finish()
        self.click(RedEnvelopePageLocator.data_detail)
        self.switch_last_page()
        self.wait_loading_finish()
        if grab_type == '拼手气红包':
            grab_type = '手气红包'
        # ======================== 紅包詳情頁搜尋目標人物 =====================
        self.type(RedEnvelopePageLocator.detail_search_ID,grab_account)
        self.click(RedEnvelopePageLocator.search_btn)
        # =================================================================
        aaa = self.get_text(RedEnvelopePageLocator.detail_list_ID)
        assert self.get_text(RedEnvelopePageLocator.detail_red_type_info) == f'红包种类:{grab_type}', f'紅包詳情頁種類錯誤'
        assert self.get_text(RedEnvelopePageLocator.detail_list_ID) == grab_account, f'搶紅包人員有誤, 預期{grab_account}, 實際:{self.get_text(RedEnvelopePageLocator.detail_list_ID)}'
        if grab_time is not None:
            assert self.get_text(RedEnvelopePageLocator.detail_list_time)[:-3].replace("/", "-") == grab_time.replace("/", "-"), f'搶紅包時間有誤'
        assert self.get_text(RedEnvelopePageLocator.detail_list_type) == '已领取', f'紅包領取狀態有誤'
        assert self.get_text(RedEnvelopePageLocator.detail_list_point) == grab_amount, f'獲得積分有誤'
