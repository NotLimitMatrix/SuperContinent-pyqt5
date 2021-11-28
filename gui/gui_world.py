from abc import ABC

from PyQt5.QtGui import QPainter

from reference.gui import COLOR, NUMBER
from reference.functions import draw_text, ident_to_row_col
from gui.gui_base import BaseGUI
from unit.block import Block


class WorldGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(WorldGUI, self).__init__(*args, **kwargs)
        self.n = NUMBER.WORLD_NUMBER
        self.size = self.width // NUMBER.WORLD_NUMBER
        self.world_list = None

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for block in self.world_list:
            rect = block.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{block.row},{block.col}", painter)

    def update(self, data):
        self.world_list = [
            Block(i, *ident_to_row_col(i, self.n), self.size)
            for i in data
        ]
