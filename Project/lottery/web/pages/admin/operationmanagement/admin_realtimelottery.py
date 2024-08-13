import time
import datetime
import sys
import re
import copy

from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage


def logged(func):
    def with_logging(*args, **kwargs):
        # print(func.__name__ + "  was called")
        return (func(*args, **kwargs))
    return with_logging

class RealTimeOrderLocator:
    # =============== 查找條件 =====================
    """
        type_of_product : 產品類型
        type_of_pankou : 盤口
        class_of_play : 玩法類型

        history_of_period : 歷史期數

        auto_fresh : 自動刷新
        Alert_of_order : 警示筆數
        Alert_of_total_amount : 警示總金額

        btn_search : 查找按鈕
    """
    type_of_product = (By.XPATH, "//select[contains(@data-bind, 'productname') and @class = 'form-control']")
    type_of_pankou = (By.XPATH, "//select[contains(@data-bind, 'roomcode') and @class = 'form-control']")
    class_of_play = (By.XPATH, "//select[contains(@data-bind, 'playcode') and @class = 'form-control']")

    history_of_period = (By.XPATH, "//div[@class = 'col-md-2']//input[@data-bind = 'value: filter.productnumber']")

    auto_fresh_checkbox = (By.XPATH, "//div[@class = 'input-group-addon']//input[@data-bind = 'checked:filter.auto']/..")
    auto_fresh = (By.XPATH, "//div[@class = 'input-group']//input[@data-bind = 'value:filter.interval']")

    btn_search = (By.XPATH, "//div[@class = 'col-md-offset-1 col-md-8 text-left']//button[@id='btnSearch']")

    # =============== 即時注單(表單) ==================
    """
        btn_return : 返回
    """
    btn_return = (By.XPATH, "//div[@class = 'table-responsive']//a[contains(text(), '返回')]")

    # ========== 即時注單(表單) (遊戲內表) =============
    """
        period_number : 期數
        table_of_classplay : 玩法類型
        Total_items : 筆數
        Total_amount : 總金額
    """
    period_number = (By.XPATH, "//div[@class = 'table-responsive']//span[@data-bind = 'text: room()']")
    table_of_classplay = (By.XPATH, "//a[contains(@data-bind,'playname')]")
    all_items = (By.XPATH, "//tbody[@data-bind = 'foreach: items']//span[@data-bind='text: count']")
    all_amount = (By.XPATH, "//tbody[@data-bind = 'foreach: items']//span[@data-bind='text: total']")

    # ===== 即時注單(表單) (asc & desc & sort) ========
    items_sort = (By.XPATH, "//th[@class='text-center']/*[contains(. , '笔数')]")
    items_asc = (By.XPATH, "//th[@class='text-center']/*[contains(. , '笔数')]//i[@class = 'fa fa-fw fa-sort-asc']")
    items_desc = (By.XPATH, "//th[@class='text-center']/*[contains(. , '笔数')]//i[@class = 'fa fa-fw fa-sort-desc']")

    amount_sort = (By.XPATH, "//th[@class='text-center']/*[contains(. , '总金额')]") 
    amount_asc = (By.XPATH, "//th[@class='text-center']/*[contains(. , '总金额')]//i[@class='fa fa-fw fa-sort-asc']")
    amount_desc = (By.XPATH, "//th[@class='text-center']/*[contains(. , '总金额')]//i[@class='fa fa-fw fa-sort-desc']")

