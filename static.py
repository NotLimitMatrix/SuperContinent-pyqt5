import _pickle
import time

def all_technologists():
    with open("Models/military_technology.pkl", 'rb') as military:
        return _pickle.load(military)


class CONST:
    all_technologists = all_technologists()
    all_keys = [k for k in all_technologists]


def all_in(tested, within):
    for item in tested:
        if item not in within:
            return False
    return True

class Country:
    finished_technologists = []
    research_able = []

    def __init__(self, name):
        self.name = name
        self.update()

    def technologist_update(self):
        for k in CONST.all_keys:
            if k in self.finished_technologists or k in self.research_able:
                continue

            if self.be_able_to_research(CONST.all_technologists[k]):
                self.research_able.append(k)

    def be_able_to_research(self, technology):
        front = technology.front

        if front:
            if isinstance(front, list):
                return all_in(front, self.finished_technologists)
            else:
                return front in self.finished_technologists
        else:
            return True

    def finish_research(self, technology_key):
        self.finished_technologists.append(technology_key)
        self.research_able.remove(technology_key)
        self.update()

    def update(self):
        self.technologist_update()

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

    def research(self, technology_key):
        technology = CONST.all_technologists[technology_key]

        while not technology.finish():
            technology.current += self.produce
            print(f"Research: {technology.name} {technology.current / technology.cost}%")
            time.sleep(0.5)
        else:
            self.belong_country.finish_research(technology_key)
            print(f"Research Finish: {technology.name}\n")

    def __repr__(self):
        return f"研究员： 生产 {self.produce}"