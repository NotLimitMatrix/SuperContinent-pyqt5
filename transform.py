import json

from os.path import join
from os import listdir
import _pickle as cPickle


# import static


def json_load(file):
    with open(file, 'r', encoding='utf-8') as r:
        return json.load(r)


def pkl_load(file):
    with open(file, 'rb') as bin:
        return cPickle.load(bin)


def pkl_dump(data, file):
    with open(file, 'wb') as bin:
        cPickle.dump(data, bin)


class CONST:
    common = "Common"
    models = "Models"


def technology_localisation():
    _dir = "Common/Localisation/Technology"
    files = ["beyond.txt", "civil.txt", "military.txt"]
    _dict = dict()
    for file in files:
        with open(join(_dir, file), 'r') as d:
            for line in d:
                line = line.strip()
                if line:
                    key, value = line.split('=')
                    _dict[key] = value
    return _dict


def all_technology():
    Tech = "Technology"
    technology_list = [
        join(CONST.common, Tech, "military_technology.json"),
        join(CONST.common, Tech, "beyond_technology.json")
    ]

    Sword_Armor = join(CONST.common, Tech, "Sword_Armor")
    for file in listdir(Sword_Armor):
        technology_list.append(join(Sword_Armor, file))

    return technology_list


##########################################################################
class Resource:
    def __init__(self, name, need=None, rate=None, _max=50000):
        self.name = name
        self.need = need
        self.rate = rate
        self._max = _max

    def __repr__(self):
        return f"<Resource: {self.name}>"


def transform_resources(s_file, b_file):
    res = json_load(join(CONST.common, s_file))
    for k, v in res.items():
        if v is None:
            res[k] = Resource(k)
        else:
            res[k] = Resource(k, need=v.get('need'), rate=v.get('rate'))
    pkl_dump(res, join(CONST.models, b_file))


##########################################################################
class Technology:
    def __init__(self, name, cost, front, weight, no=None):
        self.name = name
        self.cost = cost
        self.front = front
        self.weight = weight
        self.no = None
        self.current = 0

    def finish(self):
        return self.current >= self.cost

    def __repr__(self):
        return f"<Technology: {self.name}, cost:{self.cost}>"

# transform military technology
def transform_military_technology(s_files, b_file, name_directory):
    name_directory = json_load(join(CONST.common, "Localisation/Technology", name_directory))
    result = dict()
    for s_file in s_files:
        res = json_load(s_file)
        for k, v in res.items():
            res[k] = Technology(name_directory[k]['name'], v.get('cost'), v.get('front'), v.get('weight'),
                                       v.get('no'))
        result.update(res)
    pkl_dump(result, join(CONST.models, b_file))


def main():
    # transform_resources("resources.json", "resource.pkl")
    transform_military_technology(all_technology(), "military_technology.pkl", "military.txt")
    pass


def test(file):
    res = pkl_load(join(CONST.models, file))
    for k, v in res.items():
        print(k, v.front, v.weight, v.cost, v.no)


if __name__ == '__main__':
    # main()
    # test("military_technology.pkl")
    for k, v in technology_localisation().items():
        print(f"{k} = {v}")
    pass
