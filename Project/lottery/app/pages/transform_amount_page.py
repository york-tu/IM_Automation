import common.utils.globalvar as gl
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from retrying import retry
from poco.exceptions import PocoNoSuchNodeException
class TransformPageLocator:
    base = Xpath_Base()

    expand_wallet = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='更多'),
        iOS = base.data_collation(type_kind='name', type_name='更多')
    )

    message = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='关闭.*', action='parent().parent().child()[2]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='关闭.*', action='parent().parent().child()[2]')
    )

    message_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='关闭', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='name', type_name='关闭', action='parent().child()[2]')
    )

    transfer_out_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*src_wallet_sp'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*src_wallet_sp')
    )

    transfer_in_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*dest_wallet_sp'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*dest_wallet_sp')
    )

    transfer_out = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='1.选取转出钱包'),
        iOS = base.data_collation(type_kind='name', type_name='1.选取转出钱包')
    )

    transfer_in = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='2.选取转入钱包'),
        iOS = base.data_collation(type_kind='name', type_name='2.选取转入钱包')
    )

    success = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='转换成功'),
        iOS = base.data_collation(type_kind='name', type_name='转换成功')
    )

    submit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='提交'),
        iOS = base.data_collation(type_kind='name', type_name='提交')
    )

    submit_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确定转入'),
        iOS = base.data_collation(type_kind='name', type_name='确定转入')
    )

    amount_edit = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入存款金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入存款金额')
    )

    amount_edit_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入整数转账金额'),
        iOS = base.data_collation(type_kind='name', type_name='请输入整数转账金额')
    )

    amount_edit_field = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*transfer_amount_root_cl'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*transfer_amount_root_cl')
    )

    amount_field_closs = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*transfer_amount_clear_iv'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*transfer_amount_clear_iv')
    )

    all_return_cp = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='^一键归户.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='^一键归户.*')
    )

    register_button = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='注册账户'),
        iOS = base.data_collation(type_kind='name', type_name='注册账户')
    )

    loading = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='^处理中.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='^处理中.*')
    )

    reset = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='全部刷新.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='全部刷新.*')
    )

    reset_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*balance_refresh_iv'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*balance_refresh_iv')
    )

    ok = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='确认.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='确认.*')
    )

    ag = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='AG.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='AG.*')
    )

    # 錢包資訊
    @staticmethod
    def wallet_info(name, list):
        action = ''
        num = ''

        if gl.get_value('PHONE_PLATFORM') == 'Android':
            if name == '主钱包':
                action = 'parent().child()[2]'
            else:
                action = 'parent().child()[1]'

        elif gl.get_value('PHONE_PLATFORM') == 'iOS':
            if name == '主钱包':
                num = 0
                action = ''
            else:
                num = ''
                if list == 0:
                    action = 'child().child().child()'
                else:
                    action = ''

        wallet = TransformPageLocator.base.check_device(
            Android = TransformPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{name}.*', action=action),
            iOS = TransformPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{name}.*', action=action, num=num)
        )

        return wallet

    # 錢包按鈕
    @staticmethod
    def wallet_button(name, num='', list=0):
        action = ''

        if gl.get_value('PHONE_PLATFORM') == 'iOS':
            if name == '主钱包':
                action = ''
            else:
                num = ''
                if list == 0:
                    action = f"offspring(nameMatches='{name}.*')[2]"
                else:
                    action = ''

        wallet = TransformPageLocator.base.check_device(
            Android = TransformPageLocator.base.data_collation(type_kind='text', type_name=name),
            iOS = TransformPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{name}.*', action=action, num=num)
        )

        return wallet
    
    @staticmethod
    def maintenance(name):
        status = TransformPageLocator.base.check_device(
            Android = TransformPageLocator.base.data_collation(type_kind='text', type_name=f'{name}-维护中'),
            iOS = TransformPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{name}-维护中')
        )

        return status

    @staticmethod
    def wallet_info_napp(name):
        if name == '主钱包':
            action = 'parent().child()[3]'
        else:
            action = 'parent().child()[1]'
        status = TransformPageLocator.base.check_device(
            Android = TransformPageLocator.base.data_collation(type_kind='text', type_name=name, action=action),
            iOS = TransformPageLocator.base.data_collation(type_kind='name', type_name=name, action=action)
        )

        return status

    @staticmethod
    def specified_wallet(name):
        status = TransformPageLocator.base.check_device(
            Android = TransformPageLocator.base.data_collation(type_kind='text', type_name=name),
            iOS = TransformPageLocator.base.data_collation(type_kind='name', type_name=name)
        )

        return status

