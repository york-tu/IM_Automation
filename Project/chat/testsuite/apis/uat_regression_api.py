# -*- coding: utf-8 -*-
import unittest
import sys
import os
import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.chat.apis.testcase.uiapi.uiapi_testcase import UiApiAppTestCases
from Project.chat.apis.testcase.uiapi.uiapi_tool_testcase import UiApiToolTestCases
from jira.config.base_key import BaseKey

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'uat'
brand = 'gu'
user = 2
push = False # 將結果推倒jira, 預設請給予 True

# TestCase Setting
api_app_testcase_list = [
    # UiApiAppTestCases("test_app_login"),
    # UiApiAppTestCases("test_web_login"),
    # UiApiAppTestCases("test_admin_login"),
    UiApiAppTestCases("test_send_message"),
]

api_tool_testcase_list = [
    # UiApiToolTestCases("test_send_message_to_one"),
    # UiApiToolTestCases("test_add_friend"),
    # UiApiToolTestCases("test_add_groups"),
    # UiApiToolTestCases("test_add_chatroom"),
    UiApiToolTestCases("test_get_redenvelope"),
]


if __name__ == '__main__':
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) == 8:
        env = sys.argv[1]
        brand = sys.argv[2]
        user = sys.argv[3]

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', 'app')
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    suite = unittest.TestSuite()
    suite.addTests(api_app_testcase_list)
    # suite.addTests(api_tool_testcase_list)
    
    
    # RuningTest
    Utils.unittest_xml(suite)