class Resource:
    def __init__(self, name, need=None, rate=1, _max=50000):
        self.name = name
        self.need = need
        self.rate = rate
        self.max = _max

    def __repr__(self):
        return f"<Resource: {self.name}>"
