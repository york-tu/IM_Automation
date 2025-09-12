import sys
import os
import random, string
from time import sleep

from Project.mynah.pages.admin.admin_basepage import AdminBasePage
from selenium.webdriver.common.by import By
from queue import Queue

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class ChatLocator:
    ########### 後台 ###########
    phone_call_img = (By.XPATH, '(//div[@class="md-controls__btn md-controls__btn--receive"]/img)[last()]')   #通話按鈕
    open_talk = (By.XPATH, '//p[@class="md-msg"][1]')   #第一位會員通話
    verify_join = (By.XPATH, "//span[contains(text(), '已加入')]")    #確認客服加入對話
    admin_end = (By.XPATH, "//p[@class='chat-pool__system']/span[contains(text(),'对话结束')]") #對話結束事件
    select_id = "//p[text()='"    #在會話版 到指定的站點或聊天群組 需組合
    talk_opened = (By.XPATH, "//p[@class='md-msg' and text()='对话已开启']")        #後台 接聽後 顯示對話已開啟
    talk_opened_time ="//p[@class='md-name' and text()='"  #接起來訪客有先發話，利用時間確認對話已開啟 需組合
    blink_tab = (By.XPATH, "//div[contains(@class, 'site-btn__wrap--blink')]/p")  # 目前所在的會話版
    activesite = (By.XPATH, "//div[contains(@class, 'site-btn__wrap--active')]/p")  #會話板 鎖定的站點

    conversation_account =(By.XPATH, '((//div[@class="md-controls__btn md-controls__btn--receive"]/img)[last()])/../../div[1]/p')  #會話板 聊天群組 名稱
    active_conversation_account = (By.XPATH, "//*[@class='chat-list-body__item chat-list-body__item--active']//p[@class='md-name']")
    conversation_group_reddot = "//span[@class='md-badge__count']//..//..//..//*[text()='"       #會話板 聊天群組 未讀紅點   #//span[@class='md-badge__count']//..//..//..//*[text()='Guest#Zzqtb']
    invite_cs_icon = (By.XPATH, "//img[@title='邀请其他客服']")   #邀請客服圖示
    choice_cs_span = (By.XPATH, "//span[@class='el-checkbox__inner']")   #邀請客服方格
    invite_cs_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--mini']/span[text()='邀请']")    #邀請客服按鈕
    be_invite_cs = (By.XPATH, "//span[@class='el-checkbox__label']")
    leave_icon = (By.XPATH, "//img[@title='离开群组']")    #離開群組圖示
    leave_confirm = (By.XPATH, "//button[@type='button']/span[contains(text(),'离开')]")    #確定離開按鈕
    messages_before_in = (By.XPATH, "//div[@class='chatbubble__msg chatbubble__msg--isUpdated']/p/span")    #爬新客服加入前對話內容
    leave_alert = (By.XPATH, "//p[@class='el-message__content' and text()='请邀请其他客服再离开']")   #最後一位客服離開跳錯誤訊息
    conversation_setting = (By.XPATH, "//i[@class='el-icon-s-tools']/..")      #會話設置
    window_mode_switch = (By.XPATH, "//span[text()='视窗模式:']/../div[@class='el-switch']/span[@class='el-switch__core']")   #視窗模式切換鈕
    cs_close = (By.XPATH, "//img[@title='挂断']")   #掛斷鈕
    cs_confirm_close = (By.XPATH, "//span[contains(text(),'结束')]")    #掛斷確定鈕
    admin_lock = (By.XPATH, "//div[@class='v-modal']")  #提示框彈出時，底部鎖住
    answer_fail = (By.XPATH, "//*[text()='已被其他客服接待']")     #後台同時接聽失敗訊息
    input_field = (By.XPATH, "//div[@class='send-msg__area']")   #傳送訊息框
    span_locator = "//span[text()='"   #找對話訊息  #需組合
    sendimg_input_ad = (By.XPATH, "//input[@class='el-upload__input']")   #傳圖input
    img_uploading = (By.XPATH, "//div[@class='send-msg__uploadItem el-loading-parent--relative']")    #圖正在上傳
    personal_icon = (By.XPATH, "//img[@title='个人资讯']")      #個人資訊圖示
    nickname_info = (By.XPATH, "//h5[text()='昵称']/../p")     #暱稱資訊
    account_info = (By.XPATH, "//h5[text()='账号']/../p")      #帳號資訊
    file_group_alert = (By.XPATH, "//p[text()='是否对话归档']")     #歸檔提示窗
    file_group_confirm = (By.XPATH, "//span[contains(text(),'确认')]")  #歸檔確定鈕
    choice_group = (By.XPATH, "//p[text()='请选择聊天群组']")           #请选择聊天群组字樣
    # chat_row = (By.XPATH, "//div[@class='chat-pool__row']")           #會話框每行資料    
    message_divs = (By.XPATH, "//div[@class='chat-pool__row']/div")          #訊息文字, 不含事件 ,含名稱/時間/訊息內容
    search_img = (By.XPATH,"//div[@class='tool-btn']/img[@title='查找记录']") #查找紀錄按鈕
    search_opened_img = (By.XPATH, "//div[@class='tool-btn tool-btn--active']/img[@title='查找记录']")  #已開啟的查找紀錄按鈕
    search_input = (By.XPATH,"//input[@class='el-input__inner' and @placeholder='请输入内容']") #查找紀錄輸入框
    history_area = (By.XPATH, "//div[@class='chat-history']")   #查找紀錄的整個區塊
    history_items = (By.XPATH, "//div[@class='chat-history__item']")            #查找紀錄的資料框
    history_empty = (By.XPATH, "//p[@class='chat-history__empty--text']")       #查找紀錄為空
    
