from static import *

ALL_TECHNOLOGISTS = pkl_load("Models/military_technology.pkl")
ALL_KEYS = [k for k in ALL_TECHNOLOGISTS]


class Country:
    finished_technologists = []
    research_able = []

    def __init__(self, name):
        self.name = name
        self.update()

    def technologist_update(self):
        for k in ALL_KEYS:
            if k in self.finished_technologists or k in self.research_able:
                continue

            if self.be_able_to_research(ALL_TECHNOLOGISTS[k]):
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
