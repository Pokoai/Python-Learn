from random import randint
import pygal

class Die():
    """创建一个骰子类"""

    def __init__(self, num_sides=6):
        """初始化骰子面数属性,默认为6"""
        self.num_sides = num_sides

    def roll_die(self):
        """返回所掷骰子数"""
        return randint(1, self.num_sides)


def draw_pygal(output_value):
    """用pygal绘制直方图"""

    hist = pygal.Bar()

    hist.title = "Result of rolling one  D6 1000 times"
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = [x for x in range(1, 7)]
    hist.x_title = "Result"
    hist._y_title = "Frequencies of Result"

    hist.add("D6", output_value)
    hist.render_to_file('die1_visual.svg')



die = Die()
results = []
frequencies = []
for roll_num in range(1000):
    results.append(die.roll_die())
for number in range(1, die.num_sides + 1):
    frequencies.append(results.count(number))

draw_pygal(frequencies)


