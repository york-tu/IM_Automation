import re
import os
import imaplib
import email
import time
import json

from airtest.core.api import *
from poco.drivers.ios import iosPoco
from poco.exceptions import PocoNoSuchNodeException
from airtest.core.api import touch, swipe, text
import common.utils.globalvar as gl

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

    def map_value(self, data):
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
        self.map_value(data)

        if self.device.lower() == 'android':
            self.poco_ui.swipe([self.pos[0], self.pos[1]], [self.pos[2], self.pos[3]])
        else:
            self.wda.swipe(*self.pos, duration=0.1)

    def swipe_speed(self, data, duration):
        self.map_value(data)

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
        except Exception:
            return False

    def wait_image(self, pos, timeout=10):
        # iOS 優化：針對 iOS 使用更短的超時時間
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        try:
            wait(Template(pos), timeout=timeout)
            return True
        except Exception:
            return False

    def wait_image_swipe(self, pos, vector=[0, 0], timeout=10):
        # iOS 優化：針對 iOS 使用更短的超時時間
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        wait(Template(pos), timeout=timeout)
        swipe(Template(pos), vector=vector)

    def len_poco(self, data):
        el = self.poco(data)
        if self.action == '':
            return len(el)
        else:
            attr = getattr(el, self.action, None)
            return len(attr) if attr is not None else 0

    def poco(self, data):
        self.map_value(data)
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
        # 先解析 data 參數，獲取 type_kind 和 type_name（用於 WDA）
        self.map_value(data)
        el = self.poco(data)

        if self.device.lower() == 'android':
            if self.action == '':
                el.set_text(_text)
                return
            else:
                attr = getattr(el, self.action, None)
                if attr is not None:
                    attr.set_text(_text)
                return

        if self.device.lower() == 'ios':
            # iOS 優化：優先嘗試使用 WDA 的 set_text（最快的方式，適用於所有文字輸入）
            wda_success = False
            if self.wda:
                try:
                    # 嘗試使用 WDA 直接設置文字
                    wda_element = self.wda_base(self.type_kind, self.type_name)
                    if wda_element:
                        # WDA 返回的可能是列表或單個元素
                        if isinstance(wda_element, list) and len(wda_element) > 0:
                            element = wda_element[0]
                        elif not isinstance(wda_element, list):
                            element = wda_element
                        else:
                            raise Exception("WDA element not found")
                        
                        # 使用 WDA 的 set_text 方法
                        element.set_text(str(_text))
                        sleep(0.1)  # 短暫等待確認輸入完成
                        wda_success = True
                except Exception as e:
                    # WDA set_text 失敗，回退到原有方式
                    wda_success = False
            
            # 如果 WDA set_text 失敗，使用回退方式
            if not wda_success:
                # ===== ?斗?臬?箏?詨? >>> ios?歲?箇??詨??萇 =================================================================
                if str(_text).isdigit() is True and len(str(_text)) > 4:
                    # 數字輸入：使用座標點擊方式
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
                    # iOS 優化：減少 touch duration，加快輸入速度
                    for char in str(_text):
                        if char in key_coordinates:
                            touch(key_coordinates[char], duration=0.01)  # 減少 touch duration
                else:
                    # 一般文字輸入：使用 airtest 的 text() 函數
                    text(_text, enter=False)

    # def more_poco_send_text(self, type_kind, type_name, num, text):
    #     el = self.more_poco(type_kind, type_name, num)
    #     el.set_text(text)

    def poco_get_attr(self, data, ele):
        el = self.poco(data)
        if self.action == '':
            return el.attr(ele)
        try:
            attr = getattr(el, self.action, None)
            if attr is not None:
                return attr.attr(ele)
            return False
        except (AttributeError, TypeError):
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
            attr = getattr(el, self.action, None)
            if attr is not None:
                for _ in range(0, self.times):
                    attr.click()

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
        try:
            el = self.poco(data)
        except PocoNoSuchNodeException:
            # 元素不存在時返回 False
            return False

        if self.action == '':
            return el.exists()
        try:
            attr = getattr(el, self.action, None)
            if attr is not None:
                return attr.exists()
            return False
        except (AttributeError, TypeError, PocoNoSuchNodeException):
            return False
    
    def poco_batch_exists(self, data_list):
        """
        批量檢查多個元素是否存在（一次性獲取 UI 樹，減少 HTTP 請求）
        
        Args:
            data_list: 元素定位器列表，例如 [locator1, locator2, ...]
        
        Returns:
            dict: {locator: exists_result} 的字典
        """
        # #region agent log
        import json
        try:
            with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "A",
                    "location": "common/app/common.py:poco_batch_exists:322",
                    "message": "Function entry - data_list type and content",
                    "data": {
                        "data_list_type": str(type(data_list)),
                        "data_list_len": len(data_list) if data_list else 0,
                        "first_item_type": str(type(data_list[0])) if data_list else None,
                        "first_item_is_dict": isinstance(data_list[0], dict) if data_list else None
                    },
                    "timestamp": int(time.time() * 1000)
                }) + '\n')
        except: pass
        # #endregion
        
        # 使用 id(data) 作為鍵，同時維護映射關係
        results = {}
        locator_to_id = {}  # 映射：原始 locator -> id
        
        # #region agent log
        try:
            with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "B",
                    "location": "common/app/common.py:poco_batch_exists:after_mapping",
                    "message": "Creating locator mapping",
                    "data": {
                        "mapping_created": True
                    },
                    "timestamp": int(time.time() * 1000)
                }) + '\n')
        except: pass
        # #endregion
        
        # iOS 優化：一次性獲取 UI 樹，然後批量檢查
        if self.device.lower() == 'ios':
            # 先獲取一次 UI 樹（只請求一次）
            try:
                # 使用 poco 的批量查詢功能
                for idx, data in enumerate(data_list):
                    try:
                        # #region agent log
                        try:
                            with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                                f.write(json.dumps({
                                    "sessionId": "debug-session",
                                    "runId": "run1",
                                    "hypothesisId": "A",
                                    "location": "common/app/common.py:poco_batch_exists:loop",
                                    "message": "Processing locator in loop",
                                    "data": {
                                        "idx": idx,
                                        "data_type": str(type(data)),
                                        "data_is_dict": isinstance(data, dict),
                                        "data_id": id(data)
                                    },
                                    "timestamp": int(time.time() * 1000)
                                }) + '\n')
                        except: pass
                        # #endregion
                        
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        
                        el = self.poco(data)
                        if self.action == '':
                            results[locator_id] = el.exists()
                        else:
                            attr = getattr(el, self.action, None)
                            results[locator_id] = attr.exists() if attr is not None else False
                    except Exception as e:
                        # #region agent log
                        try:
                            with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                                f.write(json.dumps({
                                    "sessionId": "debug-session",
                                    "runId": "run1",
                                    "hypothesisId": "A",
                                    "location": "common/app/common.py:poco_batch_exists:except_inner",
                                    "message": "Exception in inner loop",
                                    "data": {
                                        "idx": idx,
                                        "error": str(e),
                                        "error_type": str(type(e))
                                    },
                                    "timestamp": int(time.time() * 1000)
                                }) + '\n')
                        except: pass
                        # #endregion
                        
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        results[locator_id] = False
            except Exception as e:
                # #region agent log
                try:
                    with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                        f.write(json.dumps({
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "A",
                            "location": "common/app/common.py:poco_batch_exists:except_outer",
                            "message": "Exception in outer try block",
                            "data": {
                                "error": str(e),
                                "error_type": str(type(e))
                            },
                            "timestamp": int(time.time() * 1000)
                        }) + '\n')
                except: pass
                # #endregion
                
                # 如果批量查詢失敗，回退到單個查詢
                for data in data_list:
                    try:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        results[locator_id] = self.poco_exists(data)
                    except:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        results[locator_id] = False
        else:
            # Android 直接批量查詢
            for data in data_list:
                try:
                    locator_id = id(data)
                    locator_to_id[data] = locator_id
                    results[locator_id] = self.poco_exists(data)
                except:
                    locator_id = id(data)
                    locator_to_id[data] = locator_id
                    results[locator_id] = False
        
        # 將結果轉換回使用原始 locator 作為鍵
        final_results = {}
        for locator, locator_id in locator_to_id.items():
            final_results[locator] = results.get(locator_id, False)
        
        # #region agent log
        try:
            with open(r'c:\automated_test_0219\.cursor\debug.log', 'a', encoding='utf-8') as f:
                f.write(json.dumps({
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "C",
                    "location": "common/app/common.py:poco_batch_exists:return",
                    "message": "Function exit - returning results",
                    "data": {
                        "final_results_keys_type": [str(type(k)) for k in final_results.keys()],
                        "final_results_len": len(final_results)
                    },
                    "timestamp": int(time.time() * 1000)
                }) + '\n')
        except: pass
        # #endregion
        
        return final_results
    
    def poco_batch_wait_exists(self, data_list, timeout=10, all_required=False):
        """
        批量等待多個元素出現（優化：減少 HTTP 請求次數）
        
        Args:
            data_list: 元素定位器列表
            timeout: 超時時間（秒）
            all_required: 是否所有元素都需要存在（True=全部存在才返回，False=任一存在即返回）
        
        Returns:
            dict: {locator: exists_result} 的字典
        """
        # iOS 優化：針對 iOS 使用更短的超時時間
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        results = {}
        start_time = time.time()
        
        # iOS 優化：使用輪詢方式，但減少請求頻率
        if self.device.lower() == 'ios':
            poll_interval = 0.3  # iOS 使用較短的輪詢間隔（減少等待時間）
        else:
            poll_interval = 0.5
        
        while time.time() - start_time < timeout:
            # 批量檢查所有元素
            batch_results = self.poco_batch_exists(data_list)
            results.update(batch_results)
            
            # 根據 all_required 判斷是否滿足條件
            if all_required:
                if all(results.values()):
                    return results
            else:
                if any(results.values()):
                    return results
            
            time.sleep(poll_interval)
        
        # 超時後返回最終結果
        return results
    
    def poco_get_multiple(self, data_list, attribute='text'):
        """
        批量獲取多個元素的屬性（一次性獲取 UI 樹，減少 HTTP 請求）
        
        Args:
            data_list: 元素定位器列表
            attribute: 要獲取的屬性名稱（'text', 'value', 'label' 等）
        
        Returns:
            dict: {locator: attribute_value} 的字典
        """
        # 使用 id(data) 作為鍵，同時維護映射關係
        results = {}
        locator_to_id = {}  # 映射：原始 locator -> id
        
        # iOS 優化：一次性獲取 UI 樹
        if self.device.lower() == 'ios':
            try:
                for data in data_list:
                    try:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        
                        el = self.poco(data)
                        if self.action == '':
                            if attribute == 'text':
                                results[locator_id] = el.attr("label") or el.attr("value") or ""
                            else:
                                results[locator_id] = el.attr(attribute) or ""
                        else:
                            attr = getattr(el, self.action, None)
                            if attr is not None:
                                if attribute == 'text':
                                    results[locator_id] = attr.attr("label") or attr.attr("value") or ""
                                else:
                                    results[locator_id] = attr.attr(attribute) or ""
                            else:
                                results[locator_id] = ""
                    except:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        results[locator_id] = ""
            except Exception as e:
                # 如果批量查詢失敗，回退到單個查詢
                for data in data_list:
                    try:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        if attribute == 'text':
                            results[locator_id] = self.poco_get_text(data)
                        else:
                            results[locator_id] = self.poco_get_attr(data, attribute)
                    except:
                        locator_id = id(data)
                        locator_to_id[data] = locator_id
                        results[locator_id] = ""
        else:
            # Android 批量查詢
            for data in data_list:
                try:
                    locator_id = id(data)
                    locator_to_id[data] = locator_id
                    if attribute == 'text':
                        results[locator_id] = self.poco_get_text(data)
                    else:
                        results[locator_id] = self.poco_get_attr(data, attribute)
                except:
                    locator_id = id(data)
                    locator_to_id[data] = locator_id
                    results[locator_id] = ""
        
        # 將結果轉換回使用原始 locator 作為鍵
        final_results = {}
        for locator, locator_id in locator_to_id.items():
            final_results[locator] = results.get(locator_id, "")
        
        return final_results

    def poco_wait_exists(self, data, timeout=10):
        # iOS 優化：針對 iOS 使用更短的超時時間（從 10 秒降到 5 秒）
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        el = self.poco(data)
        result = el.wait(timeout).exists()
        if self.action == '':
            return result
        try:
            attr = getattr(el, self.action, None)
            if attr is not None:
                return attr.exists()
            return False
        except (AttributeError, TypeError):
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
                el_text = el.get_text()
            else:
                attr = getattr(el, self.action, None)
                el_text = attr.get_text() if attr is not None else ''
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

    def poco_wait_appearance(self, data, timeout=10):
        # iOS 優化：針對 iOS 使用更短的超時時間
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        try:
            el = self.poco(data)
            el.wait_for_appearance(timeout=timeout)
            return True
        except Exception:
            return False

    def poco_wait_disappearance(self, data, timeout=10):
        # iOS 優化：針對 iOS 使用更短的超時時間
        if self.device.lower() == 'ios' and timeout == 10:
            timeout = 5
        
        try:
            el = self.poco(data)
            el.wait_for_disappearance(timeout=timeout)
            return True
        except Exception:
            return False

    def poco_long_click(self, data, time=''):
        el = self.poco(data)
        if time == '':
            # iOS 優化：減少默認長按 duration（從 1 秒降到 0.5 秒）
            if self.device.lower() == 'ios':
                el.long_click(duration=0.5)
            else:
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
            # Note: text() function doesn't support action parameter in standard airtest
            # This may need to be reviewed based on actual usage
            text(text_value, enter=enter)

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
        import os
        imap_server = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(imap_server)

        # Get credentials from environment variables or use defaults
        account = os.getenv('GMAIL_ACCOUNT', 'york_tu@tengyuntech.com')
        pw = os.getenv('GMAIL_PASSWORD', 'rhzt lzqi xqnz pdsf')
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
