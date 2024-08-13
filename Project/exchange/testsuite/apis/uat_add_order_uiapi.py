import os
import sys
import unittest
import logging

dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(dir_name)

import stf_api.stf as stf
import stf_api.stf_utils as stf_utils
import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.exchange.apis.testcases.uiapi_tool_testcases import UiApiToolsTestCases
from jira.config.base_key import BaseKey

# Test Setting
# 為直接打收銀台，故brand、user參數不重要
channel_brand = 'lv'
user = 2
test_type = 'web_api'
brand = 'zqb'
push = False # 將結果推倒jira,預設請給予 True

zqb_api_testcase_list = {
    UiApiToolsTestCases("test_casher_add_order"),
    UiApiToolsTestCases("test_casher_add_sell"),
}

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
        channel_brand = data[1]
        user = data[2]
        brand = data[3]
        push = bool(data[4])

    gl.set_value('ENV', env)
    gl.set_value('CHANNEL_BRAND', channel_brand)
    gl.set_value('USER', int(user))
    gl.set_value('BRAND', brand)

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    suite.addTests(zqb_api_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)