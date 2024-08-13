import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class SystemList(BaseFunction):

   def system_list(self, certification, url, master, levelcode):
      url = f'{url}apis/agent'
      querystring = {
         "login":"",
         "name":"",
         "levelcode": levelcode,
         "status":"-1",
         "locked":"-1",
         "sharelogin": master,
         "agentlogin":"",
         "isshareloginnotbound":"0",
         "isagentloginnotbound":"0",
         "pi":"1",
         "ps":"500",
         "po":"",
         "startaddedtime":"",
         "endaddedtime":"",
         "_":"1610694288746"
      }

      res = self.get(url, certification=certification, querystring=querystring)
      
      return res

   # 將層級內非指定人都踢出
   def clear_user(self, account, shareholder, generalagent, agent, certification, url, otp, default_dict):
      data_list = [[generalagent, '1', default_dict['shareholder']],\
          [agent, '0', default_dict['generalagent']]]

      for num in range(0, len(data_list)):
         system_res = self.system_list(certification, url, shareholder, data_list[num][1])
         assert system_res.status_code == 200, f'api狀態碼不正確: {system_res.status_code}, 訊息:{system_res.text}'

         for list_info in system_res.json()['Items']:
            member = list_info['login']
            if member != data_list[num][0]:
               agent = data_list[num][2]
               levelcode = data_list[num][1]
               url = f'{url}apis/agent/{member}'
               data = {
                  "agentlogin": agent,
                  "sharelogin": agent,
                  "parentlogin": agent,
                  "login": member,
                  "name": member,
                  "levelcode": levelcode
               }
               
               res = self.put(url, certification=certification, data=data)
               assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

   # 關閉登入滑動驗證
   def close_login_slide_verified(self, certification, url, brand, reseller_url):
      url = f'{url}apis/form'
      data = {
         "membertimeout": 7000,
         "usertimeout": 7000,
         "resellertimeout": 7000,
         "locktimeout": 30,
         "agentlogin": 'default_agent',
         "geetestenable": 0,
         "resellerurl": reseller_url,
         "memberregisterphone": 2,
         "generalagentlogin": 'ccp88888',
         "depositstatus": 1,
         "withdrawstatus": 1,
         "myagentstatus": 1,
      }
      if brand == 'ttmj':
         data["generalagentlogin"] = 'test5678',

      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

   # 初始化所有設定
   def initialize_all_settings(self, certification, url, brand, env, reseller_url):
      url = f'{url}apis/form'
      data = {
         "membertimeout": 7000,
         "usertimeout": 7000,
         "resellertimeout": 7000,
         "locktimeout": 30,
         "agentlogin": 'default_agent',
         "resellerurl": reseller_url,
         "memberregisterphone": 2,
         "memberrecommend": 1,
         "generalagentlogin": 'ccp88888',
         "myagentstatus": 1,
      }
      if brand == 'lv' and env == 'stage':
         data["agentlogin"] = 'test1234'

      if brand == 'cdd' or brand == '3h':
         data["wapversion"] = '1'

      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
      
   #初始化充提款設定
   def deposit_withdraw_settings(self, certification, url):
      url = f'{url}apis/form/deposit-withdraw'
      data = {
         "depositstatus": 1,
         "depositenablelevel": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
         "withdrawstatus": 1,
         "withdrawenablelevel": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24",
      }

      res = self.put(url, certification=certification, data=data)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'     
