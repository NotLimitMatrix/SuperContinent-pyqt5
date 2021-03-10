import zlib, json

from unit.block import Block
from unit.zoning import Zoning

JSONEncoder = json.JSONEncoder()
JSONDecoder = json.JSONDecoder()


def compress_string(s: str):
    return zlib.compress(s.encode('utf-8'))


def decompress_string(s):
    return zlib.decompress(s).decode('utf-8')


def compress_dict(s):
    return zlib.compress(zlib.compress(''.join(JSONEncoder.encode(s)).encode('utf-8')))


def decompress_dict(s):
    return JSONDecoder.decode(zlib.decompress(zlib.decompress(s)).decode('utf-8'))


if __name__ == '__main__':
    from pprint import pprint

    bl = [Block(i) for i in range(900)]
    zl = []
    for block in bl:
        z_start = len(zl)
        z_end = z_start + block.zoning_number ** 2

        block.insert_zoning_list(range(z_start, z_end))
        zl.extend(Zoning(i, block.id) for i in range(z_start, z_end))

    cs = {
        'block_list': Block.collect(bl),
        'zoning_list': Zoning.collect(zl)
    }

    print(len(compress_dict(cs))/1024)

    print(cs == decompress_dict(compress_dict(cs)))