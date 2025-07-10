from time import sleep

from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage
import os,random, re, datetime


class IntegralPageLocator:
    #通用
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')
    header_back = (By.XPATH, "(//div[@class='header-close']/div)[last()]")
    header_title = (By.XPATH, "(//div[@class='header-title'])[last()]")
    header_text = (By.XPATH, "//span[@class='chat-setting-head__head-title__text']")
    confirm_btn = (By.XPATH, "(//div[(@class='btn-group') and not(contains(@style,'none'))]//button[2])[last()]")
    security_password = (By.XPATH, '(//input[@placeholder="000000"])[last()]')
    remind_text = (By.XPATH, '(//p[@class="common-info__text"])[last()]')
    point_balance = (By.XPATH, '//p[@class="point-board-group__subtitle"][last()]')
    
    #積分頁
    integral_page = (By.XPATH, '//p[text()="积分"]')
    integral_amount = (By.XPATH,"//p[@class='point-board-group__title']")
    exchange_integral = (By.XPATH, "//li[@class='point-record__item'][1]//p[@class='point-record__point__text']")
    exchange_source = (By.XPATH, "//li[@class='point-record__item'][1]//p[@class='point-record__name__text']")
    exchange_state = (By.XPATH ,"//li[@class='point-record__item'][1]//p[@class='point-record__status__text']")
    exchange_time =(By.XPATH ,"//li[@class='point-record__item'][1]//span[@class='point-record-time__time']")
    exchange_btn = (By.XPATH, '//p[text()="兑换"]')
    
    #兌換頁(選擇順付或平台)
    exchange_wellpay = (By.XPATH, '//ul[@class="ui-tableviewcell-list"]//p[text()="顺付 积分兑换"]')
    exchange_platform = (By.XPATH, '//ul[@class="ui-tableviewcell-list"]//p[text()="平台 积分兑换"]')
    exchange_wellpay_state = (By.XPATH, '//li[@class = "ui-tableviewcell -click"][1]//p[@class = "ui-tableviewcell__num"]')
    exchange_platform_state = (By.XPATH, '//li[@class = "ui-tableviewcell -click"][2]//p[@class = "ui-tableviewcell__num"]')
    
    #兌換頁(綁定)
    wallet_name = (By.XPATH, '//p[text() = "钱包名称"]')
    wallet_address_text = (By.XPATH, '//p[text() = "钱包地址"]')
    wallet_address = (By.XPATH, '//input[@placeholder="请输入钱包地址"]')
    exchange_address = (By.XPATH, '//input[@placeholder="请输入兑换地址"]')
    exchange_next_btn = (By.XPATH, "//*[text() = '下一步']")
    exchange_confirm_btn = (By.XPATH, "//*[text() = '兑换']")
    first_exchange_note_confirm_btn = (By.XPATH, "//*[text() = '确定']")
    submit_confirm_btn = (By.XPATH, '//p[text() = "确定"]')

    brand_exchange_text = (By.XPATH, "//p[text()='平台 积分兑换']/..//p[@class='ui-tableviewcell__num']")
    back_btn = (By.XPATH, '//div[@class="header-back"]')

    #順付兌換
    wellpay_exchange_amount = (By.XPATH, '//p[text() = "兑换金额"]')
    exchange_amount = (By.XPATH, '//input[@placeholder="请输入兑换金额"][last()]')
    wellpay_point = (By.XPATH, '//p[@class="point-board-group__subtitle"]')

    exchange_remind_btn = (By.XPATH, "(//div[(@class='btn-group') and not(contains(@style,'none'))]//button)[last()]")
    

