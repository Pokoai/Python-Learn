#! python
# 读取命令行参数或剪贴板获取地址，然后使用 Google 地图进行搜索

import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.copy()

url = 'https://map.baidu.com/poi/' + address
webbrowser.open(url)