# -------------------------------------------------------------------------------
class RealTimeOrderPage(BasePage):
    # 六合彩系列玩法類型
    six_current = tuple(["总表", "特码-号码", "特码-合肖", "特码-两面", "特码-特肖", "特码-头数", "特码-尾数", "特码-五行", "正码-号码", "正码-总和", "正码-正肖", \
        "正码特-正码特一-号码", "正码特-正码特一-两面", "正码特-正码特一-色波", "正码特-正码特二-号码", "正码特-正码特二-两面", "正码特-正码特二-色波", "正码特-正码特三-号码", "正码特-正码特三-两面", \
        "正码特-正码特三-色波", "正码特-正码特四-号码", "正码特-正码特四-两面", "正码特-正码特四-色波", "正码特-正码特五-号码", "正码特-正码特五-两面", "正码特-正码特五-色波", "正码特-正码特六-号码", \
        "正码特-正码特六-两面", "正码特-正码特六-色波", "正码特-正码特一", "正码特-正码特二", "正码特-正码特三", "正码特-正码特四", "正码特-正码特五", "正码特-正码特六", \
        "平特肖尾-一肖", "连肖连尾-二肖连", "连肖连尾-三肖连", "连肖连尾-四肖连", "连肖连尾-五肖连", "平特肖尾-一尾", "连肖连尾-二尾碰", "连肖连尾-三尾碰", "连肖连尾-四尾碰", "连肖连尾-五尾碰", \
        "连码-特串", "连码-二中特", "连码-二全中", "连码-三中二", "连码-三全中", "连码-四全中", "正码-总肖", "不中-五不中", "不中-六不中", "不中-七不中", "不中-八不中", "不中-九不中", \
        "不中-十不中", "不中-十一不中", "不中-十二不中", "色波-色波", "色波-半波", "色波-半半波", "色波-七色波", "中一-五中一", "中一-六中一", "中一-七中一", "中一-八中一", "中一-九中一", \
        "中一-十中一"])
    
    # Error testing
    # six_current = tuple(["总表", "特码-号码", "特码-合肖", "特码-两面", "特码-特肖", "特码-头数", "特码-尾数", "特码-五行", "正码-号码", "正码-总和", "正码-正肖", \
    #     "正码特-正码特一-号码", "正码特-正码特一-两面", "正码特-正码特一-色波", "正码特-正码特二-号码", "正码特-正码特二-两面", "正码特-正码特二-色波", "正码特-正码特三-号码", "正码特-正码特三-两面", \
    #     "正码特-正码特三-色波", "正码特-正码特四-号码", "正码特-正码特四-两面", "正码特-正码特四-色波", "正码特-正码特五-号码", "正码特-正码特五-两面", "正码特-正码特五-色波", "正码特-正码特六-号码", \
    #     "正码特-正码特六-两面", "正码特-正码特六-色波", "正码特-正码特一", "正码特-正码特二", "正码特-正码特三", "正码特-正码特四", "正码特-正码特五", "正码特-正码特六", \
    #     "平特肖尾-一肖", "连肖连尾-二肖连", "连肖连尾-三肖连", "连肖连尾-四肖连", "连肖连尾-五肖连", "平特肖尾-一尾", "连肖连尾-二尾碰", "连肖连尾-三尾碰", "连肖连尾-四尾碰", "连肖连尾-五尾碰", \
    #     "连码-特串", "连码-二中特", "连码-二全中", "连码-三中二", "连码-三全中", "连码-四全中", "正码-总肖", "不中-五不中", "不中-六不中", "不中-七不中", "不中-八不中", "不中-九不中", \
    #     "不中-十不中", "不中-十一不中", "不中-十二不中", "色波-色波", "色波-半波", "色波-半半波", "色波-七色波", "中一-五中一", "中一-六中一", "中一-七中一", "中一-八中一", "中一-九中一", \
    #     "中一-十中一", "Norman_error_test"])

    # 時時彩系列玩法類型
    shihshih_current = tuple(["总表", "两面 - 万", "两面 - 千", "两面 - 百", "两面 - 十", "两面 - 个", "总和", "总和 - 尾数", "龙虎和", "和值 - 五字", "和值 - 前三", "和值 - 中三", \
        "和值 - 后三", "和值 - 万千", "和值 - 万百", "和值 - 万十", "和值 - 万个", "和值 - 千百", "和值 - 千十", "和值 - 千个", "和值 - 百十", "和值 - 百个", "和值 - 十个", "和尾数 - 五字", \
        "和尾数 - 前三", "和尾数 - 中三", "和尾数 - 后三", "和尾数 - 万千", "和尾数 - 万百", "和尾数 - 万十", "和尾数 - 万个", "和尾数 - 千百", "和尾数 - 千十", "和尾数 - 千个", "和尾数 - 百十", \
        "和尾数 - 百个", "和尾数 - 十个", "任选一 - 全五", "任选一 - 前三", "任选一 - 中三", "任选一 - 后三", "一字定位 - 万", "一字定位 - 千", "一字定位 - 百", "一字定位 - 十", "一字定位 - 个", \
        "二字定位 - 万千", "二字定位 - 万百", "二字定位 - 万十", "二字定位 - 万个", "二字定位 - 千百", "二字定位 - 千十", "二字定位 - 千个", "二字定位 - 百十", "二字定位 - 百个", "二字定位 - 十个", \
        "三字定位 - 前三", "三字定位 - 中三", "三字定位 - 后三", "五字定位", "组选三 - 前三", "组选三 - 中三", "组选三 - 后三", "组选六 - 前三", "组选六 - 中三", "组选六 - 后三", "跨度 - 前三", \
        "跨度 - 中三", "跨度 - 后三", "特殊玩法 - 前三", "特殊玩法 - 中三", "特殊玩法 - 后三"])

    # PK10系列玩法類型
    pk10_current = tuple(["总表", "冠军", "亚军", "季军", "第四名", "第五名", "第六名", "第七名", "第八名", "第九名", "第十名", "冠亚军和-号码", "冠亚军和-两面", "冠军VS第十名-龙虎", \
        "亚军VS第九名-龙虎", "季军VS第八名-龙虎", "第四名VS第七名-龙虎", "第五名VS第六名-龙虎"])

    # 幸運28系列玩法類型
    lucky28_current = tuple(["总表", "特码 - 号码", "特码 - 包三", "色波", "两面", "特殊"])

    # 11選5系列玩法類型
    choice5_current = tuple(["总表", "总和", "两面-第一球", "两面-第二球", "两面-第三球", "两面-第四球", "两面-第五球", "单码-第一球", "单码-第二球", "单码-第三球", "单码-第四球", \
        "单码-第五球", "任选一", "任选二", "任选三", "任选四", "任选五", "任选六", "任选七", "任选八", "组选前二", "组选前三", "直选前二", "直选前三"])

    # 快3系列玩法類型
    fast3_current = tuple(["总表", "两面", "点数", "三军", "围骰/全骰", "长牌", "短牌"])

    # 一般彩票系列玩法類型
    basic_current = tuple(["总表", "一字定位-百", "一字定位-十", "一字定位-个", "字串关", "二星组选", "三星组选三", "三星组选六", "三星特别玩法", "和值(百十个位)", "龙虎和", "和尾数", "跨度"])

    # 分類遊戲玩法
    game_name_list = ["香港六合彩", "极速时时彩", "澳洲幸运10", "PC蛋蛋", "极速11选5", "极速快3", "福彩3D"]

    # 正確遊戲分類
    ticket_current_list = [(six_current), (shihshih_current), (pk10_current), (lucky28_current), (choice5_current), (fast3_current), (basic_current)]

    # Auto refresh and alert
    checkbox_list = [(RealTimeOrderLocator.auto_fresh_checkbox)]

