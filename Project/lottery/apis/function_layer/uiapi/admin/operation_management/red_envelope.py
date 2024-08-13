import requests, os, sys, pytz
import random, string
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class RedEnvelope(BaseFunction):
   # 注單中心-紅包-掃雷-廳別管理
   def hb_create_channel(self, kind, certification, url):

      # bot_id = datetime.now().strftime('bot%Y%m%d%H%M%S_' + str(random.randrange(1, 10000)))
      bot_id = datetime.now().strftime("QA_Automated_%Y%m%d_" + str(random.randrange(1, 10000)))

      if kind == '掃雷':
         url = f'{url}apis/red_envelope/room/hbsl'

         payload = {
            'name': bot_id,
            'minamount': '1',
            'maxamount': '1',
            'ttl': '1',
            'qty': '9',
            'rate': '1.68',
            'fee': '1',
            'sort': '0',
            'status': '0',
            'remark': bot_id,
            'pointvisible': '0'
         }
      elif kind == '牛牛':
         url = f'{url}apis/red_envelope/room/hbnn'

         payload = {
            'name': bot_id,
            'minamount': '1',
            'maxamount': '1',
            'ttl': '1',
            'minqty': '1',
            'maxqty': '1',
            'n1rate': '1',
            'n2rate': '1',
            'n3rate': '1',
            'n4rate': '1',
            'n5rate': '1',
            'n6rate': '1',
            'n7rate': '1',
            'n8rate': '1',
            'n9rate': '1',
            'nnrate': '1',
            'fee': '1',
            'sort': '0',
            'status': '0',
            'remark': bot_id,
            'pointvisible': '0'
         }

      res = self.post(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert '已新增' in res.text, f'response不正確: {res.text}'

      return bot_id

   # 確認廳別是否有建立
   def hb_channel_search(self, kind, channel_name, certification, url):

      if kind == '掃雷':
         url = f'{url}apis/red_envelope/room/hbsl?pi=1&ps=500'
      elif kind == '牛牛':
         url = f'{url}apis/red_envelope/room/hbnn?pi=1&ps=500'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert res.json()['Pager']['Pages'] >= 1, f"未查詢到紅包廳別資訊"

      check = False
      for channel in res.json()['Items']:
         if channel['name'] == channel_name:
            check = True
            break
      
      if check == False:
         raise EOFError('查詢不到剛新增的紅包廳別')