import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
class GameSetting(BaseFunction):
   # 所有遊戲的列表
   def game_list_api(self, certification, url, channelcode=''):
      url = f'{url}apis/product?status=1&recommend=-1&channelcode={channelcode}&pi=1&ps=5000'
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息: {res.text}'

      return res
   
   # 取所有遊戲的中文名稱
   def game_list(self, certification, url):
      game_dict = {}
      res = self.game_list_api(certification, url)

      items = res.json()['Items']
      for i in range(len(items)):
         game_dict[items[i]['name']] = items[i]['channelname']
   
      return game_dict

   # 取所有遊戲的codename
   def game_code_list(self, certification, url, channelcode=''):
      res = self.game_list_api(certification, url, channelcode)

      items = res.json()['Items']
      game_code_list = [items[i]['code'] for i in range(len(items))]

      return game_code_list

   def compare(self, game_dict):
      error_dict = {}
      for name, brand in game_dict.items():
            simplified = self.font('t2s', name)
            if simplified != name:
               error_dict[name] = brand

      if len(error_dict) != 0:
         raise EOFError(f'遊戲名稱包含繁體字 \n {error_dict}')