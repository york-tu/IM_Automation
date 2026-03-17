from time import sleep
from selenium.webdriver.common.by import By
from Project.chat.web.pages.web2.web2_basepage import BasePage


class FirstPageLocator:
    # ========== 左側導航欄 ==========
    firstPage_btn = (By.XPATH, "//span[text()='首页']")  # 首頁鍵
    login_btn = (By.XPATH, "//button[text()='登录']")  # 登录鍵
    mainPage_button = (By.XPATH, "//span[text()='主页']")  # 主頁鍵(已登入)
    more_btn = (By.XPATH, "//span[text()='更多']")  # 更多(已登入)

    # ========== 右側頁籤 ==========
    btn_following = (By.XPATH, "//button[normalize-space(text())='已关注']")  # 「已关注」tab
    btn_recommend = (By.XPATH, "//button[normalize-space(text())='推荐']")  # 「推荐」tab
    switch_display_mode_btn = (By.XPATH, "//div[@class='overflow-y-auto no-scrollbar h-[calc(100vh-160px)]']")  # 單一/多則貼文模式鍵
    multiple_post_mode = (By.XPATH, "//div[@class='overflow-y-auto no-scrollbar h-[calc(100vh-160px)]']")  # 多貼文模式
    single_post_mode = (By.XPATH, "//div[@class='swiper-wrapper']")  # 單一貼文模式


class FirstPage(BasePage):
    def switch_post_display_mode(self, mode='0'):  # 0->multi_mode, 1->single_mode
        self.click(FirstPageLocator.firstPage_btn)
        if mode == '0':
            if self.is_element_finded(FirstPageLocator.single_post_mode):
                self.click(FirstPageLocator.switch_display_mode_btn)
            assert self.is_element_finded(FirstPageLocator.multiple_post_mode)
        else:
            if self.is_element_finded(FirstPageLocator.multiple_post_mode):
                self.click(FirstPageLocator.switch_display_mode_btn)
            assert self.is_element_finded(FirstPageLocator.single_post_mode)
