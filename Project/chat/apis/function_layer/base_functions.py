import os, sys, math, requests, json
from datetime import datetime, timezone, timedelta
from common.web.common_api import Common as Common_api
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class BaseFunction(Common_api):
    def do_web_login(self, nation, phone, psw, device_id, url):

        if phone == '' or psw == '' or url == '' or nation == '' or device_id == '':
            raise EOFError(f'登入資料不完整 手機號:{phone} 密碼:{psw} 網址:{url} 國碼:{nation} 裝置ID:{device_id}')
        
        payload = {
                "country": nation,
                "phone": phone,
                "password": psw,
                "device_id": device_id,
                "grant_type": "password",
               
            }

        url = "%sapi/v1/login" % url
        res = self.post(url, data=json.dumps(payload), header=self.header())
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, res.json()['result']['access_token']

    def do_app_login(self, nation, phone, psw, device_id, url):

        if phone == '' or psw == '' or url == '' or nation == '' or device_id == '':
            raise EOFError(f'登入資料不完整 手機號:{phone} 密碼:{psw} 網址:{url} 國碼:{nation} 裝置ID:{device_id}')
        
        payload = {
                "country": nation,
                "phone": phone,
                "password": psw,
                "device_id": device_id,
                "grant_type": "password"
            }

        url = "%sv1/login" % url 
        res = self.post(url, data=json.dumps(payload), header=self.header())

        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
        
        return res, res.json()['result']['access_token']
    
    def do_admin_login(self, account, password, url): 

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
                'password': password,
                'username': account
            }

        url = "%sv1/admin/login" % url
        res, session = self.post(url, data=json.dumps(payload), header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session

    def get_full_phone_number(self, nation, phone):
        if nation == 'CN':
            fullnumber = '86' + str(phone)
        elif nation == 'TW':
            fullnumber = '886' + str(phone)
        elif nation == 'JP':
            fullnumber = '81' + str(phone)

        return fullnumber
    
    def headers(self, token):
        header = {
            "Authorization": "Bearer %s" %token,
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json;charset=UTF-8",
        }

        return header