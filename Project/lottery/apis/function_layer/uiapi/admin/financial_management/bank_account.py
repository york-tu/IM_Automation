import requests, base64, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR_NAME)
from lottery.apis.function_layer.base_functions import BaseFunction

class BankAccount(BaseFunction):
    # 抓取線上存款內容
    def get_info(self, certification, admin_url):
        Querystring = {"contents": "", "langcode": "", "status": "-1", "pi": "1", "ps": "25", "po": "sort asc"}
        url = "%sapis/marketing/member/deposit/category" % admin_url
        response = self.get(url, Querystring, certification, self.header())
        get = self.response_json(response)
        return get

    # 全部父子類別關閉
    def change_close(self, certification, admin_url):
        gets = self.get_info(certification, admin_url)
        for list in range(0, len(gets)):
            id = gets[list]["id"]
            # name = get[list]["name"]
            subitems = gets[list]["subitems"]

            for loops in range(0, len(subitems)):
                subid = subitems[loops]["id"]

                data = {
                    'id': id,
                    'image': "",
                    'mimage': "",
                    'name': "Close",
                    'sort': "1",
                    'status': "0",
                    'subitems': '[{"id": "%s", "name": "Close", "tips": "", "status":0, "sort": 1, "tag": "deposit", "image": ""}]' % (
                        subid),
                    'tips': ""
                }
                url = "%sapis/marketing/member/deposit/category/%s" % (admin_url, id)
                self.put(url, data, certification)

    # 判斷子類別修改及新增
    def check_sort(self, certification, sort_list, num, info, admin_url, Sort, sort_child, fileserver_url, brand):
        file_path = f"p/shark/{brand}"

        image = self.upload_image(Sort, admin_url, certification)  # 父類別web,mob圖片轉base64
        image_child = self.upload_image(sort_child, admin_url, certification)  # 子類別圖片轉base64

        gets = self.get_info(certification, admin_url)
        id = gets[sort_list]["id"]
        name = gets[sort_list]["name"]
        subitems = gets[sort_list]["subitems"]

        # 判斷子類別
        if len(subitems) < num:
            data = {
                'id': id,
                'image': "",
                'mimage': "",
                'name': "%s" % name,
                'sort': "1",
                'status': "0",
                'subitems': '[{"name":"add","status":"0","tag":"deposit","tips":"","image":"","sort":1}]',
                'tips': ""
            }
            url = "%sapis/marketing/member/deposit/category/%s" % (admin_url, id)
            respsone = self.put(url, data, certification)
            code = respsone.status_code
        
            assert code == 200, f"關閉目前所有節點錯誤 code: {code}"

        # 修改子類別
        gets = self.get_info(certification, admin_url)
        subitems = gets[sort_list]["subitems"]
        count = 0
        
        for loop in range(num):
            subid = subitems[loop]["id"]
            data = {
                'id': id,
                'image': f"{file_path}/setting_deposit_category/{image[0]}",
                'mimage': f"{file_path}/setting_deposit_category/{image[1]}",
                'name': "%s" % info[len(info) - 1],
                'sort': "1",
                'status': "1",
                'subitems': '[{"id": "%s", "name": "%s", "tips": "", "status":1, "sort": 1, "tag": "%s", "image": "%s/setting_deposit_category_dtl/%s"}]' % (
                subid, info[count], info[count + 1],file_path, image_child[loop]),
                'tips': ""
            }

            url = "%sapis/marketing/member/deposit/category/%s" % (admin_url, id)
            respsone = self.put(url, data, certification)
            code = respsone.status_code
            count += 2

            assert code == 200, f"修改錯誤 code: {code}"
            

    # 確定父類別有7個
    def check_num(self, certification, admin_url):
        gets = self.get_info(certification, admin_url)
        
        if len(gets) < 9:  # 9
            for _ in range(len(gets), 9):  # 9
                data = {
                    'color': '',
                    'id': '',
                    'image': "",
                    'mimage': "",
                    'name': "add",
                    'sort': "0",
                    'status': "0",
                    'subitems': '[{"name":"add","status":"0","tag":"deposit","tips":"","image":"","sort":1}]',
                    'tips': ""
                }
                url = "%sapis/marketing/member/deposit/category" % admin_url
                respsone = self.post(url, data, certification)
                code = respsone.status_code

                assert code == 200, f"判斷數量錯誤 code: {code}"
        else:
            pass

    # 抓取所有資訊
    def get_info_all(self, certification, admin_url):
        gets = self.get_info(certification, admin_url)
        for list in range(0, len(gets)):
            print(gets[list])

    # 父類別欄位,需求子類別數量,資訊
    def add_sort_all(self, certification, admin_url, fileserver_url, brand):

        # 子類別名稱 種類 父類別名稱(放在最後一個位置)
        company = ['公司入款', 'deposit', '公司入款']
        alipay = ['支付宝面对面扫码', 'alipaydeposit', '支付宝转帐', 'alipay', '支付宝']
        wechat = ['微信面对面扫码', 'wechatdeposit', '微信转帐', 'weixin', '微信']
        upi = ['UPI入款','upi','UPI入款']
        onlinepay = ['线上支付', 'webdeposit', '线上支付']
        unionpay = ['银联支付', 'webdeposit', '银联支付']
        jdpay = ['京东支付', 'webdeposit', '京东支付']
        wellpay = ['顺付WellPay-账号入款','zqb_my_buy','顺付WellPay-扫码入款','zqb_my_buy','顺付WellPay-我要买入款']
        usdt = ['USDT(ERC)','cryptocurrency','USDT(TRC)','cryptocurrency','USDT']


        # 第一個父類別位置,子類別數量,分類,網址,照片資料夾名稱,子類別照片資料夾名稱(Child)
        self.check_sort(certification, 0, 1, company, admin_url, 'Company', 'Child', fileserver_url, brand)
        self.check_sort(certification, 1, 2, alipay, admin_url, 'AliPay', 'Child', fileserver_url, brand)
        self.check_sort(certification, 2, 2, wechat, admin_url, 'WeChat', 'Child', fileserver_url, brand)
        self.check_sort(certification, 3, 1, upi, admin_url, 'Upi', 'Child', fileserver_url, brand)
        self.check_sort(certification, 4, 1, onlinepay, admin_url, 'OnlinePay', 'Child', fileserver_url, brand)
        self.check_sort(certification, 5, 1, unionpay, admin_url, 'UnionPay', 'Child', fileserver_url, brand)
        self.check_sort(certification, 6, 1, jdpay, admin_url, 'JdpayPay', 'Child', fileserver_url, brand)
        self.check_sort(certification, 7, 2, wellpay, admin_url, 'WellPay', 'Child', fileserver_url, brand)
        self.check_sort(certification, 8, 2, usdt, admin_url, 'Usdt', 'UsdtChild', fileserver_url, brand)

    # 上傳圖片並轉成md5
    def upload_image(self, path, admin_url,certification):
        if 'Child' in path :
            file_path = '/setting_deposit_category_dtl'
        else:
            file_path = '/setting_deposit_category'
            
        paths = '%s/admin/bank_account/%s/' % (os.path.abspath('image'), path)
        items = os.listdir(paths)
        data = []

        for names in items:
            if names.endswith(".png"):

                image_file = open("%s%s" % (paths, names), "rb")
                for _ in range(0,3):
                    try:
                        image_md5 = self.upload(names, image_file, file_path, admin_url, certification)
                        break
                    except:
                        self.sleep(2)
                        image_md5 = self.upload(names, image_file, file_path, admin_url, certification)
                data.append(image_md5)

        return data
    
    def upload(self,names, image_file, file_path, admin_url, certification):
        url = f'{admin_url}v1/fs/upload'
        files = {
            'file': image_file
        }

        data = {
            'filepath': file_path
        }
        
        respsone = self.post(url, data, certification, file=files)
        code = respsone.status_code
        if code == 200 or code ==204:
            pass
        else:
            raise Exception(f"上傳圖片失敗 code: {code}")
        # assert code == 200 or code == 204, f"上傳圖片失敗 code: {code}"

        return (respsone.json()['fileinfo']['name'])