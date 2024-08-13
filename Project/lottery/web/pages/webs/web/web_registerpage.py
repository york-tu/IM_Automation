from selenium.webdriver.common.by import By
import unittest
import random
from pages.webs.web.webs_basepage import BasePage


class RegisterPageLocator:
    member_id_input = (By.XPATH, "//input[@name='ts_account']")
    member_pwd_inpud = (By.XPATH, "//input[@name='ts_password']")
    member_pwd_confirm_input = (By.XPATH, "//input[@name='ts_confirmpassword']")
    member_withdraw_pwd_input = (By.XPATH, "//input[@name='ts_withdrawals']")

    @staticmethod
    def member_withdraw_pwd_num_btn(num):
        return (By.XPATH, "//li[contains(@class,'num_btn') and text()='%s']" % str(num))
    
    member_captcha_input = (By.XPATH, "//input[@class='ipt ipt-code login-popup-input']")
    member_captcha_img = (By.XPATH, "//div[contains(@class,'tip')]//img[contains(@src,'gif')]")
    member_name_input = (By.XPATH, "//input[@name='ts_name']")
    member_mail_input = (By.XPATH, "//input[@name='ts_mail']")
    member_qq_input = (By.XPATH, "//input[@name='ts_qq']")
    member_wechat_input = (By.XPATH, "//input[@name='ts_wechat']")
    member_phone_input = (By.XPATH, "//input[@name='ts_phone']")
    member_recommend_input = (By.XPATH, "//input[@name='ts_aid']")

    member_submit_btn = (By.ID, "registerbtn")
    member_datawrong = (By.XPATH, "//div[@class='s-pop-head']/..//div[@class='text-warning']")
    member_wrong_btn = (By.XPATH, "//div[@class='s-pop-footer']//div[@class='btn-1']")
    # 代理註冊
    agent_id_input = (By.XPATH,"//input[@name='account']")
    agent_pwd_input = (By.XPATH,"//input[@name='password']")
    agent_pwd_confirm_input = (By.XPATH,"//input[@name='confirm']")

    agent_name_input = (By.XPATH, "(//input[@name='name'])[last()]")
    agent_qq_input = (By.XPATH, "//input[@name='qq']")
    agent_phone_input = (By.XPATH, "//input[@name='mobile']")
    agent_captcha_input = (By.XPATH, "//input[@class='ipt ipt-code login-popup-input']")
    agent_captcha_img = (By.XPATH, "(//img[contains(@src,'gif')])[last()]")

    agent_submit_btn = (By.XPATH, "//button[text()='提交']")
    agent_pop = (By.XPATH, "//div[@class='s-pop-container']")
    pop_close = (By.XPATH, "//div[text()='确认']") 

    member_about_us = (By.XPATH,"//*[contains(text(),'关于我们')]")
    # check_about_us=(By.XPATH,"//*[@class='article' ]//*[contains(text(),'关于我们')]")
    check_about_us1 = (By.XPATH,"//*[@class='active' and contains(text(),'关于我们')]")
    check_about_us2 = (By.XPATH,"//*[@class='active']//*[ contains(text(),'关于我们')]")

    member_contact_us = (By.XPATH,"//*[contains(text(),'联系我们')]")
    # check_contact_us=(By.XPATH,"//*[contains(@class,'cont')]//*[contains(text(),'联系我们')]")
    check_contact_us1 = (By.XPATH,"//*[@class='active' and contains(text(),'联系我们')]")
    check_contact_us2 = (By.XPATH,"//*[@class='active']//*[ contains(text(),'联系我们')]")

    member_partners = (By.XPATH,"//div[contains(@class,'links') or (@class='guild')]//*[contains(text(),'联盟合作') or contains(text(),'代理注册') or contains(text(),'合作伙伴')]")
    co_member_partners = (By.XPATH, "//div[contains(@class,'page-tab')]//*[contains(text(),'联盟合作') or contains(text(),'代理注册') or contains(text(),'合作伙伴')]")
    check_partners_register_form = (By.XPATH,"(//fieldset[@class='form-group'])[1]")
    partners_register = (By.XPATH,"//a[contains(text(), '代理注册')]")
    check_partners_register = (By.XPATH,"//li[@class='active']//a[contains(text(), '代理注册')]")
    partners_help = (By.XPATH,"//a[contains(text(), '代理协议')]")
    check_partners_help = (By.XPATH,"//li[@class='active']//a[contains(text(), '代理协议')]")
    partners_plan = (By.XPATH,"//a[contains(text(), '代理方案')]")
    check_partners_plan = (By.XPATH,"//li[@class='active']//a[contains(text(), '代理方案')]")
    partners_login = (By.XPATH,"//a[contains(text(), '代理登入')]")

    member_deposit = (By.XPATH,"//*[contains(text(),'存款帮助')]")
    # check_deposit=(By.XPATH,"//*[@class='cont']//u[contains(text(),'充值')]")
    check_deposit1 = (By.XPATH,"//*[@class='active' and contains(text(),'存款帮助')]")
    check_deposit2 = (By.XPATH,"//*[@class='active']//*[ contains(text(),'存款帮助')]")

    member_withdraw = (By.XPATH,"//*[contains(text(),'取款帮助')]")
    # check_awithdraw=(By.XPATH,"//*[@class='cont']//u[contains(text(),'提款')]")
    check_awithdraw1 = (By.XPATH,"//*[@class='active' and contains(text(),'取款帮助')]")
    check_awithdraw2 = (By.XPATH,"//*[@class='active']//*[ contains(text(),'取款帮助')]")

    member_questions = (By.XPATH,"//*[contains(text(),'常见问题')]")
    # check__questions=(By.XPATH,"//*[@class='cont']//*[contains(text(),'帮助')]")
    check__questions1 = (By.XPATH,"//*[@class='active' and contains(text(),'常见问题')]")
    check__questions2 = (By.XPATH,"//*[@class='active']//*[ contains(text(),'常见问题')]")

    check_admin_login = (By.XPATH, "//h3[contains(text(),'管理系统')]")
    login_ok_point = (By.XPATH, "//div[@class='top-menu']")  # 判斷已登入點   

