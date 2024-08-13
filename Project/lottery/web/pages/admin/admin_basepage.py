from selenium.webdriver.common.by import By
from copy import deepcopy
import os,platform,getpass,glob,sys,math,zipfile,shutil
import pandas as pd


DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
from common.web.common import Common
import logging

class BasePageLocator:
    # LOADING
    first_page = (By.XPATH, '//a[text()="首页"]')
    last_page = (By.XPATH, '//a[text()="尾页"]')
    record_total = (By.XPATH, '//span[@data-bind="text: pager.total"]')                     # 紀錄總數
    search_loading_mask = (By.XPATH, "//button[@class='btn btn-sm btn-primary']")
    last_page_v2 = (By.XPATH, "//li[contains(@class,'number')][last()]")
    record_total_v2 = (By.XPATH, "//span[@class='el-pagination__total']")                      # 共 * 条
    rows_total_v2 = (By.XPATH, "//table[@class='el-table__body']//tr//*[contains(text(),'总计')]")
    rows_sub_total_v2 = (By.XPATH, "//table[@class='el-table__body']//tr//*[contains(text(),'小计')]")
    rows_both_total_v2 = (By.XPATH,"//span[contains(text(),'小计')]/../span[contains(text(),'总计')]/..")

    # 頁數
    page_size = (By.XPATH,"//*[contains(@data-bind,'pageSize')]//option") # 每頁最多顯示筆數 個別
    page_list = (By.XPATH,"//*[contains(@data-bind,'pageSize')]") # 每頁最多筆數 總下拉式選單
    rows = (By.XPATH,"//tbody[@data-bind='foreach: items']//tr") # 列 

    page_size_v2 = (By.XPATH, "//div[@class='el-select-dropdown el-popper' and not(contains(@style,'display: none'))]//span[contains(text(),'条/页')]")       # 每頁最多筆數 總下拉式選單 ex(50条/页)
    page_size_25_v2 = (By.XPATH, "//span[contains(text(),'25条/页')]")
    rows_v2 = (By.XPATH, "//div[@class='ps-content']/div/div[contains(@class,'is-scrolling-')]/table[@class='el-table__body']/tbody/tr")        # 列(含總計or小計)
    page_change = (By.XPATH, "//span[@class='el-pagination__sizes']")     # 每頁顯示筆數
    page_selected = (By.XPATH, "//li[contains(@class,'el-select-dropdown__item selected')]/span[contains(text(),'条/页')]")    #目前每頁顯示筆數

    
    # 匯出
    export_btn = (By.XPATH, "//button[contains(@data-bind,'export') or @qa-button='export']") # 匯出
    export_disabled_btn = (By.XPATH, "//button[@id='btnExport' and @disabled='true']") # 匯出
    search_btn = (By.XPATH, "//button[@id='btnSearch']")       # 查找按鈕
    export_comfirm_btn = (By.XPATH, "//i[@class='glyphicon glyphicon-ok']")
    export_disabled_btn_v2 = (By.XPATH, "//button[@disabled='disabled' and @qa-button='export']") # 匯出反灰
    time_btn = (By.XPATH, "//button[@qa-button='quick-time-lastWeek']")     # 上週時間按鈕
    search_btn_v2 = (By.XPATH, "//div[@class='query-action']/button[1]")       # 查找按鈕
    export_btn_v2 = (By.XPATH, "//button[@qa-button='export']")
    export_comfirm_btn_v2 = (By.XPATH, "//div[@aria-hidden='false']//p[contains(text(),'确定汇出吗？')]") # 確定匯出二次彈窗

    # total_pages TAB
    @staticmethod
    def multiple_total_pages(index):
        return (By.XPATH, f'(//span[contains(@data-bind,"pager.total")])[{index}]')

    # page_size TAB
    @staticmethod
    def multiple_page_size(index):
        return (By.XPATH, f'(//*[contains(@data-bind,"pageSize")])[{index}]//option')

    # page_list TAB
    @staticmethod
    def multiple_page_list(index):
        return (By.XPATH, f'(//*[contains(@data-bind,"pageSize")])[{index}]')

    # 尾頁 TAB
    @staticmethod
    def multiple_last_pages(index):
        return (By.XPATH, f'(//a[text()="尾页"])[{index}]')

    # Rows Tab
    @staticmethod
    def multiple_rows(index):
        return (By.XPATH, f'(//tbody[@data-bind="foreach: items"])[{index}]/tr[not(@data-bind)]')

    # Online_Deposit Rows Tab
    @staticmethod
    def online_deposit_multiple_rows(index):
        return (By.XPATH, f'(//tbody[@data-bind="foreach: items"])[{index}]/tr[(@data-bind)]')

    # 款项审核 Rows Tab
    @staticmethod
    def artificial_deposit_cancel_multiple_rows(index):
        return (By.XPATH, f'(//tbody[@data-bind="foreach: items"])[{index}]/tr')

