from selenium.webdriver.common.by import By
from pages.cmweb.cmweb_basepage import BasePage

class GameListPageLocator:
    search_icon = (By.XPATH,"//span[text()='查找']") # 查找圖示
    game_field = (By.XPATH,"//input[@placeholder= '输入游戏名称']") # 遊戲名稱欄位
    class_field = (By.XPATH,"//div[@placeholder= '游戏分类']//input") # 遊戲分類選單
    class_field_click = (By.XPATH,"//li[@class= 'el-select-dropdown__item hover']") # 點擊該分類
    btn_search = (By.XPATH,"//span[text()='确 定']") # 查找按鈕
    channel_code = (By.XPATH,"//td[@class= 'el-table_1_column_2 is-center  el-table__cell']//div") # 平台代碼
    game_name = (By.XPATH,"//td[@class= 'el-table_1_column_4 is-center  el-table__cell']//div") # 遊戲名稱
    game_id = (By.XPATH,"//td[@class= 'el-table_1_column_5 is-center  el-table__cell']//div") # 遊戲id
    game_class = (By.XPATH,"//td[@class= 'el-table_1_column_3 is-center  el-table__cell']//div") # 遊戲分類
    game_display = (By.XPATH,"//td[@class= 'el-table_1_column_6 is-center  el-table__cell']//div") # 顯示
    game_delete = (By.XPATH,"//td[@class= 'el-table_1_column_7 is-center  el-table__cell']//div") # 刪除


class GameListPage(BasePage):
    # 頻道名轉換 
    def third_channel_rename(self, third_channel):
        if len(third_channel) > 2:
            third_channel = third_channel[0:2]
        elif third_channel == 'AG':
            third_channel = ['YOPLAY', 'XIN', 'AGIN', 'HUNTER']
        elif third_channel == 'MG':
            third_channel = ['Maverick', 'MG']
        elif third_channel == 'KX':
            third_channel = 'LC'
        elif third_channel == '3S':
             third_channel = 'SS' 
        return third_channel
    
    # 檢查遊戲下架
    def remove_game_check(self, third_channel, game_type, game_code, game_list, web_name_list, admin_name_list):     
        game_type = game_type + '游戏'
        cm_name_list = []
        for num, name in enumerate(game_list):
            self.click(GameListPageLocator.search_icon)
            self.wait_visibility(GameListPageLocator.game_field)
            self.type(GameListPageLocator.game_field, name)
            self.click(GameListPageLocator.btn_search)

            self.wait_loading_finish()
            if self.is_element_finded(GameListPageLocator.game_display) == True:
                games_name = self.find_elements(GameListPageLocator.game_name)
                games_channel = self.find_elements(GameListPageLocator.channel_code)
                game_id = self.find_elements(GameListPageLocator.game_id)
                games_display = self.find_elements(GameListPageLocator.game_display)
                games_delete = self.find_elements(GameListPageLocator.game_delete)

                for index, display in enumerate(games_display):
                    if display.text != '否' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                        if game_code[num] == game_id[index].text:
                            cm_name_list.append(name)

                for index, delete in enumerate(games_delete):
                    if delete.text != '是' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                        if game_code[num] == game_id[index].text:
                            cm_name_list.append(name)
                        else:
                            if name not in cm_name_list and name in web_name_list and name in admin_name_list:
                                web_name_list.remove(name)
                                admin_name_list.remove(name)
                
        return web_name_list, admin_name_list, list(set(cm_name_list))

    # 檢查遊戲上架
    def add_game_check(self, third_channel, game_type, game_code, game_list, web_name_list, admin_name_list):
        game_type = game_type + '游戏'
        cm_name_list = []
        correct_name_list = []
        for num, name in enumerate(game_list):
            self.click(GameListPageLocator.search_icon)
            self.wait_visibility(GameListPageLocator.game_field)
            self.type(GameListPageLocator.game_field, name)
            self.click(GameListPageLocator.btn_search)
            self.wait_loading_finish()

            if self.is_element_finded(GameListPageLocator.game_display) == True:
                games_name = self.find_elements(GameListPageLocator.game_name)
                games_channel = self.find_elements(GameListPageLocator.channel_code)
                game_id = self.find_elements(GameListPageLocator.game_id)
                games_display = self.find_elements(GameListPageLocator.game_display)
                games_delete = self.find_elements(GameListPageLocator.game_delete)

                for index, display in enumerate(games_display):
                    if display.text != '是' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                        if game_code[num] == game_id[index].text:
                            cm_name_list.append(name)
                    elif display.text == '是' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                        if game_code[num] == game_id[index].text:
                            correct_name_list.append(name)
                            
                for index, delete in enumerate(games_delete):
                    if delete.text != '否' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                        if game_code[num] == game_id[index].text:
                            cm_name_list.append(name)
                        elif display.text == '是' and games_channel[index].text in third_channel and len(name) == len(games_name[index].text):
                            if game_code[num] == game_id[index].text:
                                if name in correct_name_list and name in web_name_list and name in admin_name_list:
                                    web_name_list.remove(name)
                                    admin_name_list.remove(name)

            elif self.is_element_finded(GameListPageLocator.game_display) == False:
                print("{0}{1}_{2}, 查詢後沒有正確顯示於CMWEB遊戲列表_Table".format(third_channel[1], game_type, name))
                
        return web_name_list, admin_name_list, list(set(cm_name_list))
                    
                
            


        

