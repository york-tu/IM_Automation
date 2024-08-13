import requests, os, sys, math, uuid, pytz, time, re, random, json
from random import sample
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
import common.utils.globalvar as gl
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta, timezone

class ThirdParty(BaseFunction):

   def get_game_list(self, brand, certification, web_url):
      game_list = {}
      # 取得url的品牌名稱
      platform = web_url.split('https://')[1].split('-')[0]

      mobile = 0
      url = f'{web_url}apis/game/list/{brand}/0?mobile={mobile}&pi=1&ps=1000'
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      
      for game in res.json()['Items']:
         game_list[game['gameid']] = game['name']

      return game_list

   def forward_game(self, brand, gameid, certification, url, mobile=0):
      url = f'{url}apis/game/{brand}/forward-game?gameid={gameid}&enabletls=0&mobile={mobile}&domain={url.replace("https://", "")}'
      res = self.get(url, certification=certification)

      return res

   def open_games(self, brand, game_list, certification, url):
      error_game_list = {}
      unknow_game_list = {}
      # 取得url的品牌名稱
      platform = url.split('https://')[1].split('-')[0]

      retry = 60
      while True:
         for game in list(game_list.keys()):
            try:
               if platform == 'ttmj':
                  open_game = self.forward_game(brand, game, certification, url, 1)
               else:
                  open_game = self.forward_game(brand, game, certification, url)
            except:
               continue
            
            if open_game.status_code != 200:
               continue

            if open_game.json()['status'] == 0:
               error_game_list[game] = game_list[game]
               del game_list[game]
            elif open_game.json()['status'] != 0 and open_game.json()['status'] != 1:
               unknow_game_list[game] = game_list[game]
               del game_list[game]
            elif open_game.json()['status'] == 1:
               del game_list[game]

         if game_list == {}:
            break
         else:
            retry += 1
            time.sleep(1)

         assert retry <= 60 , f'重試超過60次，仍然未完成所有遊戲確認: {game_list}'

      assert len(error_game_list) == 0 and len(unknow_game_list) == 0, f'遊戲接口不正確: {error_game_list}；未知遊戲狀態: {unknow_game_list}'

   def open_game(self, brand, game_id, certification, url):
      
      # 取得url的品牌名稱
      platform = url.split('https://')[1].split('-')[0]

      retry = 0
      while True:
         try:
            if platform == 'ttmj':
               open_game = self.forward_game(brand, game_id, certification, url, 1)
            else:
               open_game = self.forward_game(brand, game_id, certification, url)

            if open_game.status_code != 200:
               retry += 1
               time.sleep(1)
            else:
               break
         except:
            retry += 1
            time.sleep(1)
         
         assert retry <= 60 , f'重試超過 60 次，仍然未完成遊戲確認'

      assert open_game.json()['status'] == 1, f'遊戲接口不正確: {brand}: {game_id}，狀態: {open_game.json()["status"]}'

   def lottery_order_api(self, producttype, productnumber, roomcode, playcode, playname, amount, bet_item, id, certification, url):
      url = f'{url}apis/order'
      orders = [{"producttype":producttype,"productnumber":productnumber,"roomcode":roomcode,"playcode":playcode,"playname":playname,"nums":1,"amount":amount,"total":amount,"items":bet_item,"id":id}]
      jsonbody = json.dumps(orders)

      payload = {
         'orders': jsonbody,
      }

      res = self.post(url, certification=certification, data=payload)
      return res, productnumber

   # 彩票投注
   def lottery_order(self, producttype, handicap_info, bet_name, bet_count, env, certification, url):

      bet_info = {}
      bets_data = []
      bet_item = []
      uuid_number = ''
      period = ''

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['rate'] = bet_rates['rate']
                  bet_data['name'] = bet_rates['name']
                  bet_data['value'] = bet_rates['value']
                  bet_data['code'] = bet_info['code']
                  bets_data.append(bet_data)

      # 計算今年生肖該取的賠率
      this_year = f"{datetime.now().strftime('%Y')}"
      num = (int(this_year) % 12) - 4
      if num > 4 or num >= bet_count or '尾碰' in bet_name:
         num = 0

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         uuid_number = str(uuid.uuid4())
         period = self.get_handicap_period(producttype, certification, url)
         
         # 有兩種版型
         summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[num]['rate'])} x 1.00"
         summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[num]['rate'])} x 1.00"
         
         res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, 1, bet_item, uuid_number, certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, 1, bet_item, uuid_number, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

         return uuid_number, period, res.json()[0]['number'], res.json()[0]['id'], summary_1, summary_2, res.json()[0]['validationid']
      else:
         no = 1
         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1           

            # 有兩種版型
            total_bet = ''
            for name in bet_item:
               total_bet = total_bet + name['name'] + ','
            total_bet = total_bet[:-1]

            summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[num]['rate'])} x 1.00"
            summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[num]['rate'])} x 1.00"

            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

            bet_item.clear()
            res_json = self.response_json(res)[0]
            res_json['summary_1'] = summary_1
            res_json['summary_2'] = summary_2
            res_json['productnumber'] = productnumber
            return res_json


