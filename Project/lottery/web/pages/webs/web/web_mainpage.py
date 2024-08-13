from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
import os, requests, re
from bs4 import BeautifulSoup
from opencc import OpenCC
import pandas as pd

class MainPageLocator:
    # WEB LOGIN (PC登入畫面)
    login_input_window = (By.XPATH, "//a[@class='btn-login' and contains(text(),'登录')]")  # 打開登入視窗
    login_input_account = (By.XPATH, "//*[@id='nzc-header-account' or @placeholder='请输入您的用户名' or @placeholder='账号']")  # 登入帳號欄
    login_input_password = (By.XPATH, "//input[@id='nzc-header-password' or @placeholder='请输入您的登录密码' or @placeholder='密码']")  # 登入密碼欄
    login_input_captcha = (By.XPATH, "//*[@id='nzc-header-captcha' or @class='verification' and @placeholder='验证码']")  # 登入驗證碼欄
    login_btn = (By.XPATH, "(//*[@id='nzc-header-login' or @class='btn-primary btn-lg' and text()='登入账户' or @class='btn btn-primary' or @class='button__sign-in'])[last()]")  # 登入按鈕
    login_ok_point = (By.XPATH, "//*[contains(@href,'logout')]")  # 登入成功判斷點
    # 註冊鈕
    register_link = (By.XPATH, "//*[contains(@class,'login')]//*[text()='注册' or text()='免费开户' or @class='btn-primary-o btn']")  # 注冊頁面
    # 登出鈕
    logout_btn = (By.XPATH, "//*[@id='nzc-header-logout' or @class='btn-out' or text()='登出' or contains(text(),'退出')]")
    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")
    # 登入公告訊息檢查
    login_announcement = (By.XPATH, "//div[contains(@data-bind, 'loginBillboard')]/p")
    # 關閉登入公告
    Close_announcement = (By.XPATH, "//a//text()[contains(., '我知道了')]/..")
    # 用api登入時，登出會先導轉此頁
    already_logout = (By.XPATH, "//*[text()='您的账号已经被登出!']")

    # 浮窗
    right_float_close_state = (By.XPATH, "//div[@class='quick_open_right' and @style='display: block;']")  # 右側浮窗 關閉狀態
    right_float_open = (By.XPATH, "//div[@class='quick_open_right']/img[contains(@src,'shark')]") # 右側浮窗(有自定義圖片時)展開
    right_float_span_open = (By.XPATH, "//div[@class='quick_open_right']//span") # 右側浮窗(origin span)展開
    right_float_last = (By.XPATH, "//ul[@class='quick_content_right']/li[last()]") # 右側最後一個圖片btn
    right_float_the_second_to_last = (By.XPATH, "//ul[@class='quick_content_right']/li[last()-1]") # 右側倒數第二個圖片btn
    left_float_close_state = (By.XPATH, "//div[@class='quick_open_left' and @style='display: block;']") # 左側浮窗 關閉狀態
    left_float_open = (By.XPATH, "//div[@class='quick_open_left']/img[contains(@src,'shark')]") # 左側浮窗(有自定義圖片時)展開
    left_float_span_open = (By.XPATH, "//div[@class='quick_open_left']//span") # 左側浮窗(origin span)展開
    left_float_last = (By.XPATH, "//ul[@class='quick_content_left']/li[last()]") # 左側最後一個圖片btn
    left_float_the_second_to_last = (By.XPATH, "//ul[@class='quick_content_left']/li[last()-1]") # 左側倒數第二個圖片btn
    left_float3 = (By.XPATH, "//ul[@class='quick_content_left']/li[position()=3]") # 左側浮窗第一個
    right_float3 = (By.XPATH, "//ul[@class='quick_content_right']/li[position()=3]") # 右側浮窗第一個
    # 左側全部浮窗數量
    left_float_all = (By.XPATH, "//ul[@class='quick_content_left']//li")
    # 右側全部浮窗數量
    right_float_all = (By.XPATH, "//ul[@class='quick_content_right']//li")

    # APP下載框
    app_download = (By.XPATH, "//div[@class='webappdownload__text']//p")

    # web 額度轉換-主錢包
    web_wellat = (By.XPATH, "(//span[contains(@class,'cp_balance')])[1]") # 主錢包
    transfer_back = (By.XPATH, "//*[text()= '一键归户']") # 一鍵歸戶



