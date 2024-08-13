from selenium.webdriver.common.by import By
from Project.sbk.web.pages.admin.admin_basepage import BasePage

class MainPageLocator:
    # ADMIN MAIN PAGE (導航欄)
	menu_member_list = (By.XPATH, "//a[text()='会员列表']")     # 會員列表

	menu_groups = (By.XPATH, "//span[text()='群组管理']")    	# 群組管理
	menu_groups_list = (By.XPATH, "//a[text()=' 群组列表']") 	# 群組管理 - 群組列表
	menu_groups_set = (By.XPATH, "//a[text()=' 群组设定']")  	# 群組管理 - 群組設定
	menu_groups_own = (By.XPATH, "//a[text()=' 群组建立成员']")  # 群組管理 - 群組建立成員

	menu_systum = (By.XPATH, "//span[text()='系统管理']")           # 系統管理
	menu_systum_maintenance = (By.XPATH, "//a[text()=' APP维护']") # 系統管理 - APP 維護
	menu_systum_app_setting = (By.XPATH, "//a[text()=' APP设定']") # 系統管理 - APP 設定

	menu_recode = (By.XPATH, "//a[text()='聊天纪录']")             # 聊天記錄

	menu_setting = (By.XPATH, "//span[text()='设置']")                # 設置
	menu_setting_account = (By.XPATH, "//a[text()=' 帐号管理']")       # 設置 - 帳號管理
	menu_setting_role = (By.XPATH, "//a[text()=' 角色权限']")          # 設置 - 角色權限
	menu_setting_otp = (By.XPATH, "//a[text()=' OTP管理']")           # 設置 - OTP 管理
	menu_setting_otp_operation = (By.XPATH, "//a[text()=' 运营OTP']") # 設置 - 運營 OTP

	menu_logging = (By.XPATH, "//a[text()='操作日志']")          # 操作日誌

	menu_red = (By.XPATH, "//span[text()='紅包管理']")           # 紅包管理
	menu_red_list = (By.XPATH, "//a[text()=' 紅包列表']")        # 紅包管理 - 紅包列表
	menu_red_integral = (By.XPATH, "//a[text()=' 积分使用纪录']") # 紅包管理 - 積分使用紀錄
	menu_red_water = (By.XPATH, "//a[text()=' 水量控制']")        # 紅包管理 - 水量控制

	page_title = (By.XPATH, "//span[@class='title']")
	user_icon = (By.XPATH, "//*[@class='svg-icon user-avatar']")
	change_time_icon = (By.XPATH, "(//*[contains(text(),'变更时区')])[2]")
	user_time_7 = (By.XPATH, "//p[contains(text(),'UTC+07:00')]")
	user_time_8 = (By.XPATH, "//p[contains(text(),'UTC+08:00')]")
	time_dropdown = (By.XPATH, "//input[@placeholder='请选择']")
	time_dropdown_07 = (By.XPATH, "//span[text()='UTC+07:00']")
	time_dropdown_08 = (By.XPATH, "//span[text()='UTC+08:00']")
	time_dropdown_12 = (By.XPATH, "//span[text()='UTC+12:00']")
	time_dropdown_closs = (By.XPATH, "//span[text()='关闭']")
	time_dropdown_list = (By.XPATH, "//span")
    # 切換語言
	switch_languages_btn_en = (By.XPATH, "//span[text()='Switch Languages']")
	switch_languages_btn_cn = (By.XPATH, "//span[text()='切换语言']")
	switch_languages_dropdown_cn = (By.XPATH, "//li[text()=' 中文 ']")
	switch_languages_dropdown_en = (By.XPATH, "//li[text()=' English ']")
	# 變更密碼
	switch_change_password_btn_cn = (By.XPATH, "(//*[contains(text(),'变更密码')])[2]")
	original_password_field_cn = (By.XPATH, "(//input[@type='password'])[1]")
	new_password_btn_cn = (By.XPATH, "(//input[@type='password'])[2]")
	again_password_btn_cn = (By.XPATH, "(//input[@type='password'])[3]")
	switch_change_password_confirm_btn_cn = (By.XPATH, "//span[text()='确定']")
	change_successfully = (By.XPATH, "//p[@class='el-message__content']")
	aaaaa = (By.XPATH, "//p[@class='el-message__content']")
	
	# partner/player
	partner_btn = (By.XPATH, "//*[@class='svg-inline--fa fa-people-group fa-solid fa-people-group sub-el-icon']")
	partner_player_btn = (By.XPATH,"//span[text()='商户与玩家管理']")
	partner_UID = (By.XPATH, "//tbody/tr[20]/td[2]/div")
	partner_UID_1 = (By.XPATH, "//tbody/tr[1]/td[2]/div")
	partner_name = (By.XPATH, "//tbody/tr[20]/td[3]/div")
	currency = (By.XPATH, "//tbody/tr[20]/td[4]/div")
	time_zone = (By.XPATH, "//tbody/tr[20]/td[5]/div")
	languages = (By.XPATH, "//tbody/tr[20]/td[6]/div")
	partner_status = (By.XPATH, "//tbody/tr[20]/td[8]/div")
	details_btn = (By.XPATH, "//tbody/tr[20]/td[9]/div/button[1]")
	player_btn = (By.XPATH, "//tbody/tr[20]/td[9]/div/button[2]")
	keywords_input = (By.XPATH, "//input[@class='el-input__inner']")
	partner_search = (By.XPATH, "//*[@class='el-icon-search']")
	partner_new_btn = (By.XPATH, "//span[text()='新增']") #商戶新增btn
	partner_edit_lightmode_btn = (By.XPATH, "//span[text()='白天版']")
	partner_edit_darkmode_btn = (By.XPATH, "//span[text()='夜晚版']")
	partner_edit_btn = (By.XPATH, "//span[text()=' 编辑 ']") #商戶編輯btn
	partner_save_btn = (By.XPATH, "(//button[@class='el-button el-button--primary el-button--mini'])[3]/span") #儲存按鈕
	partner_default_layout = (By.XPATH, "(//*[@class='el-input__inner'])[3]") #預設版型
	partner_name_content = (By.XPATH, "(//*[@class='el-form-item__content'])[2]") #商戶名稱
	partner_name_input = (By.XPATH, "((//input[@class='el-input__inner'])[1])") #商戶名稱寫入欄位
	partner_language_content = (By.XPATH, "(//*[@class='el-form-item__content'])[7]") #使用語系內容
	partner_language = (By.XPATH, "(//*[@class='el-input__inner'])[2]") #預設版型
	partner_edit_cn_btn = (By.XPATH, "//span[text()='zh-CN']") #下拉選單-簡中
	partner_edit_us_btn = (By.XPATH, "//span[text()='en-US']") #下拉選單-英文
	partner_default_layout_content = (By.XPATH, "(//*[@class='el-form-item__content'])[8]") #預設版型內容
	partner_contact_person_content = (By.XPATH, "(//*[@class='el-form-item__content'])[9]") #聯絡人內容
	partner_contact_person_input = (By.XPATH, "((//input[@class='el-input__inner'])[4])") #寫入聯絡人
	partner_system_service_fee_content = (By.XPATH, "(//*[@class='el-form-item__content'])[10]") #系統服務費
	partner_time_zone_content = (By.XPATH, "(//*[@class='el-form-item__content'])[14]") #商戶時區
	partner_time_zone_input = (By.XPATH, "((//input[@class='el-input__inner'])[8])") #更換商戶時區
	partner_time_zone_utc_8 = (By.XPATH, "(//span[text()='UTC+08:00'])[2]") #更換商戶時區到utc+8
	partner_time_zone_utc_9 = (By.XPATH, "(//span[text()='UTC+09:00'])[2]") #更換商戶時區到utc+9
	partner_time_zone_utc_12 = (By.XPATH, "(//span[text()='UTC+12:00'])[2]") #更換商戶時區到utc+9
	partner_status_content = (By.XPATH, "(//*[@class='el-form-item__content'])[15]") #商戶狀態
	partner_status_enable_btn = (By.XPATH, "(//*[@class='el-radio__inner'])[2]") #商戶開關啟用
	partner_status_disable_btn = (By.XPATH, "(//*[@class='el-radio__inner'])[3]") #商戶開關停用
	partner_contract_period_content = (By.XPATH, "(//*[@class='el-form-item__content'])[16]") #商戶合約期間
	partner_email_content = (By.XPATH, "(//*[@class='el-form-item__content'])[17]") #Email

	player_partnerUID = (By.XPATH, "(//div[@class='el-form-item__content'])[1]") #玩家商戶UID
	player_currency = (By.XPATH, "(//div[@class='el-form-item__content'])[2]") #玩家幣別
	player_language = (By.XPATH, "(//div[@class='el-form-item__content'])[3]") #玩家語系
	player_partner_name = (By.XPATH, "(//div[@class='el-form-item__content'])[4]") #玩家商戶名稱
	player_time_zones = (By.XPATH, "(//div[@class='el-form-item__content'])[5]") #玩家時區
	player_partner_status = (By.XPATH, "(//div[@class='el-form-item__content'])[6]") #玩家商戶狀態
	special_annotation_warning_tag = (By.XPATH, "//*[@class='el-tag el-tag--danger el-tag--light'][text()='警']") #商戶與玩家管理-警示tag
	special_annotation_abnormal_tag = (By.XPATH, "//*[@class='el-tag el-tag--danger el-tag--light'][text()='异']") #商戶與玩家管理-異常tag
	special_annotation_warning_checkbox = (By.XPATH, "(//*[@class='el-checkbox__inner'])[1]") #商戶與玩家管理-警示checkbox
	special_annotation_abnormal_checkbox = (By.XPATH, "(//*[@class='el-checkbox__inner'])[2]") #商戶與玩家管理-異常checkbox
	special_not_activated_checkbox = (By.XPATH, "(//*[@class='el-checkbox__inner'])[3]") #商戶與玩家管理-玩家未啟用checkbox
	special_enable_checkbox = (By.XPATH, "(//*[@class='el-checkbox__inner'])[4]") #商戶與玩家管理-玩家啟用checkbox
	special_blacklist_checkbox = (By.XPATH, "(//*[@class='el-checkbox__inner'])[6]") #商戶與玩家管理-玩家黑名單checkbox
	player_search = (By.XPATH, "//*[@class='el-icon-search']") #商戶與玩家管理-玩家搜尋btn
	playerlist_status = (By.XPATH, "//*[@class='el-table_1_column_10 is-center  ']//span") #商戶與玩家管理-玩家列表狀態列
	
	#transaction_log
	transaction_log_btn = (By.XPATH,"//span[text()='玩家钱包流水记录']") #玩家钱包流水记录btn
	transaction_log_search = (By.XPATH,"//*[@class='el-icon-search']") #玩家钱包流水记录-搜尋btn
	transaction_log_transfer_from_the_main_wallet = (By.XPATH,"(//*[@class='el-checkbox__inner'])[1]") #玩家钱包流水记录-從錢包轉入checkbox
	transaction_log_payouts = (By.XPATH,"(//*[@class='el-checkbox__inner'])[2]") #玩家钱包流水记录-派彩checkbox
	transaction_log_refunded = (By.XPATH,"(//*[@class='el-checkbox__inner'])[3]") #玩家钱包流水记录-退回本金checkbox
	transaction_log_transfers_increase = (By.XPATH,"(//*[@class='el-checkbox__inner'])[4]") #玩家钱包流水记录-調帳-增加checkbox
	transaction_log_go_back_to_your_main_wallet = (By.XPATH,"(//*[@class='el-checkbox__inner'])[5]") #玩家钱包流水记录-轉回主錢包checkbox
	transaction_log_betting = (By.XPATH,"(//*[@class='el-checkbox__inner'])[6]") #玩家钱包流水记录-投注checkbox
	transaction_log_recycle_payout_Rollback = (By.XPATH,"(//*[@class='el-checkbox__inner'])[7]") #玩家钱包流水记录-回收派彩(回滾)checkbox
	transaction_log_recycle_payout_cancel = (By.XPATH,"(//*[@class='el-checkbox__inner'])[8]") #玩家钱包流水记录-回收派彩(取消)checkbox
	transaction_log_re_bet = (By.XPATH,"(//*[@class='el-checkbox__inner'])[9]") #玩家钱包流水记录-重新下注checkbox
	transaction_log_transfers_decrease = (By.XPATH,"(//*[@class='el-checkbox__inner'])[10]") #玩家钱包流水记录-掉帳-減少checkbox
	transaction_log_Olny_show_the_lastest_log_for_each_player = (By.XPATH,"(//*[@class='el-checkbox__inner'])[11]") #玩家钱包流水记录-只顯示每位玩家新一次交易紀錄checkbox
	transaction_log_partner_dropdown = (By.XPATH,"(//input[@class='el-input__inner'])[2]") #玩家钱包流水记录-商戶下拉選單
	transaction_log_transaction_type = (By.XPATH,"(//td[@class='el-table_1_column_5  '])[1]//span[2]") #玩家钱包流水记录-交易類型欄位

	#wallet_adjust
	wallet_adjust_btn = (By.XPATH,"//span[text()='调帐申请与审核']") #调帐申请与审核btn
	wallet_adjust_transaction_number_input = (By.XPATH,"(//input[@class='el-input__inner'])[1]") #調帳申請與審核_搜尋_調帳單號欄位
	wallet_adjust_partner_input = (By.XPATH,"(//input[@class='el-input__inner'])[2]") #調帳申請與審核_搜尋_商戶欄位
	wallet_adjust_partner_william_auto = (By.XPATH,"(//li[@class='el-select-dropdown__item']/span[text()='william_auto'])[3]") #調帳申請與審核_搜尋_商戶william_auto
	wallet_adjust_partner_ktest = (By.XPATH,"//li[@class='el-select-dropdown__item']/span[text()='ktest']")  #調帳申請與審核_搜尋_商戶ktest
	wallet_adjust_player = (By.XPATH,"(//div[@class='el-input el-input--mini el-input--suffix'])[2]") #調帳申請與審核_搜尋_玩家欄位
	wallet_adjust_player_input = (By.XPATH,"//div[@class='el-input el-input--mini el-input--suffix is-focus']/input") #調帳申請與審核_搜尋_玩家欄位
	wallet_adjust_player_dropdown = (By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//span[contains(text(),'regression001')]") #調帳申請與審核_搜尋_玩家_下拉選單
	wallet_adjust_applicants_input = (By.XPATH,"//div[@class='el-input el-input--mini el-input--suffix is-focus']/input") #調帳申請與審核_搜尋_操作人員欄位

	wallet_adjust_partner = (By.XPATH,"//*[@class='el-table_1_column_2 is-center ']//div") #調帳申請與審核_列表_商戶
	wallet_adjust_player_list = (By.XPATH,"//td[@class='el-table_1_column_3 is-center ']//span")
	wallet_adjust_transaction_number = (By.XPATH,"(//td[@class='el-table_1_column_1 is-center '])[1]//span") #調帳申請與審核_列表_調帳單號欄位
	wallet_adjust_new_btn = (By.XPATH,"//i[@class='el-icon-plus']") #調帳新增btn
	wallet_adjust_new_partner = (By.XPATH,"(//input[@class='el-input__inner'])[10]") #新增商戶欄位
	wallet_adjust_new_partner_list_24 = (By.XPATH,"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[10]/li[24]") #新增頁商戶下拉選單選最後一個
	wallet_adjust_new_partner_list_20 = (By.XPATH,"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[10]/li[20]") #新增頁商戶下拉選單選第20個
	wallet_adjust_new_player_dropdown = (By.XPATH, "(//i[@class='el-select__caret el-input__icon el-icon-arrow-up'])[9]") #新增玩家欄位下拉選單
	wallet_adjust_new_player_input = (By.XPATH, "//div[@class='el-input el-input--mini el-input--suffix is-focus']/input") #新增玩家欄位
	wallet_adjust_new_transfer_amount = (By.XPATH, "(//i[@class='el-select__caret el-input__icon el-icon-arrow-up'])[10]") #調帳增加/減少欄位
	wallet_adjust_new_transfer_amount_transfers_increase = (By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[10]/li[1]/span") #調帳增加
	wallet_adjust_new_transfer_amount_transfers_decrease = (By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[10]/li[2]/span") #調帳減少
	wallet_adjust_new_transfer_amount_input = (By.XPATH, "(//div[@class='el-input el-input--mini'])[2]/input")  #調帳金額欄位
	wallet_adjust_new_related_tracking_number_input = (By.XPATH, "(//div[@class='el-input el-input--mini'])[3]/input")
	wallet_adjust_new_cause_input = (By.XPATH, "//*[@class='el-textarea__inner']") #新增的原因欄位
	wallet_adjust_new_save_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small']/span") #保存
	wallet_adjust_new_close_btn = (By.XPATH, "//button[@class='el-button el-button--default el-button--small']/span") #取消
	wallet_adjust_new_dropdown_list = (By.XPATH, "//span[text()='regression001']") #下拉選單regression001
	wallet_adjust_new_confirmed_amount = (By.XPATH, "(//td[@class='el-table_1_column_4 is-center '])[1]//span") #確認金額
	wallet_adjust_list_void_btn = (By.XPATH, "(//button[@class='el-button el-button--danger el-button--mini el-popover__reference'])[1]") #作廢按鈕
	wallet_adjust_list_view_btn = (By.XPATH, "(//button[@class='el-button el-button--primary el-button--mini']/span[text()='检视'])[1]") #檢視按鈕
	wallet_adjust_list_submit_for_view_btn = (By.XPATH, "(//button[@class='el-button el-button--primary el-button--mini el-popover__reference'])[1]") #提交送審按鈕
	wallet_adjust_list_porgress = (By.XPATH, "(//td[@class='el-table_1_column_7 is-center ']/div)") #進度欄位
	wallet_adjust_list_view_details = (By.XPATH, "(//span[@class='el-dialog__title'])[3]") #檢視頁明細名稱
	wallet_adjust_list_view_edit_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small']") #檢視頁編輯按鈕/保存按鈕
	wallet_adjust_view_transfer_amount = (By.XPATH, "(//i[@class='el-select__caret el-input__icon el-icon-arrow-up'])[8]") #調帳增加/減少欄位
	wallet_adjust_view_transfer_amount_transfers_increase = (By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[8]/li[1]") #檢視編輯的調帳增加
	wallet_adjust_view_transfer_amount_transfers_decrease = (By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[8]/li[2]") #檢視編輯的調帳減少
	wallet_adjust_title = (By.XPATH, "(//span[@class='no-redirect'])[2]") #麵包屑標題
	wallet_adjust_void_confirm = (By.XPATH, "//*[contains(text(),'确认')]") #浮窗再次確認(確定)

	wallet_adjust_progress_applying_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[1]") #調帳申請與審核_搜尋_進度_申請中
	wallet_adjust_progress_submit_review_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[2]") #調帳申請與審核_搜尋_進度_提交審核
	wallet_adjust_progress_void_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[3]") #調帳申請與審核_搜尋_進度_作廢
	wallet_adjust_progress_audit_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[4]") #調帳申請與審核_搜尋_進度_審核中
	wallet_adjust_progress_approved_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[5]") #調帳申請與審核_搜尋_進度_審核通過
	wallet_adjust_progress_reject_checkbox = (By.XPATH, "(//span[@class='el-checkbox__inner'])[6]") #調帳申請與審核_搜尋_進度_審核駁回





	



	
	
	

	







class MainPage(BasePage):

	def switch_languages(self): #切換語系
		self.wait_loading_finish()
		if  self.is_element_finded(MainPageLocator.switch_languages_btn_en) == True: #英文語系
			self.click(MainPageLocator.switch_languages_btn_en)
			self.click(MainPageLocator.switch_languages_dropdown_cn)
			assert self.get_text(MainPageLocator.page_title) == '仪表板', f"切換語系失敗"
		elif self.is_element_finded(MainPageLocator.switch_languages_btn_cn) == True: #中文語系
			self.click(MainPageLocator.switch_languages_btn_cn)
			self.click(MainPageLocator.switch_languages_dropdown_en)
			assert self.get_text(MainPageLocator.page_title) == 'Dashboard', f"切換語系失敗"
			self.click(MainPageLocator.switch_languages_btn_en)
			self.click(MainPageLocator.switch_languages_dropdown_cn)
	    
	def change_time(self): #切換時區
		self.wait_loading_finish()
		if  self.is_element_finded(MainPageLocator.user_time_8) == True: #判斷是否為utc+8
			self.click(MainPageLocator.user_icon)  #打開使用者設置
			self.click(MainPageLocator.change_time_icon) #打開更換時區
			self.click(MainPageLocator.time_dropdown) #打開時區列表
			self.click(MainPageLocator.time_dropdown_07) #點擊UTC+7
			self.click(MainPageLocator.time_dropdown_closs) #關閉時區列表
			self.wait_loading_finish()
			assert self.is_element_finded(MainPageLocator.user_time_7) == True, f"時區切換失敗"
		else:
			self.click(MainPageLocator.user_icon)
			self.sleep(0.5)
			self.click(MainPageLocator.change_time_icon)
			self.click(MainPageLocator.time_dropdown)
			self.sleep(0.5)
			self.scroll_to_element(MainPageLocator.time_dropdown_12)
			self.sleep(0.5)
			self.click(MainPageLocator.time_dropdown_08)
			self.click(MainPageLocator.time_dropdown_closs)
			self.wait_loading_finish()
			assert self.is_element_finded(MainPageLocator.user_time_8) == True, f"時區切換失敗"

	def change_password(self): #更換密碼
		self.wait_loading_finish()
		self.click(MainPageLocator.user_icon)
		self.sleep(0.5)
		self.click(MainPageLocator.switch_change_password_btn_cn)
		self.type(MainPageLocator.original_password_field_cn, '123456')
		self.type(MainPageLocator.new_password_btn_cn, '234567')
		self.type(MainPageLocator.again_password_btn_cn, '234567')
		self.click(MainPageLocator.switch_change_password_confirm_btn_cn)
		self.wait_visibility(MainPageLocator.change_successfully)
		assert self.get_text(MainPageLocator.change_successfully) == '变更成功', f"密碼有誤"
		self.wait_loading_finish()
		self.click(MainPageLocator.user_icon)
		self.sleep(0.5)
		self.click(MainPageLocator.switch_change_password_btn_cn)
		self.type(MainPageLocator.original_password_field_cn, '234567')
		self.type(MainPageLocator.new_password_btn_cn, '123456')
		self.type(MainPageLocator.again_password_btn_cn, '123456')
		self.click(MainPageLocator.switch_change_password_confirm_btn_cn)
		self.wait_visibility(MainPageLocator.change_successfully)
		assert self.get_text(MainPageLocator.change_successfully) == '变更成功', f"密碼有誤"
		
	def partner_and_player_list(self): #檢查商戶與玩家管理
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn)
		self.click(MainPageLocator.partner_player_btn)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_UID) == 'william_auto', f"商戶UID有誤"
		assert self.get_text(MainPageLocator.partner_name) == 'william_auto', f"商戶名稱有誤"
		assert self.get_text(MainPageLocator.currency) == 'RMB', f"幣別有誤"
		assert self.get_text(MainPageLocator.time_zone) == 'UTC+08:00', f"時區有誤"
		assert self.get_text(MainPageLocator.languages) == '简中', f"語系有誤"
		assert self.get_text(MainPageLocator.partner_status) == '启用', f"狀態有誤"
		assert self.get_text(MainPageLocator.details_btn) == '明细', f"明细btn有誤"
		assert self.get_text(MainPageLocator.player_btn) == '玩家', f"玩家btn有誤"
	
	def partner_and_player_keywords_search(self): #商戶與玩家管理關鍵字搜尋
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn)
		self.click(MainPageLocator.partner_player_btn)
		self.type(MainPageLocator.keywords_input,'william_auto')
		self.click(MainPageLocator.partner_search)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_UID_1) == 'william_auto', f"搜尋結果有誤"

	def partner_and_player_partner_new_btn(self): #商戶與玩家管理新增按鈕
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn)
		self.click(MainPageLocator.partner_player_btn)
		self.click(MainPageLocator.partner_new_btn)
		self.wait_loading_finish()
		print(self.get_text(MainPageLocator.partner_save_btn))
		assert self.get_text(MainPageLocator.partner_save_btn) == '保存', f"進入新增頁面失敗"

	def partner_and_player_partner_edit(self): #商戶與玩家管理編輯
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.partner_player_btn) #商戶與玩家管理
		self.click(MainPageLocator.details_btn) #明細按鈕
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_default_layout) #點預設版型
		self.click(MainPageLocator.partner_edit_darkmode_btn) #切換成夜晚版
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_default_layout_content) == "夜晚版" ,f"切換預設版型失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_default_layout) #點預設版型
		self.click(MainPageLocator.partner_edit_lightmode_btn) #切換成白天版
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()

		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.type(MainPageLocator.partner_name_input, 'william_auto1') #點商戶名稱
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_name_content) == "william_auto1" ,f"編輯商戶名稱失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.type(MainPageLocator.partner_name_input, 'william_auto') #點商戶名稱
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_language) #點預設版型
		self.click(MainPageLocator.partner_edit_us_btn) #切換成英文
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_language_content) == "en-US" ,f"切換語系失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_language) #點使用語系
		self.click(MainPageLocator.partner_edit_cn_btn) #切換成簡中
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.type(MainPageLocator.partner_contact_person_input, '測試人員1') #寫入聯絡人
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_contact_person_content) == "測試人員1" ,f"編輯聯絡人失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.type(MainPageLocator.partner_contact_person_input, '測試人員') #寫入聯絡人
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_time_zone_input)  #點時區下拉選單
		self.wait_loading_finish()
		self.scroll_to_element(MainPageLocator.partner_time_zone_utc_12) #下滑到最下方
		self.click(MainPageLocator.partner_time_zone_utc_9) #切換utc+9
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_time_zone_content) == "UTC+09:00" ,f"切換時區失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_time_zone_input) #點時區下拉選單
		self.click(MainPageLocator.partner_time_zone_utc_8) #切換utc+8
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_status_disable_btn)  #點商戶停用
		self.click(MainPageLocator.partner_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.partner_status_content) == "停用" ,f"切換狀態失敗"
		self.click(MainPageLocator.partner_edit_btn) #編輯按鈕
		self.click(MainPageLocator.partner_status_enable_btn)  #點商戶啟用
		self.click(MainPageLocator.partner_save_btn) #保存

	def partner_and_player_player(self): #商戶與玩家管理作業_玩家列表
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.partner_player_btn) #商戶與玩家管理
		self.click(MainPageLocator.player_btn) #商戶與玩家管理-玩家按鈕
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.player_partnerUID) == 'william_auto', f"商戶UID有誤"
		assert self.get_text(MainPageLocator.player_currency) == 'RMB', f"商戶幣別有誤"
		assert self.get_text(MainPageLocator.player_language) == '简中', f"商戶語系有誤"
		assert self.get_text(MainPageLocator.player_partner_name) == 'william_auto', f"商戶名稱有誤"
		assert self.get_text(MainPageLocator.player_time_zones) == 'UTC+08:00', f"商戶時區有誤"
		assert self.get_text(MainPageLocator.player_partner_status) == '启用', f"商戶狀態有誤"

	def partner_and_player_player_search(self): #商戶與玩家管理作業_玩家列表搜尋
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.partner_player_btn) #商戶與玩家管理
		self.click(MainPageLocator.player_btn) #商戶與玩家管理-玩家按鈕
		self.click(MainPageLocator.special_annotation_warning_checkbox) #商戶與玩家管理-警示checkbox
		self.click(MainPageLocator.player_search)
		assert self.get_text(MainPageLocator.special_annotation_warning_tag) == '警', f'查詢特殊注記(警示)錯誤'
		self.click(MainPageLocator.special_annotation_warning_checkbox) #商戶與玩家管理-警示checkbox
		self.click(MainPageLocator.special_annotation_abnormal_checkbox) #商戶與玩家管理-異常checkbox
		self.click(MainPageLocator.player_search) #搜尋
		assert self.get_text(MainPageLocator.special_annotation_abnormal_tag) == '异', f'查詢特殊注記(異常)錯誤'
		self.refresh_browser()
		self.click(MainPageLocator.special_not_activated_checkbox) #商戶與玩家管理-未啟用checkbox
		self.click(MainPageLocator.player_search) #搜尋
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.playerlist_status) == '未启用(未转帐)', f'查詢未启用錯誤'

	def partner_and_player_player_edit(self): #商戶與玩家管理作業_玩家列表編輯
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.partner_player_btn) #商戶與玩家管理
		self.click(MainPageLocator.player_btn) #商戶與玩家管理-玩家按鈕

	def transaction_log(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.transaction_log_btn) #玩家錢包流水紀錄
		self.click(MainPageLocator.transaction_log_payouts) #玩家钱包流水记录-派彩checkbox
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.transaction_log_transaction_type) == '派彩', f'搜尋不到派彩資料'
		self.click(MainPageLocator.transaction_log_payouts) #玩家钱包流水记录-派彩checkbox
		self.click(MainPageLocator.transaction_log_refunded) #玩家钱包流水记录-退回本金checkbox
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.transaction_log_transaction_type) == '退回本金', f'搜尋不到退回本金資料'
		self.click(MainPageLocator.transaction_log_refunded) #玩家钱包流水记录-退回本金checkbox
		self.click(MainPageLocator.transaction_log_transfers_increase) #玩家钱包流水记录-調帳-增加checkbox
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.transaction_log_transaction_type) == '调帐(增)', f'搜尋不到調帳-增加資料'
		self.click(MainPageLocator.transaction_log_transfers_increase) #玩家钱包流水记录-調帳-增加checkbox
		self.click(MainPageLocator.transaction_log_betting) #玩家钱包流水记录-投注checkbox
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.transaction_log_transaction_type) == '投注', f'搜尋不到投注資料'
		self.click(MainPageLocator.transaction_log_betting) #玩家钱包流水记录-投注checkbox
		self.click(MainPageLocator.transaction_log_recycle_payout_Rollback) #玩家钱包流水记录-回收派彩(回滾)checkbox
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.transaction_log_transaction_type) == '回收派彩(回滾)', f'搜尋不到回收派彩(回滾)資料'

	def wallet_adjust_transaction_number(self): #調帳申請與審核_搜尋_調帳單號
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.type(MainPageLocator.wallet_adjust_transaction_number_input, 'AD-1694248748760174592') #調帳單號欄位
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.wallet_adjust_transaction_number) == 'AD-1694248748760174592', f'搜尋不到單號'

	def wallet_adjust_partner(self): #調帳申請與審核_搜尋_調帳單號
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn	
		self.click(MainPageLocator.wallet_adjust_partner_input) #點開商戶下拉選單
		self.wait_loading_finish()
		self.scroll_to_element(MainPageLocator.wallet_adjust_partner_ktest) #下滑到ktest
		self.click(MainPageLocator.wallet_adjust_partner_william_auto) #選william_auto
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.wallet_adjust_partner) == 'william_auto', f'搜尋不到商戶'
	
	def wallet_adjust_player(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_partner_input) #點開商戶下拉選單
		self.wait_loading_finish()
		self.scroll_to_element(MainPageLocator.wallet_adjust_partner_ktest) #下滑到ktest
		self.click(MainPageLocator.wallet_adjust_partner_william_auto) #選william_auto
		# self.wait_loading_finish()
		self.click(MainPageLocator.wallet_adjust_player)
		self.type(MainPageLocator.wallet_adjust_player_input,'re')
		self.click(MainPageLocator.wallet_adjust_player_dropdown) 
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		player_list = self.find_elements(MainPageLocator.wallet_adjust_player_list)
		print(player_list[1].text)
		assert player_list[1].text and player_list[-1].text == '[Default] regression001', f'搜尋不到玩家'


	def wallet_adjust_newly_added_increase(self): #調帳申請與審核_新增_調帳增加
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_new_btn) #打開新增
		self.click(MainPageLocator.wallet_adjust_new_partner) #打開商戶下拉選單
		self.scroll_to_element(MainPageLocator.wallet_adjust_new_partner_list_24) #下滑到底部
		self.click(MainPageLocator.wallet_adjust_new_partner_list_20) #選擇william_auto
		self.click(MainPageLocator.wallet_adjust_new_player_dropdown) #打開輸入玩家帳號
		self.type(MainPageLocator.wallet_adjust_new_player_input, 're') #輸入玩家帳號regression001
		self.click(MainPageLocator.wallet_adjust_new_dropdown_list) #點下拉選單名稱
		self.type(MainPageLocator.wallet_adjust_new_transfer_amount_input,'77') #輸入調帳金額
		self.type(MainPageLocator.wallet_adjust_new_related_tracking_number_input, 'test-123456789') #相關單號
		self.type(MainPageLocator.wallet_adjust_new_cause_input, '測試調帳增加！') #原因
		self.click(MainPageLocator.wallet_adjust_new_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.wallet_adjust_new_confirmed_amount) == 'RMB 77', f'新增調帳-增加失敗'

	def wallet_adjust_newly_added_decrease(self): #調帳申請與審核_新增_調帳減少
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_new_btn) #打開新增
		self.click(MainPageLocator.wallet_adjust_new_partner) #打開商戶下拉選單
		self.scroll_to_element(MainPageLocator.wallet_adjust_new_partner_list_24) #下滑到底部
		self.click(MainPageLocator.wallet_adjust_new_partner_list_20) #選擇william_auto
		self.click(MainPageLocator.wallet_adjust_new_player_dropdown) #打開輸入玩家帳號
		self.type(MainPageLocator.wallet_adjust_new_player_input, 're') #輸入玩家帳號regression001
		self.click(MainPageLocator.wallet_adjust_new_dropdown_list) #點下拉選單名稱
		self.wait_loading_finish()
		self.click(MainPageLocator.wallet_adjust_new_transfer_amount) #點調帳增加/減少欄位
		self.click(MainPageLocator.wallet_adjust_new_transfer_amount_transfers_decrease) #選調帳-減少
		self.type(MainPageLocator.wallet_adjust_new_transfer_amount_input,'88') #輸入調帳金額
		self.type(MainPageLocator.wallet_adjust_new_related_tracking_number_input, 'test-123456789') #相關單號
		self.type(MainPageLocator.wallet_adjust_new_cause_input, '測試調帳減少！') #原因
		self.click(MainPageLocator.wallet_adjust_new_save_btn) #保存
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.wallet_adjust_new_confirmed_amount) == 'RMB -88', f'新增調帳-減少失敗'

	def wallet_adjust_view_edit(self): #調帳申請與審核_檢視_編輯
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		if self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '申请中':
			self.click(MainPageLocator.wallet_adjust_list_view_btn) #檢視按鈕
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_list_view_details) == '明细', '編輯頁面名稱錯誤'
			self.click(MainPageLocator.wallet_adjust_list_view_edit_btn) #編輯
			self.click(MainPageLocator.wallet_adjust_view_transfer_amount) #點調帳增加/減少欄位
			self.click(MainPageLocator.wallet_adjust_view_transfer_amount_transfers_decrease) #選調帳-減少
			self.type(MainPageLocator.wallet_adjust_new_cause_input, '測試調帳減少！(更改金額)') #原因
			self.type(MainPageLocator.wallet_adjust_new_transfer_amount_input,'99') #輸入調帳金額
			self.wait_loading_finish()
			self.click(MainPageLocator.wallet_adjust_list_view_edit_btn)
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_new_confirmed_amount) == 'RMB -99', f'更改調帳-減少失敗'
		else:
			self.wallet_adjust_newly_added_increase()
			self.click(MainPageLocator.wallet_adjust_list_view_btn) #檢視按鈕
			assert self.get_text(MainPageLocator.wallet_adjust_list_view_details) == '明细', '編輯頁面名稱錯誤'
			self.click(MainPageLocator.wallet_adjust_list_view_edit_btn) #編輯
			self.click(MainPageLocator.wallet_adjust_view_transfer_amount) #點調帳增加/減少欄位
			self.click(MainPageLocator.wallet_adjust_view_transfer_amount_transfers_decrease) #選調帳-減少
			self.type(MainPageLocator.wallet_adjust_new_cause_input, '測試調帳減少！(更改金額)') #原因
			self.type(MainPageLocator.wallet_adjust_new_transfer_amount_input,'99') #輸入調帳金額
			self.wait_loading_finish()
			self.click(MainPageLocator.wallet_adjust_list_view_edit_btn) #檢視編輯的調帳減少
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_new_confirmed_amount) == 'RMB -99', f'更改調帳-減少失敗'

	def wallet_adjust_view_void(self): #調帳申請與審核_作廢
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		if self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '申请中':
			self.click(MainPageLocator.wallet_adjust_list_void_btn) #點作廢
			self.wait_loading_finish()
			void_btn_list = self.find_elements(MainPageLocator.wallet_adjust_void_confirm) #作廢再次確認(確定)
			void_btn_list[-1].click()
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '作废', '作廢失敗'
		else:
			self.wallet_adjust_newly_added_increase() 
			self.click(MainPageLocator.wallet_adjust_list_void_btn) #點作廢
			self.wait_loading_finish()
			void_btn_list = self.find_elements(MainPageLocator.wallet_adjust_void_confirm) #作廢再次確認(確定)
			void_btn_list[-1].click()
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '作废', '作廢失敗'

	def wallet_adjust_submit_for_view(self): #調帳申請與審核_提交申請
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		if self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '申请中':
			self.click(MainPageLocator.wallet_adjust_list_submit_for_view_btn) #點提交送審
			void_btn_list = self.find_elements(MainPageLocator.wallet_adjust_void_confirm) #浮窗再次確認(確定)
			void_btn_list[-1].click()
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '提交审核', '提交审核失敗'
		else:
			self.wallet_adjust_newly_added_increase()
			self.click(MainPageLocator.wallet_adjust_list_submit_for_view_btn) #點提交送審
			void_btn_list = self.find_elements(MainPageLocator.wallet_adjust_void_confirm) #浮窗再次確認(確定)
			void_btn_list[-1].click()
			self.wait_loading_finish()
			assert self.get_text(MainPageLocator.wallet_adjust_list_porgress) == '提交审核', '提交审核失敗'

	def wallet_adjust_progress_applying(self): #調帳申請與審核_搜尋_進度_申請中
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_applying_checkbox) #勾選調帳申請與審核_搜尋_進度_申請中
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '申请中', '搜尋申請中失敗'

	def wallet_adjust_progress_submit_review(self): #調帳申請與審核_搜尋_進度_提交審核
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_submit_review_checkbox) #勾選調帳申請與審核_搜尋_進度_提交審核
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '提交审核', '搜尋提交审核失敗'

	def wallet_adjust_progress_void(self): #調帳申請與審核_搜尋_進度_作廢
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_void_checkbox) #勾選調帳申請與審核_搜尋_進度_作廢
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '作废', '搜尋作废失敗'

	def wallet_adjust_progress_audit(self): #調帳申請與審核_搜尋_進度_審核中
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_audit_checkbox) #勾選調帳申請與審核_搜尋_進度_審核中
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '审核中', '搜尋審核中失敗'

	def wallet_adjust_progress_approved(self): #調帳申請與審核_搜尋_進度_審核通過
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_approved_checkbox) #勾選調帳申請與審核_搜尋_進度_審核通過
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '审核通过', '搜尋審核通過失敗'

	def wallet_adjust_progress_reject(self): #調帳申請與審核_搜尋_進度_審核駁回
		self.wait_loading_finish()
		self.click(MainPageLocator.partner_btn) #商戶與玩家管理作業
		self.click(MainPageLocator.wallet_adjust_btn) #调帐申请与审核btn
		self.click(MainPageLocator.wallet_adjust_progress_reject_checkbox) #勾選調帳申請與審核_搜尋_進度_審核駁回
		self.click(MainPageLocator.transaction_log_search) #搜尋btn
		self.wait_loading_finish()
		progress_list = self.find_elements(MainPageLocator.wallet_adjust_list_porgress)
		assert progress_list[1].text and progress_list[-1].text == '审核驳回', '搜尋审核驳回失敗'



	
























	def into_member_list(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_member_list)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '会员列表', f"進入會員列表有誤"

	def into_groups_list(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_groups)
		self.click(MainPageLocator.menu_groups_list)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '群组列表', f"進入群組列表有誤"

	def into_groups_set(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_groups)
		self.click(MainPageLocator.menu_groups_set)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '群组设定', f"進入群組設定有誤"

	def into_groups_own(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_groups)
		self.click(MainPageLocator.menu_groups_own)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '群组建立成员', f"進入群組建立成員有誤"

	def into_systum_maintenance(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_systum)
		self.click(MainPageLocator.menu_systum_maintenance)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == 'APP维护', f"進入APP维护有誤"

	def into_systum_app_setting(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_systum)
		self.click(MainPageLocator.menu_systum_app_setting)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == 'APP设定', f"進入APP设定有誤"

	def into_menu_recode(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_recode)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '聊天纪录', f"進入聊天纪录有誤"

	def into_setting_account(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_setting)
		self.click(MainPageLocator.menu_setting_account)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '帐号管理', f"進入帳號管理有誤"

	def into_setting_role(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_setting)
		self.click(MainPageLocator.menu_setting_role)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '角色权限', f"進入角色權限有誤"

	def into_setting_otp(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_setting)
		self.click(MainPageLocator.menu_setting_otp)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == 'OTP管理', f"進入OTP管理有誤"

	def into_setting_otp_operation(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_setting)
		self.click(MainPageLocator.menu_setting_otp_operation)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '运营OTP', f"進入運營OTP有誤"

	def into_logging(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_logging)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '操作日志', f"進入操作日誌有誤"

	def into_red_list(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_red)
		self.click(MainPageLocator.menu_red_list)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '紅包列表', f"進入紅包列表有誤"

	def into_red_integral(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_red)
		self.click(MainPageLocator.menu_red_integral)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '积分使用纪录', f"進入積分使用紀錄有誤"

	def into_red_water(self):
		self.wait_loading_finish()
		self.click(MainPageLocator.menu_red)
		self.click(MainPageLocator.menu_red_water)
		self.wait_loading_finish()
		assert self.get_text(MainPageLocator.page_title) == '水量控制', f"進入水量控制有誤"
