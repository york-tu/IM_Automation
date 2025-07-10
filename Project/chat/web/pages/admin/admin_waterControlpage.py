from time import sleep

from selenium.webdriver.common.by import By
import datetime
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
        time = datetime.datetime.now().strftime("%Y-%m-%d")
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
        assert self.get_text(WaterControlPageLocator.data_member_name) == member_name, f'暱稱有誤'
        self.click(WaterControlPageLocator.data_detail_btn)
        self.wait_loading_finish()
        assert self.get_text(WaterControlPageLocator.data_detail_title) == member_name, f'標題有誤'
        assert self.get_text(WaterControlPageLocator.data_detail_original_water) == original_water, f'原水量有誤, 預期:{original_water}, 實際:{self.get_text(WaterControlPageLocator.data_detail_original_water)}'
        assert self.get_text(WaterControlPageLocator.data_detail_after_water) == after_water, f'水量餘額有誤'
        assert self.get_text(WaterControlPageLocator.data_detail_operate) == f'发拼手气红包: -{total_cost}', f'操作內容有誤,預期-{total_cost},實際{self.get_text(WaterControlPageLocator.data_detail_operate)}'
        actual_time = self.get_text(WaterControlPageLocator.data_detail_time)[:-3].replace("/", "-")
        assert actual_time == operate_time.replace("/", "-"), f'操作時間有誤, 預期: {operate_time.replace("/", "-")}, 實際: {actual_time}'
        assert self.get_text(WaterControlPageLocator.data_detail_operate_ID) == member_name, f'操作ID有誤'
        assert self.get_text(WaterControlPageLocator.data_detail_operate_name) == member_name, f'操作名稱有誤'

    def edit_point(self, user_id, set_water):
        self.wait_loading_finish()
        self.type(WaterControlPageLocator.member_name, user_id)
        self.click(WaterControlPageLocator.search_btn)
        self.wait_loading_finish()
        self.click(WaterControlPageLocator.data_waterControl_btn)
        self.wait_loading_finish()
        self.type(WaterControlPageLocator.data_edit_water_control, set_water)
        self.click(WaterControlPageLocator.data_detail_save_btn)

