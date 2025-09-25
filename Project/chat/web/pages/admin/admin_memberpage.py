from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.admin.admin_basepage import BasePage


class MemberPageLocator:
    # 共用
    page_title = (By.XPATH, "//div[@class='page-title']")
    confirm_btn = (By.XPATH, "//div[(@class='el-overlay')and not(contains(@style,'none'))]//button[2]")
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

    # 搜尋列
    search_member_ID = (By.XPATH, '//input[@placeholder="搜寻多个请以逗号分隔"]')
    search_member_name = (By.XPATH, '//input[@placeholder="搜寻多个请以逗号分隔"]')
    search_brand_id = (By.XPATH, '//input[@placeholder="请输入品牌帐号"]')
    search_start_time = (By.XPATH, '//input[@placeholder="开始日期"]')
    search_end_time = (By.XPATH, '//input[@placeholder="结束日期"]')
    search_ID_type = (By.XPATH, '//input[@placeholder="请选择帐号类型"]')
    search_remark = (By.XPATH, '//input[@placeholder="请输入备注"]')
    search_btn = (By.XPATH, '//span[text()="搜寻"]')
    export_btn = (By.XPATH, '//span[text()="汇出"]')

    # 新增會員帳號
    new_account_btn = (By.XPATH, '//button//span[text()="新增会员帐号"]')
    new_account_title = (By.XPATH, '//div[text()="帐号设定"]')
    new_account_ID = (By.XPATH, '//input[@placeholder="请填写3-30字且不可包含特殊符号"]')
    new_account_name = (By.XPATH, '(//input[@placeholder="请填写3-30字且不可包含特殊符号"])[last()]')
    new_account_password = (By.XPATH, '//span[text()="新增会员帐号"]/../..//input[@placeholder="请填写8-16位数英文、数字"]')
    new_account_password_confirm = (By.XPATH, '//span[text()="新增会员帐号"]/../..//input[@placeholder="请再次输入密码"]')
    new_account_remark = (By.XPATH, '//span[text()="新增会员帐号"]/../..//input[@placeholder="请输入品牌帐号"]')

    # 人工創建帳號
    manual_create_app_account_btn = (By.XPATH, '//button//span[text()="人工创建帐号"]')
    manual_add_account_btn = (By.XPATH, '//button//span[text()="手动新增账号"]')
    manual_account_phone_input = (By.XPATH, '//input[@placeholder="请填写手机号(符合所选国家/地区手机号位数)"]')
    manual_account_password = (By.XPATH, '//span[text()="人工创建帐号"]/../..//input[@placeholder="请填写8-16位数英文、数字"]')
    manual_account_password_confirm = (By.XPATH, '//span[text()="人工创建帐号"]/../..//input[@placeholder="请再次输入密码"]')
    manual_account_remark = (By.XPATH, '//span[text()="人工创建帐号"]/../..//input[@placeholder="请输入品牌帐号"]')


    # 會員列表資料
    member_list_member_status_title = (By.XPATH, '//div[text()="会员状态"]')
    member_list_member_last_login_time_title = (By.XPATH, '//div[text()="最后登入时间"]')
    member_list_account_type_title = (By.XPATH, '//div[text()="帐号类型"]')

    member_list_ID = (By.XPATH, '//tr[@class="el-table__row"]//td[2]')
    member_list_name = (By.XPATH, '//tr[@class="el-table__row"]//td[3]')
    member_list_brand_id = (By.XPATH, '//tr[@class="el-table__row"]//td[5]')
    member_list_member_status = (By.XPATH, '//tr[@class="el-table__row"]//td[7]')
    member_list_group_amount = (By.XPATH, '//tr[@class="el-table__row"]//td[10]')
    member_list_build_time = (By.XPATH, '//tr[@class="el-table__row"]//td[12]')
    member_list_revise_time = (By.XPATH, '//tr[@class="el-table__row"]//td[13]')
    member_list_ID_type = (By.XPATH, '//tr[@class="el-table__row"]//td[14]')
    member_list_ID_remark = (By.XPATH, '//tr[@class="el-table__row"]//td[15]')
    
    # 社群權限
    social_permission_btn = (By.XPATH, '//button[@class="el-button el-button--primary el-button--mini"]//span[text()="社群权限"]')
    social_post_comment_permission_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[8]/div/div[2]/form/div/div/div') # 評論切換開關
    social_permission_page_close_btn = (By.XPATH, '//span[text()="关闭"]')
    social_permission_page_title = (By.XPATH, '//span[text()="社群权限"]')
    update_succeed_toast = (By.XPATH, '//p[text()="更新成功"]')

    # 修改會員帳號
    member_change_data_title = (By.XPATH, '//span[text()="修改会员帐号"]')
    member_change_name = (By.XPATH, '//div[@aria-label="修改会员帐号"]/..//input[@placeholder="请输入会员昵称"]')
    member_change_remark = (By.XPATH, '//div[@aria-label="修改会员帐号"]/..//input[@placeholder="请输入品牌帐号"]')
    member_change_btn= (By.XPATH, '//button[@class="el-button el-button--primary el-button--mini"]//span[text()="修改资料"]')

    # 重製安全密碼
    reset_security_password_btn = (By.XPATH, '//tr[@class = "el-table__row"]//td[11]//span[text()="重置安全密码"]')
    reset_security_password_title = (By.XPATH, '//div[@class = "el-dialog__header"]//span[text() = "重置安全密码"]')

    # 變更密碼
    member_password_tips = (By.XPATH, '//span[text()="变更密码"]/../..//div[text()="提醒：密码需英+数，不区分英文大小写，与一数字，不包含空白"]')
    member_password_setting = (By.XPATH, '//span[text()="变更密码"]/../..//input[@placeholder="请填写8-16位数英文、数字"]')
    member_password_confirm = (By.XPATH, '//span[text()="变更密码"]/../..//input[@placeholder="请再次输入密码"]')
    member_password_record = (By.XPATH, '//textarea[@placeholder="请填写操作记录"]')
    member_password_btn =(By.XPATH, '//button[@class="el-button el-button--primary el-button--mini"]//span[text()="变更密码"]')
    
    # 刪除
    member_delete_title = (By.XPATH, '(//span[text()="删除会员"])[last()]')
    member_delete_check = (By.XPATH, '//td[@class="el-table_1_column_17 is-center  "]//span[text()="已删除的帐号"]')
    member_delete_btn = (By.XPATH, '//td[@class="el-table_1_column_17 is-center  "]//span[text()="删除"]')

    # 設定備註
    remark_title = (By.XPATH, '//span[text() ="备注文案"]') 
    remark_textarea = (By.XPATH, '//textarea[@class="el-textarea__inner"and@style="resize: none; min-height: 369px; height: 369px;"]')
    remark_btn = (By.XPATH, '//div[@class="cell"]//i[@class="el-icon-edit edit-button"]')

    # 兌換綁定
    exchange_title = (By.XPATH, '//span[text() = "兑换绑定"]')
    wellpay_page = (By.XPATH, '//li[text()="顺付"]')
    lottery_page = (By.XPATH, '//li[text()="平台"]')
    bind_platform = (By.XPATH, '//div[@aria-label= "兑换绑定"]//tr[1]//td[1]')
    bind_member_account = (By.XPATH, '//div[@aria-label= "兑换绑定"]//tr[1]//td[2]')
    bind_time = (By.XPATH, '//div[@aria-label= "兑换绑定"]//tr[1]//td[3]')
    bind_operate = (By.XPATH, '//div[@aria-label= "兑换绑定"]//tr[1]//td[4]')
    entry_rebind_btn = (By.XPATH, '//tr[@class="el-table__row"]//td[16]//span[@class="text-link"]')
    rebind_btn = (By.XPATH, '//span[text()="重新绑定"]')

    # ============================== 会员层级 ===================================
    member_level_dropdownlist = (By.XPATH, '//input[@placeholder="请选择会员层级"]')
    new_member_level_btn = (By.XPATH, '//button//span[text()="新增层级"]')
    member_level_list_level_title = (By.XPATH, '//div[text()="层级名称"]')
    member_level_list_member_amount_title = (By.XPATH, '//div[text()="会员数量"]')
    member_level_list_wellpay_exchange_title = (By.XPATH, '//div[text()="顺付积分兑换"]')
    member_level_list_brand_exchange_title = (By.XPATH, '//div[text()="品牌积分兑换"]')
    member_level_list_operator_title = (By.XPATH, '//div[text()="操作人"]')
    member_level_list_note_title = (By.XPATH, '//div[text()="备注"]')
    member_level_list_operate_title = (By.XPATH, '//div[text()="操作"]')


