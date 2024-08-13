# -*- coding: utf-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.apis.testcases.uiapi.uiapi_tool_testcases import UiApiToolsTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
import common.utils.globalvar as gl

# Test Setting
brand = 'lv'
user = 1
test_type = 'coustomer'

# TestCase Setting
api_tools_testcase_list = [
    UiApiToolsTestCases("test_trigger"),
]

# TestCase frame add
suite = unittest.TestSuite()

if __name__ == "__main__":
    env = 'stage'
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        data = sys.argv[4].split(',,')
        env = data[0]
        brand = data[1]
        user = data[2]

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('TEST_TYPE', test_type)

    # TestCase add
    suite.addTests(api_tools_testcase_list)   
    

    # RuningTest
    Utils.unittest_xml(suite)
    