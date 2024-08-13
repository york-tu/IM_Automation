from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime,pytz

class GenernalPageLocator:
    # 查找
    btn_search = (By.XPATH, "//button/span[contains(text(), '查找')]") # 查找按鈕
    button_expand = (By.XPATH, '//i[@class="el-icon-arrow-down"]')      # 查找區展開鈕
    btn_Today = (By.XPATH,"//button/span[contains(text(),'今日')]")
    footer_page = (By.XPATH,"(//input[@class='el-input__inner'])[last()]")   # 頁腳
    
    # 資料排序
    btn_amount = (By.XPATH,"//label[text()='资料排序']/..//div//label[1]") # 單量按鈕
    btn_bet_amount = (By.XPATH,"//label[text()='资料排序']/..//div//label[2]") # 投注額按鈕
    btn_result = (By.XPATH,"//label[text()='资料排序']/..//div//label[3]") # 損益按鈕
    btn_effective_bet = (By.XPATH,"//label[text()='资料排序']/..//div//label[4]") # 有效投注按鈕


      # 體系報表
    def sort(self,Web_account):
        total_list = (By.XPATH,"//div[@class='report-item__title']/span[text()='总计']")
        amount_info = (By.XPATH,"(//div[contains(text(),'%s')])[1]/../../../../td[2]"%Web_account) # 單量
        bet_amount = (By.XPATH,"(//div[contains(text(),'%s')])[1]/../../../../td[3]"%Web_account) # 投注額
        result = (By.XPATH,"(//div[contains(text(),'%s')])[1]/../../../../td[4]"%Web_account) # 損益
        effective_bet = (By.XPATH,"(//div[contains(text(),'%s')])[1]/../../../../td[5]"%Web_account) # 有效投注

        info={'total_list':total_list,'amount_info':amount_info,'bet_amount':bet_amount,'result':result,'effective_bet':effective_bet}
        return info

    total_quantity = (By.XPATH,"//th[contains(@class,'is-leaf cell-warn')]/div") # 總下注數量
    final_quantity = (By.XPATH,"(//th[contains(@class,'is-leaf cell-warn')]/div)[last()]") # 最後一筆下注數量
    game_name = (By.XPATH,"//div[@class='report-item__title']/span") # 個別遊戲名稱
    
    # 圖形報表
    graphical_report = (By.XPATH,"//button[@qa-button='openPieChartDialog']/span[text()='图形报表']") # 圖形報表
    graphical_title_first = (By.XPATH,"//div[@class='chart-content__title']//span[contains(text(), '单量')]") # 報表第一標題
    graphical_title_second = (By.XPATH,"(//div[@class='chart-content__title']//span[contains(text(), '单量')])[2]") # 報表第二標題
    total_graphical_shareholder_amount = (By.XPATH,"(//div[@class='amChartsLegend']//*[@text-anchor='end'])[1]") # 股東單量數量
    total_graphical_channel_name = (By.XPATH,"//div[contains(@data-bind,'visibleChannel')]//div[@class='amChartsLegend']//*[@text-anchor='start']") # 頻道名稱
    total_graphical_channel_amount = (By.XPATH,"//div[contains(@data-bind,'visibleChannel')]//div[@class='amChartsLegend']//*[@text-anchor='end']") # 頻道數量
    close_windows_pie = (By.XPATH,"(//span[text()='关闭'])[1]") # 圓餅圖視窗關閉
    close_windows_bar = (By.XPATH,"(//span[text()='关闭'])[last()]") # 長條圖視窗關閉
    
    # 趨勢報表
    trend_report = (By.XPATH,"(//button[@qa-button='openTrendChartDialog'])[1]") # 趨勢報表
    bar_graph = (By.XPATH,"(//div[@class='chart-content__title']/span)[1]") # 長條圖
    line_chart = (By.XPATH,"(//div[@class='chart-content__title']/span)[2]") # 折線圖

    # 會員圖形報表
    graphical_report_account = (By.XPATH,"(//div[@qa-button='jumpToOrderPage']/..//button/span[text()='图形报表'])[1]") # 個別帳號 圖形報表
    total_amount_account = (By.XPATH,"//div[contains(@data-bind,'visibleChannel')]//div[@class='amChartsLegend']//*[@text-anchor='end']") # 圖形報表數量
    
    # 會員趨勢報表
    trend_report_account = (By.XPATH,"(//div[@qa-button='jumpToOrderPage']/..//button/span[text()='趋势图表'])[1]") # 個別帳號 趨勢報表
    

