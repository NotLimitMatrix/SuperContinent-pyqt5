from Country import Country, ALL_TECHNOLOGISTS, ALL_KEYS
from Researcher import Researcher
import transform

from MainGui import MainGameGUI, QApplication, sys

from Panel import Panel


class Tester:
    def __init__(self, be_test, country: Country):
        self.be_test = be_test
        self.country = country

    def _run(self, input_str: str):
        if ' ' in input_str:
            command, *args = input_str.split()
            func = getattr(self, command)
            func(*args)
        else:
            command = input_str
            func = getattr(self, command)
            func()

    def run(self):
        input_str = input("> ")
        while input_str:
            self._run(input_str)
            input_str = input("> ")

    def show(self, technology_key):
        technology = ALL_TECHNOLOGISTS[technology_key]
        information = """
        Technology: {name}
        花费：{cost}
        前置科技：{fronts}
        循环科技：{yes}{level}
        """
        fronts = technology.front
        str_fronts = ", ".join(fronts) if isinstance(fronts, list) else fronts
        loop = technology.loop
        yes = "是" if loop else "否"
        try:
            level = f"\n\t\t\t等级：{technology.level}"
        except:
            level = ''

        print(information.format(name=technology.name, cost=technology.cost, fronts=str_fronts, yes=yes, level=level))

    def research(self):
        for i, item in enumerate(self.country.RESEARCH_ABLE):
            temp = ALL_TECHNOLOGISTS[item]
            print(f"{i}) {temp.name}, Cost:{temp.cost}")
        index = int(input("> "))
        select_technology = self.country.RESEARCH_ABLE[index]
        self.be_test.research(select_technology, ALL_TECHNOLOGISTS)

    def technologists(self):
        for i, item in enumerate(ALL_KEYS):
            print(f"{i}) {item}")


class TestGui:
    def __init__(self, panel):
        self.PANEL = panel

    def display(self):
        panel_display = self.PANEL.display()

        return {
            'time_flow': 1,
            'resources_list': panel_display.get('resource'),
            'power_list': panel_display.get('power'),
            'wait_select_list': {
                'type': 'technology',
                'options': [
                    ['灵能理论', 30000, ['帝国所有人口消耗 -20%', '帝国所有人口效率 +50%', '军队战斗力 +100%']],
                    ['灵能工程', 60000, ['生产物资所需矿物 -30%', '生产合金所需矿物 -30%', '军队生命值 +100%']],
                    ['基因编码实验', 30000, ['人口增长率 +20%', '人口消耗食物 -50%', '军队生命值 +200%']],
                    ['基因改造工程', 60000, ['人口增长率 +30%', ' 帝国所有人口消耗 -10%', '帝国所有人口效率 +30%']]
                ]
            },
            'research_label_list': [
                ("导弹防御系统", 81),
                ("研究中心", 23),
                ("灵能理论", 67)
            ],
            'detail_text': """地块：
--------------------
环境： 还行 50%
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
        }


def main():
    # country = Country("World")
    # researcher = Researcher(1000, country)
    #
    # tester = Tester(researcher, country)
    # tester.run()
    app = QApplication(sys.argv)

    panel = Panel()

    game = MainGameGUI(TestGui(panel))
    sys.exit(app.exec_())


if __name__ == '__main__':
    # transform.main()
    main()
