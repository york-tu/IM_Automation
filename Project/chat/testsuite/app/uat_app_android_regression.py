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
# ======================== [ios] ========================================
# phone_name = 'IPHONE_32'  # 手機型號 'HUAWEI_26', 'IPHONE_32'
# phone_platform = 'iOS'  # 手機作業系統 (Android, iOS)
# app_version = '4.25.0(99946.116)'  # android: 1.42.0-rc.4 , ios: 4.25.0(99946.116)
# ======================== [Android] ========================================
phone_name = 'HUAWEI_26'
phone_platform = 'Android'
app_version = '2.15.0-rc.4'
account_type = 'phone'  # 帳號類型: mail, phone...
# =================================================================================================
specific_os_version = []  # 指定OS版本, ['10','11','8']
push = True  # 將結果推倒jira, 預設請給予 True

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
    AppTestCase("test_change_password"),
    AppTestCase("test_account_info"),
    AppTestCase("test_free_up_space"),

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
    ContextTestCase("test_group_remove_admin"),  # 移除 gubot03 管理員權限
    ContextTestCase("test_group_change_group_rules"),  # 群組成員權限設定
    ContextTestCase("test_group_add_admin_and_change_admin_rules"),  # 將 gubot03 加為管理員並更改管裡員權限
    ContextTestCase("test_group_add_and_remove_member"),  # 加好友A(auto_test_7788) > 將A加入群 > 將A退群 > 刪好友A
    ContextTestCase("test_group_add_and_remove_block_member"),  # gubot05 加入黑名單 > 移出黑名單

    AppTestCase("test_join_group_by_share_code"),
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

    ContextTestCase("test_user_contact_whitelist_be_fe_linkage"),
    ContextTestCase("test_search_contact_by_phone_be_fe_linkage"),
    ContextTestCase("test_admin_send_system_notification"),  # 後台發送系統訊息 > 前台確認系統通知
    ContextTestCase("test_admin_send_group_msg"),  # 後台發送群組訊息 > 前台確認群內訊息
]

# =========== 發現設定測試 ===========
discover_regression_list = [
    ContextTestCase("test_discover_list"),  # 後台切換發現功能 > 前台確認排序
    AppTestCase("test_discover_floating_icon"),  # 確認功能懸浮按鈕與選單
]

# =========== 搶紅包測試 ===========
grab_red_envelop_regression_list = [
    ContextTestCase("test_app_grab_red_envelope"),
    ContextTestCase("test_app_grab_luck_red_envelope"),
    ContextTestCase("test_app_grab_bulk_upload_luck_red_envelope")
]

# =========== 社群相關功能測試 ===========
social_features_regression_list = [
    AppTestCase("test_social_post_photo"),  # 發布圖片
    AppTestCase('test_social_post_video'),  # 發布影片
    AppTestCase("test_social_draft_photo"),  # 發布草稿_圖片

    AppTestCase("test_social_search"),  # 搜索視頻 & 用戶

    AppTestCase("test_social_follow_unfollow"),  # 關注/取消關注
    AppTestCase("test_social_post_add_like_collect"),  # 貼文點贊收藏

    AppTestCase("test_social_self_post_add_comments_reply_like"),  # 自己貼文評論上留言回覆點贊
    AppTestCase("test_social_other_post_add_comments_reply"),  # 他人貼文評論上留言回覆

    AppTestCase("test_social_change_account_privacy"),  # 切換帳號隱私設定 > 確認他人端觀看"已點贊"媒體區
    AppTestCase('test_social_post_with_different_privacy'),  # 不同權限貼文對應不同關注用戶觀看

    AppTestCase('test_social_share_self_main_page'),  # 分享"自己主頁"到群組
    AppTestCase('test_social_share_other_main_page'),  # 分享"他人主頁"到群組
    AppTestCase('test_social_share_self_post'),  # 分享"自己貼文"到群組
    AppTestCase('test_social_share_others_post'),  # 分享"他人貼文"到群組

    ContextTestCase("test_social_change_post_privacy"),  # 前台切換貼文隱私權限 > 後台確認貼文觀看權限
    ContextTestCase("test_post_removed_after_impeach_approve"),  # 前台提出貼文檢舉 > 後台approve > 前台確認貼文下架
    ContextTestCase("test_post_view_then_check_views_and_viewers"),  # 前台觀看貼文 > 後台確認[貼文數據]&[創作者數據]觀看次數&觀看人數
    ContextTestCase("test_social_change_poster_auto_audit_type"),  # 後台變更發布者自動審核權限
    ContextTestCase("test_block_words_blocks_instructions_input"),  # 後台新增屏蔽字詞 >前台確認個人簡介阻擋屏蔽字輸入
    ContextTestCase("test_post_comment_when_social_permission_change"),  # 後台切換帳號社群權限 > 前台確認評論留言
    ContextTestCase("test_post_URL_when_post_permission_change"),  # 後台切換貼文評論超連結開關 > 前台確認評論留言URL
]
combination_regression_list = [
    ContextTestCase("test_app_email_registration"),  # 測試-email註冊 (後台需先關閉極驗)
    # AppTestCase('test_email_input_field_check'),  # 測試-email欄位檢核
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
    gl.set_value('ACCOUNT_TYPE', account_type)
    gl.set_value('SPECIFIC_OS_VERSION', specific_os_version)

    # for jira config
    gl.set_value('TEST_TYPE', 'app_android')  # android: app_android , ios: app_ios
    BaseKey().get_jira_data()
    gl.set_value('PUSH', push)

    # TestCase add
    suite = unittest.TestSuite()
    suite.addTests(one_on_one_chat_regression_list)
    suite.addTests(group_chat_regression_list)
    suite.addTests(discover_regression_list)
    suite.addTests(grab_red_envelop_regression_list)
    suite.addTests(social_features_regression_list)
    suite.addTests(combination_regression_list)

    # RunningTest
    Utils.unittest_xml(suite)
