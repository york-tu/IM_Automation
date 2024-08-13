import os
import sys
DIR_NAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_NAME)
class Functions:
    def __init__(self, skip_test_method=''):
        self.pages_parameter = skip_test_method

    def ui_admin_deposit_management(self):
        from function_layer.uiapi.admin.financial_management.deposit_management import DepositManagement
        return DepositManagement()

    def ui_admin_withdraw_management(self):
        from function_layer.uiapi.admin.financial_management.withdraw_management import WithdrawManagement
        return WithdrawManagement()
    
    def ui_paybox_casher_tool(self):
        from function_layer.uiapi.paybox.casher_tool import CasherTool
        return CasherTool()