import os
import sys
import unittest
import logging
import common.utils.globalvar as gl

from common.utils.utils import Utils
from Project.chat.app.testcase.app_testcase import AppTestCase
from Project.chat.app.testcase.context_testcase import ContextTestCase
from jira.config.base_key import BaseKey

root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'uat'
brand = 'chit'
user = 1
connect_type = 'local'  # 手機連線模式 remote or local
phone_name = 'IPHONE_15_PRO'  # 手機型號 'IPHONE_15_PRO (ios18.6.2)', 'IPHONE_73 (ios16.1.1)', 'IPHONE_11_PRO (ios15)'
phone_platform = 'iOS'  # 手機作業系統
app_version = '5.21.0(114263.116)'  # 版本號
account_type = 'phone'  # 帳號類型: email, phone...
push = True  # 將結果推倒jira, 預設請給予 True

# ============================================== S1 Test Cases ===================================================
# -------------- 私聊相關功能測試 --------------
s1_personal_chat_regression_list = [
    AppTestCase("test_login"),
    AppTestCase("test_version_check"),
    AppTestCase("test_change_nickname_and_instructions"),
    AppTestCase("test_free_up_space"),
    AppTestCase("test_change_password"),
    AppTestCase("test_account_info"),
    AppTestCase("test_add_friend"),
    AppTestCase("test_friend_remark"),
    AppTestCase("test_send_message"),
    AppTestCase('test_send_voice_message'),
    AppTestCase('test_send_file_message'),
    AppTestCase("test_delete_friend"),
    AppTestCase("test_logout"),
]
# -------------- 群聊相關功能測試 --------------
s1_group_chat_regression_list = [
    ContextTestCase("test_group_remove_admin"),  # 移除 gubot03 管理員權限
    ContextTestCase("test_group_change_group_rules"),  # 群組成員權限設定
    ContextTestCase("test_group_add_admin_and_change_admin_rules"),  # 將 gubot03 加為管理員並更改管裡員權限
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
]
# -------------- 搶紅包測試 --------------
s1_grab_red_envelop_regression_list = [
    ContextTestCase("test_app_grab_red_envelope"),
    ContextTestCase("test_app_grab_luck_red_envelope"),
    ContextTestCase("test_app_grab_bulk_upload_luck_red_envelope")
]
# -------------- 社群相關功能測試 --------------
s1_social_regression_list = [
    AppTestCase("test_social_post_photo"),  # 發布圖片
    AppTestCase("test_social_search"),  # 搜索視頻 & 用戶
    AppTestCase("test_social_follow_unfollow"),  # 關注/取消關注
    AppTestCase("test_social_other_post_add_comments_reply"),  # 他人貼文評論上留言回覆
    AppTestCase("test_social_self_post_add_comments_reply_like"),  # 自己貼文評論上留言回覆點贊
    AppTestCase('test_social_share_self_main_page'),  # 分享"自己主頁"到群組
    AppTestCase('test_social_share_other_main_page'),  # 分享"他人主頁"到群組
    AppTestCase('test_social_share_self_post'),  # 分享"自己貼文"到群組
    AppTestCase('test_social_share_others_post'),  # 分享"他人貼文"到群組
]

# ============================================== S2 Test cases ===================================================
# -------------- 私聊相關功能測試 --------------
s2_personal_chat_regression_list = [
    AppTestCase("test_notify_switch"),
    AppTestCase("test_about_product"),
    AppTestCase("test_add_friend"),  # s1
    AppTestCase("test_add_myself"),
    AppTestCase("test_block_friend"),
    AppTestCase("test_block_setting"),
    AppTestCase("test_unblock_friend"),
    AppTestCase("test_share_message"),
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
    AppTestCase('test_voice_message_reply'),
    AppTestCase('test_voice_message_delete'),
    AppTestCase('test_voice_message_revoke'),
    AppTestCase('test_file_message_reply'),
    AppTestCase('test_file_message_delete'),
    AppTestCase('test_file_message_revoke'),
    AppTestCase("test_delete_friend"),  # s1
    AppTestCase("test_logout"),  # s1
]
# -------------- 群聊相關功能測試 --------------
s2_group_chat_regression_list = [
    AppTestCase("test_message_pin_reply_group"),
    AppTestCase("test_message_pin_delete_group"),
    AppTestCase("test_message_pin_revoke_group"),
    ContextTestCase("test_user_contact_whitelist_be_fe_linkage"),  # 測試-會員添加好友設定前後端連動
    ContextTestCase("test_search_friend_by_phone_and_ID"),  # 測試-透過ID/手機號搜索添加白名單/非白名單成員
    ContextTestCase("test_admin_send_system_notification"),  # 後台發送系統訊息 > 前台確認系統通知
    ContextTestCase("test_admin_send_group_msg"),  # 後台發送群組訊息 > 前台確認群內訊息
]
# -------------- 發現設定測試 --------------
s2_discover_regression_list = [
    ContextTestCase("test_discover_list"),  # 後台切換發現功能 > 前台確認排序
    AppTestCase("test_discover_floating_icon"),  # 確認功能懸浮按鈕與選單
]
# -------------- 社群相關功能測試 --------------
s2_social_regression_list = [
    ContextTestCase("test_social_change_poster_auto_audit_type"),  # 不同審核權限下發布的貼文
    ContextTestCase("test_block_words_blocks_instructions_input"),  # 後台新增屏蔽字詞 >前台確認個人簡介阻擋屏蔽字輸入
    ContextTestCase("test_post_comment_when_social_permission_change"),  # 後台切換帳號社群權限 > 前台確認評論留言
    ContextTestCase("test_post_URL_when_post_permission_change"),  # 後台切換貼文評論超連結開關 > 前台確認評論留言URL
]
# -------------- 其他功能測試 --------------
s2_combination_regression_list = [
    ContextTestCase("test_app_email_registration"),  # 測試-email註冊 (後台需先關閉極驗)
    ContextTestCase("test_app_email_forgetPW"),  # 測試-email登入時忘記密碼 > 重設
]

s1_test_cases = (s1_personal_chat_regression_list + s1_group_chat_regression_list + s1_grab_red_envelop_regression_list
                 + s1_social_regression_list)
s2_test_cases = (s2_personal_chat_regression_list + s2_group_chat_regression_list + s2_discover_regression_list
                 + s2_social_regression_list + s2_combination_regression_list)
all_test_cases = (s1_test_cases + s2_test_cases)

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
    gl.set_value('ACCOUNT_TYPE', account_type)

    # for jira config
    gl.set_value('TEST_TYPE', 'app_ios')  # android: app_android , ios: app_ios
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # 自動啟動 iOS WDA
    Utils.start_wda_for_ios()

    # TestCase add：S1 跑完 + retry 失敗後發 S1 報告到 Slack，再跑 S2 + retry 後發 S2 報告到 Slack
    suite_s1 = unittest.TestSuite()
    suite_s1.addTests(s1_test_cases)  # total 44*s1
    suite_s2 = unittest.TestSuite()
    suite_s2.addTests(s2_test_cases)  # total 40*s2 + 3*s1

    # S1：跑完 + retry 失敗案例 → 發 S1 報告到 Slack
    # Utils.unittest_xml_with_retry_and_slack(suite_s1, report_label='S1', run_check_last_result=False)
    # S2：跑完 + retry 失敗案例 → 發 S2 報告到 Slack，並執行 Jira check_last_result
    Utils.unittest_xml_with_retry_and_slack(suite_s2, report_label='S2', run_check_last_result=True)
