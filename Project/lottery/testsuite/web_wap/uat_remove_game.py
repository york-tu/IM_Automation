# -*- coding: utf-8 -*-
# 目前沒有在執行此檔案
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.lottery.web.testcases.web_tool_testcases import WebToolsTestCases, MobileToolsTestCases
import common.utils.globalvar as gl

# Test Setting
brand = 'lv'
user = 1


# TestCase Setting
web_testcase_list = [
    WebToolsTestCases("test_game_remove"),
]

mobile_testcase_list = [
    MobileToolsTestCases("test_game_remove"),
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
        gl.set_value('GAME', data[3])

    gl.set_value('ENV', 'uat')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # TestCase add
    suite.addTests(web_testcase_list)
    suite.addTests(mobile_testcase_list)   
    
    # RuningTest
    Utils.unittest_xml(suite)
    