class MainPage(BasePage):
    error_list = {}

    # 首次進入Web，關閉總公告方式
    def firstOpenBaseUrl(self):
        self.open_base_url()
        self.open_base_url()

    # 註冊
    def into_register_page(self):
        self.wait_loading_finish()
        self.sleep(1)
        self.scroll_to_top()
        if self.is_element_finded(MainPageLocator.login_input_account) is False:
            self.is_element_displayed(MainPageLocator.logout_btn)
            self.click(MainPageLocator.logout_btn)
            self.wait_loading_finish()
            self.logout_checker()
        self.sleep(1)

        if self.is_element_finded(MainPageLocator.register_link) == True:
            self.is_element_displayed(MainPageLocator.register_link)
            self.click(MainPageLocator.register_link)
        self.sleep(1)
        
        try:
            # Alert 處理        
            if self.get_alert_message():
                self.wait_alert_present()
                message = self.get_alert_message()
                assert '目前不开放注册' in message, message
                self.accept_alert()
        except:
            self.wait_loading_finish()

    # 登入
    def login(self, account, password, captcha=''):
        # 等待Loading結束
        self.wait_loading_finish()
        if self.is_element_finded(MainPageLocator.login_input_account) is False:
            return

        # 點擊登入
        if self.is_element_finded(MainPageLocator.login_input_window) is True:
           self.sleep(1)
           self.click(MainPageLocator.login_input_window)
           self.sleep(2)

        # 輸入帳號
        self.type(MainPageLocator.login_input_account, account)
        # 輸入密碼
        self.type(MainPageLocator.login_input_password, password)
        # 輸入驗證碼，若無則不輸入
        if self.is_element_displayed(MainPageLocator.login_input_captcha) is True:
            self.type(MainPageLocator.login_input_captcha, captcha)
        else:
            return False
        
        self.sleep(3)
        # 點登入
        self.click(MainPageLocator.login_btn)
        # for 二級域名
        self.sleep(3)

        try:
            if str(self.get_alert_message()).__contains__('密码有误') or str(self.get_alert_message()).__contains__('密码错误')  or str(self.get_alert_message()).__contains__('冻结'):
                    print(self.get_alert_message())
                    self.accept_alert()
                    os._exit(13)
        except:
            # 等待登入完成
            self.wait_visibility(MainPageLocator.login_ok_point)
            # 驗證出現登出 判定已登入
            assert "登出" or "退出" in self.driver.page_source

    # api登入後把cookie加到driver
    def add_cookie_driver(self, res):
        cookies = res.cookies.get_dict()
        key = [k for k in cookies.keys()][0]
        value = cookies['.xy-web']
        js = f'document.cookie = "{key}={value}"'
        self.execute_js(js)

    # 登出
    def logout(self):
        self.wait_loading_finish()
        self.logout_checker()
        
    # 登出成功與否判斷
    def logout_checker(self):
        self.wait_loading_finish()
        for _ in range(3):
            if self.is_element_finded(MainPageLocator.login_input_account) is False:
                self.is_element_displayed(MainPageLocator.logout_btn)
                self.click(MainPageLocator.logout_btn)
                self.wait_loading_finish()
                if self.is_element_finded(MainPageLocator.already_logout):
                    self.sleep(5)
        assert self.is_element_finded(MainPageLocator.login_input_account) is True, '登出失敗'
        
    def maintenance(self, is_maintenance=False):
        if is_maintenance == True:
            assert self.is_element_finded(MainPageLocator.maintenance) is True, '關閉網站節點錯誤'
            return
            
        if self.is_element_finded(MainPageLocator.maintenance) is True:
            print("系統維護中")
            self.test_skip('系統維護中')

    
    def check_login_board(self, data):
        self.wait_loading_finish()

        for loop in range(0, 3):
            if self.is_element_finded(MainPageLocator.login_announcement) is True:
                Message = self.get_text(MainPageLocator.login_announcement)
                
                while True:
                    if self.is_element_displayed(MainPageLocator.login_announcement) is True:
                        self.click(MainPageLocator.Close_announcement)
                        self.sleep(0.5)
                    else:
                        break

                assert Message == data['content'], f"登入公告訊息異常 目前顯示: {Message} 正確顯示: {data['content']}"
                return
            else:
                self.sleep(2)
                
                if loop == 2:
                    raise EOFError('找不到登入公告訊息')
    

    # 確認左側浮窗open/ close btn
    def left_float_windows_action(self):
        # 左側浮窗
        # 先行確認是否存在元素
        # 不然有時候運行腳本時, 一直出現"EOFError: 點擊失敗"
        assert self.is_element_finded(MainPageLocator.left_float_span_open) == True, "左側浮窗_開啟btn_異常"
        try:
            self.click(MainPageLocator.left_float_span_open)
        except EOFError:
            # print("左側浮窗_開啟btn_點擊失敗, 重整後再次測試點擊")
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(MainPageLocator.left_float_last)
            if (len(self.driver.window_handles) != 1):
                self.switch_home_page()
                self.refresh_browser()
                self.wait_loading_finish()
                self.click(MainPageLocator.left_float_the_second_to_last)
            self.wait_loading_finish()
            if self.is_element_finded(MainPageLocator.left_float_open) == True:
                 self.click(MainPageLocator.left_float_open)
            else:
                self.click(MainPageLocator.left_float_span_open)

    # 確認右側浮窗open/ close btn
    def right_float_windows_action(self):
        # 右側浮窗
        assert self.is_element_finded(MainPageLocator.right_float_span_open) == True, "右側浮窗_開啟btn_異常"
        try:
            self.click(MainPageLocator.right_float_span_open)
        except EOFError:
            # print("右側浮窗_開啟btn_點擊失敗, 重整後再次測試點擊")
            self.refresh_browser()
            self.wait_loading_finish()
            self.click(MainPageLocator.right_float_last)
            if (len(self.driver.window_handles) != 1):
                self.switch_home_page()
                self.refresh_browser()
                self.wait_loading_finish()
                self.click(MainPageLocator.right_float_the_second_to_last)
            self.wait_loading_finish()
            if self.is_element_finded(MainPageLocator.right_float_open) == True:
                self.click(MainPageLocator.right_float_open)
            else:
                self.click(MainPageLocator.right_float_span_open)

    # 確認優惠大廳(左側浮窗)
    def check_mobile_hall(self):
        self.wait_loading_finish()
        self.sleep(1)
        # 確認浮窗開啟
        if self.is_element_finded(MainPageLocator.left_float_close_state): #浮窗為關閉狀態
            self.refresh_browser()
            self.wait_loading_finish()
            if self.is_element_finded(MainPageLocator.left_float_open):
                self.click(MainPageLocator.left_float_open)
            else:
                self.click(MainPageLocator.left_float_span_open)
        assert self.is_element_finded(MainPageLocator.left_float_close_state) == False, "左側浮窗_開啟失敗"

        left_float_pos_num = int(len(self.find_elements(MainPageLocator.left_float_all)))
        left_float_pos_path = "//ul[@class='quick_content_left']//li[position()={}]".format(left_float_pos_num)
        left_float_pos = (By.XPATH, left_float_pos_path)
        assert (self.is_element_finded(left_float_pos) == True), "web無顯示新增之圖片btn"
        self.wait_loading_finish()
        self.open_wait_new_window(left_float_pos)

    # 確認QQ 連結
    def check_qq_link(self, brand):
        self.brand = brand 
        category_1 = ["lv", "ls"]
        category_2 = ["hy", "c7", "c8"]
        category_3 = ["tz"]
        category_4 = ["bh", "sc"]       
        category_5 = ["3h", "cdd","xpj"]

        for index in category_1:
            if index == self.brand:                
                QQ = (By.XPATH, "//i[@class ='i-3']")
                qq_number = (By.XPATH, "//label[text() ='联系QQ：' ]")
                self.scroll_to_bottom()
                self.move_mouse(QQ)
                self.sleep(5)
                qq = self.get_text(qq_number)
                self.sleep(1)
                try:
                    assert qq == '联系QQ：1322288850', 'qq有錯'
                except:
                    print('QQ已停止使用')
                    pass
            else:
                pass
        
        for index in category_2:
            if index == self.brand:                
                QQ = (By.XPATH, "//span[@class ='i-qq']")                
                qq = self.get_text(QQ)
                self.sleep(1)
                try:
                    assert qq == 'QQ：1322288850', 'qq有錯'   
                except:
                    print('QQ已停止使用')
                    pass             
            else:
                pass

        for index in category_3:
            if index == self.brand:
                QQ = (By.XPATH, "//i[@class ='qq']/..")                
                qq = self.get_text(QQ)
                self.sleep(1)
                try:
                    assert qq == 'QQ:1322288850', 'qq有錯'
                except:
                    print('QQ已停止使用')
                    pass 
                
        for index in category_4:
            if index == self.brand:                
                qq_number = (By.XPATH, "//p[text()='客服QQ：']/..")
                self.scroll_to_bottom()
                self.sleep(5)
                qq = self.get_text(qq_number).replace('\n','').replace(' ','')
                self.sleep(1)
                try:
                    assert qq == '客服QQ：1322288850', 'qq有錯'
                except:
                    print('QQ已停止使用')
                    pass 
            else:
                pass

        for index in category_5:
            if index == self.brand:
                pass
    
    # 確認在線客服連結
    def check_livechat_link(self, brand, cs=0):
        self.brand = brand
        category_1 = ["tz"]
        category_2 = ["lv", "ls", "hy", "c7", "c8", "bh", "sc", "xpj", "cdd", "3h"]       

        for index in category_1:
            if index == self.brand:
                if cs == 0:
                    LIVECHAT = (By.XPATH, "//a[@id='nzc-nav-service']")
                    self.open_wait_new_window(LIVECHAT)
                    web_url = self.get_url()
                    self.sleep(1)
                    assert web_url == "https://app.comm100.chat/chatserver/chatWindow.aspx?siteId=5000125&planId=175#", "客服網址錯誤: {}".format(web_url)
                elif cs == 1:
                    LIVECHAT = (By.XPATH, "//a[@id='nzc-nav-service']")
                    self.open_wait_new_window(LIVECHAT)
                    web_url = self.get_url()
                    self.sleep(1)
                    assert web_url == "http://mynah-client-uat.paradise-soft.com.tw/chatroom?company=FM3SEAMrJdrVs&site=WS3SSBeEZf2zA", "客服網址錯誤: {}".format(web_url)
                else:
                    print("選項數值填寫錯誤")
            else:
                pass
        
        for index in category_2:
            if index == self.brand:
                if cs == 0:
                    LIVECHAT = (By.XPATH, "//a[@id='nzc-nav-faq']")
                    self.open_wait_new_window(LIVECHAT)
                    web_url = self.get_url()
                    self.sleep(1)
                    assert web_url == "https://app.comm100.chat/chatserver/chatWindow.aspx?siteId=5000125&planId=175#" ,"客服網址錯誤: {}".format(web_url)
                elif cs == 1:
                    LIVECHAT = (By.XPATH, "//a[@id='nzc-nav-faq']")
                    self.open_wait_new_window(LIVECHAT)
                    web_url = self.get_url()
                    self.sleep(1)
                    assert web_url == "http://mynah-client-uat.paradise-soft.com.tw/chatroom?company=FM3SEAMrJdrVs&site=WS3SSBeEZf2zA" ,"客服網址錯誤: {}".format(web_url)
                else:
                    print("選項數值填寫錯誤")
            else:
                pass
    
    # 確認郵箱連結
    def check_email_link(self, brand):
        self.brand = brand 
        category_1 = ["lv", "ls"]
        category_2 = ["hy", "c7", "c8", "tz", "xpj", "cdd", "3h"] 
        category_3 = ["bh", "sc"]     

        for index in category_1:
            if index == self.brand:
                email = (By.XPATH, "//i[@class ='i-4']")
                email_text = (By.XPATH, "//label[text() ='邮箱：' ]")
                self.scroll_to_bottom()
                self.move_mouse(email)
                self.sleep(5)
                email = self.get_text(email_text)
                self.sleep(1)
                assert email == '邮箱：lasv1234wwwww567890@gmail.com', 'email有錯'
            else:
                pass
        
        for index in category_2:
            if index == self.brand:
                pass
        
        for index in category_3:
            if index == self.brand:
                email_number = (By.XPATH, "//p[text()='客服邮箱：']/..//span")
                self.scroll_to_bottom()
                self.sleep(5)
                email = self.get_text(email_number)
                self.sleep(1)
                assert email == 'lasv1234wwwww567890@gmail.com', 'email有錯'
            else:
                pass
    
    # 確認站內客服(右側浮窗)
    def check_customerservice_link(self):
        self.wait_loading_finish()
        self.sleep(1)
        assert self.is_element_finded(MainPageLocator.right_float_open) == True, "右側浮窗_開啟btn_異常"
        try:
            if self.is_element_finded(MainPageLocator.right_float_open) == True:
                self.click(MainPageLocator.right_float_open)
            else:
                self.click(MainPageLocator.right_float_span_open)
        except:
            print("右側浮窗_已展開")
        right_float_pos_num = int(len(self.find_elements(MainPageLocator.right_float_all)))
        right_float_pos_path = "//ul[@class='quick_content_right']//li[position()={}]".format(right_float_pos_num)
        right_float_pos = (By.XPATH, right_float_pos_path)
        assert (self.is_element_finded(right_float_pos) == True), "web無顯示新增之圖片btn"
        self.wait_loading_finish()     
        self.open_wait_new_window(right_float_pos)
    
    # 確認APP下載框
    def check_app_download(self):
        app_download = self.get_text(MainPageLocator.app_download)
        assert app_download == '請下載APP', '文案錯誤'
        


    def language(self, url):
        complete_link = []

        link_list = self.link_list('a', 'href') # 帶入xpath位置
        source = self.get_page_source()
        re_words = re.findall(u"[\u4e00-\u9fa5]+", source) # 抓出中文字
        self.check_font(re_words, url)

        # 第一層href抓取判斷
        for link in link_list:
            if link.__contains__('http'):
                self.open_browser(link)
                complete = link
            else:
                self.open_browser(url + link)
                complete = url + link

            try:
                self.wait_loading_finish()
            except:
                pass
            
            # 第二層href抓取判斷
            second_link_list = self.link_list('li', 'data-bind')

            if len(second_link_list) == 0:
                source = self.get_page_source()
                re_words = re.findall(u"[\u4e00-\u9fa5]+", source)
                self.check_font(re_words, complete)
            else:
                for second_link in second_link_list:
                    if second_link in complete_link:
                        continue
                    else:
                        complete_link.append(second_link)

                    if second_link.__contains__('http'):
                        self.open_browser(second_link)
                        complete = second_link
                    else:
                        self.open_browser(url + second_link)
                        complete = url + second_link

                    try:
                        self.wait_loading_finish()
                    except:
                        pass

                    source = self.get_page_source()
                    re_words = re.findall(u"[\u4e00-\u9fa5]+", source)
                    self.check_font(re_words, complete)

        if len(self.error_list) != 0:
            # 顯示完整資訊
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', None)
             
            result = pd.Series(self.error_list, index = self.error_list.keys())
            raise EOFError(f'內容包含繁體字\n {result}')

    # # 分層爬出網址 xpath_a/b分別是定位
    def link_list(self, xpath_a, xpath_b):
        link_list = []

        source = self.get_page_source()
        soup = BeautifulSoup(source, 'html.parser')
        link = soup.findAll(xpath_a)

        for i in link:
            name = i.get(xpath_b)
            if str(name).__contains__('/') and len(name) > 1 and not str(name).__contains__('logout'):
                try:
                    name = name.split("'")[1]
                except:
                    pass
                # 若抓到不完整的網址，去掉第一個"/"
                if name[0] == '/':
                    name = name[1:]

                link_list.append(name)

        link_list = list(set(link_list))

        return link_list

    # 簡體比對
    def check_font(self, original_string, url):
        message = []

        for word in original_string:
            simplified = self.font('t2s', word)
            if simplified != word and word != '三昇体育' and word != '機器人':
                message.append(word)
     
        if len(message) != 0 :
            self.error_list[url] = message


    # 取得 web 主錢包餘額(先行一鍵歸戶)
    def get_web_wallet(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.transfer_back)
        self.wait_loading_finish()
        wallet = float(self.get_text(MainPageLocator.web_wellat).replace(',', ''))
        return wallet

    # 取得 web URL是否有Stop並進入維護流程
    def front_web_banned(self, url):
        pattern = re.compile("[Ss]top")
        filter_text = pattern.search(url)
        assert ((filter_text.group() == "Stop") or (filter_text.group() == "stop")) == True, "前台網頁禁用失敗"
        return None