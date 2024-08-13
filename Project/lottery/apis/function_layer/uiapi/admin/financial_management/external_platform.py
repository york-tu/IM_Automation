import requests, os, sys, random, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class ExternalPlatform(BaseFunction):

   # 確認Admin額度轉換是否有資料，並與transfer_data比對
   def get_wallet_transfer_list(self, web_account, transfer_data, certification, url):
      
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      url = f'{url}apis/wallet/transfer?memberlogin={web_account}&status=-99&starttime={start_time}&endtime={end_time}&pi=1&ps=500'
      
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert res.json()['Pager']['Pages'] >= 1, "找不到額度轉換資料"

      # 處理額度轉換失敗的資料
      admin_list = [item for item in res.json()['Items'] if item['status'] != -1]

      # 比對資料 建立集合以加速查找
      admin_set = {admin_data['id'] for admin_data in admin_list}

      # 找不到的資料列表
      not_found_data = []

      # 檢查 transfer_set 的元素是否都在 admin_set 中
      for web_data in transfer_data:
         if web_data['productnumber'] not in admin_set:
            not_found_data.append(web_data['productnumber'])

      # 檢查是否有找不到的資料
      assert not not_found_data, f"以下資料在 admin_額度轉換 中找不到匹配的訂單號碼: {not_found_data}"




   # 取得CM Web顯示的廠商餘額
   def get_cm_vendor_wallet(self, jwt, vendor_name):
      # 取得CM Web的餘額
      url = f'http://uat.cmapi.pstdsf.com:10080/v1/wallets'

      headers = {
        'Content-Type': 'application/json',
        'authorization': jwt
    }

      res = self.get(url, header=headers)
      assert res.status_code == 200, f'CM_WEB廠商餘額api狀態碼不正確: {res.status_code}'

      check = False
      for wallet in res.json()['data']:
         if wallet['name'] == vendor_name:
            check = True
            return str(wallet['amount'])[:-2]

      assert check == True, f"找不到廠商餘額: {vendor_name}"

   # CM 與 Admin廠商餘額比較
   def vendor_balance_check(self, cm_balance, vendor_name, certification, url):
      # 取得Admin的廠商餘額
      url = f'{url}apis/cmwallet'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      check = False
      for wallet in res.json():
         if wallet['name'] == vendor_name:
            check = True
            assert int(wallet['balance']) == int(cm_balance), f"Admin顯示的廠商餘額: {wallet['balance']} 與 CM Web顯示的廠商餘額: {cm_balance} 不一致"
            break

      assert check == True, f"找不到廠商餘額: {vendor_name}"      