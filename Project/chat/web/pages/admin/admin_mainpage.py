import random
import common.utils.globalvar as gl
from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.admin.admin_basepage import BasePage


class MainPageLocator:
    # ADMIN MAIN PAGE (導航欄)
    admin_board = (By.XPATH, "//a[text()='仪表板']")  # 儀表板
    # ------------------------- 會員管理 ------------------------
    menu_member = (By.XPATH, "//span[text()='会员管理']")  # 會員管理
    menu_member_list = (By.XPATH, "//a[text()=' 会员列表']")  # 會員列表
    menu_level_list = (By.XPATH, "//a[text()=' 会员层级']")  # 會員列表

    # ------------------------- 群組管理 ------------------------
    menu_groups = (By.XPATH, "//span[text()='群组管理']")  # 群組管理
    menu_groups_list = (By.XPATH, "//a[text()=' 群组列表']")  # 群組管理 - 群組列表
    menu_groups_set = (By.XPATH, "//a[text()=' 群组设定']")  # 群組管理 - 群組設定
    menu_groups_own = (By.XPATH, "//a[text()=' 群组建立成员']")  # 群組管理 - 群組建立成員

    # ------------------------- 群組管理 > 邀請碼管理 ------------------------
    menu_share_code = (By.XPATH, "//a[text()=' 邀请码管理']")  # 群組管理 - 邀请码管理
    search_share_code = (By.XPATH, '//input[@placeholder="请输入邀请码"]')  # 邀請碼輸入欄位
    search_group_name = (By.XPATH, '//input[@placeholder="请输入群组名称"]')  # 群組名輸入欄位
    search_btn = (By.XPATH, '//span[text()="搜寻"]')  # 搜尋鍵
    list_code = (By.XPATH, '//tr[@class="el-table__row"]//td[1]')  # 搜尋結果 - 邀請碼欄位
    list_related_group = (By.XPATH, '//tr[@class="el-table__row"]//td[2]')  # 搜尋結果 - 對應群組欄位
    share_code_result_empty = (By.XPATH, '//div[@class = "el-table__empty-block"]')  # 搜尋結果顯示的列表為空
    # -------------------------- 群組管理 > 邀請碼管理 > 新增邀請碼 --------------
    add_btn = (By.XPATH, '//button//span[text()="新增"]')  # "新增"鍵
    add_share_code_input_field = (By.XPATH, '(//div[@class="el-dialog"]/..//input[@placeholder="请输入邀请码"])')  # 新增視窗 - 邀請碼輸入框
    search_bind_group_input_field = (By.XPATH, '(//div[@class="el-dialog"]/..//input[@placeholder="请输入群组名称"])')  # 新增視窗 - 搜索綁定群組輸入框
    search_bind_group_btn = (By.XPATH, '//div[@class = "el-input-group__append"]')  # 搜尋鍵
    add_bind_group_add_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[4]/div/div[2]/div[3]/div/div[3]/table/tbody/tr/td[4]/div/i')  # "+"鍵
    set_save = (By.XPATH, '//button//span[text()="储存"]')
    share_code_list_delete_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr/td[4]/div/div/button[2]')  # 刪除鍵
    delete_confirm_btn = (By.XPATH, '(//span[text()="删除"])[last()]')  # 二次確認刪除鍵
    # -------------------------- 群組管理 > 邀請碼管理 > 編輯储存og"]/..//span[text()="仅后台"])')  # 分享權限 - 僅後台
    share_code_list_modify_btn = (By.XPATH,
                                  '//*[@id="app"]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr/td[4]/div/div/button[1]')  # 編輯鍵
    all_members_btn = (By.XPATH, '(//div[@class="el-dialog"]/..//span[text()="所有成员"])')  # 分享權限 - 所有成員
    backstage_only_btn = (By.XPATH, '(//div[@class="el-dialog"]/..//span[text()="仅后台"])')  # 分享權限 - 僅後台
    admin_only_btn = (By.XPATH, '(//div[@class="el-dialog"]/..//span[text()="仅管理员"])')  # 分享權限 - 僅管理員
    # ------------------------- 群組管理 > 群發訊息 ------------------------
    menu_group_msg = (By.XPATH, "//a[text()=' 群发讯息']")  # 群組管理 - 群發消息

    # ------------------------- 系統管理 -------------------------
    menu_system = (By.XPATH, "//span[text()='系统管理']")  # 系統管理

    # ------------------------- 系統管理 > APP/Web維護 ------------
    menu_system_maintenance = (By.XPATH, "//a[text()=' APP/Web维护']")  # APP 維護

    # ------------------------- 系統管理 > APP/Web設定 ------------
    menu_system_app_setting = (By.XPATH, "//a[text()=' APP/Web设定']")  # APP 設定
    register_with_social_account = (By.XPATH, "//label[text()='品牌帐号']")  # 品牌帐号選項
    geetest = (By.XPATH, "//label[text()='极验']")  # 极验選項
    geetest_on = (By.XPATH, '(//label[text()="极验"]/..//span[text() = "开启"])')  # 极验: 開
    geetest_off = (By.XPATH, '(//label[text()="极验"]/..//span[text() = "关闭"])')  # 极验: 關
    user_contact_whitelist = (By.XPATH, "//label[text()='会员添加好友']")  # 会员添加好友選項
    add_friend_by_search_phone = (By.XPATH, "//label[text()='手机号搜索添加好友']")  # 手机号搜索添加好友選項

    # ------------------------- 系統管理 > APP/Web設定 > 會員添加好友 ------------
    set_member_add_friend_on = (By.XPATH, '(//label[text()="会员添加好友"]/..//span[text() = "开启"])')  # 會員添加好友: 開
    set_member_add_friend_off = (By.XPATH, '(//label[text()="会员添加好友"]/..//span[text() = "关闭"])')  # 會員添加好友: 關
    member_add_friend_off_checked = (By.XPATH, '(//label[text()="会员添加好友"]/..//label[@class = "el-radio is-checked"]//span[text() = "关闭"])')  # 會員添加好友"關閉"checked
    member_add_friend_on_checked = (By.XPATH,'(//label[text()="会员添加好友"]/..//label[@class = "el-radio is-checked"]//span[text() = "开启"])')  # 會員添加好友"開啟"checked
    member_add_friend_tip = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div[1]/form/div[4]')  # 會員添加好友選項tip

    # ------------------------- 系統管理 > APP/Web設定 > 手机号搜寻添加好友 ------------
    search_friend_by_phone_on = (By.XPATH, '(//label[text()="手机号搜索添加好友"]/..//span[text() = "开启"])')  # 手机号搜寻添加好友: 開
    search_friend_by_phone_off = (By.XPATH, '(//label[text()="手机号搜索添加好友"]/..//span[text() = "关闭"])')  # 手机号搜寻添加好友: 關
    search_friend_by_phone_on_checked = (By.XPATH, '(//label[text()="手机号搜索添加好友"]/..//label[@class = "el-radio is-checked"]//span[text() = "开启"])')  # 手机号搜寻添加好友"開啟"checked
    search_friend_by_phone_off_checked = (By.XPATH, '(//label[text()="手机号搜索添加好友"]/..//label[@class = "el-radio is-checked"]//span[text() = "关闭"])')  # 手机号搜寻添加好友"關閉"checked
    add_friend_by_search_phone_tip = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div[1]/form/div[6]')  # 手机号搜寻添加好友tip

    # ------------------------- 系統管理 > 保存二次確認視窗 -------------------------
    save_btn = (By.XPATH, '//div[@class = "flex justify-end"]//span[text() = "储存"]')  # 保存
    save_confirm_btn = (By.XPATH, '//div[@class = "el-popconfirm__action"]//span[text() = "确定"]')  # 二次確認

    # ------------------------- 系統管理 > 好友添加白名单设定 ------------------------
    menu_system_contact_whitelist_setting = (By.XPATH, "//a[text()=' 好友添加白名单设定']")  # 系統管理 - 好友添加白名单设定
    contact_whitelist_setting_hint = (By.XPATH, "//p[@class='hint']")  # 好友添加白名单设定頁提示說明文字
    add_new_whitelist_member_btn = (By.XPATH, '//button//span[text()="新增"]')  # "新增"鍵


    # 搜尋列
    search_member_ID = (By.XPATH, '//input[@placeholder="输入会员帐号ID"]')  # 會員帳號ID輸入欄位
    # search_btn = (By.XPATH, '//span[text()=" 搜寻 "]')  # 搜尋鍵
    member_list_ID = (By.XPATH, '//tr[@class="el-table__row"]//td[2]')  # 白名單列表會員帳號ID欄位
    member_delete_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr/td[6]/div/div/button')  # 白名單列表刪除鍵
    member_delete_confirm_btn = (By.XPATH, '(//span[text()="删除"])[last()]')  # 二次確認刪除鍵
    search_result_is_empty = (By.XPATH, '//div[@class = "el-table__empty-block"]')  # 搜尋結果顯示的列表為空

    # -------------------------- 系統管理 > 好友添加白名单设定 > 新增成員 --------------
    add_member_page_search_field = (By.XPATH, '//input[@placeholder="输入帐号/昵称搜索"]')  # 新增成員輸入框
    add_member_page_search_btn = (By.XPATH, '//div[@class = "el-input-group__append"]')  # 搜尋鍵
    add_member_page_add_btn = (By.XPATH,
                               '//*[@id="app"]/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[4]/div/i')  # "+"鍵

    # -------------------------- 系統管理 > 發現设定 --------------
    discover_setting = (By.XPATH, "//a[text()=' 发现设定']")  # 發現設定
    discover_list_0_name = (By.XPATH, "(//div[@class='draggable item'])[1]//div[@class='name']")  # 第一行功能名稱
    discover_list_1_name = (By.XPATH, "(//div[@class='draggable item'])[2]//div[@class='name']")  # 第二行功能名稱
    discover_list_2_name = (By.XPATH, "(//div[@class='draggable item'])[3]//div[@class='name']")  # 第三行功能名稱

    discover_list_0_url = (By.XPATH, "(//div[@class='draggable item'])[1]//div[@class='url']")  # 第一行功能網址

    discover_list_0_switch_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[4]/div')  # 第一行功能switch
    discover_list_1_switch_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/div')  # 第二行功能switch
    discover_list_2_switch_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div[4]/div')  # 第三行功能switch

    discover_list_0_edit_btn = (By.XPATH, "(//div[@class='draggable item'])[1]//div[@class='edit']")  # 第一行功能編輯鍵

    discover_edit_title = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div/div[1]')  # 編輯視窗標題
    discover_edit_function_name = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div/div[2]/form/div[1]/div')
    discover_edit_function_url = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div/div[3]/div/div[2]/form/div[3]/div')
    discover_edit_input_url = (By.XPATH, '//input[@placeholder="请输入网址"]')

    # ------------------------- 聊天纪录 -------------------------
    menu_recode = (By.XPATH, "//a[text()='聊天记录']")  # 聊天記錄

    # ------------------------- 設置 -------------------------
    menu_setting = (By.XPATH, "//span[text()='设置']")  # 設置
    menu_setting_account = (By.XPATH, "//a[text()=' 帐号管理']")  # 設置 - 帳號管理
    menu_setting_role = (By.XPATH, "//a[text()=' 角色权限']")  # 設置 - 角色權限
    menu_setting_otp = (By.XPATH, "//a[text()=' OTP管理']")  # 設置 - OTP 管理
    menu_setting_otp_operation = (By.XPATH, "//a[text()=' 运营OTP']")  # 設置 - 運營 OTP

    # ------------------------- 操作日志 -------------------------
    menu_log_query = (By.XPATH, "//span[text()='日志查询']")  # 日志查询
    menu_operation_log = (By.XPATH, "//a[@href='/logging/auditlog']")  # 日志查询 - 操作日誌

    # ------------------------- 紅包管理 -------------------------
    menu_red = (By.XPATH, "//span[text()='红包管理']")  # 紅包管理
    menu_red_list = (By.XPATH, "//a[text()=' 红包列表']")  # 紅包管理 - 紅包列表
    menu_red_water = (By.XPATH, "//a[text()=' 水量控制']")  # 紅包管理 - 水量控制

    # ------------------------- 积分管理 -------------------------
    menu_integral = (By.XPATH, "//span[text()='积分管理']")  # 積分管理
    menu_integral_record = (By.XPATH, "//a[text()=' 积分使用纪录']")  # 積分管理 - 積分使用紀錄

    manual_deposit = (By.XPATH, "//a[text()=' 人工存入']")  # 積分管理 - 人工存入
    add_manual_deposit = (By.XPATH, "//span[text()='新增人工存入']")  # "新增人工存入"鍵
    # add_manual_deposit_title = (By.XPATH, '//div[text()="新增人工存入"]')  # 新增人工存入視窗標題
    manual_deposit_account_ID = (By.XPATH, '//input[@placeholder="请输入会员帐号"]')  # 新增人工存入 - 會員帳號
    manual_deposit_item_dropdown_list = (By.XPATH, '//label[text()="存入项目"]/..//input')  # 新增人工存入 - 存入項目下拉選單
    manual_deposit_item_red_envelope = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="红包奖励积分"]')  # 新增人工存入 - 存入項目 - 红包奖励积分
    manual_deposit_item_red_envelope_used = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="红包使用积分"]')  # 新增人工存入 - 存入項目 - 红包使用积分
    manual_deposit_item_reward_for_reporting = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="检举奖金"]')  # 新增人工存入 - 存入項目 - 检举奖金
    manual_deposit_item_others = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="其他"]')  # 新增人工存入 - 存入項目 - 其他
    manual_deposit_system_notification = (By.XPATH, '//textarea[@placeholder="请输入系统讯息"]')  # 新增人工存入 - 系統訊息
    deposit_amount = (By.XPATH, "//label[text()='存入积分']/..//input[@placeholder='请输入存入积分']")  # 新增人工存入 - 存入積分

    confirm_btn = (By.XPATH, "//div[(@class='el-overlay')and not(contains(@style,'none'))]//button[2]")  # 視窗"確認"鍵

    manual_withdraw = (By.XPATH, "//a[text()=' 人工提出']")  # 積分管理 - 人工提出
    add_manual_withdraw = (By.XPATH, "//span[text()='新增人工提出']")  # "新增人工提出"鍵
    # add_manual_withdraw_title = (By.XPATH, '//div[text()="新增人工提出"]')  # 新增人工提出視窗標題
    manual_withdraw_account_ID = (By.XPATH, '//input[@placeholder="请输入会员帐号"]')  # 新增人工提出 - 會員帳號
    manual_withdraw_search = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small search-button']")  # "搜寻"鍵
    manual_withdraw_item = (By.XPATH, '//label[text()="提出项目"]/..//input')  # 新增人工提出- 提出項目下拉選單
    manual_withdraw_item_select = (By.XPATH, '//div[@aria-hidden="false"]//span[text()="红包误存"]')  # 新增人工提出 - 提出項目 - 红包误存积分
    withdraw_amount = (By.XPATH, "//input[@placeholder='请输入提出积分']")  # 新增人工提出 - 提出積分

    detail_list_id = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")  # 會員帳號ID
    detail_list_deposit_type = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")  # 存入類型
    detail_list_deposit_status = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[6]")  # 狀態
    detail_list_deposit_amount = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[7]")  # 存入積分

    # -----------------------------------------------------
    page_title = (By.XPATH, "//div[@class='page-title']")