class BasePage(Common):

    # # 等待搜尋Loading消失
    # def wait_loading_finish(self):
    #     self.sleep(1)

    #     if self.is_element_finded(BasePageLocator.search_loading_mask) is True:
    #         try:
    #             self.wait_invisibility(BasePageLocator.search_loading_mask)
    #         except:
    #             raise Exception("讀取時間過長,請確認讀取屏蔽視窗")

    # 等待搜尋Loading消失
    def wait_loading_finish(self):
        for loop in range(0, 3):
            if self.is_element_displayed(BasePageLocator.search_loading_mask) is True:
                try:
                    self.wait_invisibility(BasePageLocator.search_loading_mask)
                    return
                except:
                     if loop == 5:
                        raise Exception("讀取時間過長,請確認讀取屏蔽視窗")

            self.sleep(0.5)

    # 檢查頁數
    def check_page(self, tab_page=0, record_per_page=25):
        '''
            檢查頁數顯示是否正確
            參數 : 
                tab_page : 欲選擇的 tab page，輸入0或不輸入則不做選擇tab的動作
                record_per_page : 每頁紀錄數下拉式選單的值
        '''
        common = Common(self.driver, self.sec, self.base_url, self.test_skip_method)
        
        self.wait_loading_finish()
        self.sleep(2)
        
        if not common.is_element_displayed(BasePageLocator.last_page):
            return

        first_page = deepcopy(BasePageLocator.first_page)
        last_page = deepcopy(BasePageLocator.last_page)
        record_total = deepcopy(BasePageLocator.record_total)

        if tab_page != 0:
            first_page = (first_page[0], f'//div[@id="tab_{tab_page}"]{first_page[1]}')
            last_page = (last_page[0], f'//div[@id="tab_{tab_page}"]{last_page[1]}')
            record_total = (record_total[0], f'//div[@id="tab_{tab_page}"]{record_total[1]}')
        
        if self.is_element_displayed(locator=last_page):
            common.click(locator=last_page)
            self.wait_loading_finish()
            total_page = math.ceil(float(common.get_text(locator=record_total)) / record_per_page)       # 取得總頁數
            total_page = (By.XPATH, f'//a[text()="{total_page}"]')
            assert common.is_element_displayed(total_page), '頁數顯示錯誤'

    # 二代報表檢查頁數
    def check_page_v2(self, tab_page=0, record_per_page=25):
        '''
            檢查頁數顯示是否正確
            參數 : 
                tab_page : 欲選擇的 tab page，輸入0或不輸入則不做選擇tab的動作，例如CP上下分流水0，第三方上下分流水1
                record_per_page : 每頁紀錄數下拉式選單的值
        '''

        self.wait_loading_finish()

        last_page = self.find_element(BasePageLocator.last_page_v2)
        record_total = self.find_element(BasePageLocator.record_total_v2)

        if tab_page != 0:
            last_page = self.find_elements(BasePageLocator.last_page_v2)[tab_page]
            record_total = self.find_elements(BasePageLocator.record_total_v2)[tab_page]
        
        if int(self.get_text_by_dom(last_page)) == 1:
            return

        self.click_by_dom(last_page)
        self.wait_loading_finish()
        total_page = math.ceil(float(self.get_text_by_dom(record_total)[2:-2]) / record_per_page)       # 取得總頁數

        assert total_page == int(self.get_text_by_dom(last_page)), f'頁數顯示錯誤{total_page} == {self.get_text_by_dom(last_page)}'

    # 解壓匯出之zip
    def un_zip(self, brand):
        try:
            # 判斷系統

            if platform.system() == 'Windows': 
                user = os.environ['HOMEPATH']
                path = (r'{0}\\Downloads\\{1}\\*.zip'.format(user, brand))
                download_path = (r'{0}\\Downloads\\{1}\\'.format(user, brand))
                self.sleep(3)
                zip_path = glob.glob(path)

            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                path = (r'{0}/Downloads/{1}/*.zip'.format(user, brand))
                download_path = (r'{0}/Downloads/{1}/'.format(user, brand))
                self.sleep(1)
                zip_path = glob.glob(path)

            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                path = (r'{0}/Downloads/{1}/*.zip'.format(user, brand))
                download_path = (r'{0}/Downloads/{1}/'.format(user, brand))
                self.sleep(1)
                zip_path = glob.glob(path)

            # 下載速度不一
            for loop in range(0,10):
                try:
                    files=zipfile.ZipFile(zip_path[0])
                    break
                except:
                    logging.exception('exception log')
                    if loop == 9:
                        raise EOFError('讀取zip錯誤,請確認資料下載完整')
                    
                    self.sleep(1)
            
            names = files.namelist()
            files.extractall(download_path)
            files.close()
            for name in names:
                shutil.move(download_path+name,download_path)

            # 讀完刪掉該檔案
            try:
                for zip in range(0,len(zip_path)):
                    os.remove(zip_path[zip])
            except:
                pass

        except:
            for zip in range(0,len(zip_path)):
                os.remove(zip_path[zip])

            raise BaseException('解析zip錯誤')
    
    # 讀取匯出之excel資料
    def read_excel(self, index_range, brand):
        try:
            # 判斷系統

            if platform.system() == 'Windows': 
                user = os.environ['HOMEPATH']
                path = (r'{0}\\Downloads\\{1}\\*.xlsx'.format(user, brand))
                excel_path = glob.glob(path)

            elif platform.system() == 'Linux':
                user = os.environ['HOME']
                path = (r'{0}/Downloads/{1}/*.xlsx'.format(user, brand))
                excel_path = glob.glob(path)

            elif platform.system() == 'Darwin':
                user = os.environ['HOME']
                path = (r'{0}/Downloads/{1}/*.xlsx'.format(user, brand))
                excel_path = glob.glob(path)

            # 下載速度不一
            for loop in range(0,10):
                try:
                    df = pd.read_excel(excel_path[0])
                    break
                except:
                    logging.exception('exception log')
                    if loop == 9:
                        raise EOFError('讀取excel錯誤,請確認資料下載完整')
                    
                    self.sleep(1)
            
            # 讀完刪掉該檔案
            try:
                for file in range(0,len(excel_path)):
                    os.remove(excel_path[file])
            except:
                pass

            df = df.fillna("") # 填充Nan
            excel_dict = {}

            for col in df.columns.tolist():
                tmp = {col: df.loc[:index_range-1, col].tolist()}
                excel_dict.update(tmp)

            return excel_dict 

        except:
            for file in range(0,len(excel_path)):
                os.remove(excel_path[file])
            
            raise BaseException('解析Excel錯誤')


    # 每頁最大筆數測試
    def max_num(self, tab=1, sort='general_deposit'):
        record_num = self.get_text(BasePageLocator.multiple_total_pages(tab)) # 共x條紀錄
        
        if record_num =='0':
            return
            
        for loop in self.find_elements(BasePageLocator.multiple_page_size(tab)):
            num = self.get_text_by_dom(loop) # 每一頁顯示數量選擇按鈕
            self.select_by_text(BasePageLocator.multiple_page_list(tab), num)
            self.wait_loading_finish()
            last_page_record_num = int(record_num) % int(num)

            if sort == 'online_deposit':
                page_nums = str(len(self.find_elements(BasePageLocator.online_deposit_multiple_rows(tab))))
            elif sort == 'artificial_deposit_cancel':
                page_nums = str(len(self.find_elements(BasePageLocator.artificial_deposit_cancel_multiple_rows(tab))))
            else:
                page_nums = str(len(self.find_elements(BasePageLocator.multiple_rows(tab))))

            if int(record_num) > int(num):
                assert page_nums == num, '每頁最大筆數不正確'
                self.sleep(1)
                self.click(BasePageLocator.multiple_last_pages(tab))
                self.wait_loading_finish()
                
                if sort == 'online_deposit':
                    page_nums = str(len(self.find_elements(BasePageLocator.online_deposit_multiple_rows(tab))))
                elif sort == 'artificial_deposit_cancel':
                    page_nums = str(len(self.find_elements(BasePageLocator.artificial_deposit_cancel_multiple_rows(tab))))
                else:
                    page_nums = str(len(self.find_elements(BasePageLocator.multiple_rows(tab))))

                if last_page_record_num == 0:
                    assert page_nums == str(num), f'page_nums:{page_nums} != num:{num}, 每頁最大筆數不正確'
                else:
                    assert page_nums == str(last_page_record_num), f'page_nums:{page_nums} != last_page_record_num:{last_page_record_num}, 每頁最大筆數不正確'
            else:
                assert page_nums == record_num, f'page_nums:{page_nums} != record_num:{record_num}, 每頁最大筆數不正確'
        
        # 切回25筆
        if int(record_num) >= 26:
            self.select_by_text(BasePageLocator.multiple_page_list(tab), '25')


    # 每頁最大筆數測試 新版
    def max_num_v2(self):
        record_num = (self.get_text(BasePageLocator.record_total_v2))[2:-2]     # 新版 共x條紀錄
        num_list = []
        if record_num =='0':
            return
        # 先抓取每頁顯示數量的所有項目 25、50、100、500
        self.click(BasePageLocator.page_change)
        self.wait_visibility(BasePageLocator.page_size_v2)
        loops = self.find_elements(BasePageLocator.page_size_v2)
        for buf in loops:
            num_list.append(self.get_text_by_dom(buf)[:-3])
        self.click(BasePageLocator.page_change)

        for index, loop in enumerate(loops):    #切換每頁顯示數量
            num = num_list[index]
            self.click(BasePageLocator.page_change)
            self.wait_visibility(BasePageLocator.page_size_v2)
            self.click_by_dom(loop)
            self.wait_loading_finish()
            self.wait_visibility(BasePageLocator.rows_total_v2)
            last_page_record_num = int(record_num) % int(num)       #計算尾頁應有筆數
            page_nums = self.get_row_num()    #算列表筆數

            if int(record_num) > int(num):
                assert page_nums == str(num), f'page_nums:{page_nums} != num:{num}, 非尾頁時，列表顯示筆數與每頁最大筆數不一致'
                self.sleep(1)
                self.click(BasePageLocator.last_page_v2)
                self.wait_loading_finish()
                
                page_nums = self.get_row_num()

                if last_page_record_num == 0:
                    assert page_nums == str(num), f'page_nums:{page_nums} != num:{num}, 每頁最大筆數不正確'
                else:
                    assert page_nums == str(last_page_record_num), f'page_nums:{page_nums} != last_page_record_num:{last_page_record_num}, 尾頁時，列表筆數顯示不正確'
            else:
                assert page_nums == record_num, f'page_nums:{page_nums} != record_num:{record_num}, 僅一頁時，列表顯示筆數與總筆數不一致'
        
        # 切回25筆
        if int(record_num) >= 26:
            self.click(BasePageLocator.page_change)
            self.wait_visibility(BasePageLocator.page_size_25_v2)
            self.click(BasePageLocator.page_size_25_v2)

    # 抓取列表行數，去除總計與小計行數
    def get_row_num(self):
        nums = len(self.find_elements(BasePageLocator.rows_v2))
        if self.is_element_finded(BasePageLocator.rows_both_total_v2):
            nums = nums - 1
        else:
            if self.is_element_finded(BasePageLocator.rows_sub_total_v2):   #若有小計欄位
                nums = nums - 1
            if self.is_element_finded(BasePageLocator.rows_total_v2):   #若有總計欄位
                nums = nums - 1
        return str(nums)

    def check_export_btn(self, page):
        self.wait_loading_finish()
        self.sleep(1)
        # 二代報表頁 需先輸入時間查找過才可以點擊匯出
        if self.is_element_finded(BasePageLocator.export_btn_v2) is True:
            if self.is_element_finded(BasePageLocator.export_disabled_btn_v2) is True:
                self.click(BasePageLocator.time_btn)
                self.click(BasePageLocator.search_btn_v2)
                self.sleep(1.5)
            self.wait_visibility(BasePageLocator.export_btn)
            self.click(BasePageLocator.export_btn)
            if self.wait_visibility_status(BasePageLocator.export_comfirm_btn_v2) is False:
                return f'{page} 頁點擊匯出按鈕錯誤, 沒有出現確定 or 取消視窗'
            
        elif self.is_element_finded(BasePageLocator.export_btn) is True:
            if self.is_element_finded(BasePageLocator.export_disabled_btn) is True:
                self.click(BasePageLocator.search_btn)
                self.sleep(1.5)
            self.click(BasePageLocator.export_btn)
            if self.is_element_finded(BasePageLocator.export_comfirm_btn) is False:
                return f'{page} 頁點擊匯出按鈕錯誤, 沒有出現確定 or 取消視窗'
        else:
            return f'{page} 頁點擊匯出按鈕錯誤, 沒有出現匯出視窗'