import requests, os, sys, random
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime


class AccountManagement(BaseFunction):

   # 查詢銀行帳號所属分类
   def get_online_merchant_list(self, certification, url, deposit_or_withdraw='0'):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/merchant?status=1&pi=1&inout={deposit_or_withdraw}'
      res = self.get(url, certification=certification)

      return res

   # 刪除指定的在線商號
   def delete_old_online_merchant(self, merchant_name, certification, url):
      merchant_id = ''

      # Admin
      # 確認是否有對應的商號
      check_res = self.get_online_merchant_list(certification, url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'

      for merchant in check_res.json()['Items']:
         if merchant['category'] == f'{merchant_name}/{merchant_name}':
            merchant_id = merchant['id']
            break
         
      if merchant_id != '':
         # 刪除舊的商號
         url = f'{url}apis/merchant/{merchant_id}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'
         assert '已删除' in delete_res.text, f'{merchant_name}商號刪除失敗'

   def create_online_merchant(self, merchant_id, merchant_name, categorydtlid, certification, url, transfer_method, payment_code, private_sign, public_sign, callback, availamount, deposit_amount_interval,category_type, deposit_or_withdraw):
      url = f'{url}apis/merchant'

      payload = {
         'isDisabled': False,
         'transfermethod': transfer_method,
         'account': merchant_id,
         'name': merchant_name,
         'currencycode': 'RMB',
         'paymentcode': payment_code,
         'appkey': merchant_id,
         'appsecret': private_sign,
         'apppubkey': public_sign,
         'callback' : callback,
         'maxamount': '0',
         'minamount': '0',
         'remarklinkstatus': '0',
         'status': '1',
         'sort': '0',
         'inout': deposit_or_withdraw,
         'charge': '0',
         'levelcodes': '1,2,3,4,5,6,7,8,9,10,22,21,20,19,17,18,16,15,14,13,12,11',
         'showpc': '1',
         'showwap': '1',
         'showapp': '1',
         'categorydtlid': categorydtlid,
         'type': category_type,
         'availamount': availamount,
         'depositamountinterval': deposit_amount_interval
         
      }

      res = self.post(url, payload, certification=certification)

      return res

   # 新增指定的在線商號
   def readd_online_merchant(self, category_name, certification, admin_url, merchant_name, transfer_method, payment_code, private_sign, public_sign='', bank_id='', callback='', availamount='',deposit_amount_interval='',category_subname='', deposit_or_withdraw='0'):
      merchant_id = ''
      categorydtlid = ''
      category_type = '0'

      # Admin
      # 設定商號用途 0為入款；1為出款，出款沒有商號類型與所屬分類
      if deposit_or_withdraw == '0':
         
         # 查詢銀行帳號所属分类
         url = f'{admin_url}apis/setting/deposit/category/items?depositflag=1'
         category_res = self.get(url, certification=certification)
         assert category_res.status_code == 200, f'api狀態碼不正確: {category_res.status_code},  訊息:{category_res.text}'

         for category_item in category_res.json():
            for category_id in category_item['items']:
               if category_id['categorydtlname'] == f'{category_name}' and category_id['categoryname'] == f'{category_name}' and category_id['tagname'] == '线上支付':
                  categorydtlid = category_id['categorydtlid']
                  break
               elif category_id['categoryname'] == f'{category_name}' and category_id['categorydtlname'] == f'{category_subname}' and  category_id['tagname'] == '顺付WellPay-我要买':
                  categorydtlid = category_id['categorydtlid']
                  category_type = '1'
                  break
            
            if categorydtlid != '':
               break

         assert categorydtlid != '', '查詢不到在線商號所属分类'

      # 新增對應的商號
      if bank_id == '':
         bank_id = datetime.now().strftime('00000_bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))

      create_res = self.create_online_merchant(bank_id, merchant_name, categorydtlid, certification, admin_url, transfer_method, payment_code, private_sign, public_sign, callback, availamount,deposit_amount_interval,category_type, deposit_or_withdraw)
      assert '已新增' in create_res.text, f'{category_name}商號新增失敗'

      res = self.get_online_merchant_list(certification, admin_url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for merchant in res.json()['Items']:
         if merchant['category'] == f'{category_name}/{category_name}':
            merchant_id = merchant['id']
            break

      return merchant_id

   # 刪除所有的在線商號存款方式
   def delete_all_online_merchant(self, certification, admin_url):
      # 查詢銀行帳號所属分类
      res = self.get_online_merchant_list(certification, admin_url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for merchant in res.json()['Items']:
         # 刪除舊的在線商號
         url = f'{admin_url}apis/merchant/{merchant["id"]}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'

      check_res = self.get_online_merchant_list(certification, admin_url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'
      assert len(check_res.json()['Items']) == 0, f"在線商號沒有刪除乾淨: {check_res.json()['Items']}"

   # 檢查指定的在線商號是否存在_入款商號
   def check_online_merchant_exist(self, account_category_left, account_category_right, certification, url):
      
      check_res = self.get_online_merchant_list(certification, url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'

      check = False
      for merchant in check_res.json()['Items']:
         if merchant['category'] == f'{account_category_left}/{account_category_right}':
            check = True
            return merchant['id']

      assert check == True, f'在線商號: {account_category_right}，沒有新增成功'
   
   # 檢查指定的在線商號是否存在_出款商號
   def check_online_merchant_withdraw_exist(self, merchant_name, certification, url):
      
      check_res = self.get_online_merchant_list(certification, url, deposit_or_withdraw='1')
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'

      check = False
      for merchant in check_res.json()['Items']:
         if merchant['name'] == merchant_name:
            check = True
            return merchant['id']

      assert check == True, f'在線商號: {merchant_name}，沒有新增成功'

   def get_bank_account_list(self, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/account?status=1&pi=1&ps=500'
      res = self.get(url, certification=certification)

      return res

   # 刪除指定的銀行帳號
   def delete_old_bank_account(self, account_category_left, account_category_right, account_name, certification, url):
      account_number = ''

      # Admin
      # 確認是否有公司入款的分類
      res = self.get_bank_account_list(certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for bank_account in res.json()['Items']:
         if bank_account['category'] == f'{account_category_left}/{account_category_right}' and bank_account['name'] == account_name:
            account_number = bank_account['number']
            break
      
      if account_number != '':
         # 刪除舊的公司入款帳號
         url = f'{url}apis/account/{account_number}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'
         assert '已删除' in delete_res.text, f'{account_category_left} 銀行帳號刪除失敗'

   # 新增指定的銀行帳號
   def readd_bank_account(self, categorydtlname, categoryname, tagname, account_name, sort_type, certification, admin_url):
      categorydtlid = ''

      # 查詢銀行帳號所属分类
      url = f'{admin_url}apis/setting/deposit/category/items?depositflag=0'
      res = self.get(url, certification=certification)      # 取得在線商號所属分類
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for category_item in res.json():
         for category_id in category_item['items']:
            if category_id['categorydtlname'] == categorydtlname and category_id['categoryname'] == categoryname and category_id['tagname'] == tagname:
               categorydtlid = category_id['categorydtlid']
               break

      assert categorydtlid != '', '查詢不到銀行帳號所属分类'

      # 新增對應的銀行帳號
      bank_id = datetime.now().strftime('00000_bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))

      url = f'{admin_url}apis/account'

      payload = {
         'account': bank_id,
         'name': account_name,
         'currencycode': 'RMB',
         'bankcode': 'ABC',
         'branch': f'自動市_{categorydtlname}',
         'status': '1',
         'sort': '0',
         'minamount': '0',
         'maxamount': '0',
         'levelcodes': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22',
         'discount': '1',
         'type': sort_type,
         'autoaccept': '0',
         'autoduration':'60',
         'categoryid': '0',
         'categorydtlid': categorydtlid,
         'selectAll': True,
      }

      res = self.post(url, payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'
      assert '已新增' in res.text, f'{categoryname} 銀行帳號新增失敗'

      return bank_id

   # 刪除所有的銀行帳號存款方式
   def delete_all_bank_account(self, certification, admin_url):
      # 取得所有的銀行帳號info
      res = self.get_bank_account_list(certification, admin_url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for bank_account in res.json()['Items']:
         # 刪除存款銀行類型
         bank_id = bank_account['number']
         url = f'{admin_url}apis/account/{bank_id}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'

      check_res = self.get_bank_account_list(certification, admin_url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'
      assert len(check_res.json()['Items']) == 0, f"銀行帳號沒有刪除乾淨: {check_res.json()['Items']}"

   # 檢查指定的銀行帳號是否存在
   def check_bank_account_exist(self, account_category_left, account_category_right, account_name, certification, url):
      
      check_res = self.get_bank_account_list(certification, url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'

      check = False
      for bank_account in check_res.json()['Items']:
         if bank_account['category'] == f'{account_category_left}/{account_category_right}' and bank_account['name'] == account_name:
            check = True
            return bank_account['number']
      
      assert check == True, f'銀行帳號: {account_category_right}，沒有新增成功'


   #### 錢包地址
   # 新增指定的錢包地址
   def readd_crypto_wallet(self, categorydtlname, categoryname, tagname, account_name, sort_type, bankcode, certification, admin_url):
      categorydtlid = ''
      cryptocurrencywalletcode = ''

      # 查詢銀行帳號/錢包地址所属分类
      url = f'{admin_url}apis/setting/deposit/category/items?depositflag=0'
      res = self.get(url, certification=certification)      # 取得在線商號所属分類
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for category_item in res.json():
         for category_id in category_item['items']:
            if category_id['categorydtlname'] == categorydtlname and category_id['categoryname'] == categoryname and category_id['tagname'] == tagname:
               categorydtlid = category_id['categorydtlid']
               break

      assert categorydtlid != '', '查詢不到虛擬幣所属分类'
      # 判別相符的錢包名稱
      if categorydtlname =='USDT(TRC)':
         cryptocurrencywalletcode = 'usdt_trc20'
      elif categorydtlname =='USDT(ERC)':
         cryptocurrencywalletcode = 'usdt_erc20'
      assert cryptocurrencywalletcode != '', '查詢不到相符的錢包名稱'

      # 新增對應的錢包地址
      wallet_address = datetime.now().strftime('0x0walletxbot%Y%m%d%H%M%Sxx' + str(random.randrange(1, 10000)))

      url = f'{admin_url}apis/account/crypto-wallet'

      payload = {
         'account': wallet_address,
         'cryptocurrencywalletcode':cryptocurrencywalletcode, #usdt_erc20 / usdt_trc20
         'name': account_name,
         'currencycode': 'RMB',
         'bankcode': bankcode, #對應不同交易所名稱 #币安 BNB/ 火币 HT/ imToken LON /OLEX OKB/ TokenPocket TP
         # 'branch': f'自動市_{categorydtlname}',
         'limit':'1000000',
         'status': '1',
         'sort': '0',
         'minamount': '0',
         'maxamount': '0',
         'levelcodes': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22',
         'discount': '1',
         'type': sort_type,
         'autoaccept': '0',
         'autoduration':'60',
         'categoryid': '0',
         'categorydtlid': categorydtlid,
         'selectAll': True,
      }

      res = self.post(url, payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'
      assert '已新增' in res.text, f'{categoryname} 錢包地址新增失敗'

      return wallet_address


   def get_crypto_wallet_list(self, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/account/crypto-wallet?status=1&pi=1&ps=500'
      res = self.get(url, certification=certification)

      return res
   
   # 檢查指定的錢包地址是否存在
   def check_crypto_wallet_exist(self, category_left, category_right, account_name, certification, url):
      
      check_res = self.get_crypto_wallet_list(certification, url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'

      check = False
      for crypto_wallet in check_res.json()['Items']:
         if crypto_wallet['category'] == f'{category_left}/{category_right}' and crypto_wallet['name'] == account_name:
            check = True
            return crypto_wallet['number'] # 钱包地址序号
      
      assert check == True, f'錢包地址: {category_right},{account_name}，沒有新增成功'
   
   # 刪除所有的錢包地址存款方式
   def delete_all_crypto_wallet(self, certification, admin_url):
      # 取得所有的錢包地址info
      res = self.get_crypto_wallet_list(certification, admin_url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for crypto_wallet in res.json()['Items']:
         # 刪除存款錢包地址類型
         bank_id = crypto_wallet['number']
         url = f'{admin_url}apis/account/{bank_id}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'

      check_res = self.get_crypto_wallet_list(certification, admin_url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code},  訊息:{check_res.text}'
      assert len(check_res.json()['Items']) == 0, f"錢包地址沒有刪除乾淨: {check_res.json()['Items']}"
   
   # 刪除指定的錢包地址
   def delete_old_bank_account(self, category_left, category_right, account_name, certification, url):
      account_number = ''

      # Admin
      # 確認是否有虛擬幣的分類
      res = self.get_bank_account_list(certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code},  訊息:{res.text}'

      for bank_account in res.json()['Items']:
         if bank_account['category'] == f'{category_left}/{category_right}' and bank_account['name'] == account_name:
            account_number = bank_account['number']
            break
      
      if account_number != '':
         # 刪除舊的錢包地址
         url = f'{url}apis/account/{account_number}'
         delete_res = self.delete(url, certification=certification)
         assert delete_res.status_code == 200, f'api狀態碼不正確: {delete_res.status_code},  訊息:{delete_res.text}'
         assert '已删除' in delete_res.text, f'{category_left} 錢包地址刪除失敗'