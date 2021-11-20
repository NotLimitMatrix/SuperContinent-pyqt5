from abc import ABC

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter

from reference.gui import SIZE, POSITION, COLOR
from reference.functions import row_col_to_ident, draw_text
from gui.gui_base import BaseGUI


class Block:
    def __init__(self, ident, row, col, size):
        self.ident = ident
        self.row = row
        self.col = col
        self.size = size

    def real_position(self, top, left):
        return QRect(self.size * self.col + top, self.size * self.row + left, self.size, self.size)


class WorldGUI(BaseGUI, ABC):
    def __init__(self, n, *args, **kwargs):
        super(WorldGUI, self).__init__(*args, **kwargs)
        self.n = n
        self.size = self.width // self.n
        self.world_list = self.init_world(n)

    def init_world(self, number):
        return [
            Block(row_col_to_ident(row, col, number), row, col, self.size)
            for row in range(number) for col in range(number)
        ]

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for block in self.world_list:
            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{block.row},{block.col}", painter)

    def update(self):
        pass
