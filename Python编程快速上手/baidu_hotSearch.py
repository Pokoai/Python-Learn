#! python
# baidu_hotSearch - 打开百度热搜所有标签页

import requests, bs4, webbrowser

print("Googling...")

# 获取网页
url = 'https://top.baidu.com/board'
res = requests.get(url)
res.raise_for_status()

# with open('./source/temp2.html', 'wb') as f:
#     for chunk in res.iter_content(10000):
#         f.write(chunk)

# 提取热搜链接
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.item-wrap_2oCLZ ')

# numOpen = min(5, len(linkElems))
numOpen = len(linkElems)
for i in range(numOpen):
    # print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))