class RegisterPage(BasePage):
    # captcha=1 驗證碼功能關閉中, 前台注冊頁不會顯示
    # captcha=0 驗證碼功能開啟中, 前台注冊頁會顯示(自定義略過_驗證碼檢查)
    def do_register(self, _id, pwd, brand, withdraw_pwd, name='自動化測試', email='autotest@qq.com', qq='123456', wechat='123456', 
                    aid='cmtest001', captcha=1):
        phone = '13' + str(random.randrange(100000000, 999999999, 9))
        if brand == "co":
            # Bet365_spec設計沒有再注冊頁有這欄位, 預設安全密碼為"123456"
            return 
        if captcha == 1:
            if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
                if self.is_element_finded(RegisterPageLocator.member_captcha_img) is False:
                    # raise EOFError('驗證碼圖片沒出現')    # 有開滑動驗證就不會出現驗證碼
                    self.test_skip('滑動驗證開啟，無法測試')
                self.test_skip('註冊驗證碼開啟，無法測試')

            assert len(withdraw_pwd) == 6, '提款密碼不足六碼'

            self.wait_loading_finish()
        
            # 輸入帳、密、名
            self.type(RegisterPageLocator.member_id_input, _id)
            self.type(RegisterPageLocator.member_pwd_inpud, pwd)
            self.type(RegisterPageLocator.member_pwd_confirm_input, pwd)

            # 輸入提款密碼
            self.click(RegisterPageLocator.member_withdraw_pwd_input)
            for num in str(withdraw_pwd):
                self.click(RegisterPageLocator.member_withdraw_pwd_num_btn(num))

            self.scroll_to_bottom()

            # 會員資料，無欄位則不需填
            if self.is_element_displayed(RegisterPageLocator.member_name_input):
                self.type(RegisterPageLocator.member_name_input, name)
            if self.is_element_displayed(RegisterPageLocator.member_mail_input):
                self.type(RegisterPageLocator.member_mail_input, email)
            if self.is_element_displayed(RegisterPageLocator.member_qq_input):
                self.type(RegisterPageLocator.member_qq_input, qq)
            if self.is_element_displayed(RegisterPageLocator.member_wechat_input):
                self.type(RegisterPageLocator.member_wechat_input, wechat)
            if self.is_element_displayed(RegisterPageLocator.member_phone_input):
                self.type(RegisterPageLocator.member_phone_input, phone)
            if self.is_element_displayed(RegisterPageLocator.member_recommend_input):
                self.type(RegisterPageLocator.member_recommend_input, aid)

            # 送出註冊
            self.click(RegisterPageLocator.member_submit_btn)

            # Alert處理        
            self.wait_alert_present()
            message = self.get_alert_message()
            assert '注册成功' in message, message
            self.accept_alert()
            
            # 註冊完回首頁需Loading
            self.wait_loading_finish()
        
        # captcha=0 驗證碼功能開啟中, 前台注冊頁會顯示(自定義略過_驗證碼檢查)
        elif captcha == 0:
            if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
                if self.is_element_finded(RegisterPageLocator.member_captcha_img) is False:
                    raise EOFError('驗證碼圖片沒出現')
            
            # 輸入帳、密、名
            self.type(RegisterPageLocator.member_id_input, _id)
            self.type(RegisterPageLocator.member_pwd_inpud, pwd)
            self.type(RegisterPageLocator.member_pwd_confirm_input, pwd)

            # 輸入提款密碼
            self.click(RegisterPageLocator.member_withdraw_pwd_input)
            for num in str(withdraw_pwd):
                self.click(RegisterPageLocator.member_withdraw_pwd_num_btn(num))

            self.scroll_to_bottom()

            # 會員資料，無欄位則不需填
            if self.is_element_displayed(RegisterPageLocator.member_name_input):
                self.type(RegisterPageLocator.member_name_input, name)
            if self.is_element_displayed(RegisterPageLocator.member_mail_input):
                self.type(RegisterPageLocator.member_mail_input, email)
            if self.is_element_displayed(RegisterPageLocator.member_qq_input):
                self.type(RegisterPageLocator.member_qq_input, qq)
            if self.is_element_displayed(RegisterPageLocator.member_wechat_input):
                self.type(RegisterPageLocator.member_wechat_input, wechat)
            if self.is_element_displayed(RegisterPageLocator.member_phone_input):
                self.type(RegisterPageLocator.member_phone_input, phone)
            if self.is_element_displayed(RegisterPageLocator.member_recommend_input):
                self.type(RegisterPageLocator.member_recommend_input, aid)

            # 送出註冊
            self.click(RegisterPageLocator.member_submit_btn)

            self.wait_loading_finish()

            # 驗證碼未填入的警告彈窗
            if self.is_element_finded(RegisterPageLocator.member_datawrong) == True:
                alert = self.get_text(RegisterPageLocator.member_datawrong)
                assert str(alert).__contains__("为必填栏位"), "驗證碼警告彈窗內文: %s" % alert
                assert self.is_element_finded(RegisterPageLocator.member_datawrong) == True, "警告彈窗確認鈕錯誤"
                self.click(RegisterPageLocator.member_wrong_btn)

    def about_us(self):
        self.wait_loading_finish()
        self.is_element_finded(RegisterPageLocator.member_about_us) is True, "註冊頁找不到關於我們"
        self.click(RegisterPageLocator.member_about_us)
        self.wait_loading_finish()

        if self.is_element_finded(RegisterPageLocator.check_about_us1) is True:
            assert self.is_element_displayed(RegisterPageLocator.check_about_us1) is True
        else:
            assert self.is_element_displayed(RegisterPageLocator.check_about_us2) is True

    def contains_us(self):
        self.click(RegisterPageLocator.member_contact_us)
        self.wait_loading_finish()
        if self.is_element_finded(RegisterPageLocator.check_contact_us1) is True:
            assert self.is_element_displayed(RegisterPageLocator.check_contact_us1) is True
        else:
            assert self.is_element_displayed(RegisterPageLocator.check_contact_us2) is True

    def partners(self):
        self.click(RegisterPageLocator.member_partners)
        self.wait_loading_finish()
        assert self.is_element_displayed(RegisterPageLocator.partners_register) is True, '進入幫助錯誤'

        self.click(RegisterPageLocator.partners_register)
        self.wait_loading_finish()
        assert self.is_element_displayed(RegisterPageLocator.check_partners_register) is True, '點擊代理註冊下頁面錯誤'

        self.click(RegisterPageLocator.partners_help)
        self.wait_loading_finish()
        assert self.is_element_displayed(RegisterPageLocator.check_partners_help) is True, '點擊代理協議錯誤'

        self.click(RegisterPageLocator.partners_plan)
        self.wait_loading_finish()
        assert self.is_element_displayed(RegisterPageLocator.check_partners_plan) is True, '點擊代理方案錯誤'

        self.open_wait_new_window(RegisterPageLocator.partners_login)
        # assert self.wait_visibility(RegisterPageLocator.check_admin_login),'連結分銷商管理系統錯誤'

    # 代理註冊
    # captcha=1, 驗證碼功能關閉中, 前台注冊頁不會顯示
    # captcha=0, 驗證碼功能啟用中, 前台注冊頁會顯示(自定義略過_驗證碼檢查)
    def doagent_registered(self, _id, pwd, brand, name='自動化測試', qq='123456', captcha=1):
        phone = '13' + str(random.randrange(100000000, 999999999, 9))
        if brand == "co":
            # Bet365已經全部換用全民代理, 注冊代理已經拔除
            return 
        else:
            self.click(RegisterPageLocator.member_partners)
        
        if captcha == 1:
            if self.is_element_displayed(RegisterPageLocator.check_partners_register_form) is True:

                if self.is_element_finded(RegisterPageLocator.agent_captcha_input) is True:
                    if self.is_element_finded(RegisterPageLocator.agent_captcha_img) is False:
                        # raise EOFError('驗證碼圖片沒出現')
                        self.test_skip('滑動驗證開啟，無法測試')

                    self.test_skip('註冊驗證碼開啟，無法測試')
                self.wait_loading_finish()
        
                # 輸入帳、密、名
                self.type(RegisterPageLocator.agent_id_input, _id)
                self.type(RegisterPageLocator.agent_pwd_input, pwd)
                self.type(RegisterPageLocator.agent_pwd_confirm_input, pwd)
                
                self.scroll_to_bottom()

                # 會員資料，無欄位則不需填
                if self.is_element_displayed(RegisterPageLocator.agent_name_input):
                    self.type(RegisterPageLocator.agent_name_input, name)
                if self.is_element_displayed(RegisterPageLocator.agent_qq_input):
                    self.type(RegisterPageLocator.agent_qq_input, qq)
                if self.is_element_displayed(RegisterPageLocator.agent_phone_input):
                    self.type(RegisterPageLocator.agent_phone_input, phone)

                # 送出註冊
                self.click(RegisterPageLocator.agent_submit_btn)

                # Alert/彈窗處理
                self.wait_presence(RegisterPageLocator.agent_pop)
                self.click(RegisterPageLocator.pop_close)

                self.open_wait_new_window(RegisterPageLocator.partners_login)
                
            elif self.is_element_finded(RegisterPageLocator.agent_id_input) == False:
                pass

        elif captcha == 0:
            if self.is_element_displayed(RegisterPageLocator.check_partners_register_form) is True:
                if self.is_element_finded(RegisterPageLocator.agent_captcha_input) is True:
                    if self.is_element_finded(RegisterPageLocator.agent_captcha_img) is False:
                        raise EOFError('驗證碼圖片沒出現')
                    # print("註冊驗證碼開啟，自定義略過")

                # 輸入帳、密、名
                self.type(RegisterPageLocator.agent_id_input, _id)
                self.type(RegisterPageLocator.agent_pwd_input, pwd)
                self.type(RegisterPageLocator.agent_pwd_confirm_input, pwd)
                
                self.scroll_to_bottom()

                # 會員資料，無欄位則不需填
                if self.is_element_displayed(RegisterPageLocator.agent_name_input):
                    self.type(RegisterPageLocator.agent_name_input, name)
                if self.is_element_displayed(RegisterPageLocator.agent_qq_input):
                    self.type(RegisterPageLocator.agent_qq_input, qq)
                if self.is_element_displayed(RegisterPageLocator.agent_phone_input):
                    self.type(RegisterPageLocator.agent_phone_input, phone)

                # 送出註冊
                self.click(RegisterPageLocator.agent_submit_btn)
                self.wait_loading_finish()

                # Alert/彈窗處理
                assert self.is_element_displayed(RegisterPageLocator.agent_pop) == True, "錯誤顯告彈窗未顯示"
                assert self.is_element_displayed(RegisterPageLocator.pop_close) == True, "彈窗確認BTN未顯示"
                self.wait_presence(RegisterPageLocator.agent_pop)
                self.click(RegisterPageLocator.pop_close)

                self.open_wait_new_window(RegisterPageLocator.partners_login)

            elif self.is_element_finded(RegisterPageLocator.agent_id_input) == False:
                pass

    def deposit(self):
        self.click(RegisterPageLocator.member_deposit)
        self.wait_loading_finish()
        if self.is_element_finded(RegisterPageLocator.check_deposit1) is True:
            assert self.is_element_displayed(RegisterPageLocator.check_deposit1) is True
        else:
            assert self.is_element_displayed(RegisterPageLocator.check_deposit2) is True
            
    def withdraw(self):
        self.click(RegisterPageLocator.member_withdraw)
        self.wait_loading_finish()
        if self.is_element_finded(RegisterPageLocator.check_awithdraw1) is True:
            assert self.is_element_displayed(RegisterPageLocator.check_awithdraw1) is True
        else:
            assert self.is_element_displayed(RegisterPageLocator.check_awithdraw2) is True

    def questions(self):
        self.click(RegisterPageLocator.member_questions)
        self.wait_loading_finish()
        if self.is_element_finded(RegisterPageLocator.check__questions1) is True:
            assert self.is_element_displayed(RegisterPageLocator.check__questions1) is True
        else:
            assert self.is_element_displayed(RegisterPageLocator.check__questions2) is True

    # admin 會員資料設定
    def check_Register(self, _id, brand, pwd, withdraw_pwd, name='自動化測試', email='autotest@qq.com', qq='123456', wechat='123456',
                   phone='13500456789', aid='cmtest001', display=0, captcha=1):
        # captcha=1, 驗證碼功能關閉中, 前台注冊頁不會顯示
        # captcha=0, 驗證碼功能啟用中, 前台注冊頁會顯示(自定義略過_驗證碼檢查)
        if captcha == 1:
            if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
                if self.is_element_finded(RegisterPageLocator.member_captcha_img) is False:
                    # raise EOFError('驗證碼圖片沒出現')
                    self.test_skip('滑動驗證開啟，無法測試')

                self.test_skip('註冊驗證碼開啟，無法測試')

            assert len(withdraw_pwd) == 6, '提款密碼不足六碼'

            self.wait_loading_finish()
        
            # 輸入帳、密、名
            self.type(RegisterPageLocator.member_id_input, _id)
            self.type(RegisterPageLocator.member_pwd_inpud, pwd)
            self.type(RegisterPageLocator.member_pwd_confirm_input, pwd)

            if self.is_element_displayed(RegisterPageLocator.member_name_input):
                self.type(RegisterPageLocator.member_name_input, name)

            # 輸入提款密碼
            self.click(RegisterPageLocator.member_withdraw_pwd_input)
            for num in str(withdraw_pwd):
                self.click(RegisterPageLocator.member_withdraw_pwd_num_btn(num))

            self.scroll_to_bottom()
            # 會員資料
            if display == 0:
                # 隱藏
                self.sleep(1)
                self.is_element_displayed(RegisterPageLocator.member_mail_input)
                self.is_element_displayed(RegisterPageLocator.member_qq_input)
                self.is_element_displayed(RegisterPageLocator.member_wechat_input)
                self.is_element_displayed(RegisterPageLocator.member_phone_input)
                self.is_element_displayed(RegisterPageLocator.member_recommend_input)
            elif display == 1:
                # 選填
                self.is_element_displayed(RegisterPageLocator.member_mail_input)
                self.type(RegisterPageLocator.member_qq_input, qq)
                self.is_element_displayed(RegisterPageLocator.member_wechat_input)
                self.type(RegisterPageLocator.member_phone_input, phone)
                self.is_element_displayed(RegisterPageLocator.member_recommend_input)
            elif display == 2:
                # 必填
                self.type(RegisterPageLocator.member_mail_input, email)
                self.type(RegisterPageLocator.member_qq_input, qq)
                self.type(RegisterPageLocator.member_wechat_input, wechat)
                self.type(RegisterPageLocator.member_phone_input, phone)
                self.type(RegisterPageLocator.member_recommend_input, aid)

            # 送出註冊
            self.click(RegisterPageLocator.member_submit_btn)

            # Alert處理       
            self.wait_alert_present()
            message = self.get_alert_message()
            assert '注册成功' in message, message
            self.accept_alert()
        
            # 註冊完回首頁需Loading
            self.wait_loading_finish()
        
        elif captcha == 0:
            if self.is_element_finded(RegisterPageLocator.member_captcha_input) is True:
                try:
                    self.wait_presence(RegisterPageLocator.member_captcha_img)
                except Exception as e:
                    print(e)
                    raise EOFError("驗證碼圖片_XPATH位置錯誤 or 未正確出現")
                # print("註冊驗證碼開啟，自定義略過")
                
            self.wait_loading_finish()

            # 輸入帳、密、名
            self.type(RegisterPageLocator.member_id_input, _id)
            self.type(RegisterPageLocator.member_pwd_inpud, pwd)
            self.type(RegisterPageLocator.member_pwd_confirm_input, pwd)

            if self.is_element_displayed(RegisterPageLocator.member_name_input):
                self.type(RegisterPageLocator.member_name_input, name)

            # 輸入提款密碼
            if brand != "co":
                self.click(RegisterPageLocator.member_withdraw_pwd_input)
                for num in str(withdraw_pwd):
                    self.click(RegisterPageLocator.member_withdraw_pwd_num_btn(num))

            self.scroll_to_bottom()
            # 會員資料
            if display == 0:
                # 隱藏
                self.sleep(1)
                self.is_element_displayed(RegisterPageLocator.member_mail_input)
                self.is_element_displayed(RegisterPageLocator.member_qq_input)
                self.is_element_displayed(RegisterPageLocator.member_wechat_input)
                self.is_element_displayed(RegisterPageLocator.member_phone_input)
                self.is_element_displayed(RegisterPageLocator.member_recommend_input) 
            elif display == 1:
                # 選填
                self.is_element_displayed(RegisterPageLocator.member_mail_input)
                self.type(RegisterPageLocator.member_qq_input, qq)
                self.is_element_displayed(RegisterPageLocator.member_wechat_input)
                self.type(RegisterPageLocator.member_phone_input, phone)
                self.is_element_displayed(RegisterPageLocator.member_recommend_input)
            elif display == 2:
                # 必填
                self.type(RegisterPageLocator.member_mail_input, email)
                self.type(RegisterPageLocator.member_qq_input, qq)
                self.type(RegisterPageLocator.member_wechat_input, wechat)
                self.type(RegisterPageLocator.member_phone_input, phone)
                self.type(RegisterPageLocator.member_recommend_input, aid)

            # 送出註冊
            self.click(RegisterPageLocator.member_submit_btn)
            self.wait_loading_finish()

            assert self.is_element_displayed(RegisterPageLocator.agent_pop) == True, "錯誤顯告彈窗未顯示"
            assert self.is_element_displayed(RegisterPageLocator.pop_close) == True, "彈窗確認BTN未顯示"
            self.wait_presence(RegisterPageLocator.agent_pop)
            self.click(RegisterPageLocator.pop_close)

        

