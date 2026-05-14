import os, sys, glob, platform, shutil, logging
from selenium import webdriver
from common.utils.path_utils import PathUtils

# 使用 PathUtils 獲取專案根目錄
path_utils = PathUtils()
root_path = str(path_utils.get_project_root())
sys.path.append(root_path)
from configs.web.setting_chrome import Setting_Chrome
import common.utils.globalvar as gl
from jira.module.base_module import UnittestModule
from webdriver_manager.chrome import ChromeDriverManager
import logging


class WebDriver(UnittestModule):
    
    def setting_driver(self, width, height, implicitly_wait_time=35, mode='', headless=1, is_wap=True):
        brand = gl.get_value('BRAND')

        # 使用 PathUtils 獲取下載路徑
        download_path = path_utils.get_download_path(brand)
        path = str(download_path)

        if os.path.isdir(path):
            shutil.rmtree(path)

        os.makedirs(path)

        # Linux（Jenkins Docker）：bundled chromedriver 常與映像內 google-chrome 主版本不符 → session 失敗。
        # 預設用 ChromeDriverManager 對齊已安裝 Chrome；若需離線可設環境變數 USE_LOCAL_CHROMEDRIVER_ON_LINUX=1
        if platform.system() == 'Linux' and os.environ.get('USE_LOCAL_CHROMEDRIVER_ON_LINUX') != '1':
            logging.getLogger('WDM').setLevel(logging.NOTSET)
            self.chrome_path = ChromeDriverManager().install()
        else:
            self.chrome_path = Setting_Chrome().get_chromedriver_path_by_os()
        self.chrome_option = Setting_Chrome().get_chrome_options(width=width, height=height, _is_wap=is_wap, Headless=headless)

        # 注意：add_experimental_option("prefs", ...) 會「覆蓋」整個 prefs dict，
        # 不會 merge。setting_chrome.py 已經設定了密碼外洩偵測 / 自動填入等
        # 關閉項目，這裡需把下載目錄合併進去，避免把上面設定全洗掉。
        existing_prefs = self.chrome_option.experimental_options.get('prefs', {}) or {}
        merged_prefs = {**existing_prefs, "download.default_directory": f"{path}"}
        self.chrome_option.add_experimental_option("prefs", merged_prefs)

        # Note: ChromeDriverManager deprecated in Selenium 4.x, using direct path
        # For Selenium 4.x, use: webdriver.Chrome(service=Service(self.chrome_path), options=self.chrome_option)
        if platform.system() == 'Windowssss':  # 'Windows' (chrome目前更新到最新版為試用版，套件無法自動安裝試用版的chromedriver，故跳過此段，直接跑else)
        # 消除WDM的LOG在console顯示
            logging.getLogger('WDM').setLevel(logging.NOTSET)
            # Deprecated: executable_path and chrome_options in Selenium 4.x
            # For Selenium 3.x compatibility, keeping as is
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=self.chrome_option)
        else:
            self.driver = webdriver.Chrome(executable_path=self.chrome_path, chrome_options=self.chrome_option)

        self.driver.implicitly_wait(implicitly_wait_time)

        # self.driver.set_network_conditions(        # 測試慢網速用
        #     offline=False,
        #     latency=5,  # additional latency (ms)  defalut is 5
        #     download_throughput=500 * 1024,  # maximal throughput  500MB
        #     upload_throughput=500 * 1024)  # maximal throughput  500MB

        return self.driver