class AdminChatPage(AdminBasePage):

    #後台傳送訊息
    def admin_send_message(self,message):
        try:
            self.wait_visibility(ChatLocator.input_field)
            self.type(ChatLocator.input_field, message)
            self.type_enter(ChatLocator.input_field)
        except:
            raise EOFError('後台傳送訊息失敗')

    #後台確認收到訊息
    def admin_check_message(self,message):
        mes = (By.XPATH, self.mix_xpath(ChatLocator.span_locator, message))
        assert self.wait_visibility_status(mes) , '後台接收訊息失敗，訊息內容：'+ message 


    # 接聽 前台確認 後台點進聊天室              #前台需另外確認 check_service_joined
    def admin_answer_and_open(self):
        try:
            self.wait_visibility(ChatLocator.phone_call_img)
        except:
            raise EOFError('未響鈴')
        try:
            self.sleep(1)
            self.click(ChatLocator.phone_call_img)                                           #接聽
            # self.wait_visibility(ChatLocator.talk_opened)
            self.sleep(1)
            self.click(ChatLocator.open_talk)
        except:
            raise EOFError('接聽失敗')
        self.sleep(1)
        self.click(ChatLocator.open_talk)               #進入聊天室


    # 接聽 前台確認 後台點進聊天室              #前台需另外確認 check_service_joined
    def already_talking_answer_and_open(self, guest):
        try:
            self.sleep(1)
            self.click(ChatLocator.phone_call_img)                                           #接聽
            t_xpath = (By.XPATH, str(ChatLocator.talk_opened_time + guest + "']/../p[@class='md-time']"))    #//p[@class='md-name' and text()='Guest#hDCs5']/../p[@class='md-time']
            self.wait_visibility(t_xpath)
        except:
            raise EOFError('接聽失敗')
        self.sleep(1)
        self.click(t_xpath)               #進入聊天室


    # 進入已開啟的對話
    def admin_open_talk(self):
        try:
            self.wait_visibility(ChatLocator.talk_opened)
            self.click(ChatLocator.open_talk)   
            self.wait_visibility(ChatLocator.verify_join)   
        except:
            raise EOFError('進入對話失敗')
    
    #確認 後台 是否響鈴 會回傳訪客名稱
    def check_ringing(self):
        try:
            self.sleep(1)
            self.wait_visibility(ChatLocator.phone_call_img)
            return self.find_element(ChatLocator.conversation_account).text
        except:
            raise EOFError("沒響鈴")

    #進入指定的站點
    def into_select_site(self, siteID):  #select_id= (By.XPATH, "//p[text()='站點2_組2'")
        self.sleep(1)
        try:
            select_id = (By.XPATH, self.mix_xpath(ChatLocator.select_id,siteID))
            self.click(select_id)
            self.sleep(1)
        except:
            raise EOFError("進入 '%s' 站點失敗" %(siteID))

    #進入指定聊天群組
    def into_select_group(self, guest_ID):
        self.sleep(2)
        try:
            guest_id = (By.XPATH, self.mix_xpath(ChatLocator.select_id,guest_ID))
            self.wait_visibility(guest_id)
            self.click(guest_id)
        except:
            raise EOFError("進入 '%s' 聊天群組失敗" %(guest_ID))
        

    def check_site_blink(self, site_ID):
        now_site = self.get_text(ChatLocator.activesite)
        if now_site == site_ID:
            pass
        else:
            assert self.get_text(ChatLocator.blink_tab) == site_ID, f'未讀訊息的站點錯誤'


    #確認站點未讀訊息紅點提示
    def check_site_red_dot(self, site_ID):
        now_site = self.get_text(ChatLocator.activesite)
        if now_site == site_ID:
            pass
        else:
            try:
                site_xpath= (By.XPATH, str(ChatLocator.select_id+site_ID+"']/../../sup"))
                self.wait_visibility(site_xpath)
            except:
                raise EOFError("確認站點 '%s' 未讀紅點提示失敗" %(site_ID))
    
    #確認會話板聊天群組未讀紅點提示
    def check_group_red_dot(self, guest_ID):
        self.sleep(1)
        now_group = self.get_text(ChatLocator.active_conversation_account)
        if now_group == guest_ID:
            pass
        else:
            try:
                guest_xpath= (By.XPATH, self.mix_xpath(ChatLocator.conversation_group_reddot, guest_ID))
                self.wait_visibility(guest_xpath)
                # print("成功找到 聊天群組 '%s' 紅點提示" %(guest_ID))
            except:
                raise EOFError("確認聊天群組 '%s' 未讀紅點提示失敗" %(guest_ID))
        
    #邀請客服 取得客服名
    def invite_cs(self):                             
        try:
            self.wait_visibility(ChatLocator.invite_cs_icon)
            self.click(ChatLocator.invite_cs_icon)
            self.wait_visibility(ChatLocator.choice_cs_span)
            self.sleep(1)
            second_cs = self.get_text(ChatLocator.be_invite_cs)
            self.click(ChatLocator.choice_cs_span)
            self.click(ChatLocator.invite_cs_btn)
        except:
            raise EOFError("邀請客服失敗")
        cs_name = second_cs.split('(')
        return cs_name[0]
    
    #驗證某客服加入對話
    def verify_person_join(self, name):                 
        try:
            verify_name_join = (By.XPATH, f"//span[contains(text(),'{name} 已加入')]")
            self.wait_visibility(verify_name_join)
        except:
            raise EOFError(f"{name}未加入對話")
    
    #新加入客服驗證加入前對話
    def text_before_invite(self,textfromSE,textfromAD):
        self.wait_visibility(ChatLocator.messages_before_in)
        elements = self.find_elements(ChatLocator.messages_before_in)
        messages = [x.text for x in elements]
        messageFE = messages[-2].replace(' ','')
        messageAD = messages[-1].replace(' ','')
        textfromSE = textfromSE.replace(' ','')
        textfromAD = textfromAD.replace(' ','')
        assert textfromSE == messageFE, '加入前對話，前台比對錯誤'
        assert textfromAD == messageAD, '加入前對話，後台比對錯誤'
    
    #客服離開對話
    def leave_conversation(self):
        self.wait_visibility(ChatLocator.leave_icon)
        self.click(ChatLocator.leave_icon)
        self.wait_visibility(ChatLocator.leave_confirm)
        self.click(ChatLocator.leave_confirm)

    #驗證還在的客服可看離開對話事件       #需再驗證 (1)已離開客服結束對話 (2)前台出現客服離開訊息 
    def leave_check(self, name):
        try:
            VERIFY_CS_LEAVE = (By.XPATH, f"//span[contains(text(),'{name} 已离开')]")
            self.wait_visibility(VERIFY_CS_LEAVE)
        except:
            raise EOFError(f'還在的客服沒看 {name} 離開事件')
    
    #確認客服 對話結束/已離開對話
    def check_chat_end(self):
        try:
            self.wait_visibility(ChatLocator.admin_end) 
        except:
            raise EOFError('客服對話未結束')

    #最後一位客服離開對話
    def last_cs_leave_check(self):
        self.leave_conversation()
        try:
            self.wait_visibility(ChatLocator.leave_alert) 
        except:
            raise EOFError('最後一位客服離開對話')
    
    #開啟視窗模式
    def window_mode_on(self):
        try:
            self.click(ChatLocator.conversation_setting)
            if self.is_element_finded(ChatLocator.window_mode_switch) is True:
                self.click(ChatLocator.window_mode_switch)
            self.click(ChatLocator.conversation_setting)
        except:
            raise EOFError('視窗模式切換失敗')

    #後端掛斷
    def admin_hang_up_phone(self):
        try:
            self.wait_visibility(ChatLocator.cs_close)
            self.click(ChatLocator.cs_close)
            self.wait_visibility(ChatLocator.admin_lock)
            self.wait_visibility(ChatLocator.cs_confirm_close)
            self.sleep(1)
            self.click(ChatLocator.cs_confirm_close)
        except:
            raise EOFError('掛斷對話失敗')
    

    #驗證後台已掛斷(多人)
    def verify_phone_close_multi(self, admin_pages):
        self.sleep(2)
        for ap in admin_pages:
            assert ap.adminBasePage().is_element_finded(ChatLocator.admin_end) , '後台對話未結束'

    #多客服接聽 1客服進聊天室
    def admins_answer_one_open(self, account, admin_page, q):
        self.click(ChatLocator.phone_call_img)        
        try:
            self.wait_visibility(ChatLocator.answer_fail)          
            # print(f'{account}沒接聽到')
        except:
            self.wait_visibility(ChatLocator.talk_opened)
            self.click(ChatLocator.open_talk)               
            self.wait_visibility(ChatLocator.verify_join)
            q.put(admin_page)


    #後台傳送圖片
    def admin_send_img(self):
        img_name_list=['img_1.jpg','img_2.jpg','img_3.jpg','img_4.jpg','img_5.jpg','img_6.jpg','img_體育遊戲.jpg']
        pics = random.randint(1,3)
        for x in range(pics):
            ran_img = random.choice(img_name_list)

            filepath = '/pages/files/'
            apath = root_path.replace('\\','/') + filepath + ran_img             #取圖片絕對路徑
            self.type(ChatLocator.sendimg_input_ad, apath)
            # self.wait_visibility(ChatLocator.img_uploading)          #等待圖片開始上傳
            # img_upload_done = (By.XPATH, f"//div[@class='send-msg__uploadItem'][{str(x+1)}]")

            img_upload_done = (By.XPATH, "//div[contains(@class, 'chatbubble__msg--isUpdated')]")
            self.wait_visibility(img_upload_done)       #等待圖片上傳完成

        self.click(ChatLocator.input_field)
        self.type_enter(ChatLocator.input_field)
        self.type_enter(ChatLocator.input_field)
        sleep(5)
        return pics
        
    # 後台驗證圖片
    def cs_verify_img(self, guest, imgs):
        sleep(5)
        verify_img_admin = (By.XPATH, f"//p[@class='chatbubble__chatname' and text()='{guest}']/../..//img")
        try:
            self.sleep(1)
            self.wait_visibility(verify_img_admin)
        except:
            raise EOFError('傳送圖片失敗')
        ad_imgs = self.find_elements(verify_img_admin)
        assert len(ad_imgs) == imgs , f'圖片數量不正確，前台傳送{imgs}張，後台接收{len(ad_imgs)}張'

    # 取得個人資訊暱稱和帳號
    def personal_info(self):
        try:
            self.wait_visibility(ChatLocator.personal_icon)
            self.click(ChatLocator.personal_icon)           
        except:
            raise EOFError('後台開啟訪客個人資訊失敗')
        self.wait_visibility(ChatLocator.nickname_info)
        nickname = self.get_text(ChatLocator.nickname_info)   
        account_info = self.get_text(ChatLocator.account_info)

        return nickname, account_info

    # 驗證暱稱和帳號
    def verify_name(self, channel_account, guest_id, nickname, account_info):
        if "(" in nickname:
            nicknameA, nicknameB = nickname.replace("(","").replace(")","").split()    
            accountA, accountB = account_info.replace("(","").replace(")","").split()
            if channel_account == nicknameA == accountA:
                if guest_id == nicknameB == accountB:
                    pass
                else:
                    raise EOFError('訪客名稱和個人資訊不一致')
            else:
                raise EOFError('品牌帳號和個人資訊不一致，可能沒設第三方接入')
        elif guest_id == nickname:  # channel_account == guest_id == nickname == account_info
            pass
        else:
            raise EOFError('暱稱和帳號不一致，可能沒設第三方接入')


    
    # 指定訪客歸檔
    def file_group(self, guest_id):
        try:
            # //p[text()='Guest#7TERo']/../..//p[text()='对话已结束']
            group_close = "//p[text()='" + guest_id + "']/../..//p[text()='对话已结束']"
            close_xpath = (By.XPATH, group_close)
            self.wait_visibility(close_xpath)                           #確認左側對話已結束
            # //p[text()='Guest#ATccw']/../..//div[@class='md-controls']
            controls_close = "//p[text()='" + guest_id + "']/../..//div[@class='md-controls']"
            controls_xpath = (By.XPATH, controls_close)
            self.sleep(2)
            self.wait_visibility(controls_xpath)                        #確認歸檔按鈕出現
            self.click(controls_xpath)                                  #點擊歸檔按鈕
            self.wait_visibility(ChatLocator.file_group_confirm)        #確認歸檔彈窗出現
            self.click(ChatLocator.file_group_confirm)                  #點擊彈窗確認按鈕
            self.check_operation_error()
            self.wait_visibility(ChatLocator.choice_group)              #確認右側對話框為空
            # guest_xpath= (By.XPATH, self.mix_xpath(ChatLocator.select_id, guest_id))
            # self.wait_invisibility(guest_xpath)                         #確認此聊天群組消失
        except:
            raise EOFError(f"歸檔失敗")



    # 會話框搜尋查找紀錄
    def search_group_message(self):
        self.window_mode_on()                   # 會話設置 單視窗
        self.sleep(2)
        
        messages_list = self.find_elements(ChatLocator.message_divs)
        self.click(ChatLocator.search_img)              # 點擊 查找紀錄按鈕
        self.wait_visibility(ChatLocator.history_area)  # 確認 查找區塊出現
        self.wait_visibility(ChatLocator.search_input)  # 確認 搜尋輸入框出現

        self.search_message(messages_list)
        self.search_random()
        self.search_message(messages_list)

        self.click(ChatLocator.search_opened_img)
        self.wait_invisibility(ChatLocator.search_input)  # 確認 搜尋輸入框隱藏
        
        
        
    # 從對話中挑其中一則訊息的一個字來做查詢，並比對查詢到的資料 名稱/時間/訊息內容是否一致
    def search_message(self, message_list):
        mes_dict={}
        ran_data = random.choice(message_list).text.split('\n', 2)
        a=mes_dict['name'] = ran_data[0]
        b=mes_dict['time'] = ran_data[1][:5]
        c=mes_dict['text'] = ran_data[2]
        
        random_mes = random.choice(mes_dict['text'])        # 隨機從text中抽一個字
        # print(random_mes)
        self.type(ChatLocator.search_input, random_mes)
        self.sleep(2)

        check_find = False
        history_list = self.find_elements(ChatLocator.history_items)
        for history in history_list:
            buf = history.text
            if (mes_dict['text'] in buf) & (mes_dict['name'] in buf) & (mes_dict['time'] in buf):
                check_find = True
                break
        if check_find == False:
            raise EOFError(f"查詢歷史訊息失敗...找不到 名稱:{mes_dict['name']} 時間:{mes_dict['time']} 訊息內容:{mes_dict['text']}")
        

    # 搜尋亂數產生的字串
    def search_random(self):
        random_str = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(10))
        self.type(ChatLocator.search_input, random_str)
        self.sleep(2)
        self.wait_visibility(ChatLocator.history_empty)  # 確認 查無資料


    # 爬下所有訊息內容 不含事件
    def get_all_message(self):
        messages_list = self.find_elements(ChatLocator.message_divs)   
        mes_list = []   #含 mes_dict 字典
        for data in messages_list:
            data_list = data.text.split('\n', 2)    # 陣列 分為名稱 時間 訊息
            mes_dict = {}
            mes_dict['name'] = data_list[0]
            mes_dict['time'] = data_list[1]
            mes_dict['text'] = data_list[2]
            mes_list.append(mes_dict)
        return mes_list

