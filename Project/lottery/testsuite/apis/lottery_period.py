# -*- coding: UTF-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)
import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.lottery.apis.testcases.uiapi.uiapi_web_testcases import UiApiWebTestCases

# Test Setting
env = 'dev'
brand = 'lv'
user = 1
game= 'hk6'
ball = '1,1,1,1,1,1,1'
num = 1

api_testcase_list = [
    UiApiWebTestCases("test_dwh_set_period"),
]


# TestCase frame add
suite = unittest.TestSuite()

if __name__ == "__main__":
    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 5:
        env = sys.argv[1]
        game = sys.argv[2]
        ball = sys.argv[3]
        num = sys.argv[4]
    
    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    UiApiWebTestCases.test_data = game, ball, int(num)
    # TestCase add
    suite.addTests(api_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)
    