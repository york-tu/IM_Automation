import requests, os, sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(DIR_NAME)
from apis.function_layer.base_functions import BaseFunction

class ScaleSetting(BaseFunction):

   # 新增退佣方案
   def add_comm(self, commision_program, certification, url):

      url = f'{url}apis/comm'

      payload = {
         'name': commision_program,
         'cycle': 'd'
      }

      res = self.post(url, data=payload, certification=certification)
      assert res.status_code == 200, f'api狀態碼不正確: {res.status_code}'
      assert '已新增' in res.text, '退佣方案新增失敗'

   def get_comm_api(self, comm_name, certification, url):
      url = f'{url}apis/comm'

      res = self.get(url, certification=certification)

      return res

   # 取得退佣方案
   def get_comm(self, commision_program, certification, url):

      check_res = self.get_comm_api(commision_program, certification, url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code}'

      check = False
      for comm in check_res.json():
         if comm['name'] == commision_program:
            check = True
            return comm['id']
      
      assert check == True, f'找不到退佣方案: {commision_program}'

   # 刪除退佣方案
   def del_comm(self, commision_program, certification, admin_url):

      check_res = self.get_comm_api(commision_program, certification, admin_url)
      assert check_res.status_code == 200, f'api狀態碼不正確: {check_res.status_code}'

      for comm in check_res.json():
         if comm['name'] == commision_program:
            comm_id = comm['id']
            url = f'{admin_url}apis/comm/{comm_id}'

            del_res = self.delete(url, certification=certification)
            assert del_res.status_code == 200, f'api狀態碼不正確: {del_res.status_code}'
            assert '已删除' in del_res.text, '退佣方案删除失敗'
            break

   # 新增階梯
   def add_step(self, comm_id, certification, url):

      url = f'{url}apis/comm/{comm_id}/step'

      payload = {
         'earnfrom': '0',
         'earnto': '100000',
         'memfrom': '1',
         'memto': '5'
      }

      add_step_res = self.put(url, data=payload, certification=certification)
      assert add_step_res.status_code == 200, f'api狀態碼不正確: {add_step_res.status_code}'
      assert add_step_res.text != '', '階梯新增失敗'

      return add_step_res.text.replace('"','')

   # 更新階梯
   def push_step(self, comm_id, step_id, certification, url):

      url = f'{url}apis/comm/{comm_id}/step/{step_id}'

      payload = {
         'id': step_id,
         'earnfrom': '0',
         'earnto': '100000',
         'memfrom': '1',
         'memto': '5',
         'depositpercent': '10',
         'webdepositpercent': '10'
      }

      push_step_res = self.put(url, data=payload, certification=certification)
      assert push_step_res.status_code == 200, f'api狀態碼不正確: {push_step_res.status_code}'
      assert '已修改' in push_step_res.text, '階梯更新失敗'

   # 更新頻道退佣
   def push_channel(self, comm_id, step_id, certification, url):

      url = f'{url}apis/comm/{comm_id}/step/{step_id}/channel'

      payload = {
         'items': "[{\"channelcode\":\"ag_fish\",\"channelname\":\"AG-捕鱼\",\"commpercent\":0,\"rebatepercent\":5,\"errors\":[]},{\"channelcode\":\"ag_game\",\"channelname\":\"AG-电子\",\"commpercent\":0,\"rebatepercent\":\"5\",\"errors\":[]},{\"channelcode\":\"ag_video\",\"channelname\":\"AG-视讯\",\"commpercent\":0,\"rebatepercent\":\"5\",\"errors\":[]},{\"channelcode\":\"bbin_fish\",\"channelname\":\"BBIN-捕鱼\",\"commpercent\":0,\"rebatepercent\":\"5\",\"errors\":[]},{\"channelcode\":\"bbin_game\",\"channelname\":\"BBIN-电子\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"bbin_sport\",\"channelname\":\"BBIN-体育\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"bbin_video\",\"channelname\":\"BBIN-视讯\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"bs_fish\",\"channelname\":\"百胜捕鱼\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"bs_qipai\",\"channelname\":\"百胜棋牌\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"cq_fish\",\"channelname\":\"CQ9-捕鱼\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]},{\"channelcode\":\"cq_game\",\"channelname\":\"CQ9-电子\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]},{\"channelcode\":\"dg_video\",\"channelname\":\"DG-视讯\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]},{\"channelcode\":\"dt_game\",\"channelname\":\"DT-电子\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]},{\"channelcode\":\"fctc\",\"channelname\":\"福彩/体彩\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]},{\"channelcode\":\"fg_game\",\"channelname\":\"FG-电子\",\"commpercent\":0,\"rebatepercent\":\"20\",\"errors\":[]},{\"channelcode\":\"fg_qipai\",\"channelname\":\"FG-棋牌\",\"commpercent\":0,\"rebatepercent\":\"20\",\"errors\":[]},{\"channelcode\":\"gc_video\",\"channelname\":\"GC-视讯\",\"commpercent\":0,\"rebatepercent\":\"20\",\"errors\":[]},{\"channelcode\":\"gm_qipai\",\"channelname\":\"GM-棋牌\",\"commpercent\":0,\"rebatepercent\":\"20\",\"errors\":[]},{\"channelcode\":\"hb\",\"channelname\":\"红包\",\"commpercent\":0,\"rebatepercent\":\"20\",\"errors\":[]},{\"channelcode\":\"hg_sport\",\"channelname\":\"皇冠体育\",\"commpercent\":0,\"rebatepercent\":\"25\",\"errors\":[]},{\"channelcode\":\"hk\",\"channelname\":\"香港彩票\",\"commpercent\":0,\"rebatepercent\":\"25\",\"errors\":[]},{\"channelcode\":\"js\",\"channelname\":\"极速彩种\",\"commpercent\":0,\"rebatepercent\":\"25\",\"errors\":[]},{\"channelcode\":\"ky_qipai\",\"channelname\":\"开元棋牌\",\"commpercent\":0,\"rebatepercent\":\"25\",\"errors\":[]},{\"channelcode\":\"lc_qipai\",\"channelname\":\"龙城棋牌\",\"commpercent\":0,\"rebatepercent\":\"25\",\"errors\":[]},{\"channelcode\":\"mg_game\",\"channelname\":\"MG-电子\",\"commpercent\":0,\"rebatepercent\":\"30\",\"errors\":[]},{\"channelcode\":\"mg_video\",\"channelname\":\"MG-视讯\",\"commpercent\":0,\"rebatepercent\":\"30\",\"errors\":[]},{\"channelcode\":\"pt_fish\",\"channelname\":\"PT-捕鱼\",\"commpercent\":0,\"rebatepercent\":\"30\",\"errors\":[]},{\"channelcode\":\"pt_game\",\"channelname\":\"PT-电子\",\"commpercent\":0,\"rebatepercent\":\"30\",\"errors\":[]},{\"channelcode\":\"qipai\",\"channelname\":\"棋牌游戏\",\"commpercent\":0,\"rebatepercent\":\"30\",\"errors\":[]},{\"channelcode\":\"sb_game\",\"channelname\":\"SB-电子\",\"commpercent\":0,\"rebatepercent\":\"35\",\"errors\":[]},{\"channelcode\":\"sb_numbergame\",\"channelname\":\"SB-百练赛\",\"commpercent\":0,\"rebatepercent\":\"35\",\"errors\":[]},{\"channelcode\":\"sb_sportbooks\",\"channelname\":\"SB-体育\",\"commpercent\":0,\"rebatepercent\":\"35\",\"errors\":[]},{\"channelcode\":\"sb_virtualsport\",\"channelname\":\"SB-虚拟体育\",\"commpercent\":0,\"rebatepercent\":\"35\",\"errors\":[]},{\"channelcode\":\"sb_virtualsport2\",\"channelname\":\"SB-虚拟体育2\",\"commpercent\":0,\"rebatepercent\":\"35\",\"errors\":[]},{\"channelcode\":\"sf\",\"channelname\":\"三分彩种\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]},{\"channelcode\":\"ssc\",\"channelname\":\"高频彩种\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]},{\"channelcode\":\"ss_sport\",\"channelname\":\"3S-体育\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]},{\"channelcode\":\"sw_game\",\"channelname\":\"SW-电子\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]},{\"channelcode\":\"vg_qipai\",\"channelname\":\"VG-棋牌\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]},{\"channelcode\":\"wf\",\"channelname\":\"五分彩种\",\"commpercent\":0,\"rebatepercent\":\"40\",\"errors\":[]}]"
      }

      push_channel_res = self.put(url, data=payload, certification=certification)
      assert push_channel_res.status_code == 200, f'api狀態碼不正確: {push_channel_res.status_code}'
      assert '已修改' in push_channel_res.text, '頻道退佣更新失敗'

   # 更新產品比例
   def push_products(self, comm_id, step_id, certification, url):

      url = f'{url}apis/comm/{comm_id}/step/{step_id}/channel/ag_fish/products'

      payload = {
         'items': "[{\"channelcode\":\"ag_fish\",\"custom\":0,\"productcode\":\"0\",\"productname\":\"AG预设\",\"commpercent\":0,\"rebatepercent\":5,\"errors\":[]},{\"channelcode\":\"ag_fish\",\"custom\":0,\"productcode\":\"3102\",\"productname\":\"捕鱼新乐园\",\"commpercent\":0,\"rebatepercent\":\"10\",\"errors\":[]},{\"channelcode\":\"ag_fish\",\"custom\":0,\"productcode\":\"519\",\"productname\":\"捕鱼王\",\"commpercent\":0,\"rebatepercent\":\"15\",\"errors\":[]}]"
      }

      push_products_res = self.put(url, data=payload, certification=certification)
      assert push_products_res.status_code == 200, f'api狀態碼不正確: {push_products_res.status_code}'
      assert '已修改' in push_products_res.text, '產品比例更新失敗'