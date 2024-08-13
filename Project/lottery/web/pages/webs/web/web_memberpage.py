from selenium.webdriver.common.by import By
from pages.webs.web.webs_basepage import BasePage
from selenium.common.exceptions import TimeoutException
import math,datetime, logging, random
from random import choice, randint
import os, platform


class MemberPageLocator(BasePage):
    # L_MENU 左側選單項目
    l_menu_logout = (By.ID, "nzc-member-logout")
    l_menu_deposit = (By.ID, "nzc-member-deposit")
    l_menu_withdraw = (By.ID, "nzc-member-redirect")  # id命名有問題
    l_menu_mywallet = (By.ID, "nzc-member-withdraw")  # id命名有問題
    l_menu_bettingrecord = (By.ID, "nzc-member-order")
    l_menu_myprofile = (By.ID, "nzc-member-profile")
    l_meny_mymessage = (By.ID, "nzc-member-inbox")

    # MYwallet MENU (我的錢包-主選單)
    menu_wallet = (By.ID, "nzc-wallet-nav-wallet")  # 額度管裡
    menu_deposit = (By.ID, "nzc-wallet-nav-deposit")  # 線上存款
    menu_withdraw = (By.ID, "nzc-wallet-nav-withdraw")  # 線上取款
    menu_history = (By.ID, "nzc-wallet-nav-history")  # 交易流水
    menu_wallet_deposit = (By.ID, "nzc-wallet-nav-walletdeposit")  # 入款記錄
    menu_wallet_withdraw = (By.ID, "nzc-wallet-nav-walletwithdraw")  # 出款記錄
    menu_tranfer = (By.ID, "nzc-wallet-nav-transfer")  # 轉換記錄

    # My Profile Menu (我的資料-主選單)
    profile_menu_cg_pwd = (By.ID, "passwd")
    proflie_menu_cg_s_pwd = (By.ID, "securitycode")
    profile_menu_contact = (By.ID, "contact")
    profile_menu_card = (By.ID, "card")

    # MEMBER wallet ONLINE DEPOSIT (線上存款選單-入款方式)================================

    # 入款紀錄
    search_today=(By.XPATH, "//*[@class='top-nav-right']/a[text()='今天']")
    search_company=(By.XPATH, "//div[@class='select-box']//select[@data-bind='value: filter.type']")

    amount_before=(By.XPATH,"//tr[1]//td[contains(@data-bind,'amountbefore')]")
    amount_to=(By.XPATH,"//tr[1]//td[contains(@data-bind,'depositamount')]")
    amount_after=(By.XPATH,"//tr[1]//td[contains(@data-bind,'amountafter')]")
    amount_status=(By.XPATH,"//tr[1]//td[contains(@data-bind,'status].name')]")
    amount_time=(By.XPATH,"//tr[1]//td[contains(@data-bind,'added')]")
    owner_total_money=(By.XPATH, "//span[@class='balance-text']")
    type_ = (By.XPATH, "//select[@data-bind = 'value: filter.type']")

    #出款紀錄

    amount_before_out = (By.XPATH,"(//td[contains(@data-bind,'amountbefore')])[1]") # 出款前
    amount_to_Out = (By.XPATH,"(//td[contains(@data-bind,'text:amount')])[1]") # 出款金額
    amount_after_Out = (By.XPATH,"(//td[contains(@data-bind,'amountafter')])[1]") # 出款後
    withdraw_status = (By.XPATH,"(//div[@style='']/*[contains(@data-bind,'showStatusMsg') or contains(@data-bind,'showPayboxStatusMsg')])[1]") # 出款紀錄
    want_buy_check_btn = (By.XPATH, "(//a[text()='确认收到'])[1]") # 確認收到
    want_buy_pop_btn = (By.XPATH, "//div[text()='确认']") # 確認

    #額度轉換主錢包
    wallet=(By.XPATH,"//*[@class='cp_balance']")

    # 交易流水類型
    search_all=(By.XPATH, "//div[@class='choice']")
    search_info=(By.XPATH, "//div[@class='select-box']//a[text()='额度转换']")
    amount_change=(By.XPATH, "//tr[1]//td[contains(@data-bind,'amount')]")
    money_now=(By.XPATH, "//tr[1]//td[contains(@data-bind,'changed')]")
    #儲值類型
    @staticmethod
    def amount_sort(Sort):
        amount_sort=(By.XPATH,"//tr[1]//td[contains(@data-bind,'type') and text()='%s']"%Sort)
        return amount_sort

    # 付款方式
    def deposit_name(self, name, delete= False):
        deposit_enter = (By.XPATH, "//*[text()='%s']" % name)

        if delete == True:
            if self.is_element_finded(deposit_enter) is False:
                return
            else:
                raise EOFError(f'不應該顯示此入款方式: {name}')

        if self.is_element_finded(deposit_enter) is False and delete == False:
            self.test_skip('無此支付方式')
            self.sleep(2)
        else:
            self.click(deposit_enter)


    # 微信/支付寶第一層支付方式
    def paytitle(self, TitleName):
        paytitle = (By.XPATH, "//*[contains(@data-bind,'text') and contains(text(),'%s')]" % TitleName)
        if self.is_element_finded(paytitle) is False:
            self.test_skip('無此支付方式')

        message = self.get_text(paytitle)
        assert str(message).__contains__(TitleName), '%s 建立失敗' % TitleName

        # 避免只有一種付款方式跳出錯誤
        try:
            self.click(paytitle)
        except:
            pass

    # 微信/支付寶
    deposit_amount = (By.XPATH, "//input[@class='input-box']")  # 支付寶/微信 轉帳第一層金額輸入
    deposit_qrcode_next_btn = (By.XPATH, "//div[text()='查看二维码']")  # 支付寶/微信 面對面下一步
    user_name_qr = (By.XPATH, "//*[@data-bind='text: account']")  # 確認面對面方式的使用者名稱
    deposit_f2f_submit_btn = (By.XPATH, "//div[text()='完成转账']")
    real_money = (By.XPATH, "//span[contains(@data-bind,'transferamount')]")
    select_money = (By.XPATH, "//li[@class='active' and contains(@data-bind, 'text: amount')]") # 線上支付_金額選項


    # 找最新的銀行開戶人
    def users_find_and_check(self, Realuser):
        self.wait_loading_finish()
        userlink =(By.XPATH,"//*[contains(@id,'radio')]") #全部選項
        for ele in range(0, len(self.find_elements(userlink))):
            self.sleep(1)
            userlink_click =(By.XPATH, "//*[@class='radio-label' and @for='radio-%d']" %ele) #點擊選項
            self.click(userlink_click)
            user = (By.XPATH, "//span[@style='']//span[contains(@data-bind, 'name')]")  # 開戶名
            
            message = self.get_text(user) #開戶人名

            if message == Realuser:
                break

        assert message == Realuser, '找不到開戶人名稱:%s' % Realuser

    # 找錢包地址
    def address_find_and_check(self, address):
        self.wait_loading_finish()
        userlink =(By.XPATH,"//*[contains(@id,'radio')]") #全部選項
        for ele in range(0, len(self.find_elements(userlink))):
            self.sleep(1)
            userlink_click =(By.XPATH, f"(//*[@class='radio-label'])[{ele+1}]") #點擊選項
            self.click(userlink_click)
            user = (By.XPATH, "//table[@style='']//span[contains(@data-bind, 'account')]")  # 地址
            
            message = self.get_text(user) #地址

            if message == address:
                break
        assert message == address, '找不到錢包地址:%s' % address

    # 五碼QRcode
    def deposit_wechat_ailpay_five_code(self):
        deposit_wechat_ailpay_five_code = (By.XPATH, "//input[@class='input']")
        for ele in range(1, len(self.find_elements(deposit_wechat_ailpay_five_code)) + 1):
            code = (By.XPATH, "//input[@class='input'][%d]" % ele)  # 帳號類型
            self.type(code, '1')


    web_deposit_enter = (By.XPATH, "//*[text()='线上支付']/..")

    # DEPOSIT PAGE (公司入款)
    deposit_next_btn = (By.XPATH, "//div[text()='下一步']")
    deposit_transfer_amount_input = (By.XPATH, "//label[text()='存入金额']/../input")
    DEPOSIT_TRANSFER_time_INPUT = (By.XPATH, "//label[text()='存入时间']/../input")
    deposit_transfer_name_input = (By.XPATH, "//label[text()='存款姓名']/../input")
    deposit_transfer_depositotp_input = (By.XPATH, "//div[(contains(@data-bind,'OTP'))and not(contains(@style,'none'))]//input")
    deposit_transfer_bank_select = (By.XPATH, "//label[text()='转帐银行']/../select")
    deposit_transfer_cardnumber_select = (By.XPATH, "//label[text()='转帐卡号']/../input")
    deposit_submit_btn = (By.XPATH, "//div[text()='确认提交']")
    deposit_dialog_message = (By.XPATH, "//h2[@class='swal2-title']")
    deposit_dialog_ok_btn = (By.XPATH, "//button[@class='swal2-confirm swal2-styled']")
    deposit_airpay_name_input = (By.XPATH, "//input[@placeholder='请填写汇款人姓名']")
    deposit_upload_photo = (By.XPATH, "//input[@type='file']")

    def pay_methods(self,name):
        pay_method = (By.XPATH, "//li[text()='%s']"%name)  # 支付方式
        return pay_method

    Onlinepaytitle = (By.XPATH, "//h1[text()='线上支付']")  # 線上支付
    unionpay_title = (By.XPATH, "//h1[text()='银联支付']")  # 銀聯支付
    Jdpaypaytitle = (By.XPATH, "//h1[text()='京东支付']")  # 京東支付
    wellpay_title = (By.XPATH, "//h1[contains(text(),'顺付WellPay')]")  # 順付入款
    deposit_submit_btn2 = (By.XPATH, "//div[contains(text(),'立即支付')]")  # 立即支付

    # OLD VERSION DEPOSIT PAGE (舊公司入款流程)
    OLD_COMPANY_deposit_enter = (By.XPATH, "//*[@class='pay-left' and text()='公司入款']")
    OLD_DEPOSIT_TRANSFER_AMOUNT_INPUT = (By.XPATH, "//input[contains(@data-bind,'transferamount')]")
    OLD_deposit_transfer_name_input = (By.XPATH, "//input[contains(@data-bind,'cardname')]")
    OLD_deposit_submit_btn = (By.XPATH, "//div[contains(@data-bind,'submit')]")

    # WITHDRAW PAGE (線上取款)
    Withdraw_hour = (By.XPATH, "//span[@data-bind='text:withdrawhours']")
    Withdraw_free_time = (By.XPATH, "//span[@data-bind='text:withdrawtimes']")
    Withdraw_time = (By.XPATH, "//span[@data-bind='text:times']")
    withdraw_min = (By.XPATH, "//span[@data-bind='text:withdrawmin']")
    Withdraw_Max = (By.XPATH, "//span[@data-bind='text:withdrawmax']")

    withdraw_refunddiscount = (By.XPATH, "//*[@*='text: refunddiscount']")
    withdraw_auditcharge = (By.XPATH, "//*[@*='text: auditcharge']")
    withdraw_charge = (By.XPATH, "//*[@*='text: charge']")
    withdraw_apply= (By.XPATH, "//td[@data-bind='text:amount' or contains(@data-bind,'toFixed')]")
    withdraw_amount_input = (By.XPATH, "//input[@type='number']")
    withdraw_password = (By.XPATH, "//input[@type='password']")
    withdraw_submit_btn = (By.XPATH, "//a[contains(@data-bind, 'submit')]")
    withdraw_closed = (By.XPATH, "//div[@class='btn bill-hide']")
    withdraw_message = (By.XPATH, "//div[@class='audit-end' and @style='']/h1")

    withdraw_account = (By.XPATH, "//select[@class='select-style']")
    withdraw_account_now =(By.XPATH, "//div[@class='bank-message']")
    withdraw_account_bank = (By.XPATH, "//select[@class='select-style']/option[contains(text(),'银行')]")
    withdraw_account_wellpay = (By.XPATH, "//div[contains(@class,'bank-message') and contains(text(),'顺付-Well Pay')]")
    
    withdraw_use_bank = (By.XPATH, "//p[text()='银行卡']")
    withdraw_use_wallet = (By.XPATH, "//p[text()='虚拟钱包']")
    withdraw_use_wellpay = (By.XPATH, "//p[text()='顺付-Well Pay']")
    withdraw_use_not_add = (By.XPATH, "//div[@style='']//*[contains(text(),'前往绑定')]")

    # 確認線上取款後的資訊
    withdraw_apply_next=(By.XPATH, "//em[contains(@data-bind,'total')]")
    withdraw_refunddiscount_next = (By.XPATH, "//em[contains(@data-bind,'refunddiscount')]")
    withdraw_auditcharge_next = (By.XPATH, "//em[contains(@data-bind,'auditcharge')]")
    withdraw_charge_next = (By.XPATH, "//em[contains(@data-bind,'charge')]")
    withraw_total_next= (By.XPATH, "//em[contains(@data-bind,'amount')]")

    # wallet PAGE (額度轉換) ===========================================================
    wallet_conversion_loading_mask = (By.ID, "betAreaLoading")
    # 額度刷新
    wallet_refresh_btn = (By.XPATH, "//div[@class='refresh-all']")

    # 一鍵歸戶
    wallet_return_btn = (By.XPATH, "//span[text()='一键归户']/..")
    wallet_check = (By.XPATH, "//li//span[contains(@class,'_balance')]")
    wallet_maintain = (By.XPATH, "//li[@class='disabled']//*[contains(text(),'维护中')]")
    maintain_money = (By.XPATH, "//li[@class='disabled']/span")
    
    # 錢包名稱 & 錢包金額
    get_name_and_money = (By.XPATH, "//li[contains(@data-bind, 'from')]")

    # 錢包選擇鈕
    @staticmethod
    def wallet_choosing_btn(from_or_to, thirdparty_name):
        locator = (By.XPATH, "//span[contains(@class,'%s')]/../../li[contains(@data-bind,'%s')]" % (thirdparty_name, from_or_to))
        return locator


    @staticmethod
    def wallet_choosing_btn_maintenance(thirdparty_name):
        locator = (By.XPATH, "//li[(@class='disabled')and not(@style='display: none;')]//span[@class='%s_balance']" % thirdparty_name)
        return locator


    # 被選錢包額度
    @staticmethod
    def wallet_choosing_amount(from_or_to, thirdparty_name):
        locator = (By.XPATH, "//li[contains(@data-bind,'%s')]//span[contains(@class,'%s')]" % (from_or_to, thirdparty_name))
        return locator

    @staticmethod # NWAP選擇銀行
    def change_bank(num=1):
        into = (By.XPATH, f"(//a[@class='list-item'])[{num}]")
        return into

    # 額度轉換金額
    wallet_conversion_amount_input = (By.XPATH, "//input[@placeholder='填入金额']")
    # 提交
    wallet_conversion_submit = (By.XPATH, "//div[@class='btn' and text()='提交']")
    # 額度轉換Alert處理
    wallet_conversion_alertclose_message = (By.XPATH, "//div[@data-context='transfer.message']//span")
    wallet_conversion_alertclose_message_l = (By.XPATH, "//div[@data-bind='foreach: contents']//span")
    wallet_conversion_alertclose_btn = (By.XPATH, "//div[@data-context='transfer.message']//div[@class='alert-close btn']")
    wallet_conversion_alertclose_btn_L = (By.XPATH, "//div[@class='alert-close btn']")
    wallet_conversion_erroralertclose_message = (By.XPATH, "//*[text()='系统忙碌中，请稍后再试']")
    wallet_conversion_erroralertclose_btn = (By.XPATH, "//*[text()='错误提示']/../*[text()='确认关闭']")

    # 我的資料 ===========================================================================
    # 修改登入密碼 (Change LoginPassword)
    # cgpwd_input_oldpwd = (By.XPATH, "//*[text()='旧的密码']/..//input")
    cgpwd_input_oldpwd = (By.XPATH, "//*[@type='password' and @placeholder='请输入旧的密码']")
    cgpwd_input_newpwd = (By.XPATH, "//*[@type='password' and @placeholder='请输入新的密码']")
    cgpwd_input_newpwd2 = (By.XPATH, "//*[@type='password' and @placeholder='请再次填入新密码']")
    cgpwd_input_securitycode = (By.XPATH, "//*[@type='password' and @placeholder='填入您提款密码']")
    cgpwd_submit = (By.XPATH, "//*[@class='btn-submit show-alert' and @value='确认提交']")
    cgpwd_seccess_point = (By.XPATH, "//*[text()='您的资料已修改']")
    cgpwd_alert_close = (By.XPATH, "//*[text()='您的资料已修改']/../div[text()='确认关闭']")

    # 修改提款密碼 (Change SecurityPassword)
    cgspwd_input_oldpwd = (By.XPATH, "(//label[contains(., '旧的提款密码')]/following::input)[1]")
    cgspwd_input_newpwd = (By.XPATH, "(//label[contains(., '新的提款密码')]/following::input)[1]")
    cgspwd_input_newpwd2 = (By.XPATH, "(//label[contains(., '重复提款密码')]/following::input)[1]")
    cgspwd_submit = (By.XPATH, "//*[@value='确认提交']/../input")
    cgspwd_seccess_point = (By.XPATH, "//*[text()='您的资料已修改']")
    cgspwd_alert_close = (By.XPATH, "//*[text()='您的资料已修改']/../div[text()='确认关闭']")

    # 修改聯絡方式 (Change Contact)
    contact_edit_btn = (By.XPATH, "//*[text()='[修改]' and @style != 'display: none;']")
    contact_input_change_email = (By.XPATH, "//div[(@style != 'display: none') and (@data-bind='visible: emailEdit')]//input")
    contact_input_change_phone = (By.XPATH, "//div[(@style != 'display: none') and (@data-bind='visible: mobileEdit')]//input")
    contact_input_change_qq = (By.XPATH, "//div[(@style != 'display: none') and (@data-bind='visible: qqEdit')]//input")
    contact_input_change_wechat = (By.XPATH, "//div[(@style != 'display: none') and (@data-bind='visible: wechatEdit')]//input")
    contact_input_change_spwd = (By.XPATH, "//input[@data-bind='value: securitycode']")
    contact_submit = (By.XPATH, "//input[@class='btn-submit']")
    contact_seccess_point = (By.XPATH, "//*[text()='您的资料已修改']")
    contact_alert_close = (By.XPATH, "//*[text()='您的资料已修改']/../div[text()='确认关闭']")
    contact_edit_mobile_btn = (By.XPATH, "(//*[text()='[修改]'])[2]")

    # 修改出款銀行 (Change BANK card)
    profile_menu_cardnumber = (By.XPATH,"//input[@data-bind='value: cardnumber, enable: firsttime']")
    bank_input_cardbranch_num = (By.XPATH, "//input[@placeholder = '省(自治区)']")
    bank_input_cardcity_num = (By.XPATH, "//input[@placeholder = '城市(区)']")
    bank_input_securitycode = (By.XPATH, "//input[@type= 'password']")
    bank_submit = (By.XPATH, "//*[@value='确定新增']")
    bank_seccess_point = (By.XPATH, "//*[text()='您的资料已修改']")
    bank_alert_close = (By.XPATH, "//*[text()='您的资料已修改']/../div[text()='确认关闭']")
    bank_select_btn = (By.XPATH, "//p[text()='请选择']")
    bank_card = (By.XPATH, "//input[@placeholder = '请输入银行卡号']")
    card_method = (By.XPATH, "//p[@class = 'card-method__text' and text()='银行卡']")
    card_method_virtual = (By.XPATH, "//p[@class = 'card-method__text' and text()='虚拟钱包']")
    card_method_wellpay = (By.XPATH, "//p[@class = 'card-method__text' and text()='顺付-Well Pay']")
    credit_items = (By.XPATH, "//div[@class='credit__item']")
    add_alert = (By.XPATH, "//div[@style='']/div[@class='alert-content']")
    alert_close = (By.XPATH, "//div[@style='']//div[@class='alert-close btn']")

    # 綁定虛擬錢包_帳戶安全
    bind_mobile = (By.XPATH, "//div[@data-bind='visible: bindMobileShow' and @style='']")
    bind_mobile_input = (By.XPATH, "//input[@data-bind='numeric, textInput: bindPhoneNumber']")
    bind_securitycode = (By.XPATH, "//input[@data-bind='numeric, textInput: securityNumber']")
    bind_confirm = (By.XPATH, "//a[text()='确认送出']")
    verify_mobile = (By.XPATH, "//div[@data-bind='visible: verifyMobileShow' and @style='']")
    verify_mobile_input =(By.XPATH, "//input[@data-bind='numeric, textInput: phoneNumber']")
    verify_confirm = (By.XPATH, "//a[text()='验证']")
    verify_cancel = (By.XPATH, "//div[@data-bind='visible: verifyMobileShow']//*[text()='取消']")

    # 虛擬錢包
    credit_item_add = (By.XPATH, "//div[@class='credit__item']//p[contains(text(),'新增虚拟钱包')]")
    credit_item_cgpay = (By.XPATH, "//div[@class='credit__item']//p[contains(text(),'CGPay')]")
    credit_item_wellpay = (By.XPATH, "//div[@class='credit__item']//p[contains(text(),'顺付-Well Pay')]")

    # 綁定頁麵包屑    
    def breadcrumb_item(self, name):
        pay_method = (By.XPATH, f"//li[@class='breadcrumb__item']/span[text()='{name}']")  # 支付方式
        return pay_method

    virtual_card = (By.XPATH, "//input[@placeholder = '请输入钱包地址']")
    wallet_select = (By.XPATH, "//input[@placeholder='请选择钱包名称']/preceding-sibling::select")
    wallet_select_now = (By.XPATH, "(//label[text()='钱包名称']/..)[1]")
    wallet_option_cgpay = (By.XPATH, "//option[@value='cgpay']")
    wallet_option_wellpay = (By.XPATH, "//option[@value='zqb']")

