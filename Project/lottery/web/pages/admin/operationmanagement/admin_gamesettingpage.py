from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import datetime
class GameSettingPageLocator:
    #### 維運管理 -> *彩票 -> 遊戲設置
    radio_off = (By.XPATH,"//div[@class='col-md-12']//label[@class='radio-inline']/..//*[contains(.,'禁用')]") # 禁用
    radio_on = (By.XPATH,"//div[@class='col-md-12']//label[@class='radio-inline']/..//*[contains(.,'启用')]") # 啟用
    radio_auto = (By.XPATH,"//div[@class='col-md-12']//label[@class='radio-inline']/..//*[contains(.,'自动维护')]") # 自動維護
    auto_maintenance_time = (By.XPATH, "//input[contains(@data-bind, 'start')]") # 自動維護時間
    save_btn = (By.XPATH,"//button[@type='button' and text()='保存']") # 保存
    # 彩票
    # ------------------------------------------------------------- web 狀態 -------------------------------------------------------------
    web_status_radio_open = (By.XPATH, '//label[contains(text(), "web状态")]/..//label[contains(., "启用")]')
    web_status_radio_close = (By.XPATH, '//label[contains(text(), "web状态")]/..//label[contains(., "禁用")]')
    web_status_radio_auto_maintenance = (By.XPATH, '//label[contains(text(), "web状态")]/..//label[contains(., "自动维护")]')
    web_close_announcment = (By.XPATH, '//body[contains(@class, "cke_editable cke_editable_themed")]')
    # ------------------------------------------------------------- APP 狀態 -------------------------------------------------------------
    app_status_radio_open = (By.XPATH, '//label[contains(text(), "APP状态")]/..//label[contains(., "启用")]')
    app_status_radio_close = (By.XPATH, '//label[contains(text(), "APP状态")]/..//label[contains(., "禁用")]')
    app_status_radio_auto_maintenance = (By.XPATH, '//label[contains(text(), "APP状态")]/..//label[contains(., "自动维护")]')
    # ------------------------------------------------------------- 開盤操作 -------------------------------------------------------------
    opening_operation_radio_auto = (By.XPATH, '//label[contains(text(), "开盘操作")]/..//label[contains(., "自动")]')
    opening_operation_radio_manual = (By.XPATH, '//label[contains(text(), "开盘操作")]/..//label[contains(., "手动")]')
    # ------------------------------------------------------------- 結算動作 -------------------------------------------------------------
    settlement_operation_radio_auto = (By.XPATH, '//label[contains(text(), "结算动作")]/..//label[contains(., "自动")]')
    settlement_operation_radio_manual = (By.XPATH, '//label[contains(text(), "结算动作")]/..//label[contains(., "手动")]')

    # 封盤時間
    input_box_closing_time = (By.XPATH, '//input[contains(@data-bind, "close")]')
    # 開盤時間
    input_box_opening_time = (By.XPATH, '//input[contains(@data-bind, "open")]')
    # 未開提醒
    input_box_remind_unopened = (By.XPATH, '//input[contains(@data-bind, "nodrawingtime")]')
    # 未派提醒
    input_box_remind_unpaid = (By.XPATH, '//input[contains(@data-bind, "nopayouttime")]')
    # 保存
    button_save = (By.XPATH, '//button[contains(text(), "保存")]')
    # 返回
    button_cancel = (By.XPATH, '//button[contains(text(), "返回")]')


