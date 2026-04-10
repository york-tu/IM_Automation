import os
import sys
import unittest
from common.utils.utils import Utils
from Project.chat.web.testcase.web2_testcases import Web2TestCase

import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

# Test Setting
env = 'uat'  # uat, prod
brand = 'gu'
user = 1
test_type = 'web2'
# web2_version = '2.11.0'
os_version = 'Win11'  # 作業系統
platform = 'PC'  # 測試環境
account_type = 'phone'  # 帳號類型: mail, phone...
push = True  # 將結果推倒jira, 預設請給予 True

# ============================================== S1 Test Cases ===================================================
s1_case_list = [
    Web2TestCase("test_web2_login"),  # 測試-登入
    Web2TestCase('test_change_nickname_and_instructions'),  # 測試-編輯個人暱稱&說明
    Web2TestCase("test_social_post_photo"),  # 測試-發布圖片
    Web2TestCase('test_social_post_video'),  # 測試-發布影片
    #                 # Web2TestCase('test_social_search'),  # 測試-搜索視頻&用戶
    Web2TestCase('test_social_follow_unfollow'),  # 測試-關注 & 取消關注
    Web2TestCase("test_social_post_add_remove_likes_collections"),  # 貼文點贊/取消贊/收藏/取消收藏
    Web2TestCase('test_social_other_post_add_comments_reply'),  # 他人貼文評論上留言回覆
    Web2TestCase("test_social_self_post_add_comments_reply_like"),  # 自己貼文評論上留言回覆點贊
    Web2TestCase('test_web2_logout'),  # 測試-登出
]
s2_case_list = [
    Web2TestCase('test_social_post_with_different_privacy'),  # 測試-不同關注狀態用戶 v.s. 不同隱私權限貼文
    Web2TestCase('test_social_change_poster_auto_audit_type'),  # 後台變更發布者自動審核權限
    Web2TestCase("test_web2_email_registration"),  # 測試-email註冊
]

# ================================================================================================
# =========================================== UAT ================================================
# =========================================== Prod ===============================================


if __name__ == "__main__":
    gl._init()
    # 初始化 HOLD，確保第一個測試案例也能正確由 DecorateClass 綁定 Jira TESTCASE_KEY
    gl.set_value('HOLD', '')
    gl.set_value('TESTCASE_ID_MAP', {})
    gl.set_value('ERROR', [])
    gl.set_value('FAILURE', [])

    # 以CMD方式執行
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        raw = sys.argv[4] if len(sys.argv) > 4 else ''
        data = raw.split(',,') if raw else []
        brand = sys.argv[2]
        user = sys.argv[3]
        if len(data) >= 1 and data[0]:
            env = data[0]
        if len(data) >= 4 and data[3] != '':
            push = str(data[3]).strip().lower() in ('1', 'true', 'yes', 'y')
        if len(data) >= 5 and data[4]:
            web2_version = data[4]
        if len(data) >= 6 and data[5]:
            account_type = data[5]
        if len(data) < 6:
            print(f"[WARN] argv[4] segments < 6, using defaults. raw={raw!r} parsed={data!r}")

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', int(user))
    gl.set_value('ACCOUNT_TYPE', account_type)

    # gl.set_value('PHONE_PLATFORM', web2_version)  # 作業系統名稱
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
    suite_s1.addTests(s1_case_list)
    suite_s2 = unittest.TestSuite()
    suite_s2.addTests(s2_case_list)

    # S1：跑完 + retry 失敗案例 → 發 S1 報告到 Slack（不做最終補回填，避免與 S2 重複）
    Utils.unittest_xml_with_retry_and_slack(suite_s1, report_label='S1', run_check_last_result=False)
    # S2：跑完 + retry 失敗案例 → 發 S2 報告到 Slack（最後一段再做補回填）
    Utils.unittest_xml_with_retry_and_slack(suite_s2, report_label='S2', run_check_last_result=True)
