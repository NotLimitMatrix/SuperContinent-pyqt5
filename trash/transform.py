from models import *


class Localisation:
    DIR = "Common/Localisation"

    def __init__(self):
        self.files = [
            "technology/beyond.txt",
            "technology/civil.txt",
            "technology/military.txt",
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
            self._dict[k] = Resource(name=l[k], need=v.get('need'), rate=v.get('rate'))


class JobTransformer(Transformer):
    def init(self, l):
        self.dir = "Common/jobs.json"
        self.output = "Models/jobs.pkl"
        for k, v in self.gen_technologists(json_load(self.dir)):
            name = l[k]
            produce_dict, consume_dict = v.get('produce'), v.get('consume')

            # 生产物资， 生产所需， 生产效率
            p_produce, p_material, p_rate = produce_dict.keys()
            p_produce_number = produce_dict.get(p_produce)
            p_material_key = produce_dict.get(p_material)
            p_rate_number = produce_dict.get(p_rate)

            producer = Product(material=p_produce, number=p_produce_number, rate=p_rate)

            consume = {
                "food": consume_dict.get("food"),
                "consumer_goods": consume_dict.get("consumer_goods"),
                p_material_key: (p_produce_number * p_rate_number) if p_material_key else 0
            }

            consumer = Consumption(materials=consume, rate=consume_dict.get('rate'))

            self._dict[k] = Job(name, producer, consumer)


class TechnologyTransformer(Transformer):
    def init(self, l):
        self.dir = "../common/technology"
        self.files = [
            "Common/technology/military_technology.json",
            "Common/technology/beyond_technology.json",
            "Common/technology/civil_technology.json"
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
                _type=v.get('type'),
                loop=False,
                no=v.get('no'),
                key=k
            )

    def transform_sword_armor(self, l):
        Sword_Armor = join(self.dir, "SwordArmor")
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
                    _type=v.get('type'),
                    no=v.get('no'),
                    loop=loop,
                    level=level,
                    key=k
                )


def main():
    localisation = Localisation()

    transforms = [
        ResourceTransformer(),
        TechnologyTransformer(),
        JobTransformer()
    ]

    for tf in transforms:
        tf.init(localisation)
        tf.transform()


def test(file):
    import pprint
    res = pkl_load(join("Models", file))
    pprint.pprint(res)


if __name__ == '__main__':
    main()
    # test("resources.pkl")
    pass
