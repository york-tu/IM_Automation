import os, sys, unittest
import logging, wda
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
import common.utils.globalvar as gl
import stf_api.stf as stf
import stf_api.stf_utils as stf_utils
from configs.app.setting import Setting as Setting_Phone
from Project.lottery.configs.setting import Setting
from jira.module.base_module import UnittestModule

class AppDriver(UnittestModule):
    
    # stf控制手機
    def stf_connect_phone(self):
        self.phone_name = gl.get_value('PHONE_NAME')

        if self.phone_name == 'None':
            phone_platform, phone_serial, phone_manufacturer, phone_marketName, \
                stf_notes, os_version = stf_utils.get_unuse_phone_serial(self.specific_os_version)
        else:
            phone_platform, phone_serial, phone_manufacturer, phone_marketName, \
                stf_notes, os_version = stf_utils.get_specific_phone_serial(self.phone_name)
        
        assert phone_serial != None, '沒有未使用中的手機 or 指定手機目前不可用'

        stf.post_use_phone(phone_serial) # 在stf上 把手機狀態改為using
        remote_url = stf.post_connect_phone(phone_serial) # 取得手機stf遠端網址 

        if phone_platform == 'iOS':
            remote_url = remote_url[0:-5]
        
        gl.set_value('PHONE_PLATFORM', phone_platform) # 手機OS
        gl.set_value('PHONE_SERIAL', phone_serial) # 手機UDID
        gl.set_value('PHONE_MANUFACTURER', phone_manufacturer) # 廠牌名稱
        gl.set_value('PHONE_MARKETNAME', phone_marketName) # 手機型號
        gl.set_value('STF_NOTES', stf_notes) # 手機備註(主要是填手機公司編號)
        gl.set_value('OS_VERSION', os_version) # 作業系統版本
        gl.set_value('PHONE_REMOTE_IP', remote_url) # 手機遠端控制的URL
        
        # 覆蓋原始local手機資訊
        self.phone_name = stf_notes
        gl.set_value('PHONE_NAME', stf_notes)

        print('\n==========================================')
        print(f'serial name: {gl.get_value("PHONE_SERIAL")}')
        print(f'manufacturer_name: {gl.get_value("PHONE_MANUFACTURER")}')
        print(f'marketName_name: {gl.get_value("PHONE_MARKETNAME")}')
        print(f'os_version: {gl.get_value("OS_VERSION")}')
        print(f'stf_notes: {gl.get_value("STF_NOTES")}')
        print('==========================================\n')

    # 注意func執行順序不可倒，要先執行過setting_test_data()
    def airtest_connect_phone(self):
        self.phone_name = gl.get_value('PHONE_NAME')
        self.connect_type = gl.get_value('CONNECT_TYPE')
        # 取得Airtest格式的手機連線link
        self.connection = Setting_Phone().get_phone_connect_link(self.phone_name, gl.get_value('PHONE_REMOTE_IP'), self.connect_type)

        cap_method = ''
        if 'MI' in gl.get_value('PHONE_NAME'):
            cap_method = 'javacap'
        if 'POCO' in gl.get_value('PHONE_NAME'):
            cap_method = 'javacap'

        while True:
            try:
                auto_setup(__file__, logdir=False, devices=[f'{self.connection}?cap_method={cap_method}']) # Airtest 連線手機
                break
            except Exception:
                logging.exception('exception log')

        if gl.get_value("PHONE_PLATFORM") == 'Android':
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=True)
            parameter = (poco, '')

        if gl.get_value("PHONE_PLATFORM") == 'iOS':
            if not cli_setup():
                auto_setup(__file__, logdir=True, devices=[self.connection,])
            poco = iosPoco()
            wda_service = wda.Client(self.connection.split('///')[-1])    
            parameter = (poco, wda_service)
            
        return parameter
