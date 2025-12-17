from selenium.webdriver.common.by import By
import pandas as pd
from Project.exchange_wellpay.app.pages.admin.admin_base_page import BasePage
from common.web.common import Common

class MenuPageLocator:

    button_menu = (By.XPATH, "//div[@class='hamburger-container hamburger-container']")
    svg_menu_opening = (By.XPATH, "//*[local-name()='svg' and @class='hamburger is-activea']")
    svg_menu_closed = (By.XPATH, "//*[local-name()='svg' and @class='hamburger']")

    #### 充值管理 ####
    recharge_management = (By.XPATH, "//div[@class='el-submenu__title']//span[text()='充值管理 ']")
    bank = (By.XPATH, "//div[@class='test nest-menu']//span[text()='银行 ']")
    recharge_audit = (By.XPATH, "//div[@class='test nest-menu']//span[text()='充值审核 ']")

    check_bank = (By.XPATH, "//span[@class='no-redirect' and text()='银行']")
    check_recharge_audit = (By.XPATH, "//span[@class='no-redirect' and text()='充值审核']")


    #### 我要買 ####
    buy_management = (By.XPATH, "//div[@class='el-submenu__title']//span[text()='买单（我要买） ']")
    brand_order_record = (By.XPATH, "//div[@class='test nest-menu']//span[text()='买单纪录-品牌出款 ']")    #品牌订单记录
    check_brand_order_record = (By.XPATH, "//span[@class='no-redirect' and text()='买单纪录-品牌出款']")    #品牌订单记录    
    brand_all_order = (By.XPATH, "//div[@class='test nest-menu']//span[text()='全部订单-品牌出款 ']")       #品牌全部订单 
    check_brand_all_order = (By.XPATH, "//span[@class='no-redirect' and text()='全部订单-品牌出款']")       #品牌全部订单

    #### 我要賣 ####
    sale_management = (By.XPATH, "//div[@class='el-submenu__title']//span[text()='卖单（我要卖） ']")
    sale_order_record = (By.XPATH, "//div[@class='test nest-menu']//span[text()='买单记录-顺付挂卖 ']")    #我要卖订单记录
    check_sale_order_record = (By.XPATH, "//span[@class='no-redirect' and text()='买单记录-顺付挂卖']")    #我要卖订单记录
    sale_all_order = (By.XPATH, "//div[@class='test nest-menu']//span[text()='全部订单-顺付挂卖 ']")       #我要卖全部订单
    check_sale_all_order = (By.XPATH, "//span[@class='no-redirect' and text()='全部订单-顺付挂卖']")       #我要卖全部订单


    #### 會員管理 ####
    member_management = (By.XPATH, "//div[@class='el-submenu__title']//span[text()='会员管理 ']")
    member_list = (By.XPATH, "//div[@class='test nest-menu']//span[text()='会员列表 ']")

    check_member_list = (By.XPATH, "//span[@class='no-redirect' and text()='会员列表']")

    #### 系統管理 ####
    system_management = (By.XPATH, "//div[@class='el-submenu__title']//span[text()='系統管理 ']")
    site_management = (By.XPATH, "//div[@class='test nest-menu']//span[text()='站点管理 ']")

    check_site_management = (By.XPATH, "//span[@class='no-redirect' and text()='站点管理']")
    
    
class MenuPage(BasePage):

    def open_menu(self):
        if self.is_element_finded(MenuPageLocator.svg_menu_closed):
            self.click(MenuPageLocator.svg_menu_closed)
        assert self.wait_visibility_status(MenuPageLocator.svg_menu_opening), f"後台左側導航欄開啟失敗"

    ############ 充值管理 ############
    # 進入充值審核
    def into_recharge_audit_management(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.recharge_management)
        self.click(MenuPageLocator.recharge_management)
        self.wait_visibility(MenuPageLocator.recharge_audit)
        self.click(MenuPageLocator.recharge_audit)
        assert self.wait_visibility_status(MenuPageLocator.check_recharge_audit), f"後台進入充值審核失敗"


    ############ 買單(我要買) ############
    # 進入品牌訂單紀錄/買單紀錄-品牌出款
    def into_brand_order_record(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.buy_management)
        self.click(MenuPageLocator.buy_management)
        self.wait_visibility(MenuPageLocator.brand_order_record)
        self.click(MenuPageLocator.brand_order_record)
        assert self.wait_visibility_status(MenuPageLocator.check_brand_order_record), f"後台進入 買單紀錄-品牌出款 失敗"

    # 進入我要賣訂單紀錄/買單紀錄-順附掛賣
    def into_sale_order_record(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.buy_management)
        self.click(MenuPageLocator.buy_management)
        self.wait_visibility(MenuPageLocator.sale_order_record)
        self.click(MenuPageLocator.sale_order_record)
        assert self.wait_visibility_status(MenuPageLocator.check_sale_order_record), f"後台進入 買單紀錄-順付掛賣 失敗"
    


    ############ 賣單(我要賣) ############
    
    # 進入我要賣全部訂單/全部訂單-順附掛賣
    def into_sale_all_order(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.sale_management)
        self.click(MenuPageLocator.sale_management)
        self.wait_visibility(MenuPageLocator.sale_all_order)
        self.click(MenuPageLocator.sale_all_order)
        assert self.wait_visibility_status(MenuPageLocator.check_sale_all_order), f"後台進入 全部訂單-順附掛賣 失敗"

    # 進入品牌全部訂單/全部訂單-品牌出款
    def into_brand_all_order(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.sale_management)
        self.click(MenuPageLocator.sale_management)
        self.wait_visibility(MenuPageLocator.brand_all_order)
        self.click(MenuPageLocator.brand_all_order)
        assert self.wait_visibility_status(MenuPageLocator.check_brand_all_order), f"後台進入 全部訂單-品牌出款 失敗"


    ############ 會員管理 ############
    # 進入會員列表
    def into_member_list(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.member_management)
        self.click(MenuPageLocator.member_management)
        self.wait_visibility(MenuPageLocator.member_list)
        self.click(MenuPageLocator.member_list)
        assert self.wait_visibility_status(MenuPageLocator.check_member_list), f"後台進入會員列表失敗"


    ############ 系統管理 ############
    # 進入站點管理
    def into_site_management(self):
        self.open_menu()
        self.wait_visibility(MenuPageLocator.system_management)
        self.click(MenuPageLocator.system_management)
        self.wait_visibility(MenuPageLocator.site_management)
        self.click(MenuPageLocator.site_management)
        assert self.wait_visibility_status(MenuPageLocator.check_site_management), f"後台進入站點管理失敗"
