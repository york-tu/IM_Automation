import os, sys, math, requests, json
from datetime import datetime, timezone, timedelta
from common.web.common_api import Common as Common_api
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class BaseFunction(Common_api):
    def do_web_login(self, account, password, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
                'login': account,
                'passwd': password,
            }

        url = "%sapis/session" % url
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session

    def do_wap_login(self, account, password, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
                'login': account,
                'passwd': password,
            }

        url = f'{url[:-2]}apis/{url[-2:]}session' # 由於現在位置變成/apis/m/session,導致我們必須先切開
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session
    
    def do_admin_login(self, account, password, admin_otp, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
                'login': account,
                'passwd': password,
                'otp':admin_otp
            }

        url = "%sapis/session" % url
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session

    def do_cm_login(self, account, password):
        url = 'http://uat.cmapi.pstdsf.com:10080/v1/token'

        payload = {
            'grant_type': 'password',
            'username': account,
            'password': password,
        }

        res = self.post(url, data=payload, header=self.header())
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, res.json()['access_token']

    def do_reseller_login(self, account, password, reseller_otp, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
            'login': account,
            'passwd': password,
            'securitycode': reseller_otp,
        }

        url = "%sapis/session" % url
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session
        
    def do_dwh_login(self, account, password, url):

        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload = {
                'login': account,
                'passwd': password,
            }

        url = "%sapi/v1/admin/session" % url
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session
    
    def do_mynah_login(self, account, password, url):

        # mynah的domain已經更換_113行, 此步驟仍先不修改, 待之後穩定後修改config or 這段code
        if account == '' or password == '' or url == '':
            raise EOFError(f'登入資料不完整 帳號:{account} 密碼:{password} 網址:{url}')
        
        payload_data = {
            "grant_type":"password",
            "username":f"{account}",
            "password":f"{password}"
            }
        # 需要轉raw且要使用雙引號
        payload = r'{0}'.format(payload_data).replace("'",'"').encode()

        # url = "%s/peacock/v1/oauth2/token" % url
        url = "https://mynah-uat.paradise-soft.com.tw/peacock/v1/oauth2/token"
        res, session = self.post(url, data=payload, header=self.header(), get_login = True)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res, session

    def balance(self, certification, url):
        now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)
        header = ''

        request_url = f'{url}apis/my/wallet/balance?forcerefresh=1&_={now_timestamp}'
        res = self.get(request_url, certification=certification, header=header)
 
        return res

    def total_amount(self, certification, url):
        now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)
        header = ''

        request_url = f'{url}apis/my/wallet/balance?forcerefresh=1&_={now_timestamp}'
        res = self.get(request_url, certification=certification, header=header)

        balance = (res.text)[1:-2].split(',{', 1)[0]
        money = json.loads(balance)
 
        return float(money['balance'])

    def total_amount(self, certification, url):
        now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)
        header = ''

        request_url = f'{url}apis/my/wallet/balance?forcerefresh=1&_={now_timestamp}'
        res = self.get(request_url, certification=certification, header=header)

        balance = (res.text)[1:-2].split(',{', 1)[0]
        money = json.loads(balance)
 
        return float(money['balance'])

    def total_amount(self, certification, url):
        now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)
        header = ''

        request_url = f'{url}apis/my/wallet/balance?forcerefresh=1&_={now_timestamp}'
        res = self.get(request_url, certification=certification, header=header)

        balance = (res.text)[1:-2].split(',{', 1)[0]
        money = json.loads(balance)
 
        return float(money['balance'])