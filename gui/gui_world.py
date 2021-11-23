from abc import ABC

from PyQt5.QtGui import QPainter

from reference.gui import COLOR, NUMBER
from reference.functions import row_col_to_ident, draw_text
from gui.gui_base import BaseGUI
from unit.block import Block


class WorldGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(WorldGUI, self).__init__(*args, **kwargs)
        self.n = NUMBER.WORLD_NUMBER
        self.size = self.width // NUMBER.WORLD_NUMBER
        self.world_list = self.init_world()

    def init_world(self):
        return [
            Block(row_col_to_ident(row, col, self.n), row, col, self.size)
            for row in range(self.n) for col in range(self.n)
        ]

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for block in self.world_list:
            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{block.row},{block.col}", painter)

    def update(self):
        pass
