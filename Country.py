from static import *


class ResourcePanel:
    def __init__(self, monthlys, rates):
        self.monthlys = monthlys
        self.rates = rates
        self.dynamic_resources = DYNAMIC_RESOURCE_PANEL

    def monthly(self):
        for k, v in self.dynamic_resources.items():
            self.dynamic_resources[k] = v.update(self.monthlys, self.rates)


class GameTime:
    def __init__(self, time):
        self.time = time

        self.year = self.time % 360
        self.month = (self.time - 360 * self.year) % 30
        self.day = (self.time - 360 * self.year - 30 * self.month)

    def __repr__(self):
        return f"<Time {self.year}:{self.month}:{self.day}>"

    def flow(self):
        self.time += 1


class Country:
    FINISHED_TECHNOLOGISTS = []
    RESEARCH_ABLE = []
    LOOP_TECHNOLOGISTS = dict()

    def __init__(self, name):
        self.name = name
        self.resource_panel = ResourcePanel(5, 1)
        # self.modifiers = []
        # self.blocks = []
        self.time = GameTime(0)

        self.update()

    def technologist_update(self):
        for k in ALL_KEYS:
            if k in self.FINISHED_TECHNOLOGISTS or k in self.RESEARCH_ABLE or k in self.LOOP_TECHNOLOGISTS:
                continue
            if self.be_able_to_research(ALL_TECHNOLOGISTS[k]):
                self.RESEARCH_ABLE.append(k)

    def be_able_to_research(self, technology):
        front = technology.front
        if front:
            if isinstance(front, list):
                return all_in(front, self.FINISHED_TECHNOLOGISTS)
            else:
                return front in self.FINISHED_TECHNOLOGISTS
        else:
            return True

    def finish_research(self, technology_key):
        if 'x' in technology_key:
            if technology_key in self.LOOP_TECHNOLOGISTS:
                self.LOOP_TECHNOLOGISTS[technology_key].level_up()
            else:
                self.LOOP_TECHNOLOGISTS[technology_key] = ALL_TECHNOLOGISTS[technology_key]
        else:
            self.FINISHED_TECHNOLOGISTS.append(technology_key)
            self.RESEARCH_ABLE.remove(technology_key)

        self.update()

    def update(self):
        self.technologist_update()
