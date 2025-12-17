import os
import sys
import unittest
import logging
import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.chat.app.testcase.app_testcase import AppTestCase
from Project.chat.app.testcase.context_testcase import ContextTestCase
from jira.config.base_key import BaseKey

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'prod'
brand = 'gu'  # gu, mee, chit
user = 1
connect_type = 'local'  # 手機連線模式
phone_name = 'HUAWEI_MATE_30_PRO_5G'  # 手機型號
phone_platform = 'Android'  # 手機作業系統
app_version = '2.18.0'  # 版本號
account_type = 'phone'  # 帳號類型: mail, phone...
# specific_os_version = []  # 指定OS版本, ['10','11','8']
push = True  # 將結果推倒jira, 預設請給予 True

Prod_regression_list = [
    AppTestCase("test_login"),
    AppTestCase("test_version_check"),
    AppTestCase("test_change_nickname_and_instructions"),
    AppTestCase("test_change_password"),
    AppTestCase("test_add_friend"),
    AppTestCase("test_friend_remark"),
    AppTestCase("test_send_message"),
    AppTestCase("test_message_copy"),
    AppTestCase("test_message_reply"),
    AppTestCase("test_message_delete"),
    AppTestCase("test_message_revoke"),
    AppTestCase("test_message_pin"),
    AppTestCase("test_message_emoji"),
    AppTestCase('test_send_voice_message'),
    AppTestCase('test_voice_message_reply'),
    AppTestCase('test_voice_message_delete'),
    AppTestCase('test_voice_message_revoke'),
    AppTestCase('test_send_file_message'),
    AppTestCase('test_file_message_reply'),
    AppTestCase('test_file_message_delete'),
    AppTestCase('test_file_message_revoke'),
    AppTestCase("test_send_message_group"),
    AppTestCase("test_message_copy_group"),
    AppTestCase("test_message_reply_group"),
    AppTestCase("test_message_delete_group"),
    AppTestCase("test_message_revoke_group"),
    AppTestCase("test_message_pin_group"),
    AppTestCase("test_send_voice_message_group"),
    AppTestCase('test_voice_message_reply_group'),
    AppTestCase('test_voice_message_delete_group'),
    AppTestCase('test_voice_message_revoke_group'),
    AppTestCase('test_send_file_message_group'),
    AppTestCase('test_file_message_reply_group'),
    AppTestCase('test_file_message_delete_group'),
    AppTestCase('test_file_message_revoke_group'),
    AppTestCase("test_discover_floating_icon"),  # 確認功能懸浮按鈕與選單
    AppTestCase("test_delete_friend"),
    AppTestCase("test_logout"),
]

# ==================================================== Backup ==========================================================
# =========== 私聊相關功能測試 ===========
one_on_one_chat_regression_list = [
    AppTestCase("test_login"),
    AppTestCase("test_version_check"),
    AppTestCase("test_into_member"),
    AppTestCase("test_into_friend"),
    AppTestCase("test_change_nickname_and_instructions"),
    AppTestCase("test_notify_switch"),
    AppTestCase("test_detail_switch"),
    AppTestCase("test_voice_switch"),
    AppTestCase("test_vibration_switch"),
    AppTestCase("test_about_terms"),
    AppTestCase("test_free_up_space"),
    AppTestCase("test_change_password"),
    AppTestCase("test_account_info"),
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
    AppTestCase('test_send_voice_message'),
    AppTestCase('test_voice_message_reply'),
    AppTestCase('test_voice_message_delete'),
    AppTestCase('test_voice_message_revoke'),
    AppTestCase('test_send_file_message'),
    AppTestCase('test_file_message_reply'),
    AppTestCase('test_file_message_delete'),
    AppTestCase('test_file_message_revoke'),
    AppTestCase("test_delete_friend"),
    AppTestCase("test_logout"),
]
# =========== 群聊相關功能測試 ===========
group_chat_regression_list = [
    AppTestCase("test_send_message_group"),
    AppTestCase("test_message_copy_group"),
    AppTestCase("test_message_reply_group"),
    AppTestCase("test_message_delete_group"),
    AppTestCase("test_message_revoke_group"),
    AppTestCase("test_message_pin_group"),
    AppTestCase("test_message_pin_reply_group"),
    AppTestCase("test_message_pin_delete_group"),
    AppTestCase("test_message_pin_revoke_group"),
    AppTestCase("test_send_voice_message_group"),
    AppTestCase('test_voice_message_reply_group'),
    AppTestCase('test_voice_message_delete_group'),
    AppTestCase('test_voice_message_revoke_group'),
    AppTestCase('test_send_file_message_group'),
    AppTestCase('test_file_message_reply_group'),
    AppTestCase('test_file_message_delete_group'),
    AppTestCase('test_file_message_revoke_group'),
]
# =========== 發現功能測試 ==============
discover_regression_list = [
    AppTestCase("test_discover_floating_icon"),
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
    gl.set_value('PHONE_PLATFORM', phone_platform) # 作業系統名稱
    gl.set_value('APP_VERSION', app_version)
    gl.set_value('ACCOUNT_TYPE', account_type)
    # gl.set_value('SPECIFIC_OS_VERSION', specific_os_version)

    # for jira config
    gl.set_value('TEST_TYPE', 'app_android')
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    suite = unittest.TestSuite()
    suite.addTests(Prod_regression_list)  # total 38 cases

    # =================== Backup ===================
    # suite.addTests(one_on_one_chat_regression_list)
    # suite.addTests(group_chat_regression_list)
    # suite.addTests(discover_regression_list)

    # RunningTest
    Utils.unittest_xml(suite)