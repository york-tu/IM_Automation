import sys
import os
import random
from selenium.webdriver.common.by import By
from common.web.common import Common

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class WebBasePage(Common):
    
    #組合Xpath
    def mix_xpath(self,locator,text):
        return str(locator+text+"']")

    # 開新分頁 關原分頁
    def close_and_change_window(self):
        # js = "window.open('"+ BasePageLocator.URL_MYNAH_UAT +"');"
        self.execute_js("window.open()")
        self.close_browser()              #關掉原本的分頁
        self.switch_last_page() #轉換為新的分頁

    def random_read_file(self): 
        files_name_list=['Message1.txt','Message2.txt','Message3.txt','Message5.txt',
            'Message6.txt','Message7.txt','Message8.txt','Message9.txt']
        ranFile='./Project/mynah/pages/files/' + random.choice(files_name_list)
        file_object = open(ranFile,'r',encoding="utf-8")
        # file_object = open('./Project/mynah/pages/files/Message1.txt','r',encoding="utf-8")
        try:
            file_context = file_object.read().replace('\n', ' ')
        finally:
            file_object.close()
        return file_context

    def read_random_words(self):
        file_object = open(root_path + '/pages/files/Message10.txt', 'r', encoding="utf-8")
        try:
            file_context = file_object.read().replace('\n', ' ')
            file_words = ''.join(random.sample(file_context, random.randint(4,12)))
        finally:
            file_object.close()
        return file_words


