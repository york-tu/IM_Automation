from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import random, string, datetime

class HallManagementLocator:
    # ----------------------------- 廳別列表 -----------------------------
    hall_list = (By.XPATH, '//tbody[contains(@data-bind, "items")]//tr')
    hall_name_text = (By.XPATH, '//td[@data-bind="text: name"]') # 廳別名稱
    hall_remark_text = (By.XPATH, '//td[@data-bind="text: remark"]') # 廳別內容註釋
    min_amount_text = (By.XPATH, '//td[@data-bind="text: minamount"]') # 開局底標金額
    max_amount_text = (By.XPATH, '//td[@data-bind="text: maxamount"]') # 開局頂標金額
    odds_text = (By.XPATH, '//td[contains(@data-bind, "rate")]') # 賠率
    commision_text = (By.XPATH, '//td[@data-bind="text: fee"]') # 抽水%數
    opening_status_text = (By.XPATH, '//td[contains(@data-bind, "text: (status")]') # 狀態
    packet_time_text = (By.XPATH, '//td[@data-bind="text: ttl"]') # 封包時間
    detail_text = (By.XPATH, '//span[contains(@data-bind, "if: pointvisible")]/..') # 紅包內容詳細訊息

    button_modify = (By.XPATH, '//a[contains(text(), "修改")]') # 修改
    online_list_text = (By.XPATH, '//a[contains(text(), "在线清单")]') # 在線清單

    button_add_hall = (By.XPATH, '//button[text()="新增厅别"]') # 新增廳別

    button_last_page = (By.XPATH, '//a[text()="尾页"]') # 尾頁
    button_first_page = (By.XPATH, '//a[text()="首页"]') # 首頁

    # ----------------------------- 新增/修改 -----------------------------
    ## ------------------- 盤口 -------------------
    radio_open = (By.XPATH, '//label[contains(., "启用")]') # 啟用
    radio_close = (By.XPATH, '//label[contains(., "禁用")]') # 禁用
    ## ------------------- 名稱及註釋 -------------------
    input_box_hall_name = (By.XPATH, '//input[@data-bind="value: filter.name"]') #廳別名稱
    input_box_hall_remark = (By.XPATH, '//input[@data-bind="value: filter.remark"]') #廳別內容註釋
    ## ------------------- 金額設定 -------------------
    input_box_red_envelope = (By.XPATH, '//input[@data-bind="value: filter.qty"]') # 紅包
    input_box_package_time = (By.XPATH, '//input[@data-bind="value: filter.ttl"]') # 封包時間
    input_box_min_amount = (By.XPATH, '//input[@data-bind="value: filter.minamount"]') # 開局底標金額
    input_box_max_amount = (By.XPATH, '//input[@data-bind="value: filter.maxamount"]') # 開局頂標金額

    input_box_red_envelope_min_amount = (By.XPATH, '//input[@data-bind="value: filter.minqty"]') # 紅包數量底標
    input_box_red_envelope_max_amount = (By.XPATH, '//input[@data-bind="value: filter.maxqty"]') # 紅包數量上限
    ## ------------------- 賠率&抽水設定 -------------------
    input_box_odds = (By.XPATH, '//input[@data-bind="value: filter.rate"]') # 中雷賠率設定

    input_box_niu_1 = (By.XPATH, '//input[@data-bind="value: filter.n1rate"]') # 牛1倍數
    input_box_niu_2 = (By.XPATH, '//input[@data-bind="value: filter.n2rate"]') # 牛2倍數
    input_box_niu_3 = (By.XPATH, '//input[@data-bind="value: filter.n3rate"]') # 牛3倍數
    input_box_niu_4 = (By.XPATH, '//input[@data-bind="value: filter.n4rate"]') # 牛4倍數
    input_box_niu_5 = (By.XPATH, '//input[@data-bind="value: filter.n5rate"]') # 牛5倍數
    input_box_niu_6 = (By.XPATH, '//input[@data-bind="value: filter.n6rate"]') # 牛6倍數
    input_box_niu_7 = (By.XPATH, '//input[@data-bind="value: filter.n7rate"]') # 牛7倍數
    input_box_niu_8 = (By.XPATH, '//input[@data-bind="value: filter.n8rate"]') # 牛8倍數
    input_box_niu_9 = (By.XPATH, '//input[@data-bind="value: filter.n9rate"]') # 牛9倍數
    input_box_niu_niu = (By.XPATH, '//input[@data-bind="value: filter.nnrate"]') # 牛牛倍數

    input_box_commision = (By.XPATH, '//input[@data-bind="value: filter.fee"]') # 抽水設定
    ## ------------------- 紅包相關設定 -------------------
    radio_hide = (By.XPATH, '//label[contains(., "点数全隐藏")]') # 點數全隱藏
    radio_own = (By.XPATH, '//label[contains(., "只显示本身点数")]') # 只顯示本身點數
    radio_display = (By.XPATH, '//label[contains(., "点数全显示")]') # 點數全顯示
    ## ------------------- 確認 新增/修改 返回 Alert -------------------
    button_confirm = (By.XPATH, '//button[contains(@data-bind, "submit")]') # 確認 新增/修改
    button_back = (By.XPATH, '//button[contains(@data-bind, "backPage")]') # 返回
    add_alert = (By.XPATH, "//div[@class='toast toast-error']//div[@class='toast-message']")
    # ------------------- 頁面切換 -------------------
    button_first_page = (By.XPATH, '//a[text()="首页"]')
    button_last_page = (By.XPATH, '//a[text()="尾页"]')
    page_size = (By.XPATH, "//select[contains(@data-bind, 'pageSize')]")
    def get_page(self, index):
        return (By.XPATH, f'//a[text()="{index}"]')

