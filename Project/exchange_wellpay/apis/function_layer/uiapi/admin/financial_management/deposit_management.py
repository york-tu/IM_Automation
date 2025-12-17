import requests, os, sys, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta
import time

class DepositManagement(BaseFunction):

   def online_deposit(self, memberlogin, starttime, endtime, certification, url):
      if memberlogin == '':
         url = f'{url}apis/webdeposit?starttime={starttime}&endtime={endtime}&pi=1&ps=25&status=-1'
      else:
         url = f'{url}apis/webdeposit?memberlogin={memberlogin}&starttime={starttime}&endtime={endtime}&pi=1&ps=25&status=-1'
      res = self.get(url, certification=certification)

      return res

   # 取得在線入款對應的存款記錄
   def get_online_deposit(self, desposit_id, web_account, certification, admin_url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      check = False
      for _ in range(60):
         res = self.online_deposit(web_account, start_time, end_time, certification, admin_url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         for record in res.json()['Items']:
               if record['id'] == desposit_id:
                  assert record['transferamount'] == 100, '存款金額不正確'
                  check = True
                  break
               else:
                  break

         if check == True:
               break
         else:
               time.sleep(1)

      assert check == True, 'Admin 找不到相關存款金額的紀錄'

   # 同意在線商號特定的存款申請
   def agree_webdeposit_apply(self, web_account, certification, admin_url, desposit_id='', otp=''):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      if desposit_id == '':
         record_res = self.online_deposit(web_account, start_time, end_time, certification, admin_url)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'

         for record_item in record_res.json()['Items']:
            desposit_id = record_item['id']
            break

      url = f'{admin_url}apis/webdeposit/{desposit_id}/status'

      payload = {
         'status': '1',
         'memberlogin': web_account,
         'otp': otp
      }

      res = self.put(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def company_deposit(self, memberlogin, starttime, endtime, certification, url):
      if memberlogin == '':
         url = f'{url}apis/deposit?startaddedtime={starttime}&endaddedtime={endtime}&pi=1&ps=25&status=-1&accountstatus=-1&auditstatus=-1&isexportmode=0'
      else:
         url = f'{url}apis/deposit?memberlogin={memberlogin}&startaddedtime={starttime}&endaddedtime={endtime}&pi=1&ps=25&status=-1&accountstatus=-1&auditstatus=-1&isexportmode=0'
      res = self.get(url, certification=certification)

      return res

   # 取得公司入款對應的存款記錄
   def get_company_deposit(self, deposit_money, web_account, certification, admin_url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      check = False
      for _ in range(60):
         res = self.company_deposit(web_account, start_time, end_time, certification, admin_url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         for record in res.json()['Items']:
            if record['memberlogin'] == web_account:
               record_item = str(record['transferamount'])
               
            if record_item == deposit_money:
               check = True
               break
            else:
               break

         if check == True:
            break
         else:
            time.sleep(1)

      assert check == True, 'Admin 找不到相關存款金額的紀錄'

   # 同意銀行帳號特定的存款申請
   def agree_deposit_apply(self, web_account, certification, url):
      desposit_id = ''
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      record_res = self.company_deposit(web_account, start_time, end_time, certification, url)
      assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'

      for record_item in record_res.json()['Items']:
         desposit_id = record_item['id']
         break

      url = f'{url}apis/deposit/{desposit_id}/status'

      payload = {
         'status': '1',
         'memberlogin': web_account,
      }

      res = self.put(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'