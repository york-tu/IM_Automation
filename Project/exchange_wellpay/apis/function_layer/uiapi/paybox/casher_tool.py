import json
import random
import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
import pytz, time
from Project.exchange_wellpay.apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class CasherTool(BaseFunction):
    
    #新增搶單
    def add_order(self, money, merchant_id=2015, method='ZFB_ZZ'):
        casher_url = "http://uat-zqb.paradise-soft.com.tw:17805"
        url = f'{casher_url}/casher/v1/deposit'
        order_id = random.randint(100000000000,999999999999)
        payload = {
            "order_id": order_id,
            "merchant_id": merchant_id,
            "member_id": 1275,
            "member_login": "qacmtest001",
            "member_name": "qacmtest001",
            "method": method,
            "amount": money,
            "added_time": "2022-01-20T09:42:54.636154217Z",
            "Retry": 0
        }
        data = json.dumps(payload)
        res = self.post(url, data)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'


    #新增買單
    def add_sell(self, money, merchant_id=2015):
         
      url = 'http://uat-zqb.paradise-soft.com.tw:17805/casher/v1/sell'
      order_id = random.randint(100000000000,999999999999)
      payload = {
         "order_id": order_id,
         "merchant_id": merchant_id,
         "member_id": 818,
         "member_login": "qatest001",
         "card_number": "5522455233066152",
         "card_holder": "林先生",
         "card_bank_code": "BANK_ZZ",
         "amount": money
      }
      data = json.dumps(payload)
      res = self.post(url, data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'