class HallManagement(BasePage):

    # 將 dom 定位list 轉為text list
    def get_text_list_by_dom_list(self, dom_list):
        self.wait_loading_finish()                                                                                                # 等待一下R
        text = []
        for dom in dom_list:
            text.append(self.get_text_by_dom(dom))
        return text

    def try_parse_to_int(self, arg):
        if isinstance(arg, float) and arg.is_integer():
            return int(arg)
        elif isinstance(arg, str) and arg.isdigit():
            return int(arg)

        return arg

    def try_int_to_str(self, value):
        if isinstance(value, int):
            return (str(value).zfill(5))
        else:
            value = random.randint(1, 9999)
            return (str(value).zfill(5))
     

    def generate_data(self):
        random.seed(a=datetime.datetime.now())
        status = ['啟用', '禁用']
        detail = ['隱藏', '本身點數', '顯示']
        random_mark = random.randint(1, 9999)
        bot_id = datetime.datetime.now().strftime("QA_Automated_%Y%m%d_" + self.try_int_to_str(random_mark))
        data = {
            'status': self.try_parse_to_int(status[0]),
            # 'name': self.try_parse_to_int(''.join(random.choices(string.ascii_lowercase + string.digits, k=12))),
            # 'remark': self.try_parse_to_int(''.join(random.choices(string.ascii_lowercase + string.digits, k=12))),
            "name": bot_id,
            "remark": bot_id,
            'red_envelope': self.try_parse_to_int(random.randint(5, 10)),
            'package_time': self.try_parse_to_int(random.randint(1, 3)),
            'min_amount': 1,
            'max_amount': 1000,
            'odds': self.try_parse_to_int(round(random.uniform(1.6, 2.0) - 0.005, 2)),
            'commision': self.try_parse_to_int(random.randint(0, 5)),
            'detail': self.try_parse_to_int(random.choice(detail)),
            'red_envelope_min_amount': self.try_parse_to_int(random.randint(1, 5)),
            'red_envelope_max_amount': self.try_parse_to_int(random.randint(5, 10)),
            'niu_1': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_2': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_3': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_4': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_5': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_6': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_7': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_8': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_9': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
            'niu_niu': self.try_parse_to_int(round(random.uniform(1, 2) - 0.005, 2)),
        }

        return data

    def is_bot_hall_exist(self, name):
        index = 2

        while True:
            self.wait_loading_finish()

            hall_name = self.get_text_list_by_dom_list(self.find_elements(HallManagementLocator.hall_name_text))

            if name in hall_name:
                return True

            if self.is_element_displayed(HallManagementLocator.button_last_page):
                self.click(HallManagementLocator.get_page(HallManagementLocator, index))
            else:
                return False
            
            index += 1

    # 點擊 點數全隱藏
    def click_all_hide(self):
        self.click(HallManagementLocator.radio_hide)
    
    # 點擊 只顯示本身點數
    def click_own(self):
        self.click(HallManagementLocator.radio_own)
    
    # 點擊 點數全顯示
    def click_all_display(self):
        self.click(HallManagementLocator.radio_display)

    # 檢查新增大廳
    def check_add_hall(self, red_envelope_type, data):
        self.wait_loading_finish()
        num = 0

        if red_envelope_type == '掃雷':
            odds = 'odds'
        else:
            odds = 'niu_niu'

        self.wait_visibility(HallManagementLocator.hall_name_text) # 等待頁面跳轉回廳別規則頁面
        self.refresh_browser()
        self.wait_loading_finish()
        self.sleep(2)
        self.scroll_to_bottom()
        self.select_by_index(HallManagementLocator.page_size, 3)
        self.wait_loading_finish()
        self.scroll_to_top()
        
        assert self.wait_visibility_status(HallManagementLocator.hall_name_text) is True, '找不到廳別資料'

        self.sleep(3)

        for name in self.find_elements(HallManagementLocator.hall_name_text):
            if self.get_text_by_dom(name) == str(data['name']):
                break
            
            num += 1

        if num == 0:
            raise EOFError('未paser到廳別資料')
        
        halls = len(self.find_elements(HallManagementLocator.hall_name_text))
        self.sleep(2)
        
        if num == halls:
            raise EOFError('找不到預期廳別')
           

        # 測試try 
        try:
            temp = self.get_text_by_dom(self.find_elements(HallManagementLocator.hall_name_text)[num])
        except IndexError:
            print("重整一次")
            self.refresh_browser()


        last_hall_name = self.get_text_by_dom(self.find_elements(HallManagementLocator.hall_name_text)[num])
        last_hall_remark = self.get_text_by_dom(self.find_elements(HallManagementLocator.hall_remark_text)[num])
        last_min_amount = self.get_text_by_dom(self.find_elements(HallManagementLocator.min_amount_text)[num])
        last_max_amount = self.get_text_by_dom(self.find_elements(HallManagementLocator.max_amount_text)[num])
        last_odds = self.get_text_by_dom(self.find_elements(HallManagementLocator.odds_text)[num])
        last_commision = self.get_text_by_dom(self.find_elements(HallManagementLocator.commision_text)[num])
        last_status = self.get_text_by_dom(self.find_elements(HallManagementLocator.opening_status_text)[num])
        last_package_time = self.get_text_by_dom(self.find_elements(HallManagementLocator.packet_time_text)[num])
        last_detail = self.get_text_by_dom(self.find_elements(HallManagementLocator.detail_text)[num])

        assert last_hall_name == str(data['name']), \
            f'{red_envelope_type} -> 新增廳別 -> 廳別名稱錯誤 ... {last_hall_name} 應為-> {data["name"]}'
        assert last_hall_remark == str(data['remark']), \
            f'{red_envelope_type} -> 新增廳別 -> 廳別內容註釋錯誤 ... {last_hall_remark} 應為-> {data["remark"]}'
        assert last_min_amount == str(data['min_amount']), \
            f'{red_envelope_type} -> 新增廳別 -> 開局底標金額錯誤 ... {last_min_amount} 應為-> {data["min_amount"]}'
        assert last_max_amount == str(data['max_amount']), \
            f'{red_envelope_type} -> 新增廳別 -> 開局頂標金額錯誤 ... {last_max_amount} 應為-> {data["max_amount"]}'
        assert last_odds == str(data[odds]), \
            f'{red_envelope_type} -> 新增廳別 -> 賠率錯誤 ... {last_odds} 應為-> {data[odds]}'
        assert last_commision == str(data['commision']), \
            f'{red_envelope_type} -> 新增廳別 -> 抽水%數錯誤 ... {last_commision} 應為-> {data["commision"]}'
        assert last_package_time == str(data['package_time']), \
            f'{red_envelope_type} -> 新增廳別 -> 封包時間錯誤 ... {last_package_time} 應為-> {data["package_time"]}'

        if data['status'] == '啟用':
            assert last_status.__contains__(f'开启'), f'{red_envelope_type} -> 新增廳別 -> 狀態錯誤 ... {last_status} 應為-> 开启'
        else:
            assert last_status.__contains__(f'关闭'), f'{red_envelope_type} -> 新增廳別 -> 狀態錯誤 ... {last_status} 應為-> 关闭'

        if data['detail'] == '隱藏':
            assert last_detail.__contains__(f'点数全隐藏'), f'{red_envelope_type} -> 新增廳別 -> 紅包內容詳細訊息錯誤 ... {last_detail} 應為-> 点数全隐藏'
        elif data['detail'] == '本身點數':
            assert last_detail.__contains__(f'只显示本身点数'), f'{red_envelope_type} -> 新增廳別 -> 紅包內容詳細訊息錯誤 ... {last_detail} 應為-> 只显示本身点数'
        else:
            assert last_detail.__contains__(f'点数全显示'), f'{red_envelope_type} -> 新增廳別 -> 紅包內容詳細訊息錯誤 ... {last_detail} 應為-> 点数全显示'

    # 新增掃雷大廳
    def mine_sweeping_add_hall(self, data:dict):
        self.wait_loading_finish()
        
        for _ in range(5):

            if self.is_element_finded(HallManagementLocator.button_add_hall):
                self.click(HallManagementLocator.button_add_hall)
                break

            self.sleep(0.5)

        self.wait_loading_finish()

        switcher = {
            '隱藏': self.click_all_hide,
            '本身點數': self.click_own,
            '顯示': self.click_all_display,
        }

        self.click(HallManagementLocator.radio_open) if data['status'] == '啟用' else self.click(HallManagementLocator.radio_close)
        self.type(HallManagementLocator.input_box_hall_name, data['name'])
        self.type(HallManagementLocator.input_box_hall_remark, data['remark'])

        self.type(HallManagementLocator.input_box_red_envelope, data['red_envelope'])
        self.type(HallManagementLocator.input_box_package_time, data['package_time'])
        self.type(HallManagementLocator.input_box_min_amount, data['min_amount'])
        self.type(HallManagementLocator.input_box_max_amount, data['max_amount'])

        self.type(HallManagementLocator.input_box_odds, data['odds'])
        self.type(HallManagementLocator.input_box_commision, data['commision'])

        # 輸入其他值後，會出現紅色提示，導致 button 的位置跑掉，因此點第一下先消除提示，第二下才能正確點擊 button
        switcher[data['detail']]()
        switcher[data['detail']]()

        for _ in range(3):

            if self.is_element_finded(HallManagementLocator.button_confirm):
                self.click(HallManagementLocator.button_confirm)
                # assert self.is_element_finded(HallManagementLocator.add_alert) == True, "新增廳別失敗"
                    
                break

            self.sleep(1)

    # 檢查新增掃雷大廳
    def mine_sweeping_check_add_hall(self, data:dict):
        self.check_add_hall('掃雷', data)
            
    # 新增牛牛大廳
    def niu_niu_add_hall(self, data:dict):
        self.wait_loading_finish()

        for _ in range(5):

            if self.is_element_finded(HallManagementLocator.button_add_hall):
                self.click(HallManagementLocator.button_add_hall)
                break

            self.sleep(0.5)

        self.wait_loading_finish()
        self.sleep(1)

        switcher = {
            '隱藏': self.click_all_hide,
            '本身點數': self.click_own,
            '顯示': self.click_all_display,
        }

        if data['status'] == '啟用':
            self.click(HallManagementLocator.radio_open)
        else:
            self.click(HallManagementLocator.radio_close)

        self.type(HallManagementLocator.input_box_hall_name, data['name'])
        self.type(HallManagementLocator.input_box_hall_remark, data['remark'])

        self.type(HallManagementLocator.input_box_package_time, data['package_time'])
        self.type(HallManagementLocator.input_box_min_amount, data['min_amount'])
        self.type(HallManagementLocator.input_box_max_amount, data['max_amount'])
        self.type(HallManagementLocator.input_box_red_envelope_min_amount, data['red_envelope_min_amount'])
        self.type(HallManagementLocator.input_box_red_envelope_max_amount, data['red_envelope_max_amount'])

        self.type(HallManagementLocator.input_box_niu_1, data['niu_1'])
        self.type(HallManagementLocator.input_box_niu_2, data['niu_2'])
        self.type(HallManagementLocator.input_box_niu_3, data['niu_3'])
        self.type(HallManagementLocator.input_box_niu_4, data['niu_4'])
        self.type(HallManagementLocator.input_box_niu_5, data['niu_5'])
        self.type(HallManagementLocator.input_box_niu_6, data['niu_6'])
        self.type(HallManagementLocator.input_box_niu_7, data['niu_7'])
        self.type(HallManagementLocator.input_box_niu_8, data['niu_8'])
        self.type(HallManagementLocator.input_box_niu_9, data['niu_9'])
        self.type(HallManagementLocator.input_box_niu_niu, data['niu_niu'])
        self.type(HallManagementLocator.input_box_commision, data['commision'])

        # 輸入其他值後，會出現紅色提示，導致 button 的位置跑掉，因此點第一下先消除提示，第二下才能正確點擊 button
        switcher[data['detail']]()
        switcher[data['detail']]()

        for _ in range(3):
            if self.is_element_finded(HallManagementLocator.button_confirm):
                self.click(HallManagementLocator.button_confirm)
                break
            self.sleep(1)

    # 檢查新增牛牛大廳
    def niu_niu_check_add_hall(self, data:dict):
        self.check_add_hall('牛牛', data)