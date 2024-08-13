import requests, os, sys, math, time, re
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction
from datetime import datetime, timezone, timedelta

class MyProfile(BaseFunction):
   # 修改登入密码
   def change_login_password(self, oldpasswd, newpasswd, securitycode, certification, url):
      # Web
      url = f'{url}apis/my/profile/passwd?oldpasswd={oldpasswd}&newpasswd={newpasswd}&newpasswd2={newpasswd}&securitycode={securitycode}'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code} 訊息: {res.text}'

   # 修改提款密码
   def change_security_password(self, oldcode, newcode, certification, url):
      # Web
      url = f'{url}apis/my/profile/securitycode?oldcode={oldcode}&newcode={newcode}&newcode2={newcode}'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code} 訊息: {res.text}'

   # 联系方式
   def change_contact(self, email, mobile, qq, securitycode, certification, url):
      # 單跑此腳本皆可成功"200"回傳, 因此多添加time.sleep還有判斷式, 預期當機器回傳第一次400時, 再讓他跑一次.
      count = 0
      url = f'{url}apis/my/profile/contact?email={email}&mobile={mobile}&securitycode={securitycode}&qq={qq}'

      res = self.get(url, certification=certification)
      if (res.status_code != 200) and (count < 1):
         count += 1
         time.sleep(3)
         res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code} 訊息: {res.text}'

   # 绑定出款银行
   def change_bank_card(self, cardbankname, cardbranch, cardcity, securitycode, certification, url):
      #抓取銀行卡號
      source = (self.get(f'{url}my/profile/card', certification=certification)).text
      card_info = re.finditer(r'"cardnumber":.\d+', source) 
      name_info = re.finditer(r'"name":.[\u4e00-\u9fa5]+"', source) 

      for match in name_info: 
         name = ((match.group().split(','))[0].split(':'))[1]
         name = name.split('"')[1]
         break

      for match in card_info: 
         number = match.group()

      number = re.sub('\D', '', number)

      # 取得url的品牌名稱 
      url = f'{url}apis/my/profile/card?name={name}&cardnumber={number}&cardbankname={cardbankname}&cardbranch={cardbranch}&cardcity={cardcity}&securitycode={securitycode}'

      res = self.get(url, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code} 訊息: {res.text}'