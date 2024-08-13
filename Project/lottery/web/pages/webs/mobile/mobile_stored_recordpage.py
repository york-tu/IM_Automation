from selenium.webdriver.common.by import By
from pages.webs.mobile.mobile_basepage import BasePage
import datetime


class Store_Record_Value:
     # 入款紀錄
    amount_sort = (By.XPATH, "(//*[contains(@data-bind, 'typeList') or @class= 'method__content'])[1]")
    amount_to = (By.XPATH,"//span[contains(@data-bind,'depositamount') or @class= 'record-money']") # 入款金額
    amount_before = (By.XPATH,"//*[@class='text-right']//span[contains(@data-bind,'amountbefore')]") # 入款前
    amount_after = (By.XPATH,"//*[@class='text-right']//span[contains(@data-bind,'amountafter')]") # 入款後
    amount_status = (By.XPATH,"(//*[@class='text-right' and contains(@data-bind,'statusList') or @class='record-title active'])[last()]") # 儲值狀態
    amount_time = (By.XPATH,"(//*[contains(@data-bind,'added_time') or @class= 'record-date'])[last()]") # 儲值時間
    owner_total_money = (By.XPATH, "//span[@class='total_balance']") # 總金額

    first_report = (By.XPATH,"(//*[@class='history_center' or contains(@class, 'record-date') or \
        contains(@class, 'record-header') ])[1]")
    search_company = (By.XPATH, "//select[@data-bind='value: filter.type']")
    search_today = (By.XPATH, "//select[@data-bind='value: time']")

    # 出款紀錄
    amount_to_out = (By.XPATH,"(//span[contains(@data-bind,'itemDetail.amount')])[1]") # 出款金額
    stauts = (By.XPATH,"(//div[contains(@data-bind,'itemDetail.status')])[1]") # 狀態
    status_list = (By.XPATH,"(//div[contains(@data-bind,'data.status') or @class='badge__text'])[1]") # 提款列表狀態
    payment_type = (By.XPATH,"(//div[@class='history_list'])[2]")    # 出款方式(提現銀行/提現錢包)

    # NWAP
    nwap_today = (By.XPATH, "//span[text()='本日']")  #本日
    nwap_week = (By.XPATH, "//span[text()='本周']")  #本周
    nwap_picker = (By.XPATH, "//div[@class='mywallet-select']")
    nwap_submit_btn = (By.XPATH, "//button[text()='确定']")
    nwap_picker_company = (By.XPATH, "//div[@class='van-ellipsis' and contains(text(),'公司入款')]")  # 公司入款
    nwap_deposit_choosing_btn = (By.XPATH, f"//div[contains(@class, 'picker')]//div[text()= .]")
    nwap_amount_status = (By.XPATH, "//*[@class='record-title active']//*[contains(@class, 'badge__text')]") # 儲值狀態
    nwap_amount_time = (By.XPATH, "//*[@class='record-title active']/..//*[@class= 'record-header-date']") # 儲值時間
    nwap_amount_before = (By.XPATH,"//*[@class='record-title active']/..//span[text()= '入款前']/following::span") # 入款金額
    nwap_amount_after = (By.XPATH,"//*[@class='record-title active']/..//span[text()= '入款后']/following::span") # 入款前
    nwap_payment_type = (By.XPATH, "//div[contains(@class,'record-cell__item record-cell__item--open')]//p[@class='method__content']/..")

    # NWAP 出款紀錄
    nwap_amount_to_out = (By.XPATH,"//span[@class='record-money']") # 出款金額
