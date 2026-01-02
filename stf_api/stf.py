# coding=utf-8

import requests
import json
import logging

logging.basicConfig(level=logging.WARNING)

import os

# for linux server
stf_url = os.getenv('STF_URL', 'http://10.200.6.1:7100')
# Get STF auth token from environment variable or use default
auth_token = os.getenv('STF_AUTH_TOKEN', '5919cbb37a484e12b65cd65fda9d376337c8a219e96e46fb93a2afb545d047c5') # qa_admin@paradise-soft.com.tw

# for mac server
# stf_url = 'http://10.200.202.85:7100'
# auth_token = '4a2449b428cc4128b1892601f2681e97cb91511315064df18ba18d407879db7c' # qa token

# 取得 remote 手機info
def get_phone_list():
    url = f'{stf_url}/api/v1/devices'

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        res = requests.request('GET', url, headers=headers).json()['devices']
        return res
    except Exception:
        logging.exception('exception log')
        return None

# 使用指定的手機
def post_use_phone(phone_serial):
    url = f'{stf_url}/api/v1/user/devices'

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    try:
        data = {"serial":phone_serial}
        jsonbody = json.dumps(data)
        
        res = requests.request('POST', url, headers=headers, data=jsonbody).json()
        return res
    except Exception:
        logging.exception('exception log')
        return None

# 連接特定手機
def post_connect_phone(phone_serial):
    url = f'{stf_url}/api/v1/user/devices/{phone_serial}/remoteConnect'

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        res = requests.request('POST', url, headers=headers).json()['remoteConnectUrl']
        return res
    except Exception:
        logging.exception('exception log')
        return None

# 取消連接特定手機
def post_disconnect_phone(phone_serial):
    url = f'{stf_url}/api/v1/user/devices/{phone_serial}'

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        res = requests.request('DELETE', url, headers=headers).json()
        return res
    except Exception:
        logging.exception('exception log')
        return None

#取得特定手機資訊
def get_phone_info(phone_serial):
    url = f'{stf_url}/api/v1/devices/{phone_serial}'

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        res = requests.request('GET', url, headers=headers).json()
        return res
    except Exception:
        logging.exception('exception log')
        return None