class MemberPage(BasePage):

    # 檢查會員列表頁面基本資訊
    def check_member_list_page(self):
        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.search_member_ID), f'未看見會員帳號輸入欄位'
        assert self.is_element_finded(MemberPageLocator.search_brand_id), f'未看見品牌帳號輸入欄位'
        assert self.is_element_finded(MemberPageLocator.search_btn), f'未看見"搜尋"鍵'
        assert self.is_element_finded(MemberPageLocator.manual_create_app_account_btn), f'未看見"+人工創建帳號"鍵'
        assert self.is_element_finded(MemberPageLocator.export_btn), f'未看見"匯出"鍵'
        assert self.is_element_finded(MemberPageLocator.member_list_member_status_title), f'未看見會員列表的"會員狀態"欄位'
        assert self.is_element_finded(MemberPageLocator.member_list_member_last_login_time_title), f'未看見會員列表的"最後登入時間"欄位'
        assert self.is_element_finded(MemberPageLocator.member_list_account_type_title), f'未看見會員列表的"帳號類型"欄位'

    def check_member_level_page(self):
        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.member_level_dropdownlist), f'未看見會員層級下拉選單'
        assert self.is_element_finded(MemberPageLocator.search_btn), f'未看見"搜尋"鍵'
        assert self.is_element_finded(MemberPageLocator.new_member_level_btn), f'未看見"+新增層級"鍵'
        assert self.is_element_finded(MemberPageLocator.member_level_list_level_title), f'未看見層級列表"層級名稱"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_member_amount_title), f'未看見層級列表"會員數量"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_wellpay_exchange_title), f'未看見層級列表"顺付积分兑换"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_brand_exchange_title), f'未看見層級列表"品牌积分兑换"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_operator_title), f'未看見層級列表"操作人"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_note_title), f'未看見層級列表"备注"欄位'
        assert self.is_element_finded(MemberPageLocator.member_level_list_operate_title), f'未看見層級列表"操作"欄位'
    # 檢查搜尋功能
    def search(self, member_ID):
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.search_member_ID) is True :
            self.type(MemberPageLocator.search_member_ID, member_ID)
            self.click(MemberPageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, F'搜尋帳號失敗'
        self.refresh_browser()
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.search_member_name) is True:
            self.type(MemberPageLocator.search_member_name, member_ID)
            self.click(MemberPageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID, F'搜尋暱稱失敗'
        self.refresh_browser()
        self.wait_loading_finish()
        # if self.is_element_finded(MemberPageLocator.search_brand_id) is True :
        #     self.type(MemberPageLocator.search_brand_id, brand_ID)
        #     self.click(MemberPageLocator.search_btn)
        #     assert self.is_element_finded(MemberPageLocator.member_brand_id) == brand_ID, F'查無此品牌帳號'
        # self.refresh_browser()
        # self.wait_loading_finish
        if self.is_element_finded(MemberPageLocator.search_remark) is True :
            self.type(MemberPageLocator.search_remark, member_ID)
            self.click(MemberPageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_ID_remark) == member_ID, F'搜尋備註失敗'
        self.wait_loading_finish()
        
    # 搜尋ID
    def search_ID(self, member_ID):
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.search_member_ID) is True :
            self.type(MemberPageLocator.search_member_ID, member_ID)
            self.click(MemberPageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, f'搜尋帳號失敗'
        self.wait_loading_finish()

    # 新增會員 會員帳號填寫 test月份m日期d
    def build_account(self, member_ID): 
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.new_account_btn) is True:
            self.click(MemberPageLocator.new_account_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.new_account_title) == "帐号设定", f'進入新增帳號頁面失敗'
            self.type(MemberPageLocator.new_account_ID, member_ID)
            self.type(MemberPageLocator.new_account_name, member_ID)
            self.type(MemberPageLocator.new_account_password, 'Heaven5267')
            self.type(MemberPageLocator.new_account_password_confirm, 'Heaven5267')
            self.type(MemberPageLocator.new_account_remark, 'TestRemark')
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()
        self.wait_loading_finish()

    def manual_create_app_account(self, member_id, phone, password):
        self.wait_loading_finish()
        self.click(MemberPageLocator.manual_create_app_account_btn)
        if self.is_element_finded(MemberPageLocator.manual_add_account_btn):
            self.click(MemberPageLocator.manual_add_account_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.new_account_title) == "帐号设定", f'進入人工創建帳號頁面失敗'
            self.type(MemberPageLocator.manual_account_phone_input, phone)
            self.type(MemberPageLocator.new_account_ID, member_id)
            self.type(MemberPageLocator.new_account_name, member_id)
            self.type(MemberPageLocator.manual_account_password, password)
            self.type(MemberPageLocator.manual_account_password_confirm, password)
            self.type(MemberPageLocator.manual_account_remark, 'AutoTest')
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()
        self.wait_loading_finish()


    # 設定備註 備註填寫 西元年y月份m日期d
    # 設定完備住後應更新修改時間 需開BUG單
    def revise_remark(self, member_ID):
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.remark_btn) is True :
            self.click(MemberPageLocator.remark_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.remark_title) == "备注文案", f'進入更改備註頁面失敗'
            self.type(MemberPageLocator.remark_textarea, member_ID)
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_ID_remark) == member_ID ,f'修改備註失敗'
        else:
            print('進入修改帳號頁面失敗')
        self.wait_loading_finish()
     
    # 修改資料 暱稱填寫 test月份m日期d
    # 設定完備住後應更新修改時間 需開BUG單
    def member_change_data(self, member_ID): 
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.member_change_btn):
            self.click(MemberPageLocator.member_change_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_change_data_title) == '修改会员帐号', f'進入更改資料頁面失敗'
            self.type(MemberPageLocator.member_change_name, member_ID)
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID ,f'修改會員帳號失敗'
        self.wait_loading_finish()

    # 重製安全密碼
    def reset_security_password(self, member_ID):
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.reset_security_password_btn):
            self.click(MemberPageLocator.reset_security_password_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.reset_security_password_title) == '重置安全密码', f'進入修改安全密碼頁面失敗'
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()

    # 變更密碼
    def member_change_password(self, member_ID): 
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.member_password_btn) is True:
            self.click(MemberPageLocator.member_password_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_password_tips) == '提醒：密码需英+数，不区分英文大小写，与一数字，不包含空白' ,f'進入更改密碼頁面失敗'
            self.type(MemberPageLocator.member_password_setting, 'Heaven4394')
            self.type(MemberPageLocator.member_password_confirm, 'Heaven4394')
            self.type(MemberPageLocator.member_password_record, member_ID)
            self.click(MemberPageLocator.confirm_btn)
        self.wait_loading_finish()
     
    # 檢查資料 須從建立帳號、修改密碼 def 提取時間 進行比對 (未完成)
    def check_data(self, member_ID, build_time, revise_time, condition):
        self.search_ID(member_ID)
        if condition == 'confirm_build':
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, f'搜尋帳號失敗'
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID, f'帳號資料有誤'
            assert self.get_text(MemberPageLocator.member_list_brand_id) == 'TestRemark', f'品牌帳號有誤'
            assert self.get_text(MemberPageLocator.member_list_member_status) == '正常', f'會員狀態有誤'
            assert self.get_text(MemberPageLocator.member_list_group_amount) == '0', f'群組數量有誤'
            assert self.get_text(MemberPageLocator.member_list_build_time)[:-3] == build_time , f'預期:{self.get_text(MemberPageLocator.member_list_build_time)},實際:{build_time}, 建立時間有誤'
            assert self.get_text(MemberPageLocator.member_list_ID_type) == '后台开通', f'帳號類型有誤'
        elif condition == 'confirm_revise':
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, f'搜尋帳號失敗'
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID, f'帳號資料有誤'
            assert self.get_text(MemberPageLocator.member_list_brand_id) == 'AutoTest', f'品牌帳號有誤'
            assert self.get_text(MemberPageLocator.member_list_member_status) == '正常', f'會員狀態有誤'
            assert self.get_text(MemberPageLocator.member_list_group_amount) == '0', f'群組數量有誤'
            assert self.get_text(MemberPageLocator.member_list_revise_time)[:-3] == revise_time, f'預期:{self.get_text(MemberPageLocator.member_list_revise_time)},實際:{revise_time},修改時間有誤'
            assert self.get_text(MemberPageLocator.member_list_ID_type) == 'App注册', f'帳號類型有誤'
            assert self.get_text(MemberPageLocator.member_list_ID_remark) == member_ID, f'帳號備註有誤'
        elif condition == 'confirm_base':
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, f'print member_ID fail'
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID, f'print name fail'
            assert self.get_text(MemberPageLocator.member_list_brand_id) == 'AutoTest', f'品牌帳號有誤'
            assert self.get_text(MemberPageLocator.member_list_member_status) == '正常', f'會員狀態有誤'
            assert self.get_text(MemberPageLocator.member_list_group_amount) == '0', f'群組數量有誤'
            assert self.get_text(MemberPageLocator.member_list_ID_type) == 'App注册', f'帳號類型有誤'
        elif condition == 'confirm_manual_create':
            assert self.get_text(MemberPageLocator.member_list_ID) == member_ID, f'搜尋帳號失敗'
            assert self.get_text(MemberPageLocator.member_list_name) == member_ID, f'帳號資料有誤'
            assert self.get_text(MemberPageLocator.member_list_brand_id) == 'AutoTest', f'品牌帳號有誤'
            assert self.get_text(MemberPageLocator.member_list_member_status) == '正常', f'會員狀態有誤'
            assert self.get_text(MemberPageLocator.member_list_group_amount) == '0', f'群組數量有誤'
            actual_time = self.get_text(MemberPageLocator.member_list_build_time)[:-3]
            assert self.get_text(MemberPageLocator.member_list_build_time)[:-3] == build_time, f'建立時間有誤,預期:{build_time},實際:{actual_time}'
            assert self.get_text(MemberPageLocator.member_list_ID_type) == 'App注册', f'帳號類型有誤'
        self.wait_loading_finish()
        
    # 順付解綁
    def unbind_wellpay(self, member_ID):
        self.search_ID(member_ID)
        if self.get_text(MemberPageLocator.entry_rebind_btn) == '已绑定':
            self.click(MemberPageLocator.entry_rebind_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.exchange_title) == '兑换绑定', f'進入兌換綁定頁面失敗'
            self.click(MemberPageLocator.wellpay_page)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.bind_platform) == '顺付', f'進入順付頁面失敗'
            if self.is_element_finded(MemberPageLocator.rebind_btn):
                self.click(MemberPageLocator.rebind_btn)
                self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.bind_operate) == '已解绑', f'兌換解綁失敗'
        self.send_escape()
        self.wait_loading_finish()

    # 平臺解綁
    def unbind_brand(self, member_ID):
        self.search_ID(member_ID)
        if self.get_text(MemberPageLocator.entry_rebind_btn) == '已绑定':
            self.click(MemberPageLocator.entry_rebind_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.exchange_title) == '兑换绑定', f'進入兌換綁定頁面失敗'
            self.click(MemberPageLocator.rebind_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.bind_operate) == '已解绑', f'兌換解綁失敗'
        self.send_escape()
        self.wait_loading_finish()

    # 檢查綁定資料 #綁定時間 須等web綁定完成回傳
    def check_wellpay_bind_data(self, member_ID, bind_time, wellpay_address):
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.search_member_ID) is True:
            self.type(MemberPageLocator.search_member_ID, member_ID)
            self.click(MemberPageLocator.search_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_list_name) == '積分測試', f'搜尋帳號失敗'
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.entry_rebind_btn) is True:
            self.click(MemberPageLocator.entry_rebind_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.exchange_title) == '兑换绑定', f'進入兌換綁定頁面失敗'
            self.click(MemberPageLocator.wellpay_page)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.bind_platform) == '顺付', f'進入順付頁面失敗'
            assert self.get_text(MemberPageLocator.bind_member_account) == wellpay_address, f'錢包地址錯誤'
            assert self.get_text(MemberPageLocator.bind_time)[:-3] == bind_time, f'綁定時間有誤'
            assert self.get_text(MemberPageLocator.bind_operate) == '重新绑定', f'兌換綁定失敗'
        self.wait_loading_finish()

    # 刪除帳號
    def delete_member(self, member_ID): 
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.member_delete_btn) is True:
            self.click(MemberPageLocator.member_delete_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_delete_title) == '删除会员', f'進入刪除頁面失敗'
            self.click(MemberPageLocator.confirm_btn)
            self.wait_loading_finish()
            assert self.get_text(MemberPageLocator.member_delete_check) == '已删除的帐号', f'刪除帳號失敗'
            assert self.get_text(MemberPageLocator.member_list_member_status) == '已刪除', f'會員狀態錯誤'
        self.wait_loading_finish()

    def change_social_permission(self, member_ID, enable=True):
        self.search_ID(member_ID)
        if self.is_element_finded(MemberPageLocator.social_permission_btn) is True:
            self.click(MemberPageLocator.social_permission_btn)
            sleep(3)
            assert self.is_element_finded(MemberPageLocator.social_permission_page_title)
            origin_switch_status = self.get_attribute(MemberPageLocator.social_post_comment_permission_btn, 'aria-checked')
            if enable and origin_switch_status == 'false':
                self.click(MemberPageLocator.social_post_comment_permission_btn)
                self.wait_visibility(MemberPageLocator.update_succeed_toast)
                assert self.get_attribute(MemberPageLocator.social_post_comment_permission_btn, 'aria-checked') == 'true'
                self.click(MemberPageLocator.social_permission_page_close_btn)
            elif not enable and origin_switch_status == 'true':
                self.click(MemberPageLocator.social_post_comment_permission_btn)
                self.wait_visibility(MemberPageLocator.update_succeed_toast)
                assert self.get_attribute(MemberPageLocator.social_post_comment_permission_btn, 'aria-checked') == 'false'
                self.click(MemberPageLocator.social_permission_page_close_btn)
            else:
                assert str(enable).lower() == self.get_attribute(MemberPageLocator.social_post_comment_permission_btn, 'aria-checked')
                self.click(MemberPageLocator.social_permission_page_close_btn)


