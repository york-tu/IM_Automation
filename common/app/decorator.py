import os, sys
import common.utils.globalvar as gl

class DecorateClass:
    def __init__(self, testcase_key=None):
        self.testcase_key = testcase_key
        
    def __call__(self, f):
        def set_testcase_key(*args, **kargs):
            if self.testcase_key != None:
                if gl.get_value('HOLD') == '':
                    gl.set_value('HOLD', self.testcase_key)
                    gl.set_value('TESTCASE_KEY', self.testcase_key)

            result = f(*args, **kargs)
            return result
        return set_testcase_key
  