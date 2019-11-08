import json

from os.path import join
from os import listdir
import _pickle as cPickle


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


def all_military_technology():
    Tech = "Technology"
    technology_list = [
        join(CONST.common, Tech, "military_technology.json"),
    ]

    Sword_Armor = join(CONST.common, Tech, "Sword_Armor")
    for file in listdir(Sword_Armor):
        technology_list.append(join(Sword_Armor, file))

    return technology_list


##########################################################################
# transform Resources
class Resource:
    def __init__(self, need=None, rate=None, _max=50000):
        self.need = need
        self.rate = rate
        self._max = _max


def transform_resources(s_file, b_file):
    res = json_load(join(CONST.common, s_file))
    for k, v in res.items():
        if v is None:
            res[k] = Resource()
        else:
            res[k] = Resource(need=v['need'], rate=v['rate'])
    pkl_dump(res, join(CONST.models, b_file))


##########################################################################
class Technology:
    def __init__(self, cost, front, weight):
        self.cost = cost
        self.front = front
        self.weight = weight


# transform military technology
def transform_military_technology(s_files, b_file):
    result = dict()
    for s_file in s_files:
        res = json_load(s_file)
        for k, v in res.items():
            res[k] = Technology(v['cost'], v['front'], v['weight'])
        result.update(res)
    pkl_dump(result, join(CONST.models, b_file))


def main():
    # transform_resources("resources.json", "resource.pkl")
    transform_military_technology(all_military_technology(), "military_technology.pkl")
    pass


def test(file):
    res = pkl_load(join(CONST.models, file))
    for k,v in res.items():
        print(k, v.front, v.weight, v.cost)


if __name__ == '__main__':
    # main()
    # test("military_technology.pkl")
    pass
