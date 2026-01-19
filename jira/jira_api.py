import os, sys, requests
import json
import filetype
import common.utils.globalvar as gl

from common.web.common_api import Common
from requests_toolbelt import MultipartEncoder
from uuid import uuid4

DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)


class JiraApi(Common):
    server_url = 'https://jira.paradise-soft.com.tw'
    header = ''
    
    def jira_login(self):
        import os
        # 登入
        login_url = self.server_url + '/login.jsp'

        self.headers = {
        "Accept": "application/json",
        }

        # Get credentials from environment variables or use defaults
        username = os.getenv('JIRA_USERNAME', 'qa_admin')
        password = os.getenv('JIRA_PASSWORD', '1qaz!QAZ')
        
        payload = {
            'login': 'Log in',
            'os_username': username,
            'os_password': password
        }
        try:
            response, session = self.login(login_url, data=payload, header=self.headers)
        except Exception:
            response, session = self.login(login_url, data=payload, header=self.headers)

        status = response.headers['X-Seraph-LoginReason']
    
        return session

    def upload_testcase_img(self, certification):
        img_path_list = []
        url = self.server_url + '/rest/tests/1.0/attachment/embeddedimage'

        if gl.get_value('IMG_PATH') == None:
            return
        
        # 把截圖轉換二進制並上傳至JIRA圖庫
        for file_path in gl.get_value('IMG_PATH'):
            file_name = os.path.basename(file_path)
            file_type = filetype.guess(file_path)
            mime_type = file_type.mime   #image/jpeg
            with open(file_path,"rb") as f:
                img_bin = f.read()
                f.close()
            boundary_value = uuid4().hex
            boundary = '--{0}'.format(boundary_value)

            fields = {"file": (file_name, img_bin, mime_type)}
            encode_data = MultipartEncoder(fields, boundary)
            ContentType = encode_data.content_type

            self.headers = {
                'content-type': ContentType,  
            }
            response = self.post(url, certification=certification, data=encode_data, header=self.headers)
            assert response.status_code == 201 or response.status_code == 200, f'api狀態碼不正確: {response.status_code}'

            img_path_list.append(response.text)

        return img_path_list

    def set_cycle_result(self, certification, cycle_key, testcase_key, status):
        # 依照結果給予適當的comment
        if gl.get_value('ERROR') != [] and gl.get_value('ERROR') != None:
            comment = gl.get_value('ERROR')[-1][1].replace('\n','<br>')
        elif gl.get_value('FAILURE') != [] and gl.get_value('FAILURE') != None:
            comment = gl.get_value('FAILURE')[-1][1].replace('\n','<br>')
        else:
            comment = 'automation test'

        if status != 'pass' and status != 'skip':
            last_comment = comment.split('<br>')[-2]
            img_path_list = self.upload_testcase_img(certification)

            if img_path_list == None:
                comment = f'Result: <span style="color: rgb(184, 49, 47);">{last_comment}</span><br><br><br><br>Report:<br>' + comment
            else:
                imgs_comment = ''
                for img_path in img_path_list:
                    # import json
                    # Parse JSON string safely instead of using eval()
                    img_data = json.loads(img_path) if isinstance(img_path, str) else img_path
                    img_link = img_data.get('link', '') if isinstance(img_data, dict) else str(img_path)
                    img_comment = f'<img src=\"{img_link}\" style=\"width: 300px;\" class=\"fr-fil fr-dib\">'
                    imgs_comment += img_comment
                comment = f'Result: <span style="color: rgb(184, 49, 47);">{last_comment}</span><br>' + imgs_comment + 'Report:<br>' + comment

        # 構建 Platform 欄位值（包含 iOS 版本）
        phone_name = gl.get_value("PHONE_NAME", "").upper()
        phone_platform = gl.get_value("PHONE_PLATFORM", "")
        os_version = gl.get_value("OS_VERSION", "")
        
        # 如果是 iOS 設備且有版本信息，則組合顯示
        if phone_platform == 'iOS' and os_version:
            # 格式化：IPHONE_15_PRO (iOS18.2) 或 IPHONE_15_PRO (iOS26.2)
            platform_value = f'{phone_name} ({os_version})'
        else:
            # 非 iOS 或沒有版本信息時，只顯示設備名稱
            platform_value = phone_name

        # 把測試結果上傳JIRA
        url = f'{self.server_url}/rest/atm/1.0/testrun/{cycle_key}/testcase/{testcase_key}/testresult'
        self.headers = {
            'content-type': "application/json",
            }
        data = {
            "environment": f"{gl.get_value('BRAND').upper()}_{gl.get_value('ENV').upper()}",
            "comment": f'{comment}',
            "status": f'{status}',
            "customFields": {
                "Build Version": f'{gl.get_value("APP_VERSION")}',
                "Platform": platform_value,
                "Test Type": f"{gl.get_value('TEST_TYPE').upper()}",
                "Duration": f"{gl.get_value('Duration')}"
            }
        }

        response = self.post(url, certification=certification, data=json.dumps(data), header=self.headers)
        
        # 當cycle沒有testcase的時候會產生500,當下無法給我pass or fail,固再進行一次put修改
        if response.status_code == 500:
            response = self.put(url, certification=certification, data=json.dumps(data), header=self.headers)

        if response.text.__contains__('id'):
            message = ((response.text).split(':'))[1]
            assert response.status_code == 201 or response.status_code == 200, f'\ncode:{response.status_code},\
                 \nresponse:{message}\ncycle:{cycle_key},testcase_key:{testcase_key}, status:{status}'