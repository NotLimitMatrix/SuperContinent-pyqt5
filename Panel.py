from models import Resource
from static import display_number, CONST


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


class Panel:
    def __init__(self,
                 energy=OneResource('能量', 100, 5),
                 mineral=OneResource('矿物', 100, 5),
                 food=OneResource('食物', 100, 5),
                 alloys=OneResource('合金', 100, 5),
                 consumer_goods=OneResource('物资', 100, 5),
                 economic_power=0,
                 military_power=0,
                 research_point=100
                 ):
        self.energy = energy
        self.mineral = mineral
        self.food = food
        self.alloys = alloys
        self.consumer_goods = consumer_goods
        self.ep = economic_power
        self.mp = military_power
        self.rp = research_point

    def update(self):
        self.energy.update()
        self.mineral.update()
        self.food.update()
        self.consumer_goods.update()
        self.alloys.update()
        self.ep = self.to_economic_power()
        self.mp = 0

    def set_military_power(self, mp):
        self.mp = mp
        self.update()

    def set_research_point(self, rp):
        self.rp = rp
        self.update()

    def to_economic_power(self):
        (es, ed), (ms, md), (fs, fd), (as_, ad), (cs, cd) = CONST.RESOURCE_WEIGHT
        e_power = es * self.energy.storage + ed * self.energy.daily
        m_power = ms * self.mineral.storage + md * self.mineral.daily
        f_power = fs * self.food.storage + fd * self.food.daily
        a_power = as_ * self.alloys.storage + ad * self.alloys.daily
        c_power = cs * self.consumer_goods.storage + cd * self.consumer_goods.daily
        return e_power + m_power + f_power + a_power + c_power

    def display(self):
        self.update()

        return {
            'resource': [self.energy.display(), self.mineral.display(), self.food.display(),
                         self.consumer_goods.display(), self.alloys.display()],
            'power': [display_number(self.ep, False), display_number(self.mp, False), display_number(self.rp, False)]
        }
