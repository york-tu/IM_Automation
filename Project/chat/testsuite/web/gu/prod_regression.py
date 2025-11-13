import os
import sys
import unittest
import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from common.utils.utils import Utils
from Project.chat.web.testcase.web_testcases import WebTestCase
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'gu'  # gu > mee > s365 > chit
user = 1
test_type = 'web'
os_version = 'Win11'  # 作業系統
platform = 'PC'  # 測試環境
web_version = '1.25.0'  # 版本號 (開web console: VITE_APP_VERSION: 正式版號; VITE_LAST_HASH: uat測試版號)

push = True  # 將結果推倒jira, 預設請給予 True

web_regression_list = [
    # WebTestCase("test_send_media"),
    # WebTestCase("test_web_login"),
    # WebTestCase("test_into_notification"),
    # WebTestCase("test_into_security"),
    # WebTestCase("test_into_black"),
    # WebTestCase("test_into_share"),
    # WebTestCase("test_into_about"),
    # WebTestCase("test_account_info"),
    # WebTestCase("test_change_password"),
    # WebTestCase("test_change_nickname"),
    # WebTestCase("test_notify_switch"),
    # WebTestCase("test_about_terms"),
    WebTestCase("test_add_friend"),
    # WebTestCase("test_friend_remark"),
    WebTestCase("test_block_friend"),
    # WebTestCase("test_block_setting"),
    WebTestCase("test_unblock_friend"),

    # WebTestCase("test_share_url"),
    # WebTestCase("test_send_message"),
    # WebTestCase("test_message_copy"),
    # WebTestCase("test_message_reply"),
    # WebTestCase("test_message_revoke"),
    # WebTestCase("test_message_reply_revoke"),
    # WebTestCase("test_message_emoji"),
    # WebTestCase("test_message_pin"),
    # WebTestCase("test_message_pin_reply"),
    # WebTestCase("test_message_pin_revoke"),
    #
    # WebTestCase("test_send_file_message"),
    # WebTestCase("test_file_message_reply"),
    # WebTestCase("test_file_message_revoke"),
    # WebTestCase("test_send_message_group"),
    # WebTestCase("test_message_copy_group"),
    # WebTestCase("test_message_reply_group"),
    # WebTestCase("test_message_revoke_group"),
    # WebTestCase("test_message_pin_group"),
    # WebTestCase("test_message_pin_reply_group"),
    # WebTestCase("test_message_pin_revoke_group"),
    # WebTestCase("test_send_file_message_group"),
    # WebTestCase("test_file_message_reply_group"),
    # WebTestCase("test_file_message_revoke_group"),
    WebTestCase("test_delete_friend"),
    # WebTestCase("test_web_logout"),
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
        push = bool(data[3])
    
    gl.set_value('ENV', 'prod')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('PHONE_PLATFORM', os_version)  # 作業系統名稱
    gl.set_value('APP_VERSION', web_version) # 版本
    gl.set_value('PHONE_NAME', platform)

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    suite.addTests(web_regression_list)
    
    # RunningTest
    Utils.unittest_xml(suite)
