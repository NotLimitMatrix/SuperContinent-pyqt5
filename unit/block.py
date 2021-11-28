from collections.abc import Iterable

from PyQt5.QtCore import QRect

from reference.templates import TEMPLATE_BLOCK
from reference.game import BLOCK


class Attribute:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', 0)
        self.display = kwargs.get('display', False)
        self.color = kwargs.get('color', )


class Block:
    def __init__(self, ident, row, col, size):
        self.ident = ident
        self.row = row
        self.col = col
        self.size = size

        self.attribute = Attribute()

        self.z_num = 1
        self.z_set = set()

    def init(self, **kwargs):
        self.attribute.status = kwargs.get('status', 0)
        self.z_num = kwargs.get('z_num', 1)

    def add_zoning(self, z):
        if isinstance(z, int):
            self.z_set.add(z)
        elif isinstance(z, Iterable):
            self.z_set.update(z)
        else:
            raise ValueError("Block: Insert element must be int or iterable")

    def real_position(self, top, left):
        return QRect(self.size * self.col + left, self.size * self.row + top, self.size, self.size)

    def __repr__(self):
        modifier = 100 * BLOCK.MODIFIER[self.attribute.status]
        return TEMPLATE_BLOCK.format(
            ident=self.ident,
            row=self.row,
            col=self.col,
            env_desc=BLOCK.WORD[self.attribute.status],
            env_modifier=modifier,
            product_modifier=modifier,
            upkeep_modifier=-modifier
        )
