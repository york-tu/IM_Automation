from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium import webdriver
import time, pytz, datetime, platform, sys
import pyautogui, logging
from random import randint
from opencc import OpenCC
import imaplib
import email
import re

class Common(object):
    def __init__(self, driver, sec, base_url, test_skip_method):
        if driver == '':
            return

        self.driver = driver
        # self.driver = webdriver.Chrome()  # for test
        self.driver.implicitly_wait(sec)
        self.driver.set_page_load_timeout(sec)
        self.wait = WebDriverWait(driver, sec)
        self.base_url = base_url
        self.sec = sec
        self.test_skip_method = test_skip_method
        self.os = platform.system()

    # ======== Browser ===============================================

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def refresh_browser(self):
        self.driver.refresh()

    def maximize_window(self):
        self.driver.maximize_window()

    def quit_browser(self):
        self.driver.quit()

    def close_browser(self):
        self.driver.close()

    def open_base_url(self):
        self.driver.get(self.base_url)

    def open_browser(self, url):
        self.driver.get(url)



    def sleep(self, seconds):
        time.sleep(seconds)

    def back(self):
        self.driver.back()

    # ======== Element ===============================================

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_finded(self, locator):
        self.implicitly_wait(0)
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            try:
                self.implicitly_wait(self.sec)
            except:
                self.implicitly_wait(20)

    def is_element_displayed(self, locator):
        self.implicitly_wait(0)
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
        finally:
            try:
                self.implicitly_wait(self.sec)
            except:
                self.implicitly_wait(20)
    
    def is_element_displayed_by_dom(self, element):
        '''
            回傳element是否有顯示 ， 參數element為webdriver.find_element的回傳值
        '''
        return element.is_displayed()

    def is_element_enable(self, locator):
        return self.find_element(locator).is_enabled()

    def is_element_selected(self, locator):
        return self.find_element(locator).is_selected()

    def wait_click_able(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_click_able_click(self, locator):
        self.wait_click_able(locator)
        self.click(locator)

    def wait_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_visibility_status(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_not_presence(self, locator):
        return self.wait.until_not(EC.presence_of_element_located(locator))

    def wait_window_opened(self, current_handles):
        return self.wait.until(EC.new_window_is_opened(current_handles))

    def implicitly_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def wait_alert_present(self):
        return self.wait.until(EC.alert_is_present())

    def wait_text_present(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_text_not_present(self, locator, text):
        return self.wait.until_not(EC.text_to_be_present_in_element(locator, text))

    # ======== Action ================================================

    def type(self, locator, text):
        el = self.find_element(locator)

        try:
            el.clear()
            if self.os == 'Darwin':
                el.send_keys(Keys.COMMAND + 'a') # mac
            else:
                el.send_keys(Keys.CONTROL + 'a') # windows
        except:
            pass

        el.send_keys(str(text))
    
    def type_js(self, locator, text, num=0):
        js = f'document.querySelectorAll("{locator}")[{num}].value=\"{text}\"'
        self.execute_js(js)
        
    def type_enter(self,locator):
        el = self.find_element(locator)
        el.send_keys(Keys.RETURN)
    
    def type_delete(self,locator):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(Keys.RETURN)
        el.send_keys(Keys.BACK_SPACE)

    def type_tab(self,locator):
        el = self.find_element(locator)
        el.send_keys(Keys.TAB)

    def type_page_up(self,locator):
        el = self.find_element(locator)
        el.send_keys(Keys.PAGE_UP)

    def type_page_down(self,locator):
        el = self.find_element(locator)
        el.send_keys(Keys.PAGE_DOWN)

    def type_paste(self, locator):
        el = self.find_element(locator)

        if self.os == 'Darwin':
            el.send_keys(Keys.COMMAND + 'v') # mac
        else:
            el.send_keys(Keys.CONTROL + 'v') # windows

    def type_by_dom(self, element, text):
        try:
            element.clear()
            if self.os == 'Darwin':
                element.send_keys(Keys.COMMAND + 'a') # mac
            else:
                element.send_keys(Keys.CONTROL + 'a') # windows
        except:
            pass

        element.send_keys(text)

    def click(self, locator):
        try:
            el = self.find_element(locator)
            el.click()
        except:
            try:
                self.scroll_to_top()
                self.sleep(1)
                el = self.find_element(locator)
                ActionChains(self.driver).move_to_element(el).perform()
                el.click()
            except:
                raise EOFError('點擊失敗')

    def context_click(self, locator):
        try:
            self.scroll_to_top()
            self.sleep(1)
            
            el = self.find_element(locator)
            ActionChains(self.driver).move_to_element(el).context_click(el).perform()
        except:
            raise EOFError('點擊失敗')

    def move_mouse(self, locator):
        self.sleep(0.5)
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()
    
    def click_by_dom(self, element):
        try:
            element.click()
        except:
            self.scroll_to_top()
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()

    def click_all(self, locator):
        els = self.find_elements(locator)
        for el in els:
            el.click()

    def click_js(self, locator):
        js = f'document.querySelectorAll("{locator}")[0].click()'
        self.execute_js(js)

    def submit(self, locator):
        el = self.find_element(locator)
        el.submit()

    def select_by_index(self, locator, index):
        el = self.find_element(locator)
        Select(el).select_by_index(index)

    def select_by_text(self, locator, text):
        el = self.find_element(locator)
        Select(el).select_by_visible_text(text)

    def scroll_to(self, num):
        js = 'window.scrollTo(0, '+str(num)+');'  # 頁面滾到最上方js
        self.execute_js(js)

    def scroll_to_top(self):
        js = 'window.scrollTo(0, 0);'  # 頁面滾到最上方js
        self.execute_js(js)

    def scroll_to_bottom(self):
        js = 'window.scrollTo(0, document.body.scrollHeight);'  # 頁面滾到最下方js
        self.execute_js(js)

    def scroll_to_middle(self):
        js = 'window.scrollTo(0, document.body.scrollHeight / 2);'  # 頁面滾到畫面中js
        self.execute_js(js)

    def scroll_to_element(self, locator):
        ActionChains(self.driver).move_to_element(self.find_element(locator)).perform()

    def scroll_bottom_java(self, locator):
        js = f'document.getElementsByClassName("{locator}")[0].scrollTop = 1000'  # 頁面滾到最下方jave
        self.execute_js(js)

    def send_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def long_press(self, locator):
        el = self.find_element(locator)
        ActionChains(self.driver).click_and_hold(el).pause(2).perform()

    def menu_click(self, locator):
        el = self.find_element(locator)
        ActionChains(self.driver).move_to_element(el).click().perform()
        el.click()

    def enable_DevTools(self):
        time.sleep(1)
        pyautogui.click(x=200, y=500)
        pyautogui.hotkey("ctrl", "shift", "i")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "shift", "m")


    # ======== GetSomething ===========================================
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def get_text(self, locator):        
        try:
            element = self.find_element(locator)
            return element.text
        except:
            self.scroll_to_top()
            element = self.find_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
            return element.text
        
    def get_text_by_dom(self, element):
        '''
            回傳element的text ， 參數element為webdriver.find_element的回傳值
        '''
        try:
            return element.text
        except:
            self.scroll_to_top()
            self.sleep(1)
            ActionChains(self.driver).move_to_element(element).perform()
            return element.text

    def get_display(self, locator):
        return self.find_element(locator).is_displayed()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    # ======== Alert & Frame ==========================================

    def sendkey_alert(self, string):
        Alert(self.driver).send_keys(string)

    # def switchAlert(self):
    #     Alert(self.driver).switch_to.alert()

    def accept_alert(self):
        Alert(self.driver).accept()

    def dismiss_alert(self):
        Alert(self.driver).dismiss()

    def get_alert_message(self):
        return Alert(self.driver).text

    def switch_frame(self, locator):
        # self.driver.switch_to.frame(locator)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_default_frame(self):
        self.driver.switch_to.default_content()

    def switch_window(self, target_window):
        self.driver.switch_to.window(target_window)
    
    def switch_last_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_home_page (self):
        if len(self.driver.window_handles) > 1:
            if len(self.driver.window_handles) > 0:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

    def open_new_window(self, locator):
        original_windows = self.driver.current_window_handle
        el = self.find_element(locator)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def open_wait_new_window(self, locator):
        current_handle = self.driver.window_handles
        self.click(locator)
        self.wait_window_opened(current_handle)
        self.switch_window(self.driver.window_handles[-1])

    def page_name(self):
        return self.driver.window_handles
        
    # ======== Others =================================================
    def get_page_source(self):
        return self.driver.page_source

    def execute_js(self, script):
        self.driver.execute_script(script)

    def test_skip(self, *args):
        print(*args)
        return self.test_skip_method(self, *args)

    def get_us_time(self):
        us = (datetime.datetime.now() - datetime.timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")
        time = datetime.datetime.strptime(us, "%Y-%m-%d %H:%M:%S")
        return time

    def image_search(self, path, precision): # 圖形辨識
        return pyautogui.locateCenterOnScreen(path, confidence=precision)  # 精準度最高為1

    def font(self, language, text):
        return OpenCC(language).convert(text)
    
    def windows_to_top(self, full=True):
        if full:
            width, height = pyautogui.size()
        else:
            width, height = 300, 1000
        self.driver.set_window_size(width, height)
        self.driver.set_window_position(0, 0)

    def hide_windows(self):
        width, height = pyautogui.size()
        self.driver.set_window_size(1, 1)
        self.driver.set_window_position(width, height)
    
    def mouse_click(self, x, y, round):
        for _ in range(round):
            self.sleep(0.5)
            pyautogui.leftClick(x, y)


    def set_attribute(self, locator, key, value):
        xpath = self.driver.find_element_by_xpath(locator[1])
        self.driver.execute_script(f"arguments[0].setAttribute({key}, {value}", xpath)

    def get_location(self, locator):
        el = self.find_element(locator)
        return el.location

    def get_verification_code_from_mail(self):
        """
        從 Gmail 收件匣獲取第一封未讀驗證碼郵件並回傳驗證碼
        條件: 寄件人包含 'GuChat' 且主旨包含 'GuChat'
        """
        imap_server = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(imap_server)

        account = "york_tu@tengyuntech.com"
        pw = "rhzt lzqi xqnz pdsf"

        try:
            # 登入 Gmail
            mail.login(account, pw)
            mail.select("inbox")

            # 搜尋未讀信件
            status, data = mail.search(None, '(UNSEEN FROM "GuChat" SUBJECT "GuChat")')
            mail_ids = data[0].split()

            if not mail_ids:
                return None  # 沒有符合的信件

            # 取最新一封
            latest_email_id = mail_ids[0]
            status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            # 取郵件內容
            email_content = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        email_content = part.get_payload(decode=True).decode()
                        break
            else:
                email_content = msg.get_payload(decode=True).decode()

            clean_text = re.sub(r"<.*?>", "", email_content)  # 去掉所有 HTML 標籤
            match = re.search(r"验证码：\s*(\d{6})", clean_text)

            if match:
                code = match.group(1)
                return code
            else:
                return None

        finally:
            mail.logout()
