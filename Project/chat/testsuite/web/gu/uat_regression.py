import os
import sys
import unittest

root_path = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

from common.utils.utils import Utils
from Project.chat.web.testcase.web_testcases import WebTestCase
from Project.chat.web.testcase.admin_testcases import AdminTestCase
import common.utils.globalvar as gl
from jira.config.base_key import BaseKey

# Test Setting
brand = 'gu'  # gu, chit
user = 1
test_type = 'web'
os_version = 'Win11'  # 作業系統
platform = 'PC'  # 測試環境
push = True  # 將結果推倒jira, 預設請給予 True
# ============================================== S1 Test Cases ===================================================
s1_web_regression_list = [
    WebTestCase("test_web_login"),  # 測試-登入
    WebTestCase("test_account_info"),  # 測試-檢查帳號與手機號碼
    WebTestCase("test_change_password"),  # 測試-變更登入密碼
    WebTestCase("test_change_nickname"),  # 測試-更改個人暱稱
    WebTestCase("test_notify_switch"),   # 測試-訊息通知開關
    WebTestCase("test_add_friend"),  # 測試-新增好友
    WebTestCase("test_friend_remark"),  # 測試-好友暱稱
    WebTestCase("test_block_friend"),  # 測試-好友黑名單
    WebTestCase("test_block_setting"),  # 測試-好友黑名單設定
    WebTestCase("test_unblock_friend"),  # 測試-解除好友黑名單
    WebTestCase("test_send_message"),  # 測試-個人發送文字超連結訊息
    WebTestCase("test_message_copy"),  # 測試-個人訊息複製
    WebTestCase("test_message_reply"),  # 測試-個人訊息回覆
    WebTestCase("test_message_revoke"),  # 測試-個人訊息撤回
    WebTestCase("test_message_pin"),  # 測試-個人訊息設置公告
    WebTestCase("test_send_file_message"),  # 測試-個人發送檔案
    WebTestCase("test_file_message_reply"),  # 測試-個人檔案訊息回覆
    WebTestCase("test_file_message_revoke"),  # 測試-個人檔案訊息撤回
    WebTestCase("test_groups_build"),  # 測試-建立群組
    WebTestCase("test_group_name_change"),  # 測試-變更群組名稱
    WebTestCase("test_group_rule_all"),  # 測試-變更群組權限設定
    WebTestCase("test_send_message_group"),  # 測試-群組發送文字超連結訊息
    WebTestCase("test_message_copy_group"),  # 測試-群組訊息複製
    WebTestCase("test_message_reply_group"),   # 測試-群組發訊息回覆
    WebTestCase("test_message_revoke_group"),   # 測試-群組訊息撤回
    WebTestCase("test_message_pin_group"),  # 測試-群組訊息設置公告
    WebTestCase("test_send_file_message_group"),  # 測試-群組發送檔案
    WebTestCase("test_file_message_reply_group"),  # 測試-群組檔案訊息回覆
    WebTestCase("test_file_message_revoke_group"),  # 測試-群組檔案訊息撤回
    WebTestCase("test_delete_friend"),  # 測試-刪除好友
    WebTestCase("test_web_logout"),  # 測試-登出
]
s1_admin_regression_list = [
    AdminTestCase("test_admin_login"),  # 測試-ADMIN登入
    AdminTestCase("test_into_and_check_member_list"),  # 測試-進入會員列表並檢查基本資訊
    AdminTestCase("test_into_and_check_member_level"),  # 測試-進入會員層級並檢查基本資訊
    AdminTestCase("test_into_and_check_groups_list"),  # 測試-進入群組列表
    AdminTestCase("test_into_groups_set"),  # 測試-進入群組設定
    AdminTestCase("test_into_groups_own"),  # 測試-進入群組建立成員
    AdminTestCase("test_into_share_code_setting"),  # 測試-後台登入不同權限帳號,確認對應'邀請碼管理'頁顯示與不顯示
    AdminTestCase("test_into_system_maintenance"),  # 測試-進入APP/Web维护
    AdminTestCase("test_into_system_app_setting"),  # 測試-進入APP/Web设定
    AdminTestCase("test_into_setting_account"),   # 測試-進入帳號管理
    AdminTestCase("test_into_setting_role"),  # 測試-進入角色權限
    AdminTestCase("test_into_logging"),  # 測試-進入操作日誌
    AdminTestCase("test_into_red_list"),  # 測試-進入紅包列表
    AdminTestCase("test_into_red_integral"),  # 測試-進入積分使用紀錄
    AdminTestCase("test_into_red_water"),  # 測試-進入水量控制
    AdminTestCase("test_build_group_permission"),  # 測試-群組建立權限設定
    AdminTestCase("test_manual_create_account"),  # 測試-人工創建帳號
    AdminTestCase("test_member_revise_remark"),  # 測試-設定備註
    AdminTestCase("test_member_change_data"),  # 測試-修改資料
    AdminTestCase("test_member_reset_security_password"),  # 測試-重製安全密碼
    AdminTestCase("test_member_change_password"),  # 測試-變更密碼
    AdminTestCase("test_member_search_function"),   # 測試-搜尋功能
    AdminTestCase("test_manual_create_account_delete"),  # 測試-刪除人工創建帳號
    AdminTestCase("test_group_delete"),  # 測試-刪除群組
]
s1_exchange_related_list = [
    WebTestCase("test_manual_deposit_and_withdraw"),  # 測試-人工存入&人工提出積分
    # ======================積分兌換=====================================
    # ---------- 順付 ---------
    WebTestCase("test_exchange_wellpay"),  # 測試-綁定正確的錢包並兌換積分 (順付)
    AdminTestCase("test_exchange_success_recode"),   # 測試-順付成功積分紀錄
    # ---------- 平臺 ---------
    WebTestCase("test_exchange_brand"),  # 測試-綁定平臺SC,兌換積分,確認兌換紀錄
]
s1_red_envelope_related_list = [
    AdminTestCase("test_add_redenvelope"),  # 測試-[後台]新增紅包
    AdminTestCase("test_check_red_envelope"),  # 測試-[後台]檢查紅包詳情
    WebTestCase("test_grab_red_envelope"),  # 測試-[前台]搶紅包
    AdminTestCase("test_add_luck_redenvelope"),  # 測試-[後台]新增拚手氣紅包
    AdminTestCase("test_check_luck_red_envelope"),  # 測試-[後台]檢查拚手氣紅包詳情
    WebTestCase("test_grab_luck_red_envelope"),  # 測試-[前台]搶拚手氣紅包
]

