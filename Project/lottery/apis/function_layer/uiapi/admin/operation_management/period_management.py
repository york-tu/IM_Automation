import requests, base64, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class PeriodManagement(BaseFunction):
    
    def get_period(self, certification, game, period_num, url):
        num = 0
        period_list = []
        api_url = f"{url}apis/lottery/{game}/periods"
        querystring = {"status": "1", "pi": "1", "ps": "25"}

        period_info = self.get(api_url, querystring, certification)
        code = period_info.status_code
        
        assert code == 200,f"撈取資料錯誤 訊息: {code}"

        period_json = self.response_json(period_info)

        for num in range(0, period_num + 5):
            try:
                Period = period_json['data']['Items'][num]['number']
                period_list.append(Period)
            except:
                raise EOFError(f'解析錯誤 {Period}')
        
        return period_list

    def change_period(self, certification, game, period_num, period_list, ball_number, url):
        num = 0
        api_url = f"{url}apis/lottery/{game}/period/"
        Sync_url = f"{url}apis/lottery/period/revise"
        data = {"balls": ball_number}
        
        for num in range(0, period_num):
            Period = period_list[num]

            Sync_data = {
            "number": Period,
            "product": game,
            "brand": '',
            }

            # 修改球號
            set_url = f"{api_url}{Period}"
            modify = self.put(set_url, data, certification)
            period_json = self.response_json(modify)
            result = period_json['message']

            assert result == "资料更新成功", f"修改球號錯誤,訊息: {result}"
            print(f"修改: {result}")

            # 期數同步
            modify = self.post(Sync_url, Sync_data, certification)
            Status = modify.status_code
            period_json = self.response_json(modify)
            result = period_json['message']

            assert Status == 200, f"同步球號錯誤,訊息: {Status}"
            print(f"同步: {result}")

    def statistical_data(self):
        pass


    def show_result(self):
        pass

        