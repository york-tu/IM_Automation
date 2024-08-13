import os
from selenium.webdriver.common.by import By
from Project.mynah.pages.web.webs_basepage import WebBasePage


class ChannelLocator:
    logout_btn = (By.XPATH, "//*[@id='nzc-header-logout' or @class='btn-out' or text()='登出' or contains(text(),'退出')]")     #登出按鈕
    login_input_window = (By.XPATH, "//a[@class='btn-login' and contains(text(),'登录')]")  # 打開登入視窗
    login_input_account = (By.XPATH, "//*[@id='nzc-header-account' or @placeholder='请输入您的用户名' or @placeholder='账号']")  # 登入帳號欄
    login_input_password = (By.XPATH, "//input[@id='nzc-header-password' or @placeholder='请输入您的登录密码' or @placeholder='密码']")  # 登入密碼欄
    login_input_captcha = (By.XPATH, "//*[@id='nzc-header-captcha' or @class='verification' and @placeholder='验证码']")  # 登入驗證碼欄
    login_btn = (By.XPATH, "(//*[@id='nzc-header-login' or @class='btn-primary btn-lg' and text()='登入账户' or @class='btn btn-primary' or @class='button__sign-in'])[last()]")  # 登入按鈕
    login_chagnepwd_btn = (By.XPATH, "//a[contains(text(),'暂不修改')]")  # 更換密碼彈窗按鈕
    login_billboard_btn = (By.XPATH, "//a[@class='btn']")  # 登入公告確定鈕
    login_ok_point = (By.XPATH, "//*[contains(@href,'logout')]")  # 登入成功判斷點
    channel_right_extend = (By.XPATH, "//div[@class='quick_open_right' and @style='display: none;']")       #右側浮窗展開(浮窗有展開時找的到)
    right_float_open = (By.XPATH, "//div[@class='quick_open_right']/img[contains(@src,'shark')]")           #右側浮窗(有自定義圖片時) 展開
    right_float_span_open = (By.XPATH, "//div[@class='quick_open_right']//span")                            #右側浮窗(origin span)   展開
    channel_to_mynah = (By.XPATH, "//ul[@class='quick_content_right']/li[@class='block'][2]")               #右側浮窗連結
    channel_to_mynah_sec = (By.XPATH, "//ul[@class='quick_content_right']/li[position()=3]")
    right_float_all = (By.XPATH, "//ul[@class='quick_content_right']//li")                                  # 右側全部浮窗數量


class WebChannelPage(WebBasePage):
    # 品牌端登入
    def channel_login(self,account,password,captcha=''):    
        if self.is_element_finded(ChannelLocator.logout_btn) is True:
            return

        # 點擊登入
        if self.is_element_finded(ChannelLocator.login_input_window) is True:
           self.sleep(1)
           self.click(ChannelLocator.login_input_window)
           self.sleep(2)

        # 輸入帳號
        self.type(ChannelLocator.login_input_account, account)
        # 輸入密碼
        self.type(ChannelLocator.login_input_password, password)
        # 輸入驗證碼，若無則不輸入
        if self.is_element_finded(ChannelLocator.login_input_captcha) is True:
            self.type(ChannelLocator.login_input_captcha, captcha)
        
        self.sleep(3)
        # 點登入
        self.click(ChannelLocator.login_btn)
        # for 二級域名
        self.sleep(3)

        try:
            if str(self.get_alert_message()).__contains__('密码有误') or str(self.get_alert_message()).__contains__('密码错误')  or str(self.get_alert_message()).__contains__('冻结'):
                    print(self.get_alert_message())
                    self.accept_alert()
                    os._exit(13)
        except:
            # 等待登入完成
            self.wait_visibility(ChannelLocator.login_ok_point)
            # 驗證出現登出 判定已登入
            assert "登出" or "退出" in self.driver.page_source
        
        self.close_change_pwd()
        self.close_login_board()

    # 關閉更換密碼彈窗
    def close_change_pwd(self):        
        for _ in range(3):
            while True:
                
                if self.is_element_displayed(ChannelLocator.login_chagnepwd_btn) is True:
                    self.click(ChannelLocator.login_chagnepwd_btn)
                else:
                    break
                    
            self.sleep(0.5)

    # 關閉登入公告
    def close_login_board(self):
        self.sleep(2)
        while self.is_element_displayed(ChannelLocator.login_billboard_btn):
            self.click(ChannelLocator.login_billboard_btn)

    # 連結客服寶
    def mynah_connect(self):
        try:
            self.sleep(2)
            if self.is_element_finded(ChannelLocator.channel_right_extend) is False:
                if self.is_element_finded(ChannelLocator.right_float_open) == True:
                    self.click(ChannelLocator.right_float_open)
                else:
                    self.click(ChannelLocator.right_float_span_open)

            right_float_pos_num = int(len(self.find_elements(ChannelLocator.right_float_all)))
            if right_float_pos_num==5:
                self.click(ChannelLocator.channel_to_mynah)
            else:
                self.click(ChannelLocator.channel_to_mynah_sec)

            self.switch_last_page()
        except:
            raise EOFError('品牌端連結客服寶失敗')