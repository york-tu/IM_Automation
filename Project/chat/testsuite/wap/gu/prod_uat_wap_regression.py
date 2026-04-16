import os
import sys
import unittest
import common.utils.globalvar as gl

from common.utils.utils import Utils
from Project.chat.web.testcase.wap_testcases import WapTestCase
from jira.config.base_key import BaseKey

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

# Test Setting
env = 'prod'  # uat, prod
brand = 'gu'
user = 1
test_type = 'wap'
wap_version = '2.12.0'
os_version = 'Win11'  # 作業系統
platform = 'PC'  # 測試環境
account_type = 'phone'  # 帳號類型: mail, phone...
push = True  # 將結果推倒jira, 預設請給予 True

# ============================================== S1 Test Cases ===================================================
s1_personal_chat_case_list = [
    WapTestCase("test_wap_login"),  # 測試-登入
    WapTestCase('test_version_check'),  # 測試-確認版號
    WapTestCase("test_into_member"),  # 測試-進入主頁我的設定頁
    WapTestCase("test_into_friend"),  # 測試-進入好友名單頁
    WapTestCase("test_change_password"),  # 測試-修改登入密碼
    WapTestCase('test_change_nickname_and_instructions'),  # 測試-編輯個人暱稱&說明
    WapTestCase("test_add_friend"),  # 測試-新增好友
    WapTestCase("test_friend_remark"),  # 測試-好友聊天詳情頁備註暱稱 & 描述
    WapTestCase("test_block_and_report_friend"),  # 測試-好友加入黑名單&檢舉
    WapTestCase("test_unblock_friend"),  # 測試-解除好友黑名單
    WapTestCase('test_1v1_send_message'),  # 測試-私聊-發送訊息
    WapTestCase('test_1v1_send_voice_message'),  # 測試-私聊-發送語音訊息
    WapTestCase('test_1v1_send_file_message'),  # 測試-私聊-發送檔案訊息
    WapTestCase("test_delete_friend"),  # 測試-刪除好友
]
s1_group_chat_case_list = [
    WapTestCase("test_group_send_message"),  # 測試-群組-發送訊息
    WapTestCase("test_group_message_copy"),  # 測試-群組-訊息複製並發送
    WapTestCase("test_group_message_reply"),  # 測試-群組-訊息回覆
    WapTestCase("test_group_message_revoke"),  # 測試-群組-訊息撤回
    WapTestCase("test_group_message_pin"),  # 測試-群組-設置公告
    WapTestCase("test_group_send_voice_message"),  # 測試-群組-發送語音訊息
    WapTestCase('test_group_voice_message_reply'),  # 測試-群組-語音訊息回覆
    WapTestCase('test_group_voice_message_revoke'),  # 測試-群組-語音訊息撤回
    WapTestCase('test_group_send_file_message'),  # 測試-群組-發送檔案訊息
    WapTestCase('test_group_file_message_reply'),  # 測試-群組-檔案訊息回覆
    WapTestCase('test_group_file_message_revoke'),  # 測試-群組-檔案訊息撤回
    WapTestCase('test_wap_logout'),  # 測試-登出
]
# =========================================== UAT only ===========================================
s1_social_case_list = [
    WapTestCase("test_social_post_photo"),  # 測試-發布圖片
    WapTestCase('test_social_post_video'),  # 測試-發布影片
    WapTestCase('test_social_search'),  # 測試-搜索視頻&用戶
    WapTestCase('test_social_follow_unfollow'),  # 測試-關注&取消關注
    WapTestCase('test_social_share_self_main_page'),  # 測試-分享自己主頁
    WapTestCase('test_social_share_self_post'),  # 測試-分享自己貼文
]

