# Automated test

## 客服寶自動化

### 專案主要⽬的及特性
1. 改進品質
2. 減少人工測試的成本
3. 短時間內找出錯誤
4. 確保主要功能運作正常

### 系統需求
- Windows 10 以上作業系統
- Mac OS X
- Python 3.6 以上版本
- Chrome 86 以上版本
- Centos 7

### 基本開發原則及注意要點
- 自動化程式裡缺少的yaml檔存放在團隊clickup自動化開發-文件區
- 開發時先在develop線上開新分支進行開發，分支命名需在前面加mynah，例: mynah/addnewfunction，開發完成可自行合入develop線
- 程式命名依照python PEP8命名規範
- 開發測試時，請使用分配好的帳號以免衝突

### 架構圖


### 設計細節
- 檔案依照前後端分類，再往下依頁面分類
- 請使用common包裝好的方法進行開發
- 各檔案名詞介紹:
    - common
        > 將 selenium 的操作另外包成 function，如 common.click() : 先做一次 findElement().click()，如果出現錯誤，則會將畫面移動到元件的位置，再做一次 findElement().click() 的操作

    - basepage
        > 每個頁面通用的基本操作，如 close_and_chang_window()，開新分頁，關原分頁

    - pages
        > 將所有頁面重新命名後回傳，沒有任何操作頁面或處理資料的行為

    - setting
        > 將資料(帳號、密碼...等)整理成 dictionary 的格式並回傳

    - setting_Chrome
        > 處理瀏覽器的一些基本設定

    - unittest.TestCase
        > python 套件，bj4

    - base_testcase
        > 將 Setting 及 Setting_Chrome 所回傳的資料存入成員變數中

    - testcases
        > 每個 TestCase 都是以 "完成此測試，所需的所有動作" 為前提來撰寫，因此 **前後台發話** 的 TestCase 也會包含 **後台登入** 的操作