# -------------------------------------------------------------------------------
    # one of the main action
    # 產品類型、盤口、玩法類型(總表)
    # 包含 Compare {Table, Current}
    @logged
    def product_period_check(self):
        game_name_list = copy.deepcopy(self.game_name_list)
        ticket_current_list = copy.deepcopy(self.ticket_current_list)
        
        for _ in (ticket_current_list):
            self.change_setting_for_search(game_name_list)
            tick_name = self.popout_list(ticket_current_list)

            # search finish return three parameter
            tickname, table_game_list, select_game_list = self.search_table_and_select(tick_name)
            self.compare_current(tickname, table_game_list, select_game_list)

    # for each search
    @logged
    def change_setting_for_search(self, game_name_list):
        self.wait_loading_finish()
        game_name = self.popout_list(game_name_list)
        self.select_by_text(RealTimeOrderLocator.type_of_product, game_name)
        assert self.is_element_finded(RealTimeOrderLocator.type_of_product) == True, "產品類型 can't find"
        self.select_by_index(RealTimeOrderLocator.type_of_pankou, 0)
        assert self.is_element_finded(RealTimeOrderLocator.type_of_pankou) == True, "盤口類型 can't find"
        self.select_by_text(RealTimeOrderLocator.class_of_play, "总表")
        assert self.is_element_finded(RealTimeOrderLocator.class_of_play) == True, "玩法類型 can't find"
        self.click(RealTimeOrderLocator.btn_search)
        assert self.is_element_finded(RealTimeOrderLocator.btn_search) == True, "search button can't find"
        self.wait_loading_finish()

    # 搜尋列表使用 each time to popout list[0] position and return
    @logged
    def popout_list(self, list_type):
        ticket = list_type.pop(0)
        return ticket
    
    # search and catch "table & select" name from datalist
    @logged
    def search_table_and_select(self, tick_name_tuple):
        tick_name = tick_name_tuple
        table_game_list = []
        select_game_list = []
        
        # Table report
        for element in (self.find_elements(RealTimeOrderLocator.table_of_classplay)):
            # table_text = (self.get_text_by_dom(element).encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding))
            table_text = self.get_text_by_dom(element)
            table_game_list.append(table_text)

        # Select report
        if tick_name == self.six_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element)
                table_text = re.split('\\n| ', table_text)
                table_text_num = len(table_text)
                table_popnum_list = []

                for index in range(table_text_num):
                    if table_text[index] == '':
                        table_popnum_list.append(index)
                table_popnum_list.reverse()
                for index in (table_popnum_list):
                    del table_text[index]

                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

        elif tick_name == self.shihshih_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

        elif tick_name == self.pk10_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

        elif tick_name == self.lucky28_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

        elif tick_name == self.choice5_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

        elif tick_name == self.fast3_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text

            return tick_name, table_game_list, select_game_list

        elif tick_name == self.basic_current:
            for element in (self.find_elements(RealTimeOrderLocator.class_of_play)):
                table_text = self.get_text_by_dom(element).strip()
                table_text = re.split('\n', table_text)
                select_game_list = table_text
            
            return tick_name, table_game_list, select_game_list

    #  Compare "Table & Select" data current
    @logged
    def compare_current(self, tick_name, table_game_list, select_game_list):
        table_game_set = set(table_game_list)
        select_game_set = set(select_game_list)
        compare_set = set(tick_name)
        
        difference_table_list = list(table_game_set.difference(compare_set))
        difference_select_list = list(select_game_set.difference(compare_set))

        assert len(difference_table_list) == 0, "即時注單(Table)玩法類型不正確({0})".format(difference_table_list)
        assert len(difference_select_list) == 0, "玩法類型(Select)玩法類型不正確({0})".format(difference_select_list)

