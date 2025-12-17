from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
# import datetime
from Project.chat.web.pages.admin.admin_basepage import BasePage


class WaterControlPageLocator:
    # 通用
    page_title = (By.XPATH, '//div[@class="page-title"]')
    search_btn = (By.XPATH, "//span[text()='搜寻']")
    close_btn = (By.XPATH ,"//span[text()='关闭']")

    # 搜尋欄位
    member_ID = (By.XPATH, '//label[text()="存入ID"]/..//input[@placeholder="请输入"]')
    member_name = (By.XPATH, '//label[text()="存入帐号名称"]/..//input[@placeholder="请输入"]')

    search_start_time = (By.XPATH, '//input[@placeholder="开始日期"]')
    search_end_time = (By.XPATH, '//input[@placeholder="结束日期"]')

    # 資料欄位
    data_member_ID = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[1]")
    data_member_name = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[2]")
    data_point = (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[3]")
    data_time= (By.XPATH, "//table[@class='el-table__body']//tr[1]/td[4]")

    # 水量編輯 / 詳情
    data_detail_title = (By.XPATH, "(//span[@class='el-dialog__title'])[3]")
    data_edit_title = (By.XPATH, "(//span[@class='el-dialog__title'])[2]")

    data_detail_original_water = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[1])[last()]")
    data_detail_after_water = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[2])[last()]")
    data_detail_operate = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[3])[last()]")
    data_detail_time = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[4])[last()]")
    data_detail_operate_ID = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[5])[last()]")
    data_detail_operate_name = (By.XPATH, "(//table[@class='el-table__body']//tr[1]/td[6])[last()]")

    data_edit_original_water = (By.XPATH, "//label[text()='原水量']/..//span")
    data_edit_water_control = (By.XPATH, "//label[text()='水量编辑']/..//input")

    data_detail_save_btn = (By.XPATH, "//span[text()='储存']")
    data_detail_btn = (By.XPATH, "//table[@class='el-table__body']//tr[1]//span[text()=' 详情']")
    data_waterControl_btn = (By.XPATH, "//table[@class='el-table__body']//tr[1]//span[text()='水量编辑']")

    data_total_line = (By.XPATH, "//span[@class='el-pagination__total']")
    

class WaterControlPage(BasePage):
    def test_point_control_search(self, member_name):
        self.wait_loading_finish()
        assert self.get_text(WaterControlPageLocator.page_title) == '水量控制' , f'頁面標題有誤'
        self.type(WaterControlPageLocator.member_name, member_name)
        time = datetime.now().strftime("%Y-%m-%d")
        self.click(WaterControlPageLocator.search_start_time)
        self.type(WaterControlPageLocator.search_start_time, time)
        self.click(WaterControlPageLocator.search_end_time)
        self.type(WaterControlPageLocator.search_end_time, time)
        self.click(WaterControlPageLocator.search_btn)
        
    def test_point_control(self, member_name, original_water, set_water):
        self.wait_loading_finish()
        assert self.get_text(WaterControlPageLocator.data_member_name) == member_name, f'水量控制成員暱稱有誤'
        self.click(WaterControlPageLocator.data_waterControl_btn)
        self.wait_loading_finish()
        assert self.get_text(WaterControlPageLocator.data_edit_title) == '水量编辑', f'標題有誤'
        assert self.get_text(WaterControlPageLocator.data_edit_original_water) == original_water, f'原水量有誤'
        self.type(WaterControlPageLocator.data_edit_water_control, set_water)
        self.click(WaterControlPageLocator.data_detail_save_btn)

    def test_water_control_detail(self, operate_time, member_name, original_water, total_cost, after_water):
        self.wait_loading_finish()

        list_account_name = self.get_text(WaterControlPageLocator.data_member_name)
        assert list_account_name == member_name, f'搜尋結果有誤'  # 確認水量控制頁搜尋結果
        self.click(WaterControlPageLocator.data_detail_btn)
        self.wait_loading_finish()

        # ========================== 帳號水量詳情彈窗 ==========================
        DetailPageTitle = self.get_text(WaterControlPageLocator.data_detail_title)  # 彈窗標題
        listOriginalRemainWater = self.get_text(WaterControlPageLocator.data_detail_original_water)  # 原剩餘水量
        listAfterRemainWater = self.get_text(WaterControlPageLocator.data_detail_after_water)  # 水量餘額
        listOperateDetail = self.get_text(WaterControlPageLocator.data_detail_operate)  # 操作內容
        listOperateTime = self.get_text(WaterControlPageLocator.data_detail_time)[:-3]  # 操作時間
        listOperateID = self.get_text(WaterControlPageLocator.data_detail_operate_ID)  # 操作ID
        listOperateNickname = self.get_text(WaterControlPageLocator.data_detail_operate_name)  # 操作名稱
        # ========================== 確認資料 ==========================
        assert DetailPageTitle == member_name, f'帳號水量詳情彈窗標題有誤'
        assert listOriginalRemainWater == original_water, f'帳號原剩餘水量有誤'
        assert listAfterRemainWater == after_water, f'帳號使用積分後水量餘額有誤'
        assert listOperateDetail == f'发拼手气红包: -{total_cost}', f'操作內容有誤'

        # 轉成 datetime 物件
        t1 = datetime.strptime(listOperateTime, "%Y/%m/%d %H:%M")
        t2 = datetime.strptime(operate_time, "%Y/%m/%d %H:%M")
        # 判斷是否相等 或 t2 +- 1分鐘相等
        assert t1 == t2 or t1 == t2 + timedelta(minutes=1) or t1 == t2 - timedelta(minutes=1), f'操作時間有誤'

        assert listOperateID == member_name, f'操作ID有誤'
        assert listOperateNickname == member_name, f'操作名稱有誤'

    def edit_point(self, user_id, set_water):
        self.wait_loading_finish()
        self.type(WaterControlPageLocator.member_name, user_id)
        self.click(WaterControlPageLocator.search_btn)
        self.wait_loading_finish()
        self.click(WaterControlPageLocator.data_waterControl_btn)
        self.wait_loading_finish()
        self.type(WaterControlPageLocator.data_edit_water_control, set_water)
        self.click(WaterControlPageLocator.data_detail_save_btn)
        return datetime.now().strftime("%Y/%m/%d %H:%M")

