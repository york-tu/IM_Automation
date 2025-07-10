from selenium.webdriver.common.by import By
from Project.chat.web.pages.webs.web_basepage import BasePage


class FirstPageLocator:
    # ============================= 導航欄 ==============================================================================
    firstPage_button_not_selected = (By.XPATH, "//p[@class='text-[12rem] font-bold' and text()='首页']")  # 導航欄-首页
    firstPage_button_selected = (By.XPATH, "//p[@class='text-[12rem] font-bold active' and text()='首页']")  # 導航欄-首页
    # ============================= 頁籤-已關注 =========================================================================
    followed_tab = (By.XPATH, "//p[@class='text-[16rem] font-semibold text-[#FFFFFF66] text_shadow' and text()='已关注']")  # 頁籤-已關注
    # ============================= 頁籤-推薦 ==========================================================================
    recommend_tab = (By.XPATH, "//p[@class='text-[16rem] font-semibold text-[#FFFFFF66] text_shadow' and text()='推荐']")  # 頁籤-推薦
    # ============================= 頁籤-搜尋貼文 =======================================================================
    search_post_tab = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/a[3]')  # 導航欄-搜尋貼文
    # ============================= 頁籤-圖庫/走勢 =======================================================================
    gallery_tab = (By.XPATH, "//div[@class='flex flex-col items-center flex-1 cursor-pointer py-[8rem] relative']//p[text()='图库']")  # 頁籤-圖庫
    trend_tab = (By.XPATH, "//div[@class='flex flex-col items-center flex-1 cursor-pointer py-[8rem] relative']//p[text()='走势']")  # 頁籤-走勢
    webpage_title = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[1]/span')  # 頁面標題


class FirstPage(BasePage):

    # =========================== 已關注 ======================================
    # =========================== 推薦 ========================================
    # =========================== 搜尋 ========================================
    # =========================== 圖庫/走勢 ====================================
    def open_gallery_page(self):
        if self.is_element_finded(FirstPageLocator.firstPage_button_not_selected):
            self.click(FirstPageLocator.firstPage_button_not_selected)
        self.click(FirstPageLocator.gallery_tab)
        self.wait_loading_finish()
        self.switch_last_page()
        self.wait_loading_finish()
        assert self.get_text(FirstPageLocator.webpage_title) == '六合图库'
        self.switch_home_page()

    def open_trend_page(self):
        if self.is_element_finded(FirstPageLocator.firstPage_button_not_selected):
            self.click(FirstPageLocator.firstPage_button_not_selected)
        self.click(FirstPageLocator.trend_tab)
        self.wait_loading_finish()
        self.switch_last_page()
        self.wait_loading_finish()
        assert self.get_text(FirstPageLocator.webpage_title) == '开奖号码'
        self.switch_home_page()
    # =========================== 首頁 ========================================
    # =========================== 好友 ========================================
    # =========================== 信息 ========================================
    # =========================== 主頁 ========================================










