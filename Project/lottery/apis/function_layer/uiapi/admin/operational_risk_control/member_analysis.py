import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(DIR_NAME)
from apis.pages.apis_basepage import BasePage

class MemberAnalysis(BasePage):
   def new_trace_detail(self, start_time, end_time, member, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/memberanalysis/new/trace/detail?pi=1&category=new_member&start_time={start_time}&end_time={end_time}&member_login={member}'
      res = self.get(url, certification=certification)

      return res

   def new_trace(self, start_time, end_time, member, certification, url):
      if certification == '' or url == '':
         raise EOFError('參數不完整')

      url = f'{url}apis/memberanalysis/new/trace?pi=1&ps=100&start_time={start_time}&end_time={end_time}&member_login={member}'
      res = self.get(url, certification=certification)

      return res