class GenernalPage(BasePage):
        
    # 體系報表
    def structure_report(self,sum,Web_account):
        assert self.wait_visibility_status(GenernalPageLocator.btn_search) is True,'進入一般報表錯誤'
        self.click(GenernalPageLocator.btn_Today) 

        sort=[GenernalPageLocator.btn_amount,GenernalPageLocator.btn_bet_amount,GenernalPageLocator.btn_result,GenernalPageLocator.btn_effective_bet]
        info=GenernalPageLocator.sort(self,Web_account)
        
        # 抓取指定會員資訊,並依據不同排列進行查找比對
        for loop in sort:
            assert self.is_element_finded(GenernalPageLocator.button_expand) == False, "查找條件預設不應收合"
            self.click(loop)
            self.click(GenernalPageLocator.btn_search)
            self.wait_loading_finish()
            self.sleep(3)

            assert self.is_element_finded(info['total_list']) is True,'查無資料,請與admin後台進行確認'
            assert self.get_text(info['amount_info']) == str(sum['Total']),'單量不符'
            assert self.get_text(info['bet_amount']) == str(sum['Amount']),'投注額不符'
            assert self.get_text(info['result']) == str(sum['Income']),'損益不符'
            assert self.get_text(info['effective_bet']) == str(sum['Point']),'有效投注不符'
    
    # 體系報表(代理外)
    def unstructure_report(self,Web_account):
        self.wait_loading_finish()
        assert self.is_element_finded(GenernalPageLocator.btn_search) is True,'進入一般報表錯誤'

        self.click(GenernalPageLocator.btn_Today)
        self.click(GenernalPageLocator.btn_search)
        self.wait_loading_finish()
        self.sleep(3)

        page_user_find = (By.XPATH,"//*[contains(text(),'%s')]"%Web_account)
        assert self.is_element_finded(page_user_find) is False,'錯誤,會員已轉出此代理,資料依然存在. 會員帳號:%s'%Web_account

    # 總圖形報表
    def graphical_report(self,Web_account):
        info=GenernalPageLocator.sort(self,Web_account)
        assert self.is_element_finded(GenernalPageLocator.button_expand) == False, "查找條件預設不應收合"
        self.click(GenernalPageLocator.btn_amount)
        self.click(GenernalPageLocator.btn_search)
        self.wait_loading_finish()

        gamelist=self.get_game_name_amount() # 抓取一般報表首頁遊戲名稱數量

        self.click(GenernalPageLocator.graphical_report)
        self.wait_visibility(GenernalPageLocator.graphical_title_first)
        self.sleep(1)

        # graphical_game_list=self.get_graphical_game_amount() # 抓取圖形報表首頁遊戲名稱數量  (改版後已無法抓取圖表內容資料)

        assert self.get_text(GenernalPageLocator.graphical_title_first) == '单量','圖形報表未出現 單量'
        assert str(self.get_text(GenernalPageLocator.graphical_title_second)).__contains__('频道'),'圖形報表未出現 頻道單量'
        # assert self.get_text(GenernalPageLocator.total_graphical_shareholder_amount) == self.get_text(info['amount_info']),'%s 單量不正確'%Web_account  (改版後已無法抓取圖表內容資料)
        # assert (set(gamelist) == set(graphical_game_list)) == True,'一般報表遊戲名稱及遊玩數量與圖形報表不相符'

        self.click(GenernalPageLocator.close_windows_pie)
        self.wait_invisibility(GenernalPageLocator.close_windows_pie)
    
    # 總趨勢報表
    def trend_report(self):
        self.click(GenernalPageLocator.trend_report)
        self.wait_visibility(GenernalPageLocator.bar_graph)

        assert str(self.get_text(GenernalPageLocator.bar_graph)).__contains__('长条图'),'趨勢報表未出現 長條圖'
        assert str(self.get_text(GenernalPageLocator.line_chart)).__contains__('折线图'),'趨勢報表未出現 折線圖'
        
        self.click(GenernalPageLocator.close_windows_bar)
        self.wait_invisibility(GenernalPageLocator.close_windows_bar)

    # 會員圖形報表
    def graphical_report_account(self,Web_account):
        sum=0
        info=GenernalPageLocator.sort(self,Web_account)

        self.click(GenernalPageLocator.graphical_report_account)
        self.wait_visibility(GenernalPageLocator.graphical_title_first)

        # for loop in self.find_elements(GenernalPageLocator.total_amount_account):
        #     sum=sum+int(loop.text)
        
        assert str(self.get_text(GenernalPageLocator.graphical_title_first)).__contains__('频道'),'圖形報表未出現 頻道單量'
        # assert str(sum) == self.get_text(info['amount_info']),'圖形報表單量不符'      (改版後已無法抓取圖表內容資料)

        self.click(GenernalPageLocator.close_windows_pie)
        self.wait_invisibility(GenernalPageLocator.close_windows_pie)

    # 會員趨勢報表
    def trend_report_account(self):
        self.click(GenernalPageLocator.trend_report_account)
        self.wait_visibility(GenernalPageLocator.bar_graph)

        assert str(self.get_text(GenernalPageLocator.bar_graph)).__contains__('长条图'),'趨勢報表未出現 長條圖'
        assert str(self.get_text(GenernalPageLocator.line_chart)).__contains__('折线图'),'趨勢報表未出現 折線圖'
        
        self.click(GenernalPageLocator.close_windows_bar)
        self.wait_invisibility(GenernalPageLocator.close_windows_bar)
            
    def get_game_name_amount(self):
        total=0
        amount_list=[]
        game_name_list=[]
        game_sum_list=[]
        
        # 抓取各玩法總數 
        self.type_page_down(GenernalPageLocator.footer_page)
        self.sleep(0.5)
        num=0
        for loop in self.find_elements(GenernalPageLocator.total_quantity):
            num+=1
            if num == 1 :
                total=int(loop.text)
            else:
                total=total-int(loop.text)
                amount_list.append(loop.text)
        
        # 抓取各玩法名稱
        num=0
        for loop in self.find_elements(GenernalPageLocator.game_name):
            num+=1
            if num == 1 :
                pass
            else:
                game_name_list.append(loop.text)
        
        # 遊戲與單量合併
        game_sum_list = list(map(lambda x, y: x + y, game_name_list,amount_list))
        
        assert total == 0,'總數量與個別數玩法數量不相符'
        return game_sum_list
    
    # 抓取圖形報表 -> 頻道 比對
    def get_graphical_game_amount(self):
        amount_list=[]
        game_name_list=[]
        game_sum_list=[]

        # 抓取各玩法總數
        for loop in self.find_elements(GenernalPageLocator.total_graphical_channel_amount):
            amount_list.append(loop.text)
            
        # 抓取各玩法名稱
        for loop in self.find_elements(GenernalPageLocator.total_graphical_channel_name):
            game_name_list.append(loop.text)
        
        # 遊戲與單量合併
        game_sum_list = list(map(lambda x, y: x + y, game_name_list,amount_list))
        
        return game_sum_list
    


