def build_profile(first, last, **info):
    my_info = {}
    my_info['first_name'] = first
    my_info['last_name'] = last
    
    for k, v in info.items():
        my_info[k] = v
    return my_info

info = build_profile('hu', 'min', age = 23, field = 'automation')
print(info)
