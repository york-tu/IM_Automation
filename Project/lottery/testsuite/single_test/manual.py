# -*- coding: UTF-8 -*-
import unittest
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.lottery.web.testcases.web_testcases import WebTestCases, MobileWebCases
from Project.lottery.web.testcases.admin_testcases import AdminTestCases
from Project.lottery.web.testcases.reseller_testcases import ResellerTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_web_testcases import UiApiWebTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
from Project.lottery.web.testcases.nwap_testcases.nwap_testcases import MobileWebCases as MobileWebCases_nwap
from Project.mynah.testsuite.testcases.web_testcases import WebTestCases as WebTestCases_mynah
from Project.lottery.web.testcases.admin_testcases_wap import AdminTestCasesWap

# Test Setting
brand = 'xpj'
user = 1
env = 'uat'
test_type = 'single_test'

# TestCase Setting
manual_list = [
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
        test_list = data[3]
        test_list = test_list.replace('(','("').replace(')','")')

        # env = sys.argv[1]
        # brand = sys.argv[2]
        # user = sys.argv[3]
        # test_list = sys.argv[4]
        # test_list = test_list.replace('(','("').replace(')','")')
        
        if ',' not in test_list:
            manual_list.append(eval(test_list))
        else:
            test_list = test_list.split(',')
            for test in test_list:
                manual_list.append(eval(test))

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('TEST_TYPE', test_type)
    
#     # TestCase add
    suite.addTests(manual_list)

    # RuningTest
    Utils.unittest_xml(suite)
