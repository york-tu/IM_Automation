from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage

class ChannelSettingsPageLocators(BasePage):
    # 運維管理 -> 外接平台 -> 頻道設置

    button_save = (By.XPATH, '//button[contains(text(), "保存")]')  # 保存
    button_back = (By.XPATH, '//button[contains(text(), "返回")]')  # 返回
    button_disable = (By.XPATH,'//input[contains(@value, 0)]')  # 禁用按鈕

    def disable_text(self, num):
        disable_text = (By.XPATH, f'(//*[text()="禁用公告"]/..//textarea[@class="form-control" and not(@disabled="")])[{num+1}]')
        return disable_text

    def assign_disable(self, num):
        assign_disable = (By.XPATH, f'//input[contains(@name, "ko_unique_{num}")]')
        return assign_disable

    # ------------------------------------------------------------- 頻道選擇 -------------------------------------------------------------
    title_channel = (By.XPATH, "//div[contains(text(), '频道选择')]")

    channel_3s = (By.XPATH, "//h3[contains(text(), '3S')]")
    ok_channel_setting_3s = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='3S']/../..//*[text()='频道设置']")
    channel_ag = (By.XPATH, "//h3[contains(text(), 'AG')]")
    ok_channel_setting_ag = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='AG']/../..//*[text()='频道设置']")
    channel_bbin = (By.XPATH, "//h3[contains(text(), 'BBIN')]")
    ok_channel_setting_bbin = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='BBIN']/../..//*[text()='频道设置']")
    channel_bg = (By.XPATH, "//h3[contains(text(), 'BG')]")
    ok_channel_setting_bg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='BG']/../..//*[text()='频道设置']")
    channel_bsp = (By.XPATH, "//h3[contains(text(), 'BSP')]")
    ok_channel_setting_bsp = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='BSP']/../..//*[text()='频道设置']")
    channel_cq9 = (By.XPATH, "//h3[contains(text(), 'CQ9')]")
    ok_channel_setting_cq9 = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='CQ9']/../..//*[text()='频道设置']")
    channel_dg = (By.XPATH, "//h3[contains(text(), 'DG')]")
    ok_channel_setting_dg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='DG']/../..//*[text()='频道设置']")
    channel_fg = (By.XPATH, "//h3[contains(text(), 'FG')]")
    ok_channel_setting_fg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='FG']/../..//*[text()='频道设置']")
    channel_gc = (By.XPATH, "//h3[contains(text(), 'GC')]")
    ok_channel_setting_gc = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='GC']/../..//*[text()='频道设置']")
    channel_gm = (By.XPATH, "//h3[contains(text(), 'GM')]")
    ok_channel_setting_gm = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='GM']/../..//*[text()='频道设置']")
    channel_hg = (By.XPATH, "//h3[contains(text(), 'HG')]")
    ok_channel_setting_hg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='HG']/../..//*[text()='频道设置']")
    channel_kk = (By.XPATH, "//h3[contains(text(), 'KK')]")
    ok_channel_setting_kk = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='KK']/../..//*[text()='频道设置']")
    channel_kx = (By.XPATH, "//h3[contains(text(), 'KX')]")
    ok_channel_setting_kx = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='KX']/../..//*[text()='频道设置']")
    channel_ky = (By.XPATH, "//h3[contains(text(), 'KY')]")
    ok_channel_setting_ky = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='KY']/../..//*[text()='频道设置']")
    channel_lgd = (By.XPATH, "//h3[contains(text(), 'LGD')]")
    ok_channel_setting_lgd = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='LGD']/../..//*[text()='频道设置']")
    channel_mg = (By.XPATH, "//h3[contains(text(), 'MG')]")
    ok_channel_setting_mg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='MG']/../..//*[text()='频道设置']")
    channel_pt = (By.XPATH, "//h3[contains(text(), 'PT')]")
    ok_channel_setting_pt = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='PT']/../..//*[text()='频道设置']")
    channel_sb = (By.XPATH, "//h3[contains(text(), 'SB')]")
    ok_channel_setting_sb = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='SB']/../..//*[text()='频道设置']")
    channel_sp365 = (By.XPATH, "//h3[contains(text(), 'SP365')]")
    ok_channel_setting_sp365 = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='SP365']/../..//*[text()='频道设置']")
    channel_sw = (By.XPATH, "//h3[contains(text(), 'SW')]")
    ok_channel_setting_sw = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='SW']/../..//*[text()='频道设置']")
    channel_vg = (By.XPATH, "//h3[contains(text(), 'VG')]")
    ok_channel_setting_vg = (By.XPATH, "//span[contains(@data-bind, 'channelName') and text()='VG']/../..//*[text()='频道设置']")


