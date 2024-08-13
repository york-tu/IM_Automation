import requests, os, sys, random
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from datetime import datetime
from lottery.apis.function_layer.base_functions import BaseFunction as BaseFunction_API

class CashSystem(BaseFunction_API):
   # 比對金額
   def compare_member_wallet(self, web_account, platform, money, certification, url):
      self.sleep(10)
      # 取得會員錢包資訊
      url = f'{url}apis/wallet?memberlogin={web_account}&pi=1'
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      for wallet in res.json()['Items']:
         if wallet['walletcode'] == platform:
            assert int(wallet['balance']) == money, f"第三方: {platform} 的可用餘額不正確，預期: {money}；會員錢包: {wallet['balance']}"
            break