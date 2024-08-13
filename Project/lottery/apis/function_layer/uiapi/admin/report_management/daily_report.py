import requests, os, sys, pytz
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timedelta
from decimal import Decimal

class DailyReport(BaseFunction):
    # 每日報表-取得報表資料
    def get_daily_recode(self, shareholder, startaddedtime, endaddedtime, certification, url):
        url =  f'{url}apis/reports/dailyreporting?start_time={startaddedtime}&end_time={endaddedtime}&share_login={shareholder}'
        
        res = self.get(url, certification=certification)
        return res
    
    def get_daily_detail(self, shareholder, certification, url):
        start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) - timedelta(days=3)).strftime('%Y-%m-%d')} 00:00"
        end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4)).strftime('%Y-%m-%d')} 00:00"
        res = {'day':[],'deposit':[],'order':[],'register':[],'login':[]}
        get_daily_res = self.get_daily_recode(shareholder, start_time, end_time, certification, url)
        assert get_daily_res.status_code == 200, f'api狀態碼不正確: {get_daily_res.status_code}, 訊息:{get_daily_res.text}'

        day_list = []
        deposit_list = []
        order_list = []
        register_list = []
        login_list = []
        for i in range(len(get_daily_res.json()['Items'])):
            day = get_daily_res.json()['Items'][i]['day'] #日期
            register_count = get_daily_res.json()['Items'][i]['register_count'] #註冊數
            login_count = get_daily_res.json()['Items'][i]['login_count'] #登入數
            first_count = get_daily_res.json()['Items'][i]['first_deposit_count'] #首儲數
            first_amount = get_daily_res.json()['Items'][i]['first_deposit_amount'] #首儲額
            deposit_count = get_daily_res.json()['Items'][i]['deposit_count'] #上分數
            deposit_member = get_daily_res.json()['Items'][i]['deposit_member'] #上分人數
            deposit_amount = get_daily_res.json()['Items'][i]['deposit_amount'] #上分額
            deposit_discount = get_daily_res.json()['Items'][i]['deposit_discount'] #上分優惠
            deposit_charge = get_daily_res.json()['Items'][i]['deposit_charge'] #上分手續費
            withdraw_count = get_daily_res.json()['Items'][i]['withdraw_count'] #下分數
            withdraw_amount = get_daily_res.json()['Items'][i]['withdraw_amount'] #下分額
            withdraw_fee = get_daily_res.json()['Items'][i]['withdraw_fee'] #下分手續費
            order_count = get_daily_res.json()['Items'][i]['order_count'] #投注數
            total = get_daily_res.json()['Items'][i]['order_total'] #投注額
            point = get_daily_res.json()['Items'][i]['order_point'] #打碼量
            earning = get_daily_res.json()['Items'][i]['order_earning'] #損益
            rebate = get_daily_res.json()['Items'][i]['rebate'] #返水
            
            deposit_list.append([
                first_count,first_amount,deposit_count,deposit_member,
                deposit_amount,deposit_discount,deposit_charge,
                withdraw_count,withdraw_amount,withdraw_fee])
            login_list.append(login_count)
            register_list.append(register_count)
            order_list.append([order_count,total,point,earning,rebate])
            day_list.append(day)
        
        res['day'] = day_list
        res['deposit'].append(deposit_list)
        res['order'].append(order_list)
        res['register'].append(register_list)
        res['login'].append(login_list)

        assert res != {}, '無法取得注單列表資料'

        return res

    # 核對-每日報表-注單金額
    def check_daily_order(self, shareholder, kind, certification, url):
        daily_res = self.get_daily_detail(shareholder, certification, url)
        day_list = daily_res['day']

        order_res = self.get_shareholder_betting(shareholder, kind, certification, url, day_list)
        for i in range(len(daily_res['day'])):
            assert daily_res['order'][0][i][0] == order_res['recode'][0][i][0], f"投注數不正確 報表顯示為: {daily_res['order'][0][i][0]} 注單中心顯示為: {order_res['recode'][0][i][0]}"
            assert daily_res['order'][0][i][1] == order_res['recode'][0][i][1], f"投注額不正確 報表顯示為: {daily_res['order'][0][i][1]} 注單中心顯示為: {order_res['recode'][0][i][1]}"
            assert daily_res['order'][0][i][2] == order_res['recode'][0][i][2], f"打碼量不正確 報表顯示為: {daily_res['order'][0][i][2]} 注單中心顯示為: {order_res['recode'][0][i][2]}"
            assert daily_res['order'][0][i][3] == order_res['recode'][0][i][3], f"損益不正確 報表顯示為: {daily_res['order'][0][i][3]} 注單中心顯示為: {order_res['recode'][0][i][3]}"
            assert daily_res['order'][0][i][4] == order_res['recode'][0][i][4], f"返水不正確 報表顯示為: {daily_res['order'][0][i][4]} 注單中心顯示為: {order_res['recode'][0][i][4]}"

    # 核對-每日報表-上下分金額
    def check_daily_overview(self, shareholder, certification, url):
        daily_res = self.get_daily_detail(shareholder, certification, url)
        day_list = daily_res['day']

        overview_res = self.get_overview_recode(shareholder, certification, url, day_list)
        for i in range(len(daily_res['day'])):
            assert daily_res['deposit'][0][i][5] == overview_res['recode'][0][i][0], f"上分優惠不正確 報表顯示為: {daily_res['deposit'][0][i][5]} :上分總攬顯示為: {overview_res['recode'][0][i][0]}"
            assert daily_res['deposit'][0][i][4] == overview_res['recode'][0][i][1], f"上分額不正確 報表顯示為: {daily_res['deposit'][0][i][4]} 上分總攬顯示為: {overview_res['recode'][0][i][1]}"
            assert daily_res['deposit'][0][i][6] == overview_res['recode'][0][i][2], f"上分手續費不正確 報表顯示為: {daily_res['deposit'][0][i][6]} 上分總攬顯示為: {overview_res['recode'][0][i][2]}"
            assert daily_res['deposit'][0][i][8] == overview_res['recode'][0][i][3], f"下分額不正確 報表顯示為: {daily_res['deposit'][0][i][8]} 下分總攬顯示為: {overview_res['recode'][0][i][3]}"
            assert daily_res['deposit'][0][i][7] == overview_res['recode'][0][i][4], f"下分數不正確 報表顯示為: {daily_res['deposit'][0][i][7]} 下分總攬顯示為: {overview_res['recode'][0][i][4]}"
            assert daily_res['deposit'][0][i][9] == overview_res['recode'][0][i][5], f"下分手續費不正確 報表顯示為: {daily_res['deposit'][0][i][9]} 下分總攬顯示為: {overview_res['recode'][0][i][5]}"

    # 注單中心-取得注單列表
    def get_shareholder_order(self, shareholder, kind, startaddedtime, endaddedtime, certification, url):
        if kind == 'add':
           url = f'{url}apis/order?status=1&start_added_time={startaddedtime}&end_added_time={endaddedtime}&pi=1&ps=25'
        elif kind == 'payout':
           url = f'{url}apis/order?status=1&start_payout_time={startaddedtime}&end_payout_time={endaddedtime}&pi=1&ps=25'
       
        if shareholder != '':
           url = url + f'&share_login={shareholder}'

        res = self.get(url, certification=certification)
        return res

    # 注單中心-取得注單列表的總計資料
    def get_shareholder_betting(self, shareholder, kind, certification, url, day_list):
        res={'recode':[]}
        recode=[]
        for i in range(len(day_list[0])):
            start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) - timedelta(days=i+1)).strftime('%Y-%m-%d')} 00:00"
            end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) - timedelta(days=i)).strftime('%Y-%m-%d')} 00:00"
       
            get_order_res = self.get_shareholder_order(shareholder, kind, start_time, end_time, certification, url)
            assert get_order_res.status_code == 200, f'api狀態碼不正確: {get_order_res.status_code}, 訊息:{get_order_res.text}'

            total = get_order_res.json()['Pager']['Total']
            amount = get_order_res.json()['Pager']['stat']['total']
            point = get_order_res.json()['Pager']['stat']['point']
            earning = get_order_res.json()['Pager']['stat']['income']
            rebate = get_order_res.json()['Pager']['stat']['rebate']
            recode.append([total,amount,point,earning,rebate])
        
        res['recode'].append(recode)

        assert res != {}, '無法取得注單列表資料'
        
        return res

    # 上下分總攬-取得上下分列表
    def get_shareholder_overview(self, shareholder, startaddedtime, endaddedtime, certification, url, lucre=''):
        if lucre == 'deposit':
            url = f'{url}apis/deposit/overview?currency_code=RMB&share_login={shareholder}&start_time={startaddedtime}&end_time={endaddedtime}&pi=1&ps=25'
        elif lucre == 'withdraw':
            url = f'{url}apis/withdraw/overview?currency_code=RMB&share_login={shareholder}&start_time={startaddedtime}&end_time={endaddedtime}&pi=1&ps=25'
        
        res = self.get(url, certification=certification)
        return res

    # 上下分總攬-取得上下分列表的總計資料
    def get_overview_recode(self, shareholder, certification, url, day_list ):    
        res={'recode':[]}
        recode=[]
        for i in range(len(day_list[0])):
            start_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) - timedelta(days=i+1)).strftime('%Y-%m-%d')}+00:00"
            end_time = f"{(datetime.now().astimezone(pytz.utc) + timedelta(hours=-4) - timedelta(days=i)).strftime('%Y-%m-%d')}+00:00"

            get_deposit_overview = self.get_shareholder_overview(shareholder, start_time, end_time, certification, url, 'deposit')
            assert get_deposit_overview.status_code == 200, f'api狀態碼不正確: {get_deposit_overview.status_code}, 訊息:{get_deposit_overview.text}'

            get_withdraw_overview = self.get_shareholder_overview(shareholder, start_time, end_time, certification, url, 'withdraw')
            assert get_withdraw_overview.status_code == 200, f'api狀態碼不正確: {get_withdraw_overview.status_code}, 訊息:{get_withdraw_overview.text}'

            deposit_discount = get_deposit_overview.json()['Pager']['stat']['discount_amount']
            deposit_amount = get_deposit_overview.json()['Pager']['stat']['transfer_amount']
            deposit_charge = get_deposit_overview.json()['Pager']['stat']['transfer_charge']
            withdraw_amount = get_withdraw_overview.json()['Pager']['stat']['transfer_amount']
            withdraw_count = get_withdraw_overview.json()['Pager']['Total']
            withdraw_all_amount = get_withdraw_overview.json()['Pager']['stat']['amount']
            withdraw_fee = Decimal(str(withdraw_all_amount)) - Decimal(str(withdraw_amount))
            recode.append([deposit_discount, deposit_amount, deposit_charge, withdraw_amount, withdraw_count, float(withdraw_fee)])
        
        res['recode'].append(recode)

        assert res != {}, '無法取得上分&下分總攬列表資料'

        return res
