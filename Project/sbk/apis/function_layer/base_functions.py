import os, sys, math, requests, json
from datetime import datetime, timezone, timedelta
from common.web.common_api import Common as Common_api
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class BaseFunction(Common_api):

    def do_wap_login(self,divice_token ,account, url):

        if account == '' or divice_token == '' or url == '':
            raise EOFError(f'登入資料不完整 商戶:{divice_token} 帳號:{account} 網址:{url}')
        
        payload = json.dumps({
                'account': account,
                "langCode":"zh-CN"
            })
        header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {divice_token}' 
        }

        url = f'{url}/partner-api/player-game-urls' # 由於現在位置變成/apis/m/session,導致我們必須先切開
        res, session = self.post(url, data=payload, header=header, get_login = True)
        assert res.status_code == 201 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
        token = res.json()['data'][41:]
        return token, session
    
    # def do_admin_(self, account, password, admin_otp, url):

    #     if account == '' or password == '' or url == '':
    #         raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
    #     payload = {
    #             'login': account,
    #             'passwd': password,
    #             'otp':admin_otp
    #         }

    #     url = "%sapis/session" % url
    #     res, session = self.post(url, data=payload, header=self.header(), get_login = True)
    #     assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

    #     return res, session

    # def do_cm_login(self, account, password):
    #     url = 'http://uat.cmapi.pstdsf.com:10080/v1/token'

    #     payload = {
    #         'grant_type': 'password',
    #         'username': account,
    #         'password': password,
    #     }

    #     res = self.post(url, data=payload, header=self.header())
    #     assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

    #     return res, res.json()['access_token']

