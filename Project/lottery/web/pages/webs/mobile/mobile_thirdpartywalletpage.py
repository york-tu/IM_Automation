from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import datetime, re

class Store_Record_Value:
  # WALLET PAGE (額度轉換)

  # 轉換 title
  transfer_message = (By.XPATH, '//p[@class = "transfer-alert__title"]')
  # 轉換 Dialog 確認鈕
  transfer_dialog_confirm_btn = (By.XPATH, '//button[@class = "btn-alert"]')

  # 一鍵歸戶
  wallet_return_btn = (By.XPATH, "//*[text() = '一键归户']/..")
  wallet_check = (By.XPATH, "//p[@class = 'wallet-text']//span[contains(@class,'_balance')]")
  wallet_maintain = (By.XPATH, "//p[contains(text(),'维护中')and @style!='display: none;']")
  maintain_money = (By.XPATH, "//div[@class='wallet-list__item wallet-list__item--disabled']/div/p[3]/span[2]")

  # 主錢包
  main_wallet_from = (By.XPATH, "//span[@class= 'cp_balance']")
  # 錢包選擇鈕
  @staticmethod
  def wallet_choosing_btn( from_or_to, thirdparty_name):
    locator = (By.XPATH, "//div[@id = 'transfer_%s']/div/div[./div[@class = 'wallet-list__item__rt']//span[contains(@class,'%s')]]" % (from_or_to, thirdparty_name))
    return locator

  # 被選錢包額度
  @staticmethod
  def wallet_choosing_amount(from_or_to, thirdparty_name):
    locator = (By.XPATH, "//div[@id = 'transfer_%s']//span[@class = '%s_balance']" % (from_or_to, thirdparty_name))
    return locator

  @staticmethod
  def wallet_choosing_btn_maintenance(thirdparty_name):
    locator = (By.XPATH, "//span[@class = '%s_balance']/../..//p[contains(text(),'维护中') and @style != 'display: none;']" % thirdparty_name)
    return locator

  #New Wap only

  # -------------------------------------------
  # 錢包展開
  nwap_from_btn = (By.XPATH, "(//div[@class= 'item-select__sel'])[1]")
  nwap_to_btn = (By.XPATH, "(//div[@class= 'item-select__sel'])[2]")
  # 確認
  nwap_submit_btn = (By.XPATH, "//button[text()= '确定']")
  # 錢包選擇鈕
  nwap_wallet_choosing_btn = (By.XPATH, f"//div[contains(@class, 'picker-column')]//div[text()= .]")
  # 更多
  more = (By.XPATH, "//p[text()= '更多']/..")
  # 收藏
  less = (By.XPATH, "//p[text()= '收起']/..")

  @staticmethod
  def nwap_wallet_choosing_btn_info(thirdparty_name='all'):
    if thirdparty_name == 'all':
      locator = (By.XPATH, f"//div[@class= 'list-item']//p[text()=.]/..")
    else:
      locator = (By.XPATH, f"//div[@class= 'list-item']//p[text()= '{thirdparty_name}']/..")

    return locator

  # 主錢包
  nwap_main_wallet_from = (By.XPATH, "//p[text()= '主钱包']/following::p")
  get_name_and_money = (By.XPATH, "//div[contains(@class,'list-item__text') or @class='main-item__text' or @class='wallet-list__item__rt']")
  main_wallet = (By.XPATH, '(//span[@class="cp_balance" or @class="text-txt__number"])[1]')
  nwap_main_wallet_money = (By.XPATH, "//p[text()= '主钱包']/..//span")

  # 交易流水
  nwap_today = (By.XPATH, "//span[text()='本日']")  #本日
  nwap_week = (By.XPATH, "//span[text()='本周']")  #本周
  nwap_amount_time = (By.XPATH, "(//h4[@class='mywallet-head'])[1]") #時間
  nwap_bet = (By.XPATH, "//div[@class='mywallet-list__item']") #單
  # 彩票選單
  nwap_picker_open = (By.XPATH, "//div[@class='mywallet-select']") # 下拉選單
  nwap_picker_down = (By.XPATH, "//div[@class='van-ellipsis' and contains(text(),.)]") # 向下滑動
  nwap_picker_submit = (By.XPATH, "//button[text()='确定']") # 確定
  # -------------------------------------------

  thirdparty_wallet_loading_mask = (By.ID, "jqueryEasyOverlayDiv")
  check_point_wallet_conversion = (By.XPATH, "//*[text()= '一键归户']")
  wallet_conversion=(By.XPATH, "//*[@id='nzc-menu-wallet' or text()= '转账']")
  wallet_maintain_btn_js = "span[class='van-button__text']" # js_click 定位用
  wallet_maintain_text = (By.XPATH, "//div[@class='van-dialog__message van-dialog__message--has-title']")
  wallet_amount_refresh_btn = (By.XPATH, "(//a[text() = '全部刷新' or @class= 'refresh'])[last()]")
  thirdparty_wallet_amount_input = (By.XPATH, "//input[@placeholder='请输入存款金额' or @placeholder='请输入整数转账金额']")
  thirdparty_wallet_submit = (By.XPATH, "//*[@class = 'submit' or contains(text(),'确定转入') or contains(text(), '提交')]")

  transfer_message_ok = (By.XPATH, "//p[@class = 'transfer-alert__title' or @class= 'xfe__title' and text() = '转换成功']") # 額度轉換訊息 成功
  transfer_message_other = (By.XPATH, "//p[@class = 'transfer-alert__title' or @class= 'xfe__title']") # 額度轉換訊息 其他
  transfer_message_btn = (By.XPATH, "//button[@class = 'btn-alert' or @class= 'btn btn-primary' and text() = '确认']") # 確定

  # 入款紀錄

  amount_to = (By.XPATH,"//*[@class = 'text-right']/span[contains(@data-bind,'depositamount')]") # 入款金額
  amount_before = (By.XPATH,"//*[@class = 'text-right']//span[contains(@data-bind,'amount_before')]") # 入款前
  amount_after = (By.XPATH,"//*[@class = 'text-right']//span[contains(@data-bind,'amount_after')]") # 入款後
  amount_status = (By.XPATH,"//*[@class = 'text-right' and contains(@data-bind,'statusList')]") # 儲值狀態
  amount_time = (By.XPATH,"(//td[contains(@data-bind,'addedtime')])[1]") # 儲值時間
  owner_total_money = (By.XPATH, "//span[@class = 'total_balance']") # 總金額

  # 交易流水類型
  search_all = (By.XPATH, "//select[contains(@data-bind,'typecodes')]")
  search_info = (By.XPATH, "//td[contains(@data-bind,'typename')]")
  amount_change = (By.XPATH, "//div[contains(@class, 'wallet_list') or contains(@class, 'mywallet')] \
    //*[contains(@data-bind, 'amount') or contains(text(), '金额')]/following::*")
  money_now = (By.XPATH, "//div[contains(@class, 'wallet_list') or contains(@class, 'mywallet')] \
    //*[contains(@data-bind, 'changed') or contains(text(), '现有金额') or contains(text(), '钱包馀额')]/following::*")

  def amount_sort(self,Sort):
    amount_sort = (By.XPATH,"//div[@class = 'text-right' and text() = '%s']"%Sort)
    return amount_sort

