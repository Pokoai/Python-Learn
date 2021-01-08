import json
import pygal
import math
from itertools import groupby

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期、收盘价等数据
dates = []
months = []
weeks = []
weekdays = []
close = []  
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(eval(btc_dict['close']))


# x轴标签顺时针旋转20°，不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) 
line_chart.title = '收盘价（元）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图.svg')


# x轴标签顺时针旋转20°，不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) 
# line_chart = pygal.Bar()
line_chart.title = '收盘价对数变换（元）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')


def draw_line(x_data, y_data, title, y_legend):
    """数据分组后计算均值"""

    xy_map = []
    # 将x轴与y轴的数据合并、排序，再用groupby分组
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        # 求出每组均值，并存储到xy_map中
        xy_map.append([x, sum(y_list) / len(y_list)])
    # 分离x轴与y轴数据
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], '收盘价月日均值（元）', '月日均值')


idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], '收盘价周日均值（元）', '周日均值')


idx_week = dates.index('2017-12-11')
# 将weekdays内容替换成1~7的整数，从而顺序显示
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [(wd.index(w) + 1) for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], '收盘价星期均值（元）', '星期均值')
#将x轴标签1~7替换为中文
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（元）.svg')


# 创建一个网页，作为数据仪表盘（Dashboard），来显示所有图表
with open('收盘价Dashboard.html', 'w', encoding = 'utf-8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图.svg', '收盘价对数变换折线图.svg', '收盘价月日均值（元）.svg', 
            '收盘价周日均值（元）.svg', '收盘价星期均值（元）.svg'
    ]:
        html_file.write(
            '   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')