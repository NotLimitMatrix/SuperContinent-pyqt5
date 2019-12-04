import sys

import transform

from Core import CONST, KEY, INTERFACE
from GUI.MainGUI import MainGameGUI
from GUI import QApplication

from Panel import Panel

temp = """地块：
--------------------
环境： 一般 50%
--------------------
人口： 934
  电工： 40
  矿工： 20
  农民： 40
  工人： 21
  冶金师： 24
  研究员： 80
--------------------
产出：
  能量：80 (100 - 20)
  矿物：40 (80 - 40)
  食物：20 (24 - 4)
  物资：24 (64 - 40)
  合金：94 (94 - 0)
  科研点： 24
"""


# class Tester:
#     def __init__(self, be_test, country: Country):
#         self.be_test = be_test
#         self.country = country
#
#     def _run(self, input_str: str):
#         if ' ' in input_str:
#             command, *args = input_str.split()
#             func = getattr(self, command)
#             func(*args)
#         else:
#             command = input_str
#             func = getattr(self, command)
#             func()
#
#     def run(self):
#         input_str = input("> ")
#         while input_str:
#             self._run(input_str)
#             input_str = input("> ")


class TestGui:
    def __init__(self, panel: Panel):
        self.PANEL = panel
        # self.RESEARCHER = MainResearcher()

        # technologist = {
        #     'mility': 'energy_armor_1',
        #     'civil': None,
        #     'beyond': 'dark_energy_technology'
        # }
        # self.RESEARCHER.assign(self.PANEL.power_dict.get('research_point'), CONST.USE_RESEARCHER_RATES, technologist)

    def display(self):
        panel_display = self.PANEL.display()

        resources_list = panel_display.get('resource')
        power_list = panel_display.get('power')

        content = INTERFACE.MESSAGE_TEMPLATE.copy()

        content[INTERFACE.RESOURCES] = resources_list
        content[INTERFACE.POWERS] = power_list
        content[INTERFACE.WAIT_SELECT_ITEMS] = {
            INTERFACE.WAIT_ITEMS_TYPE: KEY.TECHNOLOGY,
            INTERFACE.WAIT_ITEMS_OPTIONS: [
                ['灵能理论', 30000,
                 ['帝国所有人口消耗 -20%', '帝国所有人口效率 +50%', '军队战斗力 +100%']],
                ['灵能工程', 60000,
                 ['生产物资所需矿物 -30%', '生产合金所需矿物 -30%', '军队生命值 +100%']],
                ['基因编码实验', 30000, ['人口增长率 +20%', '人口消耗食物 -50%', '军队生命值 +200%']],
                ['基因改造工程', 60000,
                 ['人口增长率 +30%', ' 帝国所有人口消耗 -10%', '帝国所有人口效率 +30%']]
            ]
        }
        content[INTERFACE.RESEARCHER_ITEMS] = {
            KEY.MILITARY: (None, None),
            KEY.CIVIL: (None, None),
            KEY.BEYOND: (None, None)
        }
        content[INTERFACE.DETAIL_TEXT] = None

        return content


def main():
    # country = Country("World")
    # researcher = Researcher(1000, country)
    #
    # tester = Tester(researcher, country)
    # tester.run()
    app = QApplication(sys.argv)

    panel = Panel()
    tester = TestGui(panel)

    MainGameGUI(tester)
    sys.exit(app.exec_())


if __name__ == '__main__':
    # transform.main()
    main()
