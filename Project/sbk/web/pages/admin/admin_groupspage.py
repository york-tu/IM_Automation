from selenium.webdriver.common.by import By
import os, sys
from Project.chat.web.pages.admin.admin_basepage import BasePage

class GroupsPageLocator:
    # 搜尋欄位
    group_id = (By.XPATH, '//input[@placeholder="请输入群组编号"]')
    group_name = (By.XPATH, '//input[@placeholder="请输入群组名称"]')
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
    add_group_ = (By.XPATH, '')
    add_group_ = (By.XPATH, '')
    add_group_ = (By.XPATH, '')
    add_group_ = (By.XPATH, '')

    # -------------------- 群組設定 -------------------- 
    set_history_on = (By.XPATH, '(//label[text()="新加入群組的成員，是否可查看歷史訊息"]/..//span[@class="el-radio__inner"])[1]')
    set_history_off = (By.XPATH, '(//label[text()="新加入群組的成員，是否可查看歷史訊息"]/..//span[@class="el-radio__inner"])[2]')
    set_biuld_on = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[1]')
    set_biuld_off = (By.XPATH, '(//label[text()="建立群组功能"]/..//span[@class="el-radio__inner"])[2]')
    set_save = (By.XPATH, '//span[text()="保存"]')
    set_save_cancel = (By.XPATH, '//span[text()="取消"]')
    set_save_submit = (By.XPATH, '//span[text()="確定"]')


class GroupsPage(BasePage):

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
                assert self.get_text(GroupsPageLocator.delete_group_name) == group_name,f'刪除群組 名稱有誤'

                self.click(GroupsPageLocator.delete_select)

                self.select_operate_id(group_onwer)
                
                self.click(GroupsPageLocator.delete_popup_btn)
                assert self.get_text(GroupsPageLocator.result_group_state) == '删除'
        else:
            print('群組已被刪除')

    def groups_add(self, account): ## 未完成
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