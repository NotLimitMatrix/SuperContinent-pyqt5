from static import *


def main():
    country = Country("World")
    researcher = Researcher(10, country)
    researcher.set_modifier(True, 98)

    while country.research_able:
        for i, item in enumerate(country.research_able):
            temp = CONST.all_technologists[item]
            print(f"{i + 1}) {temp.name} cost:{temp.cost}")
        print("0) quit")

        index = int(input("> "))

        if index:
            select_technology = country.research_able[index - 1]
            researcher.research(select_technology)
        else:
            quit(0)


if __name__ == '__main__':
    main()
