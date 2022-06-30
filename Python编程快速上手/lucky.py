#! python
# lucky.py - 打开Google关键词搜索结果的标签页

import requests, bs4, webbrowser, sys

# 获取命令行参数，进而取得查询结果页面
print("Googling...")

url = 'https://arctee.cn/?s=' + '+'.join(sys.argv[1:])
# print(url)
res = requests.get(url)
res.raise_for_status()

with open('./source/temp.txt', 'wb') as f:
    for chunk in res.iter_content(10000):
        f.write(chunk)

# 提取排名靠前的页面链接
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.title a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))

