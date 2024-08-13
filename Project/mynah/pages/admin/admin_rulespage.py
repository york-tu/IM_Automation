import sys
import os
import random
from Project.mynah.pages.admin.admin_basepage import AdminBasePage
from selenium.webdriver.common.by import By


class RulesLocator:
    label_disconnect_notend = (By.XPATH, "//*[text()='客服断线']/..//*[text()='不自动结束']")                   #客服斷線 不自動結束
    label_disconnect_autoend = (By.XPATH, "//*[text()='客服断线']/..//*[text()='分钟后未连线自动结束']/..//span[@class='el-radio__inner']")   #客服斷線 要自動結束
    input_disconnect = (By.XPATH, "//*[text()='客服断线']/..//*[text()='分钟后未连线自动结束']/.//input")       #客服斷線 輸入框
    label_visitor_notend = (By.XPATH, "//*[text()='访客未发话']/..//*[text()='不自动结束']")                    #訪客不發話 不自動結束
    label_visitor_autoend = (By.XPATH, "//*[text()='访客未发话']/..//*[text()='分钟后未连线自动结束']/..//span[@class='el-radio__inner']")   #訪客不發話 要自動結束
    input_visitor = (By.XPATH, "//*[text()='访客未发话']/..//*[text()='分钟后未连线自动结束']/.//input")        #訪客不發話 輸入框
    btn_save = (By.XPATH, "//button[@class='el-button el-button--primary el-button--mini']")      #保存按鈕
    alert_save = (By.XPATH, "//*[@class='el-message el-message--success']")                       #保存提示

class AdminRulesPage(AdminBasePage):

    # 打開"客服斷線"自動結束對話
    def open_disconnect_auto_end(self, times):
        self.wait_visibility(RulesLocator.input_disconnect)
        self.type(RulesLocator.input_disconnect, str(times))

        self.click(RulesLocator.label_disconnect_autoend)           #客服斷線 要自動結束
        self.click(RulesLocator.btn_save)                           #保存
        self.wait_visibility(RulesLocator.alert_save)                #保存成功提示

        
    # 打開"訪客未發話"自動結束對話
    def open_visitor_auto_end(self, times):
        self.wait_visibility(RulesLocator.input_visitor)
        self.type(RulesLocator.input_visitor, str(times))

        self.click(RulesLocator.label_visitor_autoend)              #點 訪客不發話 要自動結束
        self.click(RulesLocator.btn_save)                           #保存
        self.wait_visibility(RulesLocator.alert_save)                            #保存成功提示
    
    # 關閉"客服斷線"自動結束對話
    def close_disconnect_auto_end(self):
        self.wait_visibility(RulesLocator.label_disconnect_notend)
        self.click(RulesLocator.label_disconnect_notend)         #客服斷線 不要自動結束
        self.click(RulesLocator.btn_save)                        #保存
        self.wait_visibility(RulesLocator.alert_save)                            #保存成功提示

    # 關閉"訪客未發話"自動結束對話
    def close_visitor_auto_end(self):
        self.wait_visibility(RulesLocator.label_visitor_notend)
        self.click(RulesLocator.label_visitor_notend)           #訪客不發話 不要自動結束
        self.click(RulesLocator.btn_save)                        #保存
        self.wait_visibility(RulesLocator.alert_save)                            #保存成功提示
        
    