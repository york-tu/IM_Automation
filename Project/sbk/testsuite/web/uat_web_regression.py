import os
import sys
import unittest
import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from common.utils.utils import Utils
from Project.sbk.web.testcase.web_testcases import WebTestCase
from Project.sbk.web.testcase.admin_testcases import AdminTestCase
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'sbk'
user = 1
test_type = 'web'
push = False # 將結果推倒jira, 預設請給予 True

web_regression_list = [
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
    # WebTestCase("test_add_friend"),
    # WebTestCase("test_friend_remark"),
    # WebTestCase("test_block_friend"),
    # WebTestCase("test_block_setting"),
    # WebTestCase("test_unblock_friend"),
    # WebTestCase("test_share_url"),
    # WebTestCase("test_send_message"),
    # WebTestCase("test_message_copy"),
    # WebTestCase("test_message_reply"),
    # WebTestCase("test_message_revoke"),
    # WebTestCase("test_message_reply_revoke"),
    # WebTestCase("test_message_pin"),
    # WebTestCase("test_message_emoji"),
    # WebTestCase("test_message_pin_reply"),
    # WebTestCase("test_message_pin_revoke"),
    # WebTestCase("test_groups_biuld"),
    # WebTestCase("test_group_name_change"),
    # WebTestCase("test_group_rule_all"),
    # WebTestCase("test_send_message_group"),
    # WebTestCase("test_message_copy_group"),
    # WebTestCase("test_message_reply_group"),
    # WebTestCase("test_message_revoke_group"),
    # WebTestCase("test_message_pin_group"),
    # WebTestCase("test_message_pin_reply_group"),
    # WebTestCase("test_message_pin_revoke_group"),
    # WebTestCase("test_delete_friend"),
    # WebTestCase("test_web_logout"),
]

admin_regression_list = [
    # AdminTestCase("test_admin_login"),
    # AdminTestCase("test_admin_switch_languages"),
    # AdminTestCase("test_admin_change_time"),
    # AdminTestCase("test_admin_change_pass"),
    # AdminTestCase("test_partner_and_player_list"),
    # AdminTestCase("test_partner_and_player_keywords_search"),
    # AdminTestCase("test_partner_and_player_new"),
    # AdminTestCase("test_partner_and_player_partner_edit"),
    # AdminTestCase("test_partner_and_player_player"),
    # AdminTestCase("test_partner_and_player_player_search"),
    # AdminTestCase("test_partner_and_player_player_edit"),
    # AdminTestCase("test_transaction_log"),
    # AdminTestCase("test_wallet_adjust_transaction_number"),
    AdminTestCase("test_wallet_adjust_partner"),
    # AdminTestCase("test_wallet_adjust_player"),
    # AdminTestCase("test_wallet_adjust_newly_added_increase"),
    # AdminTestCase("test_wallet_adjust_newly_added_decrease"),
    # AdminTestCase("test_wallet_adjust_view_edit"),
    # AdminTestCase("test_wallet_adjust_view_void"),
    # AdminTestCase("test_wallet_adjust_submit_for_view"),
    # AdminTestCase("test_wallet_adjust_progress_applying"),
    # AdminTestCase("test_wallet_adjust_progress_submit_review"),
    # AdminTestCase("test_wallet_adjust_progress_void"),
    # AdminTestCase("test_wallet_adjust_progress_audit"),
    # AdminTestCase("test_wallet_adjust_progress_approved"), 
    # AdminTestCase("test_wallet_adjust_progress_reject"),

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
    
    gl.set_value('ENV', 'uat')
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)
    
    # TestCase add
    # suite.addTests(web_regression_list)
    suite.addTests(admin_regression_list)
    
    # RuningTest
    Utils.unittest_xml(suite)