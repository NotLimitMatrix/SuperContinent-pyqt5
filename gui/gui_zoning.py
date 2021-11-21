from abc import ABC

from PyQt5.QtGui import QPainter

from reference.gui import COLOR
from reference.functions import draw_text, row_col_to_ident
from gui.gui_base import BaseGUI
from unit.zoning import Zoning


class ZoningGUI(BaseGUI, ABC):
    def __init__(self, n, *args, **kwargs):
        super(ZoningGUI, self).__init__(*args, **kwargs)
        self.n = n
        self.size = self.width // n
        self.zoning_list = self.init_zoning()

    def init_zoning(self):
        return [
            Zoning(row_col_to_ident(row, col, self.n), row, col, self.size)
            for row in range(self.n) for col in range(self.n)
        ]

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for zoning in self.zoning_list:
            rect = zoning.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{zoning.row},{zoning.col}", painter)

    def update(self):
        pass
