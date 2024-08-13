import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timezone, timedelta
import math

class Utils(BaseFunction):

   def server_time(self, certification, url):
      now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)

      url = f'{url}apis/server-time?&_={now_timestamp}'
      res = self.get(url, certification=certification)

      return res

   def marquees(self, certification, url):
      now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)

      url = f'{url}apis/marquees?&_={now_timestamp}'
      res = self.get(url, certification=certification)

      return res

   def unread_total(self, certification, url):
      now_timestamp = math.floor((datetime.utcnow().replace(tzinfo=timezone.utc)).astimezone(timezone(timedelta(hours=8))).timestamp()*1000)

      url = f'{url}apis/my/inbox/unread/total?&_={now_timestamp}'
      res = self.get(url, certification=certification)

      return res

   def get_specific_balance(self, wallet, certification, url):
      money = 0
      # 取得url的品牌名稱
      brand = url.split('https://')[1].split('-')[0]

      res = self.balance(certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      
      found = False
      for wallet_item in res.json():
         if wallet_item['walletcode'] == wallet:
            found = True
            money = wallet_item['balance']
            break
      
      assert found == True, f'找不到錢包: {wallet}'

      return money

   def get_all_balance(self, certification, url):
      before_wallet = {}
      return_money = 0
      # 取得url的品牌名稱
      platform = url.split('https://')[1].split('-')[0]

      # Web
      # 取得一鍵歸戶前各錢包的金額
      res = self.balance(certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      for wallet in res.json():
         before_wallet[wallet['walletcode']] = wallet['balance']
         if wallet['walletcode'] != 'cp':
            return_money += int(wallet['balance'])

      return before_wallet, return_money