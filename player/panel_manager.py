class PanelManager:
    def __init__(self, parent):
        self.parent = parent
        self.food = 10, 5
        self.mineral = 10, 5
        self.energy = 10, 5
        self.commodity = 10, 5
        self.alloy = 10, 5
        self.population = 10
        self.civil = 10
        self.military = 10
        self.technology = 10

    def update(self, panel, storage, daily):
        exec(f"self.{panel} = {storage}, {daily}")

    def daily(self):
        for member in (i for i in dir(self) if not i.startswith('__') and not i.endswith('__')):
            try:
                storage, _daily = getattr(self, member)
                setattr(self, member, (storage + _daily, _daily))
            except Exception as e:
                ...


if __name__ == '__main__':
    pm = PanelManager()
    print(pm.food)
    for i in range(10):
        pm.daily()
    print(pm.food)
