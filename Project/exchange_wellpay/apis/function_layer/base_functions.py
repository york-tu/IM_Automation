import os
import sys
import requests
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)
from common.web.common_api import Common as Common_api

class BaseFunction(Common_api):
    def headers(self):
        headers = {
            'x-requested-with': "XMLHttpRequest",
        }
        return headers

    def do_login(self, account, password, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
            'login': account,
            'passwd': password,
            'otp': "1",
        }

        url = "%sapis/session" % url
        res, session = self.post(url, data=payload, header=self.header(), get_login=True)
        assert res.status_code == 204, f'api狀態碼不正確: {res.status_code}'

        return res, session