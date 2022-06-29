#! python3
# pw.py - An insecure password locker program.

import sys
import pyperclip

# 存储账户名和密码的字典结构
PASSWORDS = {'email': 'faf94rhkfef0923jr',
             'blog': 'fkf9834ihrfjsadgrf'}

# 命令行参数：1：python，2：程序名，3：账户名
if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

# 命令行第二个参数为账户
account = sys.argv[1]
# 检查账户名是否存在
if account in PASSWORDS:
    # 将密码粘贴到剪贴板里
    pyperclip.copy(PASSWORDS[account])
    pyperclip.paste()
    print(account + " 账户密码已拷贝至剪贴板")
else:
    print("没有找到账户：" + account)


