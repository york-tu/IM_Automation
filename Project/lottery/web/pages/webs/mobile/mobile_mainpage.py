from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import os,random, re
from opencc import OpenCC
import pandas as pd
from bs4 import BeautifulSoup

class MainPageLocator:

    # APP DOWNLOAD PAGE
    visit = (By.XPATH, "//*[text()='继续访问' or contains(@class, 'visit')]")
    visit_hb = (By.XPATH, "//div[@data-context= 'm-appDownload']//*[contains(@class, 'start')]")
    downloader_bar_close = (By.XPATH, '//div[@class="downloadbar__close"]/*')
    downloader_bar_display = (By.XPATH, '//div[@class="downloadbar" and contains(@style,  "none")]')

    # MAIN PAGE
    close_homecontenwindow_btn = (By.XPATH, "//div[@class='addhome_content']/i")
    link_login_page = (By.XPATH, "//div[@class='user-info']//*[contains(text(), '登入') or text()='登录']")
    link_register_page = (By.XPATH, "//a[contains(text(), '注册')]")
    link_nwap_register = (By.XPATH, "//*[contains(text(), '注册新用户')]")
    link_lottery_page1 = (By.XPATH, "//span[text()='彩票大厅']")
    link_first_lottery_page = (By.XPATH, "//*[contains(@alt,'极速快3')]")
    link_chatroom_page = (By.XPATH, "//a[@href='/m/stock/chatroom']")
    link_old_page = (By.XPATH, "//p[text()='返回怀旧版本']")

    # 登入頁
    m_login_btn_nwap = (By.XPATH, "//a[contains(text(),'会员登录')]")

    # 登入公告訊息檢查
    login_announcement = (By.XPATH, "//div[contains(@data-bind, 'loginBillboard') or @class='bulletin__content']/p[1]")
    # 關閉登入公告
    close_announcement = (By.XPATH, "//*[@class='bulletin-close__img' or @class='btn-billboard' and text()[contains(., '我知道了')]]")

    def into_lottery(self, random_list):
        link_lottery_page = (By.XPATH, "(//div[@class='index_lettory' or @class='index_lettory_new1']//a/..)[%d]" %random_list)
        return link_lottery_page
    
    # 前往舊版彩票
    old_lottery_entrance = (By.XPATH, "//a[@class='recommend-title__rt back-change']//span[@class='back-change__text']")

    # 維護監測
    maintenance = (By.XPATH, "//*[contains(@alt,'维护中')]")

