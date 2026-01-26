# Scripts 目錄說明

此目錄包含專案中使用的各種工具腳本。

## start_wda.py - iOS WDA 啟動腳本

### 功能說明

此腳本用於手動啟動 iOS 設備上的 WebDriverAgent (WDA)，使用與自動化測試相同的啟動方式。

### 使用方法

#### 基本用法（使用第一個 iOS 設備）

```bash
python scripts/start_wda.py
```

#### 指定設備

```bash
python scripts/start_wda.py IPHONE_15_PRO
```

### 前置需求

1. **iOS 設備已連接**
   - 設備必須通過 USB 連接到電腦
   - 設備必須已解鎖並信任電腦

2. **WDA 已安裝**
   - WebDriverAgent 必須已安裝在 iOS 設備上
   - 通常需要通過 Xcode 編譯並安裝

3. **Python 套件已安裝**
   - `airtest`
   - `pocoui`
   - `wda` (facebook-wda)

4. **配置檔案已設置**
   - `configs/app/phone_config.yml` 中必須包含 iOS 設備配置
   - 配置必須包含 `udid`、`port` 和 `model` 欄位

### 配置範例

在 `configs/app/phone_config.yml` 中，iOS 設備配置格式如下：

```yaml
Phone_conf:
    IPHONE_15_PRO:
        platformName: iOS
        udid: 00008130-000C45500292001C
        port: 8100
        model: 7
```

### 工作原理

1. 讀取 `configs/app/phone_config.yml` 中的 iOS 設備配置
2. 使用 `AppDriver.airtest_connect_phone()` 方法連接設備
3. Airtest 會自動啟動 WDA（與測試執行時相同的方式）
4. 保持連接直到用戶按 Ctrl+C 中斷

### 注意事項

- 此腳本會保持連接狀態，直到手動中斷（Ctrl+C）
- 如果 WDA 已經在運行，Airtest 會自動使用現有的 WDA 連接
- 確保設備配置中的 UDID 與實際設備一致
- 如果連接失敗，請檢查設備是否已解鎖並信任電腦

### 疑難排解

#### 錯誤：找不到配置檔案
- 確認 `configs/app/phone_config.yml` 存在
- 確認配置檔案格式正確（YAML 格式）

#### 錯誤：找不到指定的設備
- 確認設備名稱拼寫正確
- 使用 `python scripts/start_wda.py` 查看可用的設備列表

#### 錯誤：連接設備時發生錯誤
- 確認設備已通過 USB 連接
- 確認設備已解鎖並信任電腦
- 確認 WDA 已安裝在設備上
- 確認設備 UDID 配置正確

#### WDA 啟動失敗
- 檢查設備上的 WDA 應用程式是否正常運行
- 確認設備已信任開發者證書
- 嘗試重新安裝 WDA

