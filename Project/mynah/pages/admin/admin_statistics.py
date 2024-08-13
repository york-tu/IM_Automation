import sys
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class StatisticsLocator:
    select_left_site = "//p[@class='op-box-title' and text()='"     #需組合
    btn_search = (By.XPATH, "//i[@class='el-icon-search']/../span")         #查詢鈕
    time_zone_last = (By.XPATH, "//button[@class='el-button el-button--mini'][last()]")         #最後一個時間區塊
    time_zone_active = (By.XPATH, "//button[@class='el-button el-button--primary el-button--mini']/span/div")         #選取的時間區塊
    
    score_items = (By.XPATH, "//th[@colspan='1' and @rowspan='1']/div[not(text()='评分项目')]")         #評分項目
    score_statistics = (By.XPATH, "//td[@colspan='1' and @rowspan='1']/div")         #評分分數
    btn_detail = (By.XPATH, "//span[text()='明细']")         #評分明細按鈕
    btn_opinion = (By.XPATH, "//span[text()='查看意见']")         #查看意見按鈕
    opinion_contain = (By.XPATH, "//div[@class='comment-container']")         #意見內容

class AdminStatisticsPage(AdminBasePage):

    # 客服評分統計_選擇站點，需輸入站點名稱
    def into_statistics_select_site(self, site_id):
        try:
            site_locator = (By.XPATH, self.mix_xpath(StatisticsLocator.select_left_site, site_id))
            self.wait_visibility(site_locator)
            self.click(site_locator)
        except:
            raise EOFError("客服評分統計_選擇站點失敗")
    
    def search_score_statistics(self):
        self.wait_visibility(StatisticsLocator.btn_search)
        self.click(StatisticsLocator.btn_search)
        self.sleep(2)
        if self.is_element_finded(StatisticsLocator.time_zone_last) == True:
            self.click(StatisticsLocator.time_zone_last)
            self.wait_visibility(StatisticsLocator.time_zone_active)
        self.sleep(1)
        items = self.find_elements(StatisticsLocator.score_items)
        statistics_items = [x.text for x in items]
        scores = self.find_elements(StatisticsLocator.score_statistics)
        statistics_scores = [x.text for x in scores]
        self.click(StatisticsLocator.btn_detail)
        self.wait_visibility(StatisticsLocator.btn_opinion)
        self.click(StatisticsLocator.btn_opinion)
        self.wait_visibility(StatisticsLocator.opinion_contain)
        statistics_opinion = self.find_element(StatisticsLocator.opinion_contain).text
        return statistics_items, statistics_scores[2:-1], statistics_opinion

    def compare_items_scores(self, items, scores, opinion, s_items, s_scores, s_opinion):
        assert items == s_items , f"評分項目不一致\n新增的:{items}\n統計的:{s_items}"
        assert scores == s_scores , f"評分分數不一致\n填寫的:{scores}\n統計的:{s_scores}"
        assert opinion == s_opinion , f"評分項目不一致\n填寫的:{opinion}\n統計的:{s_opinion}"
        
