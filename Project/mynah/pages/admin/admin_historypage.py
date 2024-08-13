import sys
import os
import random
from selenium.webdriver.common.by import By
from Project.mynah.pages.admin.admin_basepage import AdminBasePage

class HistoryLocator:
    select_left_site = "//p[@class='op-box-title' and text()='"     #需組合
    table_guest_id = "//div[@class='cell' and text()='"             #需組合
    view_btn = "//div[@class='cell']/span[text()='"                 #需組合
    history_dialog = (By.XPATH,"//span[@class='el-dialog__title' and text()='接待对话']")  #確認接待對話浮框
    message_row = (By.XPATH,"//div[@class='chat-pool__row']/div")      #每個訊息包括事件
    click_search = (By.XPATH, "//span[text()='查询']") # "//button[@class='el-button el-button--primary el-button--small']"  #"//span[text()='查询']" 
    loading_finish = (By.XPATH,"//div[@class='ps-container']")
class AdminHistoryPage(AdminBasePage):

    # 接待信息_選擇站點，需輸入站點名稱
    def into_left_select_site(self, site_id):       #//p[@class='op-box-title' and text()='站點2_組2']   #//div[@class='cell' and text()='站點 c7 / lv (A&B)']
        try:        
            site_locator = (By.XPATH, self.mix_xpath(HistoryLocator.select_left_site, site_id))
            site_check_locator = (By.XPATH, self.mix_xpath(HistoryLocator.table_guest_id, site_id))
            self.wait_visibility(site_locator)
            self.click(site_locator)
            self.wait_visibility(site_check_locator)
            self.sleep(1)
        except:
            raise EOFError("接待信息_選擇站點失敗")
    
    # 點擊查詢按鈕
    def click_search(self):
        self.click(HistoryLocator.click_search)
        self.wait_visibility(HistoryLocator.loading_finish)
        


    # 選擇指定群組查看          #//div[@class='cell']/span[text()='Guest#Pt49u']/../../..//button
    def select_group_history(self, guest):
        view_locator = (By.XPATH, str(HistoryLocator.view_btn + guest +"']/../../..//button"))
        self.click(view_locator)
        self.wait_visibility(HistoryLocator.history_dialog)     # 確認接待對話浮框顯示



    # 爬下所有訊息內容 不含事件
    def get_history_data(self):
        history_all_data = self.find_elements(HistoryLocator.message_row)   
        history_list = []   #含 mes_dict 字典
        for data in history_all_data:
            data_list = data.text.split('\n', 2)    # 陣列 分為名稱 時間 訊息
            mes_dict = {}
            mes_dict['name'] = data_list[0]
            mes_dict['time'] = data_list[1]
            mes_dict['text'] = data_list[2]
            history_list.append(mes_dict)
        return history_list

    # 比對 對話訊息 與 接待信息 的 訊息內容(不含事件)
    def check_message_and_history(self, mes_list, history_list):
        for i in range(len(mes_list)):
            assert mes_list[i]['name'] == history_list[i]['name'] ,f"名稱不一致：後台會話框名稱{mes_list[i]['name']} 與 接待信息名稱{history_list[i]['name']} 不一致"
            assert mes_list[i]['time'] == history_list[i]['time'] ,f"時間不一致：後台會話框時間{mes_list[i]['time']} 與 接待信息時間{history_list[i]['time']} 不一致"
            assert mes_list[i]['text'] == history_list[i]['text'] ,f"訊息內容不一致：後台會話框訊息內容{mes_list[i]['text']} 與 接待信息訊息內容{history_list[i]['text']} 不一致"