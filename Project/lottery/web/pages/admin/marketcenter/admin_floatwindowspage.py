from selenium.webdriver.common.by import By
from pages.admin.admin_basepage import BasePage
import os, platform

class FloatWindowsLocator():
    # 左側浮窗
    left_display = (By.XPATH, "(//input[@value='1'])[1]") # 左測浮窗顯示
    left_hidden = (By.XPATH, "(//input[@value='0'])[1]") # 左側浮窗隱藏
    btn_left_revising = (By.XPATH, "//a[@href='/connectionlink/floatingwindowpc/floating-left/advancedsetting']") # 左側浮窗修改

    # 右側浮窗
    right_display = (By.XPATH, "(//input[@value='1'])[2]") # 右測浮窗顯示
    right_hidden = (By.XPATH, "(//input[@value='0'])[2]") # 右測浮窗顯示
    btn_right_revising = (By.XPATH, "//a[@href='/connectionlink/floatingwindowpc/floating-right/advancedsetting']") # 右測浮窗修改

    btn_submit = (By.XPATH, "//button[@type='button']") # 保存

    # 內容圖片
    content_image = (By.XPATH, "(//div[contains(@data-bind, 'sortable')])[1]//input[@type='file']") # 內容圖片底下所有的圖片欄位

    # 修改
    title = (By.XPATH, "(//input[@data-bind='textInput: model.title'] )[1]") # 標題
    display = (By.XPATH, "(//input[@value='1'])[1]") # 顯示
    hidden = (By.XPATH, "(//input[@value='0'])[1]") # 隱藏
    slip = (By.XPATH, "//span[text()='滑入滑出']") # 滑入滑出
    check = (By.XPATH, "//span[text()='滑鼠点击']") # 滑鼠點擊
    photo = (By.XPATH, "(//input[@type='file'])[1]") # 展開圖片
    delete_image = (By.XPATH, "//button[contains(@data-bind, 'deleteWindowTitlePicture()')]")

    link3 = (By.XPATH, "(//option[text()='內部连结'])[3]") # 內部連結
    last_internal_link = (By.XPATH, "(//option[text()='內部连结'])[last()]") # 最後的內部連結
    last_close_link = (By.XPATH, "(//option[text()='收起浮窗'])[last()]") # 最後的收起浮窗連結
    link_external = (By.XPATH, "(//option[text()='外部连结'])[1]") # 外部連結
    promo_link = (By.XPATH, "(//option[text()='优惠大厅'])[3]") # 優惠大廳
    customerservice = (By.XPATH, "(//option[text()='站内客服'])[3]")
    submit = (By.XPATH, "//button[text()='保存']") # 保存

    #
    inside_link = (By.XPATH, "//option[text()='內部连结']")
    add_image_column = (By.XPATH, "//a[contains(@data-bind, '$root.addImage();') and text()='+新增图片']")

    
