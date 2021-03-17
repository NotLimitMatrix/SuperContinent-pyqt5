class Technology:
    def __init__(self, name, key, cost, front, no, _type):
        self.name = name
        self.key = key
        self.cost = cost
        self.front = front
        self.no = no
        self.type = _type  # 0:military 1:civil 2:beyond
        self.loop = False

        self.current = 0

    def finish(self):
        return self.current >= self.cost

    def __repr__(self):
        return f"<Technology: {self.name}, cost:{self.cost}>"


class LoopTechnology(Technology):
    def __init__(self, name, key, cost, front, no, _type, dyc):
        super().__init__(name, key, cost, front, no, _type)
        self.dyc = dyc
        self.loop = True
        self.level = 1

    def levelup(self, n=1):
        self.level += 1
        self.update()

    def update(self):
        self.cost += self.level * self.dyc
