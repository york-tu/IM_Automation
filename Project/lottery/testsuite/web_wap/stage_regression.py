# -*- coding: UTF-8 -*-
# 目前沒有在執行此檔案
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.web.testcases.web_testcases import WebTestCases, MobileWebCases
from Project.lottery.web.testcases.admin_testcases import AdminTestCases
from Project.lottery.web.testcases.reseller_testcases import ResellerTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_web_testcases import UiApiWebTestCases
import common.utils.globalvar as gl
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
from jira.config.base_key import BaseKey

# Test Setting
brand = 'lv'
user = 1
test_type = 'web'
push = True # 將結果推倒jira,預設請給予 True

# TestCase Setting
web_testcase_list = [
    WebTestCases("test_register_logout"),
    WebTestCases("test_login_announcement"),
    WebTestCases("test_web_login"),
    # WebTestCases('test_check_lottery_game'), #維護
    WebTestCases('test_station_news'),
    WebTestCases("test_company_deposit"),
    WebTestCases("test_desposit_alipay_f2f"),
    WebTestCases("test_desposit_alipay_transfer"),
    WebTestCases("test_desposit_wechat_f2f"),
    WebTestCases("test_desposit_wechat_transfer"),
    WebTestCases("test_desposit_onlinepay"),
    WebTestCases("test_desposit_unionpay"),
    WebTestCases("test_desposit_jdpay"),
    WebTestCases("test_manual_deposit"),
    WebTestCases("test_withdraw"),
    WebTestCases("test_wallet_conversion_return_local"),
    WebTestCases("test_ag_wallet_conversion"),
    WebTestCases("test_mg_wallet_conversion"),
    WebTestCases("test_sb_wallet_conversion"),
    WebTestCases("test_bbin_wallet_conversion"),
    WebTestCases("test_3s_wallet_conversion"),
    WebTestCases("test_dt_wallet_conversion"),
    # WebTestCases("test_gc_wallet_conversion"), # 目前"GC_視訊"都是維護狀態
    WebTestCases("test_ky_wallet_conversion"),
    WebTestCases("test_vg_wallet_conversion"),
    WebTestCases("test_sw_wallet_conversion"),
    WebTestCases("test_pt_wallet_conversion"),
    WebTestCases("test_lc_wallet_conversion"),
    WebTestCases("test_kk_wallet_conversion"),
    WebTestCases("test_hg_wallet_conversion"),
    WebTestCases("test_gm_wallet_conversion"),
    WebTestCases("test_fg_wallet_conversion"),
    WebTestCases("test_dg_wallet_conversion"),
    WebTestCases("test_cq_wallet_conversion"),
    WebTestCases("test_bs_wallet_conversion"),
    WebTestCases("test_bg_wallet_conversion"),
    WebTestCases("test_betting_fu3d"),
    WebTestCases("test_betting_jisuk3"),
    WebTestCases("test_betting_jisu11to5"),
    WebTestCases("test_betting_pcegg"),
    WebTestCases("test_betting_hk"),
    WebTestCases("test_betting_js6"),
    WebTestCases("test_betting_jsssc"),
    WebTestCases("test_betting_jspk10"),
    WebTestCases('test_betting_sf6'), 
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
    # WebTestCases("test_maintenance"), #維護
    WebTestCases('test_language_check'),
    WebTestCases("test_web_logout"),
    WebTestCases("test_about_us_help"),
    WebTestCases("test_contains_us_help"),
    WebTestCases("test_partners_help"),
    WebTestCases("test_deposit_help"),
    WebTestCases("test_withdraw_help"),
    WebTestCases("test_questions_help"),
]

