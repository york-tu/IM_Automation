import os, sys, unittest
import common.utils.globalvar as gl
from common.utils.utils import Utils

class UnittestModule(unittest.TestCase):
    #紀錄測試結果並且上傳
    def check_result(self, testcase_id):
        utils = Utils()
        gl.set_value('HOLD', '')
        # 優先用完整 test_id 對應 DecorateClass 紀錄的 Jira key，避免使用全域 TESTCASE_KEY 造成錯位回填
        full_test_id = self.id() if hasattr(self, 'id') else ''
        mapping = gl.get_value('TESTCASE_ID_MAP', {}) or {}
        testcase_key = mapping.get(full_test_id, gl.get_value('TESTCASE_KEY'))
        utils.check_test_result(
            full_test_id or testcase_id, testcase_key, gl.get_value('RESULT'), test_case=self
        )

    