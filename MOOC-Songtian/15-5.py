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

    def get_step(self):
        """获取随机漫步x或y的移动向量：方向、距离"""
          
        direction = choice([-1,1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
        
    def fill_walk(self):
        """计算随机漫步的所有坐标"""

        #一直循环，直到达到随机点数
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #x,y下一步坐标
            next_x = x_step + self.x_values[-1]
            next_y = y_step + self.y_values[-1]

            #更新x,y最新坐标
            self.x_values.append(next_x)
            self.y_values.append(next_y)


def draw_scatter(x_values, y_values):
    """绘制散点图"""

    #设置绘图窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.scatter(x_values, y_values, edgecolors='none', c=list(range(len(x_values))), cmap=plt.cm.Blues, s=1)

    #重新绘制起点、终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(x_values[-1], y_values[-1], c='red', edgecolors='none', s=100)

    #设置标题,x、y的标签
    #plt.title("RandomWalk", fontsize=24)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()


rw = RandomWalk(50000)
rw.fill_walk()
draw_scatter(rw.x_values, rw.y_values)