# -------------------------------------------------------------------------------
    # compare period number
    # def compare_period_number(self, Current_period):
    #     now = self.get_text(RealTimeOrderLocator.period_number)
    #     Current = Current_period
    #     print(now)

    # record chance lottery period(default: 
    # def record_period_number(self, ):
    #     record_number = 
    #     return record_number
# ------------------------------------------------------------------------------- 

# -------------------------------------------------------------------------------
    # Table action
    @logged
    def basic_table_check(self):
        game_name_list = copy.deepcopy(self.game_name_list)
        for _ in (game_name_list):
            game_name = self.popout_list(game_name_list)
            self.select_by_text(RealTimeOrderLocator.type_of_product, game_name)
            self.click(RealTimeOrderLocator.btn_search)
            self.wait_loading_finish()
            info = self.build_order_table_info()
            self.order_table_info_check(info)

# -------------------------------------------------------------------------------
    # "即時注單" -> all infomation tranform to dict type
    @logged
    def build_order_table_info(self):
        all_items = RealTimeOrderLocator.all_items
        all_amount = RealTimeOrderLocator.all_amount
        table_game = RealTimeOrderLocator.table_of_classplay
        info_list = [table_game, all_items, all_amount]

        table_game_list = []
        all_items_list = []
        all_amount_list = []

        info_record_list = []

        for index in info_list:
            for element in (self.find_elements(index)):           
                table_text = (self.get_text_by_dom(element))
                if index == info_list[0]:
                    table_game_list.append(table_text)
                elif index == info_list[1]:
                    all_items_list.append(table_text)
                elif index == info_list[2]:
                    all_amount_list.append(table_text)

        assert (len(table_game_list) == len(all_items_list)) and (len(all_items_list) == len(all_amount_list)), "即時注單(Table)有誤"

        for index in range(len(table_game_list)):
            order_table_record = {
                "gamename": table_game_list[index],
                "items": all_items_list[index],
                "amount": all_amount_list[index]
            }
            info_record_list.append(order_table_record)

        return info_record_list

    # dict_in_list (e.g. [{}, {}, {}])
    @logged
    def order_table_info_check(self, dict_in_list):
        for index in range(len(dict_in_list)):
            order_info = dict_in_list[index]
            assert (order_info["items"] == 0 and order_info["amount"] == 0) or (order_info["items"] != 0 and order_info["amount"] != 0), "{0} 玩法類型錯誤".format(order_info["gamename"])           

# -------------------------------------------------------------------------------
    # alert_action
    @logged
    def alert_action_check(self):
        self.auto_refresh_set()
        self.sleep(1)
        self.refresh_data_check()
        locator = self.return_checkbox_locator()
        self.cancel_click(locator)
        self.sleep(1)
        
# -------------------------------------------------------------------------------
    # auto refresh
    @logged
    def auto_refresh_set(self):
        loading_mask = (By.XPATH, "//*[@id='jqueryEasyOverlayDiv' and contains(@style,'display: block')]")
        self.select_by_text(RealTimeOrderLocator.type_of_product, "香港六合彩")
        self.type(RealTimeOrderLocator.auto_fresh, "25")
        self.click(RealTimeOrderLocator.auto_fresh_checkbox)
        start_time = time.time()
        while(True):
            if self.wait_visibility_status(loading_mask) is True:
                end_time = time.time()
                # self.wait_visibility(loading_mask)
                break
        auto_fresh_time = end_time - start_time
        # print("%.4f" %auto_fresh_time)
        self.sleep(1)
        assert auto_fresh_time > float(24.5) or auto_fresh_time < float(25.5), "{0} sec is overset".format("%.4f" %auto_fresh_time)

        # Conform reload updata data equal current data
        table_game_list = []
        for element in (self.find_elements(RealTimeOrderLocator.table_of_classplay)):
            table_text = self.get_text_by_dom(element)
            table_game_list.append(table_text)

        current_data_from_six = copy.deepcopy(self.six_current)
        current_data_from_six = list(current_data_from_six)
        current_data_from_six_set = set(current_data_from_six)

        table_game_set = set(table_game_list)

        different_Table_list = list(table_game_set.difference(current_data_from_six_set))

        # assert current_data_from_six == table_game_list, "Reload data not equal with current data"
        assert len(different_Table_list) == 0, "Reload data not equal with current data, 即時注單(Table)玩法類型不正確({0})".format(different_Table_list)
        
    # after refresh, the table data will success transform to right data by HK
    @logged
    def refresh_data_check(self):
        table_game_list = []
        six_current = copy.deepcopy(self.six_current)
        for element in (self.find_elements(RealTimeOrderLocator.table_of_classplay)):
            table_text = self.get_text_by_dom(element)
            table_game_list.append(table_text)

        table_game_set = set(table_game_list)
        compare_set = set(six_current)

        difference = list(table_game_set.difference(compare_set))
        
        assert len(difference) == 0, "Refresh & update data wrong"

    # checkbox locator
    # only for checkbox (auto_fresh_checkbox, Alert_of_order_checkbox, Alert_of_total_amount_checkbox)
    @logged
    def return_checkbox_locator(self):
        checkbox_list = self.checkbox_list
        if len(checkbox_list) > 0:
            locator = self.popout_list(checkbox_list)
        return locator

    # 暴力動作取消
    @logged
    def cancel_click(self, locator):
        if self.is_element_enable(locator) is True:
            self.click(locator)
        else:
            pass

