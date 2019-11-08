import _pickle
import time
import json

from os.path import join
from os import listdir


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


class Resource:
    def __init__(self, name, need=None, rate=None, _max=50000):
        self.name = name
        self.need = need
        self.rate = rate
        self._max = _max

    def __repr__(self):
        return f"<Resource: {self.name}>"


class Technology:
    def __init__(self, name, cost, front, weight, no, _type, loop):
        self.name = name
        self.cost = cost
        self.front = front
        self.weight = weight
        self.no = no  # 如果研究了互斥的科技，则该科技不能被研究

        self.type = _type  # 0: military, 1: civil, 2: beyond
        self.current = 0
        self.loop = loop

    def finish(self):
        return self.current >= self.cost

    def __repr__(self):
        return f"<Technology: {self.name}, cost:{self.cost}>"


class SwordArmor(Technology):
    def __init__(self, level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = level

        if 'X' in self.name:
            self.name.replace('X', str(self.level))
