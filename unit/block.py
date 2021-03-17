from random import choice

from trash.STATIC.CONST import BLOCK_STATUS, BLOCK_ZONING_NUMBER


class Block:
    def __init__(self, ident, belong=0):
        self.id = ident
        self.belong = belong

        self.status = choice(BLOCK_STATUS)

        self.zoning_number = choice(BLOCK_ZONING_NUMBER)
        self.zoning_set = ''

    def get_xy(self, dx):
        return divmod(self.id, dx)

    def insert_zoning(self, z_id):
        zs = self.zoning_set.split()
        zs.append(str(z_id))
        self.zoning_set = ' '.join(zs)

    def insert_zoning_list(self, z_list):
        # [1,2,3,4]
        self.zoning_set = ' '.join(str(i) for i in z_list)

    def dump(self):
        return {
            'status': self.status,
            'belong': self.belong,
            'zoning_number': self.zoning_number * self.zoning_number,
            'zoning_set': self.zoning_set
        }

    @staticmethod
    def collect(block_list):
        return {str(block.id): block.dump() for block in block_list}
