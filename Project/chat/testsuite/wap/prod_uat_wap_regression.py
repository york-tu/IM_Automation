import os
import sys
import unittest

root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from common.utils.utils import Utils
from Project.chat.web.testcase.wap_testcases import WapTestCase
from Project.chat.web.testcase.admin_testcases import AdminTestCase
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
env = 'prod'  # uat, prod
brand = 'gu'
user = 1
test_type = 'wap'
wap_version = '2.4.0'
os_version = 'Win11'  # 作業系統

push = True  # 將結果推倒jira, 預設請給予 True

wap_regression_list = [

    WapTestCase("test_wap_login"),  # 測試-登入
    WapTestCase('test_version_check'),  # 測試-確認版號
    WapTestCase("test_into_member"),  # 測試-進入主頁我的設定頁
    WapTestCase("test_into_friend"),  # 測試-進入好友名單頁
    WapTestCase("test_about_terms"),  # 測試-進入關於股聊-服務條款/隱私權政策
    WapTestCase("test_change_password"),  # 測試-修改登入密碼
    WapTestCase('test_change_nickname_and_instructions'),  # 測試-編輯個人暱稱&說明

    WapTestCase("test_add_friend"),  # 測試-新增好友
    WapTestCase("test_friend_remark"),  # 測試-好友聊天詳情頁備註暱稱 & 描述
    WapTestCase("test_block_and_report_friend"),  # 測試-好友加入黑名單&檢舉
    WapTestCase("test_unblock_friend"),  # 測試-解除好友黑名單

    WapTestCase('test_1v1_send_message'),  # 測試-私聊-發送訊息
    WapTestCase('test_1v1_message_copy'),  # 測試-私聊-訊息複製並發送
    WapTestCase('test_1v1_message_reply'),  # 測試-私聊-訊息回覆
    WapTestCase("test_1v1_message_revoke"),  # 測試-私聊-訊息撤回
    WapTestCase("test_1v1_message_reply_revoke"),  # 測試-私聊-訊息回覆後撤回
    WapTestCase("test_1v1_message_add_emoji"),  # 測試-私聊-訊息添加表情符號
    WapTestCase("test_1v1_message_pin"),  # 測試-私聊-設置公告
    WapTestCase("test_1v1_message_pin_reply"),  # 測試-私聊-回覆訊息設為公告
    WapTestCase("test_1v1_message_pin_revoke"),  # 測試-私聊-訊息設為公告後撤回

    WapTestCase('test_1v1_send_voice_message'),  # 測試-私聊-發送語音訊息
    WapTestCase('test_1v1_voice_message_reply'),  # 測試-私聊-語音訊息回覆
    WapTestCase('test_1v1_voice_message_revoke'),  # 測試-私聊-語音訊息撤回

    WapTestCase('test_1v1_send_file_message'),  # 測試-私聊-發送檔案訊息
    WapTestCase('test_1v1_file_message_reply'),  # 測試-私聊-檔案訊息回覆
    WapTestCase('test_1v1_file_message_revoke'),  # 測試-私聊-檔案訊息撤回

    WapTestCase("test_group_send_message"),  # 測試-群組-發送訊息
    WapTestCase("test_group_message_copy"),  # 測試-群組-訊息複製並發送
    WapTestCase("test_group_message_reply"),  # 測試-群組-訊息回覆
    WapTestCase("test_group_message_revoke"),  # 測試-群組-訊息撤回
    WapTestCase("test_group_message_reply_revoke"),  # 測試-群組-訊息回覆後撤回
    WapTestCase("test_group_message_add_emoji"),  # 測試-群組-訊息添加表情符號
    WapTestCase("test_group_message_pin"),  # 測試-群組-設置公告
    WapTestCase("test_group_message_pin_reply"),  # 測試-群組-回覆訊息設為公告
    WapTestCase("test_group_message_pin_revoke"),  # 測試-群組-訊息設置公告後撤回

    WapTestCase("test_group_send_voice_message"),  # 測試-群組-發送語音訊息
    WapTestCase('test_group_voice_message_reply'),  # 測試-群組-語音訊息回覆
    WapTestCase('test_group_voice_message_revoke'),  # 測試-群組-語音訊息撤回

    WapTestCase('test_group_send_file_message'),  # 測試-群組-發送檔案訊息
    WapTestCase('test_group_file_message_reply'),  # 測試-群組-檔案訊息回覆
    WapTestCase('test_group_file_message_revoke'),  # 測試-群組-檔案訊息撤回

    WapTestCase("test_delete_friend"),  # 測試-刪除好友
    WapTestCase('test_wap_logout'),  # 測試-登出

]
# UAT only
social_regression_list = [
    WapTestCase("test_social_post_photo"),
    WapTestCase('test_social_post_video'),
    WapTestCase('test_social_search'),
    WapTestCase('test_social_follow_unfollow'),

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
        wap_version = data[4]
        push = bool(data[3])

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    # gl.set_value('WAP_VERSION', wap_version)
    gl.set_value('PHONE_PLATFORM', wap_version)  # 作業系統名稱

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    suite.addTests(wap_regression_list)

    # ===================== UAT Only ========================
    # suite.addTests(social_regression_list)

    # RunningTest
    Utils.unittest_xml(suite)