class TransformPage(Base):
    # 全部刷新
    def refresh_all(self):
        self.common.poco_wait_exists(TransformPageLocator.reset)
        self.common.poco_click(TransformPageLocator.reset)

        for i in range(0, 30):
            self.common.sleep(1) # 避免執行太快, loading還未出現
            if self.common.poco_exists(TransformPageLocator.loading) is False:
                break
            
            if i == 29:
                raise EOFError('全部刷新的loading屏幕未消失, 等待時間:30秒')

    # 全部刷新
    def refresh_all_napp(self):
        self.common.go_top()
        self.common.poco_wait_exists(TransformPageLocator.reset_napp)
        self.common.poco_click(TransformPageLocator.reset_napp)
        self.common.sleep(3) 

    # 尋找指定錢包
    def look_for_wellet(self, wallet):
        for down_count in range(3):
            # 如果指定錢包不在畫面上, 就下滑畫面尋找
            if self.common.poco_exists(TransformPageLocator.wallet_info(wallet, 0)) is False:
                if self.common.poco_exists(TransformPageLocator.wallet_info(wallet, 1)) is False:
                    self.common.go_down()
                else:
                    return down_count       # 紀錄下滑幾次，之後就不用再尋找錢包
            else:
                return down_count
                
        raise EOFError(f'找不到{wallet}錢包')

    # 下滑轉出錢包選單
    def down_wallet_out_list(self):
        data = {'pos':(0.25, 0.9, 0.25, 0.5)}
        self.common.swipe_speed(data, 0.2)

    # 上滑轉出錢包選單
    def up_wallet_out_list(self):
        data = {'pos':(0.25, 0.5, 0.25, 0.9)}
        self.common.swipe_speed(data, 0.1)

    # 下滑轉入錢包選單
    def down_wallet_in_list(self):
        data = {'pos':(0.75, 0.9, 0.75, 0.5)}
        self.common.swipe_speed(data, 0.2)

    # 上滑轉入錢包選單置頂
    def up_wallet_in_list(self):
        data = {'pos':(0.75, 0.5, 0.75, 0.9)}
        self.common.swipe_speed(data, 0.05)

    # 下滑到指定錢包
    def down_to_wallet(self, down_count):
        for _ in range(down_count):
            self.common.go_down()
            self.common.sleep(1)

    # 抓取錢包餘額
    def get_wallet_amount(self, wallet_list: list, down_count=0):
        amount_dict = {}
        
        for wallet in wallet_list:
            self.common.go_top()    # 抓取錢包前, 返回畫面最上方
            if wallet != '主钱包':
                if len(wallet_list) > 2:
                    self.look_for_wellet(wallet)
                else:
                    self.down_to_wallet(down_count)     
            try:
                info = self.common.poco_get_text(TransformPageLocator.wallet_info(wallet, 0))
            except:
                info = self.common.poco_get_text(TransformPageLocator.wallet_info(wallet, 1))
            
            try:
                money = float(info.replace(f'{wallet}', '').replace('馀额: ', ''))
                gl.set_value(wallet, money)
                amount_dict[wallet] = money
            except:
                raise EOFError(f'找不到{wallet}錢包資訊')
        
        self.common.go_top()    # 抓取錢包完畢, 返回畫面最上方

        return amount_dict

    # 抓取錢包餘額
    def get_wallet_amount_napp(self, wallet_list: list):
        amount_dict = {}
        
        for wallet in wallet_list:   
            try:
                info = self.common.poco_get_text(TransformPageLocator.wallet_info_napp(wallet))
                if info == '维护中':
                    gl.set_value(wallet, info)
                    continue
                money = float(info.replace(',',''))
                gl.set_value(wallet, money)
                amount_dict[wallet] = money
            except:
                raise EOFError(f'找不到{wallet}錢包資訊')

        return amount_dict

    # 點擊錢包
    def click_wallet(self, wallet, down_count, num=''):
        if wallet != '主钱包':      
            self.down_to_wallet(down_count)
        try:
            self.common.poco_click(TransformPageLocator.wallet_button(wallet, num, 0))
        except:
            self.common.poco_click(TransformPageLocator.wallet_button(wallet, num, 1))

    # 錢包額度轉換
    def transform_money(self, start, stop, amount, down_count):
        while not self.common.poco_exists(TransformPageLocator.amount_edit):
            self.click_wallet(start, down_count, 0)
            self.common.sleep(1)
            self.click_wallet(stop, down_count, 2)
            self.common.sleep(1)
            self.common.go_top()

        self.common.poco_send_text(TransformPageLocator.amount_edit, amount)
        self.common.poco_click(TransformPageLocator.submit)
        
        # 確認額度轉換狀態彈窗
        for i in range(0, 31):
            if self.common.poco_exists(TransformPageLocator.ok) is True:
                self.common.poco_click(TransformPageLocator.ok)
                break
            
            try: # 不知道為什麼常常message在畫面上，還是會抓不到
                message = self.common.poco_get_text(TransformPageLocator.message)
                if message.__contains__('维护中'):
                    self.common.skip_test(message)
            except PocoNoSuchNodeException: 
                pass 
            
            if i == 30:
                raise EOFError(f'{start} to {stop} 太久未完成, 等待時間:30秒, {message}')

    # 操作轉出錢包
    def select_transform_out_wallet(self, start):
        self.common.go_bottom()
        self.common.poco_click(TransformPageLocator.transfer_out_napp)
        self.up_wallet_out_list()
        if self.common.poco_exists(TransformPageLocator.specified_wallet(start)):
            self.common.poco_click(TransformPageLocator.specified_wallet(start))
        else:
            for _ in range(3):
                self.down_wallet_out_list()
                if self.common.poco_exists(TransformPageLocator.specified_wallet(start)):
                    self.common.poco_click(TransformPageLocator.specified_wallet(start))
                    return 
            
            if self.common.poco_exists(TransformPageLocator.specified_wallet('GC')):
                self.common.poco_click(TransformPageLocator.specified_wallet('GC'))     # 指定的轉出錢包如果已經是轉入錢包就先選其他錢包
            else:
                self.up_wallet_out_list()
                self.common.poco_click(TransformPageLocator.specified_wallet('GC'))
            return True

    # 操作轉入錢包
    def select_transform_in_wallet(self, stop):
        self.common.go_bottom()
        self.common.poco_click(TransformPageLocator.transfer_in_napp)
        self.up_wallet_in_list()
        for i in range(4):
            if self.common.poco_exists(TransformPageLocator.specified_wallet(stop)):
                self.common.poco_click(TransformPageLocator.specified_wallet(stop))
                break
            else:
                self.down_wallet_in_list()
            
            if i == 3:
                raise EOFError('找不到轉入錢包')

    # 錢包額度轉換
    def transform_money_napp(self, start, stop, amount):
        # 操作轉出錢包
        wallet_unfound = self.select_transform_out_wallet(start)
        self.common.sleep(1)

        # 操作轉入錢包
        self.select_transform_in_wallet(stop)
        self.common.sleep(1)

        if wallet_unfound:
            self.select_transform_out_wallet(start)     # 指定的轉出錢包如果剛剛是轉入錢包就需要再選一次
            self.common.sleep(1)

        if self.common.poco_exists(TransformPageLocator.amount_edit_napp):
            self.common.poco_send_text(TransformPageLocator.amount_edit_napp, amount)
        else:
            self.common.poco_click(TransformPageLocator.amount_edit_field)
            self.common.poco_click(TransformPageLocator.amount_field_closs)
            self.common.poco_send_text(TransformPageLocator.amount_edit_napp, amount)
        self.common.poco_click(TransformPageLocator.submit_napp)
        
        # 確認額度轉換狀態彈窗
        for i in range(0, 31):
            if self.common.poco_exists(TransformPageLocator.ok) is True:
                self.common.poco_click(TransformPageLocator.ok)
                break
            self.common.sleep(1)

            try: 
                message = self.common.poco_get_text(TransformPageLocator.message_napp)
                if message.__contains__('维护中'):
                    self.common.skip_test(message)
            except PocoNoSuchNodeException: 
                pass 
            
            if i == 30:
                raise EOFError(f'{start} to {stop} 太久未完成, 等待時間:30秒, {message}')

    # 額度轉換並比對
    def transform_money_compare(self, start, stop, amount):
        
        if stop != '主钱包':
            # 載入頁面時, 第三方錢包顯示的速度比較慢, 如果直接執行有可能跳錯, 拿AG當等待標的
            if self.common.poco_wait_exists(TransformPageLocator.ag) is False:
                raise EOFError('進入額度轉換錯誤')
            # 如果第三方在維護, 則skip操作
            down_count = self.look_for_wellet(stop)
            if self.common.poco_exists(TransformPageLocator.maintenance(stop)):
                self.common.skip_test(f"{stop}錢包維護中")
        else:
            down_count = self.look_for_wellet(start)

        # 撈取轉換前 錢包的錢
        self.refresh_all()
        amount_before = self.get_wallet_amount([start, stop], down_count) # 取得轉換前兩個錢包
        before_start = int(amount_before[start]) # 取出轉出錢包
        before_stop = int(amount_before[stop]) # 取出轉入錢包

        # 進行額度轉換
        self.transform_money(start, stop, amount, down_count)

        # 確認額度轉換前後 錢包金額正確
        for loop in range(0, 6):
            # 撈取轉換後 錢包的錢
            self.refresh_all()
            amount_after = self.get_wallet_amount([start, stop], down_count) # 取得轉換後兩個錢包
            after_start = int(amount_after[start]) # 取出轉出錢包
            after_stop = int(amount_after[stop]) # 取出轉入錢包
            
            # 計算錢包轉換前後的差額
            # 浮點數運算後, 做==比對 有機會出錯, 反正額度轉換無法轉小數, 故皆取整數比較
            result1 = before_start - after_start
            result2 = after_stop - before_stop

            if result1 == result2 and result1 == int(amount):
                break

            if loop == 5:
                raise EOFError(f'{start} to {stop} 金額錯誤, 刷新次數:{loop}, {start} 轉換前:{before_start} 後:{after_start}' \
                    + f', {stop} 轉換前:{before_stop} 後:{after_stop}')
              
            self.common.sleep(1)

    # 額度轉換並比對
    def transform_money_compare_napp(self, start, stop, amount):
        
        if stop != '主钱包':
            # 載入頁面時, 第三方錢包顯示的速度比較慢, 如果直接執行有可能跳錯, 拿AG當等待標的
            if self.common.poco_wait_exists(TransformPageLocator.ag) is False:
                raise EOFError('進入額度轉換錯誤')
            # 如果第三方在維護, 則skip操作
            self.refresh_all_napp()
            self.common.poco_click(TransformPageLocator.expand_wallet)  # 展開錢包列表
            if self.common.poco_get_text(TransformPageLocator.wallet_info_napp(stop)) == '维护中':
                self.common.skip_test(f"{stop}錢包維護中")
        else:
            self.refresh_all_napp()
            self.common.poco_click(TransformPageLocator.expand_wallet)

        # 撈取轉換前 錢包的錢
        amount_before = self.get_wallet_amount_napp([start, stop]) # 取得轉換前兩個錢包
        before_start = int(amount_before[start]) # 取出轉出錢包
        before_stop = int(amount_before[stop]) # 取出轉入錢包

        # 進行額度轉換
        self.transform_money_napp(start, stop, amount)

        # 確認額度轉換前後 錢包金額正確
        for loop in range(0, 6):
            # 撈取轉換後 錢包的錢
            self.refresh_all_napp()
            self.common.poco_click(TransformPageLocator.expand_wallet)
            amount_after = self.get_wallet_amount_napp([start, stop]) # 取得轉換後兩個錢包
            after_start = int(amount_after[start]) # 取出轉出錢包
            after_stop = int(amount_after[stop]) # 取出轉入錢包
            
            # 計算錢包轉換前後的差額
            # 浮點數運算後, 做==比對 有機會出錯, 反正額度轉換無法轉小數, 故皆取整數比較
            result1 = before_start - after_start
            result2 = after_stop - before_stop

            if result1 == result2 and result1 == int(amount):
                break

            if loop == 5:
                raise EOFError(f'{start} to {stop} 金額錯誤, 刷新次數:{loop}, {start} 轉換前:{before_start} 後:{after_start}' \
                    + f', {stop} 轉換前:{before_stop} 後:{after_stop}')

    # 一鍵歸戶
    def money_return_cp(self):
        self.common.poco_click(TransformPageLocator.all_return_cp)
        if self.common.poco_wait_exists(TransformPageLocator.ok) is True:
            self.common.poco_click(TransformPageLocator.ok)
        else:
            raise EOFError('一鍵歸戶申請失敗')
        self.common.sleep(20) # 有些第三方錢包, 歸戶速度真的慢
    
    # 一鍵歸戶
    def money_return_cp_napp(self):
        self.common.poco_click(TransformPageLocator.all_return_cp)
        if self.common.poco_exists(TransformPageLocator.all_return_cp) is False:
            pass
        else:
            raise EOFError('一鍵歸戶申請失敗')
        self.common.sleep(20) # 有些第三方錢包, 歸戶速度真的慢

    # 一鍵歸戶並比對
    def money_return_cp_compare(self, wallets):
        # 載入頁面時, 第三方錢包顯示的速度比較慢, 如果直接執行有可能跳錯, 拿AG當等待標的
        if self.common.poco_wait_exists(TransformPageLocator.ag) is False:
            raise EOFError('進入額度轉換錯誤')
        
        total_amount = 0
        all_wallet = wallets
        all_wallet.insert(0,'主钱包')
        self.refresh_all()
        amount_before = self.get_wallet_amount(all_wallet)
        before_cp_amount = int(amount_before['主钱包'])

        for wallet in all_wallet:
            if self.common.poco_exists(TransformPageLocator.maintenance(wallet)):
                continue
            total_amount = total_amount + int(amount_before[wallet])

        self.money_return_cp()
        
        # 確認一鍵歸戶前後 錢包金額正確
        for loop in range(0, 6):
            self.refresh_all()
            amount_after = self.get_wallet_amount(['主钱包'])
            after_cp_amount = int(amount_after['主钱包'])
            
            if total_amount == after_cp_amount:
                break
            
            if loop == 5:
                raise EOFError(f'一鍵歸戶金額錯誤, 刷新次數:{loop}, 主钱包轉換前:{before_cp_amount} 後:{after_cp_amount} 應為:{total_amount}')

            self.common.sleep(5)

    # 一鍵歸戶並比對
    def money_return_cp_compare_napp(self, wallets):
        # 載入頁面時, 第三方錢包顯示的速度比較慢, 如果直接執行有可能跳錯, 拿AG當等待標的
        if self.common.poco_wait_exists(TransformPageLocator.ag) is False:
            raise EOFError('進入額度轉換錯誤')
        
        total_amount = 0
        all_wallet = wallets
        all_wallet.insert(0,'主钱包')
        self.refresh_all_napp()
        self.common.poco_click(TransformPageLocator.expand_wallet)
        amount_before = self.get_wallet_amount_napp(all_wallet)
        before_cp_amount = int(amount_before['主钱包'])

        for wallet in all_wallet:
            if self.common.poco_get_text(TransformPageLocator.wallet_info_napp(wallet)) == '维护中':
                continue
            total_amount = total_amount + int(amount_before[wallet])

        self.money_return_cp_napp()
        
        # 確認一鍵歸戶前後 錢包金額正確
        for loop in range(0, 7):        # 有些錢包回來比較慢，總時長拉到約1分鐘
            self.refresh_all_napp()
            self.common.poco_click(TransformPageLocator.expand_wallet)
            amount_after = self.get_wallet_amount_napp(['主钱包'])
            after_cp_amount = int(amount_after['主钱包'])
            
            if total_amount == after_cp_amount:
                break
            
            if loop == 6:
                raise EOFError(f'一鍵歸戶金額錯誤, 刷新次數:{loop}, 主钱包轉換前:{before_cp_amount} 後:{after_cp_amount} 應為:{total_amount}')

            self.common.sleep(5)