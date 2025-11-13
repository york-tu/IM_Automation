import re
from time import sleep

from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage
import common.utils.globalvar as gl

class GroupsPageLocator:
    # 搜尋欄位
    group_id = (By.XPATH, '//input[@placeholder="请输入群组编号"]')
    group_name = (By.XPATH, '//input[@placeholder="请输入群组名称"]')
    invitation_code = (By.XPATH, '//input[@placeholder="请输入邀请码"]')

    group_search = (By.XPATH, '//span[text()="搜寻"]/..')
    group_add = (By.XPATH, '//span[text()="新增群组"]/..')

    operate_id = (By.XPATH, '//li[@class="el-select-dropdown__item"]/span[not (contains(text(),"条/页"))]')

    # -------------------- 搜尋結果欄位 --------------------
    result_empty = (By.XPATH, '//span[@class="el-table__empty-text"]')

    # -------------------- 群組編號欄位 -------------------- 
    result_group_id = (By.XPATH, '(//td[contains(@class,"el-table_1_column_1 ")])[1]')

    # -------------------- 名稱欄位 -------------------- 
    result_group_name = (By.XPATH, '(//td[contains(@class,"el-table_1_column_2")])[1]')

    # -------------------- 成員數欄位 -------------------- 
    result_group_member = (By.XPATH, '(//td[contains(@class,"el-table_1_column_4")])[1]')

    # -------------------- 黑名單欄位 -------------------- 
    result_group_black = (By.XPATH, '(//td[contains(@class,"el-table_1_column_6")])[1]')

    # -------------------- 建立時間欄位 -------------------- 
    result_group_create = (By.XPATH, '(//td[contains(@class,"el-table_1_column_7")])[1]')

    # -------------------- 修改時間欄位 --------------------
    result_group_update = (By.XPATH, '(//td[contains(@class,"el-table_1_column_8")])[1]')

    # -------------------- 成員權限欄位 -------------------- 
    result_group_rule = (By.XPATH, '(//td[contains(@class,"el-table_1_column_9")])[1]')

    # -------------------- 擁有者欄位 -------------------- 
    result_group_owner = (By.XPATH, '(//td[contains(@class,"el-table_1_column_10")])[1]')

    # -------------------- 管理員欄位 -------------------- 
    result_group_admin = (By.XPATH, '(//td[contains(@class,"el-table_1_column_11")])[1]')

    # -------------------- 狀態欄位 -------------------- 
    result_group_state = (By.XPATH, '(//td[contains(@class,"el-table_1_column_12")])[1]')

    # -------------------- 操作欄位 -------------------- 
    # button_delete = (By.XPATH, '//button[contains(@class,"button--danger")]/span[text()="删除"]')
    button_delete = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[13]/div/div/button[4]')

    delete_title = (By.XPATH, '//div[@aria-label="删除群组"]//span[@class="el-dialog__title"]')
    delete_group_name = (By.XPATH, '//span[@class="item-name"]')
    delete_select = (By.XPATH, '//span[@class="item-name"]/..//span[@class="el-input__suffix-inner"]')
    delete_popup_btn = (By.XPATH, '(//span[text()="删除"])[last()]')

    button_edit = (By.XPATH, '//button[contains(@class,"button--primary")]/span[text()="编辑"]')

    # -------------------- 新增群組 -------------------- 
    add_group_title = (By.XPATH, '//div[@class="setting-template-title"]')
    add_group_select = (By.XPATH, '//input[@placeholder="请选择建群帐号"]/..//span[@class="el-input__suffix-inner"]')
    add_group_name = (By.XPATH, '//input[@placeholder="请输入群组名称"]')

    add_group_member = (By.XPATH, '//input[@placeholder="输入会员帐号/昵称搜索"]')
    add_group_member_search_btn = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[6]/div/div[2]/div[1]/div/div/button')
    add_group_member_confirm_add_btn = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[6]/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/i')
    group_management = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/ul/li[3]/div')
    group_list = (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/ul/li[3]/ul/li[1]/a')
    group_stress_test_member_num_icon = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/div/span')
    operator_id_dropdown = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/input')
    operator_york = (By.XPATH, "//div[@class='el-input el-input--small el-input--suffix']//span[text()='york01]")
    group_addmember_btn = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[2]/button')

    # -------------------- 群組設定 --------------------
    set_history_on = (
    By.XPATH, '(//label[text()="新加入群組的成員，是否可查看歷史訊息"]/..//span[@class="el-radio__inner"])[1]')
    set_history_off = (
    By.XPATH, '(//label[text()="新加入群組的成員，是否可查看歷史訊息"]/..//span[@class="el-radio__inner"])[2]')
    set_build_on = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[1]')
    set_build_off = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[2]')
    set_save = (By.XPATH, '//span[text()="储存"]')
    set_save_cancel = (By.XPATH, '//span[text()="取消"]')
    set_save_submit = (By.XPATH, '(//span[text()="确认"])[last()]')

    # ------------------------- 群組管理 > 群發訊息 ------------------------
    menu_group_msg = (By.XPATH, "//a[text()=' 群发讯息']")  # 群組管理 - 群發消息
    search_sender_id = (By.XPATH, '//input[@placeholder="请输入会员帐号"]')  # 發布帳號輸入欄位
    group_msg_add = (By.XPATH, '//span[text()="新增"]')  # 新增鍵
    # ------------------------- 群發訊息 > 新增 ------------------------
    group_msg_send_time = (By.XPATH, '//input[@data-test="dp-input"]')  # 開始時間
    select_sender_ID = (By.XPATH, '(//label[text()="发布帐号"]/..//input)[last()]')  # 發布帳號
    add_sender = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="gubot01"]')
    select_chatroom = (By.XPATH, '//label[text()="发布聊天室"]/..//input')
    # add_chatroom = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="QA_bot_only"]')
    text_radio_btn = (By.XPATH, '(//span[@class="el-radio__inner"])[1]')  # 訊息類型-文字
    group_msg_content = (By.XPATH, '//textarea[@placeholder="请输入讯息内容"]')  # 訊息內容
    group_msg_save = (By.XPATH, '//span[text()="保存"]')  # 保存鍵
    # ------------------------- 群發訊息 > 消息列表 ---------------------
    detail_group_msg_list_send_time = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")  # 發布時間
    detail_group_msg_list_sender_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")  # 發布帳號
    detail_group_msg_list_target_group = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")  # 發布群組
    detail_group_msg_list_msg_content = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")  # 訊息內容
    detail_group_msg_list_msg_send_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[5]")  # 發送狀態
    detail_group_msg_list_msg_fail_group = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")  # 失敗群組

    @staticmethod
    def add_chatroom_select(brand):
        text = "QA bot only" if brand.lower() == "mingpin" else "QA_bot_only"
        return By.XPATH, f'//div[@aria-hidden="false"]//span[text()="{text}"]'

