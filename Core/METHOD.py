from Core import CONST
import random


def coordinate_to_index(i, j, size):
    return i * size + j


def index_to_coordinate(index, size):
    return divmod(index, size)


def format_number(number):
    if number > 1000000000:
        return "1G"
    elif number > 999999:
        return f"{number // 1000000}M"
    elif number > 999:
        return f"{number // 1000}K"
    else:
        return str(number)


def display_number(n, have_neg=True):
    if have_neg:
        number = abs(n)
        neg = '-' if n < 0 else '+'
        return f"{neg}{format_number(number)}"
    else:
        return format_number(n) if n > 0 else '0'


def xy_to_position(x, y, size, lt_x, lt_y):
    return lt_x + x * size, lt_y + y * size


def index_to_xy(index, n, size, lt_x, lt_y):
    # lt_x : left_top_x
    # lt_y : left_top_y
    x, y = divmod(index, n)
    return xy_to_position(x, y, size, lt_x, lt_y)


class RandomBlock:
    def __init__(self, r: tuple = CONST.BLOCK_STATUS_WEIGHT):
        self.r = r
        self.check()

        self.r1 = r[0]
        self.r2 = self.r1 + r[1]
        self.r3 = self.r2 + r[2]
        self.r4 = self.r3 + r[3]

    def check(self):
        if sum(self.r) != 100:
            raise ValueError("生成地块的权重分配错误")

    def to_index(self, n):
        if 0 <= n < self.r1:
            return 0
        elif self.r1 <= n < self.r2:
            return 1
        elif self.r2 <= n < self.r3:
            return 2
        elif self.r3 <= n < self.r4:
            return 3
        else:
            return 4

    def new_world(self, size):
        return [self.to_index(random.randint(0, 100)) for _ in range(size)]


if __name__ == '__main__':
    b = RandomBlock()
    x = b.new_world(100)
    print(x)
