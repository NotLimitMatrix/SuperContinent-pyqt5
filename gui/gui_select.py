from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE, NUMBER
from reference.functions import draw_text
from reference.templates import TEMPLATE_SELECT_ITEM
from gui.gui_base import BaseGUI


class SelectItemGUI(BaseGUI, ABC):
    def __init__(self, ident, *args, **kwargs):
        super(SelectItemGUI, self).__init__(*args, **kwargs)
        self.ident = ident

    def draw(self, content, painter: QPainter):
        rect = QRect(self.left, self.top, self.width, self.height)
        painter.drawRect(rect)
        draw_text(rect, content, painter)

    def update(self, *args, **kwargs):
        pass

    def display(self):
        return TEMPLATE_SELECT_ITEM.format(
            ident=self.ident
        )


class SelectGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(SelectGUI, self).__init__(*args, **kwargs)
        self.options = [
            SelectItemGUI(ident=i, left=self.left, top=self.top + i * SIZE.SELECT_LINE_HEIGHT,
                          width=self.width, height=SIZE.SELECT_LINE_HEIGHT)
            for i in range(NUMBER.SELECT_OPTIONS)
        ]

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        for index, item in enumerate(self.options):
            item.draw(str(index), painter)

    def mouse_choose_item(self, event: QMouseEvent):
        index = (event.pos().y() - self.top) // SIZE.SELECT_LINE_HEIGHT
        if index >= len(self.options):
            index = -1

        return self.options[index]
