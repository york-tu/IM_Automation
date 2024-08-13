from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re

class ChatRoomPageLocator:
    # --------------- 聊天室標題 詳情 ---------------
    menu_icon = (By.XPATH, "//div[@class='menu-icon']/div")
    detile_close = (By.XPATH, "//div[@class='header-close']/div[1]")
    detile_back = (By.XPATH, "//div[@class='header-back']/div[1]")
    detile_title = (By.XPATH, "(//div[@class='header-title'])[1]")
    room_title = (By.XPATH, "//p[@class='chat-detail__name__text']")
    setting_btn = (By.XPATH, "//div[@class='head-icon__img -more']")
    setting_title = (By.XPATH, "//div[@class='chat-setting-modal']//div[@class='header-title']")
    system_message = (By.XPATH, "(//p[@class='wcr-system-message__text'])[last()]")
    chat_room_last_msg = (By.XPATH, "(//div[@class='wcr-list__msg']//span[1])[last()]")
    # -------------------- 會員暱稱 --------------------
    friend_edit_btn = (By.XPATH, "//div[@class='text-edit']")
    friend_edit_text = (By.XPATH, "//p[@class='chat-info__name__text']")
    friend_edit_input = (By.XPATH, "//input[@class='user-name__input']")
    friend_edit_submit = (By.XPATH, "//p[text()='保存']/..")
    # -------------------- 會員備註 --------------------
    friend_remark_btn = (By.XPATH, "//p[@class='remark__text']")
    friend_remark_pen = (By.XPATH, "//p[@class='chat-info__desc__text']/../div[@class='text-edit']")
    friend_remark_text = (By.XPATH, "//p[@class='chat-info__desc__text']")
    friend_remark_hint = (By.XPATH, "//textarea[@placeholder='描述最長至300字...']")
    friend_remark_input = (By.XPATH, "//textarea[@class='chat-info__textarea__input']")
    friend_remark_submit = (By.XPATH, "//div[@class='submit-btn__img']/..")
    # -------------------- 會員詳情設定 --------------------
    friend_delete = (By.XPATH, "//p[text()='删除好友']")
    friend_blocks = (By.XPATH, "//label[@for='blocks']")
    friend_notify = (By.XPATH, "//label[@for='notify']")
    # -------------------- 聊天室訊息輸入 --------------------
    message_mask = (By.XPATH, "//div[text()='解除封锁']")
    message_input = (By.XPATH, "//div[@class='enter-message__input']")
    message_submit = (By.XPATH, "//div[@class='prepend__btn btn-send']")
    # -------------------- 聊天室訊息操作 --------------------
    message_menu = (By.XPATH, "//div[@class='el-menu -show']")
    message_copy = (By.XPATH, "//p[@class='menu-text' and text() = '复制']")
    message_reply = (By.XPATH, "//p[@class='menu-text' and text() = '回覆']")
    message_revoke = (By.XPATH, "//p[@class='menu-text' and text() = '撤回']")
    message_pin = (By.XPATH, "//p[@class='menu-text' and text() = '设为公告']")
    # -------------------- 訊息回覆框 --------------------
    reply_preview_title = (By.XPATH, "//div[@class='chat-detail__footer']//p[@class='reply-item__name__text']")
    reply_preview_text = (By.XPATH, "//div[@class='chat-detail__footer']//p[@class='reply-item__msg__text']")
    reply_view_title = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__name__text'])[last()]")
    reply_view_text = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__msg__text'])[last()]")
    reply_msg = (By.XPATH, "(//div[@class='wcr-list__block']//p[@class='reply-item__msg__text'])[last()]")
    # -------------------- 二次確認彈窗 --------------------
    confirm_popup = (By.XPATH, "//div[@class='common-modal']")
    confirm_title = (By.XPATH, "//div[@class='common-modal__header']")
    confirm_text = (By.XPATH, "//p[@class='common-info__text']")
    confirm_submit = (By.XPATH, "//button[@class='btn btn-danger btn-md']")
    confirm_cancel = (By.XPATH, "//button[@class='btn btn-primary btn-md btn-outline']")
    # -------------------- 訊息置頂公告 --------------------
    pin_list = (By.XPATH, "//div[@class='announcement-list']")
    pin_list_show = (By.XPATH, "//div[@class='wcr-system-announcement -show']")
    pin_btn = (By.XPATH, "//div[@class='announcement-toggle']")
    pin_no_show = (By.XPATH, "(//p[@class='announcement-list__no-show'])[1]")
    pin_msg = (By.XPATH, "//p[@class='head-text']")
    pin_frist_msg = (By.XPATH, "(//p[@class='head-text'])[1]")
    pin_popup = (By.XPATH, "//div[@class='wcr-system-alert']")
    pin_popup_close = (By.XPATH, "//div[@class='alert__close']")
    # -------------------- 表情符號 --------------------
    emoji_panel = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']")
    emoji_good = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][1]")
    emoji_funny = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][2]")
    emoji_love = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][3]")
    emoji_sad = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][4]")
    emoji_wow = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']//div[@class='el-emoji__item'][5]")
    emoji_view = (By.XPATH, "//div[@class='el-emoji -emoji-view']")
    emoji_list = (By.XPATH, "//div[@class='el-emoji -emoji-panel -show']")
    # -------------------- 群組設定 --------------------
    group_name = (By.XPATH, "//p[@class='chat-info__name__text']")
    group_member_count = (By.XPATH, "//p[@class='rough-member-list__text']")
    group_user_add = (By.XPATH, "//div[@class='ui-tableviewcell__icon__img -user-add']")
    group_rule_btn = (By.XPATH, "//p[text()='群组设定']/..//div[contains(@class,'-arrow')]")
    group_rule_name = (By.XPATH, "//p[@class='chat-name__text']")
    group_rule_name_btn = (By.XPATH, "//p[@class='chat-name__text']/..//div[contains(@class,'-pencil')]")
    group_rule_input = (By.XPATH, "//input[@placeholder='请输入群组名称']")
    group_rule_submit = (By.XPATH, "//p[text()='保存']/..")
    group_rule_count = (By.XPATH, "//p[text()='群组设定']/..//p[@class='ui-tableviewcell__num']")
    group_rule_text = (By.XPATH, "//label[@for='member-permission-can_send_messages']")
    group_rule_img = (By.XPATH, "//label[contains(@for,'_send_images')]/..//input[not(@disabled)]")
    group_rule_img_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_images')]")
    group_rule_link = (By.XPATH, "//label[contains(@for,'_send_hyperlink')]/..//input[not(@disabled)]")
    group_rule_link_btn = (By.XPATH, "//input[not(@disabled)]/..//label[contains(@for,'_send_hyperlink')]")
    group_rule_user = (By.XPATH, "//label[@for='member-permission-can_invite_users']")
    
    group_ = (By.XPATH, "")
    group_admin_btn = (By.XPATH, "//p[text()='管理员']/..//div[contains(@class,'-arrow')]")
    group_block_btn = (By.XPATH, "//p[text()='黑名单']/..//div[contains(@class,'-arrow')]")


    # 特定訊息定位
    def message_locator(self, text):
        locator = (By.XPATH, f"(//span[text()='{text}'])[last()]")
        return locator
    
    # 特定訊息表情符號定位
    def message_emoji_locator(self, text):
        locator = (By.XPATH, f"(//span[text()='{text}']/ancestor-or-self::div[contains(@class,'wcr-list__content')]//div[@class='open-emoji'])[last()]")
        return locator

