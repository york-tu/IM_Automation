import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class DepositOffer(BaseFunction):
   # 存款優惠刪除
   def delete_offer(self, certification, url):
      # 手续费用-更新会员设定
      url = f'{url}apis/discount/deposit'

      querystring = {
      "name":"",
      "deposittype":"-1",
      "depositwhen":"-1",
      "optional":"-1",
      "status":"-1",
      "levelcodes":"",
      "currencycode":"",
      "pi":"1",
      "ps":"500",
      "po":"",
      }

      res = self.get(url, querystring=querystring, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

      items = res.json()['Items']
      for offer in items:
         offer_id = offer['id']
         url = f'{url}/{offer_id}'
         res = self.delete(url, certification=certification)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert '已删除' in res.text, f'刪除存款優惠錯誤 錯誤訊息{res.text}'
