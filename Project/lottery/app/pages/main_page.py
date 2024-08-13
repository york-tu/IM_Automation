import logging
from time import sleep
from common.app.common import Common
from Project.lottery.app.pages.base import Base
from Project.lottery.app.pages.xpath.xpath_base import Xpath_Base
from airtest.core.android import Android
import common.utils.globalvar as gl

class MainPageLocator:
    base = Xpath_Base()

    @staticmethod
    def env(env):
        env = MainPageLocator.base.check_device(
            Android = MainPageLocator.base.data_collation(type_kind='textMatches', type_name=f'{env}.*'),
            iOS = MainPageLocator.base.data_collation(type_kind='nameMatches', type_name=f'{env}.*')
        )
        
        return env

    close_pop = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='关闭'),
        iOS = base.data_collation(type_kind='name', type_name='关闭')
    )

    always_allow = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='始終允許'),
        iOS = base.data_collation(type_kind='name', type_name='始終允許')
    )

    uniformly_allow = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='一律允許'),
        iOS = base.data_collation(type_kind='name', type_name='一律允許')
    )
    
    allow_simplified = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='允许'),
        iOS = base.data_collation(type_kind='name', type_name='允许')
    )

    allow_traditional = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='允許'),
        iOS = base.data_collation(type_kind='name', type_name='允許')
    )

    card_checkbox = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='id/hidden_card_checkbox'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='id/hidden_card_checkbox')
    )

    allow_forever = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='以後都允許'),
        iOS = base.data_collation(type_kind='name', type_name='以後都允許')
    )

    update = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='立即重启'),
        iOS = base.data_collation(type_kind='name', type_name='立即重启')
    )

    update_napp = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android:id/button1'),
        iOS = base.data_collation(type_kind='name', type_name='android:id/button1')
    )

    allow_switch = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='android:id/switch_widget'),
        iOS = base.data_collation(type_kind='name', type_name='android:id/switch_widget')
    )

    continue_setup = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='繼續安裝'),
        iOS = base.data_collation(type_kind='text', type_name='繼續安裝')
    )

    continue_update = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='繼續更新'),
        iOS = base.data_collation(type_kind='text', type_name='繼續更新')
    )

    update_setup = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='安裝'),
        iOS = base.data_collation(type_kind='text', type_name='安裝')
    )

    set_up = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='设置'),
        iOS = base.data_collation(type_kind='text', type_name='设置')
    )

    setup_image = 'image/app/setup/oppo_setup.png'

    open_app_style_1 = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='打开'),
        iOS = base.data_collation(type_kind='text', type_name='打开')
    )

    open_app_style_2 = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='開啟'),
        iOS = base.data_collation(type_kind='text', type_name='開啟')
    )

    open_app_style_3 = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='打開.*'),
        iOS = base.data_collation(type_kind='textMatches', type_name='打開.*')
    )

    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='確定'),
        iOS = base.data_collation(type_kind='name', type_name='確定')
    )

    allow_camera = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*permission_allow.*')
    )

    close_login = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='inputAccount', action='parent().parent().parent()', pos=[0.5, 0.1]),
        iOS = base.data_collation(type_kind='name', type_name='inputAccount')
    )

    login = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='登入'),
        iOS = base.data_collation(type_kind='name', type_name='btnLogin', num=-2)
    )

    register = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='注册.*'),
        iOS = base.data_collation(type_kind='name', type_name='btnLogin', num=-1)
    )

    account = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='inputAccount'),
        iOS = base.data_collation(type_kind='name', type_name='inputAccount')
    )
    
    password = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='inputPassword'),
        iOS = base.data_collation(type_kind='name', type_name='inputPassword')
    )

    account_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*cuz_username_input', action='child()[0]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*cuz_username_input', action='child()[0]')
    )

    account_field = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入账号'),
        iOS = base.data_collation(type_kind='name', type_name='请输入账号')
    )
    
    password_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*cuz_password_input'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*cuz_password_input')
    )

    closs_icon = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*btn_clear'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*btn_clear')
    )

    password_field = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='请输入密码'),
        iOS = base.data_collation(type_kind='name', type_name='请输入密码')
    )

    login_button = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='登入账户'),
        iOS = base.data_collation(type_kind='name', type_name='登入账户')
    )

    login_button_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='会员登录'),
        iOS = base.data_collation(type_kind='name', type_name='会员登录')
    )

    login_napp = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*登录.*'),
        iOS = base.data_collation(type_kind='textMatches', type_name='.*登录.*')
    )

    guestview_first = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='先去逛逛'),
        iOS = base.data_collation(type_kind='name', type_name='先去逛逛')
    )

    register_button = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='注册账户'),
        iOS = base.data_collation(type_kind='name', type_name='注册账户')
    )

    skip_change_password = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='暂不修改'),
        iOS = base.data_collation(type_kind='name', type_name='暂不修改')
    )

    confirm_announcement = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='我知道了', action='parent().parent()'),
        iOS = base.data_collation(type_kind='name', type_name='我知道了')
    )

    close_announcement = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*ibClose'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*ibClose')
    )

    close_mail = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='稍后阅读'),
        iOS = base.data_collation(type_kind='text', type_name='稍后阅读')
    )

    close_popup = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='关闭'),
        iOS = base.data_collation(type_kind='text', type_name='关闭')
    )

    close_lucky_wheel = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*iv_close'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*iv_close')
    )

    member_login = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='账号登录'),
        iOS = base.data_collation(type_kind='name', type_name='账号登录')
    )

    logout = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='.*登出'),
        iOS = base.data_collation(type_kind='textMatches', type_name='.*登出')
    )

    confirm = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='确认'),
        iOS = base.data_collation(type_kind='name', type_name='确认')
    )

    error = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='登入失败.*'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='登入失败.*')
    )

    error_message = base.check_device(
        Android = base.data_collation(type_kind='textMatches', type_name='登入失败.*', action='parent().child()[2]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='登入失败.*', action='parent().child()[2]')
    )

    error_message_napp = base.data_collation(type_kind='name', type_name='android:id/message')

    # 導航欄
    home = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[0]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[0]')
    )

    member = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_member'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_member')
    )

    member_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[4]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[4]')
    )

    transaction = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_transaction'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_transaction')
    )
    
    deposit = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_deposit'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_deposit')
    )

    deposit_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='充值'),
        iOS = base.data_collation(type_kind='name', type_name='充值')
    )

    withdraw = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_withdraw'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_withdraw')
    )

    withdraw_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='提款'),
        iOS = base.data_collation(type_kind='name', type_name='提款')
    )

    trend = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_trend'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_trend')
    )
    
    transfer = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_transfer'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_transfer')
    )

    promotions = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='优惠活动'),
        iOS = base.data_collation(type_kind='name', type_name='优惠活动')
    )

    promotions_napp = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[1]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[1]')
    )

    faq = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_service'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_service')
    )

    customer_service = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[3]'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*rvTabBar', action='child()[3]')
    )
    
    red_envelope = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='紅包游戏'),
        iOS = base.data_collation(type_kind='name', type_name='紅包游戏')
    )

    red_envelope_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='红包'),
        iOS = base.data_collation(type_kind='name', type_name='红包')
    )

    red_envelope_other = base.check_device(
        Android = base.data_collation(type_kind='name', type_name='tabBarItem_hb'),
        iOS = base.data_collation(type_kind='name', type_name='tabBarItem_hb')
    )

    game_lobby = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='游戏大厅'),
        iOS = base.data_collation(type_kind='name', type_name='游戏大厅')
    )

    # 快捷選項
    card_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='棋牌游戏'),
        iOS = base.data_collation(type_kind='name', type_name='棋牌游戏')
    )

    vedio_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='真人娱乐'),
        iOS = base.data_collation(type_kind='name', type_name='真人娱乐')
    )

    electronic_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='电子游戏'),
        iOS = base.data_collation(type_kind='name', type_name='电子游戏')
    )

    sport_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='体育投注'),
        iOS = base.data_collation(type_kind='name', type_name='体育投注')
    )

    fish_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='捕鱼王'),
        iOS = base.data_collation(type_kind='name', type_name='捕鱼王')
    )

    lottery_home_icon = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='彩票大厅'),
        iOS = base.data_collation(type_kind='name', type_name='彩票大厅')
    )

    # napp快捷選項
    card_game = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='棋牌'),
        iOS = base.data_collation(type_kind='name', type_name='棋牌')
    )

    lottery_home_napp = base.check_device(
        Android = base.data_collation(type_kind='text', type_name='彩票'),
        iOS = base.data_collation(type_kind='name', type_name='彩票')
    )

    mail = 'image/app/mail.png'

    mail_center = base.check_device(
        Android = base.data_collation(type_kind='nameMatches', type_name='.*btnMsg'),
        iOS = base.data_collation(type_kind='nameMatches', type_name='.*btnMsg')
    )

    # 第三方棋牌
    kk_card = base.data_collation(type_kind='name', type_name='kk_qipai')
    fg_card = base.data_collation(type_kind='name', type_name='fg_qipai')
    vg_card = base.data_collation(type_kind='name', type_name='vg_qipai')
    ky_card = base.data_collation(type_kind='name', type_name='ky_qipai')
    bs_card = base.data_collation(type_kind='name', type_name='bs_qipai')
    lc_card = base.data_collation(type_kind='name', type_name='lc_qipai')
    gm_card = base.data_collation(type_kind='name', type_name='gm_qipai')

    # 第三方真人視訊
    bbin_vedio = base.data_collation(type_kind='name', type_name='bbin_vedio')
    ag_vedio = base.data_collation(type_kind='name', type_name='ag_video')
    mg_vedio = base.data_collation(type_kind='name', type_name='mg_video')
    gc_vedio = base.data_collation(type_kind='name', type_name='gc_vedio')

    # 第三方電子
    ag_electronic = base.data_collation(type_kind='name', type_name='ag_game')
    mg_electronic = base.data_collation(type_kind='name', type_name='mg_game')
    lgd_electronic = base.data_collation(type_kind='name', type_name='dt_game')
    cq9_electronic = base.data_collation(type_kind='name', type_name='cq_game')
    pt_electronic = base.data_collation(type_kind='name', type_name='pt_game')
    bbin_electronic = base.data_collation(type_kind='name', type_name='bbin_game')
    sb_electronic = base.data_collation(type_kind='name', type_name='sb_game')
    fg_electronic = base.data_collation(type_kind='name', type_name='fg_game')
    sw_electronic = base.data_collation(type_kind='name', type_name='sw_game')
    kk_electronic = base.data_collation(type_kind='name', type_name='kk_game')

    # 第三方體育
    sb_sport = base.data_collation(type_kind='name', type_name='sb_sportbooks', action='child()[1].child()[1]')
    bbin_sport = base.data_collation(type_kind='name', type_name='bbin_sport', action='child()[1].child()[1]')
    ss_sport = base.data_collation(type_kind='name', type_name='ss_sport', action='child()[1].child()[1]')
    hg_sport = base.data_collation(type_kind='name', type_name='hg_sport', action='child()[1].child()')
    
    # 第三方捕魚
    ag_fish = base.data_collation(type_kind='name', type_name='ag_fish')
    bbin_fish = base.data_collation(type_kind='name', type_name='bbin_fish')
    cq9_fish = base.data_collation(type_kind='name', type_name='cq_fish')

