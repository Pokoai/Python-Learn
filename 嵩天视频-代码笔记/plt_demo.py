"""1.matplot绘制折线图"""
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16 ,25]

#设置绘图窗口尺寸
plt.figure(dpi=128, figsize=(10, 6))
plt.plot(input_values, squares, linewidth=5)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of value", fontsize=16)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


"""2.matplot绘制散点图"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置每个坐标的取值范围
plt.axis = [0, 1100, 0, 1100000]

#plt.tick_params(axis='both', which='major', labelsize=14)

#plt.savefig("square.png")
plt.show()


"""3.pygal绘制直方图"""
import pygal

def draw_pygal(output_value):
    """用pygal绘制直方图"""

    hist = pygal.Bar()

    hist.title = "Result of rolling one  D6 1000 times"
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = [x for x in range(1, 7)]
    hist.x_title = "Result"
    hist.y_title = "Frequencies of Result"

    hist.add("D6", output_value)
    hist.render_to_file('die1_visual.svg')


"""4.pygal绘制折线图"""
import pygal

# x轴标签顺时针旋转20°，不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) 
#line_chart = pygal.Bar()
line_chart.title = '收盘价（元）'

line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]

line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图.svg')



