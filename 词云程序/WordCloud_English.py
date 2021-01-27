#WordCloud_English.py
import wordcloud
from scipy.misc import imread
mk = imread("pic.png")
f = open("Hamlet.txt", "r")
txt = f.read()
f.close()
w = wordcloud.WordCloud(width=1000,\
    height=700, font_path="msyh.ttc",\
    background_color="white", mask=mk)
w.generate(txt)
w.to_file("wordcloud_e.png")