class GroupsPage(BasePage):
    brand = gl.get_value("BRAND")

    def check_group_list_page(self):
        assert self.is_element_finded(GroupsPageLocator.group_id), f'未出現"群組編號"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.group_name), f'未出現"群組名稱"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.invitation_code), f'未出現"邀請碼"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.group_search), f'未出現"搜尋"鍵'
        assert self.is_element_finded(GroupsPageLocator.group_add), f'未出現"+新增群組"鍵'

    def groups_delete(self, name):
        self.wait_loading_finish()
        self.wait_visibility(GroupsPageLocator.group_name)
        self.type(GroupsPageLocator.group_name, name)
        self.click(GroupsPageLocator.group_search)
        assert not self.is_element_finded(GroupsPageLocator.result_empty), f'搜查結果為空'
        self.wait_loading_finish()
        group_name = self.get_text(GroupsPageLocator.result_group_name)
        group_owner = (re.search(r'\((.*?)\)', self.get_text(GroupsPageLocator.result_group_owner))).group(1)

        if self.get_text(GroupsPageLocator.result_group_state) == '启用':
            self.execute_js("window.scrollBy(500, 0)")
            self.click(GroupsPageLocator.button_delete)

            self.wait_visibility(GroupsPageLocator.delete_title)
            assert self.get_text(GroupsPageLocator.delete_group_name) == group_name, f'刪除群組 名稱有誤, 預期:{group_name}, 實際:{self.get_text(GroupsPageLocator.delete_group_name)}'

            self.click(GroupsPageLocator.delete_select)
            self.select_operate_id(group_owner)

            self.click(GroupsPageLocator.delete_popup_btn)
            sleep(3)
            assert self.get_text(GroupsPageLocator.result_group_state) == '删除', f'預期: 删除, 實際: {self.get_text(GroupsPageLocator.result_group_state)}'
        else:
            print('群組已被刪除')

    def groups_add(self, account):  ## 未完成
        self.wait_loading_finish()

        if self.is_element_finded(GroupsPageLocator.group_add) == True:
            self.click(GroupsPageLocator.group_add)

        self.wait_loading_finish()

        assert self.get_text(GroupsPageLocator.add_group_title) == "新增群组", f'進入新增頁面失敗'

        self.click(GroupsPageLocator.add_group_select)
        self.select_operate_id(account)

        self.type(GroupsPageLocator.add_group_name, 'acb')

    def select_operate_id(self, account):
        for element in self.find_elements(GroupsPageLocator.operate_id):
            sleep(1)
            if element.text == account:
                element.click()
                break
            # else:
            #     continue

    def groups_history_switch(self, status):
        self.wait_loading_finish()

        if status == True:
            self.click(GroupsPageLocator.set_history_on)
        else:
            self.click(GroupsPageLocator.set_history_off)

        self.click(GroupsPageLocator.set_save)
        self.click(GroupsPageLocator.set_save_submit)

    def groups_build_switch(self, status):
        self.wait_loading_finish()

        if status == True:
            self.click(GroupsPageLocator.set_build_on)
        else:
            self.click(GroupsPageLocator.set_build_off)

        self.click(GroupsPageLocator.set_save)
        self.click(GroupsPageLocator.set_save_submit)

    def group_add_members(self):
        self.click(GroupsPageLocator.group_management)
        self.click(GroupsPageLocator.group_list)
        sleep(3)
        self.click(GroupsPageLocator.group_stress_test_member_num_icon)
        sleep(2)
        self.click(GroupsPageLocator.operator_id_dropdown)
        # self.click(GroupsPageLocator.operator_york)
        self.click(GroupsPageLocator.group_addmember_btn)
        for i in range(2500,3000):
            self.type(GroupsPageLocator.add_group_member,f'auto_test_{i}')
            self.click(GroupsPageLocator.add_group_member_search_btn)
            self.click(GroupsPageLocator.add_group_member_confirm_add_btn)

    def group_add_group_msg(self, msg):
        self.click(GroupsPageLocator.group_msg_add)
        self.wait_loading_finish()
        send_time = self.get_attribute(GroupsPageLocator.group_msg_send_time, 'value')
        self.click(GroupsPageLocator.select_sender_ID)
        self.click(GroupsPageLocator.add_sender)  # Select gubot01
        self.click(GroupsPageLocator.select_chatroom)
        self.click(GroupsPageLocator.add_chatroom_select(self.brand))  # Select QA_bot_only
        self.click(GroupsPageLocator.text_radio_btn)  # Select 文字類型
        self.click(GroupsPageLocator.group_msg_content)
        self.type(GroupsPageLocator.group_msg_content, msg)
        self.click(GroupsPageLocator.group_msg_save)
        sleep(60)
        return send_time

    def check_group_msg_list(self, send_time, sender, target_group, msg):
        self.type(GroupsPageLocator.search_sender_id, sender)  # 輸入發布帳號
        self.type(GroupsPageLocator.add_group_name, target_group)  # 輸入發布群組
        self.click(GroupsPageLocator.group_search)
        self.wait_loading_finish()
        sleep(1)
        actual_send_time = self.get_text(GroupsPageLocator.detail_group_msg_list_send_time)
        actual_sender_id = self.get_text(GroupsPageLocator.detail_group_msg_list_sender_id)
        actual_target_group = self.get_text(GroupsPageLocator.detail_group_msg_list_target_group)
        actual_msg_content = self.get_text(GroupsPageLocator.detail_group_msg_list_msg_content)
        actual_send_status = self.get_text(GroupsPageLocator.detail_group_msg_list_msg_send_status)
        actual_fail_group = self.get_text(GroupsPageLocator.detail_group_msg_list_msg_fail_group)
        assert actual_send_time == f'{send_time.replace("-", "/")}:00', f'發布時間錯誤, 預期:{send_time.replace("-", "/")}:00,實際:{actual_send_time}'
        assert actual_sender_id == sender, f'發布帳號錯誤, 預期:{sender},實際:{actual_sender_id}'
        assert actual_target_group == target_group, f'發布群組錯誤, 預期:{target_group},實際:{actual_target_group}'
        assert actual_msg_content == msg, f'發布內容錯誤, 預期:{msg},實際:{actual_msg_content}'
        assert actual_send_status == '已发送', f'發布狀態錯誤, 預期:已发送,實際:{actual_send_status}'
        assert actual_fail_group == "-", f'失敗群組錯誤, 預期:-,實際:{actual_send_status}'





