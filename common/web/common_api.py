import requests, time, websocket, datetime
from opencc import OpenCC

class Common():
    timeout = 60
    license = ''
    
    def __init__(self, test_skip_method=''):
        self.test_skip_method = test_skip_method

    def session(self):
        self.license = requests.session()

        return self.license

    def header(self):
        header = {
            'X-Requested-With': "XMLHttpRequest",
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }

        return header

    def get(self, url, querystring='', certification='', header=''):
        if header == '':
            header = self.header()
        
        if certification == '':
            response = self.session().request("GET", url, headers=header, params=querystring, timeout=self.timeout)
        else:
            response = certification.request("GET", url, headers=header, params=querystring, timeout=self.timeout)
            
        return response

    def put(self, url, data='', certification='', header=''):
        if header == '':
            header = self.header()

        if certification == '':
            response = self.session().request("PUT", url, headers=header, data=data, timeout=self.timeout)
        else:
            response = certification.request("PUT", url, headers=header, data=data, timeout=self.timeout)

        return response

    def post(self, url, data='', certification='', header='', file='', get_login=''):
        if header == '':
            header = self.header()

        if certification == '':
            response = self.session().request("POST", url, headers=header, data=data, files=file, timeout=self.timeout)
            if get_login == True:
                return response, self.license
        else:
            response = certification.request("POST", url, headers=header, data=data, files=file, timeout=self.timeout)
    
        return response

    def delete(self, url, data='', certification='', header=''):
        if header == '':
            header = self.header()

        if certification == '':
            response = self.session().request("DELETE", url, headers=header, data=data, timeout=self.timeout)
        else:
            response = certification.request("DELETE", url, headers=header, data=data, timeout=self.timeout)
    
        return response
    
    def login(self, url, data='', certification='', header='', file=''):
        session = self.session()
        if header == '':
            header = self.header()

        if certification == '':
            response = session.request("POST", url, headers=header, data=data, files=file, timeout=self.timeout)
        else:
            response = certification.request("POST", url, headers=header, data=data, files=file, timeout=self.timeout)
    
        return response, session

    def response_json(self, data):
      resp_json = data.json(encoding = 'utf-8')

      return resp_json
    
    def sleep(self, seconds):
        time.sleep(seconds)

    def websocket(self):
       return websocket

    def font(self, language, text):
        return OpenCC(language).convert(text)

    def get_us_time(self):
        us = (datetime.datetime.now() - datetime.timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")
        time = datetime.datetime.strptime(us, "%Y-%m-%d %H:%M:%S")
        return time

    def test_skip(self, *args):
        print(*args)
        return self.test_skip_method(self, *args)   