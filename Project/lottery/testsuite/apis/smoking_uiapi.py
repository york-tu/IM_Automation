# -*- coding: utf-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.apis.testcases.uiapi.uiapi_web_testcases import UiApiWebTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'lv'
user = 2
test_type = 'smoking'
push = True # 將結果推倒jira,預設請給予 True

# TestCase Setting
api_web_testcase_list = [
    UiApiAdminTestCases("test_initialize_settings"),
    UiApiAdminTestCases("test_close_deposit_otp"),
    UiApiWebTestCases("test_web_login"),
    UiApiWebTestCases("test_wap_login"),
    UiApiWebTestCases("test_reseller_login"),
    UiApiWebTestCases("test_cmweb_login"),
    UiApiWebTestCases("test_dwh_login"),
    UiApiWebTestCases("test_mynah_admin_login"),
    UiApiWebTestCases("test_mynah_web"),
    UiApiWebTestCases("test_register"),
    UiApiAdminTestCases("test_add_bank_api"),
    UiApiAdminTestCases("test_add_desposit_bank"),
    UiApiWebTestCases("test_company_deposit"),
    UiApiWebTestCases("test_return_cp"),
    UiApiWebTestCases("test_cp_to_ag"),
    UiApiWebTestCases("lottery_order_special_number"),
]

api_aa_testcase_list = [
    UiApiAdminTestCases("test_initialize_settings"),
    UiApiAdminTestCases("test_close_deposit_otp"),
    UiApiWebTestCases("test_wap_login"),
    UiApiWebTestCases("test_cmweb_login"),
    UiApiWebTestCases("test_dwh_login"),
    UiApiWebTestCases("test_mynah_admin_login"),
    UiApiWebTestCases("test_mynah_web"),
    UiApiWebTestCases("test_register"),
    UiApiAdminTestCases("test_add_bank_api"),
    UiApiAdminTestCases("test_add_desposit_bank"),
    UiApiWebTestCases("test_company_deposit"),
    UiApiWebTestCases("stock_order_positioning_champion"),
    UiApiWebTestCases("stock_chat_room_follow"),
]

# TestCase frame add
suite = unittest.TestSuite()

if __name__ == "__main__":
    env = 'uat'
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
        
    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
  
    # TestCase add
    if brand == 'aa':
        suite.addTests(api_aa_testcase_list)
    else:
        suite.addTests(api_web_testcase_list)  
        
    # RuningTest
    Utils.unittest_xml(suite)
    