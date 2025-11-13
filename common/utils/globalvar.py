import traceback
def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value
    # print(f"[DEBUG] gl.set_value({name}, {value})")
    # if name == 'PHONE_NAME':
    #     print("⚠️ PHONE_NAME was just changed! Here's who did it:")
    #     traceback.print_stack(limit=4)

def get_value(name, def_value=None):
    try:
        return _global_dict[name]
    except:
        return def_value