# 彩票投注
   def lottery_random(self, producttype_list, handicap_info_list, bet_count, env, certification, url):
      for handicap_info, producttype  in zip(handicap_info_list, producttype_list):
         bet_info = {}
         bets_data = []
         bet_item = []

         # 整理下注的玩法資料
         for info in handicap_info:
            bet_info['code'] = info['code']
            random_num = random.choice(list(info['plays']))
            plays_info = info['plays'][random_num]
            bet_info['playcode'] = plays_info['code']
            bet_info['name'] = plays_info['name']

            for bet_rates in plays_info['rates']:
               bet_data = {}
               bet_data['item_code'] = bet_rates['code']
               bet_data['rate'] = bet_rates['rate']
               bet_data['name'] = bet_rates['name']
               bet_data['value'] = bet_rates['value']
               bet_data['code'] = bet_info['code']
               bets_data.append(bet_data)
            no = 1
            break

         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)
            break
            
         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_info['name'], bet_count, bet_item, str(uuid.uuid4()), certification, url)

         if res.json()[0]['status'] != 1:
            print(f"error code: {res.status_code} message: {res.json()[0]['message']}")
         else:
            break

   # 六合彩 - 特码-合肖 - 客製
   def lottery_order_special_he_xiao(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url):

      bet_info = {}
      rate_data = {}
      bets_data = []
      bet_item = []

      # 整理下注的玩法資料
      bet_info['code'] = handicap_info[0]['code']
      for info in handicap_info:
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               no = 2
               bet_info['playcode'] = plays_info
               for bet_rates in info['plays'][plays_info]['rates']:
                  rate_data[no] = bet_rates['rate']
                  no += 1
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['value']
                  bet_data['name'] = bet_rates['name']
                  bet_data['value'] = bet_rates['value']
                  bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = rate_data[bet_count]
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
      else:
         no = 1
         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = rate_data[bet_count]
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1            

            # 有兩種版型
            total_bet = ''

            if len(bet_item) > 1:
               for name in bet_item:
                  total_bet = total_bet + name['name'] + ','
               total_bet = total_bet[:-1] 

            summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[0]['rate'])} x 1.00"
            summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[0]['rate'])} x 1.00"
            
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            bet_item.clear()

            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

            res_json = self.response_json(res)[0]
            res_json['summary_1'] = summary_1
            res_json['summary_2'] = summary_2
            res_json['productnumber'] = productnumber

            return res_json


   # 六合彩 - 連碼 - 客製
   def lottery_order_consecutive_number(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url):

      bet_info = {}
      rate_data = {}
      bets_data = []
      bet_item = []

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['value']
                  bet_data['name'] = bet_rates['value']
                  bet_data['value'] = bet_rates['value']
                  bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], (bet_name + '-普通复式'), 1, bet_item, str(uuid.uuid4()), certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], (bet_name + '-普通复式'), 1, bet_item, str(uuid.uuid4()), certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
      else:
         no = 1
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1            

            # 有兩種版型
            total_bet = ''

            if len(bet_item) > 1:
               for name in bet_item:
                  total_bet = total_bet + name['name'] + ','
               total_bet = total_bet[:-1] 

            summary_1 = f"[{handicap_info[-1]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@"
            summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{total_bet}@"
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], (bet_name + '-普通复式'), 1, bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], (bet_name + '-普通复式'), 1, bet_item, str(uuid.uuid4()), certification, url)
            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

            bet_item.clear()
            res_json = self.response_json(res)[0]
            res_json['summary_1'] = summary_1
            res_json['summary_2'] = summary_2
            res_json['productnumber'] = productnumber

            return res_json

   # 時時彩 - 定位 - 客製
   def ssc_order_word_positioning(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url, third_bet_name='', fourth_bet_name='', fifth_bet_name=''):
      
      bet_info = {}
      rate_data = {}
      bets_data = []
      subbets_data = []
      third_bets_data = []
      fourth_bets_data = []
      fifth_bets_data = []
      bet_item = []

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info[:-2]
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['name'] = f"{bet_name[:-3]}:{bet_rates['name']}"
                  bets_data.append(bet_data)
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['name'] = f"{sub_bet_name[-1]}:{bet_rates['name']}"
                  subbets_data.append(bet_data)
            if bet_name[0] == '三' or bet_name[0] == '五':
               if info['plays'][plays_info]['name'] == third_bet_name:
                  for bet_rates in info['plays'][plays_info]['rates']:
                     bet_data = {}
                     bet_data['item_code'] = bet_rates['code']
                     bet_data['name'] = f"{third_bet_name[-1]}:{bet_rates['name']}"
                     third_bets_data.append(bet_data)
            if bet_name[0] == '五':
               if info['plays'][plays_info]['name'] == fourth_bet_name:
                  for bet_rates in info['plays'][plays_info]['rates']:
                     bet_data = {}
                     bet_data['item_code'] = bet_rates['code']
                     bet_data['name'] = f"{fourth_bet_name[-1]}:{bet_rates['name']}"
                     fourth_bets_data.append(bet_data)

               if info['plays'][plays_info]['name'] == fifth_bet_name:
                  for bet_rates in info['plays'][plays_info]['rates']:
                     bet_data = {}
                     bet_data['item_code'] = bet_rates['code']
                     bet_data['name'] = f"{fifth_bet_name[-1]}:{bet_rates['name']}"
                     fifth_bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)

         for bet in sample(subbets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)

         if bet_name[0] == '三' or bet_name[0] == '五':
            for bet in sample(third_bets_data, bet_count):
               bets_item = {}
               bets_item['code'] = bet['item_code']
               bets_item['name'] = bet['name']
               bets_item['amount'] = 1
               bet_item.append(bets_item)

         if bet_name[0] == '五':
            for bet in sample(fourth_bets_data, bet_count):
               bets_item = {}
               bets_item['code'] = bet['item_code']
               bets_item['name'] = bet['name']
               bets_item['amount'] = 1
               bet_item.append(bets_item)

            for bet in sample(fifth_bets_data, bet_count):
               bets_item = {}
               bets_item['code'] = bet['item_code']
               bets_item['name'] = bet['name']
               bets_item['amount'] = 1
               bet_item.append(bets_item)

         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
         
         total_bet = ''
         # 由於注單顯示資訊不一樣,故先客製化
         if len(bet_item) > 1:
            for name in bet_item:
               total_bet = total_bet + name['name'] + ','
            total_bet = total_bet[7] + total_bet[10:-1] 
         
         summary = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet}@"

         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
         
         time.sleep(0.5)
         bet_item.remove(bet_item[-1])
         bet_item.clear()
         res_json = self.response_json(res)[0]
         res_json['summary'] = summary
         res_json['productnumber'] = productnumber

         return res_json
      else:
         for bet in bets_data:
            bet_item = []
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)
            for bet in subbets_data:
               bets_item = {}
               bets_item['code'] = bet['item_code']
               bets_item['name'] = bet['name']
               bets_item['amount'] = 1
               bet_item.append(bets_item)

               if bet_name[0] == '三' or bet_name[0] == '五':
                  for bet in third_bets_data:
                     bets_item = {}
                     bets_item['code'] = bet['item_code']
                     bets_item['name'] = bet['name']
                     bets_item['amount'] = 1
                     bet_item.append(bets_item)

                     if bet_name[0] == '五':
                        for bet in fourth_bets_data:
                           bets_item = {}
                           bets_item['code'] = bet['item_code']
                           bets_item['name'] = bet['name']
                           bets_item['amount'] = 1
                           bet_item.append(bets_item)

                           for bet in fifth_bets_data:
                              bets_item = {}
                              bets_item['code'] = bet['item_code']
                              bets_item['name'] = bet['name']
                              bets_item['amount'] = 1
                              bet_item.append(bets_item)

                              res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                              if '已经封盘' in res.json()[0]['message']:
                                 self.sleep(5)
                                 res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                              assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
                              assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
      
                              total_bet_1 = ''
                              total_bet_2 = ''
                              # 由於注單顯示資訊不一樣,故先客製化
                              if len(bet_item) > 1:
                                 for name in bet_item:
                                    total_bet_1 = total_bet_1 + name['name'] + ','
                                    total_bet_2 = total_bet_2 + name['name'][-1] + ','
   
                                 total_bet_1 = bet_name[-1] + total_bet_1[5:-1]
                                 total_bet_2 = total_bet_2[:-1] 
                        
                              summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet_1}@"
                              summary_2 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet_2}@"

                              time.sleep(0.5)
                              bet_item.remove(bet_item[-1])
                              res_json = self.response_json(res)[0]
                              res_json['summary_1'] = summary_1
                              res_json['summary_2'] = summary_2
                              res_json['productnumber'] = productnumber
                              return res_json
                     else:
                        res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                        if '已经封盘' in res.json()[0]['message']:
                           self.sleep(5)
                           res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                        
                        total_bet_1 = ''
                        total_bet_2 = ''
                        # 由於注單顯示資訊不一樣,故先客製化
                        if len(bet_item) > 1:
                           for name in bet_item:
                              total_bet_1 = total_bet_1 + name['name'] + ','
                              total_bet_2 = total_bet_2 + name['name'][-1] + ','
      
                           total_bet_1 = bet_name[-1] + total_bet_1[10:-1] 
                           total_bet_2 = total_bet_2[:-1] 
                        

                        summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet_1}@"
                        summary_2 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet_2}@"

                        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
                        assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
                        
                        time.sleep(0.5)
                        bet_item.remove(bet_item[-1])
                        res_json = self.response_json(res)[0]
                        res_json['summary_1'] = summary_1
                        res_json['summary_2'] = summary_2
                        res_json['productnumber'] = productnumber
                        return res_json

                  bet_item.remove(bet_item[-1])
               else:
                  res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                  if '已经封盘' in res.json()[0]['message']:
                     self.sleep(5)
                     res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
                  
                  total_bet = ''
                  # 由於注單顯示資訊不一樣,故先客製化
                  if len(bet_item) > 1:
                     for name in bet_item:
                        total_bet = total_bet + name['name'] + ','
                     total_bet = total_bet[7] + total_bet[10:-1] 
                  
                  summary = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-3]}  [共1注]\n{total_bet}@"

                  assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
                  assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
                 
                  time.sleep(0.5)
                  bet_item.remove(bet_item[-1])
                  bet_item.clear()
                  res_json = self.response_json(res)[0]
                  res_json['summary'] = summary
                  res_json['productnumber'] = productnumber
                  return res_json

   # PC蛋蛋 - 特码-包三 - 客製
   def pc_egg_order_special_package_three(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url):

      bet_info = {}
      rate_data = {}
      bets_data = []
      bet_item = []
      res_json = ''

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_info['rates'] = bet_rates['rate']
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['name'] = bet_rates['name']
                  bet_data['value'] = bet_rates['value']
                  bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = ""
            bets_item['rate'] = bet_info['rates']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
      else:
         no = 1
         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = ""
            bets_item['rate'] = bet_info['rates']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1            

            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            
            total_bet = ''
            # 由於注單顯示資訊不一樣,故先客製化
            if len(bet_item) > 1:
               for name in bet_item:
                  total_bet = total_bet + name['name'] + ','
               total_bet = total_bet[:-1]
            summary = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[0]['rate'])} x 1.00"
            
            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"
            res_json = self.response_json(res)[0]
            res_json['summary'] = summary
            res_json['productnumber'] = productnumber
            bet_item.clear()

            return res_json
           

   # 11选5 - 直选 - 客製
   def eleven_choice_five_order_direct_selection(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url):

      bet_info = {}
      bets_data = []
      bet_item = []

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_info['rate'] = bet_rates['rate']
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['name'] = bet_rates['name']
                  bet_data['value'] = bet_rates['value']
                  bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env != '':
         bet_number = ''
         for bet in sample(bets_data, bet_count):
            bet_number += bet['name'] + ','
            continue

         bets_item = {}
         bets_item['code'] = bet_info['playcode']
         bets_item['rate'] = bet_info['rate']
         bets_item['amount'] = 1
         bets_item['name'] = bet_number.strip(',')
         bets_item['value'] = bet_number.strip(',')
         bet_item.append(bets_item)

         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

         total_bet = ''
         # 由於注單顯示資訊不一樣,故先客製化
         if len(bet_item) > 1:
            for name in bet_item:
               total_bet = total_bet + name['name'] + ','
            total_bet = total_bet[:-1]
         else:
            total_bet = bet_item[0]['value']

         summary = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[0]['rate'])} x 1.00"

         res_json = self.response_json(res)[0]
         res_json['summary'] = summary
         res_json['productnumber'] = productnumber
         bet_item.clear()

         return res_json

   # 一般彩票 - 字串關 - 客製
   def normal_lottery_order_word_parley(self, producttype, handicap_info, bet_name, sub_bet_name, bet_count, env, certification, url, third_bet_name=''):
      
      bet_info = {}
      rate_data = {}
      bets_data = []
      subbets_data = []
      third_bets_data = []
      bet_item = []

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info[:-2]
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['name'] = f"{bet_name[-1]}:{bet_rates['name']}"
                  bets_data.append(bet_data)
            if info['plays'][plays_info]['name'] == sub_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['name'] = f"{sub_bet_name[-1]}:{bet_rates['name']}"
                  subbets_data.append(bet_data)
            if info['plays'][plays_info]['name'] == third_bet_name:
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['name'] = f"{third_bet_name[-1]}:{bet_rates['name']}"
                  third_bets_data.append(bet_data)

      # 下注
      for bet in sample(bets_data, bet_count):
         bets_item = {}
         bets_item['code'] = bet['item_code']
         bets_item['name'] = bet['name']
         bets_item['amount'] = 1
         bet_item.append(bets_item)

      for bet in sample(subbets_data, bet_count):
         bets_item = {}
         bets_item['code'] = bet['item_code']
         bets_item['name'] = bet['name']
         bets_item['amount'] = 1
         bet_item.append(bets_item)

      for bet in sample(third_bets_data, bet_count):
         bets_item = {}
         bets_item['code'] = bet['item_code']
         bets_item['name'] = bet['name']
         bets_item['amount'] = 1
         bet_item.append(bets_item)

      res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
      if '已经封盘' in res.json()[0]['message']:
         self.sleep(5)
         res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet_info['code'],  bet_info['playcode'], bet_name[:-4], 1, bet_item, str(uuid.uuid4()), certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

      total_bet = ''
      # 由於注單顯示資訊不一樣,故先客製化
      if len(bet_item) > 1:
         for name in bet_item:
            total_bet = total_bet + name['name'] + ','
         total_bet = total_bet[:-1]
      else:
         total_bet = bet_item[0]['value']

      summary = f"[{handicap_info[0]['name'][0]}盘] - {bet_name[:-2]}   [共1注]\n{total_bet}@"

      res_json = self.response_json(res)[0]
      res_json['summary'] = summary
      res_json['productnumber'] = productnumber
      bet_item.clear()

      return res_json

   def get_handicap(self, producttype, certification, url):
      url = f'{url}apis/{producttype}/current?forceroom=true/'
      res = self.get(url, certification=certification)

      return res

   # 取得指定盤口的資料
   def get_handicap_info(self, producttype, certification, url):
      
      retry = 0
      while True:
         res = self.get_handicap(producttype, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         if len(res.json()) == 3:
            print(f"{res.json()['message']}，重試")
            time.sleep(1)
            retry += 1
         elif len(res.json()) == 8:
            return res.json()['rooms']

         if retry >= 10:      
            print('重試10次，仍然沒有取得盤口資料')   #調高到10次增加取得機率觀察看看，日後再想解法
            break

   # 取得指定盤口的期數
   def get_handicap_period(self, producttype, certification, url):
      
      retry = 0
      while True:
         res = self.get_handicap(producttype, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         if len(res.json()) == 3:
            print(f"{res.json()['message']}，重試")
            time.sleep(1)
            retry += 1
         elif len(res.json()) == 8:
            return res.json()['number']

         if retry >= 10:
            raise EOFError('重試10次，仍然沒有取得盤口期數')

   # 比對彩票的投注紀錄
   def check_lottery_bet_record(self, bet_info, certification, web_url):
      
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      retry = 0
      check = False
      while True:
         url = f"{web_url}apis/my/order/cp?payout=-1&status=1&time=d&starttime={start_time}&endtime={end_time}"
         res = self.get(url, certification=certification)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         if res.json()['Pager']['Pages'] >= 1:
            for record in res.json()['Items']:
         
               if record['id'] == bet_info['id']:
                  check = True

                  assert record['number'] == bet_info['number'], f"投注單號不正確: 投注紀錄: {record['number']}；投注資訊: {bet_info['number']}"
                  assert record['productnumber'] == bet_info['productnumber'], f"期數不正確: 投注紀錄: {record['productnumber']}；\n投注資訊: \n{bet_info['productnumber']}"

                  if 'summary_1' in bet_info.keys() or 'summary_2' in bet_info.keys():
                     try:
                        assert record['summary'].__contains__(bet_info['summary']), f"\n注單詳情不正確: 投注紀錄: \n{record['summary']}；\n投注資訊: \n{bet_info['summary']}"
                     except:
                        try:
                           assert record['summary'].__contains__(bet_info['summary_1']), f"\n注單詳情不正確: 投注紀錄: \n{record['summary']}；\n投注資訊: \n{bet_info['summary_1']}"
                        except:
                           assert record['summary'].__contains__(bet_info['summary_2']), f"\n注單詳情不正確: 投注紀錄: \n{record['summary']}；\n投注資訊: \n{bet_info['summary_2']}"
                  else:
                     assert record['summary'].__contains__(bet_info['summary']), f"\n注單詳情不正確: 投注紀錄: \n{record['summary']}；\n投注資訊: \n{bet_info['summary']}"
                     
                  break
         else:
            retry += 1
            time.sleep(1)

         if check == False:
            retry += 1
            time.sleep(1)
            print("尚未找到投注紀錄，重試")
         else:
            break
         
         if retry >= 10:
            raise EOFError('重試10次，仍然沒有找到正確的投注紀錄')

   # 股指投注
   def stock_order(self, producttype, handicap_info, bet_name, bet_count, env, certification, url):

      bet_info = {}
      bets_data = []
      bet_item = []

      if bet_name.split('-')[0] == '定位':
         play = 'dw'
      else:
         play = 'lm'

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name.split('-')[1] or info['plays'][plays_info]['name'] == bet_name:
               if plays_info.split('_')[0] == play:
                  bet_info['playcode'] = plays_info
                  for bet_rates in info['plays'][plays_info]['rates']:
                     bet_data = {}
                     bet_data['item_code'] = bet_rates['code']
                     bet_data['rate'] = bet_rates['rate']
                     bet_data['name'] = bet_rates['name']
                     bet_data['value'] = bet_rates['value']
                     bet_data['code'] = bet_info['code']
                     bets_data.append(bet_data)

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == 'prod':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         uuid_number = str(uuid.uuid4())
         period = self.get_handicap_period(producttype, certification, url)
         
         summary = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[0]['rate'])} x 1.00"
         
         res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, 1, bet_item, uuid_number, certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, 1, bet_item, uuid_number, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

         return uuid_number, period, res.json()[0]['number'], res.json()[0]['id'], summary, summary, res.json()[0]['validationid']
      else:
         no = 1
         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1           

            total_bet = ''
            for name in bet_item:
               total_bet = total_bet + name['name'] + ','
            total_bet = total_bet[:-1]

            summary = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[0]['rate'])} x 1.00"

            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

            bet_item.clear()
            res_json = self.response_json(res)[0]
            res_json['summary'] = summary
            res_json['productnumber'] = productnumber
            return res_json

   # 比對股指的投注紀錄
   def check_stock_bet_record(self, bet_info, certification, web_url):
      
      start_time = f"{datetime.now().strftime('%Y-%m-%d')} 00:00"
      end_time = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"

      retry = 0
      check = False
      while True:
         url = f"{web_url}apis/my/order/cp?starttime={start_time}&endtime={end_time}&channelcode=zs"
         res = self.get(url, certification=certification)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

         if res.json()['Pager']['Pages'] >= 1:
            for record in res.json()['Items']:
         
               if record['id'] == bet_info['id']:
                  check = True

                  assert record['number'] == bet_info['number'], f"投注單號不正確: 投注紀錄: {record['number']}；投注資訊: {bet_info['number']}"
                  assert record['productnumber'] == bet_info['productnumber'], f"期數不正確: 投注紀錄: {record['productnumber']}；\n投注資訊: \n{bet_info['productnumber']}"
                  assert record['summary'].__contains__(bet_info['summary']), f"\n注單詳情不正確: 投注紀錄: \n{record['summary']}；\n投注資訊: \n{bet_info['summary']}"
                     
                  break
         else:
            retry += 1
            time.sleep(1)

         if check == False:
            retry += 1
            time.sleep(1)
            print("尚未找到投注紀錄，重試")
         else:
            break
         
         if retry >= 10:
            raise EOFError('重試10次，仍然沒有找到正確的投注紀錄')
   
   # 取得跟投的資料
   def get_stock_follow_info(self, certification, web_url):

      url = f'{web_url}apis/stock-index/recommend/'
      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      res = res.json()[-1]

      now_time = datetime.now()
      close_time = res['orderInfo']['closeTime']
      close_time = datetime.strptime(close_time, '%Y-%m-%d %H:%M:%S')
      seconds = timedelta(seconds=3)
      if close_time > now_time + seconds:          # 即將封盤就先等待
         return res
      else:
         self.sleep(8)
         res = self.get_stock_follow_info(certification, web_url)
         return res

   # 股指跟投
   def stock_follow_order(self, follow_info, certification, url):

      bets_item = {}
      bet_item = []

      # 整理下注的玩法資料
      producttype = follow_info['orderInfo']['product']['productType']
      bet_name = follow_info['orderInfo']['product']['playName']
      roomCode = follow_info['orderInfo']['product']['roomCode']
      playcode = follow_info['orderInfo']['product']['playCode']
      productnumber = follow_info['orderInfo']['product']['productNumber']

      bets_item['code'] = follow_info['orderInfo']['product']['code']
      bets_item['rate'] = float(follow_info['orderInfo']['product']['rate'])
      bets_item['name'] = follow_info['orderInfo']['product']['name']
      bets_item['amount'] = 1
      bet_item.append(bets_item) 
        

      summary = f"[{roomCode}盘] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[0]['rate'])} x 1.00"

      res, productnumber = self.lottery_order_api(producttype, productnumber, roomCode, playcode, bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
      if '已经封盘' in res.json()[0]['message']:
         self.sleep(5)
         res, productnumber = self.lottery_order_api(producttype, productnumber, roomCode, playcode, bet_name, 1, bet_item, str(uuid.uuid4()), certification, url)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

      bet_item.clear()
      res_json = self.response_json(res)[0]
      res_json['summary'] = summary
      res_json['productnumber'] = productnumber
      return res_json
   
   # -------------------------------------- 任務系統投注 ---------------------------------------

   # 彩票投注
   def lottery_order_misson(self, producttype, handicap_info, bet_name, bet_count, env, certification, url):

      bet_info = {}
      bets_data = []
      bet_item = []
      uuid_number = ''
      period = ''

      # 整理下注的玩法資料
      for info in handicap_info:
         bet_info['code'] = info['code']
         for plays_info in info['plays']:
            if info['plays'][plays_info]['name'] == bet_name:
               bet_info['playcode'] = plays_info
               for bet_rates in info['plays'][plays_info]['rates']:
                  bet_data = {}
                  bet_data['item_code'] = bet_rates['code']
                  bet_data['rate'] = bet_rates['rate']
                  bet_data['name'] = bet_rates['name']
                  bet_data['value'] = bet_rates['value']
                  bet_data['code'] = bet_info['code']
                  bets_data.append(bet_data)

      # 計算今年生肖該取的賠率
      this_year = f"{datetime.now().strftime('%Y')}"
      num = (int(this_year) % 12) - 4
      if num > 4 or num >= bet_count or '尾碰' in bet_name:
         num = 0

      # 下注 - prod環境隨機挑投注項下注(不重複)
      if env == '':
         for bet in sample(bets_data, bet_count):
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bets_item['value'] = bet['value']
            bet_item.append(bets_item)

         uuid_number = str(uuid.uuid4())
         period = self.get_handicap_period(producttype, certification, url)
         
         # 有兩種版型
         summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[num]['rate'])} x {gl.get_value('AMOUNT')}.00"
         summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{bet_item[0]['name']}@{('%.2f' % bet_item[num]['rate'])} x {gl.get_value('AMOUNT')}.00"
         
         res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, gl.get_value('AMOUNT'), bet_item, uuid_number, certification, url)
         if '已经封盘' in res.json()[0]['message']:
            self.sleep(5)
            res, productnumber = self.lottery_order_api(producttype, period, bets_item['handicap'],  bet_info['playcode'], bet_name, gl.get_value('AMOUNT'), bet_item, uuid_number, certification, url)
         assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
         assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

         return uuid_number, period, res.json()[0]['number'], res.json()[0]['id'], summary_1, summary_2, res.json()[0]['validationid']
      else:
         no = 1
         for bet in bets_data:
            bets_item = {}
            bets_item['code'] = bet['item_code']
            bets_item['rate'] = bet['rate']
            bets_item['name'] = bet['name']
            bets_item['amount'] = 1
            bet_item.append(bets_item)

            if no != bet_count:
               no += 1
               continue
            else:
               no = 1           

            # 有兩種版型
            total_bet = ''
            for name in bet_item:
               total_bet = total_bet + name['name'] + ','
            total_bet = total_bet[:-1]

            summary_1 = f"[{handicap_info[0]['name'][0]}盘] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[num]['rate'])} x {gl.get_value('AMOUNT')}.00"
            summary_2 = f"[{handicap_info[0]['name']}] - {bet_name}   [共1注]\n{total_bet}@{('%.2f' % bet_item[num]['rate'])} x {gl.get_value('AMOUNT')}.00"

            res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, gl.get_value('AMOUNT'), bet_item, str(uuid.uuid4()), certification, url)
            if '已经封盘' in res.json()[0]['message']:
               self.sleep(5)
               res, productnumber = self.lottery_order_api(producttype, self.get_handicap_period(producttype, certification, url), bet['code'],  bet_info['playcode'], bet_name, gl.get_value('AMOUNT'), bet_item, str(uuid.uuid4()), certification, url)
            assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
            assert res.json()[0]['status'] == 1, f"error message: {res.json()[0]['message']}"

            bet_item.clear()
            res_json = self.response_json(res)[0]
            res_json['summary_1'] = summary_1
            res_json['summary_2'] = summary_2
            res_json['productnumber'] = productnumber
            return res_json