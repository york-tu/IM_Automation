import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
import pytz, time
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class WithdrawManagement(BaseFunction):

   # 取得出款申請資訊
   def get_withdraw_info(self, withdraw_money, web_account, certification, admin_url):
      withdraw_id = ''
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      check = False
      for _ in range(60):
         url = f'{admin_url}apis/withdraw?memberlogin={web_account}&startaddedtime={start_time}&endaddedtime={end_time}&pi=1&status=-1'
         record_res = self.get(url, certification=certification)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'

         for record in record_res.json()['Items']:
            if record['memberlogin'] == web_account:
               withdraw_id = record['id']
               check = True
               # break
               if str(record['amount']) == str(withdraw_money):
                  withdraw_id = record['id']
                  check = True
                  break
               else:
                  break
         
         if check == True:
            break
         else:
            time.sleep(1)
      
      assert check == True, 'Admin 找不到相關提款的紀錄'

      return withdraw_id

   # 鎖定特定提款申請
   def lock_specific_withdraw(self, withdraw_id, web_account, certification, url):
      url = f'{url}apis/withdraw/{withdraw_id}/lock'

      payload = {
         'memberlogin': web_account
      }

      res = self.post(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

    # 同意特定提款申請
   def agree_withdraw(self, withdraw_id, web_account, certification, url):
      url = f'{url}apis/withdraw/{withdraw_id}/status'

      payload = {
         'memberlogin': web_account,
         'status': '1'
      }

      res = self.put(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'