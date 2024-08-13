import requests, os, sys, pytz, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta
import time

class DepositManagement(BaseFunction):

   def online_deposit(self, memberlogin, starttime, endtime, certification, url):
      if memberlogin == '':
         url = f'{url}apis/webdeposit?start_added_time={starttime}&end_added_time={endtime}&pi=1&ps=25'
      else:
         url = f'{url}apis/webdeposit?member_login={memberlogin}&start_added_time={starttime}&end_added_time={endtime}&pi=1&ps=25'
      res = self.get(url, certification=certification)

      return res

   # 取得在線入款對應的存款記錄
   def get_online_deposit(self, desposit_id, web_account, certification, url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      check = False
      for _ in range(60):
         res = self.online_deposit(web_account, start_time, end_time, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
         for record in res.json()['Items']:
               if record['id'] == desposit_id:
                  assert record['transfer_amount'] == 100, '存款金額不正確'
                  check = True
                  break
               else:
                  break

         if check == True:
               break
         else:
               time.sleep(1)

      assert check == True, 'Admin 找不到相關存款金額的紀錄: 100'

   # 同意在線商號特定的存款申請
   def agree_webdeposit_apply(self, web_account, certification, admin_url, desposit_id='', otp=''):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      if desposit_id == '':
         record_res = self.online_deposit(web_account, start_time, end_time, certification, admin_url)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}, 錯誤訊息: {record_res.text}'

         for record_item in record_res.json()['Items']:
            desposit_id = record_item['id']
            break

      url = f'{admin_url}apis/webdeposit/{desposit_id}/status'

      payload = {
         'status': '1',
         'member_login': web_account,
         'otp': otp
      }

      res = self.put(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'

   def company_deposit(self, memberlogin, starttime, endtime, certification, url):
      if memberlogin == '':
         url = f'{url}apis/deposit?start_added_time={starttime}&end_added_time={endtime}&pi=1&ps=25&account_status=1'#&audit_status=-1&isexportmode=0
      else:
         url = f'{url}apis/deposit?member_login={memberlogin}&start_added_time={starttime}&end_added_time={endtime}&pi=1&ps=25&account_status=1'#&audit_status=-1&isexportmode=0
      res = self.get(url, certification=certification)
      return res

   # 取得公司入款對應的存款記錄
   def get_company_deposit(self, deposit_money, web_account, certification, url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      check = False
      for _ in range(60):
         res = self.company_deposit(web_account, start_time, end_time, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
         for record in res.json()['Items']:
            if record['member_login'] == web_account:
               record_item = str(record['transfer_amount'])
               
            if record_item == deposit_money:
               check = True
               break
            else:
               break

         if check == True:
            break
         else:
            time.sleep(1)

      assert check == True, f'Admin 找不到相關存款金額的紀錄: {deposit_money}, {record_item}'

   # 同意銀行帳號特定的存款申請
   def agree_deposit_apply(self, web_account, certification, url):
      desposit_id = ''
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      record_res = self.company_deposit(web_account, start_time, end_time, certification, url)
      assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}, 錯誤訊息: {record_res.text}'

      for record_item in record_res.json()['Items']:
         desposit_id = record_item['id']
         break

      url = f'{url}apis/deposit/{desposit_id}/status'

      payload = {
         'status': '1',
         'member_login': web_account,
      }

      res = self.put(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'

   # 比對公司入款的存款記錄
   def compare_company_deposit(self, money, certification, url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      res = self.company_deposit('', start_time, end_time, certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
      for record in res.json()['Items']:
         if str(int(record['transfer_amount'])) == money:
            break
         else:
            raise EOFError(f'存款記錄找不到該筆金額, 存款金額:{money}')

   # 比對在線入款的存款記錄
   def compare_merchant_deposit(self, certification, url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      transferamount = 0.00
      depositamount = 0.00
      discountamount = 0.00

      res = self.online_deposit('', start_time, end_time, certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
      for record in res.json()['Items']:
         transferamount += float(record['transfer_amount'])
         depositamount += float(record['deposit_amount'])
         discountamount += float(record['discount_amount'])

      transferamount_total = float(res.json()['Pager']['stat']['transfer_amount'])
      discountamount_total = float(res.json()['Pager']['stat']['discount_amount'])
      depositamount_total = float(res.json()['Pager']['stat']['deposit_amount'])

      assert re.findall(r"\d{1,}?\.\d{2}", str(transferamount)) == re.findall(r"\d{1,}?\.\d{2}", str(transferamount_total)), '轉帳金額不正確: 加總: ' + re.findall(r"\d{1,}?\.\d{2}", str(transferamount)) + '；總計: ' + re.findall(r"\d{1,}?\.\d{2}", str(transferamount_total))
      assert re.findall(r"\d{1,}?\.\d{2}", str(discountamount)) == re.findall(r"\d{1,}?\.\d{2}", str(discountamount_total)), '優惠金額不正確: 加總: ' + re.findall(r"\d{1,}?\.\d{2}", str(discountamount)) + '；總計: ' + re.findall(r"\d{1,}?\.\d{2}", str(discountamount_total))
      assert re.findall(r"\d{1,}?\.\d{2}", str(depositamount)) == re.findall(r"\d{1,}?\.\d{2}", str(depositamount_total)), '入賬金額不正確: 加總: ' + re.findall(r"\d{1,}?\.\d{2}", str(depositamount)) + '；總計: ' + re.findall(r"\d{1,}?\.\d{2}", str(depositamount_total))

   # 比對公司入款的入款總覽記錄
   def compare_company_deposit_overview(self, kind, web_account, certification, admin_url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      transferamount = 0.00
      depositamount = 0.00
      discountamount = 0.00

      if kind == '公司入款':
         res = self.company_deposit(web_account, start_time, end_time, certification, admin_url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
         for record in res.json()['Items']:
            transferamount += float(record['transfer_amount'])
            depositamount += float(record['deposit_amount'])
            discountamount += float(record['discount_amount'])
            break
      else:
         res = self.online_deposit('', start_time, end_time, certification, admin_url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
         for record in res.json()['Items']:
            transferamount += float(record['transfer_amount'])
            depositamount += float(record['deposit_amount'])
            discountamount += float(record['discount_amount'])
            break

      url = f'{admin_url}apis/deposit/overview?memberlogin={web_account}&currencycode=RMB&starttime={start_time}&endtime={end_time}&pi=1&ps=25'
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 錯誤訊息: {res.text}'
      for record in res.json()['Items']:
         assert kind == record['category'], f"交易類別不正確: 入款紀錄: {kind}；入款總覽紀錄: {record['category']}"
         assert re.findall(r"\d{1,}?\.\d{2}", str(transferamount)) == re.findall(r"\d{1,}?\.\d{2}", str(record['transfer_amount'])), '轉帳金額不正確: 入款紀錄: ' + re.findall(r"\d{1,}?\.\d{2}", str(transferamount)) + '；入款總覽紀錄: ' + re.findall(r"\d{1,}?\.\d{2}", str(record['transferamount']))
         assert re.findall(r"\d{1,}?\.\d{2}", str(depositamount)) == re.findall(r"\d{1,}?\.\d{2}", str(record['deposit_amount'])), '入款金額不正確: 入款紀錄: ' + re.findall(r"\d{1,}?\.\d{2}", str(depositamount)) + '；入款總覽紀錄: ' + re.findall(r"\d{1,}?\.\d{2}", str(record['depositamount']))
         break