class ThirdPartyWalletPage(BasePage):
  def wait_wallet_loading_finish(self):
    self.sleep(1)
    if self.is_element_finded(Store_Record_Value.thirdparty_wallet_loading_mask) is True:
      self.wait_invisibility(Store_Record_Value.thirdparty_wallet_loading_mask)

  def get_main_wallet_nwap(self):
    self.wait_loading_finish()
    main_money = round(float(re.sub("[^0-9.]", "", (self.get_text(Store_Record_Value.nwap_main_wallet_money)))), 2)
    return main_money

  def do_walletre_fresh(self):
    self.wait_loading_finish()
    self.refresh_browser()
    self.wait_loading_finish()
    self.wait_visibility(Store_Record_Value.wallet_amount_refresh_btn)

    times = 1
    while True and times <=10:
      times = times + 1
      try:
        self.click(Store_Record_Value.wallet_amount_refresh_btn) # 全部錢包刷新
        self.check_conver_maintain()
        self.wait_wallet_loading_finish() # 等待額度轉換Loading結束
        break
      except:
        self.check_conver_maintain()
        self.sleep(3)

  def check_conver_maintain(self):
    if self.is_element_finded(Store_Record_Value.wallet_maintain_text) == True:
      self.click_js(Store_Record_Value.wallet_maintain_btn_js)

      self.click(Store_Record_Value.wallet_conversion)
      self.wait_loading_finish()
      assert self.is_element_finded(Store_Record_Value.check_point_wallet_conversion) is True

  def get_main_wallet(self):
    self.wait_loading_finish()
    wallet = round(float(self.get_text(Store_Record_Value.main_wallet).replace(',', '')), 2)
    
    return wallet

  def do_wallet_conversion(self, wallet_from, wallet_to, amount):
    self.wait_loading_finish()

    if datetime.time(9) < datetime.datetime.now().time() < datetime.time(11) and wallet_to == 'bbin':
      self.test_skip('BBIN 維護中')
      
    if self.is_element_finded(Store_Record_Value.wallet_choosing_btn('from', wallet_to)) is False and wallet_to != '主钱包':
      wallet_to = wallet_to.upper
      self.test_skip('無串接第三方品牌: %s'%wallet_to)

    if self.is_element_finded(Store_Record_Value.wallet_choosing_btn_maintenance(wallet_from)) is True or \
        self.is_element_finded(Store_Record_Value.wallet_choosing_btn_maintenance(wallet_to)) is True:
      self.test_skip('該通道額度轉換-維護中')

    self.do_walletre_fresh()
    self.wait_wallet_loading_finish()

    self.wait_visibility(Store_Record_Value.wallet_choosing_btn('from', wallet_from))
    money_before = float(self.find_element(Store_Record_Value.wallet_choosing_amount('from', 'cp')).text) # 主錢包
    self.click(Store_Record_Value.wallet_choosing_btn('from', wallet_from)) # 選轉出錢包

    self.wait_visibility(Store_Record_Value.wallet_choosing_btn('to', wallet_to))
    self.sleep(2)

    # 獲取原錢包額度
    before_from_amount = float(
      self.find_element(Store_Record_Value.wallet_choosing_amount('from', wallet_from)).text)
    before_to_amount = float(
      self.find_element(Store_Record_Value.wallet_choosing_amount('to', wallet_to)).text)

    self.click(Store_Record_Value.wallet_choosing_btn('to', wallet_to)) # 選轉入錢包

    if self.wait_visibility_status(Store_Record_Value.thirdparty_wallet_submit) is True:
      self.type(Store_Record_Value.thirdparty_wallet_amount_input, str(amount)) # 輸入轉換額度
      self.click(Store_Record_Value.thirdparty_wallet_submit) # 送出
    else:
      raise EOFError('沒自動導轉至輸入金額畫面')
    self.sleep(2)

    # 額度轉換訊息
    if self.wait_visibility_status (Store_Record_Value.transfer_message_ok) is True:
      message = self.get_text(Store_Record_Value.transfer_message_other)
      self.click(Store_Record_Value.transfer_message_btn)
    else:
      message = self.get_text(Store_Record_Value.transfer_message_other)
      raise EOFError(f'額度轉換失敗:{message}')

    # # Alert處理
    # self.wait_alert_present()
    # message = self.getAlertmessage() # 抓取提交後ALERT顯示訊息
    # self.accept_alert() # 關閉ALERT
    # self.wait_wallet_loading_finish() # 等額度轉換Loading結束
    sum = 0

    while True:
      sum+= 1
      # 獲取轉後錢包額度
      after_from_amount = float(
        self.find_element(Store_Record_Value.wallet_choosing_amount('from', wallet_from)).text) # 轉出錢包現額度
      after_to_amount = float(
        self.find_element(Store_Record_Value.wallet_choosing_amount('to', wallet_to)).text) # 轉入錢包現額度
      if after_to_amount!= before_to_amount and after_from_amount!= before_from_amount:
        break
      if sum == 10:
        raise BaseException('錢包刷新異常 %s to %s 前:%.2f 後:%.2f 前:%.2f 後:%.2f 一次10秒,共:%d次'
                  %(wallet_from,wallet_to ,before_from_amount,after_from_amount ,before_to_amount,after_to_amount,sum))
      # 全部刷新異常等待
      self.sleep(5)
      self.do_walletre_fresh()

    assert round(before_to_amount + amount,2) == after_to_amount, message + ': from %s to %s,主錢包更新金額錯誤' % (wallet_from, wallet_to)

    return money_before

  # 一鍵歸戶

  def do_wallet_return(self):
    self.wait_loading_finish() # 等待頁面讀取
    
    if self.is_element_finded(Store_Record_Value.main_wallet_from) is True:
      cp_wallet = self.get_text(Store_Record_Value.main_wallet_from)
      cp_wallet = float(re.sub("[^0-9.]", "", cp_wallet))
    else:
      cp_wallet = self.get_text(Store_Record_Value.nwap_main_wallet_from)
      cp_wallet = float(cp_wallet.replace(',', ''))
    
    self.click(Store_Record_Value.wallet_return_btn)
    self.sleep(3)
    self.wait_loading_finish()
  
    if self.is_element_finded (Store_Record_Value.transfer_message) is True:
      message = self.get_text(Store_Record_Value.transfer_message)
      assert str(message).__contains__('转换成功'), '一鍵歸戶失敗'
      self.click(Store_Record_Value.transfer_dialog_confirm_btn)
    elif self.is_element_finded (Store_Record_Value.wallet_return_btn) is True:
      raise EOFError('點擊一鍵虧戶失效')

    self.sleep(30)

    return cp_wallet

  # 判斷錢包是否低於1元(主錢包除外)
  def do_wallet_check(self, cp_wallet):
    self.wait_loading_finish()
    for loop in range(1,6):
      Total = 0
      counts = 0
      Wallet = 0
      maintain_list = []
      if self.is_element_finded(Store_Record_Value.wallet_maintain) == True:
        amount = 0
        maintain_list = [maintain.text for maintain in self.find_elements(Store_Record_Value.maintain_money) if float(maintain.text) >= 1]
      for money in self.find_elements(Store_Record_Value.wallet_check):
        if money.text == '':
          continue
        
        if float(money.text) >= 1:
          counts += 1
          if counts > 1 and float(money.text) != Wallet and maintain_list != []:
            if float(money.text) == float(maintain_list[amount]):
              if amount + 1  < len(maintain_list):
                amount += 1
              else:
                maintain_list = []
              counts -= 1
          if Wallet == 0:
            Wallet = float(money.text)

        if counts < 2 and float(money.text) < Wallet:
          Total = Total+float(money.text)
      if counts < 3:
        break
      else:
        if loop == 5:
           assert counts < 3, '錢包歸戶失敗,重複刷新次數:%s'%loop
        self.sleep(10)
        self.do_walletre_fresh()
    self.wait_loading_finish()
    assert counts < 3, '錢包歸戶失敗'

    assert round(Wallet + Total, 2) == round(float(self.get_text(Store_Record_Value.owner_total_money)), 2), '帳戶餘額與額度轉換錢包不相符'
    return round(Total, 2)

  # 交易流水
  def trading_flow(self, wallet_from,amount, money_before):
    self.wait_loading_finish()
    
    self.select_by_text(Store_Record_Value.search_all,'额度转换')
    self.wait_loading_finish()

    if wallet_from == 'cp':
      money_after = money_before-abs(float(self.get_text(Store_Record_Value.amount_change)))
      assert self.get_text(Store_Record_Value.amount_change) == '-1','交易流水錯誤'
    else:
      money_after = money_before+abs(float(self.get_text(Store_Record_Value.amount_change)))
      assert self.get_text(Store_Record_Value.amount_change) == '1','交易流水錯誤'
    self.wait_loading_finish()
    # assert money_after == float(self.get_text(Store_Record_Value.money_now)),'交易流水錯誤'
    assert abs(float(self.get_text(Store_Record_Value.amount_change))) == amount,'交易流水錯誤'

    amount_time = self.get_text(Store_Record_Value.amount_time) # 儲值時間
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    assert str(amount_time)[:10] == now_time,'儲值時間不正確:%s'%amount_time

  def maintenance_check(self, brand_list, Status):
    for brand in brand_list:
      
      if Status == True:
        assert self.is_element_finded(Store_Record_Value.wallet_choosing_btn_maintenance(brand)) is True, '該品牌應該顯示維護狀態'
      else:
        assert self.is_element_finded(Store_Record_Value.wallet_choosing_btn_maintenance(brand)) is False, '該品牌應該顯示啟用狀態'

  def nwap_do_wallet_check(self, cp_wallet):
    num = 0
    wallet_list = []
    error = False

    while True:
      if self.is_element_finded(Store_Record_Value.more) is True:
        self.click(Store_Record_Value.more)
        self.sleep(0.5)

      for wallet in self.find_elements(Store_Record_Value.nwap_wallet_choosing_btn_info()):
        try:
          third_wallet =  float(re.sub("[^0-9.]", "", third_wallet))
        except:
          third_wallet =  0.0

        if third_wallet != 0.0:
          error = True
          wallet_list.append(wallet.relpace('\n', ':'))

      if len(wallet_list) == 0:
        break

      if num == 5:
        raise EOFError(f'一鍵歸戶失敗, 從新整理次數:{num}次, 主錢包:{cp_wallet}, 錯誤錢包:{wallet_list}')
      else:
        num+=1
        wallet_list == 0
        error = False
        self.sleep(10)
        continue

    if error == True:
      if self.is_element_finded(Store_Record_Value.nwap_main_wallet_from) is True:
        cp_wallet_after = self.get_text(Store_Record_Value.main_wallet_from)
      else:
        cp_wallet_after = self.get_text(Store_Record_Value.nwap_main_wallet_from)
  
      cp_wallet_after = float(cp_wallet.replace(',', ''))
      assert cp_wallet == cp_wallet_after, f'主錢包金額不正確, 歸戶前:{cp_wallet}, 歸戶後:{cp_wallet_after}'

    self.click(Store_Record_Value.less)

  def nwap_get_wallet_money(self, wallet_to, wallet_from):
    if self.is_element_finded(Store_Record_Value.more) is True:
        self.click(Store_Record_Value.more)
        self.sleep(0.5)

    cp_wallet = self.get_text(Store_Record_Value.nwap_main_wallet_from)

    # 取得錢包
    if wallet_to != '主钱包':
        third_wallet = self.get_text(Store_Record_Value.nwap_wallet_choosing_btn_info(wallet_to))
    
    if wallet_from != '主钱包':
        third_wallet = self.get_text(Store_Record_Value.nwap_wallet_choosing_btn_info(wallet_from))
    
    cp_wallet = float(cp_wallet.replace(',', ''))
    try:
      third_wallet =  float(re.sub("[^0-9.]", "", third_wallet))
    except:
      third_wallet =  0

    if self.is_element_finded(Store_Record_Value.less) is True:
        self.click(Store_Record_Value.less)
        self.sleep(0.5)

    return cp_wallet, third_wallet

  # 選擇轉出錢包
  def nwap_select_wallet_from(self, wallet_from):
    #  轉出
    status = False
    self.click(Store_Record_Value.nwap_from_btn)
    self.wait_visibility(Store_Record_Value.nwap_wallet_choosing_btn)

    for third_name in self.find_elements(Store_Record_Value.nwap_wallet_choosing_btn):
      self.sleep(0.5)
      self.click_by_dom(third_name)

      if self.get_text_by_dom(third_name) == wallet_from:
        for loop in range(3):
          self.sleep(1)
          if self.is_element_displayed(Store_Record_Value.nwap_submit_btn) is True:
            self.click(Store_Record_Value.nwap_submit_btn)
            self.sleep(1)

            if self.is_element_displayed(Store_Record_Value.nwap_submit_btn) is False:
              status = True
              break

          if loop == 2:
            raise EOFError('點擊確認失敗')
      if status == True:
        break

  # 選擇轉入錢包
  def nwap_select_wallet_to(self, wallet_to):
    # 轉入
    status = False
    self.wait_visibility(Store_Record_Value.nwap_to_btn)
    self.click(Store_Record_Value.nwap_to_btn)

    for third_name in self.find_elements(Store_Record_Value.nwap_wallet_choosing_btn):
      self.sleep(0.5)
      self.click_by_dom(third_name)
  
      if self.get_text_by_dom(third_name) == wallet_to:
        for loop in range(3):
          self.sleep(1)
          if self.is_element_displayed(Store_Record_Value.nwap_submit_btn) is True:
            self.click(Store_Record_Value.nwap_submit_btn)
            self.sleep(1)

            if self.is_element_displayed(Store_Record_Value.nwap_submit_btn) is False:
              status = True
              break

          if loop == 2:
            raise EOFError('點擊確認失敗')
      if status == True:
        break

  def nwap_do_wallet_conversion(self, wallet_from, wallet_to, amount):
    self.wait_loading_finish()
    self.click(Store_Record_Value.more)
    self.sleep(0.5)
    
    if datetime.time(9) < datetime.datetime.now().time() < datetime.time(11) and wallet_to == 'bbin':
      self.test_skip('BBIN 維護中')
      
    if self.is_element_finded(Store_Record_Value.nwap_wallet_choosing_btn_info(wallet_to)) is False and wallet_to != '主钱包':
      wallet_to = wallet_to.upper
      self.test_skip('無串接第三方品牌: %s'%wallet_to)

    before_cp_wallet, before_third_wallet= self.nwap_get_wallet_money(wallet_from, wallet_to)

    self.do_walletre_fresh()
    self.wait_wallet_loading_finish()
    # 輸入金額
    self.type(Store_Record_Value.thirdparty_wallet_amount_input, amount)

    if wallet_from == 'AG':
      wallet_from = 'BBIN'  #轉入錢包已經是AG了，先換成其他錢包讓AG空出來
      self.nwap_select_wallet_from(wallet_from)
      self.nwap_select_wallet_to(wallet_to)
      wallet_from = 'AG'   

    self.nwap_select_wallet_from(wallet_from)
    self.nwap_select_wallet_to(wallet_to)

    # 送出
    self.click(Store_Record_Value.thirdparty_wallet_submit)


    # 額度轉換訊息
    if self.wait_visibility_status(Store_Record_Value.transfer_message_ok) is True:
      message = self.get_text(Store_Record_Value.transfer_message_other)
      self.click(Store_Record_Value.transfer_message_btn)
    else:
      message = self.get_text(Store_Record_Value.transfer_message_other)
      raise EOFError(f'額度轉換失敗:{message}')
    
    sum = 0

    while True:
      sum+= 1
      self.click(Store_Record_Value.more)
      self.sleep(0.5)
      after_cp_wallet, after_third_wallet= self.nwap_get_wallet_money(wallet_from, wallet_to)
      if before_cp_wallet != after_cp_wallet and before_third_wallet !=after_third_wallet:
        break
      
      if sum == 10:
        raise BaseException(f'錢包刷新異常, \n轉前: 主錢包:{before_cp_wallet} 第三方:{before_third_wallet}\n轉後: 主錢包:{after_cp_wallet} 第三方:{after_third_wallet}')

      # 全部刷新異常等待
      self.sleep(5)
      self.do_walletre_fresh()

    if wallet_from == '主钱包':
      assert round(before_cp_wallet - amount,2) == float(after_cp_wallet), message + f': from {wallet_from} to {wallet_to}, 主錢包轉出更新金額錯誤'
      assert round(before_third_wallet + amount,2) == float(after_third_wallet), message + f': from {wallet_from} to {wallet_to}, 第三方錢包轉入更新金額錯誤'
    else:
      assert round(before_cp_wallet + amount,2) == float(after_cp_wallet), message + f': from {wallet_from} to {wallet_to}, 主錢包轉入更新金額錯誤'
      assert round(before_third_wallet - amount,2) == float(after_third_wallet), message + f': from {wallet_from} to {wallet_to}, 第三方錢包轉出更新金額錯誤'
     
    return before_cp_wallet

  def get_name_and_money(self):
    _list = []
    self.click(Store_Record_Value.more)
    self.wait_visibility(Store_Record_Value.less)
    self.sleep(1)
    for loop in self.find_elements(Store_Record_Value.get_name_and_money):
        info = self.get_text_by_dom(loop).replace(',','')
        cut = info.split('\n')
        _list.append(cut)

    return _list

