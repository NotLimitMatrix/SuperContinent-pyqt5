from Core import CONST
import random
from math import hypot

import json
import _pickle


def json_load(file):
    with open(file, 'r', encoding='utf-8') as r:
        return json.load(r)


def pkl_load(file):
    with open(file, 'rb') as bin:
        return _pickle.load(bin)


def pkl_dump(data, file):
    with open(file, 'wb') as bin:
        _pickle.dump(data, bin)


def all_in(tested, within):
    for item in tested:
        if item not in within:
            return False
    return True


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
    return x * size + y


def index_to_xy(index, size):
    x, y = divmod(index, size)
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


def points_to_indexs(points: set, wn):
    result = []
    for i, j in points:
        result.append(xy_to_index(j, i, wn))
    return result


def square_from_one_xy(x, y, sn, wn):
    if sn >= wn:
        raise ValueError("步长不能大于地图尺寸")
    sn += 1

    d = [i for i in range(sn)]

    left_x = [(0 if x - i < 0 else x - i) for i in d]
    right_x = [(wn - 1 if x + i >= wn else x + i) for i in d]

    xs = set(left_x + right_x)

    left_y = [(0 if y - i < 0 else y - i) for i in d]
    right_y = [((wn - 1) if y + i >= wn else y + i) for i in d]

    ys = set(left_y + right_y)

    return [(i, j) for i in xs for j in ys]


def square_from_one_walk(x, y, wn):
    lx = 0 if x - 1 < 0 else x - 1
    gx = wn - 1 if x + 1 == wn else x + 1
    ly = 0 if y - 1 < 0 else y - 1
    gy = wn - 1 if y + 1 == wn else y + 1

    points = [(x, y), (lx, y), (gx, y), (x, ly), (x, gy)]

    return set(points)


def AStar_path(x1, y1, x2, y2, wn):
    d = -1

    x = x1
    y = y1

    result = [(x, y)]

    while d != 0:
        can_move_list = square_from_one_walk(x, y, wn)
        tags_can_move_list = {hypot(i[0] - x2, i[1] - y2): i for i in can_move_list}
        d = min(tags_can_move_list.keys())
        x, y = tags_can_move_list[d]
        result.append((x, y))

    return result


if __name__ == '__main__':
    x = AStar_path(1, 1, 8, 9, 20)
    print(x)
