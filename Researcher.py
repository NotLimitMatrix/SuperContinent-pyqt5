from static import ALL_TECHNOLOGISTS, ALL_KEYS, all_in


def key_2_tech(technology_key):
    if technology_key:
        return ALL_TECHNOLOGISTS[technology_key]
    else:
        return None


class UnitResearcher:
    def __init__(self, technology, daily, rate=1):
        self.technology = technology
        self.daily = daily
        self.rate = 1

    def research(self):
        if self.technology.finish():
            return True
        else:
            self.technology.current += self.daily * self.rate
            return False

    def display(self):
        return (self.technology.name, 100 * self.technology.current / self.technology.cost)

    def finish(self):
        return self.technology.finish()


class Researcher:
    def __int__(self, daily, rates):
        self.daily = daily
        self.rates = rates

        self.FINISHED_TECHNOLOGISTS = list()
        self.RESEARCHER_ABLE = list()
        self.LOOP_TECHNOLOGISTS = dict()

        self.update_technologist()

        self.MILITARY_RESEARCHER = None
        self.CIVIL_RESEARCHER = None
        self.BEYOND_RESEARCHER = None

    def be_able_to_researcher(self, technology_key):
        technology = key_2_tech(technology_key)
        front = technology.front
        if front:
            if isinstance(front, list):
                return all_in(front, self.FINISHED_TECHNOLOGISTS)
            else:
                return front in self.FINISHED_TECHNOLOGISTS

    def update_technologist(self):
        for k in ALL_KEYS:
            if k in self.FINISHED_TECHNOLOGISTS or k in self.RESEARCHER_ABLE or k in self.LOOP_TECHNOLOGISTS:
                continue
            if self.be_able_to_researcher(k):
                self.RESEARCHER_ABLE.append(k)

#
#     def get_unit_researcher(self, daily, rates, technology):
#         if technology is None:
#             return None
#
#         if technology.type == 0:
#             return UnitResearcher(technology, daily * rates[0])
#         elif technology.type == 1:
#             return UnitResearcher(technology, daily * rates[1])
#         else:
#             return UnitResearcher(technology, daily * rates[2])
#
#     def assign(self, daily, rates, technology_key_dict: dict):
#         m_technology = technology_key_dict.get('mility')
#         c_technology = technology_key_dict.get('civil')
#         b_technology = technology_key_dict.get('beyond')
#
#         m_technology = key_2_tech(m_technology)
#         c_technology = key_2_tech(c_technology)
#         b_technology = key_2_tech(b_technology)
#
#         self.MILITARY_RESEARCHER = self.get_unit_researcher(daily, rates, m_technology)
#         self.CIVIL_RESEARCHER = self.get_unit_researcher(daily, rates, c_technology)
#         self.BEYOND_RESEARCHER = self.get_unit_researcher(daily, rates, b_technology)
#
#     def clean_all(self):
#         self.MILITARY_RESEARCHER = None
#         self.CIVIL_RESEARCHER = None
#         self.BEYOND_RESEARCHER = None
#
#     def clean_one(self, k):
#         if k == 'mility':
#             self.MILITARY_RESEARCHER = None
#         elif k == 'civil':
#             self.CIVIL_RESEARCHER = None
#         else:
#             self.BEYOND_RESEARCHER = None
#
#     def finish_technology(self, technology: Technology):
#         if technology.loop:
#             if technology.key in self.LOOP_TECHNOLOGISTS:
#                 self.LOOP_TECHNOLOGISTS[technology.key].level_up()
#             else:
#                 self.LOOP_TECHNOLOGISTS[technology.key] = technology
#         else:
#             self.FINISHED_TECHNOLOGISTS.append(technology.key)
#             self.RESEARCH_ABLE.remove(technology.key)
#
#         self.update_technologist_list()
#
#     def research_one(self, temp: UnitResearcher):
#         if temp:
#             if temp.finish():
#                 self.finish_technology(temp.technology)
#             else:
#                 temp.research()
#
#     def research_all(self):
#         self.research_one(self.MILITARY_RESEARCHER)
#         self.research_one(self.CIVIL_RESEARCHER)
#         self.research_one(self.BEYOND_RESEARCHER)
#
#     def display(self):
#         self.research_all()
#
#         m = self.MILITARY_RESEARCHER.display() if self.MILITARY_RESEARCHER else None
#         c = self.CIVIL_RESEARCHER.display() if self.CIVIL_RESEARCHER else None
#         b = self.BEYOND_RESEARCHER.display() if self.BEYOND_RESEARCHER else None
#         return [m, c, b]
#
#     def able_researcher_list(self):
#         return self.RESEARCH_ABLE + [k for k in self.LOOP_TECHNOLOGISTS]
