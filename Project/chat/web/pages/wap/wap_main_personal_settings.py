from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.wap.wap_basepage import BasePage

import os, random, re


class PersonalSettingPageLocator:
    # ============================= 導航欄 ==============================================================================
    mainPage_button = (By.XPATH, "//a[@href='/my-page']")  # 導航欄-主頁
    guest_mode_mainPage_button = (By.XPATH, "(//div[@class='flex flex-col items-center py-[8rem]'])[last()]")  # 導航欄-訪客模式"主頁"鍵
    discover_button = (By.XPATH, "//a[@href='/discover']")  # 導航欄-發現

    # ============================= 主頁 > 個人主頁 ======================================================================
    edit_profile_btn = (By.XPATH, "//button[@class=' bg-gray-100 py-[10rem] px-[20rem] rounded-[4rem] text-[15rem] font-semibold' and text()=' 编辑主页 ']")  # 個人主頁-編輯主頁鍵
    share_profile_btn = (By.XPATH, "//button[@class=' bg-gray-100 py-[10rem] px-[20rem] rounded-[4rem] text-[15rem] font-semibold' and text()=' 分享主页 ']")  # 個人主頁-分享主頁鍵
    header_title = (By.XPATH, '//div[@class="w-[80%] text-[16rem] font-bold flex flex-col items-center relative"]')  # 頁面標題

    # ============================= 主頁 > 個人 > 設定頁 =================================================================
    function_btn = (By.XPATH, "//div[@class='w-[24rem] h-[24rem] bg-no-repeat bg-center bg-cover menu-icon']")  # 個人主頁-右上角功能鍵

    # =========== 積分頁 =================================================================
    integral_btn = (By.XPATH, "//p[@class='text-[16rem] font-medium flex-1 ml-[8rem]' and text()='积分']")  # 積分
    remain_integral_amount = (By.XPATH, "//p[@class='text-[16rem] mr-[10rem]']")  # 積分數字

    # =========== 帳號與安全設定頁 =========================================================
    security_btn = (By.XPATH, "//p[@class='text-[16rem] font-medium flex-1 ml-[8rem]' and text()='帐号']")  # 帳號
    logout_btn = (By.XPATH, "//span[text()='登出']")
    logout_confirm_btn = (By.XPATH, "//p[@class='text-[14rem] font-medium' and text()='确定']")
    # -------------------- 修改密碼彈窗 --------------------
    change_pwd_btn = (By.XPATH, "//p[text()='更改密码']")
    change_pwd_old_input = (By.XPATH, "//input[@placeholder='请填写旧密码']")
    change_pwd_new_input = (By.XPATH, "//input[@placeholder='请填写新的密码']")
    change_pwd_new_check_input = (By.XPATH, "//input[@placeholder='请再次填写新的密码']")
    change_pwd_submit = (By.XPATH, "//span[text()='完成']")
    popup_dialog = (By.XPATH, "//div[@class='neutral-50 relative rounded-[8rem] max-h-[90%] flex-col m-auto max-w-[360rem] p-[40rem] w-full']")
    popup_dialog_title = (By.XPATH, "//p[@class='text-[20rem] font-600 break-all grand-1']")
    popup_dialog_confirm = (By.XPATH, "//p[text()='确定']")
    # =========== 黑名單頁 ===============================================================
    blocklist_btn = (By.XPATH, "//p[@class='text-[16rem] font-medium flex-1 ml-[8rem]' and text()='黑名单']")  # 黑名單
    blocklist_search_input = (By.XPATH, "//input[@placeholder='搜索']")  # 黑名單-搜索
    blocklist_search_first = (By.XPATH, "//div[@class='px-[16rem] py-[12rem] flex items-center h-[60rem] bb-1 bg-white-100']") # 黑名單-第一筆搜索結果
    friend_block_page = (By.XPATH, "//p[text()='已加入黑名单，你将不再收到对方的讯息。']")  # 黑名單成員頁
    block_switch_btn = (By.XPATH, "//span[@class='el-switch__core']")  # 黑名單成員頁-黑名單switch開關
    popup_toast = (By.XPATH, '(//p[@class="el-message__content"])[last()]')  # toast標題
    # =========== 分享頁 =================================================================
    share_btn = (By.XPATH, "//p[@class='text-[16rem] font-medium flex-1 ml-[8rem]' and text()='分享']")  # 分享

    # =========== 關於股聊頁 ==============================================================
    about_btn = (By.XPATH, "//p[@class='text-[16rem] font-medium flex-1 ml-[8rem]' and contains(text(),'关于')]")  # 關於股聊
    version_num = (By.XPATH, '//div[contains(@class, "flex items-center justify-between")]/p[@class="text-[14rem]"]')
    service_btn = (By.XPATH, "//p[text()='服务条款']")  # 服務條款
    privacy_btn = (By.XPATH, "//p[text()='隐私权政策']")  # 隱私權政策
    page_title = (By.XPATH,'//*[@id="app"]/div[1]/div[12]/div/div[2]/div')
    back_btn = (By.XPATH, '//*[@id="app"]/div/div[12]/div/div[1]/i')