# -------------------------------------------------------------------------------
    # History periods method
    # 抓取同彩種資料並比對
    # record_data expected '''list({dict})'''
    @logged
    def get_record(self, record_data):
        collect_list = []
        for index in range(len(record_data)):
            if record_data[index]["ticket_name"] == "极速快3":
                collect_list.append(record_data[index])
        
        return collect_list

    @logged
    def most_frequent(self, list):
        counter = 0
        num = list[0]

        for index in list:
            curr_frequency = list.count(index)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = index

        return num, counter

    @logged
    def get_periods(self, collect_list):
        periods_list = []
        for index in range(len(collect_list)):
            periods_list.append(collect_list[index]["ticket_period"])

        periods, counter = self.most_frequent(periods_list)
        
        return periods, counter

    def get_compare_lottery(self, collect_list, periods):
        spec_lottery_list = []
        for index in range(len(collect_list)):
            if collect_list[index]["ticket_period"] == periods:
                spec_lottery_list.append(collect_list[index])

        return spec_lottery_list

    @logged
    def search_table_data(self):
        table_game_list = []
        table_items_list = []
        table_amount_list = []
        all_record = []
        for element in (self.find_elements(RealTimeOrderLocator.table_of_classplay)):
            table_text = self.get_text_by_dom(element)
            table_game_list.append(table_text)
        for element in (self.find_elements(RealTimeOrderLocator.all_items)):
            table_text = self.get_text_by_dom(element)
            table_items_list.append(table_text)
        for element in (self.find_elements(RealTimeOrderLocator.all_amount)):
            table_text = self.get_text_by_dom(element)
            table_amount_list.append(table_text)

        assert len(table_game_list) == len(table_items_list), "Column not enough"
        assert len(table_game_list) == len(table_amount_list), "Column not enough"
        
        for index in range(len(table_game_list)):
            record = {
                "ticketName": table_game_list[index],
                "items": table_items_list[index],
                "amount": table_amount_list[index]
            }
            all_record.append(record)
        
        return all_record

    @logged
    def history_data_confirm(self, spec_lottery_list, inner_record, all_record):
        total_bets = 0
        total_money = 0
        for index in range(len(spec_lottery_list)):
            num = spec_lottery_list[index]["bets"]
            num = filter(str.isdigit, num)
            num = int(''.join(num))
            total_bets = total_bets + num
        
            money = spec_lottery_list[index]["money"]
            money = int(float(money))
            total_money = total_money + money
            
        record_bets = 0
        record_money = 0
        for index in range(len(all_record)):
            num = all_record[index]["items"]
            num = int(num)
            record_bets = record_bets + num

            money = all_record[index]["amount"]
            money = int(money)
            record_money = record_money + money

        assert total_bets == record_bets, f"total_bets:{total_bets} record_bets:{record_bets}"
        assert total_money == record_money, f"total_money:{total_money} record_money:{record_money}"

        inner_bets = 0
        inner_money = 0
        for index in range(len(inner_record)):
            num = inner_record[index]["bets"]
            num = int(num)
            inner_bets = inner_bets + num
            
            money = inner_record[index]["amount"]
            money = int(money)
            inner_money = inner_money + money

        assert inner_bets == record_bets, f"Inner_bets:{inner_bets} != record_bets:{record_bets}, Inner page bets wrong"
        assert inner_money == record_money, f"Inner_money:{inner_money} != record_money:{record_money}, Inner page amount wrong"

    @logged
    def inner_page(self):
        table_game_list = []
        table_items_list = []
        table_amount_list = []
        inner_record = []
        inner_table = (By.XPATH, "//tbody[@data-bind = 'foreach: items']//td[@data-bind='text: ratename']")
        inner_amount = (By.XPATH, "//tbody[@data-bind = 'foreach: items']//span[@data-bind='text: amount']")
        list = [inner_table, RealTimeOrderLocator.all_items, inner_amount]

        for index in list:
            for element in (self.find_elements(index)):
                if index == inner_table:
                    table_text = self.get_text_by_dom(element)
                    table_game_list.append(table_text)
                elif index == RealTimeOrderLocator.all_items:
                    table_text = self.get_text_by_dom(element)
                    table_items_list.append(table_text)
                elif index == inner_amount:
                    table_text = self.get_text_by_dom(element)
                    table_amount_list.append(table_text)
        
        assert len(table_game_list) == len(table_items_list), "inner page Column not enough"
        assert len(table_items_list) == len(table_amount_list), "inner page Column not enough"

        for index in range(len(table_game_list)):
            record = {
                "ticket_name": table_game_list[index],
                "bets": table_items_list[index],
                "amount": table_amount_list[index]
            }
            inner_record.append(record)
        
        return inner_record

