import sys
import os
from Project.mynah.pages.admin.admin_basepage import AdminBasePage
from selenium.webdriver.common.by import By

class AIReplyLocator:
    ########### 後台 ###########
    select_site_check = (By.XPATH, "//form[@class='el-form setting-container']")        #檢查站點設定出現
    reply_ischecked = (By.XPATH, "//div[@class='el-switch is-checked']")        #已開啟智能回覆
    reply_notchecked = (By.XPATH, "//div[@class='el-switch']")        #已關閉智能回覆
    btn_save = (By.XPATH, "//span[text()='保存']")      #保存按鈕
    btn_change_confirm = (By.XPATH, "//button[@class='el-button el-button--default el-button--small el-button--primary ']")      #確認異動按鈕
    
class AdminAIResponsePage(AdminBasePage):
    
    # 智能回覆_選擇站點，需輸入站點名稱
    def into_left_select_site(self, site_id):       #//p[@class='op-box-title' and text()='站點2_組2']
        try:
            site_locator = (By.XPATH, f"//div[@class='site-name' and contains(text(),'{site_id}')]")
            self.wait_visibility(site_locator)
            self.click(site_locator)
            self.wait_visibility(AIReplyLocator.select_site_check)
        except:
            raise EOFError("智能回覆_選擇站點失敗")
    
    # 關閉智能回覆
    def close_ai_response(self):
        self.sleep(1)
        try:
            if self.is_element_finded(AIReplyLocator.reply_ischecked) == True:
                self.click(AIReplyLocator.reply_ischecked)
            self.wait_visibility(AIReplyLocator.reply_notchecked)
            self.click(AIReplyLocator.btn_save)
            self.wait_visibility(AIReplyLocator.btn_change_confirm)
            self.click(AIReplyLocator.btn_change_confirm)           
        except:
            raise EOFError("後台智能回覆關閉失敗!")