class PersonalSettingPage(BasePage):
    # ==================================== 主頁-個人頁 ===============================================================
    def into_main_setting_page(self):
        if self.is_element_finded(PersonalSettingPageLocator.mainPage_button):
            self.click(PersonalSettingPageLocator.mainPage_button)
            self.wait_loading_finish()
        if self.is_element_finded(PersonalSettingPageLocator.function_btn):
            self.click(PersonalSettingPageLocator.function_btn)
            self.wait_loading_finish()
        assert self.is_element_finded(PersonalSettingPageLocator.about_btn)

    # ==================================== 主頁-個人頁-積分 ===========================================================
    def into_integral_page(self):
        remain_integral_amount = self.get_text(PersonalSettingPageLocator.remain_integral_amount)
        self.click(PersonalSettingPageLocator.integral_btn)
        self.wait_visibility(PersonalSettingPageLocator.header_title)
        assert self.get_text(PersonalSettingPageLocator.header_title) == '积分详情', f'進入積分頁面有誤'
        return remain_integral_amount

    # ==================================== 主頁-個人頁-帳號 ===========================================================
    def into_security_page(self):
        self.click(PersonalSettingPageLocator.security_btn)
        self.wait_visibility(PersonalSettingPageLocator.header_title)
        assert self.get_text(PersonalSettingPageLocator.header_title) == '帐号与安全', f'進入帳號與安全頁面有誤'

    def change_password(self, old_pwd, new_pwd):

        self.click(PersonalSettingPageLocator.change_pwd_btn)
        self.wait_loading_finish()
        self.type(PersonalSettingPageLocator.change_pwd_old_input, old_pwd)
        self.type(PersonalSettingPageLocator.change_pwd_new_input, new_pwd)
        self.type(PersonalSettingPageLocator.change_pwd_new_check_input, new_pwd)
        self.click(PersonalSettingPageLocator.change_pwd_submit)
        sleep(1)
        if self.is_element_finded(PersonalSettingPageLocator.popup_dialog):
            assert self.get_text(PersonalSettingPageLocator.popup_dialog_title) == '密码重设成功', f'沒有跳出"密码重设成功"toast'
        self.click(PersonalSettingPageLocator.popup_dialog_confirm)

    def logout(self):
        if self.is_element_finded(PersonalSettingPageLocator.logout_btn):
            self.click(PersonalSettingPageLocator.logout_btn)
        if self.is_element_finded(PersonalSettingPageLocator.logout_confirm_btn):
            self.click(PersonalSettingPageLocator.logout_confirm_btn)
        self.wait_loading_finish()
        assert self.is_element_finded(PersonalSettingPageLocator.guest_mode_mainPage_button)
        assert not self.is_element_finded(PersonalSettingPageLocator.discover_button)


    # ==================================== 主頁-個人頁-黑名單 ==========================================================
    def into_blocklist_page(self):
        self.click(PersonalSettingPageLocator.blocklist_btn)
        self.wait_visibility(PersonalSettingPageLocator.header_title)
        current_title = self.get_text(PersonalSettingPageLocator.header_title)
        assert self.get_text(PersonalSettingPageLocator.header_title) == '黑名单', f'進入黑名單頁面有誤'

    def search_blocked_friend(self, name):
        self.type(PersonalSettingPageLocator.blocklist_search_input, name)
        assert self.get_text(PersonalSettingPageLocator.blocklist_search_first) == name, f'找不到黑名單成員'
        self.click(PersonalSettingPageLocator.blocklist_search_first)
        sleep(1)
        assert self.is_element_finded(PersonalSettingPageLocator.friend_block_page), f'未進到黑名單成員頁'

    def unblock_friend(self):
        self.click(PersonalSettingPageLocator.block_switch_btn)
        self.wait_visibility(PersonalSettingPageLocator.popup_toast)
        assert self.get_text(PersonalSettingPageLocator.popup_toast) == '解除黑名单', f"黑名單鍵初始狀態有誤"

        sleep(5)
        self.click(PersonalSettingPageLocator.block_switch_btn)
        self.wait_visibility(PersonalSettingPageLocator.popup_toast)
        assert self.get_text(PersonalSettingPageLocator.popup_toast) == '设为黑名单', f"黑名單狀態切換有誤, 預期設為黑名單"

        sleep(5)
        self.click(PersonalSettingPageLocator.block_switch_btn)
        self.wait_visibility(PersonalSettingPageLocator.popup_toast)
        assert self.get_text(PersonalSettingPageLocator.popup_toast) == '解除黑名单', f"黑名單狀態切換有誤, 預期解除非名單"

    # ==================================== 主頁-個人頁-分享 ===========================================================
    # def into_share_page(self):
    #     self.click(PersonalSettingPageLocator.share_btn)
    #     assert self.get_text(PersonalSettingPageLocator.header_title) == '分享', f'進入分享頁面有誤'

    # ==================================== 主頁-個人頁-關於股聊 ========================================================
    def into_about_page(self):
        about_text = self.get_text(PersonalSettingPageLocator.about_btn)
        self.click(PersonalSettingPageLocator.about_btn)
        self.wait_loading_finish()
        assert self.get_text(PersonalSettingPageLocator.header_title) == about_text, f'進入關於聊天頁面有誤'

    def check_version(self, correct_version):
        if self.is_element_finded(PersonalSettingPageLocator.version_num):
            current_version = self.get_text(PersonalSettingPageLocator.version_num).split(" ")[0]
            assert current_version == correct_version, f'版本錯誤, 目前版本: {current_version} 正確版本: {correct_version}'
        else:
            message = f'找不到版本號'
            raise EOFError(message)

    def check_service(self):
        self.click(PersonalSettingPageLocator.service_btn)
        self.wait_loading_finish()
        title = self.get_text(PersonalSettingPageLocator.page_title)
        assert title == '服务条款', f'服务条款頁面顯示錯誤'
        self.click(PersonalSettingPageLocator.back_btn)

    def check_privacy(self):
        self.click(PersonalSettingPageLocator.privacy_btn)
        self.wait_loading_finish()
        title = self.get_text(PersonalSettingPageLocator.page_title)
        assert title == '隐私权政策', f'隱私權政策頁面顯示錯誤'
        self.click(PersonalSettingPageLocator.back_btn)
