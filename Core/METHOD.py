from Core import CONST
import random


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


def xy_to_index(x, y, size):
    return y * size + x


def index_to_xy(index, size):
    y, x = divmod(index, size)
    return x, y


def xy_to_position(x, y, size, lt_x, lt_y):
    return lt_x + x * size, lt_y + y * size


def index_to_pos_xy(index, n, size, lt_x, lt_y):
    # lt_x : left_top_x
    # lt_y : left_top_y
    y, x = divmod(index, n)
    return xy_to_position(x, y, size, lt_x, lt_y)


def mouse_int_world(x, y):
    bx = CONST.WORLD_POSITION_START <= x <= CONST.WORLD_POSITION_END
    by = CONST.WORLD_POSITION_START <= y <= CONST.WORLD_POSITION_END
    return (bx and by)


def mouse_in_zoning(x, y):
    bx = CONST.ZONING_POSITION_START_X <= x <= CONST.ZONING_POSITION_END_X
    by = CONST.ZONING_POSITION_START_Y <= y <= CONST.ZONING_POSITION_END_Y
    return (bx and by)


def mouse_in_which_block(x, y, world_size, block_number):
    index_x = (x - CONST.WORLD_POSITION_START) // world_size
    index_y = (y - CONST.WORLD_POSITION_START) // world_size
    return xy_to_index(index_x, index_y, block_number)


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

    def random_attr(self):
        return self.to_index((random.randint(0, 100))), random.choice(CONST.BLOCK_ZONING_NUMBER)

    def new_world(self, size):
        return [self.random_attr() for _ in range(size)]
