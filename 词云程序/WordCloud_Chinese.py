#WordCloud_Chinese.py
import wordcloud
from scipy.misc import imread
mk = imread("pic.png")
import jieba
f = open("电气学院生产实习报告.txt", "r")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000,\
    height=700, font_path="msyh.ttc",\
    background_color="white", mask=mk)
w.generate(txt)
w.to_file("wordcloud_c.png")