mobile_testcase_list = [
    MobileWebCases("test_skip_app_download"),
    MobileWebCases("test_register_logout"),
    MobileWebCases("test_login_announcement"),
    MobileWebCases("test_wap_login"),
    MobileWebCases('test_station_news'),
    MobileWebCases("test_company_deposit"),
    MobileWebCases("test_desposit_alipay_f2f"),
    MobileWebCases("test_desposit_alipay_transfer"),
    MobileWebCases("test_desposit_wechat_f2f"),
    MobileWebCases("test_desposit_wechat_transfer"),
    MobileWebCases("test_desposit_onlinepay"),
    MobileWebCases("test_desposit_unionpay"),
    MobileWebCases("test_desposit_jdpay"),
    MobileWebCases("test_manual_deposit"),
    MobileWebCases("test_withdraw"),
    MobileWebCases("test_wallet_conversion_return_local"),
    MobileWebCases("test_ag_wallet_conversion"),
    MobileWebCases("test_mg_wallet_conversion"),
    MobileWebCases("test_sb_wallet_conversion"),
    MobileWebCases("test_bbin_wallet_conversion"),
    MobileWebCases("test_3s_wallet_conversion"),
    MobileWebCases("test_dt_wallet_conversion"),
    # MobileWebCases("test_gc_wallet_conversion"), # 目前"GC_視訊"都是維護狀態
    MobileWebCases("test_ky_wallet_conversion"),
    MobileWebCases("test_vg_wallet_conversion"),
    MobileWebCases("test_sw_wallet_conversion"),
    MobileWebCases("test_pt_wallet_conversion"),
    MobileWebCases("test_lc_wallet_conversion"),
    MobileWebCases("test_kk_wallet_conversion"),
    MobileWebCases("test_hg_wallet_conversion"),
    MobileWebCases("test_gm_wallet_conversion"),
    MobileWebCases("test_fg_wallet_conversion"),
    MobileWebCases("test_dg_wallet_conversion"),
    MobileWebCases("test_cq_wallet_conversion"),
    MobileWebCases("test_bs_wallet_conversion"),
    MobileWebCases("test_bg_wallet_conversion"),
    # MobileWebCases("test_check_lottery_game"), #維護
    # ------------- new lottery ---------------
    MobileWebCases("test_betting_fu3d_new"),
    MobileWebCases("test_betting_jisuk3_new"),
    MobileWebCases("test_betting_jisu11to5_new"),
    MobileWebCases("test_betting_pcegg_new"),
    MobileWebCases("test_betting_hk_new"),
    MobileWebCases("test_betting_js6_new"),
    MobileWebCases("test_betting_jsssc_new"),
    MobileWebCases("test_betting_jspk10_new"),
    MobileWebCases('test_betting_sf6_bravery_tow'),
    # ------------- old lottery ---------------
    MobileWebCases("test_betting_hk6_old"), 
    MobileWebCases("test_betting_js6_old"),
    MobileWebCases("test_betting_jsssc_old"),
    MobileWebCases("test_betting_jspk10_old"),
    MobileWebCases("test_betting_jisu11to5_old"),
    MobileWebCases("test_betting_jisuk3_old"),
    MobileWebCases("test_betting_fu3d_old"),
    # -----------------------------------------
    MobileWebCases('test_mine_sweeping_betting'),
    MobileWebCases('test_niu_niu_betting'),
    MobileWebCases("test_into_member_center"),
    MobileWebCases("test_into_wallet_conversion"),
    MobileWebCases("test_into_deposit"),
    MobileWebCases("test_into_withdraw"),
    MobileWebCases("test_into_news"),
    MobileWebCases("test_into_together"),
    MobileWebCases("test_change_member_Info"),
    MobileWebCases("test_into_promo"),
    MobileWebCases("test_into_red_envelope"),
    # MobileWebCases("test_maintenance"), #維護
    MobileWebCases('test_language_check'),
    MobileWebCases("test_wap_logout"),

    # 8.0
    # MobileWebCases("test_into_description"), # 拔掉了
    # MobileWebCases("test_into_trend"), # 開獎走勢已拔除於導航欄及會員中心
]

