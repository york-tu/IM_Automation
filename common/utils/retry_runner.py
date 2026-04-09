# -*- coding: utf-8 -*-
"""
全部跑完一輪後，fail 的 case 重跑 1 次，重跑完就結束。
xmlrunner 的 result.failures/errors 存的是 (_TestInfo, tb)，重試時用實際的 TestCase 來跑。
"""
import unittest
import time
import re
from xmlrunner import XMLTestRunner
from xmlrunner.result import _XMLTestResult
import common.utils.globalvar as gl
from jira.jira_api import JiraApi


def _filter_output(output):
    """過濾重複的 pocoservice 訊息和空白行"""
    if not output:
        return output
    lines = output.split('\n')
    filtered_lines = []
    seen = set()
    for line in lines:
        if not line.strip():
            continue
        if '[pocoservice.apk]' in line:
            continue
        if 'INSTRUMENTATION_RESULT' in line and 'pocoservice' in line.lower():
            continue
        if 'Process crashed' in line and 'pocoservice' in line.lower():
            continue
        normalized = re.sub(r'\s+', ' ', line.strip())
        if normalized in seen:
            continue
        seen.add(normalized)
        filtered_lines.append(line)
    return '\n'.join(filtered_lines)


class _RetryableXMLTestResult(_XMLTestResult):
    """在 addFailure/addError 時額外記錄 (test, err, kind)，供 Retry 使用。"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._retry_list = []  # [(test, err, 'failure'|'error'), ...]

    def addFailure(self, test, err):
        self._retry_list.append((test, err, 'failure'))
        super().addFailure(test, err)

    def addError(self, test, err):
        self._retry_list.append((test, err, 'error'))
        super().addError(test, err)

    def _filter_test_outputs(self):
        """過濾所有測試的 stdout/stderr 輸出"""
        for test_info, _ in self.failures + self.errors:
            for attr_name in ('stdout', 'output', '_stdout', '_output'):
                if hasattr(test_info, attr_name):
                    val = getattr(test_info, attr_name)
                    if val:
                        if isinstance(val, str):
                            setattr(test_info, attr_name, _filter_output(val))
                        elif isinstance(val, bytes):
                            setattr(test_info, attr_name, _filter_output(val.decode('utf-8', errors='ignore')).encode('utf-8', errors='ignore'))

    def generate_reports(self, runner):
        self._filter_test_outputs()
        super().generate_reports(runner)


class RetryXMLTestRunner(XMLTestRunner):
    """全部跑完一輪後，fail/error 的 case 各重試 1 次。"""

    def __init__(self, max_retries=1, retry_delay=5, **kwargs):
        kwargs.pop('resultclass', None)
        super().__init__(resultclass=_RetryableXMLTestResult, **kwargs)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def run(self, test):
        try:
            result = self._make_result()
            result.failfast = self.failfast
            if hasattr(test, 'properties'):
                result.properties = test.properties

            self.stream.writeln()
            self.stream.writeln('Running tests...')
            self.stream.writeln(result.separator2)

            start_time = time.time()
            test(result)

            # 若 setUpClass 失敗，unittest 可能會導致 testsRun = 0。
            # 這種情況代表 regression 根本沒跑到任何案例，必須直接視為失敗，避免 Jenkins 誤判 SUCCESS。
            if getattr(result, 'testsRun', 0) == 0:
                self.stream.writeln("ERROR: Ran 0 tests. setUpClass may have failed; aborting.")
                # 盡可能把 setUpClass 相關錯誤印出來，方便在 Jenkins console 直接定位根因
                try:
                    if getattr(result, 'errors', None):
                        self.stream.writeln("---- errors ----")
                        for ti, tb in result.errors:
                            self.stream.writeln(str(ti))
                            self.stream.writeln(str(tb))
                    if getattr(result, 'failures', None):
                        self.stream.writeln("---- failures ----")
                        for ti, tb in result.failures:
                            self.stream.writeln(str(ti))
                            self.stream.writeln(str(tb))
                except Exception as _e:
                    self.stream.writeln(f"[WARN] Failed to dump errors for 0 tests: {_e}")
                raise RuntimeError("Ran 0 tests (setUpClass failure or test discovery issue)")

            delay = getattr(self, 'retry_delay', 5)
            for idx, (test_obj, _err, kind) in enumerate(list(getattr(result, '_retry_list', []))):
                if idx > 0:
                    self.stream.writeln()
                if delay > 0:
                    self.stream.writeln("  [Retry] 等待 %ds 後重試 %s ..." % (delay, test_obj.id()))
                    self.stream.flush()
                    time.sleep(delay)

                # 重試前先 tearDownClass 再 setUpClass，取得新的 driver/session，避免沿用已斷線的 session
                cls = test_obj.__class__
                if hasattr(cls, 'tearDownClass'):
                    try:
                        # tearDownClass 是 @classmethod，呼叫時不需要手動傳 cls
                        cls.tearDownClass()
                    except Exception:
                        pass
                # 強制清空 driver_list，避免 setUpClass 的 setting_browser 對已關閉的 list 做 append 造成重複
                if hasattr(cls, 'driver_list'):
                    cls.driver_list = []
                if hasattr(cls, 'function_dict') and isinstance(getattr(cls, 'function_dict', None), dict):
                    # 移除 web driver 引用，讓 setUpClass 重新建立
                    cls.function_dict.pop('wp', None)
                    cls.function_dict.pop('wap', None)
                    cls.function_dict.pop('ad', None)
                if hasattr(cls, 'setUpClass'):
                    try:
                        # setUpClass 是 @classmethod，呼叫時不需要手動傳 cls
                        cls.setUpClass()
                    except Exception:
                        pass

                result.start_time = time.time()
                temp = unittest.TestResult()
                try:
                    test_obj.run(temp)
                finally:
                    # 重跑結束（不論成功/失敗）都強制關閉瀏覽器，避免 retry 仍失敗時留下殘留 Chrome
                    try:
                        if hasattr(cls, 'tearDownClass'):
                            cls.tearDownClass()
                    except Exception:
                        pass
                    try:
                        if hasattr(cls, 'driver_list'):
                            cls.driver_list = []
                        if hasattr(cls, 'function_dict') and isinstance(getattr(cls, 'function_dict', None), dict):
                            cls.function_dict.pop('wp', None)
                            cls.function_dict.pop('wap', None)
                            cls.function_dict.pop('ad', None)
                    except Exception:
                        pass
                result.stop_time = time.time()

                if temp.failures or temp.errors:
                    for test_info, _ in temp.failures + temp.errors:
                        for attr_name in ('stdout', 'output', '_stdout', '_output'):
                            if hasattr(test_info, attr_name):
                                val = getattr(test_info, attr_name)
                                if val and isinstance(val, str):
                                    setattr(test_info, attr_name, _filter_output(val))

                if not temp.failures and not temp.errors:
                    test_info = result.infoclass(result, test_obj, result.infoclass.SUCCESS)
                    test_info.test_finished()
                    result.successes.append(test_info)
                    tid = test_obj.id()
                    if kind == 'failure':
                        result.failures = [(ti, tb) for (ti, tb) in result.failures if ti.test_id != tid]
                    else:
                        result.errors = [(ti, tb) for (ti, tb) in result.errors if ti.test_id != tid]

                    # 如果原本這個案例曾經失敗，但重試成功，則再把 Jira 結果覆寫為 pass
                    try:
                        if gl.get_value('PUSH'):
                            cycle_key = gl.get_value('CYCLE_KEY')
                            if cycle_key:
                                # 優先使用 DecorateClass 紀錄的「test_id -> testcase_key」對應
                                mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
                                testcase_key = mapping.get(tid, None)
                                # 若 mapping 中沒有，再退回全域 TESTCASE_KEY（維持舊行為）
                                if not testcase_key:
                                    testcase_key = gl.get_value('TESTCASE_KEY')
                                if testcase_key:
                                    certification = JiraApi().jira_login()
                                    JiraApi().set_cycle_result(certification, cycle_key, testcase_key, 'pass')
                    except Exception:
                        # Jira 更新失敗不影響測試流程
                        pass

            stop_time = time.time()
            time_taken = stop_time - start_time

            result.printErrors()
            self.stream.writeln(result.separator2)
            run = result.testsRun
            self.stream.writeln("Ran %d test%s in %.3fs" % (run, run != 1 and "s" or "", time_taken))
            self.stream.writeln()

            expectedFails = len(result.expectedFailures)
            unexpectedSuccesses = len(result.unexpectedSuccesses)
            skipped = len(result.skipped)
            infos = []
            if not result.wasSuccessful():
                self.stream.write("FAILED")
                failed, errored = map(len, (result.failures, result.errors))
                if failed:
                    infos.append("failures={0}".format(failed))
                if errored:
                    infos.append("errors={0}".format(errored))
            else:
                self.stream.write("OK")
            if skipped:
                infos.append("skipped={0}".format(skipped))
            if expectedFails:
                infos.append("expected failures={0}".format(expectedFails))
            if unexpectedSuccesses:
                infos.append("unexpected successes={0}".format(unexpectedSuccesses))
            if infos:
                self.stream.writeln(" ({0})".format(", ".join(infos)))
            else:
                self.stream.write("\n")

            self.stream.writeln()
            self.stream.writeln('Generating XML reports...')
            result.generate_reports(self)
        finally:
            pass
        return result