# ============================================== S2 Test Cases ===================================================
s2_web_regression_list = [
    WebTestCase("test_web_login"),  # 測試-登入  # s1
    WebTestCase("test_into_notification"),  # 測試-進入訊息通知
    WebTestCase("test_into_security"),  # 測試-進入帳號與安全頁面
    WebTestCase("test_into_black"),  # 測試-進入黑名單頁面
    WebTestCase("test_into_share"),  # 測試-進入分享頁面
    WebTestCase("test_into_about"),  # 測試-進入關於名品會頁面
    WebTestCase("test_about_terms"),  # 測試-關於聊天-檢查服務條款/隱私權政策
    WebTestCase("test_user_contact_whitelist_be_fe_linkage"),  # 測試-會員添加好友設定前後端連動
    WebTestCase("test_contact_whitelist_setting_be_fe_linkage"),  # 測試-好友添加白名單設定前後端連動
    WebTestCase("test_search_friend_by_phone_and_ID"),  # 測試-透過手機號/ID搜索添加好友
    WebTestCase("test_add_friend"),  # 測試-新增好友  # s1
    WebTestCase("test_share_url"),  # 測試-分享網址功能
    WebTestCase("test_send_media"),  # 測試-個人發送圖片/影片
    WebTestCase("test_message_reply_revoke"),  # 測試-個人訊息回覆後撤回
    WebTestCase("test_message_emoji"),  # 測試-訊息表情符號
    WebTestCase("test_message_pin_reply"),  # 測試-個人訊息設置公告後回覆
    WebTestCase("test_message_pin_revoke"),  # 測試-個人訊息設置公告後撤回
    WebTestCase("test_groups_build"),  # 測試-建立群組
    WebTestCase("test_message_pin_reply_group"),  # 測試-群組訊息設置公告後回覆
    WebTestCase("test_message_pin_revoke_group"),  # 測試-群組訊息設置公告後撤回
    WebTestCase("test_delete_friend"),  # 測試-刪除好友  # s1
]
s2_admin_regression_list = [
    AdminTestCase("test_add_share_code"),  # 測試 - 後台新增邀請碼 > 刪除邀請碼
    WebTestCase("test_share_code_visible_when_permission_change"),  # 測試-後台設定邀請碼權限>前台一般成員&管理員確認邀請碼分享欄位
    AdminTestCase("test_into_groups_message"),  # 測試-進入群發消息
    AdminTestCase("test_into_system_contact_whitelist_setting"),  # 測試-不同權限帳號下的'好友添加白名单设定'頁顯示與否
    AdminTestCase("test_into_discover_and_edit"),  # 測試-發現設定編輯網址+開關切換
    AdminTestCase("test_into_record_check_chat_record"),  # 測試-進入聊天纪录並確認紀錄
    AdminTestCase("test_into_setting_otp"),  # 測試-進入OTP管理
    AdminTestCase("test_into_setting_otp_operation"),  # 測試-進入運營OTP
    AdminTestCase("test_into_media_audit"),  # 測試-進入媒体审核
    AdminTestCase("test_into_auto_audit"),  # 測試-進入自动审核
    AdminTestCase("test_into_block_words"),  # 測試-進入屏蔽字詞
    AdminTestCase("test_into_impeach"),  # 測試-進入检举内容
    AdminTestCase("test_into_post_data"),  # 測試-進入贴文数据
    AdminTestCase("test_into_creator_data"),  # 測試-進入创作者数据
    AdminTestCase("test_group_delete"),  # 測試-刪除群組
]
s2_exchange_related_list = [
    # ======================積分兌換=====================================
    # ---------- 順付 ---------
    WebTestCase("test_exchange_wellpay_incorrect"),  # 測試-綁定錯誤的錢包並兌換積分 (順付)
    AdminTestCase("test_exchange_fail_recode"),  # 測試-順付返還積分紀錄
]
s2_red_envelope_related_list = [
    AdminTestCase("add_auto_grad_red_envelope"),
    WebTestCase("test_auto_grab_red_envelope"),  # 測試-[前台]自動搶一般紅包
    AdminTestCase("add_auto_grad_luck_red_envelope_then_check_water_control"),  # 測試-[後台]新增拚手氣紅包並檢查水量
    WebTestCase("test_auto_grab_luck_red_envelope"),  # 測試-[前台]自動搶拚手氣紅包
]

