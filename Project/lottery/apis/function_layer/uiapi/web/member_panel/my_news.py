import requests, os, sys, math
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
import time

class MyNews(BaseFunction):
   # 取得站內消息
   def get_messages(self, certification, web_url):
      
      messages_get = False

      for _ in range(60):
         url = f'{web_url}apis/my/inbox/messages'

         res = self.get(url, certification=certification)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         if len(res.json()['Items']) != 0:
            messages_get = True
            return res
         else:
            time.sleep(1)

      assert messages_get == True, '未取得站內消息'

   # 刪除站內消息
   def delete_messages(self, res, certification, web_url):

      for message in res.json()['Items']:
         url = f'{web_url}apis/my/inbox/message/del/{message["id"]}'

         del_res = self.delete(url, certification=certification)
         assert del_res.status_code == 200, f'api狀態碼不正確: {del_res.status_code}'   