class MainPage(BasePage):
    error_list = {}

    # 跳過APP下載頁
    def skip_app_download(self):
        self.wait_loading_finish()
        
        if self.is_element_finded(MainPageLocator.visit):
            self.click(MainPageLocator.visit)  # 繼續訪問
        elif self.is_element_finded(MainPageLocator.visit_hb):
            self.click(MainPageLocator.visit_hb)  # 紅包繼續訪問
        
        if self.is_element_finded(MainPageLocator.downloader_bar_display) is False and self.is_element_finded(MainPageLocator.downloader_bar_close) is True:
            try:
                self.click(MainPageLocator.downloader_bar_close)
            except:
                pass

    # 登入頁
    def into_login_page(self):
        self.wait_loading_finish()
        if self.is_element_finded(MainPageLocator.link_login_page) is True:
            self.click(MainPageLocator.link_login_page)
            assert self.wait_visibility_status(MainPageLocator.m_login_btn_nwap), f'未導轉至登入頁'

    # 註冊頁
    def into_register_page(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.link_register_page)
        self.wait_loading_finish()
    
    #NWAP註冊頁
    def into_nwap_register_page(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.link_nwap_register)
        self.wait_loading_finish()

    # 前往AA聊天室
    def into_chatroom_page(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.link_chatroom_page)
        self.wait_loading_finish()

    # 彩票頁-舊版
    def into_lottery_page(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.into_lottery(self,random.randint(1,3)))
        self.maintenance()

    # 前往舊版彩票
    def into_old_lottery_page(self):
        self.wait_loading_finish()
        assert (self.is_element_finded(MainPageLocator.old_lottery_entrance) == True), "前往舊版彩票BTN_錯誤"
        self.click(MainPageLocator.old_lottery_entrance)

    # 前往舊版頁面
    def into_old_page(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.link_old_page)
        self.wait_loading_finish()

    # 手機瀏覽器關閉捷徑添加鈕
    def close_add_home_content_window(self):
        self.wait_loading_finish()
        self.click(MainPageLocator.close_homecontenwindow_btn)

    # 登出確認器
    def logout_checker(self):
        self.wait_loading_finish()
        assert self.is_element_displayed(MainPageLocator.link_login_page) is True

    # 進入彩票-新版
    def into_menu_lottery(self):
        self.wait_loading_finish()

        if self.is_element_finded(MainPageLocator.link_lottery_page1) is True:
            self.click(MainPageLocator.link_lottery_page1)
            self.wait_loading_finish()

    # 系統維護
    def maintenance(self, is_maintenance = False):
        self.wait_loading_finish()
        
        if is_maintenance == True:
            assert self.is_element_finded(MainPageLocator.maintenance) is True, '關閉網站節點錯誤'
            return

        if self.is_element_finded(MainPageLocator.maintenance) is True:
            print("系統維護中")
            self.test_skip('系統維護中')

    def check_login_board(self, data):
        self.wait_loading_finish()

        for loop in range(0, 3):
            if self.is_element_finded(MainPageLocator.login_announcement) is True:
                message = self.get_text(MainPageLocator.login_announcement)
                
                while True:
                    if self.is_element_displayed(MainPageLocator.login_announcement) is True:
                        self.click(MainPageLocator.close_announcement)
                        self.sleep(0.5)
                    else:
                        break

                assert message == data['content'], f"登入公告訊息異常 目前顯示: {message} 正確顯示: {data['content']}"
                return
            else:
                self.sleep(2)
                
                if loop == 2:
                    raise EOFError('找不到登入公告訊息')
    
    def language(self, url):
        complete_link = []

        link_list = self.link_list('a', 'href') # 帶入xpath位置
        source = self.get_page_source()
        re_words = re.findall(u"[\u4e00-\u9fa5]+", source) # 抓出中文字
        self.check_font(re_words, url)

        # 第一層href抓取判斷
        for link in link_list:
            if link.__contains__('ttp'):
                # complete = link
                # self.open_browser(complete)
                continue
            else:
                if link[0] == 'm':
                    complete = url + link[1:]
                else:
                    complete = url + link

                self.open_browser(complete)
                try:
                    self.wait_loading_finish()
                except:
                    pass
            
            # 第二層href抓取判斷
            second_link_list = self.link_list('a', 'href')
            source = self.get_page_source()
            re_words = re.findall(u"[\u4e00-\u9fa5]+", source)
            self.check_font(re_words, complete)

            if len(second_link_list) != 0:
                for second_link in second_link_list:
                    if second_link in complete_link:
                        continue
                    else:
                        complete_link.append(second_link)

                    if second_link.__contains__('ttp'):
                        # self.open_browser(second_link)
                        # complete = second_link
                        continue
                    else:
                        if second_link[0] == 'm':
                            complete = url + second_link[1:]
                        else:
                            complete = url + second_link

                        self.open_browser(complete)
                        try:
                            self.wait_loading_finish()
                        except:
                            pass

                    source = self.get_page_source()
                    re_words = re.findall(u"[\u4e00-\u9fa5]+", source)
                    self.check_font(re_words, complete)


        if len(self.error_list) != 0:
            # 顯示完整資訊
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max_colwidth', -1)
            result = pd.Series(self.error_list, index = self.error_list.keys())
            raise EOFError(f'內容包含繁體字\n {result}')
    
    # 分層爬出網址 xpath_a/b分別是定位
    def link_list(self, xpath_a, xpath_b):
        link_list = []

        source = self.get_page_source()
        soup = BeautifulSoup(source, 'html.parser')
        link = soup.findAll(xpath_a)

        for i in link:
            name = i.get(xpath_b)
            if str(name).__contains__('/') and len(name) > 1 and not str(name).__contains__('logout'):
                try:
                    name = name.split("'")[1]
                except:
                    pass
                link_list.append(name[1:])

        link_list = list(set(link_list))

        return link_list

    # 簡體比對
    def check_font(self, original_string, url):
        message = []
      
        for word in original_string:
            simplified = self.font('t2s', word)
            if simplified != word and word != '三昇体育' and word != '機器人':
                message.append(word)

        if len(message) != 0 :
            self.error_list[url] = message
