import re

from airtest.core.api import *
# import ast,logging
import common.utils.globalvar as gl
from poco.drivers.ios import iosPoco
from airtest.core.api import touch, swipe, text
import imaplib
import email

class Common(object):
    type_kind = ''
    type_name = ''
    action = ''
    pos = ''
    times = 1
    num = 0

    # ios_poco=iosPoco()

    def __init__(self, poco='', wda_service='', skip_test_method=''):
        self.poco_ui = poco
        self.skip_test_method = skip_test_method
        self.wda = wda_service
        self.device = gl.get_value('PHONE_PLATFORM')

    def mappin_value(self, data):
        for key, value in data.items():
            if key == 'type_kind':
                self.type_kind = value
                continue
            if key == 'type_name':
                self.type_name = value
                continue
            if key == 'action':
                self.action = value
                continue
            if key == 'num' and value != '':
                self.num = value
                continue
            if key == 'pos':
                self.pos = value
                continue
            if key == 'times' and value != '':
                self.times = value
                continue

    def dict_click(self, data):
        el = self.poco(self.type_kind, self.type_name, self.num)
        el.click()

    def find_app(self, package_name):
        stop_app(package_name)
        start_app(package_name)


    def clear_app(self, package_name):
        if self.device.lower() == 'android':
            clear_app(package_name)
        else:
            stop_app(package_name)

    def stop_app(self, package_name):
        stop_app(package_name)
        self.sleep(3)

    # 頁面滑到最上方
    def go_top(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.5, 0.3], [0.5, 1], duration=0.05)
        else:
            self.wda.swipe(0.5, 0.3, 0.5, 1.0, duration=0.1)

    # 頁面滑到最下方
    def go_bottom(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.5, 0.7], [0.5, 0], duration=0.05)
        else:
            self.wda.swipe(0.5, 0.7, 1.0, 0, duration=0.1)

    # 頁面往下滑
    def go_down(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.5, 0.7], [0.5, 0.5], duration=0.1)
        else:
            self.wda.swipe(0.5, 0.7, 0.6, 0.4, duration=0.1)

    # 頁面往上滑
    def go_up(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.5, 0.4], [0.5, 0.6], duration=0.1)
        else:
            self.wda.swipe(0.5, 0.4, 0.4, 0.6, duration=0.1)

    # 頁面往左滑
    def go_left(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.8, 0.5], [0.6, 0.5])
        else:
            self.wda.swipe(0.8, 0.5, 0.6, 0.5, duration=0.1)

    # 頁面往右滑
    def go_right(self):
        if self.device.lower() == 'android':
            self.poco_ui.swipe([0.6, 0.5], [0.8, 0.5])
        else:
            self.wda.swipe(0.6, 0.5, 0.8, 0.5, duration=0.1)

    def sleep(self, sec):
        sleep(float(sec))

    def swipe(self, data):
        self.mappin_value(data)

        if self.device.lower() == 'android':
            self.poco_ui.swipe([self.pos[0], self.pos[1]], [self.pos[2], self.pos[3]])
        else:
            self.wda.swipe(*self.pos, duration=0.1)

    def swipe_speed(self, data, duration):
        self.mappin_value(data)

        if self.device.lower() == 'android':
            self.poco_ui.swipe([self.pos[0], self.pos[1]], [self.pos[2], self.pos[3]], duration=duration)
        else:
            self.wda.swipe(*self.pos, duration=duration)

    def touch_image(self, pos):
        touch(Template(pos))

    def touch_point(self, coordinate, times=1):
        touch(coordinate, times=times)

    def wait_touch(self, pos, timeout=10):
        wait(Template(pos), timeout=timeout)
        touch(Template(pos))

    def exists_image(self, pos):
        try:
            wait(Template(pos), timeout=1)
            return True
        except:
            return False

    def wait_image(self, pos, timeout=10):
        try:
            wait(Template(pos), timeout=timeout)
            return True
        except:
            return False

    def wait_image_swipe(self, pos, vector=[0, 0], timeout=10):
        wait(Template(pos), timeout=timeout)
        swipe(Template(pos), vector=vector)

    def len_poco(self, data):
        el = self.poco(data)
        if self.action == '':
            return len(el)
        else:
            return eval(f'len(el.{self.action})')

    def poco(self, data):
        self.mappin_value(data)
        if data['num'] == '':
            if self.type_kind == 'nameMatches':
                return self.poco_ui(nameMatches=self.type_name)
            if self.type_kind == 'text':
                return self.poco_ui(text=self.type_name)
            if self.type_kind == 'name':
                return self.poco_ui(name=self.type_name)
            if self.type_kind == 'desc':
                return self.poco_ui(desc=self.type_name)
            if self.type_kind == 'textMatches':
                return self.poco_ui(textMatches=self.type_name)
            if self.type_kind == 'type':
                return self.poco_ui(type=self.type_name)
            if self.type_kind == 'value':
                return self.poco_ui(value=self.type_name)
        else:
            if self.type_kind == 'nameMatches':
                return self.poco_ui(nameMatches=self.type_name)[self.num]
            if self.type_kind == 'text':
                return self.poco_ui(text=self.type_name)[self.num]
            if self.type_kind == 'name':
                return self.poco_ui(name=self.type_name)[self.num]
            if self.type_kind == 'textMatches':
                return self.poco_ui(textMatches=self.type_name)[self.num]
            if self.type_kind == 'type':
                return self.poco_ui(type=self.type_name)[self.num]
            if self.type_kind == 'value':
                return self.poco_ui(value=self.type_name)[self.num]

    # def more_poco(self, data):
    #     if self.type_kind == 'nameMatches':
    #         return self.poco_ui(nameMatches = self.type_name)[self.num]
    #     if self.type_kind == 'text':
    #         return self.poco_ui(text = self.type_name)[self.num]
    #     if self.type_kind == 'name':
    #         return self.poco_ui(name = self.type_name)[self.num]
    #     if self.type_kind == 'textMatches':
    #         return self.poco_ui(textMatches = self.type_name)[self.num]

    def poco_send_text(self, data, _text):
        el = self.poco(data)

        if self.device.lower() == 'android':
            if self.action == '':
                el.set_text(_text)
                return
            else:
                eval(f'el.{self.action}').set_text(_text)
                return

        if self.device.lower() == 'ios':
            # el.click()
            # ===== 判斷是否為全數字 >>> ios會跳出純數字鍵盤 =================================================================
            if str(_text).isdigit() is True and len(str(_text)) > 4:
                key_coordinates = {
                    '1': [0.16545893719806765, 0.6958705357142857],  # 这是示例坐标，请根据实际情况调整
                    '2': [0.5, 0.6958705357142857],
                    '3': [0.8345410628019324, 0.6958705357142857],
                    '4': [0.16545893719806765, 0.7589285714285714],
                    '5': [0.5, 0.7589285714285714],
                    '6': [0.8345410628019324, 0.7589285714285714],
                    '7': [0.16545893719806765, 0.8214285714285714],
                    '8': [0.5, 0.8214285714285714],
                    '9': [0.8345410628019324, 0.8214285714285714],
                    '0': [0.5, 0.8844866071428571]
                }
                for char in str(_text):
                    if char in key_coordinates:
                        touch(key_coordinates[char])
                    # time.sleep(0.1)
            else:
                text(_text, enter=False)

    # def more_poco_send_text(self, type_kind, type_name, num, text):
    #     el = self.more_poco(type_kind, type_name, num)
    #     el.set_text(text)

    def poco_get_attr(self, data, ele):
        el = self.poco(data)
        if self.action == '':
            return el.attr(ele)
        try:
            return eval(f'el.{self.action}.attr({ele})')  # 如果el不存在，這行會丟error
        except:
            return False

    def poco_click(self, data, times=1):
        data['times'] = times
        el = self.poco(data)

        if self.action == '':
            if self.pos == '':
                for _ in range(0, self.times):
                    el.click()
            else:
                for _ in range(0, self.times):
                    self.poco_ui.click(self.pos)
        else:
            for _ in range(0, self.times):
                eval(f'el.{self.action}.click()')

    # def more_poco_click(self, type_kind='', type_name='', action='', pos='', times=1, num=0):
    #     if type(action) == int:
    #         num = action

    #     el = self.more_poco(type_kind, type_name, num)

    #     if action == '' or type(action) == int:
    #         if pos == '':
    #             for _ in range(0, times):
    #                 el.click()
    #         else:
    #             for _ in range(0, times):
    #                 self.poco_ui.click(pos)
    #     else:
    #         for _ in range(0, times):
    #             eval(f'el.{action}[{num}].click()')

    def poco_exists(self, data):
        el = self.poco(data)

        if self.action == '':
            return el.exists()
        try:
            return eval(f'el.{self.action}.exists()')  # 如果el不存在，這行會丟error
        except:
            return False

    def poco_wait_exists(self, data, timeout=10):
        el = self.poco(data)
        result = el.wait(timeout).exists()
        if self.action == '':
            return result
        try:
            return eval(f'el.{self.action}.exists()')  # 如果el不存在，這行會丟error
        except:
            return False

    # def more_poco_exists(self, type_kind, type_name, num=0):
    #     try:
    #         el = self.more_poco(type_kind, type_name, num)
    #         return el.exists()
    #     except:
    #         return False

    def poco_position(self, data):
        el = self.poco(data)
        return el.get_position()

    # def more_poco_position(self, type_kind, type_name, num):
    #     el = self.more_poco(type_kind, type_name, num)
    #     return el.get_position()

    def poco_focus_swipe(self, data, a, b):
        el = self.poco(data)
        el.focus(a).swipe(b)

    # def more_poco_focus_swipe(self, type_kind, type_name, num,a,b):
    #     el = self.more_poco(type_kind, type_name, num)
    #     el.focus(a).swipe(b)

    def poco_get_text(self, data):
        el = self.poco(data)
        el_text = ''
        # 取文字
        if self.device.lower() == 'ios':
            el_text = el.attr("label") or el.attr("value") or ""

        if self.device.lower() == 'android':
            if self.action == '':
                el_text = eval(f'el.get_text()')
            else:
                el_text = eval(f'el.{self.action}.get_text()')
        return el_text

    # def more_poco_get_text(self, type_kind, type_name, action='', num='0'):
    #     el = self.poco(type_kind, type_name)
    #     if action == '':
    #         return el[num].get_text()
    #     else:
    #         return eval(f'el.{action}[{num}].get_text()')

    def skip_test(self, *args):
        print(args[0])
        return self.skip_test_method(self, *args)

    def poco_get_name(self, data):
        el = self.poco(data)
        return el.get_name()

    def poco_wait_appearance(self, data):
        try:
            el = self.poco(data)
            el.wait_for_appearance(timeout=10)
            return True
        except:
            return False

    def poco_wait_disappearance(self, data):
        try:
            el = self.poco(data)
            el.wait_for_disappearance(timeout=10)
            return True
        except:
            return False

    def poco_long_click(self, data, time=''):
        el = self.poco(data)
        if time == '':
            el.long_click(duration=1)
        else:
            el.long_click(duration=time)

    # 蘋果支持的keycode很少，https://cloud.tencent.com/developer/article/1838973
    def keyevent(self, keycode):
        keyevent(keycode)

    # airtest原生的輸入func，因ios設備不支援poco的set_text
    def airtest_send_text(self, text_value, enter=True, action=''):
        if action == '':
            text(text_value, enter=True)
        else:
            eval(f'text(text_value, {action}, enter=enter)')

    ## iOS wda

    def wda_base(self, type_kind, type_name):
        if type_kind == 'name' or type_kind == 'text':
            return self.wda(name=type_name)

        if type_kind == 'nameMatches':
            return self.wda(nameMatches=type_name)

        if type_kind == 'label':
            return self.wda(label=type_name)

    # 從email中取得驗證碼
    def get_verification_code_from_mail(self, brand):
        """
        從 Gmail 收件匣獲取第一封未讀驗證碼郵件並回傳驗證碼
        條件: 寄件人包含 'GuChat' 且主旨包含 'GuChat'
        """
        imap_server = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(imap_server)

        account = "york_tu@tengyuntech.com"
        pw = "rhzt lzqi xqnz pdsf"
        mail_title = ''
        if brand == 'gu':
            mail_title = 'GuChat'
        elif brand == 'mingpin':
            mail_title = 'MingpinChat'
        elif brand == 'chit':
            mail_title = 'ChitChat'

        try:
            # 登入 Gmail
            mail.login(account, pw)
            mail.select("inbox")

            # 搜尋未讀信件
            status, data = mail.search(None, f'(UNSEEN FROM "{mail_title}" SUBJECT "{mail_title}")')
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
