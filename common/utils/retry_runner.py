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

    def startTest(self, test):
        """
        讓「<test desc> ...」在案例一開始就即時顯示，而不是等到結束才輸出。
        """
        super().startTest(test)
        try:
            self.stream.flush()
        except Exception:
            pass

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
    """
    全部跑完一輪後，fail/error 的 case 各重試 1 次。

    支援「群組重跑」(retry_groups)：
    - retry_groups 為一組「測試方法名稱清單」的集合，例如：
        retry_groups=[
            ('test_add_redenvelope', 'test_check_red_envelope', 'test_grab_red_envelope'),
            ('add_auto_grad_red_envelope', 'test_auto_grab_red_envelope'),
        ]
    - 若群組內任何一條失敗，retry 階段會把整組從原 suite 撈出來「依序」一起跑，
      避免「依賴前一條的後置條件」(例: 後台先建紅包 → 前台才能搶) 的 case
      被單獨重跑時必定再次失敗。
    - 群組內原本就 pass 的 case，重跑後若仍 pass，不會影響原報告；
      若群組內原本失敗的 case 重跑後 pass，會把它從 failures/errors 移除並回填 Jira pass。
    """

    def __init__(self, max_retries=1, retry_delay=5, retry_groups=None, **kwargs):
        kwargs.pop('resultclass', None)
        super().__init__(resultclass=_RetryableXMLTestResult, **kwargs)
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        # retry_groups: list[tuple[str, ...]]，每個 tuple 為一個群組的方法名稱
        self.retry_groups = [tuple(g) for g in (retry_groups or []) if g]

    @staticmethod
    def _method_name(test_obj):
        """從 TestCase 取得方法名稱 (test.id() 的最後一段)。"""
        try:
            return test_obj.id().split('.')[-1]
        except Exception:
            return ''

    def _find_group_for(self, method_name):
        for grp in self.retry_groups:
            if method_name in grp:
                return grp
        return None

    @staticmethod
    def _walk_suite(suite):
        """遞迴列出 TestSuite 內所有 TestCase 實例。"""
        for t in suite:
            if isinstance(t, unittest.TestSuite):
                yield from RetryXMLTestRunner._walk_suite(t)
            else:
                yield t

    @staticmethod
    def _reset_class_state(cls):
        """重設 driver_list / function_dict 內的 web driver 引用，避免 setUpClass 重複疊加。"""
        if hasattr(cls, 'driver_list'):
            cls.driver_list = []
        if hasattr(cls, 'function_dict') and isinstance(getattr(cls, 'function_dict', None), dict):
            cls.function_dict.pop('wp', None)
            cls.function_dict.pop('wap', None)
            cls.function_dict.pop('ad', None)

    @staticmethod
    def _safe_teardown_class(cls):
        if hasattr(cls, 'tearDownClass'):
            try:
                cls.tearDownClass()
            except Exception:
                pass

    @staticmethod
    def _safe_setup_class(cls):
        if hasattr(cls, 'setUpClass'):
            try:
                cls.setUpClass()
            except Exception:
                pass

    @staticmethod
    def _push_jira_pass(test_id):
        """重跑成功時把 Jira cycle 結果回填為 pass。"""
        try:
            if not gl.get_value('PUSH'):
                return
            cycle_key = gl.get_value('CYCLE_KEY')
            if not cycle_key:
                return
            mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
            testcase_key = mapping.get(test_id, None)
            if not testcase_key:
                testcase_key = gl.get_value('TESTCASE_KEY')
            if testcase_key:
                certification = JiraApi().jira_login()
                JiraApi().set_cycle_result(certification, cycle_key, testcase_key, 'pass')
        except Exception:
            # Jira 更新失敗不影響測試流程
            pass

    def _retry_members(self, result, members):
        """
        members: list[(test_obj, kind_or_none)]
            kind: 'failure' / 'error' / None  (None 表示原本通過、僅因群組依賴被一起重跑)
        每組共用一次 tearDownClass + setUpClass (依群組內出現的不同 class 各執行一次)。
        """
        if not members:
            return

        # 群組內可能含多種 class (例如 AdminTestCase + WebTestCase)，先針對每個 class 重置一次
        unique_classes = []
        for test_obj, _ in members:
            cls = test_obj.__class__
            if cls not in unique_classes:
                unique_classes.append(cls)

        for cls in unique_classes:
            self._safe_teardown_class(cls)
            self._reset_class_state(cls)
            self._safe_setup_class(cls)

        try:
            for test_obj, kind in members:
                result.start_time = time.time()
                temp = unittest.TestResult()
                test_obj.run(temp)
                result.stop_time = time.time()

                # 過濾重跑階段的 stdout 雜訊
                if temp.failures or temp.errors:
                    for test_info, _ in temp.failures + temp.errors:
                        for attr_name in ('stdout', 'output', '_stdout', '_output'):
                            if hasattr(test_info, attr_name):
                                val = getattr(test_info, attr_name)
                                if val and isinstance(val, str):
                                    setattr(test_info, attr_name, _filter_output(val))

                # 只有「原本失敗、重跑成功」才需要回填 result + Jira
                if kind in ('failure', 'error') and not temp.failures and not temp.errors:
                    test_info = result.infoclass(result, test_obj, result.infoclass.SUCCESS)
                    test_info.test_finished()
                    result.successes.append(test_info)
                    tid = test_obj.id()
                    if kind == 'failure':
                        result.failures = [(ti, tb) for (ti, tb) in result.failures if ti.test_id != tid]
                    else:
                        result.errors = [(ti, tb) for (ti, tb) in result.errors if ti.test_id != tid]
                    self._push_jira_pass(tid)
        finally:
            # 重跑結束：強制 tearDown 並清掉 driver/session 殘留
            for cls in unique_classes:
                self._safe_teardown_class(cls)
                self._reset_class_state(cls)

    def run(self, test):
        try:
            # 走訪原始 suite，建立「方法名 → TestCase 實例」對照表，群組重跑時要從這裡撈出
            # 全部成員（包含原本 pass 的條目，因為依賴序列要從頭跑）。
            name_to_test = {}
            for tc in self._walk_suite(test):
                m = self._method_name(tc)
                if m and m not in name_to_test:
                    name_to_test[m] = tc

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
            retry_list = list(getattr(result, '_retry_list', []))

            # 把 _retry_list 攤成「重跑單元」(retry_units)：
            #   - 'single': 單條 retry (test_obj, kind)
            #   - 'group':  群組 retry，內含群組所有成員 (依原 suite 順序)
            retry_units = []
            processed_methods = set()
            # 先建一份 method -> (failed kind) 的對照，方便群組內判斷哪些原本是失敗
            failed_kinds = {}
            for fo, _e, k in retry_list:
                failed_kinds[self._method_name(fo)] = k

            for test_obj, _err, kind in retry_list:
                method_name = self._method_name(test_obj)
                if method_name in processed_methods:
                    continue
                grp = self._find_group_for(method_name)
                if grp:
                    members = []
                    for m in grp:
                        if m in name_to_test:
                            members.append((name_to_test[m], failed_kinds.get(m)))
                            processed_methods.add(m)
                    if members:
                        retry_units.append(('group', members))
                else:
                    retry_units.append(('single', test_obj, kind))
                    processed_methods.add(method_name)

            for idx, unit in enumerate(retry_units):
                if idx > 0:
                    self.stream.writeln()

                if unit[0] == 'single':
                    _, test_obj, kind = unit
                    if delay > 0:
                        self.stream.writeln("  [Retry] 等待 %ds 後重試 %s ..." % (delay, test_obj.id()))
                        self.stream.flush()
                        time.sleep(delay)
                    self._retry_members(result, [(test_obj, kind)])
                else:
                    _, members = unit
                    desc = ' / '.join(self._method_name(t) for t, _ in members)
                    if delay > 0:
                        self.stream.writeln("  [Retry-Group] 等待 %ds 後整組重跑：%s ..." % (delay, desc))
                        self.stream.flush()
                        time.sleep(delay)
                    self._retry_members(result, members)

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
