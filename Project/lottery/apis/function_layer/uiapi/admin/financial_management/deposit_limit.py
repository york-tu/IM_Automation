import requests, base64, os, sys, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction

class DepositLimit(BaseFunction):
    # 上分連點限制設定API (關閉連點限制)
    def set_deposit_limit_api(self, certification, admin_url, limitstatus='0'):
        gets = self.get_info(certification, admin_url)
        for list in range(0, len(gets)):
            id = gets[list]["id"]
            memberlevel = self.get_level_info(certification, admin_url)
            data = {
                'id': id,
                'limitstatus': "0",
                'limittime': "5",
                'memberlevel': memberlevel,
            }
            url = "%sapis/setting/deposit/category/limit/%s" % (admin_url, id)
            res = self.put(url, data, certification)
            assert res.status_code == 200 or res.status_code == 204, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

    # 抓取線上存款內容
    def get_info(self, certification, admin_url):
        Querystring = {"contents": "", "langcode": "", "status": "-1", "pi": "1", "ps": "25", "po": "sort asc"}
        url = "%sapis/marketing/member/deposit/category" % admin_url
        response = self.get(url, Querystring, certification, self.header())
        get = self.response_json(response)
        return get

    # 抓取會員層級內容
    def get_level_info(self, certification, admin_url):
        url = "%sapis/marketing/member/deposit/category/limit" % admin_url
        response = self.get(url,'', certification, self.header())
        get = self.response_json(response)

        level_len = get[0]['memberlevel'].count(',')+1
        memberlevel = ''
        for i in range(1,level_len):
            memberlevel += str(i) + ','
        memberlevel += str(level_len)
        
        return memberlevel