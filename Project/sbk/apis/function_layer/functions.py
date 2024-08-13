import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)

class Functions:
    def __init__(self, skip_test_method=''):
        self.pages_parameter = skip_test_method

    def ui_base_function(self):
        from function_layer.base_functions import BaseFunction
        return BaseFunction(self.pages_parameter)

    # def ui_caht_function(self):
    #     from function_layer.uiapi.display.chat_functions import ChatFunction
    #     return ChatFunction(self.pages_parameter)

    # def ui_friends_function(self):
    #     from function_layer.uiapi.display.friends_functions import FriendsFunction
    #     return FriendsFunction(self.pages_parameter)

    # def ui_redenvelopet_function(self):
    #     from function_layer.uiapi.admin.red_envelopet import RedEnvelopetFunction
    #     return RedEnvelopetFunction(self.pages_parameter)