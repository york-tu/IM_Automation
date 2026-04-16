import os, sys
import common.utils.globalvar as gl

class DecorateClass:
    def __init__(self, testcase_key=None):
        self.testcase_key = testcase_key
        
    def __call__(self, f):
        def set_testcase_key(*args, **kargs):
            if self.testcase_key is not None:
                self_obj = args[0] if args else None
                test_id = self_obj.id() if self_obj and hasattr(self_obj, 'id') else None
                current_method = test_id.split('.')[-1] if test_id else None

                # 只有 unittest 當前正在執行的方法，才更新 testcase key / mapping。
                # 避免在某個 case 內呼叫其他 test_xxx helper 時覆蓋 key。
                if current_method == f.__name__:
                    hold = gl.get_value('HOLD')
                    if not hold:
                        gl.set_value('HOLD', self.testcase_key)
                        gl.set_value('TESTCASE_KEY', self.testcase_key)

                # 紀錄 TestCase.id() -> Jira testcase key，供 check_result/retry 精準回填。
                try:
                    if test_id and current_method == f.__name__:
                        mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
                        mapping[test_id] = self.testcase_key
                        gl.set_value('TESTCASE_ID_MAP', mapping)
                except Exception:
                    pass

            result = f(*args, **kargs)
            return result
        return set_testcase_key
  