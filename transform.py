import json

import _pickle as cPickle

Sources = "./Common/Sources"
Binary = "./Common/Binary"


def join(*args):
    return '/'.join(args)


def json_load(file):
    with open(file, 'r', encoding='utf-8') as r:
        return json.load(r)


def pkl_load(file):
    with open(file, 'rb') as bin:
        return cPickle.load(bin)


def pkl_dump(data, file):
    with open(file, 'wb') as bin:
        cPickle.dump(data, bin)


class Resource:
    def __init__(self, need=None, rate=None, _max=50000):
        self.need = need
        self.rate = rate
        self._max = _max


def transform_resources(s_file="resources.json", b_file="resource.pkl"):
    res = json_load(join(Sources, s_file))
    for k, v in res.items():
        if v is None:
            res[k] = Resource()
        else:
            res[k] = Resource(need=v['need'], rate=v['rate'])
    pkl_dump(res, join(Binary, b_file))


if __name__ == '__main__':
    #transform_resources()
    res = pkl_load(join(Binary, 'resource.pkl'))
    print([k for k in res])