admin_testcase_list = [
    UiApiAdminTestCases("test_initialize_settings"),
    UiApiAdminTestCases("test_close_deposit_otp"),
    UiApiAdminTestCases('test_clear_user'),
    UiApiAdminTestCases("test_connection_link_api"),
    UiApiAdminTestCases("test_add_bank_api"),
    UiApiAdminTestCases("test_set_charge"),
    UiApiAdminTestCases("test_maintain_auto"), 
    UiApiAdminTestCases("test_artificial_wallet"),   
    AdminTestCases("test_web_login"),
    AdminTestCases("test_admin_login"),
    AdminTestCases("test_delete_bank_sort"),
    AdminTestCases("test_delete_online_bank_sort"),
    AdminTestCases("test_delete_crypto_wallet_sort"),
    AdminTestCases("test_add_desposit_bank"),
    AdminTestCases("test_add_desposit_wechat_f2f"),
    AdminTestCases("test_add_desposit_alipay_f2f"),
    AdminTestCases("test_add_desposit_wechat_transfer"),
    AdminTestCases("test_add_desposit_alipay_transfer"),
    AdminTestCases("test_add_desposit_upi"),
    AdminTestCases("test_add_desposit_crypto_bnb_trc"),
    AdminTestCases("test_add_desposit_crypto_bnb_erc"),
    AdminTestCases("test_add_desposit_crypto_ht_trc"),
    AdminTestCases("test_add_desposit_crypto_imtoken_trc"),
    AdminTestCases("test_add_desposit_crypto_olex_erc"),
    AdminTestCases("test_add_desposit_crypto_tokenpocket_erc"),
    AdminTestCases("test_add_online_desposit_onlinepay"),
    AdminTestCases("test_add_online_desposit_kcurrency_bankscan"),
    AdminTestCases("test_add_online_desposit_kcurrency_banktransfer"),
    AdminTestCases("test_add_online_desposit_kcurrency_wechatscan"),
    AdminTestCases("test_add_online_desposit_kcurrency_wechattransfer"),
    AdminTestCases("test_add_online_desposit_kcurrency_alipayscan"),
    AdminTestCases("test_add_online_desposit_kcurrency_alipaytransfer"),
    AdminTestCases("test_add_online_desposit_kcurrency_scanpay"),
    AdminTestCases("test_add_online_desposit_unionpay"),
    AdminTestCases("test_add_online_desposit_jdpay"),
    AdminTestCases("test_add_wellpay_bankaccount"),
    AdminTestCases("test_add_wellpay_alipayaccount"),
    AdminTestCases("test_add_wellpay_wechataccount"),
    AdminTestCases("test_add_wellpay_alipayscan"),
    AdminTestCases("test_add_wellpay_wechatscan"),
    AdminTestCases("test_add_rebate_and_commision"),
    AdminTestCases('test_mine_sweeping_hall_management'),
    AdminTestCases('test_niu_niu_hall_management'),
]

reseller_testcase_list = [
    ResellerTestCases("test_web_login"),
    ResellerTestCases("test_admin_login"),
    
    # 切入代理
    ResellerTestCases("test_structure_change"),
    ResellerTestCases("test_reseller_login"),
    ResellerTestCases("test_reseller_profile"), 
    ResellerTestCases("test_member_list"), 
    ResellerTestCases("test_agent_list"), 
    ResellerTestCases("test_reseller_old_agent_settlement"),
    ResellerTestCases("test_reseller_new_agent_settlement"),
    ResellerTestCases("test_ticket_name_period_account_search"),
    # 切出代理
    ResellerTestCases("test_structure_change"), 
    ResellerTestCases("test_member_list"), 
    ResellerTestCases("test_agent_list"), 
    ResellerTestCases("test_general_report"),
    ResellerTestCases("test_daily_report"),
    ResellerTestCases("test_check_valid_member"), 
    ResellerTestCases("test_ticket_name_period_account_search"), 
    # 切入代理
    ResellerTestCases("test_structure_change"), 
    ResellerTestCases("test_member_list"), 
    ResellerTestCases("test_agent_list"), 
    ResellerTestCases("test_ticket_name_period_account_search"),
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

    gl.set_value('ENV', 'stage')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    suite.addTests(admin_testcase_list)
    suite.addTests(web_testcase_list)
    if brand != 'co':
        suite.addTests(mobile_testcase_list)
    suite.addTests(reseller_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)
