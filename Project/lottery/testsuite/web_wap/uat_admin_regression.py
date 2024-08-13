# -*- coding: UTF-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.web.testcases.admin_testcases import AdminTestCases
from Project.lottery.web.testcases.admin_testcases_wap import AdminTestCasesWap
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'lv'
user = 1
test_type = 'admin'
push = True # 將結果推倒jira,預設請給予 True

# TestCase Setting
admin_testcase_list = [
    UiApiAdminTestCases("test_initialize_settings"),
    UiApiAdminTestCases("test_close_deposit_otp"),
    UiApiAdminTestCases("test_lottery_bet_order"),
    AdminTestCases("test_initialize_last_floating"),
    AdminTestCases("test_language_check"),
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
    AdminTestCases('test_external_plateform_wallet_transfer'),
    AdminTestCases('test_external_plateform_balance_inquire'),
    AdminTestCases("test_company_deposit"),
    AdminTestCases("test_online_deposit"),
    AdminTestCases("test_deposit_overview"),
    AdminTestCases("test_member_wallet"),
    AdminTestCases("test_bank_account_page"),
    AdminTestCases("test_online_merchant_page"),
    AdminTestCases("test_handing_fee_page"),
    AdminTestCases("test_manwithdraw_page"),
    AdminTestCases("test_withdraw_page"),
    AdminTestCases("test_cgpay_withdraw_page"),
    AdminTestCases("test_company_deposit_otp"),
    AdminTestCases("test_desposit_alipay_f2f_otp"),
    AdminTestCases("test_desposit_wechat_transfer_otp"),
    AdminTestCases("test_withdrawgeneral_page"),
    AdminTestCases("test_different_report"),
    AdminTestCases("test_realtime_lottery_page"),
    AdminTestCases('test_game_list'),
    AdminTestCases('test_third_party_ledger'),
    AdminTestCases('test_external_plateform_ledger'),
    AdminTestCases('test_payout_statistics'),     
    AdminTestCases("test_period_management_page"),
    AdminTestCases("test_channel_setting_page"),
    AdminTestCases("test_handicap_management_page"),
    AdminTestCases('test_cp_ledger'), 
    AdminTestCases("test_artificial_deposit_page"),
    AdminTestCases("test_financial_report_page"),    # 上下分報表數據不夠即時，待觀察
    AdminTestCases("test_three_reports_page"),
    AdminTestCases("test_operational_risk_new"),
    AdminTestCases("test_check_export_btn"),
    # UiApiAdminTestCases("test_initialize_floating"),  # 未修復
    UiApiAdminTestCases("test_initialize_settings"),
    AdminTestCases("test_sign_up"),
    AdminTestCases("test_try_verification"),
    AdminTestCases("test_website_status"),
    AdminTestCases("test_phone_discountlobby"),
    # AdminTestCases("test_signup_detail"),             # 未修復
    AdminTestCases("test_quota_conversion"),
    AdminTestCases("test_member_system"),
    # UiApiAdminTestCases("test_initialize_floating"),  # 未修復
    AdminTestCases("test_customer_service_manage"),
    # AdminTestCases("test_sidefloat_transmit"),        # 未修復
    UiApiAdminTestCases("test_initialize_settings"),    # 最後進行設定初始化
    
    # ------------------------ 投注限額 ------------------------
    # 不要開除非你確認好可以正常執行
    # AdminTestCases('test_betting_limit_js6'),
    # AdminTestCases('test_betting_limit_k3'),
    # AdminTestCases('test_betting_limit_pk10'),
    # AdminTestCases('test_betting_limit_sscb'),
    # AdminTestCases('test_betting_limit_xy28'),
    # AdminTestCases('test_betting_limit_3f6'),
    # AdminTestCases('test_betting_limit_hk6'),
    # AdminTestCases('test_betting_limit_fc3d'),
    # AdminTestCases('test_betting_limit_pl3'),
    # AdminTestCases('test_betting_limit_ff6'),
    # AdminTestCases('test_betting_limit_jsssc'),
    # AdminTestCases('test_betting_limit_jspk10'),
    # AdminTestCases('test_betting_limit_lucky_airship'),
    # AdminTestCases('test_betting_limit_pc'),
    # AdminTestCases('test_betting_limit_tw'),
    # AdminTestCases('test_betting_limit_canada'),
    # AdminTestCases('test_betting_limit_js'),
    
    # ------------------------ 遊戲設置 ------------------------
    # 不要開除非你確認好可以正常執行
    # AdminTestCases('test_game_setting_js6'),
    # AdminTestCases('test_game_setting_hk6'),
    # AdminTestCases('test_game_setting_fc3d'),
    # AdminTestCases('test_game_setting_jsssc'),
    # AdminTestCases('test_game_setting_jspk10'),
    # AdminTestCases('test_game_setting_pc'),

    # ------------------------------------------------------ 未完成 請註解掉 
    # AdminTestCases("test_period_management_page"), # w 2
    # AdminTestCases("test_handicap_management_page"), # w 2
]

