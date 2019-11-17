from models import Resource
from static import display_number

import pysnooper


class OneResource:
    def __init__(self, name, storage, daily):
        self.name = name
        self.storage = storage
        self.daily = daily

    def __repr__(self):
        return f"<{self.name}: {self.storage} {self.daily}>"

    def update(self):
        self.storage += self.daily

    def display(self):
        return display_number(self.storage), display_number(self.daily)

    def update_storage(self, n):
        self.storage += n

    def update_daily(self, n):
        self.daily += n

    def set_storage(self, n):
        self.storage = n

    def set_daily(self, n):
        self.daily = n


class ResourcePanel:
    def __init__(self,
                 energy=OneResource('能量', 100, 5),
                 mineral=OneResource('矿物', 100, 5),
                 food=OneResource('食物', 100, 5),
                 alloys=OneResource('合金', 100, 5),
                 consumer_goods=OneResource('物资', 100, 5),
                 research_point=OneResource('科研点', 100, 5),
                 ):
        self.energy = energy
        self.mineral = mineral
        self.food = food
        self.alloys = alloys
        self.consumer_goods = consumer_goods
        self.research_point = research_point

    def update(self):
        for k in self.__dict__:
            getattr(self, k).update()

    def display(self):
        self.update()
        return [getattr(self, k).display() for k in self.__dict__]