class MainPage(Base):
    # 檢查當前環境
    def check_env(self, env):
        try:
            current_env = self.common.poco_get_text(MainPageLocator.env(env))
            return current_env
        except:
            return False

    # 登入頁點擊來去逛逛
    def skip_login_page(self, level):
        if self.common.poco_exists(MainPageLocator.guestview_first):
            self.common.poco_click(MainPageLocator.guestview_first)
            return 1
        else:
            return level

    # 關閉引導新版彈窗
    def close_new_version_pop(self):
        if self.common.poco_exists(MainPageLocator.close_pop):
            self.common.poco_click(MainPageLocator.close_pop)

    # 關閉更新密碼提醒
    def skip_change_password(self, level):
        if self.common.poco_exists(MainPageLocator.skip_change_password):
            self.common.poco_click(MainPageLocator.skip_change_password)
            return 3
        else:
            return level

    # 關閉登入公告
    def skip_announcement(self):
        while self.common.poco_exists(MainPageLocator.confirm_announcement):
            self.common.poco_click(MainPageLocator.confirm_announcement)

    # 關閉登入公告
    def skip_announcement_napp(self, level):
        if self.common.poco_exists(MainPageLocator.close_announcement):
            self.common.poco_click(MainPageLocator.close_announcement)
            return 2
        else:
            return level
    
    # 關閉站內信彈窗
    def skip_mail_popup(self, level):
        if self.common.poco_exists(MainPageLocator.close_mail):
            self.common.poco_click(MainPageLocator.close_mail)
            return 4
        else:
            return level

    # 關閉登入浮窗
    def close_login_popup(self):
        if self.common.poco_exists(MainPageLocator.login_button):
            self.common.poco_click(MainPageLocator.close_login)

    # 確認熱更重啟
    def app_update_and_restart(self):
        if self.common.poco_exists(MainPageLocator.update):
            self.common.poco_click(MainPageLocator.update)

    # 確認熱更重啟napp
    def napp_update_and_restart(self):
        if self.common.poco_exists(MainPageLocator.allow_traditional):
            self.common.poco_click(MainPageLocator.allow_traditional)
        if self.common.poco_exists(MainPageLocator.uniformly_allow):
            self.common.poco_click(MainPageLocator.uniformly_allow)
        if self.common.poco_exists(MainPageLocator.allow_forever):
            self.common.poco_click(MainPageLocator.allow_forever) 
        if self.common.poco_exists(MainPageLocator.card_checkbox):
            self.common.poco_click(MainPageLocator.card_checkbox)
        if self.common.exists_image(MainPageLocator.setup_image):
            self.common.touch_image(MainPageLocator.setup_image)
        if self.common.poco_exists(MainPageLocator.open_app_style_3):
            self.common.poco_click(MainPageLocator.open_app_style_3)
        if self.common.poco_exists(MainPageLocator.continue_setup):
            self.common.poco_click(MainPageLocator.continue_setup)
        if self.common.poco_exists(MainPageLocator.continue_update):
            self.common.poco_click(MainPageLocator.continue_update)
        if self.common.poco_exists(MainPageLocator.open_app_style_2):
            self.common.poco_click(MainPageLocator.open_app_style_2)
        if self.common.poco_exists(MainPageLocator.always_allow):
            self.common.poco_click(MainPageLocator.always_allow)
        if self.common.poco_exists(MainPageLocator.update_setup):
            self.common.poco_click(MainPageLocator.update_setup)
        if self.common.poco_exists(MainPageLocator.allow_simplified):
            self.common.poco_click(MainPageLocator.allow_simplified)
        if self.common.poco_exists(MainPageLocator.update_napp):
            self.common.poco_click(MainPageLocator.update_napp)
        if self.common.poco_exists(MainPageLocator.set_up):
            self.common.poco_click(MainPageLocator.set_up)
        if self.common.poco_exists(MainPageLocator.open_app_style_1):
            self.common.poco_click(MainPageLocator.open_app_style_1)
        if self.common.poco_exists(MainPageLocator.allow_switch):
            self.common.poco_click(MainPageLocator.allow_switch)

    # 確認相機權限
    def confirm_camera(self):
        if self.common.poco_exists(MainPageLocator.confirm):
            self.common.poco_click(MainPageLocator.confirm)
        if self.common.poco_exists(MainPageLocator.allow_camera):
            self.common.poco_click(MainPageLocator.allow_camera)

    # 關閉搶登彈窗
    def skip_token_expired(self):
        if self.common.poco_exists(MainPageLocator.close_popup):
            self.common.poco_click(MainPageLocator.close_popup)

    # 關閉幸運轉盤
    def skip_lucky_wheel(self):
        if self.common.poco_exists(MainPageLocator.close_lucky_wheel):
            self.common.poco_click(MainPageLocator.close_lucky_wheel)

    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status(self):
        # 檢查畫面上是否有登入鈕
        if self.common.poco_exists(MainPageLocator.login) or self.common.poco_exists(MainPageLocator.login_button):
            return False

        return True
    
    # 回傳登入狀態，已登入回傳True，反之回傳False
    def check_login_status_napp(self):
        # 檢查畫面上是否有登入字樣
        if self.common.poco_exists(MainPageLocator.login_napp):
            return False
        
        return True

    def into_home_check(self, status):
        number = 0
        level = 0
        for loop in range(0, 60):

            self.close_new_version_pop()
            self.app_update_and_restart()
            self.skip_change_password(level)
            self.skip_announcement()

            if status is True:
                if self.check_login_status() is False:
                    logging.warning('帳號被登出了')
                    return False
            else:
                self.close_login_popup()

            if self.common.poco_exists(MainPageLocator.electronic_icon) \
                or self.common.poco_exists(MainPageLocator.lottery_home_icon): 
                number += 1     # 為避免找到首頁定位後才跳出彈窗，故找到後再跑一次
                if number == 2:
                    break

            if loop == 59:
                raise EOFError('開啟app錯誤')

    def into_home_check_napp(self, status, brand):
        level = 0       # 對應層級去跑特定function以減少時間 1=未登入 2=跑過更改密碼 3=跑過登入公告 4=跑過站內信彈窗
        for loop in range(0, 140):      # 部分裝置更新太慢，需要多一點時間
            if level < 1:
                self.confirm_camera()
                self.napp_update_and_restart()
            
            if level == 0 or level == 2:
                level = self.skip_change_password(level)

            if level == 0 or level == 3:
                level = self.skip_announcement_napp(level)

            if level < 4:
                level = self.skip_mail_popup(level)

            if level < 2:
                if status is True:
                    if self.check_login_status_napp() is False:
                        logging.warning('帳號被登出了')
                        level = self.skip_login_page(level)
                        return False
                else:
                    level = self.skip_login_page(level)
                    self.skip_token_expired()
            
            if brand == 'ttmj':
                self.skip_lucky_wheel()

            if self.common.poco_exists(MainPageLocator.card_game):
                return status

            if loop == 139:
                return '開啟app錯誤'

    # def into_home_check_napp(self, status, brand):
    #     level = 0       # 對應層級去跑特定function以減少時間 1=未登入 2=跑過更改密碼 3=跑過登入公告 4=跑過站內信彈窗
    #     for loop in range(0, 60):
    #         if level < 1:
    #             self.confirm_camera()

    #         if level == 0 or level == 2:
    #             level = self.skip_change_password(level)

    #         if level == 0 or level == 3:
    #             level = self.skip_announcement_napp(level)

    #         if level < 4:
    #             level = self.skip_mail_popup(level)

    #         if level < 2:
    #             if status is True:
    #                 if self.check_login_status_napp() is False:
    #                     logging.warning('帳號被登出了')
    #                     level = self.skip_login_page(level)
    #                     return False
    #             else:
    #                 level = self.skip_login_page(level)
    #                 self.skip_token_expired()
            
    #         if brand == 'ttmj':
    #             self.skip_lucky_wheel()

    #         if self.common.poco_exists(MainPageLocator.card_game):
    #             return status

    #         if loop == 59:
    #             return '開啟app錯誤'

    # 登出
    def logout(self):
        if self.common.poco_wait_exists(MainPageLocator.member):
            self.common.poco_click(MainPageLocator.member)
        else:
            raise EOFError('點擊會員中心錯誤')
                    
        if self.common.poco_wait_exists(MainPageLocator.logout, timeout=10):
            self.common.poco_click(MainPageLocator.logout)
        else:
            raise EOFError('點擊登出錯誤')
    
    # 登出
    def logout_napp(self):
        if self.common.poco_wait_exists(MainPageLocator.member_napp):
            self.common.poco_click(MainPageLocator.member_napp)
        else:
            raise EOFError('點擊會員中心錯誤')
                    
        self.common.go_down()
        if self.common.poco_wait_exists(MainPageLocator.logout, timeout=10):
            self.common.poco_click(MainPageLocator.logout)
        else:
            raise EOFError('點擊登出錯誤')

    # 登入
    def login(self, account:str, password:str):
        if self.check_login_status():
            self.logout()

        self.common.poco_click(MainPageLocator.login)
        self.common.poco_send_text(MainPageLocator.account, account)
        self.common.poco_send_text(MainPageLocator.password, password)
        self.common.sleep(2)
        
        if self.common.poco_exists(MainPageLocator.login_button):
            self.common.poco_click(MainPageLocator.login_button)

        if self.common.poco_exists(MainPageLocator.error):
            error_message = self.common.poco_get_text(MainPageLocator.error_message)
            raise EOFError(f'登入失敗-{error_message}')

    # 登入
    def login_napp(self, account, password):
        if self.check_login_status_napp():
            self.logout_napp()
        
        if self.common.poco_exists(MainPageLocator.member_login):
            self.common.poco_click(MainPageLocator.member_login)

        if self.common.poco_wait_exists(MainPageLocator.account_napp):
            self.common.poco_click(MainPageLocator.account_napp)    
            self.common.poco_click(MainPageLocator.closs_icon)   # 清掉記住的帳號
            self.common.poco_send_text(MainPageLocator.account_field, account)
        self.common.poco_click(MainPageLocator.login_napp)
        self.common.poco_click(MainPageLocator.password_napp)
        self.common.poco_click(MainPageLocator.closs_icon)
        self.common.poco_send_text(MainPageLocator.password_field, password)
        self.common.poco_click(MainPageLocator.login_button_napp)
        self.common.sleep(1)

        if self.common.poco_exists(MainPageLocator.close_popup):
            error_message = self.common.poco_get_text(MainPageLocator.error_message_napp)
            raise EOFError(f'登入失敗-{error_message}')
        
        if self.check_login_status_napp() != True:
            raise EOFError(f'登入失敗')

    def register(self):
        if self.check_login_status():
            self.logout()
        
        if self.common.poco_exists(MainPageLocator.register):
            self.common.poco_click(MainPageLocator.register)
        elif self.common.poco_exists(MainPageLocator.register_button):
            self.common.poco_click(MainPageLocator.register_button)

    # 註冊
    def register_napp(self):
        if self.check_login_status_napp():
            self.logout_napp()
        
        if self.common.poco_exists(MainPageLocator.member_login):
            self.common.poco_click(MainPageLocator.member_login)
        if self.common.poco_exists(MainPageLocator.register):
            self.common.poco_click(MainPageLocator.register)
    
    # 註冊完回到首頁需要檢查的項目
    def after_register(self, brand):
        level = 0
        for loop in range(0, 60):
            self.skip_announcement_napp(level)
            if brand == 'ttmj':
                self.skip_lucky_wheel()
            if self.common.poco_exists(MainPageLocator.card_game):
                break

            if loop == 59:
                raise EOFError('註冊完回首頁錯誤')

    def search_game(self, game_name):
        for i in range(0, 15):
            if self.common.poco_exists(game_name):
                self.common.poco_click(game_name)
                if self.common.poco_exists(game_name):
                    self.common.poco_click(game_name)
                return
            if i > 5:
                self.common.go_down()
            self.common.sleep(1)

        raise EOFError(f'找不到此第三方遊戲入口: {game_name}')

    # 點擊快捷選項
    # 棋牌遊戲
    def search_fg_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.fg_card)

    def search_ky_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.ky_card)

    def search_vg_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.vg_card)

    def search_bs_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.bs_card)
    
    def search_lc_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.lc_card)

    def search_gm_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.gm_card)

    def search_kk_card(self):
        self.search_game(MainPageLocator.card_icon)
        self.search_game(MainPageLocator.kk_card)

    # 真人視訊
    def search_bbin_vedio(self):
        self.search_game(MainPageLocator.vedio_icon)
        self.search_game(MainPageLocator.bbin_vedio)
    
    def search_ag_vedio(self):
        self.search_game(MainPageLocator.vedio_icon)
        self.search_game(MainPageLocator.ag_vedio)

    def search_gc_vedio(self):
        self.search_game(MainPageLocator.vedio_icon)
        self.search_game(MainPageLocator.gc_vedio)
    
    def search_mg_vedio(self):
        self.search_game(MainPageLocator.vedio_icon)
        self.search_game(MainPageLocator.mg_vedio)

    # 電子遊戲
    def search_ag_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.ag_electronic)
    
    def search_mg_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.mg_electronic)
    
    def search_lgd_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.lgd_electronic)

    def search_cq9_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.cq9_electronic)
    
    def search_pt_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.pt_electronic)
    
    def search_bbin_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.bbin_electronic)

    def search_sb_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.sb_electronic)
    
    def search_fg_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.fg_electronic)
    
    def search_sw_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.sw_electronic)
    
    def search_kk_electronic(self):
        self.search_game(MainPageLocator.electronic_icon)
        self.search_game(MainPageLocator.kk_electronic)

    # 體育投注
    def search_sb_sport(self):
        self.search_game(MainPageLocator.sport_icon)
        self.search_game(MainPageLocator.sb_sport)
    
    def search_bbin_sport(self):
        self.search_game(MainPageLocator.sport_icon)
        self.search_game(MainPageLocator.bbin_sport)

    def search_ss_sport(self):
        self.search_game(MainPageLocator.sport_icon)
        self.search_game(MainPageLocator.ss_sport)
   
    def search_hg_sport(self):
        self.search_game(MainPageLocator.sport_icon)
        self.search_game(MainPageLocator.hg_sport)

    # 捕魚王
    def search_ag_fish(self):
        self.search_game(MainPageLocator.fish_icon)
        self.search_game(MainPageLocator.ag_fish)

    def search_bbin_fish(self):
        self.search_game(MainPageLocator.fish_icon)
        self.search_game(MainPageLocator.bbin_fish)

    def search_cq9_fish(self):
        self.search_game(MainPageLocator.fish_icon)
        self.search_game(MainPageLocator.cq9_fish)


    # 點擊導航欄
    def member_click(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MainPageLocator.member):
                self.common.poco_click(MainPageLocator.member)
                return
            if loop == 2:
                raise EOFError('點擊會員中心頁面錯誤')

    # 點擊導航欄
    def member_click_napp(self):
        for loop in range(0, 3):
            if self.common.poco_exists(MainPageLocator.member_napp):
                self.common.poco_click(MainPageLocator.member_napp)
                return
            if loop == 2:
                raise EOFError('點擊會員頁面錯誤')
    
    def trend_click(self):
        if self.common.poco_exists(MainPageLocator.trend):
            self.common.poco_click(MainPageLocator.trend)
        else:
            self.common.skip_test('導航欄沒有放置開獎走勢')

    def deposit_click(self):
        if self.common.poco_exists(MainPageLocator.transaction):
            self.common.poco_click(MainPageLocator.transaction)
            self.common.poco_click(MainPageLocator.deposit)
    
    def deposit_click_napp(self):
        if self.common.poco_exists(MainPageLocator.deposit_napp):
            self.common.poco_click(MainPageLocator.deposit_napp)

    def withdraw_click(self):
        if self.common.poco_exists(MainPageLocator.transaction):
            self.common.poco_click(MainPageLocator.transaction)
            self.common.poco_click(MainPageLocator.withdraw)

    def withdraw_click_napp(self):
        if self.common.poco_exists(MainPageLocator.withdraw_napp):
            self.common.poco_click(MainPageLocator.withdraw_napp)

    def transfer_click(self):
        if self.common.poco_exists(MainPageLocator.transfer):
            self.common.poco_click(MainPageLocator.transfer)
        else:
            self.common.skip_test('導航欄沒有放置額度轉換')

    def promotions_click(self):
        if self.common.poco_exists(MainPageLocator.promotions):
            self.common.poco_click(MainPageLocator.promotions)
        else:
            self.common.skip_test('導航欄、快捷選項都沒有放置優惠活動')
    
    def promotions_click_napp(self):
        if self.common.poco_exists(MainPageLocator.promotions_napp):
            self.common.poco_click(MainPageLocator.promotions_napp)
        else:
            self.common.skip_test('導航欄、快捷選項都沒有放置優惠活動')

    def faq_click(self):
        if self.common.poco_exists(MainPageLocator.faq):
            self.common.poco_click(MainPageLocator.faq)

    def customer_service_click(self):
        if self.common.poco_exists(MainPageLocator.customer_service):
            self.common.poco_click(MainPageLocator.customer_service)

    def mail_center_click(self):
        self.common.touch_image(MainPageLocator.mail)
    
    def mail_center_click_napp(self):
        self.common.poco_click(MainPageLocator.mail_center)

    def red_envelope_click(self):
        if self.common.poco_exists(MainPageLocator.red_envelope):
            self.common.poco_click(MainPageLocator.red_envelope)
        elif self.common.poco_exists(MainPageLocator.red_envelope_other):
            self.common.poco_click(MainPageLocator.red_envelope_other)
    
    def red_envelope_click_napp(self):
        if self.common.poco_exists(MainPageLocator.red_envelope_napp):
            self.common.poco_click(MainPageLocator.red_envelope_napp)

    def home_click(self):
        if self.common.poco_exists(MainPageLocator.game_lobby):
            self.common.poco_click(MainPageLocator.game_lobby)
    
    def home_click_napp(self):
        if self.common.poco_exists(MainPageLocator.home):
            self.common.poco_click(MainPageLocator.home)
    
    def lottery_home(self):
        self.common.poco_click(MainPageLocator.lottery_home_icon)

    def lottery_home_napp(self):
        self.common.poco_click(MainPageLocator.lottery_home_napp)