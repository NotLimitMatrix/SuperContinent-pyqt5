from abc import ABC

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from reference.gui import COLOR, SIZE
from gui.gui_base import BaseGUI

test_message = """
地块: 01
坐标: 1,2
环境: 恶劣
资源:
    食物: +2
    矿物: +4
    能量: -1
"""


class TextBrowserGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(TextBrowserGUI, self).__init__(*args, **kwargs)
        self.message = test_message

    def update(self, *args, **kwargs):
        pass

    def draw_component(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        painter.drawRect(self.left, self.top, self.width, self.height)

        painter.setPen(COLOR.BLACK)
        left = self.left + SIZE.DX * 2
        for index, text in enumerate(self.message.strip().split('\n')):
            top = self.top + index * SIZE.TEXT_LINE_HEIGHT
            painter.drawText(left, top, self.width, SIZE.TEXT_LINE_HEIGHT, Qt.AlignVCenter, str(text))
