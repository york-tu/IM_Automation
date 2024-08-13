from random import randint
from random import choice
from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
from pages.webs.mobile.mobile_membercenterpage import MemberCenterPage
import random, datetime

class MemberInfoLocator:
    @staticmethod # menu進入點
    def menu_into(name):
        into = (By.XPATH, f"//span[text()='{name}']")
        return into
    
    @staticmethod # 進入修改位置
    def edit_into(name):
        into = (By.XPATH, f"//p[contains(text(), '{name}')]/..")
        return into
    
    @staticmethod # 修改內容
    def change_info(name, num=1):
        into = (By.XPATH, f"(//input[@placeholder='{name}'])[{num}]")
        return into
    
    @staticmethod # NWAP選擇銀行
    def change_bank(num=1):
        into = (By.XPATH, f"(//p[@class='title'])[{num}]")
        return into

    @staticmethod # 選擇出款方式
    def payment_method(name):
        into = (By.XPATH, f"//p[@class='item-text__title' and text()='{name}']")
        return into

    # 送出視窗
    submit_up = (By.XPATH, "//*[text()='确认送出' or text()='确定送出' and not(contains(@class, 'disabled'))]") # 檢查按鈕反灰等問題
    submit = (By.XPATH, "//div[contains(@class,'footer')]/*[text()='确认送出' or text()='确定送出']") # 確定送出
    error_message = (By.XPATH, "//p[@class='el-value__error-message']") # 格式等錯誤問題
    ok_btn = (By.XPATH, "//button[text()='OK']")  # 點擊ok
    nwap_ok_btn = (By.XPATH, "//button[contains(@class,'van-button')]")
    result_window = (By.XPATH, "//div[@role='dialog']") # 送出結果視窗
    result_window_confirm = (By.XPATH, "//div[@role='dialog']//button[contains(@class,'confirm')]") # 送出結果視窗
    readonly_check = (By.XPATH, "//input[@readonly='readonly' or contains(@data-bind,'disabled')]")
    return_btn = (By.XPATH, "//a[@class='btn-return' or @class='home_btn']")

    # 銀行編輯
    cqbank_items = (By.XPATH, "//div[@class='card-edit' or @class='com-inner__content']") # 此帳號擁有的銀行卡號清單
    wallet_items_cgpay = (By.XPATH, "//p[text()='CGPay']") # 綁定虛擬錢包_CGPay
    wallet_items_nwap = (By.XPATH, "//div[@class='bind-card__item']") # 此帳號擁有的出款方式
    add_credit_card = (By.XPATH, "//p[text()='新增银行卡']") # 新增銀行卡
    add_virtual_wallet = (By.XPATH, "//p[text()='新增虚拟钱包']") # 新增虚拟钱包
    cgbank_check_point = (By.XPATH, "//li[@data-context='profile.card']/div[text()='收起']")  # 確認編輯有點到變成收起鈕
    cgbank_name_check = (By.XPATH, "//input[@placeholder='请输入开户人真实姓名' and @readonly='readonly']")
    cgbank_name = (By.XPATH, "//input[@placeholder='请输入开户人真实姓名']")
    cgbank_select = (By.XPATH, "//select[contains(@data-bind,'cardbankselect')]") # 選擇開戶銀行
    cgbank_select_nwap = (By.XPATH, "//input[@placeholder='请选择']") # NWAP選擇開戶銀行
    cgbank_cardnumber = (By.XPATH,"//input[@placeholder= '请输入银行卡号' or @placeholder= '请输入13-19位数字']")
    cgbank_input_card_branch = (By.XPATH, "//input[@placeholder = '省(自治区)']")  # 開戶網點前三碼
    cgbank_input_card_city = (By.XPATH, "//input[@placeholder = '城市(区)']")  # 開戶網點後三碼
    wallet_address = (By.XPATH, "//input[contains(@placeholder, '请输入钱包地址')]")  # 輸入錢包地址
    cgbank_input_securitycode = (By.XPATH, "//input[@placeholder='请输入6位数字' and @type='password']")  # 提款密碼
    cgbank_submit = (By.XPATH, "//*[contains(text(),'确定新增')]")  # 送出
    cqbank_error = (By.XPATH, "//div[@class='el-value']//p[@style and contains(@data-bind, 'validationMessage')]")
    check_point_bank = (By.XPATH, "(//div[@class='basic_info_data'])[5]")  # 已綁定銀行
    cqbank_submit_window = (By.XPATH, "//div[@class='swal2-contentwrapper']")  # 送出訊息視窗
    cqbank_submit_nwap = (By.XPATH, "//div[@class='van-dialog__content']")
    cqbank_windows_ok = (By.XPATH, "//button[text()='OK']")  # 點擊ok
    cqbank_select_ok = (By.XPATH, "//button[@type='button' and text()= '确定']")
    wallet_select = (By.XPATH, "//div[@style='']/select[@class='el-input__select']")
    wallet_option_cgpay = (By.XPATH, "//option[@value='cgpay']")
    wallet_name_input_nwap = (By.XPATH, "//label[@class='el-select el-select--active']") # 可選擇時的錢包名稱
    
    # 提款密碼編輯
    edit_spwd_btn = (By.XPATH, "//li[@data-context='profile.securitycode']/div[text()='编辑']")  # 編輯按鈕
    cgspwd_check_point = (By.XPATH, "//li[@data-context='profile.securitycode']/div[text()='收起']")  # 確認編輯有點到變成收起鈕
    cgspwd_input_oldpwd= (By.XPATH, "//input[@placeholder='旧的提款密码']")
    cgspwd_input_newpwd = (By.XPATH, "//input[@placeholder='新的提款密码']")
    cgspwd_input_newpwd2 = (By.XPATH, "//input[@placeholder='重复提款密码']")
    cgspwd_submit = (By.XPATH, "(//div[text()='送出'])[5]")

    # 登錄密碼編輯
    edit_pwd_btn = (By.XPATH, "//li[@data-context='profile.passwd']/div[text()='编辑']")  # 編輯按鈕
    cgpwd_check_point = (By.XPATH, "//li[@data-context='profile.passwd']/div[text()='收起']")  # 確認編輯有點到變成收起鈕
    cgpwd_input_oldpwd = (By.XPATH, "//input[@placeholder='请输入旧的密码']")
    cgpwd_input_newpwd = (By.XPATH, "//input[contains(@placeholder,'新的密码')]")
    cgpwd_input_newpwd2 = (By.XPATH, "//input[contains(@placeholder,'新密码') and contains(@placeholder,'再次')]")
    cgpwd_input_securitycode = (By.XPATH, "(//input[@placeholder='请输入六位数提款密码'])[5]")
    cgpwd_submit = (By.XPATH, "(//div[text()='送出'])[6]")
    js_wallet = "input[placeholder='请选择钱包名称']"

    # 綁定虛擬錢包_帳戶安全
    bind_mobile = (By.XPATH, "//div[@data-bind='visible: bindMobileShow' and @style='']")
    bind_mobile_input = (By.XPATH, "//input[@data-bind='numeric, textInput: bindPhoneNumber']")
    bind_securitycode = (By.XPATH, "//input[@data-bind='numeric, textInput: securityNumber']")
    bind_confirm = (By.XPATH, "//a[text()='确认送出']")
    verify_mobile = (By.XPATH, "//div[@data-bind='visible: verifyMobileShow' and @style='']")
    verify_mobile_input =(By.XPATH, "//input[@data-bind='numeric, textInput: phoneNumber']")
    verify_confirm = (By.XPATH, "//a[text()='验证']")
    verify_cancel = (By.XPATH, "//div[@data-bind='visible: verifyMobileShow']//*[text()='取消']")
    verify_cancel_nwap = (By.XPATH,"//a[text()='取消']")
    change_phone = (By.XPATH, "//div[@class='contact-info-list__item']/p[text()='手机号码']")
    dialog_error_message_nwap = (By.XPATH, "//div[@aria-labelledby='提示']/div/div")
    
    securitycode_input = (By.XPATH, "//input[@placeholder='请输入6位数字' and @type='password']")
    def wallet_nwap(name):
        name = (By.XPATH, f"//*[contains(text(), '{name}')]")
        return name

    card_nembers = [
        6223428750972618744,6226845912966671,6223077077428244295,6223410465840261,5049230180911328,6225095209026630996,4340626481303645,
        6223450675569179787,4563517021467452186,6226606909686247,9843012961309470,6226812387177798992,6223287162347525002,4427307512870839,
        62231064689265756,6224926743637236,6226193694225903,6223374628832187,6223430651184380949,8703005458537349,
    ]
