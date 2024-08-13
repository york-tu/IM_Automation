from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import random, datetime, re

class RedEnvalopeLocator:
    red_envelope = (By.XPATH, '//a[@href="/m/hb"]')
    mine_sweeping = (By.XPATH, '//span[contains(text(), "扫雷")]/following::span[contains(text(), "进入")]') # 掃雷
    niu_niu = (By.XPATH, '//span[contains(text(), "牛牛")]/following::span[contains(text(), "进入")]') # 牛牛
    
    hall = (By.XPATH, '//span[contains(@data-bind, "name")]')

    def get_hall_by_name(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')
    
    def get_remark_by_name(self, name):
        return (By.XPATH, f'//*[text()="{name}"]')
    
    @staticmethod
    # 玩法及規則
    def rule_first_hall_name(name):
        return (By.XPATH, f'(//*[contains(text(),"此厅{name}玩法及规则") or contains(text(),"此厅 ")])[last()]') # 標題 -> 大廳名稱

    # ------------------------------------ 內容 ------------------------------------
    rule_second_hall_name = (By.XPATH, '//div[@id="swal2-content"]//p//span[contains(@data-bind, "roomName")]') # 大廳名稱
    min_amount = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "底标金")]') # 底標
    max_amount = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "顶标金")]') # 頂標
    odds = (By.XPATH, '((//div[@class= "m-rule__content" or @class= "info-item"])[last()]//*[ contains(@data-bind, "rate") or contains(text(), "中雷赔率")])[last()]') # 賠率
    red_envelope_amount = (By.XPATH, '((//div[@class= "m-rule__content" or @class= "info-item"])[last()]//*[ contains(@data-bind, "redEnvelopeNumber") or contains(text(), "发送包数")])[last()]') # 發送包數
    settlement_time = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "结算时间")]') # 結算時間
    fee = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "抽水")]') # 抽水

    menu_bar = (By.XPATH, '//a[@class="menu-btn"]') # 下拉bar
    bar_open = (By.XPATH, '//div[@class="wcr-list"]')
    deposit = (By.XPATH, '//*[contains(text(), "充值")]/..') # 充值
    game_play = (By.XPATH, '//*[contains(text(), "玩法")]/..') # 玩法
    rules = (By.XPATH, '//*[contains(text(), "规则")]/..') # 規則
    customer_service = (By.XPATH, '//*[contains(@class, "item")]//*[contains(text(), "客服")]/..') # 客服
    record = (By.XPATH, '//*[contains(text(), "纪录")]/..') # 紀錄
    close_windows = (By.XPATH, '//*[@class= "rule-close" or text()= "关闭取消"]') # 關閉視窗
    ## ------------------------------------ 跳轉連結 ------------------------------------
    deposit_page = (By.XPATH, '//*[contains(text(), "充值")]') # 入款頁面
    game_play_page = (By.XPATH, '//div[@id="app"]') # 玩法頁面
    rules_page = (By.XPATH, '//*[text()= "确认" or text()= "关闭取消"]') # 規則對話框
    ## ------------------------------------ 牛牛 ------------------------------------
    red_envelope_range = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "发送包数")]') # 發包數 -> 最大小值
    niu_1_odds = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "牛1至牛6赔率")]') # 牛1至牛6賠率
    niu_7_odds = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "牛7至牛9赔率")]') # 牛7至牛9賠率
    niu_niu_odds = (By.XPATH, '(//div[@class= "m-rule__content" or @class= "info-item"])[last()]//p[contains(text(), "牛牛赔率")]') # 牛牛赔率

    cancell = (By.XPATH, '//*[contains(text(),"取消")]') # 取消
    confirm = (By.XPATH, '//*[contains(text(),"确认")]') # 確認

    button_give_red_envelope = (By.XPATH, '//a[@class="btn"]') # 發紅包
    button_service = (By.XPATH, '//span[text()= "开始咨询"]')
    # ------------------------------------ 塞紅包頁面 ------------------------------------
    total_amount = (By.XPATH, '//div[@class="total__amount"]') # 最上方的總金額
    input_box_total_amount = (By.XPATH, '//div[contains(text(), "金额")]/../input') # 總金額
    input_box_mine_number = (By.XPATH, '//input[contains(@placeholder, "雷号")]') # 雷號
    input_box_niu_number = (By.XPATH, '//div[text()= "红包个数"]/following::input') # 紅包個數
    red_envelope_amount_give_page = (By.XPATH, '//div[contains(@class, "total")]//*[contains(@data-bind, "qty") or @class= "total__text"]') # 紅包個數
    button_confirm = (By.XPATH, '//div[contains(@data-bind, "submit") or text()= " 塞钱进红包 "]') # 塞錢進紅包

