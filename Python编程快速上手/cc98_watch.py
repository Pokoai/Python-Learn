#!python
# cc98_watch.py - 监测跳蚤市场，一旦出现’显示器‘关键词则发邮件提醒

# import requests, bs4
import time

from selenium import webdriver
import datetime

# 打开网页
browser = webdriver.Chrome("D:\Software\chromedriver.exe")
browser.get('https://www.cc98.org/board/562')
time.sleep(2)

# 进入登录页面
# loginElem = browser.find_element_by_link_text('点我登录')
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/a').click()

# 输入账户名和密码并登录
nameElem = browser.find_element_by_name('username').send_keys('xxx')
# browser.find_element_by_xpath('//*[@id="loginName"]').send_keys('xxx')
passwordElem = browser.find_element_by_name('password')
# passwordElem = browser.find_element_by_xpath('//*[@id="loginPassword"]')
passwordElem.send_keys('xxxx')
passwordElem.submit()
time.sleep(2)

# 返回首页
backElem = browser.find_element_by_link_text("返回首页")
backElem.click()

# 打开数码市场
marketElem = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/a')
marketElem.click()
time.sleep(2)

# 解析文本
# textElems = browser.find_element_by_tag_name('a')
# textElemElem = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[4]/div[11]/div[2]/a')
# textElems = browser.find_elements_by_partial_link_text("[出]")
textElems = browser.find_elements_by_tag_name('a')

for i in range(len(textElems)):
    print(textElems[i].text)

print('Done!')





