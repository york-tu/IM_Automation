import os, sys, glob, platform, shutil, logging
from selenium import webdriver
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root_path)
from configs.web.setting_chrome import Setting_Chrome
import common.utils.globalvar as gl
from jira.module.base_module import UnittestModule
from webdriver_manager.chrome import ChromeDriverManager
import logging


class WebDriver(UnittestModule):
    
    def setting_driver(self, width, height, implicitly_wait_time=35, mode='', headless=1, is_wap=True):
        brand = gl.get_value('BRAND')

        if platform.system() == 'Windows': 
            user = os.environ['HOMEPATH']
            path = ('C:{0}\\Downloads\\{1}'.format(user,brand))

        elif platform.system() == 'Linux':
            user = os.environ['HOME']
            path = (r'{0}/Downloads/{1}'.format(user,brand))

        elif platform.system() == 'Darwin':
            user = os.environ['HOME']
            path = (r'{0}/Downloads/{1}'.format(user,brand))

        if os.path.isdir(path):
            shutil.rmtree(path)

        os.makedirs(path)
        
        self.chrome_path = Setting_Chrome().get_chromedriver_path_by_os()
        self.chrome_option = Setting_Chrome().get_chrome_options(width=width, height=height, _is_wap=is_wap, Headless=headless)

        prefs = {"download.default_directory": f"{path}"}
        self.chrome_option.add_experimental_option("prefs",prefs)

        if platform.system() == 'Windowssss':  # 'Windows' (chrome目前更新到最新版為試用版，套件無法自動安裝試用版的chromedriver，故跳過此段，直接跑else)
        # 消除WDM的LOG在console顯示
            logging.getLogger('WDM').setLevel(logging.NOTSET)
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
