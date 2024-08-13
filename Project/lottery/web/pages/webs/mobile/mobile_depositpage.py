from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import platform
import os

class DepositPageLocator(BasePage):
    m_btn_next = (By.XPATH, "//*[@value='下一步' or text()= '下一步']")
    m_upfile = (By.XPATH, "//input[@type='file']")

    # 公司入款
    m_btn_deposit_company = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'公司入款') or \
        contains(@data-bind, 'name') and contains(text(),'支付宝')]/..")
    m_input_deposit_money = (By.XPATH, "(//*[contains(@placeholder, '金额')])[last()]")
    m_input_deposit_name = (By.XPATH, "(//*[contains(@placeholder, '姓名')])[1]")
    m_input_deposit_cardnum = (By.XPATH, "//label[text()='转帐卡号']/../input")
    m_btn_deposit_submit = (By.XPATH, "(//*[@value='确认提交' or contains(., '确认提交')])[last()]")
    m_check_point_deposit_success = (By.XPATH, "//*[text()='已成功提交' or text()='申请提交成功']")
    m_btn_dialog_ok = (By.XPATH, "//*[text()='关闭']")
   

    # 支付寶轉帳
    m_btn_alipay = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'支付宝') or \
        contains(@data-bind, 'name') and contains(text(),'支付宝')]/..")
    m_btn_deposit_alipay = (By.XPATH, "//span[text()='支付宝转帐']")

    m_input_deposit_alipay_amount = (By.XPATH, "//html//div[@class='my_d_item']/div[1]/input[1]")  # 金額
    m_input_deposit_alipay_name = (By.XPATH, "//html//div[@class='my_d_item']/div[2]/input[1]")  # 姓名
    m_input_deposit_airpay_name_2 = (By.XPATH, "//input[@placeholder='请填写汇款人姓名' \
        or @placeholder='请输入真实姓名']")

    # 支付寶面對面
    m_btn_deposit_alipay_qr = (By.XPATH, "//span[text()='支付宝面对面扫码']")

    # 微信轉帳
    m_btn_wechat = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'微信') or \
        contains(@data-bind, 'name') and contains(text(),'微信')]/..")
    m_btn_deposit_wechat = (By.XPATH, "//span[text()='微信转帐']")
    m_input_deposit_wechat_amount = (By.XPATH, "//div[@class='input_group']/input")  # 金額

    # 微信面對面
    m_btn_deposit_wechat_qr = (By.XPATH, "//span[text()='微信面对面扫码']")
    m_input_deposit_qr_amount = (By.XPATH, "//div[@class='input_group']//input[@type='text']")  # 金額
    m_btn_deposit_qr_next_button = (By.XPATH, "//input[@value='查看二维码']")  # 下一步按鈕
    m_input_deposit_qr_order_a = (By.XPATH, "//input[@name='A']")  # 交易單號
    m_input_deposit_qr_order_b = (By.XPATH, "//input[@name='B']")  # 交易單號
    m_input_deposit_qr_order_c = (By.XPATH, "//input[@name='C']")  # 交易單號
    m_input_deposit_qr_order_d = (By.XPATH, "//input[@name='D']")  # 交易單號
    m_input_deposit_qr_order_e = (By.XPATH, "//input[@name='E']")  # 交易單號
    m_btn_deposit_qr_submit = (By.XPATH, "(//input[@class='btn_a'])[2]")

    # 支付方式選擇
    m_deposit_radio = (By.XPATH, "//div[@class= 'pay-group__item']")
    # 線上支付
    m_btn_deposit_onlinepay = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'线上支付') or \
        contains(@data-bind, 'name') and contains(text(),'线上支付')]/..")
    # 銀聯支付
    m_btn_deposit_unionpay = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'银联支付') or \
        contains(@data-bind, 'name') and contains(text(),'银联支付')]/..")
    # 東京支付
    m_btn_deposit_tokyopay = (By.XPATH, "//*[contains(@class, 'item') and contains(text(),'京东支付') or \
        contains(@data-bind, 'name') and contains(text(),'京东支付')]/..")
    # 線上支付
    m_deposit_submit_btn2 = (By.XPATH,"//*[contains(text(),'确认提交') or contains(@value,'提') and \
        contains(@value,'交')]")
    # 入款otp
    m_transfer_depositotp_input = (By.XPATH, "//div[@class='form-group' or @style='']/input[@placeholder='请联系客服索取提交密码']")

    
    def pay_methods(self,name):
        pay_method = (By.XPATH, "(//*[contains(text(), '%s')])[last()]" %name)  # 支付方式
        return pay_method

    onlinepay_title = (By.XPATH, "(//*[contains(*, '自動市_线上支付')])[last()]")  # 線上支付
    unionpay_title = (By.XPATH, "(//*[contains(*, '自動市_银联支付')])[last()]")  # 銀聯支付
    jdpaypay_title = (By.XPATH, "(//*[contains(*, '自動市_京东支付')])[last()]")  # 京東支付
    wellpay_title = (By.XPATH, "(//*[contains(*, '顺付WellPay')])[last()]")     # 順付入款

    # 面對面
    deposit_qrcode_next_btn = (By.XPATH, "//input[@value='查看二维码']")  # 支付寶/微信 面對面下一步
    username_qr = (By.XPATH, "//*[@data-bind='text: account']")  # 確認面對面方式的使用者名稱
    deposit_f2f_submit_btn = (By.XPATH, "//*[@value='完成转账' or text()= '确认提交']")

    # 申請提交訊息
    deposit_dialog_message = (By.XPATH, "//*[@class='swal2-title' or @class= 'van-toast__text'") # 申請提交成功訊息
    deposit_dialog_massage_nwap = (By.XPATH, "//p[contains(text(),'成功') and @class='xfe__title']")
    deposit_dialog_ok_btn = (By.XPATH, "//*[text()='关闭']") # ok
    deposit_dialog_check_btn = (By.XPATH, "//*[text()='查看进度']") # 查看进度

    # 轉帳
    deposit_amount = (By.XPATH, "//input[contains(text(), '转帐金额')  or contains(@placeholder, '转账金额') \
        or @data-bind= 'textInput: amount' or contains(@data-bind, 'transferamount')]")  # 支付寶/微信 轉帳第一層金額輸入
    real_money = (By.XPATH, "//*[contains(@data-bind,'transferamount') or contains(@class, 'input-custom__text')]") # 實際轉帳金額
    deposit_submit_btn = (By.XPATH, "//*[text()='确认提交' or @value= '确认提交']") # 確認提交
    deposit_submit_btn_nwap = (By.XPATH, "//a[@class='btn btn-primary rounded-pill btn-ripple' and text()='确认提交']") # 確認提交NWAP
    def deposit_name(self, name, delete=False):
        self.wait_loading_finish()
        deposit_enter = (By.XPATH, "//*[text()='%s']" % name)

        if delete == True:
            if self.is_element_finded(deposit_enter) is False:
                return
            else:
                raise EOFError(f'不應該顯示此入款方式: {name}')

        if self.is_element_finded(deposit_enter) is False:
            self.test_skip('無此支付方式')
        self.click(deposit_enter)

    def users_find_and_check(self, realuser):
        self.wait_loading_finish()
        userlink =(By.XPATH,"//*[contains(@id,'radio')]") #全部選項
        for ele in range(1, len(self.find_elements(userlink)) + 1):
            self.sleep(1)
            userlink_click =(By.XPATH, f"(//*[@type='radio']/..)[{ele}]") #點擊選項
            self.click(userlink_click)
            user = (By.XPATH, "//*[contains(text(),'开户人：')]/..//span[last()]")  # 開戶名
            message = self.get_text(user) #開戶人名

            if message == realuser:
                break

        assert message == realuser, '找不到開戶人名稱:%s' % realuser
    
    # 找錢包地址
    def address_find_and_check(self, address):
        self.wait_loading_finish()
        userlink =(By.XPATH,"//*[contains(@id,'radio')]") #全部選項
        for ele in range(1, len(self.find_elements(userlink)) + 1):
            self.sleep(1)
            userlink_click =(By.XPATH, f"(//*[@type='radio']/..)[{ele}]") #點擊選項
            self.click(userlink_click)
            user = (By.XPATH, "//*[contains(text(),'地址：')]/..//span[last()]")  # 地址
            message = self.get_text(user) # 地址

            if message == address:
                break
        assert message == address, '找不到錢包地址:%s' % address

    def wechat_user_check_nwap(self, realuser):
        self.wait_loading_finish()
        user = (By.XPATH, "//*[@style='' and @class= 'bank_box' or \
            @class= 'bank-chklst']//*[contains(text(), '自動測試')]")  # 開戶名
        message = self.get_text(user) #開戶人名

        assert message == realuser, '開戶人名稱錯誤:%s' % realuser

    def deposit_mode_check(self, realuser):
        self.wait_loading_finish()
        mode_link =(By.XPATH,"//*[@class='pay-group__item' or @name='bank']/..") #全部選項
        for ele in range(1, len(self.find_elements(mode_link)) + 1):
            self.sleep(1)
            mode_link_click =(By.XPATH, f"(//*[@class='pay-group__item' or @name='bank']/..)[{ele}]") #點擊選項
            self.click(mode_link_click)
            message = self.get_text(mode_link_click) #開戶人名

            if message.__contains__(realuser):
                break

        assert message.__contains__(realuser), f'找不到指定方式: {realuser}'

    # 微信/支付寶第一層支付方式
    def pay_title(self, title_name):
        self.wait_loading_finish()
        pay_title = (By.XPATH, f"(//*[contains(text(),'{title_name}')])[last()]")
        if self.is_element_finded(pay_title) is False:
            self.test_skip('無此支付方式')

        message = self.get_text(pay_title)
        assert str(message).__contains__(title_name), '%s 建立失敗' % title_name
        title_btn = (By.XPATH, f"(//*[contains(text(),'{title_name}')])[last()]")
        # 點擊子項目
        if self.is_element_finded(title_btn):
            self.click(title_btn)
        
        # # 避免只有一種付款方式跳出錯誤
        # try:
        #     self.click(pay_title)
        # except:
        #     pass

    # 五碼QRcode
    def deposit_wechat_alipay_five_code(self):
        deposit_wechat_alipay_five_code = (By.XPATH, "//input[@class='input']")

        if self.is_element_finded(deposit_wechat_alipay_five_code) is True:
            for ele in range(1, len(self.find_elements(deposit_wechat_alipay_five_code)) + 1):
                code = (By.XPATH, "//input[@class='input'][%d]" % ele)  # 帳號類型
                self.type(code, '1')
            return 'public'
        else:
            deposit_wechat_alipay_five_code = (By.XPATH, "//p[text()= '交易单号']/following::input")
            self.type(deposit_wechat_alipay_five_code, '11111')
            self.type_tab(deposit_wechat_alipay_five_code)
            self.sleep(1)
            return 'nwap'


