import sys
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class FormLocator:
    q_and_a = (By.XPATH, "//div[@class='chatbubble__msg chatbubble__msg--isUpdated']/p/span")       #爬後台詢前表單的問題和答案
    select_left_site = "//p[@class='op-box-title' and text()='"     #需組合
    form_ischecked = (By.XPATH, "//label[text()='询前表单']//..//div[@class='el-switch is-checked']")       #已開啟的詢前表單開關
    form_notchecked = (By.XPATH, "//label[text()='询前表单']//..//div[@class='el-switch']")     #未開啟的詢前表單開關
    form_code_ischecked = (By.XPATH, "//label[text()='验证码']//..//div[@class='el-switch is-checked']")        #已開啟的驗證碼開關
    form_code_notchecked = (By.XPATH, "//label[text()='验证码']//..//div[@class='el-switch']")      #未開啟的驗證碼開關
    form_binding_ischecked = (By.XPATH, "//label[text()='表单资料绑定']//..//div[@class='el-switch is-checked']")   #已開啟的綁定開關
    form_binding_notchecked = (By.XPATH, "//label[text()='表单资料绑定']//..//div[@class='el-switch']")     #未開啟的綁定開關
    btn_addquestion = (By.XPATH, "//span[text()='新增问题']")       #新增問題按鈕
    input_question_text = (By.XPATH, "//span[text()='确认']/../../../..//input[@placeholder='最多10字']")       #問題內容輸入框
    btn_addquestion_confirm = (By.XPATH, "//span[text()='确认']")       #新增問題的確認按鈕
    btn_save = (By.XPATH, "//span[text()='保存']")      #保存按鈕
    save_success = (By.XPATH, "//*[text()='保存成功']")     #保存成功
    btn_deletequestion = (By.XPATH, "//button[@class='el-button el-button--danger el-button--mini']")       #刪除問題按鈕
    input_binding_question = (By.XPATH, "//div[text()='访客名称']/../../td[2]//input")      #綁定問題選單
    select_binding_question = (By.XPATH, "//div[@x-placement='bottom-start' or @x-placement='top-start']/div/div/ul/li/span")       #選擇綁定問題
    warn_message = (By.XPATH, "//span[text()='警告']/../../..//div[@class='el-message-box__message']/p")      #警告彈窗

class AdminFormPage(AdminBasePage):

    # 詢前表單_選擇站點，需輸入站點名稱
    def into_left_select_site(self, site_id):       #//p[@class='op-box-title' and text()='站點2_組2']
        try:
            site_locator = (By.XPATH, self.mix_xpath(FormLocator.select_left_site, site_id))
            self.wait_visibility(site_locator)
            self.click(site_locator)
        except:
            raise EOFError("詢前表單_選擇站點失敗")

    # 打開詢前表單
    def open_form(self):
        self.sleep(1)
        try:
            if self.is_element_finded(FormLocator.form_notchecked) == True:
                self.click(FormLocator.form_notchecked)
            self.wait_visibility(FormLocator.form_ischecked)
            # print("詢前表單是否 '已開啟'：" + str(self.is_element_finded(FormLocator.form_ischecked)))
        except:
            raise EOFError("後台詢前表單開啟失敗!")

    # 關掉驗證碼
    def close_form_code(self):
        self.sleep(1)
        try:
            if self.is_element_finded(FormLocator.form_code_ischecked) == True:
                self.click(FormLocator.form_code_ischecked)
            self.wait_visibility(FormLocator.form_code_notchecked)
            self.click(FormLocator.btn_save)
            # print("驗證碼是否 '已關閉'：" + str(self.is_element_finded(FormLocator.form_code_notchecked)))
        except:
            raise EOFError("後台驗證碼關閉失敗!")

    # 關掉資料綁定
    def close_form_binding(self):
        self.sleep(1)
        try:
            if self.is_element_finded(FormLocator.form_binding_ischecked) == True:
                self.click(FormLocator.form_binding_ischecked)
            self.wait_visibility(FormLocator.form_binding_notchecked)
            self.click(FormLocator.btn_save)
            # print("資料綁定是否 '已關閉'：" + str(self.is_element_finded(FormLocator.form_binding_notchecked)))
        except:
            raise EOFError("後台資料綁定關閉失敗!")

    # 打開資料綁定
    def open_form_binding(self):
        self.sleep(1)
        try:
            if self.is_element_finded(FormLocator.form_binding_notchecked) == True:
                self.click(FormLocator.form_binding_notchecked)
            self.wait_visibility(FormLocator.form_binding_ischecked)
            self.select_binding_question()
            self.click(FormLocator.btn_save)
        except:
            raise EOFError("後台資料綁定打開失敗!")

    # 新增詢前表單問題
    def add_question(self):
        try:
            questions = ['我是問題', '您的身分是', 'user', 'name', '該如何稱呼您', '請簡述問題', '您的暱稱是', '您游戏的账号']
            self.wait_visibility(FormLocator.btn_addquestion)
            ranquestion=random.choice(questions)
            self.click(FormLocator.btn_addquestion)
            self.type(FormLocator.input_question_text, ranquestion)
            self.click(FormLocator.btn_addquestion_confirm)
            self.click(FormLocator.btn_save)
            self.wait_visibility(FormLocator.save_success)
            # print("是否保存成功："+ str(self.is_element_finded(FormLocator.save_success)))
            return ranquestion
        except:
            raise EOFError("新增詢前表單問題失敗 "+ str(self.get_warn_message()))
    

    # 刪除詢前表單所有問題
    def delete_question(self):
        try:
            while self.is_element_finded(FormLocator.btn_deletequestion):
                self.click(FormLocator.btn_deletequestion)
        except:
            raise EOFError("刪除表單問題失敗!")

    # 取得警告訊息
    def get_warn_message(self):
        try:
            warnMessage = self.get_text(FormLocator.warn_message)
            return warnMessage
        except:
            return 

    #驗證詢前表單問題的答案和順序
    def verify_Q_and_A(self, questions, answers):
        adminQandA = self.get_text(FormLocator.q_and_a).split("\n")         #整理後台爬到的問題和答案
        textCheck = [questions[x] + "：" + answers[x] for x in range(len(questions))]           #合併隨機問題和隨機答案
        assert textCheck == adminQandA , f"問題和答案不正確\n正確的:{textCheck}\n爬到的:{adminQandA}"

    # 檢查是否有表單問題，如果沒有就新增
    def check_and_add_question(self):
        if self.is_element_finded(FormLocator.btn_deletequestion) is False:
            self.add_question()

    # 選擇綁定的問題
    def select_binding_question(self):
        self.wait_visibility(FormLocator.input_binding_question)
        self.click(FormLocator.input_binding_question)
        self.wait_visibility(FormLocator.select_binding_question)
        self.click(FormLocator.select_binding_question)
        self.click(FormLocator.btn_save)