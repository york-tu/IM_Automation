import os, sys, unittest
import common.utils.globalvar as gl
from common.utils.utils import Utils

class UnittestModule(unittest.TestCase):
    #紀錄測試結果並且上傳
    def check_result(self, testcase_id):
        utils = Utils()
        gl.set_value('HOLD', '')
        testcase_key = gl.get_value('TESTCASE_KEY')
        utils.check_test_result(testcase_id, testcase_key, gl.get_value('RESULT'))

    