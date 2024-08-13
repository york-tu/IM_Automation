# -*- coding: utf-8 -*-
import hashlib, sys, os, requests, time, random, re
from tokenize import group
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from Project.sbk.apis.testcase.apis_base_testcase import BaseTestCase
from Project.sbk.apis.function_layer.uiapi.web.home.init_profile import initProfile
from Project.sbk.apis.function_layer.functions import Functions
from Project.sbk.apis.function_layer.base_functions import BaseFunction as BaseFunction_API
import common.utils.globalvar as gl
from common.web.decorator import DecorateClass



class UiApiAppTestCases(BaseTestCase, initProfile):

    brand = gl.get_value('BRAND')
    # ================================= TestSetting ================================
    @classmethod
    def setUpClass(cls):
        # cls.setting_test_data(cls)  # 設定測試數據
        # cls.functions = Functions(cls.skipTest)
        cls.env = gl.get_value('ENV')
    
    def tearDown(self):
        self.check_result(str(self.id()).split('.')[-1])
    
    @classmethod
    def tearDownClass(cls):
        pass

    # ================================= Web_TestCases ==============================
    # 登入

    @DecorateClass('')
    def test_wap_login(self):
        return  self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_profile(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_profile('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_maintenance_status(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_maintenance_status('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_followed_matches(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_followed_matches('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_max_parlay_count(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_max_parlay_count('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_unread_count(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_unread_count('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_match_count_info(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_match_count_info('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_banners(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_banners('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_marquee(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_marquee('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_announcements(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_announcements('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_messages(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_unread_count('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_post_read_all(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.post_read_all('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_followed_matches(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_followed_matches('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_max_parlay_count(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_max_parlay_count('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')
    
    @DecorateClass('')
    def test_get_hot_matches(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_hot_matches('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_betslip(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_betslip('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_live_score_inplay(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_live_score_inplay('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')

    @DecorateClass('')
    def test_get_translation_short_competition(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_translation_short_competition('williamAuto',user_token,'https://minio-uat.paradise-soft.com.tw')   

    @DecorateClass('')
    def test_get_translation_team(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_translation_team('williamAuto',user_token,'https://minio-uat.paradise-soft.com.tw')   

    @DecorateClass('')
    def test_get_translation_stage(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_translation_stage('williamAuto',user_token,'https://minio-uat.paradise-soft.com.tw')  

    @DecorateClass('')
    def test_get_live_score_hot(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_live_score_hot('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')    
    
    @DecorateClass('')
    def test_get_recommend(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_recommend('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')    
    
    @DecorateClass('')
    def test_get_upcoming_sport(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_upcoming_sport('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com') 

    @DecorateClass('')
    def test_get_upcoming_leagues(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_upcoming_leagues('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')    

    @DecorateClass('')
    def test_get_inplay_sports(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_inplay_sports('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')    

    @DecorateClass('')
    def test_get_inplay_leagues(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_inplay_leagues('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')  
    
    @DecorateClass('')
    def test_get_preMatch_sports(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_preMatch_sports('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')  
    
    @DecorateClass('')
    def test_get_preMatch_leagues(self):
        user_token = self.do_wap_login('williamAuto','auto001','https://sbk-gateway-player-qat.idc.pstdsf.com')[0]
        return self.get_preMatch_leagues('williamAuto',user_token,'https://sbk-web-qat.idc.pstdsf.com')  
    # @DecorateClass('')
    # def test_wap_profile(self):
    #     fullnumber = self.get_full_phone_number(self.nation, self.app_phone)
    #     return self.do_app_login(self.nation, fullnumber, self.password, self.device_id, self.app_url)

    # @DecorateClass('')
    # def test_web_login(self):
    #     fullnumber = self.get_full_phone_number(self.nation, self.web_phone)
    #     return self.do_web_login(self.nation, fullnumber, self.password, self.device_id, self.web_url)

    # @DecorateClass('')
    # def test_admin_login(self):
    #     return self.do_admin_login(self.admin_account, self.admin_password, self.admin_url)

    # @DecorateClass('')
    # def test_send_message(self):
    #     res, token = self.test_app_login()
    #     headers = self.headers(token)
    #     groups_name = 'QA_chat_bot'
    #     messages = 500
    #     space = 0.1
        
    #     groups_id = self.functions.ui_caht_function().get_groups_id(groups_name, headers, self.app_url)
    #     self.functions.ui_caht_function().do_send_messages(groups_id, messages, space, headers, self.app_url, sync=True)

    # def test_send_red_envelopet(self):
    #     res, token = self.test_admin_login()
    #     headers = self.header(token)
        

    # def run(self, result=None):
    #     gl.set_value('RESULT', result)
    #     gl.set_value('RESULT_COUNT', re.findall("[0-9]+", str(result)))
    #     BaseTestCase.run(self, result) # call superclass run method
