import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class MemberList(BaseFunction):

   def check_register_success(self, account, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/member?login={account}&nicknamefuzzy=0&loginfuzzy=0&namefuzzy=0&nologindays=0&noorderdays=0&isagentloginnotbound=0&online=-1&bindcardnumber=-1&pi=1'
      res = self.get(url, certification=certification)

      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
      assert len(res.json()['Items']) > 0, f'Admin查詢不到註冊的帳號: {account}'

   def agent(self, acount, agent, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = url + 'apis/member/get'

      querystring = {
      "login":"",
      "name":"",
      "nickname":"",
      "nicknamefuzzy":"0",
      "levelcodes":"",
      "agentlogin":agent,
      "referrallogin":"",
      "langcode":"",
      "currencycode":"",
      "loginfuzzy":"0",
      "namefuzzy":"0",
      "cardnumber":"",
      "nologindays":"0","noorderdays":"0",
      "isagentloginnotbound":"0",
      "online":"-1",
      "bindcardnumber":"-1",
      "pi":"1",
      "ps":"25",
      "po":"",
      "start":"",
      "end":"",
      }

      res = self.post(url, querystring, certification=certification)

      return res

   def clear_user(self, account, agent, certification, url, otp, default_agent):
      res = self.agent(account, agent, certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

      for list_info in res.json()['Items']:
         member = list_info['login']
         if not member.__contains__(account[:-1]):
            if certification == '' or url == '':
               raise EOFError('參數不完整')

            member_url = url + f'apis/member/{member}/agent'
            
            data = {
               'agentlogin': default_agent,
               'otp': otp
            }

            res = self.put(member_url, certification=certification, data=data)

            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

   # 將bot帳號調整回正確代理
   def initialize_agent(self, account, agent, certification, url, otp):
      if certification == '' or url == '':
               raise EOFError('參數不完整')
      member_url = url + f'apis/member/{account}/agent'
      data = {
               'agentlogin': agent,
               'otp': otp
      }
      res = self.put(member_url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'


   # 關閉一二級會員入款otp
   def close_deposit_otp(self, certification, url):
      url = f'{url}apis/level'
      data = {
         'items': '[{"code":"1","name":"一级会员","enabledepositotp":0},{"code":"2","name":"二级会员","enabledepositotp":0}]'
      }
      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
      self.sleep(10)

   # 開啟一二級會員入款otp
   def open_deposit_otp(self, certification, url):
      url = f'{url}apis/level'
      data = {
         'items': '[{"code":"1","name":"一级会员","enabledepositotp":1},{"code":"2","name":"二级会员","enabledepositotp":1}]'
      }
      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
      self.sleep(10)
   
   def get_deposit_otp(self, certification, member, url):

      url = f'{url}apis/member/{member}/deposit-otp'
      
      respsone = self.post(url, certification=certification)
      code = respsone.status_code
      assert code == 200, f'api狀態碼不正確: {code.status_code}, 訊息:{code.text}'
      
      return (respsone.json()['otp'])

   def change_agent(self, member, default_agent, certification, url, opt):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = url + f'apis/member/{member}/agent'
      
      data = {
         'agentlogin': default_agent,
         'otp': opt
      }

      res = self.put(url, certification=certification, data=data)

      return res