class ChatRoomPage(BasePage):
    def into_setting(self):
        self.click(ChatRoomPageLocator.setting_btn)
        assert self.get_text(ChatRoomPageLocator.detile_title).__contains__('详情') ,f'進入設定頁面有誤'
    
    def edit_nickname(self, nickname):
        self.click(ChatRoomPageLocator.friend_edit_btn)
        self.type(ChatRoomPageLocator.friend_edit_input, nickname)
        self.click(ChatRoomPageLocator.friend_edit_submit)
        assert self.get_text(ChatRoomPageLocator.friend_edit_text) == nickname ,f'暱稱修改有誤'

    def friend_nickname(self):
        user_name = self.get_text(ChatRoomPageLocator.friend_edit_text)
        name_list = ['testaaaa', user_name]
        
        for name in name_list:
            self.edit_nickname(name)
            self.click(ChatRoomPageLocator.detile_close)
            assert self.get_text(ChatRoomPageLocator.room_title) == name ,f'暱稱修改後沒有同步聊天室名稱'       #名稱修改後列表名稱還沒去檢查
            
            self.into_setting() 

    def friend_remark(self):
        text_list = ['測試TeSt12345!@#$%测试', '']
        for text in text_list:
            self.edit_remark(text)
            
            if text == '' :
                assert self.is_element_finded(ChatRoomPageLocator.friend_remark_btn) == True
            else:
                assert self.get_text(ChatRoomPageLocator.friend_remark_text) == text, f'備註修改有誤'

    def edit_remark(self, text):
        if self.is_element_finded(ChatRoomPageLocator.friend_remark_btn) == True:
            self.click(ChatRoomPageLocator.friend_remark_btn)
            assert self.is_element_finded(ChatRoomPageLocator.friend_remark_hint) == True, f'輸入提示文案有誤'
        else:
            self.click(ChatRoomPageLocator.friend_remark_pen)
        
        self.type_delete(ChatRoomPageLocator.friend_remark_input)
        self.type(ChatRoomPageLocator.friend_remark_input, text)
        self.click(ChatRoomPageLocator.friend_remark_submit)

    def friend_block(self):
        self.click(ChatRoomPageLocator.friend_blocks)
        self.click(ChatRoomPageLocator.detile_close)
        self.sleep(1)
        assert self.is_element_finded(ChatRoomPageLocator.message_mask) == True, f'文字輸入匡沒有被封鎖'

    def friend_delete(self):
        self.click(ChatRoomPageLocator.friend_delete)
        
        if self.is_element_finded(ChatRoomPageLocator.confirm_popup) == True:
            assert self.get_text(ChatRoomPageLocator.confirm_text).__contains__('同时删除与该联络人的聊天纪录。'), f'刪除好友彈窗標題有誤'
            self.click(ChatRoomPageLocator.confirm_submit)
    
    def send_message(self, message):
        if self.is_element_finded(ChatRoomPageLocator.message_input) == True:
            self.click(ChatRoomPageLocator.message_input)
            self.type(ChatRoomPageLocator.message_input, message)

        if self.is_element_finded(ChatRoomPageLocator.message_submit) == True:
            self.click(ChatRoomPageLocator.message_submit)

    def send_text_message(self):
        messages = '測試TeSt12345!@#$%测试'
        num = 0
        for _ in range(0,6):
            text = str(messages) +'#'+ str(num)
            self.send_message(text)
            self.sleep(0.5)
            num = num + 1
    
    def send_url_message(self):
        messages = ['www.google.com.tw','tw.yahoo.com']

        for message in messages:
            message_url = 'https://' + message + '/'
            self.send_message(message_url)
            self.check_rul_message(message_url)
    
    def check_rul_message(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)) == True:
            self.click(ChatRoomPageLocator.message_locator(self, message))
        
        self.switch_last_page()
        self.sleep(3)
        message = message[message.index('//'):].replace('/','')
        current_url = self.get_url()
        assert current_url.__contains__(message), f'超連結開啟有誤'

        self.close_browser()
        self.switch_last_page()
        self.sleep(1)

    def message_copy(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)) == True:
            self.context_click(ChatRoomPageLocator.message_locator(self, message))
            self.click(ChatRoomPageLocator.message_copy)
        
        self.click(ChatRoomPageLocator.message_input)
        self.type_paste(ChatRoomPageLocator.message_input)

        if self.is_element_finded(ChatRoomPageLocator.message_submit) == True:
            self.click(ChatRoomPageLocator.message_submit)

    def message_reply(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)) == True:
            self.context_click(ChatRoomPageLocator.message_locator(self, message))
            self.click(ChatRoomPageLocator.message_reply)
        

        reply_pre_title = self.get_text(ChatRoomPageLocator.reply_preview_title)
        reply_pre_msg = self.get_text(ChatRoomPageLocator.reply_preview_text)

        assert reply_pre_title.__contains__('回复'), f'訊息回覆預覽標題有誤'
        assert reply_pre_msg == message, f'回覆訊息預覽有誤'

        self.click(ChatRoomPageLocator.message_input)
        self.type(ChatRoomPageLocator.message_input, '回覆訊息測試Test')

        if self.is_element_finded(ChatRoomPageLocator.message_submit) == True:
            self.click(ChatRoomPageLocator.message_submit)
        
        self.sleep(0.5)
        reply_title = self.get_text(ChatRoomPageLocator.reply_view_title)
        reply_msg = self.get_text(ChatRoomPageLocator.reply_view_text)
        
        assert reply_pre_title.__contains__(reply_title), f'訊息回覆標題有誤'
        assert reply_msg == message, f'回覆訊息預覽有誤 發送訊息顯示: {message} 回復訊息顯示 {reply_msg}'

    def check_reply_disappear(self, message):
        self.wait_message_finish()
        
        if self.get_text(ChatRoomPageLocator.chat_room_last_msg) == message:
            assert self.get_text(ChatRoomPageLocator.reply_msg) == '原始讯息已不存在', f'訊息遺失錯誤提示有誤'
        
    def message_revoke(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)) == True:
            self.context_click(ChatRoomPageLocator.message_locator(self, message))
            
        self.click(ChatRoomPageLocator.message_revoke)
        
        if self.is_element_finded(ChatRoomPageLocator.confirm_popup) == True:
            assert self.get_text(ChatRoomPageLocator.confirm_title) == '撤回讯息', f'撤回訊息彈窗標題有誤'
            self.click(ChatRoomPageLocator.confirm_submit)

            self.wait_loading_finish()
            if self.get_text(ChatRoomPageLocator.system_message).__contains__('设定一笔讯息为公告'):
                if self.is_element_finded(ChatRoomPageLocator.pin_list_show) == False:
                    self.click(ChatRoomPageLocator.pin_btn)
                pin_list = self.get_pin_message()
                assert message not in pin_list, f'訊息撤回後，公告沒有消失'
            else:
                assert self.get_text(ChatRoomPageLocator.system_message).__contains__('你已撤回一则讯息'), f'撤回訊息系統訊息有誤'

    def delete_all_pin(self):
        while self.is_element_finded(ChatRoomPageLocator.pin_list):
            if self.is_element_finded(ChatRoomPageLocator.pin_list_show) == False:
                self.click(ChatRoomPageLocator.pin_btn)

            if self.is_element_finded(ChatRoomPageLocator.pin_no_show) == True:
                before_message = self.get_text(ChatRoomPageLocator.pin_frist_msg)
                self.click(ChatRoomPageLocator.pin_no_show)
                self.sleep(1)

                if self.is_element_finded(ChatRoomPageLocator.pin_list_show) == True:
                    after_message = self.get_text(ChatRoomPageLocator.pin_frist_msg)
                    assert before_message != after_message, f'公告取消失敗'
                else:
                    break
            else:
                print('角色權限不足')
                break

    def message_pin(self, message):
        self.wait_message_finish()
        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)) == True:
            self.context_click(ChatRoomPageLocator.message_locator(self, message))
            if self.is_element_finded(ChatRoomPageLocator.message_menu) == True:
                self.click(ChatRoomPageLocator.message_pin)
        
        if self.is_element_finded(ChatRoomPageLocator.pin_popup) == True:
            assert self.get_text(ChatRoomPageLocator.pin_popup) == '公告已满5则，无法新增，请取消欲替换的公告', f'彈窗訊息有誤'
            self.click(ChatRoomPageLocator.pin_popup_close)
            return False
        else:
            self.sleep(1)
            pin_frist = self.get_text(ChatRoomPageLocator.pin_frist_msg)
            assert pin_frist == message , f'公告顯示有誤'
            assert self.get_text(ChatRoomPageLocator.system_message).__contains__('设定一笔讯息为公告'), f'設定置頂公告系統訊息有誤'
            return True
    
    def pin_full_messages(self):
        message = '測試TeSt12345!@#$%测试#'
        pin_sort = [2, 4, 5, 1, 0, 3]
        
        times = 1
        expected_list = []
        for number in pin_sort:
            text = message + str(number)
            if times < 6:
                assert self.message_pin(text) == True
                expected_list.append(text)
            else:
                assert self.message_pin(text) == False
                break
            times = times + 1

        if self.is_element_finded(ChatRoomPageLocator.pin_list_show) == False:
            self.click(ChatRoomPageLocator.pin_btn)
        Reality_list = self.get_pin_message()
        Reality_list.reverse()

        assert Reality_list == expected_list ,f'公告排序有誤'
        self.click(ChatRoomPageLocator.pin_btn)

    def get_pin_message(self):
        message_num = []
        for message in self.find_elements(ChatRoomPageLocator.pin_msg):
            message_num.append(message.text)

        return message_num
    
    def add_message_emoji(self, message):
        self.wait_message_finish()

        if self.is_element_finded(ChatRoomPageLocator.message_locator(self, message)):
            self.click(ChatRoomPageLocator.message_emoji_locator(self, message))

            assert self.is_element_finded(ChatRoomPageLocator.emoji_panel)

        self.click(ChatRoomPageLocator.emoji_wow)
    
    def change_group_name(self, name_old, name_new):
        self.wait_loading_finish()
        
        assert name_old == self.get_text(ChatRoomPageLocator.group_name), f'群組聊天 名稱顯示有誤'
        
        self.click(ChatRoomPageLocator.group_rule_btn)
        if self.is_element_finded(ChatRoomPageLocator.group_rule_name) == True:
            assert name_old == self.get_text(ChatRoomPageLocator.group_rule_name), f'群組設定 名稱顯示有誤'

            self.click(ChatRoomPageLocator.group_rule_name_btn)
            self.type(ChatRoomPageLocator.group_rule_input, name_new)
            self.click(ChatRoomPageLocator.group_rule_submit)
        
            assert name_new == self.get_text(ChatRoomPageLocator.group_rule_name), f'群組設定 名稱修改後同步有誤'
        
            self.click(ChatRoomPageLocator.detile_back)
            assert name_new == self.get_text(ChatRoomPageLocator.group_name), f'群組聊天 名稱顯示有誤'
        
            self.click(ChatRoomPageLocator.detile_close)
            assert name_new == self.get_text(ChatRoomPageLocator.room_title), f'群組聊天室 名稱顯示有誤'

            system = self.get_text(ChatRoomPageLocator.system_message)
            msg_list = system.replace('「',' ').replace('」','').split(' ')
            assert msg_list[2] == name_new, f'聊天室系統訊息 名稱顯示有誤'
    
    def all_group_rule(self):
        for _ in range(0,3):
            self.wait_loading_finish()

            rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
            num = rule_count.split('/')

            if  int(num[0]) < 4:
                self.click(ChatRoomPageLocator.group_rule_btn)
                self.sleep(1)

                if num[0] == '0':
                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_img) == False
                    assert self.is_element_finded(ChatRoomPageLocator.group_rule_link) == False

                    self.click(ChatRoomPageLocator.group_rule_text)
                    self.click(ChatRoomPageLocator.group_rule_user)

                    self.sleep(1)
                    if self.is_element_finded(ChatRoomPageLocator.group_rule_img) \
                        and self.is_element_finded(ChatRoomPageLocator.group_rule_link) == True:

                        self.click(ChatRoomPageLocator.group_rule_img_btn)
                        self.click(ChatRoomPageLocator.group_rule_link_btn)

                    else:
                        print('群組權限 圖片及連結沒有連動防呆')
                    self.click(ChatRoomPageLocator.detile_back)

                elif num[0] == '1':
                    if self.is_element_finded(ChatRoomPageLocator.group_rule_img) == True:
                        self.click(ChatRoomPageLocator.group_rule_img_btn)
                        self.click(ChatRoomPageLocator.group_rule_link_btn)
                        self.click(ChatRoomPageLocator.group_rule_user)
                    else:
                        self.click(ChatRoomPageLocator.group_rule_text)

                        if self.is_element_finded(ChatRoomPageLocator.group_rule_img) and self.is_element_finded(ChatRoomPageLocator.group_rule_link) == True:

                            self.click(ChatRoomPageLocator.group_rule_img_btn)
                            self.click(ChatRoomPageLocator.group_rule_link_btn)
                    self.click(ChatRoomPageLocator.detile_back)

                else:
                    self.click(ChatRoomPageLocator.group_rule_text)
                    self.click(ChatRoomPageLocator.detile_back)
            else:
                break
    
    def change_group_rule(self, data):
        self.all_group_rule_close()
        sum_data = 0
        data_list = list(data)
        for num in data_list:
            sum_data += int(num)

        self.wait_loading_finish()
        if sum_data < 4:
            self.click(ChatRoomPageLocator.group_rule_btn)
            
            self.sleep(1)
            if data_list[3] == '1':
                self.click(ChatRoomPageLocator.group_rule_user)
            
            if data_list[0] == '1':
                self.click(ChatRoomPageLocator.group_rule_text)
                self.sleep(1)

                if data_list[1] == '1':
                    self.click(ChatRoomPageLocator.group_rule_img_btn)
                
                if data_list[2] == '1':
                    self.click(ChatRoomPageLocator.group_rule_link_btn)
            else:
                assert self.is_element_finded(ChatRoomPageLocator.group_rule_img) == False, f'群組權限 圖片按鈕 沒有連動防呆'
                assert self.is_element_finded(ChatRoomPageLocator.group_rule_link) == False, f'群組權限 超連結按鈕 沒有連動防呆'
                
                if data_list[1] == '1' or data_list[2] == '1':
                    sum_data -= 1
                    print('訊息發送權限沒有開啟 無法開啟 超連結與圖片權限')

            self.click(ChatRoomPageLocator.detile_back)
            rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
            num = rule_count.split('/')
            assert str(sum_data) == num[0], f'開啟群組設定 權限有誤'
        else:
            self.all_group_rule()

    def all_group_rule_close(self):
        for _ in range(0,3):
            self.wait_loading_finish()

            rule_count = self.get_text(ChatRoomPageLocator.group_rule_count)
            num = rule_count.split('/')

            if int(num[0]) != 0:
                self.click(ChatRoomPageLocator.group_rule_btn)
                self.sleep(1)
            
                if int(num[0]) < 4 :
                    if self.is_element_finded(ChatRoomPageLocator.group_rule_img) == True:
                        self.click(ChatRoomPageLocator.group_rule_text)
                    else:
                        self.click(ChatRoomPageLocator.group_rule_user)
                else:
                    self.click(ChatRoomPageLocator.group_rule_text)        
                    self.click(ChatRoomPageLocator.group_rule_user)
                
                self.click(ChatRoomPageLocator.detile_back)
            else:
                break
