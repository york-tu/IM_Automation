import requests, os, sys, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class BettingCenter(BaseFunction):
   # 注單中心-取得注單列表
   def get_order(self, web_account, kind, startaddedtime, endaddedtime, certification, url):
      if kind == 'add':
         url = f'{url}apis/order?status=1&start_added_time={startaddedtime}&end_added_time={endaddedtime}&pi=1&ps=25'
      elif kind == 'payout':
         url = f'{url}apis/order?status=1&start_payout_time={startaddedtime}&end_payout_time={endaddedtime}&pi=1&ps=25'

      if web_account != '':
         url = url + f'&memberlogin={web_account}'

      res = self.get(url, certification=certification)

      return res

   # 注單中心-取得注單列表待派彩 number
   def get_betting_item(self, web_account, kind, certification, url):

      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      res = {}

      get_order_res = self.get_order(web_account, kind, start_time, end_time, certification, url)
      assert get_order_res.status_code == 200, f'api狀態碼不正確: {get_order_res.status_code}'

      for order in get_order_res.json()['Items']:
         if order['status'] != 4:
            res['number'] = order['number']
            break
      
      assert res != {}, '無法取得注單列表資料'

      return res

   # 注單中心-取得注單列表的總計資料
   def get_betting_pager(self, web_account, kind, certification, url):

      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      res = {}

      get_order_res = self.get_order(web_account, kind, start_time, end_time, certification, url)
      assert get_order_res.status_code == 200, f'api狀態碼不正確: {get_order_res.status_code}, 訊息:{get_order_res.text}'

      res['total'] = get_order_res.json()['Pager']['Total']
      res['amount'] = get_order_res.json()['Pager']['stat']['total']
      res['earning'] = get_order_res.json()['Pager']['stat']['earning']
      res['rebate'] = get_order_res.json()['Pager']['stat']['rebate']
      res['income'] = get_order_res.json()['Pager']['stat']['income']
      res['point'] = get_order_res.json()['Pager']['stat']['point']
      
      assert res != {}, '無法取得注單列表資料'

      return res

   # 注單中心-作廢
   def rescind_order(self, uuid, number, certification, url, otp):

      url = f'{url}apis/order/{uuid}/status'

      payload = {
         'status': '4',
         'otp': otp,
         'number': number
      }

      rescind_order_res = self.put(url, data=payload, certification=certification)
      assert rescind_order_res.status_code == 200, f'api狀態碼不正確: {rescind_order_res.status_code}'

   # 注單中心-派彩總計
   def get_searchpayout(self, bet_list_total, certification, url):

      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      
      url = f'{url}apis/order/searchpayout?start_payout_time={start_time}&end_payout_time={end_time}'

      get_searchpayout_res = self.get(url, certification=certification)
      assert get_searchpayout_res.status_code == 200, f'api狀態碼不正確: {get_searchpayout_res.status_code}'

      assert bet_list_total['total'] == get_searchpayout_res.json()['total'], f"派彩總計的单量: {get_searchpayout_res.json()['total']} 與注單中心的總計: {bet_list_total['total']} 不一致"
      assert bet_list_total['amount'] == round(float(get_searchpayout_res.json()['amount']), 2), f"派彩總計的投注额: {get_searchpayout_res.json()['amount']} 與注單中心的注额: {bet_list_total['amount']} 不一致"
      assert bet_list_total['earning'] == round(float(get_searchpayout_res.json()['earning']), 2), f"派彩總計的派彩: {get_searchpayout_res.json()['earning']} 與注單中心的派彩: {bet_list_total['earning']} 不一致"
      assert bet_list_total['rebate'] == round(float(get_searchpayout_res.json()['rebate']), 2), f"派彩總計的返水: {get_searchpayout_res.json()['rebate']} 與注單中心的返水: {bet_list_total['rebate']} 不一致"
      assert bet_list_total['income'] == round(float(get_searchpayout_res.json()['income']), 2), f"派彩總計的损益: {round(float(get_searchpayout_res.json()['income']), 2)} 與注單中心的损益: {bet_list_total['income']} 不一致"
      assert bet_list_total['point'] == round(float(get_searchpayout_res.json()['point']), 2), f"派彩總計的打码: {get_searchpayout_res.json()['point']} 與注單中心的打码: {bet_list_total['point']} 不一致"

   # 注單中心-注单校验
   def bet_validation(self, bet_number, certification, url):

      url = f'{url}apis/order/validation/{bet_number}'

      bet_validation_res = self.get(url, certification=certification)
      assert bet_validation_res.status_code == 200, f'api狀態碼不正確: {bet_validation_res.status_code}'
      assert bet_validation_res.json()['Items']['Status'] == '1', f"效驗狀態不正確: {bet_validation_res.json()['Items']['Status']}"
   
   # 注單中心-注单查詢
   def bet_search(self, bet_number, validationid, certification, url):
      url = f'{url}apis/order/validation?number={bet_number}&validationid={validationid}'

      res = self.get(url, certification=certification)

      return res

   # 抓取注單中心內容
   def get_info_member(self, certification, account, Password, url,web_account):
      today_start= self.get_us_time().strftime("%Y-%m-%d 00:00")
      now=  self.get_us_time().strftime("%M")
   
      if int(now) > 29 : # 確保遊戲報表能回來
         today_end= (self.get_us_time() - timedelta(hours=1)).strftime("%Y-%m-%d %H:59")
      else:
         today_end= (self.get_us_time() - timedelta(hours=2)).strftime("%Y-%m-%d %H:59")

      Querystring = {"number":"","member_login":web_account,"product_number":"","channel_code":"",
                  "product_type":"","play_code":"","status":"1","payout":"-1","start_added_time":"","end_added_time":"",
                  "start_payout_time":today_start,"end_payout_time":today_end,"currency_code":"","agent":"","general_agent":"",
                  "share_login":"","pi":"1","ps":"25","po":"","category_id":""
                  }

      url = "%sapis/order" % url
      response = self.get(url, Querystring, certification, self.header())
      get = response.json() # 總資料

      
      _sum={'Total':get['Pager']['Total'],            # 小計
         'Amount':"%.2f" %get['Pager']['stat']['total'],   # 注額
         'Point':"%.2f" %get['Pager']['stat']['point'],     # 打碼
         'Rebate':"%.2f" %get['Pager']['stat']['rebate'],   # 反水
         'Earning':"%.2f" %get['Pager']['stat']['earning'], # 派彩
         'Income':"%.2f" %get['Pager']['stat']['income']    # 損益
         }
      
      return _sum


   # 抓取注單中心內容
   def get_info_agent(self, certification, account, Password, url, reseller_account):
      # today_start= self.get_us_time().strftime("%Y-%m-%d 00:00")
      # now=  self.get_us_time().strftime("%M")
      # if int(now) > 29 : # 確保遊戲報表能回來
      #    today_end= (self.get_us_time() - timedelta(hours=1)).strftime("%Y-%m-%d %H:59")
      # else:
      #    today_end= (self.get_us_time() - timedelta(hours=2)).strftime("%Y-%m-%d %H:59")
      
      today_start = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      today_end = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      url = f'{url}apis/order?agent={reseller_account}&status=1&start_payout_time={today_start}&end_payout_time={today_end}&pi=1&ps=25'
      res = self.get(url, certification=certification)
      get = res.json()

      _sum={'Total':get['Pager']['Total'],            # 小計
         'Amount':"%.2f" %get['Pager']['stat']['total'],   # 注額
         'Point':"%.2f" %get['Pager']['stat']['point'],     # 打碼
         'Rebate':"%.2f" %get['Pager']['stat']['rebate'],   # 反水
         'Earning':"%.2f" %get['Pager']['stat']['earning'], # 派彩
         'Income':"%.2f" %get['Pager']['stat']['income']    # 損益
         }
      
      return _sum