class MainPage(BasePage):
    brand = gl.get_value("BRAND")

    def return_admin_version(self):  # 查看Web版本號
        self.open_base_url()
        git_version = self.driver.execute_script("return VITE_LAST_HASH;")
        official_version = self.driver.execute_script("return VITE_APP_VERSION;")
        return f'{official_version} ({git_version})'

    def into_member_list(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_member)
        self.click(MainPageLocator.menu_member_list)
        sleep(3)
        assert self.get_text(MainPageLocator.page_title) == '会员列表', f"進入會員列表有誤"

    def into_member_level(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_member)
        self.click(MainPageLocator.menu_level_list)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '会员层级', f"進入会员层级有誤"

    def into_groups_list(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_groups)
        self.click(MainPageLocator.menu_groups_list)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '群组列表', f"進入群組列表有誤"

    def into_groups_set(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_groups)
        self.click(MainPageLocator.menu_groups_set)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '群组设定', f"進入群組設定有誤"

    def into_groups_own(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_groups)
        self.click(MainPageLocator.menu_groups_own)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '群组建立成员', f"進入群組建立成員有誤"

    def into_share_code(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_groups)
        self.click(MainPageLocator.menu_share_code)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '邀请码管理', f"進入邀请码管理頁有誤"

    def into_group_msg(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_groups)
        self.click(MainPageLocator.menu_group_msg)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '群发讯息', f"進入群發訊息頁有誤"

    def add_share_code(self,share_code, group_name):
        self.into_share_code()
        self.click(MainPageLocator.add_btn)
        self.type(MainPageLocator.add_share_code_input_field, share_code)
        self.type(MainPageLocator.search_bind_group_input_field, group_name)
        self.click(MainPageLocator.search_bind_group_btn)
        self.wait_loading_finish()
        self.click(MainPageLocator.add_bind_group_add_btn)
        self.click(MainPageLocator.set_save)
        self.type(MainPageLocator.search_share_code, share_code)
        self.click(MainPageLocator.search_btn)
        assert self.get_text(MainPageLocator.list_code) == share_code.upper(), f'邀請碼搜尋結果錯誤'
        assert self.get_text(MainPageLocator.list_related_group) == group_name, f'邀請碼對應的群組錯誤'

    def delete_share_code(self, share_code):
        self.refresh_browser()
        self.into_share_code()
        self.type(MainPageLocator.search_share_code, share_code)
        self.click(MainPageLocator.search_btn)
        self.click(MainPageLocator.share_code_list_delete_btn)
        self.click(MainPageLocator.delete_confirm_btn)
        self.wait_loading_finish()
        self.type(MainPageLocator.search_share_code, share_code)
        self.click(MainPageLocator.search_btn)
        assert self.is_element_finded(MainPageLocator.share_code_result_empty), f"邀請碼未正確刪除"

    def modify_share_code(self, share_code, permission=1):
        if not self.is_element_finded(MainPageLocator.all_members_btn):
            self.type(MainPageLocator.search_share_code, share_code)
            self.click(MainPageLocator.search_btn)
            self.click(MainPageLocator.share_code_list_modify_btn)
        if permission == 1:
            self.click(MainPageLocator.all_members_btn)
        elif permission == 2:
            self.click(MainPageLocator.backstage_only_btn)
        else:
            self.click(MainPageLocator.admin_only_btn)

    def into_system_maintenance(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_system)
        self.click(MainPageLocator.menu_system_maintenance)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == 'APP/Web维护', f"進入APP/Web维护有誤"

    def into_system_app_setting(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_system)
        self.click(MainPageLocator.menu_system_app_setting)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == 'APP/Web设定', "進入APP/Web设定有誤"
        assert self.is_element_finded(MainPageLocator.register_with_social_account), "沒有顯示'品牌帳號'選項"
        assert self.is_element_finded(MainPageLocator.geetest), "沒有顯示'極驗'選項"
        assert self.is_element_finded(MainPageLocator.user_contact_whitelist), "沒有顯示'會会员添加好友'選項"

    def enable_geetest(self, enable=True):
        if enable:
            self.click(MainPageLocator.geetest_on)
            if self.is_element_finded(MainPageLocator.save_btn):
                self.click(MainPageLocator.save_btn)
                self.click(MainPageLocator.save_confirm_btn)
        else:
            self.click(MainPageLocator.geetest_off)
            if self.is_element_finded(MainPageLocator.save_btn):
                self.click(MainPageLocator.save_btn)
                self.click(MainPageLocator.save_confirm_btn)

    def check_member_add_friend_tip(self):
        aaa = self.get_text(MainPageLocator.member_add_friend_tip)
        assert self.get_text(MainPageLocator.member_add_friend_tip) == '＊全局设定会员能否主动添加好友', '說明文字錯誤或未顯示'

    # def check_add_friend_by_search_phone_tip(self):
    #     assert self.get_text(MainPageLocator.add_friend_by_search_phone_tip) == '＊是否开放透过手机号搜索添加好友', '說明文字錯誤或未顯示'

    def enable_member_add_friend_setting(self):
        self.wait_loading_finish()
        if not self.is_element_finded(MainPageLocator.page_title) or not self.get_text(MainPageLocator.page_title) == 'APP/Web设定':
            self.click(MainPageLocator.menu_system)
            self.click(MainPageLocator.menu_system_app_setting)
        self.click(MainPageLocator.set_member_add_friend_on)
        self.click(MainPageLocator.save_btn)
        self.click(MainPageLocator.save_confirm_btn)
        assert self.is_element_finded(MainPageLocator.member_add_friend_on_checked), '會員添加好友選項未開啟'
        assert not self.is_element_finded(MainPageLocator.member_add_friend_off_checked), '會員添加好友選項未開啟'

    def disable_member_add_friend_setting(self):
        self.wait_loading_finish()
        if not self.is_element_finded(MainPageLocator.page_title) or not self.get_text(MainPageLocator.page_title) == 'APP/Web设定':
            self.click(MainPageLocator.menu_system)
            self.click(MainPageLocator.menu_system_app_setting)
        self.click(MainPageLocator.set_member_add_friend_off)
        self.click(MainPageLocator.save_btn)
        self.click(MainPageLocator.save_confirm_btn)
        assert self.is_element_finded(MainPageLocator.member_add_friend_off_checked), '會員添加好友選項未關閉'
        assert not self.is_element_finded(MainPageLocator.member_add_friend_on_checked), '會員添加好友選項未關閉'

    def enable_add_friend_by_search_phone(self):
        self.wait_loading_finish()
        if not self.is_element_finded(MainPageLocator.page_title) or not self.get_text(MainPageLocator.page_title) == 'APP/Web设定':
            self.click(MainPageLocator.menu_system)
            self.click(MainPageLocator.menu_system_app_setting)
        self.click(MainPageLocator.search_friend_by_phone_on)
        self.click(MainPageLocator.save_btn)
        self.click(MainPageLocator.save_confirm_btn)
        assert self.is_element_finded(MainPageLocator.search_friend_by_phone_on_checked), '手机号搜索添加好友選項未開啟'
        assert not self.is_element_finded(MainPageLocator.search_friend_by_phone_off_checked), '手机号搜索添加好友選項未開啟'

    def disable_add_friend_by_search_phone(self):
        self.wait_loading_finish()
        if not self.is_element_finded(MainPageLocator.page_title) or not self.get_text(MainPageLocator.page_title) == 'APP/Web设定':
            self.click(MainPageLocator.menu_system)
            self.click(MainPageLocator.menu_system_app_setting)
        self.click(MainPageLocator.search_friend_by_phone_off)
        self.click(MainPageLocator.save_btn)
        self.click(MainPageLocator.save_confirm_btn)
        assert self.is_element_finded(MainPageLocator.search_friend_by_phone_off_checked), '手机号搜索添加好友選項未關閉'
        assert not self.is_element_finded(MainPageLocator.search_friend_by_phone_on_checked), '手机号搜索添加好友選項未關閉'

    def into_system_contact_whitelist_setting(self):
        self.click(MainPageLocator.admin_board)
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_system)
        self.click(MainPageLocator.menu_system_contact_whitelist_setting)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '好友添加白名单设定', f"進入好友添加白名单设定有誤"
        assert self.get_text(MainPageLocator.contact_whitelist_setting_hint) == '＊好友添加设定关闭时，例外白名单内的用户仍可主动添加他人为好友，也可被添加好友', '說明文字錯誤'

    def system_contact_whitelist_setting_show(self):
        self.click(MainPageLocator.admin_board)
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_system)
        return self.is_element_finded(MainPageLocator.menu_system_contact_whitelist_setting)

    def share_code_management_show(self):
        return self.is_element_finded(MainPageLocator.menu_share_code)

    def add_member_to_contact_whitelist(self, add_to_whitelist_member):
        self.click(MainPageLocator.add_new_whitelist_member_btn)
        self.type(MainPageLocator.add_member_page_search_field, add_to_whitelist_member)
        self.click(MainPageLocator.add_member_page_search_btn)
        self.click(MainPageLocator.add_member_page_add_btn)
        self.click(MainPageLocator.set_save)
        self.wait_loading_finish()
        assert self.search_id(add_to_whitelist_member) == add_to_whitelist_member, "搜尋不到該會員ID"

    def delete_member_from_contact_whitelist(self, add_to_whitelist_member):
        self.search_id(add_to_whitelist_member)
        self.click(MainPageLocator.member_delete_btn)
        self.click(MainPageLocator.member_delete_confirm_btn)
        self.wait_loading_finish()
        aaa = self.search_id(add_to_whitelist_member)
        assert self.search_id(add_to_whitelist_member) is None, "搜尋結果錯誤"
        assert self.is_element_finded(MainPageLocator.search_result_is_empty), "搜尋結果錯誤"
        assert self.get_text(MainPageLocator.search_result_is_empty) == '暂无数据', "搜尋結果訊息錯誤"

    def into_discover_setting(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_system)
        self.click(MainPageLocator.discover_setting)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '发现设定', f"進入发现设定頁有誤"

    def get_discover_enable_list(self):
        _list = []
        if self.get_attribute(MainPageLocator.discover_list_0_switch_btn, 'aria-checked') == 'true':
            _list.append(self.get_text(MainPageLocator.discover_list_0_name))
        if self.get_attribute(MainPageLocator.discover_list_1_switch_btn, 'aria-checked') == 'true':
            _list.append(self.get_text(MainPageLocator.discover_list_1_name))
        if self.get_attribute(MainPageLocator.discover_list_2_switch_btn, 'aria-checked') == 'true':
            _list.append(self.get_text(MainPageLocator.discover_list_2_name))
        return _list

    def disable_discover_function(self, total_runs):
        available_numbers = list(range(3))  # 0, 1, 2
        for _ in range(total_runs):
            chosen_numbers = random.sample(available_numbers, total_runs)  # 隨機挑選不重複數字
            btn_locator = getattr(MainPageLocator, f'discover_list_{chosen_numbers[0]}_switch_btn')
            if self.get_attribute(btn_locator, 'aria-checked') == 'true':
                self.click(btn_locator)
                sleep(1)
                index0_status = self.get_attribute(btn_locator, 'aria-checked')
                assert index0_status == 'false', f'預期:false, 實際:{index0_status}'

    def restore_discover_function(self):
        if self.get_attribute(MainPageLocator.discover_list_0_switch_btn, 'aria-checked') == 'false':
            self.click(MainPageLocator.discover_list_0_switch_btn)
        if self.get_attribute(MainPageLocator.discover_list_1_switch_btn, 'aria-checked') == 'false':
            self.click(MainPageLocator.discover_list_1_switch_btn)
        if self.get_attribute(MainPageLocator.discover_list_2_switch_btn, 'aria-checked') == 'false':
            self.click(MainPageLocator.discover_list_2_switch_btn)

    def edit_restore_discover_index0_url(self):
        function_name = self.get_text(MainPageLocator.discover_list_0_name)
        original_url = self.get_text(MainPageLocator.discover_list_0_url)
        self.click(MainPageLocator.discover_list_0_edit_btn)
        sleep(1)
        assert self.get_text(MainPageLocator.discover_edit_title) == '編輯', f'編輯彈窗有誤'
        # =================== 確認原功能訊息顯示正確 ====================
        assert self.get_text(MainPageLocator.discover_edit_function_name) == function_name, f'功能名稱有誤'
        self.type(MainPageLocator.discover_edit_input_url, 'https://gu-chat.com/service.html')
        self.click(MainPageLocator.set_save)
        self.wait_loading_finish()
        # =================== 確認編輯後列表顯示正確 ====================
        assert self.get_text(MainPageLocator.discover_list_0_url) == 'https://gu-chat.com/service.html', f'功能網址有誤'
        # =================== 改回原網址 ==============================
        self.click(MainPageLocator.discover_list_0_edit_btn)
        self.type(MainPageLocator.discover_edit_input_url, original_url)
        self.click(MainPageLocator.set_save)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.discover_list_0_url) == original_url, f'功能網址有誤'

    def into_menu_recode(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_recode)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '聊天记录', f"進入聊天纪录有誤"

    def into_setting_account(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_setting)
        self.click(MainPageLocator.menu_setting_account)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '帐号管理', f"進入帳號管理有誤"

    def into_setting_role(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_setting)
        self.click(MainPageLocator.menu_setting_role)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '角色权限', f"進入角色權限有誤"

    def into_setting_otp(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_setting)
        self.click(MainPageLocator.menu_setting_otp)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == 'OTP管理', f"進入OTP管理有誤"

    def into_setting_otp_operation(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_setting)
        self.click(MainPageLocator.menu_setting_otp_operation)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '运营OTP', f"進入運營OTP有誤"

    def into_logging(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_log_query)
        if self.brand == 'gu':
            self.click(MainPageLocator.menu_operation_log)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '操作日志', f"進入操作日誌有誤"

    def into_red_list(self):
        self.refresh_browser()
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_red)
        self.click(MainPageLocator.menu_red_list)
        sleep(3)
        assert self.get_text(MainPageLocator.page_title) == '红包列表', f"進入紅包列表有誤"

    def into_integral_record(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_integral)
        self.click(MainPageLocator.menu_integral_record)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '积分使用纪录', f"進入積分使用紀錄有誤"

    def into_manual_deposit(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_integral)
        self.click(MainPageLocator.manual_deposit)
        sleep(3)
        assert self.get_text(MainPageLocator.page_title) == '人工存入', f"進入人工存入頁有誤"

    def manual_add_deposit(self, target_id, deposit_amount):
        self.click(MainPageLocator.add_manual_deposit)
        self.type(MainPageLocator.manual_deposit_account_ID, target_id)
        self.click(MainPageLocator.manual_deposit_item_dropdown_list)
        self.click(MainPageLocator.manual_deposit_item_reward_for_reporting)
        self.type(MainPageLocator.deposit_amount, deposit_amount)
        self.click(MainPageLocator.confirm_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.detail_list_id) == target_id, f"會員帳號ID有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_type) == '检举奖金', f"存入類型有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_status) == '成功', f"存入狀態有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_amount) == f'{deposit_amount} (0x)', f"存入積分有誤"

    def manual_add_system_notification(self, target_id, deposit_amount, system_message, deposit_item):
        self.click(MainPageLocator.add_manual_deposit)
        self.type(MainPageLocator.manual_deposit_account_ID, target_id)
        self.click(MainPageLocator.manual_deposit_item_dropdown_list)
        options = {
            0: MainPageLocator.manual_deposit_item_red_envelope,
            1: MainPageLocator.manual_deposit_item_red_envelope_used,
            2: MainPageLocator.manual_deposit_item_reward_for_reporting,
            3: MainPageLocator.manual_deposit_item_others
        }
        if deposit_item in options:
            self.click(options[deposit_item])
        self.type(MainPageLocator.deposit_amount, deposit_amount)
        self.click(MainPageLocator.manual_deposit_system_notification)
        self.type(MainPageLocator.manual_deposit_system_notification, system_message)
        self.click(MainPageLocator.confirm_btn)
        send_system_message_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.wait_loading_finish()
        return send_system_message_time


    def into_manual_withdraw(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_integral)
        self.click(MainPageLocator.manual_withdraw)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '人工提出', f"進入人工提出頁有誤"

    def manual_add_withdraw(self, target_id, withdraw_amount):
        self.click(MainPageLocator.add_manual_withdraw)
        self.type(MainPageLocator.manual_withdraw_account_ID, target_id)
        self.click(MainPageLocator.manual_withdraw_search)
        self.click(MainPageLocator.manual_withdraw_item)
        self.click(MainPageLocator.manual_withdraw_item_select)
        self.type(MainPageLocator.withdraw_amount, withdraw_amount)
        self.click(MainPageLocator.confirm_btn)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.detail_list_id) == target_id, f"會員帳號ID有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_type) == '红包误存', f"提出類型有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_status) == '成功', f"存入狀態有誤"
        assert self.get_text(MainPageLocator.detail_list_deposit_amount) == f'{withdraw_amount} (0x)', f"積分提出有誤"

    def into_red_water(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.menu_red)
        self.click(MainPageLocator.menu_red_water)
        self.wait_loading_finish()
        assert self.get_text(MainPageLocator.page_title) == '水量控制', f"進入水量控制有誤"

    def search_id(self, member_id):
        self.type(MainPageLocator.search_member_ID, member_id)
        self.click(MainPageLocator.search_btn)
        self.wait_loading_finish()
        if self.is_element_finded(MainPageLocator.member_list_ID):
            return self.get_text(MainPageLocator.member_list_ID)
        else:
            return None