class FloatWindowsPage(BasePage):
    # 右側浮窗
    def right_setting(self, setting=True):
        # 顯示
        if setting == True:
            self.click(FloatWindowsLocator.right_display)
            self.click(FloatWindowsLocator.btn_submit)
        # 隱藏
        elif setting == False:
            self.click(FloatWindowsLocator.right_hidden)
            self.click(FloatWindowsLocator.btn_submit)
    # 左側浮窗
    def left_setting(self, setting=True):
        # 顯示
        if setting == True:
            self.click(FloatWindowsLocator.left_display)
            self.click(FloatWindowsLocator.btn_submit)
        # 隱藏
        elif setting == False:
            self.click(FloatWindowsLocator.left_hidden)
            self.click(FloatWindowsLocator.btn_submit)

    # 右側浮窗修改
    def into_right_revising(self):
        self.click(FloatWindowsLocator.btn_right_revising)
        title = self.get_text(FloatWindowsLocator.title)
        # assert title == "右侧浮窗", r"標題名稱錯誤應為 '右侧浮窗'"
        self.click(FloatWindowsLocator.display)
        self.sleep(1)
        # 上傳檔案
        if platform.system() == "Windows":
            user = os.environ['HOMEPATH']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"\image\web\setting_photo\228X113_photo.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Linux':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/228X113_photo.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Darwin':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/228X113_photo.png"
            file_path = origin_path + image_path

        self.type(FloatWindowsLocator.photo, file_path)
        self.sleep(3)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)

    # 右側浮窗展開圖片_回復原始圖片
    def right_revising_reset(self):
        self.click(FloatWindowsLocator.btn_right_revising)
        assert self.is_element_finded(FloatWindowsLocator.delete_image) == True, "刪除btn沒有找到"
        self.click(FloatWindowsLocator.delete_image)
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)

    # 右側浮窗_新增圖片
    def right_floating_add(self):
        self.click(FloatWindowsLocator.btn_right_revising)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.display)
        self.wait_loading_finish()
        self.sleep(1)
        # 先行確認內部欄位數量
        inside_column_num = len(self.find_elements(FloatWindowsLocator.inside_link))
        assert self.is_element_finded(FloatWindowsLocator.add_image_column) == True, "新增圖片_未存在"
        self.click(FloatWindowsLocator.add_image_column)
        self.wait_loading_finish()
        after_column = len(self.find_elements(FloatWindowsLocator.inside_link))
        assert (after_column == inside_column_num + 1) == True, "介面管理_右側浮窗_未新增成功"

        # 內容圖片_欄位數量
        content_image_num = len(self.find_elements(FloatWindowsLocator.content_image))

        new_link_num = "(//option[text()='內部连结'])[{}]".format(int(after_column))
        new_photo_num = f"((//div[contains(@data-bind, 'sortable')])[1]//input[@type='file'])[{int(content_image_num)}]"
        # new_customer_service_num = "(//option[text()='站内客服'])[{}]".format(int(after_column))
        
        new_link = (By.XPATH, new_link_num)
        new_photo = (By.XPATH, new_photo_num)
        # new_customer_service = (By.XPATH, new_customer_service_num)
        
        assert self.is_element_finded(new_link) == True, "新增浮窗_連結欄位未找到"
        assert self.is_element_finded(new_photo) == True, "新增浮窗_圖片欄位未找到"
        # assert self.is_element_finded(new_promo_link) == True, "新增浮窗_下拉式選單沒有'优惠大厅'選項"

        # 上傳圖片檔案
        if platform.system() == "Windows":
            user = os.environ['HOMEPATH']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"\image\web\setting_photo\QA_167x83.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Linux':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Darwin':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path

        self.scroll_to_bottom()
        self.type(new_photo, file_path)
        self.wait_loading_finish()
        self.sleep(3)
        self.click(new_link)
        self.wait_loading_finish()
        self.sleep(1)
        customer_service = (By.XPATH, "//option[text()='站内客服']")
        new_customer_service_num = len(self.find_elements(customer_service))
        new_customer_service = (By.XPATH, f"(//option[text()='站内客服'])[{int(new_customer_service_num)}]")
        self.click(new_customer_service)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)
        self.wait_loading_finish()
        self.sleep(1)

    # 右側浮窗_新增圖片_reset刪除
    def right_floating_reset(self):
        self.click(FloatWindowsLocator.btn_right_revising)
        # 先行確認內部欄位數量
        inside_column_num = len(self.find_elements(FloatWindowsLocator.inside_link))
        delete_pos_num = "(//div[@class='close pic_close'])[{}]".format(int(inside_column_num))
        delete_pos = (By.XPATH, delete_pos_num)
        assert self.is_element_finded(delete_pos) == True, "叉叉btn未找到"
        self.click(delete_pos)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)

    # 左側浮窗修改
    def into_left_revising(self):
        self.click(FloatWindowsLocator.btn_left_revising)
        title = self.get_text(FloatWindowsLocator.title)
        # assert title == "左侧浮窗", r"標題名稱錯誤應為 '左侧浮窗'"
        self.click(FloatWindowsLocator.display) # 狀態-顯示
        self.click(FloatWindowsLocator.check)   # 展開模式-滑鼠點擊
        self.sleep(1)
        # 上傳檔案
        if platform.system() == "Windows":
            user = os.environ['HOMEPATH']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"\image\web\setting_photo\50X20_photo.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Linux':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/50X20_photo.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Darwin':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/50X20_photo.png"
            file_path = origin_path + image_path

        self.type(FloatWindowsLocator.photo, file_path) # 上傳展開圖片
        self.sleep(3)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)

    # 左側浮窗展開圖片_回復原始圖片
    def left_revising_reset(self):
        self.click(FloatWindowsLocator.btn_left_revising)
        if self.is_element_finded(FloatWindowsLocator.delete_image):
            self.click(FloatWindowsLocator.delete_image)
        # assert self.is_element_finded(FloatWindowsLocator.delete_image) == True, "刪除btn沒有找到"
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)

    # 左側浮窗_新增圖片
    def left_floating_add_promo(self):
        self.click(FloatWindowsLocator.btn_left_revising)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.display)
        self.wait_loading_finish()
        self.sleep(1)
        # 先行確認內部欄位數量
        inside_column_num = len(self.find_elements(FloatWindowsLocator.inside_link))
        assert self.is_element_finded(FloatWindowsLocator.add_image_column) == True, "新增圖片BTN_未存在"
        self.click(FloatWindowsLocator.add_image_column)
        self.wait_loading_finish()
        after_column = len(self.find_elements(FloatWindowsLocator.inside_link))
        assert (after_column == inside_column_num + 1) == True, "介面管理_左側浮窗_未新增成功"
        
        # 內容圖片_欄位數量
        content_image_num = len(self.find_elements(FloatWindowsLocator.content_image))

        new_link_num = f"(//option[text()='內部连结'])[{int(after_column)}]"
        new_photo_num = f"((//div[contains(@data-bind, 'sortable')])[1]//input[@type='file'])[{int(content_image_num)}]"
        # new_promo_link_num = f"(//option[text()='优惠大厅'])[{int(after_column)}]"
        
        new_link = (By.XPATH, new_link_num)
        new_photo = (By.XPATH, new_photo_num)
        # new_promo_link = (By.XPATH, new_promo_link_num)
        assert self.is_element_finded(new_link) == True, "新增浮窗_連結欄位未找到"
        assert self.is_element_finded(new_photo) == True, "新增浮窗_圖片欄位未找到"
        # assert self.is_element_finded(new_promo_link) == True, "新增浮窗_下拉式選單沒有'优惠大厅'選項"

        # 上傳圖片檔案
        if platform.system() == "Windows":
            user = os.environ['HOMEPATH']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"\image\web\setting_photo\QA_167x83.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Linux':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path

        elif platform.system() == 'Darwin':
            user = os.environ['HOME']
            origin_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))
            image_path = r"/image/web/setting_photo/QA_167x83.png"
            file_path = origin_path + image_path
        
        self.scroll_to_bottom()
        self.type(new_photo, file_path)
        self.wait_loading_finish()
        self.sleep(3)
        self.click(new_link)
        self.wait_loading_finish()
        self.sleep(1)
        promo_link = (By.XPATH, "//option[text()='优惠大厅']")
        new_promo_link_num = len(self.find_elements(promo_link))
        new_promo_link = (By.XPATH, f"(//option[text()='优惠大厅'])[{int(new_promo_link_num)}]")
        self.click(new_promo_link)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)
        self.wait_loading_finish()
        self.sleep(1)

    # 左側浮窗_新增圖片_reset刪除
    def left_floating_reset(self):
        self.click(FloatWindowsLocator.btn_left_revising)
        # 先行確認內部欄位數量
        inside_column_num = len(self.find_elements(FloatWindowsLocator.inside_link))
        delete_pos_num = "(//div[@class='close pic_close'])[{}]".format(int(inside_column_num))
        delete_pos = (By.XPATH, delete_pos_num)
        assert self.is_element_finded(delete_pos) == True, "叉叉btn未找到"
        self.click(delete_pos)
        self.wait_loading_finish()
        self.sleep(1)
        self.click(FloatWindowsLocator.submit)
        
    # 內部連結-優惠大廳
    def mobile_hall_link(self):
        self.click(FloatWindowsLocator.btn_left_revising)
        title = self.get_text(FloatWindowsLocator.title)
        # assert title == "左侧浮窗", r"標題名稱錯誤應為 '左侧浮窗'"
        self.click(FloatWindowsLocator.display)
        self.sleep(1)
        self.click(FloatWindowsLocator.link3)
        self.click(FloatWindowsLocator.promo_link)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)
    
    # 內部連結-站內客服
    def customerservice_link(self):
        self.click(FloatWindowsLocator.btn_right_revising)
        # title = self.get_text(FloatWindowsLocator.title)
        self.click(FloatWindowsLocator.display)
        self.sleep(1)        
        self.click(FloatWindowsLocator.link3)
        self.click(FloatWindowsLocator.customerservice)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)

    # 內部連結-收起浮窗
    def close_floatwindows_link(self):
        self.click(FloatWindowsLocator.btn_left_revising)   # 設定左側浮窗
        self.click(FloatWindowsLocator.display)
        self.sleep(1)        
        self.click(FloatWindowsLocator.last_internal_link)
        self.click(FloatWindowsLocator.last_close_link)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)
        self.sleep(2)
        self.wait_loading_finish()
        self.click(FloatWindowsLocator.btn_right_revising)  # 設定右側浮窗
        self.click(FloatWindowsLocator.display)
        self.sleep(1)        
        self.click(FloatWindowsLocator.last_internal_link)
        self.click(FloatWindowsLocator.last_close_link)
        self.scroll_to_bottom()
        self.click(FloatWindowsLocator.submit)