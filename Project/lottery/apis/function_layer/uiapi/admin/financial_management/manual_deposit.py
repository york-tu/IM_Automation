import requests, os, sys, random, time
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from datetime import *
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API

class ManualDeposit(BaseFunction_API):
   # 新增
   def add_manual_deposit(self, web_account, certification, url, money):
      url = f'{url}apis/mandeposit/audit'
      data = {
         "mandepositaudit": '[{"accountnumber":"","actioncode":"0","discountamount":0,"discountauditdue":"null","discountauditpoint":"null","discountid":"","memberlogin":"bot","merchantid":"","remark":"","transferamount":10,"transferauditcharge":"null","transferauditdue":"null","transferauditrate":"null","submitinfo":"","submitid":""}]'
      }
      
      data["mandepositaudit"] = (data["mandepositaudit"].replace(':10', f':{money}')).replace('bot', web_account)

      res = self.post(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, {res.text}'

   # 審核
   def check_manual_deposit(self, web_account, certification, admin_url):
      # 審核查找
      url = f'{admin_url}apis/mandepositaudit'
      today_start = self.get_us_time()
      tomorrow_start = today_start + timedelta(days=1)

      querystring = {
         "status":"0,1",
         "ps": 25,
         "pi": 1,
         "addedstarttime": today_start,
         "addedendtime": f'{tomorrow_start} 00:00',
      }
      # time.strftime("%Y-%m-%d %H:%M", time.localtime()) 
      res = self.get(url, certification=certification, querystring=querystring)

      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, {res.text}'
      
      # 審核同意
      url = f'{admin_url}apis/mandeposit/audit'
      data = {}
      id_str = ''
      info = res.json()
      # 由於data臉面只吃雙引號,但我們印出來字串會自動變成單引號,故強制轉換
      for item in info['Items']:
         id = item['id']
         id_str += '{' + f'"id": "{id}"' + '},'

      id_str = '[' + id_str[:-1] + ']'         
      data["auditid"] = id_str
      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, {res.text}'