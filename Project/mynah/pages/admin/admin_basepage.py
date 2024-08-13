import sys
import os
import random
from selenium.webdriver.common.by import By
from common.web.common import Common

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)


class BasePageLocator:
    login_input_account = (By.XPATH, "//input[@placeholder='请输入使用者名称']")  # 登入帳號欄
    login_input_password = (By.XPATH, "//input[@placeholder='请输入密码']")  # 登入密碼欄
    login_btn = (By.XPATH, "//button[@class='el-button login-theme el-button--primary']")  # 登入按鈕
    main_tip_btn = (By.XPATH, "//div[@class='el-message-box__btns']/button")  # 首頁提示確定鈕
    btn_admin_name = (By.XPATH, "//div[@class='navbar mynah-nav']//span[@class='el-tag el-tag--light']")  # 右上角暱稱按鈕
    btn_logout = (By.XPATH, "//span[text()='登出']")
    left_dashboard = (By.XPATH, "//div[@class='el-scrollbar__view']//span[text()='仪表板']")  # 左側儀錶板

    alert_net_error = (By.XPATH, "//p[text()='*检测到您当前的网络环境不稳定, 可能造成部分功能不可用, 请检查确认*']")
    alert_operation_error = (By.XPATH, "//p[text()='操作错误']")


class AdminBasePage(Common):

    # 組合Xpath
    def mix_xpath(self, locator, text):
        return str(locator + text + "']")

    # 開新分頁 關原分頁
    def close_and_chang_window(self):
        # js = "window.open('"+ BasePageLocator.URL_MYNAH_UAT +"');"
        self.execute_js("window.open()")
        self.close_browser()  # 關掉原本的分頁
        self.switch_last_page()  # 轉換為新的分頁

    # 後台登入
    def admin_login(self, account, password):
        self.wait_visibility(BasePageLocator.login_input_account)
        self.type(BasePageLocator.login_input_account, account)
        self.type(BasePageLocator.login_input_password, password)
        self.click(BasePageLocator.login_btn)
        try:
            self.wait_visibility(BasePageLocator.main_tip_btn)
        except:
            raise EOFError("後台登入失敗")
        self.sleep(2)
        self.click(BasePageLocator.main_tip_btn)  # 關閉提示

    # 後台登出
    def admin_logout(self):
        self.click(BasePageLocator.left_dashboard)
        self.sleep(1)
        self.click(BasePageLocator.btn_admin_name)
        self.wait_visibility(BasePageLocator.btn_logout)
        self.click(BasePageLocator.btn_logout)
        try:
            self.wait_visibility(BasePageLocator.login_btn)
            self.refresh_browser()
        except:
            raise EOFError("後台登出失敗")

    # 關閉連線已建立提示
    def close_main(self):
        self.refresh_browser()
        try:
            self.wait_visibility(BasePageLocator.main_tip_btn)
            self.click(BasePageLocator.main_tip_btn)
        except:
            raise EOFError("關閉連線已建立提示 失敗")

    def random_read_file(self):
        files_name_list = ['Message1.txt', 'Message2.txt', 'Message3.txt', 'Message5.txt',
                           'Message6.txt', 'Message7.txt', 'Message8.txt', 'Message9.txt']
        ranFile = '/pages/files/' + random.choice(files_name_list)

        path = root_path + ranFile
        file_object = open(path, 'r', encoding="utf-8")
        # file_object = open('./Project/mynah/pages/files/Message1.txt','r',encoding="utf-8")
        try:
            file_context = file_object.read().replace('\n', ' ')
        finally:
            file_object.close()
        return file_context

    def read_random_words(self):

        file_object = open(root_path + '/pages/files/Message10.txt', 'r', encoding="utf-8")
        try:
            file_context = file_object.read().replace('\n', ' ')
            file_words = ''.join(random.sample(file_context, random.randint(2, 6)))
        finally:
            file_object.close()
        return file_words

    def check_operation_error(self):
        self.sleep(1)
        if self.is_element_finded(BasePageLocator.alert_operation_error) == True:
            raise EOFError('操作錯誤')
