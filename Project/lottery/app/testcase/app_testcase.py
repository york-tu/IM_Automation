import unittest, sys, os, datetime, random, re
import logging
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
        # 當自動化執行完畢後，斷掉手機連接
        if cls.connect_type == 'remote':
            stf.post_disconnect_phone(gl.get_value("PHONE_SERIAL"))
        
    @retry(stop_max_attempt_number=2, wait_fixed=1000)
    def test_choose_app(self):
        # 選APP
        try:
            self.function_dict['ap'].commonPage().find_app(self.package)
            login_status = self.function_dict['ap'].mainPage().into_home_check(self._login_status[0])
            if login_status == False:
                self._login_status[0] = False
        except Exception as e:
            if 'device offline' in str(e):
                self.device_reconnect()     # 手機斷線重連
            elif 'device' and 'not found' in str(e):
                self.device_reconnect()
            else:
                raise e
    
    def device_reconnect(self):
        gl.set_value('PHONE_NAME', 'None')
        self._login_status[0] = False
        self.unknow_env[0] = False
        self.tearDownClass()
        self.sleep(60)
        self.setUpClass()
        self.setUp()
        self.test_change_env()

    @DecorateClass('PFREQ-T6633')    
    def test_register(self):
        account = str(random.randrange(00000, 999999999))
        self.function_dict['ap'].mainPage().register()
        self.function_dict['ap'].registerPage().register(account,'ps111111')
        self.function_dict['ap'].mainPage().logout()

    def test_check_env(self, env):
        self.test_choose_app()
        current_env = self.function_dict['ap'].mainPage().check_env(env.upper())
        if current_env == env.upper():
            self.unknow_env[0] = False
        else:
            self.unknow_env[0] = True

    @DecorateClass('PFREQ-T6116')
    def test_change_env(self):
        env = self.env
        try:
            self.function_dict['ap'].mainPage().member_click()
            self.function_dict['ap'].memberPage().system_click()
            self.function_dict['ap'].systeminfoPage().change_env(env.upper())
            self.test_check_env(env)
        except:
            self.unknow_env[0] = True
            raise EOFError(f'切換環境失敗')

    @DecorateClass('PFREQ-T6122')
    def test_version_check(self):
        app_version = self.app_version
        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().system_click()
        self.function_dict['ap'].systeminfoPage().version(app_version)

    @DecorateClass('PFREQ-T6632')
    def test_login(self):
        level = 0
        if self.unknow_env[0] == True:
            self.function_dict['ap'].commonPage().skip_test('測試環境不正確')
        if self._login_status[0] == False:
            self.function_dict['ap'].mainPage().login(self.app_account, self.app_password)
            self._login_status[0] = True
        self.function_dict['ap'].mainPage().skip_change_password(level)
        self.function_dict['ap'].mainPage().skip_announcement()

    # ----彩票---------------------------------------------------
    @DecorateClass('PFREQ-T6567')
    def test_betting_wfk3(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_wfk3()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_wfk3()

        self.function_dict['ap'].k3Page().bet_k3_lottery('1','wfk3')

    @DecorateClass('PFREQ-T6568')
    def test_betting_hk(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_hk()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_hk()

        self.function_dict['ap'].hkPage().bet_hk_lottery('1','hk') 

    @DecorateClass('PFREQ-T6569')
    def test_betting_wf11x5(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_wf11x5()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_wf11x5()

        self.function_dict['ap'].x5Page().bet_x5_lottery('1','wf11x5')

    @DecorateClass('PFREQ-T6570')
    def test_betting_fu3d(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_fc3d()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_fc3d()

        self.function_dict['ap'].fc3dPage().bet_fc3d_lottery('1','fc3d')
        
    @DecorateClass('PFREQ-T6571')
    def test_betting_wfpk10(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_wfpk10()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_wfpk10()

        self.function_dict['ap'].pk10Page().bet_pk10_lottery('1','wfpk10')

    @DecorateClass('PFREQ-T6572')
    def test_betting_wfssc(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_wfssc()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_wfssc()

        self.function_dict['ap'].sscPage().bet_ssc_lottery('1','wfssc') 
    
    @DecorateClass('PFREQ-T6573')
    def test_betting_twxy28(self):
        self.test_login()

        if self.mobile_ui == 'old':
            self.function_dict['ap'].lotteryPageA().game_play_twxy28()
        else:
            self.function_dict['ap'].mainPage().lottery_home()
            self.function_dict['ap'].lotteryPageB().game_play_twxy28()

        self.function_dict['ap'].xy28Page().bet_xy28_lottery('1','twxy28')
    
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

        money = gl.get_value('LGD')

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

    #--------------------------------------------------------------
    @DecorateClass('PFREQ-T6593')
    def test_transform_ag(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','AG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('AG','主钱包', '5')
    
    @DecorateClass('PFREQ-T6592')
    def test_get_wallet_info(self):
        self.test_login()

        wallet = self.wallet

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().get_wallet_amount(wallet_list=wallet)

    @DecorateClass('PFREQ-T6594')
    def test_transform_mg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','MG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('MG','主钱包', '5')
        
    @DecorateClass('PFREQ-T6595')
    def test_transform_sb(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','SB', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('SB','主钱包', '5')
    
    @DecorateClass('PFREQ-T6596')
    def test_transform_bbin(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','BBIN', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('BBIN','主钱包', '5')
        
    @DecorateClass('PFREQ-T6597')
    def test_transform_3s(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','3S', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('3S','主钱包', '5')
        
    @DecorateClass('PFREQ-T6598')
    def test_transform_lgd(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','LGD', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('LGD','主钱包', '5')
    
    @DecorateClass('PFREQ-T6599')
    def test_transform_gc(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','GC', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('GC','主钱包', '5')
    
    @DecorateClass('PFREQ-T6600')
    def test_transform_ky(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','KY', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('KY','主钱包', '5')
    
    @DecorateClass('PFREQ-T6601')
    def test_transform_vg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','VG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('VG','主钱包', '5')
    
    @DecorateClass('PFREQ-T6602')
    def test_transform_sw(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','SW', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('SW','主钱包', '5')
    
    @DecorateClass('PFREQ-T6603')
    def test_transform_pt(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','PT', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('PT','主钱包', '5')
    
    @DecorateClass('PFREQ-T6604')
    def test_transform_kx(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','KX', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('KX','主钱包', '5')
    
    @DecorateClass('PFREQ-T6605')
    def test_transform_hg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','HG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('HG','主钱包', '5')

    @DecorateClass('PFREQ-T6606')
    def test_transform_gm(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','GM', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('GM','主钱包', '5')
    
    @DecorateClass('PFREQ-T6607')
    def test_transform_fg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','FG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('FG','主钱包', '5')
    
    @DecorateClass('PFREQ-T6608')
    def test_transform_dg(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','DG', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('DG','主钱包', '5')

    @DecorateClass('PFREQ-T6609')
    def test_transform_cq9(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','CQ9', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('CQ9','主钱包', '5')
    
    @DecorateClass('PFREQ-T6610')
    def test_transform_bsp(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','BSP', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('BSP','主钱包', '5')

    @DecorateClass('PFREQ-T6611')
    def test_transform_kk(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().transform_money_compare('主钱包','KK', '35')
        self.function_dict['ap'].transformPage().transform_money_compare('KK','主钱包', '5')
    
    @DecorateClass('PFREQ-T6612')
    def test_all_transform_cp(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().transform_click()
        self.function_dict['ap'].transformPage().money_return_cp_compare(self.wallet)
    
    @DecorateClass('PFREQ-T6613')
    def test_deposit_company(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)
        
        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().deposit_click()
        self.function_dict['ap'].depositcompanyPage().deposit_company_amount(deposit_money, '機器人測試', '公司入款')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)
        
        self.function_dict['ap'].depositrecordPage().check_deposit_record('公司入款', deposit_money)

    @DecorateClass('PFREQ-T6614')
    def test_desposit_aliPay_f2f(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().deposit_click()
        self.function_dict['ap'].depositailpayf2Page().deposit_ailpay_f2f_amount(deposit_money, 11111, '支付宝', '支付宝面对面扫码')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].depositrecordPage().check_deposit_record('公司入款', deposit_money)

    @DecorateClass('PFREQ-T6615')
    def test_desposit_aliPay_transfer(self):
        self.test_login()

        deposit_money = str(random.randint(int(30),int(300)))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().deposit_click()
        self.function_dict['ap'].depositailplaytransferPage().deposit_ailpay_transfer_amount(deposit_money, '支付宝', '支付宝转帐')
        self.functions.ui_admin_deposit_management().agree_deposit_apply(self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].depositrecordPage().check_deposit_record('公司入款', deposit_money)

    @DecorateClass('PFREQ-T6616')
    def test_withdraw(self):
        self.test_login()

        withdraw_money = random.randint(int(30),int(300))
        res, admin_certification = self.do_admin_login(self.admin_account, self.admin_password, self.admin_otp, self.admin_url)
        self.functions.ui_admin_system_list().deposit_withdraw_settings(admin_certification, self.admin_url)

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().withdraw_click()
        self.function_dict['ap'].withdrawPage().bank_enter_click()
        withdraw_money = self.function_dict['ap'].withdrawPage().withdraw(withdraw_money, 111111)

        # 驗證，出款申請是否有資料
        withdraw_id = self.functions.ui_admin_withdraw_management().get_withdraw_info(withdraw_money, self.app_account, admin_certification, self.admin_url)
        # 鎖定特定提款申請
        self.functions.ui_admin_withdraw_management().lock_specific_withdraw(withdraw_id, self.app_account, admin_certification, self.admin_url)
        # 同意出款
        self.functions.ui_admin_withdraw_management().agree_withdraw(withdraw_id, self.app_account, admin_certification, self.admin_url)

        self.function_dict['ap'].withfrawrecordPage().check_withdraw_record()

    @DecorateClass('PFREQ-T6617')
    def test_into_promotions(self):
        self.test_login()

        self.function_dict['ap'].mainPage().promotions_click()
        self.function_dict['ap'].promoPageA().promotions()

    @DecorateClass('PFREQ-T6618')
    def test_into_faq(self):
        self.test_login()

        i = 0
        service = []
        self.function_dict['ap'].mainPage().faq_click()
        service.append(self.function_dict['ap'].faqPage().wechat_exists())
        service.append(self.function_dict['ap'].faqPage().qq_exists())
        service.append(self.function_dict['ap'].faqPage().livechat_exists())
        service.append(self.function_dict['ap'].faqPage().customer_service_exists())

        for kf in service:
            if kf == 'None':
                i+=1
        
        if i == 4:
            raise EOFError(f'所有客服都沒有顯示 {service}')
    
    def test_bet_agfish(self):
        self.test_login()

        self.function_dict['ap'].mainPage().search_ag_fish()

    @DecorateClass('PFREQ-T6619')
    def test_into_mailcenter(self):
        self.test_login()

        self.function_dict['ap'].mainPage().mail_center_click()
        self.function_dict['ap'].mailcenterPage().center_exists()

    @DecorateClass('PFREQ-T6620')
    def test_into_ledger(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().ledger_click()

    @DecorateClass('PFREQ-T6621')
    def test_into_myinfo(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().myinfo_click()

    @DecorateClass('PFREQ-T6622')
    def test_into_deposit_record(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().deposit_record_click()

    @DecorateClass('PFREQ-T6623')
    def test_into_withdraw_record(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().withdraw_record_click()

    @DecorateClass('PFREQ-T6624')
    def test_into_bet_record(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().bet_record_click()

    @DecorateClass('PFREQ-T6625')
    def test_into_agent(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().agent_cooperation_click()

    @DecorateClass('PFREQ-T6626')
    def test_into_about(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().about_click()

    @DecorateClass('PFREQ-T6627')
    def test_into_feedback(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().feedback_cooperation_click()
        self.function_dict['ap'].feedbackPage().report()
    
    @DecorateClass('PFREQ-T6628')
    def test_into_share(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().share_click()
    
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

    @DecorateClass('PFREQ-T6631')
    def test_bet_record_filter(self):
        self.test_login()

        self.function_dict['ap'].mainPage().member_click()
        self.function_dict['ap'].memberPage().bet_record_click()
        self.function_dict['ap'].betrecordPage().filter_data()
    
    def run(self, result=None):
        gl.set_value('RESULT', result)
        gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
        BaseTestCase.run(self, result) # call superclass run method