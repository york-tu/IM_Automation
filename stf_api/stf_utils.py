import stf_api.stf as stf

def get_unuse_phone_serial(specific_os_version):
    second_ready_phone = []
    third_ready_phone = []
    phone_serial = None, None, None, None, None, None
    phone_infos = stf.get_phone_list()
    for phone_info in phone_infos:
        if phone_info['using'] == False and phone_info['ready'] == True and phone_info['present'] == True: # 當手機未使用中、已準備好且在線
            if 'notes' not in phone_info:
                phone_info['notes'] = None
            phone_serial = phone_info['platform'], phone_info['serial'], phone_info['manufacturer'], phone_info['marketName'], phone_info['notes'], phone_info['version']
            phone_info['version'] = phone_info['version'].split('.')[0]
            if 'QA' in phone_info['notes'] and phone_info['version'] in specific_os_version: # 優先回傳符合註解和版本的測試專用機資訊
                return phone_serial
            elif phone_info['version'] in specific_os_version:  # 暫存指定版本的測試專用機資訊
                second_ready_phone.append(phone_serial)
            elif 'QA' in phone_info['notes']:  # 暫存符合註解的測試專用機資訊
                third_ready_phone.append(phone_serial)
    
    if second_ready_phone != []:
        return second_ready_phone[0]
    elif third_ready_phone != []:
        return third_ready_phone[0]
    else:
        return phone_serial

def get_specific_phone_serial(phone_name):
    phone_serial = None, None, None, None, None, None
    phone_infos = stf.get_phone_list()
    for phone_info in phone_infos:
        if phone_info['using'] == False and phone_info['ready'] == True and phone_info['present'] == True: # 當手機未使用中、已準備好且在線
            if 'notes' in phone_info.keys() and phone_name in phone_info['notes']: # 比對是否為指定的手機
                phone_serial = phone_info['platform'], phone_info['serial'], phone_info['manufacturer'], phone_info['marketName'], phone_info['notes'], phone_info['version']
                break
            
    return phone_serial