class GameSettingPage(BasePage):

    def web_radio_on_off(self, is_maintenance):
        self.wait_loading_finish()

        if is_maintenance == True :
            for radio in self.find_elements(GameSettingPageLocator.radio_off):
                self.click_by_dom(radio)
        else:
            for radio in self.find_elements(GameSettingPageLocator.radio_on):
                self.click_by_dom(radio)

        self.sleep(1)
        self.click(GameSettingPageLocator.save_btn)
        self.scroll_to_top()
        self.sleep(10)
        self.wait_loading_finish()

    def is_radio_box_selected(self, locator):
        return self.is_element_finded((locator[0], locator[1] + '/input[contains(@checked, "checked")]'))
    
    def auto_maintain_on_off(self, is_opened = False):
        '''
            根據 is_opened 來判斷是否要切換為自動維護，自動維護時間設定為 現在時間減一小時
        '''
        self.refresh_browser()
        self.wait_loading_finish()

        maintenance_time = (self.get_us_time() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:00")

        if is_opened:
            for radio, time in zip(self.find_elements(GameSettingPageLocator.radio_auto), self.find_elements(GameSettingPageLocator.auto_maintenance_time)):
                self.click_by_dom(radio)
                self.type_by_dom(time, maintenance_time)
                # self.switch_frame(0)
                # self.type(GameSettingPageLocator.web_close_announcment, 'aaaaaa')
                # self.switch_default_frame()
        else:
            for radio in self.find_elements(GameSettingPageLocator.radio_on):
                self.click_by_dom(radio)

        self.click(GameSettingPageLocator.save_btn)

    def check_maintain_on_off(self, is_opened):
        '''
            檢查後台的 web app 維護狀態
        '''
        for _ in range(10):
            self.refresh_browser()
            self.wait_loading_finish()

            if is_opened:
                err = AssertionError(f'遊戲設置 -> web 及 app 維護狀態應為 啟用')
                if self.is_radio_box_selected(GameSettingPageLocator.web_status_radio_open) and \
                    self.is_radio_box_selected(GameSettingPageLocator.app_status_radio_open):
                    return
            else:
                err = AssertionError(f'遊戲設置 -> web 及 app 維護狀態應為 禁用')
                if self.is_radio_box_selected(GameSettingPageLocator.web_status_radio_close) and \
                    self.is_radio_box_selected(GameSettingPageLocator.app_status_radio_auto_maintenance):
                    return
            
            self.sleep(1)

        raise err

    def opening_operation_setting(self, is_auto=False, opening_time=600, seal_time=600):
        '''
            切換 開盤操作 及 封盤、開盤時間
        '''
        self.refresh_browser()
        self.wait_loading_finish()

        if is_auto:
            self.click(GameSettingPageLocator.opening_operation_radio_manual)
            self.type(GameSettingPageLocator.input_box_opening_time, str(opening_time))
            self.type(GameSettingPageLocator.input_box_closing_time, str(seal_time))
        else:
            self.click(GameSettingPageLocator.opening_operation_radio_auto)

        self.click(GameSettingPageLocator.save_btn)
        try:
            self.click(GameSettingPageLocator.save_btn)
        except:
            pass

    def check_opening_operation_setting(self, is_auto, opening_time, seal_time):
        '''
            檢查 開盤操作 及 封盤、開盤時間
        '''
        # 若 10 秒內 開盤操作 未正確切換，則 raise exception
        for _ in range(10):
            self.refresh_browser()
            self.wait_loading_finish()

            if is_auto:
                err = AssertionError(f'開盤操作 應為 自動')
                if self.is_radio_box_selected(GameSettingPageLocator.opening_operation_radio_auto):
                    return
            else:
                err = AssertionError(f'開盤操作 狀態或設定時間錯誤')
                if self.is_radio_box_selected(GameSettingPageLocator.opening_operation_radio_manual) and \
                    int(self.get_attribute(GameSettingPageLocator.input_box_opening_time, 'value')) == opening_time and \
                    int(self.get_attribute(GameSettingPageLocator.input_box_closing_time, 'value')) == seal_time:
                    return
            
            self.sleep(1)
        
        raise err

    def settlement_operation_setting(self, is_auto=False, remind_unopened=600, remind_unpaid=600):
        '''
            切換 結算動作 及 未開、未派提醒
        '''
        self.refresh_browser()
        self.wait_loading_finish()

        if is_auto:
            self.click(GameSettingPageLocator.settlement_operation_radio_manual)
            self.type(GameSettingPageLocator.input_box_remind_unopened, str(remind_unopened))
            self.type(GameSettingPageLocator.input_box_remind_unpaid, str(remind_unpaid))
        else:
            self.click(GameSettingPageLocator.settlement_operation_radio_auto)

        self.click(GameSettingPageLocator.save_btn)
        try:
            self.click(GameSettingPageLocator.save_btn)
        except:
            pass

    def check_settlement_operation_setting(self, is_auto, remind_unopened, remind_unpaid):
        '''
            檢查 結算動作 及 未開、未派提醒
        '''
        for _ in range(10):
            self.refresh_browser()
            self.wait_loading_finish()

            if is_auto:
                err = AssertionError(f'結算動作 應為 自動')
                if self.is_radio_box_selected(GameSettingPageLocator.settlement_operation_radio_auto):
                    return
            else:
                err = AssertionError(f'結算動作 狀態或設定時間錯誤')
                if self.is_radio_box_selected(GameSettingPageLocator.settlement_operation_radio_manual) and \
                    int(self.get_attribute(GameSettingPageLocator.input_box_remind_unopened, 'value')) == remind_unopened and \
                    int(self.get_attribute(GameSettingPageLocator.input_box_remind_unpaid, 'value')) == remind_unpaid:
                    return
            
            self.sleep(1)

        raise err
