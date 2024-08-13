import unittest, sys, os, datetime, random, re, string
from retrying import retry
from airtest.core.api import *

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
import stf_api.stf as stf
import driver.app_driver as app_dr
from common.app.decorator import DecorateClass
from Project.lottery.app.testcase.base_testcase import BaseTestCase
from Project.lottery.app.pages.pages import AppPages
from Project.lottery.apis.function_layer.functions import Functions
from Project.lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API

class AppTestCase(BaseTestCase, BaseFunction_API):
    brand = gl.get_value('BRAND')
    # ================================= TestSetting ================================

    @classmethod
    def setUpClass(cls):
        cls.setting_test_data(cls)  # 設定測試數據
        poco, wda_service = app_dr.AppDriver.airtest_connect_phone(cls) # 連線測試手機
        cls.function_dict['ap'] = AppPages((poco, wda_service, cls.skipTest))
        cls.folderpath = gl.get_value('FOLDER_PATH')
    
    def setUp(self):
        if gl.get_value('VERSION_MESSAGE') != None:
            self.function_dict['ap'].commonPage().skip_test(gl.get_value('VERSION_MESSAGE'))
        
        self.functions = Functions()
        self.test_choose_app()

    def tearDown(self):
        try:
            image_path = f"{self.folderpath}/{self._testMethodName}.png"
            image_path_list = [image_path]
            snapshot(filename=image_path, msg=f"{self.id()}")
            stop_app(self.package)
            self.check_result(str(self.id()).split('.')[-1])
            gl.set_value('IMG_PATH', image_path_list)
        except Exception as e:
            if 'No available screen capture method found' in str(e):
                pass
            else:
                raise e

    @classmethod
    def tearDownClass(cls):
        clear_app(cls.package)
        clear_app(cls.poco_package)
        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))
        
    # @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def test_choose_app(self):
        # 選APP
        try:
            self.function_dict['ap'].commonPage().find_app(self.package)
            # if self.first_testcase[0] == True:
            login_status = self.function_dict['ap'].mainPage().into_home_check_napp(self._login_status[0], self.brand)
            if login_status == '開啟app錯誤':
                self.tearDown()
                raise EOFError(login_status)
            if login_status == False:
                self._login_status[0] = False
            # else:
            #     login_status = self.function_dict['ap'].mainPage().into_home_check_napp(self._login_status[0], self.brand)
            #     if login_status == '開啟app錯誤':
            #         self.tearDown()
            #         raise EOFError(login_status)
            #     if login_status == False:
            #         self._login_status[0] = False
        except Exception as e:
            if 'device offline' in str(e):
                self.device_reconnect()     # 手機斷線重連
            elif 'device' and 'not found' in str(e):
                self.device_reconnect()
            else:
                raise e
            pass

    def device_reconnect(self):
        gl.set_value('PHONE_NAME', 'None')
        self._login_status[0] = False
        self.tearDownClass()
        self.sleep(60)
        self.setUpClass()
        self.setUp()

    @DecorateClass('PFREQ-T6633')    
    def test_register(self):
        account = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(9))
        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].mainPage().register_napp()
        self.function_dict['ap'].registerPage().register_napp(account,'ps111111')
        self.function_dict['ap'].mainPage().after_register(self.brand)
        self.function_dict['ap'].mainPage().logout_napp()

    # @DecorateClass('PFREQ-T6122')
    # def test_version_check(self):
    #     app_version = self.app_version
    #     self.function_dict['ap'].mainPage().member_click_napp()
    #     self.function_dict['ap'].systeminfoPage().version_napp(app_version)

    # 手機狀態檢查，此testcase如果pass表示APP正常啟用至首頁
    def test_phone_status(self):
        pass

    @DecorateClass('PFREQ-T6632')
    def test_login(self):
        level = 0   # 這裡的level沒有作用，只是有些function需要帶一個參數
        if self._login_status[0] == False:
            self.function_dict['ap'].mainPage().member_click_napp()
            self.function_dict['ap'].mainPage().login_napp(self.app_account, self.app_password)
            self._login_status[0] = True
            self.function_dict['ap'].mainPage().skip_change_password(level)
            self.function_dict['ap'].mainPage().home_click_napp()
            self.function_dict['ap'].mainPage().skip_announcement_napp(level)
            self.function_dict['ap'].mainPage().skip_mail_popup(level)

    # ----彩票---------------------------------------------------
    @DecorateClass('PFREQ-T6568')
    def test_betting_hk(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_hk()
        self.function_dict['ap'].hkPage().bet_mark6_lottery('1') 
        self.function_dict['ap'].lotteryPage().bet_lottery_record('香港彩票')

    @DecorateClass('PFREQ-T6572')
    def test_betting_wfssc(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_wfssc()
        self.function_dict['ap'].sscPage().bet_ssc_lottery_napp('1') 
        self.function_dict['ap'].lotteryPage().bet_lottery_record('五分时时彩')

    @DecorateClass('PFREQ-T6571')
    def test_betting_wfpk10(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_wfpk10()
        self.function_dict['ap'].pk10Page().bet_pk10_lottery_napp('1')
        self.function_dict['ap'].lotteryPage().bet_lottery_record('五分PK拾')

    @DecorateClass('PFREQ-T6573')
    def test_betting_twxy28(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_twxy28()
        self.function_dict['ap'].xy28Page().bet_xy28_lottery_napp('1')
        self.function_dict['ap'].lotteryPage().bet_lottery_record('台湾幸运28')

    @DecorateClass('PFREQ-T6569')
    def test_betting_wf11x5(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_wf11x5()
        self.function_dict['ap'].x5Page().bet_11x5_lottery('1')
        self.function_dict['ap'].lotteryPage().bet_lottery_record('五分11选5')

    @DecorateClass('PFREQ-T6567')
    def test_betting_wfk3(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_wfk3()
        self.function_dict['ap'].k3Page().bet_k3_lottery_napp('1')
        self.function_dict['ap'].lotteryPage().bet_lottery_record('五分快3')

    @DecorateClass('PFREQ-T6570')
    def test_betting_fc3d(self):
        self.test_login()

        self.function_dict['ap'].mainPage().lottery_home_napp()
        self.function_dict['ap'].lotteryPage().enter_fc3d()
        self.function_dict['ap'].fc3dPage().bet_fc3d_lottery_napp('1')
        self.function_dict['ap'].lotteryPage().bet_lottery_record('福彩3D')
    
    # ----棋牌---------------------------------------------------
    @DecorateClass('PFREQ-T6574')
    def test_bet_fgcard(self):
        if self.brand == 'sc':
            self.function_dict['ap'].commonPage().skip_test(f'{self.brand}沒有此第三方遊戲')
        self.test_login()

        money = gl.get_value('FG')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}')

        self.function_dict['ap'].mainPage().search_fg_card()
        self.function_dict['ap'].fgcardPage().fg_card()
    
    @DecorateClass('PFREQ-T6575')
    def test_bet_vgcard(self):
        self.test_login()

        money = gl.get_value('VG')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}')

        self.function_dict['ap'].mainPage().search_vg_card()
        self.function_dict['ap'].vgcardPage().vg_card()
    
    @DecorateClass('PFREQ-T6576')
    def test_bet_kycard(self): 
        self.test_login()

        money = gl.get_value('KY')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_ky_card()
        self.function_dict['ap'].kycardPage().ky_card()

    @DecorateClass('PFREQ-T6577')
    def test_bet_bscard(self):
        self.test_login()

        money = gl.get_value('BSP')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_bs_card()
        self.function_dict['ap'].bscardPage().bs_card()
    
    @DecorateClass('PFREQ-T6578')
    def test_bet_kxcard(self):
        self.test_login()

        money = gl.get_value('KX')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_lc_card()
        self.function_dict['ap'].lscardPage().lc_card()

    @DecorateClass('PFREQ-T6579')
    def test_bet_gmcard(self):
        self.test_login()

        money = gl.get_value('GM')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_gm_card()
        self.function_dict['ap'].gmcardPage().gm_card()
    
    @DecorateClass('PFREQ-T6580')
    def test_bet_kkcard(self):
        self.test_login()

        money = gl.get_value('KK')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_kk_card()
        self.function_dict['ap'].kkcardPage().kk_card()

    # ----電子---------------------------------------------------
    @DecorateClass('PFREQ-T6581')
    def test_bet_cq9game(self):
        self.test_login()

        money = gl.get_value('CQ9')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_cq9_electronic()
        self.function_dict['ap'].cq9electronicPage().cq9_electronic()

    @DecorateClass('PFREQ-T6582')
    def test_bet_ptgame(self):
        self.test_login()

        money = gl.get_value('PT')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_pt_electronic()
        self.function_dict['ap'].ptelectronicPage().pt_electronic()

    @DecorateClass('PFREQ-T6583')
    def test_bet_lgdgame(self):
        self.test_login()

        money = gl.get_value('DT')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_lgd_electronic()
        self.function_dict['ap'].dtelectronicPage().lgd_electronic()

    @DecorateClass('PFREQ-T6584')
    def test_bet_fggame(self):
        if self.brand == 'sc':
            self.function_dict['ap'].commonPage().skip_test(f'{self.brand}沒有此第三方遊戲')
        self.test_login()

        money = gl.get_value('FG')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}') 

        self.function_dict['ap'].mainPage().search_fg_electronic()
        self.function_dict['ap'].fgelectronicPage().fg_electronic()

    @DecorateClass('PFREQ-T6585')
    def test_bet_swgame(self):
        self.test_login()

        money = gl.get_value('SW')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_sw_electronic()
        self.function_dict['ap'].swelectronicPage().sw_electronic()

    @DecorateClass('PFREQ-T6586')
    def test_bet_bbingame(self):
        self.test_login()

        money = gl.get_value('BBIN')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_bbin_electronic()
        self.function_dict['ap'].bbinelectronicPage().bbin_electronic()

    @DecorateClass('PFREQ-T6587')
    def test_bet_kkgame(self):
        self.test_login()

        money = gl.get_value('KK')

        if money != None and money < 30:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於30, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_kk_electronic()
        self.function_dict['ap'].kkelectronicPage().kk_electronic()
    
    #----體育----------------------------------------------------------
    @DecorateClass('PFREQ-T6588')
    def test_bet_sbsport(self):
        self.test_login()

        money = gl.get_value('SB')

        if money != None and money < 10:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於10, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_sb_sport()
        self.function_dict['ap'].sbsportPage().sb_sport()

    @DecorateClass('PFREQ-T6589')
    def test_bet_bbinsport(self):
        if self.brand == 'sc':
            self.function_dict['ap'].commonPage().skip_test(f'{self.brand}沒有此第三方遊戲')
        self.test_login()

        money = gl.get_value('BBIN')

        if money != None and money < 10:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於10, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_bbin_sport()
        self.function_dict['ap'].bbinsportPage().bbin_sport()

    @DecorateClass('PFREQ-T6590')
    def test_bet_sssport(self):
        self.test_login()

        money = gl.get_value('3S')

        if money != None and money < 10:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於10, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_ss_sport()
        self.function_dict['ap'].sssportPage().ss_sport()

    @DecorateClass('PFREQ-T6591')
    def test_bet_hgsport(self):
        self.test_login()

        money = gl.get_value('HG')

        if money != None and money < 10:
            self.function_dict['ap'].commonPage().skip_test(f'金額低於10, 目前餘額:{money}')  

        self.function_dict['ap'].mainPage().search_hg_sport()
        self.function_dict['ap'].hgsportPage().hg_sport()

    def test_bet_agfish(self):
        self.test_login()

        self.function_dict['ap'].mainPage().search_ag_fish()

    @DecorateClass('PFREQ-T6629')
    def test_niu_niu_bet(self):
        self.test_login()

        self.function_dict['ap'].mainPage().red_envelope_click()
        money, amount, magnification = self.function_dict['ap'].redenvelopePage().niu_niu()
        self.function_dict['ap'].basePage().go_back()
        self.function_dict['ap'].mainPage().home_click()
        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().bet_record_click()
        self.function_dict['ap'].betrecordPage().bet_niu_niu_record(money, amount, magnification)
    
    @DecorateClass('PFREQ-T6630')
    def test_mine_sweeping_bet(self):
        self.test_login()

        self.function_dict['ap'].mainPage().red_envelope_click()
        money, num, amount = self.function_dict['ap'].redenvelopePage().mine_sweeping(2)
        self.function_dict['ap'].basePage().go_back()
        self.function_dict['ap'].mainPage().home_click()
        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().bet_record_click()
        self.function_dict['ap'].betrecordPage().bet_mine_record(money, num, amount)

    #--------------------------------------------------------------
    # @DecorateClass('PFREQ-T6592')
    # def test_get_wallet_info(self):       # 只是為了要知道各錢包金額，先註解掉日後評估有無必要
    #     self.test_login()

    #     wallet = self.wallet

    #     self.function_dict['ap'].mainPage().member_click()
    #     self.function_dict['ap'].memberPage().transform_click()
    #     self.function_dict['ap'].transformPage().get_wallet_amount(wallet_list=wallet)

    @DecorateClass('PFREQ-T6593')
    def test_transform_ag(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','AG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('AG','主钱包', '5')

    @DecorateClass('PFREQ-T8130')
    def test_transform_bg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','BG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('BG','主钱包', '5')

    @DecorateClass('PFREQ-T6594')
    def test_transform_mg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','MG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('MG','主钱包', '5')
        
    @DecorateClass('PFREQ-T6595')
    def test_transform_sb(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','SB', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('SB','主钱包', '5')
    
    @DecorateClass('PFREQ-T6596')
    def test_transform_bbin(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','BBIN', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('BBIN','主钱包', '5')
        
    @DecorateClass('PFREQ-T6597')
    def test_transform_3s(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','3S', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('3S','主钱包', '5')
        
    @DecorateClass('PFREQ-T6598')
    def test_transform_lgd(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','LGD', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('LGD','主钱包', '5')
    
    @DecorateClass('PFREQ-T6600')
    def test_transform_ky(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','KY', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('KY','主钱包', '5')
    
    @DecorateClass('PFREQ-T6601')
    def test_transform_vg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','VG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('VG','主钱包', '5')
    
    @DecorateClass('PFREQ-T6602')
    def test_transform_sw(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','SW', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('SW','主钱包', '5')
    
    @DecorateClass('PFREQ-T6603')
    def test_transform_pt(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','PT', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('PT','主钱包', '5')
    
    @DecorateClass('PFREQ-T6604')
    def test_transform_kx(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','KX', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('KX','主钱包', '5')
    
    @DecorateClass('PFREQ-T6605')
    def test_transform_hg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','HG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('HG','主钱包', '5')

    @DecorateClass('PFREQ-T6606')
    def test_transform_gm(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','GM', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('GM','主钱包', '5')
    
    @DecorateClass('PFREQ-T6607')
    def test_transform_fg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','FG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('FG','主钱包', '5')
    
    @DecorateClass('PFREQ-T6608')
    def test_transform_dg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','DG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('DG','主钱包', '5')

    @DecorateClass('PFREQ-T6609')
    def test_transform_cq9(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','CQ9', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('CQ9','主钱包', '5')
    
    @DecorateClass('PFREQ-T6610')
    def test_transform_bsp(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','BSP', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('BSP','主钱包', '5')

    @DecorateClass('PFREQ-T6611')
    def test_transform_kk(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','KK', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('KK','主钱包', '5')

    @DecorateClass('PFREQ-T8131')
    def test_transform_sp365(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().transform_money_compare_napp('主钱包','SP365', '35')
        self.function_dict['ap'].transformPage().transform_money_compare_napp('SP365','主钱包', '5')

    @DecorateClass('PFREQ-T6612')
    def test_all_transform_cp(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().transform_click_napp()
        self.function_dict['ap'].transformPage().money_return_cp_compare_napp(self.wallet)
    
    @DecorateClass('PFREQ-T6613')
    def test_deposit_company(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)
        
        self.function_dict['ap'].mainPage().deposit_click_napp()
        self.function_dict['ap'].depositcompanyPage().deposit_company_amount_napp(deposit_money, '機器人測試', '公司入款')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)
        
        self.function_dict['ap'].depositrecordPage().check_deposit_record_napp('公司入款', '公司入款', deposit_money)

    @DecorateClass('PFREQ-T6614')
    def test_desposit_aliPay_f2f(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().deposit_click_napp()
        self.function_dict['ap'].depositailpayf2Page().deposit_ailpay_f2f_amount_napp(deposit_money, 11111, '支付宝', '支付宝面对面扫码')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].depositrecordPage().check_deposit_record_napp('公司入款', '支付宝面对面扫码', deposit_money)

    @DecorateClass('PFREQ-T6615')
    def test_desposit_aliPay_transfer(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().deposit_click_napp()
        self.function_dict['ap'].depositailplaytransferPage().deposit_ailpay_transfer_amount_napp(deposit_money, '支付宝', '支付宝转帐')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].depositrecordPage().check_deposit_record_napp('公司入款', '支付宝转帐', deposit_money)

    @DecorateClass('PFREQ-T6616')
    def test_withdraw(self):
        self.test_login()

        withdraw_money = random.randint(int(30),int(300))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().withdraw_click_napp()
        self.function_dict['ap'].withdrawPage().bank_enter_click()
        withdraw_money = self.function_dict['ap'].withdrawPage().withdraw_napp(withdraw_money, 111111)

        # 驗證，出款申請是否有資料
        withdraw_id = self.functions.ui_admin_withdraw_management().get_withdraw_info(withdraw_money, self.app_account, admin_certification, self.admin_url)
        # 鎖定特定提款申請
        self.functions.ui_admin_withdraw_management().lock_specific_withdraw(withdraw_id, self.app_account, admin_certification, self.admin_url)
        # 同意出款
        self.functions.ui_admin_withdraw_management().agree_withdraw(withdraw_id, self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].withfrawrecordPage().check_withdraw_record_napp()

    @DecorateClass('PFREQ-T6617')
    def test_into_promotions(self):
        self.test_login()

        self.function_dict['ap'].mainPage().promotions_click_napp()
        self.function_dict['ap'].promoPage().promotions()

    @DecorateClass('PFREQ-T6618')
    def test_into_faq(self):
        self.test_login()

        i = 0
        service = []
        self.function_dict['ap'].mainPage().customer_service_click()
        service.append(self.function_dict['ap'].faqPage().wechat_exists_napp())
        service.append(self.function_dict['ap'].faqPage().qq_exists_napp())
        service.append(self.function_dict['ap'].faqPage().livechat_exists_napp())
        service.append(self.function_dict['ap'].faqPage().customer_service_exists_napp())

        for kf in service:
            if kf == False:
                i+=1
            elif kf != None:
                raise EOFError(f'{service}')
        
        if i == 4:
            raise EOFError('所有客服都沒有顯示')

    @DecorateClass('PFREQ-T6619')
    def test_into_mailcenter(self):
        self.test_login()

        self.function_dict['ap'].mainPage().mail_center_click_napp()
        self.function_dict['ap'].mailcenterPage().mail_center_exists()
        self.function_dict['ap'].mailcenterPage().mail_read_delete()

    @DecorateClass('PFREQ-T6620')
    def test_into_ledger(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().ledger_click_napp()

    @DecorateClass('PFREQ-T6621')
    def test_into_myinfo(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().myinfo_click_napp()

    @DecorateClass('PFREQ-T6622')
    def test_into_deposit_record(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().deposit_record_click_napp()

    @DecorateClass('PFREQ-T6623')
    def test_into_withdraw_record(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().withdraw_record_click_napp()

    @DecorateClass('PFREQ-T6625')
    def test_into_agent(self):
        if gl.get_value('BRAND') == 'ttmj' or 'co':
            self.skipTest('ttmj和co沒有代理合作')

        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().agent_cooperation_click_napp()

    @DecorateClass('PFREQ-T6626')
    def test_into_about(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().about_click_napp()

    @DecorateClass('PFREQ-T6627')
    def test_into_feedback(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click_napp()
        self.function_dict['ap'].memberPage().feedback_cooperation_click_napp()
        self.function_dict['ap'].feedbackPage().feedback()
    
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method