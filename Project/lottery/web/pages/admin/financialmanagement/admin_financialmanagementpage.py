from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class FinancialManagementPageLocator:
     # ------------財務管理分類------------
    # menu_financial_management = (By.XPATH, "//span[text()='财务管理']/..")  # 財務管理
    menu_financial_management = (By.XPATH, "(//h3[@class='uppercase']/span[@data-bind='text: name'])[3]")  # 財務管理

    # *帳號管理
    menu_account_management = (By.XPATH, "//span[text()='账号管理']/..")  # 財務管理-帳號管理
    # 銀行帳號
    menu_accountbank = (By.XPATH, "//span[text()='银行账号']/..")  # 財務管理-帳號管理-銀行帳號
    ok_point_accountbank = (By.XPATH, "//a[text() = '银行帐号']")
    # 在線商號
    menu_accountonile = (By.XPATH, "//span[text()='在线商号']/..")  # 財務管理-帳號管理-在線商號
    ok_point_accountonline = (By.XPATH, "//a[text() = '在线商号']")
    # 錢包地址
    menu_wallet_address = (By.XPATH, "//span[text()='钱包地址']/..")  # 財務管理-帳號管理-钱包地址
    ok_point_wallet_address = (By.XPATH, "//a[text() = '钱包地址']")
    
    # *比例设置
    menu_proportion = (By.XPATH, '//span[text()="比例设置"]')   # 比例设置
    # 手續費用
    handing_fee = (By.XPATH, '//span[text()="手续费用"]') # 財務管理-比例設置-手續費用
    ok_point_handing_fee = (By.XPATH, '//a[text()="手续费用"]')

    # *上分管理
    menu_deposit_management = (By.XPATH, "//span[text()='上分管理']/..")  # 財務管理-上分管理
    # 上分總覽
    total_deposit = (By.XPATH, "//span[contains(text(), '上分总览')]") # 財務管理-上分管理-上分總覽
    ok_point_total_deposit = (By.XPATH, "//a[contains(text(), '上分总览')]")
    # 公司
    enter_company_deposit = (By.XPATH, "//span[contains(text(), '公司')]")  # 財務管理-上分管理-公司
    ok_point_company_deposit = (By.XPATH, "//a[text() = '公司']")
    # 在線
    enter_online_deposit = (By.XPATH, "(//span[text()='在线'])[1]")  # 財務管理-上分管理-在線
    ok_point_online_deposit = (By.XPATH, "//a[text() = '在线']")
    # 人工存入
    manual_deposit = (By.XPATH, "//span[contains(text(), '人工存入')]") # 財務管理-上分管理-人工存入
    ok_point_manual_deposit = (By.XPATH, "//a[text() = '人工存入']")

    # *下分管理
    menu_withdraw_management = (By.XPATH, "//span[text()='下分管理']/..")  # 財務管理-下分管理
    # 下分總覽
    enter_withdrawgeneral = (By.XPATH, "//span[contains(text(), '下分总览')]")  # 財務管理-下分管理-下分總覽
    ok_point_withdrawgeneral = (By.XPATH, "//a[contains(text(), '下分总览')]")
    # 下分申请
    # enter_withdraw = (By.XPATH, "//span[contains(text(), '下分申请')]")  # 財務管理-下分管理-下分申请
    enter_withdraw = (By.XPATH, "//span[contains(text(), '下分申请')]/..") # 財務管理-下分管理-下分申请
    ok_point_withdraw = (By.XPATH, "//a[text() = '下分申请']")
    # 在線
    online_withdraw = (By.XPATH, "(//span[text()='在线'])[2]") # 財務管理-下分管理-在線
    ok_point_online_withdraw = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '在线')]")
    # 人工提出
    manual_withdraw = (By.XPATH, "//span[contains(text(), '人工提出')]") # 財務管理-下分管理-人工提出
    ok_point_manual_withdraw = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '人工提出')]")

    # *優惠規則
    menu_preferential_rules = (By.XPATH, '//span[text()="优惠规则"]')   # 優惠規則
    # 上分優惠
    deposit_preferential = (By.XPATH, "//span[contains(text(), '上分优惠')]") # 財務管理-優惠規則-上分優惠
    ok_point_deposit_preferential = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '上分优惠')]")
    # 上分規則
    deposit_rules = (By.XPATH, "//span[contains(text(), '上分规则')]") # 財務管理-優惠規則-上分規則
    ok_point_deposit_rules = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '上分规则')]")

    # *流水系統
    menu_cash_system = (By.XPATH, '//span[text()="流水系统"]')   # 流水系统
    # 上下分流水
    ledger = (By.XPATH, '//li[@permission-id="finance.stat"]//span[text()="上下分流水"]') # 財務管理-流水系統-CP現金流水
    third_party_ledger = (By.XPATH, "//div[contains(text(), '第三方上下分流水')]") # 財務管理-流水系統-第三方現金流水
    ok_point_ledger = (By.XPATH, "//div[@class='el-breadcrumb app-breadcrumb breadcrumb-container']//a[contains(text(), '上下分流水')]")
    # 會員錢包
    member_wallet = (By.XPATH, "//li[@permission-id='finance.stat']//span[text()='会员钱包']") # 財務管理-流水系統-會員錢包
    ok_point_member_wallet = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '会员钱包')]")
    # 上下分報表
    financial_report = (By.XPATH, "//li[@permission-id='finance.stat']//span[text()='上下分报表']") # 財務管理-流水系統-上下分報表
    ok_point_financial_report = (By.XPATH, "//div[@class='el-breadcrumb app-breadcrumb breadcrumb-container']//a[contains(text(), '上下分报表')]")
    # 差額報表
    difference_report = (By.XPATH, "//li[@permission-id='finance.stat']//span[text()='差额报表']") # 財務管理-流水系統-差額報表
    ok_point_difference_report = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '差额报表')]")

    # *外接平台
    # menu_external_planform_financial = (By.XPATH, "//span[text()='财务管理']/..//span[text()='外接平台']")
    # menu_external_planform_financial = (By.XPATH, "//span[text()='财务管理']/../..//span[text()='外接平台']")
    menu_external_planform_financial = (By.XPATH, "(//h3[@class='uppercase']/span[@data-bind='text: name'])[3]/../..//span[text()='外接平台']")
    
    # 額度轉換
    credit_conversion = (By.XPATH, "//span[text()='额度转换']") # 財務管理-外接平台-額度轉換
    ok_point_credit_conversion = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '额度转换')]")
    # 餘額查詢
    over_inquire = (By.XPATH, "//span[text()='余额查询']") # 財務管理-外接平台-額度轉換
    ok_point_over_inquire = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '余额查询')]")
    # 上下分流水
    ledger_in_externalplanform = (By.XPATH, '//li[@permission-id="finance.cm"]//span[text()="上下分流水"]') # 財務管理-外接平台-上下分流水
    ok_point_ledger_in_externalplanform = (By.XPATH, "//ul[@class='page-breadcrumb']//a[contains(text(), '上下分流水')]")

