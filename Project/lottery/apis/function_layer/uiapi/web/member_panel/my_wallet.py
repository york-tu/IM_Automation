import requests, os, sys, math, random, string, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta, timezone
import time
from decimal import Decimal

class MyWallet(BaseFunction):
   # 入款記錄
   def recharge_record(self, deposit_type, start_time, end_time, certification, url):
      now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)

      url = f'{url}apis/recharge/record?time=d&type={deposit_type}&starttime={start_time}&endtime={end_time}&pi=1&_={now_timestamp}&ps=25'

      res = self.get(url, certification=certification)

      return res

   # 使用在線商號渠道存款
   def online_merchant_deposit(self, merchant_id, certification, admin_url):
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      method = 'card'
      amount = '100'

      if method == '' or amount == '' or merchant_id == '':
         raise EOFError(f'存款資料不完整: 存款類型: {method} 金額: {amount} ID: {merchant_id}')

      payload = {
         'transfermethod': method,
         'transferamount': amount,
         'merchantid': merchant_id
      }

      url = f'{admin_url}apis/webdeposit'
      res = self.post(url, payload, certification)
      error_text = "操作过于频繁，请稍后再试"
      if error_text in res.text:
         self.sleep(10)
         res = self.post(url, payload, certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      desposit_id = res.json()

      check = False
      for _ in range(60):
         record_res = self.recharge_record('webdeposit', start_time, end_time, certification, admin_url)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'
         for record in record_res.json()['Items']:
            if record['id'] == desposit_id:
               check = True
               break
            else:
               break

         if check == True:
            break
         else:
            time.sleep(1)

      assert check == True, f'入款記錄找不到存款id: {desposit_id}'

      return desposit_id

   # 檢查特定錢包的金額
   def check_specific_balance(self, wallet, before_money, Comparison_money, certification, url):
      money = 0
      # 取得url的品牌名稱
      platform = url.split('https://')[1].split('-')[0]
      
      retry = 0
      while True:
         res = self.balance(certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         found = False
         for wallet_item in res.json():
            if wallet_item['walletcode'] == wallet:
               found = True
               money = wallet_item['balance']
               break
         
         assert found == True, f'找不到錢包: {wallet}'

         if money != before_money:
            break
         else:
            retry += 1
            time.sleep(1)

         assert retry <= 60, '重試60次，仍然沒有完成存款'
      
      assert Decimal(str(money)) - Decimal(str(Comparison_money)) == Decimal(str(before_money)), f'錢包異動後的金額不正確: after: {Decimal(str(money))} - Comparison: {Decimal(str(Comparison_money))} != before: {Decimal(str(before_money))}'

   def bank_account_deposit(self, method, amount, account_number, card_name, card_number, card_bank_code, time, certification, url, otp=''):
      if method == '' or amount == '' or account_number == '':
         raise EOFError(f'存款資料不完整: 存款類型: {method} 金額: {amount} 帳戶: {account_number}')

      payload = {
         'transferamount': amount,
         'cardname': card_name,
         'accountnumber': account_number,
         'transfermethod': method,
         'cardbankcode': card_bank_code,
         'cardnumber': card_number,
         'transfertime': time,
         'depositotp' : otp
      }

      url = f'{url}apis/deposit'
      res = self.post(url, payload, certification)

      return res

   # 使用銀行帳號-面對面掃碼渠道存款
   def qrcode_deposit(self, bank_id, method, card_name, card_number, card_bank_code, certification, url, otp='', deposit_money=''):
      deposit_time = datetime.now().strftime('%Y-%m-%d %H:%M')
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      if deposit_money == '':
         deposit_money = random.randint(1, 999)
         if deposit_money < 10:
            deposit_money = f'{deposit_money}00'
         elif deposit_money < 100:
            deposit_money = f'{deposit_money}0'
         else:
            deposit_money = str(deposit_money)
      
      res = self.bank_account_deposit(method, deposit_money, bank_id, card_name, card_number, card_bank_code, deposit_time, certification, url, otp)
      error_text = "操作过于频繁，请稍后再试"
      if error_text in res.text:
         self.sleep(10)
         res = self.bank_account_deposit(method, deposit_money, bank_id, card_name, card_number, card_bank_code, deposit_time, certification, url, otp)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息: {res.text}'

      check = False
      for _ in range(60):
         record_res = self.recharge_record('deposit', start_time, end_time, certification, url)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'
         for record in record_res.json()['Items']:
            if str(record['depositamount']) == deposit_money:
               check = True
               break
            else:
               break

         if check == True:
            break
         else:
            time.sleep(1)

      assert check == True, f'找不到相關存款金額的紀錄: {deposit_money}'

      return deposit_money

   # 線上取款
   def online_withdraw(self, certification, web_url, withdraw_money=''):
      loop = 0
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      if withdraw_money == '':
         withdraw_money = int(random.randint(500, 1000))

      payload = {
      'amount': withdraw_money,
      'bankaccountid': '5e8af187-2e5b-11eb-b751-42010ad2010b',   #目前因為卡號驗證問題，暫時先寫死
      'securitycode': '111111'
      }

      url = f'{web_url}apis/my/withdraw'
      error_text = "操作过于频繁，请稍后再试"

      while True:
         loop+=1
         res = self.post(url, payload, certification)

         if error_text in res.text:
            self.sleep(10)
            res = self.post(url, payload, certification)

         if res.status_code != 200:
            try:
               need = float(re.findall("[0-9.]+", (res.text))[-1]) + 1
               withdraw_money = int(need)

               if loop ==5:
                  raise EOFError(f'出款異常: {res.text}')
               continue
            except:
               assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}；error: {res.text}'
         else:
            break

      # assert '已提交，请稍后查询结果' in res.text, '提款失敗'

      check = False
      now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)

      url = f'{web_url}apis/withdrawal/record?time=d&type=withdraw&starttime={start_time}&endtime={end_time}&pi=1&_={now_timestamp}&ps=25'

      record_res = self.get(url, certification=certification)
      real_withdraw = record_res.json()['Items'][0]['amount']

      assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'
      assert real_withdraw <= withdraw_money, f'取款金額有問題: 出款金額: {withdraw_money} 實際扣除費用後: {real_withdraw}'
      
      return withdraw_money, real_withdraw

   # 使用銀行帳號-轉帳渠道存款
   def transfer_deposit(self, kind, bank_id, method, card_name, card_number, card_bank_code, certification, web_url):
      deposit_time = datetime.now().strftime('%Y-%m-%d %H:%M')
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      deposit_money = random.randint(1, 999)

      if deposit_money < 10:
         deposit_money = f'{deposit_money}00'
      elif deposit_money < 100:
         deposit_money = f'{deposit_money}0'
      else:
         deposit_money = str(deposit_money)

      # Web
      # 使用支付寶-轉帳渠道存款
      url = f'{web_url}apis/deposit/key/{kind}?amount={deposit_money}'

      key_res = self.get(url, certification=certification)
      assert key_res.status_code == 200, f'無法取得 {kind} key'
      key = key_res.json()['decimalkey']
      if key[-1] == '0':
         key = key[:-1]
      deposit_res = self.bank_account_deposit(method, f'{deposit_money}.{key}', bank_id, card_name, card_number, card_bank_code, deposit_time, certification, web_url)
      error_text = "操作过于频繁，请稍后再试"
      if error_text in deposit_res.text:
         self.sleep(10)
         deposit_res = self.bank_account_deposit(method, f'{deposit_money}.{key}', bank_id, card_name, card_number, card_bank_code, deposit_time, certification, web_url)
      assert deposit_res.status_code == 200, f'api狀態碼不正確: {deposit_res.status_code}'

      check = False
      for _ in range(60):
         record_res = self.recharge_record('deposit', start_time, end_time, certification, web_url)
         assert record_res.status_code == 200, f'api狀態碼不正確: {record_res.status_code}'
         for record in record_res.json()['Items']:
            if str(record['depositamount']) in f'{deposit_money}.{key}':
               check = True
               break
            else:
               break

         if check == True:
            break
         else:
            time.sleep(1)

      assert check == True, f'找不到相關存款金額的紀錄: {deposit_money}.{key}'

      return f'{deposit_money}.{key}'

   # 一鍵歸戶
   def return_cp(self, certification, url):
      url = f'{url}apis/my/wallet/transfer/back'
      res = self.post(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert res.json()['failedcount'] == 0, f'一鍵歸戶失敗: {res.json()["transtatus"]}'

   # 錢包正在維護時略過該錢包的歸戶
   def wallet_in_maintenance(self, certification, url):
      url = f'{url}apis/my/wallet/status'
      res = self.get(url, certification=certification)      # 錢包狀態
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      maintenance_list = [wallet for wallet, status in eval(res.text).items() if status == 0]
      return maintenance_list

   # 一鍵歸戶後，各錢包金額確認
   def check_return_cp_wallet(self, before_wallet, return_money, maintenance_list, certification, web_url):
      after_wallet = {}
      # 取得url的品牌名稱
      platform = web_url.split('https://')[1].split('-')[0]

      money_check = False
      retry = 0
      while True:
         res = self.balance(certification, web_url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         
         for wallet in res.json():
            after_wallet[wallet['walletcode']] = wallet['balance']
            if wallet['walletcode'] != 'cp' and wallet['walletcode'] not in maintenance_list:
               if int(wallet['balance']) == 0:
                  money_check = True
               else:
                  money_check = False
                  break
         
         if money_check == True:
            for wallet in maintenance_list:
               return_money -= after_wallet[wallet]
            if after_wallet['cp'] - return_money == before_wallet['cp']:
               break
            else:
               retry += 1
               time.sleep(1)
         else:
            retry += 1
            time.sleep(1)

         assert retry <= 60, '重試60次，仍然沒有完成一鍵歸戶'

      assert after_wallet['cp'] - return_money == before_wallet['cp'], f'一鍵歸戶金額不正確: {after_wallet["cp"]} - {return_money} = {before_wallet["cp"]}'

   # 額度轉換
   def quota_conversion(self, master_wallet, slave_wallet, money, certification, web_url):
      url = f'{web_url}apis/my/wallet/transfer'

      payload = {
         'from': master_wallet,
         'to': slave_wallet,
         'amount': money
      }
      for _ in range(0,3):
         res = self.post(url, data=payload, certification=certification)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息: {res.text}'
         # 避免遇操作过于频繁導致錯誤
         if type(res.json()) == dict:
            break
         else:
            time.sleep(5)
      url = f'{web_url}apis/my/wallet/transfer/{res.json()["id"]}/status'

      transfer_status_res = self.get(url, certification=certification)
      assert transfer_status_res.status_code == 200, f'api狀態碼不正確: {transfer_status_res.status_code}, 訊息: {transfer_status_res.text}'
      assert transfer_status_res.json()['status'] == 1, f"轉帳失敗，status: {transfer_status_res.json()['status']}、errormessage: {transfer_status_res.json()['errormessage']}、remark: {transfer_status_res.json()['remark']}"

      return res.json()['id']

   # 確認額度轉換是否成功
   def check_quota_conversion(self, master_wallet, slave_wallet, before_master, before_slave, money, certification, url):
      after_master = ''
      after_slave = ''
      # 取得url的品牌名稱
      platform = url.split('https://')[1].split('-')[0]

      retry = 0
      while True:
         res = self.balance(certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         for wallet in res.json():
            if wallet['walletcode'] == master_wallet:
               after_master = int(wallet['balance'])
            if wallet['walletcode'] == slave_wallet:
               after_slave = int(wallet['balance'])
            if after_master != '' and after_slave != '':
               break

         if before_master - after_master == money and after_slave - before_slave == money and after_master != '' and after_slave != '':
            break
         else:
            after_master = ''
            after_slave = ''
            time.sleep(1)
         
         retry += 1
         assert retry <= 120, '等待120秒，仍然沒有轉帳成功'

      assert int(before_master) - money == after_master and int(before_slave) + money == after_slave, f'轉帳後金額不正確: {int(before_master)} - {money} = {after_master}；{int(before_slave)} + {money} = {after_slave}'


   # 交易流水
   def transfer_flow(self, typecodes, certification, web_url):
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      # Web
      # 交易流水
      url = f'{web_url}apis/my/wallet/history?time=d&typecodes={typecodes}&starttime={start_time}&endtime={end_time}&type=period&pi=1&ps=500'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      return res.json()['Items']