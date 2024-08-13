import requests, os, sys, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class StationNews(BaseFunction):
   def send_message(self, title, web_account, certification, url):
      start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
      
      url = f'{url}apis/message'

      payload = {
         'langcode': 'zh_CN',
         'title': title,
         'content': f'<p>{title}</p>',
         'memberlogin': web_account,
         'postmode': '1',
         'starttime': start_time,
         'endtime': end_time
      }

      send_res = self.post(url, data=payload, certification=certification)
      assert send_res.status_code == 200, f'api狀態碼不正確: {send_res.status_code}'