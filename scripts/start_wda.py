# -*- coding: utf-8 -*-
"""
手動啟動 WDA 腳本
使用與測試相同的啟動方式（Airtest 自動啟動 WDA）

使用方法:
    python scripts/start_wda.py [phone_name]
    
參數:
    phone_name: 可選，指定要使用的 iOS 設備名稱（如 IPHONE_15_PRO）
                如果不指定，將使用配置檔案中的第一個 iOS 設備
"""
import sys
import os
from pathlib import Path

# 添加專案根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from common.utils.path_utils import PathUtils
from common.utils.config_loader import ConfigLoader
import common.utils.globalvar as gl
from driver.app_driver import AppDriver


def get_ios_devices(phone_config):
    """
    從配置檔案中獲取所有 iOS 設備
    
    Args:
        phone_config: 手機配置字典
        
    Returns:
        dict: iOS 設備字典 {device_name: device_config}
    """
    ios_devices = {}
    phone_conf = phone_config.get('Phone_conf', {})
    
    for device_name, device_config in phone_conf.items():
        if device_config.get('platformName', '').upper() == 'IOS':
            ios_devices[device_name] = device_config
    
    return ios_devices


def main():
    """主函數"""
    print("=" * 60)
    print("WDA 啟動腳本")
    print("使用與測試相同的啟動方式（Airtest 自動啟動 WDA）")
    print("=" * 60)
    
    # 讀取手機配置
    try:
        config_loader = ConfigLoader()
        phone_config = config_loader.get_phone_config()
    except Exception as e:
        print(f"❌ 錯誤：無法讀取配置檔案: {e}")
        print("請確認 configs/app/phone_config.yml 存在並已正確配置")
        return False
    
    # 獲取所有 iOS 設備
    ios_devices = get_ios_devices(phone_config)
    
    if not ios_devices:
        print("❌ 錯誤：配置檔案中沒有找到 iOS 設備")
        return False
    
    # 獲取指定的設備名稱（從命令行參數）
    phone_name = None
    if len(sys.argv) > 1:
        phone_name = sys.argv[1]
        if phone_name not in ios_devices:
            print(f"❌ 錯誤：找不到指定的設備 '{phone_name}'")
            print(f"可用的 iOS 設備：{', '.join(ios_devices.keys())}")
            return False
    else:
        # 使用第一個 iOS 設備
        phone_name = list(ios_devices.keys())[0]
    
    device_config = ios_devices[phone_name]
    
    print(f"\n📱 使用設備: {phone_name}")
    print(f"   UDID: {device_config.get('udid', 'N/A')}")
    print(f"   Port: {device_config.get('port', 'N/A')}")
    print(f"   Model: {device_config.get('model', 'N/A')}")
    
    # 設置必要的全局變數（模擬測試環境）
    gl.set_value('PHONE_NAME', phone_name)
    gl.set_value('PHONE_PLATFORM', 'iOS')
    gl.set_value('CONNECT_TYPE', 'local')
    gl.set_value('PHONE_REMOTE_IP', '')
    
    print("\n" + "=" * 60)
    print("開始啟動 WDA...")
    print("=" * 60)
    print("使用與測試相同的啟動方式（Airtest 自動啟動 WDA）")
    
    # 使用 AppDriver 連接設備（這會自動啟動 WDA）
    try:
        app_driver = AppDriver()
        
        print("\n🔄 正在連接 iOS 設備（Airtest 會自動啟動 WDA）...")
        print("   這可能需要幾秒鐘時間...")
        
        # 連接設備（這會自動啟動 WDA）
        parameter = app_driver.airtest_connect_phone(phone_name)
        
        poco, wda_service = parameter
        
        print("\n" + "=" * 60)
        print("✅ WDA 啟動成功！")
        print("=" * 60)
        print("\n說明：")
        print("- 已通過 Airtest 連接 iOS 設備")
        print("- Airtest 已自動啟動 WDA（與測試相同的方式）")
        print("- WDA 現在正在運行")
        print(f"- Poco 物件已初始化: {poco}")
        print(f"- WDA Service 已初始化: {wda_service}")
        print("\n提示：")
        print("- 可以開始執行測試了")
        print("- 要停止連接，請按 Ctrl+C")
        print("- 注意：此腳本會保持連接，按 Ctrl+C 會斷開連接")
        
        # 保持連接，直到用戶按 Ctrl+C
        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n⚠️  正在斷開連接...")
            # 清理資源
            if hasattr(app_driver, 'poco') and app_driver.poco:
                try:
                    # 可以添加清理邏輯
                    pass
                except:
                    pass
            print("✅ 連接已斷開")
            return True
            
    except Exception as e:
        print(f"\n❌ 連接設備時發生錯誤: {str(e)}")
        import traceback
        traceback.print_exc()
        print("\n請檢查：")
        print("1. 設備是否已通過 USB 連接")
        print("2. 設備是否已解鎖並信任電腦")
        print("3. WDA 是否已安裝在設備上")
        print("4. airtest 和 pocoui 是否已安裝")
        print("5. 設備 UDID 是否正確")
        return False


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  腳本已中斷")
        sys.exit(1)

