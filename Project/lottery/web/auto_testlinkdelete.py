import testlink
import datetime
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
sys.path.append('..')

url = "http://testlink.paradise-soft.com.tw/lib/api/xmlrpc/v1/xmlrpc.php"
key = "8fb7f0607afadcf81370a77ce152b79f"
tlc = testlink.TestlinkAPIClient(url, key)

chrome_path = "./Driver/chromedriver.exe"

#登入Testlink

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get('http://testlink.paradise-soft.com.tw/index.php')
wait = WebDriverWait(driver, 20)
account = driver.find_element_by_id('tl_login')
account.clear()
account.send_keys("shiny_hsu")
password = driver.find_element_by_id('tl_password')
password.clear()
password.send_keys("1qaz!QAZ")
login = driver.find_element_by_xpath('//input[@type="submit"]')
login.click()
time.sleep(5)
cookies = driver.get_cookies()

cookies_name ="PHPSESSID"

driver.quit()  # 關閉 chromedriver


for i in range(0, len(cookies)):
    if cookies[i]['name'] == cookies_name:
        cookies_value = cookies[i]['value']

header = {'cookie': 'PHPSESSID='+cookies_value}

response = tlc.getBuildsForTestPlan(985)  #108=UAT_WEB,522=PROD_WEB
now_date = datetime.datetime.now()
delete_date = (now_date - datetime.timedelta(days=21)).strftime('%Y-%m-%d %H:%M:%S')
# print(delete_date)
delete_list_id=[]
delete_list_name=[]
for i in range(0, len(response)):
    if response[i]['creation_ts'] < delete_date:
        delete_list_name.append(response[i]['name'])
        delete_list_id.append(response[i]['id'])
# print('delete_list:'+str(delete_list))

for i in range(0, len(delete_list_id)):
    requests.get("http://testlink.paradise-soft.com.tw/lib/plan/buildEdit.php?do_action=do_delete&build_id="+delete_list_id[i],headers=header)
    print("已刪除: "+delete_list_name[i])