# ============================================== S2 Test Cases ===================================================
s2_personal_chat_case_list = [
    WapTestCase("test_about_terms"),  # 測試-進入關於股聊-服務條款/隱私權政策
    WapTestCase("test_add_friend"),  # 測試-新增好友  #s1
    WapTestCase('test_1v1_message_copy'),  # 測試-私聊-訊息複製並發送
    WapTestCase('test_1v1_message_reply'),  # 測試-私聊-訊息回覆
    WapTestCase("test_1v1_message_revoke"),  # 測試-私聊-訊息撤回
    WapTestCase("test_1v1_message_reply_revoke"),  # 測試-私聊-訊息回覆後撤回
    WapTestCase("test_1v1_message_add_emoji"),  # 測試-私聊-訊息添加表情符號
    WapTestCase("test_1v1_message_pin"),  # 測試-私聊-設置公告
    WapTestCase("test_1v1_message_pin_reply"),  # 測試-私聊-回覆訊息設為公告
    WapTestCase("test_1v1_message_pin_revoke"),  # 測試-私聊-訊息設為公告後撤回
    WapTestCase('test_1v1_voice_message_reply'),  # 測試-私聊-語音訊息回覆
    WapTestCase('test_1v1_voice_message_revoke'),  # 測試-私聊-語音訊息撤回
    WapTestCase('test_1v1_file_message_reply'),  # 測試-私聊-檔案訊息回覆
    WapTestCase('test_1v1_file_message_revoke'),  # 測試-私聊-檔案訊息撤回
    WapTestCase("test_delete_friend"),  # 測試-刪除好友  #s1
]
s2_group_chat_case_list = [
    WapTestCase("test_group_message_reply_revoke"),  # 測試-群組-訊息回覆後撤回
    WapTestCase("test_group_message_add_emoji"),  # 測試-群組-訊息添加表情符號
    WapTestCase("test_group_message_pin_reply"),  # 測試-群組-回覆訊息設為公告
    WapTestCase("test_group_message_pin_revoke"),  # 測試-群組-訊息設置公告後撤回
]
# =========================================== UAT only ===========================================
s2_combination_case_list = [
    WapTestCase("test_mWeb_email_registration"),  # 測試-email註冊
]

# ================================================================================================
# =========================================== UAT ================================================
s1_test_cases = (s1_personal_chat_case_list + s1_group_chat_case_list + s1_social_case_list)
s2_test_cases = (s2_personal_chat_case_list + s2_group_chat_case_list + s2_combination_case_list)

# =========================================== Prod ===============================================
prod_test_cases = (s1_personal_chat_case_list + s1_group_chat_case_list + s2_personal_chat_case_list
                   + s2_group_chat_case_list)

if __name__ == "__main__":
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        # 參數格式（與其他 regression 腳本一致）
        # argv[2]=brand, argv[3]=user, argv[4]="env,,x,,x,,push,,wap_version,,account_type"
        raw = sys.argv[4] if len(sys.argv) > 4 else ''
        data = raw.split(',,') if raw else []
        brand = sys.argv[2]
        user = sys.argv[3]

        # data[0]=env, data[3]=push, data[4]=wap_version, data[5]=account_type
        if len(data) >= 1 and data[0]:
            env = data[0]
        if len(data) >= 4 and data[3] != '':
            push = str(data[3]).strip().lower() in ('1', 'true', 'yes', 'y')
        if len(data) >= 5 and data[4]:
            wap_version = data[4]
        if len(data) >= 6 and data[5]:
            account_type = data[5]

        if len(data) < 6:
            print(f"[WARN] argv[4] segments < 6, using defaults. raw={raw!r} parsed={data!r}")

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('ACCOUNT_TYPE', account_type)
    # gl.set_value('WAP_VERSION', wap_version)
    gl.set_value('PHONE_PLATFORM', wap_version)  # 作業系統名稱
    gl.set_value('PHONE_NAME', platform)

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    try:
        BaseKey().get_jira_data()
    except FileNotFoundError as e:
        print(f"[WARN] {e}. Skip Jira push for this run.")
        push = False
    gl.set_value('PUSH', push)

    # TestCase add：S1 跑完 + retry 失敗後發 S1 報告到 Slack，再跑 S2 + retry 後發 S2 報告到 Slack
    suite_s1 = unittest.TestSuite()
    suite_s1.addTests(s1_test_cases)  # total 32*s1
    suite_s2 = unittest.TestSuite()
    suite_s2.addTests(s2_test_cases)  # total 18*s2 + 2*s1

    suit_prod = unittest.TestSuite()  # prod cases
    suit_prod.addTests(prod_test_cases)

    if env == 'prod':  # uat, prod
        Utils.unittest_xml_with_retry_and_slack(suit_prod, report_label='S1', run_check_last_result=True)
    else:  # uat
        # S1：跑完 + retry 失敗案例 → 發 S1 報告到 Slack
        Utils.unittest_xml_with_retry_and_slack(suite_s1, report_label='S1', run_check_last_result=True)
        # S2：跑完 + retry 失敗案例 → 發 S2 報告到 Slack，並執行 Jira check_last_result
        Utils.unittest_xml_with_retry_and_slack(suite_s2, report_label='S2', run_check_last_result=True)