# 交易流水
  def nwap_trading_flow(self, wallet_from,amount, money_before):
    self.wait_loading_finish()
    for _ in range(0,5):
      self.click(Store_Record_Value.nwap_picker_open)
      self.wait_loading_finish()

      for type_name in self.find_elements(Store_Record_Value.nwap_picker_down):
        self.sleep(0.5)
        self.click_by_dom(type_name)

        if self.get_text_by_dom(type_name) == '额度转换':
          break

      self.wait_loading_finish()
    
      self.click(Store_Record_Value.nwap_picker_submit)
      self.wait_loading_finish()

      self.click(Store_Record_Value.nwap_week)
      self.sleep(3)
      self.click(Store_Record_Value.nwap_today)
      self.wait_loading_finish() 

      if self.is_element_finded(Store_Record_Value.nwap_bet) is True:
        if wallet_from == '主钱包':
          money_after = money_before-abs(float(self.get_text(Store_Record_Value.amount_change)))
          assert self.get_text(Store_Record_Value.amount_change) == '-1.00','交易流水錯誤'
        else:
          money_after = money_before+abs(float(self.get_text(Store_Record_Value.amount_change)))
          assert self.get_text(Store_Record_Value.amount_change) == '1.00','交易流水錯誤'

        self.wait_loading_finish()
        money_now = float(self.get_text(Store_Record_Value.money_now).replace(',', ''))
        change = int(abs(float(self.get_text(Store_Record_Value.amount_change))))

        assert money_after == money_now, f'錢包餘額與額度轉換頁不同 額度轉換頁:{money_after}, 交易流水頁:{money_now}'
        assert change == amount, f'轉帳金額與額度轉換頁不同 額度轉換頁:{change}, 交易流水頁:{amount}'

        amount_nwap = str(self.get_text(Store_Record_Value.nwap_amount_time))[3:14:1] # 儲值時間
        now_time = datetime.datetime.now().strftime('%Y{0}%m{1}%d{2}').format(*'年月日')
        assert amount_nwap == now_time,'儲值時間不正確:%s'%amount_nwap  #因server時間 有差異 後須修復再開啟
        break
      else:
        self.refresh_browser()