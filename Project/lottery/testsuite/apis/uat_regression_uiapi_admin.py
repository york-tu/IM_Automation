# # -*- coding: UTF-8 -*-
# import unittest
# import sys
# import os
# DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
# sys.path.append(DIR_NAME)

# from common.utils.utils import Utils
# from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
# import common.utils.globalvar as gl
# from jira.config.base_key import BaseKey

# # Test Setting
# brand = 'c7'
# user = 1
# test_type = 'admin_api'
# push = False # 將結果推倒jira,預設請給予 True

# # TestCase Setting
# api_testcase_list = [
#     UiApiAdminTestCases("test_initialize_settings"),
#     UiApiAdminTestCases("test_close_deposit_otp"),
#     UiApiAdminTestCases("test_admin_login"),
#     UiApiAdminTestCases("test_delete_bank_account"),
#     UiApiAdminTestCases("test_add_desposit_bank"),
#     UiApiAdminTestCases("test_add_desposit_wechat_f2f"),
#     UiApiAdminTestCases("test_add_desposit_alipay_f2f"),
#     UiApiAdminTestCases("test_add_desposit_wechat_transfer"),
#     UiApiAdminTestCases("test_add_desposit_alipay_transfer"),
#     UiApiAdminTestCases("test_delete_online_merchant"),
#     UiApiAdminTestCases("test_add_onlinedesposit_onlinepay"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_bankscan"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_wechatscan"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_wechattransfer"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_alipayscan"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_alipaytransfer"),
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_scanpay"),
#     UiApiAdminTestCases("test_add_onlinedesposit_unionpay"),
#     UiApiAdminTestCases("test_add_onlinedesposit_jdpay"),
#     UiApiAdminTestCases("test_add_rebate_and_commision"),
#     UiApiAdminTestCases("test_handing_fee"),
#     UiApiAdminTestCases("test_period_management"),
#     UiApiAdminTestCases("test_handicap_management"),
#     UiApiAdminTestCases("test_betting_center_bet_rescind"),
#     UiApiAdminTestCases("test_betting_center_payout_check"),
#     UiApiAdminTestCases("test_betting_center_bet_validation"),
#     UiApiAdminTestCases("test_mine_sweeping_hall_management"),
#     UiApiAdminTestCases("test_niu_niu_hall_management"),
#     UiApiAdminTestCases("test_external_platform_wallet_transfer"),
#     UiApiAdminTestCases("test_external_platform_balance_inquire"),
#     UiApiAdminTestCases("test_company_deposit"),
#     UiApiAdminTestCases("test_online_deposit"),
#     UiApiAdminTestCases("test_deposit_overview"),
#     UiApiAdminTestCases("test_member_wallet"),
#     UiApiAdminTestCases("test_manual_deposit"),
#     UiApiAdminTestCases("test_initialize_floating"),
# ]

# # TestCase frame add
# suite = unittest.TestSuite()

# if __name__ == "__main__":
#     env = 'uat'
#     gl._init()
    
#     # 以CMD方式執行
#     if len(sys.argv) == 1:
#         pass
#     elif len(sys.argv) > 2:
#         data = sys.argv[4].split(',,')
#         env = data[0]
#         brand = data[1]
#         user = data[2]
#         push = bool(data[3])
        
#     gl.set_value('ENV', env)
#     gl.set_value('BRAND', brand)
#     gl.set_value('USER', int(user))

#     # for jira config
#     gl.set_value('TEST_TYPE', test_type)
#     BaseKey().get_jira_data()
#     gl.set_value('PUSH', push)

#     # TestCase add
#     suite.addTests(api_testcase_list)

#     # RuningTest
#     Utils.unittest_xml(suite)