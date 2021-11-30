from PyQt5.QtCore import QRect

from reference.templates import TEMPLATE_ZONING


class Zoning:
    def __init__(self, ident, row, col, size, block_id, player=None):
        self.ident = ident
        self.row = row
        self.col = col
        self.size = size
        self.block_id = block_id
        self.player = player

    def real_position(self, top, left):
        return QRect(self.size * self.col + left, self.size * self.row + top, self.size, self.size)

    def display(self):
        return TEMPLATE_ZONING.format(
            ident=self.ident,
            row=self.row,
            col=self.col,
            block_id=self.block_id,
            building='空闲'
        )
