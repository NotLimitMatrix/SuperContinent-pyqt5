from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from reference.gui import COLOR, SIZE
from gui.gui_base import BaseGUI


class TextBrowserGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(TextBrowserGUI, self).__init__(*args, **kwargs)

    def update(self, msg):
        self.message = msg

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        painter.drawRect(self.left, self.top, self.width, self.height)

        painter.setPen(COLOR.BLACK)
        left = self.left + SIZE.DX * 2
        for index, text in enumerate(self.message.strip().split('\n')):
            top = self.top + index * SIZE.TEXT_LINE_HEIGHT
            painter.drawText(left, top, self.width, SIZE.TEXT_LINE_HEIGHT, Qt.AlignVCenter, str(text))
