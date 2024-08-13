import os
import sys
import unittest
import logging

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)

import common.utils.globalvar as gl
from common.utils.utils import Utils
from Project.lottery.app.testcase.app_testcase import AppTestCase
from jira.config.base_key import BaseKey

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'stage'
brand = 'lv'
user = 3
connect_type = 'remote' # 手機連線模式
phone_name = 'REDMI_45' # 手機型號
phone_platform = 'Android' # 手機作業系統
app_version = '14.7.10'
specific_os_version = [] # 指定OS版本, ['10','11','8']
push = True # 將結果推倒jira, 預設請給予 True

app_regression_list = [
    AppTestCase("test_change_env"),
    AppTestCase("test_version_check"),
    AppTestCase("test_register"),
    AppTestCase("test_login"),
    AppTestCase("test_transform_ag"),
    AppTestCase("test_transform_mg"),
    AppTestCase("test_transform_sb"),
    AppTestCase("test_transform_bbin"),
    AppTestCase("test_transform_3s"),
    AppTestCase("test_transform_lgd"),
    AppTestCase("test_transform_ky"),
    AppTestCase("test_transform_vg"),
    AppTestCase("test_transform_sw"),
    AppTestCase("test_transform_pt"),
    AppTestCase("test_transform_kx"),
    AppTestCase("test_transform_kk"),
    AppTestCase("test_transform_hg"),
    AppTestCase("test_transform_gm"),
    AppTestCase("test_transform_fg"),
    AppTestCase("test_transform_dg"),
    AppTestCase("test_transform_cq9"),
    AppTestCase("test_transform_bsp"),
    
    AppTestCase("test_deposit_company"),
    AppTestCase("test_desposit_aliPay_f2f"),
    AppTestCase("test_desposit_aliPay_transfer"),
    AppTestCase("test_withdraw"),

    AppTestCase('test_get_wallet_info'),
    AppTestCase("test_bet_vgcard"),
    AppTestCase("test_bet_kxcard"),
    AppTestCase("test_bet_gmcard"),
    AppTestCase("test_bet_fgcard"),
    AppTestCase("test_bet_kycard"),
    AppTestCase("test_bet_bscard"),
    AppTestCase("test_bet_kkcard"),
    
    AppTestCase("test_bet_cq9game"),
    AppTestCase("test_bet_fggame"),
    # AppTestCase("test_bet_swgame"), # sw 公司IP進不去
    AppTestCase("test_bet_ptgame"),
    AppTestCase("test_bet_lgdgame"),
    AppTestCase("test_bet_bbingame"),
    AppTestCase("test_bet_kkgame"),
    
    AppTestCase("test_bet_sbsport"),
    AppTestCase("test_bet_bbinsport"),
    AppTestCase("test_bet_sssport"),
    AppTestCase("test_bet_hgsport"),

    AppTestCase("test_niu_niu_bet"),
    AppTestCase("test_mine_sweeping_bet"),

    AppTestCase("test_into_faq"),
    AppTestCase("test_into_mailcenter"),
    AppTestCase("test_into_promotions"),
    AppTestCase("test_into_ledger"),
    AppTestCase("test_into_myinfo"),
    AppTestCase("test_into_deposit_record"),
    AppTestCase("test_into_withdraw_record"),
    AppTestCase("test_into_bet_record"),
    AppTestCase("test_into_agent"),
    AppTestCase("test_into_about"),
    AppTestCase("test_into_feedback"),
    AppTestCase("test_into_share"),
    AppTestCase("test_bet_record_filter"),

    # AppTestCase("test_bet_agfish"), # 等待翻轉螢幕功能

    AppTestCase("test_all_transform_cp"),
]

app_lottery_list = [
    AppTestCase("test_betting_wfk3"),
    AppTestCase("test_betting_hk"),
    AppTestCase("test_betting_wf11x5"),
    AppTestCase("test_betting_fu3d"),
    AppTestCase("test_betting_wfpk10"),
    AppTestCase("test_betting_wfssc"),
    AppTestCase("test_betting_twxy28"),
]

if __name__ == '__main__':
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) == 8:
        env = sys.argv[1]
        brand = sys.argv[2]
        user = sys.argv[3]
        app_version = sys.argv[4]
        connect_type = sys.argv[5]
        phone_name = sys.argv[6]
        specific_os_version = sys.argv[7]

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
    suite.addTests(app_lottery_list)
    
    # RuningTest
    Utils.unittest_xml(suite)