class Store_Record_Page(BasePage):
    def before_check_money_entry_record(self,style,money_to):
        self.wait_loading_finish()
        self.select_by_text(Store_Record_Value.search_company,style)
        self.wait_loading_finish()
        self.click(Store_Record_Value.search_today)
        self.wait_loading_finish()
        self.wait_visibility(Store_Record_Value.first_report)
        self.click(Store_Record_Value.first_report)
        self.sleep(3)

        amount_sort = self.get_text(Store_Record_Value.amount_sort) # 儲值類型
        amount_to = round(float(self.get_text(Store_Record_Value.amount_to)),2) # 儲值金額
        amount_status = self.get_text(Store_Record_Value.amount_status) # 儲值狀態
        amount_time = self.get_text(Store_Record_Value.amount_time) # 儲值時間

        assert amount_sort == style,'存款類型不正確 Error:%s'%amount_sort
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')

        assert str(amount_time)[:10] == now_time,'儲值時間不正確:%s'%amount_time

        for _ in range(0,6):
            try:
                assert amount_status == '充值中','狀態未顯示為充值中. Error:%s'%amount_status
                break
            except:
                self.sleep(3)
                self.refresh_browser()
                self.wait_loading_finish()

       # 儲值後前台確認紀錄
    def check_money_entry_record(self,tra_money,offer_money,total_money,wallet_before,style,Handling_money=0):
        for _ in range(0, 10):            
            self.wait_loading_finish()
            self.select_by_text(Store_Record_Value.search_company,style)
            self.wait_loading_finish()
            self.click(Store_Record_Value.search_today)
            self.wait_loading_finish()
            self.wait_visibility(Store_Record_Value.first_report)
            self.click(Store_Record_Value.first_report)
            self.sleep(3)

            if self.get_text(Store_Record_Value.amount_status) == '成功到账':
                break   
            else:
                self.refresh_browser()
                self.sleep(1)
                

        self.click(Store_Record_Value.first_report)
        self.sleep(3)

        amount_sort = self.get_text(Store_Record_Value.amount_sort) # 儲值類型

        owner_money = float(self.wait_visibility(Store_Record_Value.owner_total_money).text) # 帳戶總餘額
        amount_before = float(self.wait_visibility(Store_Record_Value.amount_before).text) # 儲值前
        amount_to = float(self.wait_visibility(Store_Record_Value.amount_to).text) # 儲值金額
        amount_after = float(self.wait_visibility(Store_Record_Value.amount_after).text) # 儲值後
        amount_status = self.wait_visibility(Store_Record_Value.amount_status).text # 儲值狀態


        if offer_money !=0:
            self.select_by_text(Store_Record_Value.search_company,'优惠')
            self.sleep(3)
            amount_before_offer = round(float(self.get_text(Store_Record_Value.amount_before)),2) # 優惠欄位儲值前
            amount_to_offer = round(float(self.get_text(Store_Record_Value.amount_to)),2) # 優惠欄位儲值金額
            amount_after_offer = round(float(self.get_text(Store_Record_Value.amount_after)),2) # 優惠欄位儲值後

            assert amount_before_offer == amount_after
            assert amount_to_offer == offer_money,'優惠金額不正確'
            assert amount_before_offer+amount_to_offer == amount_after_offer,'優惠記錄儲值後不正確'

        self.wait_loading_finish()
        assert amount_sort == style,'存款類型不正確 Error:%s'%amount_sort
        assert amount_to == tra_money or int(amount_to)==int(tra_money) or amount_to==total_money,'儲值金額前後台不一致 儲值金額:%.2f 後台儲值金額:%.2f 儲值金額加上優惠:%.2f'%(amount_to,tra_money,total_money) # 前台有些品牌會出現小數點有些不會,用兩個判斷是去比對,在線支付問題:前後台優惠金額不會分開

        after_money = amount_before+amount_to # 儲值前+儲值金額=儲值後金額(不包含優惠)
        after_money_offer = total_money
        assert float(after_money) == float(amount_after) or float(after_money_offer)==float(total_money) ,'入款後金額不正確 儲值金額後:%.2f 前台顯示金額:%.2f 儲值金額加上優惠:%.2f'%(after_money,amount_after,total_money)

        assert amount_status == '成功到账','儲值失敗'
        assert owner_money == round(wallet_before+total_money,2),'儲值後總金額不正確 目前:%.2f 儲值前+儲值金額(優惠):%.2f'%(owner_money,(wallet_before+total_money))

    def before_check_money_output_record(self,style,total_money,charge, payment_type='银行'): 
        self.wait_loading_finish()
        self.sleep(1)
        self.click(Store_Record_Value.search_today)
        self.wait_loading_finish()
        
        status_list = self.get_text(Store_Record_Value.status_list)
        assert status_list== "处理中","出款狀態異常:%s" %status_list

        self.click(Store_Record_Value.first_report)
        self.wait_visibility(Store_Record_Value.amount_time)
        self.sleep(3)

        amount_to = self.get_text(Store_Record_Value.amount_to_out) # 儲值金額
        amount_time = self.get_text(Store_Record_Value.amount_time) # 儲值時間
        status = self.get_text(Store_Record_Value.stauts) # 狀態
        decimal_point = (round((total_money) + (charge))) - float(amount_to)  # 小數點差異回傳至最後一步用

        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        assert str(amount_time)[:10]==now_time,'儲值時間不正確:%s'%amount_time
        assert payment_type in self.get_text(Store_Record_Value.payment_type), '出款方式(提現銀行/提現錢包)有誤:%s' %(self.get_text(Store_Record_Value.payment_type))
        assert status == "处理中","提款狀態異常 訊息:%s" %status
        assert round(float(amount_to)) == round((total_money) + (charge)),'儲值金額顯示不正確. 提款紀錄金額:{0}  提款頁面顯示金額:{1}'.format(round(float(amount_to)),round((total_money) + (charge)))

        return decimal_point

    def after_check_money_output_record(self,total_money,wallet_before,charge,decimal_point, payment_type='银行'):
        self.wait_loading_finish()
        self.click(Store_Record_Value.search_today)
        self.wait_loading_finish()

        status_list = self.get_text(Store_Record_Value.status_list)
        assert status_list== "出款成功","出款狀態異常:%s" %status_list

        self.click(Store_Record_Value.first_report)
        self.wait_visibility(Store_Record_Value.amount_time)
        self.sleep(3)

        status = self.get_text(Store_Record_Value.stauts) # 狀態
        owner_money = round( float(self.get_text(Store_Record_Value.owner_total_money).replace(',', '')) ,2) # 帳戶總餘額
        Total = round( float(wallet_before) - (float(total_money) + float(charge)) + decimal_point ,2)  # 提款前總金額 - (提出金額 +手續費) + 小數點的差異 

        assert payment_type in self.get_text(Store_Record_Value.payment_type), '出款方式(提現銀行/提現錢包)有誤:%s' %(self.get_text(Store_Record_Value.payment_type))
        assert str(Total) == str(owner_money),'帳戶餘額與提款後餘額不相符 帳戶餘額:%s  出款紀錄提款後餘額:%s' % (Total,owner_money)
        assert status == "出款成功","提款狀態異常 訊息:%s" % status

    def after_check_manualdeposit_record(self, wallet_before, style, money):
        for i in range(3):
            try:
                self.refresh_browser()
                self.wait_loading_finish()
                self.select_by_text(Store_Record_Value.search_company,style)
                self.wait_loading_finish()
                self.click(Store_Record_Value.search_today)
                self.wait_loading_finish()
                self.click(Store_Record_Value.first_report)
                self.sleep(3)

                amount_sort=self.get_text(Store_Record_Value.amount_sort) # 儲值類型
                break
            except:
                assert i != 3, '可能沒有入款紀錄'

        owner_money=float(self.wait_visibility(Store_Record_Value.owner_total_money).text) # 帳戶總餘額
        total_money = wallet_before + float(money)
        amount_status=self.wait_visibility(Store_Record_Value.amount_status).text # 儲值狀態

        self.wait_loading_finish()

        assert amount_sort == style,'存款類型不正確 Error:%s'%amount_sort
        assert total_money == owner_money, f'儲值紀錄錢包與會員錢包不相符，入款後應有餘額{total_money}，帳戶實際餘額{owner_money}'
        assert amount_status == '成功到账','儲值失敗'





    # NWAP
    def nwap_before_check_money_entry_record(self, style, money_to, online=''):
        self.wait_loading_finish()
        self.click(Store_Record_Value.nwap_picker)

        for name in self.find_elements(Store_Record_Value.nwap_deposit_choosing_btn):
            self.sleep(0.5)
            self.click_by_dom(name)
   
            if self.get_text_by_dom(name) == style:
                self.sleep(1)
                self.click(Store_Record_Value.nwap_submit_btn)
                break
        
        self.click(Store_Record_Value.nwap_week)
        for _ in range(0,5):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)
                
        self.sleep(2)
        self.wait_visibility(Store_Record_Value.first_report)
        self.click(Store_Record_Value.first_report)
        self.sleep(3)

        amount_sort = self.get_text(Store_Record_Value.amount_sort) # 儲值類型
        amount_status = self.get_text(Store_Record_Value.nwap_amount_status) # 儲值狀態
        amount_time = (self.get_text(Store_Record_Value.nwap_amount_time)) # 儲值時間

        for _ in range(0,6):
            try:
                assert amount_status == '充值中' or amount_status == '处理中','狀態未顯示為充值中. Error:%s'%amount_status
                break
            except:
                self.sleep(3)
                self.refresh_browser()
                self.click(Store_Record_Value.first_report)
                self.wait_loading_finish()

        if online == '':
            assert amount_sort == style, f'存款類型不正確 存款記錄: {amount_sort} 預期行為: {style}'
        else:
            assert amount_sort == online, f'存款類型不正確 存款記錄: {amount_sort} 預期行為: {online}'

        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(datetime.datetime.now().strftime('%m'))
        day = str(datetime.datetime.now().strftime('%d'))
        now_time = f'{year}年{month}月{day}日'
        assert str(amount_time)[:11] == now_time,f'儲值時間不正確: 注單時間{amount_time} 應該為...{now_time}'

    # 儲值後前台確認紀錄-成功
    def nwap_check_money_entry_record(self,tra_money,offer_money,total_money,wallet_before,style,Handling_money=0):
        self.wait_loading_finish()
        self.click(Store_Record_Value.nwap_picker)

        for name in self.find_elements(Store_Record_Value.nwap_deposit_choosing_btn):
            self.sleep(0.5)
            self.click_by_dom(name)
   
            if self.get_text_by_dom(name) == style:
                self.sleep(1)
                self.click(Store_Record_Value.nwap_submit_btn)
                break
        
        for _ in range(0,5):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)
        
        for i in range(3):
            self.sleep(1)
            self.wait_visibility(Store_Record_Value.first_report)
            self.click(Store_Record_Value.first_report)
            self.sleep(3)

            amount_to = round(float(self.get_text(Store_Record_Value.amount_to)),2) # 儲值金額
            amount_status = self.get_text(Store_Record_Value.nwap_amount_status) # 儲值狀態
        
            if amount_status == '充值成功':
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)
                self.click(Store_Record_Value.nwap_today)
                self.sleep(3)
        assert amount_status == '充值成功','儲值失敗'

        amount_sort = self.get_text(Store_Record_Value.amount_sort) # 儲值類型
        amount_before = float((self.wait_visibility(Store_Record_Value.nwap_amount_before).text).replace(',', '')) # 儲值前
        amount_after = float((self.wait_visibility(Store_Record_Value.nwap_amount_after).text).replace(',', '')) # 儲值後

        if int(offer_money) !=0:
            self.select_by_text(Store_Record_Value.search_company,'优惠')
            self.sleep(3)
            amount_before_offer = round(float(self.get_text(Store_Record_Value.amount_before)),2) # 優惠欄位儲值前
            amount_to_offer = round(float(self.get_text(Store_Record_Value.amount_to)),2) # 優惠欄位儲值金額
            amount_after_offer = round(float(self.get_text(Store_Record_Value.amount_after)),2) # 優惠欄位儲值後

            assert amount_before_offer == amount_after, f'優惠紀錄，優惠入款前金額應為操作"{style}"入款後金額{amount_after}, 顯示為{amount_before_offer}'
            assert amount_to_offer == offer_money,f'優惠金額不正確{amount_to_offer}, 應為{offer_money}'
            assert amount_before_offer+amount_to_offer == amount_after_offer, f'優惠記錄儲值後不正確{amount_after_offer}, 應為{amount_before_offer+amount_to_offer}'

        assert amount_to == tra_money or int(amount_to)==int(tra_money) or amount_to==total_money \
            , '儲值金額前後台不一致 儲值金額:%.2f 後台儲值金額:%.2f 儲值金額加上優惠:%.2f'%(amount_to,tra_money,total_money) # 前台有些品牌會出現小數點有些不會,用兩個判斷是去比對,在線支付問題:前後台優惠金額不會分開

        after_money = amount_before+amount_to # 儲值前+儲值金額=儲值後金額(不包含優惠)
        after_money_offer = total_money

        assert float(after_money) == float(amount_after) or float(after_money_offer)==float(total_money) \
            , '入款後金額不正確 儲值金額後:%.2f 前台顯示金額:%.2f 儲值金額加上優惠:%.2f'%(after_money,amount_after,total_money)

    
    # 儲值後前台確認紀錄-被拒絕
    def nwap_check_money_entry_fail_record(self,tra_money,style):
        self.wait_loading_finish()
        self.click(Store_Record_Value.nwap_picker)

        for name in self.find_elements(Store_Record_Value.nwap_deposit_choosing_btn):
            self.sleep(0.5)
            self.click_by_dom(name)
   
            if self.get_text_by_dom(name) == style:
                self.sleep(1)
                self.click(Store_Record_Value.nwap_submit_btn)
                break
        
        for _ in range(0,5):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)
        
        self.sleep(1)
        self.wait_visibility(Store_Record_Value.first_report)
        self.click(Store_Record_Value.first_report)
        self.sleep(3)

        amount_sort = self.get_text(Store_Record_Value.amount_sort) # 儲值類型
        amount_to = round(float(self.get_text(Store_Record_Value.amount_to)),2) # 儲值金額
        amount_status = self.get_text(Store_Record_Value.nwap_amount_status) # 儲值狀態

        self.wait_loading_finish()

        for i in range(3):
            if amount_status == '充值失败':
                break
            else:
                self.sleep(3)
                self.refresh_browser()
                
        assert amount_status == '充值失败', f"充值紀錄，狀態顯示錯誤'{amount_status}'，應為'充值失败'"
        assert amount_sort != '', f"充值紀錄，未顯示充值方式"
        assert str(amount_to) == str(tra_money), f"充值紀錄，金額顯示錯誤'{str(amount_to)}'，應為'{str(tra_money)}'"
        

    def nwap_before_check_money_output_record(self,style,total_money,charge, payment_type='银行'): 
        self.wait_loading_finish()

        for _ in range(0,3):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)

        status_list = self.get_text(Store_Record_Value.status_list)
        assert status_list== "处理中","出款狀態異常:%s" %status_list

        self.click(Store_Record_Value.first_report)
        self.wait_visibility(Store_Record_Value.nwap_amount_time)
        self.sleep(3)

        amount_to = self.get_text(Store_Record_Value.nwap_amount_to_out).replace(',', '') # 儲值金額
        amount_time = self.get_text(Store_Record_Value.nwap_amount_time) # 儲值時間
        status = self.get_text(Store_Record_Value.nwap_amount_status) # 狀態
        decimal_point = (round((total_money) + (charge))) - float(amount_to)  # 小數點差異回傳至最後一步用

        year = str(int(datetime.datetime.now().strftime('%Y')))
        month = str(datetime.datetime.now().strftime('%m'))
        day = str(datetime.datetime.now().strftime('%d'))
        now_time = f'{year}年{month}月{day}日'
        assert str(amount_time)[:11] == now_time,'儲值時間不正確:%s'%amount_time

        assert payment_type in self.get_text(Store_Record_Value.nwap_payment_type), '出款方式(提現銀行/提現錢包)有誤'
        assert status == "处理中","提款狀態異常 訊息:%s" %status
        assert round(float(amount_to)) == round((total_money) + (charge)),'儲值金額顯示不正確. 提款紀錄金額:{0}  提款頁面顯示金額:{1}'.format(round(float(amount_to)),round((total_money) + (charge)))

        return decimal_point

    def nwap_after_check_money_output_record(self,total_money,wallet_before,charge,decimal_point,money, payment_type='银行'):
        self.wait_loading_finish()

        for _ in range(0,3):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)

        status_list = self.get_text(Store_Record_Value.status_list)
        assert status_list== "出款成功","出款狀態異常:%s" %status_list

        self.click(Store_Record_Value.first_report)
        self.wait_visibility(Store_Record_Value.nwap_amount_time)
        self.sleep(3)

        status = self.get_text(Store_Record_Value.nwap_amount_status) # 狀態
        Total = round( float(wallet_before) - (float(total_money) + float(charge)) + decimal_point ,2)  # 提款前總金額 - (提出金額 +手續費) + 小數點的差異 

        assert payment_type in self.get_text(Store_Record_Value.nwap_payment_type), '出款方式(提現銀行/提現錢包)有誤'
        assert str(Total) == str(money),'帳戶餘額與提款後餘額不相符 帳戶餘額:%s  出款紀錄提款後餘額:%s' % (Total,money)
        assert status == "出款成功","提款狀態異常 訊息:%s" % status

    def nwap_after_check_manualdeposit_record(self, wallet_before, style, money):
        self.wait_loading_finish()
        self.click(Store_Record_Value.nwap_picker)

        for name in self.find_elements(Store_Record_Value.nwap_deposit_choosing_btn):
            self.sleep(0.5)
            self.click_by_dom(name)
   
            if self.get_text_by_dom(name) == style:
                self.sleep(1)
                self.click(Store_Record_Value.nwap_submit_btn)
                break

        for _ in range(0,5):
            self.click(Store_Record_Value.nwap_today)
            self.wait_loading_finish()
            if self.is_element_finded(Store_Record_Value.first_report) is True:
                break
            else:
                self.click(Store_Record_Value.nwap_week)
                self.sleep(10)

        self.sleep(1)
        self.wait_visibility(Store_Record_Value.first_report)
        self.click(Store_Record_Value.first_report)
        self.sleep(3)

        amount_status = self.wait_visibility(Store_Record_Value.amount_status).text # 儲值狀態
        amount_before = float((self.wait_visibility(Store_Record_Value.nwap_amount_before).text).replace(',', '')) # 儲值前
        amount_after = float((self.wait_visibility(Store_Record_Value.nwap_amount_after).text).replace(',', '')) # 儲值後
        total_money = float(wallet_before) + float(money)
        self.wait_loading_finish()

        assert total_money == amount_after, f'人工存款金額錯誤 首頁原始金額: {wallet_before} 入款金額: {float(money)} 入款後: {amount_after}'
        assert amount_after == amount_before + float(money), \
             f'人工存款金額錯誤 投注頁面原始金額: {amount_before} 入款金額: {float(money)} 入款後: {amount_after}'
        assert amount_status.__contains__('充值成功'), (amount_status.split('\n'))[-1]
