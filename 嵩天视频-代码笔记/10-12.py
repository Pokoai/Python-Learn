import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username 


def get_new_username():
    """提示用户输入用户名"""
    username = input("请输入用户名：")
    filename = "username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def if_new_user():
    print("")


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("你是 " + username + " 吗？")
        str = input("Y/N: ")
        if str == 'Y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print(username + ", Welcome to my site!")
    else:
        username = get_new_username()
        print(username + ", Welcome to my site!")

greet_user()