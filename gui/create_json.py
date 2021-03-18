import json

from unit.block import Block
from unit.zoning import Zoning

from reference.const import WORLD_NUMBER

if __name__ == '__main__':
    bl = [Block(i) for i in range(WORLD_NUMBER ** 2)]
    zl = []
    for block in bl:
        z_start = len(zl)
        z_end = z_start + block.zoning_number ** 2

        block.insert_zoning_list(range(z_start, z_end))
        zl.extend(Zoning(i, block.id) for i in range(z_start, z_end))

    cs = {
        'block_number': len(bl),
        'zoning_number': len(zl),
        'block_list': Block.collect(bl),
        'zoning_list': Zoning.collect(zl)
    }

    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(cs, f)
