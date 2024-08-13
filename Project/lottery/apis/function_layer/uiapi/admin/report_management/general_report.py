import requests, os, sys, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta

class GeneralReport(BaseFunction):
    # 一般報表-取得報表資料
    def get_channel_recode(self, shareholder, startaddedtime, endaddedtime, certification, url):
        url =  f'{url}/apis/reports/generalreport?start_time={startaddedtime}&end_time={endaddedtime}&share_login={shareholder}&po=order_count+desc&pi=1&ps=25&level=2'
        
        res = self.get(url, certification=certification)
        return res
    
    # 一般報表-整理報表資料
    def get_general_detail(self, shareholder, certification, url):
        start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
        end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
        res = {'channel':[],'recode':[]}
        
        get_general_res = self.get_channel_recode(shareholder, start_time, end_time, certification, url)
        assert get_general_res.status_code == 200, f'api狀態碼不正確: {get_general_res.status_code}, 訊息:{get_general_res.text}'
        
        channel_list=[]
        recode = []
        for i in range(len(get_general_res.json())-1):
            channel = get_general_res.json()[i]['channel_code']
            total = (get_general_res.json()[i]['Pager']['stat']['order_count'])
            amount = (get_general_res.json()[i]['Pager']['stat']['total'])
            earning = (get_general_res.json()[i]['Pager']['stat']['earning'])
            point = (get_general_res.json()[i]['Pager']['stat']['point'])
            channel_list.append(channel)
            recode.append([channel,total,amount,earning,point])
        
        res['channel'].append(channel_list)
        res['recode'].append(recode)

        assert res != {}, '無法取得注單列表資料'

        return res

    # 一般報表-核對資料
    def check_general_report(self, shareholder, kind, certification, url):      
        general_res = self.get_general_detail(shareholder, certification, url)
        channel_list = general_res['channel']
        
        assert channel_list != [[]], '時間區段無資料'

        order_res = self.get_shareholder_betting(shareholder, kind, certification, url, channel_list)

        for i in range(len(general_res['channel'])):
            assert general_res['recode'][0][i][1] == order_res['recode'][0][i][1],  f"總單數不正確 報表顯示為: {general_res['recode'][0][i][1]} 注單中心顯示為: {order_res['recode'][0][i][1]}"
            assert general_res['recode'][0][i][2] == order_res['recode'][0][i][2],  f"注額不正確 報表顯示為: {general_res['recode'][0][i][2]} 注單中心顯示為: {order_res['recode'][0][i][2]}"
            assert general_res['recode'][0][i][3] == order_res['recode'][0][i][3],  f"損益不正確 報表顯示為: {general_res['recode'][0][i][3]} 注單中心顯示為: {order_res['recode'][0][i][3]}"
            assert general_res['recode'][0][i][4] == order_res['recode'][0][i][4],  f"有效投注不正確 報表顯示為: {general_res['recode'][0][i][4]} 注單中心顯示為: {order_res['recode'][0][i][4]}"

    # 注單中心-取得注單列表
    def get_shareholder_order(self, shareholder, kind, startaddedtime, endaddedtime, certification, url, channel=''):
        if kind == 'add':
           url = f'{url}apis/order?status=1&start_added_time={startaddedtime}&end_added_time={endaddedtime}&pi=1&ps=25'
        elif kind == 'payout':
           url = f'{url}apis/order?status=1&start_payout_time={startaddedtime}&end_payout_time={endaddedtime}&pi=1&ps=25'
       
        if shareholder != '':
           url = url + f'&share_login={shareholder}'
       
        if channel == 'total':
            pass
        elif channel !='':
            url = url + f'&channel_code={channel}'

        res = self.get(url, certification=certification)
        return res

    # 注單中心-取得注單列表的總計資料
    def get_shareholder_betting(self, shareholder, kind, certification, url, channel_list):
        start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
        end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) + timedelta(days=1)).strftime('%Y-%m-%d')} 00:00"
        res = {'recode':[]}
        
        recode = []
        for channel in channel_list[0] :
            get_order_res = self.get_shareholder_order(shareholder, kind, start_time, end_time, certification, url, channel)
            assert get_order_res.status_code == 200, f'api狀態碼不正確: {get_order_res.status_code}, 訊息:{get_order_res.text}'

            channel = channel
            total = get_order_res.json()['Pager']['Total']
            amount = get_order_res.json()['Pager']['stat']['total']
            earning = get_order_res.json()['Pager']['stat']['income']
            point = get_order_res.json()['Pager']['stat']['point']
            recode.append([channel,total,amount,earning,point])
        
        res['recode'].append(recode)
    
        assert res != {}, '無法取得注單列表資料'
        
        return res