# -------------------------------------------------------------------------------
    # history_period_action
    @logged
    def history_period_action(self, record_data):
        collect_list = self.get_record(record_data)
        periods, counter = self.get_periods(collect_list)
        spec_lottery_list = self.get_compare_lottery(collect_list, periods)

        self.select_by_text(RealTimeOrderLocator.type_of_product, "极速快3")
        assert self.is_element_finded(RealTimeOrderLocator.type_of_product) == True, "產品類型 can't find"
        self.select_by_index(RealTimeOrderLocator.type_of_pankou, 0)
        assert self.is_element_finded(RealTimeOrderLocator.type_of_pankou) == True, "盤口類型 can't find"
        self.select_by_text(RealTimeOrderLocator.class_of_play, "总表")
        assert self.is_element_finded(RealTimeOrderLocator.class_of_play) == True, "玩法類型 can't find"
        self.type(RealTimeOrderLocator.history_of_period, periods)
        self.click(RealTimeOrderLocator.btn_search)
        assert self.is_element_finded(RealTimeOrderLocator.btn_search) == True, "search button can't find"
        self.wait_loading_finish()

        all_record = self.search_table_data()

        inner_record = []
        inner_page_path = (By.XPATH, "//td[@class='text-left']/a")
        for index in range(len(self.find_elements(inner_page_path))):
            inner_page_path = (By.XPATH, f"(//td[@class='text-left']/a)[{index+1}]")
            self.click(inner_page_path)
            self.wait_loading_finish()
            inner_record.extend(self.inner_page())
            self.click(RealTimeOrderLocator.btn_return)
            self.wait_loading_finish()
        self.history_data_confirm(spec_lottery_list, inner_record, all_record)

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
    # Sort action
    @logged
    def sort_check_action(self, record_data):
        collect_list = self.get_record(record_data)
        periods, counter = self.get_periods(collect_list)
        self.select_by_text(RealTimeOrderLocator.type_of_product, "极速快3")
        assert self.is_element_finded(RealTimeOrderLocator.type_of_product) == True, "產品類型 can't find"
        self.select_by_index(RealTimeOrderLocator.type_of_pankou, 0)
        assert self.is_element_finded(RealTimeOrderLocator.type_of_pankou) == True, "盤口類型 can't find"
        self.select_by_text(RealTimeOrderLocator.class_of_play, "总表")
        assert self.is_element_finded(RealTimeOrderLocator.class_of_play) == True, "玩法類型 can't find"
        self.type(RealTimeOrderLocator.history_of_period, periods)
        self.click(RealTimeOrderLocator.btn_search)
        assert self.is_element_finded(RealTimeOrderLocator.btn_search) == True, "search button can't find"
        self.wait_loading_finish()

        # items asc action
        table_data_list = self.get_table_data()
        asc_sort_list = self.item_asc(table_data_list)
        self.click(RealTimeOrderLocator.items_sort)
        assert self.is_element_finded(RealTimeOrderLocator.items_sort) == True, "items sort button can't find"
        assert self.is_element_finded(RealTimeOrderLocator.items_asc) == True, "items asc sort can't find"
        assert self.is_element_finded(RealTimeOrderLocator.items_desc) == False, "items desc sort should not be found"
        self.wait_loading_finish()
        after_asc_sort_list = self.get_table_data()
        for index in range(len(asc_sort_list)):
            assert asc_sort_list[index]["items"] == after_asc_sort_list[index]["items"], "items ASC Sorting Error"
        # items desc action
        desc_sort_list = self.item_desc(asc_sort_list)
        self.click(RealTimeOrderLocator.items_asc)
        assert self.is_element_finded(RealTimeOrderLocator.items_desc) == True, "items desc sort can't find"
        after_desc_sort_list = self.get_table_data()
        for index in range(len(desc_sort_list)):
            assert desc_sort_list[index]["items"] == after_desc_sort_list[index]["items"], "items DESC Sorting Error"
        # 為了之後的twoface資料先行紀錄 659行
        record_twoface = copy.deepcopy(after_desc_sort_list[0])
        # return to standard action
        self.click(RealTimeOrderLocator.items_desc)
        # amount asc action
        table_data_list = self.get_table_data()
        asc_sort_list = self.amount_asc(table_data_list)
        self.click(RealTimeOrderLocator.amount_sort)
        assert self.is_element_finded(RealTimeOrderLocator.amount_sort) == True, "amount sort button can't find"
        assert self.is_element_finded(RealTimeOrderLocator.amount_asc) == True, "amount asc sort can't find"
        assert self.is_element_finded(RealTimeOrderLocator.amount_desc) == False, "amount desc sort should not be found"
        self.wait_loading_finish()
        after_asc_sort_list = self.get_table_data()
        for index in range(len(asc_sort_list)):
            assert asc_sort_list[index]["amount"] == after_asc_sort_list[index]["amount"], "amount ASC Sorting Error"
        # amount desc action
        desc_sort_list = self.amount_desc(asc_sort_list)
        self.click(RealTimeOrderLocator.amount_asc)
        assert self.is_element_finded(RealTimeOrderLocator.amount_desc) == True, "amount desc sort can't find"
        after_desc_sort_list = self.get_table_data()
        for index in range(len(desc_sort_list)):
            assert desc_sort_list[index]["amount"] == after_desc_sort_list[index]["amount"], "amount DESC Sorting Error"
        # return to standard action
        self.click(RealTimeOrderLocator.amount_desc)
        # click into twoface last inner page action
        self.sleep(1)
        self.click(RealTimeOrderLocator.items_sort)
        self.sleep(1)
        self.click(RealTimeOrderLocator.items_asc)
        assert self.is_element_finded(RealTimeOrderLocator.items_desc) == True, "items desc sort can't find"
        self.sleep(1)
        inner_path = (By.XPATH, "(//a[contains(@data-bind,'playname')])[1]")
        self.click(inner_path)
        inner_page_record = self.inner_page_data()
        inner_page_item, inner_page_amount = self.inner_page_check(inner_page_record)
        outside_page_item = int(record_twoface["items"])
        outside_page_amount = int(record_twoface["amount"])
        assert outside_page_item == inner_page_item, "outside page not equal inner page (items)"
        assert outside_page_amount == inner_page_amount, "outside page not equal inner page (amount)"
        # inner page asc desc action
        inner_table_data_list = self.inner_page_data()
        inner_asc_sort_list = self.item_asc(inner_table_data_list)
        self.click(RealTimeOrderLocator.items_sort)
        assert self.is_element_finded(RealTimeOrderLocator.items_sort) == True, "Inner items sort button can't find"
        assert self.is_element_finded(RealTimeOrderLocator.items_asc) == True, "Inner items asc sort can't find"
        assert self.is_element_finded(RealTimeOrderLocator.items_desc) == False, "Inner items desc sort should not be found"
        self.wait_loading_finish()
        inner_after_asc_sort_list = self.inner_page_data()
        for index in range(len(inner_after_asc_sort_list)):
            assert inner_asc_sort_list[index]["items"] == inner_after_asc_sort_list[index]["items"], "Inner items ASC Sorting Error"
        # inner items desc action
        inner_desc_sort_list = self.item_desc(inner_asc_sort_list)
        self.click(RealTimeOrderLocator.items_asc)
        assert self.is_element_finded(RealTimeOrderLocator.items_desc) == True, "Inner items desc sort can't find"
        self.sleep(1)
        inner_after_desc_sort_list = self.inner_page_data()
        for index in range(len(inner_after_desc_sort_list)):
            assert inner_desc_sort_list[index]["items"] == inner_after_desc_sort_list[index]["items"], "Inner items DESC Sorting Error"
        # return to standard action
        self.click(RealTimeOrderLocator.items_desc)
        # inner amount asc action
        self.sleep(1)
        inner_page_record = self.inner_page_data()
        inner_asc_sort_list = self.amount_asc(inner_page_record)
        self.click(RealTimeOrderLocator.amount_sort)
        assert self.is_element_finded(RealTimeOrderLocator.amount_sort) == True, "Inner amount sort button can't find"
        assert self.is_element_finded(RealTimeOrderLocator.amount_asc) == True, "Inner amount asc sort can't find"
        assert self.is_element_finded(RealTimeOrderLocator.amount_desc) == False, "Inner amount desc sort should not be found"
        self.wait_loading_finish()
        self.sleep(1)
        inner_after_asc_sort_list = self.inner_page_data()
        for index in range(len(inner_asc_sort_list)):
            assert inner_asc_sort_list[index]["amount"] == inner_after_asc_sort_list[index]["amount"], "Inner amount ASC Sorting Error"
        # amount desc action
        inner_desc_sort_list = self.amount_desc(inner_desc_sort_list)
        self.click(RealTimeOrderLocator.amount_asc)
        assert self.is_element_finded(RealTimeOrderLocator.amount_desc) == True, "Inner amount desc sort can't find"
        self.sleep(1)
        after_desc_sort_list = self.inner_page_data()
        for index in range(len(inner_desc_sort_list)):
            assert inner_desc_sort_list[index]["amount"] == after_desc_sort_list[index]["amount"], "Inner amount DESC Sorting Error"