ttmj_admin_testcase_wap_list = [
    UiApiAdminTestCases("test_close_deposit_otp"),
    UiApiAdminTestCases("test_lottery_bet_order"),
    AdminTestCasesWap("test_language_check"),
    AdminTestCasesWap("test_admin_login"),
    AdminTestCasesWap("test_delete_bank_sort"),
    AdminTestCasesWap("test_delete_online_bank_sort"),
    AdminTestCasesWap("test_delete_crypto_wallet_sort"),
    AdminTestCasesWap("test_add_desposit_bank"),
    AdminTestCasesWap("test_add_desposit_wechat_f2f"),
    AdminTestCasesWap("test_add_desposit_alipay_f2f"),
    AdminTestCasesWap("test_add_desposit_wechat_transfer"),
    AdminTestCasesWap("test_add_desposit_alipay_transfer"),
    AdminTestCasesWap("test_add_desposit_upi"),
    AdminTestCasesWap("test_add_desposit_crypto_bnb_trc"),
    AdminTestCasesWap("test_add_desposit_crypto_bnb_erc"),
    AdminTestCasesWap("test_add_desposit_crypto_ht_trc"),
    AdminTestCasesWap("test_add_desposit_crypto_imtoken_trc"),
    AdminTestCasesWap("test_add_desposit_crypto_olex_erc"),
    AdminTestCasesWap("test_add_desposit_crypto_tokenpocket_erc"),
    AdminTestCasesWap("test_add_online_desposit_onlinepay"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_bankscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_banktransfer"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_wechatscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_wechattransfer"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_alipayscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_alipaytransfer"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_scanpay"),
    AdminTestCasesWap("test_add_online_desposit_unionpay"),
    AdminTestCasesWap("test_add_online_desposit_jdpay"),
    AdminTestCasesWap("test_add_wellpay_bankaccount"),
    AdminTestCasesWap("test_add_wellpay_alipayaccount"),
    AdminTestCasesWap("test_add_wellpay_wechataccount"),
    AdminTestCasesWap("test_add_wellpay_alipayscan"),
    AdminTestCasesWap("test_add_wellpay_wechatscan"),
    AdminTestCasesWap("test_add_rebate_and_commision"),
    AdminTestCasesWap('test_mine_sweeping_hall_management'),
    AdminTestCasesWap('test_niu_niu_hall_management'),
    AdminTestCasesWap('test_external_plateform_wallet_transfer'),
    AdminTestCasesWap("test_company_deposit"),
    AdminTestCasesWap("test_online_deposit"),
    AdminTestCasesWap("test_deposit_overview"),
    AdminTestCasesWap("test_member_wallet"),
    AdminTestCasesWap("test_bank_account_page"),
    AdminTestCasesWap("test_online_merchant_page"),
    AdminTestCasesWap("test_handing_fee_page"),
    AdminTestCasesWap("test_manwithdraw_page"),
    AdminTestCasesWap("test_withdraw_page"),
    AdminTestCasesWap("test_cgpay_withdraw_page"),
    AdminTestCasesWap("test_deposit_otp_nwap"),
    AdminTestCasesWap("test_deposit_alipay_f2f_otp_nwap"),
    AdminTestCasesWap("test_deposit_wechat_transfer_otp_nwap"),
    AdminTestCasesWap("test_withdrawgeneral_page"),
    AdminTestCasesWap("test_different_report"),
    AdminTestCasesWap("test_realtime_lottery_page"),
    AdminTestCasesWap('test_game_list'),
    AdminTestCasesWap('test_third_party_ledger'),
    AdminTestCasesWap('test_payout_statistics'),
    AdminTestCasesWap("test_period_management_page"),
    AdminTestCasesWap("test_channel_setting_page"),
    AdminTestCasesWap("test_handicap_management_page"),
    AdminTestCases('test_cp_ledger'), # 匯出已改為zip,導致匯出會有問題
    AdminTestCasesWap("test_artificial_deposit_page"),  
    AdminTestCasesWap("test_financial_report_page"),    # 上下分報表數據不夠即時，待觀察   (僅在後台操作)
    AdminTestCasesWap("test_three_reports_page"),  # (僅在後台操作)
    AdminTestCasesWap("test_operational_risk_new"),  # (僅在後台操作)
    AdminTestCasesWap("test_check_export_btn"),
    UiApiAdminTestCases("test_initialize_settings")
    
]

