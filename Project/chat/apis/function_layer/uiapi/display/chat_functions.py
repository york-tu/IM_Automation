import os, sys, math, requests, json
from re import T
import uuid
from Project.chat.apis.function_layer.base_functions import BaseFunction
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class ChatFunction(BaseFunction):
    def get_uuid(self):
        cid = uuid.uuid4()
        my_cid = str(cid)

        return my_cid

    def send_message(self, group_id, content, headers, url, uuid):
        if group_id == '' or content == '' or headers == '' or url == '':
            raise EOFError('參數不完整')
        
        payload = {
            "cid" : uuid,
            "type" : "text",
            "group_id" : group_id,
            "text" : content
        }
        
        url = "%sv1/messages" % url

        res = self.post(url, data=json.dumps(payload), header=headers,)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

    def do_send_messages(self, group_id, count, seconds, headers, url, sync):
        text = "測試TeSt12345!@#$%测试"
        
        num = 0
        for _ in range(0,count,1):
            if sync == True:
                cid = self.get_uuid()
            else:
                cid = ''

            content = str(text) + '-' +str(num)
            self.send_message(group_id, content, headers, url, cid)

            self.sleep(seconds=seconds)
            num = num+1
    
    def get_groups_id(self, name, headers, url):
        if url == '':
            raise EOFError(f'登入資料不完整 網址:{url}')

        url = "%sv1/users/groups/part" % url
        
        res = self.get(url, header=headers)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        groups_count = len(res.json()['result']['groups'])
        for num in range(0,groups_count):
            display_name = res.json()['result']['groups'][num]['display_name']
            if display_name == name:
                groups_id = res.json()['result']['groups'][num]['id']

                return(groups_id)
            
            else:
                pass
        raise EOFError(f'查無群組 群組名稱:{name}')

    def get_members_id(self, name, headers, url):
        if url == '':
            raise EOFError(f'登入資料不完整 網址:{url}')

        url = "%sv1/users/groups/part" % url
        
        res = self.get(url, header=headers)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        groups_count = len(res.json()['result']['dms'])
        for num in range(0,groups_count):
            display_name = res.json()['result']['dms'][num]['name']
            if display_name.__contains__(name) :
                groups_id = res.json()['result']['dms'][num]['id']

                return(groups_id)
            
            else:
                pass
        raise EOFError(f'查無群組 群組名稱:{name}')
    
    def get_redenvelope(self, red_id, headers, url):
        if url == '' or headers == '':
            raise EOFError(f'登入資料不完整 網址:{url} 登入狀態:{headers}' )

        url = "%sapi/v1/campaigns/%s/red-envelopes" % (url, red_id)

        res = self.post(url, header=headers)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

    def send_verification(self, nation, phone, headers):
        if headers == '':
            raise EOFError(f'登入資料不完整 登入狀態:{headers}' )
        
        url = "https://web-guchat.com/api/v1/verification"
        uuid = self.get_uuid()
        phone_text = str(phone)

        payload = {
            "country": nation,
            "phone": phone_text,
            "device_id": uuid
        }

        res = self.post(url, data=json.dumps(payload), header=headers)
        assert res.status_code == 204 or res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'