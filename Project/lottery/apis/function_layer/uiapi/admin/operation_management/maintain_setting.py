import requests, base64, os, datetime, json, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction
from lottery.web.testcases.base_testcase import BaseTestCase

class MaintainSetting(BaseFunction, BaseTestCase):
    def get_all_lottery_api(self, Admin_url, Host_ip, Port):
        url= f'{Host_ip}:{Port}/connectionlink/menubarpc/lottery'
        Querystring = {"contents": "", "langcode": "", "status": "-1", "pi": "1", "ps": "25", "po": "sort asc"}
        Response_info = self.get(url, Querystring)
        Resp_json = self.response_json(Response_info)['pictures']
        Name_list = []

        for name in range(0,len(Resp_json)):
            Name_list.append(Resp_json[name]['code'])

        return Name_list
        
      
    def set_lottery_status(self, certification, Admin_url, Host_ip, Port, Lottery_name):
        On_off = 1
        try:
            for name in Lottery_name:
                url = f'{Admin_url}apis/lottery/{name}/settings'
                if name == 'newam6':
                    open = 1200
                    close = 900
                elif name == 'smam6':
                    open = 5
                    close = 300
                else:
                    open = 0
                    close = 10
                data = {"appstatus": On_off, "status": On_off, "auto": On_off, "autopayout": On_off, "open":open, "close":close}
                resp = self.put(url, data, certification)
        except:
            Error_code = resp.status_code
            Error_message = resp.text
            raise EOFError(f'開啟彩票開關錯誤 彩種:{name} 錯誤代碼:{Error_code} 錯誤訊息:{Error_message}')