aa_admin_testcase_wap_list = [
    UiApiAdminTestCases("test_close_deposit_otp"),
    AdminTestCasesWap("test_language_check"),
    AdminTestCasesWap("test_admin_login"),
    AdminTestCasesWap("test_delete_bank_sort"),
    AdminTestCasesWap("test_delete_online_bank_sort"),
    AdminTestCasesWap("test_add_desposit_bank"),
    AdminTestCasesWap("test_add_desposit_wechat_f2f"),
    AdminTestCasesWap("test_add_desposit_alipay_f2f"),
    AdminTestCasesWap("test_add_desposit_wechat_transfer"),
    AdminTestCasesWap("test_add_desposit_alipay_transfer"),
    AdminTestCasesWap("test_add_online_desposit_onlinepay"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_bankscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_wechatscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_wechattransfer"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_alipayscan"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_alipaytransfer"),
    AdminTestCasesWap("test_add_online_desposit_kcurrency_scanpay"),
    AdminTestCasesWap("test_add_online_desposit_unionpay"),
    AdminTestCasesWap("test_add_online_desposit_jdpay"),
    AdminTestCasesWap("test_add_wellpay_bankaccount"),
    AdminTestCasesWap("test_add_wellpay_alipayaccount"),
    AdminTestCasesWap("test_add_wellpay_wechataccount"),
    AdminTestCasesWap("test_add_wellpay_alipayscan"),
    AdminTestCasesWap("test_add_wellpay_wechatscan"),
    AdminTestCasesWap("test_add_rebate_and_commision"),
    AdminTestCasesWap("test_bet_lottery"),    # 會進行股指下注
    AdminTestCasesWap("test_company_deposit"),
    AdminTestCasesWap("test_online_deposit"),
    AdminTestCasesWap("test_deposit_overview"),
    AdminTestCasesWap("test_bank_account_page"),
    AdminTestCasesWap("test_online_merchant_page"),
    AdminTestCasesWap("test_handing_fee_page"),
    AdminTestCasesWap("test_manwithdraw_page"),
    AdminTestCasesWap("test_withdraw_page"),
    AdminTestCasesWap("test_cgpay_withdraw_page"),
    AdminTestCasesWap("test_deposit_otp_nwap"),
    AdminTestCasesWap("test_deposit_alipay_f2f_otp_nwap"),
    AdminTestCasesWap("test_deposit_wechat_transfer_otp_nwap"),
    AdminTestCasesWap("test_withdrawgeneral_page"),
    AdminTestCasesWap("test_different_report"),
    # AdminTestCasesWap('test_third_party_ledger'),         # 財務管理 -> 流水系統 -> 上下分流水 -> 第三方現金流水 - 可修改為符合AA的
    # AdminTestCasesWap('test_payout_statistics'),          # 運維管理 -> 注單中心 -> 派彩統計 - 可修改為符合AA的
    # AdminTestCasesWap("test_handicap_management_page"),   # 運維管理 -> * -> 盤口管理 - 可修改為符合AA的 股指的盤口管理
    AdminTestCasesWap("test_artificial_deposit_page"),  
    AdminTestCasesWap("test_financial_report_page"),    # 上下分報表數據不夠即時，待觀察   (僅在後台操作)
    AdminTestCasesWap("test_three_reports_page"),  # (僅在後台操作)
    AdminTestCasesWap("test_operational_risk_new"),  # (僅在後台操作)
    AdminTestCasesWap("test_check_export_btn"),
    UiApiAdminTestCases("test_initialize_settings")
    
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
        
    gl.set_value('ENV', 'uat')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    if brand == "ttmj":
        suite.addTests(ttmj_admin_testcase_wap_list)
    elif brand == "aa" :
        suite.addTests(aa_admin_testcase_wap_list)
    else:
        suite.addTests(admin_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)
