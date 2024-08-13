from common.utils_folder.testlinkcontroller import TestlinkController
import datetime


uat_web_brand = ['LV', 'LS', 'C7', 'C8', 'HY', 'BH','TZ']
uat_app_brand = ['LV', 'C7', 'HY', 'BH', 'C8', 'TZ']
prod_web_brand = ['LV', 'LS', 'C7', 'C8', 'HY', 'BH', 'TZ']
prod_app_brand = ['LV', 'C7', 'HY', 'BH', 'C8', 'TZ']

if datetime.datetime.now().strftime('%w') == '4':
    TestlinkController().createnewbuilds('PS_web', 'uat', uat_web_brand)
    TestlinkController().createnewbuilds('PS_app', 'uat', uat_app_brand)
    with open("testlink_message.txt", "w") as text_file:
        text = "a = *already build * `UAT` *testbuild*"
        print(text, file=text_file)
    print('已建置今日UAT測試版本')

elif datetime.datetime.now().strftime('%w') == '5':
    TestlinkController().createnewbuilds('PS_web', 'prod', prod_web_brand)
    TestlinkController().createnewbuilds('PS_app', 'prod', prod_app_brand)
    with open("testlink_message.txt", "w") as text_file:
        text = "a = *already build * `Prod` *testbuild*"
        print(text, file=text_file)
    print('已建置今日Prod測試版本')

else:
    with open("testlink_message.txt", "w", encoding="utf-8") as text_file:
        text = "a = *not Thursday or Friday,will not build any testbuild*"
        print(text, file=text_file)
    print('非周四、周五，未建置任品牌測試版本')