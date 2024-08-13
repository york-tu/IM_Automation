import requests, os, sys, math
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta
import time,json

class initProfile(BaseFunction):
   # 取得站內消息
   def get_profile(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/profile?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_maintenance_status(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/maintenance-status?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
   
   def get_followed_matches(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/followed-matches?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_max_parlay_count(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/betslip/max-parlay-count?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_unread_count(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/messages/unread-count?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_match_count_info(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/guest-api/match-count-info?timeZone=UTC%2B08:00&deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_banners(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/banners?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_marquee(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/marquee?deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
   
   def get_announcements(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/announcements?pageIndex=1&pageSize=30&deviceToken=' + divice_token

      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_messages(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/messages?pageIndex=1&pageSize=30&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
   
   def post_read_all(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/messages/read-all?deviceToken=' + divice_token
      res = self.post(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_server_time(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/live-score/server-time?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_followed_matches(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/followed-matches?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_max_parlay_count(self, divice_token,user_token , web_url): #最大串關/組合數量
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/betslip/max-parlay-count?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_hot_matches(self, divice_token,user_token , web_url): #取的熱門賽事
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/favorite/hot/matches?labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_betslip(self, divice_token,user_token , web_url): #取得投注器資料
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/betslip?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_live_score_inplay(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/live-score/soccer/in-play?pageSize=-1&pageIndex=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_translation_short_competition(self, divice_token,user_token , web_url):
      header =  {
            # 'Content-Type': 'application/json',
            # 'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/sbk/translation/zh-CN/soccer/short-competition' 
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_translation_team(self, divice_token,user_token , web_url):
      header =  {
            # 'Content-Type': 'application/json',
            # 'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/sbk/translation/zh-CN/soccer/team'
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_translation_stage(self, divice_token,user_token , web_url):
      header =  {
            # 'Content-Type': 'application/json',
            # 'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/sbk/translation/zh-CN/soccer/stage'
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_live_score_hot(self, divice_token,user_token , web_url):
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/live-score/soccer/hot?pageSize=-1&pageIndex=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_recommend(self, divice_token,user_token , web_url): #取得推薦賽事
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      current_datetime = datetime.now()
      today_formatted_date = current_datetime.strftime("%Y-%m-%d")
      next_day = current_datetime + timedelta(days=1)
      next_day_formatted_date = next_day.strftime("%Y-%m-%d")
      today_timestamp = datetime.strptime(today_formatted_date, "%Y-%m-%d").timestamp()
      next_day_timestamp = datetime.strptime(next_day_formatted_date, "%Y-%m-%d").timestamp()
      url = f'{web_url}/api/player-api/favorite/recommend/matches?startTime={today_timestamp}&endTime={next_day_timestamp-1}&labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_upcoming_sport(self, divice_token,user_token , web_url): #取得即將賽事數量
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/upcoming/sports?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_upcoming_leagues(self, divice_token,user_token , web_url): #取得即將賽事
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/favorite/upcoming/leagues?sportID=2&labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_inplay_sports(self, divice_token,user_token , web_url): #取得滾球各球種賽事數量
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/inPlay/sports?deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'


   def get_inplay_leagues(self, divice_token,user_token , web_url): #取得滾球足球聯賽最佳盤口
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      url = f'{web_url}/api/player-api/favorite/inPlay/leagues?sportID=1&labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_preMatch_sports(self, divice_token,user_token , web_url): #早盤各球種賽事數量
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      current_datetime = datetime.now()
      today_formatted_date = current_datetime.strftime("%Y-%m-%d")
      next_day = current_datetime + timedelta(days=1)
      next_day_formatted_date = next_day.strftime("%Y-%m-%d")
      today_timestamp = datetime.strptime(today_formatted_date, "%Y-%m-%d").timestamp()
      next_day_timestamp = datetime.strptime(next_day_formatted_date, "%Y-%m-%d").timestamp()
      url = f'{web_url}/api/player-api/preMatch/sports?startTime={int(today_timestamp)}000&endTime={int(next_day_timestamp)-1}998&sportID=1&labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'

   def get_preMatch_leagues(self, divice_token,user_token , web_url): #取得早盤聯賽最佳盤口
      header =  {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user_token}' 
      }
      current_datetime = datetime.now()
      today_formatted_date = current_datetime.strftime("%Y-%m-%d")
      next_day = current_datetime + timedelta(days=1)
      next_day_formatted_date = next_day.strftime("%Y-%m-%d")
      today_timestamp = datetime.strptime(today_formatted_date, "%Y-%m-%d").timestamp()
      next_day_timestamp = datetime.strptime(next_day_formatted_date, "%Y-%m-%d").timestamp()
      url = f'{web_url}/api/player-api/favorite/preMatch/leagues?startTime={int(today_timestamp)}000&endTime={int(next_day_timestamp)-1}998&sportID=1&labelCode=1&deviceToken=' + divice_token
      res = self.get(url, header=header )
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'


   # # 刪除站內消息
   # def delete_messages(self, res, certification, web_url):

   #    for message in res.json()['Items']:
   #       url = f'{web_url}apis/my/inbox/message/del/{message["id"]}'

   #       del_res = self.delete(url, certification=certification)
   #       assert del_res.status_code == 200, f'api狀態碼不正確: {del_res.status_code}'   