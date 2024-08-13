from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class OddsManagementPageLocator(BasePage):

    # 盤口列表
    def button_odds(self, index):
        return (By.XPATH, f'(//a[contains(text(), "赔率")])[{index}]') # 賠率
    
    def button_modify(self, index):
        return (By.XPATH, f'(//a[contains(text(), "修改")])[{index}]')     # 修改
    
    def button_delete(self, index):
        return (By.XPATH, f'(//a[contains(text(), "删除")])[{index}]') # 刪除
    
    button_confirm = (By.LINK_TEXT, "确定")  # 確定
    button_bancel = (By.LINK_TEXT, "取消")   # 取消

    row_count = (By.XPATH, '//tr[contains(@data-bind, "0")]')         # 指定盤口行數
    page_count = (By.XPATH, '//span[@data-bind="text: pager.total"]') # 總頁數

    # 帳號內容 - 新增 
    button_add = (By.CSS_SELECTOR, "a.btn.btn-default.btn-sm > i.fa.fa-plus") # 新增

    odds_code = (By.XPATH, "//input[@data-bind = 'value:code']")                    # 盤口代碼
    odds_name = (By.XPATH, "//input[@data-bind = 'value:name']")                    # 盤口名稱 
    state_enable = (By.XPATH, "//label[contains(., '已启用')]")                     # 已啟用
    state_disable = (By.XPATH, "//label[contains(., '已禁用')]")                    # 已禁用
    check_enable = (By.XPATH, "//label[contains(., '已启用')]/input[@checked='checked']")     
    check_disable = (By.XPATH, "//label[contains(., '已禁用')]/input[@checked='checked']")              
    min_amount = (By.XPATH, "//input[@data-bind = 'value:minamount']")                  # 最小限額
    max_amount = (By.XPATH, "//input[@data-bind = 'value:maxamount']")                  # 最大限額
    max_win = (By.XPATH, "//input[@data-bind = 'value:maxwin']")                        # 可贏限額
    sort = (By.XPATH, "//input[@data-bind = 'value:sort']")                             # 排序
    odds_rate = (By.XPATH, '//input[contains(@data-bind, "value: rate")]')              # 賠率

    button_save = (By.XPATH, '//button[contains(text(), "保存")]')  # 保存
    button_back = (By.XPATH, '//button[contains(text(), "返回")]')  # 返回

    loading = (By.XPATH, "//span[contains(text(),'Loading')]")
    last_game = (By.XPATH, "//div[text()='中一-十中一']") # 極速六合彩的最後一個玩法
class OddsManagementPage(BasePage):
    # 尋找查找期數位置
    def check_row(self, code):
        # record = 0 # int(self.get_text_by_dom(self.find_element(OddsManagementPageLocator.page_count)))
        # page = record/25 + 1
        # if page > int(page):
        #     page = page + 1
        # page = int(page)

        page = 2
        for j in range(1, page):
            if j > 1:
                next_page = (By.XPATH, "(//a[contains(@data-bind,'text: label') and text()='{}'])[1]".format(j))
                self.click(next_page)
            for i in range(len(self.find_elements(OddsManagementPageLocator.row_count))):
                check = (By.XPATH, "//tbody[contains(@data-bind,'foreach: items')]/tr[{}]/td[1]".format(i + 1))
                if str(code) == self.get_text_by_dom(self.find_element(check)):
                    return (i + 1)

        return -1

    # 新增
    def add_odds(self, code='', name='', state=True, _min='', _max='', win='', sort=''):
        self.wait_loading_finish()
        self.click(OddsManagementPageLocator.button_add)
        self.wait_loading_finish()
        
        self.type(OddsManagementPageLocator.odds_code, code)
        self.type(OddsManagementPageLocator.odds_name, name)
        self.click(OddsManagementPageLocator.state_enable if state else OddsManagementPageLocator.state_disable)
        self.type(OddsManagementPageLocator.min_amount, _min)
        self.type(OddsManagementPageLocator.max_amount, _max)
        self.type(OddsManagementPageLocator.max_win, win)
        self.type(OddsManagementPageLocator.sort, sort)

        self.click(OddsManagementPageLocator.button_save)
        try:
            self.click(OddsManagementPageLocator.button_save)
        except:
            pass
        self.wait_loading_finish()
        self.sleep(2)

        row = self.check_row(code)
        assert row != -1, "新增功能異常"

    def modify_odds(self, odds):
        self.wait_loading_finish()
        self.click(OddsManagementPageLocator.button_odds(OddsManagementPageLocator, 1))
        self.wait_loading_finish()

        odds_origin = self.get_attribute(OddsManagementPageLocator.odds_rate, 'value')

        self.type(OddsManagementPageLocator.odds_rate, odds)

        self.wait_visibility(OddsManagementPageLocator.last_game) # 頁面為逐漸生成，故需等待最後生成的表格顯示
        self.click(OddsManagementPageLocator.button_save)

        try:
            self.wait_visibility(OddsManagementPageLocator.loading)
            self.wait_invisibility(OddsManagementPageLocator.loading)
        except:
            self.wait_loading_finish()
        
        return odds_origin

    # 修改
    def modify_handicap(self, code, state):
        self.wait_loading_finish()
        # row = self.check_row(code)
        self.click(OddsManagementPageLocator.button_modify(OddsManagementPageLocator, 1))
        self.wait_loading_finish()

        for loop in range(0, 2):
            if state is True:
                self.click(OddsManagementPageLocator.state_disable)

                if self.is_element_finded(OddsManagementPageLocator.check_disable) is True:
                    break
                else:
                    if loop == 2:
                        raise EOFError('點選已禁用錯誤')
            else:
                self.click(OddsManagementPageLocator.state_enable)

                if self.is_element_finded(OddsManagementPageLocator.check_enable) is True:
                    break
                else:
                    if loop == 2:
                        raise EOFError('點選已啟用錯誤')
                    
            self.sleep(1)

        self.sleep(1)
        self.click(OddsManagementPageLocator.button_save)

        # try:
        #     self.click(OddsManagementPageLocator.button_save)
        # except:
        #     pass

    # 確認修改功能
    def check_handicap_modification(self, code, state):
        # row = self.check_row(code)
        # assert row != -1, "查詢功能異常(修改後指定盤口消失)"
        self.wait_loading_finish()
        self.sleep(5)

        # 檢查
        check_results = self.get_text_by_dom(self.find_element((By.XPATH, f"//tbody[contains(@data-bind,'foreach: items')]/tr[{1}]/td[3]")))
        assert check_results == "已禁用" if state else "已启用", "修改功能異常(啟用結果和沒修改到)"

    # 刪除指定盤口
    def delete_odds(self, code):
        self.wait_loading_finish()
        row = self.check_row(code)
        if row != -1:
            self.wait_loading_finish()
            self.click( OddsManagementPageLocator.button_delete(OddsManagementPageLocator, row) )
            self.click( OddsManagementPageLocator.button_confirm )
            self.wait_loading_finish()

    # 確定刪除功能
    def check_delete(self, code):
        row = self.check_row(code)
        assert row == -1, "刪除功能異常"
