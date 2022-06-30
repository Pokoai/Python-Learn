#! python
# download_website.py - 下载XKCD网站所有漫画图片，离线阅读

import requests, bs4, os

# 新建存储图片的文件夹
os.makedirs('./source/xkcd', exist_ok=True)

url = 'https://xkcd.com/'
while not url.endswith('#'):
    # 下载页面
    print("正在下载页面：%s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    # 解析页面，获取漫画图片链接
    soup = bs4.BeautifulSoup(res.text)
    comicElems = soup.select('#comic img')
    if comicElems == []:
        print("没有找到图片")
    else:
        comicUrl = 'https:' + comicElems[0].get('src')

        # 下载图片，即将图片数据写入文件中
        print("正在下载图片 %s..." % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        filePath = os.path.join('./source/xkcd', os.path.basename(comicUrl))
        print('文件存储路径：' + filePath)
        imageFile = open(filePath, 'wb')
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()

    # 获取前一个页面链接，并更新 url
    prevLink = soup.select('a[rel="prev"]')[0].get('href')
    url = 'https://xkcd.com' + prevLink
    print('新页面链接：' + url)

print('Done.')





