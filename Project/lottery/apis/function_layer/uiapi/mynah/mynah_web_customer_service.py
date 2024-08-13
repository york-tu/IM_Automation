import requests, os, sys, math
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timezone, timedelta

class MynahWebService(BaseFunction):

   # 修改登入密码
   def mynah_health(self, mynah_web_url, mynah_admin_url, api_service_dict):
      res = self.get(mynah_web_url)
      assert res.status_code == 200 and res.reason == 'OK', f'前台網站錯誤 code:{res.status_code} reason:{res.reason}'

      for server in api_service_dict:
         url = mynah_admin_url + server + '/health'
         res = self.get(url)
         assert res.status_code == 200 and res.reason == 'OK', f'{server} 錯誤 code:{res.status_code} reason:{res.reason}'

