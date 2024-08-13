# -- coding: utf-8 --**
import os, sys, json
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from datetime import *
from apis.function_layer.base_functions import BaseFunction


class EventManagement(BaseFunction):
    
    # 取得指定任務ID
    def get_mission_id(self, certification, url, mission_name):
        url = f'{url}apis/missionsys/campaign/list'

        querystring = {
            'campaign_status': 2,
            'central_display': 'true',
            'index': 1,
            'size': 500,
        }

        mission_data = self.get(url, certification=certification, querystring=querystring)
        assert mission_data.status_code == 200, f'api狀態碼不正確: {mission_data.status_code}'

        mission_list = mission_data.json()['data']['campaigns']

        for i in mission_list:
            if i['name'] == mission_name:
                mission_id = i['id']
                campaign_no = i['campaign_no']
                return mission_id, campaign_no
        
        raise EOFError('比對不到任務')
    
    # 取得指定任務期數
    def get_mission_period(self, certification, url, mission_id):
        url = f'{url}apis/missionsys/campaign/periods/autoreward'

        querystring = {
            'campaign_unique_id': mission_id,
            'index': 1,
            'size': 25,
        }

        period_data = self.get(url, certification=certification, querystring=querystring)
        assert period_data.status_code == 200, f'api狀態碼不正確: {period_data.status_code}'

        period_list = period_data.json()['data']['periods']

        for i in period_list:
            if i['settle_status'] == 2 and i['reward_status'] == 2:      # 1:待統計/待派發, 2:統計中/派發中, 3:已完成/已完成
                period_id = i['id']
                period_no = i['period_no']
                return period_id, period_no
    
    # 確認玩家達成任務狀態
    def check_mission_status_of_user(self, brand, period_id, account):
        url = f'https://mission-uat.wit.pstdsf.com/period/{period_id}/member/{account}/statistics'

        header = {
            'BrandCode': brand,
            'Accept':'application/json',
        }

        turn = 121

        for x in range(turn):
            user_data = self.get(url, header=header)
            try:
                assert user_data.status_code == 200, f'api狀態碼不正確: {user_data.status_code}'
                user_data.json()['data']
                break
            except:
                self.sleep(5)
            if x == 120:
                raise EOFError('任務狀態還沒有被統計')
    
    # 驗證明細頁達成任務
    def verify_detail(self, certification, url, account, period_id, expected_amount):
        url = f'{url}apis/missionsys/period/{period_id}/reward/single/list'

        querystring = {
            'member_id': account,
            'index': 1,
            'size': 25,
        }

        for x in range(25):
            detail = self.get(url, certification=certification, querystring=querystring)
            assert detail.status_code == 200, f'api狀態碼不正確: {detail.status_code}'

            detail_list = detail.json()['data']['items']
            if detail_list != []:
                break
            elif x == 24:
                raise EOFError('已派金額未出現或明細不正確')
            else:
                self.sleep(5)

        amount_dict = {}
        for i in detail_list:
            amount_dict[i['threshold_index']] = float(i['rewarded_amount'])

        for y in range(len(expected_amount)):
            if round(expected_amount[y],2) != round(amount_dict[y+1],2):
                raise EOFError(f'明細已派金額不正確: 預期金額:{round(expected_amount[y],2)}, 實際金額:{round(amount_dict[y+1],2)}')
                
        return amount_dict
    
    # 驗證人工存入
    def verify_mandeposit(self, certification, url, account, mission_name, campaign_no, period_no, amount_dict):
        url = f'{url}apis/mandeposit'

        today_start = self.get_us_time().date()
        tomorrow_start = today_start + timedelta(days=1)

        querystring = {
            'member_login': account,
            'status': 1,
            'ps': 25,
            'pi':1,
            "start_added_time": f'{today_start} 00:00',
            "end_added_time": f'{tomorrow_start} 00:00',
        }

        mandeposit = self.get(url, certification=certification, querystring=querystring)
        assert mandeposit.status_code == 200, f'api狀態碼不正確: {mandeposit.status_code}'

        mandeposit_data = mandeposit.json()['Items']

        # 把每個dict驗證資料放進list
        verify_data = [{"campaignId":campaign_no,"campaignName":mission_name,"periodId":period_no,"thresholdIndex":x+1,"discount_amount":round(amount_dict[x+1],2)} for x in range(len(amount_dict.keys()))]

        count = 0
        for i in mandeposit_data:
            if mission_name in i['remark']:
                remark_dict = json.loads(i['remark'].replace('\\',''))
                del remark_dict['payoutType']
                remark_dict['discount_amount'] = round(i['discount_amount'],2)       # 處理備註資料以便比對數據
                if remark_dict not in verify_data:
                    raise EOFError(f'人工存入資料比對不正確, 人工存入資料:{remark_dict}')
                else:
                    count += 1
        if count == 0:
            raise EOFError('沒有活動明細資料')
        else:
            assert count == len(verify_data), f'人工存入筆數不正確: 實際{count}筆, 預期{len(verify_data)}筆'