s1_test_cases = (s1_web_regression_list + s1_admin_regression_list + s1_exchange_related_list
                 + s1_red_envelope_related_list)
s2_test_cases = (s2_web_regression_list + s2_admin_regression_list + s2_exchange_related_list
                 + s2_red_envelope_related_list)
all_test_cases = (s1_test_cases + s2_test_cases)

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
    gl.set_value('PHONE_PLATFORM', os_version)  # 作業系統名稱
    gl.set_value('PHONE_NAME', platform)

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    try:
        BaseKey().get_jira_data()
    except FileNotFoundError as e:
        # Jenkins/Docker 環境可能不會提供 Jira key 檔，缺檔時先跳過 Jira 回填避免整體 regression 失敗
        print(f"[WARN] {e}. Skip Jira push for this run.")
        push = False
    gl.set_value('PUSH', push)

    # TestCase add：S1 跑完 + retry 失敗後發 S1 報告到 Slack，再跑 S2 + retry 後發 S2 報告到 Slack
    suite_s1 = unittest.TestSuite()
    suite_s1.addTests(s1_test_cases)  # total 65*s1
    suite_s2 = unittest.TestSuite()
    suite_s2.addTests(s2_test_cases)  # total 37*s2 + 5*s1

    # S1：跑完 + retry 失敗案例 → 發 S1 報告到 Slack
    Utils.unittest_xml_with_retry_and_slack(suite_s1, report_label='S1', run_check_last_result=True)
    # S2：跑完 + retry 失敗案例 → 發 S2 報告到 Slack，並執行 Jira check_last_result
    Utils.unittest_xml_with_retry_and_slack(suite_s2, report_label='S2', run_check_last_result=True)
