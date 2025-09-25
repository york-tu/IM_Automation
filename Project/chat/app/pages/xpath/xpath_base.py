import common.utils.globalvar as gl

class Xpath_Base:
    def __init__(self):
        self.device_os = gl.get_value('PHONE_PLATFORM')

    def check_device(self, Android, iOS):
        if self.device_os == 'Android':
            return Android
        elif self.device_os == 'iOS':
            return iOS

    def data_collation(self, type_kind='', type_name='', action='', num='', times=1, pos='', parent=None, child=None):
        data = {
            'type_kind': type_kind,
            'type_name': type_name,
            'action': action,
            'num': num,
            'times': times,
            'pos': pos,
            'parent': parent,  # e.g. {'type_kind': 'name', 'type_name': 'Cell', 'num': 0}
            'child': child  # e.g. {'type_kind': 'name', 'type_name': 'chatList_chatCell_lastMessage_label'}
        }

        return data