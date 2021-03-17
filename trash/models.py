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
    def __init__(self, name, cost, front, no, _type, loop, key):
        self.name = name
        self.cost = cost
        self.front = front
        self.no = no  # 如果研究了互斥的科技，则该科技不能被研究

        self.type = _type  # 0: military, 1: civil, 2: beyond
        self.current = 0
        self.loop = loop

        self.key = key

    def finish(self):
        return self.current >= self.cost

    def __repr__(self):
        return f"<Technology: {self.name}, cost:{self.cost}>"


class SwordArmor(Technology):
    def __init__(self, level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = level

        self.dynamic_cost = 1000

    def level_up(self, n=1):
        self.level += n
        self.update()

    def update(self):
        if self.loop:
            self.cost = self.cost + (self.level - 5) * self.dynamic_cost


class Consumption:
    def __init__(self, rate, materials):
        self.materials = materials  # {Resource_key : Number_of_product}
        self.rate = rate

    def consume(self):
        _dict = dict()
        for k, v in self.materials.items():
            _dict[k] = v * (1 + self.rate)
        return _dict


class Product:
    def __init__(self, rate, material, number):
        self.material = material  # Key of resource
        self.number = number  # Number of product
        self.rate = rate  # one material can get (1+rate)*number

    def product(self):
        return {self.material: self.number * (1 + self.rate)}


class Job:
    def __init__(self, name, producer: Product, consumer: Consumption):
        self.name = name
        self.producer = producer
        self.consumer = consumer

    def produce_consume(self, made, rate=1):
        # made: 0 -> consumption, 1 -> produce
        _dict = self.producer.product() if made else self.consumer.consume()
        for k, v in _dict.items():
            _dict[k] = v * (1 + rate)
        return _dict

    def __repr__(self):
        return f"<Job: {self.name}, Product: {self.producer.material}>"
