import datetime, re, platform, os, sys, xmlrunner
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
import common.utils.globalvar as gl
from jira.jira_api import JiraApi
class Utils(JiraApi):
    report = ''
    testcase_key = []
    testcase_id = []
   
    @staticmethod
    def unittest_xml(suite):
        gl.set_value('STATUS', ['amount', 'errors', 'failures', 'skipped']) # 四種測試結果
        gl.set_value('HOLD', '')
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        test_type = gl.get_value('TEST_TYPE')

        basename = os.path.basename(os.path.splitext(sys.argv[0])[0])
        if len(sys.argv) == 1:
            folderpath = os.path.dirname(os.path.abspath(__file__)) + "/../Test-Reports/" + test_type + "/" + env + "/" + brand + "/" + basename + "/" + datetime.datetime.now().strftime(
                '%Y-%m-%d_%H%M%S') + "/"

        elif len(sys.argv) >= 2:
            folderpath = os.getcwd() + "/" + 'Test-Reports' + "/" + "Jenkins" + "/" + test_type + "/" + env + "/" + brand + "/" + basename + "/" + datetime.datetime.now().strftime(
                '%Y-%m-%d_%H%M%S') + "/"

        gl.set_value('FOLDER_PATH', folderpath)    
        report_path = folderpath + "/" + 'TestReport.xml'

        if not os.path.exists(folderpath):
            os.makedirs(folderpath)

        print(folderpath)
        runner = xmlrunner.XMLTestRunner(output=folderpath, verbosity=2)
        Utils.report = runner.run(suite)
        Utils.check_last_result(Utils)

    @staticmethod
    def unittest_html(unittest, Testcase):
        from common.utils import html_test_runner_py3
        basename = os.path.basename(os.path.splitext(sys.argv[0])[0])
        if len(sys.argv) == 1:
            folderpath = os.getcwd() + "/" + 'Test-Reports' + "/" + "Testcase" + "/" + basename + "/" + datetime.datetime.now().strftime(
                '%Y-%m-%d_%H%M%S') + "/"
            Testcase.folderpath = folderpath

        elif len(sys.argv) == 2:
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('build_number', default='default')
            parser.add_argument('unittest_args', nargs='*')
            args = parser.parse_args()
            sys.argv[1:] = args.unittest_args
            build_num = args.build_number
            print('build_number: ' + build_num)
            folderpath = os.getcwd() + "/" + 'Test-Reports' + "/" + "Jenkins" + "/" + basename + "/" + build_num + "/"
            Testcase.folderpath = folderpath

        Testcase.basename = basename
        suite = unittest.TestLoader().loadTestsFromTestCase(Testcase)
        report_path = folderpath + "/" + 'TestReport.html'
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        fp = open(report_path, 'wb')
        runner = html_test_runner_py3.HTMLTestRunner(stream=fp, title='Regression Test Report', description='')
        runner.run(suite)
        fp.close()

    # 檢查最後一份測試案例的結果
    def check_last_result(self):
        if gl.get_value('PUSH') != True:
            return

        certification = JiraApi().jira_login() # jira登入
        # JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), gl.get_value('TESTCASE_KEY')[0], 'in progress') # 初始化測試結果

        if gl.get_value('TESTCASE_KEY') != None:
            resultcount = gl.get_value('RESULT_COUNT')
            orange_result = re.findall("[0-9]+", str(gl.get_value('RESULT')))
            finally_result = re.findall("[0-9]+", str(self.report))

            if finally_result != orange_result or finally_result[0] == finally_result[1] or resultcount[1:] != finally_result[1:]:
                result = gl.get_value('RESULT')
                if resultcount[1] != finally_result[1]:
                    gl.set_value('ERROR', result.errors)
                else:
                    gl.set_value('FAILURE', result.failures)
                # jira api
                JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), gl.get_value('TESTCASE_KEY')[0], 'fail')
            else:
                # jira api
                JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), gl.get_value('TESTCASE_KEY')[0], 'pass')

    # 檢查這次測試案例的結果
    def check_test_result(self, id, key, result):
        if gl.get_value('PUSH') != True:
            return

        success = True
        self.testcase_id.append(id)
        self.testcase_key.append(key)

        gl.set_value('OLD', [gl.get_value('AMOUNT'), gl.get_value('ERRORS'), gl.get_value('FAILURES'), gl.get_value('SKIPPED')])
        self.total(result)
        gl.set_value('NEW', [gl.get_value('AMOUNT'), gl.get_value('ERRORS'), gl.get_value('FAILURES'), gl.get_value('SKIPPED')])

        if gl.get_value('AMOUNT') >= 2:
            certification = JiraApi().jira_login() # jira登入
            # JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), self.TESTCASE_KEY[0], 'in progress') # 初始化測試結果
            try:
                for old, new, status in zip(gl.get_value('OLD'), gl.get_value('NEW'), gl.get_value('STATUS')):
                    if status == 'amount':
                        continue
                    if old != new:
                        success = False
                        if status == 'skipped':
                            status = 'skip'
                        else:
                            if status == 'errors':
                                gl.set_value('ERROR', result.errors)
                            if status == 'failures':
                                gl.set_value('FAILURE', result.failures)
                            status = 'fail'
                        # jira api
                        JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), self.testcase_key[0], status)
            
                if success == True:
                    # jira api
                    JiraApi().set_cycle_result(certification, gl.get_value('CYCLE_KEY'), self.testcase_key[0], 'pass')
            finally:
                del self.testcase_id[0]
                del self.testcase_key[0]
                gl.set_value('ERROR', [])
                gl.set_value('FAILURE', [])
            
        gl.set_value('TESTCASE_ID', self.testcase_id)
        gl.set_value('TESTCASE_KEY', self.testcase_key)

    # 紀錄個別結果的數量
    def total(self, result=None):
        amount = result.testsRun
        errors = result.errors
        failures = result.failures
        skipped = result.skipped
   
        gl.set_value('AMOUNT', amount)
        gl.set_value('ERRORS', len(errors))
        gl.set_value('FAILURES', len(failures))
        gl.set_value('SKIPPED', len(skipped))

    @staticmethod
    def start_wda_for_ios():
        """
        為 iOS 設備自動啟動 WDA（WebDriverAgent）
        使用 go-ios 工具啟動 WDA
        僅在 phone_platform 為 'iOS' 時執行
        
        Returns:
            bool: 啟動成功返回 True，否則返回 False
        """
        import subprocess
        import time
        from pathlib import Path
        from common.utils.config_loader import ConfigLoader
        
        phone_platform = gl.get_value('PHONE_PLATFORM')
        
        # 僅在 iOS 平台時啟動 WDA
        if phone_platform != 'iOS':
            return True  # 非 iOS 平台，無需啟動，返回成功
        
        phone_name = gl.get_value('PHONE_NAME')
        if not phone_name:
            print("⚠️  警告：未找到 PHONE_NAME，跳過 WDA 啟動")
            return False
        
        # 獲取設備配置和 UDID
        try:
            config_loader = ConfigLoader()
            phone_config = config_loader.get_phone_config()
            phone_conf = phone_config.get('Phone_conf', {})
            
            if phone_name not in phone_conf:
                print(f"⚠️  警告：找不到設備配置 '{phone_name}'，跳過 WDA 啟動")
                return False
            
            device_config = phone_conf[phone_name]
            udid = device_config.get('udid')
            
            if not udid:
                print(f"⚠️  警告：設備 '{phone_name}' 沒有配置 UDID，跳過 WDA 啟動")
                return False
                
        except Exception as e:
            print(f"⚠️  警告：無法讀取設備配置: {e}，跳過 WDA 啟動")
            return False
        
        print("\n" + "=" * 60)
        print("自動啟動 iOS WDA (使用 go-ios)...")
        print("=" * 60)
        print(f"📱 設備: {phone_name}")
        print(f"🔑 UDID: {udid}")
        print("🔄 正在使用 go-ios 啟動 WDA...")
        print("   這可能需要幾秒鐘時間...")
        
        try:
            # 獲取 go-ios 目錄路徑（使用專案根目錄下的 go-ios）
            from common.utils.path_utils import PathUtils
            project_root = PathUtils.get_project_root()
            go_ios_dir = project_root / 'go-ios'
            ios_exe = go_ios_dir / 'ios.exe'
            
            if not ios_exe.exists():
                print(f"❌ 錯誤：找不到 go-ios 工具: {ios_exe}")
                print("請確認 go-ios 資料夾存在且包含 ios.exe")
                return False
            
            # WDA Bundle ID 配置
            bundle_id = "com.YT.facebook.WebDriverAgentRunner.xctrunner"
            testrunner_bundle_id = "com.YT.facebook.WebDriverAgentRunner.xctrunner"
            xctest_config = "WebDriverAgentRunner.xctest"
            
            # 1. 終止現有的 ios.exe 進程
            print("🔹 終止現有的 ios.exe 進程...")
            try:
                if platform.system() == 'Windows':
                    subprocess.run(['taskkill', '/F', '/IM', 'ios.exe'], 
                                 capture_output=True, check=False)
                else:
                    subprocess.run(['pkill', '-f', 'ios.exe'], 
                                 capture_output=True, check=False)
            except Exception:
                pass  # 忽略錯誤，可能沒有運行中的進程
            
            # 2. 啟動 userspace tunnel
            print("🔹 啟動 userspace tunnel...")
            tunnel_cmd = [
                str(ios_exe),
                'tunnel', 'start',
                '--udid', udid,
                '--userspace'
            ]
            
            # 在 Windows 上使用隱藏窗口啟動 tunnel（後台運行）
            if platform.system() == 'Windows':
                tunnel_process = subprocess.Popen(
                    tunnel_cmd,
                    cwd=str(go_ios_dir),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
            else:
                tunnel_process = subprocess.Popen(
                    tunnel_cmd,
                    cwd=str(go_ios_dir),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            
            # 等待 tunnel 初始化
            print("⏳ 等待 tunnel 初始化...")
            time.sleep(5)
            
            # 3. 啟動 WDA
            print("🔹 啟動 WebDriverAgent...")
            wda_cmd = [
                str(ios_exe),
                'runwda',
                '--udid', udid,
                '--bundleid', bundle_id,
                '--testrunnerbundleid', testrunner_bundle_id,
                '--xctestconfig', xctest_config
            ]
            
            # 啟動 WDA（非阻塞，讓它在後台運行）
            if platform.system() == 'Windows':
                wda_process = subprocess.Popen(
                    wda_cmd,
                    cwd=str(go_ios_dir),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
            else:
                wda_process = subprocess.Popen(
                    wda_cmd,
                    cwd=str(go_ios_dir),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            
            # 等待 WDA 啟動
            print("⏳ 等待 WDA 啟動...")
            time.sleep(10)
            
            print("✅ WDA 啟動完成")
            print("=" * 60 + "\n")
            return True
            
        except Exception as e:
            print(f"❌ WDA 啟動失敗: {str(e)}")
            import traceback
            traceback.print_exc()
            print("\n請檢查：")
            print("1. 設備是否已通過 USB 連接")
            print("2. 設備是否已解鎖並信任電腦")
            print("3. WDA 是否已安裝在設備上")
            print("4. go-ios 工具是否可用（go-ios/ios.exe）")
            print("5. 設備 UDID 是否正確")
            print("=" * 60 + "\n")
            # 即使啟動失敗，也繼續執行測試（測試可能會自己啟動 WDA）
            return False