class ChannelSettingsPage(BasePage):
    # 禁用此品牌所有遊戲
    def click_all_disable(self, notice="系统正在进行日常维护"):
        self.wait_loading_finish()
        for i in range(len(self.find_elements(ChannelSettingsPageLocators.button_disable))):
            index = 1 + 3 * i
            buf = ChannelSettingsPageLocators.assign_disable(self, index)
            self.click(ChannelSettingsPageLocators.assign_disable(self, index))
            self.sleep(1)
            # 提示文案  
            # 2020/10/16 PFREQ-38 應拔掉文字編輯器 所以寫法更改為直接定位輸入純文字
            # self.switch_frame(0)
            # self.type(ChannelSettingsPageLocators.text, notice)
            self.type( ChannelSettingsPageLocators.disable_text(self, i), notice)        
            # self.switch_default_frame()
        
        self.click(ChannelSettingsPageLocators.button_save)

    # 啟用此品牌所有遊戲
    def click_all_enable(self):
        self.wait_loading_finish()
        for i in range(len(self.find_elements(ChannelSettingsPageLocators.button_disable))):
            index = 2 + 3 * i
            self.click(ChannelSettingsPageLocators.assign_disable(self, index))
            self.sleep(1)
        
        self.click(ChannelSettingsPageLocators.button_save)

    def into_channel_setting_3s(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_3s)
        self.click(ChannelSettingsPageLocators.channel_3s)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_3s), f'點擊第三方，進入外接平台_頻道設置錯誤'
    
    def into_channel_setting_ag(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_ag)
        self.click(ChannelSettingsPageLocators.channel_ag)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_ag), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_bbin(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_bbin)
        self.click(ChannelSettingsPageLocators.channel_bbin)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_bbin), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_bg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_bg)
        self.click(ChannelSettingsPageLocators.channel_bg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_bg), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_bsp(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_bsp)
        self.click(ChannelSettingsPageLocators.channel_bsp)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_bsp), f'點擊第三方，進入外接平台_頻道設置錯誤'
    
    def into_channel_setting_cq9(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_cq9)
        self.click(ChannelSettingsPageLocators.channel_cq9)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_cq9), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_dg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_dg)
        self.click(ChannelSettingsPageLocators.channel_dg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_dg), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_fg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_fg)
        self.click(ChannelSettingsPageLocators.channel_fg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_fg), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_gc(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_gc)
        self.click(ChannelSettingsPageLocators.channel_gc)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_gc), f'點擊第三方，進入外接平台_頻道設置錯誤'
    
    def into_channel_setting_gm(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_gm)
        self.click(ChannelSettingsPageLocators.channel_gm)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_gm), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_hg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_hg)
        self.click(ChannelSettingsPageLocators.channel_hg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_hg), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_kk(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_kk)
        self.click(ChannelSettingsPageLocators.channel_kk)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_kk), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_kx(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_kx)
        self.click(ChannelSettingsPageLocators.channel_kx)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_kx), f'點擊第三方，進入外接平台_頻道設置錯誤'
    
    def into_channel_setting_ky(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_ky)
        self.click(ChannelSettingsPageLocators.channel_ky)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_ky), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_lgd(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_lgd)
        self.click(ChannelSettingsPageLocators.channel_lgd)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_lgd), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_mg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_mg)
        self.click(ChannelSettingsPageLocators.channel_mg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_mg), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_pt(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_pt)
        self.click(ChannelSettingsPageLocators.channel_pt)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_pt), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_sb(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_sb)
        self.click(ChannelSettingsPageLocators.channel_sb)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_sb), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_sp365(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_sp365)
        self.click(ChannelSettingsPageLocators.channel_sp365)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_sp365), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_sw(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_sw)
        self.click(ChannelSettingsPageLocators.channel_sw)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_sw), f'點擊第三方，進入外接平台_頻道設置錯誤'

    def into_channel_setting_vg(self):
        self.wait_visibility(ChannelSettingsPageLocators.channel_vg)
        self.click(ChannelSettingsPageLocators.channel_vg)
        self.wait_loading_finish()
        assert self.is_element_finded(ChannelSettingsPageLocators.ok_channel_setting_vg), f'點擊第三方，進入外接平台_頻道設置錯誤'