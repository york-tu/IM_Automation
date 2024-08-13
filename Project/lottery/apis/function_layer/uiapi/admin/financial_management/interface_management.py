import requests, base64, os, datetime, json, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction

class InterfaceManagement(BaseFunction):
    def quickstart_api(self, certification, Host_ip, Port):
    # 快捷選項
        url_video = f'{Host_ip}:{Port}/connectionlink/quickstart/video'
        url_sport = f'{Host_ip}:{Port}/connectionlink/quickstart/sport'
        url_fish = f'{Host_ip}:{Port}/connectionlink/quickstart/fish'

        url_list = [url_video, url_sport, url_fish]

        for url in url_list:
            response =self.get(url)
            resp_json = self.response_json(response)
         
            if str(resp_json).__contains__('no rows in result set'):
                return

            resp_json = resp_json['pictures']
       
            for loop in range(0, len(resp_json)):
                Title = resp_json[loop]['title']
                Gameid = resp_json[loop]['gameid']

                assert resp_json[loop]['gameid'] != '', f"遊戲名稱：{Title} Gameid: {Gameid}"

    def recommend_api(self, certification,  Host_ip, Port):
    # 推薦清單
        url_sport = f'{Host_ip}:{Port}/connectionlink/recommend/sport'
        url_fish = f'{Host_ip}:{Port}/connectionlink/recommend/fish'
        url_sport_new = f'{Host_ip}:{Port}/connectionlink/recommend_new/sport'
        url_fish_new = f'{Host_ip}:{Port}/connectionlink/recommend_new/fish'

        url_list = [url_sport, url_fish, url_sport_new, url_fish_new]

        for url in url_list:
            response =self.get(url)
            resp_json = self.response_json(response)
            
            if str(resp_json).__contains__('no rows in result set'):
                return

            resp_json = resp_json['pictures']

            for loop in range(0, len(resp_json)):
                Title = resp_json[loop]['title']
                Gameid = resp_json[loop]['gameid']

                assert resp_json[loop]['gameid'] != '', f"遊戲名稱：{Title} Gameid: {Gameid}"
    
    def menubarpc_api(self, certification, Host_ip, Port):
    # 導航,根據
        url_video = f'{Host_ip}:{Port}/connectionlink/menubarpc/video'
        url_sport = f'{Host_ip}:{Port}/connectionlink/menubarpc/sport'
        url_fish = f'{Host_ip}:{Port}/connectionlink/menubarpc/fish'

        url_list = [url_video, url_sport, url_fish]
        
        for url in url_list:
            response =self.get(url)
            resp_json = self.response_json(response)
            
            if str(resp_json).__contains__('no rows in result set'):
                return

            resp_json = resp_json['pictures']

            for loop in range(0, len(resp_json)):
                Title = resp_json[loop]['title']
                Gameid = resp_json[loop]['gameid']

                assert resp_json[loop]['gameid'] != '', f"遊戲名稱：{Title} Gameid: {Gameid}"