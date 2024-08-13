from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import os, platform, datetime
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import requests, json
import re


class WebsiteSettingLocator():
    # 表單設定-會員註冊
    btn_member_registered_enable = (By.XPATH, "//input[@name='member' and @value='1']")  # 會員註冊啟用
    btn_member_registered_disable = (By.XPATH, "//input[@name='member' and @value='0']")  # 會員註冊禁用
    btn_member_registered_default_level = (By.XPATH, "//span[@id='select2-chosen-2']")  # 默認級別
    member_registered_default_level = (By.XPATH, "//input[@id='s2id_autogen2_search']") # 輸入級別位置
    agent = (By.XPATH, "//input[@data-bind='value:agentlogin']")  # 現金代理

    # 表單設定-會員試玩(不用測試 只要測點擊沒問題)
    btn_member_play_enable = (By.XPATH, "//input[@name='membertrial' and @value='1']")  # 會員試玩啟用
    btn_member_play_disable = (By.XPATH, "//input[@name='membertrial' and @value='0']")  # 會員試玩禁用
    btn_member_play_default_level = (By.XPATH, "//span[@id='select2-chosen-4']")  # 默認級別
    member_play_default_level  = (By.XPATH, "//input[@id='s2id_autogen4_search']")  # 輸入級別位置

    # 表單設定-會員聯盟(不用測試 只要測點擊沒問題)
    btn_member_alliance_enable = (By.XPATH, "//input[@name='affiliate' and @value='1']")  # 會員聯盟啟用
    btn_member_alliance_disable = (By.XPATH, "//input[@name='affiliate' and @value='0']")  # 會員聯盟禁用

    # 表單設定-代理注冊
    btn_agent_registered_enable = (By.XPATH, "//input[@name='agent' and @value='1']")  # 代理註冊啟用
    btn_agent_registered_disable = (By.XPATH, "//input[@name='agent' and @value='0']")  # 代理註冊禁用
    agent_url = (By.XPATH, "//input[@data-bind='value:resellerurl']")  # 代理登錄
    do_mainpromotion_url = (By.XPATH, "//input[@data-bind='value:domainpromotion']")  # 推廣域名

    # 表單設定-滑動驗證
    btn_slide_verified_enable = (By.XPATH, "//input[@name='geetestenable' and @value='1']")  # 滑動驗證禁用
    btn_slide_verified_disable = (By.XPATH, "//input[@name='geetestenable' and @value='0']")  # 滑動驗證禁用

    # 表單設定-站點狀態
    btn_status_enable = (By.XPATH, "//input[@name='status' and @value='1']")  # 站點狀態啟用
    btn_status_disable = (By.XPATH, "//input[@name='status' and @value='0']") # 站點狀態禁用
    status_notice = (By.XPATH, "//textarea[@data-bind='value: notice']") # 關站公告
    btn_status_auto_disable = (By.XPATH, "//input[@name='status' and @value='2']") # 站點狀態自動維護
    start_maintenance_time = (By.XPATH, "//input[@data-bind='datetime: startmaintenancetime']") #站點狀態維護時間
    status_text = (By.XPATH, "//label[contains(text(),'站点状态')]/..//label[@class='radio-inline'][2]") # 已禁用

    # 表單設定-手機優惠大廳連接
    mobile_hall_url = (By.XPATH, "//input[@data-bind='value: linkurl']")  # 手機優惠大廳連結
    default_generalagent = (By.XPATH, "//input[@data-bind='value: generalagentlogin']")  # 默認總代

    # 表單設定-真實姓名設定/ 手機設定/ 郵箱設定/ QQ號碼設定/ 微信設定/ 推薦人設定
    real_name_setting_hide = (By.XPATH, "//input[@name='memberregistername' and @value='0']")  # 真實姓名設定隱藏
    real_name_setting_option = (By.XPATH, "//input[@name='memberregistername' and @value='1']")  # 真實姓名設定顯示且選填
    real_name_setting_necessary = (By.XPATH, "//input[@name='memberregistername' and @value='2']")  # 真實姓名設定顯示且必填
    phone_setting_hide = (By.XPATH, "//input[@name='memberregisterphone' and @value='0']")  # 手機設定隱藏
    phone_setting_option = (By.XPATH, "//input[@name='memberregisterphone' and @value='1']")  # 手機設定顯示且選填
    phone_setting_necessary = (By.XPATH, "//input[@name='memberregisterphone' and @value='2']")  # 手機設定顯示且必填
    email_setting_hide = (By.XPATH, "//input[@name='memberregisteremail' and @value='0']")  # 郵箱設定隱藏
    email_setting_option = (By.XPATH, "//input[@name='memberregisteremail' and @value='1']")  # 郵箱設定顯示且選填
    email_setting_necessary = (By.XPATH, "//input[@name='memberregisteremail' and @value='2']")  # 郵箱設定顯示且必填
    qq_setting_hide = (By.XPATH, "//input[@name='memberregisterqq' and @value='0']")  # QQ號碼設定隱藏
    qq_setting_option = (By.XPATH, "//input[@name='memberregisterqq' and @value='1']")  # QQ號碼設定顯示且選填
    qq_setting_necessary = (By.XPATH, "//input[@name='memberregisterqq' and @value='2']")  # QQ號碼設定顯示且必填
    wechat_setting_hide = (By.XPATH, "//input[@name='memberregisterwechat' and @value='0']")  # 微信帳號設定隱藏
    wechat_setting_option = (By.XPATH, "//input[@name='memberregisterwechat' and @value='1']")  # 微信帳號設定顯示且選填
    wechat_setting_necessary = (By.XPATH, "//input[@name='memberregisterwechat' and @value='2']")  # 微信帳號設定顯示且必填
    recommend_setting_hide = (By.XPATH, "//input[@name='memberrecommend' and @value='0']")  # 推薦人設定隱藏
    recommend_setting_option = (By.XPATH, "//input[@name='memberrecommend' and @value='1']")  # 推薦人設定顯示且選填
    recommend_setting_necessary = (By.XPATH, "//input[@name='memberrecommend' and @value='2']")  # 推薦人設定顯示且必填

    # 表單設定-額度轉換顯示設定
    transfer_display = (By.XPATH, "//input[@name='transferstatus' and @value='0']")  # 一律顯示
    transfer_not_show = (By.XPATH, "//input[@name='transferstatus' and @value='1']")  # 不顯示
    btn_transfer_display = (By.XPATH, "//input[@name='transferstatus' and @value='2']")  # 顯示當金額少於
    transfer_amount = (By.XPATH, "//input[@data-bind='value: transferamount, attr: { disabled: transferstatus() != 2}']")  # 當金額少於輸入框

    # 表單設定-報表設定
    member_warning = (By.XPATH, "//input[@data-bind='value: memberwinthreshold']") #會員預警
    member_warning_text = (By.XPATH, "//input[@data-bind='value: memberwinthreshold']/..")

    # 表單設定-超時登出
    member_timeout = (By.XPATH, "//input[@data-bind='value: membertimeout']") # 會員系統
    user_timeout = (By.XPATH, "//input[@data-bind='value: usertimeout']") # 營運系統
    reseller_timeout = (By.XPATH, "//input[@data-bind='value: resellertimeout']") # 代理系統
    lock_timeout = (By.XPATH, "//input[@data-bind='value: locktimeout']") # 帳號自動解鎖

    submit = (By.XPATH, "//button[@data-y2='submit']") # 保存
    esc = (By.XPATH, "//button[@data-y2='esc']")# 返回
    open_close_1 = (By.XPATH,"(//a[@data-original-title='展开/关闭'])[1]") # 展開/關閉

    # 在線客服管理
    customer_service_live_chat_link = (By.XPATH, "//label[@class='radio-inline']//input[@value='live_chat']") # 在線客服radiobox(單選)
    customer_service_link = (By.XPATH, "//label[@class='radio-inline']//input[@value='customer_service']") # 站內客服radiobox(單選)
    wechat_qrcode = (By.XPATH, "//input[@type='file']") # 微信二維碼
    wechat_qrcode_delete = (By.XPATH, "//button[text()='删除']") # 微信二維碼刪除
    wechat_prompt_text = (By.XPATH, "//body[@contenteditable]") # 微信提示文案
    qq_number = (By.XPATH, "//input[@data-bind='value: filter.qq']") # QQ號碼
    livechat = (By.XPATH,  "//input[@data-bind='value: filter.livechat']") # 在線客服
    email = (By.XPATH, "//input[@data-bind='value: filter.email']") # 郵箱
    customer_service = (By.XPATH, "//input[@data-bind='value: filter.customerservice']") # 站內客服
    submit_livechat = (By.XPATH, "//button[@id='btnSearch']")  # 保存
    open_close_2 = (By.XPATH,"(//a[@data-original-title='展开/关闭'])[2]") # 展開/關閉
    customer_service_type_livechat = (By.XPATH, "//div[@class='col-md-4']//label//input[@value='live_chat']") # 在線客服
    customer_service_type_webside = (By.XPATH, "//div[@class='col-md-4']//label//input[@value='customer_service']") # 站內客服

    # APP輸入框設定
    app_download_prompt_text = (By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']") # APP下載提示框
    submit_app = (By.XPATH, "//form[@data-context='appDownloadPrompt']//button[@class='btn blue']")  # 保存
    esc_app = (By.XPATH, "(//button[text()='返回'])[2]")  # 返回
    # 處理script資料
    # elem = (By.XPATH,"//div[@class='page-container']")
    elem = (By.XPATH, "(//div[@class='page-container']//script[@type='text/javascript'])[2]")



#登入動作
class WebsiteSettingPage(BasePage):
    # 會員註冊
    def member_registered(self, agent, setting=True, level='二'):
        if setting == False:
            # 禁用
            self.click(WebsiteSettingLocator.btn_member_registered_disable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        elif setting == True:
            # 啟用
            self.click(WebsiteSettingLocator.btn_member_registered_enable)
            self.click(WebsiteSettingLocator.btn_member_registered_default_level)
            self.type(WebsiteSettingLocator.member_registered_default_level, level)
            self.type_enter(WebsiteSettingLocator.member_registered_default_level)
            self.type(WebsiteSettingLocator.agent, agent)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)       

    # 會員試玩
    def memeber_play_setting(self, setting=True, level='二'):
        # 禁用
        if setting == False:
            self.click(WebsiteSettingLocator.btn_member_play_disable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit) 
        # 啟用
        elif setting == True:
            self.click(WebsiteSettingLocator.btn_member_play_enable)
            self.click(WebsiteSettingLocator.btn_member_play_default_level)
            self.type(WebsiteSettingLocator.member_play_default_level, level)
            self.type_enter(WebsiteSettingLocator.member_play_default_level)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
    
    # 會員聯盟
    def member_alliancr(self, setting=True):
        # 禁用
        if setting == False:
            self.click(WebsiteSettingLocator.btn_member_alliance_disable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit) 
        # 啟用
        elif setting == True:
            self.click(WebsiteSettingLocator.btn_member_alliance_enable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)

    # 代理註冊
    def agent_registered(self, brand, setting=True, url='54.65.82.189:8005'):
        # 禁用
        if setting == False:
            self.click(WebsiteSettingLocator.btn_agent_registered_disable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit) 
        # 啟用
        elif setting == True:
            self.click(WebsiteSettingLocator.btn_agent_registered_enable)
            address = "http://{}-reseller-uat.paradise-soft.com.tw".format(brand)        
            self.type(WebsiteSettingLocator.agent_url, address)
            self.type(WebsiteSettingLocator.do_mainpromotion_url, url)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)

    # 滑動驗證
    def slide_verified(self, setting=True):
        # 禁用
        if setting == False:
            self.click(WebsiteSettingLocator.btn_slide_verified_disable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit) 
        # 啟用
        elif setting == True:
            self.click(WebsiteSettingLocator.btn_slide_verified_enable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)

    # 滑動驗證_on/ off confirm
    def slide_confirm(self, target, status):
        # 確認回傳值是否符合情境
        if target == True:
            assert status == None, "滑動驗證關閉錯誤"
        elif target == False:
            assert status == False, "滑動驗證開啟錯誤"

    # 站點維護
    def status_setting(self, setting=1, time='2019-10-08 20:00', notice="系统正在进行日常维护"):
        # 禁用
        if setting == 0:
            self.click(WebsiteSettingLocator.btn_status_disable)
            self.type(WebsiteSettingLocator.status_notice, notice)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        # 啟用
        elif setting == 1:
            self.click(WebsiteSettingLocator.btn_status_enable)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)       
        # 自動維護
        elif setting == 2:
            self.click(WebsiteSettingLocator.btn_status_auto_disable)
            self.type(WebsiteSettingLocator.start_maintenance_time, time)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
            self.sleep(8)
            self.refresh_browser()
            
    # 確認自動維護>禁用
    def check_status(self):
        assert self.is_element_selected(WebsiteSettingLocator.btn_status_disable) is True, '未選擇已禁用'

    # 手機優惠大廳
    def mobile_hall(self):
        self.type(WebsiteSettingLocator.mobile_hall_url, "https://www.google.com.tw/?hl=zh-TW")
        self.sleep(1)
        self.type(WebsiteSettingLocator.default_generalagent, "ccp88888")
        self.scroll_to_element(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
    
    # 真實姓名/ 手機/ 郵箱/ QQ號碼/ 微信/ 推薦人設定
    def registered_setting(self, setting=0):
        if setting == 0:
            # 隱藏
            self.click(WebsiteSettingLocator.real_name_setting_hide) # 真實姓名隱藏
            self.click(WebsiteSettingLocator.phone_setting_hide) # 手機隱藏
            self.click(WebsiteSettingLocator.email_setting_hide) # 郵箱隱藏
            self.click(WebsiteSettingLocator.qq_setting_hide) # QQ隱藏
            self.click(WebsiteSettingLocator.wechat_setting_hide) # 微信隱藏
            self.click(WebsiteSettingLocator.recommend_setting_hide)   # 推薦人隱藏
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        elif setting == 1:
            # 選填
            self.click(WebsiteSettingLocator.real_name_setting_option) # 真實姓名選填
            self.click(WebsiteSettingLocator.phone_setting_option) # 手機選填
            self.click(WebsiteSettingLocator.email_setting_option) # 郵箱選填
            self.click(WebsiteSettingLocator.qq_setting_option) # QQ選填
            self.click(WebsiteSettingLocator.wechat_setting_option) # 微信選填
            self.click(WebsiteSettingLocator.recommend_setting_option)   # 推薦人選填
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        elif setting == 2:
            # 必填
            self.click(WebsiteSettingLocator.real_name_setting_necessary)  # 真實姓名必填
            self.click(WebsiteSettingLocator.phone_setting_necessary) # 手機必填
            self.click(WebsiteSettingLocator.email_setting_necessary) # 郵箱必填
            self.click(WebsiteSettingLocator.qq_setting_necessary) # QQ必填
            self.click(WebsiteSettingLocator.wechat_setting_necessary) # 微信必填
            self.click(WebsiteSettingLocator.recommend_setting_necessary)   # 推薦人必填
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
    
    # 額度轉換顯示設定
    def transfer_status(self, setting=0):
        if setting == 0:
            self.click(WebsiteSettingLocator.transfer_display)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        elif setting == 1:
            self.click(WebsiteSettingLocator.transfer_not_show)
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)
        elif setting == 2:
            self.click(WebsiteSettingLocator.btn_transfer_display)
            self.type(WebsiteSettingLocator.transfer_amount, "100")
            self.scroll_to_element(WebsiteSettingLocator.submit)
            self.click(WebsiteSettingLocator.submit)

    # 報表設定
    def member_warning(self, brand):
        self.type(WebsiteSettingLocator.member_warning, "100")
        self.scroll_to_element(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
        self.refresh_browser()
        self.wait_loading_finish()
        # 處理script資料
        code = self.get_attribute(WebsiteSettingLocator.elem, "innerHTML")
        soup = BeautifulSoup(code, 'html.parser')
        scripts = soup.find_all('script') # 找出所有script標籤
        items = str(soup.string)  # 取最後一個
        item = items.split("=")[1][:-2] # 去除var item跟;
        dic = json.loads(item)
        assert dic['memberwinthreshold'] == 100, "數字沒有吃到"   

    # 超時登出-會員系統
    def member_timeout_setting(self, time=0):
        self.scroll_to_element(WebsiteSettingLocator.member_timeout)
        self.type(WebsiteSettingLocator.member_timeout, time)
        # 要點擊2次離開輸入框
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
    
    # 超時登出-營運系統
    def user_timeout_setting(self, time=0):
        self.scroll_to_element(WebsiteSettingLocator.user_timeout)
        self.type(WebsiteSettingLocator.user_timeout, time)
        # 要點擊2次離開輸入框
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)

    # 秒數計算
    def counter_time(self):
        time = datetime.datetime.now()
        return time

    # 超時登出-營運系統_秒數檢測
    def auto_logout_time_check(self, check_time=60, start_time=0, end_time=0):
        diff_time = (end_time - start_time).seconds
        check_time = check_time + 10    # 多10秒
        assert diff_time <= check_time, "ADMIN_秒數自動登出失效"
    
    # 超時登出-代理系統
    def reseller_timeout(self, time=0):
        self.scroll_to_element(WebsiteSettingLocator.reseller_timeout)
        self.type(WebsiteSettingLocator.reseller_timeout, time)
        # 要點擊2次離開輸入框
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
    
    # 超時登出-帳號自動解鎖
    def lock_timeout(self, time=0):
        self.scroll_to_element(WebsiteSettingLocator.lock_timeout)
        self.is_element_displayed(WebsiteSettingLocator.lock_timeout)
        self.type(WebsiteSettingLocator.lock_timeout, time)
        # 要點擊2次離開輸入框
        self.click(WebsiteSettingLocator.submit)
        self.click(WebsiteSettingLocator.submit)
        self.refresh_browser()
        # 處理script資料
        code = self.get_attribute(WebsiteSettingLocator.elem, "innerHTML")
        soup = BeautifulSoup(code, 'html.parser')
        # items = str(soup.script.string)
        items = str(soup.string)
        item = items.split("=")[1][:-2] # 去除var item跟;
        dic = json.loads(item)        
        assert dic['locktimeout'] == time, "數字沒有吃到" 

    # 微信二維碼/提示文案
    def wechat_setting(self, notice="這是微信客服"):
        self.scroll_to(1200)
        self.sleep(1)
        # 上傳檔案
        if platform.system() == "Windows":
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"\image\web\setting_photo\QA_167x83.png"
            file_path = origin_path + image_path
        elif platform.system() == 'Linux':
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path
        elif platform.system() == 'Darwin':
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path
        self.type(WebsiteSettingLocator.wechat_qrcode, file_path)
        self.sleep(3)
        # 提示文案
        self.switch_frame(0)
        self.type(WebsiteSettingLocator.wechat_prompt_text, notice)        
        self.switch_default_frame()
        
        self.scroll_to_element(WebsiteSettingLocator.submit_livechat)
        self.click(WebsiteSettingLocator.submit_livechat)
    
    # QQ號碼
    def qq_setting(self, brand, qq="1322288850"):
        self.brand = brand 
        category_1 = ["lv", "ls", "hy", "c7", "c8", "tz", "bh", "sc"]      
        category_2 = ["3h", "cdd","xpj"]

        for index in category_1:
            if index == self.brand:
                self.scroll_to_element(WebsiteSettingLocator.qq_number)
                self.type(WebsiteSettingLocator.qq_number, qq)
                self.click(WebsiteSettingLocator.submit_livechat)
        
        for index in category_2:
            if index == self.brand:
                self.scroll_to_element(WebsiteSettingLocator.qq_number)
                self.type(WebsiteSettingLocator.qq_number, qq)
                self.click(WebsiteSettingLocator.submit_livechat)               
                assert qq == "1322288850", "數字沒有吃到" 

    # 在線客服
    def livechat_setting(self, livechat="https://app.comm100.chat/chatserver/chatWindow.aspx?siteId=5000125&planId=175#"):
        assert (self.is_element_finded(WebsiteSettingLocator.customer_service_live_chat_link)) == True, "在線客服radio box不存在"
        assert (self.is_element_finded(WebsiteSettingLocator.customer_service_link)) == True, "站內客服radio box不存在"
        # self.click(WebsiteSettingLocator.customer_service_live_chat_link)
        self.scroll_to_element(WebsiteSettingLocator.livechat)
        self.type(WebsiteSettingLocator.livechat, livechat)
        self.sleep(1)
        self.click(WebsiteSettingLocator.submit_livechat)
    
    # 郵箱
    def email_setting(self, brand, email="lasv1234wwwww567890@gmail.com"):
        self.brand = brand 
        category_1 = ["lv", "ls", "bh", "sc"]
        category_2 = ["hy", "c7", "c8", "tz", "xpj", "cdd", "3h"]

        for index in category_1:
            if index == self.brand: 
                self.scroll_to_element(WebsiteSettingLocator.email)
                self.type(WebsiteSettingLocator.email, email)
                self.click(WebsiteSettingLocator.submit_livechat)

        for index in category_2:
            if index == self.brand:
                self.scroll_to_element(WebsiteSettingLocator.email)
                self.type(WebsiteSettingLocator.email, email)
                self.click(WebsiteSettingLocator.submit_livechat)
                assert email == "lasv1234wwwww567890@gmail.com", "數字沒有吃到"

    # 站內客服
    def customerservice_setting(self, customerservice="http://mynah-client-uat.paradise-soft.com.tw/chatroom?company=FM3SEAMrJdrVs&site=WS3SSBeEZf2zA"):
        self.scroll_to_element(WebsiteSettingLocator.customer_service)
        self.type(WebsiteSettingLocator.customer_service, customerservice)
        self.click(WebsiteSettingLocator.submit_livechat)
    
    # 取得站內客服所設網址
    def customerservice_get_value(self):
        self.scroll_to_element(WebsiteSettingLocator.customer_service)
        return self.get_attribute(WebsiteSettingLocator.customer_service,'value')

    # APP輸入框設定
    def app_setting(self, notice="請下載APP"):
        self.scroll_to_bottom()
        self.sleep(3)
        # 提示文案
        self.switch_frame(1)
        self.type(WebsiteSettingLocator.app_download_prompt_text, notice)        
        self.switch_default_frame()
        
        self.click(WebsiteSettingLocator.submit_app)

    # 此頁面為web端進行, admin頁面取消該function, 移置web_mainpage做確認.
    # 前台網頁禁用, 取url判斷是否有"stop"字樣
    # def front_web_banned(self, url):
    #     pattern = re.compile("[Ss]top")
    #     filterText = pattern.search(url)
    #     assert ((filterText.group() == "Stop") or (filterText.group() == "stop")) == True, "前台網頁禁用失敗"
    #     return None

    # 在線客服管理, 菜單內置換客服連接

    def customer_service_select(self, choose:int):
        option = choose
        assert self.is_element_finded(WebsiteSettingLocator.customer_service_type_livechat) == True, "菜单内置客服链接, 選項消失錯誤"
        assert self.is_element_finded(WebsiteSettingLocator.customer_service_type_webside) == True, "菜单内置客服链接, 選項消失錯誤"
        if option == 0:
            self.click(WebsiteSettingLocator.customer_service_type_livechat)
        elif option == 1:
            self.click(WebsiteSettingLocator.customer_service_type_webside)

        self.click(WebsiteSettingLocator.submit_livechat)

        return option
        
