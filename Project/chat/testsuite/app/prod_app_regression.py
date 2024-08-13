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
brand = 'gu'  # gu, mee, s365, chit
user = 1
connect_type = 'local'  # 手機連線模式
phone_name = 'HUAWEI_26'  # 手機型號 'MI10_23' 'Pixel5_31'
phone_platform = 'Android'  # 手機作業系統
app_version = '1.42.2'
specific_os_version = []  # 指定OS版本, ['10','11','8']
push = True  # 將結果推倒jira, 預設請給予 True

app_regression_list = [
    AppTestCase("test_login"),
    AppTestCase("test_version_check"),
    AppTestCase("test_into_gallery"),
    AppTestCase("test_into_tread"),
    AppTestCase("test_into_member"),
    AppTestCase("test_into_friend"),
    AppTestCase("test_change_nickname"),
    AppTestCase("test_notify_switch"),
    AppTestCase("test_detail_switch"),
    AppTestCase("test_voice_switch"),
    AppTestCase("test_vibration_switch"),
    AppTestCase("test_about_terms"),
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
    AppTestCase("test_send_message_group"),
    AppTestCase("test_message_copy_group"),
    AppTestCase("test_message_reply_group"),
    AppTestCase("test_message_delete_group"),
    AppTestCase("test_message_revoke_group"),
    AppTestCase("test_message_pin_group"),
    AppTestCase("test_message_pin_reply_group"),
    AppTestCase("test_message_pin_delete_group"),
    AppTestCase("test_message_pin_revoke_group"),
    AppTestCase("test_delete_friend"),
    AppTestCase("test_logout"),
]

context_regression_list = [
    # ContextTestCase("test_web_login"),
    # ContextTestCase("test_app_login"),
    # ContextTestCase("test_message_check"),
    # ContextTestCase("test_group_setting"),
    # ContextTestCase("test_admin_rule"),
    # ContextTestCase("test_admin_member_delete"),
    # ContextTestCase("test_admin_member_block"), #未完成
    # ContextTestCase("test_admin_delete"),
    # ContextTestCase("test_owner_member_delete"), #未完成
    # ContextTestCase("test_owner_member_block"), #未完成

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
    gl.set_value('SPECIFIC_OS_VERSION', specific_os_version)

    # for jira config
    gl.set_value('TEST_TYPE', 'app')
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    suite = unittest.TestSuite()
    suite.addTests(app_regression_list)
    # suite.addTests(context_regression_list)
    
    # RunningTest
    Utils.unittest_xml(suite)