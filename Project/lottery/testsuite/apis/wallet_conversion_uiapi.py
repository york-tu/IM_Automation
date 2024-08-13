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

# Test Setting
brand = 'lv'
user = 2


# TestCase Setting
api_web_testcase_list = [
    UiApiWebTestCases("test_x_to_x"),
]

api_admin_testcase_list = [
    UiApiAdminTestCases("test_manual_deposit"),
]

# TestCase frame add
suite = unittest.TestSuite()

if __name__ == "__main__":
    env = 'uat'
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) == 1:
        gl.set_value('A', 'cp')
        gl.set_value('B', 'ag')
        gl.set_value('NUM', 1)
    elif len(sys.argv) > 2:
        env = sys.argv[1]
        brand = sys.argv[2]
        user = sys.argv[3]
        gl.set_value('A', sys.argv[4])
        gl.set_value('B', sys.argv[5])
        gl.set_value('NUM', int(sys.argv[6]))
        
    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # TestCase add
    if env != 'prod':
        suite.addTests(api_admin_testcase_list)
    
    suite.addTests(api_web_testcase_list)   

    # RuningTest
    Utils.unittest_xml(suite)
    