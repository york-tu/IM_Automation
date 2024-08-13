import os
import sys
import unittest
import logging

dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(dir_name)
from Project.exchange.app.testcase.app_testcase import AppTestCase
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
from common.app.common import Common

import stf_api.stf as stf
import stf_api.stf_utils as stf_utils
import common.utils.globalvar as gl
from common.utils.utils import Utils
from jira.config.base_key import BaseKey

logging.getLogger("airtest").setLevel(logging.WARNING)

# Test Setting
env = 'uat'
channel_brand = 'c7'    # 為配合共用檔案，故將 brand 改為 channel_brand
user = 1
test_type = 'app_2.0'  # app_2.0: 順付2.0
brand = 'zqb'          # 為配合共用檔案，故將 channel_name 改為 brand
connect_type = 'local' # 手機連線模式: remote / local
phone_name = 'HUAWEI_24' # 手機型號 REDMI_19/POCO_55
remote_url = ''
app_version = '9.0.1-rc.2'
specific_os_version = [] # 指定OS版本, ['10','11','8']
phone_platform = 'Android' # 手機作業系統
push = True  # 將結果推倒jira, 預設請給予 True

app_regression_list = [

    AppTestCase("test_check_version"),
    AppTestCase("test_register"),
    AppTestCase("test_buy_tutorial"),
    AppTestCase("test_sell_tutorial"),
    AppTestCase("test_deposit_tutorial"),
    AppTestCase("test_customer_service"),
    AppTestCase("test_logout"),

    ####
    AppTestCase("test_login"),
    AppTestCase("test_grap_order_account"),
    AppTestCase("test_grap_order_qrcode"),
    AppTestCase("test_want_buy"),
    AppTestCase("test_want_sell"),
    AppTestCase("test_logout"),

    ####
    AppTestCase("test_login"),
    AppTestCase("test_deposit"),
    AppTestCase("test_wallet_address_deposit"),
    AppTestCase("test_pay_info"),
    AppTestCase("test_deposit_record_info"),
    AppTestCase("test_add_and_delete_bank_transfer"),
    AppTestCase("test_add_wechat_transfer"),
    AppTestCase("test_add_alipay_transfer"),
    AppTestCase("test_member_data"),
    AppTestCase("test_change_password"),
    AppTestCase("test_change_pay_password"),
    AppTestCase("test_version_update"),  # 後續需要新增當更新鍵enable後, 點擊後需要做的事(更新版本 > 更新完比對版本)
    AppTestCase("test_take_off_sale_order"),
    AppTestCase("test_logout"),

    # =================================================================
    # AppTestCase("test_sell_all_record_page"), #
]

# channel_brand_api_list = [
#     UiApiAdminTestCases("test_add_onlinedesposit_kcurrency_alipaytransfer"),
#     UiApiAdminTestCases("test_add_wellpay_wallet_withdraw"),
#     UiApiAdminTestCases("test_add_wellpay_mybuy_withdraw"),
# ]

if __name__ == '__main__':
    gl._init()

    # 以CMD方式執行
    if len(sys.argv) > 2:
        env = sys.argv[1]
        brand = sys.argv[2]
        user = int(sys.argv[3])
        data = sys.argv[4].split(',,')
        channel_brand = data[0]
        app_version = data[1]
        connect_type = data[2]
        phone_name = data[3]
        specific_os_version = data[4]
        push = bool(data[5])

    gl.set_value('ENV', env)
    gl.set_value('BRAND', brand)
    gl.set_value('USER', user)
    gl.set_value('CHANNEL_BRAND', channel_brand)
    gl.set_value('APP_VERSION', app_version)
    gl.set_value('CONNECT_TYPE', connect_type)
    gl.set_value('PHONE_NAME', phone_name)
    gl.set_value('SPECIFIC_OS_VERSION', specific_os_version)
    gl.set_value('PHONE_PLATFORM', phone_platform) # 作業系統名稱

    # for jira config
    gl.set_value('TEST_TYPE', test_type)
    BaseKey().get_jira_data() # jira_key.yml還沒補上app的
    gl.set_value('PUSH', push)

    # TestCase add
    suite = unittest.TestSuite()
    # suite.addTests(channel_brand_api_list)
    suite.addTests(app_regression_list)
    
    # RuningTest
    Utils.unittest_xml(suite)