class MemberInfoPage(BasePage):
    # 進入我的資料
    def into_account(self):
        MemberCenterPage.into_member_info(self)

    def check_result(self):
        error_list = []
        if self.is_element_finded(MemberInfoLocator.submit_up) is True:
            self.sleep(0.5)
            self.click(MemberInfoLocator.submit)
            self.wait_visibility(MemberInfoLocator.result_window)
            message = (self.get_text(MemberInfoLocator.result_window)).replace('\nOK','')

            assert message.__contains__('修改成功') or message.__contains__('绑定成功'), f'修改失敗 \n訊息:\n{message}'
            if self.is_element_finded(MemberInfoLocator.ok_btn) is True:
                self.click(MemberInfoLocator.ok_btn)
            else:
                self.wait_loading_finish() 
                self.click(MemberInfoLocator.nwap_ok_btn)
        else:
            for message in self.find_elements(MemberInfoLocator.error_message):
                error_list.append(message)

    def do_change_mail(self, email, securitycode):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('联系方式'))
        self.wait_loading_finish()
        self.click(MemberInfoLocator.edit_into('电子邮箱'))

        assert self.is_element_finded(MemberInfoLocator.edit_into('电子邮箱')), f'進入电子邮箱錯誤'
        
        self.wait_loading_finish()
        if self.is_element_finded(MemberInfoLocator.readonly_check) == True:
            self.click(MemberInfoLocator.return_btn)
        else:
            self.type(MemberInfoLocator.change_info('请输入e-mail'), email)
            self.type(MemberInfoLocator.securitycode_input, securitycode)
            self.check_result()

    def do_change_phone(self, phone, securitycode):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.change_phone)
        assert self.is_element_finded(MemberInfoLocator.edit_into('手机号码（11位数字）')), f'進入手机号码錯誤'

        self.wait_loading_finish()
        if self.is_element_finded(MemberInfoLocator.readonly_check) == True:
            self.click(MemberInfoLocator.return_btn)
        else:
            self.type(MemberInfoLocator.change_info('请输入11位手机号码'), phone)
            self.type(MemberInfoLocator.securitycode_input, securitycode)
            self.check_result()

    def do_change_phone_nwap(self, phone, securitycode):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.edit_into('手机号码'))
        assert self.is_element_finded(MemberInfoLocator.edit_into('手机号码')), f'進入手机号码錯誤'

        self.wait_loading_finish()
        if self.is_element_finded(MemberInfoLocator.readonly_check) == True:
            self.click(MemberInfoLocator.return_btn)
        else:
            self.type(MemberInfoLocator.change_info('请输入手机号码'), phone)
            self.type(MemberInfoLocator.securitycode_input, securitycode)
            self.check_result()

    def do_change_qq(self, qq, securitycode):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.edit_into('QQ号码'))
        assert self.is_element_finded(MemberInfoLocator.edit_into('QQ号码')), f'進入QQ号码錯誤'

        self.wait_loading_finish()
        if self.is_element_finded(MemberInfoLocator.readonly_check) == True:
            self.click(MemberInfoLocator.return_btn)
        else:
            self.type(MemberInfoLocator.change_info('请输入4-20位数字'), qq)
            self.type(MemberInfoLocator.securitycode_input, securitycode)
            self.check_result()

    def random_choose_bank(self,num):
        return By.XPATH, "//select[contains(@data-bind, 'cardbankselect')]/option[%d]"%(num)

    def do_change_bank(self, card_branch, card_city, securitycode):
        error_list = []
        num = randint(2, 15)
        BankCard = choice(MemberInfoLocator.card_nembers)
        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('绑定出款方式'))
        self.wait_loading_finish()
        self.click(MemberInfoLocator.payment_method('银行卡'))
        self.wait_loading_finish()

        if self.is_element_finded(MemberInfoLocator.cqbank_items) is False:
            if self.is_element_enable(MemberInfoLocator.cgbank_cardnumber):
                self.type(MemberInfoLocator.cgbank_cardnumber,BankCard)
                self.select_by_index(MemberInfoLocator.cgbank_select, num)
                self.type(MemberInfoLocator.cgbank_input_card_branch, card_branch)
                self.type(MemberInfoLocator.cgbank_input_card_city, card_city)
                self.type(MemberInfoLocator.cgbank_input_securitycode, securitycode)

                error = self.find_elements(MemberInfoLocator.cqbank_error)
                for message in error:
                    message = self.get_text_by_dom(message)
                    if message != '':
                        error_list.append(message)
                        
                if len(error_list) > 0:
                    raise EOFError(f'設定銀行卡號錯誤 \n訊息:\n{error_list}')
                
                self.click(MemberInfoLocator.cgbank_submit)
                self.wait_visibility(MemberInfoLocator.cqbank_submit_window)
                error_message = self.get_text(MemberInfoLocator.cqbank_submit_window)

                assert error_message.__contains__('新增成功'), f'新增失敗 \n訊息:\n {error_message}'
            else:
                self.back()


    def do_change_virtualcard(self, securitycode, phone):
        # 綁定虛擬錢包
        virtual_card = datetime.datetime.now().strftime('0x00bot%Y%m%d%H%M%Sx00' + str(random.randrange(1, 10000)))

        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('绑定出款方式'))
        self.wait_loading_finish()
        assert self.is_element_finded(MemberInfoLocator.payment_method('虚拟钱包')) is True, "綁定出款方式_虛擬錢包已被禁用"
        self.click(MemberInfoLocator.payment_method('虚拟钱包'))
        self.wait_loading_finish()

        # 帳戶安全
        # 尚未設定手機號碼
        if self.is_element_finded(MemberInfoLocator.bind_mobile):
            self.type(MemberInfoLocator.bind_mobile_input, phone)
            self.type(MemberInfoLocator.bind_securitycode, securitycode)
            self.click(MemberInfoLocator.bind_confirm)
            self.check_result()
        # 已有設定手機號碼
        elif self.is_element_finded(MemberInfoLocator.verify_mobile):
            self.type(MemberInfoLocator.verify_mobile_input, phone)
            self.click(MemberInfoLocator.verify_confirm)
        else:
            raise EOFError('進入綁定虛擬錢包沒出現帳戶安全彈窗')

        self.wait_loading_finish()
        self.sleep(2)
        if self.is_element_finded(MemberInfoLocator.wallet_items_cgpay) is False:
            # self.click(MemberInfoLocator.add_virtual_wallet)      # 若已有新增其他虛擬錢包才須點擊，目前購寶不易新增故先隱藏
            # 選擇錢包名稱
            if self.is_element_finded(MemberInfoLocator.wallet_select) is True:
                self.click(MemberInfoLocator.wallet_select)
                self.click(MemberInfoLocator.wallet_option_cgpay)
            self.wait_visibility(MemberInfoLocator.wallet_address)
            self.type(MemberInfoLocator.wallet_address, virtual_card)
            self.type(MemberInfoLocator.change_info('请输入6位数字'), securitycode)
            self.click(MemberInfoLocator.cgbank_submit)

            self.wait_visibility(MemberInfoLocator.cqbank_submit_window)
            error_message = self.get_text(MemberInfoLocator.cqbank_submit_window)

            assert error_message.__contains__('新增成功'), f'新增失敗 \n訊息:\n {error_message}'         
            self.click(MemberInfoLocator.ok_btn)


    def do_change_security_password(self, old_spwd, new_spwd):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('提款密码设定'))
        self.wait_loading_finish()

        self.type(MemberInfoLocator.change_info('请输入6位数字', 2), old_spwd)
        self.type(MemberInfoLocator.change_info('请输入6位数字', 3), new_spwd)
        self.type(MemberInfoLocator.change_info('请再次输入新提款密码'), new_spwd)
        self.check_result()

    def do_change_security_password_nwap(self, old_spwd, new_spwd):
        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('提款密码设定'))
        self.wait_loading_finish()

        self.type(MemberInfoLocator.change_info('请输入6位数字'), old_spwd)
        self.type(MemberInfoLocator.change_info('请输入6位数字', 2), new_spwd)
        self.type(MemberInfoLocator.change_info('请再次输入新提款密码'), new_spwd)
        self.check_result()

    def do_change_password(self, old_pwd, new_pwd, securitycode):
        # 我的資料分頁切換至修改密碼
        self.wait_loading_finish()
        self.wait_visibility(MemberInfoLocator.menu_into('登录设定'))
        self.click(MemberInfoLocator.menu_into('登录设定'))
        self.wait_loading_finish()

        self.type(MemberInfoLocator.change_info('请输入旧的密码'), old_pwd)
        if self.is_element_finded(MemberInfoLocator.change_info('请输入8-12位英数混合密码')) is True:
            self.type(MemberInfoLocator.change_info('请输入8-12位英数混合密码'), new_pwd)  #NWAP提示文案
        else:
            self.type(MemberInfoLocator.change_info('请输入新的密码'), new_pwd)  #舊品牌提示文案
        self.type(MemberInfoLocator.change_info('请再次输入新密码'), new_pwd)
        self.type(MemberInfoLocator.change_info('请输入6位数字', 2), securitycode)
        self.check_result()

    def do_change_password_nwap(self, old_pwd, new_pwd, securitycode):
        # 我的資料分頁切換至修改密碼
        self.wait_loading_finish()
        self.wait_visibility(MemberInfoLocator.menu_into('登录设定'))
        self.click(MemberInfoLocator.menu_into('登录设定'))
        self.wait_loading_finish()

        self.type(MemberInfoLocator.change_info('请输入旧的密码'), old_pwd)
        if self.is_element_finded(MemberInfoLocator.change_info('请输入8-12位英数混合密码')) is True:
            self.type(MemberInfoLocator.change_info('请输入8-12位英数混合密码'), new_pwd)  #NWAP提示文案
        else:
            self.type(MemberInfoLocator.change_info('请输入新的密码'), new_pwd)  #舊品牌提示文案
        self.type(MemberInfoLocator.change_info('请再次输入新密码'), new_pwd)
        self.type(MemberInfoLocator.change_info('请输入6位数字'), securitycode)
        self.check_result()

    def do_nwap_change_bank(self, card_branch, card_city, securitycode, name = "自動化測試"):
        error_list = []
        num = randint(2, 15)
        BankCard = choice(MemberInfoLocator.card_nembers)
        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('绑定出款方式'))
        self.wait_loading_finish()
        self.click(MemberInfoLocator.payment_method('银行卡'))
        self.wait_loading_finish()

        if self.is_element_finded(MemberInfoLocator.wallet_items_nwap) is False:
            
            if self.is_element_finded(MemberInfoLocator.cgbank_name_check) is False:
                self.type(MemberInfoLocator.cgbank_name, name)
            else:
                pass
            self.type(MemberInfoLocator.cgbank_cardnumber,BankCard)
            self.click(MemberInfoLocator.cgbank_select_nwap)
            self.wait_click_able(MemberInfoLocator.change_bank(num))
            self.click(MemberInfoLocator.change_bank(num))
            self.type(MemberInfoLocator.cgbank_input_card_branch, card_branch)
            self.type(MemberInfoLocator.cgbank_input_card_city, card_city)
            self.type(MemberInfoLocator.cgbank_input_securitycode, securitycode)

            error = self.find_elements(MemberInfoLocator.cqbank_error)
            for message in error:
                message = self.get_text_by_dom(message)
                if message != '':
                    error_list.append(message)
                        
            if len(error_list) > 0:
                raise EOFError(f'設定銀行卡號錯誤 \n訊息:\n{error_list}')
                
            self.click(MemberInfoLocator.cgbank_submit)
            self.wait_visibility(MemberInfoLocator.cqbank_submit_nwap)
            error_message = self.get_text(MemberInfoLocator.cqbank_submit_nwap)

            assert error_message.__contains__('新增成功'), f'新增失敗 \n訊息:\n {error_message}'   
            self.wait_loading_finish()
            self.click(MemberInfoLocator.result_window_confirm)   
        else:
            self.back()    


    def do_nwap_change_virtual_card(self, securitycode, phone, name = "自動化測試"):
        # 綁定虛擬錢包
        virtual_card = datetime.datetime.now().strftime('0x00bot%Y%m%d%H%M%Sx00' + str(random.randrange(1, 10000)))

        self.wait_loading_finish()
        self.click(MemberInfoLocator.menu_into('绑定出款方式'))
        self.wait_loading_finish()
        assert self.is_element_finded(MemberInfoLocator.payment_method('虚拟钱包')) is True, "綁定出款方式_虛擬錢包已被禁用"
        self.click(MemberInfoLocator.payment_method('虚拟钱包'))
        self.wait_loading_finish()

        # 帳戶安全
        # 尚未設定手機號碼
        if self.is_element_finded(MemberInfoLocator.bind_confirm):
            self.type(MemberInfoLocator.change_info('请输入手机号码'), phone)
            self.type(MemberInfoLocator.change_info('请输入6位数字'), securitycode)
            self.click(MemberInfoLocator.bind_confirm)
            self.wait_visibility(MemberInfoLocator.result_window)
            message = (self.get_text(MemberInfoLocator.result_window)).replace('\nOK','')
            assert message.__contains__('修改成功'), f'修改失敗 \n訊息:\n{message}'
            self.click(MemberInfoLocator.nwap_ok_btn)
        # 已有設定手機號碼
        elif self.is_element_finded(MemberInfoLocator.verify_confirm):
            self.type(MemberInfoLocator.change_info('请输入手机号码'), phone)
            self.click(MemberInfoLocator.verify_confirm)
            assert self.is_element_finded(MemberInfoLocator.dialog_error_message_nwap) is False, self.get_text(MemberInfoLocator.dialog_error_message_nwap)
        else:
            raise EOFError('進入綁定虛擬錢包沒出現帳戶安全彈窗')

        self.wait_loading_finish()
        if self.is_element_finded(MemberInfoLocator.wallet_nwap("CGPay")) is False:
            # self.click(MemberInfoLocator.add_virtual_wallet)        # 若已有新增其他虛擬錢包才須點擊，目前購寶不易新增故先隱藏
            self.wait_loading_finish()

            if self.is_element_finded(MemberInfoLocator.cgbank_name_check) is False:
                self.type(MemberInfoLocator.cgbank_name, name)
            if self.is_element_finded(MemberInfoLocator.wallet_name_input_nwap) is True:
                self.click_js(MemberInfoLocator.js_wallet)
                self.sleep(1)
                self.click(MemberInfoLocator.wallet_nwap("CGPay"))
                self.sleep(1)
                self.click(MemberInfoLocator.cqbank_select_ok)
            self.type(MemberInfoLocator.wallet_address, virtual_card)
            self.type(MemberInfoLocator.cgbank_input_securitycode, securitycode)
            self.click(MemberInfoLocator.cgbank_submit)

            self.wait_visibility(MemberInfoLocator.cqbank_submit_nwap)
            error_message = self.get_text(MemberInfoLocator.cqbank_submit_nwap)

            assert error_message.__contains__('新增成功'), f'新增失敗 \n訊息:\n {error_message}'
            self.wait_loading_finish()
            self.click(MemberInfoLocator.result_window_confirm)
        else:
            self.back() 