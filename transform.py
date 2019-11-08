from static import *


class Localisation:
    DIR = "Common/Localisation"

    def __init__(self):
        self.files = [
            "Technology/beyond.txt",
            "Technology/civil.txt",
            "Technology/military.txt",
            "jobs.txt",
            "resources.txt"
        ]

        self._dict = self.localisation()

    def localisation(self):
        _dict = dict()
        for file in self.files:
            with open(join(self.DIR, file), 'r') as d:
                for line in d:
                    line = line.strip()
                    if line:
                        key, value = line.split('=')
                        _dict[key] = value
        return _dict

    def __getitem__(self, item):
        return self._dict.get(item)


class Transformer:
    def __init__(self):
        self._dict = dict()
        self.output = None
        self.localisation = Localisation()

    def init(self, l):
        pass

    def gen_technologists(self, _dict):
        for k, v in _dict.items():
            yield k, v

    def transform(self):
        pkl_dump(self._dict, self.output)


class ResourceTransformer(Transformer):
    def init(self, l):
        self.dir = "Common/resources.json"
        self.output = "Models/resources.pkl"

        for k, v in self.gen_technologists(json_load(self.dir)):
            name = l[k]
            if v is None:
                self._dict[k] = Resource(name=name)
            else:
                self._dict[k] = Resource(name=name, need=v.get('need'), rate=v.get('rate'))


class TechnologyTransformer(Transformer):
    def init(self, l):
        self.dir = "Common/Technology"
        self.files = [
            "Common/Technology/military_technology.json",
            "Common/Technology/beyond_technology.json",
            "Common/Technology/civil_technology.json"
        ]
        self.output = "Models/technology.pkl"

        self.transform_beyond_technology(l)
        self.transform_sword_armor(l)

    def transform_beyond_technology(self, l):
        Beyond = join(self.dir, "beyond_technology.json")
        for k, v in self.gen_technologists(json_load(Beyond)):
            self._dict[k] = Technology(
                name=l[k],
                cost=v.get('cost'),
                front=v.get('front'),
                weight=v.get('weight'),
                _type=v.get('type'),
                loop=False,
                no=v.get('no')
            )

    def transform_sword_armor(self, l):
        Sword_Armor = join(self.dir, "Sword_Armor")
        for file in listdir(Sword_Armor):
            for k, v in self.gen_technologists(json_load(join(Sword_Armor, file))):

                *_, level = k.split('_')
                if level == 'x':
                    loop = True
                    level = 6
                else:
                    loop = False
                    level = int(level)

                self._dict[k] = SwordArmor(
                    name=l[k],
                    cost=v.get('cost'),
                    front=v.get('front'),
                    weight=v.get('weight'),
                    _type=v.get('type'),
                    no=v.get('no'),
                    loop=loop,
                    level=level
                )


def main():
    # localisation = Localisation()
    #
    # transform_resources = ResourceTransformer()
    # transform_resources.init(localisation)
    # transform_resources.transform()
    #
    # transform_technology = TechnologyTransformer()
    # transform_technology.init(localisation)
    # transform_technology.transform()

    pass


def test(file):
    res = pkl_load(join("Models", file))
    for k, v in res.items():
        print(k, v.name, v.need, v.rate, v._max)


if __name__ == '__main__':
    # main()
    # test("resources.pkl")
    pass
