import traceback

# Initialize the global dictionary at import time so it always exists,
# even if _init() is never called explicitly.
_global_dict = {}


def _init():
    """Explicitly (re)initialize the global dictionary."""
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
    except KeyError:
        return def_value
