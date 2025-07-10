import os
import sys
import unittest
import logging

root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.chat.app.testcase.app_testcase import AppTestCase
from Project.chat.app.testcase.context_testcase import ContextTestCase
from jira.config.base_key import BaseKey

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'uat'
brand = 'gu'  # gu > mee > s365 > chit
user = 1
connect_type = 'local'  # 手機連線模式 remote or local
phone_name = 'IPHONE_32'  # 手機型號 'HUAWEI_26', 'IPHONE_32'
phone_platform = 'iOS'  # 手機作業系統 (Android, iOS)
app_version = '5.5.0(107073.116)'  # android: 1.42.0-rc.4 , ios: 4.25.0(99946.116)
specific_os_version = []  # 指定OS版本, ['10','11','8']
push = True  # 將結果推倒jira, 預設請給予 True

personal_settings_regression_list = [
    AppTestCase("test_login"),
    AppTestCase("test_version_check"),
    AppTestCase("test_into_gallery"),
    AppTestCase("test_into_tread"),
    AppTestCase("test_into_member"),
    AppTestCase("test_into_friend"),
    AppTestCase("test_change_nickname_and_instructions"),
    AppTestCase("test_notify_switch"),
    AppTestCase("test_detail_switch"),
    AppTestCase("test_voice_switch"),
    AppTestCase("test_vibration_switch"),
    AppTestCase("test_about_terms"),
    AppTestCase("test_change_password"),
    AppTestCase("test_account_info"),
]

friend_regression_list = [
    AppTestCase("test_add_friend"),
    AppTestCase("test_add_myself"),
    AppTestCase("test_friend_remark"),
    AppTestCase("test_block_friend"),
    AppTestCase("test_block_setting"),
    AppTestCase("test_unblock_friend"),
    AppTestCase("test_share_message"),
    AppTestCase("test_send_message"),
    AppTestCase("test_message_copy"),
    AppTestCase("test_message_reply"),
    AppTestCase("test_message_delete"),
    AppTestCase("test_message_revoke"),
    AppTestCase("test_message_reply_delete"),
    AppTestCase("test_message_reply_revoke"),
    AppTestCase("test_message_pin"),
    AppTestCase("test_message_pin_reply"),
    AppTestCase("test_message_pin_delete"),
    AppTestCase("test_message_pin_revoke"),
    AppTestCase("test_message_emoji"),
    AppTestCase("test_delete_friend"),
    AppTestCase("test_logout"),
]

group_regression_list = [
    AppTestCase("test_send_message_group"),
    # AppTestCase("test_message_copy_group"),
    # AppTestCase("test_message_reply_group"),
    # AppTestCase("test_message_delete_group"),
    # AppTestCase("test_message_revoke_group"),
    # AppTestCase("test_message_pin_group"),
    # AppTestCase("test_message_pin_reply_group"),
    # AppTestCase("test_message_pin_delete_group"),
    # AppTestCase("test_message_pin_revoke_group"),
]


if __name__ == '__main__':
    gl._init()
    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        data = sys.argv[4].split(',,')
        env = sys.argv[1]
        brand = sys.argv[2]
        user = sys.argv[3]
        app_version = data[4]
        connect_type = data[5]
        phone_name = data[6]
        specific_os_version = data[7]
        push = bool(data[3])

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('CONNECT_TYPE', connect_type)
    gl.set_value('PHONE_NAME', phone_name)
    gl.set_value('PHONE_PLATFORM', phone_platform)  # 作業系統名稱
    gl.set_value('APP_VERSION', app_version)
    gl.set_value('SPECIFIC_OS_VERSION', specific_os_version)

    # for jira config
    gl.set_value('TEST_TYPE', 'app_ios')  # android: app_android , ios: app_ios
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    suite = unittest.TestSuite()
    # suite.addTests(personal_settings_regression_list)
    suite.addTests(group_regression_list)
    # suite.addTests(friend_regression_list)

    # RunningTest
    Utils.unittest_xml(suite)
