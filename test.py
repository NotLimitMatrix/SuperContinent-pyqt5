from Country import Country, ALL_TECHNOLOGISTS, ALL_KEYS
from Researcher import Researcher
import transform


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


def main():
    country = Country("World")
    researcher = Researcher(1000, country)

    tester = Tester(researcher, country)
    tester.run()


if __name__ == '__main__':
    transform.main()
    main()
