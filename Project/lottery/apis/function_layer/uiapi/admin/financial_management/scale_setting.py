import requests, os, sys, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class ScaleSetting(BaseFunction):
   # 更新会员设定
   def push_member_setting_api(self, certification, url, limit_num="0"):
      url = f'{url}apis/fee'

      payload = {
         "withdrawhours": "24",              # 出款時長
         "withdrawtimes": "0",               # 免費次數
         "withdrawcharge": "0",              # 出款手續
         "withdrawchargemax": "0",           # 手續上限
         'withdrawchargestatement': '0',     # 轉帳結算手續費 (UI層面上也沒有可填入的欄位了)
         "withdrawmin": "0",                 # 最小出款  
         "withdrawmax": "",                  # 最大出款
         "bankaccountlimit": limit_num,      # 出款帳號綁定數量上限 (因為這欄位太智障limit只能往上加)
         "payboxdepositlimitmin": "1",       # 入款轉帳時限 (存錢寶_測試需求)
         "auditstatus": "0",                 # 常態稽核(0: 已禁用, 1: 已啟用)
         "auditcharge": "0",                 # 稽核費用(%)
         "auditrate": "0",                   # 稽核倍數
         "auditdue": "0",                    # 放寬額度
         "memberminamount": "0",             # 最小投注額
         "memberminpoint": "0",              # 有效投注
      }

      res = self.put(url, data=payload, certification=certification)

      return res

   # 手续费用-更新会员设定
   def push_member_setting(self, certification, url):

      push_member_res = self.push_member_setting_api(certification, url)

      if push_member_res.status_code != 200 and (push_member_res.text).__contains__("出款账号绑定数量上限不得小于"):
         backcard_limit_num = (re.findall("[0-9]+", push_member_res.text))[-1]
         push_member_res = self.push_member_setting_api(certification, url, limit_num=backcard_limit_num)

      assert push_member_res.status_code == 200, f'api狀態碼不正確: {push_member_res.status_code}, 錯誤訊息: {push_member_res.text}'
      assert '已修改' in push_member_res.text, '會員設定更新失敗'

   # 手续费用-更新代理设定
   def push_agent(self, certification, url):

      url = f'{url}apis/fee/agent'

      payload = {
         'resellerdepositcharge': '1',
         'resellerdepositchargemax': '2',
         'resellerwithdrawcharge': '3',
         'resellerwithdrawchargemax': '4'
      }

      push_agent_res = self.put(url, data=payload, certification=certification)
      assert push_agent_res.status_code == 200, f'api狀態碼不正確: {push_agent_res.status_code}, 錯誤訊息: {push_agent_res.text}'
      assert '已修改' in push_agent_res.text, '代理设定更新失敗'

   # 手续费用-更新运营设定
   def push_payment(self, certification, url):

      url = f'{url}apis/payment'

      payload = {
         'items': "[{\"code\":\"365pay\",\"name\":\"365支付\",\"charge\":\"1\",\"errors\":[]},{\"code\":\"amxmy\",\"name\":\"艾米森\",\"charge\":\"2\",\"errors\":[]},{\"code\":\"baofoo\",\"name\":\"baofoo\",\"charge\":3,\"errors\":[]},{\"code\":\"bubucolin\",\"name\":\"步步高口令支付\",\"charge\":\"4\",\"errors\":[]},{\"code\":\"fengyun\",\"name\":\"风云支付\",\"charge\":\"5\",\"errors\":[]},{\"code\":\"haofu\",\"name\":\"好付支付\",\"charge\":\"6\",\"errors\":[]},{\"code\":\"heepay\",\"name\":\"heepay\",\"charge\":7,\"errors\":[]},{\"code\":\"ka101\",\"name\":\"ka101\",\"charge\":8,\"errors\":[]},{\"code\":\"mobao\",\"name\":\"mobao\",\"charge\":9,\"errors\":[]},{\"code\":\"okfpay\",\"name\":\"OK付\",\"charge\":\"10\",\"errors\":[]},{\"code\":\"ps_qa\",\"name\":\"天堂支付（QA）\",\"charge\":11,\"errors\":[]},{\"code\":\"xingfu\",\"name\":\"星付\",\"charge\":\"12\",\"errors\":[]},{\"code\":\"xingfu_qr\",\"name\":\"星付扫码\",\"charge\":\"13\",\"errors\":[]},{\"code\":\"yefoopay\",\"name\":\"yefoopay\",\"charge\":\"14\",\"errors\":[]},{\"code\":\"yemadai\",\"name\":\"yemadai\",\"charge\":15,\"errors\":[]},{\"code\":\"yitong\",\"name\":\"逸通支付\",\"charge\":\"16\",\"errors\":[]},{\"code\":\"ytbao\",\"name\":\"赢通宝\",\"charge\":\"17\",\"errors\":[]}]"
      }

      push_payment_res = self.put(url, data=payload, certification=certification)
      assert push_payment_res.status_code == 200, f'api狀態碼不正確: {push_payment_res.status_code}, 錯誤訊息: {push_payment_res.text}'
      assert '已修改' in push_payment_res.text, '运营设定更新失敗'