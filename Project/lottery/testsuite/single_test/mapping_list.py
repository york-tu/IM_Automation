# -*- coding: UTF-8 -*-
import pathlib
import sys
import os
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

from Project.lottery.web.testcases.web_testcases import WebTestCases, MobileWebCases
from Project.lottery.web.testcases.admin_testcases import AdminTestCases
from Project.lottery.web.testcases.reseller_testcases import ResellerTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_web_testcases import UiApiWebTestCases
from Project.lottery.apis.testcases.uiapi.uiapi_admin_testcases import UiApiAdminTestCases
from Project.lottery.web.testcases.nwap_testcases.nwap_testcases import MobileWebCases as MobileWebCases_nwap
from Project.mynah.testsuite.testcases.web_testcases import WebTestCases as WebTestCases_mynah
from Project.lottery.web.testcases.admin_testcases_wap import AdminTestCasesWap

class_list = ['WebTestCases', 'MobileWebCases', 'AdminTestCases', 
'ResellerTestCases', 'UiApiWebTestCases', 'UiApiAdminTestCases', 
 'MobileWebCases_nwap', 'AdminTestCasesWap', 'WebTestCases_mynah']

test_type = ['web', 'wap', 'admin', 'reseller', 'ui_web_api', 'ui_admin_api', 'nwap', 'nwap_admin' 'mynah']
f = open(f'{pathlib.Path(__file__).parent.absolute()}/testcase_list.txt','w')

for class_name, type_name in zip(class_list, test_type):
    title_name = f'----------------------------{type_name}-------------------------------\n'
    f.write(title_name)

    for key, value in (eval(class_name).__dict__).items():
        if str(value).__contains__('DecorateClass'):
            testcase_name = f'{class_name}("{key}")\n'
            f.write(testcase_name)

f.close()
