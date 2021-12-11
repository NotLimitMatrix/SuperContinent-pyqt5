from collections.abc import Iterable

from PyQt5.QtCore import QRect

from reference.templates import TEMPLATE_BLOCK
from reference.game import BLOCK, ZONING
from reference.functions import weight_choice, tr
from reference import dictionary


class Attribute:
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', 2)
        self.display = kwargs.get('display', False)
        self.can_move = kwargs.get('can_move', False)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Block:
    def __init__(self, ident, row, col, size, player=None):
        self.ident = ident
        self.row = row
        self.col = col
        self.size = size
        self.player = player

        self.attribute = Attribute(status=weight_choice(BLOCK.ENV_WEIGHT), display=False)

        self.z_num = ZONING.ZONING_NUMBER[weight_choice(ZONING.ZONING_WEIGHT)]
        self.z_set = list()

    def add_zoning(self, z):
        if isinstance(z, int):
            self.z_set.append(z)
        elif isinstance(z, Iterable):
            self.z_set.extend(z)
        else:
            raise ValueError("Block: Insert element must be int or iterable")

    def real_position(self, top, left):
        return QRect(self.size * self.col + left, self.size * self.row + top, self.size, self.size)

    def display(self):
        modifier = 100 * BLOCK.MODIFIER[self.attribute.status]
        if self.attribute.display:
            return TEMPLATE_BLOCK.format(
                player=tr(dictionary.NO_PYALER) if self.player is None else self.player.name,
                ident=self.ident,
                row=self.row,
                col=self.col,
                env_desc=BLOCK.WORD[self.attribute.status],
                env_modifier=modifier,
                product_modifier=modifier,
                upkeep_modifier=-modifier
            )
        else:
            return "该地块不可见"
