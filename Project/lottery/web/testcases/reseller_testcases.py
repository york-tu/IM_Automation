import unittest, sys, os ,datetime, re
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(root_path)
from Project.lottery.web.pages.pages import WebPages, AdminPage, MobilePage,ResellerPage
from Project.lottery.apis.function_layer.functions import Functions
from Project.lottery.web.testcases.base_testcase import BaseTestCase
from Project.lottery.web.pages.reseller.reseller_basepage import BasePage as BasePage_Reseller
from apis.function_layer.base_functions import BaseFunction as BaseFunction_API
from Project.lottery.web.Utils_folder.screenshot import ScreenShot
import common.utils.globalvar as gl
import driver.web_driver as web_dr
from common.web.decorator import DecorateClass

class ResellerTestCases(BaseTestCase, BasePage_Reseller, BaseFunction_API):
    # Chrome Setting
    wait_time = 20
    implicitly_wait_time = 20
    money = '300'
    # is_structure_switchin 用 list 的方式來傳值，才能 pass by reference
    is_structure_switchin = [False]
    chrome_crash = 0
    foloderpath = ''
    function_dict = {}
    driver_list = []
    brand = gl.get_value('BRAND')
    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.folderpath = gl.get_value('FOLDER_PATH')
        cls.setting_browser()
        
    @classmethod
    def setUp(cls):
        for key, function in cls.function_dict.items():
            try:
                function.basePage().accept_alert()
                function.basePage().dismiss_alert()
            except:
                pass
            
            function.basePage().switch_home_page()
            if key == 'wp':
                cls.open_url(cls, function, cls.web_url)
                function.mainPage().maintenance()

        cls.test_all_windows_mini(cls)
        if key == 'wp':
            cls.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        elif key == 'mp':
            cls.function_dict['mp'].basePage().windows_to_top() # 切換視窗
    # ================================= Open Browser ================================
    
    def tearDown(self):
        self.test_all_windows_max()

        self.check_result(str(self.id()).split('.')[-1])
        image_name = self.id().split('.')[-1]
        image_path_list = []
        for driver in self.driver_list:
            image_path = ScreenShot(driver, f"{self.folderpath}/{image_name}/").screenshot(image_name)
            image_path_list.append(image_path)
        gl.set_value('IMG_PATH', image_path_list)  

    @classmethod
    def tearDownClass(cls):
        num = 0
        for function in cls.function_dict.values():
            function.basePage().quit_browser()
            num+=1

            if num == len(cls.driver_list):
                cls.driver_list = []
                break

    # ================================= Open Browser ================================

    @classmethod
    def setting_browser(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        if ResellerTestCases.brand == "ttmj":
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000, is_wap=True))  # 設定ChromeDriver
            cls.function_dict['mp'] = MobilePage(cls.driver_list[-1], cls.wait_time, cls.mobile_url, cls.skipTest)  # 導入Wap全部頁面
            cls.function_dict['mp'].basePage().hide_windows()  
            cls.functions = Functions()      
        else:
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['wp'] = WebPages(cls.driver_list[-1], cls.wait_time, cls.web_url, cls.skipTest)  # 導入Web全部頁面
            cls.function_dict['wp'].basePage().hide_windows()
            cls.functions = Functions()

        if not sys.argv[0].__contains__('prod'): # Prod 不帶入admin config
            cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['ad'] = AdminPage(cls.driver_list[-1], cls.wait_time, cls.admin_url, cls.skipTest)
            cls.function_dict['ad'].basePage().hide_windows()

            # cls.driver_list.append(web_dr.WebDriver.setting_driver(cls, 1900, 1000))  # 設定ChromeDriver
            cls.function_dict['rp'] = ResellerPage(cls.driver_list[-1], cls.wait_time, cls.reseller_url, cls.skipTest)  # 導入Reseller全部頁面
            # cls.function_dict['rp'].basePage().hide_windows()

    def open_url(self, function, url):
        try:
            function.basePage().dismiss_alert()
        except:
            pass
        
        function.basePage().open_browser(url)

            
    # ================================= TestCases =================================

    def test_all_windows_mini(self):
        for function in self.function_dict.values():
            function.basePage().hide_windows()

    def test_all_windows_max(self):
        for function in self.function_dict.values():
            function.basePage().windows_to_top() 

    # 測試-登入
    @DecorateClass('PFREQ-T1844')
    def test_web_login(self):
        self.test_all_windows_mini()
        self.function_dict['wp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['wp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['wp'].memberPage().refresh_browser()  # 關閉一般公告
        captcha_status = self.function_dict['wp'].mainPage().login(self.web_account, self.web_password, self.web_captcha)  # 登入
        if captcha_status == False:
            res, certification = self.function_dict['wp'].apibasefunction().do_web_login(self.web_account, self.web_password, self.web_url)  # 有滑動驗證時用api登入
            self.function_dict['wp'].mainPage().add_cookie_driver(res)  # 把cookie加進driver
            self.function_dict['wp'].memberPage().refresh_browser()
        self.function_dict['wp'].basePage().close_change_pwd()  # 關閉密碼更換彈窗
        self.function_dict['wp'].mainPage().close_login_board()  # 關閉登入公告

    # 測試WAP登入
    @DecorateClass('PFREQ-T1803')
    def test_wap_login(self):
        self.test_all_windows_mini()
        self.function_dict['mp'].mainPage().windows_to_top() # 切換視窗
        self.function_dict['mp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['mp'].mainPage().skip_app_download()
        self.function_dict['mp'].mainPage().into_login_page()
        captcha_status = self.function_dict['mp'].loginPage().login(self.web_account, self.web_password, self.web_captcha)
        if captcha_status == False:
            res, certification = self.function_dict['mp'].apibasefunction().do_wap_login(self.web_account, self.web_password, self.mobile_url)  # 有滑動驗證時用api登入
            self.function_dict['mp'].loginPage().add_cookie_wap(res)  # 把cookie加進driver
            self.function_dict['mp'].basePage().refresh_browser()
        self.function_dict['mp'].basePage().close_change_pwd()  # 關閉密碼更換彈窗
        self.function_dict['mp'].basePage().close_message_dialog()  # 關閉站內消息彈窗
        self.function_dict['mp'].mainPage().close_login_board()

    # 測試ADMIN登入
    @DecorateClass('PFREQ-T1804')
    def test_admin_login(self):
        self.test_all_windows_mini()
        self.function_dict['ad'].basePage().windows_to_top() # 切換視窗
        self.function_dict['ad'].basePage().open_base_url()  # 開啟admin網站
        self.function_dict['ad'].loginPage().login(self.admin_account, self.admin_password, self.admin_otp)  # 登入admin

    # 測試Reseller登入
    @DecorateClass('PFREQ-T2134')
    def test_reseller_login(self):
        self.test_all_windows_mini()
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()  # 開啟前台網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_agentinfo(self.reseller_account,'BotTest')

    # 測試代理轉移
    @DecorateClass('PFREQ-T2133')
    def test_structure_change(self):
        self.test_admin_login()
        self.function_dict['ad'].membermanagementpage().into_member_list()  # 進入銀行帳號

        # True為轉入正確代理進行測試,False則為否
        if self.is_structure_switchin[0] == False :
            self.function_dict['ad'].MemberList().change_member_structure(self.web_account, self.reseller_account, self.admin_otp)
            self.is_structure_switchin[0] = True
        else:
            '''
                部分品牌的 test1234 不是代理帳號，因此改用 testaaaa
            '''
            self.function_dict['ad'].MemberList().change_member_structure(self.web_account, 'testaaaa', self.admin_otp)
            self.is_structure_switchin[0] = False

    # 測試一般報表api_login
    @DecorateClass('PFREQ-T2141')
    def test_general_report(self):
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()  # 開啟reseller網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().into_general_report()

        if self.is_structure_switchin[0] == True :
            res, certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url)
            _sum=self.functions.ui_admin_betting_center().get_info_member(certification, self.admin_account, self.admin_password, self.admin_url,self.web_account) # Type:Dictionary 抓取注單中心資料
        
            self.function_dict['rp'].genernalPage().structure_report(_sum,self.web_account)
            self.function_dict['rp'].genernalPage().graphical_report(self.web_account)
            self.function_dict['rp'].genernalPage().trend_report()
            self.function_dict['rp'].genernalPage().graphical_report_account(self.web_account)
            self.function_dict['rp'].genernalPage().trend_report_account()
        else:
            self.function_dict['rp'].genernalPage().unstructure_report(self.web_account)
    
    
    # 測試每日報表
    @DecorateClass('PFREQ-T2142')
    def test_daily_report(self):
        # ADMIN PART  抓取注單中心資料 API
        res, certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url) 
        _sum=self.functions.ui_admin_betting_center().get_info_agent(certification, self.admin_account, self.admin_password, self.admin_url, self.reseller_account) # Type:Dictionary

        # ADMIN PART 在線入款
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_bank_online_deposit()  # 進入在線入款
        online_record = self.function_dict['ad'].OnlineDepositPage().get_sum_info(self.reseller_account, time='1')  # 收集資料

        # ADMIN PART 公司入款
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_enter_company_deposit()  # 進入公司入款
        company_record = self.function_dict['ad'].companyDepositPage().get_sum_info(self.reseller_account, time='1')  # 收集資料
        
        # ADMIN PART 人工存入
        self.function_dict['ad'].financialmanagementPage().into_manual_deposit()    # 進入 人工存入 頁面
        # 人工非優惠項目也可能會有優惠金額：上分優惠為所有交易類型
        artificial_discount_record = self.function_dict['ad'].ArtificialDeposit().get_sum_info(self.reseller_account, ['全选'], time='1')
        # 上分數、上分額不包含人工入款_優惠項目：上分數、上分額不計優惠項目
        artificial_record = self.function_dict['ad'].ArtificialDeposit().get_sum_info(self.reseller_account, ['全选', '活动优惠', '返点优惠', '存款优惠'], time='1')
        artificial_record['artificial_discount'] = artificial_discount_record['artificial_discount']
        
        # ADMIN PART 上分虛擬幣，因目前機器人不會有虛擬幣操作，故暫省略，待補

        # ADMIN PART 提款
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw()  # 進入出款申請
        withdraw_record = self.function_dict['ad'].withdrawPage().get_sum_info(self.reseller_account, time='1')   # 收集資料

        # ADMIN PART 出款總覽
        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_withdraw_general()  # 進入出款總攬
        withdraw_general_record = self.function_dict['ad'].withdrawGeneralPage().get_sum_info(self.reseller_account, time='1')   # 收集資料

        # RESELLER
        self.function_dict['rp'].basePage().open_base_url()  # 開啟reseller網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().into_daily_report()

        if self.is_structure_switchin[0] == True :
            self.function_dict['rp'].dailyPage().daily_report(online_record, company_record, artificial_record, withdraw_record, withdraw_general_record, _sum)
        else:
            self.function_dict['rp'].dailyPage().undaily_report(online_record, company_record, artificial_record, withdraw_record, withdraw_general_record, _sum)

    # 有效會員 資料對admin報表、對資料加總相符
    @DecorateClass('PFREQ-T2143')
    def test_check_valid_member(self):
        # 資料對admin報表
        res, certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp,self.admin_url) 
        ticketcenter_record = self.functions.ui_admin_betting_center().get_info_member(certification, self.admin_account, self.admin_password, self.admin_url, self.web_account)
        
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_validmember()
        self.function_dict['rp'].validmemberPage().choose_type_of_member_official()
        self.function_dict['rp'].validmemberPage().member_account_search(self.web_account)
        self.function_dict['rp'].validmemberPage().search_record(ticketcenter_record, self.is_structure_switchin[0])
        
        # 確認每個會員加總 和 總和相符
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_validmember()
        self.function_dict['rp'].validmemberPage().total_check(self.is_structure_switchin[0])


    # 注單查詢頁面 訂單號碼、期數、會員帳號 查詢
    @DecorateClass('PFREQ-T2140')
    def test_ticket_name_period_account_search(self):
        if self.brand == "ttmj":
            self.function_dict['mp'].basePage().open_base_url()
            self.test_wap_login()
            self.function_dict['mp'].lotteryGamePage().into_jisuk3_nwap()  # 進入彩票遊戲
            lottery_record = self.function_dict['mp'].lotteryGamePage().betting_game_new() # 進入極速快3
            self.test_wap_login()
            self.function_dict['mp'].lotteryGamePage().into_menu_betting_record_new()
            record = self.function_dict['mp'].gameRecordPage().game_lottery_nwap(lottery_record)
            self.function_dict['rp'].record = record
        else:    
            self.test_web_login()
            self.function_dict['wp'].menuPage().into_menu_lottery()
            self.function_dict['wp'].lotteryPage().into_jisuk3()
            record = self.function_dict['wp'].lotteryGamePage().betting_game(self.function_dict['wp'].lotteryGamePage().js3)  #下注極速快3
            self.function_dict['wp'].lotteryGamePage().into_menu_betting_recording()
            record = self.function_dict['wp'].gameRecordPage().game_lottery(record)
            self.function_dict['rp'].record = record

        # 查找訂單號碼
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_notesearch()
        self.function_dict['rp'].notesearchPage().choice_channel_product_play()
        self.function_dict['rp'].notesearchPage().order_number_search(record["ticket_name"]) # 訂單號碼
        self.function_dict['rp'].notesearchPage().search_record(record, self.is_structure_switchin[0], self.web_account)             # 爬取訂單內容、switchin判斷是否在代理內(True在代理內)

        # 查找期數
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_notesearch()
        self.function_dict['rp'].notesearchPage().period_search(record["period"])           # 期數  
        self.function_dict['rp'].notesearchPage().search_record(record, self.is_structure_switchin[0], self.web_account)             # 爬取訂單內容、switchin判斷是否在代理內(True在代理內)
        
        # 查找會員帳號
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().check_notesearch()
        self.function_dict['rp'].notesearchPage().member_account_search(self.web_account)
        self.function_dict['rp'].notesearchPage().search_record(self.function_dict['rp'].record, self.is_structure_switchin[0], self.web_account)     # 爬取訂單內容、switchin判斷是否在代理內(True在代理內)
        self.function_dict['rp'].notesearchPage().check_pages() # 檢查總筆數跟頁面正確

        
    # 測試會員列表
    @DecorateClass('PFREQ-T2136')
    def test_member_list(self):

        if self.brand == "ttmj":
            self.function_dict['mp'].basePage().open_base_url()
            self.test_wap_login()
            available_balance = self.function_dict['mp'].menuPage().get_balance_wallet()
        else:
            self.function_dict['rp'].basePage().open_base_url()     # 開啟 web 網站
            self.test_web_login()               # 登入 web
            available_balance = self.function_dict['wp'].menuPage().get_balance_wallet()

        self.test_admin_login()
        self.function_dict['ad'].financialmanagementPage().into_cp_ledger()    # 進入現金流水頁面
        self.function_dict['ad'].CPLedgerPage().search_account(self.web_account)
        admin_data = [
            self.function_dict['ad'].CPLedgerPage().get_transaction_time_list(), 
            self.function_dict['ad'].CPLedgerPage().get_member_account_list(), 
            self.function_dict['ad'].CPLedgerPage().get_current_amount_list(), 
            self.function_dict['ad'].CPLedgerPage().get_transaction_amount_list(), 
            self.function_dict['ad'].CPLedgerPage().get_final_amount_list(), 
        ]

        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()  # 開啟reseller網站
        self.function_dict['rp'].loginPage().logout()
        self.function_dict['rp'].loginPage().login(self.shareholder, self.reseller_password, self.reseller_otp)  # 登入reseller 股東
        self.function_dict['rp'].menuPage().click_on_member_list()   # 切到會員列表
        self.function_dict['rp'].memberListPage().check_all_member(self.web_account, self.generalagent, self.reseller_account, self.is_structure_switchin[0])   # 檢查所有會員資訊

        if self.is_structure_switchin[0]:
            self.function_dict['rp'].memberListPage().check_search_member(self.web_account, self.generalagent, self.reseller_account, available_balance)  # 檢查搜尋會員的資訊
            self.function_dict['rp'].memberListPage().check_detail()
            self.function_dict['rp'].memberListPage().check_click_order_button()
            self.function_dict['rp'].memberListPage().check_click_ledger_button(self.web_account, admin_data)
        else:
            self.function_dict['rp'].memberListPage().check_search_member_switchout(self.web_account)

    # 測試代理列表
    @DecorateClass('PFREQ-T2137')
    def test_agent_list(self):
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()  # 開啟reseller網站
        self.function_dict['rp'].loginPage().logout()
        self.function_dict['rp'].loginPage().login(self.shareholder, self.reseller_password, self.reseller_otp)  # 登入reseller 股東
        self.function_dict['rp'].menuPage().click_on_agent_list()
        self.function_dict['rp'].agentListPage().check_all_agent(self.reseller_account, self.generalagent)
        self.function_dict['rp'].agentListPage().check_search_agent(self.reseller_account)
        self.function_dict['rp'].basePage().open_base_url()  # 開啟reseller網站
        self.function_dict['rp'].loginPage().logout()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password, self.reseller_otp)  # 登入reseller 代理

    # 測試Reseller代理結算
    @DecorateClass('PFREQ-T2138')
    def test_reseller_old_agent_settlement(self):
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()                                                          # 開啟reseller網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().into_old_agent_settlementpage()                                          # 進入代理結算
        self.function_dict['rp'].oldAgentSettlementPage().check_special_target()                                     # 檢查特定元件是否存在

    # 測試Reseller代理結算(新版)
    @DecorateClass('PFREQ-T2139')
    def test_reseller_new_agent_settlement(self):
        # admin 頁面
        self.test_admin_login()
        self.function_dict['ad'].rebateandcommisionPage().into_new_settlement()  # 進入代理結算(新版)
        self.function_dict['ad'].NewSettlementPage().add_agent_settlement(self.commision_program) # 生成代理結算

        # 取得 admin 資料
        Admin_searching_list, number = self.function_dict['ad'].NewSettlementPage().get_searching_data_list(self.commision_program)
        # Admin_detail_table_list = self.function_dict['ad'].NewSettlementPage().get_detail_table_data()                 #目前 Reseller 代理結算(新版) 詳情頁面有誤 (已開單)
        # Admin_channel_detail_table_list = self.function_dict['ad'].NewSettlementPage().get_channel_detail_table_data()
        # Admin_third_party_table_list = self.function_dict['ad'].NewSettlementPage().get_third_party_rent_table_data()

        # reseller 頁面
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()                                                          # 開啟reseller網站
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].menuPage().into_new_agent_settlementpage()                                          # 進入reseller代理結算(新版)
        self.function_dict['rp'].newAgentSettlementPage().check_page_total()                                         # 查看結算列表頁數是否正確

        # 比較 admin 和 reseller 資料有無差異
        Reseller_searching_list = self.function_dict['rp'].newAgentSettlementPage().get_searching_data_list(self.commision_program, number)
        assert Admin_searching_list == Reseller_searching_list, f"searching_list Error, \n\nadmin: {Admin_searching_list} \n\nreseller: {Reseller_searching_list}"

        """ 目前 Reseller 代理結算(新版) 詳情頁面有誤 (已開單)
        Reseller_detl_table_list = self.function_dict['rp'].newAgentSettlementPage().get_detail_table_data()
        assert Adminetail_table_list == Reseller_detail_table_list, f"Detail_table Error, \n\nadmin: {Admin_detail_table_list} \n\nreseller: {Reseller_detail_table_list}"

        Reseller_chael_detail_table_list = self.function_dict['rp'].newAgentSettlementPage().get_channel_detail_table_data()
        assert Adminhannel_detail_table_list == Reseller_channel_detail_table_list, f"Channel_detail_table Error, \n\nadmin: {Admin_channel_detail_table_list} \n\nreseller: {Reseller_channel_detail_table_list}"

        Reseller_thi_party_table_list = self.function_dict['rp'].newAgentSettlementPage().get_third_party_rent_table_data()
        assert Adminhird_party_table_list == Reseller_third_party_table_list, f"Third_party_table Error, \n\nadmin: {Admin_third_party_table_list} \n\nreseller: {Reseller_third_party_table_list}"
        """
    # 檢查"我的資料"
    @DecorateClass('PFREQ-T2135')
    def test_reseller_profile(self):
        self.function_dict['rp'].basePage().windows_to_top() # 切換視窗
        self.function_dict['rp'].basePage().open_base_url()
        self.function_dict['rp'].loginPage().login(self.reseller_account, self.reseller_password,self.reseller_otp)  # 登入reseller
        self.function_dict['rp'].loginPage().into_profile()
        self.function_dict['rp'].profilePage().check_all_password_empty()
        self.function_dict['rp'].profilePage().check_input_error_old_password()

        try:
            self.function_dict['rp'].profilePage().change_password('000000', '000000', '000')
            self.function_dict['rp'].profilePage().change_password('000000', '123456', '123456')
            self.function_dict['rp'].profilePage().change_password('123456', '000000', '000000')
        except AssertionError as e:
            self.function_dict['rp'].profilePage().change_password('123456', '000000', '000000')
            raise e

        self.function_dict['rp'].profilePage().check_all_security_code_empty()

        try:
            self.function_dict['rp'].profilePage().change_security_code('0', '0')
            self.function_dict['rp'].profilePage().check_change_security_code('0', '0')
            self.function_dict['rp'].profilePage().change_security_code('00000', '00000')
            self.function_dict['rp'].profilePage().check_change_security_code('00000', '00000')
            self.function_dict['rp'].profilePage().change_security_code('0000', '00000')
            self.function_dict['rp'].profilePage().check_change_security_code('0000', '00000')
            self.function_dict['rp'].profilePage().change_security_code('0000', '1234')
            self.function_dict['rp'].profilePage().check_change_security_code('0000', '1234')
            self.function_dict['rp'].profilePage().change_security_code('1234', '1234')
            self.function_dict['rp'].profilePage().check_change_security_code('1234', '1234')
            self.function_dict['rp'].profilePage().change_security_code('0000', '0000')
            self.function_dict['rp'].profilePage().check_change_security_code('0000', '0000')
        except AssertionError as e:
            self.function_dict['rp'].profilePage().change_security_code(self.reseller_otp, self.reseller_otp)
            raise e

    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method