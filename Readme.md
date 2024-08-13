# Automated test

### **簡易版 class diagram**
![](https://i.imgur.com/mbWTO9R.png "簡易版 class diagram")

- regression
    > 設定要測試的品牌、登入的 bot 帳號，以及要跑的 TestCase，執行後就會開始自動化測試

- common
    > 將 selenium 的操作另外包成 function，如 common.click() : 先做一次 findElement().click()，如果出現錯誤，則會將畫面移動到元件的位置，再做一次 findElement().click() 的操作

- basepage
    > 每個網站通用的基本操作，如 waitLoadFinish()

- page
    > 每個頁面在做測試時所需要的操作

- pages
    > 將所有頁面重新命名後回傳，沒有任何操作頁面或處理資料的行為

- Setting
    > 將資料(帳號、密碼...等)整理成 dictionary 的格式並回傳

- Setting_Chrome
    > 處理瀏覽器的一些基本設定

- unittest.TestCase
    > python 套件，bj4

- base_testcase
    > 將 Setting 及 Setting_Chrome 所回傳的資料存入成員變數中

- testcases
    > 每個 TestCase 都是以 "完成此測試，所需的所有動作" 為前提來撰寫，因此 **admin -> 第三方遊戲設置** 的 TestCase 也會包含 **到前台確認功能是否正常** 的操作

---
---
### **class diagram relationship 簡易說明**

- Association
    > ![](https://i.imgur.com/3qKTcrc.png "Association")
    > - X is aware of Y; X contains a pointer or reference to Y
    > - X can issue a function call to a member function of Y

- Inheritance
    > ![](https://i.imgur.com/gsksl82.png "Inheritance")
    > - X class is derived from Y

- Dependency
    > ![](https://i.imgur.com/Oia7H6g.png "Dependency")
    > - X issues a function call to a member function of Y
    > - Short term relationship

- Composition
    > ![](https://i.imgur.com/9we2Jw8.png "Composition")
    > - X contains Y as members

關於 class diagram ，[請參考](https://myweb.ntut.edu.tw/~wkchen/courses/wprog/files/Intro%20UML%20and%20Object%20Relationships.pdf)
