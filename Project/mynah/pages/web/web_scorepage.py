import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.web.webs_basepage import WebBasePage

class ScoreLocator:
    score = (By.XPATH, "//p[text()='客服评价']")    #客服評價
    score_close = (By.XPATH, "//a[@class='header-close header-close__end']")  #客服評價叉叉
    score_q = (By.XPATH, "//div[@class='rating-star']")   #評價項目   //div[@class='rating-star']/div[X] 給X顆星星
    btn_score = (By.XPATH, "//span[@class='van-button__text' and contains(text(),'提交评价')]/../..")    #提交評價按鈕
    btn_score_confirm = (By.XPATH, "//button[@class='van-button van-button--default van-button--large van-dialog__confirm']")       #確認提交成功
    opinion_field = (By.XPATH, "//textarea[@class='feedback__textarea']")       #意見欄


class WebScorePage(WebBasePage):

    #確認客評價是否開啟
    def web_check_score_status(self):
        try:
            self.wait_visibility(ScoreLocator.score)
            # print('有客服評價')
            return True
        except:
            # print('沒客服評價')
            return False

    #前台回答評分項目
    def web_answer_score(self):
        if self.web_check_score_status()==True:
            if self.is_element_finded(ScoreLocator.score_close) == True:
                self.click(ScoreLocator.score_close)
            else:
                try:
                    Scores = self.find_elements(ScoreLocator.score_q)
                    for i in range(len(Scores)):
                        STAR=(By.XPATH, "(//div[@class='rating-star']/div[" + random.choice(['1','2','3','4','5']) + "])[" + str(i+1) + "]")
                        # print(STAR)
                        self.click(STAR)
                    self.click(ScoreLocator.btn_score)
                    self.wait_visibility(ScoreLocator.btn_score_confirm)
                    self.click(ScoreLocator.btn_score_confirm)
                except:
                    raise EOFError("填客服評價失敗") 

    #前台回答評分項目並記錄
    def web_score_record(self):
        assert self.web_check_score_status()==True, '沒客服評價'
        try:
            Scores = self.find_elements(ScoreLocator.score_q)
            scores = []
            for i in range(len(Scores)):
                score = random.choice(['1','2','3','4','5'])
                scores.append(score)
                STAR=(By.XPATH, f"(//div[@class='rating-star']/div[{score}])[{str(i+1)}]")
                self.click(STAR)
            opinion = self.read_random_words().replace(' ','')
            self.type(ScoreLocator.opinion_field, opinion)
            self.click(ScoreLocator.btn_score)
            self.wait_visibility(ScoreLocator.btn_score_confirm)
            self.click(ScoreLocator.btn_score_confirm)
        except:
            raise EOFError("填客服評價失敗") 
        return scores, opinion