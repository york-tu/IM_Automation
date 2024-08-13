# -*- coding: utf-8 -*-
import unittest
import sys
import os
import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.sbk.apis.testcase.uiapi.uiapi_testcase import UiApiAppTestCases
# from Project.sbk.apis.function_layer.uiapi.web.home.init_profile import initProfile
# from Project.sbk.apis.testcase.uiapi.uiapi_tool_testcase import UiApiToolTestCases
from jira.config.base_key import BaseKey

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'qat'
brand = 'sbk'
user = 2
push = False # 將結果推倒jira, 預設請給予 True

# TestCase Setting
api_app_testcase_list = [
    # UiApiAppTestCases("test_wap_login"),
    # UiApiAppTestCases("test_get_profile"),
    # UiApiAppTestCases("test_get_maintenance_status"),
    # UiApiAppTestCases("test_get_followed_matches"),
    # UiApiAppTestCases("test_get_max_parlay_count"),
    # UiApiAppTestCases("test_get_unread_count"),
    # UiApiAppTestCases("test_get_match_count_info"),
    # UiApiAppTestCases("test_get_banners"),
    # UiApiAppTestCases("test_get_marquee"),
    # UiApiAppTestCases("test_get_announcements"),
    # UiApiAppTestCases("test_get_messages"),
    # UiApiAppTestCases("test_post_read_all"),
    # UiApiAppTestCases("test_get_followed_matches"),
    # UiApiAppTestCases("test_get_max_parlay_count"),
    # UiApiAppTestCases("test_get_hot_matches"),
    # UiApiAppTestCases("test_get_betslip"),
    # UiApiAppTestCases("test_get_live_score_inplay"),
    # UiApiAppTestCases("test_get_translation_short_competition"),
    # UiApiAppTestCases("test_get_translation_team"),
    # UiApiAppTestCases("test_get_translation_stage"),
    # UiApiAppTestCases("test_get_live_score_hot"),
    UiApiAppTestCases("test_get_recommend"),
    UiApiAppTestCases("test_get_upcoming_sport"),
    UiApiAppTestCases("test_get_upcoming_leagues"),
    UiApiAppTestCases("test_get_inplay_sports"),
    UiApiAppTestCases("test_get_inplay_leagues"),
    UiApiAppTestCases("test_get_preMatch_sports"),
    UiApiAppTestCases("test_get_preMatch_leagues"),


]

api_tool_testcase_list = [
    # UiApiToolTestCases("test_send_message_to_one"),
    # UiApiToolTestCases("test_add_friend"),
    # UiApiToolTestCases("test_add_groups"),
    # UiApiToolTestCases("test_add_chatroom"),
    # UiApiToolTestCases("test_get_redenvelope"),
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