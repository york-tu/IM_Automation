import requests, base64, os, sys, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction

class HandlingFee(BaseFunction):
    # 手續費用設定API
    def set_charge_max_api(self, certification, admin_url, limit_num='4'):
        Querystring = {
            "withdrawchargemax": "0", 
            "withdrawcharge": "0", 
            "bankaccountlimit": limit_num
            }

        url = "%sapis/fee" % admin_url
        res = self.put(url, Querystring, certification)
        
        return res

    # 手續費用設定
    def set_charge_max(self, certification, admin_url):
        res = self.set_charge_max_api(certification, admin_url)

        if res.status_code != 200 and (res.text).__contains__("出款账号绑定数量上限不得小于"):
            limit_num = (re.findall("[0-9]+", res.text))[-1]
            res = self.set_charge_max_api(certification, admin_url, limit_num=limit_num)
        
        assert res.status_code == 200, f'手續費用設定失敗, code:{res.status_code}, message:{res.text}'