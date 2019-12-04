class Timer:
    def __init__(self, parent):
        self.parent = parent
        self.time_flow = 0

    def display(self):
        years, o = divmod(self.time_flow, 360)
        months, days = divmod(o, 30)
        self.parent.setWindowTitle(f"{self.parent.title} 【TIME: {years}-{months}-{days}】")

    def update(self, n):
        self.time_flow += n
        self.display()
