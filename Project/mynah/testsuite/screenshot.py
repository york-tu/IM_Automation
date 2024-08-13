import os, datetime


class ScreenShot(object):

    def __init__(self, webdriver, folderpath):
        self.folderpath = folderpath
        self.webdriver = webdriver

    def screenshot(self, image_name):
        #  if not exists folder name screenshots, create one
        if not os.path.exists(self.folderpath):
            os.makedirs(self.folderpath)

        index = 0
        while True:
            if index == 0:
                self.image_path = self.folderpath + image_name + ".png"
            elif index > 0:
                self.image_path = self.folderpath + image_name + str(index) + ".png"

            if os.path.exists(self.image_path):
                index += 1
            elif not os.path.exists(self.image_path):
                break

        # 截圖並照時間命名
        self.webdriver.save_screenshot(self.image_path)
