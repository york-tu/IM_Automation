import requests, os, sys, pytz, json, unicodedata
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from datetime import datetime, timedelta
from apis.function_layer.base_functions import BaseFunction
from lxml import etree

class FloatingWindow(BaseFunction):

   def get_float_window_num(self, certification, url, pos):
      """
         取得浮窗頁面資訊
         
         Args:
               certification: admin帳號登入的認證狀態
               url: 品牌後台URL
               pos: 1, 左側浮窗
                  2, 右側浮窗 
      """
      if pos == 1:
         url = f"{url}connectionlink/floatingwindowpc/floating-left/advancedsetting"
      elif pos == 2:
         url = f"{url}connectionlink/floatingwindowpc/floating-right/advancedsetting"
      else:
         raise EOFError("pos參數設定錯誤, 僅供使用1(左側浮窗), 2(右側浮窗)")

      float_window_info = self.get(url, certification=certification)
      assert float_window_info.status_code == 200, f'api狀態碼不正確: {float_window_info.status_code}'
      originHTML = etree.HTML(float_window_info.text)
      number_info = originHTML.xpath("(//script[@type='text/javascript'])[1]")
      number_info_text = number_info[0].text

      # info string process
      brand = url[7:9] # 取得當前品牌名
      tmp = number_info_text.replace("\n", "")
      tmp = tmp.replace(" ", "")
      tmp = tmp.replace("var", "")
      tmp = tmp.replace("server_connectionlinkData=", "")
      tmp = tmp.replace('currentRoute="/connectionlink/floatingwindowpc/floating-left/advancedsetting";', "")
      tmp = tmp.replace('currentRoute="/connectionlink/floatingwindowpc/floating-right/advancedsetting"', "")
      tmp = tmp.replace(";", "")
      # 撈出來的資訊與當初設計API不一樣，多了"server_brand='lv'的string
      diff_text = 'server_brand="' + brand + '"'
      tmp = tmp.replace(diff_text, "")

      # convert dictionary string to dictionary
      float_info_dict = json.loads(tmp)
      assert isinstance(float_info_dict, dict), f'資料型別轉換dict錯誤，現為: {type(float_info_dict)}'

      return float_info_dict

   # 浮窗圖示(初始化)
   # pos = 1 為左側浮窗 / pos = 2 為右側浮窗
   def float_window_init(self, certification, url, info_dict, pos):
      # 清空展開圖片dict_data
      if pos == 1:
         info_dict["model"]["flag"] = ""
         info_dict["model"]["image"] = ""
         info_dict["model"]["linkurl"] = ""
         info_dict["model"]["title"] = r"左侧浮窗".encode("utf-8")

         # 標記須排除_list index
         mark_list = []
         for num in range(len(info_dict["pictures"])):
            if info_dict["pictures"][num]["title"] != "left":
               mark_list.append(num)
         # del tester update image and column
         if len(mark_list) != 0:
            for ele in sorted(mark_list, reverse = True):
               del info_dict["pictures"][ele]
      elif pos == 2:
         info_dict["model"]["flag"] = ""
         info_dict["model"]["image"] = ""
         info_dict["model"]["linkurl"] = ""
         info_dict["model"]["title"] = r"右侧浮窗".encode("utf-8")
         
         # 標記須排除_list index
         mark_list = []
         for num in range(len(info_dict["pictures"])):
            if info_dict["pictures"][num]["title"] != "right":
               mark_list.append(num)
         # del tester update image and column
         if len(mark_list) != 0:
            for ele in sorted(mark_list, reverse = True):
               del info_dict["pictures"][ele]
      else:
         raise EOFError("pos參數設定錯誤, 僅供使用1(左側浮窗), 2(右側浮窗)")

      temp_model = json.dumps(info_dict["model"], cls=JsonEncoder)
      temp_pictures = json.dumps(info_dict["pictures"], cls=JsonEncoder)
      temp_current = {"model": temp_model, "pictures": temp_pictures}
      """
         浮窗圖示(初始化)_刪除圖片使用預設圖片
   
         Args:
               certification: admin帳號登入的認證狀態
               url: 品牌後台URL
               json: json type string
               pos: 1, 左側浮窗
                  2, 右側浮窗 
      """
      if pos == 1:
         url = f"{url}apis/connectionlink/floatingwindowpc/floating-left/advancedsetting"
      elif pos == 2:
         url = f"{url}apis/connectionlink/floatingwindowpc/floating-right/advancedsetting"
   
      float_window_res = self.put(url, data=temp_current, certification=certification)

      assert float_window_res.status_code == 200, f'api狀態碼不正確: {float_window_res.status_code}, {float_window_res.text}'

class JsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, bytes):
         return str(obj, encoding='utf-8')
      return json.JSONEncoder.default(self, obj)
