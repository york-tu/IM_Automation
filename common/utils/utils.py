import datetime, re, platform, os, sys, time, traceback, xmlrunner, atexit
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR_NAME)
import common.utils.globalvar as gl
from jira.jira_api import JiraApi
from common.utils.retry_runner import RetryXMLTestRunner
from configs.app.setting import Setting

_ORIG_STDOUT = None
_ORIG_STDERR = None
_OUTPUT_FILTER_INSTALLED = False


def install_pocoservice_output_filter():
    """安裝全域 stdout/stderr 過濾器（程式結束前不還原，以攔截 poco atexit 輸出）。"""
    global _ORIG_STDOUT, _ORIG_STDERR, _OUTPUT_FILTER_INSTALLED
    if _OUTPUT_FILTER_INSTALLED:
        return
    _ORIG_STDOUT = sys.stdout
    _ORIG_STDERR = sys.stderr
    sys.stdout = FilteredStream(_ORIG_STDOUT)
    sys.stderr = FilteredStream(_ORIG_STDERR)
    _OUTPUT_FILTER_INSTALLED = True
    atexit.register(_flush_output_filters)


def _flush_output_filters():
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, FilteredStream):
            stream.flush()


class FilteredStream(object):
    """包裝 stream，過濾 [pocoservice.apk] / INSTRUMENTATION_RESULT 重複訊息並移除空白行。"""

    def __init__(self, stream):
        self._stream = stream
        self._buffer = ''

    def _should_skip(self, line):
        if '[pocoservice.apk]' in line:
            return True
        if 'com.netease.open.pocoservice' in line:
            return True
        if 'INSTRUMENTATION_RESULT' in line or 'INSTRUMENTATION_CODE' in line:
            return True
        if 'Process crashed' in line:
            return True
        if 'still waiting for uiautomation ready' in line:
            return True
        if 'urllib3.connectionpool' in line and ('Retrying' in line or 'connection broken' in line):
            return True
        if 'NewConnectionError' in line or 'WinError 10061' in line:
            return True
        if not line.strip():
            return True
        return False

    def write(self, s):
        if not isinstance(s, str):
            s = str(s)
        self._buffer += s
        while '\n' in self._buffer or '\r' in self._buffer:
            idx = len(self._buffer)
            for sep in ('\r\n', '\n', '\r'):
                i = self._buffer.find(sep)
                if i != -1:
                    idx = min(idx, i)
            if idx == len(self._buffer):
                break
            sep = '\r\n' if self._buffer[idx:idx + 2] == '\r\n' else (self._buffer[idx] if idx < len(self._buffer) else '\n')
            line = self._buffer[:idx]
            self._buffer = self._buffer[idx + len(sep):]
            if not self._should_skip(line):
                self._stream.write(line + sep)

    def writeln(self, s=''):
        self.write(s + '\n')

    def flush(self):
        if self._buffer and not self._should_skip(self._buffer):
            self._stream.write(self._buffer)
        self._buffer = ''
        self._stream.flush()


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
        install_pocoservice_output_filter()
        runner = xmlrunner.XMLTestRunner(output=folderpath, verbosity=2)
        Utils.report = runner.run(suite)
        Utils.check_last_result(Utils)

    @staticmethod
    def send_slack_notification(result, folderpath, report_label=None, time_taken=None):
        """
        將測試結果摘要發送到 Slack。
        :param result: XMLTestRunner 的 result 物件（含 testsRun, failures, errors, skipped）
        :param folderpath: 報告目錄路徑
        :param report_label: 報告標籤，例如 'S1'、'S2'，會顯示在標題中
        :param time_taken: 總耗時（秒），若為 None 則不顯示
        """
        try:
            webhook_url = Setting.get_slack_webhook_url()
            if not webhook_url:
                return
            import requests
            env = gl.get_value('ENV', 'uat').upper()
            brand = gl.get_value('BRAND', 'gu').upper()
            test_type = gl.get_value('TEST_TYPE', 'app_ios')
            tt = test_type.lower() if test_type else ''
            if 'ios' in tt:
                platform_label = 'iOS'
            elif 'web2' in tt:
                platform_label = 'WEB2.0'
            elif 'web' in tt:
                platform_label = 'WEB'
            elif 'wap' in tt:
                platform_label = 'WAP'
            else:
                platform_label = 'Android'
            label_part = (' [%s]' % report_label) if report_label else ''
            passed = result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)
            failed = len(result.failures) + len(result.errors)
            is_ok = result.wasSuccessful()
            title = '%s [%s][%s][%s]%s Automation Regression Result' % (
                '✅' if is_ok else '❌', env, brand, platform_label, label_part
            )
            time_str = '%.2f min' % (time_taken / 60.0) if time_taken is not None else '-'
            report_path_display = folderpath.replace('\\', '/')
            def _short_name(full_name):
                """簡化為 ClassName.method_name"""
                if not full_name:
                    return full_name
                parts = full_name.split('.')
                if len(parts) >= 2:
                    return parts[-2] + '.' + parts[-1]
                return full_name

            failed_items = []
            for ti, _ in getattr(result, 'failures', []):
                name = getattr(ti, 'test_id', None) or getattr(ti, '_test_id', None) or str(ti)
                failed_items.append('%s (FAIL)' % _short_name(name))
            for ti, _ in getattr(result, 'errors', []):
                name = getattr(ti, 'test_id', None) or getattr(ti, '_test_id', None) or str(ti)
                failed_items.append('%s (ERROR)' % _short_name(name))
            failed_items = failed_items[:20]
            if (len(result.failures) + len(result.errors)) > 20:
                failed_items.append('... 還有更多失敗項目')
            app_version = gl.get_value('APP_VERSION', '-')
            blocks = [
                {"type": "header", "text": {"type": "plain_text", "text": title, "emoji": True}},
                {"type": "section", "text": {"type": "mrkdwn", "text": "*📊 測試統計*"}},
                {"type": "section", "fields": [
                    {"type": "mrkdwn", "text": "*🕐 總耗時*\n%s" % time_str},
                    {"type": "mrkdwn", "text": "*📋 總案例數*\n%d 條" % result.testsRun},
                    {"type": "mrkdwn", "text": "*✅ Pass*\n%d 條" % passed},
                    {"type": "mrkdwn", "text": "*❌ Fail*\n%d 條" % failed},
                    {"type": "mrkdwn", "text": "*⏭️ Skipped*\n%d 條" % len(result.skipped)},
                    {"type": "mrkdwn", "text": "*📦 版本號*\n%s" % app_version},
                ]},
                {"type": "section", "text": {"type": "mrkdwn", "text": "*📁 報告路徑*\n%s" % report_path_display}},
            ]
            if failed_items:
                blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": "*失敗項目*\n" + "\n".join(failed_items)}})
            payload = {"blocks": blocks}
            requests.post(webhook_url, json=payload, timeout=10)
        except Exception as e:
            print('Slack 通知發送失敗: %s' % e)

    @staticmethod
    def unittest_xml_with_retry_and_slack(suite, report_label=None, run_check_last_result=False,
                                          retry_groups=None):
        """
        執行測試（含失敗重試 1 次）、寫入 XML 報告，並將該段結果發送到 Slack。
        若 report_label 為 'S1'/'S2'，報告會寫入子目錄 S1/、S2/，且 Slack 標題會帶上標籤。
        :param suite: unittest.TestSuite
        :param report_label: 例如 'S1'、'S2'，用於子目錄與 Slack 標題
        :param run_check_last_result: 是否在本次跑完後呼叫 check_last_result（通常僅最後一段設 True）
        :param retry_groups: 群組重跑設定，例如：
            [
                ('test_add_redenvelope', 'test_check_red_envelope', 'test_grab_red_envelope'),
                ('add_auto_grad_red_envelope', 'test_auto_grab_red_envelope'),
            ]
            群組內任一條失敗時，retry 階段會把整組 case 從原 suite 撈出來依序一起重跑，
            適用於「依賴前一條後置條件」的測試（例：後台先建紅包 → 前台才能搶）。
        """
        gl.set_value('STATUS', ['amount', 'errors', 'failures', 'skipped'])
        gl.set_value('HOLD', '')
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        test_type = gl.get_value('TEST_TYPE')
        basename = os.path.basename(os.path.splitext(sys.argv[0])[0])
        if len(sys.argv) == 1:
            base_dir = os.path.dirname(os.path.abspath(__file__)) + "/../Test-Reports/" + test_type + "/" + env + "/" + brand + "/" + basename + "/"
        else:
            base_dir = os.getcwd() + "/" + 'Test-Reports' + "/" + "Jenkins" + "/" + test_type + "/" + env + "/" + brand + "/" + basename + "/"
        ts = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        if report_label:
            existing_base = gl.get_value('REPORT_BASE_PATH')
            if existing_base:
                base_with_ts = existing_base
            else:
                base_with_ts = base_dir + ts + "/"
                gl.set_value('REPORT_BASE_PATH', base_with_ts)
            folderpath = base_with_ts + report_label + "/"
        else:
            folderpath = base_dir + ts + "/"
        gl.set_value('FOLDER_PATH', folderpath)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        print(folderpath)
        install_pocoservice_output_filter()
        runner = RetryXMLTestRunner(output=folderpath, verbosity=2, max_retries=1, retry_delay=5,
                                    retry_groups=retry_groups, stream=sys.stderr)
        start_time = time.time()
        try:
            Utils.report = runner.run(suite)
        finally:
            _flush_output_filters()
        time_taken = time.time() - start_time
        Utils.send_slack_notification(Utils.report, folderpath, report_label=report_label, time_taken=time_taken)
        if run_check_last_result:
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

        testcase_key = gl.get_value('TESTCASE_KEY')
        if not testcase_key or not isinstance(testcase_key, (list, tuple)) or len(testcase_key) == 0:
            return
        cycle_key = gl.get_value('CYCLE_KEY')
        if not cycle_key:
            return

        certification = JiraApi().jira_login()  # jira登入
        resultcount = gl.get_value('RESULT_COUNT')
        orange_result = re.findall("[0-9]+", str(gl.get_value('RESULT')))
        finally_result = re.findall("[0-9]+", str(self.report))

        # 使用最後一筆 key（剛跑完的 suite 的最後一個案例），S1+S2 分段跑時 S2 才會回填到正確的 Jira
        key = testcase_key[-1]
        if finally_result != orange_result or finally_result[0] == finally_result[1] or resultcount[1:] != finally_result[1:]:
            result = gl.get_value('RESULT')
            if resultcount[1] != finally_result[1]:
                gl.set_value('ERROR', result.errors)
            else:
                gl.set_value('FAILURE', result.failures)
            JiraApi().set_cycle_result(certification, cycle_key, key, 'fail')
        else:
            JiraApi().set_cycle_result(certification, cycle_key, key, 'pass')

    @staticmethod
    def _outcome_error_for_test_case(test_case):
        """Python 3 unittest 在 tearDown 之後才呼叫 _feedErrorsToResult，tearDown 內讀 result 尚無本條錯誤。"""
        outcome = getattr(test_case, '_outcome', None)
        if not outcome or not getattr(outcome, 'errors', None):
            return None, None
        failure_exc = getattr(test_case, 'failureException', AssertionError)
        for err_test, exc_info in outcome.errors:
            if exc_info is None:
                continue
            if err_test is not test_case and getattr(err_test, 'test_case', None) is not test_case:
                continue
            tb_str = ''.join(traceback.format_exception(*exc_info))
            if issubclass(exc_info[0], failure_exc):
                return 'failure', tb_str
            return 'error', tb_str
        return None, None

    # 檢查這次測試案例的結果
    def check_test_result(self, id, key, result, test_case=None):
        if gl.get_value('PUSH') != True:
            return

        cycle_key = gl.get_value('CYCLE_KEY')
        if not cycle_key:
            return

        # key 可能是單一字串，也可能是 list/tuple（舊邏輯殘留）
        if isinstance(key, (list, tuple)):
            testcase_key = key[-1] if len(key) > 0 else None
        else:
            testcase_key = key

        # 某些執行環境（例如 __main__）test_id 前綴可能不同，補一層 mapping fallback（尾碼/方法名比對）
        if not testcase_key:
            mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
            test_id = str(id)
            testcase_key = mapping.get(test_id)
            if not testcase_key and test_id:
                method_name = test_id.split('.')[-1]
                for mapped_test_id, mapped_key in mapping.items():
                    if mapped_test_id.endswith(test_id) or test_id.endswith(mapped_test_id):
                        testcase_key = mapped_key
                        break
                    if mapped_test_id.split('.')[-1] == method_name:
                        testcase_key = mapped_key
                        break
            if not testcase_key:
                testcase_key = gl.get_value('TESTCASE_KEY') or gl.get_value('HOLD')

        if not testcase_key:
            return

        # 先刷新總體統計（供報告/其他流程使用）
        self.total(result)
        test_id = str(id)

        # 直接以「當前 test_id 是否出現在 result 對應清單」判斷狀態，避免前後案例互相污染
        status = 'pass'
        kind, tb_str = (None, None)
        if test_case is not None:
            kind, tb_str = self._outcome_error_for_test_case(test_case)
        if kind == 'error':
            status = 'fail'
            gl.set_value('ERROR', [(None, tb_str)])
        elif kind == 'failure':
            status = 'fail'
            gl.set_value('FAILURE', [(None, tb_str)])
        if status == 'pass':
            for ti, _ in getattr(result, 'errors', []):
                if getattr(ti, 'test_id', None) == test_id:
                    status = 'fail'
                    gl.set_value('ERROR', [(ti, _)])
                    break
        if status == 'pass':
            for ti, _ in getattr(result, 'failures', []):
                if getattr(ti, 'test_id', None) == test_id:
                    status = 'fail'
                    gl.set_value('FAILURE', [(ti, _)])
                    break
        if status == 'pass':
            for skipped_item in getattr(result, 'skipped', []):
                try:
                    skipped_test = skipped_item[0]
                    if hasattr(skipped_test, 'id') and skipped_test.id() == test_id:
                        status = 'skip'
                        break
                except Exception:
                    pass

        certification = JiraApi().jira_login()  # jira登入
        JiraApi().set_cycle_result(certification, cycle_key, testcase_key, status)

        # 清理，避免下一條 case 共用到前一條的失敗訊息
        gl.set_value('ERROR', [])
        gl.set_value('FAILURE', [])

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
        import tempfile
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
            
            # WDA Bundle ID（可在 phone_config.yml 以 wda_bundle_id 覆寫）
            default_wda_bundle = 'com.vl.facebook.WebDriverAgentRunner.xctrunner'
            bundle_id = device_config.get('wda_bundle_id') or default_wda_bundle
            testrunner_bundle_id = device_config.get('wda_testrunner_bundle_id') or bundle_id
            xctest_config = device_config.get('wda_xctest_config') or 'WebDriverAgentRunner.xctest'
            print(f"📦 WDA Bundle: {bundle_id}")

            from driver.app_driver import (
                ensure_ios_tunnel,
                wait_for_ios_wda_ready,
                print_go_ios_failure_logs,
                go_ios_env,
                _go_ios_popen_kwargs,
            )

            go_ios_env = go_ios_env()
            popen_kwargs = _go_ios_popen_kwargs(go_ios_dir, go_ios_env)

            # 1. 確保 tunnel 就緒（僵死 agent / 60105 衝突會在 ensure 內自動處理）
            if not ensure_ios_tunnel(ios_exe, udid, go_ios_dir, go_ios_env, force_restart=False):
                gl.set_value('WDA_START_FAILED', True)
                print("=" * 60 + "\n")
                return False

            # 2. 啟動 WDA（runwda 為長駐程序；勿用 PIPE）
            wda_proc = gl.get_value('WDA_RUN_PROCESS')
            if wda_proc is not None and wda_proc.poll() is None:
                print('🔹 沿用執行中的 runwda 進程')
            else:
                print("🔹 啟動 WebDriverAgent (runwda)...")
                log_fd, log_path = tempfile.mkstemp(suffix='.log', prefix='goios_runwda_')
                os.close(log_fd)
                gl.set_value('WDA_RUN_LOG_PATH', log_path)
                wda_cmd = [
                    str(ios_exe),
                    'runwda',
                    '--udid', udid,
                    '--bundleid', bundle_id,
                    '--testrunnerbundleid', testrunner_bundle_id,
                    '--xctestconfig', xctest_config,
                    '--log-output', log_path,
                ]
                wda_log_f = open(log_path, 'a', encoding='utf-8')
                wda_process = subprocess.Popen(
                    wda_cmd,
                    stdout=wda_log_f,
                    stderr=subprocess.STDOUT,
                    **popen_kwargs,
                )
                gl.set_value('WDA_RUN_PROCESS', wda_process)
                gl.set_value('WDA_PROCESS_PID', wda_process.pid)
                time.sleep(3)
                if wda_process.poll() is not None:
                    print(f'❌ runwda 立即退出 (exit={wda_process.returncode})')
                    print_go_ios_failure_logs()
                    gl.set_value('WDA_START_FAILED', True)
                    print("=" * 60 + "\n")
                    return False

            wda_process = gl.get_value('WDA_RUN_PROCESS')

            # 3. 等待 WDA HTTP 就緒
            print("⏳ 等待 WDA 啟動並探活...")
            if wait_for_ios_wda_ready(timeout=120, interval=2, wda_process=wda_process):
                print("✅ WDA 啟動完成")
                print("=" * 60 + "\n")
                return True

            print("❌ WDA 啟動逾時，port:8100 未就緒")
            print_go_ios_failure_logs()
            gl.set_value('WDA_START_FAILED', True)
            print("=" * 60 + "\n")
            return False
            
        except Exception as e:
            print(f"❌ WDA 啟動失敗: {str(e)}")
            gl.set_value('WDA_START_FAILED', True)
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