class FinancialManagementPage(BasePage):

    # 財務管理
    def click_financial_management(self):
        self.wait_loading_finish()
        self.scroll_to_top()
        
        for loop in range(0,4):
            if self.wait_visibility_status(FinancialManagementPageLocator.menu_financial_management) is True:
                self.wait_loading_finish()
                self.click(FinancialManagementPageLocator.menu_financial_management)
                break
            else:
                if loop == 4:
                    assert self.is_element_finded(FinancialManagementPageLocator.menu_financial_management), "财务管理BTN錯誤, 無法搜尋到該BTN"
            
            if loop == 3:
                raise EOFError('找不到財務管理按鈕')

    # 財務管理 -> 帳號管理 -> 銀行帳號
    def into_bank_account(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_account_management)
        self.wait_visibility(FinancialManagementPageLocator.menu_accountbank)
        self.click(FinancialManagementPageLocator.menu_accountbank)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_accountbank)
        self.wait_loading_finish()

    # 財務管理 -> 帳號管理 -> 在線商號
    def into_bank_online_account(self):
        self.click_financial_management()
        self.wait_visibility(FinancialManagementPageLocator.menu_account_management)
        self.click(FinancialManagementPageLocator.menu_account_management)
        self.wait_visibility(FinancialManagementPageLocator.menu_accountonile)
        self.click(FinancialManagementPageLocator.menu_accountonile)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_accountonline)
        self.wait_loading_finish()
    
    # 財務管理 -> 帳號管理 -> 錢包地址
    def into_bank_wallet_address(self):
        self.click_financial_management()
        self.wait_visibility(FinancialManagementPageLocator.menu_account_management)
        self.click(FinancialManagementPageLocator.menu_account_management)
        self.wait_visibility(FinancialManagementPageLocator.menu_wallet_address)
        self.click(FinancialManagementPageLocator.menu_wallet_address)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_wallet_address)
        self.wait_loading_finish()

    # 財務管理 -> 上分管理 -> 在線入款
    def into_bank_online_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.enter_online_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_online_deposit)
        self.wait_loading_finish()

    # 財務管理 -> 比例設置 -> 手續費用
    def into_handing_fee(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_proportion)
        self.click(FinancialManagementPageLocator.handing_fee)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_handing_fee)
        self.wait_loading_finish()

    # 財務管理 -> 上分管理 -> 上分總攬
    def into_total_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.total_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_total_deposit)
        self.wait_loading_finish()

    # 財務管理 -> 上分管理 -> 公司
    def into_enter_company_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.enter_company_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_company_deposit)
        self.wait_loading_finish()

    # 財務管理 -> 上分管理 -> 在線
    def into_enter_online_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.enter_online_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_online_deposit)
        self.wait_loading_finish()
        
    # 財務管理 -> 上分管理 -> 人工存入
    def into_manual_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.manual_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_manual_deposit)
        self.wait_loading_finish()

    # 財務管理 -> 上分管理 -> 公司
    def into_company_deposit(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_deposit_management)
        self.click(FinancialManagementPageLocator.enter_company_deposit)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_company_deposit)
        self.wait_loading_finish()

    # 財務管理 -> 下分管理 -> 下分總攬
    def into_withdraw_general(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_withdraw_management)
        self.click(FinancialManagementPageLocator.enter_withdrawgeneral)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_withdrawgeneral)
        self.wait_loading_finish()

    # 財務管理 -> 下分管理 -> 下分申請
    def into_withdraw(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_withdraw_management)
        self.click(FinancialManagementPageLocator.enter_withdraw)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_withdraw)
        self.wait_loading_finish()

    # 財務管理 -> 下分管理 -> 在線
    def into_online_withdraw(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_withdraw_management)
        self.click(FinancialManagementPageLocator.online_withdraw)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_online_withdraw)
        self.wait_loading_finish()

    # 財務管理 -> 下分管理 -> 人工提出
    def into_manual_withdraw(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_withdraw_management)
        self.click(FinancialManagementPageLocator.manual_withdraw)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_manual_withdraw)
        self.wait_loading_finish()

    # 財務管理 -> 優惠規則 -> 存款優惠
    def into_deposit_preferential(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_preferential_rules)
        self.click(FinancialManagementPageLocator.deposit_preferential)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_deposit_preferential)
        self.wait_loading_finish()

    # 財務管理 -> 優惠規則 -> 上分規則
    def into_deposit_rules(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_preferential_rules)
        self.click(FinancialManagementPageLocator.deposit_rules)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_deposit_rules)
        self.wait_loading_finish()
    
    # 財務管理 -> 流水系統 -> CP現金流水
    def into_cp_ledger(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_cash_system)
        self.click(FinancialManagementPageLocator.ledger)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_ledger)
        self.wait_loading_finish()
    
    # 財務管理 -> 流水系統 -> 第三方現金流水
    def into_thirdparty_ledger(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_cash_system)
        self.click(FinancialManagementPageLocator.ledger)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_ledger)
        self.click(FinancialManagementPageLocator.third_party_ledger)
        self.wait_loading_finish()

    # 財務管理 -> 流水系統 -> 會員錢包
    def into_member_wallet(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_cash_system)
        self.click(FinancialManagementPageLocator.member_wallet)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_member_wallet)
        self.wait_loading_finish()

    # 財務管理 -> 流水系統 -> 財務報表
    def into_financial_report(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_cash_system)
        self.click(FinancialManagementPageLocator.financial_report)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_financial_report)
        self.wait_loading_finish()

    # 財務管理 -> 流水系統 -> 差額報表
    def into_difference_report(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_cash_system)
        self.click(FinancialManagementPageLocator.difference_report)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_difference_report)
        self.wait_loading_finish()
    
    # 財務管理 -> 外接平台 -> 額度轉換
    def into_credit_conversion(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_external_planform_financial)
        self.click(FinancialManagementPageLocator.credit_conversion)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_credit_conversion)
        self.wait_loading_finish()

    # 財務管理 -> 外接平台 -> 餘額查詢
    def into_over_inquire(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_external_planform_financial)
        self.click(FinancialManagementPageLocator.over_inquire)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_over_inquire)
        self.wait_loading_finish()

    # 財務管理 -> 外接平台 -> 上下分流水
    def into_ledger_in_external_planform(self):
        self.click_financial_management()
        self.click(FinancialManagementPageLocator.menu_external_planform_financial)
        self.click(FinancialManagementPageLocator.ledger_in_externalplanform)
        self.wait_visibility(FinancialManagementPageLocator.ok_point_ledger_in_externalplanform)
        self.wait_loading_finish()