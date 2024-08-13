import requests, os, sys, random, string
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class Register(BaseFunction):

   def do_register(self, url):
      random_string = ''.join([random.choice(string.ascii_lowercase 
            + string.digits) for n in range(6)]) 
      bot_id = datetime.now().strftime(f'bot{random_string}')

      # Web - 註冊
      password = '111111'
      if bot_id == '' or password == '' or url == '':
         raise EOFError(f'註冊資料不完整: 帳號:{bot_id} 密碼:{password} 網址:{url}')
      
      payload = {
         'login': bot_id,
         'passwd': password,
         'passwd2': password,
         'securitycode': password,
         'currencycode': 'RMB',
         'langcode': 'zh_CN',
         'name': '機器人',
         'agree': True
      }

      url = f'{url}apis/member'
      res = self.post(url, payload)
      if res.text.__contains__('验证码无效'):
         self.test_skip('驗證碼已開啟')
         
      return bot_id, res.status_code