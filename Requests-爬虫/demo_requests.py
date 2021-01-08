# 爬虫代码框架
import requests
url = "https://item.jd.com/32196615406.html"
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")


# 伪装成浏览器
import requests
url = ""
try:
    kv = {'user-agent': 'Chrome/15.0'}
    #r = requests.get(url)
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")


# 百度搜索全代码
import requests
keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s",  params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")    


# 图片/视频爬取全代码
import requests
import os
url = "https://api.test.zhengguo66.com/upload/images/2020/7/143623W7ioY.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
   print("图片爬取失败")



# IP地址查询全代码
import requests
url = "https://www.ip.cn/?ip="
try:
    r = requests.get(url + '112.19.127.226')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])  
except:
   print("爬取失败")



# 获取大学排名
import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[4].string])


def printUnivList(ulist, num):
    print("{:^5}\t{:^8}\t\t{:^8}\t{:^10}".format("排名", "学校名称", "省市", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^5}\t{:^8}\t\t{:^8}\t{:^10}".format(u[0], u[1], u[2], u[3]))

def main():
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html"
    uinfo = []
    html= getHtmlText(url)
    fillUnivList(uinfo, html)    
    printUnivList(uinfo, 20)

main()





# 淘宝商品比价定向爬虫
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[-1])
            title = eval(tlt[i].split(':')[-1])
            ilt.append([price, title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods  = '书包'
    infoList = []
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + 'goods'
    for i in range(depth):
        try:
            url = start_url + '$s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
            
