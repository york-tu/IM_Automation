import os, sys, math, requests, json
from requests_toolbelt import MultipartEncoder
from Project.chat.apis.function_layer.base_functions import BaseFunction
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class FriendsFunction(BaseFunction):
    def search_friend(self, phone, headers, url):
        if phone == '' or headers == '' or url == '':
            raise EOFError('參數不完整')

        payload = {
            "contact": phone
        }

        url = "%sapi/v1/contacts/search" % url
        res = self.post(url, data=json.dumps(payload), header=headers,)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        return res
        
    def add_friend(self, user, headers, url):
        if user == '' or headers == '' or url == '':
            raise EOFError('參數不完整')
        
        username = user.json()['result']['username']
        
        payload = {
            "contact" : username
        }
        
        url = "%sapi/v1/users/contacts" % url

        res = self.post(url, data=json.dumps(payload), header=headers,)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'
        
    def add_groups(self, groups_name, users_id, headers, url):
        if users_id == '' or headers == '' or url == '':
            raise EOFError(f'登入資料不完整 網址:{url}')
        
        data = MultipartEncoder(
                fields={
                "display_name": groups_name,
                "user_ids": users_id
                }
            )
        
        ContentType = data.content_type
        header = {'Content-Type': ContentType}
        headers.update(header)

        url = "%sapi/v1/groups" % url
        res = self.post(url, data=data, header=headers)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        groups_id = res.json()['result']['id']
        return groups_id

    def user_ids(self, user_phone, headers, url):
        if url == '':
            raise EOFError(f'登入資料不完整 網址:{url}')
        
        data = self.search_friend(user_phone, headers, url)
        user_id = data.json()['result']['id']

        return user_id

    def get_friend_id(self, user, headers, url):
        if headers == '' or url == '':
            raise EOFError('參數不完整')
        
        url = "%sapi/v1/users/contacts" % url

        res = self.get(url, header=headers)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        username = user.json()['result']['username']

        for i in range(len(res.json()['result'])):
            if res.json()['result'][i]['username'] == username:
                user_id = res.json()['result'][i]['id']
        

                return user_id
    
    def friend_direct(self, user_id, headers, url):
        if user_id == '' or headers == '' or url == '':
            raise EOFError('參數不完整')

        payload = {
            "contact_id" : user_id
        }

        url = "%sapi/v1/groups/direct" % url
        res = self.post(url, data=json.dumps(payload), header=headers)
        assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}, 訊息:{res.text}'

        group_id = res.json()['result']['id']

        return group_id