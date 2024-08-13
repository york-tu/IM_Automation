# -*- coding: UTF-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)


from common.utils.utils import Utils
from Project.lottery.web.testcases.web_testcases import WebTestCases
from Project.lottery.web.testcases.nwap_testcases.nwap_testcases import MobileWebCases
from Project.lottery.web.testcases.reseller_testcases import ResellerTestCases
import common.utils.globalvar as gl
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
from jira.config.base_key import BaseKey

# Test Setting
brand = 'ttmj'
user = 1
test_type = 'web'
push = True # 將結果推倒jira,預設請給予 True

# TestCase Setting
web_testcase_list = [
    WebTestCases("test_register_logout"),
    WebTestCases("test_web_login"),
    WebTestCases("test_wallet_conversion_return_local"),
    WebTestCases("test_ag_wallet_conversion"),
    WebTestCases("test_mg_wallet_conversion"),
    WebTestCases("test_sb_wallet_conversion"),
    WebTestCases("test_bbin_wallet_conversion"),
    WebTestCases("test_dt_wallet_conversion"),
    # WebTestCases("test_gc_wallet_conversion"), # 目前"GC_視訊"都是維護狀態
    WebTestCases("test_ky_wallet_conversion"),
    WebTestCases("test_fg_wallet_conversion"),
    WebTestCases("test_gm_wallet_conversion"),
    WebTestCases("test_pt_wallet_conversion"),
    WebTestCases("test_lc_wallet_conversion"),
    WebTestCases("test_kk_wallet_conversion"),
    WebTestCases("test_sp365_wallet_conversion"),
    WebTestCases("test_dg_wallet_conversion"),
    WebTestCases("test_cq_wallet_conversion"),
    WebTestCases("test_vg_wallet_conversion"),
    WebTestCases("test_sw_wallet_conversion"),
    WebTestCases("test_3s_wallet_conversion"),
    WebTestCases("test_bs_wallet_conversion"),
    WebTestCases("test_hg_wallet_conversion"),
    WebTestCases("test_bg_wallet_conversion"),
    WebTestCases("test_betting_fu3d"),
    # WebTestCases("test_betting_pcegg"),
    WebTestCases("test_betting_hk"),
    WebTestCases("test_betting_js6"),
    WebTestCases("test_betting_jsssc"),
    WebTestCases("test_betting_jspk10"),
    WebTestCases("test_into_menu_index"),
    WebTestCases("test_into_menu_lottery"),
    WebTestCases("test_into_menu_game"),
    WebTestCases("test_into_menu_electronic"),
    WebTestCases("test_into_menu_casino"),
    WebTestCases("test_into_menu_sport"),
    WebTestCases("test_into_menu_fish"),
    WebTestCases("test_into_menu_promo"),
    WebTestCases("test_into_menu_service"),
    WebTestCases("test_into_menu_member_deposit"),
    WebTestCases("test_into_menu_member_withdraw"),
    WebTestCases("test_into_menu_member_wallet"),
    WebTestCases('test_change_member_password'),
    WebTestCases('test_change_member_security_password'),
    WebTestCases('test_change_member_contact'),
    # WebTestCases('test_change_bank_card'), # 前台已經無法修改
    WebTestCases('test_language_check'),
    WebTestCases("test_web_logout"),
    WebTestCases("test_about_us_help"),
    WebTestCases("test_contains_us_help"),
    WebTestCases("test_partners_help"),
    WebTestCases("test_deposit_help"),
    WebTestCases("test_withdraw_help"),
    WebTestCases("test_questions_help"),
]

nwap_testcase_list = [
    MobileWebCases("test_wap_login"),
    MobileWebCases("test_wallet_conversion_return_local_nwap"),
    MobileWebCases("test_ag_wallet_conversion_nwap"),
    MobileWebCases("test_mg_wallet_conversion_nwap"),
    MobileWebCases("test_sb_wallet_conversion_nwap"),
    MobileWebCases("test_bbin_wallet_conversion_nwap"),
    MobileWebCases("test_lgd_wallet_conversion_nwap"),
    # MobileWebCases("test_gc_wallet_conversion_nwap"), # 目前"GC_視訊"都是維護狀態
    MobileWebCases("test_ky_wallet_conversion_nwap"),
    MobileWebCases("test_pt_wallet_conversion_nwap"),
    MobileWebCases("test_lc_wallet_conversion_nwap"),
    MobileWebCases("test_gm_wallet_conversion_nwap"),
    MobileWebCases("test_fg_wallet_conversion_nwap"),
    MobileWebCases("test_cq_wallet_conversion_nwap"),
    MobileWebCases("test_vg_wallet_conversion_nwap"),
    MobileWebCases("test_sw_wallet_conversion_nwap"),
    MobileWebCases("test_3s_wallet_conversion_nwap"),
    MobileWebCases("test_dg_wallet_conversion_nwap"),
    MobileWebCases("test_bs_wallet_conversion_nwap"),
    MobileWebCases("test_hg_wallet_conversion_nwap"),
    MobileWebCases("test_kk_wallet_conversion_nwap"),
    MobileWebCases("test_sp365_wallet_conversion_nwap"),
    MobileWebCases("test_bg_wallet_conversion_nwap"),
    # ------------- new lottery ---------------
    MobileWebCases("test_betting_fu3d_nwap"),
    MobileWebCases("test_betting_jisuk3_nwap"),
    MobileWebCases("test_betting_jisu11to5_nwap"),
    MobileWebCases("test_betting_pcegg_nwap"),
    MobileWebCases("test_betting_hk_nwap"),
    MobileWebCases("test_betting_js6_nwap"),
    MobileWebCases("test_betting_jsssc_nwap"),
    MobileWebCases("test_betting_jspk10_nwap"),
    MobileWebCases('test_betting_sf6_bravery_tow'),
    # -----------------------------------------
    MobileWebCases("test_mine_sweeping_betting_nwap"),
    MobileWebCases("test_niu_niu_betting_nwap"),
    MobileWebCases("test_into_member_center"),
    MobileWebCases("test_into_wallet_conversion"),
    MobileWebCases("test_into_deposit"),
    MobileWebCases("test_into_withdraw"),
    MobileWebCases("test_into_news"),
    # MobileWebCases("test_into_together"), #現在WAP還沒有代理
    MobileWebCases("test_change_member_Info"),
    MobileWebCases("test_into_promo"),
    MobileWebCases("test_into_red_envelope"),
    # MobileWebCases("test_maintenance"), #維護
    MobileWebCases('test_language_check'),
    MobileWebCases("test_wap_logout"),    
]

# TestCase frame add
suite = unittest.TestSuite()

if __name__ == "__main__":
    gl._init()
    
    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        data = sys.argv[4].split(',,')
        env = data[0]
        brand = data[1]
        user = data[2]
        push = bool(data[3])
        
    gl.set_value('ENV', 'prod')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    if brand == "ttmj":
        suite.addTests(nwap_testcase_list)
    else :
        suite.addTests(web_testcase_list)
        suite.addTests(nwap_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)
