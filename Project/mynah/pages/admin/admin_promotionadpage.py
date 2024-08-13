import sys
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class PromotionAdLocator:
    ad_ischecked = (By.XPATH, "//label[text()='用户聊天室']//..//div[@class='el-switch is-checked']")       #已開啟的推廣廣告開關
    ad_notchecked = (By.XPATH, "//label[text()='用户聊天室']//..//div[@class='el-switch']")     #未開啟的推廣廣告開關
    setting_ad = (By.XPATH, "//div[@class='ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline ck-blurred']/p/br")   #推廣內容
    ad_text = "推荐收藏拉斯维加斯 易记域名--https://las808.com \n 温馨提示：若长时间未收到客服回复，可能是由于国际信号微弱导致的，请您及时联系官方QQ客服进行咨询，谢谢！"
    btn_seve = (By.XPATH, "//span[text()='保存']")                  #保存按鈕
    save_success = (By.XPATH, "//*[text()='推广广告保存成功']")      #保存成功
    warn_message = (By.XPATH, "//span[text()='警告']/../../..//div[@class='el-message-box__message']")      #警告彈窗
    warm_confirm_btn = (By.XPATH, "//span[contains(text(),'确定')]")
    iframe = (By.XPATH, "//*[@class='cke_wysiwyg_frame cke_reset']")
    iframe_body = (By.XPATH,"//html/body")
    test_B = (By.XPATH, "(//div[@class='ck ck-toolbar__items']/button[1])[1]") 
class AdminPromotionAdPage(AdminBasePage):
    # 打開推廣廣告
    def open_ad(self):
        self.sleep(1)
        try:
            if self.is_element_finded(PromotionAdLocator.ad_notchecked) == True:
                self.click(PromotionAdLocator.ad_notchecked)
            self.wait_visibility(PromotionAdLocator.ad_ischecked)
            # print("詢前表單是否 '已開啟'：" + str(self.is_element_finded(FormLocator.form_ischecked)))
            
        except:
            raise EOFError("後台詢前表單開啟失敗!")


    # 關閉推廣廣告
    def close_ad(self):
        self.sleep(1)
        try:
            if self.is_element_finded(PromotionAdLocator.ad_ischecked) == True:
                self.click(PromotionAdLocator.ad_ischecked)
            self.wait_visibility(PromotionAdLocator.ad_notchecked)
            # print("詢前表單是否 '已開啟'：" + str(self.is_element_finded(FormLocator.form_ischecked)))
        except:
            raise EOFError("後台詢前表單關閉失敗!")

    # 設定推廣廣告內文
    def setting_ad_text(self):
        try:
            ad_text = str(random.randint(1,10))*5 + "\n" + PromotionAdLocator.ad_text
            self.switch_frame(PromotionAdLocator.iframe)
            self.type(PromotionAdLocator.iframe_body, ad_text)
            self.switch_default_frame()
            self.click(PromotionAdLocator.btn_seve)
            self.wait_visibility(PromotionAdLocator.save_success)
            return ad_text
        except:
            raise EOFError("設定推廣廣告失敗 "+ str(self.get_warn_message()))

    
    # 取得警告訊息
    def get_warn_message(self):
        try:
            warnMessage = self.get_text(FormLocator.warn_message)
            return warnMessage
        except:
            return 

    def check_ad_text(self, admin_text, web_text):
        assert admin_text==web_text, f"後台設定與前台顯示不一致\n後台設定：{admin_text}\n前台設定：{web_text}"

