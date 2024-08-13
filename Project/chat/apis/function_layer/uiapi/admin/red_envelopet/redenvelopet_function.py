import os, sys, math, requests, json
from re import T
import uuid
from Project.chat.apis.function_layer.base_functions import BaseFunction
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)

class RedEnvelopetFunction(BaseFunction):
    def send_red_envelopes(self, group_id, content, headers, url):
        if group_id == '' or content == '' or headers == '' or url == '':
            raise EOFError('參數不完整')
        