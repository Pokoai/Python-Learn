import requests, bs4

url = 'https://mp.weixin.qq.com/s/Z2YJQHLdtF1utOkbWk4NLQ'

# 下载网页
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as res:
    print('异常：' % (res) )

# 写入文件
with open('./source/web_cotent.html', 'wb') as f_obj:
    for chunk in res.iter_content(10000):
        f_obj.write(chunk)

print('网页下载完成！')

# 解析html
with open('./source/web_cotent.html', encoding='utf-8') as file:
    soup = bs4.BeautifulSoup(file.read())
    elems = soup.select('#qqmusic_main_109625844_0')
    print(len(elems))
