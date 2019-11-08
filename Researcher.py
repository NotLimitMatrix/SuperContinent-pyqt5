from static import *


class Researcher:
    def __init__(self, produce, belong_country):
        self.produce = produce
        self.belong_country = belong_country
        self.rate = 1
        self.modifiers = []

    def set_modifier(self, made, rate):
        # del:False, add:True
        if made:
            self.modifiers.append(rate)
        else:
            self.modifiers.remove(rate)
        self.update()

    def update(self):
        self.produce = self.produce * (self.rate + sum(self.modifiers))

    def research(self, technology_key, ALL_TECHNOLOGIST):
        technology = ALL_TECHNOLOGIST[technology_key]

        while not technology.finish():
            technology.current += self.produce
            print(f"Research: {technology.name} {100* technology.current / technology.cost}%")
            time.sleep(0.5)
        else:
            self.belong_country.finish_research(technology_key)
            print(f"Research Finish: {technology.name}\n")

    def __repr__(self):
        return f"研究员： 生产 {self.produce}"
