from time import sleep

from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage


class GroupsPageLocator:
    # 搜尋欄位
    group_id = (By.XPATH, '//input[@placeholder="请输入群组编号"]')
    group_name = (By.XPATH, '//input[@placeholder="请输入群组名称"]')
    invitation_code = (By.XPATH, '//input[@placeholder="请输入邀请码"]')

    group_search = (By.XPATH, '//span[text()=" 搜寻 "]/..')
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
    result_group_black = (By.XPATH, '(//td[contains(@class,"el-table_1_column_5")])[1]')

    # -------------------- 建立時間欄位 -------------------- 
    result_group_create = (By.XPATH, '(//td[contains(@class,"el-table_1_column_6")])[1]')

    # -------------------- 更新時間欄位 -------------------- 
    result_group_update = (By.XPATH, '(//td[contains(@class,"el-table_1_column_7")])[1]')

    # -------------------- 成員權限欄位 -------------------- 
    result_group_rule = (By.XPATH, '(//td[contains(@class,"el-table_1_column_8")])[1]')

    # -------------------- 擁有者欄位 -------------------- 
    result_group_owner = (By.XPATH, '(//td[contains(@class,"el-table_1_column_9")])[1]')

    # -------------------- 管理員欄位 -------------------- 
    result_group_admin = (By.XPATH, '(//td[contains(@class,"el-table_1_column_10")])[1]')

    # -------------------- 狀態欄位 -------------------- 
    result_group_state = (By.XPATH, '(//td[contains(@class,"el-table_1_column_11")])[1]')

    # -------------------- 操作欄位 -------------------- 
    button_delete = (By.XPATH, '//button[contains(@class,"button--danger")]/span[text()="删除"]')

    delete_title = (By.XPATH, '//div[@aria-label="删除群组"]//span[@class="el-dialog__title"]')
    delete_group_name = (By.XPATH, '//span[@class="item-name"]')
    delete_select = (By.XPATH, '//span[@class="item-name"]/..//span[@class="el-input__suffix-inner"]')
    delete_popup_btn = (By.XPATH, '//button[contains(@class,"button--danger")]/span[text()="删 除"]')

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
    set_biuld_on = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[1]')
    set_biuld_off = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[2]')
    set_save = (By.XPATH, '//span[text()="保存"]')
    set_save_cancel = (By.XPATH, '//span[text()="取消"]')
    set_save_submit = (By.XPATH, '//span[text()="確定"]')


class GroupsPage(BasePage):

    def check_group_list_page(self):
        assert self.is_element_finded(GroupsPageLocator.group_id), f'未出現"群組編號"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.group_name), f'未出現"群組名稱"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.invitation_code), f'未出現"邀請碼"輸入搜尋欄位'
        assert self.is_element_finded(GroupsPageLocator.group_search), f'未出現"搜尋"鍵'
        assert self.is_element_finded(GroupsPageLocator.group_add), f'未出現"+新增群組"鍵'

    def groups_delete(self, name):
        self.wait_loading_finish()

        if self.is_element_finded(GroupsPageLocator.group_name) == True:
            self.type(GroupsPageLocator.group_name, name)
            self.click(GroupsPageLocator.group_search)
            assert self.is_element_finded(GroupsPageLocator.result_empty) == False, f'搜查結果為空'

        group_name = self.get_text(GroupsPageLocator.result_group_name)
        group_onwer = self.get_text(GroupsPageLocator.result_group_owner)

        if self.get_text(GroupsPageLocator.result_group_state) == '启用':
            self.click(GroupsPageLocator.button_delete)
            if self.is_element_finded(GroupsPageLocator.delete_title) == True:
                assert self.get_text(GroupsPageLocator.delete_group_name) == group_name, f'刪除群組 名稱有誤'

                self.click(GroupsPageLocator.delete_select)

                self.select_operate_id(group_onwer)

                self.click(GroupsPageLocator.delete_popup_btn)
                assert self.get_text(GroupsPageLocator.result_group_state) == '删除'
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
        for operate in self.find_elements(GroupsPageLocator.operate_id):
            if operate == account:
                self.click(GroupsPageLocator.operate)
            else:
                print('請確認帳號確實綁定')
                pass

    def groups_history_switch(self, status):
        self.wait_loading_finish()

        if status == True:
            self.click(GroupsPageLocator.set_history_on)
        else:
            self.click(GroupsPageLocator.set_history_off)

        self.click(GroupsPageLocator.set_save)
        self.click(GroupsPageLocator.set_save_submit)

    def groups_biuld_switch(self, status):
        self.wait_loading_finish()

        if status == True:
            self.click(GroupsPageLocator.set_biuld_on)
        else:
            self.click(GroupsPageLocator.set_biuld_off)

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



