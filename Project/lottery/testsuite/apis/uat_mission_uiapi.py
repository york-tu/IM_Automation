# -*- coding: utf-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.apis.testcases.uiapi.uiapi_mission_testcases import UiApiMissionTestCases
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'lv'
user = 1
test_type = 'web_api'
push = False # 將結果推倒jira,預設請給予 True

# mission_setting
deposit_money = 5  # 充值金額
amount = 5     # 投注金額
withdraw = 9    # 提款金額
mission_name = '立即派發活動-有效投注_充值倍數'   # 任務名稱
expected_amount = [10,20]    # 預期金額 [門檻1, 門檻2] 例:[10,20]


# TestCase Setting
api_web_testcase_list = [
    UiApiMissionTestCases("test_company_deposit_mission"),
    # UiApiMissionTestCases("test_withdraw_mission"),
    UiApiMissionTestCases("lottery_order_special_two_sides_mission"),
]

api_admin_testcase_list = [
    UiApiMissionTestCases("check_mission_result"),
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

    # for mission setting
    gl.set_value('DEPOSIT_MONEY', deposit_money)
    gl.set_value('AMOUNT', amount)
    gl.set_value('WITHDRAW', withdraw)
    gl.set_value('MISSION_NAME', mission_name)
    gl.set_value('EXPECTED_AMOUNT', expected_amount)
    
    # TestCase add
    suite.addTests(api_web_testcase_list)
    suite.addTests(api_admin_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)
    