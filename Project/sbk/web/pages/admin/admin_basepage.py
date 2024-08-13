from selenium.webdriver.common.by import By
import os, sys, json,requests
from common.web.common import Common

class BasePageLocator:
    # LOADING
    loading_mask = (By.XPATH, '//div[@class="el-loading-mask"]')

class BasePage(Common):
    def wait_loading_finish(self):
        self.sleep(1)
        if self.is_element_finded(BasePageLocator.loading_mask) is True:
            try:
                self.is_element_displayed(BasePageLocator.loading_mask)
            except:
                raise Exception("訊息讀取時間過長,請確認讀取屏蔽視窗")
    # def qat_api_login(self, deviceToken):
    #     url = "https://sbk-gateway-player-qat.idc.pstdsf.com/partner-api/player-game-urls"

    #     payload = json.dumps({
    #     "account": "auto001"
    #     })
    #     headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': f'Bearer {deviceToken}'
    #     }
    #     response = requests.request("POST", url, headers=headers, data=payload)

    #     print(response.text)