# -------------------------------------------------------------------------------
    @logged
    def get_table_data(self):
        table_game_list = []
        table_items_list = []
        table_amount_list = []
        temp_list = []
        self.sleep(1)
        assert self.is_element_finded(RealTimeOrderLocator.table_of_classplay), "table_of_classplay locator is not found"
        for element in (self.find_elements(RealTimeOrderLocator.table_of_classplay)):
            table_text = self.get_text_by_dom(element)
            table_game_list.append(table_text)
        assert self.is_element_finded(RealTimeOrderLocator.all_items), "all_items locator is not found"
        for element in (self.find_elements(RealTimeOrderLocator.all_items)):
            table_text = self.get_text_by_dom(element)
            table_items_list.append(table_text)
        assert self.is_element_finded(RealTimeOrderLocator.all_amount), "all_amount locator is not found"
        for element in (self.find_elements(RealTimeOrderLocator.all_amount)):
            table_text = self.get_text_by_dom(element)
            table_amount_list.append(table_text)

        for index in range(len(table_game_list)):
            basic_Record = {
                "ticket_name": table_game_list[index],
                "items": table_items_list[index],
                "amount": table_amount_list[index]
            }
            temp_list.append(basic_Record)
        return temp_list

    # for sort method "items" use
    @logged
    def take_items_data(self, unsort_list):
        return unsort_list["items"]

    @logged
    def item_asc(self, temp_list):
        temp_list.sort(key = self.take_items_data)
        return temp_list

    @logged
    def item_desc(self, temp_list):
        temp_list.sort(key=self.take_items_data, reverse=True)
        return temp_list

    # for sort method "amount" use
    @logged
    def take_amount_data(self, unsort_list):
        return unsort_list["amount"]

    @logged
    def amount_asc(self, temp_list):
        temp_list.sort(key=self.take_amount_data)
        return temp_list
    
    @logged
    def amount_desc(self, temp_list):
        temp_list.sort(key=self.take_amount_data, reverse=True)
        return temp_list

    # 最內層即時注單(table)使用
    @logged
    def inner_page_data(self):
        class_name_path = (By.XPATH, "//td[contains(@data-bind,'text: ratename')]")
        all_amount_path = (By.XPATH, "//tbody[@data-bind = 'foreach: items']//span[@data-bind='text: amount']")
        table_name_list = []
        item_list = []
        amount_list = []
        all_record = []

        for element in (self.find_elements(class_name_path)):
            self.sleep(1)
            table_text = self.get_text_by_dom(element)
            table_text = re.split('\n', table_text)
            table_name_list.append(table_text[0])

        for element in (self.find_elements(RealTimeOrderLocator.all_items)):
            self.sleep(1)
            table_text = self.get_text_by_dom(element)
            table_text = re.split('\n', table_text)
            item_list.append(table_text[0])

        for element in (self.find_elements(all_amount_path)):
            self.sleep(1)
            table_text = self.get_text_by_dom(element)
            table_text = re.split('\n', table_text)
            amount_list.append(table_text[0])

        # assert len(table_name_list) == 4, "this table gamename shouldn't over 4 column"
        # assert len(item_list) == 4, "this table items shouldn't over 4 column"
        # assert len(amount_list) == 4, "this table amount shouldn't over 4 column"
        assert len(table_name_list) == len(item_list), "data list not equal"
        assert len(item_list) == len(amount_list), "data list not equal"

        for index in range(len(table_name_list)):
            record = {
                "gamename": table_name_list[index],
                "items": item_list[index],
                "amount": amount_list[index]
            }
            all_record.append(record)

        return all_record

    @logged
    def inner_page_check(self, inner_page_record):
        total_items_sum = 0
        total_amount_sum = 0
        for index in inner_page_record:
            items = index["items"]
            amount = index["amount"]
            total_items_sum += int(items)
            total_amount_sum += int(amount)

        return total_items_sum, total_amount_sum