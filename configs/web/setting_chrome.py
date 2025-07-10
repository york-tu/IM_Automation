from selenium import webdriver
import configparser, os, sys, yaml, platform
import os
import sys
import yaml

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

class Setting_Chrome:
    # conf's path setting
    testconf_path = 'configs/web/setting_chrome.yml'

    def get_yaml_conf(self):
        yamlfile = open(os.path.join(root_path, self.testconf_path))
        ymlconf = yaml.safe_load(yamlfile)
        return ymlconf

    def get_headless_mode(self, Headless = 1):
        conf = self.get_yaml_conf()

        if Headless == 1 and conf['headless_mode'] == 1:
            return conf['headless_mode']
        else:
            Headless = 0
            return Headless

    def get_chrome_options(self, width, height, _is_wap, Headless = 1):
        headless_mode = self.get_headless_mode(Headless)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=%s,%s' % (str(width), str(height)))
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('w3c',False)
        # chrome_options.add_argument('--no-sandbox')  # disable to avoid "chromedriver cannot quit" issue (v124)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        # 限制selenium本身的Error LOG噴出(無關測試腳本問題)
        chrome_options.add_argument("--log-level=3")
        # chrome_options.add_argument("--auto-open-devtools-for-tabs")

        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-save-password-bubble")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.media_stream_mic": 1,
        }
        chrome_options.add_experimental_option("prefs", prefs)

        if _is_wap:
            mobile_emulation = {
                "deviceName": "iPhone 12 Pro"
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            # mobile_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
            # chrome_options.add_argument(f"user-agent={mobile_ua}")

        if headless_mode == 1:
            chrome_options.add_argument('--headless')

        return chrome_options

    def get_chromedriver_path_by_os(self):
        # GET CHROMEDRIVER'S PATH FROM CONFIG
        chrome_path = ''
        Device = ''
        conf = self.get_yaml_conf()
        
        if platform.system() == 'Windows':
            Device = 'win'
        elif platform.system() == 'Linux':
            Device = 'linux'
        elif platform.system() == 'Darwin':
            Device = 'mac'

        for i in range(0, 2):
            try:
                chrome_path = os.path.join(root_path, conf['driver_path'][Device]['chrome_path'])
                break
            except:
                if i == 1:
                    raise EOFError('開啟Chromedriver錯誤')
                
        return chrome_path

if __name__ == '__main__':
    pass