class IntegralPage(BasePage):
    
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(IntegralPageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(IntegralPageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")
    
    def entry_exchange_page(self):
        if self.is_element_finded(IntegralPageLocator.exchange_btn) == True:
            self.click(IntegralPageLocator.exchange_btn)
            self.wait_loading_finish() 
            assert self.get_text(IntegralPageLocator.header_title) == '兑换', f'進入兌換頁面失敗'

    # 積分詳情頁積分確認
    def exchange_record_check(self, operate_amount, operate_type, operate_time, remain_integral_amount_before):
        self.wait_loading_finish()
        exchange_integral = self.get_text(IntegralPageLocator.exchange_integral)
        after_remove_sign_amount = re.sub(r'[+-]', '', exchange_integral)  # 移除數字前+-號
        assert after_remove_sign_amount == f"{operate_amount}", f'積分有誤'
        assert self.get_text(IntegralPageLocator.exchange_source) == operate_type, f'媒介有誤, 預期: {operate_type}, 實際: {self.get_text(IntegralPageLocator.exchange_source)}'
        assert self.get_text(IntegralPageLocator.exchange_state) == '成功', f'存入/提出狀態有誤'
        if operate_time is not None:
            assert self.get_text(IntegralPageLocator.exchange_time) == operate_time, f'存入/提出日期有誤'
        current_total_integral_amount = self.get_text(IntegralPageLocator.integral_amount)
        assert round(float(remain_integral_amount_before) + float(exchange_integral), 2) == round(float(current_total_integral_amount), 2), f'總積分有誤, 前{remain_integral_amount_before}+後{exchange_integral}=預期{current_total_integral_amount}'
        return current_total_integral_amount  # return 目前總積分

    #綁定順付帳號
    def bind_wellpay(self, wellpay_address, security_code):
        self.sleep(1)
        self.click(IntegralPageLocator.exchange_wellpay)
        self.wait_loading_finish()
        assert self.get_text(IntegralPageLocator.wallet_name) == '钱包名称',  f'進入綁定頁失敗'
        self.type_delete(IntegralPageLocator.wallet_address)
        self.type(IntegralPageLocator.wallet_address, wellpay_address)
        self.type_delete(IntegralPageLocator.security_password)
        self.type(IntegralPageLocator.security_password, security_code)
        self.click(IntegralPageLocator.confirm_btn)
        self.wait_loading_finish()
        self.click(IntegralPageLocator.confirm_btn)
        self.wait_loading_finish()
        assert self.get_text(IntegralPageLocator.header_title) == '顺付 积分兑换', f'綁定後跳轉失敗'

    # 順付積分兌換 核對資料(前端web)
    def wellpay_exchange(self, security_code, exchange_amount):
        self.sleep(1)
        # self.click(IntegralPageLocator.exchange_wellpay)
        # self.wait_loading_finish()
        if self.get_text(IntegralPageLocator.wellpay_exchange_amount) == '兑换金额':
            before_point = self.get_text(IntegralPageLocator.point_balance)
            self.type_delete(IntegralPageLocator.exchange_amount)
            self.type(IntegralPageLocator.exchange_amount, exchange_amount)
            self.type_delete(IntegralPageLocator.security_password)
            self.type(IntegralPageLocator.security_password, security_code)
            self.click(IntegralPageLocator.confirm_btn)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            self.wait_loading_finish()
            self.click(IntegralPageLocator.exchange_remind_btn)       
        self.wait_loading_finish()
        self.click(IntegralPageLocator.integral_page)
        self.wait_login_finish()
        after_point = str(float(before_point) - exchange_amount)
        assert self.get_text(IntegralPageLocator.exchange_integral) == '-1', f'積分有誤, 預期{-1},實際{self.get_text(IntegralPageLocator.exchange_integral)}'
        assert self.get_text(IntegralPageLocator.exchange_source) == '顺付出金', f'媒介有誤'
        assert self.get_text(IntegralPageLocator.exchange_state) == '成功', f'轉換狀態有誤'
        assert self.get_text(IntegralPageLocator.exchange_time) == time, f'日期有誤'
        assert self.get_text(IntegralPageLocator.integral_amount) == after_point, f'總積分有誤'

    #順付錯誤 文字測試
    def wellpay_exchange_incorrect(self, security_code, exchange_amount):
        self.sleep(1)
        if self.get_text(IntegralPageLocator.wellpay_exchange_amount) == '兑换金额':
            before_point = self.get_text(IntegralPageLocator.point_balance)
            self.type_delete(IntegralPageLocator.exchange_amount)
            self.type(IntegralPageLocator.exchange_amount, exchange_amount)
            self.type_delete(IntegralPageLocator.security_password)
            self.type(IntegralPageLocator.security_password, security_code)
            self.click(IntegralPageLocator.confirm_btn)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            self.wait_loading_finish()
            self.click(IntegralPageLocator.exchange_remind_btn)       
        self.wait_loading_finish()
        self.click(IntegralPageLocator.integral_page)
        self.wait_login_finish()
        assert self.get_text(IntegralPageLocator.exchange_integral) == f'+{exchange_amount}', '積分有誤'
        assert self.get_text(IntegralPageLocator.exchange_source) == '顺付返还', f'媒介有誤'
        assert self.get_text(IntegralPageLocator.exchange_state) == '成功', f'轉換狀態有誤'
        assert self.get_text(IntegralPageLocator.exchange_time) == time, f'日期有誤, 預期{time},實際{self.get_text(IntegralPageLocator.exchange_time)}'
        assert self.get_text(IntegralPageLocator.integral_amount) == before_point, f'總積分有誤'

    def bind_brand_and_exchange(self, exchange_address, security_code):
        self.sleep(1)
        self.click(IntegralPageLocator.exchange_platform)
        self.type(IntegralPageLocator.exchange_address, exchange_address)
        self.click(IntegralPageLocator.exchange_next_btn)
        sleep(1)
        self.type(IntegralPageLocator.security_password, security_code)
        self.click(IntegralPageLocator.exchange_confirm_btn)
        if self.is_element_finded(IntegralPageLocator.first_exchange_note_confirm_btn):
            self.click(IntegralPageLocator.first_exchange_note_confirm_btn)
        self.wait_visibility(IntegralPageLocator.submit_confirm_btn)
        self.click(IntegralPageLocator.submit_confirm_btn)
        self.click(IntegralPageLocator.integral_page)
        self.entry_exchange_page()
        assert self.get_text(IntegralPageLocator.brand_exchange_text) == '已绑定', f'平台未綁定成功'
        if self.is_element_finded(IntegralPageLocator.back_btn):
            self.click(IntegralPageLocator.back_btn)
        if self.is_element_finded(IntegralPageLocator.header_back):
            self.click(IntegralPageLocator.header_back)




