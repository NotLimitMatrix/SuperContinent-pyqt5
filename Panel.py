from Recycle.static import display_number, CONST


class DynamicResource:
    def __init__(self, name, storage, daily):
        self.name = name
        self.storage = storage
        self.daily = daily
        self.rate = 1

    def __repr__(self):
        return f"<{self.name}: {self.storage} {self.daily}>"

    def update(self):
        self.storage += self.daily * self.rate

    def display(self):
        return display_number(self.storage), display_number(self.daily)


class Panel:
    def __init__(self):
        self.resource_dict = {
            'energy': DynamicResource('能量', 100, 5),
            'mineral': DynamicResource('矿物', 100, 5),
            'food': DynamicResource('食物', 100, 5),
            'consumer_goods': DynamicResource('物资', 100, 5),
            'alloys': DynamicResource('合金', 100, 5),
        }

        self.power_dict = {
            'economic_power': 0,
            'military_power': 0,
            'research_point': 100
        }

    def update(self):
        for _, v in self.resource_dict.items():
            v.update()
        self.power_dict['economic_power'] = self.to_economic_power()

    def get_one_power(self, dynamic_resource: DynamicResource, weight_tuple: tuple):
        storage_weight, daily_weight = weight_tuple
        return dynamic_resource.storage * storage_weight + dynamic_resource.daily * daily_weight

    def to_economic_power(self):
        return sum([self.get_one_power(self.resource_dict.get(k), wt) for k, wt in
                    zip(CONST.RESOURCE_KEYS, CONST.RESOURCE_WEIGHT)])

    def set_mp(self, mp):
        self.power_dict['military_power'] = mp

    def set_rp(self, rp):
        self.power_dict['research_point'] = rp

    def display_resource(self):
        return [self.resource_dict[k].display() for k in CONST.RESOURCE_KEYS]

    def display_power(self):
        ep = self.power_dict.get('economic_power')
        mp = self.power_dict.get('military_power')
        rp = self.power_dict.get('research_point')
        return [display_number(ep, False), display_number(mp, False), display_number(rp, False)]

    def display(self):
        self.update()

        return {
            'resource': self.display_resource(),
            'power': self.display_power()
        }
