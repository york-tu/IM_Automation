import unittest
import sys
import os
import datetime, random

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)

from common.utils.utils import Utils
from Project.mynah.testsuite.testcases.web_testcases import WebTestCases
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey


# Test Setting
test_brand = 'bh'  # 前台平台
user = 4  # 第n組帳號帳號
test_type = 'web'
os_version = 'Win11'  # 作業系統
push = True  # 將結果推倒jira, 預設請給予 True

# TestCase Setting
web_testcase_list = [
    # WebTestCases("test_close_ai_response"),
    # WebTestCases("test_talk_to_each_other"),
    # WebTestCases("test_hang_up_phone"),
    # WebTestCases("test_client_speak_before_not_connected"),
    # WebTestCases('test_inquiry_form'),
    # WebTestCases("test_talk_different_site"),
    # WebTestCases("test_talk_different_cs"),
    # WebTestCases("test_talk_more_guest"),
    # WebTestCases("test_invite_cs"),
    # WebTestCases("test_disconnect_auto_end"),
    # WebTestCases("test_visitor_auto_end"),
    # WebTestCases("test_send_img"),
    # WebTestCases("test_channel_account"),
    WebTestCases("test_search_group_message"),
    # WebTestCases("test_history_check"),
    # WebTestCases("test_promotion_ad"),
    # WebTestCases("test_score_statistics"),
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
        brand = sys.argv[2]
        user = sys.argv[3]
        platform = sys.argv[4]
        push = bool(data[3])

        # env = sys.argv[1]
        # brand = sys.argv[2]
        # user = sys.argv[3]

    gl.set_value('ENV', 'uat')
    gl.set_value('BRAND', 'mynah')
    gl.set_value('PLATFORM', test_brand)
    gl.set_value('USER', int(user))
    gl.set_value('TEST_TYPE', test_type)  # 測試環境
    gl.set_value('PHONE_PLATFORM', test_brand)  # 前台品牌

    # for jira config
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    suite.addTests(web_testcase_list)

    # RuningTest
    Utils.unittest_xml(suite)   

    