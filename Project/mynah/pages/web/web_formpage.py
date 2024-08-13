import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.web.webs_basepage import WebBasePage

class FormLocator:
    question_field = (By.XPATH, "//*[@class='cell-textarea__ct']")      #問題欄位
    question_xpath = "(//*[@class='cell-textarea__ct'])"     #問題欄位(組合用)
    start_talk = (By.XPATH, "//button[@class='van-button van-button--default van-button--normal btn-sign shadows-default__medium']")      #開始諮詢
    name_waitforconnect = (By.XPATH, "//p[@class='name-text' and text()='客服人员连线中']")     # 進入前台左上角客服人員名稱 客服人员连线中
    form_recaptcha = (By.XPATH, "//*[contains(text(),'向右滑')]")   #詢前表單的驗證碼

class WebFormPage(WebBasePage):

    #判斷詢前表單狀態
    def check_form_status(self):
        self.sleep(2)
        if self.is_element_finded(FormLocator.name_waitforconnect) is False:
            assert self.is_element_finded(FormLocator.form_recaptcha) is False, '詢前表單有開啟驗證碼'
            # print('有詢前表單')
            return True
        # else:
        #     print('沒有詢前表單')

    #回答詢前表單的問題
    def answer_question(self):
        answers = []
        try:
            num = len(self.find_elements(FormLocator.question_field))
            for x in range(num):
                answer = self.read_random_words().replace(' ','')
                answers.append(answer)
                fin_xpath=FormLocator.question_xpath + '['+ str(x+1) +']' 
                locators = (By.XPATH, fin_xpath)
                self.type(locators, answer)
            self.click(FormLocator.start_talk)     #點擊開始諮詢
        except:
            raise EOFError("回答詢前表單問題失敗!")
        return answers