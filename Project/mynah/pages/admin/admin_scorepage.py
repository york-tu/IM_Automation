import sys
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class ScoreLocator:
    select_left_site = "//p[@class='op-box-title' and text()='"     #需組合
    score_ischecked = (By.XPATH, "//label[text()='客服评分显示']//..//div[@class='el-switch is-checked']")       #已開啟的客服評分顯示開關
    score_notchecked = (By.XPATH, "//label[text()='客服评分显示']//..//div[@class='el-switch']")     #未開啟的客服評分顯示開關
    score_enforce_ischecked = (By.XPATH, "//label[text()='评分强制填写']//..//div[@class='el-switch is-checked']")        #已開啟的驗證碼開關
    score_enforce_notchecked = (By.XPATH, "//label[text()='评分强制填写']//..//div[@class='el-switch']")      #未開啟的驗證碼開關
    score_opinion_ischecked = (By.XPATH, "//label[text()='意见栏位显示']//..//div[@class='el-switch is-checked']")   #已開啟的綁定開關
    score_opinion_notchecked = (By.XPATH, "//label[text()='意见栏位显示']//..//div[@class='el-switch']")     #未開啟的綁定開關
    btn_add_items = (By.XPATH, "//span[text()='新增项目']")       #新增項目按鈕
    input_item_text = (By.XPATH, "//span[text()='确认']/../../../..//input[@placeholder='最多20字']")       #項目內容輸入框
    btn_add_item_confirm = (By.XPATH, "//span[text()='确认']")       #新增項目的確認按鈕
    btn_save = (By.XPATH, "//span[text()='保存']")      #保存按鈕
    save_success = (By.XPATH, "//*[text()='保存成功']")     #保存成功
    btn_delete_item = (By.XPATH, "//button[@class='el-button el-button--danger el-button--mini']")       #刪除項目按鈕
    btn_delete_last = (By.XPATH, "(//button[@class='el-button el-button--danger el-button--mini'])[last()]")    #最後一個刪除按鈕
    warn_message = (By.XPATH, "//span[text()='警告']/../../..//div[@class='el-message-box__message']/p")      #警告彈窗
    btn_warn_message = (By.XPATH, "//button[@class='el-button el-button--default el-button--small el-button--primary ']")       #警告彈窗確定鈕
    btn_search = (By.XPATH, "//i[@class='el-icon-search']/../span")         #查詢鈕
    time_zone_last = (By.XPATH, "//button[@class='el-button el-button--mini'][last()]")         #最後一個時間區塊


class AdminScorePage(AdminBasePage):

    # 客服評分項目_選擇站點，需輸入站點名稱
    def into_score_select_site(self, site_id):
        try:
            site_locator = (By.XPATH, self.mix_xpath(ScoreLocator.select_left_site, site_id))
            self.wait_visibility(site_locator)
            self.click(site_locator)
        except:
            raise EOFError("客服評分項目_選擇站點失敗")

    # 打開客服評分顯示
    def open_score(self):
        self.sleep(1)
        try:
            if self.is_element_finded(ScoreLocator.score_notchecked) == True:
                self.click(ScoreLocator.score_notchecked)
            self.wait_visibility(ScoreLocator.score_ischecked)
        except:
            raise EOFError("後台詢前表單開啟失敗!")

    # 打開評分強制填寫
    def open_score_enforce(self):
        self.sleep(1)
        try:
            if self.is_element_finded(ScoreLocator.score_enforce_notchecked) == True:
                self.click(ScoreLocator.score_enforce_notchecked)
            self.wait_visibility(ScoreLocator.score_enforce_ischecked)
        except:
            raise EOFError("後台評分強制填寫開啟失敗!")

    # 打開意見欄位顯示
    def open_score_opinion(self):
        self.sleep(1)
        try:
            if self.is_element_finded(ScoreLocator.score_opinion_notchecked) == True:
                self.click(ScoreLocator.score_opinion_notchecked)
            self.wait_visibility(ScoreLocator.score_opinion_ischecked)
        except:
            raise EOFError("後台意見欄位顯示開啟失敗!")

    # 新增評分項目
    def add_score_item(self, num):
        try:    
            try:
                items = ['請給評分', '服務滿意嗎?', '是否解決問題', '客服人員態度', '等待時間', '客服專業度', '客服回覆速度', '整體評分']
                self.wait_visibility(ScoreLocator.btn_add_items)
                ranitem = random.choice(items)
                self.click(ScoreLocator.btn_add_items)
                if num == 0:
                    ranitem = self.read_random_words()
                    if ranitem[0] == " ":
                        ranitem = ranitem[1:]
                    if ranitem[-1] == " ":
                        ranitem = ranitem[:-1]
                self.type(ScoreLocator.input_item_text, ranitem)
                self.click(ScoreLocator.btn_add_item_confirm)
                self.click(ScoreLocator.btn_save)
                self.wait_visibility(ScoreLocator.save_success)
                return ranitem
            except:
                if self.is_element_finded(ScoreLocator.warn_message) == True:
                    self.wait_visibility(ScoreLocator.btn_warn_message)
                    self.click(ScoreLocator.btn_warn_message)
                    self.wait_visibility(ScoreLocator.btn_delete_last)
                    self.click(ScoreLocator.btn_delete_last)
        except:
            raise EOFError("新增評分項目失敗 "+ str(self.get_warn_message()))

    # 刪除評分所有項目
    def delete_item(self):
        try:
            while self.is_element_finded(ScoreLocator.warn_message) == False:
                self.click(ScoreLocator.btn_delete_item)
            self.wait_visibility(ScoreLocator.btn_warn_message)
            self.click(ScoreLocator.btn_warn_message)
        except:
            raise EOFError("刪除評分項目失敗!")

    # 取得警告訊息
    def get_warn_message(self):
        try:
            warnMessage = self.get_text(ScoreLocator.warn_message)
            return warnMessage
        except:
            return 