from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE, NUMBER
from reference.functions import draw_text
from gui.gui_base import BaseGUI


class SelectGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(SelectGUI, self).__init__(*args, **kwargs)
        self.options = [
            QRect(self.left, self.top + i * SIZE.SELECT_LINE_HEIGHT, self.width, SIZE.SELECT_LINE_HEIGHT)
            for i in range(NUMBER.SELECT_OPTIONS)
        ]

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for index, rect in enumerate(self.options):
            painter.drawRect(rect)
            draw_text(rect, str(index), painter)
