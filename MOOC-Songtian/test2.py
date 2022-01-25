from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

ten_sides_die = Die(10)
for i in range(10):
    ten_sides_die.roll_die()