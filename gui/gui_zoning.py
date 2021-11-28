from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent

from reference.gui import COLOR, NUMBER
from reference.functions import draw_text, ident_to_row_col
from gui.gui_base import BaseGUI
from unit.zoning import Zoning


class ZoningGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(ZoningGUI, self).__init__(*args, **kwargs)
        self.n = NUMBER.ZONING_NUMBER
        self.size = self.width // NUMBER.ZONING_NUMBER
        self.zoning_list = None

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for zoning in self.zoning_list:
            rect = zoning.real_position(self.top, self.left)
            painter.drawRect(rect)
            draw_text(rect, f"{zoning.row},{zoning.col}", painter)

    def update(self, data):
        self.zoning_list = [
            Zoning(i, *ident_to_row_col(i, self.n), self.size)
            for i in data
        ]