class RedEnvalope(BasePage):
    def get_bot_hall_data(self):
        random.seed(a=datetime.datetime.now())
        status = ('啟用', '禁用')
        detail = ('隱藏', '本身點數', '顯示')
        data = {
            'status': status[0],
            'name': 'bot_red_envelope_hall',
            'remark': 'bot_red_envelope_hall_Remark',
            'red_envelope': 5,
            'package_time': 2,
            'min_amount': 1,
            'max_amount': 1000,
            'odds': 1.6,
            'commision': 3,
            'detail': detail[0],
            'red_envelope_min_amount': 2,
            'red_envelope_max_amount': 10,
            'niu_1': 1,
            'niu_2': 1,
            'niu_3': 1,
            'niu_4': 1,
            'niu_5': 1,
            'niu_6': 1,
            'niu_7': 1,
            'niu_8': 1,
            'niu_9': 1,
            'niu_niu': 1,
        }

        return data
    
    def get_prod_bot_hall_data(self, game):
        random.seed(a=datetime.datetime.now())
        game_name = ('5-50高赔低水', '固定赔率轻松玩 ')
        game_remark = ('可发可抢（6包1.67倍仅抽3%）24小时娱乐', '全牌型固定赔率1倍（24小时娱乐）')
        game_min_amount = (5, 1)
        game_max_amount = (50, 100)
        commision = (3, 5)
        data = {
            'name': game_name[game],
            'remark': game_remark[game],
            'red_envelope': 6,
            'package_time': 1,
            'min_amount': game_min_amount[game],
            'max_amount': game_max_amount[game],
            'odds': 1.67,
            'commision': commision[game],
            'red_envelope_min_amount': 5,
            'red_envelope_max_amount': 10,
            'niu_1': 1,
            'niu_2': 1,
            'niu_3': 1,
            'niu_4': 1,
            'niu_5': 1,
            'niu_6': 1,
            'niu_7': 1,
            'niu_8': 1,
            'niu_9': 1,
            'niu_niu': 1,
        }

        return data
    
    #進入牛牛/掃雷現在走Menupage的 這裡沒用到
    #def into_mine_sweeping(self):
    #    self.wait_loading_finish()
    #    self.click(RedEnvalopeLocator.red_envelope)
    #    self.click(RedEnvalopeLocator.mine_sweeping)
    
    #def into_niu_niu(self):
    #    self.wait_loading_finish()
    #    self.click(RedEnvalopeLocator.red_envelope)
    #    self.click(RedEnvalopeLocator.niu_niu)

    def into_give_red_envelope(self):
        self.wait_loading_finish()
        self.click(RedEnvalopeLocator.button_give_red_envelope)

    def check_hall_common_rule(self, data : dict, env):
        self.wait_loading_finish()
        self.sleep(1)

        assert self.is_element_finded(RedEnvalopeLocator.get_hall_by_name(RedEnvalopeLocator, data['name'])), f'進入大廳錯誤 ... 大廳 {data["name"]} 不存在'
        assert self.get_text(RedEnvalopeLocator.get_remark_by_name(RedEnvalopeLocator, data['remark'])) == str(data['remark']), \
            f'大廳 -> 注釋錯誤 ... {self.get_text(RedEnvalopeLocator.get_remark_by_name(RedEnvalopeLocator, data["remark"]))} 應為-> {data["remark"]}'

        self.click(RedEnvalopeLocator.get_hall_by_name(RedEnvalopeLocator, data['name']))
        self.sleep(1)

        hall_name = re.sub("[^A-Za-z0-9_]", "", self.get_text(RedEnvalopeLocator.rule_first_hall_name(data['name'])))
        min_amount = re.sub("[^0-9]", "", self.get_text(RedEnvalopeLocator.min_amount))
        max_amount = re.sub("[^0-9]", "", self.get_text(RedEnvalopeLocator.max_amount))
        settlement_time = re.sub("[^0-9]", "", self.get_text(RedEnvalopeLocator.settlement_time))
        fee = re.sub("[^0-9]", "", self.get_text(RedEnvalopeLocator.fee))
        
        if env != 'prod':
            assert hall_name == str(data['name']), f'大廳規則 -> 標題 -> 名稱錯誤 ... {hall_name} 應為-> {data["name"]}'
            # assert self.get_text(RedEnvalopeLocator.rule_second_hall_name) == str(data['name']), \
            #     f'大廳規則 -> 內容 -> 名稱錯誤 ... {self.get_text(RedEnvalopeLocator.rule_second_hall_name)} 應為-> {data["name"]}'
            assert min_amount == str(data['min_amount']), f'大廳規則 -> 內容 -> 底標錯誤 ... {min_amount} 應為-> {data["min_amount"]}'
            assert max_amount == str(data['max_amount']), f'大廳規則 -> 內容 -> 頂標錯誤 ... {max_amount} 應為-> {data["max_amount"]}'

            assert settlement_time == str(data['package_time']), f'大廳規則 -> 內容 -> 結算時間錯誤 ... {settlement_time} 應為-> {data["package_time"]}'
            assert fee == str(data['commision']), f'大廳規則 -> 內容 -> 抽水錯誤 ... {fee} 應為-> {data["commision"]}'

    def into_mine_sweeping_hall(self, data : dict, env):
        self.wait_loading_finish()
        self.check_hall_common_rule(data, env)

        red_envelope = re.sub("[^0-9]", "", self.get_text(RedEnvalopeLocator.red_envelope_amount))
        odds = re.sub("[^0-9.]", "", self.get_text(RedEnvalopeLocator.odds))

        assert red_envelope == str(data['red_envelope']), f'大廳規則 -> 內容 -> 發送包數錯誤 ... {red_envelope} 應為-> {data["red_envelope"]}'
        assert odds == str(data['odds']), f'大廳規則 -> 內容 -> 賠率錯誤 ... {odds} 應為-> {data["odds"]}'

        self.click(RedEnvalopeLocator.confirm)

    def into_niu_niu_hall(self, data : dict, env):
        self.wait_loading_finish()
        self.check_hall_common_rule(data, env)

        range_envelope = re.findall("[0-9]+", self.get_text(RedEnvalopeLocator.red_envelope_range))
        min_envelope = range_envelope[0]
        max_envelope = range_envelope[1]
   
        niu_1_odds = (re.sub("[^0-9.]", "", (self.get_text(RedEnvalopeLocator.niu_1_odds).split(':'))[-1]))
        niu_7_odds = (re.sub("[^0-9.]", "", (self.get_text(RedEnvalopeLocator.niu_7_odds).split(':'))[-1]))
        niu_niu_odds = (re.sub("[^0-9.]", "", (self.get_text(RedEnvalopeLocator.niu_niu_odds).split(':'))[-1]))

        assert min_envelope == str(data['red_envelope_min_amount']), f'大廳規則 -> 內容 -> 發送包數最小值錯誤 ... {min_envelope} 應為-> {data["red_envelope_min_amount"]}'
        assert max_envelope == str(data['red_envelope_max_amount']), f'大廳規則 -> 內容 -> 發送包數最大值錯誤 ... {max_envelope} 應為-> {data["red_envelope_max_amount"]}'
        assert niu_1_odds == str(data['niu_1']), f'大廳規則 -> 內容 -> 牛1至牛6賠率錯誤 ... {niu_1_odds} 應為-> {data["niu_1"]}'
        assert niu_7_odds == str(data['niu_7']), f'大廳規則 -> 內容 -> 牛7至牛9賠率錯誤 ... {niu_7_odds} 應為-> {data["niu_7"]}'
        assert niu_niu_odds == str(data['niu_niu']), f'大廳規則 -> 內容 -> 牛牛賠率錯誤 ... {niu_niu_odds} 應為-> {data["niu_niu"]}'

        self.click(RedEnvalopeLocator.confirm)

    def check_link_in_hall(self):
        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.menu_bar) is True:
            if self.is_element_finded(RedEnvalopeLocator.bar_open) is True:
                self.click(RedEnvalopeLocator.menu_bar)

        self.sleep(1)
        self.click(RedEnvalopeLocator.deposit)
        self.wait_loading_finish()

        assert self.is_element_finded(RedEnvalopeLocator.deposit_page), f'大廳內充值連結錯誤 ... 未正確導轉至充值頁面'

        if self.is_element_finded(RedEnvalopeLocator.close_windows) is True:
            self.click(RedEnvalopeLocator.close_windows)
        else:
            self.back()

        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.menu_bar) is True:
            if self.is_element_finded(RedEnvalopeLocator.bar_open) is True:
                self.click(RedEnvalopeLocator.menu_bar)

        self.sleep(1)
        self.click(RedEnvalopeLocator.game_play)
        self.wait_loading_finish()

        assert self.is_element_finded(RedEnvalopeLocator.game_play_page), f'大廳內玩法連結錯誤 ... 未正確導轉至玩法頁面'
        
        if self.is_element_finded(RedEnvalopeLocator.close_windows) is True:
            self.click(RedEnvalopeLocator.close_windows)
        else:
            self.back()

        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.menu_bar) is True:
            if self.is_element_finded(RedEnvalopeLocator.bar_open) is True:
                self.click(RedEnvalopeLocator.menu_bar)

        self.sleep(1)
        self.click(RedEnvalopeLocator.rules)
        self.sleep(0.75)

        assert self.is_element_finded(RedEnvalopeLocator.rules_page), f'大廳內規則連結錯誤 ... 未正確導轉至規則頁面'

        if self.is_element_finded(RedEnvalopeLocator.close_windows) is True:
            self.click(RedEnvalopeLocator.close_windows)
        elif self.is_element_finded(RedEnvalopeLocator.confirm) is True:
            self.click(RedEnvalopeLocator.confirm)
        else:
            self.back()

        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.menu_bar) is True:
            if self.is_element_finded(RedEnvalopeLocator.bar_open) is True:
                self.click(RedEnvalopeLocator.menu_bar)

        self.sleep(1)
        self.open_new_window(RedEnvalopeLocator.customer_service)
        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.button_service) is True:
            assert self.is_element_finded(RedEnvalopeLocator.button_service), f'大廳內客服連結錯誤 ... 未正確導轉至客服頁面'
            self.wait_loading_finish()
        elif self.is_element_finded(RedEnvalopeLocator.customer_service) is True:
            assert self.is_element_finded(RedEnvalopeLocator.customer_service), f'大廳內客服連結錯誤 ... 未正確導轉至客服頁面'
        else:
            print('大廳內客服連結錯誤,請確認後台是否有開啟')

        if self.is_element_finded(RedEnvalopeLocator.close_windows) is True:
            self.click(RedEnvalopeLocator.close_windows)
        else:
            self.back()

        self.wait_loading_finish()

        if self.is_element_finded(RedEnvalopeLocator.menu_bar) is True:
            if self.is_element_finded(RedEnvalopeLocator.bar_open) is True:
                self.click(RedEnvalopeLocator.menu_bar)

        self.sleep(1)
        self.click(RedEnvalopeLocator.record)
        self.wait_loading_finish()

        assert not self.is_element_finded(RedEnvalopeLocator.button_give_red_envelope), f'大廳內紀錄連結錯誤 ... 未正確導轉至紀錄頁面'

        if self.is_element_finded(RedEnvalopeLocator.close_windows) is True:
            self.click(RedEnvalopeLocator.close_windows)
        else:
            self.back()

        self.wait_loading_finish()

    def check_give_red_envelope_data(self, data):
        self.wait_loading_finish()

        Amount = self.get_attribute(RedEnvalopeLocator.input_box_total_amount, 'placeholder')
        max_amount = Amount.split(' - ')[1]
        min_amount = Amount.split(' - ')[0]

        assert max_amount == str(data['max_amount']), f'總金額提示訊息錯誤 ... 上限 {max_amount} 應為-> {data["max_amount"]}'
        assert min_amount == str(data['min_amount']), f'總金額提示訊息錯誤 ... 下限 {min_amount} 應為-> {data["min_amount"]}'

    def check_mine_sweeping_give_red_envelope_data(self, data):
        self.wait_loading_finish()

        red_envelope_amount = self.get_text(RedEnvalopeLocator.red_envelope_amount_give_page)
        assert red_envelope_amount == str(data['red_envelope']), f'紅包個數錯誤 ... {red_envelope_amount} 應為-> {data["red_envelope"]}'

        self.check_give_red_envelope_data(data)
        self.click(RedEnvalopeLocator.button_confirm)

    def check_niu_niu_give_red_envelope_data(self, data):
        self.wait_loading_finish()

        red_envelope_min_amount = self.get_attribute(RedEnvalopeLocator.input_box_mine_number, 'placeholder').split(' - ')[0]
        red_envelope_max_amount = self.get_attribute(RedEnvalopeLocator.input_box_mine_number, 'placeholder').split(' - ')[1]
        assert red_envelope_min_amount == str(data['red_envelope_min_amount']), \
            f'紅包個數最小值錯誤 ... {red_envelope_min_amount} 應為-> {data["red_envelope_min_amount"]}'
        assert red_envelope_max_amount == str(data['red_envelope_max_amount']), \
            f'紅包個數最大值錯誤 ... {red_envelope_max_amount} 應為-> {data["red_envelope_max_amount"]}'

        self.check_give_red_envelope_data(data)
        self.click(RedEnvalopeLocator.button_confirm)

    def give_red_envelope(self, amount, number):
        self.wait_loading_finish()
        self.type(RedEnvalopeLocator.input_box_total_amount, amount)

        if self.is_element_finded(RedEnvalopeLocator.input_box_niu_number) is True:
            self.type(RedEnvalopeLocator.input_box_niu_number, number)

        if self.is_element_finded(RedEnvalopeLocator.input_box_mine_number) is True:
            self.type(RedEnvalopeLocator.input_box_mine_number, number)
        
        self.click(RedEnvalopeLocator.button_confirm)