class DepositPage(BasePage):
    
    def do_company_deposit(self, user, money, otp=''):
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_btn_next) is True:
            self.click(DepositPageLocator.m_btn_next)

        self.type(DepositPageLocator.m_input_deposit_money, money)
        self.type(DepositPageLocator.m_input_deposit_name, user)
        self.type_tab(DepositPageLocator.m_input_deposit_name)
        if self.is_element_finded(DepositPageLocator.m_transfer_depositotp_input) is True:
            self.type(DepositPageLocator.m_transfer_depositotp_input, otp)
        else:
            pass
        # 上傳付款圖片
        if platform.system() == 'Linux':
            folder_path = os.path.abspath(__file__).split('/Project')[0]
        else:
            folder_path = os.path.abspath(__file__).split('\Project')[0]
        dir_path = "{0}/image/wap/lottery/{1}/{1}.png".format(folder_path, 'HK')

        self.type(DepositPageLocator.m_upfile, dir_path)
        self.sleep(2)
        self.click(DepositPageLocator.m_btn_deposit_submit)
        self.wait_loading_finish()
        self.wait_visibility(DepositPageLocator.m_check_point_deposit_success)

        if self.is_element_finded(DepositPageLocator.m_btn_dialog_ok) is True:
            self.click(DepositPageLocator.m_btn_dialog_ok)

    # 儲值 支付寶/微信 面對面
    def do_desposit_weChat_alipayf2f(self, otp=''):
        edition = DepositPageLocator.deposit_wechat_alipay_five_code(self)
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_transfer_depositotp_input) is True:
            self.type(DepositPageLocator.m_transfer_depositotp_input, otp)
        else:
            pass
        self.click(DepositPageLocator.deposit_f2f_submit_btn)  # 確認提交
        
        if self.is_element_displayed(DepositPageLocator.deposit_dialog_message) is True:
            assert self.get_text(DepositPageLocator.deposit_dialog_message) == '申请提交成功'
        elif self.is_element_finded(DepositPageLocator.deposit_dialog_massage_nwap) is True:
            assert self.get_text(DepositPageLocator.deposit_dialog_massage_nwap) == '已成功提交'

        self.wait_loading_finish()        
        self.click(DepositPageLocator.deposit_dialog_ok_btn)
        self.sleep(5)

    # 儲值 支付寶/微信 轉帳
    def do_desposit_wechat_alipay_transfer(self, otp=''):
        self.wait_loading_finish()
        if self.wait_visibility_status(DepositPageLocator.deposit_submit_btn) is True:
            # 常會點不到,故增加判斷次數
            for i in range(0, 3):
                if self.is_element_finded(DepositPageLocator.m_transfer_depositotp_input) is True:
                    self.type(DepositPageLocator.m_transfer_depositotp_input, otp)
                else:
                    pass
  
                if self.is_element_finded(DepositPageLocator.deposit_submit_btn) is True:
                    if self.is_element_finded(DepositPageLocator.deposit_submit_btn_nwap) is True:
                        self.click(DepositPageLocator.deposit_submit_btn_nwap)  # 確認提交
                        break
                    else:    
                        self.type_page_down(DepositPageLocator.deposit_submit_btn)
                        self.sleep(1)
                        self.click(DepositPageLocator.deposit_submit_btn)  # 確認提交
                        break
                else:
                    if i == 2:
                        raise EOFError('點擊確認提交錯誤')
                    
                    self.sleep(3)

            if self.is_element_displayed(DepositPageLocator.deposit_dialog_message) is True:
                assert self.get_text(DepositPageLocator.deposit_dialog_message) == '申请提交成功'
            elif self.is_element_finded(DepositPageLocator.deposit_dialog_massage_nwap) is True:
                assert self.get_text(DepositPageLocator.deposit_dialog_massage_nwap) == '已成功提交'
            
            self.wait_loading_finish()
            self.wait_visibility(DepositPageLocator.deposit_dialog_ok_btn)
            self.wait_visibility(DepositPageLocator.deposit_dialog_check_btn)
            self.click(DepositPageLocator.deposit_dialog_ok_btn)
        else:
            raise EOFError('沒出現提交按鈕錯誤')

    def do_alipay_deposit(self, amount, name):
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_btn_alipay) is False:
            self.test_skip('無此支付方式')
        self.click(DepositPageLocator.m_btn_alipay)
        self.wait_loading_finish()
        self.click(DepositPageLocator.m_btn_deposit_alipay)
        self.wait_loading_finish()
        self.type(DepositPageLocator.m_input_deposit_alipay_amount, amount)
        self.sleep(1)
        self.click(DepositPageLocator.m_btn_deposit_submit)
        assert self.is_element_enable(DepositPageLocator.m_check_point_deposit_success) is True
        self.click(DepositPageLocator.m_btn_dialog_ok)

    def do_wechat_deposit(self, amount):
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_btn_wechat) is False:
            self.test_skip('無此支付方式')
        self.click(DepositPageLocator.m_btn_wechat)
        self.wait_loading_finish()
        self.click(DepositPageLocator.m_btn_deposit_wechat)
        self.type(DepositPageLocator.m_input_deposit_wechat_amount, amount)
        self.wait_loading_finish()
        self.click(DepositPageLocator.m_btn_next)
        self.scroll_to_bottom()
        self.sleep(1)
        self.click(DepositPageLocator.m_btn_deposit_submit)
        assert self.is_element_enable(DepositPageLocator.m_check_point_deposit_success) is True
        self.click(DepositPageLocator.m_btn_dialog_ok)

    def do_wechatqa_deposit(self, amount, order):
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_btn_wechat) is False:
            self.test_skip('無此支付方式')
        self.click(DepositPageLocator.m_btn_wechat)
        self.click(DepositPageLocator.m_btn_deposit_wechat_qr)
        self.type(DepositPageLocator.m_input_deposit_qr_amount, amount)
        self.wait_loading_finish()
        self.click(DepositPageLocator.m_btn_deposit_qr_next_button)
        self.scroll_to_bottom()
        self.type(DepositPageLocator.m_input_deposit_qr_order_a, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_b, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_c, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_d, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_e, order)
        self.click(DepositPageLocator.m_btn_deposit_qr_submit)
        assert self.is_element_enable(DepositPageLocator.m_check_point_deposit_success) is True
        self.click(DepositPageLocator.m_btn_dialog_ok)

    def do_aliPayqr_deposit(self, amount, order):
        self.wait_loading_finish()
        if self.is_element_finded(DepositPageLocator.m_btn_alipay) is False:
            self.test_skip('無此支付方式')
        self.click(DepositPageLocator.m_btn_alipay)
        self.click(DepositPageLocator.m_btn_deposit_alipay_qr)
        self.type(DepositPageLocator.m_input_deposit_qr_amount, amount)
        self.wait_loading_finish()
        self.click(DepositPageLocator.m_btn_deposit_qr_next_button)
        self.scroll_to_bottom()
        self.type(DepositPageLocator.m_input_deposit_qr_order_a, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_b, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_c, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_d, order)
        self.type(DepositPageLocator.m_input_deposit_qr_order_e, order)
        self.click(DepositPageLocator.m_btn_deposit_qr_submit)
        assert self.is_element_enable(DepositPageLocator.m_check_point_deposit_success) is True
        self.click(DepositPageLocator.m_btn_dialog_ok)

    # 確認公司入款建立成功
    def check_company_deposit(self, name='', user=''):
        self.wait_loading_finish()

        if type(name) == list:
            for bank in name:
                DepositPageLocator.deposit_name(self, bank, True)
            return

        if self.is_element_finded(DepositPageLocator.m_btn_deposit_company) is False:
            self.test_skip('無此支付方式')

        DepositPageLocator.deposit_name(self, name)  # 點擊公司入款
        self.wait_loading_finish()
        DepositPageLocator.users_find_and_check(self, user)

    # 前台確認支付寶/微信面對面
    def check_qr_deposit(self, name, user, pay_title, money, status= False):
        self.wait_loading_finish()
        DepositPageLocator.deposit_name(self, name)  # 點擊支付寶 or 微信
        self.wait_loading_finish()
        DepositPageLocator.pay_title(self, pay_title)  # 點擊 面對面
        self.wait_loading_finish()

        if status is True:
            return
        else:
            if self.is_element_finded(DepositPageLocator.m_btn_next) is True:
                self.click(DepositPageLocator.m_btn_next)

            self.type(DepositPageLocator.deposit_amount, money)  # 輸入金額

            if self.is_element_finded(DepositPageLocator.deposit_qrcode_next_btn):
                self.click(DepositPageLocator.deposit_qrcode_next_btn)    
                self.wait_visibility(DepositPageLocator.username_qr)
                message = self.get_text(DepositPageLocator.username_qr)

                assert str(message).__contains__(user), '找不到開戶人名稱:%s' % user

    # 前台確認支付寶/微信轉帳
    def checktr_deposit(self, name, user, pay_title, money, status=False):
        self.wait_loading_finish()
        DepositPageLocator.deposit_name(self, name)  # 點擊支付寶 or 微信
        self.wait_loading_finish()
        DepositPageLocator.pay_title(self, pay_title)  # 點擊 轉帳
        self.wait_loading_finish()
        
        if status is True:
            return
        else:
            if name == '支付宝':
                DepositPageLocator.users_find_and_check(self, user)
                self.wait_visibility(DepositPageLocator.deposit_amount)
                self.type(DepositPageLocator.deposit_amount, money)
                self.click(DepositPageLocator.m_btn_next)
                self.wait_loading_finish()
                self.type(DepositPageLocator.m_input_deposit_airpay_name_2, '機器人測試')
            else:
                self.wait_visibility(DepositPageLocator.deposit_amount)
                self.type(DepositPageLocator.deposit_amount, money)
                self.click(DepositPageLocator.m_btn_next)
                self.wait_loading_finish()
                DepositPageLocator.users_find_and_check(self, user)


    # 前台確認支付寶/微信轉帳/USDT轉帳
    def nwap_checktr_deposit(self, name, user, pay_title, money, status=False):
        self.wait_loading_finish()
        DepositPageLocator.deposit_name(self, name)  # 點擊支付寶 or 微信 or USDT
        self.wait_loading_finish()
        DepositPageLocator.pay_title(self, pay_title)  # 點擊 轉帳
        self.wait_loading_finish()
        
        if platform.system() == 'Linux':
            folder_path = os.path.abspath(__file__).split('/Project')[0]
        else:
            folder_path = os.path.abspath(__file__).split('\Project')[0]
        dir_path = "{0}/image/wap/lottery/{1}/{1}.png".format(folder_path, 'HK')

        if status is True:
            return
        else:
            if name == '支付宝':
                DepositPageLocator.users_find_and_check(self, user)
                self.wait_visibility(DepositPageLocator.deposit_amount)
                self.type(DepositPageLocator.deposit_amount, money)
                self.type_tab(DepositPageLocator.deposit_amount)
                self.sleep(1)
                self.click(DepositPageLocator.m_btn_next)
                self.wait_loading_finish()
                self.type(DepositPageLocator.m_input_deposit_airpay_name_2, '機器人測試')
                self.type(DepositPageLocator.m_upfile, dir_path)
                self.type_tab(DepositPageLocator.m_input_deposit_airpay_name_2)
                self.sleep(1)
            elif name =='微信':
                self.wait_visibility(DepositPageLocator.deposit_amount)
                self.type(DepositPageLocator.deposit_amount, money)
                self.type_tab(DepositPageLocator.deposit_amount)
                self.sleep(1)

                self.click(DepositPageLocator.m_btn_next)
                self.wait_loading_finish()
                real_money = self.get_real_money(money)
                DepositPageLocator.wechat_user_check_nwap(self, user)
                self.click(DepositPageLocator.m_btn_next)
                self.wait_loading_finish()

                self.type(DepositPageLocator.m_upfile, dir_path)
                return real_money
            # USDT, user帶錢包地址
            else:
                DepositPageLocator.address_find_and_check(self, user)

    # 確認線上支付建立成功
    def check_onlinepay(self, name='', title='', pay_method='', status=False):
        if type(name) == list:
            for bank in name:
                 DepositPageLocator.deposit_name(self, bank, True)
            return

        DepositPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()
        DepositPageLocator.deposit_mode_check(self, pay_method)

    # 確認銀聯支付建立成功
    def check_unionpay(self, name, title, pay_method, status=False):
        if type(name) == list:
            for bank in name:
                 DepositPageLocator.deposit_name(self, bank, True)
            return

        DepositPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()

        assert self.is_element_finded(DepositPageLocator.unionpay_title) is True, f'找不到{pay_method}'

        # if status == True:
        #     return
        # else:
        #     self.click(DepositPageLocator.pay_methods(self,pay_method))
        #     message_p = self.get_text(DepositPageLocator.pay_methods(self,pay_method))

        #     assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method

    # 確認京東支付建立成功
    def check_jdpay(self, name, title, pay_method, status=False):
        if type(name) == list:
            for bank in name:
                 DepositPageLocator.deposit_name(self, bank, True)
            return

        DepositPageLocator.deposit_name(self, name)  # 點擊線上支付
        self.wait_loading_finish()

        assert self.is_element_finded(DepositPageLocator.jdpaypay_title) is True, f'找不到{pay_method}'

        # if status == True:
        #     return
        # else:
        #     self.click(DepositPageLocator.pay_methods(self,pay_method))
        #     message_p = self.get_text(DepositPageLocator.pay_methods(self,pay_method))

        #     assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method

    # 確認順付WellPay帳號入款建立成功
    def check_wellpay_account(self, name='', title='', pay_method=''):
        self.wait_loading_finish()
        DepositPageLocator.deposit_name(self, name)
        self.wait_loading_finish()
        DepositPageLocator.pay_title(self, title)
        self.wait_loading_finish()
        message = self.get_text(DepositPageLocator.wellpay_title)    # 順付入款
        assert message == title, '找不到名稱:%s' % title

        self.wait_visibility(DepositPageLocator.m_btn_next) # 等待頁面切換完成
        assert self.is_element_finded(DepositPageLocator.pay_methods(self, pay_method)) == True, '無指定支付方式'
        self.click(DepositPageLocator.pay_methods(self, pay_method))
        message_p = self.get_text(DepositPageLocator.pay_methods(self, pay_method))
        assert message_p == pay_method, '找不到支付方式名稱:%s' % pay_method


    def get_real_money(self,MoneyTo):
        real_money=self.get_text(DepositPageLocator.real_money)

        assert float(real_money) - float(MoneyTo) < 1,'儲值金額與實際金額誤差超過1 實際金額:%s 輸入金額:%s'%(real_money,MoneyTo)
        return real_money
    
         # 儲值 線上支付
    def do_all_online_deposit(self, money, pay_method):
        self.wait_loading_finish()
        self.click(DepositPageLocator.pay_methods(self,pay_method))
        self.type(DepositPageLocator.deposit_amount, money)  # 存入金額
        self.sleep(1)

        self.click(DepositPageLocator.m_deposit_submit_btn2)  # 確認提交
        self.sleep(5)
        self.switch_window(self.driver.window_handles[0])
        self.wait_loading_finish()
        self.click(DepositPageLocator.deposit_dialog_ok_btn)
