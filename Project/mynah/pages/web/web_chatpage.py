import sys
import time
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.web.webs_basepage import WebBasePage

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class ChatLocator:
    guest_close = (By.XPATH, "//a[@class='close']")     #掛斷鈕
    guest_back = (By.XPATH,"//i[@class='back van-icon van-icon-arrow-left']") #返回鈕
    guest_confirm_close = (By.XPATH, "//button[@class='van-button van-button--default van-button--large van-dialog__confirm van-hairline--left']")      #掛斷確定鈕
    # wait_for_service_locator = "//*[@class='wcr-msg-connect__title']"
    recall_link = (By.XPATH, "//a[@class='message-close__carry brand-all']")        #重新對話
    se_lock = (By.XPATH, "//body[@class='van-overflow-hidden']")        #提示框彈出時，底部鎖住
    joined_service_locator = (By.XPATH, "//span[@class='wcr-msg-ending__text' and contains(text(),'已加入')]")      #客服已加入事件
    name_waitforconnect = (By.XPATH, "//p[@class='name-text' and text()='客服人员连线中']")     #進入前台左上角客服人員名稱 客服人员连线中
    web_not_stable_message = (By.XPATH, "//p[contains(text(), '由于网络不稳定，客服会话断') and contains(text(), '麻烦请重新进线客服')]")       #前台 網路不穩訊息
    input_locator = (By.XPATH, "//div[@placeholder='请输入讯息...']")       #輸入訊息框
    end_event = (By.XPATH, "//span[@class='wcr-msg-ending__text' and contains(text(),'对话结束')]")     #對話結束事件
    p_locator = "//p[text()='"      #需組合
    sendimg_input_se = (By.XPATH, "//div[@class='wcr-input-group-prepend']/input[1]")      #傳圖input
    img_uploading = (By.XPATH, "//img[@class='content__image--img']")       #圖上傳中
    verify_img_se = (By.XPATH, "//div[@class='wcr-list__content wcr--left']//img[@class='content__image--img content__image--isUpdated']")      #驗證圖片傳送成功
    wait_for_created = (By.XPATH, "//div[contains(text(), '等待连线建立中')]")       #等待連線建立中
    wait_for_service = (By.XPATH, "//*[contains(text(),'正在等待客服接入')]")                    #聊天室時間 (連線建立時沒有時間)
    leave_event = (By.XPATH, "//span[@class='wcr-msg-ending__text' and contains(text(),'已离开')]")     #客服已離開訊息
    verify_guest_close = (By.XPATH, "//span[@class='wcr-msg-ending__text' and contains(text(),'对话结束')]")        #驗證掛斷
    advertising_div = (By.XPATH, "//div[@class='promote-message shadows-default__medium brand-all']")        #廣告div
    cs_talk_p = (By.XPATH, "//div[@class='wcr-list__content wcr--left']//p")        #客服發的話p
    guest_talk_p = (By.XPATH, "//div[@class='wcr-list__content wcr--right']//p")        #訪客發的話div
    avatar_img = (By.XPATH, "//div[@class='list__item__avatar']/img")        #頭像img
    promote_text = (By.XPATH, "//p[@class='promote-message__text']")        #推廣廣告的整個黃色區域

    
