import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """读取首行，看哪些列是自己所需要的，后面再去读取每行并提取该列的信息"""
    # #print(header_row)
    # #for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows,  temp_diffs= [], [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = eval(row[1])
            low = eval(row[3])
            temp_diff = high - low
        except SyntaxError:
            print(date, "missing data")
        else:
            dates.append(date)           
            highs.append(high)            
            lows.append(low)           
            temp_diffs.append(temp_diff)

    #print(highs)

#设置绘图窗口尺寸
fig = plt.figure(dpi=128, figsize=(16, 12))     #(10. 6)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.plot(dates, temp_diffs, c='purple')
#填充颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

#设置图标标题，并给坐标轴加上标签
plt.title("Daily high and low temerature", fontsize=24)
plt.xlabel("", fontsize=16)
#绘制斜的x标签
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)

#设置刻度标记的大小
plt.tick_params(axis='both', which= 'major', labelsize=16)

plt.show()