class MemberPage(BasePage):
    # 前台確認支付寶/微信面對面
    def check_qr_deposit(self, name, user, paytitle, money):
        self.wait_loading_finish()
        MemberPageLocator.deposit_name(self, name)  # 點擊支付寶 or 微信
        self.wait_loading_finish()
        MemberPageLocator.paytitle(self, paytitle)  # 點擊 面對面
        self.wait_loading_finish()
        self.type(MemberPageLocator.deposit_amount, money)  # 輸入金額
        self.click(MemberPageLocator.deposit_qrcode_next_btn)

        message = self.get_text(MemberPageLocator.user_name_qr)
        # user = '%s' % user + datetime.datetime.now().strftime('%m%d_') #bot+日期,確保當日建立
        assert str(message).__contains__(user), '找不到開戶人名稱:%s' % user

    def get_real_money(self, money_to):
        real_money = self.get_text(MemberPageLocator.real_money)
        assert float(real_money) - float(money_to) < 1, '儲值金額與實際金額誤差超過1 實際金額:%s 輸入金額:%s' %(real_money, money_to)
        return real_money

    # 前台確認支付寶/微信/USDT轉帳
    def checktr_deposit(self, name, user, paytitle, money):
        self.wait_loading_finish()
        MemberPageLocator.deposit_name(self, name)  # 點擊支付寶 or 微信
        self.wait_loading_finish()
        MemberPageLocator.paytitle(self, paytitle)  # 點擊 轉帳
        self.wait_loading_finish()

        if name == '支付宝':
            MemberPageLocator.users_find_and_check(self, user)
            self.type(MemberPageLocator.deposit_amount, money)
            self.click(MemberPageLocator.deposit_next_btn)
            self.wait_loading_finish()
            self.type(MemberPageLocator.deposit_airpay_name_input, '機器人測試')
        elif name =='微信':
            self.type(MemberPageLocator.deposit_amount, money)
            self.click(MemberPageLocator.deposit_next_btn)
            self.wait_loading_finish()
            MemberPageLocator.users_find_and_check(self, user)
        
        # USDT, user帶錢包地址
        else:
            MemberPageLocator.address_find_and_check(self, user)

    # 確認公司入款/USDT/UPI接口
    def check_company_deposit(self, name='', user=''):
        if type(name) == list:
            for bank in name:
                 MemberPageLocator.deposit_name(self, bank, True)
            return

        MemberPageLocator.deposit_name(self, name)  # 點擊公司入款
        self.wait_loading_finish()
        MemberPageLocator.users_find_and_check(self, user)

    # 確認線上支付建立成功
    def check_onlinepay(self, name='', title='', pay_method=''):
        if type(name) == list:
            for bank in name:
                 MemberPageLocator.deposit_name(self, bank, True)
            return

        MemberPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()
        message = self.get_text(MemberPageLocator.Onlinepaytitle)
        assert message == title, '找不到名稱:%s' % title

        self.wait_visibility(MemberPageLocator.deposit_submit_btn2) # 等待頁面切換完成
        assert self.is_element_finded(MemberPageLocator.pay_methods(self, pay_method)) == True, '無指定支付方式'
        self.click(MemberPageLocator.pay_methods(self, pay_method))
        message_p = self.get_text(MemberPageLocator.pay_methods(self, pay_method))
        assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method

    # 確認銀聯支付建立成功
    def check_unionpay(self, name, Title, pay_method):
        self.wait_loading_finish()
        MemberPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()
        message = self.get_text(MemberPageLocator.unionpay_title)
        assert message == Title, '找不到名稱:%s' % Title

        assert self.is_element_finded(MemberPageLocator.pay_methods(self,pay_method)) == True, '無指定支付方式'
        self.click(MemberPageLocator.pay_methods(self,pay_method))
        message_p = self.get_text(MemberPageLocator.pay_methods(self,pay_method))
        assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method

    # 確認京東支付建立成功
    def check_jdpay(self, name, title, pay_method):
        self.wait_loading_finish()
        MemberPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.Jdpaypaytitle)
        message = self.get_text(MemberPageLocator.Jdpaypaytitle)
        assert message == title, '找不到名稱:%s' %title

        assert self.is_element_finded(MemberPageLocator.pay_methods(self, pay_method)) == True, '無指定支付方式'
        self.click(MemberPageLocator.pay_methods(self,pay_method))
        message_p = self.get_text(MemberPageLocator.pay_methods(self, pay_method))
        assert message_p == pay_method, '找不到支付方式名稱:%s' %pay_method

    # 確認順付WellPay帳號入款建立成功
    def check_wellpay_account(self, name='', title='', pay_method=''):
        self.wait_loading_finish()
        MemberPageLocator.deposit_name(self, name)
        self.wait_loading_finish()
        MemberPageLocator.paytitle(self, title)
        self.wait_loading_finish()
        message = self.get_text(MemberPageLocator.wellpay_title)    # 順付入款
        assert message == title, '找不到名稱:%s' % title

        self.wait_visibility(MemberPageLocator.deposit_next_btn) # 等待頁面切換完成
        assert self.is_element_finded(MemberPageLocator.pay_methods(self, pay_method)) == True, '無指定支付方式'
        self.click(MemberPageLocator.pay_methods(self, pay_method))
        message_p = self.get_text(MemberPageLocator.pay_methods(self, pay_method))
        assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method

    # 儲值 線上支付
    def do_all_online_deposit(self, money, pay_method):
        self.type(MemberPageLocator.deposit_amount, money)  # 存入金額
        self.click(MemberPageLocator.pay_methods(self, pay_method))
        self.click(MemberPageLocator.deposit_submit_btn2)  # 確認提交
        self.sleep(5)
        self.switch_home_page()
        self.sleep(2)
        self.wait_loading_finish()

    # 儲值 公司入款
    def do_company_deposit(self, user, money, otp=''):
        self.type(MemberPageLocator.deposit_transfer_amount_input, money)  # 存入金額
        self.type(MemberPageLocator.deposit_transfer_name_input, user)  # 存款姓名
        if self.is_element_finded(MemberPageLocator.deposit_transfer_depositotp_input) is True:
            self.type(MemberPageLocator.deposit_transfer_depositotp_input, otp)
        else:
            pass
        
        # 上傳付款圖片
        if platform.system() == 'Linux':
            folder_path = os.path.abspath(__file__).split('/Project')[0]
        else:
            folder_path = os.path.abspath(__file__).split('\Project')[0]
        dir_path = "{0}/image/web/setting_photo/QA_pay_done.png".format(folder_path)
        self.type(MemberPageLocator.deposit_upload_photo, dir_path)
        self.sleep(2)

        self.click(MemberPageLocator.deposit_submit_btn)  # 確認提交
        self.wait_visibility(MemberPageLocator.deposit_dialog_message)
        assert self.get_text(MemberPageLocator.deposit_dialog_message) == '申请提交成功'
        self.sleep(1)
        self.click(MemberPageLocator.deposit_dialog_ok_btn)
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.search_today)

    # 儲值 支付寶/微信 面對面
    def do_desposit_weChat_alipayf2f(self, otp=''):
        MemberPageLocator.deposit_wechat_ailpay_five_code(self)
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.deposit_transfer_depositotp_input) is True:
            self.type(MemberPageLocator.deposit_transfer_depositotp_input, otp)
        else:
            pass       
        self.click(MemberPageLocator.deposit_f2f_submit_btn)  # 確認提交
        assert self.get_text(MemberPageLocator.deposit_dialog_message) == '申请提交成功'
        self.click(MemberPageLocator.deposit_dialog_ok_btn)
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.search_today)

    # 儲值 支付寶/微信 轉帳
    def do_desposit_wechat_alipay_transfer(self, otp=''):
        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.deposit_transfer_depositotp_input) is True:
            self.type(MemberPageLocator.deposit_transfer_depositotp_input, otp)
        else:
            pass       
        self.click(MemberPageLocator.deposit_submit_btn)  # 確認提交
        assert self.get_text(MemberPageLocator.deposit_dialog_message) == '申请提交成功'
        self.click(MemberPageLocator.deposit_dialog_ok_btn)
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.search_today)

    def real_output_amount(self,money_to):
        total_amount=float(self.get_text(MemberPageLocator.withraw_total_next))
        withdraw_apply=float(self.get_text(MemberPageLocator.withdraw_apply_next))
        withdraw_refunddiscount=float(self.get_text(MemberPageLocator.withdraw_refunddiscount_next))
        withdraw_audicharge=float(self.get_text(MemberPageLocator.withdraw_auditcharge_next))
        withdraw_charge=float(self.get_text(MemberPageLocator.withdraw_charge_next))

        total_charge = total_amount + withdraw_refunddiscount + withdraw_audicharge + withdraw_charge

        # assert round(float(withdraw_apply)+float(withdraw_charge),2) == round(float(money_to),2) or int(float(withdraw_apply)+float(withdraw_charge))== int(float(money_to)),'申請額度與顯示不相符'
        assert round(withdraw_apply+withdraw_refunddiscount+withdraw_audicharge+withdraw_charge,2)==round(total_amount,2),'加上所有手續費後金額不正確'
        withdraw_apply = "%.2f" %withdraw_apply
        return total_amount,withdraw_apply

    # 線上出款
    def do_withdraw(self, amount, withdraw_pwd):
        self.wait_loading_finish()

        self.wait_visibility(MemberPageLocator.withdraw_use_bank)   # 確認出款顯示銀行卡方式
        self.click(MemberPageLocator.withdraw_use_bank)             # 點擊取款方式-銀行卡
        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.withdraw_use_not_add) is False, "尚未成功绑定银行卡"
        
        new_amount = (float(amount) + float(self.get_text(MemberPageLocator.withdraw_refunddiscount)) + float(
            self.get_text(MemberPageLocator.withdraw_auditcharge)) + float(
            self.get_text(MemberPageLocator.withdraw_charge)))
        new_amount = str(math.ceil(new_amount)) 

        self.type(MemberPageLocator.withdraw_amount_input, new_amount)
        self.type(MemberPageLocator.withdraw_password, withdraw_pwd)
        self.click(MemberPageLocator.withdraw_submit_btn)
        self.wait_loading_finish()
        try:
            self.wait_visibility(MemberPageLocator.withdraw_message)
            self.get_text(MemberPageLocator.withdraw_message) == '申请成功送出，已尽快为您处理，谢谢!'
            total_amount, withdraw_apply = self.real_output_amount(amount)
            self.click(MemberPageLocator.withdraw_closed)
        except:
            self.wait_alert_present()
            message = self.get_alert_message()
            self.accept_alert()
            raise EOFError(message)
        
        return total_amount,withdraw_apply


    # 線上出款 cgpay
    def do_cgpay_withdraw(self, amount, withdraw_pwd):
        self.wait_loading_finish()

        self.wait_visibility(MemberPageLocator.withdraw_use_bank)   # 確認出款顯示虛擬錢包方式
        self.click(MemberPageLocator.withdraw_use_wallet)           # 點擊取款方式-虛擬錢包

        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.withdraw_use_not_add) is False, "尚未成功绑定虛擬錢包"
        self.wait_visibility(MemberPageLocator.withdraw_amount_input)
        assert 'CGPay' in self.get_text(MemberPageLocator.withdraw_account_now), '未新增虛擬錢包'
        
        new_amount = (float(amount) + float(self.get_text(MemberPageLocator.withdraw_refunddiscount)) + float(
            self.get_text(MemberPageLocator.withdraw_auditcharge)) + float(
            self.get_text(MemberPageLocator.withdraw_charge)))
        new_amount = str(math.ceil(new_amount)) 

        self.type(MemberPageLocator.withdraw_amount_input, new_amount)
        self.type(MemberPageLocator.withdraw_password, withdraw_pwd)
        self.click(MemberPageLocator.withdraw_submit_btn)
        self.wait_loading_finish()
        try:
            self.wait_visibility(MemberPageLocator.withdraw_message)
            self.get_text(MemberPageLocator.withdraw_message) == '申请成功送出，已尽快为您处理，谢谢!'
            total_amount, withdraw_apply = self.real_output_amount(amount)
            self.click(MemberPageLocator.withdraw_closed)
        except:
            self.wait_alert_present()
            message = self.get_alert_message()
            self.accept_alert()
            raise EOFError(message)
        
        return total_amount,withdraw_apply

    # 線上出款 WellPay
    def do_wellpay_withdraw(self, amount, withdraw_pwd):
        self.wait_loading_finish()

        self.wait_visibility(MemberPageLocator.withdraw_use_wellpay)    # 確認出款顯示顺付-Well Pay錢包方式
        self.click(MemberPageLocator.withdraw_use_wellpay)              # 點擊取款方式-顺付-Well Pay錢包

        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.withdraw_use_not_add) is False, "尚未成功绑定顺付-Well Pay"
        self.wait_visibility(MemberPageLocator.withdraw_amount_input)
        self.sleep(1)
        assert self.is_element_finded(MemberPageLocator.withdraw_account_wellpay), '收款虛擬錢包未新增顺付-Well Pay'
        
        new_amount = (float(amount) + float(self.get_text(MemberPageLocator.withdraw_refunddiscount)) + float(
            self.get_text(MemberPageLocator.withdraw_auditcharge)) + float(
            self.get_text(MemberPageLocator.withdraw_charge)))
        new_amount = str(math.ceil(new_amount)) 

        self.type(MemberPageLocator.withdraw_amount_input, new_amount)
        self.type(MemberPageLocator.withdraw_password, withdraw_pwd)
        self.click(MemberPageLocator.withdraw_submit_btn)
        self.wait_loading_finish()
        try:
            self.wait_visibility(MemberPageLocator.withdraw_message)
            self.get_text(MemberPageLocator.withdraw_message) == '申请成功送出，已尽快为您处理，谢谢!'
            total_amount, withdraw_apply = self.real_output_amount(amount)
            self.click(MemberPageLocator.withdraw_closed)
        except:
            self.wait_alert_present()
            message = self.get_alert_message()
            self.accept_alert()
            raise EOFError(message)
        
        return total_amount,withdraw_apply


    # 抓取 線上取款 之值 (進入銀行卡出款確認)
    def get_online_withdraw_info(self):
        self.wait_visibility(MemberPageLocator.withdraw_use_bank)   # 確認出款顯示銀行卡方式
        self.click(MemberPageLocator.withdraw_use_bank)             # 點擊取款方式-銀行卡
        self.sleep(1)
        assert self.is_element_finded(MemberPageLocator.withdraw_use_not_add) is False, "尚未绑定银行卡"
        self.type(MemberPageLocator.withdraw_amount_input, 100000)     # 輸入提款金額
        hour = self.get_text(MemberPageLocator.Withdraw_hour)           # 取得出款時長
        free_time = self.get_text(MemberPageLocator.Withdraw_free_time) # 取得免費次數
        time = self.get_text(MemberPageLocator.Withdraw_time)           # 取得提款次數
        charge = self.get_text(MemberPageLocator.withdraw_charge)       # 取得提款手續
        min_ = self.get_text(MemberPageLocator.withdraw_min)             # 取得最小出款
        Max = self.get_text(MemberPageLocator.Withdraw_Max)             # 取得最大出款

        return hour, free_time, time, charge, min_, Max

    # 額度轉換區 =================================================================================================
    def wait_wallet_loading_start(self):
        if self.is_element_finded(MemberPageLocator.wallet_conversion_loading_mask) is True:
            self.wait_visibility(MemberPageLocator.wallet_conversion_loading_mask)

    def wait_wallet_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(MemberPageLocator.wallet_conversion_loading_mask) is True:
            self.wait_invisibility(MemberPageLocator.wallet_conversion_loading_mask)

    # 判斷錢包是否低於1元(主錢包除外)
    def do_wallet_check(self):
        self.wait_loading_finish()
        for loop in range(1,7):
            total = 0
            counts = 0
            wallet=0
            maintain_list = []
            if self.is_element_finded(MemberPageLocator.wallet_maintain) == True:
                amount = 0
                maintain_list = [maintain.text for maintain in self.find_elements(MemberPageLocator.maintain_money) if float(maintain.text) >= 1]
            for money in self.find_elements(MemberPageLocator.wallet_check):
                if float(money.text) >= 1:
                    counts += 1
                    if counts > 1 and float(money.text) != wallet and maintain_list != []:
                        if float(money.text) == float(maintain_list[amount]):
                            if amount + 1  < len(maintain_list):
                                amount += 1
                            else:
                                maintain_list = []
                            counts -= 1
                    # print(money.get_attribute('class').rstrip('_balance'),'錢包金額: %.2f RMB' % float(money.text)) # 錢包多餘1元的(包含轉出/轉入兩邊)
                    if wallet==0:
                        wallet=float(money.text)

                if counts<2 and float(money.text) < wallet:
                    total=total+float(money.text)
            if counts < 3:
                break
            else:
                if loop==6:
                     assert counts < 3, '錢包歸戶失敗,重複刷新次數:%s'%loop
                self.sleep(10)
                self.do_walletre_fresh()
        self.wait_loading_finish()
        assert counts < 3, '錢包歸戶失敗'
        assert round(wallet+total,2)==round(float(self.get_text(MemberPageLocator.owner_total_money)),2),'帳戶餘額與額度轉換錢包不相符'
        return round(total,2)

    # 第三方主錢包
    def doCMmoney(self):
        return self.get_text(MemberPageLocator.wallet_check)

        # 刷新額度

    def do_walletre_fresh(self):
        self.wait_loading_finish()  # 等待頁面讀取
        self.wait_visibility(MemberPageLocator.wallet_refresh_btn)
        self.click(MemberPageLocator.wallet_refresh_btn)  # 全部錢包刷新
        # self.wait_wallet_loading_start()  # 等待額度轉換Loading開始
        self.wait_wallet_loading_finish()  # 等待額度轉換Loading結束
        self.refresh_browser()
        self.wait_loading_finish()  # 等待頁面讀取

        # 一鍵歸戶

    def do_wallet_return(self):
        self.wait_loading_finish()  # 等待頁面讀取
        self.click(MemberPageLocator.wallet_return_btn)
        message = self.get_text(MemberPageLocator.wallet_conversion_alertclose_message_l)
        self.click(MemberPageLocator.wallet_conversion_alertclose_btn_L)  # 關閉ALERT
        assert str(message).__contains__('成功'), '一鍵歸戶失敗'
        self.sleep(30)

        # 額度轉換

    def do_wallet_conversion(self, wallet_from, wallet_to, amount):
        self.wait_loading_finish()

        if datetime.time(9) < datetime.datetime.now().time() < datetime.time(11) and wallet_to == 'bbin':
            self.test_skip('BBIN 維護中')

        if self.is_element_finded(MemberPageLocator.wallet_choosing_btn('from', wallet_to)) is False:
            wallet_to=wallet_to.upper
            self.test_skip('無串接第三方品牌: %s'%(wallet_to))

        if self.is_element_finded(MemberPageLocator.wallet_choosing_btn_maintenance(wallet_from)) is True or \
               self.is_element_finded(MemberPageLocator.wallet_choosing_btn_maintenance(wallet_to)) is True:
            self.test_skip('該通道額度轉換-維護中')

        try:
            self.wait_visibility(MemberPageLocator.wallet_choosing_btn('from', wallet_from))
            self.click(MemberPageLocator.wallet_choosing_btn('from', wallet_from))  # 選轉出錢包
        except BaseException:
            print("Can't find %s wallet From:"% wallet_from)
            raise

        try:
            self.wait_visibility(MemberPageLocator.wallet_choosing_btn('to', wallet_to))
            self.click(MemberPageLocator.wallet_choosing_btn('to', wallet_to))  # 選轉入錢包
        except BaseException:
            print("Can't find %s wallet To:"% wallet_to)
            raise

        money_before = float(self.find_element(MemberPageLocator.wallet_choosing_amount('from', 'cp')).text)  # 主錢包

        before_from_amount = float(
            self.find_element(MemberPageLocator.wallet_choosing_amount('from', wallet_from)).text)  # 轉出錢包原額度
        before_to_amount = float(
            self.find_element(MemberPageLocator.wallet_choosing_amount('to', wallet_to)).text)  # 轉入錢包原額度

        self.type(MemberPageLocator.wallet_conversion_amount_input, str(amount))  # 輸入轉換額度
        self.click(MemberPageLocator.wallet_conversion_submit)  # 送出
        self.wait_wallet_loading_finish()  # 等額度轉換Loading結束

        try:
            try:
                # 额度转换成功
                message = self.wait_visibility(MemberPageLocator.wallet_conversion_alertclose_message).text
                self.click(MemberPageLocator.wallet_conversion_alertclose_btn)  # 關閉ALERT
            except:
                # 申请成功送出，系统会在1分钟内完成额度转换，请注意查收
                message = self.wait_visibility(MemberPageLocator.wallet_conversion_alertclose_message_l).text
                self.click(MemberPageLocator.wallet_conversion_alertclose_btn_L)  # 關閉ALERT
        except TimeoutException:
            message = self.wait_visibility(MemberPageLocator.wallet_conversion_erroralertclose_message).text
            self.click(MemberPageLocator.wallet_conversion_erroralertclose_btn)

        self.wait_wallet_loading_finish()  # 等待重整Loading結束

        for loop in range(1,2):
            try:
                after_from_amount = float(
                    self.find_element(MemberPageLocator.wallet_choosing_amount('from', wallet_from)).text)  # 轉出錢包現額度
                after_to_amount = float(
                    self.find_element(MemberPageLocator.wallet_choosing_amount('to', wallet_to)).text)  # 轉入錢包現額度

                if str(message).__contains__('成功'):
                    self.wait_loading_finish()  # 等待重整Loading結束
                    assert before_from_amount + before_to_amount == after_from_amount + after_to_amount and before_from_amount > \
                           after_from_amount, message + ': from %s to %s, before: %s & %s, after %s & %s' % (
                        wallet_from, wallet_to,
                        before_from_amount, before_to_amount, after_from_amount, after_to_amount)
                    break
                else:
                    assert False, message + ': from %s to %s' % (wallet_from, wallet_to)
                    break
            except BaseException as e:
                if loop == 10:
                    print("額度轉換錯誤,刷新次數:%d"%loop)
                    raise e
            # 全部刷新異常等待
            self.sleep(5)
            self.do_walletre_fresh()

        return money_before

     # 交易流水
    def into_wallet_Report(self):
        self.click(MemberPageLocator.menu_history)
        self.wait_loading_finish()

    def trading_flow(self,wallet_from,amount,money_before):
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.menu_history)
        self.click(MemberPageLocator.menu_history)
        self.wait_loading_finish()

        for i in range(0, 3):
            self.refresh_browser()
            self.wait_visibility(MemberPageLocator.search_all)
            self.click(MemberPageLocator.search_all)
            self.wait_visibility(MemberPageLocator.search_info)
            self.click(MemberPageLocator.search_info)
            self.wait_loading_finish()
            self.sleep(2)
            self.wait_visibility(MemberPageLocator.amount_change)
            
            if wallet_from=='cp':
                self.sleep(5)
                money_after = money_before-abs(float(self.get_text(MemberPageLocator.amount_change)))
                # 由於交易流水會過慢,所以給予三次
                try:
                    assert self.get_text(MemberPageLocator.amount_change)=='-1','交易流水錯誤'
                    break
                except:
                    if i == 2:
                        assert self.get_text(MemberPageLocator.amount_change)=='-1','交易流水錯誤'
            else:
                money_after = money_before+abs(float(self.get_text(MemberPageLocator.amount_change)))
                # 由於交易流水會過慢,所以給予三次
                try:
                    assert self.get_text(MemberPageLocator.amount_change)=='1','交易流水錯誤'
                    break
                except:
                    if i == 2:
                        assert self.get_text(MemberPageLocator.amount_change)=='-1','交易流水錯誤'

        assert money_after ==float(self.get_text(MemberPageLocator.money_now)),'交易流水錯誤'
        assert abs(float(self.get_text(MemberPageLocator.amount_change)))==amount,'交易流水錯誤'

        amount_time=self.get_text(MemberPageLocator.amount_time) # 儲值時間
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        assert str(amount_time)[:10]==now_time,'儲值時間不正確:%s'%amount_time
        self.click(MemberPageLocator.menu_wallet)



    # 左側選單 ==========================================================
    def into_L_MenuLogout(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_logout)

    def into_L_MenuDeposit(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_deposit)

    def into_L_MenuWithDraw(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_withdraw)

    def into_L_MenuMywallet(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_mywallet)

    def into_L_MenuBettingRecord(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_bettingrecord)

    def into_L_MenuMyProfile(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_menu_myprofile)

    def into_L_MenuMyMessage(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.l_meny_mymessage)

    # 我的資料 ==============================================================
    def do_change_password(self, old_pwd, new_pwd, securitycode):
        # 我的資料分頁切換至修改密碼
        self.wait_loading_finish()
        self.click(MemberPageLocator.profile_menu_cg_pwd)

        self.wait_loading_finish()
        self.type(MemberPageLocator.cgpwd_input_oldpwd, old_pwd)
        self.type(MemberPageLocator.cgpwd_input_newpwd, new_pwd)
        self.type(MemberPageLocator.cgpwd_input_newpwd2, new_pwd)
        self.type(MemberPageLocator.cgpwd_input_securitycode, securitycode)
        self.click(MemberPageLocator.cgpwd_submit)

        self.wait_visibility(MemberPageLocator.cgpwd_seccess_point)
        assert self.is_element_finded(MemberPageLocator.cgpwd_seccess_point),'修改密碼錯誤'
        self.click(MemberPageLocator.cgpwd_alert_close)

    def doChangeSecurityPWD(self, old_spwd, new_spwd):
        # 我的資料分頁切換至修改提款密碼
        self.wait_loading_finish()
        self.click(MemberPageLocator.proflie_menu_cg_s_pwd)

        self.wait_loading_finish()
        self.type(MemberPageLocator.cgspwd_input_oldpwd, old_spwd)
        self.type(MemberPageLocator.cgspwd_input_newpwd, new_spwd)
        self.type(MemberPageLocator.cgspwd_input_newpwd2, new_spwd)
        self.click(MemberPageLocator.cgspwd_submit)

        self.wait_visibility(MemberPageLocator.cgspwd_seccess_point)
        assert self.is_element_finded(MemberPageLocator.cgspwd_seccess_point),'修改提款密碼錯誤'
        self.click(MemberPageLocator.cgspwd_alert_close)

    def doChangeContact(self, mail, phone, qq, wechat, s_pwd):
        # 我的資料分頁切換至修改聯絡方式
        self.wait_loading_finish()
        self.click(MemberPageLocator.profile_menu_contact)

        self.wait_loading_finish()
        if self.is_element_finded(MemberPageLocator.contact_edit_btn) is True:
            self.click_all(MemberPageLocator.contact_edit_btn)
            if self.is_element_finded(MemberPageLocator.contact_input_change_email) is True:
                self.type(MemberPageLocator.contact_input_change_email, mail)

            if self.is_element_finded(MemberPageLocator.contact_input_change_phone) is True:    
                self.type(MemberPageLocator.contact_input_change_phone, phone)

            if self.is_element_finded(MemberPageLocator.contact_input_change_qq) is True:    
                self.type(MemberPageLocator.contact_input_change_qq, qq)

            if self.is_element_finded(MemberPageLocator.contact_input_change_wechat) is True:    
                self.type(MemberPageLocator.contact_input_change_wechat, wechat)

            if self.is_element_finded(MemberPageLocator.contact_input_change_spwd) is True:    
                self.type(MemberPageLocator.contact_input_change_spwd, s_pwd)
            
            self.click(MemberPageLocator.contact_submit)

            self.wait_visibility(MemberPageLocator.cgspwd_seccess_point)
            assert self.is_element_finded(MemberPageLocator.contact_seccess_point),'修改聯絡方式錯誤'
            self.click(MemberPageLocator.contact_alert_close)
    

    def do_change_bankCard(self, branch_num, city_num, spwd):
        # 我的資料分頁切換至修改出款銀行
        back_card_list = [6226916010229880,6226840008071395,4427295467015346,94005641216486653,
            6223384734027576414,6223256885337408,6226177213341283,8880003693333330,6226827880876136566,
            6223294699171505510,4386005742904449,4563510313248240155,6223484616443531,
            4315020329530893,6223353629215105,6223438774536974920]
        bank_card=choice(back_card_list)

        self.wait_loading_finish()
        self.click(MemberPageLocator.profile_menu_card)
        self.wait_loading_finish()
        self.click(MemberPageLocator.card_method)
        self.wait_loading_finish()

        if self.is_element_finded(MemberPageLocator.pay_methods(self, "新增银行卡")):
            num=randint(2, 15)
            self.wait_loading_finish()
            self.type(MemberPageLocator.bank_card, bank_card)
            self.click(MemberPageLocator.bank_select_btn)
            self.click(MemberPageLocator.change_bank(num))
            self.type(MemberPageLocator.bank_input_cardbranch_num, branch_num)
            self.type(MemberPageLocator.bank_input_cardcity_num, city_num)
            self.type(MemberPageLocator.bank_input_securitycode, spwd)
            self.click(MemberPageLocator.bank_submit)

            if self.wait_visibility_status(MemberPageLocator.add_alert):
                message = self.get_text(MemberPageLocator.add_alert)
                self.click(MemberPageLocator.alert_close)
                if message.__contains__('您所填入的资料有误'):
                    raise EOFError(f'輸入錯誤 \n訊息:\n{message}')

            elif self.wait_alert_present():
                message = self.get_alert_message()
                self.accept_alert()
                if message.__contains__(f'银行卡号[{bank_card}]已被使用'):
                    self.do_change_bankCard(branch_num, city_num, spwd)
                else:
                    raise EOFError(f'出現未預期警告彈窗:\n{message}')

            else:
                raise EOFError('沒出現確認訊息視窗')

    
    def do_change_virtualcard(self, spwd, phone):
        # 我的資料分頁切換至綁定虛擬錢包
        virtual_card = datetime.datetime.now().strftime('0x00bot%Y%m%d%H%M%Sx00' + str(random.randrange(1, 10000)))

        self.wait_loading_finish()
        self.click(MemberPageLocator.profile_menu_card)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.card_method_virtual) is True, "綁定出款方式_虛擬錢包已被禁用"
        self.click(MemberPageLocator.card_method_virtual)
        self.wait_loading_finish()

        # 帳戶安全
        # 尚未設定手機號碼
        if self.is_element_finded(MemberPageLocator.bind_mobile):
            self.type(MemberPageLocator.bind_mobile_input, phone)
            self.type(MemberPageLocator.bind_securitycode, spwd)
            self.click(MemberPageLocator.bind_confirm)
            self.wait_visibility(MemberPageLocator.cgspwd_seccess_point)
            assert self.is_element_finded(MemberPageLocator.contact_seccess_point),'修改聯絡方式錯誤'
            self.click(MemberPageLocator.contact_alert_close)

        # 已有設定手機號碼
        elif self.is_element_finded(MemberPageLocator.verify_mobile):
            self.type(MemberPageLocator.verify_mobile_input, phone)
            self.click(MemberPageLocator.verify_confirm)

        else:
            raise EOFError('進入綁定虛擬錢包沒出現帳戶安全彈窗')

        self.wait_visibility(MemberPageLocator.breadcrumb_item(self, "虚拟钱包"))
        self.wait_loading_finish()
        self.sleep(2)
        if self.is_element_finded(MemberPageLocator.credit_item_cgpay) is False:
            # self.wait_visibility(MemberPageLocator.credit_item_add)   # 若已有新增其他虛擬錢包才須點擊，目前購寶不易新增故先隱藏
            # self.click(MemberPageLocator.credit_item_add)
            self.wait_loading_finish()
            # 選擇錢包名稱
            self.wait_visibility(MemberPageLocator.virtual_card)
            if self.is_element_displayed(MemberPageLocator.wallet_select) is True:
                self.click(MemberPageLocator.wallet_select)
                self.click(MemberPageLocator.wallet_option_cgpay)
            self.type(MemberPageLocator.virtual_card, virtual_card)
            self.type(MemberPageLocator.bank_input_securitycode, spwd)
            self.click(MemberPageLocator.bank_submit)

            if self.wait_visibility_status(MemberPageLocator.add_alert):
                message = self.get_text(MemberPageLocator.add_alert)
                self.click(MemberPageLocator.alert_close)
                if message.__contains__('您所填入的资料有误'):
                    raise EOFError(f'輸入錯誤 \n訊息:\n{message}')
            else:
                raise EOFError('沒出現確認訊息視窗')
            self.wait_visibility(MemberPageLocator.credit_item_cgpay) # 確認已成功新增CGpay虛擬錢包


    def do_change_wellpay_wallet(self, spwd, wallet_address='', phone=''):
        # 我的資料分頁切換至綁定順付-WellPay
        if wallet_address == '':
            wallet_address = datetime.datetime.now().strftime('0x00bot%Y%m%d%H%M%Sx00' + str(random.randrange(1, 10000)))

        self.wait_loading_finish()
        self.click(MemberPageLocator.profile_menu_card)
        self.wait_loading_finish()
        assert self.is_element_finded(MemberPageLocator.card_method_wellpay) is True, "綁定出款方式_顺付-Well Pay已被禁用"
        self.click(MemberPageLocator.card_method_wellpay)
        self.wait_loading_finish()

        # 帳戶安全
        # 尚未設定手機號碼
        if self.is_element_finded(MemberPageLocator.bind_mobile):
            self.type(MemberPageLocator.bind_mobile_input, phone)
            self.type(MemberPageLocator.bind_securitycode, spwd)
            self.click(MemberPageLocator.bind_confirm)
            self.wait_visibility(MemberPageLocator.cgspwd_seccess_point)
            assert self.is_element_finded(MemberPageLocator.contact_seccess_point),'修改聯絡方式錯誤'
            self.click(MemberPageLocator.contact_alert_close)

        # 已有設定手機號碼
        elif self.is_element_finded(MemberPageLocator.verify_mobile):
            self.type(MemberPageLocator.verify_mobile_input, phone)
            self.click(MemberPageLocator.verify_confirm)

        else:
            raise EOFError('進入綁定顺付-Well Pay沒出現帳戶安全彈窗')

        self.wait_visibility(MemberPageLocator.breadcrumb_item(self, "顺付-Well Pay"))
        self.wait_loading_finish()
        self.sleep(2)
        # 確認是否已新增WellPay錢包
        if self.is_element_finded(MemberPageLocator.credit_item_wellpay) is False:
            self.wait_loading_finish()
            self.type(MemberPageLocator.virtual_card, wallet_address)
            self.type(MemberPageLocator.bank_input_securitycode, spwd)
            self.click(MemberPageLocator.bank_submit)

            if self.wait_visibility_status(MemberPageLocator.add_alert):
                message = self.get_text(MemberPageLocator.add_alert)
                self.click(MemberPageLocator.alert_close)
                if message.__contains__('您所填入的资料有误'):
                    raise EOFError(f'輸入錯誤 \n訊息:\n{message}')
            else:
                raise EOFError('沒出現確認訊息視窗')
            self.wait_visibility(MemberPageLocator.credit_item_wellpay) # 確認已成功新增顺付-Well Pay錢包


    # 儲值後前台確認紀錄-成功
    def check_money_entry_record(self,tra_money,offer_money,total_money,wallet_before,style,Handlingmoney=0):
        self.wait_loading_finish()
        wallet = self.get_text(MemberPageLocator.wallet)
        self.click(MemberPageLocator.menu_wallet_deposit)
        self.wait_loading_finish()

        for loop in range(0,3):
            try:
                self.sleep(3)
                self.select_by_text(MemberPageLocator.search_company,style)
                self.wait_loading_finish()
                self.click(MemberPageLocator.search_today)
                amount_sort_locater = MemberPageLocator.amount_sort(style)
                self.wait_visibility(amount_sort_locater)

                amount_sort=self.get_text(amount_sort_locater) # 儲值類型
                owner_money=round(float(self.get_text(MemberPageLocator.owner_total_money)),2) # 帳戶總餘額
                amount_before=round(float(self.get_text(MemberPageLocator.amount_before)),2) # 儲值前
                amount_to=round(float(self.get_text(MemberPageLocator.amount_to)),2) # 儲值金額
                amount_after=round(float(self.get_text(MemberPageLocator.amount_after)),2) # 儲值後
                amount_status=self.get_text(MemberPageLocator.amount_status) # 儲值狀態
                break
            except Exception:
                if loop == 2:
                    logging.exception('exception log')
                else:
                    continue

        if offer_money == None or '' or 'null':
            offer_money = 0

        if offer_money != 0:
            self.select_by_text(MemberPageLocator.search_company,'优惠')
            self.sleep(3)
            amount_before_offer = round(float(self.get_text(MemberPageLocator.amount_before)), 2) # 優惠欄位儲值前
            amount_to_offer = round(float(self.get_text(MemberPageLocator.amount_to)), 2) # 優惠欄位儲值金額
            amount_after_offer = round(float(self.get_text(MemberPageLocator.amount_after)), 2) # 優惠欄位儲值後

            assert amount_before_offer == amount_after, '優惠前總金額不正確'
            assert amount_to_offer == offer_money, '優惠金額不正確'
            assert amount_before_offer + amount_to_offer == amount_after_offer, '優惠記錄儲值後不正確'

        self.wait_loading_finish()
        assert amount_sort==style,'存款類型不正確 Error:%s'%amount_sort
        assert amount_to==tra_money or int(amount_to)==int(tra_money) or amount_to==total_money,'儲值金額前後台不一致 儲值金額:%.2f 後台儲值金額:%.2f 儲值金額加上優惠:%.2f'%(amount_to,tra_money,total_money) # 前台有些品牌會出現小數點有些不會,用兩個判斷是去比對,在線支付問題:前後台優惠金額不會分開

        after_money=amount_before+amount_to # 儲值前+儲值金額=儲值後金額(不包含優惠)
        after_money_offer=total_money
        assert float(after_money)==float(amount_after) or float(after_money_offer)==float(total_money) ,'入款後金額不正確 儲值金額後:%.2f 前台顯示金額:%.2f 儲值金額加上優惠:%.2f'%(after_money,amount_after,total_money)

        assert amount_status=='成功到账','儲值失敗'
        assert owner_money==round(wallet_before+total_money,2),f'儲值後總金額不正確, 目前總共:{owner_money} 儲值前 + 存款金額:{round(wallet_before+total_money,2)}'


    # 儲值後前台確認紀錄-失敗
    def check_money_entry_fail_record(self,tra_money,wallet_before,style):
        self.wait_loading_finish()
        wallet = self.get_text(MemberPageLocator.wallet)
        self.click(MemberPageLocator.menu_wallet_deposit)
        self.wait_loading_finish()

        for loop in range(0,3):
            try:
                self.sleep(3)
                self.select_by_text(MemberPageLocator.search_company,style)
                self.wait_loading_finish()
                self.click(MemberPageLocator.search_today)
                amount_sort_locater = MemberPageLocator.amount_sort(style)
                self.wait_visibility(amount_sort_locater)

                amount_sort = self.get_text(amount_sort_locater) # 儲值類型
                owner_money = round(float(self.get_text(MemberPageLocator.owner_total_money)),2) # 帳戶總餘額
                amount_before = self.get_text(MemberPageLocator.amount_before) # 儲值前
                amount_to = round(float(self.get_text(MemberPageLocator.amount_to)),2) # 儲值金額
                amount_after = self.get_text(MemberPageLocator.amount_after) # 儲值後
                amount_status = self.get_text(MemberPageLocator.amount_status) # 儲值狀態
                break
            except Exception:
                if loop == 2:
                    logging.exception('exception log')
                else:
                    continue

        for i in range(3):
            if amount_status == '审核失败':
                break
            else:
                self.refresh_browser()
                self.sleep(3)
                self.select_by_text(MemberPageLocator.search_company,style)
                self.wait_loading_finish()
                self.click(MemberPageLocator.search_today)

        assert amount_status == '审核失败', f"充值紀錄，狀態顯示錯誤'{amount_status}'，應為'审核失败'"
        assert amount_sort != '', f"充值紀錄，未顯示充值方式"
        assert (amount_before =='-') and (amount_after =='-') ,f"充值紀錄，入款前{amount_before}&入款後{amount_after}，應顯示'-'"
        assert str(amount_to) == str(tra_money), f"充值紀錄，金額顯示錯誤'{str(amount_to)}'，應為'{str(tra_money)}'"
        assert wallet_before == owner_money, f'充值失敗時，充值前{wallet_before} 與 充值失敗後{owner_money} 金額不同'


    def before_check_money_entry_record(self,style,money_to):
        self.wait_loading_finish()
        self.wait_visibility(MemberPageLocator.menu_wallet_deposit)
        self.click(MemberPageLocator.menu_wallet_deposit)
        self.wait_loading_finish()

        self.select_by_text(MemberPageLocator.search_company,style)
        self.wait_loading_finish()
        self.click(MemberPageLocator.search_today)

        self.sleep(3)
        amount_sort=self.wait_visibility(MemberPageLocator.amount_sort(style)).text # 儲值類型
        amount_before=self.wait_visibility(MemberPageLocator.amount_before).text # 儲值前
        amount_to=round(float(self.get_text(MemberPageLocator.amount_to)),2) # 儲值金額
        amount_after=self.get_text(MemberPageLocator.amount_after) # 儲值後
        amount_status=self.get_text(MemberPageLocator.amount_status) # 儲值狀態
        amount_time=self.get_text(MemberPageLocator.amount_time) # 儲值時間

        # self.select_by_text(MemberPageLocator.search_company,'优惠')
        # self.sleep(3)
        # offer_moneyPage=round(float(self.get_text(MemberPageLocator.amount_to)),2)

        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        assert str(amount_time)[:10]==now_time,'儲值時間不正確:%s'%amount_time
        assert amount_sort==style,'存款類型不正確 Error:%s'%amount_sort

        for _ in range(0,6):
            try:
                assert amount_status=='充值中','狀態未顯示為充值中. Error:%s'%amount_status
                assert amount_before=='-','充值中狀態應顯示 "-" '
                assert amount_after=='-','充值中狀態應顯示 "-" '     
                break
            except:
                self.sleep(3)
                self.refresh_browser()
                self.wait_loading_finish()

        

        # assert round(float(amount_to),2)==round(float(money_to),2),'儲值金額顯示不正確. 充值金額:%s 入款紀錄充值總金額:%s'%(money_to,amount_to)

    def before_check_money_output_record(self,style,money_to,real_money):
        self.wait_loading_finish()
        self.click(MemberPageLocator.menu_wallet_withdraw)

        self.wait_loading_finish()
        self.click(MemberPageLocator.search_today)

        withdraw_change=self.get_text(MemberPageLocator.withdraw_apply) # 實際出款金額
        amount_time=self.get_text(MemberPageLocator.amount_time) # 出款時間
        status = self.get_text(MemberPageLocator.withdraw_status)

        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        assert str(amount_time)[:10]==now_time,'出款時間不正確:%s'%amount_time
        assert str(withdraw_change) == str(real_money),'出款金額顯示不正確 %s %s' %(str(withdraw_change),str(real_money))
        assert status == "处理中","狀態顯示異常 訊息:%s" %status

    def want_buy_check(self):
        self.wait_loading_finish()
        self.click(MemberPageLocator.menu_wallet_withdraw)
        self.wait_loading_finish()
        self.click(MemberPageLocator.want_buy_check_btn)
        self.wait_visibility(MemberPageLocator.want_buy_pop_btn)
        self.click(MemberPageLocator.want_buy_pop_btn)


    def after_check_money_output_record(self,Withdraw_money,wallet_before):
        self.wait_loading_finish()
        self.click(MemberPageLocator.menu_wallet_withdraw)
        self.refresh_browser()
        self.wait_loading_finish()

        owner_money=round(float(self.get_text(MemberPageLocator.owner_total_money)),2) # 帳戶總餘額
        total=round(float(wallet_before)-float(Withdraw_money),2)
        self.sleep(1)
        status = self.get_text(MemberPageLocator.withdraw_status)

        assert status == "出款成功","狀態顯示異常 訊息:%s" %status
        assert total==owner_money,'帳戶餘額與提款後餘額不相符 帳戶餘額:%s  出款紀錄提款後餘額:%s'%(total,owner_money)

    def maintenance_check(self, brand_list, status):
        self.wait_loading_finish()
        
        for brand in brand_list:

            if status == True:
                assert self.is_element_finded(MemberPageLocator.wallet_choosing_btn_maintenance(brand)) is True, '該品牌應該顯示維護狀態'
            else:
                assert self.is_element_finded(MemberPageLocator.wallet_choosing_btn_maintenance(brand)) is False, '該品牌應該顯示啟用狀態'


    def get_name_and_money(self):
        _list = []

        for loop in self.find_elements(MemberPageLocator.get_name_and_money):
            Info = self.get_text_by_dom(loop)
            Cut = Info.split('\n')
            _list.append(Cut)

        return _list

    def after_check_manualdeposit_record(self, wallet_before, style, money):
        self.wait_loading_finish()
        self.click(MemberPageLocator.menu_wallet_deposit)
        self.wait_loading_finish()
        for i in range(3):
            try:
                self.sleep(3)
                self.refresh_browser()
                self.select_by_text(MemberPageLocator.search_company,style)
                self.wait_loading_finish()
                self.click(MemberPageLocator.search_today)
                
                amount_sort=self.wait_visibility(MemberPageLocator.amount_sort(style)).text # 儲值類型
                break
            except:
                assert i != 3, '可能沒有入款紀錄'
                    
        owner_money=round(float(self.get_text(MemberPageLocator.owner_total_money)),2) # 帳戶總餘額
        total_money = wallet_before + float(money)
        amount_status=self.get_text(MemberPageLocator.amount_status) # 儲值狀態

        self.wait_loading_finish()

        assert amount_sort == style,'存款類型不正確 Error:%s'%amount_sort
        assert total_money == owner_money, f'儲值紀錄錢包{total_money}與會員錢包{owner_money}不相符'
        assert amount_status == '成功到账','儲值失敗'
    
    # 儲值 順付線上支付
    def do_all_exchange_deposit(self, money, pay_method):
        self.type(MemberPageLocator.deposit_amount, money)  # 存入金額
        self.click(MemberPageLocator.pay_methods(self, pay_method))
        self.click(MemberPageLocator.deposit_submit_btn2)  # 確認提交
        self.sleep(5)
        self.switch_last_page()
    
    # 儲值 順付線上支付_掃碼
    def do_all_exchange_deposit_qrcode(self, pay_method):
        self.click(MemberPageLocator.pay_methods(self, pay_method))
        money = self.get_text(MemberPageLocator.select_money).replace(' ','').replace(',','')
        self.click(MemberPageLocator.deposit_submit_btn2)  # 確認提交
        self.sleep(5)
        self.switch_last_page()
        return int(money)