import os, sys
import common.utils.globalvar as gl

class DecorateClass:
    def __init__(self, testcase_key=None):
        self.testcase_key = testcase_key
        
    def __call__(self, f):
        def set_testcase_key(*args, **kargs):
            if self.testcase_key is not None:
                # HOLD 一開始是 None，第一次執行時也要視為「尚未設定」
                hold = gl.get_value('HOLD')
                if not hold:
                    gl.set_value('HOLD', self.testcase_key)
                    gl.set_value('TESTCASE_KEY', self.testcase_key)

                # 額外紀錄 unittest TestCase.id() 與 Jira testcase key 的對應關係，
                # 讓 retry 成功時可以找回正確的 Jira 測試案例來覆寫結果。
                try:
                    self_obj = args[0] if args else None
                    test_id = self_obj.id() if self_obj and hasattr(self_obj, 'id') else None
                    if test_id:
                        mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
                        mapping[test_id] = self.testcase_key
                        gl.set_value('TESTCASE_ID_MAP', mapping)
                except Exception:
                    pass

            result = f(*args, **kargs)
            return result
        return set_testcase_key
  