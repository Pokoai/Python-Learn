import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化属性"""
        self.num_points = num_points

        #存储坐标x,y,初始化（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步的所有坐标"""

        #一直循环，直到达到随机点数
        while len(self.x_values) < self.num_points:
            #计算x坐标增量
            x_direction = choice([-1,1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            #计算y坐标增量
            y_direction = choice([-1,1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #x,y下一步坐标
            next_x = x_step + self.x_values[-1]
            next_y = y_step + self.y_values[-1]

            #更新x,y最新坐标
            self.x_values.append(next_x)
            self.y_values.append(next_y)


def draw_plot(x_values, y_values):
    """绘制折线图"""

    #设置绘图窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(x_values, y_values, linewidth=0.5)

    #重新绘制起点、终点
    #plt.plot(0, 0, c='green', edgecolors='none')
    #plt.plot(x_values[-1], y_values[-1], c='red', edgecolors='none')

    #设置标题,x、y的标签
    #plt.title("RandomWalk", fontsize=24)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()


rw = RandomWalk(5000)
rw.fill_walk()
draw_plot(rw.x_values, rw.y_values)
  