class WebChatPage(WebBasePage):
    #前台確認聊天已建立
    def check_already_created(self):
        try:
            self.wait_visibility(ChatLocator.wait_for_service)
        except:
            raise EOFError('前台等待聊天室連線建立超時')    

    #前台傳送訊息
    def web_send_message(self,message):
        try:
            self.wait_visibility(ChatLocator.input_locator)
            self.type(ChatLocator.input_locator, message)
            self.type_enter(ChatLocator.input_locator)
        except:
            raise EOFError('前台傳送訊息失敗')

    #前台確認收到訊息
    def web_check_message(self,message):
        mes = (By.XPATH, self.mix_xpath(ChatLocator.p_locator, message))
        assert self.wait_visibility_status(mes) , '前台接收訊息失敗，訊息內容：'+ message
    
    #前台掛斷                               #原 SeHangUpPhone
    def web_hang_up_phone(self):
        try:
            self.sleep(1)
            if self.is_element_finded(ChatLocator.guest_close) == True:
                self.click(ChatLocator.guest_close)
            else:
                self.click(ChatLocator.guest_back)
            self.wait_visibility(ChatLocator.se_lock)
            self.wait_visibility(ChatLocator.guest_confirm_close)
            self.sleep(3)
            self.click(ChatLocator.guest_confirm_close)
        except:
            raise EOFError('前台掛斷對話失敗')

    #驗證前台已掛斷(多人)
    def verify_phone_close_multi(self, web_pages):
        self.sleep(1)
        for wp in web_pages:
            assert wp.webBasePage().is_element_finded(ChatLocator.verify_guest_close) , '前台對話未結束'
    
    #確認前台 對話結束
    def check_chat_end(self):
        try:
            self.wait_visibility(ChatLocator.verify_guest_close) 
        except:
            raise EOFError('前台對話未結束')

    #前台重啟對話 (更新後已無此按鈕)
    def web_recall(self):
        self.wait_visibility(ChatLocator.recall_link)
        self.click(ChatLocator.recall_link)

    #前台確認客服已加入對話
    def check_service_joined(self):
        try:
            self.wait_visibility(ChatLocator.joined_service_locator)
        except:
             raise EOFError("前台沒 客服加入事件")

    #前台確認1客服加入對話
    def web_check_one_join(self):
        self.wait_visibility(ChatLocator.joined_service_locator)
        number = self.find_elements(ChatLocator.joined_service_locator)
        if len(number) != 1:
            raise EOFError('多個客服加入對話')

    #驗證某客服加入對話
    def verify_person_join(self, name):                 
        try:
            verify_name_join = (By.XPATH, f"//span[contains(text(),'{name} 已加入')]")
            self.wait_visibility(verify_name_join)
        except:
            raise EOFError(f"{name}未加入對話")

    #確認第二客服離開時前台無離開訊息
    def leave_check_web(self):
        assert self.is_element_finded(ChatLocator.leave_event) is False, '前台出現客服離開訊息'


    #前台確認進入會話板，等待客服接入
    def check_client_into_conversation(self):
        try:
            self.wait_visibility(ChatLocator.name_waitforconnect)
            self.check_already_created()
        except:
             raise EOFError("前台未成功進入會話框")


    # 檢查前台客服斷線會自動結束對話
    def check_disconnect_auto_end(self, autoTimes):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print("開始等待系統自動掛斷 "+str(autoTimes)+" 分鐘 ......")
        self.sleep((autoTimes-1)*60)
        assert self.is_element_finded(ChatLocator.web_not_stable_message) is False , '對話提早收到網路不穩訊息 !!!'
        self.web_send_message("我在等待被自動掛斷...")
        self.sleep(60+20)
        # assert self.is_element_finded(ChatLocator.web_not_stable_message) ,"未收到網路不穩訊息 !!"    #RD調整過後，不會顯示該訊息
        assert self.is_element_finded(ChatLocator.end_event) ,"對話未順利結束 !!"
    
    # 檢查前台訪客未發話會自動結束對話
    def check_visitor_auto_end(self, autoTimes):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print("開始等待系統自動掛斷 "+str(autoTimes)+" 分鐘 ......")
        self.sleep((autoTimes-1)*60)
        assert self.is_element_finded(ChatLocator.end_event) is False , '對話提早結束 !!!'
        self.sleep(60+20)
        assert self.is_element_finded(ChatLocator.web_not_stable_message) is False , '對話收到網路不穩訊息 !!!'
        assert self.is_element_finded(ChatLocator.end_event) ,"對話未順利結束 !!!"

    # 檢查前台客服斷線"不會"自動結束對話
    def check_disconnect_not_end(self, autoTimes):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print("等待系統 "+str(autoTimes)+" 分鐘 '不會'自動掛斷......")
        self.sleep((autoTimes-1)*60)
        self.web_send_message("客服斷線 我不應該被自動掛斷...")
        self.sleep(60+20)
        assert self.is_element_finded(ChatLocator.web_not_stable_message) is False , '對話收到網路不穩訊息 !!!'
        assert self.is_element_finded(ChatLocator.end_event) is False ,"對話結束了 !!"
        

    # 檢查前台訪客未發話"不會"自動結束對話
    def check_visitor_not_end(self, autoTimes):
        self.web_send_message("我訪客 不發話...不該被掛斷")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print("等待系統 "+str(autoTimes)+" 分鐘 '不會'自動掛斷......")
        self.sleep(autoTimes*60+20)
        assert self.is_element_finded(ChatLocator.web_not_stable_message) is False , '對話收到網路不穩訊息 !!!'
        assert self.is_element_finded(ChatLocator.end_event) is False,"對話結束了 !!!"

    #前台傳送圖片
    def web_send_img(self):
        imgNameList=['img_1.jpg','img_2.jpg','img_3.jpg','img_4.jpg','img_5.jpg','img_6.jpg','img_體育遊戲.jpg']
        imgs = random.randint(1,3)
        for x in range(imgs):
            ranImg = random.choice(imgNameList)
            filepath = '/pages/files/'
            apath = root_path.replace('\\','/') + filepath + ranImg             #取圖片絕對路徑
            self.type(ChatLocator.sendimg_input_se, apath)
            # self.wait_visibility(ChatLocator.img_uploading)            #等待圖片開始上傳
            # img_upload_done = (By.XPATH, f"(//img[@class='content__image--img content__image--isUpdated'])[{str(x+1)}]")
            img_upload_done = (By.XPATH, "//div[contains(@class, 'content__message--isUpdated')]")
            self.wait_visibility(img_upload_done)         #等待圖片上傳完成
        time.sleep(5)
        return imgs

    #前台驗證圖片
    def web_verify_img(self,pics):
        try:
            self.sleep(1)
            self.wait_visibility(ChatLocator.verify_img_se)
        except:
            raise EOFError('傳送圖片失敗')
        seimgs = self.find_elements(ChatLocator.verify_img_se)
        assert len(seimgs) == pics , f'圖片數量不正確，後台傳送{pics}張，前台接收{len(seimgs)}張'
    
    #檢查前台對話版是否跑版
    def check_talk_layout(self):
        advertising_width = 450
        conversation_width = 286
        avatar_img_width = 40
        chat_input_width = 350
  
        if self.is_element_finded(ChatLocator.advertising_div) == True:
            advertising_w = self.find_element(ChatLocator.advertising_div).value_of_css_property('width').split('px')[0]
            assert float(advertising_w) <= advertising_width, '廣告超出寬度'

        cs_talks = self.find_elements(ChatLocator.cs_talk_p)
        guest_talks = self.find_elements(ChatLocator.guest_talk_p)
        avatars = self.find_elements(ChatLocator.avatar_img)
        chat_input_w = self.find_element(ChatLocator.input_locator).value_of_css_property('width').split('px')[0]
        for x in cs_talks:
            cs_talk_w = x.value_of_css_property('width').split('px')[0]
            assert float(cs_talk_w) <= conversation_width, '客服發話文字超出寬度'
        
        for x in guest_talks:
            guest_talk_w = x.value_of_css_property('width').split('px')[0]
            assert float(guest_talk_w) <= conversation_width, '訪客發話文字超出寬度'

        for x in avatars:
            avatar_w = x.value_of_css_property('width').split('px')[0]
            assert float(avatar_w) <= avatar_img_width, '頭像超出寬度'

        assert float(chat_input_w) <= chat_input_width, '訊息輸入框超出寬度'


    def get_ad_text(self):
        promote_message = self.get_text(ChatLocator.promote_text)
        return promote_message