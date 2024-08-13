import unittest
import sys
import os
import datetime, random, string
import time
import threading
from queue import Queue
import re

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)

from Project.mynah.pages.pages import WebPages, AdminPage
from Project.mynah.testsuite.testcases.base_testcase import BaseTestCase
from Project.mynah.pages.admin.admin_basepage import AdminBasePage
from Project.mynah.testsuite.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass



class WebTestCases(BaseTestCase, AdminBasePage):

    # Test Setting
    
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 35
    money='300'
    withdraw = '500'
    chrome_crash = 0
    foloderpath = ''
    adps=[]
    weps=[]
    driver_list = []
    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folder_path = gl.get_value('FOLDER_PATH')
        # cls.setting_browser()
        # pass
        
    @classmethod
    def setUp(cls):
        # cls.switch_home_page(cls)

        # try:
        #     cls.open_url()
        # except:
        #     cls.reopen_browser()

        # cls.wp.mainPage().maintenance()
        pass
        cls.start_time = time.time()

    def tearDown(self):
        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        # image_path_list = []
        # for driver in self.driver_list:
        #     image_path = ScreenShot(driver, f"{self.folder_path}/{image_name}/").screenshot(image_name)
        #     image_path_list.append(image_path)
        # gl.set_value('IMG_PATH', image_path_list)

        end_time = time.time()
        duration = "{:.3f}".format(end_time - self.start_time)  # 測試案例執行所花時間
        gl.set_value('Duration', f'{duration}s')

        for driver in self.driver_list:
            ScreenShot(driver, self.folder_path).screenshot(image_name)

        for ap in self.adps:
            ap.adminBasePage().quit_browser()

        for wp in self.weps:
            wp.webBasePage().quit_browser()

        self.driver_list.clear()
        self.adps.clear()
        self.weps.clear()



    @classmethod
    def tearDownClass(cls):
        # cls.close_browser(cls)
        # cls.quit_browser(cls)
        pass
    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls, ADdriver_num, Webdriver_num):
        cls.setting_test_data(cls)  # 設定測試數據
        for _ in range(ADdriver_num):
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.ap= AdminPage(cls.driver, cls.wait_time, cls.admin_url, cls.skipTest)     # 導入Web全部頁面
            cls.adps.append(cls.ap)

        for _ in range(Webdriver_num):
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))
            cls.wp= WebPages(cls.driver, cls.wait_time, cls.web_url1, cls.skipTest)     # 導入Web全部頁面
            cls.weps.append(cls.wp)
        
        
        # for i in range(Webdriver_num):
        #     cls.drivers['Webdriver_'+str(i)] = WebPages(cls.driver, cls.wait_time, cls.web_url1, cls.skipTest)    # 導入Admin全部頁面

        # cls.shot =  ScreenShot(cls.driver, cls.folderpath)

        # if not sys.argv[0].__contains__('prod'): # Prod 不帶入admin config
        #     cls.ad = AdminPage(cls.driver, cls.wait_time, cls.admin_url, cls.skipTest)

    @classmethod
    def open_url(cls):
        try:
            cls.dismiss_alert(cls)
        except:
            pass
        
        # cls.open_browser(cls, cls.admin_url)

    # ================================= TestCases =================================

    ####    後台登入
    def test_admin_login(self, driver, account='', password=''):
        if account == "":
            account = self.cs_account1
            password = self.cs_password1
        driver.adminBasePage().windows_to_top()
        driver.adminBasePage().open_browser(self.admin_url)
        driver.adminChatPage().admin_login(account, password)
    
    
    ####    關閉智能客服
    @DecorateClass('PFREQ-T2262')
    def test_close_ai_response(self):
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_ai_response_page()
        self.adps[0].adminAIResponsePage().into_left_select_site(self.site_name1)
        self.adps[0].adminAIResponsePage().close_ai_response()
        self.adps[0].adminAIResponsePage().into_left_select_site(self.site_name2)
        self.adps[0].adminAIResponsePage().close_ai_response()


    # ####    前後台發話
    @DecorateClass('PFREQ-T2263')
    def test_talk_to_each_other(self):
        self.setting_browser(1,1)
        # 客服登入進入會話版
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組

        # 互傳訊息
        web_message = self.random_read_file()
        admin_message = self.random_read_file()
        self.weps[0].chatPage().web_send_message(web_message)
        self.adps[0].adminChatPage().admin_check_message(web_message)   #後台驗證前台傳的訊息
        self.adps[0].adminChatPage().admin_send_message(admin_message)
        self.weps[0].chatPage().web_check_message(admin_message)

        self.weps[0].chatPage().check_talk_layout()                     #前台檢查版面
        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)


    # ####    前後台掛斷
    @DecorateClass('PFREQ-T2264')
    def test_hang_up_phone(self):
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().into_select_site(self.site_name1)

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminBasePage().windows_to_top()
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)        #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)          #選擇站點
        
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        self.adps[0].adminChatPage().admin_hang_up_phone()              #後台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)
        self.weps[0].chatPage().verify_phone_close_multi(self.weps)     #前台驗證電話已斷
        self.weps[0].scorePage().web_answer_score()                     #前台回答評分項目

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()  

        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.weps[0].chatPage().check_talk_layout()                     #前台檢查版面
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)
        self.weps[0].chatPage().verify_phone_close_multi(self.weps)     #前台驗證電話已斷


    ###    前台未被接通前發話 
    @DecorateClass('PFREQ-T2265')
    def test_client_speak_before_not_connected(self):
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().into_select_site(self.site_name1)

        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.guset_id = self.adps[0].adminChatPage().check_ringing()
        Web_Message=self.random_read_file()
        Ad_Message=self.random_read_file()

        self.weps[0].chatPage().web_send_message(Web_Message)
        self.weps[0].chatPage().web_check_message(Web_Message)
        
        self.adps[0].adminChatPage().already_talking_answer_and_open(self.guset_id)      #後台接起電話(有先發話)
        self.adps[0].adminChatPage().into_select_group(self.guset_id)   #進入指定聊天群組
        self.weps[0].chatPage().check_service_joined()

        self.adps[0].adminChatPage().admin_check_message(Web_Message)   #後台驗證前台傳的訊息

        self.adps[0].adminChatPage().admin_send_message(Ad_Message)
        self.weps[0].chatPage().web_check_message(Ad_Message)

        self.weps[0].chatPage().check_talk_layout()                     #前台檢查版面
        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)


    ####    詢前表單：新增問題、刪除問題、前台回答、後台驗證回復
    @DecorateClass('PFREQ-T2266')
    def test_inquiry_form(self):
        questions=[]
        self.setting_browser(1,1)
        # 登入main帳號，開啟詢前表單並新增問題
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_form_page()
        self.adps[0].adminFormPage().into_left_select_site(self.site_name2)
        self.adps[0].adminFormPage().open_form()
        self.adps[0].adminFormPage().close_form_code()
        self.adps[0].adminFormPage().close_form_binding()
        self.adps[0].adminFormPage().add_question()             #新增問題
        self.adps[0].adminFormPage().delete_question()          #刪除所有問題
        for _ in range(0,random.randint(1,5)):
            questions.append(self.adps[0].adminFormPage().add_question()) #新增問題
        self.adps[0].adminChatPage().admin_logout()
        
        # 客服登入
        self.adps[0].adminBasePage().refresh_browser()       
        self.sleep(1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().into_select_site(self.site_name2)

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url2)
        answers = self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組
        self.adps[0].adminFormPage().verify_Q_and_A(questions, answers)

        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛


    ####    同時接待不同站點
    @DecorateClass('PFREQ-T2267')
    def test_talk_different_site(self):
        self.setting_browser(1,2)
        # 客服登入進入會話版
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().window_mode_on()                                       #切換視窗模式

        guests = []

        # 2站點 訪客 回答詢前表單並進入會話頁
        for i in range(2):
            if i == 0:
                web_url= self.web_url1
                site_name= self.site_name1
            else:
                web_url= self.web_url2
                site_name= self.site_name2
            self.weps[i].chatPage().windows_to_top()                            #### 切換視窗
            self.weps[i].webBasePage().open_browser(web_url)
            status = self.weps[i].formPage().check_form_status()
            if status == True:
                self.weps[i].formPage().answer_question()
            self.weps[i].chatPage().check_client_into_conversation()

            self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
            self.adps[0].adminChatPage().check_site_blink(site_name)          #檢查站點未讀提示
            self.adps[0].adminChatPage().into_select_site(site_name)            #選擇站點
            guests.append(self.adps[0].adminChatPage().check_ringing())             #確認響鈴，並回傳ID
            self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
            self.weps[i].chatPage().check_service_joined()                      #前台確認客服加入事件
            self.adps[0].adminChatPage().into_select_group(guests[i])            #進入指定聊天群組

            web_message = self.random_read_file()
            self.weps[i].chatPage().web_send_message(web_message)
            self.adps[0].adminChatPage().admin_check_message(web_message)   #後台驗證前台傳的訊息


        #站點1訪客傳送訊息，後台確認未讀並切換站點、確認訊息
        message1 = '前台1 第二次訊息：' + self.random_read_file()
        self.weps[0].chatPage().web_send_message(message1)
        self.adps[0].adminChatPage().check_site_red_dot(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.adps[0].adminChatPage().admin_check_message(message1)   #後台驗證前台傳的訊息
        message2='後台 給前台1：' + self.random_read_file()
        self.adps[0].adminChatPage().admin_send_message(message2)
        self.weps[0].chatPage().web_check_message(message2)

        #站點2訪客傳送訊息，後台確認未讀並切換站點、確認訊息
        message3 = '前台2 第二次訊息：' + self.random_read_file()
        self.weps[1].chatPage().web_send_message(message3)
        self.adps[0].adminChatPage().check_site_red_dot(self.site_name2)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name2)      #選擇站點
        self.adps[0].adminChatPage().admin_check_message(message3)   #後台驗證前台傳的訊息
        message4='後台 給前台2：' + self.random_read_file()
        self.adps[0].adminChatPage().admin_send_message(message4)
        self.weps[1].chatPage().web_check_message(message4)

        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛
        self.adps[0].adminChatPage().into_select_site(self.site_name1)  #選擇站點
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guests[0])

        self.weps[1].chatPage().web_hang_up_phone()                     #前台掛電話
        self.weps[1].chatPage().check_chat_end()                        #前台驗證電話已掛
        self.adps[0].adminChatPage().into_select_site(self.site_name2)  #選擇站點
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guests[1])

    # ####    兩客服同時在線, 其中一客服接聽訪客，1對1
    @DecorateClass('PFREQ-T2268')
    def test_talk_different_cs(self):
        self.setting_browser(2,1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()                                  #後台1至會話版

        self.test_admin_login(self.adps[1], self.cs_account2, self.cs_password2)
        self.adps[1].adminMenuPage().into_chatBoard_page()                                  #後台2至會話版

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線
        
        self.adps[0].adminBasePage().windows_to_top()
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.adps[1].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.guset_id = self.adps[0].adminChatPage().check_ringing()                        #後台1確認響鈴
        self.adps[1].adminChatPage().check_ringing()                        #後台2確認響鈴

        self.adps[1].adminChatPage().admin_answer_and_open()
        self.weps[0].chatPage().web_check_one_join()
        message1 = self.random_read_file()
        message2 = self.random_read_file()
        self.weps[0].chatPage().web_send_message(message1)
        self.adps[1].adminBasePage().windows_to_top()
        self.adps[1].adminChatPage().admin_check_message(message1)

        self.adps[1].adminChatPage().admin_send_message(message2)
        self.weps[0].chatPage().web_check_message(message2)

        self.weps[0].chatPage().web_hang_up_phone()         #前台掛電話
        self.adps[1].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[1].adminChatPage().file_group(self.guset_id)
        # q = Queue()
        # firstCS = threading.Thread(target=self.adps[0].adminChatPage().admins_answer_one_open, args=(self.cs_account1,self.adps[0],q))
        # secondCS = threading.Thread(target=self.adps[1].adminChatPage().admins_answer_one_open, args=(self.cs_account2,self.adps[1],q))      #後台同時接聽
        # firstCS.start()
        # secondCS.start()
        # new_adps = q.get()      #拿到接聽到電話的adps
        #
        # self.weps[0].chatPage().web_check_one_join()        #前台驗證加入的客服只有一人
        #
        # message1 = self.random_read_file()
        # message2 = self.random_read_file()
        # self.weps[0].chatPage().web_send_message(message1)
        # new_adps.adminBasePage().windows_to_top()
        # new_adps.adminChatPage().admin_check_message(message1)
        #
        # new_adps.adminChatPage().admin_send_message(message2)
        # self.weps[0].chatPage().web_check_message(message2)
        #
        # self.weps[0].chatPage().web_hang_up_phone()         #前台掛電話
        # new_adps.adminChatPage().check_chat_end()                   #後台驗證電話已掛
        # new_adps.adminChatPage().file_group(self.guset_id)

    # ####    同站點接待多訪客
    @DecorateClass('PFREQ-T2269')
    def test_talk_more_guest(self):
        self.setting_browser(1,3)
        # 客服登入進入會話版
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        guests = []

        # 訪客 回答詢前表單並進入會話頁*2
        for i in range(2):
            self.weps[i].chatPage().windows_to_top()                            #### 切換視窗
            self.weps[i].webBasePage().open_browser(self.web_url1)
            status = self.weps[i].formPage().check_form_status()
            if status == True:
                self.weps[i].formPage().answer_question()
            self.weps[i].chatPage().check_client_into_conversation()

            self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
            self.adps[0].adminChatPage().check_site_red_dot(self.site_name1)    #檢查站點未讀提示
            self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
            guests.append(self.adps[0].adminChatPage().check_ringing())         #確認響鈴，並回傳ID
            self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
            self.weps[i].chatPage().check_service_joined()                      #前台確認客服加入事件
            self.adps[0].adminChatPage().into_select_group(guests[i])           #進入指定聊天群組
        
        #兩訪客傳訊息
        for i in range(2):
            message1 = self.random_read_file()
            message2 ='【'+ str(i)+'】客服第一次傳給訪客：' + self.random_read_file()
            self.weps[i].chatPage().web_send_message(message1)
            self.adps[0].adminChatPage().check_group_red_dot(guests[i])
            self.adps[0].adminChatPage().into_select_group(guests[i])               #進入指定聊天群組
            self.adps[0].adminChatPage().admin_check_message(message1)           #後台驗證前台傳的訊息
            self.adps[0].adminChatPage().admin_send_message(message2)
            self.weps[i].chatPage().web_check_message(message2)
        
        #產生訪客3
        self.weps[2].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[2].webBasePage().open_browser(self.web_url1)
        status = self.weps[2].formPage().check_form_status()
        if status == True:
            self.weps[2].formPage().answer_question()
        self.weps[2].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_site_red_dot(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        guests.append(self.adps[0].adminChatPage().check_ringing())         #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[2].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guests[2])           #進入指定聊天群組

        message3 = self.random_read_file()
        message4 ='【2】客服第一次傳給訪客：' + self.random_read_file()
        self.weps[2].chatPage().web_send_message(message3)
        self.adps[0].adminChatPage().check_group_red_dot(guests[2])
        self.adps[0].adminChatPage().into_select_group(guests[2])           #進入指定聊天群組
        self.adps[0].adminChatPage().admin_check_message(message3)          #後台驗證前台傳的訊息
        self.adps[0].adminChatPage().admin_send_message(message4)
        self.weps[2].chatPage().web_check_message(message4)

        # 3訪客與客服互傳訊息
        web_message=[]
        admin_message=[]
        for i in range(3):
            web_message.append('前台 傳訊息【'+str(i)+'】'+self.random_read_file())
            admin_message.append('後台 傳訊息【'+str(i)+'】'+self.random_read_file())
            self.weps[i].chatPage().web_send_message(web_message[i])

        for i in range(3):
            self.adps[0].adminChatPage().check_group_red_dot(guests[i])             #檢查聊天群組未讀提示

        for i in range(3):
            self.adps[0].adminChatPage().into_select_group(guests[i])               #進入指定聊天群組
            self.adps[0].adminChatPage().admin_check_message(web_message[i])        #後台驗證前台傳的訊息
            self.adps[0].adminChatPage().admin_send_message(admin_message[i])       #後台傳訊息

        for i in range(3):
            self.weps[i].chatPage().web_check_message(admin_message[i])             #前台確認訊息
            self.weps[i].chatPage().web_hang_up_phone()                             #前台掛電話
            self.weps[i].chatPage().check_chat_end()                                #前台驗證電話已掛

        for i in range(3):
            self.adps[0].adminChatPage().into_select_group(guests[i])               #進入指定聊天群組
            self.adps[0].adminChatPage().check_chat_end()                           #後台驗證電話已掛
            self.adps[0].adminChatPage().file_group(guests[i])


    # ####    邀請客服
    @DecorateClass('PFREQ-T2270')
    def test_invite_cs(self):
        self.setting_browser(2,1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)            #後台1登入
        self.adps[0].adminMenuPage().into_chatBoard_page()                                  #後台1至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)                      #選擇站點
        self.adps[0].adminChatPage().window_mode_on()                                       #切換視窗模式

        self.test_admin_login(self.adps[1], self.cs_account2, self.cs_password2)            #後台2登入
        self.adps[1].adminMenuPage().into_chatBoard_page()                                  #後台2至會話版
        self.adps[1].adminChatPage().into_select_site(self.site_name1)                      #選擇站點
        self.adps[1].adminChatPage().window_mode_on()                                       #切換視窗模式

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        # 客服1接訪客，邀請客服2
        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        message1 = self.random_read_file()
        message2 = self.random_read_file()
        self.weps[0].chatPage().web_send_message(message1)              #前後台對話
        self.adps[0].adminChatPage().admin_check_message(message1)

        self.adps[0].adminChatPage().admin_send_message(message2)
        self.weps[0].chatPage().web_check_message(message2)    

        CS2_name = self.adps[0].adminChatPage().invite_cs()                     #邀請客服
        self.adps[0].adminChatPage().verify_person_join(CS2_name)               #後台驗證客服加入
        self.weps[0].chatPage().verify_person_join(CS2_name)                    #前台驗證客服加入
        self.adps[1].adminBasePage().windows_to_top()
        self.adps[1].adminChatPage().into_select_group(guset_id)                #進入指定聊天群組
        self.adps[1].adminChatPage().text_before_invite(message1,message2)      #新客服確認之前對話

        # 三方傳訊息
        message3 = self.random_read_file()
        message4 = self.random_read_file()
        message5 = self.random_read_file()
        self.adps[1].adminChatPage().admin_send_message(message3)       #後台2發話
        self.weps[0].chatPage().web_check_message(message3)             #前台確認訊息
        self.adps[0].adminChatPage().admin_check_message(message3)      #後台1確認訊息

        self.weps[0].chatPage().web_send_message(message4)              #前台發話
        self.adps[1].adminChatPage().admin_check_message(message4)      #後台2確認訊息
        self.adps[0].adminChatPage().admin_check_message(message4)      #後台1確認訊息

        self.adps[0].adminChatPage().admin_send_message(message5)       #後台1發話
        self.weps[0].chatPage().web_check_message(message5)             #前台確認訊息
        self.adps[1].adminChatPage().admin_check_message(message5)      #後台2確認訊息
        self.weps[0].chatPage().check_talk_layout()                     #前台檢查版面
        
        #客服1掛斷(首次接待的那方)
        self.adps[0].adminChatPage().admin_hang_up_phone()                      #後台1掛斷
        self.adps[0].adminChatPage().verify_phone_close_multi(self.adps)        #後台驗證電話已斷
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[1].adminChatPage().file_group(guset_id)
        self.weps[0].chatPage().verify_phone_close_multi(self.weps)             #前台驗證電話已斷

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].scorePage().web_answer_score()                 #前台回答評分項目
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()        #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        # 客服2接訪客，邀請客服1，客服1掛斷(被邀的那方)
        self.adps[1].adminBasePage().windows_to_top()
        guset_id = self.adps[1].adminChatPage().check_ringing()         #後台2確認響鈴
        self.adps[1].adminChatPage().admin_answer_and_open()            #後台2接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[1].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
    
        CS1_name = self.adps[1].adminChatPage().invite_cs()             #邀請客服
        self.adps[1].adminChatPage().verify_person_join(CS1_name)       #後台驗證客服加入
        self.weps[0].chatPage().verify_person_join(CS1_name)            #前台驗證客服加入

        self.adps[0].adminChatPage().into_select_group(guset_id)                #進入指定聊天群組
        self.adps[0].adminChatPage().admin_hang_up_phone()                      #後台1掛斷
        self.adps[0].adminChatPage().verify_phone_close_multi(self.adps)        #後台驗證電話已斷
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[1].adminChatPage().file_group(guset_id)
        self.weps[0].chatPage().verify_phone_close_multi(self.weps)             #前台驗證電話已斷

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].scorePage().web_answer_score()                     #前台回答評分項目
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        # 客服1接待，邀客服2，前台掛電話
        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        CS2_name = self.adps[0].adminChatPage().invite_cs()                     #邀請客服
        self.adps[0].adminChatPage().verify_person_join(CS2_name)               #後台驗證客服加入
        self.weps[0].chatPage().verify_person_join(CS2_name)                    #前台驗證客服加入
        self.adps[1].adminChatPage().into_select_group(guset_id)                #進入指定聊天群組
        self.weps[0].chatPage().web_hang_up_phone()                             #前台掛電話
        self.adps[0].adminChatPage().verify_phone_close_multi(self.adps)        #後台驗證電話已斷
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[1].adminChatPage().file_group(guset_id)
        self.weps[0].chatPage().verify_phone_close_multi(self.weps)             #前台驗證電話已斷
        
        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].scorePage().web_answer_score()                     #前台回答評分項目
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        # 客服1接待，邀客服2，測試離開對話
        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
        
        CS2_name = self.adps[0].adminChatPage().invite_cs()             #邀請客服
        self.adps[1].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
        self.adps[1].adminChatPage().leave_conversation()               #客服2離開對話
        self.adps[1].adminChatPage().check_chat_end()                   #驗證客服2離開對話
        self.adps[1].adminChatPage().file_group(guset_id)
        self.adps[0].adminChatPage().leave_check(CS2_name)              #客服1驗證客服2離開對話
        self.weps[0].chatPage().leave_check_web()                       #前台驗證無客服離開訊息
        self.adps[0].adminChatPage().last_cs_leave_check()              #最後一位客服無法離開對話

        CS2_name = self.adps[0].adminChatPage().invite_cs()             #邀請客服
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
        self.adps[0].adminChatPage().leave_conversation()               #客服1離開對話
        self.adps[0].adminChatPage().check_chat_end()                   #驗證客服1離開對話
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[1].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組
        self.adps[1].adminChatPage().leave_check(CS1_name)              #客服2驗證客服1離開對話
        self.weps[0].chatPage().leave_check_web()                       #前台驗證無客服離開訊息
        self.adps[1].adminChatPage().last_cs_leave_check()              #最後一位客服無法離開對話

        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[1].adminChatPage().check_chat_end()                   
        self.adps[1].adminChatPage().file_group(guset_id)



    ####    自動結束對話-客服斷線
    @DecorateClass('PFREQ-T2271')
    def test_disconnect_auto_end(self):
        autoTimes = random.randint(10,12)
        self.setting_browser(1,1)
        # 後台main 設定對話規則開啟
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_rules_page()                                  #進入對話規則
        self.adps[0].adminRulesPage().open_disconnect_auto_end(autoTimes)               #打開"客服斷線"自動結束對話
        self.adps[0].adminRulesPage().close_visitor_auto_end()                          #關閉"訪客未發話"自動結束對話
        self.adps[0].adminChatPage().admin_logout()                                     # main登出

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        # 登入客服並接待
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()                              #後台至會話版
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        guset_id = self.adps[0].adminChatPage().check_ringing()             #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)            #進入指定聊天群組

        # 使客服斷線
        mark=random.choice(['關瀏覽器','登出'])
        if mark=='關瀏覽器':
            self.adps[0].adminBasePage().close_and_chang_window()
        else:
            self.adps[0].adminChatPage().admin_logout()

        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].chatPage().check_disconnect_auto_end(autoTimes)        #檢查前台 客服斷線會自動結束對話
        self.weps[0].scorePage().web_answer_score()                         #前台回答評分項目

        # 後台main 設定對話規則關閉
        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        if mark=='關瀏覽器':
            self.adps[0].adminBasePage().open_browser(self.admin_url)
            self.adps[0].adminBasePage().close_main()                   #關閉連線提示
            self.adps[0].adminChatPage().admin_logout()                 #後台登出
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_rules_page()                                  #進入對話規則
        self.adps[0].adminRulesPage().close_disconnect_auto_end()              #關閉"客服斷線"自動結束對話
        self.adps[0].adminChatPage().admin_logout()                                     #後台登出

        # 登入客服並進行歸檔動作
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()                  #後台至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.adps[0].adminChatPage().file_group(guset_id)

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        # 客服接待
        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        guset_id = self.adps[0].adminChatPage().check_ringing()             #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)            #進入指定聊天群組

        # 使客服斷線
        mark=random.choice(['關瀏覽器','登出'])
        if mark=='關瀏覽器':
            self.adps[0].adminBasePage().close_and_chang_window()
        else:
            self.adps[0].adminChatPage().admin_logout()

        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].chatPage().check_disconnect_not_end(autoTimes)         #檢查前台 客服斷線會自動結束對話
        self.weps[0].chatPage().web_send_message("我沒被自動掛斷")
        self.weps[0].chatPage().web_check_message("我沒被自動掛斷")
        self.weps[0].chatPage().web_hang_up_phone()                         #前台掛電話
        self.weps[0].chatPage().check_chat_end()                            #前台驗證電話已掛

        # 重新登入客服，並確認訊息且歸檔
        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        if mark=='關瀏覽器':
            self.adps[0].adminBasePage().open_browser(self.admin_url)
            self.adps[0].adminBasePage().close_main()                   #關閉連線提示
            self.adps[0].adminChatPage().admin_logout()                 #後台登出
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)        
        self.adps[0].adminMenuPage().into_chatBoard_page()                  #後台至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.adps[0].adminChatPage().into_select_group(guset_id)            #進入指定聊天群組
        self.adps[0].adminChatPage().admin_check_message("我沒被自動掛斷")
        self.adps[0].adminChatPage().check_chat_end()                   
        self.adps[0].adminChatPage().file_group(guset_id)


    ####    自動結束對話-訪客未發話
    @DecorateClass('PFREQ-T2272')
    def test_visitor_auto_end(self):
        autoTimes = random.randint(10,12)
        self.setting_browser(1,1)
        # 後台main 設定對話規則開啟
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)

        self.adps[0].adminMenuPage().into_rules_page()                                  #進入對話規則
        self.adps[0].adminRulesPage().open_visitor_auto_end(autoTimes)                  #打開"訪客未發話"自動結束對話
        self.adps[0].adminRulesPage().close_disconnect_auto_end()                       #關閉"客服斷線"自動結束對話
        self.adps[0].adminChatPage().admin_logout()                                     # main登出

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        # 登入客服並接待
        self.test_admin_login(self.adps[0], self.cs_account2, self.cs_password2)
        self.adps[0].adminMenuPage().into_chatBoard_page()                              #後台至會話版
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        guset_id = self.adps[0].adminChatPage().check_ringing()             #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)            #進入指定聊天群組

        # 前台 訪客未發話 會自動結束對話
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].chatPage().check_visitor_auto_end(autoTimes)           #檢查前台 訪客未發話會自動結束對話
        self.weps[0].scorePage().web_answer_score()                         #前台回答評分項目
        
        # 後台main 設定對話規則關閉
        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_chat_end()                       #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[0].adminChatPage().admin_logout()                         #客服登出
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_rules_page()                                  #進入對話規則
        self.adps[0].adminRulesPage().close_visitor_auto_end()              #關閉"訪客未發話"自動結束對話
        self.adps[0].adminChatPage().admin_logout()                         # main登出

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().refresh_browser()                    #前台刷新頁面:重新開啟對話
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        # 登入客服並接待
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()                              #後台至會話版
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        guset_id = self.adps[0].adminChatPage().check_ringing()             #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)            #進入指定聊天群組
        
        # 前台 訪客未發話 不會自動結束對話
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].chatPage().check_visitor_not_end(autoTimes)            #檢查前台訪客未發話"不會"自動結束對話

        web_message= self.random_read_file()
        admin_message="後台傳：" + self.random_read_file()
        self.adps[0].adminChatPage().admin_send_message(admin_message)
        self.weps[0].chatPage().web_check_message(admin_message)
        self.weps[0].chatPage().web_send_message(web_message)
        self.adps[0].adminChatPage().admin_check_message(web_message)   #後台驗證前台傳的訊息
        self.weps[0].chatPage().web_hang_up_phone()     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()   #後台驗證電話已掛
        self.weps[0].chatPage().check_chat_end()        #前台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)



    # ####    前後台傳送圖片
    @DecorateClass('PFREQ-T2273')
    def test_send_img(self):
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)        #後台登入
        self.adps[0].adminMenuPage().into_chatBoard_page()                              #後台至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)                  #選擇站點
        
        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #後台確認響鈴
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接聽
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服已加入對話
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        self.weps[0].webBasePage().windows_to_top()
        imgs = self.weps[0].chatPage().web_send_img()                   #前台傳圖
        self.adps[0].adminBasePage().windows_to_top()
        pics = self.adps[0].adminChatPage().admin_send_img()            #後台傳圖
        self.adps[0].adminChatPage().cs_verify_img(guset_id,imgs)       #後台驗證圖片
        self.weps[0].chatPage().web_verify_img(pics)                    #前台驗證圖片

        self.weps[0].chatPage().web_hang_up_phone()         #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()   #後台驗證電話已掛
        self.weps[0].chatPage().check_chat_end()        #前台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)



    # ####    品牌端登入、資料綁定
    @DecorateClass('PFREQ-T2274')
    def test_channel_account(self):
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)          #後台登入
        self.adps[0].adminMenuPage().into_form_page()
        self.adps[0].adminFormPage().into_left_select_site(self.site_name1)             #選擇站點，需輸入站點名稱
        self.adps[0].adminFormPage().open_form()
        self.adps[0].adminFormPage().close_form_code()
        self.adps[0].adminFormPage().check_and_add_question()                           #檢查是否有表單問題，如果沒有就新增
        self.adps[0].adminFormPage().open_form_binding()                                #打開資料綁定
        self.adps[0].adminFormPage().select_binding_question()                          #選擇綁定問題
        self.adps[0].adminBasePage().admin_logout()                                     #登出
        self.sleep(1)
        
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()                                  #後台至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)                      #選擇站點

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().open_browser(self.channel_url)                           #開品牌
        self.weps[0].webBasePage().refresh_browser()                                        #關閉一般公告
        self.weps[0].channelPage().channel_login(self.web_account, self.web_password,captcha='1')       #登入品牌
        self.weps[0].channelPage().mynah_connect()                                          #進客服寶前台

        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接起電話
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        nickname, account_info = self.adps[0].adminChatPage().personal_info()                           #後台開個人資訊取得暱稱和帳號
        self.adps[0].adminChatPage().verify_name(self.web_account,guset_id,nickname,account_info)       #比對暱稱和帳號

        self.weps[0].chatPage().web_hang_up_phone()         #前台掛電話
        self.weps[0].scorePage().web_answer_score()

        self.adps[0].adminChatPage().check_chat_end()       #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)
        self.adps[0].adminBasePage().admin_logout()         #登出
        self.sleep(1)

        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)          #後台登入
        self.adps[0].adminMenuPage().into_form_page()
        self.adps[0].adminFormPage().into_left_select_site(self.site_name1)             #選擇站點，需輸入站點名稱
        self.adps[0].adminFormPage().close_form_binding()                               #關閉資料綁定
        self.adps[0].adminBasePage().admin_logout()                                     #登出
        self.sleep(1)

        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)       
        self.adps[0].adminMenuPage().into_chatBoard_page()                              #後台至會話版
        self.adps[0].adminChatPage().into_select_site(self.site_name1)                  #選擇站點

        self.weps[0].webBasePage().windows_to_top()
        self.weps[0].webBasePage().switch_home_page()
        self.weps[0].channelPage().mynah_connect()                                          #進客服寶前台
        status = self.weps[0].formPage().check_form_status()            #檢查詢前表單狀態 
        if status == True:
            self.weps[0].formPage().answer_question()                   #回答詢前表單問題
        self.weps[0].chatPage().check_client_into_conversation()        #前台確認進線

        self.adps[0].adminBasePage().windows_to_top()
        guset_id = self.adps[0].adminChatPage().check_ringing()         #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()            #後台接起電話
        self.weps[0].chatPage().check_service_joined()                  #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(guset_id)        #進入指定聊天群組

        nickname, account_info = self.adps[0].adminChatPage().personal_info()                           #後台開個人資訊取得暱稱和帳號
        self.adps[0].adminChatPage().verify_name(self.web_account,guset_id,nickname,account_info)       #比對暱稱和帳號

        self.weps[0].chatPage().web_hang_up_phone()         #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()       #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(guset_id)



    # ####    聊天群組查詢對話內容，歸檔
    @DecorateClass('PFREQ-T2275')
    def test_search_group_message(self):
        self.setting_browser(1,1)
        # 客服登入進入會話版
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID        
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組

        # 互傳訊息
        web_message = self.random_read_file()
        admin_message = self.random_read_file()
        self.weps[0].chatPage().web_send_message(web_message)
        self.adps[0].adminChatPage().admin_check_message(web_message)   #後台驗證前台傳的訊息
        self.adps[0].adminChatPage().admin_send_message(admin_message)
        self.weps[0].chatPage().web_check_message(admin_message)
        for _ in range(3):
            web_message2 = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
            admin_message2 = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
            self.weps[0].chatPage().web_send_message(web_message2)
            self.adps[0].adminChatPage().admin_check_message(web_message2)   #後台驗證前台傳的訊息
            self.adps[0].adminChatPage().admin_send_message(admin_message2)
            self.weps[0].chatPage().web_check_message(admin_message2)

        self.adps[0].adminChatPage().search_group_message()             # 會話框搜尋查找紀錄

        self.weps[0].chatPage().web_hang_up_phone()                     # 前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   # 後台驗證電話已掛
        self.weps[0].chatPage().check_chat_end()                        # 前台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)          # 後台歸檔

        
    # #### 接待信息查看 (目前沒檢查事件)
    @DecorateClass('PFREQ-T2276')
    def test_history_check(self):
        self.setting_browser(1,1)
        # 客服登入進入會話版
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url1)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_site_blink(self.site_name1)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name1)      #選擇站點
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組

        # 互傳訊息
        for _ in range(2):
            web_message = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
            admin_message = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
            self.weps[0].chatPage().web_send_message(web_message)
            self.adps[0].adminChatPage().admin_check_message(web_message)   #後台驗證前台傳的訊息
            self.adps[0].adminChatPage().admin_send_message(admin_message)
            self.weps[0].chatPage().web_check_message(admin_message)

        # 爬下所有訊息內容
        mes_list = self.adps[0].adminChatPage().get_all_message()                  

        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛

        # main 至接待紀錄確認
        self.adps[0].adminChatPage().admin_logout()                             # 客服登出
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_history_page()                        # 進入接待信息
        self.adps[0].adminHistoryPage().into_left_select_site(self.site_name1)  # 接待信息_選擇站點
        self.adps[0].adminHistoryPage().click_search()                          # 點擊查詢按鈕
        self.adps[0].adminHistoryPage().select_group_history(self.guset_id)     #選擇指定群組查看
        history_list = self.adps[0].adminHistoryPage().get_history_data()
        self.adps[0].adminHistoryPage().check_message_and_history(mes_list, history_list)


    # #### 設置推廣廣告
    @DecorateClass('PFREQ-T2277')
    def test_promotion_ad(self):
        self.setting_browser(1,1)
        # 登入main帳號，設定推廣廣告
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_promotion_ad_page()
        self.adps[0].adminFormPage().into_left_select_site(self.site_name2)
        self.adps[0].adminPromotionAdPage().open_ad()
        ad_text = self.adps[0].adminPromotionAdPage().setting_ad_text()
        self.adps[0].adminChatPage().admin_logout()

        # 客服登入
        self.adps[0].adminBasePage().refresh_browser()       
        self.sleep(1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().into_select_site(self.site_name2)

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url2)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        web_text = self.weps[0].chatPage().get_ad_text()
        self.adps[0].adminPromotionAdPage().check_ad_text(ad_text, web_text)

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組


        self.weps[0].chatPage().web_hang_up_phone()                     #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                   #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)
        self.weps[0].chatPage().check_chat_end()                        #前台驗證電話已掛


    # #### 評分項目設置
    @DecorateClass('PFREQ-T2278')
    def test_score_statistics(self):
        items=[]
        self.setting_browser(1,1)
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)
        self.adps[0].adminMenuPage().into_score_item_page()
        self.adps[0].adminScorePage().into_score_select_site(self.site_name2)
        self.adps[0].adminScorePage().open_score()
        self.adps[0].adminScorePage().open_score_enforce()
        self.adps[0].adminScorePage().open_score_opinion()
        items.append(self.adps[0].adminScorePage().add_score_item(0))          #新增項目
        self.adps[0].adminScorePage().delete_item()              #刪除所有項目
        for _ in range(0,random.randint(2,5)):
            item = self.adps[0].adminScorePage().add_score_item(1)
            if item != None:
                items.append(item)           #新增項目
        self.adps[0].adminChatPage().admin_logout()

         # 客服登入
        self.adps[0].adminBasePage().refresh_browser()       
        self.sleep(1)
        self.test_admin_login(self.adps[0], self.cs_account1, self.cs_password1)
        self.adps[0].adminMenuPage().into_chatBoard_page()
        self.adps[0].adminChatPage().into_select_site(self.site_name2)

        # 訪客回答詢前表單並進入會話頁
        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].webBasePage().open_browser(self.web_url2)
        status = self.weps[0].formPage().check_form_status()
        if status == True:
            self.weps[0].formPage().answer_question()
        self.weps[0].chatPage().check_client_into_conversation()

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().check_site_blink(self.site_name2)    #檢查站點未讀提示
        self.adps[0].adminChatPage().into_select_site(self.site_name2)      #選擇站點
        self.guset_id = self.adps[0].adminChatPage().check_ringing()        #確認響鈴，並回傳ID
        self.adps[0].adminChatPage().admin_answer_and_open()                #後台接起電話
        self.weps[0].chatPage().check_service_joined()                      #前台確認客服加入事件
        self.adps[0].adminChatPage().into_select_group(self.guset_id)       #進入指定聊天群組

        self.weps[0].chatPage().windows_to_top()                            #### 切換視窗
        self.weps[0].chatPage().web_hang_up_phone()                         #前台掛電話
        self.adps[0].adminChatPage().check_chat_end()                       #後台驗證電話已掛
        self.adps[0].adminChatPage().file_group(self.guset_id)
        scores, opinion = self.weps[0].scorePage().web_score_record()       #前台回答評分項目

        self.adps[0].adminChatPage().windows_to_top()                       #### 切換視窗
        self.adps[0].adminChatPage().admin_logout()
        self.test_admin_login(self.adps[0], self.bs_account, self.bs_password)      
        self.adps[0].adminMenuPage().into_score_statistics_page()
        self.adps[0].adminStatisticsPage().into_statistics_select_site(self.site_name2)
        s_items, s_scores, s_opinion = self.adps[0].adminStatisticsPage().search_score_statistics()
        self.adps[0].adminStatisticsPage().compare_items_scores(items, scores, opinion, s_items, s_scores, s_opinion)

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result)  # call superclass run method