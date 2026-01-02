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