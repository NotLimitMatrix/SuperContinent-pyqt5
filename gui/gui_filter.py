from abc import ABC

from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import QRect

from reference.gui import COLOR, SIZE
from reference.game import OPTIONS
from reference.functions import draw_text, tr
from reference.templates import TEMPLATE_FILTER
from gui.gui_base import BaseGUI


class FilterUnitGUI(BaseGUI, ABC):
    def __init__(self, name, *args, **kwargs):
        super(FilterUnitGUI, self).__init__(*args, **kwargs)
        self.name = name

    def update(self):
        pass

    def draw(self, painter: QPainter):
        painter.setBrush(COLOR.WHITE)
        rect = QRect(self.left, self.top, self.width, self.height)
        painter.drawRect(rect)
        draw_text(rect, tr(self.name), painter)

    def display(self):
        return TEMPLATE_FILTER.format(
            filter_type=tr(self.name)
        )


class FilterGUI(BaseGUI, ABC):
    def __init__(self, *args, **kwargs):
        super(FilterGUI, self).__init__(*args, **kwargs)

        self.item_width = SIZE.FILTER_WIDTH // len(OPTIONS.FILTERS)
        self.filter_list = [
            FilterUnitGUI(item, top=self.top, left=self.left + index * self.item_width,
                          width=self.item_width, height=SIZE.FILTER_HEIGHT, parent=self.parent)
            for index, item in enumerate(OPTIONS.FILTERS)
        ]

    def update(self, *args, **kwargs):
        pass

    def draw(self, painter: QPainter):
        for component in self.filter_list:
            component.draw(painter)

    def mouse_choose_item(self, event: QMouseEvent):
        return self.filter_list[(event.pos().x() - self.left) // self.item_width]
