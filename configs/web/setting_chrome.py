from selenium import webdriver
import os, sys, platform
from common.utils.path_utils import PathUtils
from common.utils.config_loader import ConfigLoader

# 使用 PathUtils 添加專案根目錄到 sys.path
path_utils = PathUtils()
project_root = str(path_utils.get_project_root())
if project_root not in sys.path:
    sys.path.append(project_root)

# 使用 ConfigLoader 載入配置
config_loader = ConfigLoader()


class Setting_Chrome:
    """Chrome 設定配置類（使用統一的 ConfigLoader）"""

    def get_yaml_conf(self):
        """獲取 Chrome 配置（使用 ConfigLoader）"""
        return config_loader.get_chrome_config()

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
                # 獲取配置中的相對路徑（如 'driver/driver/chromedriver.exe'）
                relative_path = conf['driver_path'][Device]['chrome_path']
                # 使用 PathUtils 獲取完整路徑
                chrome_path = str(path_utils.get_relative_path(*relative_path.replace('\\', '/').split('/')))
                break
            except:
                if i == 1:
                    raise EOFError('開啟Chromedriver錯誤')
                
        return chrome_path

if __name__ == '__main__':
    pass